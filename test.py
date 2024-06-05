import requests

cookie = 'REC_T_ID=23efa179-2314-11ef-912e-6ef10eea5593; SPC_EC=.S1l0U0FlcFM5c2k0ekhqTkU0zvkSgjtkIQs3mFgJFcuN/GIoIrADfPsv2ezqYLP+0ficcNj9Ll1qX+m+WHoufFnnPKRHPWAReeEFnp0x9Zq9bP2MAEPKn9El/zpimh0ptxm1Xm3xTApBXxcyteJMiKMs6vsKQhQwPPhuGXi5Im8X2eJTCS1dQDmJ2HGqHG+9o6yFXgOwEVKqxslc++JHLA==; SPC_F=tduKPEgeehuoGW1xZ2OfSoA2TsOHniHE; SPC_R_T_ID=YouX0GpkR+2itWAjmX9hCguVGit+3zjEHllnOW6l7tOsCGW6eFOwEdhOCPNz8AZRnwaeL1qk83K4NWEZ71AAN0cAV2JzH8PEkv3D2lstXNo9Tt+qZBdBmbR6hls3tN/c95+W5uJxY/xlPC3Yrtp0KWQyGordnutcq7FsuPgh7P4=; SPC_R_T_IV=aXhTajNpUGg2WDltZ2QzVQ==; SPC_SI=zE4vZgAAAABGOXlUd0FsbkTviAUAAAAAaGNiMmozVTA=; SPC_ST=.S1l0U0FlcFM5c2k0ekhqTkU0zvkSgjtkIQs3mFgJFcuN/GIoIrADfPsv2ezqYLP+0ficcNj9Ll1qX+m+WHoufFnnPKRHPWAReeEFnp0x9Zq9bP2MAEPKn9El/zpimh0ptxm1Xm3xTApBXxcyteJMiKMs6vsKQhQwPPhuGXi5Im8X2eJTCS1dQDmJ2HGqHG+9o6yFXgOwEVKqxslc++JHLA==; SPC_T_ID=YouX0GpkR+2itWAjmX9hCguVGit+3zjEHllnOW6l7tOsCGW6eFOwEdhOCPNz8AZRnwaeL1qk83K4NWEZ71AAN0cAV2JzH8PEkv3D2lstXNo9Tt+qZBdBmbR6hls3tN/c95+W5uJxY/xlPC3Yrtp0KWQyGordnutcq7FsuPgh7P4=; SPC_T_IV=aXhTajNpUGg2WDltZ2QzVQ==; SPC_SEC_SI=v1-UHE3dW5qc1Z0YXViT3RYT6x4o0NjVSgUSjHo1fAv/4VUlMd5KJOOUGQ+H/dA0PCwbeO/Ae/qXVhK/dtga3sOwQuGDk6Q8kirMJaYtzUNQ4s='

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8',
    'af-ac-enc-dat': 'be7b487fe7d9a788',
    'af-ac-enc-sz-token': '',
    'content-type': 'application/json',
    'cookie': cookie,
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://shopee.co.id/user/account/profile',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'x-api-source': 'pc',
    'x-csrftoken': 'TMheiBXOHheQ8TI4DLND4h69yxUCxx7F',
    'x-requested-with': 'XMLHttpRequest',
    'x-sap-ri': 'b01c606612b4baf3a0ebf439030187914156458055a18ebe3f90',
    'x-sap-sec': 'EUcfrdfLHtO0EtO0ehO+EtB0ehO0EtB0EtOLEtO08tE0E1BLEtO7EtO0QTjFjLW0EtPSELO06tE0E8lM6fEBd7x7rV8Fe9ZeUmNcfxlE6JAFjd2MsQCEftQQmx4MLj8c3TJKiol0fQyHo7KtQBx1La38D08DjbCiiYBU39aLTffhnSUM9S54ljzmIteanzv4jdPXw3zjUi+q/XxblGqfOx4SPcN7hM49ZDTAP8qnzuxx/Vl6XkXv+rr2s573D01DzcPa283kSRIJ32JB2YFfpt4mnblL1WvgLARx3lKJWNxK+JoiGHiZzCxJjQpishZdlGBX3xdScMWX5UiazTFO77fLDV0WNXgHce+7EdjAFt78yGLorzXpeRzT2gtgPFqV+z1bFfIZTtJS31zXglFxORk519oF95GOvN7Zl90yVCKLCgwfyQyOc62w6SMb5Dl3yPw04Iqp9HJ6zKFdm4KJJw1qIH9dh9uCBAVgipJM2zt03Bd6yrXlIA8A+EfmB0xe+V+xek2klOFQ5kUas625eXnkVsfzaDRGxpkU3eM5YyBq6dLeqHHY/JOAXWdlLQHVaFKFkMdg/ZLOEMPbIxxLA4BY/UDh7Y3OJmBSted2oQifX6MR5FkCA4BXCjkj59BRIK/q+DyUalwHCRql23sxD5NJg0VuZw2kWWW0L25NjeV2ihDCrC9JJhNFTmrLkpzWk/nGcDZaz+C5jbbG8CDbNRDhKNzzlNQSgrKtTPPcuH9C0EVOPQdk7Z/WZFOy0R6ls3Fo8YCts0OIEBXQ1M2hYu0m+srKhyxgu29S1qlKG7VSQtn34nLDQPvFv1m3cMqYbfc7LiX/qSgLExBIQtpITlZI53z+aaX7DufQgD/ye50Utbz4lYqmp04vYbbF/V33xg6qSGLtXjPp7JfF8A/bD6XtnI3suwzl30m/iptiQaEWNMg7x1ryD7cJVw2XsCW7nAWa25B35dkARRJUiO13cJAptmYbLCALgScE+K+sQ5qh4nYGISgnnJ0Jpe07gi2aosPC5oWabCalLQ3Ix8VLHOSf+CItCC2GlJiWInOasbpylKHFUe1iuo66AY3UsIQrOAkjEZQebKR3h4xKDqWDV8KNaVz/Ey4hoeeCq6r350wPAqdmhZ40RyLZQMlI4S4W4ic2Q3MBaqT5PB2Xz4nOd6UxgKYfB7X7DufQgD/ye50Utbz4lYn+EtO0cqDnOo8GkbB0EtO0bTbFjLW0EtO4EtO0htO0EtjQ+JjvUkuE+5u8rgCDMVWJN6s7StO0EVcaQHeGOoWnEtO0EtW0HtO+EtB0StO0EtW0EtO4EtO0htO0EWvB2T42gNWJ7IP9foZB85x21PNIeLO0Eq8GQYEUcqI0',
    'x-shopee-language': 'id',
    'x-sz-sdk-version': '1.9.1',
}

response = requests.get('https://shopee.co.id/api/v4/account/get_profile', headers=headers).json()
print(response)