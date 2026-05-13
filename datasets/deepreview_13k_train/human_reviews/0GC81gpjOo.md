# Cognitive Insights and Stable Coalition Matching for Fostering Multi-Agent Cooperation

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
Cognitive abilities, such as Theory of Mind (ToM), play a vital role in facilitating cooperation in human social interactions. However, our study reveals that agents with higher ToM abilities may not necessarily exhibit better cooperative behavior compared to those with lower ToM abilities. To address this challenge, we propose a novel matching coalition mechanism that leverages the strengths of agents with different ToM levels by explicitly considering belief alignment and specialized abilities when forming coalitions. Our proposed matching algorithm seeks to find stable coalitions that maximize the potential for cooperative behavior and ensure long-term viability. By incorporating cognitive insights into the design of multi-agent systems, our work demonstrates the potential of leveraging ToM to create more sophisticated and human-like coordination strategies that foster cooperation and improve overall system performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper focuses on the problem of cooperation in multi-agent systems when the agents are LLM agents. In particular, this work focuses on how theory of mind interacts with cooperation and introduce a mechanism for designing diverse ToM groups amongst these agents that optimise the overall cooperative performance.

### Strengths
- The related work is clear and concise.
- The paper is well motivated
- The empirical results for HumanEval demonstrating the effectiveness of the matching mechanism to match agents to those that they are able to accurately predict beliefs about is promising. This is alongside promising improvements in terms of Pass@1 rates.
- The empirical results are similarly promising in terms of problem solving and general reasoning.

### Weaknesses
 - Whilst the authors do mention that the coalition formation is generally an NP-hard problem, they do not offer any ideas about potential future possibilities that would help with the scalability of the framework
- I do not understand the prompt referenced in Appendix A and the corresponding LLM output. The belief model is rather vague, and when looking at the output of the alignment scores it seems a bit arbitrary - e.g. the belief model does not mention using an object oriented approach, but in the alignment score this seems to be highly valued? I am just slightly concerned that some of the alignment scores outputted by the LLMs are not particularly strong signals and ideally it would be measured using something more robust.
- Overall, my main concern is the potential scalability of the proposed framework, with firstly the coalition forming being difficult and secondly the requirement to generate beliefs over all other agents. Furthermore, whilst the empirical results are good and I am not downplaying them, I am not convinced the proposed settings are those that can really leverage ToM fully. However, this is not impacting my score.

### Questions
- For the insight that low ToM exhibits better cooperation compared to high ToM, I wonder how specific this is to the environment being looked at. For example, the multi-agent programming setting, at least to me, does not strike me as an environment that requires much ToM to successfully cooperate in, therefore low ToM being more successful may simply be due to the lower complexity of using it. Have the authors noticed this same trend in other environments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors present a method for using using Theory of Mind (ToM) and a coalition matching algorithm to allow LLM agents (using various LLM models) to cooperatively perform tasks in environments such as:

-Iterative Programming (HumanEval, MBPP)

-Debate (Two cooperative teams compete, with affirmative team taking on various forms of the model (no-ToM, ToM without matching, ToM with matchin), and negative team takes the baseline no-ToM)

-Logical and General Reasoning (Using AQUA-RAT and MMLU datasets)

The k-level ToM is set to take in an observation, the action of all agents at the previous timestep and the belief of the actions of all agents at the previous timestep, at the 0-level this is set to start with no belief. These are open-ended action spaces defined by natural language, and the observations, actions and beliefs are textual outputs. (The prompts of these are demonstrated in the appendix)

The Matching coalition algorithm takes a set of LLM agents and the possible matchings of these agents. It then assigns a preference order of these matchings. It aims to create stable matchings based on this preference order, such that agent i prefers agent j over all other pairings and agent j prefers agent i and neither agent has incentive to deviate from this pairing. A specific rule for this preference order is define based on the alignment, based on semantic similarity as calculated by the LLM, between beliefs of actions and the actual actions, and the agents are only matched if this  is above a certain threshold.

The results show that without matching lower ToM levels have higher cooperative trends, while with matching higher ToM levels have better cooperative trends. In all shown environments the ToM w. Matching  (their method) outperforms the baselines of no-ToM, or ToM w.o. matching.

