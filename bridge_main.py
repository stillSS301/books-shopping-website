from flask import Flask, render_template, request, url_for, session, redirect
import random
import webbrowser
import mysql.connector as s

passkey = input("Enter SQL Password AGAIN.....")

mycon=s.connect(host='localhost', user='root', passwd=passkey, database='mc1')

bridge = Flask(__name__, static_url_path='/static')

bridge.secret_key = 'project313'
app = Flask(__name__)
def details_():
    a1 = """Neharika Gupta is a writer, poet, yogi and martial arts practitioner. She worked in publishing for a year before shifting to writing full-time. She holds a B.A. (H) in English Literature from Lady Shri Ram College for Women and an M.A. in Creative Writing from Bath Spa University, UK."""
    s1 = """Social media manager and popular blogger Aisha is flirty and flamboyant … even as she battles personal demons that tell her she must stop eating if she wants to stay pretty.
    Ruhi couldn’t be more different from her friend Aisha. Working at Literacy Publishing, she feels grossly underappreciated by the editor-in-chief, who happens to be her mother. What keeps her going are her own ambitions – and her handsome author Tejas.
    Bestselling novelist Tejas has a bad case of writer’s block. He leans on Ruhi for emotional support before getting enamored by Aisha as he struggles to live up to everyone’s expectations, including his own."""
    a2 = """George R.R. Martin is the globally bestselling author of many fine novels, including A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, and A Dance with Dragons, which together make up the series A Song of Ice and Fire, on which HBO based the world’s most-watched television series, Game of Thrones. Other works set in or about Westeros include The World of Ice and Fire, and A Knight of the Seven Kingdoms. His science fiction novella Nightflyers has also been adapted as a television series; and he is the creator of the shared-world Wild Cards universe, working with the finest writers in the genre. He lives in Santa Fe, New Mexico."""
    s2 = """The first volume in Martin's first fantasy saga, A Song of Ice and Fire, combines intrigue, action, romance, and mystery in a family saga. The family is the Starks of Winterfell, a society in crisis due to climatic change that has created decades-long seasons, and a society almost without magic but with human perversity abundant and active. Martin reaches a new plateau in terms of narrative technique, action scenes, and integrating (or not injecting) his political views into the story. He does not avoid a dauntingly large cast and a daunting number of viewpoint shifts, but these are problems seemingly inseparable from the multivolume fantasy genre. Accordingly, one doubts there will be any other comfortable entry point into this example of the genre except at the beginning. Judging by this beginning, however, it promises to repay reading and rereading, from first volume to last, on account of its literacy, imagination, emotional impact, and superb world-building."""
    a3 = """Sabyn Javeri was born in Pakistan and now lives between London and Karachi, where she teaches Creative Writing at the university level. A graduate of the University of Oxford, she has a PhD from the University of Leicester."""
    s3 = """The nation sinks deep into mourning as news of former Prime Minister Rani Shah’s assassination arrives. Intelligence agencies, opposition leaders, the army top brass, her closest relatives – all seem to be shifting in their chairs even as special investigative teams gear up to file a report. Conspiracy theories abound for there were many who stood to gain if she pulled out of the imminent elections. The needle of suspicion points most immediately to Madam Shah’s close confidante Nazneen Khan, who was seen sitting right beside her in the convoy and, oddly, escaped the bomb blast unscathed. Sabyn Javeri’s tale of intense friendship between two ambitious women unfolds in a country steeped in fanaticism and patriarchy. Set against a backdrop of intrigue and political machinations, this is a novel about love, loyalty, obsession, and deception."""
    a4 = """Zarreen Khan has previously worked for brands such as Pepsi, Hindustan Times and AC Nielson. She is currently enjoying her break raising two children, while also working as a marketing consultant. In the little time that she gets away from her two roles, she likes to channel her inner writer and pen hilarious yet relatable works of fiction."""
    s4 = """When Mona Mathur of Dehradun had married her college sweetheart Ramit Deol of Amritsar, there were two things she wasn’t prepared for:1. The size of the Deol family – it put any Sooraj Barjatiya movie to shame2. The fertility of the Deol family – they reproduce faster than any other species are known to mankind for four years now, Mona and Ramit have done the unthinkable and remained childless. Of course, that also means that they’ve battled that one question day in and day out: ‘Koi Good News?’ It doesn’t matter that they have been happy to be child-free – they are married; they are expected to make babies. After all, there are grandparents, great-grandparents, uncles, aunts, and even colony aunties in waiting."""
    a5 = """Ravinder Singh (born 4 February 1982) is an Indian software engineer and author of nine novels — I Too Had a Love Story, Can Love Happen Twice?, Like it happened Yesterday, Love Stories That Touched My Heart, Tell Me A Story, Your Dreams are Mine Now, This Love That Feels Right, Will You Still Love Me? and The Belated Bachelor Party."""
    s5 = """It’s been twelve years since Happy, MP, Raamji and Ravin graduated. Well into their married lives, they realize that none of them had a bachelor party before their weddings.But it’s never too late to set things right. They go about planning their belated bachelor party – a Euro trip which, well, ends up becoming the trip of their lifetime.Picture this: It’s the middle of the night. The four friends wait to be strip-searched by the border police. They are stuck in the no-man’s land between Croatia and Slovenia, without valid visas, but with banned party drugs and a rifle cartridge ."""
    a6 = """Winner of the Juggernaut Short Story Prize (2017), Shuma Raha is the author of The Love Song of Maya K and Other Stories (2018). A journalist formerly with The Telegraph and The Times of India, she continues to write columns for publications in India and abroad."""
    s6 = """There is nothing really wrong with Priya Bakshi and Akash Srivastav’s six-year-old marriage … except that Priya is having an affair. And Akash, too, seems to be on the lookout for sexual adventure. When Tarun, their richer, older, and manipulative friend, tells them about Delhi’s couple-swapping parties, Akash wants to jump right in. With some reluctance, Priya agrees to give him company. Soon, Priya and Akash find themselves in a world of swinging couples and sexual abandon, joined by friends who are equally keen to test the waters. But as the clothes come off and the secrets begin to tumble out, it seems that none of them will emerge unscathed.Witty and racy, The Swap is a sparkling social novel about sex, marriage, and morality."""
    a7 = """Manu Joseph is an Indian journalist and writer. He was born on July 22, 1974. Joseph is the former editor of Open magazine. He is also a novelist and a columnist for Mint. Joseph has previously worked for the New York Times. He is the creator of the Netflix series, ‘Decoupled’."""
    s7 = """Read before you watch the Netflix series starring Nawazuddin Siddiqui!
    All a man really wants is to be greater than his friends. Such is the belief of Ayyan Mani, who spends his time dreaming up ways to elevate himself above the banality of everyday life in the Mumbai chawls. But this time he’s hit the jackpot with a ruse so brilliant, it can’t possibly fail. All it needs is a little subterfuge and a willing partner-in-crime in the form of his eleven-year-old son, who is a genius. At least that’s what his teachers think. But father and son might have gone a step too far, as they set in motion a chain of extraordinary events they are unable to stop."""
    a8 = """Aravind Adiga was born in Madras (now Chennai) on 23 October 1974 to Dr. K. Madhava Adiga and Usha Adiga from Mangalore. His paternal grandfather was K. Suryanarayana Adiga, former chairman of Karnataka Bank, and maternal great-grandfather, U. Rama Rao, was a popular medical practitioner and Congress politician from Madras."""
    s8 = """Now a major Netflix series! A page-turner of a novel set in the world of cricket in Mumbai Fourteen-year-old Manjunath Kumar knows that he is good at cricket – even if he’s not as good as his elder brother Radha. He knows that he fears and resents his cricket-obsessed father. But there are many things about himself and the world that he doesn’t know. When he meets Radha’s great rival – a boy as privileged and confident as Manju is not – everything in his world begins to change, and he is faced with decisions that will change his sense of self forever."""
    a9 = """Aravind Adiga was born in Madras (now Chennai) on 23 October 1974 to Dr. K. Madhava Adiga and Usha Adiga from Mangalore. His paternal grandfather was K. Suryanarayana Adiga, former chairman of Karnataka Bank, and maternal great-grandfather, U. Rama Rao, was a popular medical practitioner and Congress politician from Madras."""
    s9 = """Winner of the 2008 Booker Prize, now a major Netflix film starring Priyanka Chopra and Rajkumar RaoMeet Balram Halwai, the ‘white tiger’: servant, philosopher, entrepreneur, murderer…
    The White Tiger is a tale of two Indias. Balram’s journey from the darkness of village life to the light of entrepreneurial success is utterly amoral, brilliantly irreverent, deeply endearing, and altogether unforgettable."""
    a10 = """Harikumar Krishnamoorthy (born 3 January 1989), better known as K. Hari Kumar, is an Indian novelist and screenwriter born in Cochin and brought up in Gurgaon. He did his schooling from DAV Public School. His first book When Strangers Meet was published in 2013, followed by That Frequent Visitor (2015), A Game of Gods (2016) and The Other Side Of Her (2018)."""
    s10 = """There are places where the past lingers, making shapes in the moonlight and blowing in the curtains even as the air goes suddenly still. K. Hari Kumar, the bestselling author of spine-chilling horror fiction, brings you the terrifying tales of some of India’s most haunted places – including Bhangarh Fort, Malabar Hill’s Tower of Silence, and Jammu and Kashmir’s notorious Khooni Nala. Whether you read them at night or in daylight, these stories will remain with you long after you’ve turned the last page."""
    a11 = """Kiran Nagarkar (2 April 1942 – 5 September 2019) was an Indian novelist, playwright and screenwriter. A noted drama and film critic, he was one of the most significant writers of post-colonial India. Amongst his notable works are Saat Sakkam Trechalis (tr. Seven Sixes Are Forty Three) (1974), Ravan and Eddie (1994) manymore."""
    s11 = """The time is the early 16th century. The Rajput kingdom of Mewar is at the height of its power. It is locked in a war with the Sultanates of Delhi, Gujarat, and Malwa. But there is another deadly battle being waged within Mewar itself. who will inherit the throne after the death of the Maharana? The course of history, not just of Mewar but of the whole of India, is about to be changed forever."""
    a12 = """Pankaj Kapur (born 1954) is an acclaimed Indian theatre, television and film actor and director. He has won numerous awards for his work, including three National Film Awards and one Filmfare Award. Dopehri is his first novel."""
    s12 = """Amma Bi is an elderly widow who lives alone in her deserted Lucknow haveli. Every afternoon, at precisely 3 o’clock, she hears the sound of unknown footsteps. Every afternoon, she peeks out … but no one is there. In a state of growing panic, Amma Bi considers moving to an old people’s home, before finally taking in a lodger — a winsome young woman named Sabiha. Her arrival fills Amma Bi’s lonely world with love and laughter, and Jumman, the household help, is transformed as well. When Sabiha finds herself in trouble, Amma Bi must draw on hidden reserves of skill and empathy in order to resolve the situation."""
    a13 = """Farrukh Dhondy is an Indian-born British writer, playwright, screenwriter and left-wing activist. He has been active in Britain since the mid 1970s. Dhondy is especially known for his provocative young adult fiction, and his role in shaping British television viewing habits."""
    s13 = """Marked by the lyrical beauty and spiritual insight, a deep understanding of human suffering that coexists with rapturous abandon, the poems of Jalaluddin Rumi continue to be relevant almost eight centuries after they were composed, with contemporary audiences finding new meanings in them. Rumi’s poems bring together the divine and the human, the mystical and the corporeal to create a vivid kaleidoscope of poetic images."""
    a14 = """Chitra Banerjee Divakaruni is an Indian-born American author, poet, and the Betty and Gene McDavid Professor of Writing at the University of Houston Creative Writing Program1. She was born in Calcutta, India in 19561. She received her B.A. from the University of Calcutta in 1976 and a PhD in English from the University of California, Berkeley in 1985."""
    s14 = """In this brilliant retelling of the Ramayana, Chitra Banerjee Divakaruni places Sita at the centre of the novel: this is Sita’s version. The Forest of Enchantments is also a very human story of some of the other women in the epic, often misunderstood and relegated to the margins: Kaikeyi, Surpanakha, Mandodari. A powerful comment on duty, betrayal, infidelity, and honour, it is also about women’s struggle to retain autonomy in a world that privileges men, as Chitra transforms an ancient story into a gripping, contemporary battle of wills."""
    a15 = """Indu Sundaresan is the author of six books so far. Her works include the Taj Mahal trilogy, which consists of The Twentieth Wife (2002), The Feast of Roses (2003), and Shadow Princess (2010). She has also written a collection of short stories, In the Convent of Little Flowers, and two standalone novels: The Splendor of Silence (2006) and The Mountain of Light (2013)."""
    s15 = """Mehrunnisa – the Sun of Women – one of India’s most legendary and controversial empresses … a woman who overcame insurmountable obstacles through sheer brilliance and determination … whose love shaped the course of the Mughal Empire. She is the twentieth wife. The daughter of refugees from Persia, growing up on the fringes of Emperor Akbar’s opulent palace grounds, Mehrunnisa first encounters Prince Salim on his wedding day. Eight years old at the time, she decides that she too will one day become Salim’s wife – unaware of the great price she and her family will pay for this dream."""
    a16 = """Aravind Adiga was born in Madras (now Chennai) on 23 October 1974 to Dr. K. Madhava Adiga and Usha Adiga from Mangalore. His paternal grandfather was K. Suryanarayana Adiga, former chairman of Karnataka Bank, and maternal great-grandfather, U. Rama Rao, was a popular medical practitioner and Congress politician from Madras."""
    s16 = """Winner of the 2008 Booker Prize, now a major Netflix film starring Priyanka Chopra and Rajkumar RaoMeet Balram Halwai, the ‘white tiger’: servant, philosopher, entrepreneur, murderer…
    The White Tiger is a tale of two Indias. Balram’s journey from the darkness of village life to the light of entrepreneurial success is utterly amoral, brilliantly irreverent, deeply endearing, and altogether unforgettable."""
    a17 = """Harikumar Krishnamoorthy (born 3 January 1989), better known as K. Hari Kumar, is an Indian novelist and screenwriter born in Cochin and brought up in Gurgaon. He did his schooling from DAV Public School. His first book When Strangers Meet was published in 2013, followed by That Frequent Visitor (2015), A Game of Gods (2016) and The Other Side Of Her (2018)."""
    s17 = """There are places where the past lingers, making shapes in the moonlight and blowing in the curtains even as the air goes suddenly still. K. Hari Kumar, the bestselling author of spine-chilling horror fiction, brings you the terrifying tales of some of India’s most haunted places – including Bhangarh Fort, Malabar Hill’s Tower of Silence, and Jammu and Kashmir’s notorious Khooni Nala. Whether you read them at night or in daylight, these stories will remain with you long after you’ve turned the last page."""
    a18 = """Kiran Nagarkar (2 April 1942 – 5 September 2019) was an Indian novelist, playwright and screenwriter. A noted drama and film critic, he was one of the most significant writers of post-colonial India. Amongst his notable works are Saat Sakkam Trechalis (tr. Seven Sixes Are Forty Three) (1974), Ravan and Eddie (1994) manymore."""
    s18 = """The time is the early 16th century. The Rajput kingdom of Mewar is at the height of its power. It is locked in a war with the Sultanates of Delhi, Gujarat, and Malwa. But there is another deadly battle being waged within Mewar itself. who will inherit the throne after the death of the Maharana? The course of history, not just of Mewar but of the whole of India, is about to be changed forever."""
    a19 = """Winner of the Juggernaut Short Story Prize (2017), Shuma Raha is the author of The Love Song of Maya K and Other Stories (2018). A journalist formerly with The Telegraph and The Times of India, she continues to write columns for publications in India and abroad."""
    s19 = """There is nothing really wrong with Priya Bakshi and Akash Srivastav’s six-year-old marriage … except that Priya is having an affair. And Akash, too, seems to be on the lookout for sexual adventure. When Tarun, their richer, older, and manipulative friend, tells them about Delhi’s couple-swapping parties, Akash wants to jump right in. With some reluctance, Priya agrees to give him company. Soon, Priya and Akash find themselves in a world of swinging couples and sexual abandon, joined by friends who are equally keen to test the waters. But as the clothes come off and the secrets begin to tumble out, it seems that none of them will emerge unscathed.Witty and racy, The Swap is a sparkling social novel about sex, marriage, and morality."""
    a20 = """Manu Joseph is an Indian journalist and writer. He was born on July 22, 1974. Joseph is the former editor of Open magazine. He is also a novelist and a columnist for Mint. Joseph has previously worked for the New York Times. He is the creator of the Netflix series, ‘Decoupled’."""
    s20 = """Read before you watch the Netflix series starring Nawazuddin Siddiqui!
    All a man really wants is to be greater than his friends. Such is the belief of Ayyan Mani, who spends his time dreaming up ways to elevate himself above the banality of everyday life in the Mumbai chawls. But this time he’s hit the jackpot with a ruse so brilliant, it can’t possibly fail. All it needs is a little subterfuge and a willing partner-in-crime in the form of his eleven-year-old son, who is a genius. At least that’s what his teachers think. But father and son might have gone a step too far, as they set in motion a chain of extraordinary events they are unable to stop."""
    a21 = """Aravind Adiga was born in Madras (now Chennai) on 23 October 1974 to Dr. K. Madhava Adiga and Usha Adiga from Mangalore. His paternal grandfather was K. Suryanarayana Adiga, former chairman of Karnataka Bank, and maternal great-grandfather, U. Rama Rao, was a popular medical practitioner and Congress politician from Madras."""
    s21 = """Now a major Netflix series! A page-turner of a novel set in the world of cricket in Mumbai Fourteen-year-old Manjunath Kumar knows that he is good at cricket – even if he’s not as good as his elder brother Radha. He knows that he fears and resents his cricket-obsessed father. But there are many things about himself and the world that he doesn’t know. When he meets Radha’s great rival – a boy as privileged and confident as Manju is not – everything in his world begins to change, and he is faced with decisions that will change his sense of self forever."""
    a22 = """Balli Kaur Jaswal is a Singaporean novelist, having family roots in Punjab. Her first novel Inheritance won the Sydney Morning Herald's Best Young Australian Novelist Award in 2014, and was adapted for a film presented at the 2017 Singapore International Festival of the Arts. Her second novel Sugarbread was a finalist for the 2015 inaugural Epigram Books Fiction Prize. Her third novel, Erotic Stories for Punjabi Widows was released in 2017, and garnered her a wider international following, driven in part by being picked as a selection for Reese Witherspoon's Hello Sunshine online book club"""
    s22 = """The Shergill sisters never needed each other–until they did. Rajni, Jezmeen, and Shirina Shergill have never been close but when their mother dies, she has only one request: that they take a pilgrimage across India to carry out her final rites. While an extended family holiday is the last thing they want, each sister has her own reasons to run away from her life. Rajni is the archetypal know-it-all eldest but her son dropped a bombshell before she left and, for the first time, she doesn’t know what the future holds. Middle sister Jezmeen, always a loudmouth, has translated her need for attention into life as a struggling actress. But her career is on the skids after an incident went viral and now she’s desperate to find her voice again. Shirina, the golden child, has confounded expectations by having an arranged marriage and moving to the other side of the world."""
    a23 = """Madhuri Vijay is an Indian author who won the second JCB Prize for Literature, India’s most prestigious literary award, for her debut novel, The Far Field . She was born and raised in Bangalore, India, and currently resides in Hawaii, where she teaches English 12. She graduated Phi Beta Kappa from Lawrence University, where she studied psychology and English ."""
    s23 = """With rare acumen and evocative prose, in The Far Field Madhuri Vijay gives a potent critique of Indian politics and class prejudice through the lens of a guileless outsider, while also offering up a profound meditation on grief, guilt and the limits of compassion."""
    a24 = """ehana Munir ran a bookshop in Bombay in the mid 2000s, a few years after graduating with top honours in English literature from St. Xavier's College. An independent writer on culture and lifestyle, she has a weekly humour column in HT Brunch, and a cinema column in Arts Illustrated magazine. She is also an occasional copywriter."""
    s24 = """When her estranged father passes away, Fiza, fresh out of college, discovers that he has left her a tidy sum in the hope that she will open a bookshop… Overnight, Fiza’s placid life is thrown into a whirl of decor decisions and book-buying sprees, unconventional staff and colourful patrons, small pleasures and little heartbreaks, as the store — Paper Moon — begins to take shape in a charming, old Bandra mansion. To top it all, she is being wooed by Iqbal, a mysterious customer who frequents the shop, and Dhruv, her ex-boyfriend, her feelings for whom are still confused."""
    d1 = [s1,a1]
    d2 = [s2,a2]
    d3 = [s3,a3]
    d4 = [s4,a4]
    d5 = [s5,a5]
    d6 = [s6,a6]
    d7 = [s7,a7]
    d8 = [s8,a8]
    d9 = [s9,a9]
    d10 = [s10,a10]
    d11 = [s11,a11]
    d12 = [s12,a12]
    d13 = [s13,a13]
    d14 = [s14,a14]
    d15 = [s15,a15]
    d16 = [s16,a16]
    d17 = [s17,a17]
    d18 = [s18,a18]
    d19 = [s19,a19]
    d20 = [s20,a20]
    d21 = [s21,a21]
    d22 = [s22,a22]
    d23 = [s23,a23]
    d24 = [s24,a24]
    details = [d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24]
    return details
