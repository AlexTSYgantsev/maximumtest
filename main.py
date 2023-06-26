# === Ассимптотическая сложность ===

# * Первый, но долгий способ *
# def strcounter(s):
#     for syn in s:
#         counter = 0
#         for sub_syn in s:
#             if syn == sub_syn:
#                 counter += 1
#         print(syn, counter)
# s= 'aaabc'
# strcounter(s)

# * Второй способ, не подходит, все символы могут быть уникальны *

# def strcounter(s):
#     for syn in set(s): # для каждой УНИКАЛЬНОЙ буквы перебираем свое, повторений нету
#         counter = 0
#         for sub_syn in s:
#             if syn == sub_syn:
#                 counter += 1
#         print(f'{syn}:{counter}')
#
# s = 'aaabc'
# # M * N
# # N * N - худший сдучай, если все символы уникальны
# strcounter(s)

# * Третий способ, самый оптимальный *
def strcounter(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0) + 1 # хочу взять предыдущее значение, если такого ключа нет, то дать ему значение 0
    print('hello')
    print(syms_counter)

# O(N) = N
strcounter('aaagiabca')
