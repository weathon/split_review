# Active Task Disambiguation with LLMs

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Despite the impressive performance of large language models (LLMs) across various benchmarks, their ability to address ambiguously specified problems—frequent in real-world interactions—remains underexplored. To address this gap, we introduce a formal definition of task ambiguity and frame the problem of task disambiguation through the lens of Bayesian Experimental Design. By posing clarifying questions, LLM agents can acquire additional task specifications, progressively narrowing the space of viable solutions and reducing the risk of generating unsatisfactory outputs. Yet, generating effective clarifying questions requires LLM agents to engage in a form of meta-cognitive reasoning, an ability LLMs may presently lack. Our proposed approach of active task disambiguation enables LLM agents to generate targeted questions maximizing the information gain. Effectively, this approach shifts the load from implicit to explicit reasoning about the space of viable solutions. Empirical results demonstrate that this form of question selection leads to more effective task disambiguation in comparison to approaches relying on reasoning solely within the space of questions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the question/user intent disambiguation problem for LLM agents. When the initial query do not provide enough information for LLM agent to solve the task, the agent should actively ask user questions to better clarify the task to solve. This paper proposed a method that can select the best clarification question at every turn. In particular, the method first samples a set of possible answers based on the existing information, and a set of possible clarification questions, then the question is selected based on the EIG score (expected information gain). The question along with its answer is added to the problem context for the next round of prompting. This execution loop can repeat for a few iterations until reaching a final answer. The authors evaluated the proposed method on two datasets, 1) 20-question games about animal names and 2) HumanEval coding tasks. The results suggest that the propose method of selecting clarification questions leads to better ovrall results than vanilla zero-shot question generation.

### Strengths
1. The formulation of EIG scores for selecting the best clarification question is well designed.  Intuitively, the question that brings maximum information gain will narrow down the possible search space the most,  but how to prompt the model to generate the most informative question is challenging. The authors did a nice work by shifting the question generation problem to a question selection problem, which leverages LLM’s reasoning ability and potentially external tools that provides more accurate signals for the selection. 

2. The proposed method of generating/selecting best clarification questions can have wide application to different tasks. For example, in many real-world applications where LLM agents can be deployed, e.g. travel agent or coding agent, the user queries can be ambiguous and miss critical information. The proposed method can potentially be applied to help the agent understand uesr intent in fewer turns and thus complete tasks more efficiently.

### Weaknesses
The benchmarks used in this paper are too simple. For example the 20-question games only require guessing animal names, and it is designed for asking clarification questions. For HumanEval, it also contains mostly simple coding problems. It would be better if we can see results from more challenging agent benchmarks such as SWE-bench.

### Questions
1. For the two benchmarks tested in this paper, the EIG scores can be easily computed since there are only single word answers or executable code. I’m wondering how would you compute the EIG scores when the answer set is arbitrarily large. For example, for free form response generation where all answers are unique, and each answer can be arbitrarily long?

2. There is a typo in Line 900

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper addresses task ambiguity, where the intended goal of the user is not clear/is underspecified. The proposed method seeks to reduce ambiguity by asking follow-up questions to the user that clarify their intent. The authors use LLMs to both perform tasks and generate questions, and implement an information-gain-based ranking method to obtain questions that best reduce uncertainty; the method is based on Bayesian Experiment Design, and tries to partition the space of possible solutions s.t. the partitions are maximally balanced. The method is tested on two tasks and three LLMs. First, the authors test on a 20-questions style game where the agent has to correctly guess an animal by asking questions about its properties. Here, their method results in a better ranking of the correct animal, and they show that their questions eliminate more possible alternatives than a baseline without information gain. The second domain is coding, where the authors show that their method is able to generate unit tests (which act as questions). Here, their unit tests generally result in improvements on HumanEval, both when unit tests are posed as true/false statements and when open-ended unit tests are permitted.

### Strengths
**Quality:** The work rigorously defines its problem and then offers a potential solution. The authors do a good job of illustrating that their method works/how it works on 20 questions, while still showing real-world results on a naturalistic dataset in a coding domain, where many users actually use LLMs on a daily basis. This is a major strength of the paper. The experiments themselves are generally clearly described and well-documented/well-executed. The authors also run across a large number of seeds and release code, making their approach more reproducible. 

**Significance:** Ambiguity and task ambiguity are increasingly important problems as more people use LLMs and AI systems. The authors make a strong case in the introduction for why ambiguity is important and the kinds of risks posed. The clarification-based approach they suggest has the potential to improve AI safety by reducing misunderstandings, and takes a human-centric approach to dealing with ambiguity.

**Originality:** The information-gain approach to dealing with ambiguity that is proposed here is novel, and the definition of task ambiguity in definition 1 is valuable.

**Clarity:** The paper is generally well-written and clear. I appreciated the colored boxes that provide additional detail/clarification. I found the formalizations made the paper more precise and were accessible. Several questions I had were preemptively addressed, e.g. on L509-511 where the authors point out that adding unit tests could provide other avenues for improvement beyond ambiguity. The figures (especially figure 2) nicely illustrate the problem and method.

### Weaknesses
 **Empirical gains vs. cost**: Looking at Fig. 3, it seems like the proposed method improves the rank by ~2 ranks at iteration 10 for GPT3.5 and ~1 for GPT-4o-mini. While these results are significant, I do wonder (especially given the smaller gain on GPT4o-mini) whether they track with the added computational cost of the method. It would be worth noting the cost (i.e. number of tokens, number of model calls) to be able to directly compare these methods, since some of the baselines like ToT also incur more computational cost. 

**Baseline clarity**: It's not completely clear what the ToT baseline is. Is this tree-of-thought? If so, it should be cited.

### Questions
Relevant references:
- https://arxiv.org/abs/1805.04655
- https://stokhof.org/wp-content/uploads/2020/09/groenendijk-stokhof_ssqpa.pdf 
- https://arxiv.org/abs/2004.10645
- https://arxiv.org/abs/2211.07516

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the challenge of large language models (LLMs) dealing with ambiguously specified problems, which is common in real-world interactions. The authors propose a Bayesian Experimental Design framework to tackle task disambiguation by having LLM agents ask clarifying questions to acquire additional task specifications. This approach requires meta-cognitive reasoning, which the authors argue LLMs currently lack. They introduce a method to generate targeted questions that maximize information gain, shifting the reasoning from implicit to explicit. Empirical results show this method leads to more effective task disambiguation compared to question-space reasoning approaches. The paper contributes by identifying the need for new reasoning methods, formalizing task ambiguity, proposing a BED-based strategy for question generation, and evaluating its effectiveness in interactive task elicitation scenarios.

### Strengths
* It introduces a novel method to handle ambiguity in task specifications by leveraging the principles of Bayesian Experimental Design, which is a significant advancement in the field of LLMs.
* The paper provides a clear and formal definition of task ambiguity, which is crucial for framing and addressing the problem within a mathematical and computational context.

### Weaknesses
 * Consider adding a concrete example of task ambiguity in the main text, rather than relegating it to supplementary materials. A practical example would help readers grasp this key concept more easily.
* Why just show the rank in Figure 3?

### Questions
* IG in Eq. (2) denotes information gain?
* What does $c(q)$ mean ? Does it mean cost of API usage (tokens) ? Please clarify it.

### Soundness
2

### Presentation
2

### Contribution
2
