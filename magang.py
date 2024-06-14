# Sistemkode

#fungsi untuk menghitung gaji
def hitung_gaji(jam_kerja, tarif_per_jam):
    #kondisiawal
    jam_standar = 40

    #pengkondisian jam kerja dan declare variabel
    if jam_kerja > jam_standar:
        jam_lembur = jam_kerja - jam_standar
        gaji_lembur = jam_lembur * tarif_per_jam * 1.5
        gaji_standar = jam_standar * tarif_per_jam
        total_gaji = gaji_standar + gaji_lembur
    else:
        total_gaji = jam_kerja * tarif_per_jam
        
    return total_gaji

jam_kerja = int(input("Masukkan jumlah jam kerja: "))
tarif_per_jam = float(input("Masukkan tarif per jam: ")) #float agar lebih fleksibel dengan hasil gaji

gaji = hitung_gaji(jam_kerja, tarif_per_jam)

print(f"Gaji karyawan adalah: {gaji:.2f}")
