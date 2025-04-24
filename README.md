🧭 1. Giới thiệu bài toán
Trong nhiều bài toán tối ưu phức tạp (như lập lịch, bài toán balo, routing...), thuật toán di truyền (Genetic Algorithm - GA) là một công cụ mạnh mẽ. Tuy nhiên, hiệu suất của GA phụ thuộc rất lớn vào các tham số điều khiển như:

- Kích thước quần thể (population size)

- Tỉ lệ đột biến (mutation rate)

- Tỉ lệ lai ghép (crossover rate)

- Chiến lược chọn lọc (selection method)

Mục tiêu: Tìm bộ tham số GA tối ưu nhất giúp giải bài toán Knapsack hiệu quả nhất (tối đa hóa giá trị balo mà không vượt quá trọng lượng).

🧠 2. Phương pháp xử lý
Chúng ta sẽ thực hiện tối ưu GA theo cách sau:

- Bước 1: Định nghĩa một hàm đánh giá: cho một bộ tham số GA, chạy GA và trả lại fitness cao nhất đạt được.

- Bước 2: Thử nhiều tổ hợp mutation rate (hoặc các tham số khác).

- Bước 3: Ghi nhận kết quả và chọn tham số tốt nhất.

Phương pháp được sử dụng trong demo này là Random Search / Grid Search – đơn giản và dễ hiểu.

⚙️ 3. Các bước xử lý
- Xây dựng bài toán Knapsack với dữ liệu ngẫu nhiên.

- Cài đặt thuật toán di truyền GA giải bài toán này.

- Tạo một vòng lặp thử nhiều giá trị mutation rate.

- Đánh giá và chọn mutation rate cho kết quả tốt nhất.

💻 4. Mã nguồn demo (Python)


# Tạo dữ liệu bài toán Knapsack
NUM_ITEMS = 10
MAX_WEIGHT = 50
items = [(random.randint(10, 100), random.randint(5, 20)) for _ in range(NUM_ITEMS)]

# GA giải bài toán Knapsack với mutation rate tùy chỉnh
def run_ga(mutation_rate, pop_size=100, gens=100):
    def fitness(individual):
        total_value = 0
        total_weight = 0
        for i in range(NUM_ITEMS):
            if individual[i] == 1:
                value, weight = items[i]
                total_value += value
                total_weight += weight
        return total_value if total_weight <= MAX_WEIGHT else 0

    def create_individual():
        return [random.randint(0, 1) for _ in range(NUM_ITEMS)]

    def crossover(p1, p2):
        point = random.randint(1, NUM_ITEMS - 2)
        return p1[:point] + p2[point:]

    def mutate(individual):
        for i in range(NUM_ITEMS):
            if random.random() < mutation_rate:
                individual[i] = 1 - individual[i]

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

    return fitness(population[0])

# Tối ưu mutation rate
def optimize_mutation_rate():
    rates = np.linspace(0.01, 0.3, 15)
    results = []
    print("Tối ưu mutation rate:")
    for rate in rates:
        score = run_ga(mutation_rate=rate)
        print(f"  Rate = {rate:.2f} → Fitness = {score}")
        results.append((rate, score))

    best = max(results, key=lambda x: x[1])
    print(f"\n✅ Mutation rate tối ưu: {best[0]:.2f} đạt fitness = {best[1]}")

if __name__ == "__main__":
    print("Dữ liệu vật phẩm (value, weight):")
    for i, (v, w) in enumerate(items):
        print(f"  Item {i}: value={v}, weight={w}")
    print("\n=== Bắt đầu tối ưu hóa GA ===\n")
    optimize_mutation_rate()
📌 Kết luận
Chúng ta đã tối ưu một tham số (mutation rate) của GA để giải bài toán Knapsack tốt hơn.

Cách làm có thể mở rộng để:

Tối ưu nhiều tham số đồng thời (bằng Grid Search, Bayesian Optimization...).

Tối ưu trên bài toán thực tế hoặc phức tạp hơn.

Đây là bước đầu tiên quan trọng trong quá trình tối ưu meta-heuristic: tối ưu thuật toán tối ưu.

