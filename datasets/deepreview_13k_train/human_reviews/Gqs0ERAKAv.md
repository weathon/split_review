# Filling the Gaps: LLMs for Causal Hypothesis Generation

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Scientific discovery is a catalyst for human intellectual advances, driven by the cycle of hypothesis generation, experimental design, data evaluation, and iterative assumption refinement. This process, while crucial, is expensive and heavily dependent on the domain knowledge of scientists to generate hypotheses and navigate the scientific cycle. Central to this is causality, the ability to establish the relationship between the cause and the effect. Motivated by the scientific discovery process, in this work, we formulate a novel task where the input is a partial causal graph with missing variables, and the output is a hypothesis about the missing variables to complete the partial graph. We design a benchmark with varying difficulty levels and knowledge assumptions about the causal graph. With the growing interest in using Large Language Models (LLMs) to assist in scientific discovery, we benchmark open-source and closed models on our testbed. We show the strong ability of LLMs to hypothesize the mediation variables between a cause and its effect. In contrast, they underperform in hypothesizing the cause and effect variables themselves. We also observe surprising results where some of the open-source models outperform the closed GPT-4 model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new task of using large language models (LLMs) to propose new causal hypotheses for scientific discovery. To this end, the paper proposes a benchmark dataset based on existing causal graphs to create four tasks to prompt the LLM to identify related variables in causal hypotheses. Various language models are benchmarked on this dataset. The paper shows that LLMs can perform well in some easier tasks but not as much in more challenging open-world settings.

### Strengths
* originality: the paper proposed an interesting task that demonstrates how well LLMs may do in generating causal hypotheses.
* quality: the proposed tasks are defined with various metrics that help to automatically assess the performance of the LLMs. the proposed tasks also seem reasonable to me. the proposed dataset is applied to various LLMs. Finetuning experiments and chain of thoughts are used in benchmarking the models.
* clarity: The presentation of the paper is clear.
* significance: the proposed task is orthogonal to other aspects of causality such as casual discovery.

### Weaknesses
While the paper proposed an interesting task to generate causal hypotheses, it is not clear to me what might be the real-world utility of the proposed task beyond the evaluation with existing causal graphs. The paper will be more convincing if the author can demonstrate additional empirical benefits of the proposed task (i.e. using LLMs to generate causal hypotheses) beyond the curated causal graphs.

### Questions
Does few-shot learning help improve the performance of LLMs?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel benchmark designed to evaluate the ability of LLMs to hypothesize missing variables in causal directed acyclic graphs (DAGs). Motivated by the scientific discovery process, the objective is to simulate the generation of hypotheses in partially complete causal graphs, where LLMs hypothesize about missing nodes, particularly mediators, causes, and effects. The benchmark’s results indicate that LLMs do well at hypothesizing mediating variables between causes and effects, however, they struggle with hypothesizing direct causes and effects.

### Strengths
1. The paper presents a novel use of LLMs in scientific discovery by applying them to generate hypotheses through predicting causal variables in partially incomplete causal DAGs. 

2. It provides a comprehensive evaluation of how various LLMs perform in predicting missing causal variables across different levels of difficulty. The benchmark assesses both open-source and proprietary LLMs, using diverse causal DAGs from multiple domains.  

3. Given the recent focus on LLMs in scientific contexts, the benchmark is highly relevant. By introducing this task, the paper makes a valuable contribution to the community’s understanding of LLMs in scientific discovery, potentially inspiring future research to enhance LLMs’ causal reasoning abilities.

### Weaknesses
1. The paper could be clearer, especially in the methodology section, which does not adequately motivate each task or present them naturally. The tasks became clearer only upon reading the evaluation.  

2. There is a risk of data leakage in most of the datasets used. While the authors attempt to address this limitation by presenting the causal graphs to the LLMs in a novel way if the LLMs were trained on the datasets, the underlying causal patterns could be memorized, and the benchmark’s validity could be compromised. This raises the need for further analysis to determine whether LLMs are genuinely performing causal reasoning or merely memorizing causal patterns. 

3. The assumption that all causal relationships are known and correct may be unrealistic in practical applications. For example, it may be improbable to know the inbound and outbound edges of a mediator variable without knowing the variable itself. This restrictive assumption limits the benchmark’s ability to fully assess LLMs’ causal reasoning.

