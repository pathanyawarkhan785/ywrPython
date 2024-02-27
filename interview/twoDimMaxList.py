# lst = [[1, 2, 433, 13], [5, 6, 78, 32]]
# max = lst[0][0]
# ind = [0, 1]


class twoDimMaxList:
    def twodMaxlist(self, lst, max, ind):
        for i in range(0, len(lst)):
            for j in range(0, len(lst[i])):
                if max < lst[i][j]:
                    max = lst[i][j]
                    ind[0] = i
                    ind[1] = j

        return ind


# maxNum = twoDimMaxList()
# print(maxNum.twodMaxlist(lst, max, ind))
