# 1. 暗号化用のルール（ひらがな ➔ 絵文字）
encode_rules = {
    # あ行
    "あ": "😀", "い": "😃", "う": "😄", "え": "😁", "お": "😆",
    # か行
    "か": "🥹", "き": "😅", "く": "😂", "け": "🤣", "こ": "🥲",
    # さ行
    "さ": "☺️", "し": "😊", "す": "😇", "せ": "🙂", "そ": "🙃",
    # た行
    "た": "😉", "ち": "😌", "つ": "😍", "て": "🥰", "と": "😘",
    # な行
    "な": "😗", "に": "😙", "ぬ": "😚", "ね": "😋", "の": "😛",
    # は行
    "は": "😝", "ひ": "😜", "ふ": "🤪", "へ": "🤨", "ほ": "🧐",
    # ま行
    "ま": "🤓", "み": "😎", "む": "🥸", "め": "🤩", "も": "🥳",
    # や行
    "や": "😏", "ゆ": "😒", "よ": "😞",
    # ら行
    "ら": "😔", "り": "😟", "る": "😕", "れ": "🙁", "ろ": "☹️",
    # わ行・ん
    "わ": "😣", "を": "😖", "ん": "😫"
}

# 2. 復元用のルールを自動で逆向き（絵文字 ➔ ひらがな）に作る
decode_rules = {v: k for k, v in encode_rules.items()}


# --- 暗号化する関数 ---
def soramame_encode(text):
    encoded_text = ""
    for char in text:
        if char in encode_rules:
            encoded_text += encode_rules[char]
        else:
            encoded_text += char  # ルールにない文字はそのまま
    return encoded_text


# --- 復元（デコード）する関数 ---
def soramame_decode(text):
    decoded_text = ""
    for char in text:
        if char in decode_rules:
            decoded_text += decode_rules[char]
        else:
            decoded_text += char  # ルールにない絵文字などはそのまま
    return decoded_text


# ==========================
# テスト実行してみよう！
# ==========================
original_message = "そらまめ"

# 1. 暗号化
encrypted = soramame_encode(original_message)
# 2. 復元
decrypted = soramame_decode(encrypted)

print("元の言葉:", original_message)
print("暗号化:", encrypted)
print("復元した言葉:", decrypted)
