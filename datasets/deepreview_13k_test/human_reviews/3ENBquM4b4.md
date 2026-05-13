# Plasticity from Structured Sparsity: Mastering Continual Reinforcement Learning through Fine-grained Network Allocation and Dormant Neuron Exploration

- Decision: Reject
- Scores: 5, 5, 5, 8

## Abstract
Continual reinforcement learning faces a central challenge in striking a balance between plasticity and stability to mitigate catastrophic forgetting. In this paper, we introduce SSDE, a novel structure-based method that aims to improve plasticity through a fine-grained allocation strategy with Structured Sparsity and Dormant-guided Exploration. Specifically, SSDE decomposes the parameter space for each task into forward-transfer (frozen) parameters and task-specific (trainable) parameters. Crucially, these parameters are allocated by an efficient co-allocation scheme under sparse coding, ensuring sufficient trainable capacity for new tasks while promoting efficient forward transfer through frozen parameters. Furthermore, structure-based methods often suffer from rigidity due to the accumulation of non-trainable parameters, hindering exploration. To overcome this, we propose a novel exploration technique based on sensitivity-guided dormant neurons, which systematically identifies and resets insensitive parameters. Our comprehensive experiments demonstrate that SSDE outperforms current state-of-the-art methods and achieves a superior success rate of $95\%$% on CW10 Continual World benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a new structure-based method for plasticity and stability tradeoff  in continual RL. Specifically, the authors proposed (1) a sub-network co-allocation method which enhances meta sparse prompting by task-specific sparse prompting, (2) a finegrained masking method which only freeze exact parameters trained in previous tasks, and (3) a periodic resetting strategy for dormant neurons. However, this work is largely built upon previous works, which limits its technical contributions. And the reported experimental results are somewhat misleading. Thus, I lean towards reject at current stage.

### Strengths
1. The authors proposed to separate sub-network sparse prompting into global and task-specific levels, which seems effective in their ablation study. 

2. The introduction of parameter-level masking and dormant neuron resetting techniques is beneficial for mitigating plasticity loss and keeping the learning capability of networks. 

3. Combining the proposed techniques, the overall framework achieves higher computation efficiency.

### Weaknesses
1. This paper largely follows the technical parts of [1][2], which limits their own contribution. In detail,

1.1. The authors claim a crucial contribution of introducing task-level sparse prompting, which has also been proposed in [1], where the task dictionary is obtained through a dictionary learning algorithm using previous tasks' optimized prompts and their embedding. Here the authors sampled the task dictionary from N(0, 1) which shares the same distribution of global dictionary. I don't see the motivation of this choice. Could the authors elaborate more on this part and also detail the difference between [1] and their method?

1.2. In 4.2, since periodic dormant neuron resetting is well established in [2] for continual RL, it is inappropriate to claim this as a key contribution of their framework. In addition, the use of "exploration" is arguably misleading, which has various meanings in different contexts. I would suggest the authors use the specific term "structural exploration" throughout the paper for better clarification. 

2. There are many model choices made without sufficient justification. In addtion to 1.1, the proposed "sensitivity dormant scores" also lacks clear motivation. What is the advantage of this metric than previously defined dormant scores? And ablation study is necessary for justifying such choices. 

3. The experiments results seem misleading.

3.1. Throughout the experiments, their reproduced results of CoTASP has a huge gap with the reported ones in CoTASP's paper (e.g. for P: 0.73 v.s. 0.92 in CW10 and 0.74 v.s. 0.88 in CW20), which has no essential difference with SSDE (CW10) or even better (CW20). And the generation performance of SSDE is not reported for a fair comparison with previous methods. 

3.2. In addition, the results are quite misleading given the reported P in CoTASP. In Table 4, the average success of SSDE w/o Dormant is 0.85 while that of CoTASP which also don't use Dormant neuron resetting achieves 0.92. Does this indicate that the proposed co-allocation strategy is inferior to the allocation method in [1] which also use sparse prompting? 

4. The overall frameworks contain a lot of hyperparameters, such as the sparsity controlling parameters in Equation (3-4), the trade-off paramter in Equation (6), and the dormant threshold in Definition 4.1, which make the framework less practical. In addition, no ablation results are provided to show the robustness of the system to these hyperparameters. 

