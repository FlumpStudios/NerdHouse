from django.db import models
from django.db import models
import os
import sys
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from modelcluster.fields import ParentalKey


class galleryOrderable(Orderable, models.Model):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='galleryOrderable')
    gallery = models.ForeignKey('gallery', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "gallery item"
        verbose_name_plural = "gallery items"

    panels = [
        SnippetChooserPanel('gallery'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name

@register_snippet
class gallery(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    link = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=10)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('link'),
        FieldPanel('name'),
        FieldPanel('description')
    ]

    def __str__(self):
        return self.name

class HomePage(Page):
    #DATABASE FIELDS
    intro_header = models.CharField(max_length=50,default="Welcome to our website!")
    
    intro_text = RichTextField(blank=True)
    intro_continue_button_text = models.CharField(max_length=50, default='Continue')        
    
    client_firstname = models.CharField(max_length=50, default="Joe")    
    client_surname = models.CharField(max_length=50, default="Blogs")    
    client_organisationName = models.CharField(max_length=50, default="Nerdhouse", null=True)
    
    blurb_header_1 = models.CharField(max_length=50, default="My Blurb")    
    blurb_header_2 = models.CharField(max_length=50, default="My Blurb 2")
    blurb_text = RichTextField(blank=True)

    about_us_header = models.CharField(max_length=50, default="About Us")    
    about_us_sub_header = models.CharField(max_length=50, default="stuff about us")
    about_us_text = RichTextField(blank=True)
    about_us_button_text = models.CharField(max_length=50, default="Learn More")    
    about_us_button_link = models.CharField(max_length=50, default="#")    

    image_gallery_title = models.CharField(max_length=50, default="Gallery")  
    image_gallery_text = RichTextField(blank=True)
    
    
    intro_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    blurb_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    


    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('client_firstname'),
                FieldPanel('client_surname'),
                FieldPanel('client_organisationName'),         
            ],
            heading="Client Information",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('intro_header'),
                FieldPanel('intro_text'),
                FieldPanel('intro_continue_button_text'),
                ImageChooserPanel('intro_background')
            ],
            heading="Introduction",  
        ),
    ]
    
    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('blurb_header_1'),
                FieldPanel('blurb_header_2'),
                FieldPanel('blurb_text'),
                ImageChooserPanel('blurb_background')
            ],
            heading="Blurb",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('about_us_header'),
                FieldPanel('about_us_sub_header'),
                FieldPanel('about_us_text'),
                FieldPanel('about_us_button_text'),
                FieldPanel('about_us_button_link'),
                ImageChooserPanel('blurb_background')
            ],
            heading="About Us",  
        ),
    ] 
    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('image_gallery_title'),
                FieldPanel('image_gallery_text'),                
                InlinePanel('galleryOrderable', label="Gallery")
            ],
            heading="Gallery",  
        ),
    ]

    

    # promote_panels = [
    #     MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    #     ImageChooserPanel('intro_background'),
    #     ]  


