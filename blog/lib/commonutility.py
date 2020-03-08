def getPaginationRange(page, itemPerPage):
	try:
		pageNumber = int(page)
	except:
		pageNumber = 1
	endItem = itemPerPage * pageNumber
	startItem = endItem - itemPerPage
	return startItem, endItem
