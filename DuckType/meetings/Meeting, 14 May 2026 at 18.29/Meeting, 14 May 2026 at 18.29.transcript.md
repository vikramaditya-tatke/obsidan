---
id: "d2aea396-5833-471b-9992-7920a2e215dd"
name: "Meeting, 14 May 2026 at 18:29"
createdAt: "2026-06-15T10:20:28.715939+00:00"
---

# Transcript

**[Them]** 00:00
So that's there. That's released right now under a feature flag. So we've got a group of companies who are trying it. And yeah, response has been really good. We'd be happy to bring you guys in.

**[Them]** 00:15
into that preview also. And then the next one is the ClickHouse adapter, or direct ClickHouse connector. So right now, evidence manages

**[You]** 00:22
mhm

**[Them]** 00:30
We do a lot in that warehouse, like we manage row level security and access control rules. We tie those to the identity of the users in the application. And then we also flow into the user's data.

**[You]** 00:32
Hmm

**[You]** 00:41
hmm

**[Them]** 00:45
and follow control over those sessions to the embedded APIs, which I'll talk about in a second. We're going to be bringing that ClickHouse connector. What we're doing under the hood for our

**[Them]** 01:00
and we're going to basically expose that as a bring-your-own click house and evidence will connect to that extremely natively. I think it'll be our most

**[You]** 01:03
嗯

**[Them]** 01:11
like full featured kind of native connector that we that we offer because you know we've been building on top of Clickhouse for for so long. So that should be coming I think in the next like two or three weeks. So I think I think

**[You]** 01:18
right

**[You]** 01:24
Okay

**[Them]** 01:26
I think that's gonna look really good to you guys. It'll certainly have a better kind of like native row level security, click out support, all the tuning and stuff than the like Sigma story. I don't know as much about this.

**[You]** 01:34
hmm

**[Them]** 01:41
the other tool that you mentioned. But yeah, so I think that'll be a great fit. And of course, then your data is staying in your infrastructure. And then the final piece here, which actually isn't something that we're currently working on, but is not really

**[You]** 01:48
right

**[Them]** 01:56
is not really that tricky. It's like, let me show you how is this like no iframe requirement?

**[You]** 02:04
hmm

**[Them]** 02:05
I don't think we would give you back, like right now, our embedding system, you call an API, we give you back a link, you drop it into an iframe. And that's kind of the flow for creating like a session that has row level security.

**[Them]** 02:20
attributes attached into an interactive dashboard that you can embed in your app. And that works for lots of very large compliance-heavy customers. But I hear you, maybe you guys are even a step up beyond the

**[You]** 02:23
Mhm

**[You]** 02:25
Mm-hmm

**[You]** 02:32
mm-hmm-hmm

**[Them]** 02:35
like insurance tech folks that are using that flow. But what I think we could do is really like basically give you a web component or a TypeScript, you know,

**[You]** 02:38
heheheheh

**[Them]** 02:50
component that you could add to your front end and then rather than returning, you know, an iframe and serving that session, we would return markup or basically something

**[Them]** 03:05
that could render into the browser. So that's pretty light because that's how the rest of the tool works. Like, that's how we serve dashboards. We're not iframing them internally. So like, that's more of just a reshaping of the,

**[You]** 03:12
you're right yeah, yeah

**[You]** 03:16
Yeah

**[Them]** 03:20
off of iframe and onto a TypeScript dependency. I think there's other people who would choose that.

**[You]** 03:27
Mm-hmm

**[Them]** 03:29
And then like the iframe has a bunch of it's just really simple for people to to adopt. So I would imagine we'd offer both but

**[Them]** 03:38
Yeah, I think we could probably overcome these three, uh, kind of requirement challenges. Um, the way I can share how we, we work on, uh, like procurement processes. And of course we're, we're happy to like adjust

**[Them]** 03:53
to your timelines and your flow. But typically we run a 30-day proof of concept. We open a private Slack or Teams channel with the team that's evaluating the tool.

