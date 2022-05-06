import random

def NorJokes():
       a=['A plateau is the highest form of flattery.','I used to think the brain was the most important organ. Then I thought, look what’s telling me that.','It’s hard to explain puns to kleptomaniacs because they always take things literally.',
            'Time flies like an arrow, fruit flies like a banana','The midget fortune teller who kills his customers is a small medium at large.',
            'A soldier survived mustard gas in battle, and then pepper spray by the police. He’s now a seasoned veteran.','A farmer in the field with his cows counted 196 of them, but when he rounded them up he had 200.',
            'What’s the best thing about Switzerland? I don’t know, but their flag is a huge plus.','A Buddhist walks up to a hotdog stand and says, Make me one with everything.',
            'I’m addicted to brake fluid, but I can stop whenever I want.','What is Bruce Lee’s favorite drink? Wataaaaah!','What’s the difference between my ex and the titanic? The titanic only went down on 1,000 people',
            'Why is 6 afraid of 7? Because 7 is a registered 6 offender.','I told my doctor that I broke my arm in two places. He told me to stop going to those places.',
            'If you want to catch a squirrel just climb a tree and act like a nut.','What do kids play when their mom is using the phone? Bored games.',
            'My grandad has the heart of a lion and a life time ban from the San Diego Zoo.','I went on a once in a lifetime holiday. Never again.',
            'Why did the bee get married? He found his honey.','Why are snails slow? Because they’re carrying a house on their back.',
            'Did you hear the rumor about the butter? Never mind, I shouldn’t spread it!','I asked my North Korean friend how it was there, he said he couldn’t complain.']
       x= random.choice(a)
       print(x)
def ProgJokes():
    b=['programmer is a machine, who converts coffee into code','programmer is a person who fixed a problem that you dont know you have, in a way you dont understand','algorithm is a word used by programmers when they dont want to explain what they did',
       'hardware is a part of computer that can you can kick','what is the object oriented to become wealthy. inheritance','what is the programmers favourite place to hangout place. foo bar','why did programmer quit his job. because he didnt get arrays',
       'teacher, o is false and 1 is true.right.everybody 1','what are similarities in both programs and air conditioners. they both become useless when you open window',
       'why do java programmers  use glass. because they dont see sharp.i mean c hash, a programming language','how you can tell h t m l from h t m l 5 . try it in internet explorer if it does not work than it is h t m l 5','real programmers count from 0',
       'chunk norris writes codes that optimizes itself','software developers like to solve problems. if they dont get any probelms . they will create their own problem','a programmer had a problem so he decided to use java. he now has a problem factory',
        '3 database s q l walked into a N o s q l bar. a little while late they walked out. because they counld not find table','Programming is like sex One mistake and you have to support it for the rest of your life',
       'How did the programmer die in the shower He read the shampoo bottle instructions: Lather. Rinse. Repeat.']
    y=random.choice(b)
    print(y)
def MathJokes():
    c=['How does a mathematician plow fields? With a pro tractor.','Parallel lines have so much in common It’s a shame they’ll never meet.',
       'What do you call more than one L. A parallel.','Why wasn’t the geometry teacher at school? Because she sprained her angle.','I had an argument with a 90° angle. It turns out it was right.','Did you hear about the over-educated circle. It has 360 degree',
     'What shape is usually waiting for you inside a Starbucks? A line.','Why doesn’t anybody talk to circles? Because there’s no point.','Why was the obtuse triangle always upset? Because it’s never right.',
     'What do geometry teachers have decorating their floor? Area rugs','What do mathematicians do after a snowstorm? Make snow angles','Why did the mathematician spill all of his food in the oven? The directions said, Put it in the oven at 180 degree.','Why was math class so long. The teacher kept going off on a tangent.']
    x1=random.choice(c)
    print(x1)
