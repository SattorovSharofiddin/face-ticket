# from rest_framework.request import Request
# from rest_framework.permissions import BasePermission
#
#
# class BaseRolePermission(BasePermission):
#     role = None
#
#     def has_permission(self, request: Request, view):
#         return request.user.is_authenticated and request.user.status == self.role
#
#     def has_object_permission(self, request, view, obj):
#         return request.user.is_authenticated and request.user.status == self.role
