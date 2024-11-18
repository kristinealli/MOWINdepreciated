from django.contrib import admin
from cards.models import Deck, DeckShare, Card, UserDeck, UserCardProgress, Profile, Tag

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
    list_display = ('user', 'study_streak', 'total_cards_studied')
    search_fields = ('user__username',)
    list_filter = ('study_streak',)

# Tag Admin
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# DeckShare Admin
class DeckShareAdmin(admin.ModelAdmin):
    list_display = ('deck', 'shared_with', 'shared_by')
    search_fields = ('deck__name', 'shared_with__username', 'shared_by__username')

# UserDeck Admin
class UserDeckAdmin(admin.ModelAdmin):
    list_display = ('user', 'deck', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('user__username', 'deck__name')

# Register all models
admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(UserCardProgress, UserCardProgressAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(DeckShare, DeckShareAdmin)
admin.site.register(UserDeck, UserDeckAdmin)
