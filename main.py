import sys
from pathlib import Path

# 取得專案根目錄並加入搜尋路徑
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT))

# 將各子模組資料夾加入 sys.path，解決跨模組找不到內部檔案的問題 (如 edit_student)
sys.path.append(str(PROJECT_ROOT / "f1_edit"))
sys.path.append(str(PROJECT_ROOT / "f1_delete"))
sys.path.append(str(PROJECT_ROOT / "F1_search"))
sys.path.append(str(PROJECT_ROOT / "f1_search"))

from general_fun import clear_screen

# 1. 查詢模組 (Search)
try:
    from F1_search.menu import search_menu
except ImportError:
    try:
        from F1_search.menu import search_menu
    except ImportError:
        search_menu = None

# 2. 編輯模組 (Edit)
from f1_edit.edit_manager import edit_menu

# 3. 刪除模組 (Delete)
from f1_delete.f1_del_model import del_ui

# 4. 新增模組 (Add，待組員提供入口函式後接入)
# from f1_add.add_manager import add_ui


def main():
    while True:
        clear_screen()
        print("\n=========================================")
        print("    國立臺北科技大學 選課排課系統 (F1)     ")
        print("=========================================")
        print("[1] 查詢模組 (Search)")
        print("[2] 新增模組 (Add)")
        print("[3] 編輯模組 (Edit)")
        print("[4] 刪除模組 (Delete)")
        print("[0] 結束系統")
        print("=========================================")

        choice = input("請選擇功能代號 (0-4)：").strip()

        if choice == "1":
            clear_screen()
            if search_menu:
                search_menu()
            else:
                print("【提示】未找到查詢選單，請確認 F1_search/menu.py 是否包含 search_menu()。")
                input("\n按 Enter 鍵返回主選單...")

        elif choice == "2":
            clear_screen()
            # add_ui()
            print("【提示】新增模組待組員提供入口函式後接入。")
            input("\n按 Enter 鍵返回主選單...")

        elif choice == "3":
            clear_screen()
            edit_menu()

        elif choice == "4":
            clear_screen()
            del_ui()

        elif choice == "0":
            clear_screen()
            print("系統已安全關閉，感謝使用！")
            sys.exit(0)

        else:
            print("無效代號，請按 Enter 重新選擇...")
            input()


if __name__ == "__main__":
    main()