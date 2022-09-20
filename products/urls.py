from rest_framework import routers
from products.api import ProductViewSet

router = routers.DefaultRouter()

router.register("api/products", ProductViewSet, "products")

urlpatterns = router.urls
