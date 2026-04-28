# Machine Unlearning For Alleviating Negative Transfer In Partial-Set Source-Free Unsupervised Domain Adaptation

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 3, 5, 5

## Abstract
Source-free Unsupervised Domain Adaptation (SFUDA) aims to adjust a source model trained on a labeled source domain to a related but unlabeled target domain without accessing the source data. Many SFUDA methods are studied in closed-set scenarios where the target domain and source domain categories are perfectly aligned. However, a more practical scenario is a partial-set scenario where the source label space subsumes the target one. In this paper, we prove that reducing the differences between the source and target domains in the partial-set scenario helps to achieve domain adaptation. And we propose a simple yet effective SFUDA framework called the Machine Unlearning Framework to alleviate the negative transfer problem in the partial-set scenario, thereby allowing the model to focus on the target domain category. Specifically, we first generate noise samples for each category that only exists in the source domain and generate pseudo-labeled samples from the target domain. Then, in the forgetting stage, we use these samples to train the model, making it behave like the model has never seen the class that only exists in the source domain before. Finally, in the adaptation stage, we use only the pseudo-labeled samples to conduct self-supervised training on the model, making it more adaptable to the target domain. Our method is easy to implement and pluggable, suitable for various pre-trained models. Experimental results show that our method can well alleviate the negative transfer problem and improve model performance under various target domain category settings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the Partial-Set Source-Free Unsupervised Domain Adaptation (SFUDA) problem by proposing a novel pluggable framework, termed the Machine Unlearning Framework, designed to mitigate the negative transfer issue in partial-set SFUDA. The framework generates noise samples from the source’s private classes, enabling the model to unlearn and forget the information specific to these private classes. Additionally, it employs self-supervised training using pseudo-labeled target data to optimize the model. The effectiveness of the proposed method is evaluated on two benchmark datasets.

### Strengths
- This paper induces a new aspect to solve the partial-set source-free domain adaptation problem.
- It induces a method based on the guide of negative transfer problems.

### Weaknesses
 - Since the target domain is unlabeled, how do you ensure that the source pre-trained model can accurately identify the target class space $C_t$​?
- How do you substantiate the claim that "the model does not require high-performance hardware," given that your method is described as a pluggable framework?
- In your abstract, you state that $h_s$ is pre-trained with one source domain. Why, then, does your experiment involve a model pre-trained on multiple source domains?
- The benchmarks used are insufficient to demonstrate the efficiency of the proposed method. The authors should consider using DomainNet and VisDA as additional benchmarks.

### Questions
See weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a machine unlearning-based module for partial source-free unsupervised domain adaptation in image classification tasks. The module aims to “unlearn” non-target classes prior to adaptation, reducing the domain shift caused by mismatched label sets between the source and target domains. Pseudo-labeling is then applied for target domain adaptation. Experiments on two benchmark datasets show that incorporating this module enhances the performance of existing methods.

### Strengths
1. Innovative use of machine unlearning to address label mismatch in domain adaptation tasks.
2. Demonstrated effectiveness on the Office-Home and Office-31 datasets.

### Weaknesses
1. Unfair Experimental Setup: The chosen setup is overly complex and seems tailored to fit the proposed method, lacking a strong motivation. It assumes that the target label set is fully known while addressing a partial label adaptation problem in a source-free context. This setup is especially questionable given the recent advancements in vision-language models, such as CLIP, which provide alternative domain adaptation solutions.

2. As a hot-swappable module, it should ideally apply across various source-free models, not only for image classification but also for other tasks like semantic segmentation and object detection. However, only a few baseline models for image classification were chosen for evaluation.

3. The evaluation lacks breadth; a more comprehensive set of benchmarks, such as VisDA, along with various source-target combinations and different backbone architectures, should be included to thoroughly validate the method’s performance.

4. The method relies on top-K pseudo-labeling and unlearning, requiring multiple inference steps, which reduces computational efficiency.

5. The theoretical analysis focuses on the domain adaptation aspect, whereas a theoretical justification of the unlearning mechanism would be more relevant and impactful. For example, why learning data noise for these labels could results unlearning of the original class.

6. While applying unlearning to domain adaptation is interesting, the approach appears to be a straightforward combination of two existing research directions, which limits its contribution—especially within a potentially biased experimental setup.

