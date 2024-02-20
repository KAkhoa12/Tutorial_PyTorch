import torch
#=========================================================

# Khỏi tạo giá trị rỗng vô hướng
#==== 1 chiều 1 phần tử ====
var_empty_1 = torch.empty(1) 

#==== 2 chiều 3 phần tử ====
var_empty_2 = torch.empty(2,3) 

#==== 3 chiều 3 phần tử ====
var_empty_3 = torch.empty(3,3,3) 

#==== 4 chiều 3 phần tử ====
var_empty_4 = torch.empty(3,3,3,3) 

# print(var_empty_1)
# print(var_empty_2)
# print(var_empty_3)
# print(var_empty_4)


#=========================================================

# Thay đổi và xem kiểu dữ liệu 

var_type = torch.ones(2,2, dtype=torch.int16)

# print(var_type)
# print(var_type.size())

# tạo tensor 
var_tensor_1 = torch.tensor([1,2,3,4,5,6,7])

# print(var_tensor_1)
# print(var_tensor_1.size())

#=========================================================

# Tính toán các phép toán

x_rand = torch.rand(2,3)
y_rand = torch.rand(2,3)

print(x_rand)
print(y_rand)

# Cộng 
print("\n\n===================== cong ======================")
result_sum_normal = x_rand + y_rand
result_sum_torch = torch.add(x_rand,y_rand)
result_sum_torch_variable = y_rand.add_(x_rand)

# print(result_sum_normal)
# print(result_sum_torch)
# print(result_sum_torch_variable)

#Trừ
print("\n\n===================== Tru ======================")
result_minus_normal = x_rand - y_rand
result_minus_torch = torch.sub(x_rand,y_rand)
result_minus_torch_variable = y_rand.sub_(x_rand)

# print(result_minus_normal)
# print(result_minus_torch)
# print(result_minus_torch_variable)

#Nhân
print("\n\n===================== Nhan ======================")
result_multi_normal = x_rand * y_rand
result_multi_torch = torch.mul(x_rand,y_rand)
result_multi_torch_variable = y_rand.mul_(x_rand)

# print(result_multi_normal)
# print(result_multi_torch)
# print(result_multi_torch_variable)

#Chia
print("\n\n===================== Chia ======================")
result_divi_normal = x_rand / y_rand
result_divi_torch = torch.div(x_rand,y_rand)
result_divi_torch_variable = y_rand.div_(x_rand)

# print(result_divi_normal)
# print(result_divi_torch)
# print(result_divi_torch_variable)


#=========================================================
# Lấy vị trí



