import json

class JsonExportPipeline(object):
    def __init__(self):
        self.file = open("Tomates.json", "w")

    def process_item(self, item, spider):
        data = {
            "title": item["title"],
            "tomates": item["tomates"],
        }
        json_data = json.dumps(data, ensure_ascii=False)
        self.file.write(json_data + ",\n")
        return item

    def close_spider(self, spider):
        self.file.close()
