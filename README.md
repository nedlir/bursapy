# :chart_with_downwards_trend: Welcome to Bursa Signaler!  :chart_with_upwards_trend:

Bursa Signaler is a simple python script utilizing [Bizportal](https://www.bizportal.co.il)'s API. The script is designed to assist those who are interested in following Israeli stock market papers in their portfolio efortlessly.

Bursa Signaler provides you updates regarding a stock drop or rise in value through favourite communication method: WhatsApp, SMS or Email.

Bursa Signaler lets you choose a percentage or point rate targets of the stock you follow and informs you by the chosen method whether the target change occured. This allows you to invest passively without constantly checking your portfolio. This practice has been suggested by [behavioural economy researchers](https://en.wikipedia.org/wiki/Robert_J._Shiller) as an healthy practice.

Bursa Signaler gives you the chance to capitalize on [flash crashes](https://en.wikipedia.org/wiki/2010_flash_crash) or any crash in the stock market as a long term investor.

Please refer to disclaimer in the next section before utilizing the script.

## Disclaimer :page_with_curl:

>The information contained herein is provided for informational purposes only, is not comprehensive, does not contain important disclosures and risk factors associated with investments, and is subject to change without notice. 
>The author of this code (from now on: The author) is not responsible for the accuracy, completeness or lack thereof of information, nor has the author verified information from third parties which may be relied upon. 
>The information does not take into account the particular investment objectives or financial circumstances of any specific person or organization which may view it. 
>The author is not a registered investment advisor and does not represent the information as a recommendation for users to buy or sell the securities under discussion. 
>Nothing contained within may be considered an offer or a solicitation to purchase or sell any particular financial instrument. 
>All liability for the content of this information, including any omissions, inaccuracies, errors, or misstatements is expressly disclaimed. Always complete your own due diligence. Before making any investment, investors are advised to review such investment thoroughly and carefully with their financial, legal and tax advisors to determine whether it is suitable for them.
>Investing in the mentioned securities is dangerous and may cause a loss of the entire invested capital.
>If you act according to information presented on this page and by using the code you bear sole responsibility for the results of these actions, the author shall not be held responsible for any such action whatsoever.

Alright, now that we are done with the necessary CYA, let's go straight over to the usage instructions of the script.

## Instructions :book:

Please install required packages and follow the instructions.
Check [example.py](example.py) for an example of how this script may be implemented.

### Requirements :clipboard:
- Python 3.8 is the version the script was built for, it may work on earlier versions as well.
- Sms and WhatsApp communication require account at [Twilio](https://www.twilio.com).
- Install missing packages from [requirements.txt](requirements.txt) file.

### Communication :mailbox:

At the moment these are the communication methods available, you are more than welcome to use more than one.

| *Communication Method* | *Code* |
| ------ | ------ |
| **Mail** | `'mail'` | 
| **Gmail** | `'gmail'` |
| **WhatsApp** | `'wapp'` |
| **SMS** | `'sms'` |


### Usage :bar_chart:
- Follow the instructions written inside the [example.env](example.env) and create a brand new *.env* file.

- Choose a paper from Israeli Bursa to follow, the paper's ID should be inserted as a string argument of a Paper object. 
    - Example: 
    
        If we would like to follow `תכלית - MSCI World - 5124573`, we will create a new object and pass the paper's ID as a string.

        `paper1 = Paper('5124573')`
    
- The program provides 2 methods to trigger an update, by daily percentage change or by a points rate change.



   - For a percentage change update put a percentage target. Percentage target could be either a rise or decrease in value (i.e: -0.3% or 6%). If you would like to recieve daily mail regardless of any change, just type "0".
       - Example:
            ```
            paper1 = Paper('5124573')
            signaler.send_percentage_change(paper1, -4.7, 'wapp')
            ```
        The code above will send us an update by WhatsApp every time the paper's daily percentage rate drops by -4.7%.

   - For a points rate change update put a desired rate target.
       For a change *above* target points rate type **`True`**,
       for a change *below* target points rate type **`False`**.
       - Example:
            ```
            paper1 = Paper('5124573')
            signaler.send_rate_change(paper1, 1500, True, 'gmail')
            ```
        The code above will send us an update by Gmail every time the paper points rate is above 1500.

- Kindly note that a preffered communication method code should be typed into the 'communicate' argument regardless of the method chosen.

## Using Bizportal's API :book:

Sending multiple requests during a short period of time is not respectful to the good people at Bizportal. Please abstain from abusing this code and use it as Peter Parker's Uncle would suggest.

## License
[MIT](LICENSE.md)
