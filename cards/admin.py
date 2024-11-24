from django.contrib import admin
from cards.models import UserCardProgress, Profile, Deck, Card
# Deck Admin
class DeckAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_public')
    list_filter = ('is_public',)
    search_fields = ('name',)

# Card Admin
class CardAdmin(admin.ModelAdmin):
    list_display = ('anishinaabemowin', 'english', 'pronunciation', 'deck')
    list_filter = ('deck',)
    search_fields = ('anishinaabemowin', 'english', 'pronunciation')

# UserCardProgress Admin
class UserCardProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'card', 'box_level', 'last_reviewed')
    list_filter = ('box_level', 'last_reviewed')
    search_fields = ('user__username', 'card__anishinaabemowin', 'card__english')

# Profile Admin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'study_streak')
    search_fields = ('user__username',)
    list_filter = ('study_streak',)


# Register all models
admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(UserCardProgress, UserCardProgressAdmin)
admin.site.register(Profile, ProfileAdmin)
