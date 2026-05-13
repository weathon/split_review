# DIG-MILP: a Deep Instance Generator for Mixed-Integer Linear Programming with Feasibility Guarantee

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Mixed-integer linear programming (MILP) stands as a notable NP-hard problem pivotal to numerous crucial industrial applications. The development of effective algorithms, the tuning of solvers, and the training of machine learning models for MILP resolution all hinge on access to extensive, diverse, and representative data. Yet compared to the abundant naturally occurring data in image and text realms, MILP is markedly data deficient, underscoring the vital role of synthetic MILP generation. We present \dgm, a deep generative framework based on variational auto-encoder (VAE), adept at extracting deep-level structural features from highly limited MILP data and producing instances that closely mirror the target data. Notably, by leveraging the MILP duality, \dgm{} guarantees a correct and complete generation space as well as ensures the boundedness and feasibility of the generated instances.git}}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a deep instance generator for MILPs with feasibility gurantee. It uses a VAE model trained on a dataset to generate similar MILP instances, and leverages a dual method proposed by Bowly et al. for feasibility.

### Strengths
1. This paper proposes a MILP generator with feasibility gurantee.
2. It conduct some experiments to demonstrate the effectiveness and for analysis.

### Weaknesses
1. The technical novelty is minor. The proposed model is a direct combination of two existing methods [1] and [2]. [1] is a recent work accepted by NeurIPS and this paper is almost the same with [1]. Even if taking [1] without consideration, this work is an application of existing techniques, i.e., the VAE for graph generation and the feasible instance construction method proposed in [2]. The combination of these methods is not particularly insightful, and the paper does not demonstrate any significant modifications or adaptations to these existing techniques that would warrant a novel contribution. The core idea of using a VAE for generating graph-based problem instances and then ensuring feasibility through a separate method is a straightforward application of existing knowledge.
2. Does this paper deal with MILPs or IPs? In Eq. (1) all variables are constrained as integers. In table 1 there are no features indicating whether the variables are integers. The lack of clarity on whether the method is intended for Mixed Integer Linear Programs (MILPs) or Integer Programs (IPs) is a significant issue. The formulation in Eq. (1) suggests an IP due to the integer constraints on all variables, yet the paper claims to generate MILPs. The absence of features in Table 1 that would distinguish between integer and continuous variables further exacerbates this confusion. This ambiguity needs to be resolved for the paper to be technically sound.
3. Do the datasets contain unfeasible MILPs? Can the model learn to generate feasible MILPs without the feasibility gurantee? The necessity of this component is not demonstrated with ablation study. It is unclear whether the feasibility guarantee component is actually necessary. If the training data consists only of feasible instances, it is possible that the VAE itself could learn to generate feasible instances without explicit enforcement. An ablation study that removes the feasibility component would be needed to demonstrate its necessity. The paper should also clarify whether the datasets contain any infeasible instances, and if so, how the model handles them.
4. The proposed method does not performs better than random significantly. The experimental results do not show a substantial improvement over a random baseline. This raises concerns about the practical utility of the proposed method. The reported performance gains are marginal and do not justify the complexity of the approach. The lack of significant improvement over a simple random generation method suggests that the proposed model may not be learning meaningful patterns from the training data.
5. Why not report the hyper-configuration results to show whether this method can benefit this task? The paper lacks a detailed analysis of the hyperparameter tuning process. It is crucial to understand how different hyperparameter settings affect the performance of the model. Reporting the optimal hyperparameter configurations and their corresponding performance metrics would provide valuable insights into the robustness and sensitivity of the proposed method. The absence of this information makes it difficult to assess the true potential of the approach.
6. What is the useness of the optimal value prediction task? Can the proposed method help the solving instead of just predicting the optimal value? The motivation for including the optimal value prediction task is unclear. The paper does not explain how this task contributes to the overall goal of generating useful MILP instances. Furthermore, it is not clear whether the proposed method can be used to aid in solving MILPs, rather than just predicting the optimal value. The paper needs to clarify the practical relevance of this task and its connection to the broader objective of MILP generation.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of instance generation for mixed-integer linear programming (MILP). The authors propose a deep generative framework based on variational auto-encoder (VAE) to capture complex structural characteristics from limited MILP data and generate instances that resemble the original data. Experiments demonstrate the proposed method outperforms baselines on various benchmarks.

