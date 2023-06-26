## 该项目使用Python 将图片转为为base编码，后再gzip压缩得到的编码。使得无介质(除HID设备外)传输二进制数据

### Q:为什么每个base编码后的内容长度不一样，但gzip后的内容长度一样?
*** 
```
当使用 gzip 进行数据压缩时，压缩后的数据大小受到多个因素的影响，包括原始数据的特点、压缩算法的实现、以及所使用的编码方式等。
对于原始数据的特点而言，如果原始数据中存在大量重复的内容，gzip 压缩算法可以利用这些重复的内容来实现更好的压缩效果。例如，对于含有大量文本重复的数据（如文本文件），gzip 压缩算法通常可以实现较高的压缩比。相反，如果原始数据中的内容非常随机且没有重复，压缩后的数据大小可能与原始数据大小相差不大。
对于压缩算法的实现而言，不同的 gzip 实现可能会使用不同的压缩算法和参数，从而产生不同的压缩效果。例如，某些实现可能会使用更高级的算法或采用更紧凑的数据结构表示压缩后的数据，从而实现更好的压缩效果。
对于所使用的编码方式而言，Base64、Base32 和 Base16 这些编码方式本身并不会对数据进行压缩，它们只是将二进制数据转换为 ASCII 字符，从而方便在文本格式中传输和存储。因此，使用这些编码方式后，压缩后的数据大小可能会与原始数据大小相差不大。但是，如果在压缩之前对数据进行了一些处理（例如，进行了一些数据清理或转换操作），那么压缩后的数据大小可能会发生变化。
```
#### 综上所述，压缩后的数据大小受到多个因素的影响，需要根据实际情况选择合适的压缩算法和编码方式以实现最优效果。
```
编码后的字符串长度比:
b64≈133%
b32≈160%
b16≈200%
```
### 对于其他二进制文件的编码，我推荐采用与其适用的算法压缩后使用
