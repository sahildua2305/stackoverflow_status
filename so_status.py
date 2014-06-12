import urllib2
import smtplib
from bs4 import BeautifulSoup

def check(found):
    link = "http://stackoverflow.com/questions/24178980/how-to-monitor-vlc-player-on-windows-7-using-python"
    url = urllib2.urlopen(link)
    data = url.read()
    soup = BeautifulSoup(data)
    if soup.find('div', class_="answers-subheader").h2.__str__() != "<h2>\n</h2>":
        print "There is an answer"
        try:
            smtpObj = smtplib.SMTP('127.0.0.1', 25, 'localhost')
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail('sahildua2305@gmail.com', 'sahil@collegespace.in', "There is an answer to your StackOverflow question.\nCheck here:<a href='"+link+"'>Question</a>")
            print "Email Sent!!!"
        except:
            print "Error: Unable to send email!!!"
        return "Yes"
    print "There is no answer as of now"
    return "No"

if __name__ == '__main__':
    found = "No"
    while found == "No":
        found = check(found)
