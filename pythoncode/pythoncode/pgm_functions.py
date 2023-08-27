import math
import numpy as np
from matplotlib import pyplot as plt


def show_img(values):
    plt.imshow(values, cmap='gray')
    plt.show()


def show_histogram(values_list, passo):
    plt.hist(values_list, bins=int(256/passo))
    print(int(256/passo))
    plt.show()


def rdcurve(file):
    filename = f'{file}.pgm'
    peak = 255
    pgm = PgmFunctions()
    pgm.reader_p2(filename)
    # Given values
    original_values = pgm.data_list  # Y_true = Y (original values)

    quantized_filenames = [f'{file}_q8.pgm', f'{file}_q16.pgm', f'{file}_q32.pgm']
    quantized_values = []
    MSE = []
    PSNR = []
    cont = 0
    for test_file in quantized_filenames:
        pgm = PgmFunctions()
        pgm.reader_p2(test_file)
        quantized_values.append(pgm.data_list)
        MSE.append(np.square(np.subtract(original_values, quantized_values[cont]).mean()))
        PSNR.append(10 * math.log((peak * peak)/MSE[cont], 10))
        cont += 1


    """
    # Given values
    Y_true = [1, 1, 2, 2, 4]  # Y_true = Y (original values)

    # Calculated values
    Y_pred = [0.6, 1.29, 1.99, 2.69, 3.4]  # Y_pred = Y'

    # Mean Squared Error
    MSE = np.square(np.subtract(Y_true, Y_pred)).mean()
    """
    return [PSNR, MSE]





class PgmFunctions:
    def __init__(self):
        self.data_list = None
        self.min_value = None
        self.max_value = None
        self.data = None
        self.width = None
        self.height = None

    def reader_p2(self, pgm_file):
        with open(pgm_file, 'r') as f:
            lines = f.readlines()

        for line in list(lines):
            if line[0] == '#':
                lines.remove(line)

        data = []
        for line in lines[1:]:
            data.extend([int(c) for c in line.split()])

        self.width = data[0]
        self.height = data[1]
        self.max_value = data[2]

        data = np.array(data[3:])
        self.min_value = min(data)

        self.data_list = data
        data = data.reshape(self.width, self.height)
        self.data = data

    def quantifier_image(self, passo, data_list):
        new_data_list = []
        new_data_list.extend(self.aprox_calculator(value, passo) for value in data_list)
        new_data = np.array(new_data_list)
        new_data = new_data.reshape(self.width, self.height)
        return [new_data, new_data_list]

    def aprox_calculator(self, number, passo):
        aproximated_number = (math.floor(number / passo)) * passo + (passo / 2)
        """
        if (number / passo) % (passo/2) == 0:
            aproximated_number = math.floor(number / passo) * passo
        else:
            # aproximated_number = round(number / passo) * passo
            aproximated_number = (math.floor(number / passo)) * passo + (passo/2)
        return aproximated_number
        """
        return aproximated_number

    def create_file_pgm(self, data, filename):
        # open file for writing
        show_img(data)
        fout = open(filename, 'w')

        # define PGM Header
        pgmHeader = 'P2' + '\n' + str(self.width) + ' ' + str(self.height) + '\n' + str(self.max_value) + '\n'

        # write the header to the file
        fout.write(pgmHeader)

        # write the data to the file
        img = np.reshape(data, (self.height, self.width))

        for j in range(self.height):
            bnd = list(img[j, :])
            bnd_str = np.char.mod('%d', bnd)
            bnd_str = np.append(bnd_str, '\n')
            bnd_str = ['  '.join(bnd_str)][0]
            fout.write(bnd_str)
        fout.close()



