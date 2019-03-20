from django.contrib import admin
from .models import QuizCategory # Import QuizCategory module


# Register QuizCategory module on the admin interface
@admin.register(QuizCategory)
class QuizCategoryAdmin(admin.ModelAdmin):
    class Meta:
        model = QuizCategory
        # All fields of QuizCategory
        fields = '__all__'
