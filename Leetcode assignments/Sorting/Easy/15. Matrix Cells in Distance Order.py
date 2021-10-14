class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        coordinates = []
        dist = []
        hashmap = defaultdict(list)
        
        for r in range(0,rows):
            for c in range(0,cols):
                coordinates.append([r,c])
                
        for i in coordinates:
            distance = abs(i[0] - rCenter) + abs(i[1] - cCenter)
            dist.append(distance)
            hashmap[distance].append(i)
            
        arr = []
        dist = sorted(list(set(dist)))
        
        for i in dist:
            arr.extend(hashmap[i])

        return arr