[1] Yang, Yijun, et al. "Continual task allocation in meta-policy network via sparse prompting." International Conference on Machine Learning. PMLR, 2023.

[2] Sokar, Ghada, et al. "The dormant neuron phenomenon in deep reinforcement learning." International Conference on Machine Learning. PMLR, 2023.

### Questions
**Regarding Weakness 1**:

Q1.1. Could the authors explicitly compare their task-level sparse prompting approach to that in [1], highlighting key methodological differences, and discuss any potential advantages of their approach over the method in [1]? 

Q1.2. Could the authors explain their motivation for sampling the task dictionary from N(0,1) rather than using dictionary learning?

Q1.3. Could the authors clarify how their use of dormant neuron resetting differs from or improves upon the approach in [2], and explain why they consider it a key contribution despite its prior use in continual RL?

**Regarding Weakness 2**:

Q2.1. Could the authors provide clear explanation of the advantages of their "sensitivity dormant scores" over previous dormant score definitions, and provide an ablation study comparing their "sensitivity dormant scores"  to other dormant score metrics?

Q2.2. Could the authors provide theoretical or empirical justification for their key model choices?

**Regarding Weakness 3.1**:

Q3.1. Could the authors explain the discrepancy between their reproduced CoTASP results and those reported in the original paper?

Q3.2. Could the authors provide generation performance results for SSDE for a fair comparison?

Q3.3. Could the authors discuss how the performance gap affects their conclusions about SSDE's effectiveness compared to CoTASP?

**Regarding Weakness 3.2**:

Q3.4. Could the author explain why their method performs inferior to [1] when dormant neuron resetting is not used, and provide additional analysis or experiments to clarify whether their co-allocation strategy offers advantages over the method in [1]?

Q3.5. Could the authors discuss potential reasons for the performance difference when dormant neuron resetting is not used and its implications for their method's effectiveness?

**Regarding Weakness 4**:

Q4.1. Could the authors provide a sensitivity analysis or ablation study for key hyperparameters to demonstrate the method's robustness?

Q4.2. Could the authors provide a discussion of strategies for hyperparameter selection in practical applications?

Q4.3. Could the authors provide a comparison of the number and sensitivity of hyperparameters in SSDE to those in baseline methods like CoTASP?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a structure-based method, SSDE, to enhance the plasticity-stability trade-off in continual reinforcement learning. It introduces a fine-grained allocation strategy that decomposes network parameters into fixed forward-transfer and task-specific trainable components. Furthermore, to improve the model’s exploration capability, this paper presents an exploration technique based on sensitivity-guided dormant neurons. Experiments conducted on the Continual World benchmark demonstrate that the proposed method achieves a superior success rate and outperforms current state-of-the-art methods in the CW10 task.

### Strengths
This paper addresses a critical issue in continual reinforcement learning: balancing plasticity and stability to mitigate catastrophic forgetting. The proposed method offers greater computational efficiency than existing approaches. Experimental results are promising, demonstrating that the proposed method achieves a higher success rate and outperforms other baseline methods on the CW10-v1 Continual World benchmark.

### Weaknesses
1. The paper can be improved in terms of writing/presentation.
2. From Table 3, it is evident that the author’s proposed method generally performs weaker than the ClonEx-SAC method. Therefore, will the ClonEx-SAC method continue to outperform the author’s method as the number of sequential tasks increases? Additionally, why doesn’t the forward transfer ability, or generalization ability, of the author’s method improve as the number of tasks increases?
3. The proposed sensitivity-guided dormant neurons offer limited novelty.
4. The author does not include comparisons with the latest regularization-based methods in continuous reinforcement learning, and the multi-task methods referenced are also outdated.

### Questions
1. If the differences between tasks are substantial, could using fixed forward-transfer parameters introduce issues that reduce flexibility?
2. Can the method proposed by the author continue adapting to additional tasks, and can its task completion performance still outperform other methods?
3. For additional issues, please refer to the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work introduces SSDE, a novel structure-based continual RL method. SSDE formulates an efficient co-allocation algorithm that enhances sub-network allocation by increasing the capacity for trainable parameters while leveraging frozen parameters for effective forward transfer from previous policies. SSDE introduces a trade-off parameter to balance these two groups of parameters in its fine-grained inference process.

