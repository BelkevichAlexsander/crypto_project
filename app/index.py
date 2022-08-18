import json
import os
import hashlib

blockchain_dir = os.curdir + '/app/blockchain_block/'


def write_block(first_name: str, amount: int, second_name: str):
    """
        function for create blockchain
    """
    last_file = __get_files()[-1]
    hash_prev_block = __get_hash(str(last_file))

    data = {"first_name": first_name,
            "amount": amount,
            "second_name": second_name,
            "hash_block": hash_prev_block}


    with open(blockchain_dir + str(last_file + 1), "w") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def check_hash_block():
    """
        function to check hash in file and create list with results of check
    """
    files = __get_files()
    result = []

    for file in files[1::]:
        h = json.load(open(blockchain_dir + str(file)))['hash_block']

        prev_file = str(file - 1)
        actual_hash = __get_hash(prev_file)

        if h == actual_hash:
            res = "ok!"
        else:
            res = "corrupted!"

        result.append({"Block": prev_file, "result": res})
            
    return result


def __get_hash(filename: str):
    """
        Function for return hash from previos file
    """

    file = open(blockchain_dir + filename, "rb").read()

    return hashlib.md5(file).hexdigest()


def __get_files():
    files = os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])


def main():
    write_block("ivan", 2, "katya")
    print(check_hash_block())


if __name__ == '__main__':
    main()