### Strengths
The paper is easy to follow, with the appendix clearly aiding in understanding how the models function.

There is a clear logic as to why each component is added, this is shown through the experimentation and the results. Especially the need for adding coalition matching on top of the theory of mind.

There is a clear increase in Pass@1 the iterative programming environment with this model.

There is a clear increase in accuracy in the logic and reasoning problems compared to existing methods.

### Weaknesses
The calculation of the semantic similarity of beliefs and actions is left to the LLM, this does not lend itself to a general approach as the title alludes to. It is made clear throughout the paper that this is applied to LLMs however and I do not see this as a big weakness, but would like to see this made clear in the title if possible.

In the debate environment the baselines where both affirmative and negative lead to a bias of the affirmative winning 65.45% of the time, that is they are both using the same method. This is a cause for concern that this result may not be robust enough and might simply be taking advantage of this bias, is it possible to show the results the other way around? (With your model placed in the negative.)

Minor: The acronym FTM (Fraction of trust members/Frequency of team matching) is used multiple times making some sections difficult to understand.

### Questions
1)	For a non-LLM environment, how will the matching scores be calculated?
2)	In the debate environment the baselines where both affirmative and negative lead to a bias of the affirmative winning 65.45% of the time, that is they are both using the same method. This is a cause for concern that this result may not be robust enough and might simply be taking advantage of this bias, is it possible to show the results the other way around? (With your model placed in the negative.)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work examines the influence of different levels of Theory of Mind capabilities on collaboration among multiple Large Language Model (LLM) agents. The authors propose an algorithm to enhance LLM agents’ teamwork performance by matching partners with high belief alignment. While the idea of guiding multi-agent collaboration through ToM and belief alignment is novel, this paper presents the proposed method in a less comprehensive manner, missing many important details. Researchers may encounter difficulties when applying the proposed algorithm in specific scenarios. Additionally, the claimed conclusions do not align well with the empirical results and therefore need further clarification.

### Strengths
The introduction and related work section motivate the research pretty well. 

The idea of guiding multi-agent collaboration through ToM and belief alignment is novel. 

The authors conduct comprehensive evaluations across diverse task scenarios and base LLMs, presenting both quantitative and qualitative results.

### Weaknesses
The ToM formulation presented in Section 4.1 deviates from the common definition of higher-order ToM. When conducting recursive ToM inferences at level-k, agents are only given their own belief at level-(k-1) rather than the beliefs of other agents. This approach limits the model's ability to capture complex inter-agent mental state reasoning, as it does not allow for modeling nested beliefs about others' beliefs, which is a key aspect of higher-order ToM. I recommend that the authors refer to [1] for its definition of higher-order mental state inference.

The proposed alignment measurement in Section 4.2 may not apply to general high-order ToM inferences in multi-agent systems. For example, “what I think A is thinking about B’s action” and “what I think C is thinking about B’s action” are different 1-level ToM inferences that result in the same alignment measurement as defined in this paper. The alignment metric, as currently defined, fails to distinguish between these different types of inferences, which reduces its utility in complex multi-agent scenarios. The authors might want to explicitly define the format of beliefs to clarify the formulation and address this limitation.

The multi-agent setup for each evaluation scenario is not clearly described. It is unclear how many agents are involved, what their action and observation spaces are, and how they collaborate. For instance, the interactive programming scenario appears to be a centralized system with full observation, as the PM is the only agent making decisions and ToM inferences. This setup limits the applicability of the proposed method to truly decentralized multi-agent systems. The value of ToM is less salient in such a single-agent system, as the benefits of modeling other agents' mental states are diminished when only one agent is making decisions.

The two evaluation metrics, FTM and coalition stability, are the optimization objectives of the proposed algorithm rather than direct measurements of LLM agents’ collaboration performance or “cooperation trends.” Using these metrics to quantify “cooperation trend” introduces a circularity issue, as they are not independent measures of performance. The claim that “agents with higher ToM capabilities may not necessarily exhibit better cooperative trends” conflicts with the results shown in Tables 3 and 4, where agents with ToM perform better. I recommend using other metrics, such as task completion rate or efficiency, to provide consistent conclusions and increase criterion validity. The current metrics do not provide a clear picture of how ToM impacts actual task performance.

