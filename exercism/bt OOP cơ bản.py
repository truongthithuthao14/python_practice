import math
class vector:
    def __init__(self, *toa_do):
        self.toa_do =list(toa_do)
    def __repr__(self):
        return f"= Vector({self.toa_do})"
    def __getitem__(self, index):
        return self.toa_do[index]
    def __len__(self):
        return len(self.toa_do)
    '''Sd dụng zip(vector a, vector b,..) khi +,-,*,/ các vector or matrix vs nhau-ko giới hạn số lượng, zip sẽ gom lại thành cặp (xa, xb)...'''

    def __add__(self, other):
        return vector([a+b for a,b in zip(self.toa_do, other.toa_do)])
    #return cong_vec -> đang trả về list chứ ko phải object của class vector nữa

    def __sub__(self, other):
        return vector([a-b for a,b in zip(self.toa_do, other.toa_do)])
    def __mul__(self, so): #phép nhân vector với 1 số
        return vector([a*so for a in self.toa_do])


    def dot(self, other):
    #return vector(sum([a*b for a,b in zip(self.toa_do, other.toa_do)])) -> lỗi: trg hợp kq là số mà đặt trong vector()->tp dạng tuple
        return sum(a*b for a,b in zip(self.toa_do, other.toa_do))
  #tính độ lớn vector
    def magnitude(self):
        return math.sqrt(sum(x**2 for x in self.toa_do))
  #tìm vector đơn vị
    def normalize(self):
        do_lon = self.magnitude() #định nghĩa = thêm self.
        return vector([x/do_lon for x in self.toa_do])
    def __eq__(self, other): 
        return self.toa_do == other.toa_do

    '''so sánh 2 vector có = ko thì sd hàm __eq__, so trực típ ko cần len(). Thay vì:
    def sosanh(self, other): 
       return len(self.toa_do) == len(other.toa_do). Ta code:'''

    #so sánh 2 vector có // ko
    def is_parallel(self, other):
        ratios = [a/b for a,b in zip(self.toa_do, other.toa_do)]  #2 vector song song khi tỉ số các tọa độ bằng nhau
        return all(math.isclose(r,ratios[0]) for r in ratios) 

    #so sánh 2 vector có vg góc ko?
    def is_orthogonal(self, other):
        return math.isclose(self.dot(other),0)
v1 = vector(1,2,3)
v2 = vector(4,5,6)
print("a", v1)
print("b", v2)
print(len(v1))
print(v1[1])
print("a+b", v1+v2)
print("a-b", v1-v2)
print("a*2", v1*2)
print("a*b =", v1.dot(v2))
print("căn(1^2+2^2+3^2) =",v1.magnitude())
print("vector đơn vị",v1.normalize())
print(v1 == v2)
print(v1.is_parallel(v2))
print(v1.is_orthogonal(v2))

'''BT2: 
Bạn sẽ tự tay thiết kế một "Mô hình nơ-ron nhân tạo" (Artificial Neuron) - viên gạch cơ bản nhất của mọi hệ thống AI (như ChatGPT hay Midjourney).
🟢 Cấp độ 1: Cơ bản (Luyện tập OOP thuần)
Yêu cầu: Tạo một class tên là Neuron. Hàm __init__ nhận vào 2 tham số: weight (trọng số) và bias (độ lệch) là các số thực (float).
Viết phương thức forward(self, x) thực hiện phép tính toán học cơ bản nhất của AI:
  output = (x * weight) + bias
Tạo một object từ class này với weight = 2.0, bias = 1.0. Thử truyền $x = 3.0$ vào hàm forward xem kết quả có ra đúng bằng $7.0$ không.

🟡 Cấp độ 2: Trung cấp (Ứng dụng __call__ và NumPy)
Bối cảnh: Trong thực tế, dữ liệu đầu vào (x) không phải là 1 số đơn lẻ, mà là một danh sách các số (Vector/Ma trận). 
Lúc này Python thuần chạy rất chậm, ta phải dùng NumPy. 
Yêu cầu: Cài đặt và import thư viện numpy (viết tắt là np).
Nâng cấp class Neuron:__init__ nhận vào một mảng NumPy các trọng số weights (ví dụ: np.array([1.5, 2.0])) và một số bias.
Sử dụng hàm __call__ thay vì forward để có thể gọi model như một hàm số. Bên trong __call__(self, x), 
sử dụng hàm nhân vô hướng của NumPy (np.dot(x, self.weights)) để tính toán:
  output = (x_1 * w_1 + x_2 * w_2) + bias
Chạy thử nghiệm với dữ liệu đầu vào vector.

🔴 Cấp độ 3: Nâng cao (Kế thừa kiểu PyTorch thực thụ)
Bối cảnh: Một mạng Neural lớn được cấu thành từ nhiều Neuron liên kết với nhau. Bạn sẽ đóng vai kỹ sư PyTorch để thiết kế cấu trúc này.
Yêu cầu: Tạo một class cha tên là Layer (đại diện cho một tầng mạng). Class này có hàm __init__ để thiết lập chung và một hàm info() để in ra dòng chữ: 
"Đây là một tầng mạng neural". Tạo class con NeuralLayer kế thừa từ Layer. Trong class con, sử dụng super().__init__() để giữ lại các thuộc tính của cha.
Class con này sẽ quản lý một danh sách gồm 3 đối tượng Neuron (đã làm ở Cấp độ 2). Viết hàm xử lý để khi truyền dữ liệu vào NeuralLayer, 
nó sẽ cho dữ liệu chạy qua cả 3 Neuron và trả ra kết quả cuối cùng.
'''
import numpy as np
class Neuron_c1:
  def __init__(self, weight: float, bias: float):
    self.w = weight
    self.bs = bias
  def forward(self, x: float):
    return (x*self.w) + self.bs
