# Model Swarms: Collaborative Search to Adapt LLM Experts via Swarm Intelligence

- Decision: Reject
- Scores: 5, 6, 8, 8

## Abstract
We propose Model Swarms, a collaborative search algorithm to adapt LLMs via swarm intelligence, the collective behavior guiding individual systems. Specifically, Model Swarms starts with a pool of LLM experts and a utility function. Guided by the best-found checkpoints across models, diverse LLM experts collaboratively move in the weight space and optimize a utility function representing model adaptation objectives. Compared to existing model composition approaches, Model Swarms offers tuning-free model adaptation, works in low-data regimes with as few as 200 examples, and does not require assumptions about specific experts in the swarm or how they should be composed. Extensive experiments demonstrate that Model Swarms could flexibly adapt LLM experts to a single task, multi-task domains, reward models, as well as diverse human interests, improving over 12 model composition baselines by up to 21.0% across tasks and contexts. Further analysis reveals that LLM experts discover previously unseen capabilities in initial checkpoints and that Model Swarms enable the weak-to-strong transition of experts through the collaborative search process.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a collaborative search algorithm that uses swarm intelligence to adapt LLMs.  The method proposed starts with different LLM experts and a utility function; collaboratively the LLMs experts optimize the utility function. Each expert is a particle in the swarm. It has a location that depends on the model weights, a velocity which is the direction where it should move next, the personal best found location, and the global best and worst location over the entire history.  The population is initialized using crossover, the velocity is updated as a weighted average of the current velocity, personal best, global best, and global worst.  Weights and locations are updated in steps. The length of the steps is reduced over time until convergence. The results are compared with baselines for different ways of doing the composition (trivial, static, dynamic) on multiple datasets. The examples shown in the paper work in multiple cases, i.e., for a single task, multi-tasks, reward models, and different human interests.  The results overall are good.

### Strengths
The method proposed is training free and can be used with a small number of examples.

It is interesting to see how the collaboration of week models can outperform strong models.

The experimental results presented are overall positive, showing the method is a promising approach over a large variety of domains.

### Weaknesses
There are no examples in the paper of the kind of text the LLMs experts produce. There are detailed examples in the appendix but showing an example would have gone a long way in helping the readers understand the significance of the work.

The method proposed is a variation on Particle Swarm Optimization and Genetic Algorithms, so the innovation seem limited to apply those methods to LLMs.

The paper is not an easy read. The tables are dense, there are a lot of charts, but since no examples have been included, they feel too abstract. Some tables are not in numerical order, and they are presented with limited explanations.

### Questions
Can you explain what changes done compared to the PSO and GA algorithms are the most useful to achieve the results obtained?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents MODEL SWARMS, a collaborative search algorithm that adapts various Large Language Models (LLMs) for multiple applications. This method employs the best checkpoints as guides to optimize utility functions for different objectives, utilizing the concept of evolutionary games. Extensive testing demonstrated that MODEL SWARMS enhances performance by up to 21.0% compared to twelve conventional model composition baselines in four adaptation scenarios. Notably, this model does not require fine-tuning or presuppose the existence of expert models.

### Strengths
1. The concept is straightforward and the writing is clear and easy to comprehend.
2. This model operates without the need for fine-tuning and does not depend on already established expert models.
3. The performance appears to be quite strong relative to existing approaches.

### Weaknesses
1. Why did you choose Particle Swarm Optimization (PSO) for your model instead of other evolutionary algorithms such as Ant Colony Optimization (ACO) or Genetic Algorithms? Could you discuss the benefits of using PSO compared to these other common evolutionary game theory (EGT) strategies in your context?

2. Evolutionary Game Theory (EGT) is often criticized for its lengthy and unstable search times, as well as the significant computational resources required. Could you provide details on the computational time associated with your design?

### Questions
see Weaknesses

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
4

### Summary
The paper introduces MODEL SWARMS, a collaborative search algorithm for adapting Large Language Models through swarm intelligence. The approach involves a pool of LLM experts that collectively optimize a utility function by adjusting in the weight space, guided by checkpoints from the most successful models. MODEL SWARMS offers tuning-free model adaptation and is designed to operate effectively even with minimal data (as few as 200 examples). The method is evaluated across various domains, showing improvements of up to 21.0% over 12 model composition baselines.

