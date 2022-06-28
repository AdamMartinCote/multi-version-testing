from titlecase import title_case


def main():
    for s in (
        title_case("This is a good morning to die"),
        title_case("hello you"),
        title_case("this is the title of the article"),
    ):
        print(s)


if __name__ == "__main__":
    main()
