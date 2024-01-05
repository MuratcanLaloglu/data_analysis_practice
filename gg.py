import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Gider Verileri
is_istasyonu_server_maliyet = 269000  # TL
colab_pro_plus_maliyet = 9600  # TL/yıl
bakim_maliyet = 25000  # TL/yıl

toplam_gider = is_istasyonu_server_maliyet + colab_pro_plus_maliyet + bakim_maliyet  # Toplam gider hesaplaması

# Gelir Verileri (Örnek)
kullanici_sayisi = [1000, 2500, 3500, 5000, 8000]  # Örnek: 5 yıl boyunca kullanıcı sayısı
aylik_ucret = 10  # Örnek: Aylık kullanıcı başına ücret 10 TL

toplam_gelir = [kullanici_sayisi[i] * aylik_ucret * 12 for i in range(len(kullanici_sayisi))]  # Toplam yıllık gelir hesaplaması

# Net Bugünkü Değer (NBD) Hesaplaması
indirgeme_orani = 0.1  # Örnek: %20 indirgeme oranı

nakit_akislari = [-is_istasyonu_server_maliyet - colab_pro_plus_maliyet - bakim_maliyet] + toplam_gelir
nbd = [nakit_akis / (1 + indirgeme_orani) ** i for i, nakit_akis in enumerate(nakit_akislari)]

# Başabaş Noktası Hesaplaması
toplam_sabit_maliyetler = is_istasyonu_server_maliyet + bakim_maliyet
birim_basina_degisken_maliyet = colab_pro_plus_maliyet / kullanici_sayisi[-1]  # Son yılda öngörülen kullanıcı sayısı
birim_fiyat = aylik_ucret

birim_basina_degisken_maliyetler = [birim_basina_degisken_maliyet * i for i in range(len(kullanici_sayisi))]
kar = [toplam_gelir[i] - (toplam_sabit_maliyetler + birim_basina_degisken_maliyetler[i]) for i in range(len(kullanici_sayisi))]

# Yılları Tanımla
yillar = [2024, 2025, 2026, 2027, 2028]

# Gelir-Gider Grafiği
plt.figure(figsize=(10, 6))

plt.plot(yillar, toplam_gelir, label='Toplam Gelir', marker='o')
plt.plot(yillar, [toplam_sabit_maliyetler + birim_basina_degisken_maliyetler[i] + bakim_maliyet for i in range(len(yillar))], label='Toplam Maliyet', marker='o')
#plt.plot(yillar, kar, label='Kar', marker='o')
plt.plot(yillar, nbd[1:], label='Net Bugünkü Değer (NBD)', marker='o')  # NBD'nin ilk değeri genellikle çok büyük olduğu için çizgi grafiğe uygun değildir.

plt.xlabel('Yıl')
plt.ylabel('Tutar (bin TL)')
plt.title('Gelir-Gider Analizi')
plt.legend()
plt.grid(True)

# Y ekseni düzenleme
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:,.0f}'.format(x)))

plt.show()
