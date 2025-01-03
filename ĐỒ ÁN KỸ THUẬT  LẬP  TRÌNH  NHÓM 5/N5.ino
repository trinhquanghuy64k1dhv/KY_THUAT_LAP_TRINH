#include <Wire.h> //Thư viện hỗ trợ giao tiếp IC2
#include <LiquidCrystal_I2C.h>  //Thư viện này hỗ trợ điều khiển màn hình LCD thông qua giao tiếp I2C

int cambien = 2; // Cảm biến kết nối với chân 2 
int dem = 0; // Biến đếm số lượng sản phẩm 
int pre = HIGH; // Biến lưu trạng thái của biến đếm trước đó 

// Khởi tạo LCD với địa chỉ I2C là 0x27, kích thước màn hình 16x2
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Khai báo các chân nối với mạch ULN2003
int motorPin1 = 8;
int motorPin2 = 9;
int motorPin3 = 10;
int motorPin4 = 11;

// Mảng định nghĩa các bước của động cơ bước 28BYJ-48 (4 pha) (motor)
int steps[8][4] = { 
  {1, 0, 0, 0}, // Mỗi hàng đại diện cho một bước của động cơ.
  {1, 1, 0, 0}, // Mỗi cột tương ứng với một cuộn dây trong động cơ (IN1, IN2, IN3, IN4).
  {0, 1, 0, 0}, // Giá trị 1 nghĩa là cấp điện cho cuộn dây đó, và giá trị 0 nghĩa là không cấp điện.
  {0, 1, 1, 0},
  {0, 0, 1, 0},
  {0, 0, 1, 1},
  {0, 0, 0, 1},
  {1, 0, 0, 1}
};

void setup() 
{
  Wire.begin();  // Không cần tham số vì sử dụng chân mặc định A4, A5 /A4: SDA (Serial Data Line)/A5: SCL (Serial Clock Line)
  lcd.begin(16, 2);  // Khởi động LCD với kích thước 16x2
  lcd.backlight();  // Bật đèn nền LCD
  lcd.setCursor(0, 0);  // Đặt con trỏ tại vị trí dòng 0, cột 0
  lcd.print("DO AN NHOM 5");// In dòng đầu tiên
  lcd.setCursor(1, 0); // Đặt con trọ tại vị trí dòng 0, cột 1
  lcd.print("DO AN NHOM 5"); // In dòng thứ 2
  delay(2000);  // Dừng 2 giây trước khi chuyển sang dòng tiếp theo

  lcd.clear();  // Xóa màn hình LCD
  lcd.setCursor(0, 1);  // Đặt con trỏ tại vị trí dòng 2, cột 0
  pinMode(cambien,INPUT); // Đặt các chân điều khiển động cơ là đầu vào (INPUT)
  lcd.backlight();// Bật đèn nền LCD 

  // Khởi tạo các chân điều khiển động cơ bước là OUTPUT
  pinMode(motorPin1, OUTPUT);// Đặt các chân điều khiển động cơ là đầu ra
  pinMode(motorPin2, OUTPUT);// Đặt các chân điều khiển động cơ là đầu ra
  pinMode(motorPin3, OUTPUT);// Đặt các chân điều khiển động cơ là đầu ra
  pinMode(motorPin4, OUTPUT);// Đặt các chân điều khiển động cơ là đầu ra
  
  // Bắt đầu giao diện Serial để gửi dữ liệu đến máy tính
  Serial.begin(9600);
}

void loop()// Chức năng trong loop
{
  int giatricambien = digitalRead(cambien);// Đọc giá trị từ cảm biến
  if(giatricambien==LOW && pre ==HIGH) // Khi cảm biến chuyển từ HIGH xuống LOW
  {
    dem = dem +1;//Tăng biến đếm dem lên 1 mỗi khi cảm biến được kích hoạt.
    delay(200);//tạm dừng 200ms để tránh việc ghi nhận nhiều lần khi cảm biến dao động 
  }
    pre=giatricambien; // Lưu trạng thái cảm biến hiện tại
    // Xóa dòng LCD cũ và hiển thị lại số lượng sản phẩm  
    lcd.setCursor(0,0);//Đặt con trỏ ở vị trí dòng 0, cột 0.
    lcd.print("so luong: ");//In dòng chữ "so luong: " lên LCD.
    lcd.setCursor(10,0);// Đặt con trỏ của màn hình LCD vào vị trí dòng 0, cột 10
    lcd.print(" "); // In một khoảng trắng để xóa nội dung cũ trên màn hình, tránh lỗi 
    lcd.print(dem); // in ra số lượng sản phẩm hay số lần cảm biến kích hoạt 

    //Gửi số lượng sản phẩm qua 
    Serial Monitor (máy tính)
    Serial.print("Số lượng sản phẩm:");
    Serial.println(dem);
   
   // Lặp qua các bước để quay động cơ
    for (int i = 0; i < 10; i++) {  // số bước để quay một vòng
     for (int j = 0; j < 8; j++) {
       // Cập nhật các chân điều khiển theo bước
       digitalWrite(motorPin1, steps[j][0]);
       digitalWrite(motorPin2, steps[j][1]);
       digitalWrite(motorPin3, steps[j][2]);
       digitalWrite(motorPin4, steps[j][3]);
       delay(1);  // Đợi một chút trước khi chuyển sang bước tiếp theo
     }
  }
}