**[You]** 03:57
mm-hmm

**[You]** 04:00
mm-hmm

**[Them]** 04:08
We do a weekly touchpoint with our team. And the goal, especially for embedded cases, is you want to have something that is ready to go live with your first pilot customers during those 30 days.

**[Them]** 04:23
And yeah, we'll ship the handful of features that are required to close the gap there. So yeah, that's how we typically approach this. We run a POC and most customers get their use case live in a couple weeks.

**[You]** 04:28
Mm-hmm

**[Them]** 04:38
any features that are required we commit to delivering those during the proof of concept period and yeah

**[You]** 04:38
nice

**[You]** 04:46
Okay

**[You]** 04:47
okay so sounds very interesting to be honest so that that's that's very good to hear well just coming back to the click house integration that you mentioned so why why do you say it will be like one of them

**[Them]** 04:58
Yeah.

**[You]** 05:02
most native connections that you have

**[Them]** 05:06
Yeah, so we're releasing native support for Snowflake and BigQuery this week, and then we're going to follow on with our ClickHouse connection. The reason I say that it'll be the most native is like, we

**[Them]** 05:21
We currently serve a large number of customers who have embedded reporting use cases with row level security and access control and all those things. And we serve them through our like managed Clickhouse instance. And so we're managing

**[Them]** 05:36
publicist instance on their behalf, letting them manage all their row level security. So it's just the data warehouse that we have worked the most with and that the product is already sort of designed to work with. We're just exposing the ability to bring your own.

**[Them]** 05:51
I think it's going to be the kind of most featured depth in terms of like

**[Them]** 05:56
Managing access controls, you know, all the like little things that bite you when you're adapting this platform like this for other warehouses, like it's the one that it's been on the longest. So yeah. Does that make sense?

**[You]** 06:07
Hmm, okay

**[You]** 06:11
yeah makes sense so basically what you're trying what you're doing is you are managing the data warehouse

**[Them]** 06:15
you

**[Them]** 06:17
Thank you.

**[You]** 06:19
for customers. So the customers are basically ingesting data into the Clickhouse instance that you are managing and then they see the dashboards that you present, right?

**[Them]** 06:26
Yeah.

**[Them]** 06:30
Yeah, exactly. So the tool has always had ClickHouse as the one warehouse that it's managing against. And then we're adding additional warehouses. So Snowflake basically,

**[You]** 06:35
hmm

**[Them]** 06:45
and then ClickHouse as warehouses that customers can bring.

**[You]** 06:45
嗯

**[You]** 06:49
Okay, and when he's mentioned that data can live within our own infrastructure, how would that work? I tried with Evidence Studio and I connected it to Mother Duck. So it takes quite some time to sync.

**[Them]** 07:01
Sure

**[You]** 07:04
the data and then it syncs on a schedule so that led me to believe that the data is being pulled out of mother duck into the backend that evidence has and open source evidence has duckdb as the backend right

**[Them]** 07:05
Yep, yep.

**[You]** 07:19
you

**[Them]** 07:20
A hundred a hundred percent that's a totally correct understanding of the offering uh

**[Them]** 07:28
today. We are launching native support for Snowflake and BigQuery likely in the next week. Like we've already got customers running on them. That moves all of the queries that are being generated from evidence, though

**[You]** 07:43
Mm-hmm.

**[Them]** 07:43
Those go directly to the underlying warehouse. So there's no sync, there's no kind of data movement associated with those. And that's what we'll be offering for ClickHouse as well.

**[You]** 07:56
Okay, so that makes sense. So any query that we have in the data models, if you have to find any data models and any SQL query that we've put there, we'll go back to SQL.

**[You]** 08:11
like push down to click house and then it's like a live connection compared to like a refreshed connection

**[Them]** 08:12
Exactly.

**[Them]** 08:16
Yes.

**[Them]** 08:18
Exactly, exactly

**[You]** 08:20
Okay, that's very nice to be honest. A lot of the BI tools that we are looking at currently, they have their own caches, they have their own storage systems, right? They have their own storage formats as well.

