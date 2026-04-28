# The Human-AI Substitution game: active learning from a strategic labeler

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The standard active learning setting assumes a willing labeler, who provides labels on informative examples to speed up learning. However, if the labeler wishes to be compensated for as many labels as possible before learning finishes, the labeler may benefit from actually slowing down learning. This incentive arises for instance if the labeler is to be replaced by the ML model once it is trained. In this paper, we initiate the study of learning from a strategic labeler, who may abstain from labeling to slow down learning. We first prove that strategic abstention can prolong learning, and propose a novel complexity measure and representation to analyze the query complexity of the learning game. Next, we develop a near-optimal deterministic algorithm, prove its robustness to strategic labeling, and contrast it with other active learning algorithms. We also analyze extensions that encompass more general learning goals and labeler assumptions. Finally, we characterize the query cost of multi-task active learning, with and without abstention. Our first exploration of strategic labeling aims to consolidate our theoretical understanding of the \emph{imitative} nature of ML in human-AI interaction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper consides strategic labelers for active learning task who may abstain to prolong the complexity of quering, such that they may be compensated with more labeling. The authors show that abstention could indeed enlarge query complexity, and present a novel minimax game as well as query complexity measure. A near-optimal algorithm based on E-VS bisection is designed to defend strategic labeling, and extensions to other active learning settings such as approximate learning, noisy labeling, multi-task learning are also discussed.

### Strengths
The strengths of this paper are its novelty of strategic learners for active learning tasks, as well as the theoretical soundness in the minmax formation and the effective version space bisection algorithm. This paper initiates the study of learning from a strategic labeler, which is original. The complexity of proposed E-VS method $O(\log{|\mathcal{X}|})$ clearly significantly improves existing VS algorithm of $\Omega(\{|\mathcal{X}|})$.

### Weaknesses
I think the biggest concern that might weaken this paper is its lack of empirical evidence. Despite the theoretical gaurantees, some of the settings are probabilistic (PAC or noisy observations for instance), making empirical evaluation of the proposed methods valuable. I understand there are so many great results in this paper and there is a page limit, but including some simple simulation studies could be beneficial.

### Questions
I only have a minor question. This paper assumes "the learner’s strategy corresponds to some deterministic, querying algorithm". Nevertheless, non-deterministic policies such as Thompson sampling is quite common in some active learning tasks such as Bayesian optimization. How does these non-deterministic policies fit into the framework of this paper?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides a set of theoretical evidence that labelers can slow down learning, in an active learning setting. The labelers is compensated by the number of labels that provided, and the learner wants to minimize the cost of learning. The paper proposes a maximal bisection algorithm for this setting and proves its sample complexity is optimal up to logarithmic factors. The paper further studies the noisy labels and multi-task learning, advancing its assumptions realisticity and applicability.

### Strengths
1. The paper is very well-motivated; the problem is of increasing interest for the society by more and more ML applications in the wild.
2. Quality: the paper flows smoothly by starting with the minimal setting of single task learning without noise and generalizes to wider settings. It proves lower bounds for the sample complexity of the problem, and proposes algorithms matching that lower bound up to logarithmic factors.
3. Significance: this paper is introducing a new interesting setting into active learning literature and proposes near-optimal algorithms for it.

### Weaknesses
1. Clarity: the notation is convoluted; $V$ is used for both VS and a hypothesis space variable. For instance, in table 1, what is $V$? it seems introducing a specific notation for VS (e.g., $\mathbf{V}$) or for the hypothesis space variable (e.g., $\mathcal{V}$) could help. The use of $V$ to represent both the version space and a generic hypothesis space variable creates significant ambiguity, especially when discussing the algorithm's behavior and sample complexity. This lack of notational clarity makes it difficult to follow the theoretical arguments and understand the precise meaning of the derived bounds. For example, in the context of the maximal bisection algorithm, it's crucial to distinguish between the space of possible hypotheses and the subset of hypotheses consistent with the observed data, and the current notation obscures this distinction.
2. There is no experimental reported. It could help clarify many abstract concepts introduced in the paper using even synthetic data. Examples like Table 1 could help practitioners employ the algorithms introduced in the paper in their applications. The absence of experimental results makes it challenging to assess the practical implications of the proposed algorithms. While the theoretical analysis is thorough, empirical validation is essential to demonstrate the algorithms' effectiveness in realistic scenarios. The paper introduces several abstract concepts, such as the cost-sensitive active learning setting and the maximal bisection algorithm, and experiments, even with synthetic data, would help illustrate these concepts and their behavior.

### Questions
Suggestions: Please consider 
1. moving table 1 after Definition 2.3 since it uses that definition.
2. separating the notations of $V$ (see 1. in the weaknesses section)

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
The authors study an active learning problem where the labeler can choose to give the correct label or abstain from labeling (refuse to label) for each query, in order to prolong the learner's learning process, hence get more reward. This is motivated by real-world scenarios where AI training data come from human workers who will eventually be replaced by AI once the AI is fully trained. The authors formalize this interaction as a game, propose query complexity notations to measure how long the learning process can be prolonged, and provide an active learning algorithm with a small query complexity. Extensions to approximate learning, noisy labeling, arbitrary labeling, multiple tasks, are discussed.

### Strengths
(1) The problem is well-motivated.  Although the "teacher wants to prolong learning process" phenomenon is not new in other literature, it is an important, new problem for the active learning community.  This paper can potentially lead to many follow-up results. 

(2) The various definitions of the query complexity are interesting. Theoretical results are sound.

