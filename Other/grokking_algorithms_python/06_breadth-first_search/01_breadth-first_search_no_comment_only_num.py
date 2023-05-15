from collections import deque


def person_is_seller(name):
    return name[-1] == '8'


graph = {}
graph["00"] = ["11", "22", "33"]
graph["22"] = ["22-1", "22-2"]
graph["11"] = ["22-2"]
graph["33"] = ["33-1", "33-8"]
graph["22-1"] = []
graph["22-2"] = []
graph["33-1"] = []
graph["33-8"] = []


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " ==> is end on 8")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False


if __name__ == '__main__':
    search("00")
