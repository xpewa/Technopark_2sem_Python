import unittest
import factory
from unittest.mock import patch
import parser_html as parser

class Generate:
    def __init__(self, attrs, data):
        self.attrs = attrs
        self.data = data

class GenerateFactory(factory.Factory):
    class Meta:
        model = Generate

    attrs = factory.Sequence(lambda n: 'attrs=%d' % n)
    data = factory.Sequence(lambda n: 'data%d' % n)

class TestCallback(unittest.TestCase):
    def test_find_open_tag(self):
        cb = parser.Callback()
        generate = GenerateFactory.create()
        cb.find_open_tag("img", generate.attrs)
        self.assertEqual("img", cb.open_tag_list[0])
        self.assertEqual(generate.attrs, cb.attrs_list[0])

    def test_find_data(self):
        cb = parser.Callback()
        generate = GenerateFactory.create()
        cb.find_data(generate.data)
        self.assertEqual(generate.data, cb.data_list[0])

    def test_find_close_tag(self):
        cb = parser.Callback()
        cb.find_close_tag("img")
        self.assertEqual("img", cb.close_tag_list[0])
        
class TestHTMLParser(unittest.TestCase):
    def test_parse_simple_html(self):
        cb = parser.Callback()
        generate = GenerateFactory.create()
        html_str = "<html>" + generate.data + "</html>"
        parser.parse_html(html_str, cb.find_open_tag, cb.find_data, cb.find_close_tag)
        self.assertEqual("html", cb.open_tag_list[0])
        self.assertEqual("", cb.attrs_list[0])
        self.assertEqual(generate.data, cb.data_list[0])
        self.assertEqual("html", cb.close_tag_list[0])

    def test_parse_difficult_html(self):
        cb = parser.Callback()
        generate1 = GenerateFactory.create()
        generate2 = GenerateFactory.create()
        html_str = "<html><head><title>" + generate1.data +\
                    "</title></head><body><p " + generate1.attrs +\
                    ">" + generate2.data + "</p></body></html>"
        parser.parse_html(html_str, cb.find_open_tag, cb.find_data, cb.find_close_tag)
        self.assertEqual("html", cb.open_tag_list[0])
        self.assertEqual("head", cb.open_tag_list[1])
        self.assertEqual("title", cb.open_tag_list[2])
        self.assertEqual("body", cb.open_tag_list[3])
        self.assertEqual("p", cb.open_tag_list[4])
        self.assertEqual("", cb.attrs_list[0])
        self.assertEqual("", cb.attrs_list[1])
        self.assertEqual("", cb.attrs_list[2])
        self.assertEqual("", cb.attrs_list[3])
        self.assertEqual(generate1.attrs, cb.attrs_list[4])
        self.assertEqual(generate1.data, cb.data_list[0])
        self.assertEqual(generate2.data, cb.data_list[1])
        self.assertEqual("title", cb.close_tag_list[0])
        self.assertEqual("head", cb.close_tag_list[1])
        self.assertEqual("p", cb.close_tag_list[2])
        self.assertEqual("body", cb.close_tag_list[3])
        self.assertEqual("html", cb.close_tag_list[4])

    @patch('parser_html.Callback.find_close_tag')
    def test_call_count_close_tag_callback(self, find_close_tag_mock):
        cb = parser.Callback()
        html_str = "<html><a></a><body><p><im></im></p></body></html>"
        parser.parse_html(html_str, cb.find_open_tag, cb.find_data, cb.find_close_tag)
        self.assertEqual(find_close_tag_mock.call_count, 5)

    @patch('parser_html.Callback.find_open_tag')
    def test_call_count_open_tag_callback(self, find_open_tag_mock):
        cb = parser.Callback()
        generate = GenerateFactory.create()
        html_str = "<html><a" + generate.attrs +\
                    "></a><body><p><im></im></p></body></html>"
        parser.parse_html(html_str, cb.find_open_tag, cb.find_data, cb.find_close_tag)
        self.assertEqual(find_open_tag_mock.call_count, 5)

    @patch('parser_html.Callback.find_data')
    def test_call_count_data_callback(self, find_data_mock):
        cb = parser.Callback()
        generate = GenerateFactory.create()
        html_str = "<html><a " + generate.attrs + ">" +\
                   generate.data + "</a><body><p><im>" +\
                   generate.data + "</im></p></body></html>"
        parser.parse_html(html_str, cb.find_open_tag, cb.find_data, cb.find_close_tag)
        self.assertEqual(find_data_mock.call_count, 2)
        

if __name__ == '__main__':
    unittest.main()
