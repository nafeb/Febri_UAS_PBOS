class DataMahasiswa():
    def init(self,nama,alamat,nim):
        
        print("Inputkan DataPribadi Anda")
        
    def input(self):
        self.nama = input("Nama   : ")
        self.alamat = input("Alamat : ")
        self.nim = input("NIM    : ")
        
class datamahasiswa(DataMahasiswa):
    def cetak(self):
        print ("================================================")
        print ("Berikut adalah Data Pribadi yang telah di input ")
        print ("Nama   : ", self.nama)
        print ("Alamat : ", self.alamat)
        print ("NIM    : ", self.nim)
        
data = datamahasiswa()
data.input()
data.cetak()