### Strengths
1.	This paper proposes to leverage the MILP duality theory to ensure the boundedness and feasibility of the generated instances.
2.	Experiments demonstrate the proposed method outperforms baselines on various benchmarks.

### Weaknesses
1.	The technical novelty of the proposed method is incremental, as the proposed method primarily use the existing VAE [1, 2] model to generate MILP instances. The authors may want to explain the technical novelty of the proposed methods in detail. 
2.	The relationship between the theoretical derivations (i.e., Theorem 1) and the proposed MILP generation pipeline based on the VAE [1, 2] model is unclear.
3.	The motivation of using the VAE [1, 2] model to generate MILP instances is unclear. The popular generative models include VAE [1, 2], Generative Adversarial Network (GAN) [3], and diffusion model [4]. The authors may want to explain the motivation of using the VAE [1, 2] model rather than the other generative models.
4.	I found the proposed method is similar to one recent work at NIPS [5]. The authors may want to explain the differences between their proposed method and the recent work [5] in detail.
5.	The experiments are insufficient. First, it would be more convincing if the authors could evaluate their method on large-scale benchmarks, such as instances from the MIPLIB with over 100,000 variables and 100,000 constraints. Second, the authors may want to evaluate their method on popular downstream tasks, such as learning to cut [6, 7] and learning to branch [8, 9]. Third, the baselines are insufficient. The authors may want to compare their method to G2SAT [10], which is the first deep generative framework that learns to generate Boolean Satisfiability (SAT) problems.

### Questions
1.	What is the technical novelty of the proposed method?
2.	What is the relationship between the theoretical derivations and the proposed method?
3.	What is the motivation of using the VAE model?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The manuscript presents DIG-MILP, an innovative deep generative approach tailored for Mixed Integer Linear Programming (MILP) generation. Unlike traditional MILP generation methods, DIG-MILP eschews the need for domain-specific insights. A significant attribute of DIG-MILP is its assurance of the feasibility and boundedness of the crafted data. The generative spectrum of DIG-MILP spans all feasible and bounded MILPs, endowing it with the prowess to produce a "variety" of instances. Experimental analyses underscore DIG-MILP's promise in: (S1) facilitating MILP data dissemination for solver hyperparameter optimization without publishing original datasets, and (S2) data enrichment to bolster the robustness of machine learning techniques dedicated to tackling MILPs.

### Strengths
1.	It is impressive that the authors propose to use VAE sampling in dual space to generate MILP instance. In this way, the feasibility guarantee is directly obtained. 
2.	The experimental results endorse that the proposed techniques indeed facilitate the enhancement of MILP solver and business scenarios.

### Weaknesses
1.	It seems that the literature review lacks of the most related paper that recently published in NeurIPS 2023 (Geng, Zijie, Xijun Li, Jie Wang, Xiao Li, Yongdong Zhang, and Feng Wu. "A Deep Instance Generative Framework for MILP Solvers Under Limited Data Availability." arXiv preprint arXiv:2310.02807 (2023).) This submission is highly similar to the above paper. Thus the authors are supposed to highlight the largest difference and improvement from the mentioned paper.
2.	Similar to the above point, the experimental setting of this paper highly resembles one in the paper “A Deep Instance Generative Framework for MILP Solvers Under Limited Data Availability”. Thus, Are the authors supposed to compared their proposed method with one proposed in that paper?
3.	It is hard to read several Figures. Because the font size of axis in those figures is too small

