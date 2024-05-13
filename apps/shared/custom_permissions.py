# from rest_framework.request import Request
# from rest_framework.permissions import BasePermission
#
#
# class BaseRolePermission(BasePermission):
#     role = None
#
#     def has_permission(self, request: Request, view):
#         return request.users.is_authenticated and request.users.status == self.role
#
#     def has_object_permission(self, request, view, obj):
#         return request.users.is_authenticated and request.users.status == self.role
