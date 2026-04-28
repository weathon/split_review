# Data Pruning by Information Maximization

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 8, 3, 6, 6, 5

## Abstract
In this paper, we present InfoMax, a novel data pruning method, also known as coreset selection, designed to maximize the information content of selected samples while minimizing redundancy. By doing so, InfoMax enhances the overall informativeness of the coreset. The information of individual samples is measured by importance scores, which capture their influence or difficulty in model learning. To quantify redundancy, we use pairwise sample similarities, based on the premise that similar samples contribute similarly to the learning process.
We formalize the coreset selection problem as a discrete quadratic programming (DQP) task, with the objective of maximizing the total information content, represented as the sum of individual sample contributions minus the redundancies introduced by similar samples within the coreset.
To ensure practical scalability, we introduce an efficient gradient-based solver, complemented by sparsification techniques applied to the similarity matrix and dataset partitioning strategies. 
This enables InfoMax to seamlessly scale to datasets with millions of samples. 
Extensive experiments demonstrate the superior performance of InfoMax in various data pruning tasks, including image classification, vision-language pre-training, and instruction tuning for large language models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces InfoMax, a novel data pruning method designed to maximize the information content of selected samples while minimizing overlap. The authors formulate this objective as a discrete quadratic programming problem, which they then relax and solve using an efficient gradient-based approach. Experimental results demonstrate the substantial effectiveness of InfoMax, underscoring its potential in data-centric applications such as image classification, multi-modal pretraining, and instruction tuning for large language models.

### Strengths
1. The paper presents an elegant and well-formulated approach to data pruning, with a solid theoretical foundation that supports its design.
2. The authors conduct a diverse set of experiments, including pretraining vision-language and fine-tuning LLM, further strengthening the validation of the method.
3. The performance of InfoMax is impressive, achieving high accuracy in various applications and outperforming existing state-of-the-art methods in many cases.

### Weaknesses
1. Some notations in the paper are unclear. For example, the symbols \( P \) on line 163 and \( z_n \) on line 1104 lack sufficient explanation. Furthermore, the variable \( X_t \) in lines 1054 to 1067 should be bolded for consistency.
2. The motivation behind InfoMax is not entirely novel, as the concepts of diversity and importance (information) have been previously discussed in [1, 2].
3. The paper does not include comparisons with some relevant baseline methods, such as geometry-based methods.

### Questions
The authors argue that $D^2$-Pruning may result in suboptimal solutions due to its greedy selection process. However, the relaxation applied to the quadratic optimization problem in Eq. 7 is not proven to produce solutions consistent with the original formulation, which could also result in suboptimal solutions. Given this, what factors contribute to the improved performance of your method compared to $D^2$-Pruning?

### Soundness
2

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
3

### Summary
This work presents a novel approach to data pruning, that aims to maximise the core set information through the simultaneous optimisation of individual sample information and overlapping information between samples. To solve this equality the authors present this as a discrete quadratic programming problem, presenting an efficient gradient based solver to improve the scalability of the method. The resulting core set’s are tested in a variety of settings to demonstrate performance and information preservation, where the authors demonstrate significant improvements over prior methods. Furthermore, the authors demonstrate their findings across a variety of tasks, and datasets to present generalisation of the method. A full sensitivity analysis is presented alongside all key details for reproducibility, providing readers with the necessary information to apply or replicate the findings.

### Strengths
**Structure and Clarity:**
- The work is well organised and presented clearly defining the problem statement hypothesis of the work. The core narrative and all technical contributions are written in a clear and concise manner, guiding most readers well to fully understand the contributions.
- Most of the key concepts discussed are presented in the form of visualisations, or figures which help justify the narrative, and provide evidential basis of the investigations.

**Method, hypothesis, findings, and rationale:**
- The method is well justified with Figure 2 presenting clear empirical evidence to claims of prior method weaknesses and properties. This figure alone does a lot of the heavy lifting in providing strong rationale behind the decision making which defines the proposed method. 
- Method description itself is sensible, clearly presented and interpretable. The method section is further supported with proofs and significant empirical findings justifying decisions made.
- The findings demonstrate the proposed method is highly performant when compared to the selected benchmark methods and on the selected tasks.
- Broader impact statement is provided and some limitations are addressed.

**Reproducibility:**
- All details are presented for full reproduction in the text including optimisation, hyperparameterisation, datasets, and architectural settings. The algorithm presented in the appendix is a nice addition to support reproducibility, and the 
- Descriptions of empirical setups are present and clear to follow, 

**Experimental results:**
- Generally, the authors do a good job covering a variety of empirical evaluations to test their method, presenting results on a variety of datasets for different tasks. 
- The sensitivity analysis is a nice addition, presenting the trade-off between the first and second order terms. While also having a secondary effect of demonstrating the robustness of the method to hyperparamter changes. 
- While additional experimentation would improve the work (see weaknesses) the core empirical evaluation does a good job of conveying the core message and rationale of the work

