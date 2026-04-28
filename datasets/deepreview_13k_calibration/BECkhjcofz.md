# Evaluating the Goal-Directedness of Large Language Models

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
LLM-based agents may transform AI and society in the near future. Along with opportunities for automation and increased productivity come novel safety and ethics concerns. This means both researchers and regulators need good ways to keep track of progress and properties of LLM-based agents. A key feature of agentic behaviour is goal-directedness, which has so far received limited attention in the context of AI agents. In this work we define the concept of goal-directedness for LLM agents, and develop a framework for evaluating it empirically on tasks involving information gathering, information processing, and execution. Results on state-of-the-art LLM agents indicate a lack of goal-directedness, meaning models often fail to fully deploy capabilities that they evidently have. This raises the question of how we can elicit the full capabilities of LLM-based agents, as well as what policies should be in place for future more goal-directed systems.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Authors defined the concept of goal-directedness for LLM-based agents and measured this metric in tasks that involve information gathering, planning, and execution phases. They empirically probed four SOTA LLM agents to tackle a block stacking task focusing on different combinations of the phases. They found limited goal-directedness across all LLMs with Gemini performing better overall.

### Strengths
* New Metric: There is a huge interest in the community to better evaluate LLMs for planning and the goal-directedness can play a role

* Empirical evaluation: Authors highlighted that current LLMs, despite their sophisticated capabilities, do not fully deploy these capabilities toward goal achievement.

* It was refreshing to see authors focused on stochastic environments.

### Weaknesses
 * Readability: The paper is hard to follow and the definitions are not rigourous. In 79, you mentioned "The gap between actual and expected performance given optimal use of capabilities". To me this means the difference between expected return under optimal policy and observed return under optimal policy. Not sure how this translates to goal-directedness as it only captures domain stochasticity. In 171, you mean expected return vs. expected reward. Reward is instantaneous while return is the cumulative return. In 174, can you define E[regret | optimal use of capabilities]? The second eqn. means how much the return could improve with additional capabilities. I don't think it is the same as goal-directedness-deficit.


* Generalization Issues (Line 139): The statement that LLMs do not ask clarifying questions might not fully apply, as some LLMs, like GPT-4, demonstrate this capability.

* Terminology Ambiguity (Lines 159 & 171): Concepts such as “capability-conditioned goal-directedness” and expected “return” versus “reward” lack clarity and could be better explained.

* Undefined Terms (Lines 174, 289 & 313): Key terms, including 
E[regret∣optimal use of capabilities], "unexplained_regret," and "statistical sophistication," need explicit definitions to improve comprehensibility.

* Algorithm Motivation (Line 244): Lacks clear motivation for Algorithm 1. Would be great to discuss its creation.

* Inconsistent Noise Parameters (Line 250): On 205 you mentioned sigma to be .1 * true height, yet here you also added a constant factor. 

* Presentation Quality (Various Lines): Figures and images are of low quality, lacking necessary labels (e.g., missing legend in Fig 8.b) and captions (e.g., Fig 4), and should be vectorized with larger fonts for readability.

Minor:
* 389: "Gemini performs better than would be expected from" Fix grammar 
* 492: Whence -> hence
* 504: language-based LLM -> LLM as L stands for language

### Questions
* (Line 369): Why does the regret for GPT 3.5 fluctuate (i.e., drop and then increase) in the observed experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a mathematical definition of "goal-directedness" in the context of LLM-agents as the difference between the agent's actual and its expected performance on tasks given optimal use of its capabilities. The authors then introduce a toy Blocksworld environment and an associated task with three variants and proceed to measure the performance and goal-directedness of some LLM-agents on this task. The LLM-agents studied are based on GPT-3.5-turbo, GPT-4-1106, GPT-4o, and Gemini-1.5-Pro. They find that the agents differ in their capabilities and goal-directedness, and while they are generally all rather capable, they are not very goal-directed. The paper also discusses associated ablation experiments and closer analyses.

### Strengths
**Originality**

