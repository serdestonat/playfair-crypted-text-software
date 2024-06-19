from pozisyonBul import pozisyon_bul
from playfair import metin_hazirla

def playfair_encrypt(plaintext, table):
    hazirlanmis_metin = metin_hazirla(plaintext)
    ciphertext = ""
    for i in range(0, len(hazirlanmis_metin), 2):
        row1, col1 = pozisyon_bul(hazirlanmis_metin[i], table)
        row2, col2 = pozisyon_bul(hazirlanmis_metin[i + 1], table)
        
        if row1 == row2:
            ciphertext += table[row1][(col1 + 1) % 6] + table[row2][(col2 + 1) % 6]
        elif col1 == col2:
            ciphertext += table[(row1 + 1) % 6][col1] + table[(row2 + 1) % 6][col2]
        else:
            ciphertext += table[row1][col2] + table[row2][col1]
    return ciphertext