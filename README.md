I. Trình tự sử dụng

0. run:

    pip3 install -r requirements.txt

1. copy xlsx files into 'input' folder


2. run:

    python3 test-aiml-gen.py


3. get results at 'output' folder


II. LInh tinh

Đây là công cụ chuyển đổi từ text sang aiml, cụ thể:
    - Input: file excel 2 cột và n hàng, mỗi hàng là 1 cặp câu hỏi - câu trả lời bằng tiếng Việt được lưu trong 2 cột cạnh nhau
    - Output: file aiml có tên giống như tên file excel.  

Danh sách các tag để gán cho từ loại:
    https://github.com/undertheseanlp/underthesea/wiki/M%C3%B4-t%E1%BA%A3-d%E1%BB%AF-li%E1%BB%87u-b%C3%A0i-to%C3%A1n-POS-Tag
    
Trong trường hợp này, các tag sau sẽ bị loại bỏ:
    ['C','Cc','CH','E','Fw','FW','I','L','M','P','S','T','X','Z','A']

Để chỉnh sửa danh sách trên, có thể edit file constant.py

Để thay đổi thư mục đầu vào và đầu ra, edit file contstant.py 


Hạn chế:
    - Chưa có kiểm tra tr
