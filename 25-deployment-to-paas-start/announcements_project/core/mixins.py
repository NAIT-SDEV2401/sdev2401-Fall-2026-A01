from django.contrib.auth.mixins import UserPassesTestMixin

class IsTeacherRoleMixin(UserPassesTestMixin):
    '''
    Mixin to check if the user has a teacher role. This can be used in any view that requires the user to be a teacher.
    '''

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.role == 'teacher'