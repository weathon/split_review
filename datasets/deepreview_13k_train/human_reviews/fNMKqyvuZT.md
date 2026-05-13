# Looking Backward: Retrospective Backward Synthesis for Goal-Conditioned GFlowNets

- Decision: Accept
- Scores: 8, 5, 8, 6

## Abstract
Generative Flow Networks (GFlowNets) are amortized sampling methods for learning a stochastic policy to sequentially generate compositional objects with probabilities proportional to their rewards. GFlowNets exhibit a remarkable ability to generate diverse sets of high-reward objects, in contrast to standard return maximization reinforcement learning approaches, which often converge to a single optimal solution. Recent works have arisen for learning goal-conditioned GFlowNets to acquire various useful properties, aiming to train a single GFlowNet capable of achieving different goals as the task specifies.
    However, training a goal-conditioned GFlowNet poses critical challenges due to extremely sparse rewards, which is further exacerbated in large state spaces. In this work, we propose a novel method named \textbf{R}etrospective \textbf{B}ackward \textbf{S}ynthesis (RBS) to address these challenges. 
    Specifically, RBS synthesizes a new backward trajectory based on the backward policy in GFlowNets to enrich training trajectories with enhanced quality and diversity, thereby efficiently solving the sparse reward problem. Extensive empirical results show that our method improves sample efficiency by a large margin and outperforms strong baselines on various standard evaluation benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduces a novel method, Retrospective Backward Synthesis (RBS), aimed at enhancing the training of goal-conditioned Generative Flow Networks (GFlowNets) by synthesizing new backward trajectories. RBS augments "virtual" backward trajectories in
goal-conditioned GFlowNets to enrich training trajectories with enhanced quality and diversity. RBS improves the sample efficiency and performance of GFlowNets across a range of tasks, including sequence generation and biological sequence design.

### Strengths
1. The paper identifies and targets a significant issue in the training of goal-conditioned GFlowNets, offering a practical and innovative solution. Augmenting backward trajectories for training is interesting.
2. Comprehensive empirical results are provided, demonstrating the effectiveness of RBS over existing methods on multiple benchmarks.

### Weaknesses
1. Limited Discussion on Potential Drawbacks: The paper does not sufficiently address the potential limitations of RBS. For instance, there is no discussion about the computational overhead of synthesizing backward trajectories, nor is there a mention of whether the method is robust to different types of reward structures or environment dynamics. Specifically, the paper lacks an analysis of how the computational cost of RBS scales with the complexity of the state space or the length of the trajectories. Furthermore, the method's sensitivity to the choice of backward policy and its potential impact on the quality of synthesized trajectories remains unexplored. It is also unclear how RBS would perform in environments with non-Markovian dynamics or where the backward transitions are not well-defined.
2. Relevance and Scope of Application: The improvements are made specifically within the context of GC-GFlowNets, which may limit the applicability of the method. The paper does not adequately discuss the transferability of RBS to other goal-conditioned learning frameworks or its potential limitations when applied to different types of tasks beyond sequence generation and biological sequence design. The authors should clarify whether the method is designed to be a general-purpose technique or if it is tailored to the specific characteristics of GFlowNets.
3. Comparison with Diffusion Policies: Given the similarities between the proposed RBS and diffusion policies, a direct comparison would be valuable to understand the unique contributions and differences of RBS. The paper should elaborate on the specific mechanisms that differentiate RBS from diffusion-based approaches, particularly in terms of how they handle trajectory generation and the learning process. It is not clear if RBS offers advantages in terms of computational efficiency or sample complexity compared to diffusion policies.
4. Assumptions on Environment Dynamics: It is unclear whether the proposed RBS method assumes or requires any particular properties of the environment, such as determinism or stochasticity. If the backward dynamics are infeasible or the environment is highly stochastic, the performance of RBS may be affected, and this should be addressed. The paper should explicitly state the assumptions made about the environment and discuss the potential impact of violating these assumptions on the performance of RBS. For example, how does RBS handle situations where the backward transition probabilities are not easily computable or are highly uncertain?
5. Quality of Synthetic Trajectories: The paper should include a discussion on how to ensure the quality of the synthesized backward trajectories, especially in cases where such trajectories may not correspond to realistic or feasible paths in the actual environment. The paper should address the potential for RBS to generate unrealistic or suboptimal trajectories, and how this might affect the learning process. It is not clear if the synthesized trajectories are guaranteed to be consistent with the underlying environment dynamics or if they could introduce biases into the training process.
6. Lack of Comparison with Goal-Conditioned RL: Without a comparison to goal-conditioned RL, it is difficult for readers to fully appreciate the relative strengths and weaknesses of GC-GFlowNets. Including such a comparison would provide a more complete picture of the method's positioning within the broader field of goal-directed learning. The paper should discuss the advantages and disadvantages of using GC-GFlowNets compared to other goal-conditioned RL methods, particularly in terms of sample efficiency, generalization, and robustness.
7. The authors may further investigate existing literature on augmenting backward trajectories for sample-efficient RL or backward learning in goal-conditioned RL, which makes the paper more comprehensive.

