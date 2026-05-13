# The (co)limit of metabeliefs

- Decision: Reject
- Scores: 8, 3, 5, 5, 5

## Abstract
Potentially infinite sequences of beliefs arise when reasoning about the future, one's own beliefs, or others' beliefs.  Machine learning researchers are typically content with heuristic truncation, or proofs of asymptotic convergence, of sequences of beliefs; however, such approaches lack insight into the structure of the possible choices. We construct and analyze several (co)limits of meta beliefs to understand the topological and geometric structure of sequences of beliefs.  We analyze the relationship between different levels, the relationship between different beliefs at different levels, the encoding of temporal and other indexing structures in belief space, and structures preserved in the colimit. Examples demonstrate the ability to formalize and reason about problems of learning, cooperative and competitive reasoning, and sequential decision making. We conclude by emphasizing insights gained, and future directions for more concrete machine learning models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper deals with the limit of beliefs of beliefs.
In a very general setting, without making many structural assumptions, the authors perform a theoretical study of the properties of the limiting space. Their first main theoretical contributions is a result guaranteeing that the limiting space is Hausdorff when the initial space is. They continue their investigation by focussing on distributions with finite p-moments (almost everywhere), which is where their second main theoretical distribution is: they identify and characterise the topology on the limiting space in this setting. Besides this, the paper shows connections between these two settings, ans well as relations with a setting of index-dependent distributions.
The authors end their paper with some examples of specific structures, with an summary of how to compute the distance in a simple 3-state game, and with an overview of related work.

### Strengths
To the best of my knowledge, the content and problem setting are original.

This paper is well written, and contains clear definitions and results.
I appreciate the structure of the paper.
Overall, the paper clearly shows that the authors thought well about their presentation.
I particularly appreciate the clear set up for each of the three settings; in particular the first and second one.

The main strength of this paper are the large number of theoretical results.
The authors manage to both clearly define all the objects, as well as derive many results in the main text, in a limited space, for which I want to commend them.
I have tried and checked the proofs.
To the best of my knowledge, they are correct—bar two questions I have later on with hopefully minor consequences.

I also like the philosophical justification for the problem under investigation. I admit that I am sceptical about many of the justifications for higher order beliefs, but the limiting approach that the authors take seem well founded, and alleviates some of my initial reservations. I like that the authors do not assume that there is a boundary of the level of uncertainty of uncertainty

In section 4, the example that shows the most promise in my opinion, is the one about hierarchical models. I like that the authors identify the relevant concepts in their setting.

### Weaknesses
I don't think the paper has major weaknesses.
Its focus certainly is on the theoretical front, so one might argue that the paper lacks applications, simulations, or computational details; however, given the large number of results I would tend to find this of minor importance here.

As I indicated above, the writing style is very clear. However, I found myself sometimes lost in Section 2, which contains abstract material. I believe that, given the page limitations, it is difficult to improve this, but perhaps some clarifications are possible.

I believe that there on two technical parts, there are details missing. I'll list the details in the section Questions underneath, but they concern Lemma 2 and Lemma 6. I am hopeful, however, that even if I am right, this won't have major consequences for the rest of the story and results.

I start with my two main questions:

1/ page 3, Lemma 2: I think that the authors need to be careful with the range of n. More specifically, what happens if n=0? Does the metric space {\cal X} contain distributions?
- If not, can we always assume that n≥1? Why?
- If so, that is a structural assumption on {\cal X} that seems strange, and needs to be spelled out.
It could be that I misunderstand something here. What could improve my understanding, is having the answer to the following question: What is the form of the equivalence class that contains an element of {\cal X}?

2/ page 5, Lemma 6: The authors don't prove that the alleged metric is positive definite (that W(mu,nu)>0 if mu≠nu). I believe that this is a requirement of the usual definition of a metric. Do the authors need this? If so, does their map W satisfy this?

I conclude my review with a list of some small remarks and typos:

