#tugas uts klompok
#wattlampu       = 5
#wattkipas       = 40
#wattTv          = 75
#durasipemakaian = 17 jam
def hitung_konsumsi_listrik(wattlampu, wattkipas, watttv, durasi, biayaperkwh = 1500):
    # Hitung kWh
    kwhlampu = wattlampu * durasi / 1000
    kwhkipas = wattkipas * durasi / 1000
    kwhtv = watttv * durasi / 1000

    # Tampilkan hasil kWh masing-masing
    print("Hasil kWh lampu = ", kwhlampu)
    print("Hasil kWh kipas = ", kwhkipas)
    print("Hasil kWh TV = ", kwhtv)

    # Hitung total kWh
    total_kwh = kwhlampu + kwhkipas + kwhtv
    print("Total seluruh kWh = ", total_kwh)

    # Hitung biaya per hari
    biaya_per_hari = total_kwh * biayaperkwh
    print("Biaya per hari = ", biaya_per_hari)

    # Hitung biaya per bulan
    biaya_per_bulan = biaya_per_hari * 30
    print("Biaya per bulan = ", biaya_per_bulan)
    return biaya_per_hari, biaya_per_bulan

# Contoh pemanggilan fungsi
wattlampu = int(input("Masukkan watt lampu = "))
wattkipas = int(input("Masukkan watt kipas = "))
watttv = int(input("Masukkan watt TV = "))
durasi = int(input("Masukkan durasi penggunaan (jam) = "))
hitung_konsumsi_listrik(wattlampu, wattkipas, watttv, durasi)