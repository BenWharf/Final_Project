slash = int(input("Enter Number: "))

bin_mask = ("0" * slash) + ("1" * (32 - slash))

new_mask = [int(bin_mask[:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:], 2)]

new_mask = map(str, new_mask)

print(".".join(list(new_mask)))
