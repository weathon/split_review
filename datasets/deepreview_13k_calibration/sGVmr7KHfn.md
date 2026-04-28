# Memory-Assisted Sub-Prototype Mining for Universal Domain Adaptation

- Decision: Accept
- Avg Score: 5.50
- Scores: 8, 3, 5, 6

## Abstract
Universal domain adaptation aims to align the classes and reduce the feature gap between the same category of the source and target domains. The target private category is set as the unknown class during the adaptation process, as it is not included in the source domain. However, most existing methods overlook the intra-class structure within a category, especially in cases where there exists significant concept shift between the samples belonging to the same category. When samples with large concept shifts are forced to be pushed together, it may negatively affect the adaptation performance. Moreover, from the interpretability aspect, it is unreasonable to align visual features with significant differences, such as fighter jets and civil aircraft, into the same category. Unfortunately, due to such semantic ambiguity and annotation cost, categories are not always classified in detail, making it difficult for the model to perform precise adaptation. To address these issues, we propose a novel Memory-Assisted Sub-Prototype Mining (MemSPM) method that can learn the differences between samples belonging to the same category and mine sub-classes when there exists significant concept shift between them. By doing so, our model learns a more reasonable feature space that enhances the transferability and reflects the inherent differences among samples annotated as the same category. We evaluate the effectiveness of our MemSPM method over multiple scenarios, including UniDA, OSDA, and PDA. Our method achieves state-of-the-art performance on four benchmarks in most cases.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on Universal Domain Adaptation (UniDA), a practical DA setting that does not make any assumptions on the relation between source and target label sets. The goal is to adapt a classifier from source to target domain such that both source and target domains may have their own private classes apart from shared classes. The paper claims that existing UniDA methods overlook the intrinsic structure in the categories, which leads to suboptimal feature learning and adaptation. Hence, they propose memory-assisted sub-prototype mining (MemSPM) that learns sub-prototypes in a memory mechanism to embody the subclasses from the source data. Then, for target samples, weighted sub-prototype sampling is used before passing the embedding to a classifier, which results in reduced domain shift for the embedding. They also propose an adaptive thresholding technique to select relevant sub-prototypes. Finally, they adopt the cycle consistent matching loss objective from DCC [24] along with an auxiliary reconstruction loss for training. They show results on UniDA, Partial DA, and Open-Set DA using standard benchmarks like Office-31, Office-Home, VisDA, and DomainNet.

### Strengths
* The motivating ideas for the approach are interesting and intuitive. Further, the technical contributions are novel as well as effective.

* It is intriguing that the auxiliary reconstruction task provides interpretability, which is usually not possible in existing DA solutions.

* The paper is fairly well-written and easy to understand.

* With their method and the advantages of a CLIP-pretrained ViT model, they achieve large improvements over existing ResNet-based methods. While they also show improvements over some existing methods using the CLIP-pretrained model, this will serve as a new strong baseline for future UniDA work.

### Weaknesses
 * Missing sensitivity analysis to hyperparameter $K$ in adaptive thresholding
    * There is no information on how $K$ is chosen to be used in the top-$K$ operation used to compute the adaptive threshold $\lambda$ in Eq. 5. It may be difficult to tune for new datasets.
    * As per Table 6, using a fixed threshold drops the performance by almost 10%, which is alarming. Hence, the sensitivity to $K$ could be important and needs to be studied. It is unclear how the performance varies with different values of $K$ and whether the current choice is optimal. The paper should include an ablation study on the effect of different $K$ values on the final performance.
    * One simple baseline to get rid of $K$ could be to use a higher temperature in the attention computation, i.e. to make the attention distribution sharper. This alternative approach should be explored and compared to the proposed top-$K$ selection.

* Incomplete analysis of sensitivity to hyperparameter $S$
    * As per Fig. 3b, the performance improves drastically when $S$ is increased. But the analysis is only up to $S=40$ and it seems that the performance should improve further if $S$ is increased more. It is important to determine the point at which the performance saturates with increasing $S$ to provide practical guidance for hyperparameter selection.
    * The paper says that “When $S \geq 20$, the performance achieves a comparable level” but there is almost a 3-4% increase when $S$ increases from 20 to 30 and also from 30 to 40. Then, it seems that increasing $S$ further should yield more improvements. The analysis should be extended to higher values of $S$ to fully understand its impact.
    * In any case, it would be good to identify when the performance starts saturating, to help users select the hyperparameter properly for other datasets. The paper should provide a more comprehensive analysis of the impact of $S$ on performance, including the computational cost associated with increasing $S$.

* Missing discussion on training time and memory requirements
    * Given the extra prototypes involved, there should be some discussion on training time and GPU memory usage compared to the baseline DCC. The paper should quantify the additional computational overhead introduced by the memory mechanism and provide a comparison with the baseline method. This is crucial for practical applications of the proposed method.

### Questions
* Please see the weaknesses section.

