# -*- coding utf-8 -*-

# filename: fiber_budget.py
# Author: Luiz Felipe Coelho


def lim_aten(P_rx, P_tx, wavelen, P):
    if wavelen == 1310:
        alpha_f = 0.34
    else:
        alpha_f = 0.22
    L_b = 3
    alpha_e = 0.1
    marg = 2
    alpha_c = 0.5
    num_c = 2
    L_max = (P_tx - P_rx - alpha_c*num_c - P - marg - alpha_e)/(alpha_e/L_b + 
                                                                alpha_f)
    return L_max


def lim_crom(delta_disp, wavelen):
    if wavelen == 1310:
        D_f = 2
    else:
        D_f = 19
    if delta_disp == 'NA':
        L_max = 'NA'
    else:
        L_max = delta_disp/D_f
    return L_max

# ----------------------------------------------------------------------------
#                                  SDH L-4.1
# ----------------------------------------------------------------------------
lim1_a = lim_aten(-28, -3, 1310, 1)
lim2_a_MLM = lim_crom(92, 1310)
lim2_a_SLM = lim_crom('NA', 1310)

if lim1_a < lim2_a_MLM:
    lim_a_MLM = lim1_a
else:
    lim_a_MLM = lim2_a_MLM

lim_a_SLM = lim1_a
print('\n a)')
print('------------------------------------------------------------------')
print('                        SDH L-4.1:')
print('------------------------------------------------------------------')
print('Para um transmissor do tipo MLM, a distância máxima será de %.3f km' % lim_a_MLM)
print('Para um transmissor do tipo SLM, a distância máxima será de %.3f km' % lim_a_SLM)
print('\n')

# ----------------------------------------------------------------------------
#                                  SDH L-16.2
# ----------------------------------------------------------------------------
lim1_b = lim_aten(-28, -2, 1550, 2)
lim2_b = lim_crom((1200+1600)/2, 1550)

if lim1_b < lim2_b:
    lim_b = lim1_b
else:
    lim_b = lim2_b

print('b)')
print('------------------------------------------------------------------')
print('                        SDH L-16.2:')
print('------------------------------------------------------------------')
print('A distância máxima será de %.3f km' % lim_b)
print('\n')

# ----------------------------------------------------------------------------
#                                  SDH L-4.2
# ----------------------------------------------------------------------------
lim1_c = lim_aten(-28, -3, 1550, 1)
lim2_c = lim_crom('NA', 1550)

print('c)')
print('------------------------------------------------------------------')
print('                        SDH L-4.2:')
print('------------------------------------------------------------------')
print('A distância máxima será de %.3f km' % lim1_c)
print('\n')

# ----------------------------------------------------------------------------
#                                  SDH L-1.2
# ----------------------------------------------------------------------------
lim1_d = lim_aten(-34, -5, 1550, 1)
lim2_d = lim_crom('NA', 1550)

print('d)')
print('------------------------------------------------------------------')
print('                        SDH L-1.2:')
print('------------------------------------------------------------------')
print('A distância máxima será de %.3f km' % lim1_d)
print('\n')
