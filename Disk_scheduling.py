"""
=============================================================
Lab Assignment-4: Disk Scheduling Algorithms
Course: Fundamentals of Operating System Lab (ENCA252)
Program: BCA (AI & DS) - K.R. Mangalam University
=============================================================
Algorithms Implemented:
  1. FCFS   - First Come First Serve
  2. SSTF   - Shortest Seek Time First
  3. SCAN   - Elevator Algorithm
  4. C-SCAN - Circular SCAN
=============================================================
"""


# ─────────────────────────────────────────────
# TASK 1 – Input Handling
# ─────────────────────────────────────────────
def get_input():
    """Read disk request queue, head position, and disk size."""
    print("\n" + "=" * 60)
    print("        DISK SCHEDULING ALGORITHM SIMULATOR")
    print("=" * 60)

    head = int(input("\nEnter initial head position: "))
    disk_size = int(input("Enter disk size (total cylinders): "))
    raw = input("Enter disk request queue (space-separated): ")
    requests = list(map(int, raw.split()))

    print(f"\nInitial Head  : {head}")
    print(f"Disk Size     : {disk_size}")
    print(f"Request Queue : {requests}")
    print(f"Total Requests: {len(requests)}")
    return requests, head, disk_size


# ─────────────────────────────────────────────
# TASK 2 – FCFS (First Come First Serve)
# ─────────────────────────────────────────────
def fcfs(requests, head):
    """
    Requests are serviced in the order they arrive.
    Simple but can cause large seek times.
    """
    seek_time = 0
    sequence  = [head]
    current   = head

    for req in requests:
        seek_time += abs(current - req)
        current = req
        sequence.append(current)

    return seek_time, sequence


# ─────────────────────────────────────────────
# TASK 3 – SSTF (Shortest Seek Time First)
# ─────────────────────────────────────────────
def sstf(requests, head):
    """
    Always picks the request closest to current head position.
    Reduces seek time but may cause starvation of far requests.
    """
    seek_time  = 0
    sequence   = [head]
    current    = head
    remaining  = requests.copy()

    while remaining:
        # Find nearest request to current head
        nearest = min(remaining, key=lambda x: abs(x - current))
        seek_time += abs(current - nearest)
        current = nearest
        sequence.append(current)
        remaining.remove(nearest)

    return seek_time, sequence


# ─────────────────────────────────────────────
# TASK 4 – SCAN (Elevator Algorithm)
# ─────────────────────────────────────────────
def scan(requests, head, disk_size):
    """
    Head moves in one direction servicing requests,
    goes to end of disk, then reverses direction.
    Like an elevator going up then down.
    """
    seek_time = 0
    sequence  = [head]
    current   = head

    left  = sorted([r for r in requests if r < head], reverse=True)
    right = sorted([r for r in requests if r >= head])

    # Move right first
    for r in right:
        seek_time += abs(current - r)
        current = r
        sequence.append(current)

    # Go to end of disk
    seek_time += abs(current - (disk_size - 1))
    current = disk_size - 1
    sequence.append(current)

    # Now move left
    for r in left:
        seek_time += abs(current - r)
        current = r
        sequence.append(current)

    return seek_time, sequence


# ─────────────────────────────────────────────
# TASK 5 – C-SCAN (Circular SCAN)
# ─────────────────────────────────────────────
def cscan(requests, head, disk_size):
    """
    Head moves in one direction only.
    When it reaches the end, it jumps back to cylinder 0
    and continues servicing — gives uniform wait time.
    """
    seek_time = 0
    sequence  = [head]
    current   = head

    left  = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])

    # Move right first
    for r in right:
        seek_time += abs(current - r)
        current = r
        sequence.append(current)

    # Go to end of disk
    seek_time += abs(current - (disk_size - 1))
    current = disk_size - 1
    sequence.append(current)

    # Jump back to 0
    seek_time += disk_size - 1
    current = 0
    sequence.append(current)

    # Service left requests from 0 upward
    for r in left:
        seek_time += abs(current - r)
        current = r
        sequence.append(current)

    return seek_time, sequence


