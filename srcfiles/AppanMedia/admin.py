from django.contrib import admin
from django.contrib.admin.decorators import action
from AppanMedia.models import ContactModel, userProfile, blogPost, Comment, Testimonial

# Register your models here.
@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'email', 'phone')

@admin.register(userProfile)
class userProfileAdmin(admin.ModelAdmin):
    model= userProfile


@admin.register(blogPost)
class blogPostAdmin(admin.ModelAdmin):
    model = blogPost

    list_display = (
        "id", "title", "published_date", "published_status",
    )

    list_filter=(
        "published_status",
        "published_date",
    )

    search_fields = (
        "title", "subtitle", "slug","content",
    )

    prepopulated_fields = { "slug":(
        "title",
    )
    }

    date_hierarchy = "published_date"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display=('client_name', 'client_feedback')