While other work has aimed to define goal-directedness in similar settings, the definition proposed in this paper seems to be novel, while also being elegantly simple and powerful in its generality.

**Quality**

The toy setting and task introduced in the paper are well-designed and highly appropriate for the investigation. The experiments are well-motivated, the ablations are interesting and useful, the analyses are informative and include confidence intervals. Overall, it is clear the authors had good attention to the question at hand and applied good intuition to what experiments would be most informative.

**Clarity**

The proposed definition of goal-directedness is clear, straightforward (this is a positive thing), and well-motivated. The experiments conducted are very close to "minimal but complete" in that they include all and only the aspects that are necessary to study goal-directedness, which makes for very clear results. The text flows well and the sections motivate each other. The plots are clear and informative.

**Significance**

As LLM-agents become increasingly widely studied and deployed, it becomes increasingly important to form nuanced understanding of them in general settings. This paper contributes to this. Goal-directedness as a trait of LLM-agents also has safety implications, and as such this contribution is all the more significant.

### Weaknesses
1. It is a significant issue that the calculation of goal-directedness assumes direct access to the agent's capabilities. This is because the measurement of the capabilities looks a lot like the measurement of the agent's overall performance on a task. Presumably it already will reflect the agent's goal-directedness in some capacity. Essentially, it creates a "turtles all the way down" problem. Breaking the task down seems like a reasonable thing to do, but not only is it imperfect in the sense above, it also requires some subjective judgement on the part of the experimenter (different experimenters can reasonably disagree on how a task should be broken down, especially in the case of more realistic tasks).

2. A concrete example of the issues above: prompting for motivation significantly affected the agent's motivation on the "Cognitive Effort" partial task. So the claim being made here is that this partial task is already very "goal-directedness"-loaded, i.e. "goal-directedness" is a significant component of the agent's performance on the task. But this is already a broken-down task, and to get to direct capabilities, the authors only break it down further into two component capabilities. How can we be confident that we have now reached a pure source for capabilities measurements?

3. The only results are shown in the toy BlocksWorld environment. I think it makes sense for the main experiments to be conducted there, but I am left very curious to see how the framework can be applied to realistic tasks, and in particular, whether the results would hold there.

### Questions
1. Do the authors agree with the issue I point out in Weakness 1? How do they think the presumed purity of the capabilities measurements can be justified?

2. Similarly, how do the authors recommend that a task be broken down into its constituent capabilities? Is there an objective general procedure?

3. Is goal-directedness here claimed to be a property of an agent? Is there any claim as to how the goal-directedness measurements on an agent would differ across different tasks? We do expect the same agent to be differently capable at different tasks. Should they also be differently goal-directed? From the conceptual motivation, I would hope this is not strongly the case, but I expect that experimental results might show otherwise. Do the authors agree?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates the performance of LLMs in goal-directedness behavior. It explores whether LLMs can effectively leverage their capabilities and resources to achieve defined objectives by defining goal-directedness, developing an evaluation framework, and assessing LLM performance in practical tasks.  The primary contribution of this paper lies in the design of the evaluation framework. This framework quantifies the extent to which agents utilize their capabilities toward a specific goal by measuring relevant agent abilities, predicting how agents would resolve problems if they fully employed these abilities, and comparing the predicted performance with the agents' actual problem-solving outcomes.

### Strengths
1. The goal-directedness approach enhances the effectiveness of LLM-based agents by providing robust constraints in terms of safety and ethics. Therefore, evaluating the goal-oriented nature of LLMs is of significant importance.
2. The clarity of the writing is commendable, facilitating comprehension.
3.  The design of the evaluation framework is intriguing, and the conclusions drawn regarding the goal-directedness  of several state-of-the-art LLMs are persuasive.

