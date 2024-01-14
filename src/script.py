import matplotlib.pyplot as plt

def calculate_efficiency(input_energy, output_energy, total_loss):
    return (output_energy / (input_energy - total_loss)) * 100.0

def main():
    input_energy = float(input("Введите входную энергию: "))
    output_energy = float(input("Введите выходную энергию: "))

    fuel_loss = input_energy * 0.015 # Потери от недожога топлива
    transport_loss = input_energy * 0.06 # Потери при доставке топлива
    generator_loss = input_energy * 0.04 # Потера генератора
    thermodynamic_loss = input_energy * 0.12 # Термодинамические потери
    insulation_loss = input_energy * 0.03 # Потери из-за неидеальной изоляции теплоносителей

    total_loss = fuel_loss + transport_loss + generator_loss + thermodynamic_loss + insulation_loss

    efficiency = calculate_efficiency(input_energy, output_energy, total_loss)
    energy_percentage = (output_energy / (input_energy - total_loss)) * 100

    print(f"КПД энерговыработки: {efficiency}%")
    print(f"Процент добытой энергии: {energy_percentage}%")

    losses = [fuel_loss, transport_loss, generator_loss, thermodynamic_loss, insulation_loss]
    labels = ["Топливо", "Транспорт", "Генератор", "Термодинамика", "Изоляция"]
    plt.bar(labels, losses)
    plt.title("Потери от различных факторов")
    plt.show()

if __name__ == "__main__":
    main()
