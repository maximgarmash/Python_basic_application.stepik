from exception import BadName as bad, greet as exc_greet
import exception as ex

print(ex)
print(bad)
def greet():
    print("Greetings!")

greet()
print(exc_greet("Student"))
