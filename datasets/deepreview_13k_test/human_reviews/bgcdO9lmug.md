# RePrompt: Prompt Engineering for Large Language Models Agents through Reflection

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
In this past year, large language models (LLMs) have had remarkable success in domains outside the traditional natural language processing, and people are starting to explore the usage of LLMs in more general and close to application domains like code generation, travel planning, and robot controls. Connecting these LLMs with great capacity and external tools, people are building the so-called LLM agents, which are supposed to help people do all kinds of work in everyday life. In all these domains, the prompt to the LLMs has been shown to make a big difference in what the LLM would generate and thus affect the performance of the LLM agents. Therefore, automatic prompt engineering (APE) has become an important question for many researchers and users of LLMs. However, previous works in APE all rely on a final checker to evaluate the performance of the given prompt, which is hard to meet in the case of LLM agents where intermediate feedback is easier to get, and the final evaluation could be expensive, inaccurate, or even missing. In this paper, we propose a novel method, \textsc{RePrompt}, which does a ``gradient descent"-like approach to optimize the step-by-step instructions in the prompts given to LLM agents based on the chat history obtained from interactions and reflections with LLM agents. By leveraging intermediate feedback, \textsc{RePrompt} can optimize the prompt without the need for a final solution checker. We have used experiments in PDDL generation and travel planning to show that our method could generally improve the performance for different reasoning tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on the problem of prompt optimization for LLMs for tasks in which the final evaluation of the task performance is either difficult or not possible to access. The proposed method aims to optimize step-by-step instruction following prompts (i.e., chain-of-thought) by gathering feedback (either human or LLM-generated) on the intermediate steps in the LLM-generated response, summarizing the key points of feedback, and using an LLM to generate an updated prompt that incorporates the single most important point of feedback for that iteration of the method. This process repeats until some notion of convergence has been satisfied. The method, RePrompt, is experimentally evaluated on two tasks: (1) PDDL action precondition generation and (2) constraint-satisfying travel planning.

### Strengths
I think the paper identifies a challenging problem with prompt optimization for black-box LLMs. Many existing methods rely on task success signals to improve the associated prompt, but such a signal may be expensive or not available. Tackling the problem by utilizing feedback about the LLM's intermediate steps is a promising research direction.

### Weaknesses
There are several weaknesses of note. I first list the weaknesses, then provide a clear statement of my recommendation along with arguments that support the recommendation, concluding with some suggestions about how to change my decision. Finally, there are a few general comments that did not impact my review recommendation.

Weakness:
- The paper is rough to read, making it generally difficult to understand the points being made.
- The description of the method is difficult to follow and is not formalized mathematically or algorithmically.
- To the best of my understanding, several of the stated contributions are not novel and appear in existing work.

I recommend rejection primarily for the following reasons.

1. The paper is difficult to read, making it hard to follow both the description of the method and the experimental design. For example, PromptAgent is used as a baseline for the Travel Planner experiment, but it is not described at all. I do not enumerate all of the comprehension challenges here; it is generally pervasive. 

2. Several of the claimed contributions are not novel. Below, I go through these individually.

2A. The first claimed contributed is to propose using a "gradient-based"-like prompt optimization. First, if this is a key contribution, it is necessary to make explicit what the gradient analog is; is the idea that the feedback provides something like a semantic direction in which to step to improve the prompt? Second, there are several other works that propose an analogy to gradient-based optimization for black-box LLMs [1,2], one of which is cited in this paper.

2B. The second claimed contribution is a summarization-based method for providing specific feedback. There is existing work that also explicitly includes a summarizer over batches of feedback for prompt optimization [3].

2C. The third claimed contribution is that the method does not require a solution checker. It is unclear to me how this is different than ReAct and Reflexion, both of which are described in this paper.


[1] Yuksekgonul, Mert, et al. "TextGrad: Automatic" Differentiation" via Text." arXiv preprint arXiv:2406.07496 (2024).
[2] Pryzant, Reid, et al. "Automatic prompt optimization with" gradient descent" and beam search." arXiv preprint arXiv:2305.03495 (2023).
[3] Chen, Yongchao, et al. "Prompt optimization in multi-step tasks (promst): Integrating human feedback and preference alignment." arXiv preprint arXiv:2402.08702 (2024).

My recommendation is based on my understanding of the paper. As it stands, I think the main possible way my recommendation could be improved is if I have significantly misunderstood the method and contributions, which is entirely possible since I found the paper confusingly written and unclear. I would recommend that the authors significantly rework Section 3.2 by introducing unabiguous notation, providing a concrete example to walk through with their method that utilizes the new notation, and clearly identifying the novel steps that differentiate their approach from ReAct/Reflexion.


