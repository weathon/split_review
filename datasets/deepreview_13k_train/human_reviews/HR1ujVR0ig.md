# Learning Generalizable Skills from Offline Multi-Task Data for Multi-Agent Cooperation

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Learning cooperative multi-agent policy from offline multi-task data that can generalize to unseen tasks with varying numbers of agents and targets is an attractive problem in many scenarios.
Although aggregating general behavior patterns among multiple tasks as skills to improve policy transfer is a promising approach,
two primary challenges hinder the further advancement of skill learning in offline multi-task MARL. 
Firstly, extracting general cooperative behaviors from various action sequences as common skills lack bringing cooperative temporal knowledge into them.
Secondly, existing works only involve common skills and can not adaptively choose independent knowledge as task-specific skills in each task for fine-grained action execution.
To address these challenges, we propose an approach named Hierarchical and Separate Skill Discovering (HiSSD) for generalizable offline multi-task MARL through skill learning.
HiSSD leverages a hierarchical framework that jointly learns common and task-specific skills.
The common skills learn cooperative temporal knowledge and enable in-sample exploration for offline multi-task MARL.
The task-specific skills represent the priors of each task and achieve a task-guided fine-grained action execution.
To verify the advancement of our method, we conduct experiments on multi-agent MuJoCo and SMAC benchmarks.
After training policy using HiSSD on offline multi-task data, the empirical results show that HiSSD assigns effective cooperative behaviors and obtains superior performance in unseen tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new method called Hierarchical and Separate Skill Discovering (HiSSD) for learning generalizable multi-agent policies from offline multi-task data. The key idea is to jointly learn common skills that capture cooperative behaviors across tasks, as well as task-specific skills for fine-grained action execution. The method uses a hierarchical framework with a high-level planner that learns common skills and a low-level controller that learns task-specific skills. Experiments on SMAC and Multi-Agent MuJoCo benchmarks show improved generalization to unseen tasks compared to baselines. Overall, this paper presents a novel and effective approach to an important problem in multi-agent RL. With some additional analysis and clarifications, it would make a good contribution to the field.

### Strengths
1. Novel approach to learning generalizable multi-agent policies by jointly learning common and task-specific skills.

2. Theoretical analysis and derivation of objectives for skill learning.

3. Comprehensive experiments on multiple benchmarks showing improved generalization.

4. Addresses an important problem in multi-agent RL of transferring to tasks with varying numbers of agents.

5. The authors have shared comprehensive details of implementation along with codebase, which further bolsters the experimental efforts.

### Weaknesses
1. Ablation study can be further expanded to have a comprehensive analysis of different components. Comparison to some recent related works like HyGen is missing.

### Questions
1. There is a very recent work that tackles the same problem from a different methodology perspective found here : "Variational Offline Multi-agent Skill Discovery" by Chen et. al. I would like to know the authors' thoughts on how their methodology is different from this work, and if there are scenarios where one or the other might work well/worse.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes HiSSD to leverage a hierarchical framework to jointly learn the common and task-specific skills in offline MARL settings. Experiments in SMAC and multi-agent MuJoCo show its effectiveness and generalizability to different tasks.

### Strengths
1.	The division into common and task-specific skills provides a balance between generalization and task adaptation, addressing the limitations of previous methods that only focused on common skills.
2.	The proposed objective to learn common skills for exploration and prediction is new.
3.	HiSSD enables multi-agent policy transfer across varying tasks, outperforming existing multi-task MARL baselines on two benchmarks

### Weaknesses
1.	HiSSD’s hierarchical design and multi-component training can lead to instability. I think the authors should reveal more about the training details, hyperparameters selection, and tuning methods. 
2.	It can be better to present an algorithm of the whole training process and the execution process for understanding. 
3.	In the ablation studies, the HiSSD variants (e.g., w/o Planning and Half-Negative) often show strong performance compared to HiSSD with minor differences or even surpassing HiSSD. 
4.	The visualization experiments do not show clear evidence about the latent skills. For example, the task-specific skills in the same task seem closer in Figure 3.

### Questions
1.	From Equation (3), does $q(s_{t+1}\mid c_t^{1:K})$ has any meaning in real? How does HiSSD model the sequence $c_t^{1:K}$?
2.	If the negative samples are drawn from limited seen tasks when doing task-specific skill learning, how can we ensure a correct skill when facing unseen task distribution?
3.	Why are the two baselines, ITD3-CQL and ITD3-BC, not compared in the SMAC experiments?
4.	How is the performance if we only adopt a common skill without using the task-specific skills?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a hierarchical framework, HiSSD, for jointly learning common and task-specific skills from offline multi-task datasets. The common skills represent the general cooperation patterns, while task-specific skills achieve a task-guided fine-grained action execution. The algorithm is broken up into two phases. In the first phase, the high-level planner discovers common skills. In the second stage, the low-level controller learns task-specific skills.

### Strengths
1. The paper is well written, with thorough experiments, and a variety of tasks across two environments.
2. In order to achieve better performances in cooperative multi-agent environments, the paper brings cooperative temporal knowledge into common skills, which is reasonable.

