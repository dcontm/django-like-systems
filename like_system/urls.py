from django.urls import path
from . import views
from . conf import LIKES_OBJS
from . models import LikeSystem


urlpatterns = [path(f'{i.__name__.lower()}/<pk>/like/',
               views.LikeSystemView.as_view(model=i,
                                            action_type=LikeSystem.LIKE))
               for i in LIKES_OBJS]

urlpatterns += [path(f'{i.__name__.lower()}/<pk>/dislike/',
                views.LikeSystemView.as_view(model=i,
                                             action_type=LikeSystem.DISLIKE))
                for i in LIKES_OBJS]
