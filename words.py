import random

words = {
	"verbs": ["arranging", "beginning", "blocking", "changing", "distilling", "instantiating", "voiding", "substituting", "creating", "concatenating", "visualizing", "analyzing", "downloading", "uploading"],
	"others_first": ["distilled", "binaural", "meridian", "networked", "correlated", "nulled", "procedural", "formatted", "cleansed", "supported", "monitoring", "quantum", "hacked"],
	"others_second": ["networks", "software", "arrays", "byte objects", "server keys", "hard drives", "pixels", "voxels", "strings", "integers", "polices", "servers", "dictionaries", "programs", "repositories"]
}

inside = ["the", "some of the", "more of the", "newer versions of"]

def technobabble():
	return words["verbs"][random.randrange(0, len(words["verbs"]))] + ' ' + inside[random.randrange(0, len(inside))] + ' ' + words["others_first"][random.randrange(0, len(words["others_first"]))] + ' ' + words["others_second"][random.randrange(0, len(words["others_second"]))]