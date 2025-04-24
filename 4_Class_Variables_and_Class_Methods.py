class Bank:
    bank_name : str = "MCB Bank"
 
    @classmethod
    def change_bank_name(cls, name: str) -> None :
        cls.bank_name = name

if __name__ in "__main__" :
    bank_1 : Bank = Bank()
    bank_2 : Bank = Bank()

    print(f"\nBank 1 : {bank_1.bank_name}")
    print(f"Bank 2 : {bank_2.bank_name}")

    print("\nChange Bank Name")

    ChangeName : Bank = Bank()
    ChangeName.change_bank_name("UBL Bank")


    print(f"\nBank 1 : {bank_1.bank_name}")
    print(f"Bank 2 : {bank_2.bank_name}")