def cart_html(rows,style):
    
    if not registered():
        c = f"""<a href="{url_for('reg_login', button='login')}">Sign In</a>
            <a href="{url_for('reg_login', button='register')}">Join</a>
                """
    if registered():
        a = session['user_data']
        a[1] = a[1].capitalize()
        c = f"""<a href="{url_for('about')}"><div class = "log">{a[1]}</div></a>"""
        
        
    html = f"""
            <html>
            <head>
            <title>NovelNest</title>
            </head>
            <style>
            {style}
            </style>
            <body>
            <div class="topnav">
              {c}
              <a href="{url_for('home')}">Home</a>
              <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
            </div>
            <br>
            <h1>CART</h1>
            <div class='cart'>
            <form method="post" action="{url_for('final_call')}">
            <table border="1">
            <tr>
            <th>Id</th>
            <th>Product</th>
            <th>Qty.</th>
            <th>Rate</th>
            <th>Amount</th>
            <th>Action</th>
            </tr>
            """
    sum = 0
    for row in rows:
        product_id, product_name, quantity, rate, amount = row
        sum = sum + amount
        html += f"""
                <tr>
                <td>{product_id}</td>
                <td>{product_name}</td>
                <td>{quantity}</td>
                <td>&#8377;{rate}</td>
                <td>&#8377;{amount}</td>
                <td>
                <input type="hidden" name="product_id_{product_id}" value="{product_id}">
                <button type="submit" name="action_{product_id}" value="plus">+</button>
                <button type="submit" name="action_{product_id}" value="minus">-</button>
                <button type="submit" name="action_{product_id}" value="remove">x</button>
                </td>
                </tr>
                """
    html += f"""
            </table>
            </form>
            </div>
            <div class = "cart_out">
            <h3>Total- &#8377;{sum}.00/-</h3>
            </div>
            <br>
            <div class = "checkout-button"><a href="{url_for('final_call', button='checkout')}"><center>Checkout</center></a></div>
            </body>
            </html>
            """
    return html
