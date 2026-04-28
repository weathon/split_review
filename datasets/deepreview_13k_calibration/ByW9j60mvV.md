# RL Algorithms are Information-State Policies in the Bayes-Adaptive MDP

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 3, 5, 5

## Abstract
RL studies the challenge of maximizing reward in unknown environments; the Bayes-Adaptive MDP (BAMDP) provides a formal specification of this problem, albeit one that may be intractable to solve directly. In this paper, rather than trying to solve the BAMDP, we use it as a theoretical resource. In particular, we view RL algorithms as *hand-written information-state policies* for the BAMDP and derive a number of insights from this approach. For instance, one simple observation from bandit theory is that optimal policies for the BAMDP, i.e., ideal RL algorithms, do not necessarily converge to optimal policies for the underlying MDP---even though RL theory has typically regarded the latter property as essential. We also apply the theory of potential-based reward shaping in the BAMDP to analyze valid forms of intrinsic motivation. We then show that BAMDP Q-values can be decomposed into separate measures of the value gained from exploration and exploitation. We finally derive a direct relationship between an RL algorithm's shaping function in the MDP and its suboptimality in the BAMDP, and use these results to clarify the roles of many forms of reward shaping.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new framework for understanding reinforcement learning (RL) algorithms as policies in Bayes-adaptive Markov decision processes (BAMDPs).

A BAMDP is a species of "meta" sequential decision-making process that -- given a set of candidate tasks (represented as MDPs) within which the true task lives as well as a prior over those tasks -- formalizes the problem of balancing acquiring information about the task being solved with maximizing its lifelong expected return. Unlike policies for single tasks/MDPs that seek to myopically maximize rewards under a fixed policy without accounting for policy changes based on future information gain, a BAMDP policy can be viewed as a procedure for updating policies over time based on the task information they generate.

In light of the foregoing, the paper describes how RL algorithms can be viewed as BAMDP policies and investigates useful consequences of doing so. Specifically:
* standard, "myopic" RL algorithms are formally characterized within the BAMDP framework;
* the regret of such standard RL algorithms with respect to Bayes-optimal solutions to the BAMDP is characterized;
* a decomposition of the regret into two familiar components corresponding to information gain (exploration) and value improvement (exploitation) is provided;
* a characterization of potential-based reward shaping in the context of BAMDPs and its relationship to reward shaping of standard, myopic RL algorithms is given.

### Strengths
This paper provides a creative, insightful new formal framework for reasoning about RL algorithms as policies in BAMDPs. The work is theoretical in nature and will be of significant interest to the RL theory community. The connections it draws between reward shaping in the BAMDP realm and effects on standard, myopic RL algorithms may provide a catalyst for new developments in the experiment RL community as well. The paper is primarily a conceptual work synthesizing existing ideas (BAMDPs with RL algorithms) and providing new perspectives. The theoretical results are straightforward with no serious mathematical heavy lifting required, but they are clear and insightful. The paper is well-written and the recurring example pictured in Fig. 1 is used effectively to provide concrete illustration of main concepts throughout.

### Weaknesses
The primary weakness of this paper is the absence of a direct practical application of the ideas developed. This is natural, given the conceptual nature and theoretical focus of the work, but some experimental evidence supporting the main ideas would make the paper much more accessible to the experimental RL community. For example, it would be very helpful to have numerical experiments illustrating key aspects of the discussion of reward shaping provided in Sec. 6 on a non-trivial problem. Specifically, while the paper discusses the potential for reward shaping to alter the effective exploration-exploitation trade-off, it does not provide concrete examples of how this could be leveraged to improve performance in practice. The paper would benefit from a demonstration of how the BAMDP framework can inform the design of novel reward shaping functions that lead to improved learning outcomes compared to standard, myopic RL approaches. Furthermore, while the theoretical results are clear and insightful, the paper could benefit from a more detailed discussion of the limitations of the proposed framework. For instance, how does this framework handle situations with very large or continuous task spaces, and what are the computational implications of using a BAMDP approach in such settings?

### Questions
* why is $R(r_t | s_t, a_t)$ included in the definition of $\bar{T}$ in bullet point four of the BAMDP definition on page 3? can you clarify how $\bar{T}( \cdot | \bar{s}_t, a_t)$ remains a pdf/pmf?
* the analysis in the appendix seems to consist primarily of proving Theorem 3.1 and providing computations for the caterpillar example; are there any key innovations in the analysis that you consider worth highlighting?
* do you have any ideas for how the discussion in Sec. 6 might be illustrated experimentally?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies reinforcement learning through the lens of Bayes-Adapative MDPs, in which the RL algorithm is viewed as a policy of the BAMDP. The paper first provides a formal description of the setting and its components. Then, it derives a decomposition of the BAMDP value into the sum of the Incremental Value of Information, which coarsely measure the information gain over the true MDP, and the Value of Opportunity, which measures the expected return given the current information. Finally, the decomposition is used to analyse a set of reward-shaping mechanisms that have been previously considered in RL literature, including intrinsic motivation.

