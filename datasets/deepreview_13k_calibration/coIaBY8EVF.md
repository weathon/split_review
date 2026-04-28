# Decongestion by Representation: Learning to Improve Economic Welfare in Marketplaces

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Congestion is a common failure mode of markets,  where consumers compete inefficiently on the same subset of goods
(e.g.,  chasing the same small set of properties on a vacation rental platform).
The typical economic story is that prices  decongest by 
balancing supply and demand. % in order to decongest the market.
But in modern online marketplaces, prices are typically set in a decentralized way by sellers, \galiadd{and the information about items is inevitably partial.} %\gn{or, ``inherently?'' This is an attempt to add the aspect of partial information that was missing in the abstract I think. Not sure if this is the best way to add this, but space is limited.}
The power of a platform  is limited to controlling \emph{representations}---the 
\niradd{subset of information about items presented by default to users.}
This motivates the present study of \emph{decongestion by representation},
where a platform seeks to learn representations that reduce  congestion and thus improve social welfare.
The technical challenge is twofold: relying only on revealed preferences from the choices of consumers, rather than true preferences; and the combinatorial problem associated with
 representations that  determine \dcpadd{the  features to reveal in the default view}.
 We tackle both challenges by proposing a 
{\em differentiable proxy of welfare} that can be trained end-to-end on consumer choice data.
We develop sufficient conditions for when decongestion promotes welfare,
and present \dcpadd{the results of extensive} experiments on both synthetic and real data
that demonstrate the utility of our approach.
\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the issue of market congestion, where consumers often compete inefficiently for the same subset of goods or services. To alleviate the issue, the authors propose "decongestion by representation," where a platform learns to display item information in ways that reduce congestion and improve social welfare. The key of the approach is a "differentiable proxy of welfare", which enables an end-to-end training process based on consumer choice data. Extensive experiments on both synthetic and real data show the effectiveness of the approach.

### Strengths
- The study is highly relevant to modern e-commerce platforms, potentially leading to better consumer experiences and more efficient markets.
- The idea of resolving market congestion through selective information representation is novel and addresses real-world concerns in online marketplaces.
- The differentiable proxy for welfare approach is sound and technically rigorous, which provides a strong analytical foundation of the proposed solution.

### Weaknesses
 - The discussion in the ethics statement does not really relieve my concern that the manipulation of representations would open up the Pandora's box for online recommender platforms. The same approach can be applied to optimize user welfare but can also be exploited for promoting the revenue which might hurt the user satisfaction.

 - The core of the optimization technique is to replace the welfare function with a lower bound proxy. I'm curious how tight Eq (5) is? It would be nice to add some discussions in this regard.

- The experiment result in Figure 4 seems to suggest that a larger mask size $k$ leads to a higher welfare gain when $d$ is large. I'm not sure why it is possible: since a larger $k$ induces a loss in the perceived value so there should be a trade-off between perceived value and congestion level. I'm expecting an inverted-U curve and the result seems counterintuitive to me. Could you explain what I'm missing here?

### Questions
- The core of the optimization technique is to replace the welfare function with a lower bound proxy. I'm curious how tight Eq (5) is? It would be nice to add some discussions in this regard.

- The experiment result in Figure 4 seems to suggest that a larger mask size $k$ leads to a higher welfare gain when $d$ is large. I'm not sure why it is possible: since a larger $k$ induces a loss in the perceived value so there should be a trade-off between perceived value and congestion level. I'm expecting an inverted-U curve and the result seems counterintuitive to me. Could you explain what I'm missing here?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper initiates the study of decongestion by representation in the setting that f a platform is limited to controlling representations— the subset of information about items presented by default to users. A differentiable learning framework is developed to learn item representations in order to reduce congestion and improve social welfare. It is shown that partial information is a necessary aspect of modern online markets, and that systems have both the opportunity and responsibility in choosing representations that serve their users well.  Sufficient conditions for when decongestion promotes welfare are developed. Extensive experiments on both synthetic and real data demonstrate the utility of the proposed approach.

