def katta_harf(*ismlar):
    list1 = []
    for i in ismlar:
        list1.append(i.title())
    return list1
print(katta_harf("ali", "vali", "mahdiy", "sayfiddin"))