from django.contrib.auth.mixins import LoginRequiredMixin


class MyMixin(object):
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, s):
        return s.upper()

# class MyView(LoginRequiredMixin, View):
