import tkinter

def type_check(input: str) -> float | None:
    """Check if input is a number"""
    if input.strip():
        try:
            input = float(input)
            return input
        except ValueError:
            return None

def update_input_mile(event, input_mile, input_km) -> None:
    """Convert km to miles"""
    input_val = type_check(input_km.get())
    if input_val:
        output = round(input_val / 1.60934, 2)
    else:
        output = ''
    input_mile.delete(0, tkinter.END)
    input_mile.insert(0, output)

def update_input_km(event, input_mile, input_km) -> None:
    """Convert miles to km"""
    input_val = type_check(input_mile.get())
    if input_val:
        output = round(input_val * 1.60934, 2)
    else:
        output = ''
    input_km.delete(0, tkinter.END)
    input_km.insert(0, output)

def main() -> None:
    window = tkinter.Tk()
    window.title("Mile Kilometer Converter")
    window.minsize(300, 300)
    window.config(padx=20, pady=20)

    input_mile = tkinter.Entry()
    input_mile.grid(column=0, row=0)

    input_km = tkinter.Entry()
    input_km.grid(column=0, row=2)

    input_mile.bind('<KeyRelease>', lambda event: update_input_km(event, input_mile, input_km))
    input_km.bind('<KeyRelease>', lambda event: update_input_mile(event, input_mile, input_km))

    label_mile = tkinter.Label(text="Miles")
    label_mile.grid(column=1, row=0)

    label_km = tkinter.Label(text="Kilometers")
    label_km.grid(column=1, row=2)

    window.mainloop()

if __name__ == "__main__":
    main()
