# On the Expressivity of Objective-Specification Formalisms in Reinforcement Learning

- Decision: Accept
- Scores: 8, 1, 6, 3

## Abstract
Most algorithms in reinforcement learning (RL) require that the objective is formalised with a Markovian reward function. However, it is well-known that certain tasks cannot be expressed by means of an objective in the Markov rewards formalism, motivating the study of alternative objective-specification formalisms in RL such as Linear Temporal Logic and Multi-Objective Reinforcement Learning. To date, there has not yet been any thorough analysis of how these formalisms relate to each other in terms of their expressivity. We fill this gap in the existing literature by providing a comprehensive comparison of 17 salient objective-specification formalisms. We place these formalisms in a preorder based on their expressive power, and present this preorder as a Hasse diagram. We find a variety of limitations for the different formalisms, and argue that no formalism is both dominantly expressive and straightforward to optimise with current techniques. For example, we prove that each of Regularised RL, (Outer) Nonlinear Markov Rewards, Reward Machines, Linear Temporal Logic, and Limit Average Rewards can express a task that the others cannot. The significance of our results is twofold. First, we identify important expressivity limitations to consider when specifying objectives for policy optimization. Second, our results highlight the need for future research which adapts reward learning to work with a greater variety of formalisms, since many existing reward learning methods assume that the desired objective takes a Markovian form. Our work contributes towards a more cohesive understanding of the costs and benefits of different RL objective-specification formalisms.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Um. Wow.

This paper is remarkable in many ways. The paper contributes a comprehensive set of proofs designed to show which reward formalisms in RL are distinctive and which can be subsumed by others; the central contribution of the paper is a lattice that diagrams these relationships. One conclusion from the work is that many formalisms offer distinctive capabilities, and that no single formalism is dominant.

The paper really does seem to be an incredible, detailed set of work. It is is highly theoretical, and is likely to be useful only to a select subset of researchers who are deeply steeped in RL research.

I am not capable of evaluating the proofs in any sort of detail, even though I have spent many years in RL. However, the way that the paper is written, combined with the parts that I was able to evaluate, suggests a serious contribution to the literature.

The question is: is ICLR the right venue for this work? While this is probably the magnum opus of this sort of work, it's unclear how much the general ICLR community would benefit from including it in the conference proceedings.

Would a journal be a better outlet?

### Strengths
+ Comprehensive evaluation
+ Clearly summarized results
+ Interesting resulting insights
+ Well-written, despite extensive technical detail

### Weaknesses
 - Likely to be useful to a very small subset of people
- Unclear if ICLR is the right venue
- Dense notation / writing

### Questions
Why do you think that ICLR is the right venue for this work, as opposed to an RL-specific conference or a journal?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper compares the relative expressivity of different task specification mechanisms for reinforcement learning agents. The authors set out to compare the relative expressivity of Markov rewards, limit average rewards, reward machines, linear temporal logic, regularized RL, and outer non-linear Markov rewards, and prove that each of these formalisms have a non-zero intersection, but also a non-zero exclusive component. In doing so the authors define 17 different task specification formalisms, and posit that a complete ordering over all possible policies of an agent is the most expressive (if impractical) tasks specification mechanism available for RL agents. 

The authors primarily provide expressivity result as a Hasse diagram where a directed edge represents subsumption of the task specification formalism.

### Strengths
1. **Timely and major significance**: The authors assertion that each of the popular reward mechanisms do not completely express all aspects of other reward formalisms is an important result, and the conclusions are supported by extensive background materials, and proofs. I also believe that the recommendation of the authors that researchers be more aware of reward specification frameworks, and algorithms catering to them is also well received. 

2. **Comprehensive survey of reward mechanisms**: The authors were systematic in their coverage of task specification formalisms, and have exhaustively documented each pairwise dependency. Although for presentational clarity, the proofs had to be relegated to the supplementary materials. The paper seems well indexed.

