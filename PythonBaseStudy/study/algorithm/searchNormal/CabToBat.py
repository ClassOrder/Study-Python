from collections import deque

graph = {}
graph["CAB"] = ["CAT", "CAR"]
graph["CAR"] = ["CAT", "BAR"]
graph["CAT"] = ["MAT", "BAT"]
graph["BAR"] = ["BAT"]
graph["MAT"] = ["BAT"]

def findWay(name):
    find_queue = deque()
    find_queue += graph[name]
    edgeCount = {}
    edgeCount[name] = 0
    beforeTag = {}
    visited = []
    for nextWord in graph[name]:
        edgeCount[nextWord] = edgeCount[name] + 1
        beforeTag[nextWord] = name
        visited.append(nextWord)
    while find_queue:
        word = find_queue.popleft()
        if is_word(word):
            print("Found BAT")
            return edgeCount[word]
        else:
            print("NOT YET LEACHED BAT. CURRENT: " + word)
            visited.append(word)
            for nextWord in graph[word]:
                if not nextWord in visited:
                    edgeCount[nextWord] = edgeCount[word] + 1
                    beforeTag[nextWord] = word
                    visited.append(nextWord)
                find_queue += graph[word]
    return False

def is_word(name):
    return name == "BAT"

print(findWay("MAT"))