### Weaknesses
- The discussion of related work is insufficient. For instance, the paper "Can Large Language Models Reason About Goal-Oriented Tasks?" appears to provide a more comprehensive interpretation of the goal-oriented nature of LLMs. I recommend that the authors elaborate on the distinctions and connections between the two studies.
- The contributions of the paper are relatively limited, with the primary contribution seemingly revolving around the design of the goal-directedness deficit and the evaluation of several LLMs' performance.
- The experimental design is somewhat simplistic and does not adequately capture the goal-directedness of LLMs across more complex and diverse tasks. Further investigation is needed into the internal mechanisms of the models, specifically how decisions are made and how these decisions relate to their goal-directed behavior.
- It is essential to test the influence of auxiliary methods (e.g. COT, TOT) aimed at enhancing the reasoning capabilities of the models on the experimental outcomes.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a new benchmark to evaluate the "goal-directedness" of Large Language Models (LLMs); "goal-directedness" in this context is defined as "the propensity to use available resources and capabilities to achieve a given goal".  To do so, the authors create a BlocksWorld environment in which the "goal-directedness" deficit can be estimated as the difference between the expected rewards given that the capabilities are used to their fullest extend and the actual reward obtained . Then, the authors evaluate different LLMs in this environment (and ablations of it) demonstrating that current models lack the ability to use their resources and capabilities fully.

### Strengths
I want to preface this review by saying that LLMs and their evaluation is not my area of expertise so I might be not familiar enough with the current literature to assess the impact of the contributions of this paper. Overall I see potential in the area of research and the problem that is trying to be addressed. The problem is well motivated in terms of potential applications for the evaluation and understanding of LLMs.

1. **Neglectedness**: The study of goal directed behavior in LLMs is interesting, has some useful applications and has been almost completely neglected in current research directions.
2. **Safety and Ethics Implications**: The paper discusses the potential risks associated with more goal-directed AI agents, which is a valuable contribution to the state of AI safety and ethical considerations of AI.
2. **Ablation Study**: The ablation study does a good job at trying to isolate the components of the task and identify the most challenging aspects.

### Weaknesses
1. **Coherence of the metric and its goal**: My main issue with this paper is that the connection between the "goal-directedness" deficit and the actual metric that is introduced is not completely clear. More especifically, the authors state that they want to differentiate between two subtle cases: wether the model fails because it lacks the $\textit{capabilities}$ or the $\textit{motivation}$ to do the task. By definition,  $\text{goal-directedness-deficit(regret, capabilities)} = \mathbb{E}[\text{reward} | \text{optimal use of capabilities}] − \text{reward}$. This makes the assumption that the goal, namely stacking the blocks so as to minimize the height difference between two towers, is a task that is within the capabilities of LLMs. And this is likely to be false, as LLMs have been shown to be unable to perform well in seemingly simple tasks that require quantitative reasoning, e.g. reverse alphabetical sorting of words, even with chain of thought [1]. Therefore the metric fails to stablish the distinction on wether the evaluated LLMs fail because they lack capabilities or the motivation to do the task.

2. **Experimental rigor**: For all of the results plots it is not stated the number of evaluation seeds and the standard deviation of the  sample, making it impossible for the reviewers to make an assessment about the statistical properties of the result and validate some of the authors' claims (e.g. in line 412 the at"perhaps a statistical fluke"). More importantly, the authors derive their conclusions from a small number of datapoints (evaluation with only 3,4 and 5 blocks) and a single environment. Ideally a good benchmark should be able to show that the results might generalize to more complex scenarios, by showing results in a diversity of low complexity scenarios.
3. **Clarity**: Although the motivation is good, it was very difficult for me to understand what it was originally because some of its key ideas fail to be highlihted and reiterated (e.g. the importance of "goal-directedness" for safety and the distinction between "goal-directedness" and other reasoning tasks).

### Questions
1. What was the reasoning for using a BlocksWorld environment as an indicator of "goal-directedness"? 
2. Did you consider other potential tasks?
3. What would constitute a good task for the purpose of measuring goal-directed behavior, i.e. what properties were you looking for?
4. Why not fine-tune a model to provide more insight about the difficulty of the task?

### Soundness
2

### Presentation
1

### Contribution
2
