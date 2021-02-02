import wikipedia


def main():
    input_prompt = input("Enter a page title or search phrase >>> ")
    search_results = wikipedia.search(input_prompt, results=3)
    search_summary = wikipedia.summary(input_prompt)
    user_input = wikipedia.page(input_prompt)
    title = user_input.title
    url = user_input.url
    print(search_results)
    print(title)
    print(search_summary)
    print(url)


if __name__ == '__main__':
    main()