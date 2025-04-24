import random
import numpy as np

# Tạo dữ liệu bài toán Knapsack
NUM_ITEMS = 10
MAX_WEIGHT = 50
items = [(random.randint(10, 100), random.randint(5, 20)) for _ in range(NUM_ITEMS)]

# GA giải bài toán Knapsack với mutation rate tùy chỉnh
def run_ga(mutation_rate, pop_size=100, gens=100):
    def fitness(ind):
        value, weight = 0, 0
        for i in range(NUM_ITEMS):
            if ind[i]:
                v, w = items[i]
                value += v
                weight += w
        return value if weight <= MAX_WEIGHT else 0

    def create_individual():
        return [random.randint(0, 1) for _ in range(NUM_ITEMS)]

    def crossover(p1, p2):
        point = random.randint(1, NUM_ITEMS - 2)
        return p1[:point] + p2[point:]

    def mutate(ind):
        for i in range(NUM_ITEMS):
            if random.random() < mutation_rate:
                ind[i] = 1 - ind[i]

    population = [create_individual() for _ in range(pop_size)]
    for _ in range(gens):
        population = sorted(population, key=fitness, reverse=True)
        next_gen = population[:10]
        while len(next_gen) < pop_size:
            p1, p2 = random.choices(population[:50], k=2)
            child = crossover(p1, p2)
            mutate(child)
            next_gen.append(child)
        population = next_gen

    best = population[0]
    return fitness(best), best

# Tối ưu mutation rate
def optimize_mutation_rate():
    rates = np.linspace(0.01, 0.3, 15)
    results = []
    print("Tối ưu mutation rate:")
    for rate in rates:
        score, _ = run_ga(mutation_rate=rate)
        print(f"  Rate = {rate:.2f} → Fitness = {score}")
        results.append((rate, score))

    best_rate, best_score = max(results, key=lambda x: x[1])
    print(f"\n✅ Mutation rate tối ưu: {best_rate:.2f} đạt fitness = {best_score}")

    # Chạy lại để lấy cá thể tốt nhất và in chi tiết
    _, best_individual = run_ga(mutation_rate=best_rate)
    print("\n📦 Vật phẩm được chọn:")
    total_v, total_w = 0, 0
    for i, gene in enumerate(best_individual):
        if gene == 1:
            v, w = items[i]
            print(f"  - Item {i}: value = {v}, weight = {w}")
            total_v += v
            total_w += w
    print(f"\n➡️  Tổng giá trị: {total_v}, Tổng trọng lượng: {total_w}")

if __name__ == "__main__":
    print("Dữ liệu vật phẩm (value, weight):")
    for i, (v, w) in enumerate(items):
        print(f"  Item {i}: value={v}, weight={w}")
    print("\n=== Bắt đầu tối ưu hóa GA ===\n")
    optimize_mutation_rate()