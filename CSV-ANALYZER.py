# імпорти
import pandas as pd
import matplotlib.pyplot as plt


# Завантаження CSV файлу
def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Помилка при завантаженні файлу: {e}")
        return None


# інформація про файл
def get_file_info(data):
    print("~~~~~ Інформація про файл: ~~~~~")
    print("Кількість рядків:", data.shape[0])
    print("Кількість стовпців:", data.shape[1])
    print("Назви стовпців:", data.columns.tolist())
    print("Типи даних стовпців:\n", data.dtypes)


# статистика по числовим стовпцям
def get_statistics(data):
    print("~~~~~ Статистика: ~~~~~")
    print("Середня ціна:", data['price'].mean(), "грн")
    print("Мінімальна ціна:", data['price'].min(), "грн")
    print("Максимальна ціна:", data['price'].max(), "грн")
    print("Загальна кількість проданих товарів:", data['quantity'].sum())

    revenue = (data['price'] * data['quantity']).sum()
    print("Загальна виручка:", revenue, "грн")


# аналіз по містам
def analyze_by_city(data):
    print("~~~~~ Аналіз по містам: ~~~~~")

    data = data.copy()
    data['revenue'] = data['price'] * data['quantity']

    city_group = data.groupby('city').agg(
        Кількість_товарів=('quantity', 'sum'),
        Виручка=('revenue', 'sum')
    )

    print(city_group)


# найпопулярніші категорії
def analyze_by_category(data):
    print("~~~~~ Аналіз по категоріям: ~~~~~")

    category_group = data.groupby('product')['quantity'].sum().sort_values(
        ascending=False
    ).head(6)

    print(category_group)


# візуалізація даних
def visualize_data(data):

    # Візуалізація розподілу цін
    plt.figure(figsize=(10, 6))
    plt.hist(data['price'], bins=10, edgecolor='black')
    plt.title('Розподіл цін товарів')
    plt.xlabel('Ціна (грн)')
    plt.ylabel('Кількість товарів')
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    # Візуалізація кількості товарів по містам
    city_counts = data.groupby('city')['quantity'].sum()

    plt.figure(figsize=(10, 6))
    city_counts.plot(kind='bar')
    plt.title('Кількість проданих товарів по містам')
    plt.xlabel('Місто')
    plt.ylabel('Кількість товарів')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

    # Візуалізація кількості товарів по категоріям
    category_counts = data.groupby('product')['quantity'].sum().sort_values(
        ascending=False
    ).head(6)

    plt.figure(figsize=(10, 6))
    category_counts.plot(kind='bar')
    plt.title('Найпопулярніші товари')
    plt.xlabel('Товар')
    plt.ylabel('Кількість проданих товарів')
    plt.xticks(rotation=45)
    plt.grid(axis='y', alpha=0.75)
    plt.show()


# головна функція
def main():
    file_path = input("Введіть шлях до CSV файлу: ")
    data = load_csv(file_path)

    if data is None:
        return

    while True:
        try:
            input("\nНатисніть Enter, щоб продовжити...")

            print("\n===== CSV ANALYZER =====")
            print("1. Показати інформацію про файл")
            print("2. Показати статистику")
            print("3. Показати продажі по містах")
            print("4. Показати найпопулярніші товари")
            print("5. Показати графіки")
            print("0. Вихід")

            choice = input("\nВаш вибір: ")

            if choice == '1':
                get_file_info(data)

            elif choice == '2':
                get_statistics(data)

            elif choice == '3':
                analyze_by_city(data)

            elif choice == '4':
                analyze_by_category(data)

            elif choice == '5':
                visualize_data(data)

            elif choice == '0':
                print("Вихід з програми.")
                break

            else:
                print("Невірний вибір. Будь ласка, спробуйте ще раз.")

        except Exception as e:
            print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    main()