# Semi-Supervised Semantic Segmentation via Marginal Contextual Information

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
We present a novel confidence refinement scheme that enhances pseudo labels in semi-supervised semantic segmentation. Unlike existing methods, which filter pixels with low-confidence predictions in isolation, our approach leverages the spatial correlation of labels in segmentation maps by grouping neighboring pixels and considering their pseudo labels collectively. With this contextual information, our method, named \methodname{}, increases the amount of unlabeled data used during training while maintaining the quality of the pseudo labels, all with negligible computational overhead. Through extensive experiments on standard benchmarks, we demonstrate that \methodname{} outperforms existing state-of-the-art semi-supervised learning approaches, offering a promising solution for reducing the cost of acquiring dense annotations. For example, \methodname{} achieves a  1.39 mIoU improvement over the prior art on PASCAL VOC 12 with 366 annotated images. The code to reproduce our experiments is available at \url{https://s4mcontext.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper tackles the problem of semi-supervised semantic segmentation by introducing the S4MC (Semi-Supervised Semantic Segmentation via Marginal Contextual Information) method, which enhances the use of pseudo-labels by considering the spatial correlation among neighboring pixels, rather than treating each pixel in isolation. The confidence-based pseudo-label refinement (PLR) module exploits neighboring pixels (3x3 grid) to adjust per-class predictions, whilst the Dynamic Partition Adjustment (DPA) module gradually lowers the threshold after each training iteration, increasing the number of propagated pseudo-labels (predictions on unlabeled data) without sacrificing quality. Extensive ablative studies justify the authors' design decisions and prove the effectiveness of the approach compared to other state-of-the-art SSL methods on popular benchmarks, such as PASCAL VOC 2012 and Cityscapes.

### Strengths
Originality: The approach offers some degree of novelty - filtering low-confidence predictions by using the context around the pixel, rather than the pixel in isolation (current sota approaches). The contribution is relevant to an actual problem, it increases the use of unlabeled data.
Quality: The method is sound and thoroughly explained. Experiments prove the effectiveness of the approach when applied on top of state-of-the-art methods with a negligible added computational cost. 
Clarity: The paper is an interesting read, well-structured, well-detailed, and very easy to understand (fairly enjoyed reading it). 
Significance: The results offer marginal improvements only in some scenarios, compared to state-of-the-art methods.

### Weaknesses
 * I would suggest changing the main figure of the paper (the elements within the figure are way too small and hard to follow).
* The contribution is not groundbreaking. The +1.29 mIoU gain on PASCAL VOC 2012 and +1.01 mIoU improvement on Cityscapes declared at the beginning of the paper are not backed up by the numbers in the table (Table 1 and Table 3). The numbers in the tables show that the method is not robust enough to offer a consistent improvement in all tested scenarios.  
* The biggest weakness of the paper is Section 4.3 (the ablation studies) and Tables 4 & 5. The text states that the experiments were conducted using the CutMix-Seg framework, but I could not find the numbers in the previous tables. Also in Table 5, the caption states that the numbers are for FixMatch. The text, the numbers, and the tables do not correspond, this part needs further clarification (or another check) because it confuses me the most. 
* Low range of datasets, more experiments that include more varied and challenging scenarios to better understand the method's limitations.
* There are no insights as to why the best window for the used contextual information is in a 3x3 range - this actually suggests that the context is not used properly, or what is actually causing this degradation in performance when more neighboring pixels are used?

### Questions
* There are no insights as to why the best window for the used contextual information is in a 3x3 range - this actually suggests that the context is not used properly, or what is actually causing this degradation in performance when more neighboring pixels are used?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents an approach for performing semi-supervised semantic image segmentation. To address the issue of a threshold-based filtering strategy prevailing in the semi-supervised field, the author proposes a pseudo-label refinement algorithm dedicated to the segmentation task. Specifically, the predicted pseudo-label of each pixel is improved by considering the predictions of that pixel's neighboring pixels using a proposed method. The method achieved state-of-the-art performance on both datasets.

### Strengths
1. The paper is easy to follow and well-structured.
2. It is interesting to explore a refinement method for pseudo-labels that has been rarely discussed in the literature.
2-1. The proposed pixel-selection and propagation concept is simple yet intriguing to the reviewer since this kind of refinement is somewhat novel, as far as I know.
3. The experiments, including the appendix, are thorough and well-designed, providing comprehensive results across all settings.
4. The listed performance demonstrates the effectiveness of the proposed method, significantly improving performance compared to the baseline.

### Weaknesses
The main concern of the proposed work lies in its case analysis. According to the algorithm outlined in Section 3.2.1, the refinement process heavily relies on neighboring pixel predictions. However, we can identify two common failure scenarios in practice:

1. The model may mispredict the majority of interesting regions (e.g., labeling a sofa as a chair or a car as a bus), rendering it unable to refine its predictions with neighboring pixels. This is particularly concerning when the initial pseudo-labels are substantially incorrect, as the propagation mechanism might reinforce these errors rather than correct them. For instance, if a large contiguous region is misclassified, the refinement process, based on the majority of neighboring pixels, will likely propagate this incorrect label, leading to a larger area of incorrect segmentation.

2. In the case of boundary regions, the neighboring pixels may exhibit similar confidence values (lack of confidence). In such instances, the reviewer considers that the proposed method may not perform effectively in these areas. Specifically, if the model is uncertain about the class of pixels along an object boundary, the neighboring pixels will likely also exhibit low confidence, making it difficult for the proposed refinement to make a decisive correction. This is because the refinement relies on a clear majority of confident predictions among neighbors, which is unlikely to occur at boundaries. Furthermore, the method does not explicitly address the inherent ambiguity of boundary pixels, which often require more sophisticated techniques to resolve.

Additionally, it would be beneficial to conduct another ablation study involving the propagation of pseudo-labels based on a k-NN (k-Nearest Neighbors) propagation algorithm with various pixel selection strategies, such as including all neighboring pixels (after filtering out those with low confidence) or other strategies.

### Questions
1. The proposed method is nor working well for the evaluation set. What are the author's reasonable explanations for this?

2. The refinement process appears to be ineffective in the later training period, as indicated by Figure 4-b. What is the reason for this phenomenon?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript presents a technique for semi-supervised learning of semantic segmentation models. The techniue extends previous approaches based on unsupervised consistency where predictions of the teacher branch are used as targets for training the student. In order to avoid meaningless learning, these approaches train only on the most confident teacher predictions. The proposed technique extends this idea by expressing the confidence according to an upper bound of probability of that a small pixel neighbourhood contains more predictions of the same class. The technique changes the baseline method in two ways. First, the learning takes into account more unlabeled pixels since the threshold \gamma_t is a quantile of the pixel-level confidence (5) that tends to be less than the proposed union-level confidence. Second, the consistency loss also works on union-level predictions instead of on pixel-level predictions.

### Strengths
S1 The proposed method can be combined with many existing techniques for semi-supervised segmentation (feature perturbation appears as a notable exception)

S2 The proposed method is conceptually simple and effective; Table 1 claims that it improves the CutMix-Seg mIoU by 4 percentage points on VOC aug with 1/1 training images.

### Weaknesses
W1 Comparison with UniMatch is difficult due to different experimental setups. The authors do not explain the reasons for reproducing UniMatch performance instead of just copying the numbers from the original paper.

W2 Comparison with CutMix-Seg is difficult due to different backbone and different segmentation architecture.  

W3 Experiments do not report variance across different subsets of labeled/unlabeled images.

### Questions
Questions

Q1 Can you provide a comparison with previous work under their original experimental setups?

Q2 Can you confirm that the supervised baselines for all approaches in Tables 1-3 are equal?

Q3 Can you decouple improvement due to threshold \gamma_t being applied to union-level confidence from the improvement due to using union-level predictions in the loss (3)? 

Q4 Why do the blue graph and the orange graph in Figure 4b converge at the end of training?

Q5 Report experiments with ResNet-50 in order to reduce environmental impact and to allow reproduction on modest hardware.

Q6 Explain the difference between the best numbers in Tables 4a/b and Table 5.

Q7 Report minimal hardware requirements (GPU RAM) and computational budget (GPU days) for reproducing the experiments


Suggestions

G1 Consider correcting "coarse PASCAL" as "augmented PASCAL"

G2 Consider rephrasing the term "information gain" since information gain is often considered as a synonym to KL divergence

G3 Improve descriptions of the related work. For instance the sentence with "unreliable prediction" fails to describe the gist of (Wang et al 2022).

G4 Explain where is the experimental performance of CutMix-Seg taken from.

G5 Consider clarifying (3) by replacing \hat[y] with f_{\theta_t}(x_i^u)

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a teacher-student paradigm for the task of pseudo labeling within the context of semi-supervised segmentation. The idea is to have two identical deep learning network for teacher and student. The teacher is only fed with the unlabeled data, while the student network takes in both labeled and unlabeled data, in a bid to dynamically set the threshold of the unlabeled data pseudo label which is used to guide the student network. The pseudo label assignment is done through assessing an event-union probability of a group of neighboring pixels wherein the probability that at least one pixel belongs to a given class is computed. Using the neighboring pixels introduces the contextual cues to enhance the pseudo label propagation.

### Strengths
The angle at which the pseudo labeling problem is solved in this paper is encompassing different aspects of concerns that exist in the relevant literature. Different component of the approach that are put together as a unified module are interesting and may open up new perspective for future research and need further investigation.

### Weaknesses
Although the qualitative results shows smooth segmentation in internal parts of the object, the artifacts are exaggerated in the boundary regions (compared against the baseline) of the segmentation despite the fact that neighboring pixels and the decaying distance-dependent factor are used in the conjunction of each other and it is supposed to refine the segmentation certainty. The paper needs to showcase more segmentation results in the qualitative section because it is not quite clear how the performance is like from only two sets of samples (Fig3). Specially when it is compared against the numerical results in the quantitative section.  Most of the improvement are marginal (less that one percent) in the provided tables (and within the error range) and the correspondence of of the qualitative result to the experiment "partition" is not obvious in this regard.

### Questions
1- The inclusion of neighboring pixels may affect the segmentation in the boundary of the object and it may cause artifacts as it can be seen in Fig 3. The authors have not discussed how they would tackle/minimize this problem.
2- Most of the given samples in the figures contain one object and the background. How is the performance if a complicated background exist with multiple depth facades ?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