page 1, first paragraph following the abstract: "... to sequences of beliefs quantify uncertainty ..." should read something like "... to sequences of beliefs that quantify uncertainty ..." (so sets with a "that", or an alternative).

page 1, second paragraph: There is a dot missing after the third sentence.

page 1, fourth paragraph: "... one must play of the three options." should read "... one must play one of the three options.".

page 1, fifth paragraph: "geoemtric" should read "geometric". In the following sentence, the word "gives" is superfluous.

page 2, paragraph following Theorem 1: "Parts (2)--(6)" should be "Parts (2)--(5)", I believe, since there are only 5 parts in Theorem 1.

page 3, Lemma 3: In the proof, the authors use a result that guarantees that each {\cal P}^m({\cal X}) is T1 if {\cal X} is T1. While I can believe this is true, I would like to have a proof. Is this a standard 
result? If so, it might be worth giving a reference.

page 3, Lemma 5: Its proof appears in the supplementary material as well as in the paper; perhaps the copy in the paper can be omitted?

page 4, proof of Theorem 4: Theorem 1 part (4) talks about *compact* spaces, and not about the weaker notion of *paracompact* spaces. Why can this be inferred? If that's not immediate, perhaps it suffices for the 
further applications that the spaces are compact, in addition to being paracompact?

page 5, Lemma 6: There is a dot missing at the end of the lemma.

page 5, right hand side of Equation (10): the part of the expression after | is not a condition, which reads a bit strangely. I suggest that the authors add that \tilde\nu \in the sets shown, if that's correct.

page 5, Equation (11): Why is does \Delta^i commute with \bigcap and \bigcup? This must be some standard result, but I don't seem to find a reference for this.

page 6, Lemma 11: The authors should define the map ev already here, as they use it in their commuting diagram. Now they only define the map ev later on in Section 2.

page 8, subsection "Competitive/Cooperative games": There is a dot lacking between the first two sentences. Also, "In this sense, both agents beliefs ..." should read "In this sense, both agents' beliefs ...".

### Questions
I start with my two main questions:

1/ page 3, Lemma 2: I think that the authors need to be careful with the range of n. More specifically, what happens if n=0? Does the metric space {\cal X} contain distributions?
- If not, can we always assume that n≥1? Why?
- If so, that is a structural assumption on {\cal X} that seems strange, and needs to be spelled out.
It could be that I misunderstand something here. What could improve my understanding, is having the answer to the following question: What is the form of the equivalence class that contains an element of {\cal X}?

2/ page 5, Lemma 6: The authors don't prove that the alleged metric is positive definite (that W(mu,nu)>0 if mu≠nu). I believe that this is a requirement of the usual definition of a metric. Do the authors need this? If so, does their map W satisfy this?

I conclude my review with a list of some small remarks and typos:

page 1, first paragraph following the abstract: "... to sequences of beliefs quantify uncertainty ..." should read something like "... to sequences of beliefs that quantify uncertainty ..." (so sets with a "that", or an alternative).

page 1, second paragraph: There is a dot missing after the third sentence.

page 1, fourth paragraph: "... one must play of the three options." should read "... one must play one of the three options.".

page 1, fifth paragraph: "geoemtric" should read "geometric". In the following sentence, the word "gives" is superfluous.

page 2, paragraph following Theorem 1: "Parts (2)--(6)" should be "Parts (2)--(5)", I believe, since there are only 5 parts in Theorem 1.

page 3, Lemma 3: In the proof, the authors use a result that guarantees that each {\cal P}^m({\cal X}) is T1 if {\cal X} is T1. While I can believe this is true, I would like to have a proof. Is this a standard 
result? If so, it might be worth giving a reference.

page 3, Lemma 5: Its proof appears in the supplementary material as well as in the paper; perhaps the copy in the paper can be omitted?

