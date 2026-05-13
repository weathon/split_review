# Generalized Behavior Learning from Diverse Demonstrations

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Diverse behavior policies are valuable in domains requiring quick test-time adaptation or personalized human-robot interaction. Human demonstrations provide rich information regarding task objectives and factors that govern individual behavior variations, which can be used to characterize \it{useful} diversity and learn diverse performant policies.
However, we show that prior work that builds naive representations of demonstration heterogeneity fails in generating successful novel behaviors that generalize over behavior factors.
We propose Guided Strategy Discovery (GSD), which introduces a novel diversity formulation based on a learned task-relevance measure that prioritizes behaviors exploring modeled latent factors.
We empirically validate across three continuous control benchmarks for generalizing to in-distribution (interpolation) and out-of-distribution (extrapolation) factors that GSD outperforms baselines in novel behavior discovery by $\sim$21\%.
Finally, we demonstrate that GSD can generalize striking behaviors for table tennis in a virtual testbed while leveraging human demonstrations collected in the real world.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a novel diversity formulation based on a learned task-relevance measure that prioritizes behaviors exploring modeled latent factors, called Guided Strategy Discovery (GSD).
The proposed method is empirically validated across three continuous control benchmarks for generalizing to in-distribution (interpolation) and out-of-distribution (extrapolation) preferences, as well as demonstrated to generalize striking behaviors for table tennis in a virtual testbed while leveraging human demonstrations collected in the real world.

### Strengths
The paper is written in a clear way and is well structured. The proposed method is formulated clearly and scoped within relevant literature. The proposed method is also evaluated experimentally, including comparisons with alternatives. Figures and visualisations are clear and help capture the contribution of the method.

### Weaknesses
Some results are not immediately clear from the plots, for example the visualisation of the interpolation/extrapolation experiments in Figure 5 is difficult to read. It is unclear how the method performs with higher dimensional latent spaces, and whether the approach scales to more complex tasks with higher dimensional preferences and rewards. The paper does not discuss the limitations of the chosen regularization in the latent space, specifically how the choice of the task-relevance measure affects the learned representation. It is also unclear how much the representation is limited by the demonstrations, and whether this approach suffers from problems similar to behavior cloning, such as sensitivity to the distribution of the demonstrations. Finally, the paper does not discuss if the exploration strategy is limited by the framework and whether this has an effect on the final performance.

### Questions
What are the limiting factors of the chosen regularization in the latent space? 
How much is the representation limited by demonstrations? Does this approach suffer from problems similar to behavior cloning?
Are there more intuitive visualisations for your results, eg for interpolation/extrapolation?
Is exploration limited and does this have an effect on final performance?

### Soundness
3

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
2

### Summary
The authors address the challenge of generating diverse behaviors that are useful for a wide range of tasks. They introduce a novel approach called *Guided Strategy Discovery (GSD)*, which features a diversity formulation that uses a learned task-relevance measure to prioritize behaviors that effectively explore modeled latent factors. The proposed method is  evaluated across multiple simulated tasks and in a task with real-world data.

### Strengths
The paper addresses a significant and relevant problem , contributing to our understanding of behavior diversity in various tasks. The use of real-world human data for evaluation is praiseworthy, as it enhances the applicability findings. Additionally, the paper features well-designed and illustrative figures that support the discussed concepts .

### Weaknesses
The paper addresses a significant and relevant problem , contributing to our understanding of behavior diversity in various tasks. The use of real-world human data for evaluation is praiseworthy, as it enhances the applicability findings. Additionally, the paper features well-designed and illustrative figures that support the discussed concepts .

The paper builds upon InfoGAIL, an adversarial imitation learning method; however, it does not explore other adversarial imitation learning (AIL) methods or potential modifications that could enhance performance. A more comprehensive overview and comparison of relevant AIL techniques, such as those discussed in Orsini et al [1], would strengthen the contextualization of the proposed approach and highlight its novelty by discussing how different design choices influence learning. Specifically, the paper should discuss how the choice of discriminator architecture, optimization strategy, and regularization techniques within different AIL methods might impact the diversity and quality of learned behaviors, and how these choices compare to the proposed method.