### Weaknesses
1. According to the paper, HiSSD is superior to previous skill-based methods like ODIS because it brings cooperative temporal knowledge into common skills and discovers task-specific skills that can distinguish each task’s specific knowledge. However, HiSSD fails to outperform ODIS in some tasks, particularly the large-scale scenarios in SMAC, which raises questions about the method's robustness across varying task complexities.
2. In MAMuJoCo, the paper didn't use ODIS as a baseline, which is a missed opportunity for a direct comparison, especially given ODIS's strong performance in SMAC. This lack of a consistent baseline makes it difficult to assess the true relative performance of HiSSD in a different environment.
3. The process of learning skills is similar to imitation learning, which may limit its generalization ability to unseen tasks, especially those that are significantly different from the training distribution. For example, in Table 1, the win rates for 10m12m and 13m15m are lower than 10% with the medium-quality dataset, suggesting a potential weakness in handling out-of-distribution scenarios.
4. In the passage, some verbs sound a bit odd. For example, 'contain' in the sentence 'Equipping offline multi-task MARL with skill learning to improve policy transfer still contains issues.'
5. One concern for the paper is to evaluate HiSSD in maps that are more difficult (like the Stalker-Zealot task set in ODIS), to validate its effectiveness, especially given the method's stated goal of improving generalization across tasks.

### Questions
- In Table 3, I wonder why presents BC-best's results, rather than ODIS. ODIS seems to be the baseline with the best performances.
- In Figure 3, Large-scale tasks (i.e., 10m and 12m) overlap with each other but small-scale tasks don't. The paper said this is because 10m and 12m are similar. However, 3m, 4m, and 5m are also similar. I would appreciate some further discussion about this.
- In Equation 6, the weight $\alpha$ serves as the trade-off between guiding to space with high-reward and space that the execution policy ought to have a correct imitation. I wonder why the paper didn't conduct a sensitive analysis for this parameter like $\beta$ in Equation 11, as shown in Appendix E.2.
- The task-specific skills learn task-specific knowledge of source tasks, why do these skills play an important role in unseen tasks?

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
This paper introduces Hierarchical and Separate Skill Discovering (HiSSD), a method for learning generalizable skills in offline multi-task multi-agent reinforcement learning. HiSSD's hierarchical framework simultaneously learns common skills (cooperative behaviors across tasks) and task-specific skills (unique task characteristics). It uses an objective function combining reward maximization and next-state prediction for common skills, and contrastive learning for task-specific skills. HiSSD trains on offline data and enables decentralized execution with local information during testing.

### Strengths
This paper introduces Hierarchical and Separate Skill Discovering (HiSSD), a method for learning generalizable skills in offline multi-task multi-agent reinforcement learning. HiSSD's key strength is its hierarchical framework that simultaneously learns common and task-specific skills, overcoming existing limitations. It enables fine-grained action execution and trains using only offline data. During testing, HiSSD allows decentralized execution using local information and learned skills without centralized control. Experiments on SMAC and MAMuJoCo benchmarks showed HiSSD's performance improvements, especially in unseen tasks.

### Weaknesses
While the paper claims to integrate cooperative temporal knowledge into the process of learning common skills, it fails to adequately explain the clear causal relationship or mechanism between these two concepts. There appears to be a logical leap in assuming that simply performing global state prediction and value estimation directly leads to the learning of cooperative knowledge. Furthermore, the paper lacks a clear definition of what exactly "cooperative temporal knowledge" means and how it is measured and evaluated. This ambiguity makes it difficult to verify whether this knowledge has been learned. Specifically, the paper does not detail how the global state prediction is explicitly used to promote cooperation, nor does it explain how the value estimation, which is inherently a scalar, captures the complex temporal dynamics of multi-agent interactions. The connection between predicting a future state and the emergence of cooperative behavior is not sufficiently justified, and the paper would benefit from a more rigorous explanation of this link.

### Questions
* Can you explain how performing global state prediction and value estimation directly leads to learning cooperative knowledge?
* HiSSD claims to simultaneously learn common skills and task-specific skills, but how did you verify how distinct these two types of skills actually are? Was there any overlap or interference between the two skills?

### Soundness
3

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
3

### Summary
This paper proposes an algorithm for multi-task multi-agent skill discovery from offline data, which is a quite meaningful and challenging research direction. The novelty (compared with ODIS) mainly lies in jointly learning common and task-specific skills.

### Strengths
(a) This paper targets at a challenging problem setup, i.e., recovering generalizable multi-agent skills from multi-task offline data.

(b) The evaluation results are sufficient and show consistent improvements over the SOTA algorithm -- ODIS.

### Weaknesses
(a) The algorithm framework, including both the multiple components to learn (Fig. 1) and the objective design (Eqs. 4, 7, 11), is quite convoluted compared to ODIS, which could potentially bring training difficulty.

(b) The writing needs to be significantly improved, especially for methodology part in Section 3. 

(c) It's not clear why the common skills can integrate cooperative temporal knowledge and enable an offline exploration.

(d) Since all tasks share the same space for the local skills z^{1:K}_t, why z can embed task-specific knowledge?

(e) Multi-agent skills should provide abstractions at both temporal-level and subgroup-level. That is, each multi-agent skill should embed a (short) control sequence of a subgroup of agents. How is this aspect shown in the algorithm design?

(f) Thanks for releasing the code package. But it seems that the authors only made minimal changes to the readme file provided by ODIS. Please provide a detailed instruction (in the readme file) on how to reproduce all the reported results in this paper. Also, the released yaml files do not include the ones for MAMuJoCo.

### Questions
Please see the weakness part.

### Soundness
2

### Presentation
2

### Contribution
3
