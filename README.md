# django-like-system


An easy way to add feedback "like/dislike"  to any of your models.

# Requirements


+ Django 2.2+
+ jQuery

## Installation


    pip install django-like-system

## Usage


+ Add 'django-like-system' to your INSTALLED_APPS:
    
      INSTALLED_APPS = (
      ...
      'django-like-system',
      ...
      )

+ You must add LIKES_OBJS_DICT dictionary to your settings.py file. The keys in this dictionary - are the path to your model, value - list with class name:

      LIKES_OBJS_DICT = {'example.models': ['Test', 'Test2'],
                         'example1.models': ['Test3']}

+ Your models to which you want to attach as feedback 'like/dislike'
  should inherit class LikesTarget:

      from like_system.models import LikesTarget

      # Create your models here.

      class Test(LikesTarget):
          headline = models.CharField(max_length=500)

      class Test1(LikesTarget):
        headline1 = models.CharField(max_length=500)

+ Add jQuery and app.js in your html template:

      <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
      <script src="{% static 'like_system.js' %}"></script>

+ Your buttons like and dislike should have class css class 'like' and 'dislike'.
 Like and dislike counters should have class 'likecount' and 'dislikecount'.
For live mapping, wrap the entire construction in a div
with css class 'likesystem':

      {% for obj in my_list %}
      <div class='likesystem'>
        <p>{{obj.headline}}-{{obj.likesystem.total}}</p>
        <span class='likes' data-id={{obj.id}} data-type='test'>like</span>
        <span class='countlikes'>{{obj.likesystem.likes.count}}</span>      
        <span class='dislikes' data-id={{obj.id}} data-type='test'>dislike</span>
        <span class='countdislikes'>{{obj.likesystem.dislikes.count}}</span>
      </div>
      {% endfor%}