### Questions
1.	Please clarify more in-depth about the feature mentioned in Table 1, especially the all 0’s of y, r and the all 1’s about x, s.
2.	It is not that dogmatical to claim that the boundness and feasibility of the generated instances can sure the authenticity of the produced data. The authenticity of MILP dataset can be defined in kinds of perspectives. Can you give more evidences to support your claim?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a MILP instance generator with the help of the variational auto-encoder (VAE), aiming at generating enough MILP instances for academic research and industry usage. The authors first prove the boundedness and feasibility when generating instances using the dual formation, which ensures the correctness of the proposed generator DIG-MILP. In the training step, DIG-MILP continues to mask a random node and the connections to it, and use the incomplete instance as input to the VAE, aiming to reconstruct the instance. This task is suitable for VAE and helps the model to learn how to generate more MILP instances. The proposed method is well-designed and the proofs are sufficient. The experiments on multiple datasets and scenarios show the performance of the proposed method.

### Strengths
1. There is indeed a need to generate more high-quality MILP instances in both the industry and academia. Therefore, this work is necessary and interesting to the community.
2. The proposed VAE framework for generating MILP instances is self-contained and reasonable, as VAE is demonstrated to be useful in many instance generation tasks.
3. The authors have proven the generated instances to be feasible-bounded.

### Weaknesses
1. In the pipeline of the proposed method, I see that one node will be removed and the origin G is changed to G'. I wonder if this one-node change is too small to identify. In common MILP datasets, the size of nodes/constraints is more than thousands, and for the industry area, the size is even larger. The incremental change by removing a single node and its connections seems insufficient for the VAE to learn the complex underlying structure of large-scale MILP instances. This could lead to the generator producing instances that are only marginally different from the training data, lacking the desired diversity and complexity.
2. In section 3.2, the authors provide the feasibility guarantee for the proposed methods. But I am curious about unfeasible instances, can the proposed framework generate unfeasible MIP instances? In my view, it is okay when a MIP instance is infeasible and this situation is common in the real world. The limitation to only generating feasible instances restricts the applicability of the method. Real-world MILP problems often include infeasible scenarios due to modeling errors or conflicting constraints, and a robust generator should ideally be able to capture this aspect of problem space. The inability to generate infeasible instances could limit the generator's utility in certain contexts.
3. The metrics in the experiments are confusing to me. The authors mentioned: "The similarity score is derived from the Jensen-Shannon (JS) divergence (the lower the better) between each metric of the generated and original data", while in the caption of table 1 said: "The similarity score ↑ between the original and generated data." The similarity score is lower the better or higher the better? Actually, I wonder what we expect about the similarity score. I mean, more similarity could increase Authenticity while less similarity could increase Diversity. Both cases seem to mean something. The contradictory description of the similarity score makes it difficult to interpret the experimental results. It's unclear whether the goal is to maximize or minimize similarity, and what the implications are for the quality of the generated instances. The lack of clarity on this fundamental aspect makes it hard to evaluate the method's performance.
4. About the datasets in the experiments, I see that for small datasets SC and CA the amount of instances is 1000, but for large datasets CVS and IIS the amount is less than 10. This gap looks very strange to me. Moreover, in, table 2, does training and testing on merely 3 instances lead to an overfitting to these instances? I think the datasets CVS and IIS need to be further refined. I understand that they are selected from MIPLIB17, but MIPLIB17 at least has hundreds of instances. If the MIPLIB17 is too hard, I think NeurIPS 2021 ML4CO[1] datasets could be more suitable.

### Questions
Please refer to the weakness part of my review. Admittedly, I am not familiar with generative models, so my questions are mainly about this part. However, based on my experience, I think the dataset problem is more severe, as I do not think training and testing on only 3 instances is suitable for meeting the bar of ICLR.

Besides, some closely related works on graph generation especially SAT instance generation are missed, including [1], [2], [3], all of which exhibit highly similar task structures for generating bipartite combinatorial optimization problems.

If there are some fatal mistakes in my review, please point it to me.


[1] G2SAT: Learning to Generate SAT Formulas. NeurIPS 2019.

[2] On the Performance of Deep Generative Models of Realistic SAT Instances. SAT 2022.

[3] HardSATGEN: Understanding the Difficulty of Hard SAT Formula Generation and A Strong Structure-Hardness-Aware Baseline. SIGKDD 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