### Questions
1. How does RBS compare with diffusion policies, and in what scenarios does RBS offer distinct advantages?
2. Does RBS assume deterministic or stochastic environments, and how does it handle situations where the backward dynamics are not straightforward?
3. How can the authors ensure that the synthesized backward trajectories are meaningful and do not lead to false positives in the learning process?
4. Could the authors include a comparison with goal-conditioned RL methods to highlight the specific benefits of using GC-GFlowNets?

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
3

### Summary
The paper proposes Retrospective Backward Synthesis (RBS), a novel method to enhance the training of goal-conditioned Generative Flow Networks (GC-GFlowNets). GC-GFlowNets have shown potential in generating diverse sets of high-reward candidates but face challenges due to sparse reward structures and limited coverage of explored trajectories, especially when using offline data. To address these limitations, RBS synthesizes backward trajectories that originate from a desired goal, enriching the training data with high-quality, diverse samples. This approach helps transform unsuccessful action sequences into positive learning experiences, thereby improving sample efficiency and generalizability.

The authors introduce additional techniques, such as reward signal intensification and backward policy regularization, to stabilize training and prevent mode collapse. Empirical results across various benchmarks, including GridWorld and bit sequence generation, demonstrate that RBS outperforms state-of-the-art methods in terms of success rates, sample efficiency, and scalability. Notably, RBS achieves nearly 100% success in large-scale tasks where competing approaches fail, highlighting its robustness and potential for further advancements in GC-GFlowNets.

### Strengths
- Backward-Looking Strategy for Enhanced Training: The proposed Retrospective Backward Synthesis (RBS) method utilizes a backward-looking strategy to synthesize trajectories from the goal state, significantly enriching training data. This approach effectively improves sample efficiency by converting failed experiences into successful learning signals, addressing the sparse reward problem.
- Empirical Validation of Sample Efficiency: The paper presents strong empirical results across a range of benchmarks, demonstrating that RBS markedly improves sample efficiency. The method achieves nearly 100% success rates in complex tasks where state-of-the-art baselines fall short, underscoring its practical impact.
- Clear Writing and Presentation: The paper is well-written and presented, with clear explanations, structured methodology, and comprehensive experimental results. The clarity facilitates a strong understanding of both the theoretical and practical aspects of the proposed approach.

### Weaknesses
 - Scalability and Continuous Environments: The paper’s experiments focus on relatively simple and discrete environments, raising concerns about how well the Retrospective Backward Synthesis (RBS) method would scale to more complex, continuous, real-world tasks. The absence of testing in high-dimensional or continuous state-action spaces limits insights into its broader applicability. Specifically, the paper lacks experiments in environments with continuous action spaces, which are common in many real-world robotic and control problems. This makes it difficult to assess the method's performance in scenarios where actions are not discrete choices but rather continuous values.
