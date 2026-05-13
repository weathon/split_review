# Bayesian Persuasion Is a Bargaining Game

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
Bayesian persuasion studies how a sender with an informational advantage can persuade a receiver with a different motive to take actions that benefit the sender. This problem is previously formulated from an equilibrium perspective, where the sender is to choose a Bayes correlated equilibrium and the receiver is willing to respect the signaling scheme based on posterior beliefs. However, evidence in real-world scenarios and studies in farsighted receivers suggest otherwise: senders tend to be much more honest than the equilibrium. In this work, we show that Bayesian persuasion is reducible to a bargaining game. This reduction suggests that the receiver in Bayesian persuasion can be aware of the game structure and can develop an anti-exploitation strategy. This equalizes the power of commitment of the two parties and prevents the sender from taking the maximum possible payoff. Through experiments on large language models, we demonstrate the receiver's retaliatory strategies and the sender's compromise to that. More findings on the impact of the context and alignments further suggest that bargaining behavior emerges in persuasion tasks. The insights given by our results have potential implications on various scenarios to reduce exploitation, improve equality, and improve social welfare.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper provides a new perspective on Bayesian persuasion by showing it can be reduced to a bargaining game. 
The authors tries to show that receivers can develop anti-exploitation strategies when they're aware of the game structure. By simulations with large language models, the authors show that these bargaining dynamics emerge naturally in persuasion tasks.

### Strengths
1. The theory looks solid and the perspective to compare a BP game to a bargain game is very interesting.

### Weaknesses
1. The authors claimed the reason for LLM agents as the person to test the mechanism is “It is immediate  for LLMs to provide their interpretation as to why such decisions are made by giving appropriate prompts.” Caution must be taken since LLM tend to rectify the decision it just made. This is dubious as a recent paper shows https://arxiv.org/abs/2410.19599.
2. Even the LLM simulation setting is not clearly described. Context like when will the game end or how many times do these LLM agent play, are these repeated or started from afresh, or the temperature of the models are not described at all. 
3. How does the results of LLM game compared to the one with real human? In Table 1 and 2 summarize the results of LLM agents playing the task games. And these tables are not mentioned in the draft any more, which adding more confusing to the audience. What does the experiment result try to establish? The display is very confusing.
4. If the author want to demonstrate how the receiver in a BP task can use an action rule with game structure awareness to achieve higher expected gain, the statistical analysis are required. In the discussion follows, the author seems to describe the similarity in strategic behavior.

### Questions
1. I suggest the authors look into the paper https://arxiv.org/abs/2410.19599 and argue why the LLM simulation can provide any insights into the their scenario.
2. More clarification of the simulation context is required
3. More explanation of Table 1 and Table 2 and the statistical analysis is encouraged.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates connections between Bayesian persuasion and bargaining games. The key message as far as I'm concerned, is that the receiver may be able to gain more than in a standard solution to Bayesian persuasion by applying strategies that are more sophisticated than just best responding the the principal's commitment. The paper therefore proposes to apply the concept of bargaining game to Bayesian persuasion. It is shown that Bayesian persuasion with this new solution concept is reducible to bargaining games. Additionally, the authors conducted experiments with LLMs to test the theoretical claim.

### Strengths
The idea of studying the connection between persuasion and bargaining is very interesting. The paper has made a good effort to elaborate the background of the problem. The idea of using LLMs in the experiments is novel and inspiring. Overall I appreciate the endeavor of pushing research of Bayesian persuasion to more realistic setups beyond the standard theoretical model.

### Weaknesses
The main weakness of the paper as I see is a lack of clarity in its key message. I hope the authors could help to clarify the concerns in the rebuttal phase.

- The claim that Bayesian persuasion reduces to bargaining game is a bit confusing. It appears that what the authors actually mean is that a bargaining version of Bayesian persuasion, instead of Bayesian persuasion in its original form (where the sender commits), is reducible to bargaining games. If this is the case, the claim seems somewhat misleading, and in a sense it appears to me this claim will just apply to any kind of games, and it's not a property unique to Bayesian persuasion. It would be good if the authors could clarify these points.