**[You]** 08:35
as well. They have the different backups. That's like very heavy tools. We have and since that's something that I was worried about because if it's syncing the data, there's quite a lot of our reports where

**[You]** 08:50
Currently all of our business logic resides within the BI tool itself. So what they do is they just pull like massive amounts of data from click house because they just do like a select star.

**[You]** 09:05
and make all the changes. Yeah.

**[Them]** 09:06
Oh yeah, no. Yeah, this will be way better. Because if you think about how our system works today, we were syncing all of this data into a ClickHouse cluster that we were running. And then every chart is like writing ClickHouse queries.

**[You]** 09:12
yeah

**[Them]** 09:21
to get just what it needs for that chart. And we're just removing that sync step. We'll just query your ClickHouse directly. And so it should be it should be much better than like a BI tool that's doing like select star and then

**[You]** 09:26
Yeah.

**[You]** 09:28
Yeah.

**[You]** 09:36
Yeah

**[Them]** 09:36
and doing all aggregations will push all the aggregation down to your ClickOS instance.

**[You]** 09:40
Yeah

**[You]** 09:41
Yeah, that makes...

**[Them]** 09:43
And then just Vikram, just to be 100% sure though, so data at rest is stored in your ClickHouse. We will send you queries. Your ClickHouse is going to respond and send us back results.

**[Them]** 09:58
And we only have like a cloud, we only have a cloud offering. So I just want to ask you a question.

**[You]** 10:04
Hmm

**[You]** 10:11
that's fine

**[Them]** 10:13
I just wanna make sure that's okay, yeah.

**[You]** 10:14
yeah no that's fine so we don't expect to have like to deploy it on our own uh premises uh even with clickhouse we are deployed on clickhouse cloud so we haven't deployed it on our own aws infrastructure so yeah so that would be like a

**[Them]** 10:19
Yeah

**[Them]** 10:23
Right.

**[Them]** 10:27
Yeah, okay.

**[You]** 10:29
we are also with astronomer for our data pipelines so the only thing that we are concerned about is having like a private link between all of the data flow so even right now we have like a lot of

**[Them]** 10:33
Nice.

**[You]** 10:44
There are a lot of data sources that are deployed on our own infrastructure in AWS. So when you're sending the data out, it goes via private link to astronomer. When astronomer sends the data back to buckets in our account, there's a private link.

**[You]** 10:59
link and when a astronomer sends data to click house there's again a private link so we would

**[Them]** 11:03
yep

**[You]** 11:05
You'd also want the private link to extend from ClickHouse to the BI tool

**[Them]** 11:10
Got it. Okay.

**[Them]** 11:12
I'm not the final authority on this portion of it. This is another team member who will be able to advise on this, but that does make sense to me.

**[You]** 11:15
yeah

**[You]** 11:17
That's alright

**[You]** 11:22
Okay

**[You]** 11:23
okay perfect so if you were to say talk about next steps how would that look like like if it's the POC phase and there's a lot of enterprise features obviously that we are very interested in this SOC 2 type

**[Them]** 11:34
yeah

**[You]** 11:38
2

**[You]** 11:40
is one of them also how does the pricing look like do you if you have say now we have 200 customers at the moment for simplicity sake then do you would you charge like

**[Them]** 11:40
Yep.

**[Them]** 11:45
Sure.

**[You]** 11:55
like one seat per customer, or would you just charge the seats that are for developers who are going to actually develop with evidence,

**[Them]** 12:05
Yeah, so for internal users, we've got just one seat price. So it's $25 a month on the pro tier. It's $15 a month on the team tier. And, you know, enterprises are right around.

**[Them]** 12:20
around there as well. So for internal seats, it's just one seat price and it's based on the number of seats that you want to have. And then for embedded and customer facing cases,

**[You]** 12:21
Mm-hmm

**[Them]** 12:35
I would say quite a lot more flexibility. Most of our embedded customers buy on a per customer organization level, basically like on a per tenant level. And then we give unlimited individual

