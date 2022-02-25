def delete_single_line_comments(text):
    start_index = text.find("//")
    end_index = text.find('\n', start_index + 1)
    if end_index == -1:
        end_index = len(text)

    while start_index > -1:
        print(end_index)
        substring_to_remove = text[start_index: end_index]
        text = text.replace(substring_to_remove, '')
        start_index = text.find("//")
        end_index = text.find('\n', start_index + 1)
        if end_index == -1:
            end_index = len(text)

    return text


def delete_multi_line_comments(text):
    start_index = text.find("/*")
    end_index = text.find('*/', start_index + 1) + 2

    while start_index > -1:
        substring_to_remove = text[start_index: end_index]
        text = text.replace(substring_to_remove, '')
        start_index = text.find("/*")
        end_index = text.find('*/', start_index + 1) + 2

    return text


with open('input4.txt') as file_input:
    code = file_input.read()

code = delete_single_line_comments(code)
code = delete_multi_line_comments(code)


with open('output4.txt', 'w') as file_output:
    file_output.write(code)
