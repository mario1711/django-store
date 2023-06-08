from django.shortcuts import render , redirect
from .models import Product , Category
from .forms import FormularioPost
from django.contrib import messages
from django.core.paginator import Paginator
from user.models import Review

def inicio(request):
    category_name = request.GET.get('category')
    search_query = request.GET.get('search_query')
    
    if category_name:
        listado_productos = Product.objects.filter(category__name=category_name)
    elif search_query:
        listado_productos = Product.objects.filter(name__icontains=search_query)
    else:
        listado_productos = Product.objects.all()
    
    categories = Category.objects.all()
    reviews = Review.objects.all()

    paginator = Paginator(listado_productos, 4)
    pagina = request.GET.get("page") or 1
    products = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, products.paginator.num_pages + 1)

    return render(request, 'tienda/inicio.html', {
        "products": products,
        "categories": categories,
        "paginas": paginas,
        "pagina_actual": pagina_actual,
        "reviews": reviews,
    })



def anadir_producto(request):
    if request.method == "POST":
        form = FormularioPost(request.POST , request.FILES)
        if form.is_valid():
            product = form.save()
            nombre = form.cleaned_data.get("nombre")
            messages.success(request , f'Se anadio correctamente {nombre}')
            return redirect("inicio")
        else:
           for msg in form.error_messages:
               messages.error(request , form.error_messages[msg]) 
    form = FormularioPost()
    return render(request , "tienda/anadir_producto.html" , {"form":form})

def mostrar_resenas(request):
    reviews = Review.objects.all()
    return render(request, 'tienda/sidebar.html', {'reviews': reviews})