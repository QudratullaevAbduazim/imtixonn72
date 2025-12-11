from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import PhoneForm
from .models import Phones, Category

class HomeView(View):
    def get(self, request):
        q = request.GET.get('q')
        categories = Category.objects.all()
        phones = Phones.objects.all().order_by('-id')

        if q:
            phones = phones.filter(Q(name__icontains=q) | Q(price__icontains=q) | Q(year__icontains=q) | Q(category__name__icontains=q)).order_by('-id')

        return render(request, 'home.html', {'categories': categories, 'phones': phones})

class CategoryDetailView(View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        phones = Phones.objects.filter(category=category).order_by('-id')
        return render(request, 'category_detail.html', {'category': category, 'phones': phones})



class PhoneDetailView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phones, pk=pk)
        return render(request, 'phone_detail.html', {'phone': phone})


class PhoneCreateView(View):
    def get(self, request):
        form = PhoneForm()
        return render(request, 'phone_create.html', {'form': form})

    def post(self, request):
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            phone = form.save()
            return redirect('phone_detail', pk=phone.pk)
        return render(request, 'phone_create.html', {'form': form})


class PhoneUpdateView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phones, pk=pk)
        form = PhoneForm(instance=phone)
        return render(request, 'phone_update.html', {'form': form, 'phone': phone})

    def post(self, request, pk):
        phone = get_object_or_404(Phones, pk=pk)
        form = PhoneForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            phone = form.save()
            return redirect('phone_detail', pk=pk)
        return render(request, 'phone_update.html', {'form': form, 'phone': phone})



class PhoneDeleteView(View):
    def get(self, request, pk):
        phone = get_object_or_404(Phones, pk=pk)
        return render(request, 'phone_delate.html', {'phone': phone})

    def post(self, request, pk):
        phone = get_object_or_404(Phones, pk=pk)
        phone.delete()
        return redirect('home')
