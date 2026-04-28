# Unlocking the Power of Representations in Long-term Novelty-based Exploration

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
We introduce \textit{Robust Exploration via Clustering-based Online Density Estimation} (\DETOCS), a non-parametric method for novelty-based exploration that estimates visitation counts for clusters of states based on their similarity in a chosen embedding space.
By adapting classical clustering to the nonstationary setting of Deep RL, \DETOCS can efficiently track state visitation counts over thousands of episodes. We further propose a novel generalization of the inverse dynamics loss, which leverages masked transformer architectures for multi-step prediction; which in conjunction with \DETOCS achieves a new state-of-the-art in a suite of challenging 3D-exploration tasks in \DMH. 
\DETOCS also sets new state-of-the-art in hard exploration Atari games, and is the first agent to reach the end screen in \textit{Pitfall!}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novelty-based intrinsic reward (RECODE) to facilitate exploration in sparse-reward environments. The proposed approach derives intrinsic rewards using approximate state visitation counts in a suitably constructed embedding space. 

RECODE builds on the previously proposed Never Give Up (NGU) intrinsic reward in two ways.

First, unlike in NGU, which uses one-step inverse dynamics to learn an observation embedding, this paper proposes Coupled Action-State Masking (CASM) to capture controllable features across multiple steps.

Second, the proposed approach maintains and derives intrinsic rewards from a global memory of embeddings updated based on a clustering principle. Whereas NGU derived intrinsic rewards using the contents of an episodic buffer and a global bonus from Random Network Distillation (RND).

Experiments show that the proposed approach to providing intrinsic rewards outperforms baselines in challenging exploration settings. Further analysis shows that the proposed approach is more robust to observation noise than NGU and RND.

### Strengths
**S1.**  The problem of exploration in sparse-reward settings and large observation spaces is of significant interest to the research community.

**S2.** The proposed approach simplifies NGU in a crucial way. NGU needed to combine an episodic bonus and a global bonus from RND. RECODE removes the need for a separate episodic novelty component. However, this simplification comes at the cost of mechanisms to manage the memory (see W1).

**S3.** In terms of the empirical evaluation, the environments considered are indeed challenging exploration problems. Further, the proposed approach provides empirical benefits, especially on the DM-HARD-8 problems.
 
**S4.** The paper is well-written and easy to follow.

### Weaknesses
 **W1.** A crucial weakness is that the proposed approach introduces additional complexity in memory management compared to NGU, which had a more straightforward episodic reset for memory. Here, there are hyperparameters for atoms of memory size, a discounting of counts and additional heuristics to update/add/remove atoms of memory. The memory management in RECODE requires careful tuning of parameters such as the memory size, the discount factor for visitation counts, the probability of inserting new atoms, and the specific heuristics used for updating and removing atoms. These hyperparameters and heuristics add complexity and might make it difficult to apply this approach to new environments, especially when compared to the simpler episodic reset of NGU. The interaction between these parameters and their impact on performance is not fully explored, which could lead to instability and difficulty in reproducing results across different environments.

**W2.** Further ablations are needed to clarify certain issues. 

Is CASM only beneficial over one-step action prediction (AP) when there is high aliasing due to partial observability (like DM-HARD-8)? Are results for MEME-RECODE/NGU-CASM available for the Atari environments? I may have missed them in the appendix.

In Appendix L, results are presented for RND on AP (one-step action prediction), where a random net is applied to features extracted by AP. As the random network is typically seen as a feature extractor itself, wouldn’t it be more natural to obtain RND-like intrinsic rewards from a predictor of the AP feature of a state (rather than a random embedding of the AP embedding)? The current approach of applying a random network on top of the AP features seems somewhat arbitrary and lacks a clear justification. It would be more intuitive to use the AP features directly for the RND reward or to predict these features using another network. 

Similarly, it would be helpful to evaluate if RECODE is better than NGU when NGU uses RND on AP (or an RND-like bonus with AP features directly) for its global bonus. This comparison is crucial to understand the specific benefits of RECODE's memory mechanism over NGU's approach when both use similar feature representations.

