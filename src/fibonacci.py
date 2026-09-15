class Fibonacci:
    def fibbo(self, n):
        if n < 0:
            raise ValueError("n doit être positif ou nul")

        previous, current = 0, 1
        for _ in range(n):
            previous, current = current, previous + current
        return previous