page 4, proof of Theorem 4: Theorem 1 part (4) talks about *compact* spaces, and not about the weaker notion of *paracompact* spaces. Why can this be inferred? If that's not immediate, perhaps it suffices for the 
further applications that the spaces are compact, in addition to being paracompact?

page 5, Lemma 6: There is a dot missing at the end of the lemma.

page 5, right hand side of Equation (10): the part of the expression after | is not a condition, which reads a bit strangely. I suggest that the authors add that \tilde\nu \in the sets shown, if that's correct.

page 5, Equation (11): Why is does \Delta^i commute with \bigcap and \bigcup? This must be some standard result, but I don't seem to find a reference for this.

page 6, Lemma 11: The authors should define the map ev already here, as they use it in their commuting diagram. Now they only define the map ev later on in Section 2.

page 8, subsection "Competitive/Cooperative games": There is a dot lacking between the first two sentences. Also, "In this sense, both agents beliefs ..." should read "In this sense, both agents' beliefs ...".

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
ICLR is not an appropriate venue for venue for this paper.


-------
Addendum:

Your last comment was "Great. It seems we agree that beliefs of finite depth are important." No, I'm claiming the opposite. Belief about belief about beliefs to finite depths are not useful and are misleading. The infinite limit (equilibrium) is useful, but as in the link I provided above, stopping at any finite depth often gives beliefs that are a function of the depth, not of anything else.  Beliefs about actions are imperative for intelligent action and AI, but that is not the same.

(I am not objecting to you claiming they are useful, I am objecting to you asserting they are useful without any evidence.  I'm also not clear why a category theory formalization is useful. Also, it isn't really relevant to ICLR.)

In another answer you said there wasn't a recent literature. Monte Carlo tree search (as, e.g., used in AlphaZero) can be seen as stochastic simulation through the space of belief about beliefs (where the beliefs are about the *actions* of the other agent); one reason it works is that it does not stop at an arbitrary point, but goes to the end of the episode/game. Also, (depending on what you mean by recent) Joe Halpern of Cornell has written many papers on this topic. A quick look found https://www.cs.cornell.edu/home/halpern/abstract.html#journal67

### Strengths
None that I can see.

### Weaknesses
The solution to the question at the end of the 4th paragraph after the abstract is "yes".  This problem was solved in 1950. The limit P^\inf(X) is the fixed point which is the definition of a Nash equilibrium. Nash proved the existence of a fixed point, and there is a considerable literature on how to compute them and its complexity (PPAD). The Nash equilibrium has a maximization step (agent agent has a utility it is trying to maximize), which seems essential to the running example, but doesn't  appear in the paper. (One of) the brilliance(s) of Nash's result is that an agent does not need to do the recursive reasoning that this paper is about. We can compute the fixed point directly.

The rest of the running example is all nonsense. "In order for Bob to generate his own strategy, he must consider what he knows..." is not true. Bob doesn't need to do this recursive reasoning.

The core issue is that the paper proposes an infinite regress of meta-beliefs as a fundamental component of rational decision-making, which is not only computationally intractable but also unnecessary. The paper's claim that considering all levels of meta-beliefs simultaneously is essential is not supported by existing literature, which has largely moved away from such approaches due to their impracticality and the availability of more efficient solutions. The paper's approach, focusing on the space of all finite sequences of beliefs, is fundamentally flawed because it is the fixed point of these beliefs, not the space itself, that provides the rational solution. The paper's running example is misleading because it suggests that agents need to explicitly perform this infinite reasoning, which is not the case in standard game-theoretic models.

### Questions
Am I wrong?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper studies chains of beliefs with tools from category theory. This is far outside my area of expertise.

### Strengths
N/A

