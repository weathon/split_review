# Flow of Reasoning: Training LLMs for Divergent Problem Solving with Minimal Examples

- Decision: Reject
- Scores: 8, 5, 5, 5

## Abstract
The ability to generate diverse solutions to a given problem is a hallmark of human creativity. This divergent reasoning is also crucial for machines, enhancing their robustness and enabling them to assist humans in many applications such as scientific discovery. However, existing approaches to multi-step reasoning with large language models (LLMs) have mostly focused only on reasoning accuracy, without further discovering more diverse valid solutions. 
For example, supervised fine-tuning can improve LLM reasoning quality, but requires extensive supervised data to capture the full range of possible solutions. Reinforcement learning aims to find limited highest-reward solutions while neglecting the solution diversity. To fill this gap, we propose Flow of Reasoning (\textbf{\ours}), an efficient diversity-seeking LLM finetuning method aimed at improving reasoning quality and diversity with minimal data.
\ours formulates multi-step LLM reasoning as a 
Markovian {\it flow} on a DAG-structured reasoning graph. This formulation allows us to incorporate and adapt principled GFlowNet approaches, for finetuning LLMs to sample diverse reasoning paths with probabilities {\it proportional} to the (unnormalized) reward of target problems. Extensive experiments show that, with limited training examples (e.g., 15 examples), \ours enables the discovery of diverse, creative, high-quality solutions, greatly outperforming a wide range of existing inference and training methods across five challenging puzzle-solving tasks, including BlocksWorld (embodied reasoning), Game24 (math puzzle solving), Rubik's Cube (spatial reasoning), 1D-ARC (abstraction reasoning), and PrOntoQA (logical reasoning).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents Flow of Reasoning (FoR), a novel fine-tuning approach for LLMs that aims to enhance solution diversity. FoR frames the reasoning process as a Markovian flow, sampling diverse reasoning paths with probabilities aligned to the reward associated with each target problem similar to GFlowNet. Extensive experiments across multiple domains and baselines demonstrate that the proposed approach helps LLMs discover more diverse and higher-quality answers, showcasing the effectiveness of the algorithm.

### Strengths
1. The paper addresses the important challenge of encouraging diverse reasoning paths, a key problem in advancing LLMs’ capability for creative and robust problem-solving.
2. The experimental setup is solid, with evaluations across a wide range of domains and baseline models. Additionally, the comprehensive ablation studies effectively demonstrate the effectiveness of the design choices.
3. Strong performance is demonstrated, with the proposed approach outperforming state-of-the-art methods, including both prompt-based and fine-tuned models. In some tasks, the method even achieves results comparable to the advanced o1 reasoning model, despite using a significantly smaller Llama 3 model.

### Weaknesses
### The Presentation of the Paper Can Be Improved

- The motivation of the method is not clear enough. While the authors emphasize formulating the problem as a Markovian flow and sampling reasoning paths proportionally to rewards by drawing from GFlowNets, it is not clear why these specific elements are essential or expected to be effective in addressing the problem of diverse reasoning paths. The paper does not adequately explain why a Markovian flow structure, with its inherent assumption of state transitions depending only on the previous state, is a suitable framework for capturing the complexities of diverse reasoning. Furthermore, the connection between GFlowNets' ability to sample proportionally to rewards and the goal of achieving diverse reasoning paths is not sufficiently motivated, leaving the reader to question the fundamental rationale behind this approach.
- The authors could consider presenting the motivation and broader rationale behind key design choices before delving into technical and mathematical specifics. For instance, Section 3.2 is challenging to follow without a detailed explanation of why and how choices like the trajectory balance approach, log-variance approximation, or local search are adopted. It would also be helpful to clarify the reasoning behind Equations (5) and (7) and the role of local search within the approach. The paper lacks a clear explanation of why trajectory balance is preferred over other objectives, such as detailed balance, and why the log-variance approximation is a suitable substitute for the computationally expensive estimation of the partition function. The specific mechanism of the local search algorithm and its interaction with the overall training process also require further clarification.
- While the empirical results are impressive, the paper would benefit from additional analysis to strengthen its scientific arguments. For example, a case study illustrating the diverse reasoning paths generated by FoR, which other methods fail to find, would be informative. Additionally, a discussion on why FoR achieves such high performance while focusing on diversity would be valuable, especially considering that in most experiments, it outperforms baselines that emphasize mostly reasoning path quality. It would also be interesting to analyze how diverse reasoning paths may contribute to FoR’s effectiveness in out-of-distribution tasks.

