from django.shortcuts import render

# Create your views here.

def index(request):
    clientes = [
        {"nombre": "Alice Johnson", "email": "alice@example.com", "telefono": "555-1111"},
        {"nombre": "Bob Williams", "email": "bob@example.com", "telefono": "555-2222"},
        {"nombre": "Charlie Brown", "email": "charlie@example.com", "telefono": "555-3333"},
    ]
    contexto = {'clientes': clientes}
    return render(request, 'index.html', contexto)