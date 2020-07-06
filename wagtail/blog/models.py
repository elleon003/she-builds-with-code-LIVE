from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogListingPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["blog.BlogPost"]
    max_count = 1

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        posts = BlogPost.objects.live().order_by('-first_published_at')

        context["posts"] = posts
        return context


class BlogPost(Page):
    parent_page_types = ["blog.BlogListingPage"]
    subpage_types = []

    subtitle = models.CharField(
        max_length = 140,
        blank=False,
        null=True,
    )
    post_date = models.DateField("Post Date")
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text='Home page image'
    )
    # @TODO Streamfield for the following
    # body
    # body_images
    # category

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('post_date'),
        ImageChooserPanel('featured_image'),
    ]
    