### Strengths
(1)SSDE not only achieves SOTA stability standards but also achieves competitive plasticity even when compared to strong behavior cloning baselines that benefit from data replay.
(2)Experimental results demonstrate that SSDE outperforms current state-ofthe-art methods and achieves a superior success rate of 95% on the CW10-v1.

### Weaknesses
As shown in Table 3, SSDE takes no obvious advantages in F and FT metrics. These two metrics usually represent backward and forward transfer. So why Average Performance (P) is so good while F and FT not? I am a little confused. Also, ClonEx-SAC seems to perform comparably with SSDE on CW 20, although it replays data.

### Questions
(1)Can we have more continual RL tasks? In the existing version, CW tasks may be not very convincing, especially CW20. Maybe you can refer to [a] for more RL tasks to evaluate continual RL methods.
[a] Online Continual Learning for Interactive Instruction Following Agents, 2024
(2)\beta in Eq.6 is very important since it balance the stability and plasticity in CL. Could you show its sensitivity or how do you decide the optimal value.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a structure-based continual reinforcement learning algorithm. To address the stability-plasticity dilemma in the previous subnetwork allocation approaches, the authors propose a fine-grained allocation strategy with two key designs: (1) The parameter space is decomposed into forward-transfer and task-specific components, which are co-allocated by sparse coding to enhance plasticity. (2) The dormant neurons are periodically reactivated to improve exploration and rapid adaptation in new tasks. The proposed method is validated on the Continual World benchmark and shows significant simprovement in performance.

### Strengths
* The paper is generally well written and very informative.
* The technical contributions (fine-grained subnetwork allocation and dormant neuron re-activation) seem solid, both effectively addressing the stability-plasticity dilemma in continual reinforcement learning.
* The experimental results on the Continual World benchmark show great improvements over the existing baselines.

### Weaknesses
* The second contribution (dormant neuron re-activation) could be validated more carefully. There are already several works dealing with dormant neurons (e.g. [1, 2]), so a comparison with the existing literature in terms of method differences and experimental results would help to justify the contribution of this paper. Also, since the authors propose a new criterion for dormant neurons, it should be investigated how it overlaps with the original definition in [1], is it possible that it induces false positives and thus destabilizes the learning process? 
* The proposed method utilizes task embeddings from a pre-trained BERT, which limits its applicability in broader scenarios involving implicit knowledge that cannot be verbalized. For example, while BERT embeddings work fine in the Continual World benchmark involving manipulation tasks, they may be difficult to transfer to the Brax scenarios used in [3, 4] involving locomotion tasks. It would be interesting to see further experiments or discussions on this issue.
* Regarding efficiency, the authors only discussed their allocation time, but there is no mention of total training time and model size. These are more representative metrics for evaluating the efficiency of continual reinforcement learning, and should be reported in detail in the paper. Also, it would be better if the authors could include an intuitive figure of the performance-size or performance-training time tradeoff, perhaps like Figure 1 in [3] and Figure 4 in [4].
* There is a lack of sensitivity analysis for several hyperparameters, including $\beta$ in Equation (6), $\Delta$ in Equation (8) and $\tau$ for thresholding. The paper determined these hyperparameters by grid search, but I am curious if their choice is critical to the final performance and difficult to choose in practice. The authors could present a sensitivity analysis of these hyperparameters to address my concern, and additional studies of their generalizability across different types of tasks would be appreciated.

---

[1] Sokar, et al. The dormant neuron phenomenon in deep reinforcement learning. ICML 2023.

[2] Dohare, et al. Loss of plasticity in deep continual learning. Nature 2024.

[3] Gaya, et al. Building a subspace of policies for scalable continual learning. ICLR 2023.

[4] Sun, et al. Rewiring neurons in non-stationary environments. NeurIPS 2023.

### Questions
* Could the authors provide an intuitive explanation for the use of sparse coding in co-allocation? I agree with the general idea of enhancing plasticity with forward-transfer parameters [1], but I do not fully understand why they can be selected using sparse coding.

---

[1] Lin, et al. TRGP: Trust region gradient projection for continual learning. ICLR 2022.

### Soundness
3

### Presentation
2

### Contribution
3
