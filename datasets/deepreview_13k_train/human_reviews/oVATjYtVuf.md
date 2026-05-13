# Cross-Domain Reinforcement Learning Under Distinct State-Action Spaces Via Hybrid Q Functions

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Cross-domain reinforcement learning (CDRL) is meant to improve the data efficiency of RL by leveraging the data samples collected from a source domain to facilitate the learning in a similar target domain. Despite its potential, cross-domain transfer in RL is known to have two fundamental and intertwined challenges: (i) The source and target domains can have distinct state space or action space, and
this makes direct transfer infeasible and thereby requires more sophisticated interdomain mappings; (ii) The domain similarity in RL is not easily identifiable a priori, and hence CDRL can be prone to negative transfer. In this paper, we propose to jointly tackle these two challenges through the lens of hybrid Q functions. Specifically, we propose QAvatar, which combines the Q functions from both the source and target domains with a proper weight decay function. Through this design, we characterize the convergence behavior of QAvatar and thereby show that QAvatar achieves reliable transfer in the sense that it effectively leverages a source-domain Q function for knowledge transfer to the target domain. Through extensive experiments, we demonstrate that QAvatar achieves superior transferability across domains on a variety of RL benchmark tasks, such as locomotion and robot arm manipulation, even in the scenarios of potential negative transfer.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on cross-domain reinforcement learning and proposes QAvatar to solve transfer across tasks with different state-action spaces. QAvatar includes inter-task mapping learning and combines Q functions from source and target tasks with a proper weight decay function. Experiments are conducted on robotics tasks, compared with several previous transfer methods.

### Strengths
1. Learning the inter-task mapping via a Bellman-like loss function looks novel;
2. Both theoretical and empirical analysis are provided.

### Weaknesses
1. Although the paper provides theoretical analysis, it heavily depends on previous work.
2. The key implication 2 of Theorem 1 doesn't look original, as most transfer methods include a decay function, that can prevent negative transfer with a large training step t.
3. Some related work should be at least discussed [1-3] in this paper. At least one method with a theoretical guarantee should be compared, for example [3,4] to support the claim in the experiment section.
4. In Fig 1, it looks like SAC learn from scratch outperforms all other transfer baselines in most of the tasks. The proposed QAvatar is only slightly better than SAC learn from scratch (some of the results are not statistically significant as the errorbars are overlapped). is there any reason for that?

### Questions
In Fig 1, it looks like SAC learn from scratch outperforms all other transfer baselines in most of the tasks. The proposed QAvatar is only slightly better than SAC learn from scratch (some of the results are not statistically significant as the errorbars are overlapped). is there any reason for that?

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
3

### Summary
The paper proposes QAvatar, a novel CDRL framework that improves data efficiency by combining Q functions from both source and target domains with weight decay functions. Theoretical analysis shows that QAvatar effectively mitigates negative transfer while ensuring reliable transfer. Extensive experiments demonstrate significant improvements in data efficiency and robustness against negative transfer in various RL benchmark tasks.

### Strengths
1. QAvatar is a good cross-domain reinforcement learning framework that effectively improves data efficiency , showing great potential for application.

2. The cross-domain Bellman loss function proposed in the paper provides better performance guarantees.

3. The authors conducted extensive experiments, demonstrating that QAvatar achieves excellent results in various environments, indicating high reliability.

### Weaknesses
The experimental analysis for the lower quality source section is quite brief. Could you explain why the method performs so well on lower quality sources?

### Questions
See questions in Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a new framework for Cross-Domain Reinforcement Learning (CDRL) named QAvatar, which provides reliable knowledge transfer from a source-domain to a target domain via a weighted combination of the given source-domain Q function $Q_{src}$ and the learned target-domain Q function $Q_{tar}$. The proposed method can handle distinct state and action space between the source and target domains with performance guarantee. Additionally, the paper presents a practical implementation of QAvatar using a normalizing-flow-based state-action mapping and demonstrates its superior performance over a range of baseline methods through extensive experiments across various environments.

### Strengths
- The paper is well-written and easy to follow. The notations are well-explained, visualizations are clear and helpful in supporting the conclusions.
- The motivation and main idea of the proposed method is clear and practical.
- The proposed method can improve sample efficiency and avoid negative transfer, the authors provide both theoretical analysis and empirical experiments across a rich set of environments with various state and action dimensions. The conclusion from the empirical experiments are well aligned with the theoretical analysis.
- The proposed method is robust to low quality source-domain policy as well as negative transfer scenarios.
- Authors provide reproduction and sanity checks for their baseline methods.

### Weaknesses
 - The performance margin between QAvatar and some other baselines various dramatically across different environments. A more thorough explanation will be helpful.
- The proposed method still relies on the assumption that the target-domain agent has access to $Q_{src}$ and $V_{src}$ in addition to $\pi_{src}$. What if we only have access to a pre-trained policy from the source-domain and nothing else (that is more practical in most real-world application scenarios).
- The proposed framework can only handle knowledge transfer from one source-domain and one target-domain, and the inter-domain mapping is required to be trained from scratch for every source-target pair.

### Questions
- Why CAT outperformed QAvatar in Table wiping task, while QAvatar has significant advantages over CAT in other two Robosuite environments block lifting and door opening? block stacking and door opening should be harder than table wiping and they have higher state and action dimensions as well.
- What will happen if an adversarial source-domain policy is given ($Q_{src}$ is "opposite" to $Q_{tar}$ in some sense), will it harm the training process via the weighted sum mechanism between the $Q_{src}$ and $Q_{tar}$?

### Soundness
3

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
3

### Summary
This paper addresses cross-domain transfer in reinforcement learning (RL), particularly when the source and target domains have distinct state and action spaces. The authors propose CDRL, which combines Q-functions from the source and target domains, demonstrating its benefits in various RL tasks, including locomotion, robotic manipulation, and autonomous driving.

### Strengths
- The paper is generally well-written, with clear definitions and proofs.
- The authors provide sufficient experiments on diverse tasks, including locomotion, robotic manipulation, and autonomous driving.

### Weaknesses
 - QAvatar shows a slight improvement in data efficiency (as shown in Figure 1); however, it still requires a similar amount of training time as SAC, which learns from scratch. Since QAvatar involves training in both the source and target domains, it doubles the training time compared to SAC, which may achieve similar performance without requiring as much training time. This makes the claim of improved data efficiency questionable.
- In a similar context to the previous question, it seems that QAvatar requires full training in the source domain. According to Figure 4, if the source-domain model is not fully trained (e.g., of low quality), QAvatar provides no benefits in such cases; instead, it is more practical to train the model directly in the target doamin from scratch. Then, what is the benifict of the cross domain transfer in this context? Could the authors provide additional experiments with other baselines, such as FT or CAT, under the same settings?”
- Can the authors provide experiments on negative transfer in other locomotion tasks, such as Hopper, HalfCheetah, and Ant? Are there specific scenarios where QAvatar may fail to transfer effectively to the target domain?
- Can the authors provide more explanation for why the baseline methods, such as CAT, DCC, and CMD, fail to transfer? It appears that CMD use the same locomotion tasks in their original papers, but no performance improvement is observed in Figure 1.

### Questions
- Can the authors provide comparison with other RL algorithm as baseline such as TD3 or PPO?

### Soundness
3

### Presentation
3

### Contribution
2
