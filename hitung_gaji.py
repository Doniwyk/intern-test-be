def hitung_gaji(jam_kerja, tarif_per_jam):
    JAM_KERJA_STANDAR = 40
    TARIF_LEMBUR = 1.5

    if jam_kerja <= JAM_KERJA_STANDAR:
        gaji_reguler = jam_kerja * tarif_per_jam
        gaji_lembur = 0
    else:
        gaji_reguler = JAM_KERJA_STANDAR * tarif_per_jam
        jam_lembur = jam_kerja - JAM_KERJA_STANDAR
        gaji_lembur = jam_lembur * (tarif_per_jam * TARIF_LEMBUR)
    
    total_gaji = gaji_reguler + gaji_lembur
    return gaji_reguler, gaji_lembur, total_gaji

def input_validasi(prompt, tipe=float):
    while True:
        try:
            nilai = tipe(input(prompt))
            if nilai < 0:
                print("Nilai tidak boleh negatif. Silakan coba lagi.")
                continue
            return nilai
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def tampilkan_laporan_gaji(gaji_reguler, gaji_lembur, total_gaji):
    print("\n========== Laporan Gaji ==========")
    print(f"Gaji Reguler    : Rp {gaji_reguler:,.2f}")
    print(f"Gaji Lembur     : Rp {gaji_lembur:,.2f}")
    print(f"Total Gaji      : Rp {total_gaji:,.2f}")

def main():
    print("=== Kalkulator Gaji Karyawan ===")
    
    jam_kerja = input_validasi("Masukkan total jam kerja dalam seminggu: ")
    tarif_per_jam = input_validasi("Masukkan tarif per jam (Rp): ")
    
    gaji_reguler, gaji_lembur, total_gaji = hitung_gaji(jam_kerja, tarif_per_jam)
    
    tampilkan_laporan_gaji(gaji_reguler, gaji_lembur, total_gaji)

if __name__ == "__main__":
    main()