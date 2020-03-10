from django.shortcuts import render, redirect
from .models import Bond
from .forms import BondForm

def list_bonds(request):
    bonds = Bond.objects.all()
    return render(request, 'bonds.html', {'bonds': bonds})

def create_bond(request):
    form = BondForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_bonds')
    
    return render(request, 'bonds-form.html', {'form':form})

def update_bond(request, id):
    bond = Bond.objects.get(id=id)
    form = BondForm(request.POST or None, instance = bond)

    if form.is_valid():
        form.save()
        return redirect('list_bonds')
    return render(request, 'bonds-form.html', {'form':form, 'bond':bond})

def delete_bond(request, id):
    bond = Bond.objects.get(id=id)

    if request.method == 'POST':
        bond.delete()
        return redirect('list_bonds')

    return render(request, 'bond-delete.html', {'bond':bond})

