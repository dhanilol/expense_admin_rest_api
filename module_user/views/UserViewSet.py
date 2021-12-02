from rest_framework import viewsets, mixins
from module_user.models.User import User
from module_user.serializers.UserSerializer import UserSerializer

# class UserFilter(ModelFilterSet):
#     class Meta:
#         model = User


class UserViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # TODO: Add authentication_classes
    # TODO: Add permissions_classes
    # TODO: Add pagination_class
    # TODO: Add filter_backends
    ordering = '-id'
    # filter_class = UserFilter

    # Exclude from Public Documentation
    # exclude_from_documentation = True
    # schema = None

    def get_queryset(self):
        # return users only for authorized users (admins)
        return self.queryset


