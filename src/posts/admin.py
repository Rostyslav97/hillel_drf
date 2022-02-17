from django.contrib import admin

from .models import Post, HealthCheck

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(HealthCheck)
class HealthCheckAdmin(admin.ModelAdmin):
    pass