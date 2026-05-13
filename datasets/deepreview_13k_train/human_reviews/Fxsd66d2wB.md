# Decoupled Offline to Online finetuning via Dynamics Model

- Decision: Reject
- Scores: 6, 6, 6, 3, 6

## Abstract
Constrained by the sub-optimal dataset in offline reinforcement learning (RL), the offline trained agent should be online finetuned before deployment. Due to the conservative offline algorithms and unbalanced state distribution in offline dataset, offline to online finetuning faces severe distribution shift. This shift will disturb the policy improvement during online interaction, even a performance drop. A natural yet unexplored idea is whether policy improvement can be decoupled from distribution shift. In this work, we propose a decoupled offline to online finetuning framework using the dynamics model from model-based methods. During online interaction, only dynamics model is finetuned to overcome the distribution shift. Then the policy is finetuned in offline manner with finetuned dynamics and without further interaction. As a result, online stage only needs to deal with a simpler supervised dynamics learning, rather than the complex policy improvement with the interference from distribution shift. When finetuning the policy, we adopt the offline approach, which ensures the conservatism of the algorithm and fundamentally avoids the sudden performance crashes. We conduct extensive evaluation on the classical datasets of offline RL, demonstrating the effective elimination of distribution shift, stable and superior policy finetuning performance, and exceptional interaction efficiency within our decouple offline to online finetuning framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a two-stage approach to address the offline-to-online problem: first, fine-tuning the dynamic model using online data, and then extracting the policy with the MBPO method. Extensive experiments demonstrate that fine-tuning the dynamic model with online data improves the accuracy of estimating true environment dynamics, thereby enhancing policy extraction using MBPO.

### Strengths
1) Fine-tuning dynamic models with online data to support model-based RL is an intuitive approach.  
2) The paper is well-structured.  
3) The experiments effectively illustrate the distribution shift problem and demonstrate the impact of the proposed method.

### Weaknesses
1) The proposed method appears to be a technical fine-tuning extension of MBPO, a model-based offline RL method. While the proposed fine-tuning concept could potentially apply to other model-based offline RL methods, this paper focuses solely on MBPO without broader discussion.  
2) In Table 1, the authors list key differences between the proposed DOOF and other methods. However, there is the conceptual difference between the baseline methods **did not** attempt offline finetuning and **cannot** be applied to it. The authors should consider the key differences between DOOF and those methods.  
3) The experimental results lack convincing evidence. For example, only one seed is used in Table 4, despite Fig. 6(a) showing significant variance during offline fine-tuning. Additionally, there seems to be a statistical mismatch between Table 4 and Fig. 6. Please see detailed feedback in Questions.

### Questions
1) What is the value of the coefficient parameter $\lambda_{on}$ in Table 4?
2) There appears to be a statistical mismatch between Table 4 and Figure 6. For example, DOOF achieves 92.5 for HC-m in Table 4 after off(300k) finetuning, but in Figure 6, the highest results fluctuate around 80. Additionally, the pretrained offline result for WK-m in Table 4 is 77.7, yet almost all DOOF results with various coefficient factors are higher than 80. Therefore, using only one seed does not convincingly demonstrate the robustness of the improvement.
3) I appreciate that the authors demonstrate and discuss the dynamics estimation error with different quality datasets under Table 3. Similarly, the final improvements with varying dataset qualities could be discussed in depth. While data are presented in Table 4, it might be more straightforward to compare the average improvement across all tasks (HC, HP, WK) under different dataset qualities (r, m, mr) in a figure. Additionally, the authors mention “medium-expert” in the caption of Table 4 but do not include the results. It would be more comprehensive to include these results in future revisions if such datasets are available.

### Soundness
2

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
4

### Summary
The authors propose a decoupled model-based offline to online finetuning framework called DOOF. In the Online Finetuning stage, DOOF only updates the Dynamic model to mitigate the distribution shift, and then obtains Policy Improvement through Offline Finetuning. Experiments on D4RL validate the effectiveness of the method.