### Weaknesses
W1: My major concern is that this paper has two really strong, restrictive assumptions. To illustrate this, let me describe the following scenario: Suppose there are two hypotheses $h_1$ and $h_2$ that give the same labels on all but one example $x^*$ (e.g., the hypotheses $h_1$ and $h_2$ in Table 1). Consider the case where the labeler correctly labels all examples except for $x^*$, and abstains from labeling $x^*$. In this case, the learner cannot tell whether the true hypothesis is $h_1$ or $h_2$. I can imagine that this scenario can easily happen in a real-world labeler-learner game where the labeler wants to prolong the learning process as long as possible. This is a key tension in the "human-AI substitution" game that motivates this paper. However, the authors simply disallow this scenario to happen by making two strong assumptions in their model:

(1) **The learner is not allowed to query an example multiple times**. If the learner can query an example multiple times, then the labeler can first abstaining from labeling for a while and then eventually give a correct label. It is very natural in practice for a learner to query an example multiple times until he gets a label. But this is not allowed in the authors' model. The concern here is that by not allowing repeated queries, the model deviates significantly from practical scenarios where a learner might repeatedly query a difficult example until a definitive label is obtained. This restriction could potentially lead to an artificial simplification of the learning dynamics.

(2) Under the assumption that the learner can query each example only once, the authors further assume **"Guaranteeing Learning Outcome"** (Section 1.1): the labeler must label in a way to guarantee that the learner can identify the hypothesis $h^*$ in the end. However, this requires the labeler to know the hypothesis space $\mathcal H$ of the learner very well so that he will not abstain from labeling critical examples (e.g., the $x^*$ above). **This is a strong assumption -- how can an average human worker knows the hypothesis space of the sophisticated machine learner?** The assumption that the labeler has comprehensive knowledge of the learner's hypothesis space seems unrealistic in many practical settings, especially when considering the potential complexity and opacity of modern machine learning models. This raises questions about the applicability of the proposed framework to real-world scenarios where labelers are unlikely to possess such detailed knowledge.

I might change my opinions if the authors can provide some strong motivations or real-world scenarios to support these two assumptions.

W2: the presentation of this paper is not very good. See my Questions and Suggestions below.

### Questions
**Questions:**

(Q1) What is the purpose of Section 3.1 (in particular Algorithm 3 and Proposition 3.7) ? My rough understanding is that, Section 3.1 wants to show that finding the maximal E-VS bisection point $x$ (line 3) in Algorithm 2 can be done efficiently by Algorithm 3 (correct me if I am wrong). If this is the case, then what is the time-complexity of Algorithm 3? How does Proposition 3.7 shows that finding the maximal E-VS bisection point can be done efficiently?

(Q2) What is the purpose of Section 3.9? The authors say that this section is to compare with EPI-CAL, but only give a formal result for EPI-CAL ($\Omega(\sqrt{m})$ samples in Proposition 3.9) and didn't give any formal result for the algorithm they proposed for comparison.

(Q3) How is this paper's model and result related to the "well documented" phenomenon that "teachers (masters) strategically slow down the training of their apprentices (Garicano & Rayo, 2017)" ?


**Suggestions:**

(S1) The presentation of Section 5.1 and 5.2 is really confusing.

Section 5.1 is about upper bound on the multi-task query complexity. Theorem 5.3 gives an upper bound under a regularity assumption and for the $c_{all}$ label cost. Proposition 5.1 is a counterexample where the upper bound doesn't hold without the regularity assumption, **but the authors didn't say which label cost this Proposition is for**. Proposition 5.2 is an example where the upper bound in Theorem 5.3 doesn't hold for the $c_{one}$ label function.

Section 5.2 is about lower bound (for the $c_{one}$ cost). Theorem 5.6 gives a lower bound on the multi-task query complexity under two conditions for the $c_{one}$ cost, while Proposition 5.4 and 5.5 are counterexamples where the lower bound does not hold if the two conditions are not met.

**I would suggest presenting the theorem first, and then give counterexamples.** And **can the authors give a lower bound result for $c_{all}$?**

(S2) $c(T(x))$ in Definition 3.1 is undefined.  (It is mentioned later in the paper but not here.)

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
This paper discuss the game between labeler and learning system, where the labeler's objective is to maximize profit, by following some strategy to choose abstaining labels and thus the learning is slowing down; meanwhile, the learning system's objective is thus finish learning as soon as possible, which puts higher requirements on the active query strategy, that is should be robust to abstaining. The paper theoretically analyzes the above observations and proves that absteining labels can indeed destroy the sample-efficient active learning system, base on which the authors further propose a near-optimal algorithm that is robust to absteining.

### Strengths
-  The problem this paper concerns is clearly defined, and all formalizations are clean.

-  The paper is well-organized with clear writing.

-  Modeling two parts of machine learning with respectively conflicting objectives by game and then it can be analyzed with some game-related techniques is novel.

### Weaknesses
 - The difference between an adversarial labeler and an abstaining labeler is not discussed.The difference between the concerning problem from active learning within an adversarial environment is not clear. Meanwhile, though it is mentioned that the labeler's strategy is identifiable, it is still unclear if it is the worst case.

- The motivation of the problem is too detailed, such that it can hardly be extended to other applications. It is recommended that real-world experiments should be conducted to validate the problem or it seems too artificial.

- The theoretical results are does not belong too much surprising information and has limited contribution to the algorithm design, since the algorithm design is mainly based on the labeler's strategy that is already pre-defined.

### Questions
See weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
