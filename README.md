# ระบบตรวจสอบการใช้พลังงานไฟฟ้าด้วย IoT

เว็บแอปพลิเคชันที่พัฒนาโดยใช้ Django framework เพื่อแสดงผลการใช้พลังงานไฟฟ้า ที่วัดค่าจากเซ็นเซอร์วัดกระแสไฟฟ้า PZEM-004T 


# ขั้นตอนการติดตั้ง
0. ติดตั้ง Python และ Pipenv ให้เรียบร้อย

1.  ดาวน์โหลดโปรเจ็คลงเครื่อง
2. เปิดโฟลเดอร์โปรเจ็คใน VSCode โดยตรง หรือเรียกใช้คำสั่งใน terminal
```bash
code .
```
3.  แก้ไขการตั้งค่าส่วน Database ในไฟล์ hometer_prj/settings.py ในสอดคล้องกับข้อมูลของคุณ แล้วบันทึกไฟล์

4. เปิด VSCode terminal
5. Activate pipenv environment และติดตั้ง Packages ของโปรเจ็ค
```bash
pipenv install

pipenv shell

pip install -r requirements.txt
```
6. Database migrations
```bash
python manage.py migrate
```
7. สร้าง Super User (ถ้าต้องการ)
```bash
python manage.py createsuperuser
```
8. เรียกใช้เว็บโปรเจ็ค
```bash
python manage.py runserver
``` 
    
    

## เครดิต
โปรเจ็คระบบตรวจสอบการใช้พลังงานไฟฟ้าด้วย IoT เป็นผลงานในรายวิชาโครงงานพิเศษ 2 
ของ**นางสาวสุจารี ทิพย์กล่อม** รหัสนักศึกษา 6209610341 
นักศึกษามหาวิทยาลัยธรรมศาสตร์ คณะวิทยาศาสตร์และเทคโนโลยี สาขาวิทยาการคอมพิวเตอร์