### Strengths
1. The authors propose an interesting perspective to solve the distribution shift problem in the Offline-to-Online stage, i.e., decoupling the elimination of distribution shift and policy improvement.
2. The authors provide a clear analysis of the sources of distribution error in the Offline-to-Online stage, which naturally leads to the proposed method.
3. The paper is clearly written.

### Weaknesses
The experimental design is not comprehensive enough.

### Questions
1. Why can't you compare with some specialized Offline-to-Online algorithms? You can set their Online interaction steps to 10k like yours, and report their Finetuning performance. If such a comparison is possible, I suggest increasing the Online interaction step budget to compare the final asymptotic performance.
2. The number of environments involved in the paper is limited. D4RL is a basic Offline Benchmark, and I suggest evaluating on more updated tasks.
3. Regarding the off(300k) baseline, does it mean that the initial Offline data, plus the 10k data from online interaction, are used for the final 300k offline gradient steps?

I'm willing to reconsider my score based on the new information provided in the Rebuttal stage.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper aims to address the decoupling of distribution shifts and policy improvement. They propose to only fine-tune the dynamics model online to address the distribution shift while leaving the policy improvement stage still performed on offline data. They employ empirical studies on classical offline RL datasets and demonstrate the effectiveness within the offline to online problems.

### Strengths
+ The paper provides a great summary of different state-of-the-art algorithms in Table 1, showing clearly how different algorithms approach offline to online fine-tuning problems;

+ The paper analyzes the distributions and shows them in clear visualization to demonstrate for example the reason for using an additional reward term.

### Weaknesses
The algorithmic innovations seem limited in the paper, it looks like moving the policy fine-tuning from the online stage into the offline stage with the online collected datasets used for fine-tuning the dynamics model.

### Questions
Since we have an online stage to finetune the dynamics model, what are the actual advantages of using offline methods to fine-tune the policy instead of using the online methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a model-based offline RL method that decouples environment dynamics model fine-tuning from policy optimization. 
It adopts an offline-online-offline manner that differs from previous work mainly in that it only fine-tunes dynamics model in the online stage, 
and introduce an additional offline stage to fine-tune policy based on extended dataset and fine-tuned dynamics model.

### Strengths
This paper introduces a model-based offline RL method that decouples environment dynamics model fine-tuning from policy optimization, which is an intuitively appealing motivation.

### Weaknesses
1. The idea of the article is relatively intuitive, but its effectiveness lacks theoretical proof. Additionally, there may be an error in Equation (5), as each of the three terms on the right side is missing a constant coefficient.
2. There is no formal definition of the three types of state-action pairs: ID state-action pairs, ID state but OOD action pairs, and totally OOD state-action pairs.
3. Experiments were only conducted on a subset of the datasets in D4RL (Halfcheetah, Hopper, Walker2D, Pen). Firstly, the computational cost of conducting experiments in D4RL is not high, and there are other environments in Mujoco like Ant, as well as environments in Adroit like Hammer, Door, and Relocate. D4RL also includes Maze-like environments and kitchen-like environments, among others. Secondly, most datasets used in this paper were collected by RL agents, and the feature distribution of these datasets differs significantly from that of data collected by human experts. Therefore, it is unknown whether the method is applicable to human data.
4. DOOF is a model-based offline RL method, but most of the experimental results are compared with model-free offline RL methods, as shown in Table 4. (According to the introduction in Section 4, only FOWM is a model-based method.)
5. The rationality of the evaluation indicators needs to be questioned. For example, in Section 5.2, TV is calculated on the data in the fake buffer, which satisfies a special distribution. Whether the TV calculated on this distribution is representative is unknown. Similarly, the results in Table 3 can only prove that DOOF can reduce TV on the data distribution represented by the fake buffer.
6. The experimental scenarios are not consistent. Table 4 provides experimental results for the four environments Halfcheetah, Hopper, Walker2D, and Pen, while Table 3 does not include experimental results for Pen. Similarly, the experimental results in Fig.1-4 also only include results from some of the environments.

