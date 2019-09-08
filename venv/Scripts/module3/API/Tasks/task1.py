import requests

api_url = "http://numbersapi.com/"

input_file = "dataset_24476_3.txt"
with open(input_file) as in_f, open("output.txt", "w") as out_f:
    for number in in_f.readlines():
        res = requests.get(api_url+number.rstrip()+"/math", params="json")
        data = res.json()
        out_f.write("Interesting\n") if data["found"] else out_f.write("Boring\n")

        # if data["found"]:
        #     out_f.write("Interesting\n")
        # else:
        #     out_f.write("Boring\n")
