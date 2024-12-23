from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def read_product_codes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]


def main():
    # Khởi tạo trình duyệt
    driver = webdriver.Chrome()
    driver.get("https://fptshop.com.vn/")
    time.sleep(2)

    # Đọc mã sản phẩm
    product_codes = read_product_codes('Data.txt')

    try:
        with open('results.txt', 'w', encoding='utf-8') as output_file:
            for code in product_codes:
                print(f"\nĐang xử lý mã: {code}")

                # Tìm và xóa ô tìm kiếm
                search_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
                search_box.clear()

                # Nhập mã và Enter
                search_box.send_keys(code)
                search_box.send_keys(Keys.RETURN)
                time.sleep(3)

                # Tìm giá sản phẩm
                try:
                    price = driver.find_element(By.CLASS_NAME, "Price_currentPrice__PBYcv").text
                    print(f"Giá: {price}")

                    # Ghi kết quả
                    result = f"Mã SP: {code}\nGiá: {price}\n{'=' * 30}\n"
                    output_file.write(result)

                except:
                    print(f"Không tìm thấy giá cho mã {code}")
                    output_file.write(f"Mã SP: {code}\nGiá: Không tìm thấy\n{'=' * 30}\n")

                time.sleep(2)
    except Exception as e:
        print(f"Lỗi: {str(e)}")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()