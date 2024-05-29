import requests



def get_random_product(product_id):
    try:
        url = f'https://api.freeapi.app/api/v1/public/randomproducts/{product_id}'
        response = requests.get(url)
        # print(response.status_code)
        # print(type(response))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    
def main():
    product_id = int(input("Enter the product id: "))
    product = get_random_product(product_id)
    product_data = product['data']
    print('\nProduct Details\n' + '-'*15 + '\n')
    print(f"Name: {product_data['title']}")
    print(f"Description: {product_data['description']}")
    print(f"Price: {product_data['price']}")
    print(f"Rating: {product_data['rating']}")
    print('\n' + '-'*15 + '\n')
    print(f'status: {product['message']}')


if __name__ == '__main__':
    main()