from django.contrib import admin
from django.db.models import Avg
from django.urls import reverse
from django.utils.html import format_html
from .models import Product, Feedback


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "price_range", "average_rating", "review_count")
    search_fields = ("name", "description")
    list_filter = ("price_range",)

    def average_rating(self, obj):
        avg = obj.feedback.aggregate(Avg("ratings"))["ratings__avg"]
        if avg:
            return round(avg, 1)
        return "No ratings"

    def review_count(self, obj):
        return obj.feedback.count()


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("product", "ratings", "submitted_at", "short_comment", "view_report_link")
    list_filter = ("ratings", "submitted_at")
    search_fields = ("product__name", "comments")
    readonly_fields = ("submitted_at",)

    def short_comment(self, obj):
        return obj.comments[:50] + "..." if len(obj.comments) > 50 else obj.comments

    def view_report_link(self, obj):
        url = reverse("feedback_report")
        return format_html('<a href="{}">View Report</a>', url)

    view_report_link.short_description = "Report"