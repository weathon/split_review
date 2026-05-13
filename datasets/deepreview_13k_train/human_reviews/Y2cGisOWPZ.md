# Towards Machine Theory of Mind with Large Language Model-Augmented Inverse Planning

- Decision: Reject
- Scores: 6, 5, 8, 5

## Abstract
We propose a hybrid approach to machine Theory of Mind (ToM) that uses large language models (LLMs) as a mechanism for generating hypotheses and likelihood functions with a Bayesian inverse planning model that computes posterior probabilities for an agent’s likely mental states given its actions. Bayesian inverse planning models can accurately predict human reasoning on a variety of ToM tasks, but these models are constrained in their ability to scale these predictions to scenarios with a large number of possible hypotheses and actions. Conversely, LLM-based approaches have recently demonstrated promise in solving ToM benchmarks, but can exhibit brittleness and failures on reasoning tasks even when they pass otherwise structurally identical versions. By combining these two methods, our approach leverages the strengths of each component, closely matching optimal results on a task inspired by prior inverse planning models and improving performance relative to models that utilize LLMs alone or with chain-of-thought prompting. We also exhibit the model’s potential to predict mental states on open-ended tasks, offering a promising direction for future development of ToM models and the creation of socially intelligent generative agent models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
* LAIP is an approach that uses LLMs as components of a cognitive model, specifically the bayesian inverse planning model that has explained human behavior in cognitive science theory of mind tasks
* LAIP uses LLMs to generate hypotheses and likelihood functions, then applies Bayesian inverse planning to compute posterior probabilities over an agent's mental states based on observed actions
* Experiments show that LAIP outperforms LLMs alone and chain-of-thought prompting on hand crafted tasks similar to the Food truck tasks from Baker et al. 
* The model also demonstrates some potential (albeit with limited envs) in predicting mental states in more open-ended tasks than Bayesian methods can practically handle, aiming to create socially intelligent generative agents

### Strengths
* Smart integration of LLMs with inverse planning—leverages the open-endedness of LLMs and the reasoning strengths of Bayesian models.
* Addresses limitations of both LLMs (brittleness, reasoning errors) and Bayesian models (scaling issues with hypothesis/action spaces).
* Experimental results are promising and cool to see them match Bayesian methods in posteriors
* Potential for application in developing socially intelligent agents and enhancing human-AI interaction

### Weaknesses
 * Limited baselines: the baselines in the paper do not reflect the current SOTA of these approaches. For Study 1
you should add few shot prompting, CoT, ReAct, Reflexion type baselines as well. Zero shot baseline is not a strong baseline
* Experiments seem narrow in scope—focused on the food truck type toy tasks from cognitive science. The true promise of the method is that it should be more scalable than bayesian methods yet a majority of the experiments were with environments that Bayesian methods could handle. The number of potential hypotheses are often small as well, simplifying the process of latent state inference to a multiple choice problem. It would be interesting to see the methods on open ended ToM inference or multiagent decision-making tasks or benchmarks. Needs testing in diverse, unpredictable environments
* Scalability and computational efficiency aren't thoroughly addressed—how does LAIP perform with more complex tasks?
* Figures, results, and what they are highlighting could be more clear. Especially for a broader ML audience that may not be familiar with these tasks. Figure 1 in particular is confusing

Minor: 
* Missing related work: Hypothetical Minds and ProAgent. Similarity to these approaches should be discussed

### Questions
How is posterior probability of a hypothesis computed with the LLMs? Can you make this clearer in the main text

What's the computational overhead of combining LLMs with Bayesian inverse planning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In Theory of Mind, many human reason prediction models struggled with the scalability of possible hypotheses and actions. The paper uses LLMs to generate hypotheses and likelihood functions to compute Bayesian inverse planning models. The combination of prior computation with Bayesian models and LLMs mitigates the brittleness often seen in LLM-only approaches.

Initially, the LLM generates a prior belief over possible hypotheses regarding the agent’s preferences. Then for each of the steps it observes the agent’s trajectories and generates reasoning about the agent’s likely choices given the state, and the likelihood of different possible actions correspondingly. LLM updates the posterior distribution over hypotheses after the agent acts. 