- Following the above, it may be helpful to include some toy examples to illustrate the concepts of bargaining games, Bayesian persuasion in the bargaining setting, and standard Bayesian persuasion, as well as the differences between them.

- It may be helpful to include a bit more details about the experiment setup in the main paper, including who are the senders and receivers in the experiments, and how do they interact in the experiments. Tables 1 and 2 may be easier to parse if they are presented as plots.

### Questions
- As mentioned above, when you say Bayesian persuasion is reducible to bargaining game (e.g., in Lemma 3.5), do you mean by solving the bargaining game you also solve Bayesian persuasion in its original form (where the sender commits), or in a bargaining version of Bayesian persuaison? I suppose you mean the latter, as defined in Definition 3.4?

- Are there any properties unique to Bayesian persuasion that makes it reducible to bargaining games where other types of games (e.g., Stackelberg games) do not? Or is it the case that this claim applies to other types of games as well?

- Line 61, Page 2: The effect of history-dependent strategy is also discovered by Gan et al. (2023): Sequential principal-agent problem with communication: efficient learning and computation.

- The idea of the receiver's counter commitment agains the sender seems to be relevant to the folk theorems in game theory, as well as deception in Stacelberg games, where the follower, instead of responding optimally, commits to a different responding function to influence the equilibrium of the game: Birmpas et al (2020), Optimally deceiving a learning leader in Stackelberg games. 

- The outcome of the bargaining game depends on the choice of the function $\omega_{BP}$. How does this influence the experiment results? Are the experiments (as well as the main goal of the paper) more about demonstrating that the receiver is able to gain more by using retaliatory strategies, so it's more from the receiver's perspective?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper considers the problem of Bayesian persuasion (also known as "information design") in which an informed sender must transmit a signal to an uniformed receiver in order for the receiver to take an action that the sender favours. The main idea of the paper is that in some settings it can be reasonable to view not only the sender but also the receiver of having the ability to commit to their strategy in advance. In such cases, Bayesian persuasion can be viewed as a bargaining game. The authors discuss this idea and conduct some experiments with LLM agents to investigate the relevance of repeated interactions to both Bayesian persuasion and bargaining games.

### Strengths
As far as I am aware (though I am unfortunately not an expert on this literature), this paper is the first to discuss the possibility of receivers being able to make commitments in Bayesian persuasion settings and the implications of this. I think this is natural idea and one that -- as the authors argue -- does map on to several real-world scenarios. A better theoretical and empirical understanding of this setting could prove useful in reasoning about such scenarios. The definitions and explanations of both Bayesian persuasion and bargaining problems are reasonably clear (though see below for weaknesses), as is the explanation of the empirical results. The use of LLMs in their experiments is valid and -- as LLMs and related models mediate more and more of humans' interactions -- an increasingly interesting topic of study, in my opinion.

### Weaknesses
The primary issue I have with the paper is that in my view it purports to be doing something it is not. In several places (see, e.g., the first sentence of the conclusion) the authors claim that "Bayesian persuasion is reducible to a bargaining game", and indeed Lemma 3.5 is a formal version of this statement. I was quite confused for most of the paper however, because what the authors _actually_ show is that **a variant of Bayesian persuasion where the receiver is also given the ability to commit and the agents are able to interact beforehand** is reducible to a bargaining game. Put this way, the surprisingness and significance of the main claim (and in fact the _title_) of the paper is greatly diminished, in my opinion. This explains as well, for example, why the "polynomial time reduction" in Lemma 3.5 is so overblown. Specifically, the authors reduce Bayesian persuasion to a bargaining game via the formation of a constrained convex optimisation problem where nothing is being optimised! Instead, the reduction results from setting the solution of the first problem to the solution of the second in the constraint of the problem. At best this is naive, at worst it is deliberately misleading (in aiming to complicate and obfuscate the result so that it appears more significant than it actually is).

