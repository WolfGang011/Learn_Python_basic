def kiem_tra_chan_le(so): 
    if so % 2 == 0:
        return "Số chẵn"
    else:
        return "Số lẻ"
    
chon = kiem_tra_chan_le(5)
print("Số 5 là :", chon)