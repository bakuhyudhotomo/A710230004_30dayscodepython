# Kontrol alur menggunakan if-else
nilai = 85

if nilai >= 90:
    grade = 'A'
elif nilai >= 80:
    grade = 'B'
elif nilai >= 70:
    grade = 'C'
elif nilai >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Nilai:", nilai)
print("Grade:", grade)