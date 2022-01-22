# MIT License
# 
# Copyright (c) 2022 Amir Hosein Hasani Roshan

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from time import perf_counter
from random import randint, shuffle


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
                array[mid:mid] = [x]
                len_arr += 1
                return
        if len_arr > low:
            array[low:low] = [x]
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
