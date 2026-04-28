# Closed-Form Merging of Parameter-Efficient Modules for Federated Continual Learning

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
Model merging has emerged as a crucial technique in Deep Learning, enabling the integration of multiple models into a unified system while preserving performance and scalability. In this respect, the compositional properties of low-rank adaptation techniques (e.g., LoRA) have proven beneficial, as simple averaging LoRA modules yields a single model that mostly integrates the capabilities of all individual modules. Building on LoRA, we take a step further by imposing that the merged model matches the responses of all learned modules. Solving this objective in closed form yields an indeterminate system with $A$ and $B$ as unknown variables, indicating the existence of infinitely many closed-form solutions. To address this challenge, we introduce \methname, an alternating optimization strategy that trains one LoRA matrix at a time. This allows solving for each unknown variable individually, thus finding a unique solution. We apply our proposed methodology to Federated Class-Incremental Learning (FCIL), ensuring alignment of model responses both between clients and across tasks. Our method demonstrates state-of-the-art performance across a range of FCIL scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel optimization method for Federated Class-incremental Learning (FCIL). Based on the LoRA approaches, the authors propose a optimization method to estimate the two low-rank matrices effiently. Rather than the previous approaches upon the various types of assumptions, the proposed algorithm employed the alternating optimization methods by optimizing the two low-rank matrices separately by fixing the other one. The optimization methods was evaluated in the scenario of FCIL, which shows the state-of-the-art performance for CIFAR-100 and ImageNet-R dataset even with the various evalutation settings.

### Strengths
The target problem and the contribution are well presented in the paper, and the following mathetmatical derivation is also easy to follow. The experimental results verify the effectiveness of the proposed algorithm, and futher ablation studies are well designed to prove the component-wise effectiveness and the mentioned contributions.

### Weaknesses
Even with the above mentioned strengths, I have several concerns about the technical algorithm and evaluations as follows:

- Contribution (Alternative optimization vs. closed-form):
 The authors emphasized the contribution of this paper as the alternating optimization and the closed-form optimization. However, the relationship between the two different optimization methods is not precisely described. As I understood, the closed-form optimization is performed at each iteration for the respective low-rank matices, and the overall optimization solver follows the mechanism of alternating optimization. Since the two optimization approaches are definitely different to each other, the authors should specify the relationship of the two contributions.

- Convergence check for the optimization solver:
 When we design the optimization solver, it is important to check its convergence. When the optimization fails to convergence, the solution can be diverged, which causes serious problems. If the convergence check fails, the strategy to stop the iteration should be given. In the paper, both the convergence check and the stop criterion are not described.

- Validity of alternating optimization:
 The approach of alternating optimization is one of the most common optimization solvers. When we employ the alternating optimization approach by fixing one other of two parameters, it is important to check the relationship between the two parameters. When the two paraemters are not indenpendent to each other, the iteration with separated optimization can cause serious problem where the basic assumption for the two parameter can be broken. To prevent the issue, the conventional alternating optimization employs a penalty term where the relationship between two optimizing parameters can be preserved as the iteration goes. I hope to know that the proposed algorithm considers the relationship between the two low-rank matrices or the two low-rank matrices are independent to each other.

- Additional measurements:
 The quantitative results are present only by the average accuracy for entire classes. However, to evaluate the FCIL method, tthe measurements of he average forgetting and accuracy of all seen classes in the final task are meaningful. To show the effectiveness of the proposed algorithm for the last rounds and the final round, I recommend such additional measurements in the tables.

- Comparison fairness:
 It seems that the most recent study (PILoRA) shows low performance upon ImageNet-R dataset. Of course, the performance can be dramatically dropped in the new dataset, but it shows too large gap between its reported performance with the ImageNet-based dataset. I hope to know the reason why the large gap happens.

### Questions
The validity of the optimization solver should be checked.
The lack of evaluation metrics should be supplemented to show the effectiveness of the proposed algorithm.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the model merging, specifically focusing on merging the low-rank adaptation (LoRA) modules. The author proposed to extend the work of RegMean to merge LoRA modules in a closed form, where the challenge lies in the infeasibility of solving the indeterminate system introduced by the LoRA modules. The author further proposes an alternative optimization algorithm, i.e., freezing one of the two matrices, A and B, in the LoRA modules and optimizing each alternatively. The author chose the federal class incremental learning as the case study for the proposed method, conducted extensive experiments to verify the effectiveness of proposed method.

### Strengths
1. The extension of RegMean for merging the LoRA module is interesting. Given the extensive applicability of the LoRA for parameter-efficient fine-tuning for foundation models, the reviewer believes that the proposed method may benefit a broad range of applications in the future.

2. The proposed alternative optimization procedure for extending RegMean to Low-rank Regression Mean (LoRM) is intuitive and sound. It is promising that the algorithm can converge quickly in practice, as shown in Fig. 2, compared to the methods that achieved the state-of-the-art (SOTA) results previously.