### Weaknesses
 **Empirical Comparisons**
- How does the method perform when compared to other data pruning methods not included in this work such as Sieve And Dyn-Unc. If there is a strong reason for not including these works then please correct me on this point. 
- The results in table 1 could be considered misleading with incorrect bolding of top results. For 70% cifar10 d2 is performing better, yet, infomax is highlighted. I assume this is a simple mistake.
- Computational compression between methods is performed but only at a small scale, against d2 and entropy. The addition to all analysed works would further support the statement that InfoMax is computationally efficient while being performant. It is hard from this small scale evaluation the trade-off between these points. 
- The addition of a more explicit ablation would be nice to have. How does changing the instantiation of the first order term I(z) effect the performance for example?

**Data Generalisation of method:**
- The authors method employs pre-trained networks to produce representations on which the method is applied (shown in Figure 3). However, from my understanding, the learnt representations themselves are produced from learning . This leads to two distinct weaknesses.
- The first is that the authors do not evaluate the performance and generalisation of the method to produce core sets when applying a different dataset. Thus, how does the method perform if the core feature extractor itself has not been trained on the data in question. 
- Secondly, this leads to a distinct contradiction of the work if it is require to re-train this network per dataset, thus meaning full datasets will have to be trained on before pruning can occur. Thus, leading to the desired computational cost decrease being lost.
- Furthermore, the choice of SSL method could be highly impactful here, it has been shown that some methods akin to MSN and DINO are both optimising to preserve maximal information across samples than say predictive methods such as BYOL. Therefore, have the authors considered how different pertained models to produce features may interact with the criteria for pruning proposed?

**Further analysis on the selected core set:**
- Does the coreset exhibit the properties you are aiming to persevere? While the empirical evaluation provide strong evidence that the method does produce a notion that the coreset is indeed informative, are there any other analyses that could be performed to provide further evidence that information redundancy is improved?
- While I am happy to be corrected on the above point, it does feel that some simpler and more explicit analyses could provide interesting introspective of the selected coreset prompting insights for future works.

**Minor:**
- Paragraph starting at line 81 could be moved to preliminaries, its place in the introduction does not flow naturally.
- Error’s are not reported on empirical results, while you state that the SD lies within 0.85, this is considerable in some comparisons, therefore these should be given.
- The paper is marginally over the page limit, but this is likely due to a formatting error which can easily be addressed.

### Questions
1. Have the authors considered testing the method under noisy data distributions? If not, why not?
2. Where do you see the future of this work? You mention larger scale experimentation, but from a methodological perspective where are the obvious gaps / limitations?
- Most questions are posed in the weaknesses section to improve clarity of the question.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The article introduces a novel data pruning method called InfoMax, which is also known as coreset selection, designed to maximize the information content of selected samples while minimizing redundancy. The proposal of the InfoMax algorithm maximizes overall information by considering both individual contributions and information overlap of samples. The development of an efficient gradient-based solver is enhanced by sparsification techniques and dataset partitioning strategies, enabling InfoMax to scale to large-scale datasets. Extensive experiments demonstrating InfoMax's superior performance across various data pruning tasks, including image classification, vision-language pre-training, and instruction tuning for large language models.

### Strengths
- InfoMax can effectively handle datasets with millions of samples within tens of minutes through sparsification techniques and dataset partitioning strategies.
- InfoMax shows better performance compared to existing methods, especially under high pruning ratios.
- InfoMax exhibits strong generalization capabilities across different datasets and tasks, including cross-model and cross-setting generalization.

### Weaknesses
 - The Introduction in this paper lacks a high-level insight of the InfoMax to explain why it could work better than \(D^2\) Pruning, which makes the reader difficult to understand the motivation of the proposed pruning algorithm intuitively, for example, what is the more intuitive motivation of the proposed work to maintain a proper balance between importance and diversity?
- In line#243, K_{z,s} should be inter-sample redundancy instead of intra-sample redundancy.
- The symbolic sign used in the method lacks clarity and conciseness. For example, I and X are repeated frequently with different and dazzling superscripts and subscripts.
- The length of the main text disobeyed the strict limits of 10 pages, because in the current typesetting the Conclusion section belongs to the main text.
- In my opinion, the contribution and novelty of this work is limited due to its start points similar to \(D^2\) Pruning, except the only scalable solver (step 4 in Figure 4).

### Questions
- What is the set-level information of the candidate subset of \(D^2\) Pruning? What is its difference from InfoMax?
- Why can \(D^2\) Pruning perform better than other hybrid approaches from a more intuitive perspective? I understand the content of Section3.3 but I hope the authors could convert the Section 3.3 into a more high-level and insightful motivation, which could be placed in Section 1 for more readers to get the key insight.

### Soundness
3