### Strengths
This paper formulates an interesting problem of decongestion by representation, which has great practical value.  

The proposed differentiable learning framework looks sound and yield insightful results. 

The theoretical analysis looks sound and it is supplemented by extensive experiments.

### Weaknesses
I am not an expert of this paper.  I do no identify any major weaknesses of this paper.

### Questions
No questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work is devoted to improving welfare of users (buyers) in marketplaces of goods (like Yelp, AirBnb, etc). The authors propose to translate this problem into the problem of adjusting representations of goods (items) in the way it improves welfare through reducing congestion per each item. The representations are binary masks over item features (a single mask per market; so, no discrimination of users or items). The authors propose learn user preferences through a dataset obtained in the past. Extensive experimentation is done to justify applicability of proposed approach.

### Strengths
-	Original and novel work, interesting setup

-	Huge experimentation (most part is deferred to Appendix)

-	Practical applicability of the solution

### Weaknesses
 - 	Argumentation of the setup

- 	Presentation

- 	Details on ML setting


(see Questions field)

### questions:
 1.	Argumentation of the setup:

a.	In Abstract “The power of a platform is limited to controlling representations— the subset of information about items presented by default to users”. This statement is very strong and seems not true. For instance, platforms definitely have other means to control information: besides representations (the amount of info provided per item) there are different ways to control user attention between different items like ranking of items, recommendation of items, etc. So, I strongly suggest rewriting this sentence.

b.	In Intro, the end of 2nd paragraph and 3rd paragraph: I do not understand why the described here issue cannot be resolved by some auction (or other mechanism design). The way these paragraphs are written, it sounds like the authors are not aware of vast practical application of auction in web services:

•	see, e.g., ad auctions, where they are built to reduce congestion by maximizing welfare (e.g., second price auctions, position auctions) through exploiting imbalance between demand and supply; and in this case, prices (bids) are also set in decentralized way – so, this argument, does not imply strong conclusion that representation is the only one way.

c.	In Intro, Page 2, 3rd paragraph: “under perceived values remain both valuable and diverse.” Why? + Example after this does not help and is unclear. Why does the problem cannot be resolved by auctions (so, the platform adjust price despite its decentralized price input) or by ranking (playing user attention)?

d.	I strongly recommend reviewing and rewrite argumentation of viability of the proposed setup: the setup itself sounds, but it should not be positioned as the only way for resolve the marketplace / platform issues… 

---------

2.	Presentation: I believe Intro can have more details (preserving the same space). For instance,

a.	While reading the whole Intro, for me, it was still unclear what is meant by “representation”: whether representation is dependent on item (in Setup I’ve found it is not), whether it is about smth like ranking or so (in Setup I’ve found it is not)

b.	Welfare: is it just about users? Or users + platform? Or welfare of users + sellers? Only, in Setup, I’ve found that it is about users only. BUT in Intro, it is written “reduced social welfare—to the detriment of users, suppliers, and the platform itself” which is misleading… 

c.	Section 4: it would be nice to see some practical examples where these conditions are working. 

---------

3.	ML 

a.	In Intro, Page 2, 2nd paragraph: “Given this, we propose to use machine learning to solve the necessary design problem of choosing beneficial item representations.” Is it true that ML usage is a separate contribution in addition to the proposed setup? (Or ML is a part of the setup?) It would be nice to have clear list of the contributions.

b.	I believe it is better to improve Sec.2 by removing discussion of ML from discussion of the setup (and discuss ML in a separate section or introduce it directly in Sec.3). Right now, it creates a mix of not fully discussed ML injection (2nd and 3rd paragraphs Page 4: there is nothing about learning objective, what to learn \mu? \beta? etc) and Problem setup. I believe optimization problem (Welfare without Expectation) should be introduced before stepping into discussion of ML.  