The experiments are performed on simple ToM tasks. The first experimental scenario is inferring preferred restaurants. There are three restaurants where the agent moves about 5 steps. The second scenario is inferring food preferences with actions on what food to choose. The two scenarios are about the same scale. The paper involves experiments with various kinds of common LLM models, and for each of the experiments LLM generates 20 hypotheses. The proposed method performed better than pure LLM and baselines.

### Strengths
The LLM effectively generates a wide range of hypotheses, significantly reducing the computational burden of hypothesis generation. It is also more reliable when combined with the Bayesian model so that the accuracy could be higher than using pure  LLM. LLMs like GPT-4o, which are strong in logical computation, can compute posterior distributions directly, further reducing computational costs. This saves lots of manpower and computation resources.

### Weaknesses
Although overall the approach is interesting, there are several weaknesses.

1) The benchmarks provided seem insufficient for a comprehensive evaluation. Currently the comparison has been made with LAIP(LLM computes posterior), LAIP (single LLM call), pure LLM, and a steadily updated model. They are the variation or downgraded versions of the proposed LAIP model. They are good baselines though.

2) The paper claims that the scalability issue is a big problem, and I fully agree. This is exponentially more difficult to calculate the bayesian probability when the state space gets a little larger. That hinders the development of inverse reinforcement learning from this certain direction. However, the paper’s chosen scenarios are simple enough that priors could almost be calculated manually, raising questions about scalability to more complex settings. It can hardly convince that LLM can help solve it as the task might not be too challenging for gpt4o.

3) The paper lacks an explanation for how smaller, less reliable LLMs consistently perform well under LAIP. The results shown in Figure 3 indicate that several small LLM models perform much better with LAIP, but there is no mechanism that ensures the models can still contribute.

### Questions
1. How is LAIP compared to sota approaches, or pure-math BIRL models? (Ramachandran 2007)
2. What are the computational and scalability limits of this approach in terms of state space and trajectory length?
3. Can you give analysis on how LLM can boost the small LLM models?
4. Figure 4 seems to be drifting, and would you please include its conclusion in the main text?
5. How do you ensure the dataset you generated is not biased, i.e. it is not your choice of distribution that affects the performance of LAIP?

Ramachandran, Deepak, and Eyal Amir. "Bayesian Inverse Reinforcement Learning." IJCAI. Vol. 7. 2007.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present an approach called LAIP (LLM-Augmented Inverse Planning) that leverages large language models for Bayesian inverse planning over unconstrained action spaces (i.e. strings of natural language). LAIP prompts an LLM to generate various hypotheses in natural language for a given environment, generates actions in natural language conditioned on a given state of the environment, and evaluates the likelihood of each action conditioned on each hypothesis. These generated actions are then compared with ground-truth actions taken by an agent in the environment, and the posterior distribution of hypotheses is calculated. The authors assess LAIP in two studies and compare various modified LAIP models with baselines including an optimal Bayesian inference model, also assessing LAIP's capabilities when using various SOTA LLMs including GPT models, LLaMA models, and Mixtral.

### Strengths
- The proposed approach is completely novel, to my knowledge, and faithfully integrates LLMs as tools for Bayesian inverse planning.
- The proposed approach is assessed in multiple clear studies and against multiple methodological variants (e.g. Single CoT), and using multiple SOTA LLMs as the engine for their approach.
- The prose is very easy to understand, arguments are well-motivated, the background literature is up to date.
- Results are compelling.

### Weaknesses
 - The paper could use some diagrams to better capture the intuition of inverse planning, perhaps by including an example of agent paths through the restaurant environment in Figure 1. Specifically, the current figure lacks a clear depiction of how an agent's actions relate to the environment and how these actions are interpreted within the inverse planning framework. A visual representation of a sample trajectory, including the agent's position, orientation, and the corresponding actions taken, would greatly enhance understanding. Furthermore, the figure should clarify the concept of visibility, perhaps by showing how the agent's view of the environment changes as it moves.
