from PIL import Image, ImageDraw

def ong_to_png(ong, file_path):
    img_size = (23 * 10, 23 * 10)  # Her bir hücre için 10x10 piksel
    img = Image.new('RGB', img_size, color='white')  # Tüm arkaplanı beyaz yap
    draw = ImageDraw.Draw(img)

    # L harfinin ortasını bul
    l_sutun = 11
    l_satir = 11

    # L harfini oluştur
    ong[l_satir][l_sutun] = 'L'
    ong[l_satir + 1][l_sutun] = 'L'
    ong[l_satir + 2][l_sutun] = 'L'
    ong[l_satir + 2][l_sutun + 1] = 'L'

    for i in range(23):
        for j in range(23):
            cell_color = 'white' if ong[i][j] == 'L' else 'Black'
            draw.rectangle([j * 10, i * 10, (j + 1) * 10, (i + 1) * 10], fill=cell_color)

    img.save(file_path)

# Boş bir matris oluştur
matris = [[' ' for _ in range(23)] for _ in range(23)]

# L harfini oluştur
matris[11][11] = 'L'
matris[12][11] = 'L'
matris[13][11] = 'L'
matris[13][12] = 'L'

# PNG dosyasını oluştur
ong_to_png(matris, 'siyah_karelerle_L.png')
