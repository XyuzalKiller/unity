import re

def main():
    unnamed_union_count = 0

    def name_unnamed_union(m):
        nonlocal unnamed_union_count
        unnamed_union_count += 1

        return f"{m.group(0)} u{unnamed_union_count}"

    with open("il2cpp.h", "r") as f:
        data = f.read()

    with open("il2cpp_rizin.h", "w") as f:
        data = data.replace(
            "typedef void(*Il2CppMethodPointer)();",
            "typedef void(*Il2CppMethodPointer)(void);",
            1
        )


        data = re.sub(
            r": (\w+) {",
            r"{\n\1 super;",
            data
        )

        data = re.sub(
            r"(?s)union\s*\{.*?\}(?=;)",
            name_unnamed_union,
            data
        )

        f.write(data)

if __name__ == "__main__":
    main()