### Weaknesses
1. The authors center the discussion around ordering of stationary policies, and while it is justified in the context of the paper, and where the research effort has been directed historically, there are many instances (especially with partial observability), where non-stationary policy over observations must be implemented. This focus on stationary policies limits the scope of the expressivity results, as many real-world tasks require agents to adapt their behavior over time based on their history of observations, which cannot be captured by a single stationary policy. For example, consider a task where an agent needs to perform a sequence of actions in a specific order, which would require a non-stationary policy that changes its behavior as the sequence progresses. The expressivity analysis should ideally consider the broader class of non-stationary policies to be more generally applicable.

### Questions
1. I am curious if the authors only considered a fragment of LTL, or the entirety of LTL that allows for accpetability definitions over infinitely long trajectories
2. I am also uncertain if ordering over stationary policies is enough to describe an LTL task that requires a memory dependent policy (usually implemented through a cross product MDP)?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper surveys a wide range of objective-specification formalisms in reinforcement learning setting and establishes the theoretical expressive relationship among these formalisms. These results facilitate the choice of objective formalism for RL practitioners.

### Strengths
1. This work connects 17 objective-specification formalisms, compares their expressivity, and present results using a Hasse diagram. This contribution is clear.
2. The discussion and review of each formalism is helpful for RL practitioners to choose specifications.

### Weaknesses
1. There are some other formal language-based specification formalisms for RL, such as Signal Temporal Logic, which is more powerful than LTL because of its robustness property, and there are a wide range of literature in this direction, see e.g., [1], [2]. The authors are encouraged to study STL formalism with others to make the comparison more thorough.

2. As mentioned in Sec. 4.1, there is no tractability comparison among various formalisms, which is however very important for researchers/practitioners to decide which one they want to use.

3. The writing can be further improved. For instance, some notations can be be more precise (e.g., in Def. 2.7, vector in R^|S||A||S| should be replaced by R^|S| \times R^|A| \times R^|S|).

### Questions
I have no question.`

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper aims to provide a comprehensive picture of the expressivity of a pletora of objective specifications in RL, which include reward machines, trajectory feedbacks, multi-objective formulations among the others. The expressive power of an objective specification is measured in terms of the orderings it can induce over stationary Markovian policies in every possible environment, which is formally defined through a set of states, a set of actions, a transition kernel, and an initial state distribution.

### Strengths
- (Significance) The paper tackles a very important question on how to specify the objective in RL. Given the recent results showing the limitations of Markovian rewards (e.g., Abel et al., 2022) and the growing popularity of alternative feedback models, such as RL from human feedback, regularized RL, and convex RL to name a few, I think this is a very relevant research line.
- (Originality) I am not aware of previous effort in exploring the expressivity of such a comprehensive set of objective specifications.
- (Limitations) The paper is upfront in reporting the limitations of the contribution (see Section 4.1).

### Weaknesses
 - (Arbitrary analysis) The works makes a series of arbitrary choices in defining the expressivity of an objective specification (e.g., limiting the analysis to ordering of stationary policies) that are not sufficiently motivated in my opinion.
- (Implications) While the paper provide lots of results in terms of expressivity (as defined in the paper) of the objective specifications, most of the implications of their analysis are left as future work.
- (Related work) Given the nature of the work, which is in part a survey of objective specifications in RL, the discussion of the related literature is insufficient.
- (Clarity) While the main messages of the paper are clear and easily accessible, some notation choices are somewhat confusing, and they also depart the objective specifications from how they are formulated in the literature in some cases.

### Questions
- Can the authors address the comment reported above?

- Can the authors clarify which of the reported result is new and not directly implied by previous works?

- How can be OMO more expressive than FOMR? I am probably missing something, but why we cannot take for any ordering over occupancy measures $m_1 > m_2 > ... > m_n$ a function $f: M \to \mathbb{R}$ such that $f(m_1) > f (m_2) > ... > f (m_3)$?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