# ─────────────────────────────────────────────
# Helper – Print Result
# ─────────────────────────────────────────────
def print_result(algo_name, seek_time, sequence):
    """Display head movement sequence and total seek time."""
    print(f"\n{'─' * 60}")
    print(f"  {algo_name}")
    print(f"{'─' * 60}")
    print(f"  Head Movement : {' → '.join(map(str, sequence))}")
    print(f"  Total Seek Time: {seek_time} cylinders")


# ─────────────────────────────────────────────
# TASK 6 – Performance Comparison
# ─────────────────────────────────────────────
def compare_algorithms(results):
    """Print ranked comparison of all algorithms."""
    print("\n" + "=" * 60)
    print("           PERFORMANCE COMPARISON")
    print("=" * 60)
    print(f"{'Algorithm':<20} | {'Total Seek Time':>16} | Rank")
    print("─" * 50)

    sorted_r = sorted(results.items(), key=lambda x: x[1])
    for rank, (algo, seek) in enumerate(sorted_r, 1):
        print(f"{algo:<20} | {seek:>16} cylinders | #{rank}")

    print(f"\n  ✔ Best  : {sorted_r[0][0]}  ({sorted_r[0][1]} cylinders)")
    print(f"  ✘ Worst : {sorted_r[-1][0]} ({sorted_r[-1][1]} cylinders)")


# ─────────────────────────────────────────────
# TASK 7 – Result Analysis
# ─────────────────────────────────────────────
def analyze_results(results):
    """Print pros/cons and conclusion for each algorithm."""
    print("\n" + "=" * 60)
    print("           RESULT ANALYSIS & CONCLUSION")
    print("=" * 60)

    analysis = {
        "FCFS": (
            "Simple and fair — requests served in arrival order.\n"
            "    Con: High seek time. No optimization. Poor performance."
        ),
        "SSTF": (
            "Always picks the nearest request — reduces seek time.\n"
            "    Con: Can cause starvation for far-away requests."
        ),
        "SCAN": (
            "Moves in one direction, reverses at end — like an elevator.\n"
            "    Pro: Balanced. No starvation. Good overall performance."
        ),
        "C-SCAN": (
            "One-directional only, jumps back to 0 after reaching end.\n"
            "    Pro: Uniform wait time. Fairer than SCAN for all requests."
        ),
    }

    for algo, comment in analysis.items():
        seek = results.get(algo, "N/A")
        print(f"\n  [{algo}]  —  {seek} cylinders")
        print(f"    {comment}")

    sorted_r = sorted(results.items(), key=lambda x: x[1])
    print("\n  CONCLUSION:")
    print(f"  • SSTF usually gives minimum seek time but risks starvation.")
    print(f"  • SCAN is the most balanced for real-world use.")
    print(f"  • C-SCAN gives uniform response — best for heavy load systems.")
    print(f"  • FCFS is simplest but least efficient.")
    print(f"\n  In this simulation, {sorted_r[0][0]} performed best "
          f"with {sorted_r[0][1]} cylinders of movement.")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    # Task 1 – Input
    requests, head, disk_size = get_input()

    # Task 2-5 – Run all algorithms
    fcfs_seek,  fcfs_seq  = fcfs(requests, head)
    sstf_seek,  sstf_seq  = sstf(requests, head)
    scan_seek,  scan_seq  = scan(requests, head, disk_size)
    cscan_seek, cscan_seq = cscan(requests, head, disk_size)

    # Print results
    print_result("FCFS  (First Come First Serve)",  fcfs_seek,  fcfs_seq)
    print_result("SSTF  (Shortest Seek Time First)", sstf_seek,  sstf_seq)
    print_result("SCAN  (Elevator Algorithm)",       scan_seek,  scan_seq)
    print_result("C-SCAN (Circular SCAN)",           cscan_seek, cscan_seq)

    # Task 6 – Comparison
    results = {
        "FCFS":   fcfs_seek,
        "SSTF":   sstf_seek,
        "SCAN":   scan_seek,
        "C-SCAN": cscan_seek,
    }
    compare_algorithms(results)

    # Task 7 – Analysis
    analyze_results(results)

    print("\n" + "=" * 60)
    print("  Simulation Complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()