The proposed algorithm is vague and highly dependent on specific prompt design when generalizing to different task scenarios. For instance, what happens when an agent is assigned to cooperate with a given partner (line 8 of Algorithm 1) is not clearly defined for each scenario. This ambiguity could lead to potential bias in evaluations. In the debate case study (i.e., lines 495-497), the ToM with matching condition has two LLM agents forming arguments, while the other conditions only involve one. The performance advantage might be due to the increased number of agents via self-reflection, rather than the proposed matching algorithm. This lack of control over the experimental conditions makes it difficult to isolate the effect of the proposed method.

### Questions
How reliable are the alignment measurements provided by LLMs? 

How are the specialized ability scores used in evaluations, and what is their impact?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the concept of theory of mind (ToM) in the context of one LLM agent forming and managing coalitions of other LLM agents. They show that prompting the first LLM agent to engage in 2-level reasoning about the others' beliefs can actually _hinder_ performance compared to 1-level reasoning (cf. the general concept of k-level reasoning). They introduce a method of comparing and matching agents based on their ability to predict each other's actions. Their experiments study how the use of that metric in forming coalitions of LLM agents impacts the agents' ability to solve problems in the domains of programming, logic, and general reasoning.

### Strengths
The questions underlying this paper are certainly interesting. While much work has focused on the improved cooperation using ToM, few (to my knowledge) have investigated how this might hinder cooperation, at least not (again, to my knowledge) in the context of LLM agents. More generally, the issue of intelligent coalition formation in this context is an interesting problem and one that I believe will have increasing real-world relevance in the coming years. The idea of alignment of beliefs in order to solve this problem is natural and original (again, that is to the best of my knowledge, though I also would not be at all surprised if a version of this had been studied before in the game theory or multi-agent systems literatures, outside the context of LLMs). I also appreciated the effort the authors put in to studying a relatively wide variety of tasks, models, and frameworks for multi-LLM problem-solving. The presentation of their results was largely clear.

### Weaknesses
Unfortunately, despite its positive aspects, I think the paper does have some significant issues. In what follows I have attempted to cluster these and order them approximately by importance.

**Matching Algorithm Confusions**

The matching algorithm seems underspecified in several places, and it is not always clear what the authors are actually doing. Moreover, I didn't feel that the underlying theoretical principles were always appropriate. More concretely:
- The authors start by talking about the set of an agent $i$'s partners $\mu(i)$, but based on their matching algorithm they seem to implicitly assume that $\mu(i)$ is always a singleton (see Equation 2). Otherwise, matchings are stable only when player $i$ would not prefer to be partnered with $j$ over its current _set_ of partners $\mu(i)$. But what would that mean? Are preferences between sets of agents instead of single agents? If so, the relevant comparison would presumably be that agent player $i$ would not prefer to be partnered with any _set_ of other agents over its current _set_ of partners $\mu(i)$. The formulation of preferences over sets of agents is not clearly defined, and it is unclear how the algorithm handles the case where an agent might prefer a different set of partners than its current one.
- In line 9 of algorithm 1, what happens after agents signal a desire to re-match? What if the belief misalignment measure is greater than the tolerance $\epsilon$ for all other agents? Does the agent end up in a singleton coalition? The authors state that the iterative process of coalition formation ends in a stable matching but they do not actually prove this. Especially with the introduction of preferences based on differing skills (see the next point), I actually suspect that it would be trivial to create a cyclic matching problem. The algorithm lacks a clear mechanism for handling situations where no suitable match can be found within the tolerance, and it's unclear how the algorithm avoids getting stuck in a cycle of rematching.
- The preference order described in equation 4 are based on agents having different skill levels $\alpha_i$ on different tasks, but where do these skill levels come from? More importantly, if the point is to match agents with complementary skills, why does the matching algorithm only compare agents' skills on a _single_ task? The algorithm's focus on a single task for skill comparison seems overly simplistic, especially if the goal is to create teams with diverse and complementary skill sets. The paper does not specify how these skill levels are determined, which is a critical detail for the reproducibility of the results.
- Minor: the authors say on line 244 that the alignment between beliefs and actions is not mathematical subtraction, despite them denoting it that way. I would strongly suggest not denoting it using subtraction to begin with and being more explicit about what the distance measure here actually is.