**[You]** 12:50
hmm

**[Them]** 12:50
users within those tenants. So it's basically would be like a license for 200 customer logos and then unlimited individual users. For the most part, that's the direction that folks have wanted to go because

**[You]** 12:56
Yeah.

**[You]** 13:01
Mmh

**[Them]** 13:05
they know what their margins are at the like customer logo level. They don't want to be managing, you know, individual seats within the customer, but we're happy to do it on a, on a seat basis as well. So is it 200 individuals or is it

**[You]** 13:13
hmm

**[Them]** 13:20
200 companies with many individuals and

**[You]** 13:22
S

**[You]** 13:24
200 companies and then there might be like a few individuals in each company.

**[Them]** 13:31
Got it

**[You]** 13:31
like that yeah um so embedded so that will be it will basically have the style of our own platform right like obviously the charts will still look like evidence as they look but they they're they're everything

**[Them]** 13:41
Yeah.

**[You]** 13:46
around it would be

**[You]** 13:48
style of the platform

**[Them]** 13:51
Yeah. So embedding is today like an iframe will give you like a renderer dependency that you can use in the front end so you can render it like natively. We have a pretty large combination.

**[Them]** 14:06
collection of theme options for colors and those types of things. And then generally our apps have a pretty neutral kind of modern style that fits in most people's applications. If you said like

**[You]** 14:15
yeah

**[Them]** 14:21
We need a theme option, which is like take the corner radius and instead of it being like rounded on buttons, like we need it squared because, you know, we're a security company and so we don't do border radiuses.

**[You]** 14:25
Mm.

**[You]** 14:32
hmm

**[Them]** 14:36
You can add theming tokens to allow you to adjust that to fit it better. Where I don't think or like I would have more of a question mark of it is like

**[You]** 14:37
Right

**[You]** 14:40
Mhm

**[Them]** 14:47
If you wanted to go, I think you mentioned Sigma has custom React components or something, I'd have to go look at what they're offering there.

**[You]** 14:56
Mm-hmm

**[Them]** 14:59
there's going to be some limitation in terms of like

**[Them]** 15:03
uh

**[Them]** 15:06
You know, do you want access to all the every sort of line of CSS that makes up the system? But on the other hand, I don't know why you would, if you want to build them all custom why buy the platform?

**[You]** 15:11
right

**[You]** 15:14
no probably yeah yeah

**[You]** 15:18
yeah no i don't i don't mean like that um so there has to be basically when you said like an iframe so if it was an iframe then the design around the iframe would be the platform and then

**[You]** 15:33
just the render would be the evidence chart, right?

**[Them]** 15:34
Yes.

**[Them]** 15:35
Yes. Yes, exactly. So our customers who embed via iframe, we give them just the evidence page that they're asking for. We don't give them any of the navigation, Chrome, no search.

**[You]** 15:38
Yeah

**[Them]** 15:50
nothing like that around it so it's just the report whether that's like

**[You]** 15:51
right

**[Them]** 15:57
two charts or a really long interactive data app. It's just the report. And then we do bundle with that, embed all of the data export. So your customer is going to export PDFs and not do

**[Them]** 16:12
download CSVs of data. Those types of things. Because those do wind up being pretty important even for embedded customers.

**[You]** 16:16
hmm

**[You]** 16:21
okay perfect that makes sense so I think that this sounds very good

**[Them]** 16:27
Evet

**[Them]** 16:29
And I think there was a question about pricing like competitive, if not slightly less expensive than Sigma would be like a benchmark. I have in your mind. There's no, we would not lose this on.

**[Them]** 16:44
price to Sigma so yeah the uh

**[You]** 16:47
Right

**[Them]** 16:51
Yeah, in terms of like, go ahead, I was going to talk about next steps, but

**[You]** 16:56
no yeah makes sense so this is like this is something that we would definitely like to explore and yeah if you can just maybe send an email with the next steps I can talk with my manager and see what he thinks of this

