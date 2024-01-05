from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     # path('products/', views.product_list),
#     path('products/', views.ProductList.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
#     path('collections/', views.CollectionList.as_view()),
#     path(
#         'collections/<int:pk>/',
#         views.CollectionDetail.as_view(),
#         name='collection-detail'
#     ),
# ]
