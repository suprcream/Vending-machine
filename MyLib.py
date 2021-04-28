def vending_art(v):
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print("　　　|　　|┌─────────────┐|")
    print("　　　|　　|│![] [] [] [] │|")
    print("　　　|　　|::l三三三三三三!|")
    print("　　　|　　|│![] [] [] [] │|")
    print("　　　|　　|::l三三三三三三!|")
    print("　　　|　　|┌─────────────┐|　    　     |ヽ,,|ヽ")
    print("　　　|　　|│",v ,"_∧∧　　　　　　　  (　　　 ）")
    print("　　　{二二 ￣￣ ⊂<　　⌒ヽ　　　　　　  と　 　 i")
    print("　　　　　　　　　∪(＿つつ　　  　　     　しーJ")
    print("")
    print("")


def pesan(p):
    cc = 1
    f = 2
    s = 3
    fr = 4
    ntah = 5
    if p == cc:
        q = "cola"
        print("Silahkan ambil Coca Cola anda :)")
        vending_art(q)
    elif p == f:
        q = "fanta"
        print("Silahkan ambil fanta anda :)")
        vending_art(q)
    elif p == s:
        q = "sprite"
        print("Silahkan ambil Sprite anda :)")
        vending_art(q)
    elif p == f:
        q = "frestea"
        print("Silahkan ambil Sprite anda :)")
        vending_art(q)
    else:
        print("not valid")
    


def masukan_uang(u):
    if u >= 10000:
        print("oke tunggu sebentar")
    elif u < 10000:
        print("uang tidak cukup silahkan masukkan uang yang pas")
    else:
        print("uang tidak valid")
    


