from django.core.mail import send_mail
from django.urls.base import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.forms import PostForm
from blog.models import Post

from fishgramm.settings import EMAIL_HOST_USER


# Create your views here.
class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)



class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object =super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        if self.object.views_counter == 100:
            subject = "Поздравляем"
            message = "Поздравляем вас с первой сотней просмотров"
            from_email = EMAIL_HOST_USER
            to_email = EMAIL_HOST_USER
            send_mail(
                subject,
                message,
                from_email,
                [to_email],
                fail_silently=False)
        return self.object


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy("blog:post_list")

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")


