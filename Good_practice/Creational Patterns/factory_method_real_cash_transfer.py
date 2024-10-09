"""Představme si aplikaci, která zpracovává platby pomocí různých
platebních metod. Každá metoda má vlastní proces, jak platbu zpracovat."""

# Abstraktní třída pro zpracování platby
"""Abstraktní třída PaymentProcessor:
Tato třída definuje obecnou strukturu pro všechny platební metody. 
Metoda process_payment() musí být implementována v každé konkrétní platební třídě."""


class PaymentProcessor:
    def process_payment(self, amount: float):
        raise NotImplementedError("Tato metoda musí být implementována!")


# Konkrétní třídy pro jednotlivé platební metody
"""Konkrétní třídy CreditCardPayment, PayPalPayment a BankTransferPayment:
Tyto třídy představují různé způsoby zpracování plateb. Každá z nich implementuje 
vlastní verzi metody process_payment(), která obsahuje logiku pro zpracování 
příslušné platby."""


class CreditCardPayment(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of {amount} Kč")


class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of {amount} Kč")


class BankTransferPayment(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing bank transfer payment of {amount} Kč")


# Factory Method pro výběr platební metody
"""Factory Method PaymentProcessorFactory:
Tato třída obsahuje metodu create_processor(), která rozhoduje, kterou 
platební metodu vrátit. Podle vstupního parametru (payment_type) vytvoří 
buď CreditCardPayment, PayPalPayment, nebo BankTransferPayment."""


class PaymentProcessorFactory:
    def create_processor(self, payment_type: str) -> PaymentProcessor:
        if payment_type == "credit_card":
            return CreditCardPayment()
        elif payment_type == "paypal":
            return PayPalPayment()
        elif payment_type == "bank_transfer":
            return BankTransferPayment()
        else:
            raise ValueError("Neznámá platební metoda!")


# Příklad použití:
"""Použití:
Vytvoříme instanci PaymentProcessorFactory a pomocí metody create_processor() 
zvolíme konkrétní platební metodu.
Podle volby (např. "paypal", "credit_card") se vrátí odpovídající platební třída, 
na které můžeme zavolat metodu process_payment() a zpracovat platbu."""
factory = PaymentProcessorFactory()

# Výběr platební metody
payment_method = factory.create_processor("paypal")
payment_method.process_payment(1500)  # Výstup: Processing PayPal payment of 1500 Kč

payment_method = factory.create_processor("credit_card")
payment_method.process_payment(2300)  # Výstup: Processing credit card payment of 2300 Kč

payment_method = factory.create_processor("bank_transfer")
payment_method.process_payment(3000)  # Výstup: Processing bank transfer payment of 3000 Kč
