import base64

# base64编码方便使用

# 通过id检验优惠券是否存在，通过goods查找商品
coupon = {
    'id': '1231',
    'goods': '0001',
}

raw = '/'.join([k+':'+v for k, v in coupon.items()])

raw_64 = base64.urlsafe_b64encode(raw.encode('utf-8'))
c_code = str(raw_64)[2:-1]
print('优惠码:', c_code)
print('解析优惠码:', base64.urlsafe_b64decode(c_code.encode('utf-8')))