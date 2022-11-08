d = {
    1:{'current_value': 5},
    2:{'current': 10}    
    }

total = []
menu = int(input("Silahkan Pilih Menu : "))
berapa  = int(input("Berapa banyak yang akan anda pesan: "))
for elem, value in d.items():
   for name, price in value.items():
    if elem == menu:
        total_harga = berapa * price
        total[:0] = [name, total_harga]
print(total)
    # for k,v in elem.items():       # for key,val in the elem of the list 
    #     if 'current_value' in k:   # if current_value is in the key
    #         elem[k] = int(v)