# A Theory of Multi-Agent Generative Flow Networks

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Generative flow networks utilize a flow-matching loss to learn a stochastic policy for generating objects from a sequence of actions, such that the probability of generating a pattern can be proportional to the corresponding given reward. However, a theoretical framework for multi-agent generative flow networks (MA-GFlowNets) has not yet been proposed. In this paper, we propose the theory framework of MA-GFlowNets, which can be applied to multiple agents to generate objects collaboratively through a series of joint actions. We further propose four algorithms: a centralized flow network for centralized training of MA-GFlowNets, an independent flow network for decentralized execution, a joint flow network for achieving centralized training with decentralized execution, and its updated conditional version. Joint Flow training is based on a local-global principle allowing to train a collection of (local) GFN as a unique (global) GFN. This principle provides a loss of reasonable complexity and allows to leverage usual results on GFN to provide theoretical guarantees that the independent policies generate samples with probability proportional to the reward function. Experimental results demonstrate the superiority of the proposed framework compared to reinforcement learning and MCMC-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies the theory of multi-agent generative flow networks for co-operative tasks. The paper proposes four learning patterns: the Centralized Flow Network (CFN), Independent Flow Network (IFN), Joint Flow Network (JFN), and Conditioned Joint Flow Network (CJFN) algorithms. The paper also does experiments on the toy hyper-grid environment and one StarCraft game.

### Strengths
Originality: The paper is one of the first to study the extension of Gflownets to multi-agent settings. 
Quality：The paper proposes four types generative algorithms, and discuss the difference of these algorithms in terms of the training complexity and the performance. 
Significance: Experiments validates the proposed method outperforms MAPPO, MCMC in terms of modes found and L1 error.

### Weaknesses
1.For the clarity, I would suggest that the authors choose the original Gflownet formulations. The FM formulations in this paper and the original FM paper are quite different, which is quite hard to follow the main idea of this paper.
2.What's the main challenge that extend the Gflownet to multi-agent settings? For now, there seems no technical difficulty for multi-agent Gflownets.
3.The paper only studies the flow matching objective? does the proposed method applies to other Gflownet learning objectives, such as the detailed balance and the trajectory balance loss?
4.For the experiments, which algorithm is the best?  In the common sense, CFN achieves the best performance.  Also, the L1 error of all algorithms are quite high, i.e., these algorithms can not sample the reward distribution in practice. Why does the paper only present the result of JFN on the StarCraft 3m map?

### Questions
See the weakness.

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
3

### Summary
The paper presents a theoretical framework focused on adapting GFlowNets to multi-agent setting, building on the previously proposed theory of non-acyclic GFlowNets. Several training algorithms are proposed that can work in centralized and decentralized settings, and experimental evaluation is provided on both synthetic and real-world tasks.

### Strengths
This work is one of the first to consider a novel setting of multi-agent GFlowNets, providing extensive theoretical framework and results. 

It is known that RL algorithms can be applied to GFlowNet training [1], and this work is among the few [2] that explore the other direction — applying GFlowNets in RL tasks.

References:

[1] Daniil Tiapkin, Nikita Morozov, Alexey Naumov, Dmitry Vetrov. Generative Flow Networks as Entropy-Regularized RL. AISTATS 2024

[2] Leo Maxime Brunswic, Yinchuan Li, Yushun Xu, Shangling Jui, Lizhuang Ma. A Theory of Non-Acyclic Generative Flow Networks. AAAI 2024

### Weaknesses
I have two major concerns about this works.

My first major concern is the clarity of the text. For the most part I did not understand the methodological and theoretical results of this paper. The main thing hindering readability is a combination of very heavy mathematical notation with a lack of consistency, clarity and correct order of definitions. Here are some examples:

1) I did not understand what is state map $S$ (line 80) and what is its purpose. It is introduced in Section 2 but never used in the main text of the paper.

2) Why does transition kernel (line 80) only depend on the action, not on state-action pairs? In standard RL and multi-agent RL formulations it depends on both.

3) Can you please explain the equation $\prod_{i \in I} p^{(i)} \circ S \circ \pi=\mathrm{Id}$ (line 94)?

4) The task that multi-agent GFlowNets try to solve is never formally defined. After reading Section 2 one can guess that it is sampling global states with probabilities proportional to the global reward, but the task has to be explicitly stated nevertheless.

5) Local rewards $R^{(i)}$ appear in Section 2 (line 148), but their definition and connection to global reward is given only in the next section.

6) Their definition given in Section 3 is $R^{(i)}\left(o_t^{(i)}\right):=\mathbb{E}\left(R\left(s_t\right) \mid o_t^{(i)}\right)$ (line 189), and they're said to be utilized in the local training loss. From what I understand, this expectation is intractable in the general case, so I do not understand how are they defined in practice. Authors mention that it is possible to use stochastic rewards instead, but as far as I am aware, GFlowNet theory introduced in previous works, upon which this paper builds, does not support stochastic rewards.

