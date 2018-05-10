"""
Script to gather comments from game threads on www.reddit.com/r/BostonCeltics
between the 2018 All-Star Weekend and the end of the 2018 regular season

Alex Freno
"""

import praw


#authenticating via OAuth2
reddit = praw.Reddit(client_id='LRivoThhfzAqbA',
                     client_secret='MxT6OAMvlspbCEyN-ShRItxSUlU',
                     password='GoCeltics',
                     user_agent='testscript by AF',
                     username='CSC450Project')


#List to store # of comments from all game threads
comment_totals = [] 

#Gather comments from all post-ASG game threads in /r/BostonCeltics
#comment totals may change if run at a later date due to threads not locking 
g1 = reddit.submission(id='7zsel6')
g1_comments = g1.comments.list()
g1_comments = len(g1_comments)
comment_totals.insert(0, g1_comments)

g2 = reddit.submission(id='800hwb')
g2_comments = g2.comments.list()
g2_comments = len(g2_comments)
comment_totals.insert(1, g2_comments)

g3 = reddit.submission(id='80ht2x')
g3_comments = g3.comments.list()
g3_comments = len(g3_comments)
comment_totals.insert(2, g3_comments)

g4 = reddit.submission(id='810zgv')
g4_comments = g4.comments.list()
g4_comments = len(g4_comments)
comment_totals.insert(3, g4_comments)

g5 = reddit.submission(id='81u9of') #Loss
g5_comments = g5.comments.list()
g5_comments = len(g5_comments)
comment_totals.insert(4, g5_comments)

g6 = reddit.submission(id='82aoz3')
g6_comments = g6.comments.list()
g6_comments = len(g6_comments)
comment_totals.insert(5, g6_comments)

g7 = reddit.submission(id='832j0z')
g7_comments = g7.comments.list()
g7_comments = len(g7_comments)
comment_totals.insert(6, g7_comments)

g8 = reddit.submission(id='83qc2t') #Loss
g8_comments = g8.comments.list()
g8_comments = len(g8_comments)
comment_totals.insert(7, g8_comments)

g9 = reddit.submission(id='84i3uz') #Loss
g9_comments = g9.comments.list()
g9_comments = len(g9_comments)
comment_totals.insert(8, g9_comments)

g10 = reddit.submission(id='84z98j')
g10_comments = g10.comments.list()
g10_comments = len(g10_comments)
comment_totals.insert(9, g10_comments)

g11 = reddit.submission(id='85eaxv') #Loss
g11_comments = g11.comments.list()
g11_comments = len(g11_comments)
comment_totals.insert(10, g11_comments)

g12 = reddit.submission(id='85xev1')
g12_comments = g12.comments.list()
g12_comments = len(g12_comments)
comment_totals.insert(11, g12_comments)

g13 = reddit.submission(id='86pokz')
g13_comments = g13.comments.list()
g13_comments = len(g13_comments)
comment_totals.insert(12, g13_comments)

g14 = reddit.submission(id='874239')
g14_comments = g14.comments.list()
g14_comments = len(g14_comments)
comment_totals.insert(13, g14_comments)

g15 = reddit.submission(id='87ehq8')
g15_comments = g15.comments.list()
g15_comments = len(g15_comments)
comment_totals.insert(14, g15_comments)

g16 = reddit.submission(id='87x4vf')
g16_comments = g16.comments.list()
g16_comments = len(g16_comments)
comment_totals.insert(15, g16_comments)

g17 = reddit.submission(id='88mb3k')
g17_comments = g17.comments.list()
g17_comments = len(g17_comments)
comment_totals.insert(16, g17_comments)

g18 = reddit.submission(id='89jtfe') #Loss
g18_comments = g18.comments.list()
g18_comments = len(g18_comments)
comment_totals.insert(17, g18_comments)

g19 = reddit.submission(id='89utxc') #Loss
g19_comments = g19.comments.list()
g19_comments = len(g19_comments)
comment_totals.insert(18, g19_comments)

g20 = reddit.submission(id='8adosr')
g20_comments = g20.comments.list()
g20_comments = len(g20_comments)
comment_totals.insert(19, g20_comments)

g21 = reddit.submission(id='8arc8d') #Loss
g21_comments = g21.comments.list()
g21_comments = len(g21_comments)
comment_totals.insert(20, g21_comments)

g22 = reddit.submission(id='8bcduv') #Loss
g22_comments = g22.comments.list()
g22_comments = len(g22_comments)
comment_totals.insert(21, g22_comments)

g23 = reddit.submission(id='8blg3e')
g23_comments = g23.comments.list()
g23_comments = len(g23_comments)
comment_totals.insert(22, g23_comments)


#Output list
print(comment_totals)
print("The average number of comments during this period was: ")
print(sum(comment_totals) / len(comment_totals))