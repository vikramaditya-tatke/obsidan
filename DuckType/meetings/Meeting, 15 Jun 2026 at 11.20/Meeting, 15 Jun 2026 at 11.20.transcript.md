---
id: "51368775-acfe-440d-9389-6e8f8c7e9f9a"
name: "Meeting, 15 Jun 2026 at 11:20"
createdAt: "2026-07-06T15:39:27.065501+00:00"
---

# Transcript

**[You]** 00:00
do a lot of people know about this it's kind of new and it's a Mac thing yes so when you yeah you download all the models and then you get a very nice transcript in front of you also you should be able

**[You]** 00:15
to use this to just dictate into other apps.

**[You]** 00:25
Yes Can I try? It's already like

**[You]** 00:29
A setup for like is it any language or Try I don't know what to say Try whichever language you can

**[You]** 00:38
Uh

**[You]** 00:39
Bisa nanggep ini ga?

**[You]** 00:42
yeah

**[You]** 00:43
They're the local journey. Okay, probably not. Yeah.

**[You]** 00:48
that's the kind of local club

**[You]** 00:50
It got it, but does it not translate what it means? No, no, it won't. It won't translate. So this is just a transcription. You can set it up to do all sorts of different things.

**[You]** 01:04
Anyways Yes, so criminal IP Yes Criminal IP is an example of threat enrichment lookup Against a third party API Yeah

**[You]** 01:13
with EDR enrichment

**[You]** 01:16
We have onboarded certain customers for EDR. We don't have all customers onboarded for EDR which we have for MDR meaning Azure Sentinel So EDR is like all the MDRs?

**[You]** 01:31
Defender for end points, Sentinel One, Crowdstrike, that type of stun Vectra. Sorry, not Vectra. Vectra is NDR.

**[You]** 01:44
Yeah, this is fine Yeah, it's fine So We do enrichment for Vectra as well What's Vectra? It's just another provider Yes Like that Yes Okay There's too many providers Yes

**[You]** 01:59
each of these events on these tools to get more information about those events.

**[You]** 02:05
and how you have the sentinel one agent installed on your laptop which runs forever so if there is any incident that is being triggered

**[You]** 02:17
for your laptop You can look it up on Sentinel 1 and it will give you even more information because it doesn't only have access to cloud but it is constantly running on your machine so it collects all the

**[You]** 02:32
all the low-level details as well. Yeah. So we performed that.

**[You]** 02:46
Okay, now we have NLM classification

**[You]** 02:59
So then what does it actually do with it? It's all enrichment basically, just ties it to the original data, just like source enrichment basically.

**[You]** 03:11
Mmhmm

**[You]** 03:13
Okay We have LLM classification Which is actually a lot earlier in the workflow Not here So does he need to update that? Yeah You need to update that When does he go?

**[You]** 03:25
Literally after this We'll probably add it Before even pushing to The common SQSQ

**[You]** 03:33
probably so this LLM classification so actually though yeah probably but we don't know it's going to look a little bit different right it will look different by the time we are done with it for each SEM

**[You]** 03:48
because I know that

**[You]** 03:50
Mohsen said for Sentinel he's already created the LLM classification yes Qradar he has not so then actually we need to reflect it what this diagram is like now versus maybe six months planned type thing yeah definitely it's

**[You]** 04:05
The processes will change quite a bit as we go along. The overall idea stays the same. So does LLM classification?

**[You]** 04:15
need to be its own work strength.

**[You]** 04:22
So in my plan you see how this is how we've broken it down. We've got ingestion layer, source enrichment layer, and then the main layer. But actually we've pulled out eliminate use case manager for cyber security.

**[You]** 04:37
This is still my LLM classification, isn't it? Use case manager is static So what happens right now But there is not What I'm saying is This step is to get rid of it

**[You]** 04:49
LLM classification is already present in the existing workflows. Yeah, LLM classification. So the way LLM classification is triggered right now is if you don't find a use case for an incident or an alert,

**[You]** 05:04
in the database, then you use LLM classification.

**[You]** 05:09
What would we call that layer?

**[You]** 05:11
LLM classification or what?

**[You]** 05:15
Technic, for me, at least even for DEMA, it doesn't matter if it's a separate workstream, it can be on the same level as EDR enrichment.

**[You]** 05:26
EDO Enrichments under the main workflow yeah so this is also a part of main workflow technically so this is maybe because it falls out maybe related to like in Jira you can say related to that other task something like that

**[You]** 05:41
Thank you

**[You]** 05:47
do you get what I'm trying to say at the moment I've kept it

**[You]** 05:53
separate but actually

**[You]** 05:55
So, talk me through about that LLM classification. It's going to look before this. Probably, yes. And then it's going to look different between all the sims, for now? No, no, no. They'll look the same.

**[You]** 06:10
for all the seams, it is going to look the same. The idea is for a datadog, there is no use case manager. Right now, we are just using LLM classification for datadog. For curator and Azure Sentinel, we have a