### Weaknesses
The categorical and geometrical results, while natural, do not have foreseeable applications to machine learning (that I am aware of or can imagine). This is not unexpected for an exploratory paper to propose a new modeling perspective (colimit of topological spaces), but stronger connections to machine learning definitely help. The paper's exploration of topological properties like metrizability and paracompactness, while mathematically sound, lacks a clear justification in the context of practical machine learning problems. Specifically, it's unclear how these properties directly translate to improved performance or understanding of learning algorithms. The use of the Wasserstein $p$-distance, while providing a geometric structure, does not demonstrate a clear advantage over other distance metrics commonly used in machine learning, such as KL divergence or total variation distance, especially given the computational challenges associated with Wasserstein distance in high-dimensional spaces. The running example of the rock-paper-scissors game, while illustrative, does not convincingly demonstrate the utility of the proposed framework for more complex, real-world machine learning scenarios. The paper does not address the computational tractability of calculating the colimit in practical settings, which is a crucial aspect for any method aiming to be applied in machine learning.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the topological and geometrical structure of a sequence of beliefs, formalized as their colimit (under final topology) of the spaces of all levels of metabeliefs, which arises when modeling the reasoning about the future among agents in reinforcement learning, Bayesian hierarchical/deep learning, and game theory and economics.

This paper shows that commonly studies topological properties (such as metrizability, paracompactness, and Hausdorffness) carry over to the colimit of the directed systems pushed by both the weak topology (Theorem 4) or the induced topology of the Wasserstein $p$-distance (whose colimits have the same final topology, Theorem 7), and such constructions carry over to the index-dependent case (Section 2, which may formalize Bayesian hierarchical models with hyperpriors or iterated game such as the iterated rock-paper-scissors or iterated prisoner dilemma).

As a running example, the paper considers the colimit of the rock-paper-scissors game, and studies its geometrical properties (under Wasserstein $p$-distance, Section 4) in addition to its topological properties.

### Strengths
The categorical and topological exposition is very well written, for those familiar with such reasoning. The constructions (e.g., final topology on the colimit) are natural (in the categorical sense), and the results are somewhat intuitive and as expected.

### Weaknesses
 **Accessibility:** The dense mathematical language can make it challenging for a broader audience to understand and appreciate the paper's contributions.

**Practical Application:** The paper leans heavily on theory, and more concrete examples or real-world applications might have bolstered its impact.

**Contextualization:** The paper could benefit from a clearer positioning within the broader landscape of machine learning research, specifically in terms of how it complements or diverges from existing works.

### Questions
While the authors argue that colimit of probability spaces (metrized under the Wasserstein $p$-distance) can model the geometry (and topology) of metabeliefs in co-operative and competitive games, are there examples showing that this modeling is better than other modeling for metabeliefs in terms _applications to machine learning?_

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper delves deep into the mathematical analysis of metabeliefs in machine learning. It adopts concepts from category theory, specifically colimits, to describe the structure and relationships of infinite sequences of metabeliefs. The primary objective is to offer a systematic and unified view of metabeliefs. The paper achieves this through a series of lemmas, definitions, and examples, particularly using the rock-paper-scissors game as a recurring motif.

### Strengths
**Originality:** The paper's approach to metabeliefs through category theory is innovative. The use of colimits provides a fresh perspective on the subject.

**Quality:** The mathematical derivations and lemmas presented are rigorous.

**Clarity:** While dense, the paper is consistent in its language and presentation.

**Significance:** The paper highlights the importance of understanding metabeliefs in machine learning, offering a theoretical foundation for further research.

### Weaknesses
**Accessibility:** The dense mathematical language can make it challenging for a broader audience to understand and appreciate the paper's contributions.

**Practical Application:** The paper leans heavily on theory, and more concrete examples or real-world applications might have bolstered its impact.

**Contextualization:** The paper could benefit from a clearer positioning within the broader landscape of machine learning research, specifically in terms of how it complements or diverges from existing works.

### Questions
1. Could the authors provide more concrete examples or real-world applications of their theory?

2. How does this work compare and contrast with other mathematical approaches to metabeliefs or similar constructs in machine learning?

3. Are there plans to test the presented theories empirically, or to develop algorithms/tools based on this framework?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