### Questions
1. Regarding Equation (3), by splitting the left side into the sum of the two terms on the right side, can it be demonstrated that the first term will decrease when fine-tuning $\hat{M}$? When optimizing $\pi_{off}$, will the second term decrease without causing the first term to increase?
2. Is it reasonable to calculate TV on the data in the fake buffer? Why not randomly sample states and actions in the environment and calculate TV?
3. If online fine-tuning of the world model is possible, why not use a random policy to sample data in the environment and learn the world model entirely based on this data; or only use reward based on uncertainty and no longer use the original reward from the environment?
4. Fig.2 presents experimental results obtained on the specific task of Walker2D. Whether the insights gained from this result are universal and sufficient to support the motivation for designing the algorithm is questionable.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors study the problem of an offline to online fine-tuning framework in model-based RL. To address the trade-off between policy optimization and distribution shift elimination, DOOF (Decoupled Offline to Online Fine-tuning) suggests a method that decouples the elimination of distribution shift from the policy improvement process. This means they utilize the fine-tuned dynamics model trained with OOD actions and unbalanced states to assist in the fine-tuning of the policy in an offline mode, without additional interaction with the environment.

### Strengths
* I think the paper provides a clear intuition for offline to online RL using a model-based approach. In equation (5), the performance difference represents the expected dynamic distance of the offline dataset, conservatism on OOD actions, and unbalanced state distribution. Also, they show the distribution of total variation distance and uncertainty figures. It clearly explains what data is needed for fine-tuning the dynamics.
* Compared to existing offline RL algorithms, DOOF has high performance, despite only 10k online interaction steps. It significantly reduces the sample complexity.

### Weaknesses
 * In Section 3.1, the authors assume minimal expected distance within the distribution of the offline dataset, overlooking a key limitation: even if specific state-action pairs are present in the offline dataset, the small sample size of some pairs can lead to significant uncertainty between the learned and true dynamics. I recommend that the authors address this limitation directly, discussing its implications for the reliability of their method in practice, particularly under conditions of sparsity in the offline dataset.
   * This issue is underscored in prior work on model-based offline RL, as noted in Theorem 1 of [1].
   * Figure 1 (the distribution of total variation distance on the WK-m dataset) further illustrates this, where the orange distribution (offline dataset) shows substantial overlap with the blue distribution (OOD actions).

* The theoretical results presented indeed appear to rely substantially on prior work by Yu et al. (2020) and Luo et al. (2018), without providing additional theoretical guarantees, such as a formal proof that the policy trained by the DOOF algorithm converges to the optimal policy. This raises questions about the potential advantages of DOOF over existing algorithms. To strengthen their theoretical contribution, the authors should explore convergence guarantees or derive performance bounds for their decoupled approach, highlighting how it compares with established methods in the field.

* The uncertainty u(s,a) indeed relies on a strong assumption, as seen in Yu et al. (2020). More recent works ([1] and [2]) have addressed this by redefining u(s,a) based on state-action pair frequency and Bellman estimation inconsistency, potentially offering a more precise measure. How about comparing their uncertainty measure with these newer approaches and discussing the benefits or limitations of incorporating these alternative interpretations within their framework?

### Questions
In addition to questions about potential weaknesses, I would like to raise a few more questions:

* Observing Equation (6), modifying the reward to encourage optimistic exploration appears very similar to UCB methods, which are commonly used in online RL.
* In Table 3, the distance differences seem almost identical regardless of the value of $\lambda_{on}$. Does this imply that simply collecting synthetic data with optimistic rewards suffices?
* $\lambda_{on}$ is also a hyperparameter; what is the optimal way to select it?
* In Appendix C.3, the offline penalty coefficient differs from the MOPO official coefficient. Did they tune it separately?

### Soundness
3

### Presentation
3

### Contribution
3
