from f1_edit import edit_manager


def test_edit_menu_returns_to_main_menu(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda: "0")
    edit_manager.edit_menu()
    assert "返回主選單" in capsys.readouterr().out