The other issues I have with the paper are less major, but are consistent with the problems above.

**Game-Theoretic Reasoning:** There are a few places where the game-theoretic reasoning in the paper seems confused:

- The authors claim that the ability of the _sender_ to commit implies that Bayesian persuasion involves long-term interactions, but this is not necessarily true -- there are plenty of one-time interactions where commitment is possible (e.g., contracts, escrow services, etc.). This is more of an issue as it this idea that the authors seem to motivate most of their experiments with. I suggest the authors weaken their claim accordingly.
- The authors claim in several places that it is game-theoretically rational for the receiver to refuse to best respond to certain commitments and signals provided by the sender, but this results only as a function of their assumption that the sender has a way of credibly committing themselves. Otherwise, the receiver is clearly making a non-credible threat and playing irrationally.

**Experimental Motivation:** There are a few things, in my mind, which make the experiments section weaker than it needs to be:

- The authors should clearly state up front what hypotheses they are aiming to test with their experiments and why. This is also related to the use of LLMs. The justification the authors provide for this choice seems to suggest that they are primarily interested in studying human behaviour and that they use LLMs as a proxy for this, but if so they should make this idea clearer. I happen to think that it is interesting in its own right to see how LLMs tackle such problems, especially if those problems can be linked to current or future real-world uses of LLMs, but the authors do not attempt to provide such links.
- Because of their mistaken supposition that the sender's ability to commit _requires_ long-term interactions, they do not consider the one-shot version (setting $\alpha$, in the paper's notation) Bayesian persuasion in their experiments, which is the obvious baseline that I was expecting to see.
- Why is the proposer chosen uniformly at random in the bargaining problems but not the sender in the Bayesian persuasion settings? More generally, at the moment these settings are examined side by side, but what should be the takeaways from the similarities and differences from the results in the two settings? What specific hypothesis has been confirmed or refuted (or neither) based on the similarities and differences between the results in the two settings?

**Notation:** This is overly complex and what appear to be typos early on in the paper make the Bayesian persuasion setting harder to understand than is necessary. Concretely:

- If the receiver has no private information, there is no need to talk about this (i.e., $q$ can be dropped completely). This also means that there is no need to distinguish between $\phi$ and $\varphi$, which would also save confusion.
- In footnote 1, it seems as though $q$ and $\phi$ are the wrong way round (the sender determines $\phi$, not $q$).
- The set of signalling schemes is denoted as blackboard bold $\psi$ but the signalling schemes themselves are elsewhere denoted as either $\phi$ or $\varphi$. Later $\psi$ is what determines the payoffs of the agents as a function of their commitments.
- Why do some symbols have tildes and others not? This is never explained.
- In Definition 3.3 $\tilde{\varphi}^*$ and $\tilde{\pi}^*$ have not been introduced.

**Language/Typos:** This is a lot more minor and I understand that the authors may not have English as a first language, but there are few claims that I could not understand because of the unusual choice of words:

- Page 1: What are "cognitive misers"?
- Page 3: What does it mean for "solutions to become conceivable"?
- Page 6: The sentence after Assumption 3.2 was unclear to me (in part because the example with the coins had not yet been introduced).
- Page 8: I think I understand what the authors mean here, but I would change the phrasing about different game structures "experienc[ing] less social context" to something like different settings being "less influenced by social norms and contexts not captured by the structure and payoffs included in the game description".

There are many other typos throughout and minor grammatical errors throughout which do not majorly impact the scientific quality and clarity of the paper, and so do not impact my review score, though I would nonetheless encourage the authors to spend a little more time to polish the manuscript in this regard.

### Questions
Please see the Weaknesses section for my questions. I also welcome the authors to correct any misunderstandings I may have about the paper and its claims.

### Soundness
1

### Presentation
2

### Contribution
2