**[Them]** 17:02
Sure

**[You]** 17:11
and yeah

**[Them]** 17:12
What I would propose as a good next step is we should do a demo of the platform. So we've gone through the requirements, some that we have today, some which are shipping soon, and then one which is actually custom to your

**[You]** 17:27
hmm

**[Them]** 17:27
to your case, but we should go through a demo of the platform and talk about how the embedding mechanic works today, how row-level security works, show the end-user Q&A

**[You]** 17:31
yeah

**[Them]** 17:42
flow for your internal use case. See if there's other questions or requirements that we can surface through that discussion. I think if we can go through that and if it still looks like it's likely going to be a

**[You]** 17:51
Mhm

**[Them]** 17:57
Uh, a fit, then I'd propose we start working on a proof of concept and like contracting in, in parallel.

**[You]** 18:01
Yes

**[You]** 18:04
Yeah, no problem. Yeah, perfect. That sounds great. I can send you my manager's email if you don't have it already. I think it's in the ad guests. So one is Nita who's with us and then another is Nita.

**[Them]** 18:06
Okay

**[Them]** 18:11
Sure.

**[You]** 18:19
M. Mahadeq

**[You]** 18:20
if you have that email

**[Them]** 18:21
Yeah, they're both on here, yep.

**[You]** 18:24
yeah perfect so nice so he's my manager he couldn't be on the call today it's like quarter to seven right now here

**[You]** 18:34
in the evening but if you can send the next steps perfect and in the demo it would be nice if we can make focus on embedded analytics because that's somewhere where we currently have an iframe and there might be more

**[Them]** 18:38
Yeah.

**[You]** 18:49
push back on it.

**[You]** 18:51
uh also it would be nice to demo like the agentic creation of charts because uh that i believe is a very strong feature that you guys have right now um whenever i've like used it it never has really fallen

**[Them]** 18:56
Yeah

**[You]** 19:06
and it has done a very, very good job at doing it. It also did a very good job at correcting the syntax as using cloud opus 4.7. So I fed it, take the documentation of all the components

**[Them]** 19:08
Paz

**[Them]** 19:15
Yeah.

**[You]** 19:21
of evidence studio and like the specific pages of some of the components that I would want it to have in the chart, like for example, Sankey is something the agent doesn't do by itself a lot. You have to really ask it to do something fancy.

**[Them]** 19:31
haha

**[You]** 19:36
It gave it like that kind of documentation from Evidence Studio. It could correctly identify that there's a syntax difference between Evidence Studio and like open source evidence, but at the end of the day, it just, they were like all red lines.

**[Them]** 19:39
Yeah

**[You]** 19:51
for the components but when I asked your own agent to correct that it was able to correct like 10 charts or something in a go which is which is very nice right it's very very very good for an agent to be able

**[Them]** 20:00
Nice

**[Them]** 20:03
Yeah.

**[You]** 20:06
to do that all by itself.

**[Them]** 20:08
Yeah, we've got a CLI for studio now as well. And we're going to be bringing the studio syntax to our open source so that it's, it's all this all the same. We want the studio syntax in the next in the next

**[You]** 20:11
Hmm

**[You]** 20:19
yeah mm-hmm

**[Them]** 20:23
training run for Mythos, whatever the next model is, and then the CLI, our customers are using that a ton for Evidence Studios.

**[You]** 20:24
Yeah.

**[You]** 20:29
Yeah

**[Them]** 20:38
They're getting their coding agent, their cursors, and cloud codes to do a ton of work.

**[You]** 20:39
嗯

**[You]** 20:43
hmm

**[Them]** 20:44
Yeah, cool. Cool. And then any other like timelines, anything else that I should be aware of? Like how far along are you guys with in the decision and the process?

**[You]** 20:54
We are looking to move quickly right now. There's a lot of workload as well so we're working on a few other projects too. So like the team is busy with many things right now but we have

**[Them]** 20:58
Sure

