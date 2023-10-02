from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from .models import Post


class LatestBlogs(Feed):
    title = "Code and Explore"
    link = reverse_lazy('frontpage')
    description = "Updates on new blogs."

    def items(self):
        return Post.posts.all()[0:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.intro, 20)

    def item_link(self, item):
        return reverse_lazy('detail', args=[item.category.slug, item.slug])