3. The chosen testbed, i.e., the federal class incremental learning (FCIL), is a surging research direction in continual learning with real-world board applications. The author conducted extensive comparisons with different methods and showed the superiority of the LoRM, which vastly improved the SOTA of FCIL.

4. The code has been attached for replication, which will benefit future study.

### Weaknesses
1. Since the proposed method is general for model merging, the reviewer may want to see whether it can achieve good results in different applications, e.g., parameter-efficient fine-tuning and class-incremental learning in computer vision and/or natural language processing.

2. Although the author shows that the LoRM can converge quickly in practice, the reviewer still wonders whether there are any theoretical guarantees for its convergence.

### Questions
Please refer to the Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Low-rank Regression Mean (LoRM) is a novel method to merge LoRA (Low-Rank Adaptation) modules in a closed-form solution specifically designed for Federated Class-Incremental Learning (FCIL) by alternatively freezing and merging A and B submatrices of LoRA method.

### Strengths
The method is privacy preserving and enables continual merging for the Image Classification experiments shown.

### Weaknesses
**Inadequate Experimental Diversity** LoRM builds on LoRA, a parameter efficient finetuning method which was introduced to finetune large LLMs and other large, computationally expensive models for diverse and complex tasks. However, LoRM is only tested on the task of image classification and on a single backbone. This counteracts the motivation of using LoRAs (and LoRM is specific to only LoRAs). Experiments with different backbones - LLM, text-image models and diverse tasks like commonsense reasoning, text to image generation - where LoRA modules are regualrly - are necessary to show the efficacy of LoRM, especially since the contributions in the work are backed by only empirical results. LoRM's effectiveness across other federated learning tasks also remains unclear. Testing LoRM in other tasks, such as reinforcement learning or generative tasks, would strengthen its generalizability​.

**Sensitivity to Data Distribution**: LoRM’s performance may degrade with extreme data heterogeneity. The method could benefit from further optimization or regularization to ensure robustness across highly imbalanced data distributions typical in federated settings​.

It is unclear why the alternating freezing is needed? Why not train another LoRA which combines the previous base model+ LoRA weights? That appears to be the simplest solution to the model merging problem and would avoid problems like highly imbalanced data distributions across different tasks which could lead to load imbalance on particular matrices. Ablation for this would also have been helpful.

Comparisons to model merging and lora merging methods like [1, 2] are needed since this method focuses on this very aspect.

[1] Stoica et al. - ZipIt! Merging Models from Different Tasks without Training
[2] Yadav et. al - TIES-Merging: Resolving Interference When Merging Models

### Questions
Please refer to the questions in the weakness section

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a solution for federated continual  learning, where information is learned across multiple devices, with each device continually learning sets of disjoint classes. The proposed method proposes a two stage approach. The first stage involves learning LoRA modules in an alternating cycle, where one of the A or B matrices is kept frozen at a time while the other is optimized across individual devices. Once this has been done for all tasks across all devices, the LoRA matrices are aggregated one final time using RegMean to create one model with knowledge from each device across all tasks. The proposed method outperforms presented CIL and FCIL

### Strengths
- Adequate novelty is shown by introducing a training scheme that can properly update LoRA modules across multiple clients.  

- LoRM preserves privacy between devices by using Gram matrices 

- Ablations clearly show the importance of the proposed components.  

- Provided results show significant improvement over SOTA.  

- Extremely detailed list of parameters for all experiments is provided, greatly aiding replication.  

- Very straightforward organization, the paper flows logically and is easy to read.

### Weaknesses
- The paper mentions  that there is relatively little work in FCIL, a brief diagram visualizing the problem setup would greatly aid in understanding the problem.  

- Figure diagrams, namely Figure 1 requires more detailed captions. - The current SOTA for exemplar free CIL, RANPAC, is missing from the comparison list, this method also uses Gram matrices collecting information across tasks, so a comparison where it is adapted to be a FCIL method would be relevant.  

- The Previous SOTA, PILoRA shows results for both Quantity-based label imbalance and Distribution-based label imbalance, but results in this paper are only shown for Distribution-based.

### Questions
- Replicated results appear to be conflicting with previous works (L2P and TARGET’s relative ranking is switched in the PILoRA paper). Is there a reason for this discrepancy?  

- It is unusual to see L2P outperforming Coda-P, as Coda-P outperforms L2P in the standard CIL setting. What is the reason for this? How do RANPAC (https://arxiv.org/abs/2307.02251) and DualPrompt (https://arxiv.org/abs/2204.04799) compare? Does this inverse relationship between CIL accuracy and FCIL accuracy hold?  

- ImageNet-A, CUB, and Cars196 have been shown to be more challenging datasets for CIL methods, with wider gaps in accuracy when comparing techniques. How does LoRM perform on these datasets?

### Soundness
3

### Presentation
3

### Contribution
3
