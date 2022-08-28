# Project-Abe-Shinzo
<b>This is an ongoing project for my study about the Chinese comments on Bilibili on the day Abe Shinzo was assassinated.</b>

All codes but the scraper of Bilibili comments, as you see here, are my creation. The NLP functions are from HanLP.

<i>This project is in memory of my late uncle who passed away one week before the news broke.</i>

# Modules
## csv_processor
Comparing data from two different batches of data: (a) the one I scraped within one hour after the news broke; (b) the one I scraped about 12 hours after. 
(I don't have more data between these two because I needed to go to sleep as the news broke during the midnight.) 
I developed this module because I found that lot of the comments I scraped into the first data files were censored by the authority.
With this module, the 2 data files I got from the Bilibili video clips of each of the four Chinese media (CCTV.com, CCTV News, Huanqiu, and Xinhua) are rearranged into three different data files: (a) the comments that got censored, (b) the comments that are only seen on the second batch, and (c) comments that are seen in both data files.

## Emoji_counter
I developed this module to know (a) how many kinds of different (Bilibili) emojis have the users used during the time and (b) how many times were each emoji used in the comments.
This module uses the csv files produced by csv_processor in this project.

## Emoji_deleter
After discussing with <b>Ms. Yuhan Li (李雨浛)</b>, a friend who has done similar studies, I decided to exclude all the emojis from the first manuscript because the ones used by Bilibili need to be carefully assessed by lots of people in a similar way like [Godard and Holtzman (2022)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9231464/) before they can be used in computer-assisted analysis of the comment texts. So I developed this module to get rid of the emojis for the sake of comment text analysis.

More modules are to be developed.

# P.S.
<b>Professors in communication or related fields, please consider Yuhan if she applies for your institution this fall as she is going to graduate from the master program of Tsinghua University. She is a very promising scholar and she is one of the winners of the EnvComm top student paper award in ICA2022.</b>
