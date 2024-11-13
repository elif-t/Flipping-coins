def flip_coins(n):
  # Function that simulates the coin flipping algorithm with an array of coins, where:
  # 1 - heads, 0 - tails
  
  # Generate array of n heads coins
  coins = [1]*n 
  
  # The first loop controls the step size (i)
  for i in range(2, n+1):
    for j in range(i-1,n,i):    # Iterate through the correct coins
      coins[j] = 1 - coins[j]   # Flip the coin at that position
  
  return coins


def find_positions(l, value = 1): 
  # Function to find the positions (not indices) of elements in a list,
  # that correspond to a particular value (by default 1, for heads)
  
  pos = list()
  for i in range(len(l)):
    if l[i] == value:
      pos.append(i+1)
  
  return pos


# Print the positions of heads for 1000 coins
print(find_positions(flip_coins(1000)))
