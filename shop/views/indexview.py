from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from django.db.models import Count
from shop.models import Product
from shop.models import Category


class IndexView(TemplateView):
    template_name = "shop/index.html"

    def get(self, request, id=None):
        categories = Category.objects.order_by("name")
        filter = request.GET.get("q", "")

        if filter:
            title = f"Search result for '{filter}'"
            products = Product.objects.filter(name__icontains=filter).order_by("name")
        elif id is None:
            title = "All Products"
            products = Product.objects.order_by("name")
        else:
            title = next((c.name for c in categories if c.id == id), None)
            products = Product.objects.filter(category_id=id).order_by("name")

        categories = categories.annotate(count=Count("product"))
        category_counts = [{"category_name": c.name, "count": c.count} for c in categories]

        context = {
            "filter": filter,
            "categories": [{"id": c.id, "name": c.name} for c in categories],
            "title": title,
            "products": [{"id": p.id, "name": p.name, "price": p.price, "images": p.images} for p in products],
            "category_counts": category_counts,
        }

        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))
