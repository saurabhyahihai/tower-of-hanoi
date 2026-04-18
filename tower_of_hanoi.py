"""
Simple Tower of Hanoi demo to show recursion in action.

Also includes optional visualization of rods.
"""

# this is the core function which uses recursion
def generate_moves(n, source, target, auxiliary):
    # generate list of moves using recursion

    # base case: only one disk → move directly
    if n == 1:
        return [(1, source, target)]

    moves = []

    # recursive step:
    # move n-1 disks to helper (function calls itself with smaller n)
    moves += generate_moves(n - 1, source, auxiliary, target)

    # move the largest disk
    moves.append((n, source, target))

    # recursive step:
    # move n-1 disks from helper to target
    moves += generate_moves(n - 1, auxiliary, target, source)

    return moves


def print_moves(moves):
    # print all moves in order
    for disk, source, target in moves:
        print(f"Move disk {disk} from {source} to {target}")


def print_state(rods):
    # print current rods
    print("\nCurrent State:")
    for rod in ['A', 'B', 'C']:
        print(f"{rod}: {rods[rod]}")
    print("-" * 30)


def simulate_moves(moves, num_disks, visualize=0):
    # simulate moves only if visualization is enabled
    if visualize != 1:
        return

    # initial rod setup
    rods = {
        'A': list(range(num_disks, 0, -1)),
        'B': [],
        'C': []
    }

    print_state(rods)

    for disk, source, target in moves:
        rods[source].pop()
        rods[target].append(disk)

        print(f"Move disk {disk} from {source} to {target}")
        print_state(rods)


def main():
    print("=== Tower of Hanoi ===")

    num_disks = 3
    visualize = 0  # set to 1 if you want to see rod states

    print(f"\nDisks: {num_disks}\n")

    # step 1: generate moves (recursion part)
    moves = generate_moves(num_disks, 'A', 'C', 'B')

    # step 2: print moves
    print("Moves:\n")
    print_moves(moves)

    # step 3: optional visualization
    simulate_moves(moves, num_disks, visualize)

    # total moves formula
    print(f"\nTotal moves: {2**num_disks - 1}")


if __name__ == "__main__":
    main()