c.	Eq (6) and (7): Is it OK to train both f on S and use the same S for W_S calculation? Should we split S? Despite theoretical analysis of non-ML setup in Sec.4, I struggle from not having any guarantees on viability of proposed ML approach (are we using standard ML setting with well-known theory and practice?).  It would be nice to have such a discussion somewhere in the text.

---------

4.	Experiments:

a.	How are V_{het} and V_{hom} formally defined?

b.	It would be nice to have formal direct link/ref to Appendix where details of experimentation are given (both for Sec.5.1 and for Sec.5.2). It is important for reproducibility.

c.	In Sec.5.2. “we optimize Eq.(8) using Adam with…”. What is “Adam”? It is better to give better ref / citation, or more convenient naming.

---------

5.	Minor:

a.	Footnote 3: it would be interesting to know which problem we face (or which assumptions are broken) when sellers adapt quickly (e.g., dynamic pricing is very common setup in ad auctions)

b.	Eq.(7): formally, it is incorrect to write M \in S since S consists of pairs (M, y). So, either need to replace by (M,y)\in S or by a sum over l = 1,…,L

c.	In Sec.6: “"..as well as the study of more elaborate user.."”:  “of” --> “to” ?

### Questions
1.	Argumentation of the setup:

a.	In Abstract “The power of a platform is limited to controlling representations— the subset of information about items presented by default to users”. This statement is very strong and seems not true. For instance, platforms definitely have other means to control information: besides representations (the amount of info provided per item) there are different ways to control user attention between different items like ranking of items, recommendation of items, etc. So, I strongly suggest rewriting this sentence.

b.	In Intro, the end of 2nd paragraph and 3rd paragraph: I do not understand why the described here issue cannot be resolved by some auction (or other mechanism design). The way these paragraphs are written, it sounds like the authors are not aware of vast practical application of auction in web services:

•	see, e.g., ad auctions, where they are built to reduce congestion by maximizing welfare (e.g., second price auctions, position auctions) through exploiting imbalance between demand and supply; and in this case, prices (bids) are also set in decentralized way – so, this argument, does not imply strong conclusion that representation is the only one way.

c.	In Intro, Page 2, 3rd paragraph: “under perceived values remain both valuable and diverse.” Why? + Example after this does not help and is unclear. Why does the problem cannot be resolved by auctions (so, the platform adjust price despite its decentralized price input) or by ranking (playing user attention)?

d.	I strongly recommend reviewing and rewrite argumentation of viability of the proposed setup: the setup itself sounds, but it should not be positioned as the only way for resolve the marketplace / platform issues… 

---------

2.	Presentation: I believe Intro can have more details (preserving the same space). For instance,

a.	While reading the whole Intro, for me, it was still unclear what is meant by “representation”: whether representation is dependent on item (in Setup I’ve found it is not), whether it is about smth like ranking or so (in Setup I’ve found it is not)

b.	Welfare: is it just about users? Or users + platform? Or welfare of users + sellers? Only, in Setup, I’ve found that it is about users only. BUT in Intro, it is written “reduced social welfare—to the detriment of users, suppliers, and the platform itself” which is misleading… 

c.	Section 4: it would be nice to see some practical examples where these conditions are working. 

---------

3.	ML 

a.	In Intro, Page 2, 2nd paragraph: “Given this, we propose to use machine learning to solve the necessary design problem of choosing beneficial item representations.” Is it true that ML usage is a separate contribution in addition to the proposed setup? (Or ML is a part of the setup?) It would be nice to have clear list of the contributions.

b.	I believe it is better to improve Sec.2 by removing discussion of ML from discussion of the setup (and discuss ML in a separate section or introduce it directly in Sec.3). Right now, it creates a mix of not fully discussed ML injection (2nd and 3rd paragraphs Page 4: there is nothing about learning objective, what to learn \mu? \beta? etc) and Problem setup. I believe optimization problem (Welfare without Expectation) should be introduced before stepping into discussion of ML.  

