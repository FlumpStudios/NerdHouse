from django.db import models
import os
import sys
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel,FieldRowPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index
from modelcluster.fields import ParentalKey
from blog.models import BlogIndexPage 
from blog.models import BlogPage 
import feedparser


class carouselOrderable(Orderable, models.Model):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='carouselOrderable')
    
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    class Meta:
        verbose_name = "carousel item"
        verbose_name_plural = "carousel items"

    panels = [
         ImageChooserPanel('image')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name


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


class enumeratedListOrderable(Orderable, models.Model):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='enumeratedListOrderable')
    enumeratedList = models.ForeignKey('enumeratedList', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Enumerated List item"
        verbose_name_plural = "Enumerated List items"

    panels = [
        SnippetChooserPanel('enumeratedList'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name

class iconListOrderable(Orderable, models.Model):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='iconListOrderable')
    iconItem = models.ForeignKey('iconItem', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Icon List item"
        verbose_name_plural = "Icon List items"

    panels = [
        SnippetChooserPanel('iconItem'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name

class testimonialOrderable(Orderable, models.Model):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='testimonialOrderable')
    testimonialItem = models.ForeignKey('testimonialItem', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Testimonial List item"
        verbose_name_plural = "Testimonial List items"

    panels = [
        SnippetChooserPanel('testimonialItem'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.gallery.name

class socialMediaOrderable(Orderable, models.Model):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='socialMediaOrderable')
    socialMediaItem = models.ForeignKey('socialMediaItem', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "Social Media item"
        verbose_name_plural = "Social Media items"

    panels = [
        SnippetChooserPanel('socialMediaItem'),
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
    
    name = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)    
    description = models.CharField(max_length=50)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('link'),
        FieldPanel('name'),
        FieldPanel('description')
    ]

    def __str__(self):
        return self.name


@register_snippet
class socialMediaItem(models.Model):
    name = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)    
    icon = models.CharField(max_length=50)

    panels = [
        FieldPanel('link'),
        FieldPanel('name'),
        FieldPanel('icon')
    ]

    def __str__(self):
        return self.name


@register_snippet
class enumeratedList(models.Model):    
    title = models.CharField(max_length=50)
    text = RichTextField(blank=True)    

    panels = [
        FieldPanel('title'),
        FieldPanel('text')        
    ]

    def __str__(self):
        return self.title


@register_snippet
class iconItem(models.Model):    
    title = models.CharField(max_length=50)        
    icon = models.CharField(max_length=50)
    text = RichTextField(blank=True)        
    linkText = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('title'),
        FieldPanel('icon'),
        FieldPanel('text'),
        FieldPanel('linkText'),                
        FieldPanel('link')
    ]

    def __str__(self):
        return self.title

@register_snippet
class testimonialItem(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    author = models.CharField(max_length=50)
    testimonial = RichTextField(blank=True)
    
    panels = [
        FieldPanel('author'),
        FieldPanel('testimonial')
    ]

    def __str__(self):
        return self.author

class HomePage(Page):
    subpage_types = ['blog.BlogIndexPage']

    def has_address(self):
        return self.client_organisationName or self.client_addressLine1 or self.client_addressLine2 or self.client_town or self.client_county or self.client_postcode

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blog_index_page = BlogIndexPage.objects.first()
        blog_pages = BlogPage.objects.child_of(blog_index_page) if blog_index_page else []
        medium_blogs = feedparser.parse(str("https://medium.com/feed/" + self.medium_username) if self.medium_username else "" )
        videoFormatIsVimeo = str(self.intro_youtube_id).isdigit()
        context['blogpages'] = blog_pages
        context['medium_blogs'] = medium_blogs.entries[:self.medium_blog_display_limit]
        context['has_address'] = self.has_address()
        context['videoFormatIsVimeo'] = videoFormatIsVimeo
        return context      

    #DATABASE FIELDS
    intro_header = models.CharField(max_length=50,default="Welcome to our website!")    
    intro_text = RichTextField(blank=True)
    intro_continue_button_text = models.CharField(max_length=50, default='Continue', blank=True)    
    intro_youtube_id = models.CharField(max_length=50, blank=True, default="")
    video_background_brightness = models.DecimalField(default=1, max_digits=3, decimal_places=2)
    
    client_firstname = models.CharField(max_length=50, default="Joe", blank=True)    
    client_surname = models.CharField(max_length=50, default="Blogs", blank=True)    
    client_organisationName = models.CharField(max_length=50, default="My Company", blank=True)
    client_addressLine1 = models.CharField(max_length=50, default="Line 1",  blank=True)
    client_addressLine2 = models.CharField(max_length=50, default="Line 2",  blank=True)
    client_town = models.CharField(max_length=50, default="Town",  blank=True)
    client_county = models.CharField(max_length=50, default="County",  blank=True)
    client_country = models.CharField(max_length=50, default="Country",  blank=True)
    client_postcode = models.CharField(max_length=50, default="XX00 0XX ",  blank=True)
    client_email = models.CharField(max_length=50, default="joe@bloggs.com" )
    client_phone = models.CharField(max_length=50, default="01234 456789",  blank=True)
    client_moblie = models.CharField(max_length=50, default="01234 456789",  blank=True)    
    
    blurb_header = models.CharField(max_length=50, default="Blurb", blank=True)    
    blurb_subheader = models.CharField(max_length=50, default="this is a blurb", blank=True)
    blurb_text = RichTextField(blank=True)            
    show_blurb = models.BooleanField(default=True)
    show_blurb_in_navigation = models.BooleanField(default=False)

    image_gallery_title = models.CharField(max_length=50, default="Gallery")  
    image_gallery_text = RichTextField(blank=True)
    show_gallery_in_navigation = models.BooleanField(default=True)

    second_blurb_header = models.CharField(max_length=50, default="Blurb 2", blank=True)    
    second_blurb_subheader = models.CharField(max_length=50, default="My Second Blurb 2", blank=True)
    second_blurb_text = RichTextField(blank=True)
    second_blurb_buttonText = models.CharField(max_length=50, default="Find out more", blank=True)
    second_blurb_link = models.URLField(blank=True, default="#")
    show_second_blurb = models.BooleanField(default=True)
    show_second_blurb_in_navigation = models.BooleanField(default=False)
 
    enumerated_list_header = models.CharField(max_length=50, default="Approach", blank=True)
    show_enumerated_list_in_navigation = models.BooleanField(default=True)    

    icon_list_header = models.CharField(max_length=50, default="Services", blank=True)    
    show_icon_list_in_navigation = models.BooleanField(default=True)

    testimonials_header = models.CharField(max_length=50, default="Testimonials", blank=True)
    show_testimonials_in_navigation = models.BooleanField(default=False) 

    contact_title = models.CharField(max_length=50, default="Contact", blank=True)        
    contact_subtitle = models.CharField(max_length=50, default="Get in contact", blank=True)    
    show_contact_form = models.BooleanField(default=True)
    show_contact_in_navigation = models.BooleanField(default=True)

    footer_info_title = models.CharField(max_length=50, default="About", blank=True) 
    footer_info = RichTextField(blank=True)   

    primary_colour = models.CharField(max_length=50, default="#f37e77")
    secondary_colour = models.CharField(max_length=50, default="#ffffff")
    
    blog_title = models.CharField(max_length=50, default="Blogs", blank=True)    
    medium_username = models.CharField(max_length=50, null=True, blank=True)
    medium_blog_display_limit = models.IntegerField(blank=True, default=6)
    

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
    
    logo = models.ForeignKey(
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
                FieldPanel('client_addressLine1'),  
                FieldPanel('client_addressLine2'),  
                FieldPanel('client_town'),  
                FieldPanel('client_county'),  
                FieldPanel('client_country'),  
                FieldPanel('client_postcode'),  
                FieldPanel('client_email'),          
                FieldPanel('client_phone'),
                FieldPanel('client_moblie'),
                InlinePanel('socialMediaOrderable', label="Social Media Item")

            ],
            heading="Personal Information",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('primary_colour'),
                ImageChooserPanel('logo')
            ],
            heading="Presentation",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('intro_header'),
                FieldPanel('intro_text'),
                FieldPanel('intro_continue_button_text'),
                ImageChooserPanel('intro_background'),
                FieldPanel('intro_youtube_id'),
                FieldPanel('video_background_brightness')
            ],
            heading="Introduction",  
        ),
    ]
    
    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('blurb_header'),
                FieldPanel('blurb_subheader'),
                FieldPanel('blurb_text'),
                ImageChooserPanel('blurb_background'),
                FieldPanel('show_blurb'),
                FieldPanel('show_blurb_in_navigation')
            ],
            heading="Blurb",  
        ),
    ]    

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('image_gallery_title'),
                FieldPanel('image_gallery_text'),                
                InlinePanel('galleryOrderable', label="Gallery Item"),
                FieldPanel('show_gallery_in_navigation')
            ],
            heading="Gallery",  
        ),
    ]   

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('second_blurb_header'),
                FieldPanel('second_blurb_subheader'),
                FieldPanel('second_blurb_text'),
                InlinePanel('carouselOrderable', label="Carousel Image"),
                FieldPanel('second_blurb_buttonText'),
                FieldPanel('second_blurb_link'),
                FieldPanel('show_second_blurb'),
                FieldPanel('show_second_blurb_in_navigation')
            ],
            heading="Second Blurb",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('enumerated_list_header'),                
                InlinePanel('enumeratedListOrderable', label="Enumerated List Item"),
                FieldPanel('show_enumerated_list_in_navigation')
            ],
            heading="Enumerated List",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('icon_list_header'),                
                InlinePanel('iconListOrderable', label="Icon List Item"),
                FieldPanel('show_icon_list_in_navigation')
            ],
            heading="Icon List",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('testimonials_header'),                
                InlinePanel('testimonialOrderable', label="Testimonial Item"),
                FieldPanel('show_testimonials_in_navigation')
            ],
            heading="Icon List",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('blog_title'),                                
                FieldPanel('medium_username'),   
                FieldPanel('medium_blog_display_limit')
            ],
            heading="Blog",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('contact_title'),                
                FieldPanel('contact_subtitle'),
                FieldPanel('show_contact_form'),
                FieldPanel('show_contact_in_navigation')
            ],
            heading="Contact Form",  
        ),
    ]

    content_panels += [
        MultiFieldPanel(
            [
                FieldPanel('footer_info_title'),                
                FieldPanel('footer_info')
            ],
            heading="Footer",  
        ),
    ]   

    # promote_panels = [
    #     MultiFieldPanel(Page.promote_panels, "Common page configuration"),
    #     ImageChooserPanel('intro_background'),
    #     ]  


