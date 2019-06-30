class Face:

    def clock_wise(self):
        a = self.stickers
        n = self.size
        for i in range(n // 2):
            strt, end = i, n - 1 - i
            temp = a[strt*n + strt: strt*n + end]
            a[strt*n + strt: strt*n + end] = a[end*n + strt: strt*n + strt: -n]
            a[end*n + strt: strt*n + strt: -n] = a[end*n + end: end*n + strt: -1]
            a[end*n + end: end*n + strt: -1] = a[strt*n + end: end*n + end: n]
            a[strt*n + end: end*n + end: n] = temp
        self.stickers = a
        return self

    def anti_clock_wise(self):
        a = self.stickers
        n = self.size
        for i in range(n // 2):
            strt, end = i, n - 1 - i
            temp = a[strt*n + end: end*n + end: n]
            a[strt*n + end: end*n + end: n] = a[end*n + end: end*n + strt: -1]
            a[end*n + end: end*n + strt: -1] = a[end*n + strt: strt*n + strt: -n]
            a[end*n + strt: strt*n + strt: -n] = a[strt*n + strt: strt*n + end]
            a[strt*n + strt: strt*n + end] = temp
        self.stickers = a
        return self

    def is_solved(self):
        for i in range(1, self.size ** 2):
            if self.stickers[i] != self.stickers[0]:
                return False
        return True

    def __init__(self, face_color='W', size=3):
        self.size = size
        self.stickers = list(face_color) * size ** 2
        self.stickers = list(map(lambda x: chr(x), range(65, 65 + size ** 2)))
