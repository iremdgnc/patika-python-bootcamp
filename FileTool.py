import csv
import json


class FileToolClass:

    def __init__(self, file_path, *fields, ):
        self.file_path = file_path
        self.fields = fields
        self.list_ = list()

    def findHeader(self):
        header = list()
        with open(self.file_path, "r") as file:
            sniffer = csv.Sniffer()
            dialect = sniffer.sniff(file.readline())
            file.seek(0)
            has_header = sniffer.has_header(file.read(2048))
            file.seek(0)
            if has_header == True:
                header.append(file.readline().split(dialect.delimiter))
            else:
                temp = file.readline().split(dialect.delimiter)
                for i in range(0, len(temp)):
                    header.append(str(i))
                file.seek(0)
            return header

    def csv_read(self):
        headerFlag = False
        if len(self.fields) < 1:
            header = self.findHeader()
        else:  #
            headerFlag = True
        with open(self.file_path, "r") as file:
            if headerFlag == True:
                self.list_.append(self.fields)
                thrash = file.readline()
            product_list = csv.reader(file)
            for item in product_list:
                self.list_.append(item)
            return self.list_

    def menu(self):
        self.csv_read()
        while True:
            selection = input("- Dosya İçinde Arama Yapmak İçin 1'e Basın. \n- Dosyadan Eleman Silmek İçin 2'ye Basın. "
                              "\n- Dosyaya Ekleme Yapmak İçin 3'e Basın. \n- Dosyayı Güncellemek İçin 4'e Basın. \n ")
            if selection == '1':
                self.search()
            elif selection == '2':
                self.delete()
            elif selection == '3':
                self.add()
            elif selection == '4':
                self.update()
            break

    def search(self):
        header = self.list_[0]
        print(header)
        searchParameter = input("Hangi Parametreye Göre Arama Yapmak İstiyorsunuz?")
        parameterIndex = header.index(searchParameter)
        searchValue = input("Aranacak Değer Nedir?")
        for i in self.list_:
            if i[parameterIndex] == searchValue:
                print(i)

    def delete(self):
        header = self.list_[0]
        print(header)
        deleteParameter = input("Hangi Parametreye Göre Silmek İstersiniz?")
        parameterIndex = header.index(deleteParameter)
        deleteValue = input("Silinecek Değer Nedir?")
        for i in self.list_:
            if i[parameterIndex] == deleteValue:
                self.list_.remove(i)

    def add(self):
        header = self.list_[0]
        print(header)
        newItem = list()
        for i in header:
            newItem.append(input(i + ":"))
        print(newItem)
        self.list_.append(newItem)
        print("Yeni Liste: ", self.list_)

    def update(self):
        header = self.list_[0]
        print(header)
        updateParameter = input("Hangi Parametre Üzerinden Güncelleme Yapmak İstersiniz?: ")
        parameterIndex = header.index(updateParameter)
        oldValue = input("Güncellenecek Eski Değer Nedir?: ")
        updateValue = input("Yeni Değer Nedir?: ")
        for item in self.list_:
            if item[parameterIndex] == oldValue:
                item[parameterIndex] = updateValue

    def save_csv_and_json(self, output_path, output_type):
        if output_type == "csv":
            with open(output_path, "w") as file:
                csv_writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
                for item in self.list_:
                    csv_writer.writerow(item)

        elif output_type == "json":
            deneme = list()
            header = self.list_[0]
            for item in self.list_[1:]:
                deneme.append(dict(zip(header, item)))
            print(deneme)
            with open(output_path, "w") as file:
                json.dump(deneme, file, indent=4)

    def auto_save(self):  # Yapılan değişiklikleri mevcut csv'ye kaydeder.
        with open(self.file_path, "w") as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar='', quotechar='')
            for item in self.list_:
                csv_writer.writerow(item)

    def degisken_json(self, row_ID, option):
        wanted_row = None
        for i in self.list_:
            if i[0] == row_ID:
                wanted_row = i

        if wanted_row == None:
            print("ID Bilgisi Bulunamadı.")

        if option == 1:
            return wanted_row

        elif option == 2:
            self.save_csv_and_json(self.file_path, "json")


deneme = FileToolClass("products.csv")
x = deneme.csv_read()
deneme.save_csv_and_json("irem.csv","csv")








