from collections import deque

graph = {}
graph["CAB"] = ["CAT", "CAR"]
graph["CAR"] = ["CAT", "BAR"]
graph["CAT"] = ["MAT", "BAT"]
graph["BAR"] = ["BAT"]
graph["MAT"] = ["BAT"]


def find_way(name, goal):
    find_queue = deque()
    find_queue += graph[name]
    edge_count = {}
    edge_count[name] = 0
    before_tag = {}
    visited = []
    for nextWord in graph[name]:
        edge_count[nextWord] = edge_count[name] + 1
        before_tag[nextWord] = name
        visited.append(nextWord)
    while find_queue:
        word = find_queue.popleft()
        if is_word(word, goal):
            print("Found BAT")
            return edge_count[word]
        else:
            print("NOT YET REACHED BAT. CURRENT: " + word)
            visited.append(word)
            for nextWord in graph[word]:
                if nextWord not in visited:
                    edge_count[nextWord] = edge_count[word] + 1
                    before_tag[nextWord] = word
                    visited.append(nextWord)
                find_queue += graph[word]
    return False


def is_word(name, goal):
    return name == goal

print(find_way("CAB", "BAT"))