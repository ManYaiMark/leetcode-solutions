from pathlib import Path


LEVELS = {"1": "easy", "2": "medium", "3": "hard"}


def main():
    print("เลือกโฟลเดอร์:")
    print("1. easy")
    print("2. medium")
    print("3. hard")
    choice = input("เลือกหมายเลข: ").strip()
    if choice not in LEVELS:
        print("กรุณาเลือกหมายเลข 1, 2 หรือ 3")
        return
    level = LEVELS[choice]

    title = input("ชื่อโจทย์: ").strip()
    if not title:
        print("กรุณากรอกชื่อโจทย์")
        return

    filename = title.replace(".", "").replace(" ", "_") + ".py"
    destination = Path(__file__).resolve().parent / level / filename
    try:
        destination.touch(exist_ok=False)
    except FileExistsError:
        print(f"ไฟล์มีอยู่แล้ว: {destination}")
        return

    print(f"สร้างไฟล์แล้ว: {destination}")


if __name__ == "__main__":
    main()