def WizzChallenge():
    questions=['Blindfolded drawing challenge.',' Pizza challenge.',' Chinese whisper challenge.','Toss and talk ball.',' Blind makeup challenge. ',
               'No thumbs challenge.','Pass the orange challenge','Jelly bean tasting challenge.', 'Try not to laugh challenge.','Seven-second challenge .','Memorize challenge.',
          ' guess who challenge .','Blindfolded food tasting challenge.','Guess the song.' ]

    rand_item=random.choice(questions)
    print(rand_item)

    if rand_item=='Blindfolded drawing challenge.':
        print('You would need a sheet of paper or a book and a pencil. The participants need to wear a blindfold and attempt to draw an object of their choice. Alternatively, before beginning each round, you can select a theme, such as fashion, kitchen, dinosaurs, spaghetti, animals, or famous characters, and challenge them further by setting a time limit.')
    elif rand_item=='Pizza challenge.':
        print('You need to get some ingredients, not necessarily pizza toppings, and place them in brown paper bags, so they’re not visible to the participants. If you have enough players, you can divide them into teams.')
    elif rand_item=='Chinese whisper challenge.':
         print('You have to get the children to sit in a circle. Ensure there’s enough distance maintained so the children cannot hear each other’s whisper. The person who starts has to think of something silly or complicated and whisper it to the person on their right. The whispering continues until it reaches the last player. Once it comes to the last player, they say the word or phrase out loud so everyone can hear how much it has changed from the first whisper. What you hear would surprise you!')
    elif rand_item=='Toss and talk ball.':
        print('''Take a plastic ball and write a bunch of questions all over it. Make the children sit in a circle and toss the ball around. When they catch the ball, they have to answer the question closest to their right index finger. After answering, they toss it again.
             Depending on the children’s age, the questions can be changed. You can go with your favorite color, favorite movie, a sports figure you would love to meet or name your best friend.''')
    elif rand_item=='Blind makeup challenge.':
         print('''You need to blindfold each participant and ask them to do their makeup themselves. The goal is to do a perfect makeup, but the outcome would be unexpected! You can also split the participants into teams, and the neatest result wins the challenge. Don’t forget to have a camera and plenty of makeup remover in hand. Also, adult supervision is recommended.

        ''')
    elif rand_item=='No thumbs challenge.':
         print('Tape the participants’ thumbs in a way they cannot use them. Once that’s done, give them a simple task such as open a door, put clothes on, eat a bowl of spaghetti, hold a pencil, or put on nail polish. Then sit back and watch as this simple task can become a lot more challenging and hilarious.')
    elif rand_item=='Pass the orange challenge':
        print(''' you will enjoy the activity. sit in a circle or stand in a line. The game is simple; you need to put an orange under the chin of the first person who must hold it using their chin and neck and then pass it to the next person in line, without using hands. The transfer has to be direct from neck to neck.
               If the orange falls, the team has to start all over. You can play this game in teams and see which team passes the orange down the line first. The game can even help to break the ice and improve relationships.''')
    elif rand_item=='Jelly bean tasting challenge.':
        print('If you’re crazy about jelly beans and can’t stop at just one, the challenge is for you. You would need a bunch of children and a bag of jelly beans. Each child has to close their eyes, taste one jelly bean, and guess the flavor. Record the answers to see who’s right and repeat the round.')
    elif rand_item=='Try not to laugh challenge.':
         print('You have to watch a funny video or a series of videos without grinning, laughing, or breaking into a smile. The first player to smile, grin, or laugh loses the game. Seems easy? It’s not that easy to keep a straight face!')
    elif rand_item=='Seven-second challenge .':
        print(''' Change your hair to a ponytail Add mascara with no mistakes. Close your eyes and open the SMS app on your phone. Count one to ten in a second language. Do ten standard push-ups. Put on lipstick without using any of your hands.
          Hop on one leg for 20 meters. Invent a challenge and do it. Name five countries in the EU. Name all the chess pieces. extra''')
    elif rand_item=='Memorize challenge.':
         print('''You can play the memory challenge in multiple ways. First, you can either play with different cards, keep them face down, and match the right ones. The other way is to listen to a part of a book/newspaper or magazine and then recite the same. You can even recite some themes/words/phrases in random, including spaghetti, flowers, fashion, fingers, mirror, or balls. Lastly, display some items and give them a time limit to memorize the order. Next, remove some items, and the participants have to guess the missing items.''')
    elif rand_item==' guess who challenge .':
        print('''You can play the challenge individually or in teams. If it’s individually, one participant goes up and makes an impression of selected characters, and the others guess. The person with the best impression wins the challenge. If it’s in teams, one team member goes up and makes an impression while the others from the same team take a guess. At the end of the game, the team with the highest number of correct guesses wins.
               You can base the themes on celebrities, musicians, animals, characters, friends, and presidents. For instance, imitate Mickey Mouse or make noises like a sheep. It’s a fun game that gets children moving and makes them think outside the box!''')
    elif rand_item=='Blindfolded food tasting challenge.':
        print('The challenge requires children to become blindfolded, taste different foods, and guess the name of the food. ')
    elif rand_item=='Guess the song.':
         print('''You would need two people to pair up. Both of them have to squeeze into one oversized T-shirt. Use the T-shirt to jumble your arms. Once the duo is ready, they have to perform tasks such as putting on makeup, drinking, eating, or brushing their teeth. You can think of some tasks that will make this challenge uber fun and even more entertaining. It’s best to have some parental supervision during this task.''')
def WizzQsn():
    questions=['WHAT DO YOU DO?','ARE YOU MARRIED?','WHY ARE YOU STUDYING ENGLISH?','HOW DID YOU LEARN ENGLISH?','WHAT DO YOU DO IN YOUR FREE TIME?',
               'WHAT IS THE WEATHER LIKE?','when you will be happy','HOW ARE YOU FEELING?', 'HOW WAS YOUR DAY?','which is your favourite subject','which is your favourite game',
               'Who is your best friend?','What time do you wake up?','What time do you have breakfast?','Where do you usually have breakfast','What time do you take a shower?',
               'What time do you start college?','What time do you start school?','Do you do exercises in the morning?','What time do you have lunch?','Where do you usually have lunch?','What time do you get home from school?','Do you do exercises in the afternoon',
               'What time do you go to bed?','Do you go to bed before midnight?','Do you go to bed past midnight?','What time do you have dinner?','Where do you usually have dinner?','Who do you have dinner with?',
               'What do you do in the evening?','What time do you get home from work?','Do you watch television at night','Do you go to the gym after work?','Do you go to the gym after school?' ]
    rand_qsn=random.choice(questions)
    print(rand_qsn)