**[You]** 21:09
if you're willing to move quickly especially with the demo at least definitely we can move as quick we can schedule one as soon as possible I'm sure my manager would be happy to hop on that call so

**[Them]** 21:10
Yeah.

**[You]** 21:24
with the next steps after the demo what happens is something that I can't promise right now how quick the response would be from our end we'll definitely because it's like a cross team thing that we need to look at we have or we have

**[Them]** 21:30
Yeah.

**[You]** 21:39
and obviously the front end team who needs to give their go ahead with this. They need to review what you've said or the documentation that evidence has, all the different options, look at the compatibility with the existing platform.

**[You]** 21:54
platform also like we have to work on it given our use case it would so i i appreciate that clickhouse connector you don't have you're not going to have it ready but

**[You]** 22:06
if you have any internal application, just to

**[Them]** 22:07
We I I think I think

**[Them]** 22:10
we should we should we should run the POC

**[Them]** 22:14
on some sample extracts. So like we, you guys should be building the, in my view, building the like thing that is going to ship to customers almost in parallel, and then we'll land the ClickHouse directly.

**[Them]** 22:29
connector and the non iframe embedding option during the POC, that would be my instinct. I don't think we want to block this on

**[You]** 22:36
hmm

**[You]** 22:39
That's right

**[You]** 22:42
yeah

**[You]** 22:44
Yes, yes

**[Them]** 22:44
on a connector. And because it's ClickHouse, anything that you're writing in evidence, you won't have any sort of SQL translation that's going to have to happen. It's already ClickHouse, yeah.

**[You]** 22:53
right

**[You]** 22:55
yeah so that's fine just for the demo right for the next steps it would be nice if we can at least demo like in any internal app that you might have that connects directly to click house just to give an idea of how it would look

**[Them]** 23:08
Sure

**[You]** 23:10
Like right now, if you, if you had to demo, like there is a sink, then, you know, later on in the conversation, it kind of becomes difficult to convince otherwise, because it's already been seen. And, you know, it's like that, that, okay.

**[Them]** 23:24
Okay

**[You]** 23:25
it's been perceived already right okay now we have to sync the data it's going to move the data we don't know if the connector is coming or not and that's that's basically the perception to at least give an idea so we can obviously demo the platform as it is right now but if

**[Them]** 23:27
Yes

**[Them]** 23:32
Okay

**[Them]** 23:35
Yeah.

**[You]** 23:40
If it is a possibility that maybe a small use case that you can showcase a direct connection, that would be good.

**[Them]** 23:47
you know

**[Them]** 23:48
Okay, yeah, I can highlight because we've got customers on the Snowflake direct connector now so I can highlight that in because that's in production now so I can at least show what that looks like.

**[You]** 23:59
Mmh

**[Them]** 24:03
and I will very much downplay the sync aspect because it's not relevant to you guys. Like, you guys are going to bring your own clickers, we'll connect directly to it. So, you know, I won't spend time on that. Cool. And then who are you pulling for in this?

**[You]** 24:08
yeah

**[Them]** 24:18
uh, in this three horse race.

**[You]** 24:20
uh

**[You]** 24:22
let's i don't know it's like it's up to the bi team so we we are like the darshan and i are part of like the data engineering core team like the lead for bi is kind of out of office right now so i'm just kind of helping out now

**[Them]** 24:35
Yep.

**[You]** 24:37
So let's see. It's completely up to them how comfortable they are with all this different functionality. If it were up to me, I definitely like evidence. I like that it is modern.

**[You]** 24:52
is modern it works very well I believe you also

**[Them]** 24:55
I was gonna say there's no way that you are gonna choose Sigma if it was just up to you. You don't want to spend your day clicking around all those menus.

**[You]** 25:03
No

**[You]** 25:05
No, that's not me I I believe you guys are also taking benefits of DuckDB Wasm. Are you not or is that open source?

**[Them]** 25:06
you

**[Them]** 25:15
That's in open source. That's really where ClickHouse sits in Studio. Those are kind of the same slot in the architecture.

