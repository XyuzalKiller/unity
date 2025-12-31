import re

def main():
    inheritance_pattern = re.compile(r": (\w+) {")

    unnamed_union_pattern = re.compile(r"(?=union .*)};")
    unnamed_union_count = 0

    def name_unnamed_union(m):
        nonlocal unnamed_union_count
        unnamed_union_count += 1

        return f"} u{unnamed_union_count};"

    with open("il2cpp.h", "r") as f:
        data = f.read()

        data = data.replace(
            "typedef void(*Il2CppMethodPointer)();",
            "typedef void(*Il2CppMethodPointer)(void);",
            1
        )

        data = unnamed_union_pattern.sub(
            name_unnamed_union,
            data
        )

        data = inheritance_pattern.sub(
            r"{\n\1 super;",
            data
        )

    with open("il2cpp_rizin.h", "w") as f:
        f.write(data)

if __name__ == "__main__":
    main()
