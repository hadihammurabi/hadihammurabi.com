from django.db import models
from django.shortcuts import render

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

class BlogPage(Page):
  description = models.CharField(max_length=255, blank=True, null=True)

  subpage_types = ['blog.PostPage']

  content_panels = Page.content_panels + [
    FieldPanel('description', classname="full"),
  ]

  def get_context(self, request):
    context = super().get_context(request)
    context['posts'] = PostPage.objects.child_of(self).live()
    return context

  def render(self, request):
    return render(request, 'blog/blog_page.html', self.get_context(request))

class PostPage(Page):
  description = models.CharField(max_length=255, blank=True, null=True)
  body = RichTextField()
  feed_image = models.ForeignKey(
    'wagtailimages.Image',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='+'
  )

  search_fields = Page.search_fields + [
    index.SearchField('body'),
    index.SearchField('description'),
  ]

  content_panels = Page.content_panels + [
    FieldPanel('description', classname="full"),
    FieldPanel('body', classname="full"),
    InlinePanel('related_links', label="Related links"),
  ]

  promote_panels = [
    MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    ImageChooserPanel('feed_image'),
  ]

  parent_page_types = ['blog.BlogPage']
  subpage_types = []

class PostPageRelatedLink(Orderable):
  page = ParentalKey(PostPage, on_delete=models.CASCADE, related_name='related_links')
  name = models.CharField(max_length=255)
  url = models.URLField()

  panels = [
    FieldPanel('name'),
    FieldPanel('url'),
  ]
