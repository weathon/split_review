# Prevalence of Negative Transfer in Continual Reinforcement Learning: Analyses and a Simple Baseline

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
We argue that the negative transfer problem occurring when the new task to learn arrives is an important problem that needs not be overlooked when developing effective Continual Reinforcement Learning (CRL) algorithms. Through comprehensive experimental validation, we demonstrate that such issue frequently exists in CRL and cannot be effectively addressed by several recent work on either mitigating plasticity loss of RL agents or enhancing the positive transfer in CRL scenario. To that end, we develop Reset & Distill (R&D), a simple yet highly effective baseline method, to overcome the negative transfer problem in CRL. R&D combines a strategy of resetting the agent's online actor and critic networks to learn a new task and an offline learning step for distilling the knowledge from the online actor and previous expert's action probabilities. We carried out extensive experiments on long sequence of Meta World tasks and show that our simple baseline method consistently outperforms recent approaches, achieving significantly higher success rates across a range of tasks. Our findings highlight the importance of considering negative transfer in CRL and emphasize the need for robust strategies like R&D to mitigate its detrimental effects.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work considers negative transfer problem in continual RL, where steam of RL tasks may severely hurt the policy's performance. The authors proposed to a method named Reset & Distill (R&D) for mitigating such issue. R&D stores  a copy of single-task policy as offline policy for each task in the task stream and also a subset of data of that task; and it then optimize the KL divergence between online policy and all offline policies on the stored data of prior tasks, and the KL divergence between online policy and offline policy of current task.

### Strengths
- Method is simple and plausible

- Empirical evaluation appears strong

### Weaknesses
 - I find the paper is a bit difficult to follow as a lot of concepts are described quite verbally such as negative/positive transfer and also the baselines -- although I am not familiar with the literature of continual RL, there might be room for clarity improvement for general RL audience with continual learning background

- Despite I like the visualization of Figure 2, and I understand the R&D is introduced after that, it might be more visually clear how R&D perform if the authors could also include R&D in Figure 2.

--- 

While I think continual RL could be an interesting area and the method proposed could be plausible to mitigate the negative transfer issue, the overall writing is somewhat verbal, hence slightly difficult to follow especially for people working in general RL. Besides, I am not sure if this evaluation is a standard evaluation protocol in the CRL community. Therefore, I find this paper is boarderline to me although with low confidence.

### Questions
- As I am not particularly familiar with the literature, I wonder do the baselines store copies of policies and data. If some of them have the same setting, storing policies and data, what are the corresponding budget, compared to R&D.

- Is the sequential evaluation of Meta World a standard benchmark in the CRL literature or it is customized in this work? (If it is customized, is there a commonly used CRL evaluation benchmark in the literature?)


---

post-rebuttal: 5 -> 6.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Authors demonstrate the existence of negative transfer in CRL setup and show that this issue can not be mitigated with previous CRL approaches. Authors also propose a solution to the problem which demonstrates strong reduction of the negative transfer effect

### Strengths
1. Authors reveal the existence of the negative transfer effect which might strongly affect the further research in CRL field. Further studies might take this aspect into consideration when designing novel approaches or applying existing for tasks of their interest.
2. The presence of the negative transfer is demonstrated across 3 different domains  (Meta World, DM and Atari) which provide significant evidence that the negative transfer might be a frequent effect.
3. Using a wide range of techniques it is shown that promoting positive transfer cannot address negative transfer.
4. The possible solution (R&D) for mitigating the negative transfer is presented. It it compared against multiple CRL approaches and shown to be effective.
5. Ablation study on hyperparamters effect for R&D is conducted.

### Weaknesses
1. While R&D reduces negative transfer effect, sometimes it suffers from forgetting more than other approaches.
2. When applied with SAC, R&D requires a vast amount of expert rollouts to keep the good performace. 
3. R&D performance is shown only on Meta World tasks if I understand correctly.

### Questions
I don't have any major concerns about this work. The only interesting thing for me would be to see the R&D performance on DM Control and Atari domains.

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
Author addresses the challenges of negative transfer in Continual Reinforcement Learning (CRL). Negative transfer occurs when learning new tasks negatively impacts performance, which is problematic for CRL systems that aim to handle multiple tasks sequentially without forgetting. The authors identify that existing CRL methods often focus on mitigating plasticity loss or promoting positive transfer, but these methods fail to effectively counteract negative transfer.
They propose a new baseline method called Reset & Distill (R&D) to address negative transfering problem. R&D works by resetting the agent’s online networks for each new task while preserving learned knowledge through distillation into an offline model. and this dual-actor setup, which allows an online network for current learning and an offline network for cumulative knowledge,enableing R&D to handle sequential tasks more effectively by preventing both negative transfer and forgetting. Experiments in their work demonstrate R&D outperforms other models on task success rates, emphasizing the need to prioritize countering negative transfer in CRL​, which seems promising

