import cv2
# Alfredo Adair Herrera Rodríguez
# Leer la imagen (asegúrate de que el nombre sea exacto)
img = cv2.imread('cartas.jpeg', 0)

if img is None:
    print("Error: no se pudo cargar la imagen")
else:
    # Aplicar detector de bordes Canny
    bordeCanny = cv2.Canny(img, 100, 200)

    # Mostrar imágenes
    cv2.imshow('Original', img)
    cv2.imshow('Borde Canny', bordeCanny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