### Strengths
- (Originality) The paper provides a novel and interesting view of reinforcement learning algorithms as policies over BAMDPs.
- (Categorization) The paper provides a valuable characterization of a handful of reward-shaping approach through the lens of BAMPD value.

### Weaknesses
 - (Motivation) Whereas the formulation is interesting, BAMDP is also known to be an intractable problem in general, so it is unclear what benefit this new perspective can bring. Specifically, given that the goal of RL is to find optimal policies in the underlying MDP, and that efficient algorithms exist for this purpose under certain assumptions, it is not clear that framing the problem as a BAMDP adds any value. The paper does not clarify how this perspective helps in the design of more efficient algorithms, or provides any new insights on the limitations of existing ones.
- (Implications) The paper does not fully clarify how the introduced perspective should help analyzing existing RL algorithms and building more advanced algorithms in the future. While the decomposition of the BAMDP value into Incremental Value of Information and Value of Opportunity is conceptually interesting, the paper fails to demonstrate concrete ways in which this decomposition can be used to improve RL algorithms. The analysis of reward shaping mechanisms remains at a high level, without providing any formal guarantees or deeper understanding of their impact on the learning process.

The paper is providing an original interpretation of RL as the problem of solving a BAMDP, and it does also report some insights, such as the value decomposition that explicitly separates exploration and exploitation contributions to the value. However, despite the promising formulation, the paper is somewhat falling short from providing a coherent set of implications resulting from this new perspective, beyond a few informal consideration over reward shaping methods. In my opinion, to clear the bar for acceptance this paper shall narrow its scope, e.g., presenting the contribution as a study of reward-shaping through BAMDP perspective, and provide more formal/deeper implications from the analysis, such as a study on how the different shaping methods impact the Bayesian regret and under which assumptions or prior any of those methods can be considered optimal. For this reason, I am currently providing a negative evaluation to the paper, but I encourage the authors to keep working on this problem, which looks like a nice research direction to pursue.

### Questions
1) What is the point of framing the RL problem as BAMPD, when it is well known that BAMDP cannot be solved efficiently in general? Especially, given that provably efficient RL algorithms exist (under somewhat restrictive assumptions), does this mean that the provided formulation is missing some of the structure of the underlying problem?

2) While setting a prior over the tasks might be reasonable in meta-RL or analogous settings, in which some knowledge of the task distribution can be collected during training, is this also reasonable in standard RL? Of course any MDP can be seen as a sample from a very uninformative prior over all the possibile MDPs, but this does not seem to provide any benefit.

3) Can the authors discuss how their framework will help producing a deeper analysis of existing RL algorithms and possibly guide the development of improved algorithms?


MINOR
- The use of \citep and \citet in the paper is sometimes confusing. I would suggest the authors to use \citet only when the papers' authors name are part of the sentence;
- Some choice of reference is somewhat odd, such as reporting Yang et al., (2021) for regret bounds in RL. There are a pletora of papers on that topic, and perhaps a more representative reference can be chosen;
- The itemize at the end of the Introduction is missing a full stop after the last bullet point.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work analyses reward shaping techniques from the perspective Bayes regret.

First, they establish a notation for viewing RL algorithms as policies in the framework of Bayes-adaptive MDP (BA-MDP), a framework which constructs a history-MDP and proposes to maintain (and predict) posteriors over the unknowns of the MDP and of which a solution will optimally explore with respect to the prior given the to agent.

The Q-values of optimal solution to the BA-MDP are decomposed into "incremental value of information" plus "value of opportunity".
The first value, loosely, is the utility of the knowledge (improving MDP posterior accuracy) that comes from doing an action in a state at a particular time step (through better informed actions in the future).
The latter, again informally, is the actual (long term) utility expected under the current posterior that is gained from doing the action in the state.

Then, the paper compares the Q values of such a optimal algorithm to a myopic (typical) RL algorithm which only considers the current information.
Concretely, as an example, Q-learning approximates the Q-values given previous data, and not given potential future interaction based on uncertainty over the MDP.
It is shown that this corresponds to maximizing only for the "value of opportunity".

Finally, the paper looks at various reward shaping approaches as compensating for the difference between the Bayes-optimal Q values and those of typical RL algorithms.
This analysis introduces the notion of shaping the Q signal or I (knowledge) signal.
For instance, adding minor rewards for getting closer to a goal state is reward shaping the Q signal, whereas positive reward for rare occurrences such as new observations means shaping the I-signal.