### Limitations of the Markov Assumption and Markovian Flow Setup

The core setup of the algorithm relies on Markov assumptions and a Markovian flow structure, which are suitable only for domains that can accommodate state/action flows under these constraints. However, many complex real-world reasoning tasks do not necessarily align with the Markov assumption, having significant partial observability challenges or making it challenging to define clear “state” and “action” flows. More discussions of these limitations would help readers better understand the specific types of domains where the proposed method is most applicable and where it may face constraints. The paper should delve deeper into the implications of the Markov assumption, particularly in scenarios where the reasoning process is not strictly sequential or where past states significantly influence future actions beyond the immediate previous step. The discussion should also address how the method would handle situations with partial observability, where the full state of the reasoning process is not available at each step.

### Challenges of Hard Exploration and Sparse Rewards

The method’s core approach—sampling reasoning paths proportionally to rewards—faces inherent challenges in many real-world decision-making problems, where exploration is difficult, and rewards are sparse. In scenarios where only a binary success/failure reward is available, for example, the proposed method may converge toward behavior similar to traditional reinforcement learning, as it becomes difficult to maintain diverse reasoning paths with limited reward signals. The paper should discuss how the method would perform in environments with sparse rewards, such as those where only a final success or failure signal is provided. The authors should also consider the potential for the method to get stuck in local optima when rewards are sparse, and how this might affect the diversity of the generated reasoning paths. A more detailed analysis of how the method’s exploration strategy interacts with the reward structure is needed to understand its robustness in different reward environments.

### See other questions below. Some of those questions may be worth discussing.

### Questions
1. Why does only the Game of 24 domain use a different model?
1. Could the authors clarify which components are borrowed from existing works and which are newly proposed in this method? Many core components (sampling proportional to rewards, trajectory balance objective, adaptive efficient exploration) seem to be derived from existing approaches.
1. Could the authors clarify the usage of examples in the test dataset? Is it used for few-shot prompting during inference, or is it only used for calculating creativity metrics?
1. In Line 301, what is the value of N for each domain? The choice of N seems to not be specified for domains like Blocks World or Game of 24.
1. While it's clear that each fine-tuning method shares the same offline dataset, has the size of the online dataset also been controlled across methods?
1. The proposed method seems to not include search during inference. Why then is its runtime significantly higher than other COT/SFT methods that also do not include search?
1. For baseline evaluation, do the prompts explicitly include keywords to encourage diverse responses? If not, this could be worth investigating.

### Soundness
4

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Paper proposed a new approach for generating diverse reasoning traces using GFlowNets.

### Strengths
- Paper is organized cleanly and easy to understanding
- Experiments involve a variety of tasks and baselines
- Approach shows improvements to accuracy and diversity of model generations

### Weaknesses
Although a variety of tasks were evaluated, all of the tasks are relatively structured and uses constrained action spaced (such as STACK, UNSTACK, PUT, PICKUP in BlocksWorld). In contrast, reasoning tasks that are useful to real users are typically much more open ended, with a more diverse variety of both questions and potential answer formats. In order to show that the proposed approach is scalable to these more open ended reasoning tasks, it would be great to also evaluate on benchmarks like MATH or GSM8k.

The proposed approach requires a reward function, which, in the experiments, required different kinds of reward shaping for each task. Designing specialized reward functions for each task is not practical when training general-purpose LLMs on a wide range of different tasks. It would be great to either show that the proposed approach leads to improvements in accuracy and diversity with just the sparse "success" reward, or use a shaped reward that can work with all tasks. 

It would be great to show qualitative examples of the different responses generated by each approach, and highlight how they differ from standard approaches

### Questions
See weaknesses

### Soundness
3

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
This paper proposes Flow of Reasoning (FOR), a data-efficient finetuning method that enables large language models (LLMs) to generate diverse, high-quality solutions for multi-step reasoning tasks. Unlike existing methods that prioritize accuracy or highest-reward solutions, FOR promotes solution diversity by modeling reasoning as a Markovian flow on a directed acyclic graph (DAG), applying principles from Generative Flow Networks (GFlowNets) to sample multiple reasoning paths based on reward. With minimal data requirements (around 15 examples), FOR significantly outperforms traditional approaches across five complex puzzle-solving tasks, demonstrating its effectiveness in improving both reasoning quality and diversity.

### Strengths
The paper effectively addresses a gap in existing LLM approaches by focusing on solution diversity in multi-step reasoning tasks, which enhances robustness and creativity in applications like scientific discovery. 

