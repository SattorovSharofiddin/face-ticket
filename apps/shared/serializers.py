# from rest_framework.exceptions import ValidationError
# from rest_framework.serializers import ModelSerializer, Serializer
#
#
# class DynamicFieldsModelSerializer(ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         fields = kwargs.pop('fields', None)
#
#         super().__init__(*args, **kwargs)
#
#         if fields:
#             allowed = set(fields)
#             existed = set(self.fields)
#             for field_name in existed - allowed:
#                 self.fields.pop(field_name)
#
#
# class ListSerializer(Serializer):
#     def is_valid(self, *, raise_exception=False):
#         if not isinstance(self.initial_data, list):
#             raise ValidationError('data should be list!')
#         assert hasattr(self, 'initial_data'), (
#             'Cannot call `.is_valid()` as no `data=` keyword argument was '
#             'passed when instantiating the serializer instance.'
#         )
#
#         if not hasattr(self, '_validated_data'):
#             self._validated_data = []
#             for item in self.initial_data:
#                 try:
#                     self._validated_data.append(self.run_validation(item))
#                 except ValidationError as exc:
#                     self._validated_data = []
#                     self._errors = exc.detail
#                 else:
#                     self._errors = {}
#
#             if self._errors and raise_exception:
#                 raise ValidationError(self.errors)
#
#         return not bool(self._errors)
#
#     @property
#     def data(self):
#         if hasattr(self, 'initial_data') and not hasattr(self, '_validated_data'):
#             msg = (
#                 'When a serializer is passed a `data` keyword argument you '
#                 'must call `.is_valid()` before attempting to access the '
#                 'serialized `.data` representation.\n'
#                 'You should either call `.is_valid()` first, '
#                 'or access `.initial_data` instead.'
#             )
#             raise AssertionError(msg)
#
#         if not hasattr(self, '_data'):
#             self._data = []
#             for instance in self.instances:
#                 if instance is not None and not getattr(self, '_errors', None):
#                     self._data.append(self.to_representation(instance))
#                 elif hasattr(self, '_validated_data') and not getattr(self, '_errors', None):
#                     self._data.append(self.to_representation(self.validated_data))
#                 else:
#                     self._data.append(self.get_initial())
#         return self._data
