#!/usr/bin/env python

import sys
import urllib2
from urlparse import urlparse

# Please install BeautifulSoup by pip install
from BeautifulSoup import BeautifulSoup


def parseDomain(url):
	parsed_uri = urlparse(url)
	return parsed_uri[1]


def trimPathOnUrl(domain, url, parent_path = ""):
	'''
	Continue only if 
		1. url domain is empty (it means that the path is located on the original domain)
		OR
		2. url domain contains the original url (it means that url is either domain or subdomain)
	'''
	parsed_uri = urlparse(url)
	if not ((not parsed_uri[1]) or parsed_uri[1].find(domain) >= 0):
		return None

	# Just trim relative path here
	path = parsed_uri[2]
	if path.startswith('./'):
		path = path[2:]
	elif path.startswith('/'):
		path = path[1:]

	return path
	

def getLinks(html_page):
	links = []

	soup = BeautifulSoup(html_page)
	for a_tag in soup.findAll('a'):
		links.append(a_tag.get('href'))

	return links


def crawlUrlViaBFS(main_domain, main_path):
	# Create visited object to prevent loops in BFS (Breadth First Search)
	visited = {}
	visited[main_path] = True
	
	# Create a graph to hold references
	# This graph is used as queue, too
	graph = [[]]
	node_paths = ['']
	parent_i, child_i = 0, 1

	# Start BFS
	while parent_i < child_i:
		cur_path = node_paths[parent_i]
		print "Crawling", cur_path, "..."

		# Try to get url and process the response only if it http status is valid there
		url = "http://" + main_domain + '/' + cur_path
		try:
			html_page = urllib2.urlopen(url)
		except Exception, ex:
			print "Exception in loading url:", url, "Error:", ex
			parent_i += 1
			continue

		# Traverse only valid links located on current domain
		# Try to crawl path only if it is not crawled before
		links = getLinks(html_page)
		for link in links:
			if link:
				link = trimPathOnUrl(main_domain, link, cur_path)
				if link and (link not in visited):
					visited[link] = True
					node_paths.append(link)
					graph.append([])
					graph[parent_i].append(child_i)
					child_i += 1

		parent_i += 1

	return graph, node_paths


def printGraphViaDFS(graph, node_paths, index, level):
	if index >= 0:
		for i in xrange(level):
			sys.stdout.write('\t')
		print node_paths[index]

	for u in graph[index]:
		printGraphViaDFS(graph, node_paths, u, level + 1)


def crawlUrl(url):
	# Trim domain and path
	main_domain = parseDomain(url)
	main_path = trimPathOnUrl(main_domain, url)

	print "** Root URL to crawl:", url, "**"
	print "** Domain Name:", main_domain, "**"

	# Start to crawl via BFS
	graph, node_paths = crawlUrlViaBFS(main_domain, main_path)

	# Print graph via DFS
	print "** SITEMAP START **"
	printGraphViaDFS(graph, node_paths, 0, -1)
	print "** SITEMAP END **"


if __name__ == "__main__":
	if len(sys.argv) <= 1:
		print "Please pass an url as an argument!"
		print "Usage: ./crawler.py url"
		sys.exit(-1)

	crawlUrl(sys.argv[1])