**W3.** The paper would benefit from connections to existing work. For instance, the recently proposed MIMEx [1] also uses masked transformers to derive trajectory level intrinsic rewards. 

Previous works have studied incorporating information over longer trajectories to derive better intrinsic rewards under partial observability, [4] uses general value functions based on RND, other approaches use successor features which naturally incorporate multi-step information [2,3]. The paper should discuss how RECODE relates to these methods and highlight its unique contributions in the context of these existing approaches. Specifically, the use of successor features or general value functions could provide alternative ways to incorporate multi-step information, and the paper should clarify why RECODE's approach is superior or complementary.

**W4.** In the abstract and the conclusion, the authors claim that the proposed approach sets a new state-of-the-art on Atari’s hard exploration dataset and DM-HARD-8. While this claim is reasonable for DM-HARD-8, I am not sure it applies to the Atari experiments, as RECODE appears to be worse than NGU in hero and venture. The claim of achieving state-of-the-art performance on Atari is not fully supported by the results presented, and the authors should be more precise about the specific environments where RECODE outperforms existing methods.

### Questions
Q. In many procedurally generated environments, episodic resets to the memory (as in NGU) could be preferable. Consider a scenario where blue circles are actually novel in the current episode (and should be sought) but have been seen in previous episodes in other contexts. Of course, some notion of global novelty would also typically be needed. It would seem that something like NGU would again be preferable to RECODE in many of these settings. I am curious to know the authors’ thoughts regarding this.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The document presents a novel approach known as RECODE for enhancing exploration in the realm of Reinforcement Learning. This method combines elements from both parametric and non-parametric techniques in this domain.

Initially, the paper delves into the existing literature of novelty-driven exploration. Parametric strategies involve assessing novelty by utilizing trained representation models on states and actions. However, these methods are prone to issues like catastrophic forgetting or predicting novelty where it is irrelevant with respect to "controllable" features. On the other hand, non-parametric techniques maintain a repository of historical embeddings. They employ approaches such as state counting to drive novelty-based exploration, or approximate state counting in continuous domains.

In contrast to traditional methods, the authors introduce RECODE, which is a non-parametric approach relying on a historical embedding repository. Instead of simply erasing entries from this history, RECODE dynamically adjusts embeddings and counters by employing a system of discounted sums.

The paper also offers a series of experiments showcasing RECODE's superior performance when compared to baseline methods. Remarkably, RECODE stands out as the first Reinforcement Learning algorithm to tackle the game "Pitfall!" and surpass the human baseline in "Push Blocks" from DM-HARD-8.

### Strengths
The paper addresses an important problem within the realm of Reinforcement Learning by introducing an algorithm centered on novelty-driven exploration. As a solution, RECODE effectively mitigates significant shortcomings observed in prior visitation count techniques like NGU. It strikes a balance between short-term and long-term novelty, avoiding an excessive bias toward short-term novelty and integrating long-term memory into the novelty determination process, despite having finite memory constraints.

In the experiments, the RECODE approach completes the “Pitfall!” benchmark for the first time, and it also attains performance levels exceeding human capabilities on the "Push Blocks" challenge from DM-HARD-8.

### Weaknesses
The rationale behind using RECODE as opposed to NGU is simplicity: RECODE uses one singular mechanism, while NGU uses two. However, it is not apparent to me that overall RECODE is simpler in terms of hyperparameter count / design space. Is there a rationale behind the optimal choice of hyperparmaters?

In addition, the experiment figures do not seem to support an overwhelming positive conclusion in favor of RECODE, besides for the headline successes on “Pitfall!” and DM-HARD-8.

### Questions
Would you kindly answer the following questions?
* Please clarify how the experimental figures support the conclusion that the method is indeed superior to alternatives.
* I believe that Figure 1 would benefit from a more explanatory caption. There is no definition for HNS, Capped HNS and the number of frames in the caption.
* Could you explain how your method is better than the alternatives when it comes to design space complexity?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a framework that integrates sophisticated representation learning with long-term memory to improve novelty-seeking behaviours in deep reinforcement learning. The framework consists of two key components: RECODE, a memory buffer that approximates visitation counts in a learned embedding space; and CASM, a transformer model that learns the embedding space by jointly addressing masked sequence modelling and inverse dynamics prediction. 

