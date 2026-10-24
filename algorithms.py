def sort_steps(numbers, algorithm):
    a, frames = numbers[:], []
    comparisons = moves = 0

    def save(action, ids=()):
        frames.append((a[:], action, tuple(ids), comparisons, moves))

    save("Ready")

    # Bubble Sort
    if algorithm == "Bubble Sort":
        for end in range(len(a)-1, 0, -1):
            for j in range(end):
                comparisons += 1
                save("Compare", (j, j+1))
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    moves += 1
                    save("Swap", (j, j+1))

    # Selection Sort
    elif algorithm == "Selection Sort":
        for i in range(len(a)-1):
            m = i
            for j in range(i+1, len(a)):
                comparisons += 1
                save("Compare", (m, j))
                if a[j] < a[m]:
                    m = j
            if m != i:
                a[i], a[m] = a[m], a[i]
                moves += 1
                save("Swap", (i, m))

    # Insertion Sort
    elif algorithm == "Insertion Sort":
        for i in range(1, len(a)):
            value, j = a[i], i-1
            while j >= 0:
                comparisons += 1
                save("Compare", (j, j+1))
                if a[j] <= value:
                    break
                a[j+1] = a[j]
                moves += 1
                save("Move", (j, j+1))
                j -= 1
            a[j+1] = value
            moves += 1
            save("Insert", (j+1,))

    # Merge Sort
    elif algorithm == "Merge Sort":
        def merge(lo, hi):
            nonlocal comparisons, moves

            if hi-lo < 2:
                return

            mid = (lo+hi)//2
            merge(lo, mid)
            merge(mid, hi)

            left, right = a[lo:mid], a[mid:hi]
            i = j = 0
            k = lo

            while i < len(left) and j < len(right):
                comparisons += 1
                save("Compare", (lo+i, mid+j))

                if left[i] <= right[j]:
                    a[k] = left[i]
                    i += 1
                else:
                    a[k] = right[j]
                    j += 1

                moves += 1
                save("Merge", (k,))
                k += 1

            while i < len(left):
                a[k] = left[i]
                i += 1
                k += 1
                moves += 1
                save("Merge", (k-1,))

            while j < len(right):
                a[k] = right[j]
                j += 1
                k += 1
                moves += 1
                save("Merge", (k-1,))

        merge(0, len(a))

    # Quick Sort
    elif algorithm == "Quick Sort":
        def quick(lo, hi):
            nonlocal comparisons, moves

            if lo >= hi:
                return

            pivot, i = a[hi], lo-1

            for j in range(lo, hi):
                comparisons += 1
                save("Compare", (j, hi))

                if a[j] <= pivot:
                    i += 1
                    if i != j:
                        a[i], a[j] = a[j], a[i]
                        moves += 1
                        save("Swap", (i, j))

            if i+1 != hi:
                a[i+1], a[hi] = a[hi], a[i+1]
                moves += 1
                save("Pivot", (i+1, hi))

            quick(lo, i)
            quick(i+2, hi)

        quick(0, len(a)-1)

    save("Sorted")
    return frames