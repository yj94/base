import base64
import gzip

# 读取原始图片文件并进行 base64 编码
with open('sound.ico', 'rb') as f:
    original_data = f.read()

original_base16 = base64.b16encode(original_data)

# 对 base16 编码后的数据进行 gzip 压缩，并得到压缩后的 base16 编码
compressed_data = gzip.compress(original_data)
compressed_base16 = base64.b16encode(compressed_data)

# 计算原始图片数据的 base16 编码的字节大小
original_size = len(original_base16)
print(original_base16)
print(f"原始图片数据的 base16 编码的字节大小为：{original_size} 字节\n")

# 计算压缩后的 base16 编码的字节大小
compressed_size = len(base64.b16decode(compressed_base16))
print(compressed_base16)
print(f"压缩后的 base16 编码的字节大小为：{compressed_size} 字节\n")

# 将压缩后的 base16 编码进行解压缩，并解码成原始图片数据
decompressed_data = gzip.decompress(base64.b16decode(compressed_base16))
decompressed_base16 = base64.b16encode(decompressed_data)

# 将原始图片数据和解压缩后的图片数据进行比较
print((original_data == decompressed_data))

with open('sound_de_b16_gzip.ico', 'wb') as ff:
    ff.write(decompressed_data)