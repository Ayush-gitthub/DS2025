adjacency_matrix = [
 [0,0,1,1],
 [1,0,0,0],
 [1,1,0,1],
 [1,1,0,0]
]

def probability_adjacent_matrix(a):
    x = 0
    for i in range(len(a)):
        x = x + a[i]
    if x == 0:
        return a
    for i in range(len(a)):
        a[i] = a[i] / x
    return a

# Normalize each row and store in a new matrix
normalized_matrix = [probability_adjacent_matrix(row) for row in adjacency_matrix]

# Print the normalized matrix
for i, row in enumerate(normalized_matrix):
    print(f"Row {i}: {row}")

d = 0.85

def calculate_pagerank_simple(adj_matrix, d=0.85, iterations=100):
    """
    A minimal, numpy-free implementation of the PageRank algorithm.
    """
    num_pages = len(adj_matrix)

    # --- Step 1: Create the probability-based transition matrix ---
    # First, find the number of outbound links for each page (column sums)
    outbound_counts = [sum(row[j] for row in adj_matrix) for j in range(num_pages)]
    print(f"\nOutbound Counts: {outbound_counts}")
    # M_tilde will store the probability of moving from page j to page i
    M_tilde = [[0] * num_pages for _ in range(num_pages)]
    for j in range(num_pages):
        if outbound_counts[j] == 0: # Handle pages with no outbound links
            for i in range(num_pages): M_tilde[i][j] = 1.0 / num_pages
        else:
            for i in range(num_pages): M_tilde[i][j] = adj_matrix[i][j] / outbound_counts[j]

    # --- Step 2: Iteratively calculate the ranks ---
    ranks = [1.0 / num_pages] * num_pages
    random_jump = (1.0 - d) / num_pages

    for _ in range(iterations):
        new_ranks = [0] * num_pages
        for i in range(num_pages): # For each page i we are calculating the rank for
            # Sum the influence from all pages j that link to i
            influence_sum = sum(M_tilde[i][j] * ranks[j] for j in range(num_pages))
            new_ranks[i] = random_jump + d * influence_sum
        ranks = new_ranks

    return ranks

# --- Run the Algorithm and Display Results ---
final_ranks = calculate_pagerank_simple(adjacency_matrix, d=0.85)

print("--- Final PageRank Scores ---")
for i, rank in enumerate(final_ranks, 1):
    print(f"Page {i}: {rank:.4f}")

# Verify that the probabilities sum to 1.0
print(f"\nSum of scores: {sum(final_ranks):.4f}")

