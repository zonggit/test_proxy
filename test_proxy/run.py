from scrapy import cmdline

name = 'proxie'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
