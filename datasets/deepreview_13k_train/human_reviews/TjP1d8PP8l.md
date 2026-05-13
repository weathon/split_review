# Discriminator-Guided Embodied Planning for LLM Agent

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Large Language Models (LLMs) have showcased remarkable reasoning capabilities in various domains, yet face challenges in complex embodied tasks due to the need for a coherent long-term policy and context-sensitive environmental understanding. Previous work performed LLM refinement relying on outcome-supervised feedback, which can be costly and ineffective. In this work, we introduce a novel framework, Discriminator-Guided Action Optimization (DGAP), for facilitating the optimization of LLM action plans via step-wise signals. Specifically, we employ a limited set of demonstrations to enable the discriminator to learn a score function, which assesses the alignment between LLM-generated actions and the underlying optimal ones at every step. Based on the discriminator, LLMs are prompted to generate actions that maximize the score, utilizing historical action-score pair trajectories as guidance. Under mild conditions, DGAP resembles critic-regularized optimization and has been demonstrated to achieve a stronger policy than the LLM planner. In experiments across different LLMs (GPT-4, Llama3-70B) in ScienceWorld and VirtualHome, our method achieves superior performance and better efficiency than previous methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors proposed an embodied agent framework to optimize LLM action plans at each step. They achieve so by employing a trained discriminator that learns a score function of alignment between LLM predicted actions and the optimal action, the author. They demonstrated the effectiveness of this policy by conducting experiments on benchmarks in ScienceWorld and VirtualHome, and outperformed previous methods.

### Strengths
-The proposed framework is effective that it achieves superior results in the benchmarks studied.

-The experiments and ablation studies in this study is thorough and the baselines compared to are extensive.

-The presentation of this paper is good, the paragraphs are well written and easy to follow

### Weaknesses
 -The novelty of this proposed framework is unclear to me. What is the fundamental differences of the motivation and the framework between this work and previous language grounding work (e.g. Saycan)?

-The generalizability of the proposed method. If I understand correctly, the method designed does not involve fine-tuning a LLM rather it use a discriminator to capture the domain knowledge of the embodied agent. How do you see this discriminator generalize to more complicated scenarios as the granularity of visual/physical environment
is far beyond than the text modality can capture. 

-The choice of benchmark. I respect your choice of experiment benchmarks. However, there are many embodied agent planning frameworks on benchmarks like ALFRED. If you cannot include them as baselines, please discuss the differences.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

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
The paper introduces a novel framework named Discriminator-Guided Action Optimization (DGAP), which aims to improve the performance of Large Language Models (LLMs) in embodied planning tasks. By leveraging a small set of demonstrations to train a discriminator, DGAP facilitates the optimization of LLM-generated action plans through step-wise signals, leading to better alignment with optimal actions. The proposed method is tested on challenging benchmarks like ScienceWorld and VirtualHome, demonstrating superior performance and efficiency compared to existing methods.

### Strengths
1. The integration of a discriminator to guide LLMs in generating higher-quality action plans is a creative and promising approach.
2. The paper establishes a connection between DGAP and critic-regularized optimization in reinforcement learning, providing a solid theoretical foundation for the method.
3. Extensive experiments are conducted on well-known benchmarks, showcasing the practical benefits of DGAP over prior methods.
4. The paper is well-written, with clear explanations and logical organization, making it easy to follow the technical details and experimental results.

### Weaknesses
1. While the paper demonstrates the effectiveness of DGAP in specific environments, it would be beneficial to explore its scalability to more complex and diverse scenarios. Future work could investigate how the method performs in real-world settings with higher-dimensional state spaces, including environments with continuous action spaces and more intricate state representations beyond simple text descriptions. The current evaluation focuses on relatively constrained environments, and it's unclear how the discriminator would perform with the increased complexity of real-world sensor data and action spaces.
2. The reliance on a limited set of demonstrations might limit the generalizability of the model. It would be valuable to analyze how the performance changes with varying amounts of demonstration data, specifically investigating the sensitivity of the discriminator's performance to the quantity and diversity of demonstrations. Furthermore, the paper should explore whether the method can adapt to unseen tasks effectively, considering scenarios where the task distribution differs significantly from the demonstration data. The current analysis lacks a thorough investigation of the trade-offs between demonstration data size and generalization performance.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a framework named Discriminator-Guided Action Optimization (DGAP), which combines the long-term reasoning capabilities of large language models (LLMs) with task-specific grounding under guidance. The authors introduce a simple discriminator learned with a limited number of demonstrations and. validate the effectiveness of this approach through experiments. The paper also provides a detailed theoretical explanation of the relationship between this method and critic-regularized optimization in RL.

### Strengths
1. The paper employs a score function to quantitatively assess the planning effectiveness of the LLM, making it more reasonable compared to previous works.
2. The paper provides a detailed theoretical derivation to model the problem and establish its relationship with critic-regularized optimization.
3. The paper compares various types of planners, including reasoning-based and search-based approaches.

### Weaknesses
1. The experiments in the paper use the ScienceWorld and VirtualHouse simulators. However, it lacks the inclusion of widely used simulators for embodied planning tasks, such as ALFRED (https://arxiv.org/abs/1912.01734).
2. The proposed method does not achieve optimal performance on short-sequence tasks; its advantages are primarily evident in long-sequence tasks.

### Questions
1. Could the authors consider experimenting with datasets like ALFRED? Due to its widespread use, ALFRED includes both LLM-based and RL-based methods, providing a valuable basis for further comparison and analysis.
2. According to my understanding, the authors implicitly store task-specific knowledge in the discriminator through training. It would be beneficial to compare this approach with explicitly stored, search-based methods to better demonstrate the discriminator's advantages.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an LLM action plan optimization framework based on discriminators to enhance the policy performance in long-term tasks with high generalization ability, where a small number of demonstrations is required to guide the optimization process. This framework first learns a score function via the discriminator with limited set of demonstrations, where the LLM is prompt to generate actions to maximize the score for optimization. The experimental results demonstrate the effectiveness of the proposed method.

### Strengths
+ The topic of LLM-based embodied planning is of great interests in embodied AI especially for general-purpose robots.
+ The theoretical formulation to link the proposed method and critic-regularized optimization in RL brought some insights on embodied planning optimization
+ The performance shows the method outperforms the baselines by a large margin.

### Weaknesses
- As introduced in the Introduction Section, the proposed framework aims to bring the long-term reasoning ability from LLMs with task grounding without harming the generalization ability. The discriminator is trained on limited collected data compared with the pre-trained LLMs, and I am not sure whether the discriminator can be generalized well. More proofs are required.

- The groundtruth score for offline data in data collection is evaluated by a sentence embedding model. The quality of the sentence embedding model might significantly influence the performance of the groundtruth, where I doubt the noise of groundtruth will affect the model performance.

- The writing needs to be improved. The proposed method contains a lot of techniques. I think the most important contribution, which I guess might be the discriminator training and usage, should be clearly emphasized.

- Some qualitative results such as the planning results should be visualized to give some more intuition of the benefits brought by the proposed method.

- More analysis to the experimental results especially the performance differences between short and long sequences should be discussed, as the generalization ability on different tasks (short and long-horizon) is both important.

### Questions
See Weakness.

### Soundness
3

### Presentation
2

### Contribution
2
