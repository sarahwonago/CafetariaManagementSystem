from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.db.models import Q
from django.contrib import messages

from myapps.cafetaria.models import Category, FoodItem

from .forms import CategoryForm, FoodItemForm


#  Define a role-based redirect function for cafeteria admins
def is_cafe_admin(user):
    if user.is_authenticated and user.role == 'admin':
        return True
    if user.is_authenticated and user.role == 'customer':
        return False
    return False


@login_required
@user_passes_test(is_cafe_admin, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def home_view(request):
    return render(request, 'cafeadmin/home.html')


@login_required
@user_passes_test(is_cafe_admin, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def categories_view(request):

    """
    Handles the categories page.
    """
    # query value from the search input
    q = request.GET.get("q")

    # filtering the categories objects based on the q value
    categories = Category.objects.filter(Q(name__icontains=q)) if q else Category.objects.all()

    context = {
        "categories": categories,
    }

    return render(request, "cafeadmin/food_categories.html", context)

@login_required
@user_passes_test(is_cafe_admin, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def add_category_view(request):

    """
    Handles the adding a new category.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("cafeadmin:categories")
    else:
        form = CategoryForm()

    context = {
        "form":form,
    }
    return render(request,"cafeadmin/add_category.html", context)


@login_required
@user_passes_test(is_cafe_admin, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def delete_category_view(request, category_id):

    """
    Handles deleting a category.
    """

    category = get_object_or_404(Category, id = category_id)
    category_name = category.name

    if request.method == 'POST':
        category.delete()
        # include the logic for a success message
        messages.success(request, f'Successfully deleted {category_name}')
        return redirect("cafeadmin:categories")

    context = {
        "category":category,
    }
    return render(request,"cafeadmin/delete_category.html", context)


@login_required
@user_passes_test(is_cafe_admin, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def update_category_view(request, category_id):

    """
    Handles the updating a new category.
    """

    category = get_object_or_404(Category, id = category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        
        if form.is_valid():
            form.save()
            return redirect("cafeadmin:categories")
    else:
        form = CategoryForm(instance=category)

    context = {
        "form":form,
        "category":category,
    }

    return render(request,"cafeadmin/update_category.html", context)


@login_required
@user_passes_test(is_cafe_admin, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def category_fooditem_view(request, category_id):

    """
    Handles the categories page.
    """
    # query value from the search input
    q = request.GET.get("q")
    category = get_object_or_404(Category, id=category_id)

    # filtering the categories objects based on the q value
    fooditems = FoodItem.objects.filter(Q(name__icontains=q),category=category) if q else FoodItem.objects.filter(category=category)

    context = {
        "category": category,
        "fooditems": fooditems,
    }

    return render(request, "cafeadmin/category_items.html", context)


@login_required
@user_passes_test(is_cafe_admin, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def add_fooditem_view(request, category_id):

    """
    Handles the adding a new fooditem.
    """
    category = get_object_or_404(Category, id = category_id)

    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            food = form.save(commit=False)
            food.category = category
            food.save()
            return redirect("cafeadmin:category-items", category_id)
    else:
        form = FoodItemForm()

    context = {
        "form":form,
    }
    return render(request,"cafeadmin/add_fooditem.html", context)


@login_required
@user_passes_test(is_cafe_admin, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def delete_fooditem_view(request, fooditem_id, category_id):

    """
    Handles deleting a fooditem.
    """

    fooditem = get_object_or_404(FoodItem, id = fooditem_id)
    category = get_object_or_404(Category, id = category_id)

    if request.method == 'POST':
        fooditem.delete()
        return redirect("cafeadmin:category-items", category_id)

    context = {
        "fooditem":fooditem,
        "category": category,
    }
    return render(request,"cafeadmin/delete_fooditem.html", context)


@login_required
@user_passes_test(is_cafe_admin, login_url='cafetaria:handle_unauthorized_access', redirect_field_name=None)
def update_fooditem_view(request, fooditem_id, category_id):

    """
    Handles updating a fooditem.
    """

    fooditem = get_object_or_404(FoodItem, id = fooditem_id)

    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES, instance=fooditem)
        
        if form.is_valid():
            form.save()
            return redirect("cafeadmin:category-items", category_id)
    else:
        form = FoodItemForm(instance=fooditem)

    context = {
        "form":form,
        "fooditem":fooditem,
    }

    return render(request,"cafeadmin/update_fooditem.html", context)
