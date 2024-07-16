import matplotlib.pyplot as plt

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    sequence = fibonacci_generator(n)
    print(f"Fibonacci Sequence: {sequence}")  # Print the sequence to the console
    ratios, golden_ratio_approx = analyze_fibonacci(sequence)
    print(f"Golden Ratio Approximation: {golden_ratio_approx}")
    visualize_fibonacci(sequence, ratios)

def fibonacci_generator(n):
    a, b = 1, 1  # Starting from 1 to avoid division by zero
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def analyze_fibonacci(sequence):
    ratios = [sequence[i+1] / sequence[i] for i in range(len(sequence) - 1)]
    golden_ratio_approx = ratios[-1] if ratios else float('inf')
    return ratios, golden_ratio_approx

def visualize_fibonacci(sequence, ratios):
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(sequence, label='Fibonacci Sequence')
    plt.title('Fibonacci Sequence')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(ratios, label='Golden Ratio Approximation')
    plt.title('Golden Ratio Approximation')
    plt.xlabel('Index')
    plt.ylabel('Ratio')
    plt.axhline(y=1.618, color='r', linestyle='--', label='Golden Ratio')
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()