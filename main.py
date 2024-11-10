from scraper import FTScraper

if __name__ == '__main__':
	scraper = FTScraper()
	# scraper.fetch_search_result_html('https://dtidirect.com/collections/all')
	# product_urls = scraper.get_product_urls()
	# scraper.fetch_product_html(product_urls)
	raw_product_datas = scraper.get_data()
	print(raw_product_datas)
	# product_datas = scraper.transform_product_datas(raw_product_datas)
	# scraper.create_csv(product_datas, 'freddotoys_products.csv')