### Strengths
The proposed method is well-founded and practical, with wide applicability across diverse adaptation scenarios, from single-task to multi-task learning, as well as reward modeling and aligning with varied human interests. 

This work is likely to inspire new directions in LLM research, providing valuable insights into adaptive model composition. 

The paper is well-organized and clear, with a logical flow and thorough experimental design, making the findings compelling and easy to follow. 

The experiments are comprehensive and detailed, offering a robust evaluation across various tasks and contexts.

### Weaknesses
No major faults were identified.

### Questions
Can this approach extend to decision-making tasks? Decision-making often requires the learning of a return or value function, which might pose challenges for stability in the search process. It would be insightful to understand how MODEL SWARMS handles stability and reliability under these conditions. 

Would larger LLMs make the search more difficult as the parameter size increases?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explores swarm intelligence to guide LLM weight updates of a set of expert LLMs. In this work, a given set of LLMs are distributed in "weight-space" with randomized velocity and location (inspired by particle swarms). The algorithm updates the LLM particles such that local and global (collective) locations are considered to find new optimal locations, that is, model weights. Optimal locations are evaluated by benchmarking across various tasks from literature, as well as model composition/ensembling methods as baselines.

### Strengths
- Novel way of utilizing swarm intelligence (particles) to update weights of a given set of LLMs (experts)
- Very well presented in terms of language, explanations, and figures, but also evidence of why and how this works
- Extensive experimentation and very well-suited benchmarks/baselines
- Especially interesting experiments on the emergence of new skills, "Correctness Emergence", as well as the diversity of LLM sets ("Diversity Matters")

### Weaknesses
 - I could not find evidence on how weights are mapped to the weight/location space. Please provide detailed explanation of how model weights are represented in the weight/location space, including any techniques used for dimensionality reduction or embedding if applicable.
- In line 110, there is a first mention of a utility function, but at this point, I think this should have been explained already. I would suggest to introduce and explain the utility function earlier in the paper, as it's a key concept for understanding the method. This would improve the paper's overall clarity and flow.
- line 154, I think it would be important to explain how to prevent experts that are best (globally) from being drawn to their own "best" initial location and how the random factor helps to explore. Please elaborate on how this issues is addressed, specifically detailing how the random factors in your method help prevent getting stuck in local optima and encourage exploration.
- line 258 - it might make sense to bring in SOTA numbers from non-composition LLMs
- line 318 - "in LLM-as-a-judge"
Here, I think we need more details on the prompts, etc. as there is evidence that LLM as a judge evaluation methods can be gamed easily. Could you provide more detail about the prompt and evaluation process? Perhaps discussing how you mitigate potential biases or gaming of this evaluation method.
- line 367
"Averaged across the four datasets, we found that only 10.4% of the ending-best particles also started as the best (#1), while surprisingly, the bottom half of the starting experts were able to rise to the top in 56.9% of the MODEL SWARMS searches."
This would be a good opportunity to further discuss the importance of the "global" values in the utility function, especially in the early iterations.

### Questions
- Paragraph following line 67 -  This should be explained at a high level at this point:
What does velocity map to?
What does "best found location" map to?
Why is it important to be in a "best" neighbourhood, and what does "best" refer to?
I suggest providing a high-level explanation of these concepts early in the paper, as this would help readers better understand the method.
- List following line 77
Is this the same model pool? Or for each point in the list of different pools?
- line 104
"location represented by model weights;" - Why are we not talking specifically about the weights being in an embedding space (locations) -  assuming this is the case? Otherwise, one would wonder how the weights can purely be taken from different size/architecture type models and mapped to the same space. 
- line 171
"Since MODEL SWARMS explicitly encourage randomness and exploration," - how? This could be picked up briefly, here again, to circle back. "repeating" this here solidifies the idea

### Soundness
4

### Presentation
4

### Contribution
4
