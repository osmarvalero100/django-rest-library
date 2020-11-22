from api.viewsets import BookViewset, AuthorViewset, EditorialViewset, UserViewsets
from rest_framework import routers


router = routers.DefaultRouter()
router.register('authors', AuthorViewset)
router.register('books', BookViewset)
router.register('editorials', EditorialViewset)
router.register('users', UserViewsets)
