import time
import requests
import qrcode

def generateQR():
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'af-ac-enc-dat': 'fd432b06a130a54d',
        'af-ac-enc-sz-token': 'WDR0k3H+6ngaEIaEWVKCxg==|1ZX/8fKnDrlmqaeLxGGUCDyUx0pHeaU6yCEa+qEhRR9gPwLS+dkBw1mL9Dru+bF8LVH8ebC/Sob+gQA=|bmgvdPQEgeTXgtoY|08|3',
        # 'cookie': '__LOCALE__null=ID; _gcl_au=1.1.1886856642.1716886591; csrftoken=sD24cMA70pq3tZqwqqm6a61lwlEU7fSN; _QPWSDCXHZQA=a6cc7352-1ab1-4917-ab9e-d68b7eaf995f; REC7iLP4Q=66a5294a-f58e-435c-93cf-b568d824ca0a; SPC_SEC_SI=v1-TktOcks2Qmdwc081TnR2MsWJVKmCKWNaBqIdIx46BMGJZyTgeq4i7pjFLnTHIoPQiarcxhzwGf12/6SrMncXBHfCbChR+56csEFmGIXpPyA=; SPC_F=s02BOJLcQYna0Ka44oJ7WterGYuIdJtj; REC_T_ID=062969f3-1cd0-11ef-9398-2e97a4c4e08e; SPC_R_T_ID=GqbQSk4jWEu5CMFuBEx1Zzm3Cdj6+ZmUrVQ5kjHW11Xs/glmKYNFnBhjlKoj24TM2IUls6QtfzXb6lP9PjMuqMTanB2TlhZucnvP+JFVj/VjYVXD4iMvPVal3A7AutWSNM5RDoX6337YTPPtOMT0hTzBq4fC7BaDpbgXARx26MM=; SPC_R_T_IV=TERCY09hVjc1b2NVMXpFMw==; SPC_T_ID=GqbQSk4jWEu5CMFuBEx1Zzm3Cdj6+ZmUrVQ5kjHW11Xs/glmKYNFnBhjlKoj24TM2IUls6QtfzXb6lP9PjMuqMTanB2TlhZucnvP+JFVj/VjYVXD4iMvPVal3A7AutWSNM5RDoX6337YTPPtOMT0hTzBq4fC7BaDpbgXARx26MM=; SPC_T_IV=TERCY09hVjc1b2NVMXpFMw==; SPC_SI=xU4vZgAAAABHMkNVR2RxTs4QSwIAAAAAejVTWWZsRnc=; _fbp=fb.2.1716886592025.1179106558; _sapid=462e9e4406b2cb22910ec44603918a20ca59d971f3e5f53fb24974c1; AC_CERT_D=U2FsdGVkX190FtRWt93fpkLJayfdvNx4fz0fnlfix4Ie7LHAWY8FvapfkO5lraBXmfiYT6dPczoUbxMnls9qmkEDWycP6AbMsqRUE8FaC6U72cyQ8EBZcXFkgV3vYmQGClgPmgWbbzcNVNmtLqPxbI5VVHpjsBAVuv9dW7plgNb9URyZKVnrQMv/m37RdeedFR4+CaJBwLBVaQB/K2gW8b8wo+MxZU7T9UFL7n8jRz3B73CjhQ5p7F0pMLE79k3KROo9WEZoWafNqdoebSbzqw==; shopee_webUnique_ccd=WDR0k3H%2B6ngaEIaEWVKCxg%3D%3D%7C1ZX%2F8fKnDrlmqaeLxGGUCDyUx0pHeaU6yCEa%2BqEhRR9gPwLS%2BdkBw1mL9Dru%2BbF8LVH8ebC%2FSob%2BgQA%3D%7CbmgvdPQEgeTXgtoY%7C08%7C3; ds=53c2a70302a077aa3eb129b4ace8e31b; _ga_SW6D8G0HXK=GS1.1.1716886605.1.0.1716886605.60.0.0; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.3.1446239137.1716886605; _gid=GA1.3.704524995.1716886607; _dc_gtm_UA-61904553-8=1',
        'dnt': '1',
        'if-none-match-': '55b03-5673b3bafd16a131d8ce8d30602c178d',
        'priority': 'u=1, i',
        'referer': 'https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2F',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-api-source': 'pc',
        'x-requested-with': 'XMLHttpRequest',
        'x-sap-ri': '0f9c556632e88c9ccd05023b0301cdb4c926768c3421a2d8c8a3',
        'x-sap-sec': 'FBzVySfa5uOYIuOYJpOiIuBYJpOYIuBYIuOGIuOYOuBYITOGIuOaIuOYJDjJw2WYIukoI2OY1uEYIuZBPOOXnM1qFWkMWttOfVw0jtGvEtJJsFEdjdNfFdswol5t0eVAOMBfiUfnCQaO7EMw4gEEAlvnZPP2HUyxVtNicDKQE4W63Tiw9tgRnBFaB0YPPHImFLSGkhZKwEN1hcZuAvuHgM1Fy/gHxlWb81qltx2ezX8MpJhxY9LLFjJLp7EcLA3Q6vhvBnTG1wavwLUTeB5qeaNh6xcwhLnirPUpe5GUqjQP1Re3+dpnT2AlKqlR3G8cnXKDD3xaZiC7KEOvwGDZ6vJoaAWsmThrlUIPuJBjoz/E14o0jukCxrSKD3OfPDJMRtdLfEfwEpZLiJsRC9F5TTfYbVZwTYv9yZxBtSVwsT3p1M/o1c4GHbXc/MJbnuydSqPc2A0J38dbXp18ctI8y+Xrumii3wAvjqWL//je+cwCB3boMaHOjO4o9+uG/g++GiBgbHQ+YNfP0/qjIzbAQPVY4oj4ct0W+Cym+2aKg/l6L5wjcIFLIoK0YIUu/BSjtSg65soKr9L0Cuh7JY363Wwbkc57lhJnJaSKJvrw72ZxYpQ4el04RpuftsPZNENc5T/VWVe1RsU9qdzoFbNRpWnyDcvfsyHhCJLL3nxmkHFimQ/IKTHhKB0PXf1f79fmHroPpSht+/okd6g65JLKLfxOfV/SuBK6OQHh92kPey3agQBz5JBIZJR6RVwcEt4xwpVfkXmAk71Ecpudqji+0clZVfStPh0FN8jsg0QeJ9LXBQE9F7907RPqhHCvazJv/aC+uXOBF81nBKzSFL/sHlMn1qD9+uOOEhlBHTJnXjfF0XJN8/tGU4SU98NCzC9uxhxKtaN/+6zxkcJXElB5M0uu4dL7SUBc/887BNcwDCNeNjPH4mx61oK1p9UYniXIo0usH/udhwAcqAiQN1ue44MCruA/+oqfXr2rBTpplsTIFkcHvUw/s+GpwFo0eorJ1o5h0/cQpy6PSyFfI4rlRh4F1KvEZhn/EsoX4LeTHBUFtkrL/urP81YpcEDw2vSbfkAtPHK5S8+3NNygGN73g09NNpVJ9rBDS2fiJmPGfYIPgu5GOU9HY7kRpwcmJOaByFief2NtBGykCJzkWnWnlyeekA8dEZL9eA8KL7Qv3FmawIknYgteeD/5GfAyG48jwTpYLNT+z3uBizWpvO7HpmtQUkIPf7SNiBy4F/tnMaxmQiWnEkGp5vyU6/1mlw/UwwuBUgEpgAXxboUd6qVswE/8P5Y10/5X4gnSmoS7scP7swWYIuOS/KEr3UM//2OYIurywQbJ4uOYIqfYIuO1IuOYpjVfxDDGIUCwldxETrQdnDYMGkOiIuOY/sDEsKse/KKYIuOY4uOyIuWYJuOiIuOY4uOYIqfYIuO1IuOYaYGNjNj5Q3ZAtDvkDJuQ5KaOaIviIuOYhZe//C3/oUBYIuOY',
        'x-shopee-language': 'id',
        'x-sz-sdk-version': '1.9.1',
    }

    response = requests.get('https://shopee.co.id/api/v2/authentication/gen_qrcode', headers=headers).json()
    # print(response['data'])

    # generate qrcode
    url = 'https://shopee.co.id/universal-link/qrcode-login?id=' + response['data']['qrcode_id']
    qr = qrcode.QRCode()
    qr.add_data(url)
    qr.print_ascii()
    # qrcode_terminal.draw(url, version=1)
    # print(pyqrcode.create(url, error='L', version=27, mode='binary').terminal())

    return response['data']['qrcode_id']

