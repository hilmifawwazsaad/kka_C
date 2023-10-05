# Nama  : Hilmi Fawwaz Sa'ad
# NRP   : 5025221103
# Kelas : Konsep Kecerdasan Artifisial (C)
# Dosen : Dini Adni Navastara, S.Kom., M.Sc.
# Build : 5 Oktober 2023
# Key   : BFS, GBFS, A*

import heapq
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v, cost):
        self.graph[u].append((v, cost))
    
    # Breadth First Search
    def breadth_first_search(self, start, goal):
        visited = set()
        queue = deque([(start, [start])])  # Menyimpan simpul dan jalur
        while queue:
            current, path = queue.popleft()
            if current == goal:
                print("Jalur terpendek:", " -> ".join(path))
                return
            if current not in visited:
                visited.add(current)
                for neighbor, _ in self.graph[current]:
                    new_path = path + [neighbor]
                    queue.append((neighbor, new_path))
        print("Jalur penghubung (edge) tidak ada")

    # Greedy Best First Search
    def greedy_best_first_search(self, start, target):
        visited = set()
        priority_queue = [(0, start, [start])]  # Store the path as well

        while priority_queue:
            cost, current_city, path = heapq.heappop(priority_queue)

            if current_city == target:
                print("Jalur terpendek:", " -> ".join(path))
                return

            visited.add(current_city)

            for neighbour, edge_cost in self.graph[current_city]:
                if neighbour not in visited:
                    heuristic_cost = self.heuristic(neighbour, target)
                    total_cost = heuristic_cost + edge_cost
                    new_path = path + [neighbour]
                    heapq.heappush(priority_queue, (total_cost, neighbour, new_path))
    
    # A* Search     
    def astar_search(self, start, target):
        visited = set()
        priority_queue = [(0, start, [start])]  # Store the path as well

        while priority_queue:
            cost, current_city, path = heapq.heappop(priority_queue)

            if current_city == target:
                print("Jalur terpendek:", " -> ".join(path))
                return

            if current_city in visited:
                continue

            visited.add(current_city)

            for neighbour, edge_cost in self.graph[current_city]:
                if neighbour not in visited:
                    g_cost = cost + edge_cost
                    h_cost = self.heuristic(neighbour, target)
                    f_cost = g_cost + h_cost
                    new_path = path + [neighbour]
                    heapq.heappush(priority_queue, (f_cost, neighbour, new_path))
    
    # Heuristik  
    def heuristic(self, city, target):
        heuristic_values = {
            'Magetan': 162,
            'Madiun': 126,
            'Ngawi': 130,
            'Surabaya': 0,
            'Ponorogo': 128,
            'Bojonegoro': 60,
            'Nganjuk': 70,
            'Jombang': 36,
            'Lamongan': 36,
            'Gresik': 12,
            'Sidoarjo': 22,
            'Probolinggo': 70,
            'Situbondo': 146,
            'Bangkalan': 140,
            'Sampang': 90,
            'Pamekasan': 104,
            'Sumenep': 150,
        }
        return heuristic_values[city]
    
# Driver code
graph = Graph()

# Edge dan bobotnya
graph.addEdge('Ponorogo', 'Magetan', 34)
graph.addEdge('Ponorogo', 'Madiun', 29)
graph.addEdge('Magetan', 'Ponorogo', 34)
graph.addEdge('Magetan', 'Madiun', 22)
graph.addEdge('Magetan', 'Ngawi', 32)
graph.addEdge('Madiun', 'Ponorogo', 22)
graph.addEdge('Madiun', 'Magetan', 22)
graph.addEdge('Madiun', 'Ngawi', 30)
graph.addEdge('Madiun', 'Nganjuk', 48)
graph.addEdge('Ngawi', 'Magetan', 32)
graph.addEdge('Ngawi', 'Madiun', 30)
graph.addEdge('Ngawi', 'Bojonegoro', 44)
graph.addEdge('Bojonegoro', 'Ngawi', 44)
graph.addEdge('Bojonegoro', 'Nganjuk', 33)
graph.addEdge('Bojonegoro', 'Jombang', 70)
graph.addEdge('Bojonegoro', 'Lamongan', 42)
graph.addEdge('Nganjuk', 'Madiun', 48)
graph.addEdge('Nganjuk', 'Bojonegoro', 33)
graph.addEdge('Nganjuk', 'Jombang', 40)
graph.addEdge('Jombang', 'Nganjuk', 40)
graph.addEdge('Jombang', 'Bojonegoro', 70)
graph.addEdge('Jombang', 'Surabaya', 72)
graph.addEdge('Lamongan', 'Bojonegoro', 42)
graph.addEdge('Lamongan', 'Gresik', 14)
graph.addEdge('Gresik', 'Lamongan', 14)
graph.addEdge('Gresik', 'Surabaya', 12)
graph.addEdge('Surabaya', 'Gresik', 12)
graph.addEdge('Surabaya', 'Jombang', 40)
graph.addEdge('Surabaya', 'Bangkalan', 44)
graph.addEdge('Surabaya', 'Sidoarjo', 40)
graph.addEdge('Bangkalan', 'Surabaya', 44)
graph.addEdge('Bangkalan', 'Sampang', 52)
graph.addEdge('Sampang', 'Bangkalan', 52)
graph.addEdge('Sampang', 'Pamekasan', 31)
graph.addEdge('Pamekasan', 'Sampang', 31)
graph.addEdge('Pamekasan', 'Sumenep', 54)
graph.addEdge('Sumenep', 'Pamekasan', 54)
graph.addEdge('Sidoarjo', 'Surabaya', 25)
graph.addEdge('Sidoarjo', 'Probolinggo', 78)
graph.addEdge('Probolinggo', 'Sidoarjo', 78)
graph.addEdge('Probolinggo', 'Situbondo', 99)
graph.addEdge('Situbondo','Probolinggo', 99)

start_city = 'Magetan'
target_city = 'Surabaya'

# membuat pilihan pencarian
print("Kota awal dari Magetan,\nKota tujuan ke Surabaya")
print("Pilih metode pencarian :")
print("1. Breadth First Search")
print("2. Greedy Best First Search")
print("3. A* Search")
pilihan = int(input("Pilihan nomor: "))

if pilihan == 1:
    print(f"Breadth First Search jalur rute dari {start_city} ke {target_city}:")
    graph.breadth_first_search(start_city,target_city)
elif pilihan == 2:
    print(f"Greedy Best First Search jalur rute dari {start_city} ke {target_city}:")
    graph.greedy_best_first_search(start_city, target_city)
elif pilihan == 3:
    print(f"A* Search jalur rute dari {start_city} ke {target_city}:")
    graph.astar_search(start_city, target_city)
else:
    print("Nomor pilihan tidak tersedia!")

