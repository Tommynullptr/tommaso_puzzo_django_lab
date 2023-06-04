from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView, ListView, DetailView


# Create your views here.

def index(request):

    return HttpResponse("Hello, world. You're at the store index.")


class UserView(FormView):

    def get(self, request):

            return HttpResponse("Hello, world. You're at the store user.")


class CartView(ListView):

    def get(self, request):

            return HttpResponse("Hello, world. You're at the your cart.")


class OrderView(ListView):

    def get(self, request):

            return HttpResponse("Hello, world. You're at the your order.")


class ProductView(DetailView):

    def get(self, request):

            return HttpResponse("Hello, world. You're at the store product.")