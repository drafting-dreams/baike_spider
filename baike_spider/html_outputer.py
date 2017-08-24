# -*- coding: utf-8 -*-
class Outputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        count = 1
        fout = open('output.html', 'w', 1, "utf-8")
        fout.write('<html lang="zh-cn">')
        fout.write('<head><meta charset="utf-8"></head>')
        fout.write("<body>")
        fout.write('<table border=1 width="100%">')

        fout.write("<tr>")
        fout.write('<th width="20%">url</th>')
        fout.write('<th width="10%">title</th>')
        fout.write("<th>summary</th>")
        fout.write("</tr>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write('<td style="word-break : break-all; ">%d: %s</td>' % (count, data['url']))
            fout.write('<td style="word-break : break-all; ">%s</td>' % data['title'])
            fout.write('<td style="word-break : break-all; ">%s</td>' % data['summary'])
            fout.write("</tr>")
            count = count + 1

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")