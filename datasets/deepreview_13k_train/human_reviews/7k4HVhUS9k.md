# A Hypothesis on Black Swan in Unchanging Environments

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
\textit{Black swan} events are statistically rare occurrences that carry extremely high risks. A standard view of black swans assumes that they originate from an unpredictable and changing environment; however, the community lacks a comprehensive definition of black swan events. To this end, this paper challenges that the standard view is \emph{incomplete} and claims that high-risk, statistically rare events can also occur in unchanging environments due to human misperception of events' values and likelihoods, which we refer to as \ours. We first carefully categorize black swan events, focusing on \ours, and mathematically formalize the definition of black swan events. We hope these definitions can pave the way for the development of algorithms to prevent such events by rationally correcting limitations in perception.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper challenges the conventional understanding of black swan events, which are typically seen as arising from unpredictable and dynamic environments. The authors propose that such high-risk, statistically rare events can also occur in static environments due to human misperception of events’ values and likelihoods, introducing the concept of S-BLACK SWAN. The paper categorizes black swan events, formalizes their definitions mathematically, and provides a framework for understanding and preventing these events through improved perception.

### Strengths
- The paper presents a novel hypothesis that black swan events can occur in static environments due to human misperception, which is a significant departure from the traditional view. This new perspective could open up fresh avenues for research in risk management and machine learning.
- The theoretical framework is well-developed, with rigorous mathematical formalizations and proofs. The use of Markov Decision Processes (MDPs) to model human perception and misperception is particularly robust.
- The paper is well-structured, with clear definitions and logical progression of ideas.
- By redefining the origins of black swan events, the paper has the potential to significantly impact the fields of machine learning, risk management, and decision theory. It provides a foundation for developing algorithms that can better handle rare, high-risk events.

### Weaknesses
 - The paper lacks empirical validation of the proposed hypothesis. While the theoretical framework is strong, it would benefit from experimental results or real-world case studies demonstrating the occurrence of S-BLACK SWAN events. Specifically, the paper does not provide any quantitative analysis of how human misperception, as modeled by the Markov Decision Processes (MDPs), leads to the emergence of these rare events. The theoretical framework needs to be substantiated with data showing the correlation between misperception parameters in the MDP and the frequency of S-BLACK SWAN events.
- The mathematical formalizations, while rigorous, are quite complex and may be difficult for practitioners to apply directly. The paper presents a complex mathematical framework using MDPs, but it does not provide clear guidelines or simplified models for practitioners to use in real-world risk assessment. The complexity of the mathematical model may hinder its practical adoption and limit its impact on risk management.
- The paper primarily focuses on financial and autonomous systems. Expanding the discussion to other domains where black swan events are critical, such as healthcare or environmental science, could broaden the impact of the work. The current examples are limited, and the paper does not explore the unique challenges and nuances of applying the proposed framework in diverse fields. For instance, the paper could discuss how the concept of misperception might manifest differently in healthcare settings compared to financial markets.

### Questions
- Can the authors provide empirical evidence or case studies that demonstrate the occurrence of S-BLACK SWAN events in real-world scenarios and model it using the proposed algorithm?
- How can the proposed algorithm be applied to other domains beyond finance and autonomous systems? Are there specific examples or case studies in areas like healthcare or environmental science?
- What are the next steps for developing algorithms based on the proposed hypothesis? Are there any preliminary results or ongoing projects that the authors can share?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces the concept of "s-Black Swan" - statistically rare, high-risk events that can occur in unchanging environments due to human misperception of event probabilities and values. Authors present a formal framework from to define this in the context of MDPs and argue that for safety in RL systems, it's important to consider stationary MDPs that present these Black Swan events.

### Strengths
- This paper presents a new view point on how to look at Black Swan events. Specifically, it points to the case of stationary MDPs where agents have distorted perspective on reward signals and visitation probabilities which are likely to be overlooked by researchers. 

- The mathematical rigor is strong - the authors have done a great job at defining s-Black Swan using the existing concepts of MDP and its special cases. It gives a good framework for future researchers to build upon while trying to model such s-Black Swan events. Specifically, theorem 5 seems to be the most useful aspect of this paper which provides an analytical bound of encountering the rare event with event probability. 

Particularly, I liked the formulation of HEMDPs - seems to be a particularly useful modeling strategy.

### Weaknesses
 - While the paper is very rigorous, the details might be very hard to follow for non-specialists. Some of the aspects are not very intuitive. 

- This paper lacks a practical application demonstration - it'll be great if the authors can describe how a practitioner can use the definitions that the paper provides for a practical applications. 

- Building upon the previous point - it'll be useful for us to understand how frequent are such MDPs where the users have a distorted view of the reward signals and the visitation probabilities.

### Questions
- Can you explain why the focus is on visitation probabilities v/s transition function? This is something that's not very intuitive. 

- Why is the value distortion function and the probability distortion function modeled in such a piece-wise way? Is this just for simplicity? How do we decide how to model them? 

- Example 2, case 3 - what does it mean for an MDP to be always a black swan? 

- What is the significance of Lemma 1? Can you describe how should one intuitively understand it? 

- Can you describe some applications where this will be useful? And how should one think about modeling such scenario - my understanding is that HEMDPs would be most appropriate for such situations.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper is a theory paper that challenges the view that black swan events only originate from changing (non-stationary) environments. Instead, the paper focuses on defining S-Black Swan events, which occur in unchanging environments due to human misperception of events’ values and probabilities. The paper is focused on formalizing the definition of S-Black-Swan events, by starting from Hypothesis 1 in the introduction.

