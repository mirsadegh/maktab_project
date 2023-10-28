from django import template
from blog.models import Post, Category

register = template.Library()



@register.simple_tag(name='totalPosts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

    
def snippet(value,args=20):
    return value[:100] + "..."    

@register.inclusion_tag('blog/blog-popular-posts.html')
def latestPosts(arg=3):
    posts = Post.objects.filter(status=1).order_by("-published_date")[:arg]
    return {'posts':posts }    
    
    
@register.inclusion_tag('blog/blog-post-categories.html')  
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    print(categories)
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count() 
    return { 'categories':cat_dict }     
     
      

    
    
    
    