from text_extract.pil_utils import GoogleSearch

question = 'Loài cây nào chỉ có một lá và một củ?'
answer = 'Phá cố chỉ'
search_instance = GoogleSearch('{} - {}'.format(question, answer))
search_instance.search()
results = search_instance.result
total = results[0].number_of_results
count_appear = 0
descriptions = [result.description for result in results]
for d in descriptions:
    if answer in d:
        count_appear += 1

print(total)
print(count_appear)
