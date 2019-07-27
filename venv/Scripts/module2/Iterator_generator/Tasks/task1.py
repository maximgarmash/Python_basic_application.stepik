
class multifilter:
    def judge_any(self): # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if self.pos >= 1:
            return True
        else:
            return False

    def judge_half(self): # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if self.pos >= self.neg:
            return True
        else:
            return False

    def judge_all(self): # допускает элемент, если его допускают все функции (neg == 0)
        if self.neg == 0:
            return True
        else:
            return False

    def filter_iterable(self):
        self.new_iterable = []
        for i in self.iterable:
            self.pos, self.neg = 0, 0
            for func in self.funcs:
                if i in filter(func, self.iterable):
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self):
                self.new_iterable.append(i)
        return self.new_iterable

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.judge, self.iterable, self.funcs = judge, iterable, funcs
        self.i, self.new_list = 0, self.filter_iterable()

    def __next__(self):
        if self.i < len(self.new_list):
            self.i += 1
            return self.new_list[self.i-1]
        else:
            raise StopIteration

    def __iter__(self):
        return self

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 4 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)]
print(a)
print()

lst = multifilter(a, mul2, mul3, mul5)
# print(lst.new_list)
print(list(lst))

lst = multifilter(a, mul2, judge=multifilter.judge_half)
print(list(lst))

lst = multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)
print(list(lst))