def out_html(rows,style):  
    a = session['user_data']
    html = f"""
            <html>
            <head>
            <title>NovelNest</title>
            </head>
            <style>
            {style}
            </style>
            <body>
            <br>
            <br>
            <br>
            <div>
            <h1>SUCCESS</h1>
            <table class = 'order'>     
            <tr>
            <th>Id</th>
            <th>Product</th>
            <th>Qty.</th>
            <th>Rate</th>
            <th>Amount</th>
            </tr>
            """
    sum = 0
    for row in rows:
        product_id, product_name, quantity, rate, amount = row
        sum = sum + amount
        html += f"""
                <tr>
                <td>{product_id}</td>
                <td>{product_name}</td>
                <td>{quantity}</td>
                <td>&#8377;{rate}</td>
                <td>&#8377;{amount}</td>
                </tr>
                """
    html += f"""
            <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td><b>Total:-</b></td>
            <td><b>&#8377;{sum}</b></td>
            </tr>
            </table>
            <h1>Shipping Details:</h1>
            <h3>Shipped to:</h3>
            <b>User ID:</b> {a[0]}<br>
            <b>User Name:</b> {a[1]}<br>
            <b>Address:</b> {a[4]}, {a[5]}, {a[6]}<br><br>
            <h3>Shipped from:</h3>
            <b>Publisher:</b> HarperCollins India<br>
            <b>Location:</b> NovelNest Main Unit India<br>
            <b>Address:</b> Golf Course Road, 110003, Delhi
            </div>
            <br><br><br><br>
            <h5>**all orders are dilivered within time period of seven days.**</h5>
            <h2><a href="{url_for('home')}">Return to Home Page.</a></h2>
            </body>
            </html>
            """
    return html
def registered():
    return 'user_data' in session
def prod_loc():
    return 'prod' in session

def prod_id():
    if mycon.is_connected():
        cursor=mycon.cursor()
    pid ="select pid from product"
    cursor.execute(pid)
    data=cursor.fetchall()
    count=cursor.rowcount
    plist = []
    for i in data:
        i = list(i)
        pd = str(i[0])
        plist.append(pd)
    return plist  
def nr_list():
    if mycon.is_connected():
        cursor=mycon.cursor()
    nrd ="select pname, rate from product"
    cursor.execute(nrd)
    datan=cursor.fetchall()
    count=cursor.rowcount
    nrlist = []
    for i in datan:
        nrlist.append(i)
    return nrlist
        
    
def clist():
    session['cart_list'] = cart = []
    return cart
def css():
    return """* body {
                font-family: 'OCR A Std', monospace;
                margin: 0;
                padding: 0;
                display: flex;
                min-height: 250mm;
                align-items: center;
                flex-direction: column;
                background-color: #121212;
                width:1920px;
                position: relative;    
                color: white;   
                }
                h3{
                color: white;
                }
                .body-text {
                display: flex;
                font-family: "Montserrat", sans-serif;
                align-items: center;
                justify-content: center;
                margin-top: 250px;
                }
                .topnav {
                position: absolute;
                background-color: #333;
                overflow: hidden;
                width:100%;
                position: sticky;
                top: 0;
                z-index: 100;
                }
                .topnav a {
                float: right;
                color: #f2f2f2;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;

                font-size: 18px;
                font-family: 'OCR A Std', monospace; 
                }
                .log {
                float: right;
                color: #f2f2f2;
                text-align: center;
                text-decoration: none;
                color: #f57b7b;
                font-size: 17px;
                font-style: oblique;
                font-weight: bold;
                font-family: 'OCR A Std', monospace;    
                }
                .log:hover {
                background-color: transperent;
                color: #ff0000;
                }
                .topnav a:hover {
                background-color: transperent;
                color: #f57b7b;
                }
                .topnav a.split {
                margin-left: 10mm;
                background-color: #1F1F1F;
                font-family: Verdana, sans-serif;
                float: left;
                color: #550f0f;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 10px;
                font-size: 20px;
                background-color: #f57b7b;
                }
                .parent {
                display: flex;
                height: 180mm;
                justify-content: center; 
                width: 100%;
                background-image: url('/static/parent.jpg'); 
                justify-content: space-around;
                align-items: center;
                flex-wrap: wrap;
                }
                .flex-container {
                flex-direction: row;
                display: flex;
                justify-content: space-around;
                align-items: center;
                flex-wrap: wrap;
                max-width: 400mm;
                background-color: transperent;
                margin-top: 113.8mm;
                }
                .detail_container {
                display: flex;
                flex-direction: column;
                float: left;
                margin-left: -25mm;
                width:475mm;
                }

                .flex-item {
                position: relative;
                background-color: #483332 ;
                width: 80mm;
                height: 135mm;
                margin: 0.5mm;
                margin-bottom: 10mm;
                aspect-ratio: 1 : 1;
                box-sizing: border-box;
                text-align: center;
                text-overflow: ellipsis;
                flex-wrap = norap;
                font-size: 17px;
                font-family: 'OCR A Std', monospace;
                }
                .detail_container h1 {

                background-color:transperent;
                height: 20mm;
                padding: 50px;
                font-size: 50px;
                color: #f57b7b;
                margin-bottom: -40mm;
                margin-top: -5mm;
                width: 100%;
                }
                .detail_containerr {
                display: flex;
                border-radius: 20px;
                flex-direction: column;
                background-color:#312322;
                width:380mm;
                margin-top: 18mm;
                margin-left:-100mm;
                }
                .detail_containerr h2 {
                background-color:transperent;
                height: 20mm;
                padding: 50px;
                text-align: left;
                color: #f57b7b;
                margin-bottom: -31mm;
                margin-top: -5mm;
                width: 60%;   
                }
                .detail_containerrr {
                display: flex;  
                border-radius: 20px;
                flex-direction: column;
                background-color:#312322;
                width:380mm;
                margin-top: 18mm;
                margin-left:-100mm;
                } 
                .detail_containerrr h2 {
                background-color:transperent;
                height: 20mm;
                padding: 13.229mm;
                text-align: left;
                color: #f57b7b;
                margin-bottom: -31mm;
                margin-top: -5mm;
                width: 60%;
                }
                .about_parent {
                display: flex;
                gap: 20px;
                margin-left: 100mm;
                }
                .detail_containerr p {
                background-color:transperent;
                height: 30mm;
                padding: 50px;
                font-size: 20px;
                color: white;
                width: 90%;
                margin-left: 10mm;
                margin-top: -5mm;
                }
                .detail_containerrr p {
                background-color:transperent;
                height: 30mm;
                padding: 13.229mm;
                gap: 15px;
                font-size: 20px;
                color: white;
                width: 90%;
                margin-left: 10mm;
                margin-top: -5mm;
                margin-bottom: -15mm; 
                }
                hr {
                margin-top: 20mm;
                width: 475mm;
                color: white;
                height: 4px;
                background-color: white;
                border-radius: 100px;
                }
                .detail_container a {
                color: red;
                margin-left: 360mm;
                }
                .check_container {
                display: flex;
                border-radius: 20px;
                flex-direction: column;
                background-color:#312322;
                width:90mm;
                height: 100mm;
                margin-top: 18mm;
                }
                .check_container h1{
                color: #f57b7b;
                }
                .check_containerq {
                display: flex;
                border-radius: 20px;
                flex-direction: column;
                background-color:#312322;
                width:90mm;
                height: 115mm;
                margin-top: 18mm;

                }
                .check_containerq h1{
                color: #f57b7b; 
                }
                .check_containerr {
                display: flex;
                border-radius: 20px;
                flex-direction: column;
                background-color:#312322;
                width:90mm;
                height: 83mm;
                margin-top: 18mm;
                }
                .check_containerr h1{
                color: #f57b7b;
                }
                .flex-item a {
                position: absolute;
                display: block;
                width: 100%;
                height: 100%;
                }
                .flex-item img {
                width: 100%;
                height: 85%;
                object-fit: cover; 
                }
                .flex-nav {
                position: absolute;
                display: flex;
                background-image: url('/static/home2.png'); 
                min-width: 100%;
                flex-direction: column;
                height: 90mm;
                justify-content: space-around;
                align-items: center;
                flex-wrap: wrap;
                margin-top: 13.8mm;
                }
                .catalog {
                position: absolute;
                display: flex;
                flex-direction: column;
                width: 100%;
                height: 15mm;
                justify-content: space-around;
                align-items: center;
                flex-wrap: wrap;
                margin-top: 103.8mm;
                z-index: 97;
                }
                .catalog2 {
                position: absolute;
                display: flex;
                background-color:red; 
                min-width: 100%;
                flex-direction: column;
                height: 6mm;
                justify-content: space-around;
                align-items: center;
                flex-wrap: wrap;
                margin-top: -84mm;
                z-index: 98;
                }
                .quote{
                position: absolute;
                background-color:transperent;
                height: 35mm;
                text-align: right;
                font-size: 50px;
                color: white;
                width: 170mm;
                margin-left: 320mm;
                margin-top: 35mm;
                margin-bottom: -15mm;
                font-family: Georgia, serif;
                z-index:99;
                }
                .quote b{
                color: #CF6679;
                }
                .cat_item{
                display: flex;
                gap: 290mm;
                width: 15mm;
                height: 2mm;
                aspect-ratio: 1:1;
                z-index: 50;
                margin-left: -233mm;
                }
                .flex-nav h1{
                font-family: Georgia, serif;
                font-size: 66px;  
                width: 50%;
                margin-left: -240mm; 
                }
                .flex-nav u{
                color: #CF6679; 
                }
                .prof{
                display: flex;
                border-radius: 20px;
                flex-direction: column;
                background-color:#312322;
                width:380mm;
                height: 150mm;
                margin-top: 100mm;
                }
                .footer {
                display: flex;
                background-image: url('/static/footer.png'); 
                min-width: 100%;
                font-size: 18px;
                height: 145mm;
                justify-content: space-around;
                align-items: left;
                flex-wrap: wrap;
                }
                .out {
                display: flex;
                justify-content: space-around;
                align-items: center;
                height: 20mm;
                background-image: url('/static/out.png'); 
                font-family: "Montserrat", sans-serif;
                flex-wrap: wrap;
                width: 100%;
                }
                .out-in {
                display: flex;
                justify-content: space-around;
                align-items: center;
                height: 20mm;
                background-color: transperent;
                font-family: "Montserrat", sans-serif;
                flex-wrap: wrap;
                width: 50mm;
                }
                .flex-fout {
                display: flex;
                background-color: #CF6679;
                min-width: 170mm;
                font-size: 18px;
                height: 170mm;
                justify-content: center;
                align-items: center;
                flex-wrap: wrap;  
                }
                .flex-fout img {
                min-width: 170mm;
                height: 100%;
                object-fit: cover; 
                }
                .out-item {
                background-color: #CF6679 ;
                width: 15mm;
                height: 15mm;
                aspect-ratio: 1 : 1; 
                box-sizing: border-box;
                }
                .out-item img {
                width: 15mm;
                height: 15mm;
                aspect-ratio: 1 : 1;
                object-fit: cover; 
                }
                .out-item a {
                display: block;
                width: 15mm;
                height: 15mm;
                aspect-ratio: 1 : 1;
                }
                .cart {
                flex-direction: row;
                display: flex;
                justify-content: space-around;
                align-items: flex-start;
                flex-wrap: wrap;
                width: 260mm;
                background-color: #1D1515;
                height: 200mm; 
                }
                .cart_out {
                display: flex;
                flex-direction: column;
                justify-content: space-around;
                padding-right: 10mm;
                align-items: flex-end;
                height: 10mm;
                background-color: #641E16; 
                font-family: "Montserrat", sans-serif;
                flex-wrap: wrap;
                width: 250mm;

                }
                .checkout {
                position: relative;
                display: flex;
                flex-direction: column;
                justify-content: space-around;
                padding: 5mm;
                align-items: center;
                height: 10mm;
                background-color: #E74C3C; 
                font-family: "Montserrat", sans-serif;
                flex-wrap: wrap;
                width: 35mm;
                margin-left: 215mm;
                }
                h2 {
                text-shadow: 2px 2px 8px black;
                }
                .overlay-box a{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background-color: transperent;
                margin-top: 13.8mm;
                display: flex;
                align-items: center;
                justify-content: center;
                }
                table {
                width: 260mm;
                max-height: 258mm;
                border-collapse: collapse;
                }
                th {
                height: 70px;
                background-color: #641E16;
                color: white;
                padding: 15px;
                text-align: left;
                }
                td {
                padding: 15px;
                text-align: left;
                background-color: #1D1515;
                color: white;
                padding: 15px;
                text-align: left;
                }
                .order {
                width: 200mm;
                max-height: 258mm;
                }
                .order th {
                height: 40px;
                background-color: #1D1515;
                color: white;
                padding: 15px;
                text-align: center;
                border-bottom: 1px solid #ddd;
                }
                .order td {
                background-color: #1D1515;
                color: white;
                border-bottom: 1px solid #ddd;
                text-align: center;
                }
                .capsule-button {
                display: inline-block;
                padding: 10px 20px;
                background-color: #fff; 
                border: 2px solid #fff;
                border-radius: 30px;
                color: #333; 
                text-decoration: none;
                font-weight: bold;
                transition: background-color 0.3s, color 0.3s;
                width: 40%;
                }
                .logout-button {
                display: inline-block;
                padding: 10px 20px;
                background-color: #fff; 
                border: 2px solid #fff;
                border-radius: 30px;
                color: #333; 
                text-decoration: none;
                font-weight: bold;
                transition: background-color 0.3s, color 0.3s;
                width: 10%;
                margin-left: 325mm;
                }
                .checkout-button {
                display: inline-block;
                padding: 15px 25px;
                background-color:  #641E16; 
                border: 2px solid  #ffffff;
                border-radius: 30px;
                color: #fff; 
                text-decoration: none;
                font-weight: bold;
                transition: background-color 0.3s, color 0.3s;
                width: 20mm;
                margin-left: 225mm;
                }
                .capsule-button:hover {
                background-color: #f57b7b;
                border: 2px solid #f57b7b;
                color: #fff; /
                }
                .capsule-button a{
                text-decoration: none;
                color: black;
                }
                .logout-button:hover {
                background-color: #f57b7b;
                border: 2px solid #f57b7b;
                color: #fff; /
                }
                .checkout-button:hover {
                background-color: #f57b7b;
                border: 2px solid #f57b7b;
                color: #fff; /
                }
                .logout-button a{
                text-decoration: none;
                color: black;
                }
                .checkout-button a{
                text-decoration: none;
                color: white;
                }
                .custom-input {
                width: 90mm; 
                padding: 5px;
                border-radius: 5px;
                font-size: 16px; 
                margin-top:5px;
                background-color: #f0dcdc;
                border: 2px solid #fff;
                }
                .rlform {
                max-width: 400px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #312322;
                background-color: #312322;
                border-radius: 20px;
                box-shadow: 10px 10px 20px black;
                }
                """


