def generate_pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(a, limit):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= limit:
                triplets.append((a, b, int(c)))
    return triplets

# Input the limit from the user
limit = int(input("Enter the limit for Pythagorean triplets: "))

# Generate Pythagorean triplets up to the limit
triplets = generate_pythagorean_triplets(limit)

# Print the generated Pythagorean triplets
print("Pythagorean triplets up to", limit, "are:")
for triplet in triplets:
    print(triplet)
