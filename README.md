# SVCE Bus Schedule Scraper

## What is it?

It's a web scraper that checks the SVCE website's bus schedule and retrieves it. It then sends an email to everyone on its list with the schedule.

I've set it up to run every week so that I get a copy of the schedule without having to manually check the website.

## Requirements

* python3
* smtplib, bs4 modules, requests

## Instructions

Rename ```sample_config.py``` to ```config.py``` and fill in the details there. For information on how to get your gmail app password, refer to [this](https://support.google.com/accounts/answer/185833?hl=en).

That's about it. You can run it after that.

## Example Message:

~~~~
Hello future me! This is your weekly bus delivery! I mean bus schedule delivery! Toodles!

Date:07/07/17 Friday
Morning: 1,2/6,3,4/2,7,8,9,10,11/12,12,13,14,15,16,17,20,20,21,23/55,24,25/55,27,28,29,30,31,34,34M,36,36M,37,39,41,42,44,45,46,47,48,50,51,52,55A,56,57,58,60,60
Special(1:30):
Evening(3:30): 1,2/6,3,4/2,7,8,10,11,12,13,15,16,17,20,21,24,23,25,27,28,29,30,31,34,34M,36,37,39,41,42,44,45,47,48,51,50,52,55A,56,58,60,60
Late(4:30): 14,27,36,44,56,,

Date:08/07/17 Saturday
Morning: Schedule unavailable
Special(1:30): Schedule unavailable
Evening(3:30): Schedule unavailable
Late(4:30): Schedule unavailable

Date:09/07/17 Sunday
Morning: Schedule unavailable
Special(1:30): Schedule unavailable
Evening(3:30): Schedule unavailable
Late(4:30): Schedule unavailable

Date:10/07/17 Monday
Morning: 1,2/6,3,4/2,7,8,9,10,11/12,12,13,14,15,16,17,20,20,21,23/55,24,25/55,27,28,29,30,31,34,34M,36,36M,37,39,41,42,44,45,46,47,48,50,51,52,55A,56,57,58,60,60
Special(1:30):
Evening(3:30): 1,2/6,3,4/2,7,8,10,11,12,13,15,16,17,20,21,24,23,25,27,28,29,30,31,34,34M,36,37,39,41,42,44,45,47,48,51,50,52,55A,56,58,60,60
Late(4:30): 14,27,36,44,56,,

Date:11/07/17 Tuesday
Morning: 1,2/6,3,4/2,7,8,9,10,11/12,12,13,14,15,16,17,20,20,21,23/55,24,25/55,27,28,29,30,31,34,34M,36,36M,37,39,41,42,44,45,46,47,48,50,51,52,55A,56,57,58,60,60
Special(1:30):
Evening(3:30): 1,2/6,3,4/2,7,8,10,11,12,13,15,16,17,20,21,24,23,25,27,28,29,30,31,34,34M,36,37,39,41,42,44,45,47,48,51,50,52,55A,56,58,60,60
Late(4:30): 14,27,36,44,56,,

Date:12/07/17 Wednesday
Morning: 1,2/6,3,4/2,7,8,9,10,11/12,12,13,14,15,16,17,20,20,21,23/55,24,25/55,27,28,29,30,31,34,34M,36,36M,37,39,41,42,44,45,46,47,48,50,51,52,55A,56,57,58,60,60
Special(1:30):
Evening(3:30): 1,2/6,3,4/2,7,8,10,11,12,13,15,16,17,20,21,24,23,25,27,28,29,30,31,34,34M,36,37,39,41,42,44,45,47,48,51,50,52,55A,56,58,60,60
Late(4:30): 14,27,36,44,56,,

Date:13/07/17 Thursday
Morning: 1,2/6,3,4/2,7,8,9,10,11/12,12,13,14,15,16,17,20,20,21,23/55,24,25/55,27,28,29,30,31,34,34M,36,36M,37,39,41,42,44,45,46,47,48,50,51,52,55A,56,57,58,60,60
Special(1:30):
Evening(3:30): 1,2/6,3,4/2,7,8,10,11,12,13,15,16,17,20,21,24,23,25,27,28,29,30,31,34,34M,36,37,39,41,42,44,45,47,48,51,50,52,55A,56,58,60,60
Late(4:30): 14,27,36,44,56,,
~~~~