* Minor comments
    * Paragraph above Eq. 6 has typos, add space after citation of Gong et al. 2019.
    * Fig. 3: increase the font size of text inside the figure to match the caption font size. This will improve the readability of the plots.
    * Paragraph on “Effect of Loss” has a typo: “We” → “we”.
    * Table 6 (last row) has a typo: use math mode in LaTeX for $\mathcal{L}\_{cdd}$.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this study, the authors introduce the Memory-Assisted Sub-Prototype Mining method, which emphasizes the significance of the internal structure within the category. Unlike conventional methods that treat the classes as a whole, MemSPM refines class features and mines sub-prototypes to represent sub-classes, thereby enhancing adaptation performance. The study provides extensive experiments on four benchmarks to validate its performance.

### Strengths
1.	This paper proposes a novel method called Memory-Assisted Sub-Prototype Mining, designed to significantly improve the model’s adaptability. Additionally, the approach provides insightful visualizations, providing a clear understanding of the methodology.
2.	The effectiveness of the proposed method has been assessed through extensive experiments.

### Weaknesses
1.	While the proposed method demonstrates effectiveness, it appears that the learned sub-prototype does not effectively handle the most challenging aspect of UniDA, such as identifying common and private samples. The Sub-Prototype Mining method seems better suited for general domain adaptation problems rather than specifically addressing the complexities of UniDA. The method's reliance on sub-prototypes, while potentially useful for capturing intra-class variations, does not inherently solve the core issue of distinguishing between known and unknown classes in the target domain, which is crucial for UniDA.
2.	The paper lacks explicit clarification on how the sub-prototype is initialized and updated, leaving a gap in understanding the methodology. The absence of details regarding the initialization process and the iterative updating mechanism of the sub-prototypes makes it difficult to assess the robustness and stability of the proposed approach. This lack of clarity also hinders reproducibility.
3.	Section 3.5 is unclear and requires further elaboration. The concept of cycle-consistent alignment needs to be more explicitly reflected in the training phase. Additionally, a comparison of performance differences with other alignment strategies would enhance the paper's comprehensiveness. The current description of cycle-consistent alignment is vague, and it is unclear how this alignment is integrated into the overall training objective and how it contributes to the final performance. A more detailed explanation and comparison with alternative alignment methods are needed.
4.	A significant portion of the paper relies heavily on DCC, and the proposed method appears to primarily involve weighting input-oriented embeddings to obtain task-oriented embeddings, which seems to be the only deviation from DCC. This raises concerns about the novelty and originality of the proposed approach. The core contribution appears to be limited to the introduction of sub-prototypes and their weighting, while the overall framework largely inherits from DCC. The incremental improvement over DCC needs to be more thoroughly justified.

### Questions
1.  In part 3.3.1, there are N memory items stored. However, the explanation of how these N items are produced and the relationship between them is not clear. Additionally, this paper does not provide a clear explanation of how the sub-prototypes are generated and updated.

2.  In Table 6, why only show the performance without the domain alignment loss?  Need to report the performance without the regularized loss and the reconstruction loss.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a Memory-Assisted Sub-Prototype Mining (MemSPM) for the UniDA problem, which involves the idea of sub-prototypes.

### Strengths
The idea of sub-prototype is reasonable and worth trying for UniDA.

### Weaknesses
1. The comparison of DCC and MemSPM+DCC is not fair, due to the usage of CLIP in MemSPM. The author SHOULD replace the CLIP with a learnable encoder to achieve a fair comparison.
2. Only involving the idea of sub-prototype is not novel enough for the acceptance of top conference. How to use it to solve the concept shift in Fig.1 for UniDA is the key. However, in my opinion, the loss in MemSPM (i.e. Cycle Consistent Matching) is exactly the same with DCC. So, I can not find anything new here.

### Questions
See the weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the Memory-Assisted Sub-Prototype Mining (MemSPM) method for Universal Domain Adaptation. The primary goal is to better align classes and reduce feature gaps between source and target domains, addressing the limitations of most existing models that do not consider intra-class structures, especially when significant concept shifts exist within the same category. The proposed MemSPM enhances model performance by effectively identifying and learning from sub-classes that have considerable concept shifts, leading to a more reasonable feature space, improved transferability, and interpretability. Experimental results across several scenarios (UniDA, OSDA, PDA) show that the MemSPM method outperforms existing benchmarks in many instances.

### Strengths
The Memory-Assisted Sub-Prototype Mining (MemSPM) brings a novel perspective to the Universal Domain Adaptation domain by addressing the challenge of significant concept shifts within the same category. The paper highlights the limitation of existing models and provides a robust solution to enhance transferability and reflect inherent sample differences. Experimental results support the claims and showcase the model's superior performance in many scenarios.

### Weaknesses
While the paper introduces a novel approach, it could benefit from clearer explanations and visual aids, making the methodology more accessible to readers. Additionally, the paper could delve deeper into potential drawbacks or limitations of the proposed method. Comparison with a broader set of benchmarks might also provide a more comprehensive understanding of the model's applicability and robustness.

### Questions
- How does the Memory-Assisted mechanism integrate with existing architectures, and what is its computational overhead?

- Are there any specific scenarios or datasets where the MemSPM method might not be as effective?

- Can the authors provide more insights into the annotation/training costs mentioned and how the proposed method addresses this?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
