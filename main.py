import csv
from prettytable import PrettyTable

def read_csv():
    try:
        with open("Data.csv", mode="r") as file:
            reader = csv.reader(file)
            headers = next(reader)

            data = []
            for row in reader:
                if row and any(cell.strip() for cell in row):
                    data.append(row)


            table = PrettyTable()
            table.field_names = headers

            for row in data:
                table.add_row(row)

            print("\n=== TABEL DATA MAHASISWA ===")
            print(table)

            print("Jumlah data:", len(data))
            
    except FileNotFoundError:
        print("File Data.csv tidak ditemukan!")

if __name__ == "__main__":
    read_csv()

