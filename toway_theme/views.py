from calendar import month_name

from django.http import Http404
from django.shortcuts import get_object_or_404

from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.blog.feeds import PostsRSS, PostsAtom
from mezzanine.conf import settings
from mezzanine.generic.models import Keyword
from mezzanine.utils.views import render, paginate
from mezzanine.utils.models import get_user_model

from social_auth import __version__ as version

User = get_user_model()


'''def show_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return render_to_response('logins.html', {'version': version},
                                  RequestContext(request))'''



def blog_post_home(request, template="blog/blog_post_list.html"):
    settings.use_editable()
    templates = []
    category = BlogCategory.objects.get(slug='ads')
    blog_posts = BlogPost.objects.published(for_user=request.user)
    ads_posts = None

    if category:
        blog_posts = blog_posts.exclude(categories=category)
        ads_posts = BlogPost.objects.published(for_user=request.user)
        ads_posts = ads_posts.filter(categories=category)

    blog_posts = paginate(blog_posts, request.GET.get("page", 1),
                          settings.BLOG_POST_PER_PAGE,
                          settings.MAX_PAGING_LINKS)
    
    context = {"blog_posts": blog_posts, "ads_posts":ads_posts,
               "year": None, "month": None, "tag": None, "category": None, "author": None}

    templates.append(template)
    return render(request, templates, context)