def checkQR(qrid):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'af-ac-enc-dat': '914f7c44043c864e',
        'af-ac-enc-sz-token': 'hBrJRmh7cuIcQuJuINEX1w==|H6AqkUORm/l9gHAA6g0YyOJUCBDHqihoJfacg4ax2IKsBggU1ZFEoKG21yeVUq9ESM/TxAZfvF6za4M=|97awL5TdDrQXCvl2|08|3',
        # 'cookie': '__LOCALE__null=ID; _gcl_au=1.1.1848457066.1717569312; csrftoken=6Yp2qzAIz2ZBLu6D7Wsi27gFeqjmI0tU; _QPWSDCXHZQA=1174aff2-2966-4f2a-b635-e3c301471735; REC7iLP4Q=24602edd-a20b-48c1-9cde-a8bef33870f9; SPC_T_IV=WHRFcVd5Zm40UW52ZmJUWA==; SPC_F=pI9xEUOAJ6CA7rpz2f9PolgM73VEXSZ1; REC_T_ID=a459e5e3-2305-11ef-bd3c-328b75ff8b40; SPC_R_T_ID=D1OuOSGNqloAQptcQdYI3riaIxGxYeN/UeuodyjFKrELagHXOs3UicLQzK4C2FZT1NN8JG9/tnu8Yu63EknFXjtUUUTh4ACmC1t6iXcRFYXXrwBgD0NPgUmAaVuAI7C1xRdVxPOnKP/jZwENMR68vgnP5r6vLpKjqDCAkIj0Oew=; SPC_R_T_IV=WHRFcVd5Zm40UW52ZmJUWA==; SPC_T_ID=D1OuOSGNqloAQptcQdYI3riaIxGxYeN/UeuodyjFKrELagHXOs3UicLQzK4C2FZT1NN8JG9/tnu8Yu63EknFXjtUUUTh4ACmC1t6iXcRFYXXrwBgD0NPgUmAaVuAI7C1xRdVxPOnKP/jZwENMR68vgnP5r6vLpKjqDCAkIj0Oew=; SPC_SI=x04vZgAAAAB1VFdMR0xybRu6TwUAAAAATWdrNDBURmw=; SPC_SEC_SI=v1-QU90eEtrTERoOUtacVBxTAstAz8iOTwPym2bDU92dv5DQ1SA0//gUglIjxuHOV6glMANYsIQx4OWQv6iNAg7Eav0uqmW5AO93AIkaQhHz14=; _fbp=fb.2.1717569314146.38036327470310771; _sapid=dbec2268f9eb420e0ccc786a174385a0657b6e79458bf2e64bf728ee; AC_CERT_D=U2FsdGVkX18FQ7mC7o7KnZv/lwF32NA0usNS5wRL/hdOcIYKgHExCYJcTpmwiP14wtCU178GYnyI+TavZbFiRDEYR1W0Q5nBrDHfR7E472wcNODbFnK5fehBqHMnsniZgcTmjQpWg84juphhqp9g/OUVzG8eeK/r+UrmiLhbutqbsQrebq4WZhtJTyJa0TnOV+uPVPn8XrBw13dhszwI7VfdWuig2pTsseRaSvfHFP5oz/wGyURBbL1vUWMGtIguEBbMWvbPQ73fiXbpznBcQQ==; shopee_webUnique_ccd=hBrJRmh7cuIcQuJuINEX1w%3D%3D%7CH6AqkUORm%2Fl9gHAA6g0YyOJUCBDHqihoJfacg4ax2IKsBggU1ZFEoKG21yeVUq9ESM%2FTxAZfvF6za4M%3D%7C97awL5TdDrQXCvl2%7C08%7C3; ds=8a219bdf6a9cd63939a88a31e400f19c; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.3.313986515.1717569327; _gid=GA1.3.829926056.1717569329; _dc_gtm_UA-61904553-8=1; _ga_SW6D8G0HXK=GS1.1.1717569327.1.1.1717569332.55.0.0',
        'dnt': '1',
        'if-none-match-': '55b03-fc6e91faf78b4fb131fe663dfd1474ca',
        'priority': 'u=1, i',
        'referer': 'https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2F',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-api-source': 'pc',
        'x-requested-with': 'XMLHttpRequest',
        'x-sap-ri': '06076066cccd4aedb55c113e03011e9dc514b57a9472cf9917d9',
        'x-sap-sec': 'BmRr3BuOCIwIwIwIYDwEwIuIYDwIwIuIwIw5wIwIJIzIwH25wIwOwIwIxpswIl2IwIG/wlwI6IzIwJIc6NIfBiSbA7otFfe9ibIriQu1gcEdbtLZSUhTeemNzRIlHuUk+ZMJi6vj02RaIIUgShC6/DMs7/AVJ4dYUiBPbJ2De0hG3AONwNgifdD/xpcY0FpD3oOxViXukTptvNzwlbjTFlk/0zMnvVei4PZLmwDuI1bXZaCc7PEC8atQAsxOj9GehWUgyRCMGUUBRvcedQaHMJpvq0RApQdwn/06sJ3SnJIOQLj0cTBlEYsmYbfn/PTT9TERMp1JB9LoCMaRkrBLfIHkhEr5tSImAKUPN4S4t0YlhUIeMxdABLvD7Wg+A8S7mSKwXj1Cw16M8Vmxstt6gLgqh6LdW+C8esJ4paoKj09DYt4ziqS8QGvURCD9bsOV3R6KZRP9E0iD/MSR9ITSGr7BfTUHQ3ojfPYgzqQqUflrgw6LV5NyRFALdKhG7DsD5m9uqZzGoHjvE9//PjZDvJUIRUDiD+1ME4yOWtsjAooMqD2L2yupR50BmDLoUz7j2fTzKeHXfEyNibHhffkJYl/24d0FMofQbyVdi/4BWbNTJ4kGuZJJX7sLbgL9pCoQ8+bGX3tNQhOhfAVj5gMHU5c4iAnQ9UvDvhqJdN9zVzYgG9mIyzbxFDrfju35RB0MA4ouji1DIoVG11fRJUJPwBMqA/0jLVbB8WGy8j6QoNTIi8Bb5SBDmwYvvdUjSPwwUYvATt3nX8dEom93WjMnbXErNSQC4cG5gpLKbLI2XLktuI2wz52ce+KSoLWgoHb34XNSNsw0zosCwQq6I8ewk+1v3vK+vtMYiswez9bqNSkFOBxZOiLg04uE4jZTPr4TuA4z5Wxdfx7s3J84ItPWpZfWzW2Sa3HAOmm1e/Gde3hhaJWAXPQ97eIYoTqheajAd1eX4m5eC8RXYTv0wo44qd7+CHj4YPUgcPkr7UvPL06qiey2SvXCwFth+HybAqctU5k9RTV37Dx2LXro8Lf9EpZhFkjXP6TXc8f4t4hh05o3kMI+dHAOqTYGi1GtyW1nfwFutwiuFvNsFGEFksTOBaS060HPpuSVQAAQDnYjrraaRZ0LqH3ZB20tZHQ53XTRZYALYh/XV87XUUyk2zFZXd/mVqKwyeVLQj1AshpQaD6/tubaChXC2HnbIw7xJNdmH/4CMrQXd6EtuTVPadBww6eVQDMAHp8Ns/EZu14d2qII++IgxXW8HzONj6eTBIyK+gYtZASevOJXuD2IwIwzy5wl95Vy9IwIwICsIwIwGIwIwJpIwIwBwIwIAZMHBozjZu8muwF7TXGVBIStxNREwIwIyzjxy+bgmkjIwIwIGIwswI2IYIwEwIwIGIwIwJpIwIwBwIwIRk8r0kl3CVdtrIGO5IVU/cngRAbEwIwIyAXlzA2zy5bIwIwI',
        'x-shopee-language': 'id',
        'x-sz-sdk-version': '1.9.1',
    }

    params = {
        'qrcode_id': qrid,
    }

    response = requests.get('https://shopee.co.id/api/v2/authentication/qrcode_status?qrcode_id', headers=headers, params=params).json()
    # print(response)
    # {
    #     "bff_meta": null,
    #     "error": 0,
    #     "error_msg": null,
    #     "data": {
    #         "status": "NEW",
    #         "qrcode_token": ""
    #     }
    # }

    # {
    #     "bff_meta": null,
    #     "error": 0,
    #     "error_msg": null,
    #     "data": {
    #         "status": "SCANNED",
    #         "qrcode_token": ""
    #     }
    # }

    return response['data']