**Strength of Motivating Claim**

The authors' motivating claim is that lower-level ToM abilities may improve the ability of agents to cooperate beyond higher-level ToM abilities. Their justification for this is a setting where one agent -- a "Project Manager" (PM) -- is instructed to use either 1-level or 2-level reasoning to organise several other agents (all of which are instructed use 0-level reasoning). But this essentially means that in the latter case the PM is being instructed to reason about the agents acting in a way that they do not in fact act. Explained this way, it is still somewhat interesting but by no means surprising that the PM is less successful when prompted to reason using higher-level ToM. Essentially, $k$-level reasoners are designed to best respond to $(k-1)$-level reasoners, not $(k-2)$-level reasoners.
- Relatedly, looking through the actual LLM outputs included in the appendices, the level-2 ToM responses seem quite strange. They are worded as if they are predicated on the other agents _actually observing_ actions in advance, rather than _anticipating_ instructions. I am not really sure what is going on here, but reading through it was not at all surprising that the higher ToM agents performed less well on the task, as they appeared to be being mis-instructed. The level-2 ToM responses appear to be based on a misunderstanding of how the other agents are acting, which undermines the validity of the comparison.
- As a final sub-point on this topic, I suggest that the authors also benchmark against a 0-level PM and against settings where the agents are 1-level or 2-level reasoners, at least for their motivating experiments described in Table 1.

**Missing Experimental Details**

There are several (relatively minor) aspects missing from the discussion and presentation of the experiments that, if present, would improve the paper.

- There are no error bars or reports of standard errors for the experimental results, making it difficult to interpret their statistical significance. The lack of error bars makes it impossible to assess the reliability of the results and to determine if the observed differences are statistically significant.
- I assume the ToM level for debating agents arguing for the negative side is 0, but it would be good to clarify this. It is important to explicitly state the ToM level of the negative side to ensure the reproducibility of the results.
- Once coalitions are formed, how do the prompts/instructions given to the agents in different coalitions actually change? The paper does not clearly explain how the prompts are modified after the coalition formation, which is a critical detail for understanding the experimental setup.
- How many agents are actually present in the various settings, and what are the sizes of the coalitions that are formed? The paper lacks specific details about the number of agents involved in each experiment and the size of the resulting coalitions, which are essential for understanding the experimental setup.

**Game-Theoretic Reasoning and Precision of Claims**

This is a relatively minor, but a few times I found myself slightly frustrated by the authors claims, which I believe did not fully take into account the relevant game-theoretic concepts (see also the confusing use of what appears to be a binary matching algorithm for n-player coalition formation, described further above).

- A key example is the authors' claim that the so-called "Fraction of Trust Members (FTM)" is a good measure of what they term the "cooperative trend"  (N.B. to be grammatical, this should probably be "Trusted" not "Trust", though it is not actually clear what the relevance of the concept of "trust" even is here). But belief alignment by itself does not imply higher levels of cooperation. I may have perfectly accurate beliefs about what you are going to do in a two-player zero-sum game (where cooperation is definitionally impossible). Thus, it is clearly not true that in general "a higher FTM value [indicates] a more cooperative agent", as claimed in line 410/411. The use of "Fraction of Trust Members" as a measure of cooperation is misleading, as belief alignment does not necessarily imply cooperation, especially in non-cooperative settings. The paper needs to clarify the specific cooperative context in which this metric is valid.
- Relatedly, the authors talk about ToM improving cooperation but is more about ToM improving the facilitation/management skills of a single PM agent. This is also a very interesting and valid topic of study, but I suggest the authors change the phrasing slightly throughout the paper to better reflect the rather narrow form of cooperation problem they consider. Indeed, my understanding is that the authors largely focus on the case where only one agent (a PM) is imbued with ToM.

### Questions
Please see the Weaknesses section for my questions. I also welcome the authors to correct any misunderstandings I may have about their paper.

### Soundness
2

### Presentation
2

### Contribution
2