The FOR framework introduces a unique approach by modeling multi-step reasoning as a Markovian flow on a directed acyclic graph (DAG), using Generative Flow Networks (GFlowNets) principles. This higher-level, step-based approach enables more efficient sampling of diverse reasoning paths, distinguishing FOR from traditional token-level models.

FOR demonstrates impressive data efficiency, requiring only about 15 training examples to achieve competitive results. This efficiency makes the method more feasible for practical applications where extensive labeled data is limited.

Through comprehensive testing across five complex tasks (embodied reasoning, logical reasoning, spatial reasoning, etc.), FOR outperforms multiple baselines by 20%–85%, showing versatility and robustness across different reasoning challenges.

### Weaknesses
The primary issue I find with this paper is the lack of clarity regarding any original insights or core observations the authors provide about large language models in the context of reasoning with diversity. Throughout the paper, it seems that all key observations, points, and techniques are primarily derived from existing works, without presenting novel contributions from the authors. For example, the authors note that existing LLMs focus on generating the reasoning path with the highest reward. However, LLMs inherently exhibit randomness and uncertainty in their reasoning processes, which could naturally encourage exploration across diverse reasoning paths. In additional papers, such as TR [1] and CR [2], they all build a DAG toward getting solutions.

The second issue is that there are plenty of high-level ideas and "big words" in the explanation parts of the paper. For instance, in Line 172, what does "As discussed in §1, to generate diverse, high-quality reasoning trajectories for solving a task, we want to sample the trajectories with probabilities proportional to the reward. " Why sampling in such a way can generate not only diverse but also high-quality reasoning paths? What is the logic between this strong conclusion and its previous and subsequent sentences?

The third issue is that this paper introduces too many existing methods, ideas, equations, and conclusions from prior works. However, the way the authors organize these elements does not integrate them effectively, resulting in a lack of clear and logical explanations to support an understanding of their own contribution. While reading the paper, I found the frequent citations, numerous "See appendix" references, and lack of important insights to be distracting and disruptive to my understanding. For example, the authors do not provide clear or consistent notation descriptions. It appears that notations are created on the spot whenever needed, leading to confusion and a lack of coherence throughout the paper.

The fourth issue is that some of the questions posed in the paper are unclear, leading to confusion about their intent and relevance. For example, (1), in Line 188, why the distribution directly equals to F(\tau)/Z? To me, this should be an approximation.; (2), in Line 191, where is the P(s_0) that is the prior in this step-wise distribution? (3). in Line 202, when F is defined for the state flow, it's unclear why F(s_n) is to be equal to R. 

The final issue is that the experiment section does not provide sufficient persuasiveness for the paper. For example, if the goal of this paper is to fine-tune the LLM to generate diverse reasoning paths, the main content should provide a more specific and detailed explanation of how to fine-tune LLMs according to the proposed objectives. Besides, how the authors define diversity is unclear to me. They may need to count successful trajectories a policy finds for the successful example. But how the two trajectories can be compared when there are many ones? Thus, during training, how can you ensure that the LLM can generate two different paths from one state? How about comparing your methods with other similar (using DAG) methods [1, 2]?

I was not impressed by the optimal results in the table due to the lack of sufficient explanation, in-depth analysis, and insights in the paper.

### Questions
See Weaknesses Above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces FOR, a novel method designed to enhance the divergent reasoning capabilities of LLMs. FOR addresses the challenge of generating diverse solutions to complex problems by formulating multi-step reasoning as a Markovian flow on a DAG structured reasoning graph. This approach allows the incorporation of GFlowNet techniques to train LLMs to sample diverse and high-quality reasoning paths proportional to the unnormalized reward of target problems. The paper demonstrates FOR's effectiveness across five diverse reasoning tasks, showing significant improvements in discovering creative and high-quality solutions with minimal training data compared to existing methods.

### Strengths
- well-written and easy to follow
- The idea of GFlowNet is quite interesting

### Weaknesses
I believe this is an interesting piece of work with a highly valuable topic. However, I think the benchmarks considered in this paper, such as Game24, PrOntoQA, Rubik's Cube, etc., do not actually require much divergent thinking. I strongly recommend directly considering some works on lateral thinking [1][2][3] to assess whether the proposed methods are truly effective. I understand that it might not be possible to fully attempt these benchmarks during the rebuttal stage, but it could be possible to try some examples or add a related works section for lateral thinking or creativity.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3
