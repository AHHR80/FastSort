print('fast sort now')


class FastSort:
    arr = []
    rang = 0
    rang2 = 0
    maximum = 0
    minimum = 0

    def __handel(self, num):
        return self.arr[(num // self.rang) + self.rang2]

    def __fast_sort_(self, num):
        x = (num - self.minimum)
        self.arr[x].append(num)
        return

    def __fast_sort(self, x):
        array = self.__handel(x)
        len_arr = len(array)
        low = 0
        high = len_arr - 1
        while low <= high:
            mid = (high + low) // 2
            if array[mid] < x:
                low = mid + 1
            elif array[mid] > x:
                high = mid - 1
            else:
                array[mid:mid] = [x]  # arr.insert(mid, x)
                len_arr += 1
                return
        if len_arr > low:
            array[low:low] = [x]  # arr.insert(low, x)  # arr.append(x)
        else:
            array.append(x)
        len_arr += 1
        return

    def __setup(self, maxi, mini, length):
        self.minimum = mini
        self.maximum = maxi
        total = abs(self.maximum) + abs(self.minimum)
        re = length // total
        if re != 0:
            self.rang = 1000 // re
            if self.rang != 0:
                self.rang2 = abs(self.minimum // self.rang)
                for i in range((maxi // self.rang) + self.rang2 + 1):
                    self.arr.append([])
                return 1
            self.rang = re // 1000
            for i in range(abs(self.maximum) + abs(self.minimum) + 1):
                self.arr.append([])
            return 0
        elif total > length:
            max_index = length // 1000
            for i in range(max_index + 2):
                self.arr.append([])
            if max_index == 0:
                self.rang = total
            else:
                self.rang = total // max_index
            self.rang2 = abs(self.minimum // self.rang)
            return 1

    def fast_sort(self, li):
        loop = self.__setup(max(li), min(li), len(li))
        if loop == 1:
            for i in li:
                self.__fast_sort(i)
        else:
            for i in li:
                self.__fast_sort_(i)
        arr2 = []
        for ii in self.arr:
            arr2 += ii
        return arr2


if __name__ == '__main__':
    lis = [randint(-1000000, 1000000) for i in range(100000)]
    # shuffle(lis)
    sor = FastSort()
    start = perf_counter()
    z = sor.fast_sort(lis)
    print(perf_counter() - start)