**[You]** 06:25
No use case manager You're serviced for a datadoc No use case manager Why? I never made one

**[You]** 06:34
Datadog is there

**[You]** 06:37
but do you not need it?

**[You]** 06:38
No, you never created one, right? So use case manager is something that we create, the SOC analysts create What is the purpose of it again, sir?

**[You]** 06:50
um

**[You]** 06:52
Too technical, to be honest.

**[You]** 06:55
It's okay Use case manager is just You're using it to classify an incident

**[You]** 07:06
So yeah, it would come before surely

**[You]** 07:10
I

**[You]** 07:13
yes

**[You]** 07:18
Because then like it would say...

**[You]** 07:20
Is this type of incident X workflow would generate?

**[You]** 07:25
It might also come as a first step in this main workflow as well, just to keep all the logic separate again, same like we are doing for ingestion layer versus source enrichment. Just to keep the logic separate, we might put LLM.

**[You]** 07:40
classification or use case classification rather not LLM classification classification as the first step in the main workflow so yeah let's do classification as a thing so it would either be LLM classification or use case management

**[You]** 07:55
which is static so this

**[You]** 08:04
LLM classification and like if I just had to

**[You]** 08:10
It's dynamic

**[You]** 08:12
yes it is

**[You]** 08:15
LN classification is currently being used when use case manager

**[You]** 08:21
fails to classify.

**[You]** 08:35
ok

**[You]** 08:36
so Datadog not needed, sentinel so then this is hybrid then the same, because it's a sentinel sentinel has a use case manager

**[You]** 08:46
but this is what Josh is telling me to get rid of because apparently because everything is hard-coded there's a lot of human error there

**[You]** 08:55
I don't know about that a lot So I think when we move to Astronomer This is going Yeah It's just gonna be LLM classification Which I feel is so wrong You feel is so wrong Yeah Trusting and then

**[You]** 09:10
LLM produces stuff. LLM's a non-deterministic. So it's like chat GPT, it's like AI-based? They're non-deterministic. They can't provide the same result twice.

**[You]** 09:25
So what's the problem with using the model that we have now, the hybrid, where it comes in as things fight? I feel like that sounds like a good thing to me as well, but I don't really know. It was never a part of my...

**[You]** 09:40
That's the plan though. This will go, that's gonna be the move forward. Alright, so is that the same Sentinel Annex deal?

**[You]** 09:51
and then we got Key Radar

**[You]** 09:54
Well at the moment isn't Curator just, it's both Use Case Manager and LLM?

**[You]** 10:02
if I remember correctly

**[You]** 10:08
so the plan

**[You]** 10:10
plus four use case

**[You]** 10:13
too good

**[You]** 10:15
this is

**[You]** 10:16
Use Case Manager

**[You]** 10:19
thank you

**[You]** 10:20
okay sorry I'm really taking up a lot of your time now that's good classification okay so then you have LLM decision making I still need to know what how the decisions are being made

**[You]** 10:34
I don't know TBC, DEMA

**[You]** 10:39
where

**[You]** 10:41
classifications

**[You]** 10:46
Okay?

**[You]** 10:47
so then you've got sorry what's the other one

**[You]** 10:55
Okay

**[You]** 10:57
Decision making is basically just deciding whether it is a false positive or not

**[You]** 11:03
What was the thing again? LLM decision making

**[You]** 11:08
How would it be? Sajun making So it decides What is it sorry? Decides

**[You]** 11:16
whether it's a false positive or not

**[You]** 11:24
okay yeah if it is false positive

**[You]** 11:28
e

**[You]** 11:30
discard it

**[You]** 11:33
It auto-closes

**[You]** 11:36
I believe so

**[You]** 11:39
They seem to discuss that piece

**[You]** 11:41
Well actually does it just discard it altogether or will it still create a thing that will...? Currently once discarded they are stored in a database

**[You]** 11:56
It's not shown in the UI? No, not shown in the UI. Just for us, for whatever reason, if something is wrongly classified and we need to debug later on.

**[You]** 12:07
so if all is possible then it discards it but it's still stored in what like an S3 bucket or something yeah it can in a database is fine for now

**[You]** 12:22
yeah

**[You]** 12:25
it's almost like I'm actually starting to understand the business yeah it is so even I'm sure this is like still 50% of it there's a lot more things coming our way

**[You]** 12:40
I'm sure and the AI summary summary is nothing but a summary of the incident that is shown on the UI

**[You]** 12:51
I bought the... Oh is it now? Yep

**[You]** 12:56
Apologies Oh, okay Erm, yeah, so what I'll... If you're free, I'm gonna come...

**[You]** 13:05
actually maybe in the afternoon yeah okay I just want to go through the rest but I also want to understand for the enrichment layer what are the tasks we actually need okay yeah

**[You]** 13:20
okay right cheers

**[You]** 13:22
Marie