7. The study does not include a broader range of universal setup SFDA baselines, limiting the comparison and making it difficult to gauge the module's performance against widely accepted SFDA approaches.

8. The paper has some notation and formatting inconsistencies that need correction.

### Questions
See the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Aiming at the problem of partial domain adaptation, this paper proposes the method of machine unlearning. To eliminate the negative transfer effect of source-specific classes on target adaptation, experiments show the effectiveness of the method.

### Strengths
1. The idea of eliminating the influence of  source-specific classes by using machine unlearning is new to some extent, which provides a new insight compared with the classical thoughts of eliminating negative transfer by weighting in adversarial learning in the past.
2. Ablation study was sufficient to demonstrate the effectiveness of the method.

### Weaknesses
1. The frame diagram is not very intuitive, it is best to label each subgraph, and combine the label to explain the frame diagram, N(0,1) in the figure has no explanation, the reviewer needs to find a definition in the main text to understand what to do. And there are many symbols, it is not easy to understand, it is suggested to further optimize the frame diagram and interpretation.
2. Experiments were only performed on the smaller scale of Office-Home/Office-31 and not on the larger scale of ImageNet/VisDA-2017 dataset, which have been extensively covered by classical methods in the past [1,2]
3. The author claims in line 301: "We can easily obtain the category set $C_f$ that only exists in the source domain". However, the method used still relies on the predictions of a model pretrained on the source domain for filtering the target samples. This step still carries a strong source domain bias, and the target samples obtained on this basis cannot guarantee that the selected categories are exclusively from the source domain.

### Questions
1. In the experimental part, the SFUDA method should not be compared only, but should be compared with both the classic and the latest PDA methods to show the effectiveness of the method.
2. Need more explanation on "Why $C_f$ can be accurately selected out without target labels".
3. On the premise of not dealing with negative transfer, SFUDA only needs to ensure sufficient spacing between the classification boundary between classes in the case of cross-domain to achieve partial domain adaptation. So why is it necessary to design modules specifically to eliminate the effects of negative migration?

### Soundness
3

### Presentation
2

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
This paper tackles Source-Free Unsupervised Domain Adaptation (SFUDA) in a partial-set scenario, where the source label space subsumes the target one, risking negative transfer. The authors propose a Machine Unlearning Framework to address this issue by first generating noise samples for source-only categories and pseudo-labeled samples from the target domain. In the forgetting stage, the model is trained to forget irrelevant source categories, while in the adaptation stage, it undergoes self-supervised learning on target data. The framework is simple, adaptable to various models, and improves performance across different target category settings. Experimental results show its effectiveness in reducing negative transfer and enhancing accuracy.

### Strengths
*	The proposed method is effective for SFUDA.
*	The paper is well-written and easy to follow.

### Weaknesses
 *   Experiments on large-scale datasets, such as DomainNet, are missing. Including comparisons on such datasets would further demonstrate the flexibility of the proposed method.
*   Algorithm 1 can be improved. For example, the authors could provide more details on line 3, specifically how the noise samples are generated and what criteria are used to ensure they are sufficiently distinct from the source data. Offering further descriptions for each step of Algorithm 1, including the specific loss functions used in the forgetting and adaptation stages, would enhance the paper's readability.
*   The comparison methods on Tabs. 1 and 2 are out-of-date. It is recommended that the authors include more recent approaches proposed in 2023 and 2024, particularly those that address partial-set SFUDA, to provide a more comprehensive benchmark.
*   The experimental tasks in Tabs. 1, 2, and 3 are also insufficient. For instance, in Tab. 1, the authors should add the tasks A→D, A→W, and W→D for SSDA, and →D, →W for MSDA. The current selection of tasks does not fully explore the method's performance across diverse domain shifts and target complexities.

### Questions
*	Could the authors include more visualization analyses (e.g., t-SNE, CAM, or confusion matrix)? Adding such analyses would further enhance the quality of the paper and demonstrate the effectiveness of the proposed method.
*	The font size on Fig. 2 seems a little bit small, could the authors adjust it?
*	Typo: $x_s^i \to x_t^i$ in line 189.

### Soundness
3

### Presentation
2

### Contribution
2
