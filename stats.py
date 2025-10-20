from collections import Counter

def get_text(filepath):
	with open(filepath, 'r', encoding='utf-8') as file:
		return file.read()

def word_count(text):
	words = text.split()
	return len(words)

def char_count(text):
	text = text.lower()
	ch_counts = Counter(c for c in text if c.isalpha())

	sorted_counts = dict(sorted(ch_counts.items(), key=lambda x: x[1], reverse=True))
	return sorted_counts

def analyze_text(filepath):
	text = get_text(filepath)
	words = word_count(text)
	chars = char_count(text)
	return {
		"word_count": words, 
		"char_count": chars
	}
