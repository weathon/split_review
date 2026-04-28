# D2G: Debiased Learning with Distribution Guidance for Generalized Category Discovery

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In this paper, we tackle the problem of Generalized Category Discovery (GCD). Given a dataset containing both labelled and unlabelled images, the objective is to cluster all images in the unlabelled subset, irrespective of whether they are from known or unknown classes. 
In GCD, an inherent label bias exists between known and unknown classes due to the lack of ground-truth labels for the latter. State-of-the-art GCD methods employ parametric classifiers trained with self-distillation using soft labels, leaving the bias issue unattended. Besides, they treat all unlabelled samples uniformly, neglecting variations in certainty levels and resulting in suboptimal learning. Moreover, the explicit identification of semantic distribution shifts between known and unknown classes, a vital aspect for effective GCD, has been neglected. To overcome these obstacles, we introduce the \textbf{D}ebiased Learning with \textbf{D}istribution \textbf{G}uidance (\textbf{D2G}) framework. Initially, D2G co-trains an auxiliary debiased classifier in the same feature space as the GCD classifier, progressively enhancing the GCD features. Moreover, we introduce a semantic distribution detector in a separate feature space to implicitly boost the learning efficacy of GCD. Additionally, we employ a curriculum learning strategy based on semantic distribution certainty to steer the debiased learning at an optimized pace. Thorough evaluations on GCD benchmarks demonstrate the consistent state-of-the-art performance of our D2G framework, highlighting its superiority.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper claims that existing GCD methods suffer from label bias, fail to account for differences in uncertainty, and do not address semantic distribution shifts. To address these issues, the author proposes D2G framework, which comprises Semantic Distribution Detection and Auxiliary Debiased Learning. The Semantic Distribution Detection module treats each labeled category as a separate binary classification, using the prediction confidence score obtained to filter and scale the debiased loss. The additional loss introduced by these components can be directly integrated with SimGCD and these modules can be entirely discarded during inference.

### Strengths
1. The motivation behind addressing label bias is sound to me. Previous methods apply soft supervision to unlabeled data, which results in weaker supervision for unknown classes. The proposed method aligns well with this motivation.
2. The approach achieves performance improvements demonstrating its effectiveness.
3. The framework is efficient in inference.
4. The writing is clear and easy to follow.

### Weaknesses
1. The distribution detector functions as multiple independent binary classification, so there is no competition between categories. It serves two purposes: first, it uses negative class confidence scores to filter out likely unknown classes in the final $L^u_{adl}$; second, it imposes stronger supervision on samples with higher uncertainty. For the first purpose, is there a significant difference in effectiveness compared to using self-entropy to filter unknown samples? Self-entropy would seem a more natural and straightforward metric, yet the author does not analyze the benefits of this one-vs-all design. Specifically, the use of a fixed threshold of 0.5 for the OVA classifier seems arbitrary and may not be optimal across different datasets. A more detailed analysis of the impact of this threshold and a comparison with adaptive thresholding methods would be beneficial. For the second, Equation 10 imposes stronger pseudo one-hot supervision on samples deemed uncertain by the distribution detector. For example, if an unknown class is close to a known class, the loss will be reduced by $d_i$. The ablation study indicates that this yields significant performance gains, but lacks detailed analysis and discussion. The mechanism by which this scaling improves performance is not fully clear, and it would be helpful to see a more in-depth investigation into the effect of different scaling functions or parameters.
2. The D2G framework finetunes more parameters than SimGCD, which only trains the last block. Since D2G builds on SimGCD, it would be more meaningful to compare performance under the same training setup. The authors did not provide this. The lack of a direct comparison with SimGCD under identical training conditions makes it difficult to isolate the specific contributions of the proposed D2G framework. It is unclear whether the performance gains are solely due to the proposed modules or simply a result of increased model capacity.
3. There is a performance drop compared to the baseline on Herbarium19. The performance drop on Herbarium19, despite improvements on other datasets, raises concerns about the generalizability of the proposed approach. The long-tailed nature of Herbarium19 may expose limitations in the method's ability to handle imbalanced datasets, which should be addressed.
4. Since all introduced modules can be discarded during inference, I think the key to performance improvement likely lies in the enhancement of the discriminability of DINO CLS token. However, the authors provide minimal discussion on this aspect. The paper does not adequately explore the impact of the proposed method on the feature space learned by the DINO CLS token. A visualization or quantitative analysis of the feature space before and after applying the D2G framework would be beneficial to understand the underlying mechanisms of improvement.
5. The description of the ablation studies is not sufficiently clear, and there is a lack of discussion between experiments. Specifically, regarding debiased learning, all debiased losses could theoretically be applied directly to the original classifier in SimGCD. It is unclear why the addition of a second classifier is necessary for effective performance. Additionally, I would like to know the impact on performance of removing the MLP prior to the OVA module. The ablation study lacks a systematic investigation of the individual contributions of each component. For example, the impact of the MLP prior to the OVA module should be explicitly evaluated to understand its role in the overall performance.

### Questions
See weakness.

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
This paper propose D2G a novel framework that addresses the challenging GCD task. Several new paradigms and mechanisms like debias learning in this framework enhance the model’s performance. Combined with these, the method proposed demonstrates its effectiveness and achieves superior performance on broad benchmark.

### Strengths
1. The paper writing is clear and easy to understand.
2. The topic of the article is of significant theoretical and practical importance, addressing a gap in the existing literature.
3. The paper clearly outlines the shortcomings of previous studies and results section is logically organized.
4. The proposed framework for DCG is novelty. Various incremental mechanisms make sense to me.

