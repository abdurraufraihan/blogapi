from lib import constants as const

def getPaginationRange(page, itemPerPage):
	try:
		pageNumber = int(page)
		if pageNumber < 1:
			pageNumber = 1
	except:
		pageNumber = 1
	endItem = itemPerPage * pageNumber
	startItem = endItem - itemPerPage
	return startItem, endItem

def getSummaryText(text, limit):
	return text[:limit] + const.ELLIPS
