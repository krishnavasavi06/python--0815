def find_lsd_msd(number):
    num_str = str(number)
    lsd = num_str[-1]
    msd = num_str[0]
    return lsd, msd

input_number = 1010101
lsd, msd = find_lsd_msd(input_number)
print("Input:", input_number)
print("MSD:", msd)
print("LSD:", lsd)