### Strengths
The paper proposes a very interesting concept, that of considering RL algorithms as policies in history-based MDPs.
The resulting derivation, one where myopic (typical) RL algorithms can be seen as optimizing only one of two terms of the optimal Q-value, has much potential for understanding and framing RL.

This is important, because the exploration-exploitation problem is a core issue unique to RL and one where progress should be of interest to the majority of RL research community.
And progress, especially non-incrementally, often requires novel insights and perspectives which, I believe, this paper has managed to find.

As a result, I find this paper a good step in a promising direction and hope to see it fleshed out a little more.

### Weaknesses
Despite these strengths, my main concerns are its presentation and lack of formality (especially in the analysis) which affect the contribution significantly.

Sometimes this results in just vague statements, such as comments like "... manually programmed RL algorithms." and "... since regardless of how much meta-learning takes place, some algorithm must be written down eventually." in the introduction (and maybe even the usage of "information-state policies", which are never really defined or seemingly used technically, but pop-up occasionally?).
Other times, however, this is detrimental to understanding the intent. 
For instance, what is the "true p(M) of the problem" (before 6.2.1)?
Also, it is still unclear to me how a potential based shaping function is relevant to the paper:
It does not seem important, especially since the section talks about reward shaping in the BA-MDP:
why would one want to shape the reward if a solution is already optimal with respect to exploration?

Most importantly, I feel like the key contribution is missing / not obvious in its current version.
The paper contains of English text describing how various reward shaping techniques can be seen (categorized?) in different lights, but for those interested in exploration in RL there seems little novel.
For example, intrinsic reward is very well known (indeed motivated by the idea) to boost the Q-value based on the notion that "knowledge" has value.

To conclude, the definition of regret of typical RL algorithms compared in Q values with the Bayesian optimal solution seems like great step, but the actual analysis (in its current form) is lacking in formality and rigor that I believe is necessary for a paper at ICLR.

### Questions
N/A

### Soundness
3 good

### Presentation
1 poor

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
This paper tries to describe RL algorithms in the context of BAMDP. It shows the regret of the algorithms in terms of BAMDP value and decomposes the value into the incremental value of information and value of opportunity. Finally, the regret is further analyzed using the concept of reward shaping.

### Strengths
The paper provides the theoretical analysis of the main topic.

### Weaknesses
The motivation and contribution of the paper is unclear. The presentation of the paper is unfocused, thereby hard to follow its main concept and insights. Also, the practicalness of the analysis is unclear because of the lack of practical examples or insights in terms of the usage of the analysis. (For example, how we can improve or design more practical RL algorithms using the insights.) Since multiple concepts such as BAMDP, RL algorithms, and reward shaping are used in the paper, it should be clear how each one is related and why it is important under a main message of the paper. But it doesn't, so it's confusing. The connection between the theoretical analysis and its practical implications remains weak. While the paper provides a theoretical decomposition of the BAMDP value, it does not clearly demonstrate how this decomposition can be used to design or improve existing RL algorithms. The paper introduces the concept of the incremental value of information and the value of opportunity, but it does not provide concrete examples of how these concepts can be used to guide the design of exploration strategies in RL. The analysis of reward shaping, while interesting, lacks a clear justification for its importance in the context of BAMDPs. The paper does not provide a clear explanation of why reward shaping is a relevant tool for analyzing regret in this framework, and how it can be used to derive practical insights for RL algorithm design. The paper also lacks a clear explanation of how the theoretical analysis relates to the practical challenges of RL, such as sample efficiency and generalization. The analysis is primarily focused on theoretical aspects, and it does not provide sufficient evidence that the proposed framework can address real-world problems in RL.

### Questions
1. The motivation and contribution of the paper is not clearly provided. It is unclear for what purpose RL algorithms are being described in the context of BAMDP. Is this because of specifying a proper way to use RL algorithms for BAMDP, or because of showing that RL algorithms are not suitable for BAMDP? 
2. In a similar context, it is not clear why the paper considers BAMDP. For meta-learning, considering BAMDP is reasonable since meta-learning tries to address multiple tasks in real-world applications together, which can be modeled as different task MDPs. Are the authors arguing that real-world problems that have traditionally been modeled with MDPs are actually more suited to be modeled with BAMDPs?
3. What is "hand-written information-state policies" in the abstract standing for precisely? That is used only in the abstract and there is no clear description in the text.
4. The rationale for applying reward shaping in analyzing the regret is unclear. Why it is important should be justified more clearly.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
