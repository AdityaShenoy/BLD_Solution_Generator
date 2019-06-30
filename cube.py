from face import Face


class Cube:

    def F(self, slice_no=1):
        n = self.size
        if slice_no == 1:
            self.front.clock_wise()
        elif slice_no == n:
            self.back.anti_clock_wise()
        temp = self.top[(n-slice_no)*n:(n+1-slice_no)*n]
        self.top[(n-slice_no)*n:(n+1-slice_no) *
                 n] = self.left[(n**2)-slice_no::-n]
        self.left[(n**2)-slice_no::-n] = self.down[(n-slice_no)
                                                   * n+(n-1):(n-slice_no-1)*n+(n-1):-1]
        self.down[(n-slice_no)*n+(n-1):(n-slice_no-1)*n+(n-1):-1] = self.right[n - slice_no::n]
        self.top[n - slice_no::n] = temp
        return self

    def R(self, slice_no=1):
        n = self.size
        if slice_no == 1:
            self.right.clock_wise()
        elif slice_no == n:
            self.left.anti_clock_wise()
        temp = self.front[n - slice_no::n]
        self.front[n - slice_no::n] = self.down[n - slice_no::n]
        self.down[n - slice_no::n] = self.back[(n-1)*n::-n]
        self.back[(n-1)*n::-n] = self.top[n - slice_no::n]
        self.top[n - slice_no::n] = temp
        return self

    def R_(self, slice_no=1):
        n = self.size
        if slice_no == 1:
            self.right.anti_clock_wise()
        elif slice_no == n:
            self.left.clock_wise()
        temp = self.top[n - slice_no::n]
        self.top[n - slice_no::n] = self.back[(n-1)*n::-n]
        self.back[(n-1)*n::-n] = self.down[n - slice_no::n]
        self.down[n - slice_no::n] = self.front[n - slice_no::n]
        self.front[n - slice_no::n] = temp
        return self

    def R2(self, slice_no=1):
        n = self.size
        if slice_no == 1:
            self.right.clock_wise().clock_wise()
        elif slice_no == n:
            self.left.clock_wise().clock_wise()
        temp = self.top[n - slice_no::n]
        self.top[n - slice_no::n] = self.down[n - slice_no::n]
        self.down[n - slice_no::n] = temp
        temp = self.back[(n-1)*n::-n]
        self.back[(n-1)*n::-n] = self.front[n - slice_no::n]
        self.front[n - slice_no::n] = temp
        return self

    def __init__(self, size=3):
        self.size = size
        self.top = Face(face_color='W', size=size)
        self.front = Face(face_color='G', size=size)
        self.right = Face(face_color='R', size=size)
        self.back = Face(face_color='B', size=size)
        self.left = Face(face_color='O', size=size)
        self.down = Face(face_color='Y', size=size)