@bridge.route('/')
def home():
    style = css()
    plist = prod_id()
    if not registered():
        
        return f"""<html>
                    <head>
                    <title>NovelNest</title>
                    </head>
                    <style>
                    {style}
                    </style>
                    <body>
                     <div class="topnav">
                      <a href="{url_for('reg_login', button='login')}">Sign in</a>
                      <a href="{url_for('reg_login', button='register')}">Join</a>  
                      <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                    </div>
                    </h1></div>
                    <div class = "quote">
                    BUY<br>
                    <i><b>READ</b></i><br>
                    REPEAT
                    </div>
                    <div class="flex-nav">
                    <div class = "catalog2"><marquee><b>Unleash the reader in you, and embark on a journey through the boundless realms of imagination. Welcome to NovelNest, where stories come alive!</b> </marquee></div>
                    <h1>
                    <i>EXPLORE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; YOUR <u>LITERARY</u> PARADISE.</i> 
                    </h1>
                    </div>
                    <div class = "catalog"><h2><div class = "cat_item">Mystery
                    <div class = "cat_item">Science </div>
                    <div class = "cat_item">Fantasy </div>
                    <div class = "cat_item">Romance</div> 
                    <div class = "cat_item">Historical </div>
                    <div class = "cat_item">Drama </div>
                    <div class = "cat_item">Horror</h2></div>
                    </div>
                    <div class="flex-container">
                    <div class="flex-item"><a href="{url_for('item', item=plist[0])}"><img src="static/images/Slide1.JPG" alt="Image 1"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Adulting  (English, Paperback, Gupta Neharika)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[1])}"><img src="static/images/Slide2.JPG" alt="Image 2"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Song Of Ice And Fire: A Game Of&nbsp;Thrones (Paperback)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[2])}"><img src="static/images/Slide3.JPG" alt="Image 3"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Nobody Killed Her (English, Paperback, Sabyn Javeri)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[3])}"><img src="static/images/Slide4.JPG" alt="Image 4"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Koi Good News? (English, Paperback, Zareen Khan)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[4])}"><img src="static/images/Slide5.JPG" alt="Image 5"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Belated Bachelor's Party (English, Paperback)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[5])}"><img src="static/images/Slide6.JPG" alt="Image 6"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Swap (English, Paperback, Shuma Raha)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[6])}"><img src="static/images/Slide7.JPG" alt="Image 7"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Serious Men (English, Paperback, Manu Joseph)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[7])}"><img src="static/images/Slide8.JPG" alt="Image 8"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Selection Day (English, Paperback, Aaravind Adiga)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[8])}"><img src="static/images/Slide9.JPG" alt="Image 9"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The White Tiger (English, Paperback, Aaravind Adiga)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[9])}"><img src="static/images/Slide10.JPG" alt="Image 10"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>India's Most Hunted (English, Paperback, K. Hari Kumar)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[10])}"><img src="static/images/Slide11.JPG" alt="Image 11"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Cuckold (English, Paperback, Kiran Nagarkar)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[11])}"><img src="static/images/Slide12.JPG" alt="Image 12"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Dopehri (English, Paperback, Pankaj Kapoor)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[12])}"><img src="static/images/Slide13.JPG" alt="Image 13"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Rumi (English, Paperback, Farrukh Dhondy)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[13])}"><img src="static/images/Slide14.JPG" alt="Image 14"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Forest Enchantments (English, Paperback, Chitra Benerjee Divakaruni)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[14])}"><img src="static/images/Slide15.JPG" alt="Image 15"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Twentieth Wife (English, Paperback, Indu Sundaresan)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[15])}"><img src="static/images/Slide16.JPG" alt="Image 16"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Daura (English, Paperback, Anukriti Upadhyay)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[16])}"><img src="static/images/Slide17.JPG" alt="Image 17"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Gypsy Goddess (English, Paperback, Meena Kandasamy)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[17])}"><img src="static/images/Slide18.JPG" alt="Image 18"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Jorasanko (English, Paperback, Aruna Chakravarti)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[18])}"><img src="static/images/Slide19.JPG" alt="Image 19"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Radiance of a Thousand Suns (English, Paperback, Manreet Sodhi)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[19])}"><img src="static/images/Slide20.JPG" alt="Image 20"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>BAAZ (English, Paperback, Anuja Chauhan)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[20])}"><img src="static/images/Slide21.JPG" alt="Image 21"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Bhaunri (English, Paperback, Anukriti Upadhyay)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[21])}"><img src="static/images/Slide22.JPG" alt="Image 22"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Unlikely Adventures of the Shergill Sisters (English, Paperback)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[22])}"><img src="static/images/Slide23.JPG" alt="Image 23"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Far Field (English, Paperback, Madhuri Vijay)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[23])}"><img src="static/images/Slide24.JPG" alt="Image 24"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Paper Moon (English, Paperback, Rehana Munir)</div>
                    </div>
                    <div class = "footer"></div>
                    </body>
                    </html>"""
    if registered():
        a = session['user_data']
        a[1] = a[1].capitalize()
        c = f"""<a href="{url_for('about')}"><div class = "log">{a[1]}</div></a>"""
        return f"""<html>
                    <head><title>NOVELNEST</title><style>{style}</style></head>
                    <body>
                    <div class="topnav">
                      {c}
                      <a href="{url_for('user')}">Cart</a>
                      <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                    </div>
                    </h1></div>
                    <div class = "quote">
                    BUY<br>
                    <i><b>READ</b></i><br>
                    REPEAT
                    </div>
                    <div class="flex-nav">
                    <div class = "catalog2"><marquee><b>Unleash the reader in you, and embark on a journey through the boundless realms of imagination. Welcome to NovelNest, where stories come alive!</b> </marquee></div>
                    <h1>
                    <i>EXPLORE&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; YOUR <u>LITERARY</u> PARADISE.</i> 
                    </h1>
                    </div>
                    <div class = "catalog"><h2><div class = "cat_item">Mystery
                    <div class = "cat_item">Science </div>
                    <div class = "cat_item">Fantasy </div>
                    <div class = "cat_item">Romance</div> 
                    <div class = "cat_item">Historical </div>
                    <div class = "cat_item">Drama </div>
                    <div class = "cat_item">Horror</h2></div>
                    </div>
                    <div class="flex-container">
                    <div class="flex-item"><a href="{url_for('item', item=plist[0])}"><img src="static/images/Slide1.JPG" alt="Image 1"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Adulting  (English, Paperback, Gupta Neharika)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[1])}"><img src="static/images/Slide2.JPG" alt="Image 2"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Song Of Ice And Fire: A Game Of&nbsp;Thrones (Paperback)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[2])}"><img src="static/images/Slide3.JPG" alt="Image 3"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Nobody Killed Her (English, Paperback, Sabyn Javeri)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[3])}"><img src="static/images/Slide4.JPG" alt="Image 4"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Koi Good News? (English, Paperback, Zareen Khan)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[4])}"><img src="static/images/Slide5.JPG" alt="Image 5"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Belated Bachelor's Party (English, Paperback)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[5])}"><img src="static/images/Slide6.JPG" alt="Image 6"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Swap (English, Paperback, Shuma Raha)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[6])}"><img src="static/images/Slide7.JPG" alt="Image 7"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Serious Men (English, Paperback, Manu Joseph)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[7])}"><img src="static/images/Slide8.JPG" alt="Image 8"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Selection Day (English, Paperback, Aaravind Adiga)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[8])}"><img src="static/images/Slide9.JPG" alt="Image 9"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The White Tiger (English, Paperback, Aaravind Adiga)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[9])}"><img src="static/images/Slide10.JPG" alt="Image 10"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>India's Most Hunted (English, Paperback, K. Hari Kumar)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[10])}"><img src="static/images/Slide11.JPG" alt="Image 11"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Cuckold (English, Paperback, Kiran Nagarkar)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[11])}"><img src="static/images/Slide12.JPG" alt="Image 12"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Dopehri (English, Paperback, Pankaj Kapoor)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[12])}"><img src="static/images/Slide13.JPG" alt="Image 13"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Rumi (English, Paperback, Farrukh Dhondy)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[13])}"><img src="static/images/Slide14.JPG" alt="Image 14"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Forest Enchantments (English, Paperback, Chitra Benerjee Divakaruni)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[14])}"><img src="static/images/Slide15.JPG" alt="Image 15"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Twentieth Wife (English, Paperback, Indu Sundaresan)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[15])}"><img src="static/images/Slide16.JPG" alt="Image 16"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Daura (English, Paperback, Anukriti Upadhyay)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[16])}"><img src="static/images/Slide17.JPG" alt="Image 17"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Gypsy Goddess (English, Paperback, Meena Kandasamy)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[17])}"><img src="static/images/Slide18.JPG" alt="Image 18"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Jorasanko (English, Paperback, Aruna Chakravarti)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[18])}"><img src="static/images/Slide19.JPG" alt="Image 19"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Radiance of a Thousand Suns (English, Paperback, Manreet Sodhi)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[19])}"><img src="static/images/Slide20.JPG" alt="Image 20"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>BAAZ (English, Paperback, Anuja Chauhan)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[20])}"><img src="static/images/Slide21.JPG" alt="Image 21"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Bhaunri (English, Paperback, Anukriti Upadhyay)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[21])}"><img src="static/images/Slide22.JPG" alt="Image 22"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Unlikely Adventures of the Shergill Sisters (English, Paperback)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[22])}"><img src="static/images/Slide23.JPG" alt="Image 23"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>The Far Field (English, Paperback, Madhuri Vijay)</div>
                    <div class="flex-item"><a href="{url_for('item', item=plist[23])}"><img src="static/images/Slide24.JPG" alt="Image 24"></a><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>Paper Moon (English, Paperback, Rehana Munir)</div>
                    </div>
                    <div class = "footer"></div>
                    </body>
                    </html>"""
