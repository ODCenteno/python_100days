from tkinter import *
import requests


def get_quote():
    """Fetch a new quote from the Kanye's quotes API and refresh the quote on the GUI"""
    # Kanye API Endpoint: https://api.kanye.rest/
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    response = response.json()
    quote = response["quote"]
    canvas.itemconfig(quote_text, text=quote)
    print(quote)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207,
                                text="Kanye Quote Goes HERE",
                                width=250,
                                font=("Arial", 30, "bold"),
                                fill="black"
                                )
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()