- Tuning Challenges: The method's reliance on hyperparameters, such as reward scaling and backward policy regularization, introduces tuning challenges. While these components are beneficial for stabilizing training, they require careful adjustment, potentially impacting the ease of replication and practical deployment in varied scenarios. The paper does not provide a clear methodology for selecting these hyperparameters, nor does it analyze the sensitivity of the method to different hyperparameter values. This lack of guidance makes it difficult for practitioners to apply the method effectively.
- Lack of Comparison with Model-Based RL: Despite the inherent use of backward trajectory synthesis, which resembles model-based planning, the paper does not compare RBS with established model-based RL approaches such as MBPO or Dreamer. This omission makes it difficult to assess how RBS performs relative to other methods that also utilize environment models for planning and sample efficiency. The paper should include a comparison with model-based approaches to highlight the differences and potential advantages of RBS over existing model-based RL techniques.

### Questions
- In algorithm 1) line 6, how do we guarantee that the backward policy could reach $s_0$ from $y$ each time?
- Are tuning for reward intensification and backward policy regularization difficult? What the the effect of hyper-parameters on the performance?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses key challenges in goal-conditioned Generative Flow Networks (GFlowNets), specifically the problems of sparse rewards and limited trajectory coverage. The authors introduce Retrospective Backward Synthesis (RBS), a method that generates additional backward trajectories to expand the training data. Their approach aims to improve both the quality and diversity of training trajectories, providing more learning signals in scenarios with sparse rewards. Empirical evaluations demonstrate improved sample efficiency and performance compared to baseline methods across multiple benchmarks.

### Strengths
* The paper is well-written and straightforward to understand.
* Retrospective Backward Synthesis (RBS) is introduced with clear motivation, and the paper also presents training techniques such as backward policy regularization. 
* Empirical results demonstrate that the proposed method outperforms baselines, showing improved performance and sample efficiency.

### Weaknesses
 * The evaluation tasks do not include key benchmarks like RNA Generation from Pan et al. (2023a), which limits direct comparison.
* The differences between the proposed RBS method and OC-GAFN are not clearly articulated. A more comprehensive discussion is needed to clarify the specific advantages of the RBS method, particularly regarding how RBS addresses the limitations of Hindsight Experience Replay (HER) used in OC-GAFN. The paper should delve deeper into the mechanisms that allow RBS to generate novel and diverse trajectories, going beyond the relabeling approach of HER which may not sufficiently explore the state space. Furthermore, the discussion should highlight the specific advantages of training a single GFN model versus the two separate models required by OC-GAFN, in terms of computational efficiency and training stability.
* It remains unclear how goals are defined across the evaluated tasks, which could impact generalizability and reproducibility. For example, in the context of the AMP generation task, are goals defined as specific sequences or properties of the generated sequences? A more detailed explanation of how goals are represented and utilized in each task is necessary to assess the method's applicability and to ensure reproducibility.

### Questions
Please address my concerns in the weakness

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
3

### Summary
The paper tackles the challenge of training goal-conditioned Generative Flow Networks (GC-GFlowNets) in environments with sparse rewards and limited offline data. It introduces Retrospective Backward Synthesis (RBS), which synthesizes new backward trajectories to enrich training data, improving sample efficiency and diversity. Experiments demonstrate that RBS significantly improves performance and generalization in various benchmarks.

### Strengths
This paper proposes a novel method called Retrospective Backward Synthesis (RBS), which synthesizes new backward trajectories in goal-conditioned GFlowNets to improve the quality and diversity of training trajectories. This approach introduces rich learnable signals, effectively addressing the sparse reward problem.

### Weaknesses
1.The experimental tasks are relatively simple and insufficiently comprehensive.

2.The latest goal-conditioned reinforcement learning algorithms are not selected for comparison.

### Questions
1.	Age-Based Sampling is a very straightforward technique. How does it compare to previous methods like Prioritized Experience Replay (PER)? Did the authors attempt using PER as well?

2.	Regarding the experimental setup, since you’ve compared your method with reinforcement learning approaches, I assume that these experiments share the same tasks as those in reinforcement learning. If that’s the case, why weren’t newer RL methods selected as baselines? Additionally, for tasks like bit sequence generation, TF binding generation, and AMP generation, is DQN an appropriate baseline?

### Soundness
2

### Presentation
3

### Contribution
2