### Questions
1. In the paper, you argue that Task 3 represents a realistic scenario where the LLM must complete partial causal DAGs in an open-ended manner. While this setting makes it practical for a scalable benchmarking framework, is it actually realistic for users to create partially complete causal DAGs where the edges are known and correct? If all causal variables are not known, then is it practical to say the users can provide such a graph? 

2. Is there a difference between Tables 3 and 11 reported in the paper? Both look almost the same. Additionally, can you clarify the metric ∆, since the captions in Tables 3 and 11 describe ∆ differently than what is described in Section 5.5? Finally, can you please explain why ∆ is better than simply presenting the difference in performance when mediators are iteratively presented to the LLM in ascending and descending orders of significance? 

3. Section 4.2 is a bit unclear. Why are two variables removed, but the LLM is only required to predict one? Additionally, Figure 2b does not depict two variables being removed, so I am unsure why two are removed.

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
4

### Summary
Authors propose new tasks that focus on the discovery of potential unobserved variables in a partially defined causal graph, hypothesising the true complete causal graph with the help of LLMs. Authors validated their approach against multiple LLMs, with different "difficulty levels" and prior knowledge about the causal graph.

### Strengths
- The tasks analysed by this work are relevant in the context of causality, especially in the field of causal discovery, where the complexity of the model scales significantly.
- Multiple LLMs are tested, providing a wide range of potential evidence in favor of the proposed approach.

### Weaknesses
 - The multiple-choice question answering (MCQA) seems to be built beforehand, in such a way that the options are distant from the true one/ones w.r.t. the rest of the graph. This makes the evaluation easier.
- Sources/sinks are fundamentally different from mediators/confounders/colliders. The former expresses a property of the graph, while the latter expresses paths configurations. This makes the interpretation of the results unclear: I'm unsure if I should focus on the graph as a whole or in the paths of interest (if any).
- The evaluation is performed against "metrics" introduced by the authors themselves (e.g. MIS), without providing any property of the said metrics, making it harder to understand the actual the outcome of the evaluation.

### Questions
- Are "missing" variables actually "unobserved" variables? If yes, what is the choice behind this naming? Otherwise, what are the differences between these two types of variables?
- In causality the term "identification" refers to the identification of the causal estimand, hence, "causal identification" is misleading. Would it be possible to avoid this confusing overlap in the paper?
- Are the vertices (capital) V1 different from the vertices v1? Is this just a typo? Otherwise, what are the differences between these two types of vertices?
- Why Natural Direct Effect (NDE) and the Natural Indirect Effect (NIE) are taken as reference "metrics" for tasks evaluation?
- How are the NDE and NIE identified? The term "identified" here refers to the identification of the causal estimand, required for estimation of NDE/NIE.
- Why is Mediation Influence Score (MIS) a relevant metric in this context? How can we interpret it? What are the properties of such metric? Is it a metric at all? NIE and NDE are signed values, how to deal with sign reversal here?
- Can the authors provide a formal definition of "out-of-context distractors"? What is the difference between "in-context" and "out-of-context" choices? Aren't the names of the variables enough to provide context to the LLM? How is the context modeled?
- Authors say that: "The role of the LLM is to select a variable from the multiple choices". Apart from the true variable/variables in the list, how are the other multiple choices generated in the first place? In the appendix it is written that: "The words were randomly chosen to be far enough from the nodes", what does it mean "far enough"? Does this make the identification easier? What if we have variables that are indeed close to the true one/ones?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The goal of this paper is to provide a benchmark for hypothesizing missing variables from a causal graph.

The paper designs progressively challenging scenarios
- partially known causal DAGs and a set of multiple choices for the missing variables.
- removing more than one node from the graph.
- hypothesize the missing variables of the causal DAGs without any explicit hints.

It formulates four tasks and has intensive experiments.

### Strengths
- This paper discusses an important and timely question. Making hypotheses on the missing causal variables is crucial to the scientific discovery process. A good benchmark is definitely needed. 
- This paper provides clear definitions of its four tasks, like how each task is constructed and related.
- It conducts solid experiments with seven LLMs and multiple datasets. Code is provided in an anonymous repo.

### Weaknesses
The datasets used may already be included in the training corpus. The authors claim that the Alzheimer’s Disease dataset is new, and they cite an ICLR 2024 paper [1]. However, in section 4 (page 5) of [1], it is stated that the ground truth of Alzheimer’s Disease is discussed in [2] and [3], which are much earlier papers.



Minors:
- Some notations should be revised, like ⊮in line 320.

### Questions
My main concern is the usage of the datasets. See the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2
