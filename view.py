import eel
import main
import search

app_name = "index"
end_point = "main.html"
size = (700, 600)


@ eel.expose
def kimetsu_search(word, csv_name):
    search.kimetsu_search(word, csv_name)


main.start(app_name, end_point, size)
# desktop.start(size=size,appName=app_name,endPoint=end_point)
