# Inv-PnCO: Invariant Predict-and-Combinatorial Optimization under Distribution Shifts

- Decision: Reject
- Avg Score: 4.40
- Scores: 6, 5, 3, 5, 3

## Abstract
Machine learning has been well introduced to solve combinatorial optimization (CO) problems over the decade, while most works only consider the deterministic setting. Yet in real-world applications, decisions have often to be made in uncertain environments, which is typically reflected by the stochasticity of the coefficients of the problem at hand, considered as a special case of the more general and emerging "predict-and-optimize" (PnO) paradigm in the sense that the prediction and optimization are jointly learned and performed. In this paper, we consider the problem of learning to solve CO under the above uncertain setting and formulate it as "predict-and-combinatorial optimization" (PnCO), particularly in a challenging yet practical out-of-distribution (OOD) setting, where there is a distribution shift between training and testing CO instances. We propose the Invariant Predict-and-Combinatorial Optimization (Inv-PnCO) framework to alleviate this challenge. Inv-PnCO derives a learning objective that reduces the distance of distribution of solutions with the true distribution and uses a regularization term to learn invariant decision-oriented factors that are stable under various environments, thereby enhancing the generalizability of predictions and subsequent optimizations. We also provide a theoretical analysis of how the proposed loss reduces OOD error. The empirical evaluation across three distinct tasks on knapsack, visual shortest path planning, and traveling salesman problem covering array, image, and graph inputs underscores the efficacy of Inv-PnCO to enhance the generalizability, both for predict-then-optimize and predict-and-optimize approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper concerns its self with the "Predict and Optimize" (PnO) setting, specifically for Combinatorial Optimization Problems (CO). In the prior, a model is trained to predict the optimization coefficients whilst jointly solving the optimization problem, contrary to "Predict then Optimize" (PtO), a two stage approach.

The paper aims to address the challenge of distribution shift between training and testing CO instances. The authors introduce a learning objective which reduces the distance of distribution of
solutions with the ground truth, and that uses regularization in the hope of learning invariant
decision-oriented factors. Toy experiments are provided for the knapsack, visual
shortest path planning, and traveling salesman problems.

### Strengths
Tackling distribution shift for NNs is a research direction with high impact, and the authors are clearly aiming for an impactful framework. The work adds to a growing line of work in learning discrete operations via NNs, which is an interesting and fast growing research direction. It was nice to see the inclusion of Section 5.5, and the ablation study (see Appendix), as such information regarding sensitivity and training is pertinent to any practitioner.

### Weaknesses
I personally found the paper difficult to follow, mainly due to the writing structure. I would have liked to have seen a more explicit motivation for the impact of this line of work in the introduction / first sections (e.g. concrete real world cases of distribution shift failure for learning to solve COs). However, I am not familiar with this exact research topic, so this could be owing to this.

I am not completely convinced by the impact of the proposed methodology, (this is harder to assess due to the way the paper is written as stated above). ~~For example, in the Grid-world example using a ResNet, how does the method compare to just training the ResNet with simple data augmentations for added visual robustness~~ ? The data sets are all toy, and no standard distribution shift baselines are included as reference.

~~Note: The paper is not completely anonnymized (link to code contains name of an author), and hence does not follow the 2024 guidelines.~~

### Questions
In section 3 (under the **Predict-and-optimize for optimization under uncertainty** paragraph,  lines ~207-210): I would suggest adding citations to the following literature: (which address smoothing / differentiability and/or PnO):

- [Berthet 2020] *Learning with Differentiable Perturbed Optimizers*
- [Jang 2016] *Categorical Reparameterization with Gumbel-Softmax*
- [Stewart 2023] *Differentiable Clustering with Perturbed Spanning Forests*
- [Peterson 2024] *Learning by Sorting: Self-supervised Learning with Group Ordering Constraints*


In line 86 you may want to include: [Zhang 2023] *Learning useful representations for shifting tasks and distributions*

### Soundness
3

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes an approach for predict-and-optimize for combinatorial optimization problems under distribution shifts and uncertain optimization coefficients. The approach involves addition of a mutual information based regularization term to the objective and optimizing a surrogate loss function which is shown to upper bound this objective. The proposed approach is empirically evaluated on knapsack, visual shortest path planning and the traveling salesman problem.

### Strengths
- Most previous approaches for predict-and-optimize are based on differentiable losses and do not apply to combinatorial optimization which involve discrete decisions. 
- The formal results imply that small error on the proposed objectives will lead to a small out-of-distribution error, making the approach theoretically principled.
- Experiments indicate usefulness of approach in minimizing regret.

### Weaknesses
- The proposed approach is not computationally efficient and therefore may not scale well to typical real-world problems.
- Missing comparison with and discussion of related work on using mutual information based regularization for adversarial robustness [1,2,3].
- The approach depends on a strong assumption about existence of invariant factors whose decision remains invariant across environments. 