c.	Eq (6) and (7): Is it OK to train both f on S and use the same S for W_S calculation? Should we split S? Despite theoretical analysis of non-ML setup in Sec.4, I struggle from not having any guarantees on viability of proposed ML approach (are we using standard ML setting with well-known theory and practice?).  It would be nice to have such a discussion somewhere in the text.

---------

4.	Experiments:

a.	How are V_{het} and V_{hom} formally defined?

b.	It would be nice to have formal direct link/ref to Appendix where details of experimentation are given (both for Sec.5.1 and for Sec.5.2). It is important for reproducibility.

c.	In Sec.5.2. “we optimize Eq.(8) using Adam with…”. What is “Adam”? It is better to give better ref / citation, or more convenient naming.

---------

5.	Minor:

a.	Footnote 3: it would be interesting to know which problem we face (or which assumptions are broken) when sellers adapt quickly (e.g., dynamic pricing is very common setup in ad auctions)

b.	Eq.(7): formally, it is incorrect to write M \in S since S consists of pairs (M, y). So, either need to replace by (M,y)\in S or by a sum over l = 1,…,L

c.	In Sec.6: “"..as well as the study of more elaborate user.."”:  “of” --> “to” ?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Online platforms typically sell goods in a decentralized fashion which complicates the equilibration of supply and demand as sellers set prices and buyers must make decisions under imperfect information. Platforms can typically only control the set of information provided to buyers. In that sense platforms want to find the representations (or sets of information to present) that improves social welfare. The paper in particular tackles the challenge of congestion where supply does not meet demand. The authors develop a learning technique that to find representations that reduce congestion which they argue using equilibrium analysis improves social welfare under a partial information framework.

### Strengths
The paper studies an important question in online platforms of what information should be presented in order to maximize social welfare. The paper poses this question through a nice framework of learning representations which allows us to employ machine learning tools to optimize this objective.  The modeling framework gives an interesting perspective to design of online platforms and has the potential for practical contributions. Furthermore, the paper uses both simulated and real world data to underscore it's point which is helpful in seeing the contributions of the paper.

### Weaknesses
 - Solving the objective requires smoothing a discrete object. As the authors note this can add some practical difficulties. One approach they take is to penalize the "no-choice" option. Is this reasonable in practice? Often the "outside" option can have a large market share in studies of demand. It's unclear how this penalty affects the learned representations and whether it introduces a bias towards selecting items even when the outside option is preferred by users. The magnitude of this penalty and its sensitivity to different market conditions should be further explored.

- The theoretical analysis feels a little misplaced. Specifically, the theoretical analysis seems to focus on the perfect information equilibrium, is this really relevant in the online marketplace scenario as the authors note earlier in the paper? Furthermore, this focuses on proxying social welfare with reducing congestion but this may not be the objective platforms want to optimize for. In fact, decongestion seems practical enough objective on its own. This also involves making assumptions like "item heterogeneity is captured in revealed features" which is likely violated in practice. The assumption that all relevant item heterogeneity is captured in the revealed features is a strong one, and it's not clear how the method would perform if there are unobserved or latent factors influencing user choices. The theoretical analysis should also consider the implications of this assumption and how it might affect the results.

- It seems like the results in the real data section may rely somewhat on how choices are simulated through prices. Can you comment on how this could affect results if there is some additional dependencies in choices. The simulation of choices based on prices might not fully capture the complexities of real-world user behavior. If there are dependencies between choices that are not captured by the price-based simulation, the results might not generalize well to real-world scenarios. For example, network effects or user preferences for specific brands could introduce dependencies that are not accounted for in the simulation.

### Questions
How easily can this optimization framework be generalized to optimize other objectives of interest? i.e. maximizing platform profits

Can you characterize further some of the loss due to smoothing the discrete problem?

Is the oracle benchmark based on the optimal representation?

Additional questions posed in weaknesses.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
