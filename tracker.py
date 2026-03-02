import requests

def check_price():
    url = "https://www.flipkart.com/api/v4/cart/view"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0',
        'X-Pincode-Id': '382330',
        'Accept': 'application/json'
    }
    
    try:
        r = requests.get(url, headers=headers, timeout=20)
        data = r.json()
        price = data['state']['cartData']['cartSummary']['totalAmount']['value']
        print(f"Current Price: {price}")
        
        if price <= 650:
            msg = f"🔥 TARGET HIT! Ahmedabad Price: ₹{price}"
            requests.post("https://api.telegram.org/bot8654556045:AAFC5hILC8gCcXZy3uEJ8OIkOQWNTxt5zEs/sendMessage", 
                          data={"chat_id": "7303588409", "text": msg})
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_price()