### Weaknesses
1. There is a error in fig.1 (d), the brown dish line is invisible.
2. The hyperparameters in Eq. 14 are empirical values or obtained through experiments? If latter, I believe the authors should include some ablation studies for clarification.
3. In Tab. 2, the performance of D2F is suboptimal compared to InfoSieve, but it lacks a specific analysis. Could the authors provide further details on this?
4. The impact of the various method proposed, such as Debias learning and Auxiliary Classifier, should be evaluated through ablation studies on a broader dataset. The paper currently reports results only on the Stanford dataset. Do authors validate only on this dataset?

### Questions
please refer to weakness.

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
4

### Summary
This paper presents the D2G (Debiased Learning with Distribution Guidance) framework for addressing the Generalized Category Discovery (GCD) problem. GCD is challenging due to label biases and semantic shifts between known and unknown categories. The D2G framework introduces a debiased learning paradigm, a semantic distribution detector, and a curriculum learning approach based on distribution certainty to address these issues. Extensive experiments demonstrate D2G’s superiority over existing GCD methods on various benchmarks.

### Strengths
1. The paper is well-organized, with clear explanations of technical details.
2. The introduction of a debiased learning framework specific to GCD with a multi-feature distribution approach is innovative.
3. The technical contributions are well-structured and effectively evaluated. The integration of auxiliary debiased learning, semantic detection, and curriculum learning reinforces the model's performance.

### Weaknesses
1. The variation in results from the GCD benchmarks can be very large, so it is important to report all results as well as the error bars from the three independent runs, as SimGCD does in its Supplementary Information.
2. While the authors claim that D2G does not introduce additional computational burdens during inference, a more detailed analysis of the training time and computational costs associated with the auxiliary components would be valuable.
3. The paper lacks a thorough discussion on the potential limitations of the debiasing strategy, particularly regarding its sensitivity to hyperparameter tuning and the potential for negative transfer if the debiasing is not carefully controlled. This is especially relevant given the use of an auxiliary classifier, which could introduce its own biases if not properly regularized.

### Questions
1. What strategies do authors envision to reduce potential overfitting during assisted debiasing learning, especially when utilizing limited unlabeled data on fine-grained datasets?
2. Based on Table 4, it can be concluded that the effect of label debiasing is not very good. Have the authors considered not using the label debiasing strategy? For example, what are the results for "w/o debiased learning, w/ auxiliary classifier, w/o semantic dist. learning, w/o dist. guidance"?

### Soundness
2

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
3

### Summary
The authors propose a novel framework called Debiased Learning with Distribution Guidance (D2G) for the GCD task, which introduces a debiased learning paradigm to optimize the clustering feature space and learns a semantic distribution detector to enhance the learning effect of GCD. Besides, D2G propose a curriculum learning mechanism that steers the debiased learning process to effectively mitigate the negative impact of uncertain samples. The authors evaluate the method on the public GCD benchmarks to demonstrate the effectiveness.

### Strengths
D2G considers both label bias and semantic shift to address the challenging GCD task. It’s a novel idea to mark the first exploration of these aspects.
D2G effectively incorporates all components into a unified framework and can be trained in a single stage without any additional computation burden.
The authors conduct extensive experimentation on public GCD benchmarks to demonstrate its effectiveness.

### Weaknesses
1. The reason for using OOD techniques to solve GCD task is not clear because the objectives of these two tasks are different. The motivation for using MLP projection network to solve this problem needs further explanation. Specifically, the paper does not adequately explain why a semantic distribution detector, typically used for identifying out-of-distribution samples, is suitable for addressing the challenges of generalized category discovery (GCD), where the goal is to cluster both known and unknown classes. The connection between detecting OOD samples and improving clustering performance in GCD is not well-established, and the choice of an MLP for this purpose lacks sufficient justification. It's unclear how the MLP's architecture and training process are specifically tailored to capture the nuances of semantic shifts in the feature space.
2. From the experimental results, the performance improvement of the method is not significant, especially on the CUB dataset. Besides, there are few comparison methods on the ImageNet-1K dataset, which can lead to unreliable comparison results. The reported gains, particularly on the CUB dataset, are marginal, raising concerns about the method's practical utility. The lack of extensive comparisons on ImageNet-1K makes it difficult to assess the generalizability and robustness of the proposed approach. The absence of a comprehensive benchmark against a wider range of state-of-the-art methods limits the confidence in the reported results and makes it challenging to determine the true contribution of the method.
3. Some hyperparameters lack ablation experiments to verify that the experimental method is optimal, including the number of layers in MLPs, the loss weights, and so on. The paper does not provide sufficient ablation studies to justify the selection of key hyperparameters, such as the number of layers in the MLP, the weighting of different loss terms, and the learning rate. This lack of analysis makes it difficult to understand the sensitivity of the method to these parameters and whether the reported results are indeed optimal. Without proper ablation, the conclusions drawn from the experiments are less convincing.

### Questions
1. I wonder whether the GCD method is sensitive to certain categories, resulting in limited performance improvement on some datasets. Perhaps the authors can design some experiments to test it.
2. Is it better to use vision-language pre-trained large models such as CLIP to solve label bias problems, as CLIP contains a lot of pre-trained knowledge for new categories.

### Soundness
3

### Presentation
3

### Contribution
2