Additional Comments (these did not impact my recommendation):
- I recommend that the authors clearly explain what makes an LLM-based system agentic. This would fit well in the introduction.
- I think an algorithm block would be one good format to present the method that should significantly reduce ambiguity.
- PDDL is an acronym for Planning Domain Definition Language (the paper writes "Planning Definition and Domain Language).
- The subsections in Section 5 appear to be LaTex subsubsections.

### Questions
1. What are the conditions under which the updated prompt converges? In the steps on lines 209-219, does convergence mean that all proposed solutions are already included? Is the feedback empty? Clarifying how this iteration terminates is important.

2. Line 226 refers to manually encoded solutions in the optimizer. What are these common problems and why is it better to manually encode solutions rather than allow the method to address them?

3. Line 243 refers to in-context learning, which I think is the first and only place this is referenced. Further, line 293 refers to zero-shot generation. How is in-context learning actually used in the experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents REPROMPT - where the authors focus on leveraging intermediate feedback (which they claim to be more readily available then final evaluator). The idea is to obtain some potential solution (LLM generated) of a given problem with intermediate feedback. These (solution, feedback) are summarized to find a "batch level" fix that should be applied (an LLM takes this batch and generates the batch level fix), which is then added back to the original prompt & the iteration continues.

### Strengths
I like the idea of using intermediate feedback instead of depending upon just the final feedback. (Specifically, the batch level fix instead of per-instance fix).
The paper is well written and covers good relevant literature.

### Weaknesses
What are the situations where intermediate feedback is easily / readily available and can be as useful as having access to a final critic? 

The major weakness of this paper is : 
1. Choice of dataset : They choose only two datasets TravelPlanning & Guan et al to showcase their results. I would expect results on a larger number of datasets to establish the claims. 
2. The results on these datasets is not encouraging. Specifically, in Guan et al, the they only improve slightly on Household domain. Moreover, the Final pass rate on TravelPlanning domain doesn't move the needle by much as well. For instance, [recent work](https://arxiv.org/abs/2405.20625) uses a bank of critics (similar to intermediate feedback) and achieves over 20% final pass rate - compared to 3.89%. 

The results on the Travel planning domain highlights my concern as well, on the belief that intermediate feedback can replace a final critic. Dependance of these individual feedback pieces can be quite complex and the paper relies on "batch fix"  to identify it, which doesn't seem to be scalable / may require lots of iterations. For instance, in TravelPlanning changing attributes like budget, accomodation preferences etc. can impact host of other changes which would be harder to capture by just looking at the intermediate feedbacks. 

Finally, while I agree if we know the "impactiful parts" of the input, given a feedback we can update those impactful parts - this may not apply to the author's example in ReAct. For instance, some works highlight the futility of "thoughts" in ReAct style prompting and that several parts of the prompt can infact be ignored / used which are not aligned with how human's infer the prompt. Therefore, depending upon an LLM may not be robust in identifying these "impactful parts" and some explainable AI strategy maybe better suited.

Minor : 
Can the authors point me to details on their "summarizing team", how was the data collected from them (beyond high level description in the main paper) and study / IRB details.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an approach for automatic prompt engineering for cases where end evaluation may be expensive or infeasible, but it may be easier to get intermediate feedback on the generated prompts. The proposed approach works in a step-by-step manner which takes the chat history 'interactions' and `reflections' along with an internal LLM evaluation into consideration for improving the prompt at every step. The authors show experimental results on the PDDL file generation domain and the travel planning domain showing improvements on reduced total number of errors and increased success rate across the two domains, respectively.

### Strengths
1) The paper aims to approach an interesting problem of optimizing prompts for reasoning tasks where external evaluations are expensive/infeasible to get, making the prompt optimization step harder.
2) The proposed approach is well-explained with the help of an example in Section 1, which allows the readers to get a good understanding of the prompt optimization flow.
3) Section 5 consists of a detailed error analysis, which unfortunately is not seen in many LLM papers, and is therefore a very refreshing and useful component of the work in its current stage.

### Weaknesses
1) Novelty: One of the biggest concerns in the current version of the work are in the novelty/contribution of the claims. The authors state (specifically in line 102, along with other places in abstract and Introduction) that the proposed approach uses a `summarization-based' to improve the prompt at any given step. However, please note that this is indeed what the core idea of Reflexion [1] is, which suffers from its own drawbacks due to the dependence on ReAct for exemplar-query similarity as shown in [2]. It is hard to understand from the current text what the difference is, other than this work being an application of Reflexion for APE. It would be helpful if the authors can clearly highlight/elaborate on this claim, or present this work as being Reflexion's application for APE (which still seems to be novel, but needs to be said upfront if that is the case.)

2) Abuse of terminology: The authors use terms such as as 'gradient-based' and 'standard fine-tuning procedure in ML' and 'loss optimization', however, the approach does not seem to be fundamentally the same as these. If the authors intend to use these terms as an analogy for easier understanding of the readers, that needs to be made clear in the paper. Although, it still seems to be a very far-fetched and overused analogy throughout the paper. If the authors believe that the reviewer misunderstood the usage of these terms for the proposed approach, it will be really helpful to have a transparent explanation of how these terms make sense in the given context of APE, what is the gradient-based approach, what is the mathematical loss function used, etc.

