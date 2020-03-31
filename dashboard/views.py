from django.shortcuts import render, redirect
from .models import Bond
from .forms import BondForm

from alpha_vantage.timeseries import TimeSeries
import time

#bond_list = []


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
    api_key = 'G52RTNSQBOQ4FZZY'

    try:
        ts = TimeSeries(key = api_key, output_format='json')
        data = ts.get_daily(symbol=bond, outputsize = 'compact')

        paivat = []
        avaimet = []
        #if bond not in bond_list:
            #bond_list.append(bond)
            
        for rivi in data:
            for paiva in rivi.keys():
                print(paiva)
                avain = rivi[paiva]
                avaimet.append(avain)

        
        if form.is_valid():
            form.save()
            return redirect('list_bonds')
        return render(request, 'bonds-form.html', {'form':form, 'bond':bond, 'paivat':paivat, 'avaimet':avaimet})

    except: 
        print("papukaija")
        return render(request, 'bond_not_found.html', {'bond':bond})
     

def delete_bond(request, id):
    bond = Bond.objects.get(id=id)
    
    if request.method == 'POST':
        print(bond)
        bond.delete()
        
        return redirect('list_bonds')
    
    return render(request, 'bond-delete.html', {'bond':bond})



def not_in_database(request, id):
    bond = Bond.objects.get(id=id)

    if request == 'GET':
        bond.delete()
        print("kissa")
        return redirect('list_bonds')
    
    print("koira")

    return redirect(request, 'bond_not_found.html', {'bond':bond})
    
    