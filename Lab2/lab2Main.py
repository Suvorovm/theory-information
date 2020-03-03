import string

from Lab1Functions.genrator import generate_probability_dict
from Lab2.ShennonCod import calculate_Shennon_cod_with_sort

alphabet = string.ascii_letters + string.digits + ' '

probabilityDict = generate_probability_dict(alphabet)
calculate_Shennon_cod_with_sort()