### Strengths
Firstly, it focuses on an important yet overlooked issue,the occurrence of negative transfer in Continual Reinforcement Learning (CRL). This problem has a significant impact in practical applications, but prior research has largely concentrated on preventing forgetting or promoting positive transfer, often neglecting negative transfer. Authorr introduces the "Reset & Distill" (R&D) method specifically to tackle this issue, demonstrating a strong sense of innovation and hitting the problem "right on target." The experimental design is also solid, verifying the prevalence of the negative transfer issue across different environments, such as Meta World, DeepMind Control Suite, and Atari, which adds credibility to the results. Additionally, the paper is written in a clear manner, particularly in explaining the design and implementation of the R&D method, making it easy for readers to understand the authors' approach. Overall, this paper brings fresh perspectives and practical solutions to the CRL field

### Weaknesses
While the paper does a good job of demonstrating the effectiveness of the R&D method through extensive experiments, it somewhat lacks a deep theoretical analysis explaining why this approach is effective at mitigating negative transfer. What are the fundamental mechanisms that allow R&D to sidestep the pitfalls of negative transfer?

### Questions
① Balancing Negative and Positive Transfer: The R&D method seems to heavily focus on preventing negative transfer by resetting the online learner's parameters. While this is a novel approach, I wonder about the potential for R&D to leverage positive transfer. Is there a way to modify R&D to harness the knowledge from previous tasks without incurring negative transfer? Your thoughts on this balance would be insightful.
② Theoretical Underpinnings: The paper does a great job showcasing the empirical success of R&D, but I must say, I'm left wanting more in terms of theoretical analysis. What are the theoretical reasons behind R&D's effectiveness in reducing negative transfer? How does the periodic reset and distillation process interact with the learning dynamics at a deeper level? A bit more depth here could really help solidify the contribution of your work.
③ Computational Cost: The dual-network architecture of R&D, with periodic resets and distillation, seems promising. However, I'm concerned about the computational overhead this might introduce, especially for resource-constrained settings. Could you discuss the computational efficiency of R&D and any potential strategies to mitigate these costs?

### Soundness
4

### Presentation
4

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
The paper proposes Reset and Distill (R&D), a method inspired by policy distillation [1] and neural network growth [2], to address catastrophic forgetting in knowledge transfer. R&D operates by reusing expert samples from previous tasks to transfer knowledge to subsequent ones while resetting the online learner network’s knowledge. The authors demonstrate, through comprehensive experiments, that the sequence of tasks [3] significantly affects performance when learning multiple tasks. 

*[1] Hinton, Geoffrey. "Distilling the Knowledge in a Neural Network." arXiv preprint arXiv:1503.02531 (2015).*

*[2] Rusu, Andrei A., et al. "Progressive neural networks." arXiv preprint arXiv:1606.04671 (2016).*

*[3] S. Narvekar, J. Sinapov, and P. Stone, “Autonomous task sequencing for customized curriculum design in reinforcement learning,” in (IJCAI), The 2017 International Joint Conference on Artificial Intelligence, 2017.*

### Strengths
* *Comprehensive literature review*: The authors provide a thorough and well-structured review of recent research related to plasticity loss in non-stationary environments and negative transfer in transfer learning. This positions the paper well in the context of existing research.

* *Robust experiments*: The empirical validation is solid, with experiments conducted on recognized benchmarks in the RL community. These experiments effectively test the assumption that the arrival order of tasks impacts learning performance, and R&D outperforms previous methods in mitigating catastrophic forgetting, providing valuable insights.

### Weaknesses
 * *Similarity with P&C*: In Figure 3, the concept of an "adaptor" within the Progress & Compress (P&C) framework is not well explained. While the term "reset" may be somewhat intuitive, it is not clearly detailed in either the main text or the Appendix. Given that the novelty of R&D is acknowledged to be marginal compared to P&C, a more in-depth discussion of how these concepts differ is necessary to strengthen the paper's contribution.

* *Sequence of tasks focus*: The paper emphasizes that the arrival order of tasks have impact in negative transfer, yet the proposed method does not directly address this issue. Instead, R&D relies on known techniques (distillation and resetting) to mitigate catastrophic forgetting.


* *Contradictory hypothesis*: The authors propose that *all prior knowledge from previous tasks should be erased* when learning a new task. However, this approach seems contradictory, as retaining certain previous knowledge can, in some cases, enhance learning, especially when tasks share high similarity.

### Questions
- [Q1] If task sequencing is feasible, could curriculum learning enhance R&D performance by optimizing task order?

- [Q2] It’s unclear why mitigating negative transfer does not necessarily imply facilitating positive transfer, and vice versa.

- [Q3] Could you provide more details about why Proximal Policy Optimization (PPO) appears more susceptible to negative transfer than Soft Actor-Critic (SAC)? Given the comparison between these algorithms, understanding the underlying reasons could offer valuable guidance for developing more robust approaches to continual learning.

### Soundness
3

### Presentation
4

### Contribution
2