@bridge.route('/profile', methods=['GET', 'POST'])
def reg_login():
    style = css()
    user_click = request.args.get('button')
    if request.method == 'POST':
        form_id = request.form.get('form_id')
        if form_id == 'reg_form':
            first_name = request.form.get('fname')
            last_name = request.form.get('lname')
            email = request.form.get('email')
            password = request.form.get('password')
            contact = request.form.get('contact')
            address = request.form.get('address')
            postal = request.form.get('postal')
            state = request.form.get('stated')
            full_name = first_name + " " + last_name
            cursor=mycon.cursor()
            existance = 0
            if len(first_name)==0 or len(last_name)==0 or len(email)==0 or len(password)==0 or len(postal)==0 or len(contact)==0 or len(address)==0 or len(state) == 0:
                return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body background="static/wallpaper desktop.jpeg">
                            <div class="topnav">
                            <a href="{url_for('reg_login', button='login')}">Sign in</a>
                            <a href="{url_for('home')}">Home</a>
                            <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                            </div><br><br><br>
                            <form action="/profile" method="post" class = "rlform">
                            <h1>Join:</h1>
                            <input type="hidden" name="form_id" value="reg_form">
                            <b>First Name:</b><br><input type="text" id="fname" name="fname" class="custom-input"><br><br>
                            <b>Last Name:</b><br><input type="text" id="lname" name="lname" class="custom-input"><br><br>
                            <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                            <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                            <b>Contact:</b><br><input type="text" id="contact" name="contact" class="custom-input"><br><br>
                            <b>Address:</b><br><input type="text" id="address" name="address" class="custom-input"><br><br>
                            <b>Postal Code:</b><br><input type="text" id="postal" name="postal" class="custom-input"><br><br>
                            <b>State:</b><br><select id="stated" name="stated" class="custom-input">                  
                            <option value="Andhra Pradesh">Andhra Pradesh</option>         
                            <option value="Arunachal Pradesh">Arunachal Pradesh</option>         
                            <option value="Assam">Assam</option>         
                            <option value="Bihar">Bihar</option>         
                            <option value="Chhattisgarh">Chhattisgarh</option>         
                            <option value="Goa">Goa</option>         
                            <option value="Gujarat">Gujarat</option>         
                            <option value="Haryana">Haryana</option>         
                            <option value="Himachal Pradesh">Himachal Pradesh</option>         
                            <option value="Jharkhand">Jharkhand</option>         
                            <option value="Karnataka">Karnataka</option>         
                            <option value="Kerala">Kerala</option>         
                            <option value="Madhya Pradesh">Madhya Pradesh</option>         
                            <option value="Maharashtra">Maharashtra</option>         
                            <option value="Manipur">Manipur</option>         
                            <option value="Meghalaya">Meghalaya</option>         
                            <option value="Mizoram">Mizoram</option>         
                            <option value="Nagaland">Nagaland</option>         
                            <option value="Odisha">Odisha</option>         
                            <option value="Punjab">Punjab</option>         
                            <option value="Rajasthan">Rajasthan</option>         
                            <option value="Sikkim">Sikkim</option>         
                            <option value="Tamil Nadu">Tamil Nadu</option>         
                            <option value="Telangana">Telangana</option>         
                            <option value="Tripura">Tripura</option>         
                            <option value="Uttar Pradesh">Uttar Pradesh</option>         
                            <option value="Uttarakhand">Uttarakhand</option>         
                            <option value="West Bengal">West Bengal</option>     
                            </select><br><br>
                            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button"><br>
                            <center><h4>Flill all fields correctly!</h4></center>
                            </form>
                            </body>
                            </html>"""
            elif len(password)<8:
                return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body background="static/wallpaper desktop.jpeg">
                            <div class="topnav">
                            <a href="{url_for('reg_login', button='login')}">Sign in</a>
                            <a href="{url_for('home')}">Home</a>
                            <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                            </div><br><br><br>
                            <form action="/profile" method="post" class = "rlform">
                            <h1>Join:</h1>
                            <input type="hidden" name="form_id" value="reg_form">
                            <b>First Name:</b><br><input type="text" id="fname" name="fname" class="custom-input"><br><br>
                            <b>Last Name:</b><br><input type="text" id="lname" name="lname" class="custom-input"><br><br>
                            <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                            <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                            <b>Contact:</b><br><input type="text" id="contact" name="contact" class="custom-input"><br><br>
                            <b>Address:</b><br><input type="text" id="address" name="address" class="custom-input"><br><br>
                            <b>Postal Code:</b><br><input type="text" id="postal" name="postal" class="custom-input"><br><br>
                            <b>State:</b><br><select id="stated" name="stated" class="custom-input">              
                            <option value="Andhra Pradesh">Andhra Pradesh</option>         
                            <option value="Arunachal Pradesh">Arunachal Pradesh</option>         
                            <option value="Assam">Assam</option>         
                            <option value="Bihar">Bihar</option>         
                            <option value="Chhattisgarh">Chhattisgarh</option>         
                            <option value="Goa">Goa</option>         
                            <option value="Gujarat">Gujarat</option>         
                            <option value="Haryana">Haryana</option>         
                            <option value="Himachal Pradesh">Himachal Pradesh</option>         
                            <option value="Jharkhand">Jharkhand</option>         
                            <option value="Karnataka">Karnataka</option>         
                            <option value="Kerala">Kerala</option>         
                            <option value="Madhya Pradesh">Madhya Pradesh</option>         
                            <option value="Maharashtra">Maharashtra</option>         
                            <option value="Manipur">Manipur</option>         
                            <option value="Meghalaya">Meghalaya</option>         
                            <option value="Mizoram">Mizoram</option>         
                            <option value="Nagaland">Nagaland</option>         
                            <option value="Odisha">Odisha</option>         
                            <option value="Punjab">Punjab</option>         
                            <option value="Rajasthan">Rajasthan</option>         
                            <option value="Sikkim">Sikkim</option>         
                            <option value="Tamil Nadu">Tamil Nadu</option>         
                            <option value="Telangana">Telangana</option>         
                            <option value="Tripura">Tripura</option>         
                            <option value="Uttar Pradesh">Uttar Pradesh</option>         
                            <option value="Uttarakhand">Uttarakhand</option>         
                            <option value="West Bengal">West Bengal</option>     
                            </select><br><br>
                            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button"><br>
                            <center><h4>Password must have atleast 8 characters!</h4></center>
                            </form>
                            </body>
                            </html>"""
            elif len(contact)!=10 or not contact.isdigit():
                return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body background="static/wallpaper desktop.jpeg">
                            <div class="topnav">
                            <a href="{url_for('reg_login', button='login')}">Sign in</a>
                            <a href="{url_for('home')}">Home</a>
                            <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                            </div><br><br><br>
                            <form action="/profile" method="post" class = "rlform">
                            <h1>Join:</h1>
                            <input type="hidden" name="form_id" value="reg_form">
                            <b>First Name:</b><br><input type="text" id="fname" name="fname" class="custom-input"><br><br>
                            <b>Last Name:</b><br><input type="text" id="lname" name="lname" class="custom-input"><br><br>
                            <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                            <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                            <b>Contact:</b><br><input type="text" id="contact" name="contact" class="custom-input"><br><br>
                            <b>Address:</b><br><input type="text" id="address" name="address" class="custom-input"><br><br>
                            <b>Postal Code:</b><br><input type="text" id="postal" name="postal" class="custom-input"><br><br>
                            <b>State:</b><br><select id="stated" name="stated" class="custom-input">                  
                            <option value="Andhra Pradesh">Andhra Pradesh</option>         
                            <option value="Arunachal Pradesh">Arunachal Pradesh</option>         
                            <option value="Assam">Assam</option>         
                            <option value="Bihar">Bihar</option>         
                            <option value="Chhattisgarh">Chhattisgarh</option>         
                            <option value="Goa">Goa</option>         
                            <option value="Gujarat">Gujarat</option>         
                            <option value="Haryana">Haryana</option>         
                            <option value="Himachal Pradesh">Himachal Pradesh</option>         
                            <option value="Jharkhand">Jharkhand</option>         
                            <option value="Karnataka">Karnataka</option>         
                            <option value="Kerala">Kerala</option>         
                            <option value="Madhya Pradesh">Madhya Pradesh</option>         
                            <option value="Maharashtra">Maharashtra</option>         
                            <option value="Manipur">Manipur</option>         
                            <option value="Meghalaya">Meghalaya</option>         
                            <option value="Mizoram">Mizoram</option>         
                            <option value="Nagaland">Nagaland</option>         
                            <option value="Odisha">Odisha</option>         
                            <option value="Punjab">Punjab</option>         
                            <option value="Rajasthan">Rajasthan</option>         
                            <option value="Sikkim">Sikkim</option>         
                            <option value="Tamil Nadu">Tamil Nadu</option>         
                            <option value="Telangana">Telangana</option>         
                            <option value="Tripura">Tripura</option>         
                            <option value="Uttar Pradesh">Uttar Pradesh</option>         
                            <option value="Uttarakhand">Uttarakhand</option>         
                            <option value="West Bengal">West Bengal</option>     
                            </select><br><br>
                            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button"><br>
                            <center><h4>Contact no. is invalid.</h4></center>
                            </form>
                            </body>
                            </html>"""
            elif len(postal)!=6 or not postal.isdigit() :
                return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body background="static/wallpaper desktop.jpeg">
                            <div class="topnav">
                            <a href="{url_for('reg_login', button='login')}">Sign in</a>
                            <a href="{url_for('home')}">Home</a>
                            <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                            </div><br><br><br>
                            <form action="/profile" method="post" class = "rlform">
                            <h1>Join:</h1>
                            <input type="hidden" name="form_id" value="reg_form">
                            <b>First Name:</b><br><input type="text" id="fname" name="fname" class="custom-input"><br><br>
                            <b>Last Name:</b><br><input type="text" id="lname" name="lname" class="custom-input"><br><br>
                            <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                            <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                            <b>Contact:</b><br><input type="text" id="contact" name="contact" class="custom-input"><br><br>
                            <b>Address:</b><br><input type="text" id="address" name="address" class="custom-input"><br><br>
                            <b>Postal Code:</b><br><input type="text" id="postal" name="postal" class="custom-input"><br><br>
                            <b>State:</b><br><select id="stated" name="stated" class="custom-input">                  
                            <option value="Andhra Pradesh">Andhra Pradesh</option>         
                            <option value="Arunachal Pradesh">Arunachal Pradesh</option>         
                            <option value="Assam">Assam</option>         
                            <option value="Bihar">Bihar</option>         
                            <option value="Chhattisgarh">Chhattisgarh</option>         
                            <option value="Goa">Goa</option>         
                            <option value="Gujarat">Gujarat</option>         
                            <option value="Haryana">Haryana</option>         
                            <option value="Himachal Pradesh">Himachal Pradesh</option>         
                            <option value="Jharkhand">Jharkhand</option>         
                            <option value="Karnataka">Karnataka</option>         
                            <option value="Kerala">Kerala</option>         
                            <option value="Madhya Pradesh">Madhya Pradesh</option>         
                            <option value="Maharashtra">Maharashtra</option>         
                            <option value="Manipur">Manipur</option>         
                            <option value="Meghalaya">Meghalaya</option>         
                            <option value="Mizoram">Mizoram</option>         
                            <option value="Nagaland">Nagaland</option>         
                            <option value="Odisha">Odisha</option>         
                            <option value="Punjab">Punjab</option>         
                            <option value="Rajasthan">Rajasthan</option>         
                            <option value="Sikkim">Sikkim</option>         
                            <option value="Tamil Nadu">Tamil Nadu</option>         
                            <option value="Telangana">Telangana</option>         
                            <option value="Tripura">Tripura</option>         
                            <option value="Uttar Pradesh">Uttar Pradesh</option>         
                            <option value="Uttarakhand">Uttarakhand</option>         
                            <option value="West Bengal">West Bengal</option>     
                            </select><br><br>
                            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button"><br>
                            <center><h4>Postal code is invalid.</h4></center>
                            </form>
                            </body>
                            </html>"""
            else:
                em_len = len(email)
                mail_list = ["@gmail.com","@outlook.com","@yahoo.com","@gmail.in","@hotmail.com"]
                if email[em_len-10:em_len] == mail_list[0] or email[em_len-12:em_len] == mail_list[1] or email[em_len-10:em_len] == mail_list[2] or email[em_len-9:em_len] == mail_list[3] or email[em_len-12:em_len] == mail_list[4]:
                    find_rec ="select*from userdat where email = '{}'".format(email)
                    cursor.execute(find_rec)
                    existing_data=cursor.fetchall()
                    count=cursor.rowcount
                    for counter in existing_data:
                        existance = existance + 1
                    if existance==0:
                        uid = random.sample(range(1000000, 10000000), 1)[0]
                        insert_rec = "insert into userdat(id,name,email,password,contact,address,postal,state)values({},'{}','{}','{}','{}','{}','{}','{}')".format(uid,full_name,email,password,contact,address,postal,state)
                        cursor.execute(insert_rec)
                        mycon.commit()
                        sel_pf="select id, name, email, contact, address, postal, state from userdat where password = '{}' and email = '{}'".format(password,email)
                        cursor.execute(sel_pf)
                        datab=cursor.fetchall()
                        count=cursor.rowcount
                        for i in datab:
                            i = list(i)
                        session['user_data'] = i
                        if prod_loc():
                            return redirect(url_for("item", item = session["prod"]))
                            session.pop('prod', None)
                        if not prod_loc():
                            return redirect(url_for('about'))
                    else:
                        return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body background="static/wallpaper desktop.jpeg">
                            <div class="topnav">
                            <a href="{url_for('reg_login', button='login')}">Sign in</a>
                            <a href="{url_for('home')}">Home</a>
                            <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                            </div><br><br><br>
                            <form action="/profile" method="post" class = "rlform">
                            <h1>Join:</h1>
                            <input type="hidden" name="form_id" value="reg_form">
                            <b>First Name:</b><br><input type="text" id="fname" name="fname" class="custom-input"><br><br>
                            <b>Last Name:</b><br><input type="text" id="lname" name="lname" class="custom-input"><br><br>
                            <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                            <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                            <b>Contact:</b><br><input type="text" id="contact" name="contact" class="custom-input"><br><br>
                            <b>Address:</b><br><input type="text" id="address" name="address" class="custom-input"><br><br>
                            <b>Postal Code:</b><br><input type="text" id="postal" name="postal" class="custom-input"><br><br>
                            <b>State:</b><br><select id="stated" name="stated" class="custom-input">         
                            <option value="Andhra Pradesh">Andhra Pradesh</option>         
                            <option value="Arunachal Pradesh">Arunachal Pradesh</option>         
                            <option value="Assam">Assam</option>         
                            <option value="Bihar">Bihar</option>         
                            <option value="Chhattisgarh">Chhattisgarh</option>         
                            <option value="Goa">Goa</option>         
                            <option value="Gujarat">Gujarat</option>         
                            <option value="Haryana">Haryana</option>         
                            <option value="Himachal Pradesh">Himachal Pradesh</option>         
                            <option value="Jharkhand">Jharkhand</option>         
                            <option value="Karnataka">Karnataka</option>         
                            <option value="Kerala">Kerala</option>         
                            <option value="Madhya Pradesh">Madhya Pradesh</option>         
                            <option value="Maharashtra">Maharashtra</option>         
                            <option value="Manipur">Manipur</option>         
                            <option value="Meghalaya">Meghalaya</option>         
                            <option value="Mizoram">Mizoram</option>         
                            <option value="Nagaland">Nagaland</option>         
                            <option value="Odisha">Odisha</option>         
                            <option value="Punjab">Punjab</option>         
                            <option value="Rajasthan">Rajasthan</option>         
                            <option value="Sikkim">Sikkim</option>         
                            <option value="Tamil Nadu">Tamil Nadu</option>         
                            <option value="Telangana">Telangana</option>         
                            <option value="Tripura">Tripura</option>         
                            <option value="Uttar Pradesh">Uttar Pradesh</option>         
                            <option value="Uttarakhand">Uttarakhand</option>         
                            <option value="West Bengal">West Bengal</option>     
                            </select><br><br>
                            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button"><br>
                            <center><h4>Account already exists. Log in! </h4></center>
                            </form>
                            </body>
                            </html>"""
                else:
                    return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body background="static/wallpaper desktop.jpeg">
                            <div class="topnav">
                            <a href="{url_for('reg_login', button='login')}">Sign in</a>
                            <a href="{url_for('home')}">Home</a>
                            <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                            </div><br><br><br>
                            <form action="/profile" method="post" class = "rlform">
                            <h1>Join:</h1>
                            <input type="hidden" name="form_id" value="reg_form">
                            <b>First Name:</b><br><input type="text" id="fname" name="fname" class="custom-input"><br><br>
                            <b>Last Name:</b><br><input type="text" id="lname" name="lname" class="custom-input"><br><br>
                            <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                            <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                            <b>Contact:</b><br><input type="text" id="contact" name="contact" class="custom-input"><br><br>
                            <b>Address:</b><br><input type="text" id="address" name="address" class="custom-input"><br><br>
                            <b>Postal Code:</b><br><input type="text" id="postal" name="postal" class="custom-input"><br><br>
                            <b>State:</b><br><select id="stated" name="stated" class="custom-input">         
                            <option value="Andhra Pradesh">Andhra Pradesh</option>         
                            <option value="Arunachal Pradesh">Arunachal Pradesh</option>         
                            <option value="Assam">Assam</option>         
                            <option value="Bihar">Bihar</option>         
                            <option value="Chhattisgarh">Chhattisgarh</option>         
                            <option value="Goa">Goa</option>         
                            <option value="Gujarat">Gujarat</option>         
                            <option value="Haryana">Haryana</option>         
                            <option value="Himachal Pradesh">Himachal Pradesh</option>         
                            <option value="Jharkhand">Jharkhand</option>         
                            <option value="Karnataka">Karnataka</option>         
                            <option value="Kerala">Kerala</option>         
                            <option value="Madhya Pradesh">Madhya Pradesh</option>         
                            <option value="Maharashtra">Maharashtra</option>         
                            <option value="Manipur">Manipur</option>         
                            <option value="Meghalaya">Meghalaya</option>         
                            <option value="Mizoram">Mizoram</option>         
                            <option value="Nagaland">Nagaland</option>         
                            <option value="Odisha">Odisha</option>         
                            <option value="Punjab">Punjab</option>         
                            <option value="Rajasthan">Rajasthan</option>         
                            <option value="Sikkim">Sikkim</option>         
                            <option value="Tamil Nadu">Tamil Nadu</option>         
                            <option value="Telangana">Telangana</option>         
                            <option value="Tripura">Tripura</option>         
                            <option value="Uttar Pradesh">Uttar Pradesh</option>         
                            <option value="Uttarakhand">Uttarakhand</option>         
                            <option value="West Bengal">West Bengal</option>     
                            </select><br><br>
                            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button"><br>
                            <center><h4>Email service is invalid or not supported.</h4></center>
                            </form>
                            </body>
                            </html>"""
        if form_id == 'login_form':
            email = request.form.get('email')
            password = request.form.get('password')  
            if mycon.is_connected():
                cursor=mycon.cursor()
            existance = 0
            if len(password)==0 or len(email)==0 :
                return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body background="static/wallpaper desktop.jpeg">
                            <div class="topnav">
                            <a href="{url_for('reg_login', button='register')}">Sign up</a>
                            <a href="{url_for('home')}">Home</a>
                            <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                            </div><br><br><br>
                            <form action="/profile" method="post" class = "rlform">
                            <h1>Sign In:</h1>
                            <input type="hidden" name="form_id" value="login_form">
                            <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                            <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button"><br><center>
                            </form>
                            <h4>Fill all fields correctly!</h4>
                            </body>
                            </html>"""
            else:
                em_len = len(email)
                mail_list = ["@gmail.com","@outlook.com","@yahoo.com","@gmail.in","@hotmail.com"]
                if email[em_len-10:em_len] == mail_list[0] or email[em_len-12:em_len] == mail_list[1] or email[em_len-10:em_len] == mail_list[2] or email[em_len-9:em_len] == mail_list[3] or email[em_len-12:em_len] == mail_list[4]:
                    find_rec ="select*from userdat where password = '{}' and email = '{}'".format(password,email)
                    cursor.execute(find_rec)
                    existing_data=cursor.fetchall()
                    count=cursor.rowcount
                    for counter in existing_data:
                        existance = existance + 1
                    if existance==1:
                        sel_pf="select id, name, email, contact, address, postal, state from userdat where password = '{}' and email = '{}'".format(password,email)
                        cursor.execute(sel_pf)
                        datab=cursor.fetchall()
                        count=cursor.rowcount
                        for i in datab:
                            i = list(i)
                        session['user_data'] = i
                        if prod_loc():
                            return redirect(url_for("item", item = session["prod"]))
                            session.pop('prod', None)
                        if not prod_loc():
                            return redirect(url_for('home'))
                    else:
                        return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body background="static/wallpaper desktop.jpeg">
                            <div class="topnav">
                            <a href="{url_for('reg_login', button='register')}">Sign up</a>
                            <a href="{url_for('home')}">Home</a>
                            <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                            </div><br><br><br>
                            <form action="/profile" method="post" class = "rlform">
                            <h1>Sign In:</h1>
                            <input type="hidden" name="form_id" value="login_form">
                            <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                            <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button"><br><center>
                            </form>
                            <h4>Incorrect email id or password.</h4>
                            </body>
                            </html>"""
                else:
                    return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body background="static/wallpaper desktop.jpeg">
                            <div class="topnav">
                            <a href="{url_for('reg_login', button='register')}">Sign up</a>
                            <a href="{url_for('home')}">Home</a>
                            <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                            </div><br><br><br>
                            <form action="/profile" method="post" class = "rlform">
                            <h1>Sign In:</h1>
                            <input type="hidden" name="form_id" value="login_form">
                            <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                            <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                            <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button"><br><center>
                            </form>
                            <h4>Invalid Email ID or Password.</h4>
                            </body>
                            </html>"""
    elif user_click == 'register':
        return f"""<html>
                    <head><title>NOVELNEST</title><style>{style}</style></head>
                    <body background="static/wallpaper desktop.jpeg">
                    <div class="topnav">
                    <a href="{url_for('reg_login', button='login')}">Sign in</a>
                    <a href="{url_for('home')}">Home</a>
                    <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                    </div><br><br><br>
                    <form action="/profile" method="post" class = "rlform">
                    <h1>Join:</h1>
                    <input type="hidden" name="form_id" value="reg_form">
                    <b>First Name:</b><br><input type="text" id="fname" name="fname" class="custom-input"><br><br>
                    <b>Last Name:</b><br><input type="text" id="lname" name="lname" class="custom-input"><br><br>
                    <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                    <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                    <b>Contact:</b><br><input type="text" id="contact" name="contact" class="custom-input"><br><br>
                    <b>Address:</b><br><input type="text" id="address" name="address" class="custom-input"><br><br>
                    <b>Postal Code:</b><br><input type="text" id="postal" name="postal" class="custom-input"><br><br>
                    <b>State:</b><br><select id="stated" name="stated" class="custom-input">         
                    <option value="Andhra Pradesh">Andhra Pradesh</option>         
                    <option value="Arunachal Pradesh">Arunachal Pradesh</option>         
                    <option value="Assam">Assam</option>         
                    <option value="Bihar">Bihar</option>         
                    <option value="Chhattisgarh">Chhattisgarh</option>         
                    <option value="Goa">Goa</option>         
                    <option value="Gujarat">Gujarat</option>         
                    <option value="Haryana">Haryana</option>         
                    <option value="Himachal Pradesh">Himachal Pradesh</option>         
                    <option value="Jharkhand">Jharkhand</option>         
                    <option value="Karnataka">Karnataka</option>         
                    <option value="Kerala">Kerala</option>         
                    <option value="Madhya Pradesh">Madhya Pradesh</option>         
                    <option value="Maharashtra">Maharashtra</option>         
                    <option value="Manipur">Manipur</option>         
                    <option value="Meghalaya">Meghalaya</option>         
                    <option value="Mizoram">Mizoram</option>         
                    <option value="Nagaland">Nagaland</option>         
                    <option value="Odisha">Odisha</option>         
                    <option value="Punjab">Punjab</option>         
                    <option value="Rajasthan">Rajasthan</option>         
                    <option value="Sikkim">Sikkim</option>         
                    <option value="Tamil Nadu">Tamil Nadu</option>         
                    <option value="Telangana">Telangana</option>         
                    <option value="Tripura">Tripura</option>         
                    <option value="Uttar Pradesh">Uttar Pradesh</option>         
                    <option value="Uttarakhand">Uttarakhand</option>         
                    <option value="West Bengal">West Bengal</option>     
                    </select><br><br>
                    <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button">
                    </form>
                    </body>
                    </html>"""
    elif user_click == 'login':
        return f"""<html>
                    <head><title>NOVELNEST</title><style>{style}</style></head>
                    <body background="static/wallpaper desktop.jpeg">
                    <div class="topnav">
                    <a href="{url_for('reg_login', button='register')}">Sign up</a>
                    <a href="{url_for('home')}">Home</a>
                    <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                    </div><br><br><br>
                    <form action="/profile" method="post" class = "rlform">
                    <h1>Sign In:</h1>
                    <input type="hidden" name="form_id" value="login_form">
                    <b>Email:</b><br><input type="text" id="email" name="email" class="custom-input"><br><br>
                    <b>Password:</b><br><input type="password" id="password" name="password" class="custom-input"><br><br>
                    <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="submit" value="Continue" class="capsule-button">
                    <br><center>
                    </form>
                    </body>
                    </html>"""        
    elif user_click == 'logout':
        cursor=mycon.cursor()
        if len(session) > 0:
            session.clear()
            dt = "delete from cart"
            cursor.execute(dt)
            mycon.commit()
        else:
            return redirect(url_for('reg_login', button='login'))
    elif user_click == 'del_ac':
        cursor=mycon.cursor()
        a = session['user_data']
        st = "delete from userdat where email = '{}' ".format(a[2])
        cursor.execute(st)
        mycon.commit()
        if len(session) > 0:
            session.clear()
            dt = "delete from cart"
            cursor.execute(dt)
            mycon.commit()   
        else:
            return redirect(url_for('reg_login', button='register'))
    return redirect(url_for('home'))
@bridge.route('/products/<item>')
def item(item):
    if registered():
        aw = session['user_data']
        aw[1] = aw[1].capitalize()
        cs = f"""<a href="{url_for('about')}"><div class = "log">{aw[1]}</div></a>
                    <a href="{url_for('user')}">Cart</a>"""
        dz = f"""{aw[4]},{aw[5]},{aw[6]}"""
    if not registered():
        cs = f"""<a href="{url_for('reg_login', button='login')}">Sign In</a>
            <a href="{url_for('reg_login', button='register')}">Join</a>
                """
        dz = f"""---"""
        session['prod'] = item
    style = css()
    plist = prod_id()
    nrlist = nr_list()
    details = details_()
    cursor=mycon.cursor()
    existance = 0
    availability = []
    st = "select*from cart where pid = {}".format(int(item))
    cursor.execute(st)
    pur=cursor.fetchall()
    count=cursor.rowcount
    for i in pur:
        existance = existance + 1
        
    avail = "select pid from product where qty = 0 "
    cursor.execute(avail)
    ava=cursor.fetchall()
    count=cursor.rowcount
    for a in ava:
        a = list(a)
        c = str(a[0])
        availability.append(c)
    for f in range(0,24):
        k = f + 1
        pname = nrlist[f][0]
        rate = nrlist[f][1]
        summary = details[f][0]
        author = details[f][1]
        if item == plist[f]: 
            if item in availability:
                return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body>
                            <div class="topnav">
                          {cs} 
                          <a href="{url_for('home')}">Home</a>
                          <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                        </div>
                            <div class = "parent">
                            <div class = "flex-fout">
                            <img src = "/static/images/Slide{k}.JPG" alt="BUY NOW">
                            </div></div>
                            <div class = "out">
                            <div class = "out-in">
                            <div class="out-item"><img src = "/static/images/Slide{k}.JPG" alt="BUY NOW"></div>
                            </div></div>
                            <div class = "detail_container">
                            <h1>{pname}(English, Paperback)</h1></div><br><br><hr>
                            <div class = "about_parent">
                            <div class = "detail_containerr">
                            <h2>About The Book:</h2>
                            <p>{summary}</p>
                            <h2>About The Author:</h2>
                            <p>{author}</p>
                            </div>
                            <div class = "check_container"><br>
                            <h1>&nbsp;&#8377;{rate}.00</h1>
                            &nbsp;FREE Delivery within 7 Days.<br>
                            &nbsp;AT: {dz}<br><br>
                            &nbsp;Publisher  :  HarperCollins India (21 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;November 2023)<br>
                            &nbsp;Language  :  English<br>
                            &nbsp;Paperback  :  344 pages<br>
                            &nbsp;Item Weight  :  280 g<br>
                            &nbsp;Dimensions  :  14 x 2 x 22 cm<br><br><br>
                            <center>OUT OF STOCK</center>
                            </div></div>
                            <div class = "footer"></div>
                            </body>
                            </html>"""
            if existance == 0:
                return f"""<html>
                            <head><title>NOVELNEST</title><style>{style}</style></head>
                            <body>
                            <div class="topnav">
                          {cs} 
                          <a href="{url_for('home')}">Home</a>
                          <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                        </div>
                            <div class = "parent">
                            <div class = "flex-fout">
                            <img src = "/static/images/Slide{k}.JPG" alt="BUY NOW">
                            </div></div>
                            <div class = "out">
                            <div class = "out-in">
                            <div class="out-item"><img src = "/static/images/Slide{k}.JPG" alt="BUY NOW"></div>
                            </div></div>
                            <div class = "detail_container">
                            <h1>{pname}(English, Paperback)</h1></div><br><br><hr>
                            <div class = "about_parent">
                            <div class = "detail_containerr">
                            <h2>About The Book:</h2>
                            <p>{summary}</p>
                            <h2>About The Author:</h2>
                            <p>{author}</p>
                            </div>
                            <div class = "check_container"><br>
                            <h1>&nbsp;&#8377;{rate}.00</h1>
                            &nbsp;FREE Delivery within 7 Days.<br>
                            &nbsp;AT: {dz}<br><br>
                            &nbsp;Publisher  :  HarperCollins India (21 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;November 2023)<br>
                            &nbsp;Language  :  English<br>
                            &nbsp;Paperback  :  344 pages<br>
                            &nbsp;Item Weight  :  280 g<br>
                            &nbsp;Dimensions  :  14 x 2 x 22 cm<br><br><br>
                            <center><div class = "capsule-button"><a href="{url_for('cart', item=plist[f], ptype = 'add_to_cart' )}">Add to Cart</a></div></center>
                            </div></div>
                            <div class = "footer"></div>
                            </body>
                            </html>"""
            if existance > 0:
                return f"""<head><title>NOVELNEST</title><style>{style}</style></head>
                            <body>
                            <div class="topnav">
                          {cs}
                          <a href="{url_for('home')}">Home</a>
                          <a href="{url_for('home')}", class = 'split'>NOVELNEST</a>
                        </div>
                            <div class = "parent">
                            <div class = "flex-fout">
                            <img src = "/static/images/Slide{k}.JPG" alt="BUY NOW">
                            </div>
                            </div>
                            <div class = "out">
                            <div class = "out-in">
                            <div class="out-item"><img src = "/static/images/Slide{k}.JPG" alt="BUY NOW"></div>
                            </div>
                            </div>
                            <div class = "detail_container">
                            <h1>{pname}(English, Paperback)</h1></div><br><br>
                            <hr>
                            <div class = "about_parent">
                            <div class = "detail_containerr">
                            <h2>About The Book:</h2>
                            <p>{summary}</p>
                            <h2>About The Author:</h2>
                            <p>{author}</p>
                            </div>
                            <div class = "check_containerq"><br>
                            <h1>&nbsp;&#8377;{rate}.00</h1>
                            &nbsp;FREE Delivery within 7 Days.<br>
                            &nbsp;AT: {dz}<br><br>
                            &nbsp;Publisher  :  HarperCollins India (21 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;November 2023)<br>
                            &nbsp;Language  :  English<br>
                            &nbsp;Paperback  :  344 pages<br>
                            &nbsp;Item Weight  :  280 g<br>
                            &nbsp;Dimensions  :  14 x 2 x 22 cm<br><br><br>
                            <center><div class = "capsule-button"><a href="{url_for('cart', item=plist[f], ptype = 'add_to_cart' )}">Add Again!</a></div></center><br>
                            <center><div class = "capsule-button"><a href="{url_for('user')}">View Cart</a></div></center>
                            </div></div>
                            <div class = "footer"></div>
                            </body>
                            </html>"""