- The paper could use some diagrams to better capture the pipeline of different LAIP variations, or at least the main LAIP approach, including the main components of the pipeline (the LLM, the hypotheses, the generated actions, the true grounded actions, the true hypothesis) and how they are elicited. A flowchart or similar diagram would be beneficial to illustrate the flow of information and the interactions between the different components of the LAIP framework. This diagram should clearly show how the LLM is used to generate hypotheses and actions, how these generated actions are compared to the ground truth, and how the posterior distribution over hypotheses is updated. The different variants of LAIP, such as 'Single CoT', should also be clearly differentiated in this diagram.
- Some discussion about previous work in using likelihood estimates of strings of text generated by LLMs would be welcomed so that the reader can better contextualize how LLMs have been/can be used for such tasks. The paper should delve into how these likelihood estimates are obtained from LLMs, and what assumptions are made about the probability distributions over text. A discussion of the limitations of using LLM-generated likelihoods, such as potential biases or calibration issues, would also be valuable.
- While this is not exactly a weakness, I think there are some interesting philosophical questions about how LLMs are able to capture these kinds of causal relationships in strings of text that are worthy of discussion. Also questions about how a visually grounded VLM might behave differently than a text-only LLM. The paper should consider the implications of using LLMs to model causal relationships, particularly when these relationships are expressed in natural language. It would be interesting to explore whether the LLM is truly capturing causal relationships or merely identifying statistical correlations within the text. Furthermore, the potential differences in behavior between a text-only LLM and a visually grounded VLM in this context should be discussed, including how visual information might influence the model's understanding of the environment and agent behavior.

### Questions
No questions, interesting paper.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a hybrid approach to machine Theory of Mind (ToM) that leverages large language models (LLMs) to generate hypotheses and likelihood functions within a Bayesian inverse planning framework, which then computes posterior probabilities for an agent’s likely mental states based on its actions. This model is intended to improve upon LLMs alone, which can be unreliable in certain reasoning tasks, as well as traditional Bayesian models, which often struggle with complex scenarios. The combined model, termed LLM-Augmented Inverse Planning (LAIP), outperforms either approach independently. It accurately predicts mental states in the experiments, even when using smaller LLMs that typically struggle in these scenarios.

### Strengths
1. This paper introduces a hybrid model, called LLM-Augmented Inverse Planning (LAIP), that combines Bayesian inverse planning with large language models (LLMs). This approach enhances Theory of Mind (ToM) reasoning by using LLMs to generate a wider range of hypotheses and actions than traditional Bayesian methods typically allow.
2. The effectiveness of the LAIP model is tested in controlled experimental settings. By using a restricted action and hypothesis space, the study enables a direct, systematic comparison between LAIP’s predictions and those of a Bayes-optimal model, providing clear insights into the model's strengths and limitations in inferring agent beliefs and preferences. The authors provide a detailed analysis of the trajectories and correlations between the optimal model and LLMs.
3. LAIP also demonstrates adaptability in ambiguous scenarios by dynamically generating and updating multiple hypotheses and possible actions based on new cues. This feature allows the model to attribute mental states even in complex situations where intentions are unclear, supporting more flexible social reasoning.

### Weaknesses
1. The authors overlook the discussion and comparison of a closely related method presented in the paper "MMToM-QA: Multimodal Theory of Mind Question Answering." This work also employs language models for scalable Bayesian inverse planning, generating likelihoods of different actions under various hypotheses in a similar way. It also concludes that Bayesian inverse planning with smaller language models can outperform larger models, albeit on different tasks.

2. The authors may consider including additional baselines, such as Sim-ToM [2], SymbolicToM [3], along with similar methods like BIP-ALM [1] and LIMP [4]. These approaches have shown significant improvements in LLM reasoning on Theory of Mind benchmarks.

3. Although the experimental setup follows a classic design, it appears somewhat simplistic and limited. The proposed method aims to serve as a general approach to machine Theory of Mind, so it should be tested in more complex, real-life-like scenarios that involve inferring different human mental states (e.g., beliefs, goals, plans, desires). It would be beneficial if the authors tested their method on at least one additional ToM benchmark to further demonstrate its effectiveness.

### Questions
1. The Hypotheses 1 to 20 in the results and Figure 2 are not clearly introduced. Could you provide an explanation of how these were generated and what they represent?

2. Could you provide an error analysis of the proposed method (types of errors, accuracy of each component of the method) to help clarify its limitations?

### Soundness
3

### Presentation
3

### Contribution
2