### Presentation
2

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
The paper introduces InfoMax, a novel data pruning method aimed at maximizing information content while minimizing redundancy in selected samples. It measures sample information through importance scores and quantifies redundancy using pairwise sample similarities. The coreset selection problem is formalized as a discrete quadratic programming task. An efficient gradient-based solver is proposed, along with sparsification techniques and dataset partitioning strategies, to scale InfoMax to large datasets. The significance lies in its ability to enhance model training efficiency and data storage without compromising performance.

### Strengths
1.) The paper is well-organized, with clear explanations of complex concepts, making it accessible to a broad readers.
2.) InfoMax offers a new perspective on data pruning by focusing on information maximization, formalizing the problem as a quadratic programming task and offering a clear explanation of the underlying information theory.
3.) Extensive experiments across diverse datasets and tasks validate the effectiveness of InfoMax, showing consistent improvements over existing methods.

### Weaknesses
1.) The method's reliance on calculating pairwise similarities and the construction of the similarity matrix may become computationally intensive and could be further optimized.
2.) The performance of InfoMax is sensitive to hyperparameters like the partition rate, sparse rate, and pairwise weight, which may require careful tuning for different datasets.
3.) The paper could provide more analysis on the risk of overfitting when using the gradient-based solver, especially with high pruning ratios.

### Questions
see the Weaknesses

### Soundness
2

### Presentation
2

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
A novel method, InfoMax, is proposed for data pruning and core set selection. The motivation of the method is finding a subset of samples that maximizes overall information by simultaneously considering each sample’s information contribution and the information overlap among them. The authors formulate the core set selection as a discrete quadratic programming (DQP) problem with equality constraints that specify the desired number of selected samples. And a robust gradient-based solver is proposed to address scalability. Extensive experiments conduct the best performance and consistently outperforms the state-of-the-art schemes in a series of tasks.

### Strengths
The proposed InfoMax designed to maximize overall information by accounting for each sample’s individual contribution while reducing information overlap, with a simultaneous focus on maintaining diversity and importance. And the proposed efficient gradient-based solver makes InfoMax scale to large-scale datasets. The proposed method brings performance enhancements in a series of different tasks.

### Weaknesses
Some typo: a) 95.7 is best result in CIFAR-10 70% setting from Tab. 1.  b) 51.8 should not be bolded in MMUL 10% setting from Tab. 3.
The ablation study for 4 hyper-parameters only conducted in multi-modality pre-training task. For classification and instruction tuning tasks, what kind of impact do the 4 parameters have on the final results?

### Questions
The selection of the four hyper-parameters depends on the specific dataset or task? If it depends on the specific dataset, how should the corresponding hyper-parameters be determined when faced with a new dataset?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper targets at designing a new coreset selection method to enhance the informativeness of the coreset. Specifically, the authors formalize the coreset selection problem as a discrete quadratic programming task. They adopt an objective of indivisual sample contribution minus the redundancies introduced by similar samples within the coreset. An efficient gradient-based solver is introduced to enhance the efficiency for the implementation. The method is proven to be effective on multiple coreset selection benchmarks including both vision and language tasks.

### Strengths
1. The proposed informax solver is interesting, and can be a solution for coreset selection optimization. 
2. The proposed method achieves state-of-the-art performance on multiple benchmarks including both vision and language data. 
3. The presentation of the paper is professional.

### Weaknesses
1. The framework of the proposed Infomax method is reasonable. However, the actual implementation simply adopts the existing submodular and graph cut methods. And there is no comparison with graph cut in the experiment section. Can the authors give more detailed explanation what is the difference of the proposed method from graph cut? Will the proposed gradient-based solver improve the performance over the original graph cut?
2. The authors propose an efficiency enhancement technique, where the original dataset is divided into several subsets, and only the similarity between neighbors is calculated.
    - Have the authors compare the efficiency enhancement technique with some existing efficient similarity calculation techniques, e.g., faiss?
    - The technique is not only applicable to the proposed Infomax method, but also to previous coreset selection methods. The authors claim that the proposed method achieves faster selection compared with D$^2$-Pruning. The comparison seems a little bit unfair.
3. While efficiency is a major advantage of the proposed method, the authors only provide one group of time cost comparison. As the computation time will be affected by the coreset size, more comparison is expected under different coreset sizes. Futhermore, there is also expected to be the time comparison w/ or w/o each proposed efficient module.
4. In section 4.4(a), the text part says partition rate d, but in figure 5(a) it says subset size. Although they refer to the same thing, it would still be better to keep these two terms consistent.
5. The original paper surpasses the limit of 10 pages.

### Questions
1. The authors adopt Dinov2 to extract embeddings for the unsupervised scenario. Will the model choice matter? 
2. The authors apply softmax on $\mathbf{X}$. Will this operation have large influence on the results? How about simple normalize? I cannot see the exact motivation of adopting a softmax here.

### Soundness
2

### Presentation
3

### Contribution
2