**[You]** 25:20
Mmh

**[You]** 25:26
okay so yeah that's something that I really like so yeah I would be definitely rooting for Everton's but let's see it's a completely different team I'm just a rep right now

**[Them]** 25:35
Cool.

**[Them]** 25:39
Of course, yeah, yeah, yeah.

**[Them]** 25:41
Cool. Well, I really appreciate you taking the time to take me through the requirements. Genuinely, this is an area that has proven to have a really, really good fit for us, especially the embedded analytics.

**[You]** 25:42
yeah

**[You]** 25:55
mhm

**[Them]** 25:56
People really care about what's going into those things. They want to be able to update them quickly, and they want to run them under version control. So, yeah, I appreciate you taking the time. I'll follow up with some proposed times for a demo and a demo.

**[You]** 26:04
yep

**[Them]** 26:11
and then we can hopefully move into a proof of concept.

**[You]** 26:14
yeah makes sense if you just if you don't mind me asking who are like your top customers at the moment would I know them by any chance

**[Them]** 26:23
Yeah, I mean, like, Apollo Management is probably the largest open source user.

**[You]** 26:33
mm-hmm

**[Them]** 26:34
They're like a multi-trillion dollar. Then there's two teams at Apple that also use evidence. Again, they're on prem completely.

**[You]** 26:42
Mm-hmm

**[You]** 26:44
Mm-hmm

**[Them]** 26:47
Victory Plus is a pretty cool company. They're a media streaming business. They do embedded and customer facing analytics. So they stream into live event data into

**[Them]** 27:02
through Iceberg, and then they serve like real-time analytics back to their, um, advertising partners through, uh, through there.

**[You]** 27:04
mhm

**[You]** 27:09
Mhm

**[Them]** 27:11
who else is a cool customer nobody who's in the like security vertical like exclusive dialogue health they're a big insure tech in in Canada so they've got

**[Them]** 27:26
A hundred thousand or so businesses and HR reps logging in to look at benefits consumption, that type of thing. They're cool. I guess they're not really a startup anymore. They've been acquired by a large insurer.

**[You]** 27:28
hmm

**[You]** 27:34
nice

**[Them]** 27:41
but really cool company obviously very compliance heavy use case

**[You]** 27:41
Right

**[You]** 27:45
hmm hmm

**[You]** 27:47
okay that's that's very good to hear

**[Them]** 27:50
Yeah, no, the benefit that we're having from Claude code is just tremendous, right? Every call is, you know, for the most part, it's like, hey, we don't want to do this work anymore. We want Claude to do it.

**[You]** 28:03
Yeah.

**[Them]** 28:05
get us off of Tableau or Sigma or whatever.

**[You]** 28:05
yeah i think that's really the

**[You]** 28:08
yeah it's the beauty of like BIS code certainly it's version controlled it's lightweight and since the warehouses are so powerful these days

**[You]** 28:20
i can't think of a situation where if the data is modeled correctly you would need to have these massive bi tools sitting in front of the warehouse because you're using click house right now anyways

**[Them]** 28:31
For sure.

**[You]** 28:35
if you were to scale to the highest end possible, let's say on an EC2 instance, I'm sure that ClickHouse is going to process

**[You]** 28:43
like absurd amount of data

**[You]** 28:46
Very fast So Yeah

**[Them]** 28:48
Oh yeah

**[Them]** 28:50
Yeah, it's really like you're trying to give a sort of identity and like context frame around the warehouses and have a place that's like token efficient to generate reports and dashboards.

**[You]** 29:01
Yeah.

**[You]** 29:03
yeah

**[Them]** 29:05
with the stuff.

**[You]** 29:06
Yeah, alright.

**[Them]** 29:06
Cool. Well, thanks for taking the time. I'll follow up with some proposed times and yeah, excited to work with you guys on this.

**[You]** 29:13
like this all right thank you so much cheers have a good day yeah bye

**[Them]** 29:16
have a good one