7) On line 241, authors mention: "At this stage, the relations between the global/joint/local flow-matching constraints are unclear, and furthermore, the induced policy of the local GFlowNets still depends on the yet undefined local rewards." In my humble opinion, if any novel definition/theorem/algorithm depends on some object, the object has to be previously introduced and properly defined in all cases.

I believe that this paper could greatly benefit from using simplified notation in the main text (while the full set of definitions can be introduced and used in appendix), as well as major revision of Sections 2 and 3 to ensure that the problem itself and all objects we work with are properly defined and explained to the reader in proper order. 

My second concern is related to the presentation of experimental results. The abstract states: "Experimental results demonstrate the superiority of the proposed framework compared to reinforcement learning and MCMC-based methods." Conclusion also has a similar statement (line 470). While on toy synthetic hypergrid environment the proposed methods do show significant improvement over baselines, the results on a more interesting StarCraft task do not support this claim. The proposed JFN algorithm falls behind 3 out of 4 baselines and performs similarly to the remaining one (which is Independent Q-Learning, one of the simplest existing algorithms in multi-agent RL). I understand that the main contributions of this paper are theoretical and methodological, but neverhtless I suggest correcting the statements to faithfully reflect the presented results. I also understand that such metric as win rate may not favor GFlowNets compared to RL approaches, but then I would also suggest presenting some other quantitative metric to demonstrate the utility of the proposed approach in this task, e.g. some measure of diversity.

### Questions
0) See Weaknesses.

1) Can you please give more detail on how the proposed framework and algorithms differ from the ones presented in [3]?

References:

[3] Shuang Luo, Yinchuan Li, Shunyu Liu, Xu Zhang, Yunfeng Shao, Chao Wu. Multi-Agent Continuous Control with Generative Flow Networks. Neural Networks, Volume 174, 2024

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a theoretical framework for multi-agent generative flow networks (MA-GFlowNets) and presents four algorithms: Centralized Flow Network (CFN), Independent Flow Network (IFN), Joint Flow Network (JFN), and Conditioned Joint Flow Network (CJFN). The authors introduce a local-global principle based on the principles in MARL that allows training individual GFNs as a unified global GFN. The authors evaluate their approach on Grid and SMAC tasks by comparing with MARL and MCMC approaches.

### Strengths
The paper is easy to understand (although some important details are missing as discussed in the next part), and the paper studies an important problem in extending GFlowNets to handle multi-agent tasks.

### Weaknesses
1. The paper's novelty claim is questionable. The authors state "However, based on current theoretical results, GFlowNets cannot support multi-agent systems" while ignoring relevant prior work, particularly Li et al. (2023) which already explored multi-agent GFlowNets. The paper fails to clearly articulate how its approach differs fundamentally from existing multi-agent GFlowNet methods, making the contribution seem incremental at best.
2. The experimental evaluation has several limitations:
- Only uses the simplest 3m StarCraft II environment, and there is little performance improvement. The lack of experiments on more complex scenarios makes it difficult to assess the scalability and robustness of the proposed algorithms.
- Results in Figure 3 show very high L1 errors, which suggests poor learning. The magnitude of these errors raises concerns about the convergence and accuracy of the learned flow networks. The paper doesn't provide sufficient analysis of why these errors are so high, nor does it demonstrate clear advantages over single-agent GFlowNets approaches.
- Little performance improvements over baselines. The marginal gains observed in the experiments do not provide compelling evidence for the effectiveness of the proposed MA-GFlowNet framework.
3. The paper doesn't adequately address the cyclic environment problem. GFlowNets traditionally work best in acyclic environments, but the paper doesn't explain how they handle cycles in StarCraft II scenarios. This is a critical omission, as cyclic transitions can significantly impact the training and performance of GFlowNets.
4. The motivation for using MA-GFN in the chosen tasks is not well justified. Many of the presented problems could potentially be solved more effectively with single-agent GFlowNets approaches. The paper does not provide a clear rationale for why a multi-agent approach is necessary or beneficial for the specific tasks considered.

### Questions
1. How does the proposed approach differ from Li et al. (2023)'s work on multi-agent GFlowNets? Please clarify the novel contributions relative to this prior work.
2. How does the proposed method handle cyclic state transitions in StarCraft II environments, given that GFlowNets traditionally assume acyclic state spaces?
3. The L1 errors shown in Figure 3 are quite high. Could the authors explain why this occurs and how it affects the practical utility of the method? What specific advantages does the MA-GFN approach offer over single-agent GFN solutions for the presented Grid tasks? Could the authors provide experimental comparisons?
4. Why is it evaluated only on the simplest 3m StarCraft II scenario? Have the authors tested your approach on more complex multi-agent scenarios?

### Soundness
1

### Presentation
1

### Contribution
2
