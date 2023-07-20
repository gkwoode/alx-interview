def minOperations(n):
    if n == 1:
        return 0

    operations = 0
    clipboard = 1
    h_count = 1

    while h_count < n:
        # If we can double the existing 'H's in the file
        if n % h_count == 0:
            operations += 1
            clipboard = h_count
            h_count *= 2
        else:
            # Paste the current clipboard content
            operations += 1
            h_count += clipboard

    return operations