@bridge.route('/cart/<item>/<ptype>')
def cart(item,ptype):
    style = css()
    plist = prod_id()
    cart = clist()
    if not registered():
        session['prod'] = item
        return redirect(url_for('reg_login', button='register'))
    if registered():
        r = session['user_data']
        user_id = r[0]
        full_name = r[1]
        user_email = r[2]
        session.pop('prod', None)
        for f in range(0,24):
            if item == plist[f]:
                if mycon.is_connected():
                    cursor=mycon.cursor()
                pn = "select pname, rate from product where pid = {}".format(int(item))
                cursor.execute(pn)
                pnr=cursor.fetchall()
                count=cursor.rowcount
                for k in pnr:
                    k = list(k)
                pname = k[0]
                prate = k[1]
                if ptype == 'add_to_cart':
                    cursor=mycon.cursor()
                    existance = 0
                    st = "select*from cart where pid = {}".format(int(item))
                    cursor.execute(st)
                    pur=cursor.fetchall()
                    count=cursor.rowcount
                    for i in pur:
                        existance = existance + 1
                    if existance == 0:
                        inrec = "insert into cart values({},'{}',{},{},{})".format(int(item),pname,1,prate,prate)
                        cursor.execute(inrec)
                        mycon.commit()
                        pchange = "update product set qty = qty - 1 where pid = {}".format(int(item))
                        cursor.execute(pchange)
                        mycon.commit()
                        session['cart_req'] = item
                        return redirect(url_for("item", item = session['cart_req'] ))
                    if existance > 0:
                        inrec = "update cart set qty = qty + 1, price = price + {} where pid = {}".format(prate,int(item))
                        cursor.execute(inrec)
                        mycon.commit()
                        pchange = "update product set qty = qty - 1 where pid = {}".format(int(item))
                        cursor.execute(pchange)
                        mycon.commit()
                        session['cart_req'] = item
                        return redirect(url_for("item", item = session['cart_req'] ))