def loginQR(token):
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8',
        'af-ac-enc-dat': 'ea0d1db45bd917af',
        'af-ac-enc-sz-token': '',
        'content-type': 'application/json',
        # 'cookie': '__LOCALE__null=ID; csrftoken=YYNyNl0QvqQehzcR2uosiDqGuQnj5fQZ; _QPWSDCXHZQA=c431c65a-bcd9-4d57-86e1-1a6dd5c40231; REC7iLP4Q=b21317c0-173d-49b1-87c5-e12191dc1d8e; SPC_F=x31R5R04d3Yq4gsXED295pSmfz6P8J2C; REC_T_ID=0eec6ce0-230f-11ef-9adf-9aaced435c2e; SPC_SI=TE0vZgAAAABwc3JTaHg5WuPafgUAAAAAN2wxOWYzcEg=; SPC_SEC_SI=v1-aGdVd05yRWxOMzBQOWp2UUxN/TIBGvmTZwsiPzPTyk+C8WtCx7c34wjD9kmJ45FAdy8MKJ6dMjVSwmVDp4D+CaEs21xwXdD36+jsw6NS6/I=; _sapid=d37fd0211f1ce647b80ea973e872ab938a6d92fa53a6190a598631b5; SPC_CLIENTID=eDMxUjVSMDRkM1lxezcgbhrokwwtgvda; SPC_U=1053170472; SPC_R_T_ID=fn+WFQTQCe6VzV6+K2WOh9w4Fg9OHompf/KuRkz5x6UMsajSa7rBBfXVzEXNRAijo0FNM4OAp6yY13L34bRjzQ4GTsjMwFws1wHf9czNcNQU4nAwPeutS8hJwiqbgpYDpe4ZH9BBN0QYDSv0nIjg2ZRhd9vLFbsKv74cDR+XWUw=; SPC_R_T_IV=RTB1OEhUTGJDQVZzUGVsZA==; SPC_T_ID=fn+WFQTQCe6VzV6+K2WOh9w4Fg9OHompf/KuRkz5x6UMsajSa7rBBfXVzEXNRAijo0FNM4OAp6yY13L34bRjzQ4GTsjMwFws1wHf9czNcNQU4nAwPeutS8hJwiqbgpYDpe4ZH9BBN0QYDSv0nIjg2ZRhd9vLFbsKv74cDR+XWUw=; SPC_T_IV=RTB1OEhUTGJDQVZzUGVsZA==; SPC_IA=1; SPC_CDS_CHAT=c7e23359-9ef6-4679-9d08-2db64d845407',
        'dnt': '1',
        'origin': 'https://shopee.co.id',
        'priority': 'u=1, i',
        'referer': 'https://shopee.co.id/buyer/login/qr?next=https%3A%2F%2Fshopee.co.id%2F%3Fis_from_login%3Dtrue',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-api-source': 'pc',
        'x-csrftoken': 'YYNyNl0QvqQehzcR2uosiDqGuQnj5fQZ',
        'x-requested-with': 'XMLHttpRequest',
        'x-sap-ri': '4d19606686c71b3ccd28083e030176fb1039f1483792c14f14fb',
        'x-sap-sec': '7OlQakioqW+StW+SnO+4tWkSnO+StWkStW+otW+S7W7Stt9etWNqtB+SnW+StX8id614tW+SCW7StX9etWMxmmaeGnWkZyCPoFdAtI4OAjbSCpcwZVNiH7BFiS3UmU/zLxflRuvA0otIDqVEwPnysI0VRazKwqTxW2yhIkKqm0bVBT7heYZX6QfFJyWIkX/PyHyWRVGoZb+XdKcEMLXMiaY07EsEMZCWEwLfoTFbqTPE4954AhfmqDdgenmjp+wKguG7gjw8fRd/1x+pid13dQNs8z4BMXCGAtx5ttD4r4sd98VJQ2/d9dvFMHkoaesvyuEyyh+8dpD1HXaqWw1H4O52XatnEJpDCxQya3F+BrAKmATfAyst5/m3uKQ5fsSNtVpUMP0Ren1aW30tJHZEJ7/WHLWnYSOQUo0z2Ty/2U43lIj+uCB4QKMWD1+g7qEbyEY/MyTGMM8Mj56t46W3ZcWCAebsNO4E4aChegoiRRuG+T5UACRIiYYSa+Fqlj/ZEfvS7MOBmS8efm+3gWh45dW+LrHsRCy8Q4jT3NF/Y4qHYKkr9vgdDaMPzK64ernCTxRLi27Th5YX6DnNJPjMo9WvEVe3GIT5fuQikPDFV+ea6+NlXg9TW7Bix4aBCKQAPIzTj3z9OZRs/qFlfFuUusrGcAGTIatHXk+0Uwa14TNvxEDd32Wu37NKWxPHPVhcf6iSPvYEzVzy9WNFamSjk7sKC4/wWbvedaS35IZx23/Iu93rUrJVHyvCLkees9LFqTkdUOd0UWxP0Dyi+juv0ADTB9Pp5lp+bKOrgFwQg2VBWExFIDwxjqx+TBi1/lMqQW5ywTseK82zbZeU76eQZCOFeQ2i0c9rEAi7jI4TXXQP6Sv1ckPlm3Dtgqx9Gczjv+13R4tGDjzJJfgIK8htiTdEhWZqt7NTcG+SJGpQleWha8H+FOXIfvfOOvcQdKZmqzaqgeLftXvkamVT5IQw5mOVVYgTe9r+zF/lrDwOzlzfKw7T5qKBso5+dQlUlPVDSd1NjbWgmNRoviPAnwLwSobv7L4ULa8uBYBVvzwXTM8dBy6pLznb3gUuq0f0JX8Fi93GFSUZuRmvhT0XNYs8c01VEz5ofqTmm/gwuGLlTJnygL5jVQDd9ER3kcOPal93c2yYuhAkl0Ln5r148U5SBVkpzDjnh/k/zmy4tW+SAy5VfrozFjSStW+SHVUgdBiStW++tW+SvW+StqbuGJek/eQjAAxgCqbxwomlv0YquW+StToGDjiGgd4ztW+Stv8gd614tW+S1W+St8kStWMbJ+7W9+ipgkYkrZ1ujtsP+n9GZfiStW+xgrrvFjSxDB+StW+4tW9SuW+otWiStW+4tW+S1W+St8kStWNrsIAlfiTcyqaKwaiJk070jxJqifiStW+wAj7aDjrvAW+StWB=',
        'x-shopee-language': 'id',
        'x-sz-sdk-version': '1.9.1',
    }

    json_data = {
        'qrcode_token': token,
        'device_sz_fingerprint': 'DxcBAAAABAAAAIAAAAVOMis6egA9CQFdzhMGC67HaZP2utsVI0ki1SGxBg6RS5om0YvIeDfJqdfiPkloYvavQVVJRmON7PV+gM29SksYD5NPmROdqSkJ8/EbHuJDe9O0nE41GgIhPDPWl3dHwtyUZQlwC3KJt3ElIp0cVdd2eBlD4ZX1lLIQ2WZYb3Rq1md/c+54+i3JtgAAAAYAAAAAAAAAAATA24KIFIROyDl5Z/szAl4ADvD/I+MBNzEB6uB+nd8j2+0UMaTEzGcXM3ca7+olHuM92zB3CiKNI0YAquTkB/z9kS3vXHXeFeUxnNPg4itJ0mez7FFnuSgfJsJ/YrZIU1UR15qMBQ5S+uT0s2tNDkXPkMDLaYKIfzilzRLoajWAXaKoHoO4Ap0ZlFMwqQoc9w8IemhRH7YgxjHSAnMhVDcJVKbG10f13jXZrOWvRqrh3/g+b/LrzYQY8/JGY+r7JCX/M7Wx4U4PUXfDMIX4y5qGszKpS6RkQU+4kItvAzckk0LgBje/sIiO93DNOC8IO3pKX+via5sj/TogaXqPuUqHLACmr/j8pxGCKCskOeAD973AjBaLtatbkKhmICte0CupISJD3VB0GIbBFF4vazgLFrlnZep6Kna2oC531Qv6rnAktlDVCoj7j7Igz1d0kGGe3RI0GrocIVFBjF7B7nBxnJqq/711gtC4oTR3WjWh/YBawSIAPgj6NVbxUST9eTiiU/iKwL6sztUn9AyTdVclhqQ+wnVsmpvFxnSisD/j0hp0+XZxli1tvk6aZbCEg25AGnDHVtSCSvsYQJLyVQblcw0PLDDE8IWvSFzhyic6G7BEwPxLoZl1jR8sm8geG53wRDqQDz4Fw04Bb5Q3oCAqXn82i3OyV4qOarHPqYGpctLRudmJF1tmafK+HNYOwAe3c6C5RXx2AHXw9emL7oblx6f23eoUN5l2Nq8md8DUV3CPcgIjak4J+6a24tiv3FUUtxKcXotum87MgwuvV0cba47bZrBJiShyOCfVcTbo4CXLsXpSrIbLji5RZsxHZrkYmeItXxMXYrWuS0e8T17jeNHy4uTYYJ2pxpGK3A942e5FXTVLnbXj9Vl9sEgmIH3rnq12iVsKkBMqAUyvpe9xCqvLjL9+Bp0EPcoY9o9jNz0I4snIWhfVyN/OjoTeXm2YG6fRGwhYGp5NmOAStlaKerqMekNaBzom1XFA7La4gqPqP7b9/3NjEYMlJtIpjw8em7hxlFvbyJJ64nr4ERsvHOwLyknQ0vWIyqGo9rWOUh3gURAyy8EViSI21K1jDtEbbboM/CPefrBp3xI/G7GiyUxE4EHPF4fogqQ6UaojatWyGwDp3boJ7+yU9yxI2Lf4yzwKGsVlbUaNlBwBpqCwhndjpq+LX1XPOq1tACxgXel+70/NVMms/ORzNTz8GszrpzINjLMhGPE5RCYkZLC3pOUwsq+y0lfxMBBqnyTyC4FyLnDRoQGBFiYdo0vscXoIDKvenDlROLd6sY0w1fGJHErZqh25ThaGM+s+ujzRY7JRGO5lJQPqTnn2uxUTaXJ96qILset93P9B2ek/fnwJio7S03VztcnQyoSBfJ/bJbE1CsBJg3Kun8Uoth9pkuGlIPSdCd1rxZu+KawwYpsOUbZ4MQc0Sy4vxrIswI1M/ZTAZnjHy5zi8juN8EdsftlAUdSXQ5R6NQqsC4iXVFaU0kFc38g4hRc92GO5Z7gPqAcq1A9jZA5aqnjAwm+7hBAH/bTQTQC4upERGNBuRKO7QrzeW9n3CJhdWJJFig2xpWx1jTbuS1rDTYQZYy03yXbzH5uKa20qaBiko2THSgwqwA==||MTAwMDA=',
        'client_identifier': {
            'security_device_fingerprint': 'DxcBAAAABAAAAIAAAAVOMis6egA9CQFdzhMGC67HaZP2utsVI0ki1SGxBg6RS5om0YvIeDfJqdfiPkloYvavQVVJRmON7PV+gM29SksYD5NPmROdqSkJ8/EbHuJDe9O0nE41GgIhPDPWl3dHwtyUZQlwC3KJt3ElIp0cVdd2eBlD4ZX1lLIQ2WZYb3Rq1md/c+54+i3JtgAAAAYAAAAAAAAAAATA24KIFIROyDl5Z/szAl4ADvD/I+MBNzEB6uB+nd8j2+0UMaTEzGcXM3ca7+olHuM92zB3CiKNI0YAquTkB/z9kS3vXHXeFeUxnNPg4itJ0mez7FFnuSgfJsJ/YrZIU1UR15qMBQ5S+uT0s2tNDkXPkMDLaYKIfzilzRLoajWAXaKoHoO4Ap0ZlFMwqQoc9w8IemhRH7YgxjHSAnMhVDcJVKbG10f13jXZrOWvRqrh3/g+b/LrzYQY8/JGY+r7JCX/M7Wx4U4PUXfDMIX4y5qGszKpS6RkQU+4kItvAzckk0LgBje/sIiO93DNOC8IO3pKX+via5sj/TogaXqPuUqHLACmr/j8pxGCKCskOeAD973AjBaLtatbkKhmICte0CupISJD3VB0GIbBFF4vazgLFrlnZep6Kna2oC531Qv6rnAktlDVCoj7j7Igz1d0kGGe3RI0GrocIVFBjF7B7nBxnJqq/711gtC4oTR3WjWh/YBawSIAPgj6NVbxUST9eTiiU/iKwL6sztUn9AyTdVclhqQ+wnVsmpvFxnSisD/j0hp0+XZxli1tvk6aZbCEg25AGnDHVtSCSvsYQJLyVQblcw0PLDDE8IWvSFzhyic6G7BEwPxLoZl1jR8sm8geG53wRDqQDz4Fw04Bb5Q3oCAqXn82i3OyV4qOarHPqYGpctLRudmJF1tmafK+HNYOwAe3c6C5RXx2AHXw9emL7oblx6f23eoUN5l2Nq8md8DUV3CPcgIjak4J+6a24tiv3FUUtxKcXotum87MgwuvV0cba47bZrBJiShyOCfVcTbo4CXLsXpSrIbLji5RZsxHZrkYmeItXxMXYrWuS0e8T17jeNHy4uTYYJ2pxpGK3A942e5FXTVLnbXj9Vl9sEgmIH3rnq12iVsKkBMqAUyvpe9xCqvLjL9+Bp0EPcoY9o9jNz0I4snIWhfVyN/OjoTeXm2YG6fRGwhYGp5NmOAStlaKerqMekNaBzom1XFA7La4gqPqP7b9/3NjEYMlJtIpjw8em7hxlFvbyJJ64nr4ERsvHOwLyknQ0vWIyqGo9rWOUh3gURAyy8EViSI21K1jDtEbbboM/CPefrBp3xI/G7GiyUxE4EHPF4fogqQ6UaojatWyGwDp3boJ7+yU9yxI2Lf4yzwKGsVlbUaNlBwBpqCwhndjpq+LX1XPOq1tACxgXel+70/NVMms/ORzNTz8GszrpzINjLMhGPE5RCYkZLC3pOUwsq+y0lfxMBBqnyTyC4FyLnDRoQGBFiYdo0vscXoIDKvenDlROLd6sY0w1fGJHErZqh25ThaGM+s+ujzRY7JRGO5lJQPqTnn2uxUTaXJ96qILset93P9B2ek/fnwJio7S03VztcnQyoSBfJ/bJbE1CsBJg3Kun8Uoth9pkuGlIPSdCd1rxZu+KawwYpsOUbZ4MQc0Sy4vxrIswI1M/ZTAZnjHy5zi8juN8EdsftlAUdSXQ5R6NQqsC4iXVFaU0kFc38g4hRc92GO5Z7gPqAcq1A9jZA5aqnjAwm+7hBAH/bTQTQC4upERGNBuRKO7QrzeW9n3CJhdWJJFig2xpWx1jTbuS1rDTYQZYy03yXbzH5uKa20qaBiko2THSgwqwA==||MTAwMDA=',
        },
    }

    response = requests.post('https://shopee.co.id/api/v2/authentication/qrcode_login', headers=headers, json=json_data)
    # print(response.json())
    # print(response.cookies.get_dict())
    # print(response.headers['set-cookie'])

    saveCookies(response.cookies.get_dict())

