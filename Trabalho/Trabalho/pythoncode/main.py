# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from pgm_functions import PgmFunctions, show_img, show_histogram, rdcurve

passo_inicial = 1
file = 'lena.ascii'
filename = f'{file}.pgm'
original_image = PgmFunctions()
original_image.reader_p2(filename)
[pixel_values, pixel_values_list] = [original_image.data, original_image.data_list]
print(pixel_values)
show_img(pixel_values)
show_histogram(pixel_values_list, passo_inicial)

# QUANTIZAR IMAGEM

passo = 64
quantized_filename = f'{file}_q{passo}.pgm'
quantized_image = PgmFunctions()
quantized_image.reader_p2(quantized_filename)
[q_pixel_values, q_pixel_values_list] = quantized_image.quantifier_image(passo, pixel_values_list)
print(q_pixel_values)
original_image.create_file_pgm(q_pixel_values, quantized_filename)
show_histogram(q_pixel_values_list, passo)

print(f"PSNR = {rdcurve(file)[0]}, MSE = {rdcurve(file)[1]}")
