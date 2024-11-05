class NamaKelas:
    def __init__(self):
        self.__dataPribadi = "ini adalah variable Private"

    # Metode Private
    def __metodePribadi(self):
        return "ini adalah metode Private"

    # Getter untuk __dataPribadi
    def getDataPribadi(self):
        return self.__dataPribadi

    # Setter untuk __dataPribadi
    def setDataPribadi(self, nilaiBaru):
        self.__dataPribadi = nilaiBaru

    # Metode Publik untuk mengakses __metodePribadi
    def aksesMetodePribadi(self):
        return self.__metodePribadi()

    def metodePublik(self):
        print("ini adalah metode publik")
        # metode publik ini bisa mengakses metode dan data pribadi
        print(self.__metodePribadi())
        print(self.__dataPribadi)

class TurunanNamaKelas(NamaKelas):
    def __init__(self):
        # Memanggil konstruktor kelas induk
        super().__init__()

    def demoTurunan(self):
        # Menggunakan getter dari kelas induk
        dataPribadi = self.getDataPribadi()
        print(f"Data pribadi dari kelas induk: {dataPribadi}")

        # Mengubah data pribadi melalui setter kelas induk
        self.setDataPribadi("nilai baru dari turunan")
        dataPribadiBaru = self.getDataPribadi()
        print(f"Data pribadi setelah diubah oleh turunan: {dataPribadiBaru}")
 
        # Mengakses metode pribadi dari kelas induk melalui metode publik
        hasilMetodePribadi = self.aksesMetodePribadi()
        print(f"Hasil akses metode pribadi dari turunan: {hasilMetodePribadi}")


# Membuat objek dari TurunanNamaKelas dan memanggil demonya
objekTurunan = TurunanNamaKelas()
objekTurunan.demoTurunan()
