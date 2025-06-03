from pages.heroku_table_reader import HerokuTableReader

def test_read_table1(web_table1):
    reader = HerokuTableReader(web_table1)
    reader.read_table()
