from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import PageNotAnInteger,Paginator
from .models import CourseOrg,CityDict,Teacher
from .forms import UserAskForm
from django.http import  HttpResponse
from operation.models import UserFavorite
from django.contrib import auth
# Create your views here.

class OrgView(View):

    # 课程列表
    def get(self,request):
        all_orgs= CourseOrg.objects.all()
        all_citys = CityDict.objects.all()
        org_nums = all_orgs.count()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]

        city_id= request.GET.get('city','')

        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        sort = request.GET.get('sort', '')
        if  sort:
            if sort=='students':
                all_orgs = all_orgs.order_by("-students")
            elif sort=='courses':
                all_orgs =all_orgs.order_by('-course_nums')

        category = request.GET.get('ct','')
        if category:
            all_orgs=all_orgs.filter(category=category)
        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page=1
        p=Paginator(all_orgs,5,request=request)
        orgs=p.page(page)

        return render(request,'org-list.html',{
            'all_orgs':orgs,
            'all_citys':all_citys,
            'org_nums':org_nums,
            'city_id':city_id,
            'category':category,
            'hot_orgs':hot_orgs,
            'sort':sort,
        })
    def post(self):
        pass


class AddUserAskView(View):

    def post(self,request):
        userask_form= UserAskForm(request.POST)
        if userask_form.is_valid():
            user_ask= userask_form.save(commit=True)
            return HttpResponse('{"status":"success"}',content_type='application/json') # ajsz 提交数据时，最外为单引号，内部为双引号
        else:
            return  HttpResponse('{"status":"fail","msg":"添加出错"}',content_type='application/json')


class OrgHomeView(View):
    """
    机构首页
    """
    def get(self,request,org_id):
        """

        :param request:
        :param org_id:
        :return:
        """
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses= course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        return render(request,'org-detail-homepage.html',{
            'all_courses':all_courses,
            'all_teachers':all_teachers,
            'course_org':course_org,
            'current_page':current_page,
        })

class OrgCourseView(View):
    """
    机构课程
    """
    def get(self,request,org_id):
        """

        :param request:
        :param org_id:
        :return:
        """
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_courses= course_org.course_set.all()

        return render(request,'org-detail-course.html',{
            'all_courses':all_courses,
            'current_page':current_page,
            'course_org':course_org,
        })

class OrgDescView(View):
    """
    机构介绍
    """
    def get(self,request,org_id):
        """

        :param request:
        :param org_id:
        :return:
        """
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=int(org_id))

        return render(request,'org-detail-desc.html',{
            'current_page':current_page,
            'course_org':course_org,
        })

class OrgTeachersView(View):
    """
    机构老师
    """
    def get(self,request,org_id):
        """

        :param request:
        :param org_id:
        :return:
        """
        current_page = 'teachers'
        course_org = CourseOrg.objects.get(id=int(org_id))
        all_teachers = course_org.teacher_set.all()
        return render(request,'org-detail-teachers.html',{
            'all_teachers':all_teachers,
            'current_page':current_page,
            'course_org': course_org,
        })

class AddFavView(View):

    def post(self,request):
        fav_id = request.POST.get('fav_id',0)
        fav_type = request.POST.get('fav_type',0)

        if not request.user.is_authenticated:
            return HttpResponse('{"status":"fail","msg":"用户未登录"}',content_type='application/json')

        exit_records= UserFavorite.objects.filter(user=request.user,fav_id=int(fav_id),fav_type=int(fav_type))

        if exit_records:
            exit_records.delete()
            return HttpResponse('{"status":"success","msg":"收藏"}', content_type='application/json')
        else:
            user_fav= UserFavorite()
            if int(fav_id)>0 and int(fav_type)>0:
                user_fav.user= request.user
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type= int(fav_type)
                user_fav.save()
                return HttpResponse('{"status":"success","msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail","msg":"收藏出错"}', content_type='application/json')


