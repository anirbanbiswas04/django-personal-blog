from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from core.views import frontpage, about, robots_txt
from blog.views import category, detail, search
from blog.feed import LatestBlogs
from .sitemaps import CategorySitemap, PostSitemap

sitemaps = {'category': CategorySitemap, 'post': PostSitemap}

urlpatterns = [
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
                  path('robots.txt', robots_txt, name='robots_txt'),
                  path('admin/', admin.site.urls),
                  path('', frontpage, name="frontpage"),
                  path('about/', about, name="about"),
                  path('search/', search, name='search'),
                  path('rss-feed/', LatestBlogs(), name='rss_feed'),
                  path('<slug:slug>/', category, name="category_detail"),
                  path('<slug:category_slug>/<slug:slug>/', detail, name="detail"),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Code and Explore Admin Panel'
admin.site.index_title = 'Manage The Content'