@bridge.route('/user_cart')  
def user():
    style = css()
    user_cart = []
    cursor=mycon.cursor()
    ucart = "select*from cart"
    cursor.execute(ucart)
    rows=cursor.fetchall()
    count=cursor.rowcount
    html_con = cart_html(rows,style)
    return html_con
@bridge.route('/final_call', methods=['GET', 'POST'])
def final_call():
    cursor=mycon.cursor()
    user_click = request.args.get('button')
    if request.method == 'POST':
        form_keys = request.form.keys()
        for key in form_keys:
            if key.startswith('product_id_'):
                product_id = request.form.get(key)
                action = request.form.get('action_{}'.format(product_id))
                if action == 'plus':
                    st = "update cart set qty = qty + 1, price = price + rate where pid = {}".format(product_id)
                    cursor.execute(st)
                    mycon.commit()
                    pt = "update product set qty = qty - 1 where pid = {}".format(product_id)
                    cursor.execute(pt)
                    mycon.commit()
                elif action == 'minus':
                    st = "update cart set qty = qty - 1, price = price - rate where pid = {}".format(product_id)
                    cursor.execute(st)
                    mycon.commit()
                    pt = "update product set qty = qty + 1 where pid = {}".format(product_id)
                    cursor.execute(pt)
                    mycon.commit()
                    dt = "delete from cart where qty = 0 and pid = {}".format(product_id)
                    cursor.execute(dt)
                    mycon.commit()
                elif action == 'remove':
                    st = "delete from cart where pid = {}".format(product_id)
                    cursor.execute(st)
                    mycon.commit()
        return redirect(url_for('user'))
    elif user_click == 'checkout':
        existance = 0
        st = "select*from cart"
        cursor.execute(st)
        pur=cursor.fetchall()
        count=cursor.rowcount
        for i in pur:
            existance = existance + 1
        if existance == 0:
            return redirect(url_for('user'))
        else:
            pids = ''
            a = session['user_data']
            tqty = 0
            s = 0
            for f in pur:
                c = str(f[0])+" "+ '('+str(f[2])+')'+','+' '
                pids = pids + c
                tqty = tqty + f[2]
                s = s + f[4]
            oid = random.sample(range(10000, 100000), 1)[0]
            uid = a[0]
            insert_rec = "insert into orders(orderid,pids,uid,qty,amount)values({},'{}',{},{},{})".format(oid, pids, uid, tqty, s)
            cursor.execute(insert_rec)
            mycon.commit()
            style = css()
            user_cart = []
            cursor=mycon.cursor()
            ucart = "select*from cart"
            cursor.execute(ucart)
            rows=cursor.fetchall()
            count=cursor.rowcount
            html_out = out_html(rows,style)
            dt = "delete from cart"
            cursor.execute(dt)
            mycon.commit() 
            return html_out
