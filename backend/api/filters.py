from django_filters.rest_framework import FilterSet, filters
from rest_framework.filters import SearchFilter

from recipes.models import Recipe


class IngredientSearchFilter(SearchFilter):
    search_param = 'name'


class RecipeFilter(FilterSet):

    tags = filters.AllValuesMultipleFilter(field_name='tags__slug')
    is_in_shopping_cart = filters.BooleanFilter(
        method='shopping_cart_filter'
    )
    is_favorited = filters.BooleanFilter(method='favorited_filter')

    class Meta:
        model = Recipe
        fields = ('tags', 'author', 'is_favorited', 'is_in_shopping_cart')

    def shopping_cart_filter(self, queryset, name, value):
        if value:
            return queryset.filter(shop_list__user=self.request.user)
        return queryset

    def favorited_filter(self, queryset, name, value):
        if value:
            return queryset.filter(favorites__user=self.request.user)
        return queryset
