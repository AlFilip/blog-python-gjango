
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from news.forms import NewsForm
from news.models import News, Category
from .utils import MyMixin


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'home'
    context_object_name = 'news'
    mixin_prop = 'hello world!'
    # extra_context = {'title': 'Главная'}
    #
    # queryset = News.objects.select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Главная страница')
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
#     news = News.objects.filter(is_published=True)
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context)
class NewsByCategory(ListView):
    model = News
    template_name = 'home'
    context_object_name = 'news'
    extra_context = {'title': 'Новости'}
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(id=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True).select_related('category')


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id, is_published=True)
#     category = Category.objects.get(id=category_id)
#     context = {
#         'news': news,
#         'category': category,
#     }
#     return render(request, 'news/category.html', context)

class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'


# def view_news(request, news_id):
#     # news_item = News.objects.get(news_id)
#     news_item = get_object_or_404(News, id=news_id)
#     context = {'news_item': news_item}
#     return render(request, 'news/view_news.html', context)


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'



# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(data=request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     context = {'form': form}
#     return render(request, 'news/add_news.html', context)


