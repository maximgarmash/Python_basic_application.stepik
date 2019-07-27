file_input = "input.txt"

with open(file_input, "r") as f_in, open("output.txt", "w") as f_out:
    con_in_lst = f_in.read().splitlines() #[-1:-len(f_in.readlines())]
    for i in range(len(con_in_lst)-1, -1, -1):
        f_out.write(con_in_lst[i]+"\n")


    # f_out.write(con_lst)