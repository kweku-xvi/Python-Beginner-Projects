import urllib.request as urllib

def main(url):
    print("Checking connectivivty: ")

    response = urllib.urlopen(url)

    print(f'Connected to {url} successfully')
    print(f'The response was {response.getcode()}')


print('This is a site connectivity checker program: ')
input_url = input('Input the URL of the site you want to check: ')
main(input_url)