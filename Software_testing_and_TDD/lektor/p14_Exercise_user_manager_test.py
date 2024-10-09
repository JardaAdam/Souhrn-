"""Správa uživatelských účtů a volání externího API
Vytvořte třídu User, která má atributy username (uživatelské jméno) a email.
Vytvořte třídu UserManager, která umožňuje přidávat uživatele a odesílat ověřovací e-mail prostřednictvím externí služby.
Metoda send_verification_email(user) ve třídě UserManager by měla volat metodu send_email(to, subject, body), která simuluje volání externího API pro odesílání e-mailu.
Použijte mock objekty, abyste otestovali, zda metoda send_verification_email volá send_email s odpovídajícími parametry.
"""

import pytest
from unittest.mock import patch
from p14_Exercise_user_manager import User, UserManager


def test_user_creation():
    user = User("john_doe", "john@example.com")
    assert user.username == "john_doe"
    assert user.email == "john@example.com"


@patch('tasks.UserManager.send_email')
def test_send_verification_email(mock_send_email):
    manager = UserManager()
    user = User("john_doe", "john@example.com")

    manager.add_user(user)
    manager.send_verification_email(user)

    mock_send_email.assert_called_once_with(
        "john@example.com",
        "Verify your email",
        "Please verify your email for john_doe."
    )


if __name__ == "__main__":
    pytest.main()