Minor:
- Citations should be correctly bracketed

[1] Zhu, Sicheng, Xiao Zhang, and David Evans. "Learning adversarially robust representations via worst-case mutual information maximization." International Conference on Machine Learning. PMLR, 2020.

[2] Wang, Tianhao, Yuheng Zhang, and Ruoxi Jia. "Improving robustness to model inversion attacks via mutual information regularization." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 35. No. 13. 2021.

[3] Zhou, Dawei, et al. "Improving adversarial robustness via mutual information estimation." International Conference on Machine Learning. PMLR, 2022.

### Questions
- Why is the approach of adding mutual information based regularization specific to combinatorial optimization? Can the proposed approach be applied to predict-and-optimize for continuous optimization?
- How should the regularization hyperparameter ($\beta$ in (8)) be set and what is its impact?
- What are the novel technical insights in the proofs of the theoretical results?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses combinatorial optimization under uncertainty, proposing the PnCO paradigm for OOD scenarios where training and testing distributions differ. The proposed method, Inv-PnCO, improves generalization by a regularization term to learn invariant decision factors stable across environments. Theoretical and empirical results on tasks like knapsack and shortest path planning demonstrate that Inv-PnCO effectively enhances generalizability in uncertain settings.

### Strengths
1. The motivation is clear and the manuscript is well written.
2. The experiment includes sufficient tasks across different applications for OOD case.

### Weaknesses
As the abstract suggests, since the CO problems has been introduced for a long time, how is Inv-PnCO compared to other previous methods? This paper compares with vanilla ERM only (Table 3, 4, 5), which is a strong drawback. There has been other papers for CO with distribution shift. For example, [1] proposed to use meta learning for better distribution generalization. This paper does not compare to enough SOTA methods.

[1] UNSUPERVISED LEARNING FOR COMBINATORIAL OPTIMIZATION NEEDS META LEARNING. ICLR 2023.

### Questions
The proposed method requires a set of training environments of different distribution to reduce the variance of their losses. This setting is similar to multi source domain adaptation, where a model is trained using labeled data from multiple source domains to generalize well to a new, unseen target domain with a different data distribution. I wonder why the author stated that these methods are not applicable to this problem. With access to the set of training environments, other methods also can directly applied similarly as Theorem 2.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies optimization with unknown coefficients, where the learner must first estimate these coefficients from empirically observed data before making decisions. The main focus is on the distribution shift problem, where coefficients may differ between the training and test phases. To address this, the paper proposes a regularizer designed to learn invariant features from training data across multiple environments. Theoretical analysis and experimental results validate the effectiveness of the proposed approach.

### Strengths
+ This paper addresses a novel problem of optimization with an unknown coefficient under distribution shift. The problem setup is unique and holds practical significance
+ Extensive empirical studies are conducted to validate the proposed method, including ablation studies on parameters and the number of environments.

### Weaknesses
- **Regarding Novelty**: One of my main concerns is the novelty of the proposed method, as the objective function in Eq. (7) appears similar to Eq. (10) in Federici et al., 2021, developed for supervised learning. Although the problem setting differs, the main challenges and how the previous work’s ideas are extended to the setting studied in this paper are not clearly discussed. A more detailed comparison with Federici et al., 2022 would enhance clarity.