def getProfile(cookies_str):
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8',
        'af-ac-enc-dat': 'be7b487fe7d9a788',
        'af-ac-enc-sz-token': '',
        'content-type': 'application/json',
        'cookie': cookies_str,
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
    # print(response)
    return response['data']['user_profile']['username']

def saveCookies(cookies):
    cookies_str = '; '.join(key + "=" + str(val) for key, val in cookies.items())
    # print(cookies_str)

    # get username
    username = getProfile(cookies_str)

    name = f'cookie-{username}.txt'
    f = open(name, 'w')
    f.write(cookies_str)
    f.close()

    print(f'cookie saved [{name}]')

# saveCookies({'REC_T_ID': 'd562498d-2310-11ef-9fed-72ce1bcd0480', 'SPC_EC': '.RGVXTE9jSFphSFpyYUdyaI3qGp2VdBga9EMFLQkxK70+SaUy8+7GmLbh2uRBYI9Sy/PsB1Jl8XXAW2lHOIy3JSjprN1SJkk8QcYGY7tF7Fu/sgvv6MDuwEkkRvLJXQ0tVosrWQn/fTNwVKPxFW4PEedlSvwSJQ2bU128XieC3Q9jIcU/atyuhkhDSy0AsLPKyJshM2cE4YWZQiKpFItLVg==', 'SPC_F': 'PwUA4EfEEGQjg9z31AoWGA7N0wQOziex', 'SPC_R_T_ID': '4WYgrX+IJz2XayjUhyNsTCDUMPt4og9wNS83xdXrUcb0gzy+84/K/LDX4cJCQgcZJIemu5/Glb+F3ngC3sS+tWOfWu7RX7IVh/Bi5u4X5J0wsZG/ocw5Ag7q1/YWLms+dHflYGS+GYSYj1VRV5weVmFhOo1KTUP8/NT+gnkIHoU=', 'SPC_R_T_IV': 'MndURmdlSlB0ak5BWHRKNw==', 'SPC_SI': 'y04vZgAAAAB3ekxPRXBoORSiUAUAAAAAOTFjRlRyZ0o=', 'SPC_ST': '.RGVXTE9jSFphSFpyYUdyaI3qGp2VdBga9EMFLQkxK70+SaUy8+7GmLbh2uRBYI9Sy/PsB1Jl8XXAW2lHOIy3JSjprN1SJkk8QcYGY7tF7Fu/sgvv6MDuwEkkRvLJXQ0tVosrWQn/fTNwVKPxFW4PEedlSvwSJQ2bU128XieC3Q9jIcU/atyuhkhDSy0AsLPKyJshM2cE4YWZQiKpFItLVg==', 'SPC_T_ID': '4WYgrX+IJz2XayjUhyNsTCDUMPt4og9wNS83xdXrUcb0gzy+84/K/LDX4cJCQgcZJIemu5/Glb+F3ngC3sS+tWOfWu7RX7IVh/Bi5u4X5J0wsZG/ocw5Ag7q1/YWLms+dHflYGS+GYSYj1VRV5weVmFhOo1KTUP8/NT+gnkIHoU=', 'SPC_T_IV': 'MndURmdlSlB0ak5BWHRKNw==', 'SPC_SEC_SI': 'v1-MlpvOEJJcU56OXhCTGJGVctlk2gQ37albplyYhhAz8Wbz6I52pfEN5Bw+VF46lbxsZExYej+GHLaIQ8dPQn80hB2VPgG8yQb4ft+PRw+EqA='})
# exit()

def do():
    qrid = generateQR()
    last_status = ''
    # print(qrid)

    while True:

        response = checkQR(qrid)
        current_status = response['status']
        # print(response)

        if current_status != last_status:
            print(f'QR Status: {current_status}')
            last_status = current_status

        if response['status'] == 'CONFIRMED':
            loginQR(response['qrcode_token'])
            print('success login, wait 5 seconds for next qr...')
            time.sleep(5)
            break
        if response['status'] == 'CANCELED':
            print('QR Canceled, try again in 5 seconds...')
            time.sleep(5)
            break
        if response['status'] == 'EXPIRED':
            print('QR Expired, try again in 5 seconds...')
            time.sleep(5)
            break

        time.sleep(2)

while True:
    do()