### Strengths
* The main arguments of the paper are well-structured and well-communicated. The flow of the paper is helpful to the reader in communicating both the preliminary materials as well as leading to the mathematical formulation of the S-Black-Swan definition. For a theory paper, which could have the tendency to overcomplicate results, it feels like the authors have made significant effort to make the paper readable and therefore potentially meaningful to those who might use it as a future reference.
* The definitions of the stationary ground MDP, the Human MDP, and the Human Estimation MDP form a clear picture of the potential Agent-Environment Framework that could lead to a S-Black-Swan event.
* The presentation showing that black-swan events can arise in stationary environments is interesting.

### Weaknesses
 * One weakness of the paper is in its ability to build a strong link between the results of the paper and how it might affect the wider machine learning community. This weakness can be broken down into a combination of the following:
	*  The related works section is left to the end and reads a bit like a list of works at the intersection of expected utility theory and reinforcement learning. The reader gets to the end of the section and is then told that this literature does not cover black swan events, but this statement lacks enough motivation.
	* The contribution of the paper is highlighted as defining an S-Black Swan event, but this contribution does not appear to be motivated by issues the current RL algorithms struggle within the literature. Every so often the paper includes comments like “aimed at guiding the design of safer ML algorithms in the future”; “laying the groundwork for future algorithmic design”; and “traditional risk criteria in RL are insufficient for managing the unique risks associated with black swan events”. While these comments might be the motivation of the paper, a more concrete motivation could be showing (or referencing) a specific RL (or ML) scenario which could benefit from this new definition and formalization of a S-Black-Swan event. This update seems like it would be important for an ICLR conference venue.

Typos:
* Line 108 $\mathbf{p}_c = …$ should be 3 prob choices.

Comment:
* Figures 1c and 1d could benefit from being moved further down in the paper.

### Questions
1. Are there any examples where a machine learning study/problem/algorithm would have benefited from the definition of a S-Black-Swan event?
2. The probability distortion function seems like it would be an easier function to measure in practice compared to the value distortion function. Each individual might legitimately have different reasons to value outcomes differently. Going with Example 1, a loss of -1000 might be significantly worse for a poorer person than a richer person. It looks like the theory still holds when $\epsilon_r = 0$, but $\epsilon_d > 0$, but could the authors comment on that?
3. If possible, could the authors provide additional context to the novelty of the work and how previous works have not considered an S-Black-Swan event, and attributed rare events to changing environments.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes that rare and high-risk events, namely black swans, can originate from misperceptions of an event’s reward and likelihood even in static environments. The paper formalizes this concept in the context of MDP-based decision tasks using the machineary of cumulative prospect theory, where the misperceptions of rewards and transition functions in MDPs are characterized by distortion functions, resulting in a gap between the ground truth MDP and the MDP perceived by humans. The paper then theoretically analyzes the impact of black swans on the value function and the hitting time of black swan events.

### Strengths
The main proposal of the paper, namely the black swan events can emerge in stationary environments, is interesting and makes sense to me. I also found the formalization using distortion functions on transition probabilities and rewards natural and captures the intuition of human irrationality.

### Weaknesses
In my opinion, the most important weakness of the paper is that apart from the main claim (black swans in unchanging environments), it is not clear to me what the main takeaways of the paper are. The authors wrote in the abstract "We hope these definitions can pave the way for the development of algorithms to prevent such events by rationally correcting limitations in perception", but it is not clear to me how the definitions and theoretical results presented in the paper can really benefit this: under the formalization of the paper, black swans in stationary environments essentially stem from the distorted transition and reward functions, which naturally create a gap between the ground truth MDP and the human MDP. The main theoretical result of the paper (Theorem 4) focuses on proving this gap in the context of value function estimation, yet such a result is quite straightforward and the techniques used in proving it (bounding the gap in value estimation given the gap in transition and reward functions) is also somewhat common in the RL literature. Perhaps more importantly, I feel that such a result (and also the result in Theorem 5) is not really useful to inspire algorithm design since it does not tell us _how_ to correct the misperceptions in the human MDP. Other results in the paper are also quite natural to me and seem not really tied to the specific black swan problem considered by the paper (see Questions for details). While the authors have extensively discussed in the appendix that existing solutions in safe RL may also fall short, only _defining_ such a problem is not enough to me for acceptance.

I also have some concerns about the overall presentation of the paper. For example, the formal definition of s-black swan is deferred to Section 6 but heavily referred to in earlier sections, and I think it may be better to move this definition to earlier sections in the paper. I also do not understand the role of Section 3 beyond it re-emphasizes the main claim of the paper in Remark 1.

### Questions
- Is the proof of Lemma 1 in the appendix correct? The lemma in the main text is stated for visitation probabilities, while the proof in the appendix seems to only deal with rewards. The authors could clarify if there is a connection between the reward-based proof and the visitation probability statement that is not immediately apparent.

- Theorem 3 seems a quite general (and somewhat trivial) result to me: of course if we consider a sufficiently general case, the difference in MDP transition probabilities would result in different optimal policies. What is the concrete relation between this result and the s-black swan defined by the paper?

- What is the role of Proposition 1？And isn't it contradictory to Algorithm 1 (Algorithm 1 defines an s-black swan for arbitrary $t$, while Proposition 1 considers $t$ in specific time intervals)?

- How the definitions and theoretical results in the paper may be used to aid algorithm design?

- Could the hitting time analysis in Theorem 5 be used to inform when to trigger perception updates?

### Soundness
3

### Presentation
2

### Contribution
2
