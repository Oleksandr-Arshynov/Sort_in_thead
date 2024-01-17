import multiprocessing
import time

def factorize(number):
    
    """Функція приймає ціле число number 
    і повертає список його дільників без залишку."""
    
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def synchronous_factorization(numbers):
    
    """Функція приймає список чисел та використовує 
    синхронний підхід для обчислення дільників кожного числа."""
    
    results = []
    for number in numbers:
        result = factorize(number)
        results.append(result)
    return results

def parallel_factorization(numbers):
    
    """Функція приймає список чисел та використовує паралельний 
    підхід за допомогою кількох ядер процесора для обчислення 
    дільників кожного числа."""
    
    with multiprocessing.Pool() as pool:
        results = pool.map(factorize, numbers)
    return results

if __name__ == "__main__":
    # Генеруємо список чисел для тестування
    numbers_to_factorize = [128, 255, 99999, 10651060]

    # Синхронна версія
    start_time = time.time()
    synchronous_results = synchronous_factorization(numbers_to_factorize)
    end_time = time.time()
    print(f"Synchronous execution time: {end_time - start_time} seconds")
    print("Synchronous results:", synchronous_results)
    print("", end="\n")

    # Паралельна версія
    start_time = time.time()
    parallel_results = parallel_factorization(numbers_to_factorize)
    end_time = time.time()
    print(f"Parallel execution time: {end_time - start_time} seconds")
    print("Parallel results:", parallel_results)


