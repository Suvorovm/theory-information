import string

from Lab1Functions.genrator import generate_probability_dict
from Lab2.Khartli import calculate_Khartli_code_with_sort
from Lab2.ShennonCod import calculate_Shennon_cod_with_sort

alphabet = string.ascii_letters + string.digits + ' '

probabilityDict = {'А': 0.3, 'Б': 0.25, 'В': 0.15, 'Г': 0.1, 'Д': 0.1,
                   'Е': 0.05, 'Ж': 0.04, 'З': 0.005,'И': 0.005}  # generate_probability_dict(alphabet)
calculate_Shennon_cod_with_sort(probabilityDict)
#calculate_Khartli_code_with_sort(probabilityDict)