@bridge.route('/user_profile')
def about():
    if not registered():
        return redirect(url_for('reg_login', button='register'))
    if registered():
        cursor=mycon.cursor()
        a = session['user_data']
        a[1] = a[1].capitalize()
        style = css()
        st = "select pname from cart "
        cursor.execute(st)
        cart=cursor.fetchall()
        count=cursor.rowcount
        l = len(cart)
        if l==1:
            c = f"""<br>{cart[0][0]}<br><br><br><br><br><br><br>"""
        if l == 2:
            c = f"""<br>{cart[0][0]}<br>{cart[1][0]}<br><br><br><br><br><br>"""
        if l == 3:
            c = f"""<br>{cart[0][0]}<br>{cart[1][0]}<br>{cart[2][0]}<br><br><br><br><br>"""
        if l > 3:
            c = f"""<br>{cart[0][0]}<br>{cart[1][0]}<br>{cart[2][0]}<br>{cart[3][0]}<br>.<br>.<br><br>"""
        if l== 0:
            c = f"""<br><br><br>Empty<br><br><br><br><br>"""
        return f"""<html>
                        <head><title>NOVELNEST</title><style>{style}</style></head>
                        <body>
                         <div class="topnav">
                         <a href="{url_for('reg_login', button='logout')}">Sign out</a>
                         <a href="{url_for('home')}">Home</a>
                          <a href="{url_for('home')}", class = 'split'>PROFILE</a>
                        </div>
                        </h1></div>
                        <div class="flex-nav">
                        <h1>
                        WELCOME, {a[1]}
                        </h1></div><br><br><br>
                        <div class = "detail_container">
                                <h1>&nbsp;&nbsp;&nbsp</h1></div><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
                                <div class = "about_parent">
                                <div class = "detail_containerrr">
                                <h2>Personal Information:</h2>
                                <p><br>ID: {str(a[0])}<br>
                                Name: {a[1]}<br>
                                Email ID: {a[2]}<br>
                                Ethnicity: Indian<br></p>
                                <div class = "logout-button"><a href="{url_for('reg_login', button='del_ac')}"><center>Delete Account</center></a></div>
                                <h2>Shipping Details:</h2>
                                <p><br>Contact No.: {a[3]}<br>
                                Address: {a[4]}<br>
                                Postal Code: {a[5]}<br>
                                State: {a[6]}<br></p>
                                <div class = "logout-button"><a href="{url_for('reg_login', button='logout')}"><center>Sign Out</center></a></div><br>
                                </div>
                                <div class = "check_containerr"><br>
                                <h1><center>CART VIEW</center></h1>
                                <center>{c}</center>
                                <center><div class = "capsule-button"><a href="{url_for("user" )}">Go To Cart</a></div></center>
                                </div></div><br><br><br>
                                <h2>You are all set to Grab some bOOOOOOOks!</h2>
                        </body>
                        </html>"""
if __name__ == '__main__':

    webbrowser.open_new_tab('http://127.0.0.1:5000')

    bridge.run(debug=True, use_reloader=False)
    
    
    
# This Code has Been written by ss301.
