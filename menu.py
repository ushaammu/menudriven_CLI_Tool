import subprocess

# -------------------------------
# Task 1 function: IP Reachability Test
# -------------------------------
def test_ip_reachability(ip_list):
    for ip in ip_list:
        print(f"\nPinging {ip} ...")

        result = subprocess.run(
            ["ping", "-c", "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        if result.returncode == 0:
            print(f"IP address {ip} is reachable.")
        else:
            print(f"IP address {ip} is unreachable.")


# -------------------------------
# Task 2 functions: Latency Summary
# -------------------------------
def calculate_average(data):
    return sum(data) / len(data)

def get_summary(data):
    return {
        "Min": min(data),
        "Max": max(data),
        "Average": calculate_average(data)
    }


# -------------------------------
# Task 3: Menu Driven CLI Tool
# -------------------------------
def menu():
    while True:   # Step 1: Main Loop
        print("\n--- Network Utility Menu ---")
        print("1. Test IP Reachability")
        print("2. Calculate Latency Summary")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")   # Step 2: Get Input

        # Step 3: Conditional Logic
        if choice == "1":
            # Choice 1: IP Test
            raw_ips = input("Enter comma-separated IP addresses: ")
            ip_list = [ip.strip() for ip in raw_ips.split(",")]
            test_ip_reachability(ip_list)

        elif choice == "2":
            # Choice 2: Latency Summary
            raw_data = input("Enter comma-separated latency values: ")
            data = [int(x.strip()) for x in raw_data.split(",")]

            summary = get_summary(data)
            print("\nLatency Summary:")
            print(f"Minimum: {summary['Min']} ms")
            print(f"Maximum: {summary['Max']} ms")
            print(f"Average: {summary['Average']:.2f} ms")

        elif choice == "3":
            print("Exiting the program...")   # Choice 3: Exit
            break

        else:
            print("Invalid choice. Please try again.")   # Invalid input


# -------------------------------
# Run the Menu
# -------------------------------
menu()