3) Both PDDL generation and Travel Planning have sound verifiers/checkers, which is contrary to the author's claims and problem setting for the proposed approach. It will be helpful if the authors can provide evidence on why these verifiers are unavailable (due to a modified problem setting perhaps). In the current stage of the work, it does not seem that the paper's motivation is coherent with the experimental settings used. Additionally, the work done by [3] has far superior results than the baselines used in the work, and it would be useful to know why the authors did not use it as a baseline or perhaps not consider it as a reasonable baseline for this work.


[1] Shinn, Noah, et al. "Reflexion: Language agents with verbal reinforcement learning." Advances in Neural Information Processing Systems 36 (2024).
[2] Verma, Mudit, Siddhant Bhambri, and Subbarao Kambhampati. "On the Brittle Foundations of ReAct Prompting for Agentic Large Language Models." arXiv preprint arXiv:2405.13966 (2024).
[3] Gundawar, Atharva, et al. "Robust Planning with LLM-Modulo Framework: Case Study in Travel Planning." arXiv preprint arXiv:2405.20625 (2024).

### Questions
1) The entire motivation of the work rests on the fact that there are cases where final prompt evaluations may be expensive or infeasible. Could the authors provide examples of such problem settings and domains, and clearly explain why the respective evaluations are not easily available?
2) Line 312: what is meant by `train RePrompt'? What exactly is the training step and what is being learnt in this case?
3) Why are there no other APE methods used as baselines in the experimental setting?

### Soundness
2

### Presentation
2

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
This paper proposed a new method called RePrompt, a prompt optimization procedure specially tailored for planning domains. RePrompt combines Act procedure (a method used in previous literature to improve the reasoning by providing reflection step-by-step) and prompt optimization. 

RePrompt is evaluated on two task planning domains: PDDL Generation and Travel Planning. In PDDL Generation domain, RePrompt demonstrate reduced incorrect actions and errors compared to the original paper. In the Travel Planning domain, RePrompt is compared with Reflexion and PromptAgent with better success rates across all groups.

### Strengths
The performance improvement over the baselines are rather strong.

### Weaknesses
1. The method can be understood as an combination of ReAct and Automatic Prompt Optimization. However, it is not clear why the Act part that provides feedbacks during generation of the plan can improve the prompt optimization. Further ablation study is necessary, for example, optimizing prompts without Act and inferencing with/without Act in figure 1. 

2. The paper does not have any formulation or an algorithm box. Some descriptions are very vague and the references to some components are not consistent. For example, in figure 1, the work flow involves a LLM summarizer, but line 186 indicates using a summarization team. Also, line 182 mentions "focus point". This is very illy-defined. If it is emerged from a prompt, the author should explicitly show the prompt that instruct LLMs to label "focus point". More vague descriptions like "some interaction schemes with some kind of feedback provider" (line 179). Such process should be more precisely described with formulation and algorithm box. Right now, I don't believe the Methods Section is describing a method that is replicable and able to be applied to other domains by the community.

3. The difference with existing methods are not clear. For example, the reference to ProTeGi says "Compared to previous work in automatic prompt engineering, including APE (Zhou et al., 2023) and PROTEGI (Pryzant et al., 2023), we do a summarization over a batch, and we prevent the prompt optimization from overfitting on a single outlier data point." This reference is incorrect as ProTeGi also optimizes the prompt over a minibatch.

### Questions
1. I would appreciate a more clear presentation of the Method section. The author should clearly indicate the LLMs and human summarization team. Different LLMs should be referred to with consistent names with the prompt used prompt them acting their roles in the pipeline

2. The framework is designed for optimizing prompt for LLM agents, for example, those involve Act Procedure. Could author explain how the method is accommodated to LLM agent that involves multiple rounds generation and more than one LLMs? After I reading the method section, the Act part can be removed and the rest of the system is exactly the same as previously prompt optimization framework.

### Soundness
2

### Presentation
1

### Contribution
1
