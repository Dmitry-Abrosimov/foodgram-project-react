from recipes.models import IngredientRecipe


def get_shopping_list(user):
    shopping_list = {}
    ingredients = IngredientRecipe.objects.filter(
        recipe__shop_list__user=user.user
    )
    for ingredient in ingredients:
        name = ingredient.ingredient.name
        measurement_unit = ingredient.ingredient.measurement_unit
        amount = ingredient.amount
        if name not in shopping_list:
            shopping_list[name] = {
                'measurement_unit': measurement_unit,
                'amount': amount,
            }
        else:
            shopping_list[name]['amount'] += amount
    list_display = ([
        f"- {item}: {value['amount']} {value['measurement_unit']}\n"
        for item, value in shopping_list.items()
    ])
    return list_display
