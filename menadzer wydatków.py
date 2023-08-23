import tkinter as tk
from tkinter import messagebox
import json

class ExpenseManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Menadżer wydatków")

        self.expenses = []
        self.load_expenses()

        self.label = tk.Label(root, text="Menadżer wydatków", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.expense_frame = tk.Frame(root)
        self.expense_frame.pack()

        self.expense_label = tk.Label(self.expense_frame, text="Wydatki:")
        self.expense_label.grid(row=0, column=0, padx=5, pady=5)

        self.expense_entry = tk.Entry(self.expense_frame, width=40)
        self.expense_entry.grid(row=0, column=1, padx=5, pady=5)

        self.amount_label = tk.Label(self.expense_frame, text="Ilosc:")
        self.amount_label.grid(row=1, column=0, padx=5, pady=5)

        self.amount_entry = tk.Entry(self.expense_frame, width=15)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Dodaj wydatek", command=self.add_expense)
        self.add_button.pack(pady=5)

        self.expense_listbox = tk.Listbox(root, width=50)
        self.expense_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Usuń wydatek", command=self.delete_expense)
        self.delete_button.pack(pady=5)

        self.load_expenses_to_listbox()

    def add_expense(self):
        expense = self.expense_entry.get()
        amount = self.amount_entry.get()
        if expense and amount:
            self.expenses.append({"Wydatek": expense, "Ilosc": amount})
            self.save_expenses()
            self.expense_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.load_expenses_to_listbox()

    def delete_expense(self):
        selected_indices = self.expense_listbox.curselection()
        if selected_indices:
            selected_index = selected_indices[0]
            del self.expenses[selected_index]
            self.save_expenses()
            self.load_expenses_to_listbox()

    def load_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file)

    def load_expenses_to_listbox(self):
        self.expense_listbox.delete(0, tk.END)
        for expense_data in self.expenses:
            expense = expense_data["expense"]
            amount = expense_data["amount"]
            display_text = f"{expense}: {amount}"
            self.expense_listbox.insert(tk.END, display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseManagerApp(root)
    root.mainloop()
