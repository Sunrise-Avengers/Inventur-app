def display_kasten(data):
    print("\nKasten:")
    for kasten in data.get('kasten', []):
        print(f"ID: {kasten['id']}, Name: {kasten['name']}, Gross: {kasten['gross']}")
    print("\n")
