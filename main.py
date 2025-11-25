import pandas as pd
from prettytable import PrettyTable

# =========================================
# 1. BACA DATA CSV
# =========================================
df = pd.read_csv("data.csv")

# =========================================
# 2. DATA RAW (PrettyTable)
# =========================================
table_raw = PrettyTable()
table_raw.field_names = df.columns.tolist()

for _, row in df.iterrows():
    table_raw.add_row(row.tolist())

print("\n=======================================")
print("        DATA MAHASISWA (RAW)")
print("=======================================")
print(table_raw)



# =========================================
# 3. PENGELOMPOKKAN PER PRODI (TABEL FORMAT)
# =========================================
print("\n=======================================")
print("     PENGELOMPOKKAN MAHASISWA PER PRODI")
print("=======================================")

prodi_list = df["Prodi"].unique()

for prodi in prodi_list:
    print(f"\n\n===== PRODI: {prodi} =====")

    df_prodi = df[df["Prodi"] == prodi]

    table = PrettyTable()
    table.field_names = df.columns.tolist()

    for _, row in df_prodi.iterrows():
        table.add_row(row.tolist())

    print(table)

    # Total angkatan di dalam prodi
    print("\n   Rekap Angkatan dalam Prodi:")
    angkatan_count = df_prodi.groupby("Angkatan").size().reset_index(name="Jumlah")

    for _, row in angkatan_count.iterrows():
        print(f"      - Angkatan {row['Angkatan']}: {row['Jumlah']} mahasiswa")



# =========================================
# 4. TOTAL MAHASISWA PER ANGKATAN
# =========================================
print("\n=======================================")
print("        TOTAL MAHASISWA PER ANGKATAN")
print("=======================================")

angkatan_group = df.groupby("Angkatan").size().reset_index(name="Jumlah")

for _, row in angkatan_group.iterrows():
    print(f"Angkatan {row['Angkatan']}: {row['Jumlah']} mahasiswa")



# =========================================
# 5. TOTAL SELURUH MAHASISWA
# =========================================
print("\n=======================================")
print("        TOTAL SELURUH MAHASISWA")
print("=======================================")
print(f"Total mahasiswa: {len(df)} orang")