- **Regarding the Condition in Theorem 1**: It is not entirely clear whether the condition \( I_{e',q}(x; y \vert y) = I_{e, q}(x; y \vert y) \) in Theorem 1 is achievable. As discussed in line 292 and in the proof, this condition is satisfied when \( D_{\text{KL}}(p(z \vert x) \Vert q(z \vert y)) \) is minimized. However, in Eq. (7), we are optimizing a regularized version, which might make the condition in Theorem 1 challenging to satisfy. Is the conclusion in Theorem 1 still valid under these circumstances?

- **Experiments**: I appreciate the authors' efforts in conducting extensive experiments to validate the proposed methods. However, some aspects of the presentation remain unclear:
    - The standard deviations are missing in the tables. For instance, in the Warcraft shortest path task, the performance of SPO under "OOD: ERM" and "OOD: Inv-PnCO" is quite close. It’s unclear whether the advantage of Inv-PnCO over ERM is statistically significant. Including error bars in the results and performing a statistical test would improve clarity.
    - In Figure 3(c), it is interesting to observe that the performance of the proposed method decreases with 5 environments compared to 4 environments, which seems contrary to the remark in lines 319-322. Additional explanation of this phenomenon would be helpful.

- **Clarity on Notation**: Several important notations are omitted in the main paper, making it difficult to follow. For example, it would be clearer to include the definition of $ I_{e,q}(x; z \vert y) $ in Theorem 1 and $ \mathcal{L} $ in Theorem 2 directly in the main text.

### Questions
- Could you highlight the technical novelty and contributions of the proposed method compared to Federici et al., 2021?
- How can we ensure that the condition in Theorem 1 is satisfied by the proposed algorithm?
- Could you add error bars for all results in the experiments?
- Could you provide a more detailed explanation of the phenomenon in Figure 3(c), where the performance of the proposed method deteriorates as the number of environments increases?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates combinatorial optimization problems in uncertain environments, and formulate it as "predict-and-combinatorial optimization" (PnCO), particularly in a challenging yet practical out-of-distribution (OOD) setting. The authors propose the Invariant Predict-and-Combinatorial Optimization (Inv-PnCO) framework to address the challenge caused by distribution shift problem. Furthermore, they also provide the theoretical analysis and conduct empirical evaluation across three distinct tasks to validate the effectiveness of their proposed framework.

### Strengths
Addressing the combinatorial optimization problem for distribution shift and out-of-distribution (OOD) scenarios holds substantial value in practical applications. Additionally, the experimental settings in this paper are highly diverse, including artificial, perceptual, and topological shifts in knapsack, visual shortest path (SP) and traveling salesman problem (TSP) covering the input of the array, images and graphs.

### Weaknesses
**Writing Issue:** The writing of this paper requires meticulous revision and further improvement. The primary contribution lies in the theoretical analysis; however, I found numerous errors in the notation and proofs, which hindered my understanding of the theoretical guarantees provided by this work. For instance, in Section B.2, it should be "$R(q(\mathbf{y}|\mathbf{x}))$" rather than "$R(q(\mathbf{y}|\mathbf{x})$", yet the authors overlooked such an obvious error. Many similar issues exist, as detailed in ***Questions***.  

**Citation Issue:** I find the citation format in this paper rather unusual. Although this is not a criterion for evaluating the quality of the paper, I still recommend that the authors use `\citep{}` for citations in LaTeX, rather than `\citet{}`. The `\citet{}` command is used when the cited reference needs to be incorporated as part of the sentence. 

**Experiment Issue:** In the experimental section, this work only compares with ERM, which does not convincingly validate the effectiveness of their framework.

### Questions
First, I raise some questions regarding the notation used in this work. 

**Q1:** In Definition 2, the authors introduce $\mathbb{E}_{(x_i,z_i)\sim D} [\mathcal{F}(\hat{z}_i(y_i),y_i,\theta)]$, but according to your explanation, $z_i$ is obtained by solving with the true coefficients. Then, why is $(x_i,z_i)\sim D$ also present? $(x_i,z_i)\sim D$ seems to imply that $z_i$ is sampled from $D$, correct? Additionally, I believe the authors have not consistently used definitions for variables and functions. Specifically, if $\hat{z}_i(\cdot)$ is written out, it should denote a function, not an output. However, the authors also use it as an output. 

**Q2:** Let us examine lines 274 to 287 of this paper. Before Theorem 1, the authors use $\mathbf{z}$ and $\mathbf{x}$ (boldface) to represent the solution and feature, respectively. However, in Theorem 1, they switch to non-boldface $z$ and $x$. More confusingly, in the proof of Theorem 1 in Section B.3, $\mathbf{z}$ and $\mathbf{x}$ (boldface) are used again. I found similar issues throughout the paper, such as in Equations (11) and (12) of Section B.1. Though the authors explain that "we denote variables in bold lowercase letters and data samples as lowercase letters", I still find it confusing. Could the authors clarify if this was done for any particular reason? If not, they should carefully revise the paper to ensure consistent notation throughout. 

Second, I believe that labeling Theorem 2 as a ***theorem*** may be somewhat overstated; it might be more appropriate to refer to it as a ***proposition***. Regarding the proof of Theorem 2, I have the following questions.

**Q3:** What exactly is the difference between $p(\cdot,\cdot)$ and $p_e (\cdot,\cdot)$? I have seen these two used in many places throughout the paper, but the distinction between them is not clearly explained. In Equation (15), you directly switch from $p(\mathbf{y}|\mathbf{x}=x)$ to $p_e(\mathbf{y}|\mathbf{x}=x)$ in the first inequality. 

**Q4:** What is the reason for the inequality in Equation (15)? I understand that you might be using the convexity of $\log \frac{1}{x}$, but how did you convert $p(\mathbf{z}|\mathbf{x})$ to $q(\mathbf{z}|\mathbf{y})$? 

Finally, I have one more question regarding the experimental baseline. 

**Q5:** Distribution shift and OOD problems have been extensively studied in machine learning for years. Why did this paper use only ERM as the baseline in Tables 3, 4, and Figure 5? I am not sure if I missed other baselines. In the literature, there should be many algorithms handling distribution shift (such as DRO) and OOD generalization. The authors should compare more baselines to validate the effectiveness of their framework.

### Soundness
2

### Presentation
1

### Contribution
2
