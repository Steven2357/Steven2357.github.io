n=int(input("題號："))
spade=input("黑桃")
heart=input("紅心")
diamond=input("方塊")
club=input("梅花")

bidding="""        <table id="bidding">
            <tr>
                <th class="NVUL">S</th>
                <th class="NVUL">W</th>
                <th class="NVUL">N</th>
                <th class="NVUL">E</th>
            </tr>

            <tr>
                <td>"""
bid=input("S:")
while bid!="?":
    bidding+=bid
    bidding+="""</td>
                <td>"""
    bid=input("W:")
    bidding+=bid
    bidding+="""</td>
                <td>"""
    bid=input("N:")
    bidding+=bid
    bidding+="""</td>
                <td>"""
    bid=input("E:")
    bidding+=bid
    bidding+="""</td>
            </tr>

            <tr>
                <td>"""
    bid=input("S:")

bidding+="""?</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </table>
"""

bidding=bidding.replace("!S","&spades;")
bidding=bidding.replace("!H","&hearts;")
bidding=bidding.replace("!D","&diamondsuit;")
bidding=bidding.replace("!C","&clubs;")

answer="""        <p id="bids">
            <button type="button" onclick="Incorrect()">1NT</button>
            <button type="button" onclick="Incorrect()">2NT</button>
            <button type="button" onclick="Incorrect()">3NT</button>
            <button type="button" onclick="Incorrect()">4NT</button>
            <button type="button" onclick="Incorrect()">5NT</button>
            <button type="button" onclick="Incorrect()">6NT</button>
            <button type="button" onclick="Incorrect()">7NT</button>
            <br>


            <button type="button" onclick="Incorrect()">1&spades;</button>
            <button type="button" onclick="Incorrect()">2&spades;</button>
            <button type="button" onclick="Incorrect()">3&spades;</button>
            <button type="button" onclick="Incorrect()">4&spades;</button>
            <button type="button" onclick="Incorrect()">5&spades;</button>
            <button type="button" onclick="Incorrect()">6&spades;</button>
            <button type="button" onclick="Incorrect()">7&spades;</button>
            <br>


            <button type="button" onclick="Incorrect()">1&hearts;</button>
            <button type="button" onclick="Incorrect()">2&hearts;</button>
            <button type="button" onclick="Incorrect()">3&hearts;</button>
            <button type="button" onclick="Incorrect()">4&hearts;</button>
            <button type="button" onclick="Incorrect()">5&hearts;</button>
            <button type="button" onclick="Incorrect()">6&hearts;</button>
            <button type="button" onclick="Incorrect()">7&hearts;</button>
            <button type="button" onclick="Incorrect()">XX</button>
            <br>

            
            <button type="button" onclick="Incorrect()">1&diamondsuit;</button>
            <button type="button" onclick="Incorrect()">2&diamondsuit;</button>
            <button type="button" onclick="Incorrect()">3&diamondsuit;</button>
            <button type="button" onclick="Incorrect()">4&diamondsuit;</button>
            <button type="button" onclick="Incorrect()">5&diamondsuit;</button>
            <button type="button" onclick="Incorrect()">6&diamondsuit;</button>
            <button type="button" onclick="Incorrect()">7&diamondsuit;</button>
            <button type="button" onclick="Incorrect()">X</button>
            <br>

            <button type="button" onclick="Incorrect()">1&clubs;</button>
            <button type="button" onclick="Incorrect()">2&clubs;</button>
            <button type="button" onclick="Incorrect()">3&clubs;</button>
            <button type="button" onclick="Incorrect()">4&clubs;</button>
            <button type="button" onclick="Incorrect()">5&clubs;</button>
            <button type="button" onclick="Incorrect()">6&clubs;</button>
            <button type="button" onclick="Incorrect()">7&clubs;</button>
            <button type="button" onclick="Incorrect()">PASS</button>
            <br>
        </p>"""
ans=input("正解:")
ans=ans.replace("!S","&spades;")
ans=ans.replace("!H","&hearts;")
ans=ans.replace("!D","&diamondsuit;")
ans=ans.replace("!C","&clubs;")
answer=answer.replace(f'<button type="button" onclick="Incorrect()">{ans}</button>',f'<button type="button" onclick="Correct()">{ans}</button>')

text=f"""<!DOCTYPE html>
<html>
    <head>
        <link href="styles/style.css" rel="stylesheet" type="text/css" />
        <title>{n}</title>
    </head>
    <body>
        <h1 id="number">{n}</h1>
        <h2 id="creator">Steven Jocker</h2>

        <p id="hand">
            &spades;{spade}<br>
            <span style="color: red;">&hearts;</span>{heart}<br>
            <span style="color: red;">&diamondsuit;</span>{diamond}<br>
            &clubs;{club}
        </p>

{bidding}
{answer}

        <p id="answer">
            rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr
        </p>

        <a id="Previous" href="Q{n-1}.html">Previous</a>
        <a id="Next" href="Q{n+1}.html">Next</a>

        <script src="scripts/main.js"></script>

    </body>
</html>"""

name=f"Q{n}.html"
with open(name,"w") as f:
    f.write(text)
    print("寫入完成")