import math
from copy import deepcopy
from heapq import heappop, heappush


class AStarManhattanHeuristic:  # The puzzle is solved using Manhattan Heuristic
    def __init__(self):
        pass

    def compute_heuristic(self, boxes):
        self.boxsAxises = {}
        for row in range(len(boxes)):
            for col in range(len(boxes[row])):
                self.boxsAxises[boxes[row][col].val] = boxes[row][col].axis

        sum = 0
        counter = 0
        for row in range(int(math.sqrt(len(self.boxsAxises)))):
            for col in range(int(math.sqrt(len(self.boxsAxises)))):
                rowDifferent = abs(self.boxsAxises[counter][0] - row)
                colDifferent = abs(self.boxsAxises[counter][1] - col)
                sum += rowDifferent + colDifferent
                counter += 1
        return sum


class Solver:
    def __init__(self, table):
        print("going to solve the puzzle")
        self.table = table
        self.AStarHeuristic = AStarManhattanHeuristic()

    def get_box_tup(self, table):
        tup = []
        for row in range(self.table.n):
            for col in range(self.table.n):
                tup.append(table.boxes[row][col].val)
        tup = tuple(tup)
        return tup

    def solve(self):
        newManDistance = self.AStarHeuristic.compute_heuristic(self.table.boxes)

        visited = set([])
        f = [(newManDistance, newManDistance, [], deepcopy(self.table))]

        while len(f) > 0:

            newManDistance, cost, path, table = heappop(f)
            if newManDistance == 0:
                print("Please wait until the puzzle is solved...")
                return path

            tup = self.get_box_tup(table)
            if tup in visited:
                continue
            visited.add(tup)

            for move in ["right", "left", "up", "down"]:
                newBoard = deepcopy(table)
                if newBoard.move(move) and self.get_box_tup(newBoard) not in visited:
                    newManDistance = self.AStarHeuristic.compute_heuristic(newBoard.boxes)
                    heappush(f, [newManDistance, newManDistance, path + [move], deepcopy(newBoard)])