Furthermore, the tasks considered in the paper do not align with established benchmarks. For example, recent work has introduced benchmarks for diverse behaviors, as highlighted by Jia et al[2]. Additionally, the paper lacks comparisons to other methods, including diffusion-based approaches that can effectively represent diverse, multimodal data. The absence of these comparisons makes it difficult to assess the relative performance and advantages of the proposed approach compared to state-of-the-art methods in both imitation learning and diverse behavior generation. The paper should consider comparisons to methods that explicitly model multimodal action distributions, such as those using normalizing flows or variational autoencoders.

The writing quality of the paper could be improved for clarity and conciseness. The term "preference" does not align with its common usage in related fields such as Reinforcement Learning from Human Feedback (RLHF) [3], which may lead to confusion among readers. The paper should use more precise terminology to describe the latent factors being discovered, and avoid terms that have established meanings in other contexts. In terms of presentation, the caption for Figure 10 appears integrated into the surrounding text, making it difficult to read. Additionally, Algorithm 1 (Lines 270-287) is quite dense and may overwhelm readers. The notation used in Algorithm 1, Line 274, could also be confusing due to the presence of commas following terms (e.g., policy, $\pi$).

### Questions
In Appendix C.2, the authors state that they used PPOBC for the DriveLaneshift and FetchPickPlace tasks. However, it is important to note that PPOBC is not a pure reinforcement learning (RL) algorithm, as it incorporates demonstrations. How would the proposed method differ if it were implemented using only PPO without the influence of demonstrations?

Additionally, could the authors clarify what is meant by diverse behaviors in the context of the HalfCheetah task? Specifically, how are different speeds relevant for tasks in the sense of improved task performance?

Finally, will the code be made publicly available? Furthermore, will the dataset of real-world human demonstrations also be accessible to the research community?

[1]Rohit Jena, Changliu Liu, and Katia Sycara. Augmenting gail with bc for sample efficient imitation learning. In Conference on Robot Learning, pp. 80–90. PMLR, 2021

### Soundness
2

### Presentation
2

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
This paper introduces Guided Strategy Discovery (GSD), which provides a new diversity formulation that is able to learn diverse, task-accomplishing behaviors from demonstrations. Through a 2d Point Maze task, the authors demonstrate that prior works fail to generalize to new behaviors. GSD introduces a new constraint $f$-relevant diversity to assign high energy to new state-action pairs. A learned task-relevance measure is used to guide the meaningful/task-relevant behavior patterns. The empirical experiments show that GSD outperforms other baselines in novel behavior discovery.

### Strengths
- The authors design a 2D toy task PointMaze, which demonstrates the existing diversity formulations, InfoGAIL, and Lipschitz constraints, fail to generate new, task-accomplishing behaviors.
- The authors provide an insightful motivation for the task-relevant diversity.
- The effectiveness of GSD is demonstrated on 3 simulation tasks and 1 real-to-sim Table Tennis task (The demonstrations are collected using a real-world setup).

### Weaknesses
 - The experiments only contain tasks with 1-d latent factors, which restricts the applications of GSD. More complex task evaluations would greatly improve the quality of the paper. Specifically, the current evaluation does not explore the method's ability to handle multiple, potentially correlated, latent factors that are common in real-world scenarios. For instance, in a robotic manipulation task, multiple degrees of freedom and object properties could contribute to the diversity of behaviors, and it's unclear how GSD would perform in such cases.
- The experiments only consider the InfoGAIL setting. Extensions to other general imitation learning frameworks would be appreciated. The current evaluation lacks a comparison with other imitation learning methods, especially those that do not rely on adversarial training. This limits the understanding of GSD's general applicability and its potential benefits over simpler approaches. For example, behavior cloning with variational autoencoders could be a relevant baseline to compare against.
- The implementation seems complex to me. It would be great to provide the code for better understanding and reproduction. The description of the energy function and its derivation is not entirely clear, making it difficult to understand how it is implemented and how the different components interact. The lack of publicly available code further hinders the reproducibility and verification of the results.

### Questions
Overall, this paper provides the potential to learn a diverse range of novel behaviors while maintaining the task success rate. However, scaling to tasks with complex behaviors needs to be further evaluated. I have the following questions:

- In the experiments, the 1-d latent factors generally refer to position, velocity, or ball height. How would the authors expect to solve more complex behaviors in robot manipulation tasks? D3IL [1] provides multiple tasks with diverse behaviors. Taking the pushing task for example, could GSD be able to address this task when interacting with objects frequently?
- Could the diversity objectives be used in general behavior cloning?
- Regarding the energy function $f$, how to the authors model it? Maybe I missed something, but how do we get the desired energy function $f(s,a)$

[1] Towards Diverse Behaviors: A Benchmark for Imitation Learning with Human Demonstrations, ICLR’24

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel framework called Guided Strategy Discovery (GSD) for learning diverse behaviors from demonstrations, aiming to generalize these behaviors to unseen task variations. The authors introduce a task-relevance diversity objective that encourages behavior exploration of latent factors in demonstrations, outperforming baseline methods in continuous control benchmarks like robot control and virtual table tennis.

### Strengths
- The work introduces a new approach for behavior learning that focuses on task-relevant diversity. The proposed GSD framework creatively balances imitation with exploration of unseen behavior spaces.
- The empirical evaluation is robust, spanning multiple domains (robot control, driving, and manipulation) and showing consistent improvement over baselines, especially in behavior generalization. The metrics used, such as interpolation and extrapolation errors, are well-chosen to highlight the effectiveness of GSD in diverse and novel task variations.
- The paper is well-structured, with clear explanations of the problem, related work, and contributions. Figures and diagrams effectively communicate the GSD framework and its comparative performance.

### Weaknesses
 - The task-relevance diversity formulation, while promising, may still need refinement for more complex behaviors in physical systems, particularly where task success is less clear or difficult to define in terms of energy regions. Specifically, the method relies on the assumption that high occupancy regions in state-action space correlate with task success, which may not hold in scenarios with non-expert demonstrations or partially observable environments. The energy function, which is essentially a discriminator, might not accurately capture the nuances of task success in these more complex settings, leading to suboptimal behavior.
- The writing is mostly clear, but some sections on the technical implementation of the diversity objective could benefit from further simplification for a broader audience. The description of the algorithm and the mathematical formulation of the diversity objective could be made more intuitive, especially for readers not deeply familiar with adversarial imitation learning. The current presentation might obscure the core ideas behind the method.
- The state-action space assumes a continuously varying task relevance, and the experiments are primarily performed in environments with this feature. The proposed method may fail to scale to settings where adjacent state-action pairs have significantly different energy. The linear constraint in Eq. 1, which enforces similar latent vector assignments for neighboring state-action pairs, might not be appropriate for tasks with sparse, non-adjacent high-energy regions. This assumption limits the method's applicability to a specific class of problems and raises concerns about its generalization capabilities.

### Questions
- Some existing works aim to learn diverse task-accomplishing behaviors from demonstrations that generalize over latent preferences using mutual information-based methods [1, 2] and latent space structure design [3]. It may help to discuss these existing works to motivate the need for the proposed method. How to convince people of a need of GSD given these prior works targeting the same goal?
- The constraint shown in Eq.1 assumes linearity of the state-action space. The proposed method may fail to scale to settings where adjacent state-action pairs have significantly different energy. How generally does this assumption apply to different tasks and state action space design? 
- As pointed out in the limitation section, the experiments are constrained to one-dimensional latent factors, limiting the evaluation of the method's scalability to more complex, higher-dimensional spaces. Please analyze if and how GSD may potentially fail when applied to higher-dimensional latent space. And if not, why not evaluate such environments?


[1] Li, C., Blaes, S., Kolev, P., Vlastelica, M., Frey, J. and Martius, G., 2023, May. Versatile skill control via self-supervised adversarial imitation of unlabeled mixed motions. In 2023 IEEE international conference on robotics and automation (ICRA) (pp. 2944-2950). IEEE.

[2] Peng, X.B., Guo, Y., Halper, L., Levine, S. and Fidler, S., 2022. Ase: Large-scale reusable adversarial skill embeddings for physically simulated characters. ACM Transactions On Graphics (TOG), 41(4), pp.1-17.

[3] Li, C., Stanger-Jones, E., Heim, S. and Kim, S., 2024. FLD: Fourier Latent Dynamics for Structured Motion Representation and Learning. arXiv preprint arXiv:2402.13820.

### Soundness
4

### Presentation
4

### Contribution
3
