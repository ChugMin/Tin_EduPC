diem_chuyen_can = int(input("Nhập vào điểm chuyên cần: "))
diem_giua_ky = int(input("Nhập vào điểm giữa kỳ: "))
diem_cuoi_ky = int(input("Nhập vào điểm cuối kỳ: "))

diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3
if diem_trung_binh >= 9:
	xl = 'A'
elif diem_trung_binh >= 7 and diem_trung_binh < 9:
	xl = 'B'
elif diem_trung_binh >= 5 and diem_trung_binh < 7:
	xl = 'C'
elif diem_trung_binh < 5 and diem_trung_binh > 0:
	xl = 'D'
else: 
	xl = '0'

if xl == '0':
	print("Nhập sai!")
else: 
	print("Xếp loại: ", xl)