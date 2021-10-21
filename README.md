# Trading-signals-scanner
This is a  market scanner that, given data of the major support and resistances to track for some stocks or cryptos, scans the markets twice a day and communicate through telegram API  the price of a given stock or crypto that reached a support or a resistance

In this read.me file I'll go through the functions used and what's the idea behind them.

TelegramMex just allows us to communicate with our telegram account: In order to do that, we need to create a group (for you and all people you want to send signals) and add a bot to this
group. The send method will just send a message with all information and data to the group.

The Supp_Res and EMA classes are used to build objects that help us to identify the type of signal we are sending (the EMA idea is yet to be implemented, so for now only Supp_Res is used).
It has attributes like the relative tycker for that signal, the price range where we expect to find the support/res (we don't use a single value because it would be impossible to track it:
we are using free data from yahoo finance API so we can't have total precision but is not necessary if you use this code for large timeframes as 1 week).

Then we save the relative used timeframe (again: using a 1-week timeframe is the best choice!) and all other ranges, to evaluate how much this range is away from the others (we need to know this to understand his strength).

Then, we have a Signal class, that contains an object Signal_type (like Supp_Res) and is identified with a unique ID.

Scanning function just the search: for each supp_res it downloads data from yahoo API and looks if the price is in the range of a supp/res range. If it is it will send a telegram mex. 

We also save all the generated Signals in JSON files to track them  and avoid generating signals if they have been already generated (if already in JSON --> don't generate a signal)

In the main file, we just add all the data and run all this process.
