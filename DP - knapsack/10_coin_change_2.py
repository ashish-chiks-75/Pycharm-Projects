from sys import maxsize as I
# problem statement: given array of coins, find the number of min coins to make given amount.


def minCoins(coins, m, V):
    # table[i] will be storing the minimum
    # number of coins required for i value.
    # So table[V] will have result
    # Initialize all table values as Infinite
    table = [I for _ in range(V + 1)]

    # Base case (If given value V is 0)
    table[0] = 0

    # Compute minimum coins required
    # for all values from 1 to V
    for i in range(1, V + 1):

        # Go through all coins smaller than i
        # coin array should be sorted.
        for j in range(m):
            if coins[j] <= i:
                val = table[i - coins[j]]
                if val != I:
                    table[i] = min(table[i], val + 1)
            else:
                break
    return table[V]


arr1 = [1, 4, 8, 10]
x = 32
print("min coins required:", minCoins(arr1, len(arr1), x))
