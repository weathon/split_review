# Federated Few-Shot Class-Incremental Learning

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 5, 6, 6, 8

## Abstract
This study proposes a challenging yet practical Federated Few-Shot Class-Incremental Learning (FFSCIL) problem, where clients only hold very few samples for new classes.  We develop a novel Unified Optimized Prototype Prompt (UOPP) model to simultaneously handle catastrophic forgetting, over-fitting, and prototype bias in FFSCIL. UOPP utilizes task-wise prompt learning to mitigate task interference and over-fitting, unified static-dynamic prototypes to achieve a stability-plasticity balance, and adaptive dual heads for enhanced inferences. Dynamic prototypes represent new classes in the current few-shot task and are rectified to deal with prototype bias. Our comprehensive experimental results show that UOPP significantly outperforms state-of-the-art (SOTA) methods on three datasets with improvements up to $76\%$ on average accuracy and $67\%$ on balance mean accuracy respectively. Our extensive analysis shows UOPP robustness in various numbers of local clients and global rounds, low communication costs, and moderate running time. The source code of UOPP is publicly available at \url{https://anonymous.4open.science/r/op71m15}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel model named Unified Optimized Prototype Prompt (UOPP) to address the Federated Few-Shot Class-Incremental Learning (FFSCIL) problem. This problem is characterized by clients holding very few samples for new classes, which presents challenges such as catastrophic forgetting, overfitting, and prototype bias. The UOPP model incorporates task-wise prompt learning, unified static-dynamic prototypes optimized by Neural Ordinary Differential Equations (ODEs), and adaptive dual heads for enhanced inference. The dynamic prototypes are particularly designed to rectify prototype bias, which is a significant issue in few-shot learning scenarios. It defines the Federated Few-Shot Class-Incremental Learning (FFSCIL) problem and proposes the UOPP model to address it. UOPP uses prompt learning and dynamic prototypes to handle task interference, overfitting, and prototype bias. Experiments show UOPP outperforms existing methods on three datasets, with up to 76% higher accuracy and 67% better balance mean accuracy. It provides theoretical studies on the convergence and generalization of the UOPP method. It shows that UOPP is robust under various numbers of local clients and global rounds, with low communication costs and moderate running time.

### Strengths
1. The paper presents a novel solution for the challenging Federated Few-Shot Class-Incremental Learning (FFSCIL) problem, combining few-shot learning with federated learning. The UOPP model addresses this by integrating prompt learning, dynamic prototypes, and a dual-head classifier, showing high effectiveness.

2. The UOPP model excels on benchmark datasets, surpassing existing methods and proving its real-world applicability. It's supported by a robust theoretical framework that ensures convergence and generalization.

3. The UOPP model's utilization of dynamic prototype rectification through Neural Ordinary Differential Equations (ODEs) is a significant technical strength. This approach allows for the continuous optimization of prototypes, which are critical for representing new classes in few-shot learning scenarios. 

4. Designed with practical considerations in mind, UOPP respects data privacy, optimizes communication efficiency, and accommodates computational constraints, making it an ideal solution for federated learning environments. 

5. Enhancing transparency and fostering further research, the paper makes the UOPP source code publicly available.

### Weaknesses
1.The paper lacks a discussion on the future outlook and limitations of the method, which could provide a more comprehensive understanding of the research's implications, potential areas for advancement, and the constraints that may affect its practical application in various scenarios.

2 In federated learning, there's always a risk of introducing bias due to non-i.i.d. data distribution across clients, which the paper might not fully address. The paper should include a more rigorous analysis of how the model performs under varying degrees of data heterogeneity, including scenarios with significant class imbalance across clients, and how this impacts the convergence and generalization of the UOPP model.

3. There is a need for a more detailed analysis on how the model's performance is affected over extended periods and with a growing number of tasks, including the sustainability of its memory retention and its ability to adapt to new data without significant decreases in accuracy on previously learned tasks. The paper should investigate the long-term stability of the model, including a quantitative analysis of catastrophic forgetting and how the model's performance degrades with an increasing number of incremental learning tasks. This should include evaluating the model's ability to retain knowledge of base classes while adapting to new classes.

4. Although the model aims to be efficient, the use of advanced techniques like Neural ODEs could still demand significant computational resources, potentially limiting its applicability in resource-constrained environments. The paper does not sufficiently discuss this trade-off, which could be a critical consideration for practical deployment scenarios. A more detailed analysis of the computational cost of the Neural ODE component is needed, including a breakdown of the time and memory requirements for both training and inference, and a comparison with alternative, potentially less resource-intensive, methods for dynamic prototype rectification.

### Questions
1. How does the scalability of the UOPP model hold up when there is a significant increase in the number of clients or data volume? Can the model adapt to the continuous addition of new categories without a significant increase in training time or resource consumption?

2. How does the UOPP model perform in the face of class imbalance or distribution shift? Has the model undergone tests for generalization capabilities across different domains or tasks?

3. What specific operations are used in the iterative correction process of dynamic prototypes to guide them closer to the actual data distribution? How is the number of iterations for prototype correction determined? Is there an early stopping mechanism to prevent overfitting?

4. Regarding the dynamic updating of prototypes, can Neural ODEs be replaced by other optimization strategies, or how significant is the impact on the results without the ODE method, and was its computational complexity considered?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper defines a new problem named Federated Few-Shot ClassIncremental Learning (FFSCIL) problem, where clients only hold very few samples for new classes. They develop a novel Unified Optimized Prototype Prompt (UOPP) model that utilizes task-wise prompt learning to mitigate task interference empowered by shared static-dynamic prototypes, adaptive dual heads, and weighted aggregation. The proposed UOPP significantly outperforms existing SOTA methods of FCIL, FSCIL, and CIL, on three datasets, along with deeper analysis confirms that the proposed method achieves better stability-plasticity trade-off, and robustness in different local clients and small global rounds.

### Strengths
1. The experiments are comprehensive and solid, achieving state-of-the-art performance.
2. The paper includes a deeper theoretical analysis, demonstrating a better stability-plasticity trade-off and robustness across different local clients and smaller global rounds.
3. Resource analysis is thorough, covering complexity, running time, parameters, and communication costs.
4. Clear implementation details and algorithm pseudocode are provided, along with an anonymous GitHub repository, making reproduction accessible.

### Weaknesses
1.The motivation is very weak
The introduction of this work is poorly written; I cannot grasp the new insights regarding the federated learning task provided by the authors. The two components of this work (1) prototype calibration and (2) introduction of prompts have already been discussed in a large number of prototype-based continual learning and prompt-based continual learning works. The authors should emphasize the uniqueness of their work.

2.The lacked comparison with the recent Federated Class-Incremental Learning work
[1] also uses Parameter-Efficient Fine-Tuning technique for Federated Class-Incremental Learning, i.e., LoRA. Thus, except for the task difference, what is the true difference between the prompt used in this paper and the LoRA used in [1]? In addition, the difference about the prototpye use between this work and [1] should also introduced.
[1]PILoRA: Prototype Guided Incremental LoRA for Federated Class-Incremental Learning
ECCV 2024

3.The comparison with prototype works in continual learning is insufficient
Prototype Calibration is one of the important techniques in continuallearning, and there is a lot of existing work focusing on it, e.g., [2,3,4]. However, the authors do not compare their work with these efforts.
[2] Few-Shot Class-Incremental Learning via Training-Free Prototype Calibration, ECCV 2024
[3] Exemplar-free Continual Representation Learning via Learnable Drift Compensation, ECCV 2024
[4] Few-Shot Class-Incremental Learning via Training-Free Prototype Calibration, ICCV 2023

4.The possible data leakage issue
Although the authors do not use rehearsal to correct prototypes, the support set S is needed. Essentially, samples in the supported set S are pseudo rehearsal sampled from Gaussian distributions located on prototypes, and this technique is also common in continual learning, e.g., HiDe-Prompt [5]. I am concerned that the pseudo rehearsal still violates data privacy principles.
[5] Hierarchical Decomposition of Prompt-Based Continual Learning: Rethinking Obscured Sub-optimality.

### Questions
1. Please address the problems proposed in weaknesses.
2. Table captions should be placed at the top of each table according to the ICLR template guidelines.
3. To comprehensively evaluate the limitations in few-shot scenarios, it would be beneficial to explore additional settings between one-shot and five-shot, as well as settings with more than five shots. (optinal)
4. Although the method claims lower resource consumption, the running time of 6.05 hours is longer than that of most other methods.

### Soundness
3

### Presentation
3

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
The authors introduce Federated Few-Shot Class-Incremental Learning (FFSCIL), a new federated learning framework, along with the Unified Optimized Prototype Prompt (UOPP) model. UOPP tackles catastrophic forgetting, overfitting, and prototype bias by integrating task-specific prompt learning, unified static-dynamic prototypes, and an adaptive dual-head structure. Experiments demonstrate that UOPP surpasses state-of-the-art methods across multiple datasets, showing strong performance and robustness with low communication costs and efficient runtime.

### Strengths
•	Innovative Approach: UOPP combines prompt learning, prototype rectification, and an adaptive dual-head structure to address key challenges like catastrophic forgetting and overfitting.
•	Comprehensive Experiments: Extensive experiments demonstrate UOPP's robustness and superior performance across multiple datasets.
•	Open Source Code: The provided source code enhances reproducibility and supports further research.

### Weaknesses
•	In what situations is Federated Few-Shot Class-Incremental Learning (FFSCIL) actually useful, and why is it important to have a specific approach for these cases?
•	The paper’s prototype rectification method might not fully solve prototype bias issues, especially when data is really limited. With few local samples, it may still struggle to perform well in non-i.i.d. settings. Specifically, the method's reliance on local data for rectification could lead to biased prototypes if the local data distribution is significantly different from the global distribution, which is common in federated settings.
•	The experimental setup could be a bit limited since many of the comparison methods don’t fully match the FFSCIL scenario, which might make the performance comparisons less relevant and not show the method’s true strengths. The baselines used are primarily designed for either federated class-incremental learning or few-shot class-incremental learning, but not the combination of both. This makes it difficult to isolate the performance gains specifically attributable to the FFSCIL setting.

### Questions
see weaknesses

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
The paper propose a new setting - Federated Few-Shot Class Incremental Learning (FFSCIL) where each client in the system has very few samples per class. The work focus on the prototype bias rectification process and propose a prompt-learning method named “Unified Optimized Prototype Prompt (UOPP)” which is based on static and dynamic class prototypes optimized using Neural Ordinary Differential Equations. The proposed method outperforms existing methods across three benchmark datasets and achieves better stability-plasticity trade-off.

### Strengths
1. The paper has good analysis of the prototype rectification problem with good illustrations.
2. The paper proposed a new and interesting few-shot setting for FCIL.
3. The method section is well-written with lot of theoretical analysis.
4. The extensive experiments and ablation study is appreciated.

### Weaknesses
1. The writing needs to be improved and more precise with appropriate and more FSCIL references. For instance, more context and details are necessary here (line 54 - “this mechanism may violate data privacy principles since it may reveal partial information about private data of a client to another party”; line 57 - “that may breach data openness policy, where data are only open for a client at a specific moment”). The introduction section could better introduce and establish the problem statement instead of directly jumping to the solution. The motivation for the proposed FFSCIL setting, why not save exemplars and why not use synthetic samples is not clear and needs to be discussed in details.

2. Existing works [1,2,3] which extensively studied prototype calibration for FSCIL which is the same concept termed as prototype rectification in this work, are completely ignored. TEEN [1] and statistics calibration [3] are very relevant single-step prototype rectification baselines which should be considered, adapted for FFSCIL and compared to the proposed method since this naive averaging method is already established for FSCIL. It is important to discuss the difference of class-similarity based rectification as in [1,3] with the proposed Neural ODE-based rectification and see its impact.

3. Recent work from Federated Learning [4] used prototype-based NCM classifiers and achieved very good performance without any training. Using NCM classifier is pretty common and standard practice in FSCIL where the model is trained in the base task and the frozen model is used in all subsequent tasks to compute class means for NCM classifier. FedNCM [4] is an important baseline method missing from the discussion and comparison tables. FedNCM is the baseline which shows how much the models can perform without any further fine-tuning or learning prompts after base task.

4. It is not clear what is the balance mean accuracy? Recent FSCIL papers [1,2,3] considered the harmonic mean accuracy which is quite helpful in FSCIL settings to evaluate performance of old and new classes since most of the accuracy comes from the old classes.

### Questions
1. It is not clear if the ViT model used for UOPP in the experiments used pre-trained weights or not. This is not mentioned in the paper. It is important to have a fair comparison and start from the same weights for all compared methods.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper define a new Federated Few-shot Class-Incremental Learning (FFSCIL) problem which is interesting and has significante value in real model deployment. A novel Univfied Optimizaed Prototype Prompt (UOPP) method is proposed for FFSCIL problem. UOPP utilizes task-wise prompt-learning to mitigate task interference empowered by shared static-dynamic prototypes, adaptive dual heads, and weighted aggregation. The dynamic prototype tackles prototype bias by iterative rectiffcations. Comprehensive experimental results show that UOPP signiffcantly outperforms existing SOTA methods of FCIL, FSCIL, and CIL, on three benchmarks with a signiffcant gap. The proposed method achieves better stability-plasticity trade-off, and robustness in different local clients and small global rounds.

### Strengths
1. A new Federated Few-shot Class-Incremental Learning (FFSCIL) problem which is interesting and has significant value in real model deployment.
2. An effective method UOPP is proposed for FFSCIL.
3. Comprehensive experiments are designed and demonstrate the effectiveness in final performance, stability-plasticity balance, and robustness, which are important in class-incremental learning.
4. The whole paper is well organized and easy to follow. The problem and idea are clearly presented.
5. Codes are available and theoretical analysis is provided.

### Weaknesses
1. The few-shot constraint when T>0 is defined in the task level or just client level is vague. Could the authors explain whether the images assigned to each client is randomly selected from the whole training set or from a small fixed subset of the training images? If former manner, the few-shot constraint is defined in the client level and prototype rectification through different clients is able to improve the performance. If the latter manner, the few-shot constraint is defined in the task-level. Prototype rectification through globally stored representation is limited to improve the learned prototype as no more information provided. Specifically, if each client receives a random subset of the entire training set for each task, the few-shot constraint is effectively at the client level, and the global aggregation of prototypes could be leveraging a larger, albeit distributed, dataset. However, if each client only ever sees a small, fixed subset of the training data, then the few-shot constraint is at the task level, and the global prototype rectification is more limited by the lack of diverse data.
2. Unclear details: How Z_l is augmented to construct query sample set Q? What's the loss to train GradNet? How is ω_l determined in server-side aggregation? How is setting of D implemented in table 4? The paper lacks a clear explanation of how the query set Q is generated from the prototype set Z_l. The training process for GradNet is not specified, and the loss function used is not defined. The method for determining the client weights ω_l during server-side aggregation is also unclear. Furthermore, the implementation details for the parameter D in Table 4 are missing, making it difficult to reproduce the results.
3. Typos: line270, "parameter Ψ" should be "parameter Φ". line362: "10 round per class" should be "10 round per task".

### Questions
1. Is there any error in equation (4)? As ω is a regularizer not a weight, should ωzc(s) be ω(zc(s))?
2. Why larger round leads to worse performance for UOPP according to table 3?

### Soundness
4

### Presentation
4

### Contribution
3
