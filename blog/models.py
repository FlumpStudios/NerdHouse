from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from django.db import models

# New imports added for ParentalKey, Orderable, InlinePanel, ImageChooserPanel

from modelcluster.fields import ParentalKey


class BlogIndexPage(Page):
    subpage_types = ['BlogPage']
    intro = RichTextField(blank=True)
    
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

class BlogPage(Page):
    subpage_types = ['BlogPage']
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    author = models.CharField(max_length=50, default="Joe Blogs")
    body = RichTextField(blank=True)
    caption = models.CharField(blank=True, max_length=250)
    main_image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=True,
        on_delete=models.SET_NULL, 
        related_name='+'
    )
   

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('author'),
        FieldPanel('body', classname="full"),
        ImageChooserPanel('main_image'),
        FieldPanel('caption')
    ]

