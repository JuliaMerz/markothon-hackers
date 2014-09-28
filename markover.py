import facebook
from urlparse import urlparse, parse_qs
from pymarkovchain import MarkovChain

HACKATHON = "759985267390294"

mc1 = MarkovChain("./posts")
mc2 = MarkovChain("./comments")

oauth_access_token = "CAACEdEose0cBAO96rmoA3luiTliISPKEFLdzqM9aRiZC14EAVT155wXWdiZChcSnuKa7koxRZAx4Wx7yccSlUKnZApZAPfaJ555ZBZAsqR82D38w4yBxYKQg8i9USw9ImrwZBZBZCZBeWkfCNzfAirNBQZBc04POWXFgQoek3Eq3rdqFZCFzZAhJxFDxoRlwnmCuf8AZCTCtoz0Jz4QSAnDQJfGKLzmKLZBMXyoGCs8ZD"
graph = facebook.GraphAPI(oauth_access_token)

"Input: result. ['paging']['next']"
def parse_next(result):
    try:
        url = result['paging']['next']
    except:
        return False
    u = urlparse(url)
    return parse_qs(u.query)

def parse_prev(result):
    try:
        url = result['paging']['previous']
    except:
        return False
    u = urlparse(url)
    return parse_qs(u.query)

print dir(graph)
print "test"
mega_comments = []
mega_posts = []
profile = graph.get_connections("759985267390294", "feed")
next_url = profile['paging']['next']

def process_comments_chunk(comments):
    print "chunk"
    try:
        for comment in comments['data']:
            mega_comments.append(comment['message'])
    except:
        print "ERROR!"
        print comments

def process_comments(postid):
    "Process comments for the post"
    print "processing comments"
    comments = graph.get_connections(postid, "comments")
    process_comments_chunk(comments)
    parse = parse_next(comments)
    while(parse):
        comments = graph.get_connections(postid, "comments", after= parse['after'][0])
        process_comments_chunk(comments)
        parse = parse_next(comments)

def parse_posts(results):
    print "parsing posts"
    try:
        for post in results['data']:
            try:
                mega_posts.append(post['message'])
            except:
                print "ERROR!"
                print post
            process_comments(post['id'])
            final_posts = "\n\n".join(mega_posts)
            final_comments = "\n\n".join(mega_comments)
            mc1.generateDatabase(final_posts)
            mc2.generateDatabase(final_comments)
    except:
        print "MEGAERROR!"

"gets comments after"
def parse_after(results):
    parse = parse_next(results)

    final_posts = "\n\n".join(mega_posts)
    final_comments = "\n\n".join(mega_comments)
    mc1.generateDatabase(final_posts)
    mc2.generateDatabase(final_comments)

    while(parse):
        posts = graph.get_connections(HACKATHON, "feed", until= parse['until'][0], limit=parse['limit'][0])
        parse_posts(posts)
        parse = parse_next(posts)

"gets comments before"
def parse_before(results):
    parse = parse_prev(results)
    final_posts = "\n\n".join(mega_posts)
    final_comments = "\n\n".join(mega_comments)
    mc1.generateDatabase(final_posts)
    mc2.generateDatabase(final_comments)
    while(parse):
        posts = graph.get_connections(HACKATHON, "feed", since= parse['since'][0], limit=parse['limit'][0])
        parse_posts(posts)
        parse = parse_prev_posts(posts)

initial = graph.get_connections("759985267390294", "feed")
parse_posts(initial)
parse_after(initial)
parse_before(initial)




"""
main:
    for post catch comments
        for comment go next until end

go to all prev pages while possible
    for post catch comments
        for comment go next until end

go to all next pages while possible
    for post catch comments
        for comment go next until end
"""



