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
        paivatrvrs = []
        avaimet = []
        open_values = []
        volume_values = []

        paivastr = "["
        k = 0 
        for rivi in data:
            for paiva in rivi.keys():
                if(k<=99):
                    paivat.append(paiva)
                    paivatrvrs.append(paiva)
                    if(k>0):
                        paivastr = paivastr + ", " + paiva
                    if(k<1):
                        paivastr = paivastr + paiva

                avain = rivi[paiva]
                avaimet.append(avain)
                k += 1
        paivastr = paivastr + "]"
        i = 0
        volumestr = "["

        for arvo in avaimet:
            if(i<=99):
                open_values.append(arvo['1. open'])
                volume_values.append(int(arvo['5. volume']))
                if(i>0):
                    volumestr = volumestr + ", " + arvo['5. volume']
                elif(i<1):
                    volumestr = volumestr + arvo['5. volume']
        
                
            i += 1
        volumestr = volumestr + "]"
        paivatrvrs.reverse()
        volume_values.reverse()
        open_values.reverse()
        
        testi = str('kissa')
        if form.is_valid():
            form.save()
            return redirect('list_bonds')
        return render(request, 'bonds-form.html', {'form':form, 'bond':bond, 'paivat':paivat, 
        'avaimet':avaimet, 'open_values':open_values,
        'volume_values':volume_values, 'paivastr':paivastr, 'volumestr':volumestr,'testi':testi, 'paivatrvrs':paivatrvrs})

    except:     
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
    
    