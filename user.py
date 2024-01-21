
import requests



def write_response(response, type):
    f = open("response_" + type + ".txt", "w")
    f.write(response.text)
    f.close()
    

def post_file(url, file_path, user):
    files = {'file': (file_path, open(file_path, 'rb'))}
    data = {'user': user}
    response = requests.post(url, data=data, files=files)
    write_response(response, 'upload')
    return response


def get_file(url, file_path, user):
    data = {'file': file_path,
            'user': user}
    response = requests.get(url, data=data)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    write_response(response, 'download')
    return response


if __name__ == "__main__":
    url = 'http://192.168.0.169:5000/'
    file_path = "./my_file.txt"
    user = 'jhon_doe'
    # post_file(url + 'upload', file_path, user)
    get_file(url + 'download', file_path, user)
    print('ran')