Neuron = Neuron_c1(2.0, 1.0)
print(Neuron.forward(3.0))
print("---------------------------------")
class Neuron_c2:
  def __init__(self, *weights: float, bias: float):
    self.w = np.array(weights)
    self.bs = bias
  def __call__(self, x):
    return np.dot(x, self.w) + self.bs
Neuron_A = Neuron_c2(1.5, 2.0, bias = 2.0)
print(Neuron_A([4.0, 3.5]))
print("---------------------------------")
class Layer:
  #Để Class 1 có thể điều khiển được Class 2 mà không cần biết chi tiết bên trong Class 2 chạy như thế nào, 
  #cả hai class con này phải tuân thủ một "giao kèo" do Class cha đặt ra.
  def __init__(self):
    pass
  def info(self):
    print(f"Đây là 1 tầng mạng neural")

class Neuron_c3(Layer):  #Class Neuron
  def __init__(self, *weights: float, bias: float):
    super().__init__()
    self.w = np.array(weights)
    self.bs = bias
  def __call__(self, x):
    return np.dot(x, self.w) + self.bs

class NeuralLayer(Layer): #class cả tầng mạng, nó như 1 "người quản lý" đưa dl cho class Neuron xử lý và nó sẽ gom hết lại vào 1 list
  def __init__(self):
    super().__init__()
    self.neurons = [] 
  def add_neuron(self, neuron: Neuron_c3): #hàm thêm các object của Nc3 vào list rỗng đã tạo
    self.neurons.append(neuron)
  def __call__(self, x):
    kq = [neuron(x) for neuron in self.neurons] # gọi từng object 'neuron' truyền vào dữ liệu x
    return np.array(kq)
  
Neuron_A = Neuron_c3(1.5, 2.0, bias = 2.0)
Neuron_B = Neuron_c3(1.6, 2.5, bias = 3.0)
Neuron_C = Neuron_c3(1.8, 2.1, bias = 2.8)

#Tạo tầng mạng và gom neuron vào
layer_1 = NeuralLayer() 
layer_1.add_neuron(Neuron_A)
layer_1.add_neuron(Neuron_B)
layer_1.add_neuron(Neuron_C)

#Cho dữ liệu đầu vào đi qua cả tầng mạng
x = [4.0, 3.5]
out_layer = layer_1(x)

layer_1.info()
print("Kết quả đầu ra của Tầng mạng (gồm 3 neuron):", out_layer)

print("---------------------------------")
'''ĐÁNH GIÁ MỨC ĐỘ TƯƠNG ĐỒNG CỦA KHÁCH HÀNG'''
'''🔏 Đề bài: Bạn là nhà nghiên cứu AI cho một sàn thương mại điện tử. 
Bạn có: Một ma trận dữ liệu khách hàng X kích thước (M, N). Trong đó M là số lượng khách hàng (M=1000), N là số lượng đặc trưng (N=5) 
như: số lần mua hàng, số phút lướt app, số tuổi... Một ma trận bộ lọc tiêu chuẩn C kích thước (K, N). Trong đó K là số lượng "Khách hàng hình mẫu lý tưởng" 
mà công ty định nghĩa (K=3).
Nhiệm vụ của bạn: Tính khoảng cách Euclide (Euclidean Distance) giữa từng khách hàng trong X tới từng khách hàng hình mẫu trong C.
'''
import numpy as np
class Hethong_Phantich:
   def info(self):
      print(f"Hệ thống đánh giá mức dộ tương đồng khách hàng")

class Xuly_Dulieu(Hethong_Phantich):
  def __init__(self, X_matrix: np.ndarray, C_matrix: np.ndarray):
    super().__init__()
    self.X = X_matrix
    self.C = C_matrix
  def __call__(self):
    self.X_new = self.X[:, np.newaxis, :]
    hieu_binhphuong = (self.X_new - self.C)**2
    d = np.sqrt(np.sum(hieu_binhphuong, axis = 2))
    return d
 
M, N, K = 1000, 5, 3

np.random.seed(43)
X = np.random.rand(M,N)
C = np.random.rand(K,N)

Du_lieu = Xuly_Dulieu(X, C)
Du_lieu.info()
Matrix_Kq = Du_lieu()

print("Kích thước ma trận kết quả:", Matrix_Kq.shape)
print("Khoảng cách 5 khách đầu tới 3 hình mẫu lí tưởng", Matrix_Kq[:5])
     

   