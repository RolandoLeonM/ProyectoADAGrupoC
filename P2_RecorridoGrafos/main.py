# main.py

from skimage import io, color, data
# Se debe tener instalado scikit-image utilizando pip:
# >> pip install -U scikit-image

# Avance del Proyecto2: Recorrido Grafos

# Utilizamos la función imread del módulo io para leer la imagen
img = io.imread("P2_RecorridoGrafos/images/chicos.png")

# # mostrando imagen con la función imshow del módulo io
# io.imshow(img)
# io.show()

# mostrando información del número de filas, columnas y capas de la matriz.
# tenemos una imagen de 98x177 pixeles. El tercer número indica que tenemos
# tres capas o canales del módelo de color RGB,
# print(img.shape)    # Forma

# # otras formas de obtener información
# print(img.shape[0]) # filas de imagen
# print(img.shape[1]) # columnas de imagen
# print(img.shape[2]) # Número de canal de imagen
# print(img.size)     # Mostrar el número total de píxeles
# print(img.max())    # Valor máximo de píxeles
# print(img.min())    # Valor mínimo de píxeles
# print(img.mean())   # Promedio de píxeles

# # transformamos la imagen en tono de grises. Para ello vamos
# # a importar el módulo color y a utilizar la función rgb2gray
# img_gris = color.rgb2gray(img)
# io.imshow(img_gris)
# io.show()

# Se convierte la imagen en color gris
img_gray = color.rgb2gray(img)
rows, cols = img_gray.shape

# Se convierte la imagen gris a binario
for i in range(rows):
    for j in range(cols):
        if (img_gray[i, j] <= 0.5):
            img_gray[i, j] = 0
        else:
            img_gray[i, j] = 1
io.imshow(img_gray)
io.show()