The paper explores and implements various components to tackle challenges inherent in deep RL, such as non-stationary distributions, online learning of representations, and sparse rewards. Experimental results on challenging benchmark tasks demonstrate that RECODE (the memory buffer) enhances performance regardless of the representation learning method, and CASM improves performance independently of the memory-based approach. The algorithm is compared with NGU and Byol-Explore, two recent and popular deep exploration algorithms. 

Overall, the paper presents a sophisticated algorithm that achieves great performance in hard-exploration tasks, and its implementation details are well-justified and clearly presented.

### Strengths
The paper builds upon prior work in the fields of exploration in deep reinforcement learning and representation learning. Concerning RL-related work, it extends existing non-parametric novelty estimation methods that maintain a history of observations in a memory buffer and use KNN to compute similarity. However, this work pushes the boundaries of previous memory-based algorithms by operating the memory buffer in a much more compact embedding space. Additionally, the paper presents several implementation details to ensure an accurate estimation of true visitation counts, addressing challenges related to non-stationary data and representation distributions. For representation learning, the paper adopts the widely recognized transformer architecture for sequence modelling and employs masked training to learn compact representations in reinforcement learning. Furthermore, the study incorporates the established inverse dynamics prediction objective but frames it within the more condensed embedding space. This work effectively combines and adapts robust foundations from multiple fields into a high-quality and well-justified framework for reinforcement learning, resulting in outstanding practical performance.

The paper maintains clarity, offering comprehensive descriptions of the background theory and the architecture of the presented framework. It includes numerous helpful figures and algorithm pseudo-code, enhancing the reader's understanding of the method. Notably, the paper meticulously addresses significant challenges related to long-horizon exploration in deep RL, each thoroughly examined with dedicated experiments and figures that surpass typical task-return analyses.

In summary, this work makes a significant contribution to the community. Specifically, it introduces an algorithm that harnesses potent representation learning and precise novelty estimation to solve challenging long-horizon exploration problems effectively.

### Weaknesses
The presented algorithm demonstrates impressive performance in well-established hard-exploration benchmarks. However, it lacks evaluation in an open-ended environment, such as Minecraft. While the complexity of long-horizon tasks from Atari and rich observations from environments like DM-Hard-8 are represented in the current evaluation, an open-ended environment would introduce additional challenges related to emergent behaviors and less structured exploration. This would provide a more comprehensive assessment of the algorithm's ability to generalize to diverse and potentially unpredictable scenarios.

While the authors assert the robustness of the presented algorithm to different RL algorithms for policy learning, the RL training solely relies on MEME and VMPO. The paper lacks an analysis showcasing the performance of more commonly used algorithms like PPO or DQN when coupled with RECODE. Although MEME is a powerful RL algorithm, demonstrating compatibility with widely adopted algorithms like PPO or DQN would significantly strengthen the claim that RECODE can enhance long-horizon exploration across various RL algorithms. The use of VMPO for the DM-Hard-8 suite is noted, but this does not provide sufficient evidence that RECODE would integrate well with other popular RL algorithms, especially in different domains.

The paper does not provide sufficient detail regarding the computational resources required for training RECODE. While the number of environment interactions is reported, critical details such as memory usage, CPU requirements, and GPU memory usage are missing. This omission raises concerns about the practicality and scalability of the framework. For instance, if RECODE requires significantly more memory or computational power compared to existing methods, it could limit its adoption in resource-constrained settings. Conversely, if RECODE achieves its performance with comparable or lower resource usage, it would be a notable advantage that should be highlighted.

### Questions
The computational resource requirements for training RECODE remain unclear. The paper indicates a substantial number of environment interactions, around 7.5e8 steps, for various environments, comparable to previous studies. However, essential details such as memory usage, CPU requirements, and GPU memory are not provided. This lack of information poses a significant concern, as it could either limit the framework's practical applicability or potentially underscore its uniqueness as a noteworthy contribution.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
