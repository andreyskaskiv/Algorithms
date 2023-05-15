from collections import deque


def person_is_seller(name):
    return name[-1] == 'm'  # Проверяем, заканчивается ли имя на m, если да, то мы нашли продавца манго (для примера)


graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def search(name):
    # Создание новой очереди
    search_queue = deque()
    # Все соседи добавляются в очередь поиска
    search_queue += graph[name]
    # This is how you keep track of which people you've searched before.
    # этот массив используется для отслеживания уже проверенных людей
    searched = set()
    while search_queue:  # Пока очередь не пусто...
        # из очереди извлекается первый человек
        person = search_queue.popleft()
        # Only search this person if you haven't already searched them.
        if person not in searched:  # человек проверяется в том случае, ели он не поверялся ранее
            if person_is_seller(person):  # Проверем, является ли этот человек продавцом манго
                print(person + " is a mango seller!")  # Да, это продовец манго
                return True
            else:
                search_queue += graph[
                    person]  # Нет, не является. Все друзья этого человека добавляются в очередь поиска
                # Marks this person as searched
                searched.add(person)  # помечаем человека как уже проверянного
    return False  # Если выполнение дошло до этой строчки, значит в очереди нет продавцов манго


if __name__ == '__main__':
    search("you")
