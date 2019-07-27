print('This line is executed')

class EvenLengthMixin:
    def even_length(self):
        return len(self)%2 == 0

class MyList(list, EvenLengthMixin):
    pass


ml = MyList([1, "abc", 4, 17, 3, 8])
ml.sort()
print(ml)