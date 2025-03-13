# 練習題 1: 資料型態

# 1. 建立一個變數，並賦值為一個整數。
integer_var = 10

# 2. 建立一個變數，並賦值為一個浮點數。
float_var = 10.5

# 3. 建立一個變數，並賦值為一個字串。
string_var = "Hello, World!"

# 4. 建立一個變數，並賦值為一個布林值。
boolean_var = True

# 5. 建立一個列表，包含三個不同的資料型態。
list_var = [integer_var, float_var, string_var]

# 6. 建立一個固定列表，包含三個不同的資料型態。
tuple_var = (integer_var, float_var, string_var)

# 7. 建立一個集合，包含三個不同的資料型態。
set_var = {integer_var, float_var, string_var}

# 8. 建立一個字典，包含三個鍵值對，每個鍵值對的值為不同的資料型態。
dict_var = {
    "integer": integer_var,
    "float": float_var,
    "string": string_var
}

# 練習題 2: 變數宣告與使用

# 1. 宣告一個變數，並賦值為你的名字。
name = "Martin"

# 2. 宣告一個變數，並賦值為你的年齡。
age = 25

# 3. 宣告一個變數，並賦值為一個布林值，表示你是否喜歡Python。
likes_python = True

# 4. 使用上述變數，打印出一個句子，例如：「你好，我叫[名字]，我今年[年齡]歲。我[喜歡/不喜歡]Python。」
print(f"你好，我叫{name}，我今年{age}歲。我{'喜歡' if likes_python else '不喜歡'}Python。")
