# Controllable Continual Test-Time Adaptation

- Decision: Reject
- Scores: 6, 5, 3, 3

## Abstract
Continual Test-Time Adaptation (CTTA) is an emerging and challenging task where a model trained in a source domain must adapt to continuously changing conditions during testing, without access to the original source data. CTTA is prone to error accumulation due to uncontrollable domain shifts, leading to blurred decision boundaries between categories. Existing CTTA methods primarily focus on suppressing domain shifts, which proves inadequate during the unsupervised test phase.
In contrast, we introduce a novel approach that guides rather than suppresses these shifts.
Specifically, we propose \textbf{C}ontrollable \textbf{Co}ntinual \textbf{T}est-\textbf{T}ime \textbf{A}daptation (C-CoTTA), which explicitly prevents any single category from encroaching on others, thereby mitigating the mutual influence between categories caused by uncontrollable shifts. 
Moreover, our method reduces the sensitivity of model to domain transformations, thereby minimizing the magnitude of category shifts. 
Extensive quantitative experiments demonstrate the effectiveness of our method, while qualitative analyses, such as t-SNE plots, confirm the theoretical validity of our approach.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of continual test-time adaptation (TTA) by guiding and controlling shifts by utilizing Concept Activation Vectors (CAV), an interpretability tool for deep learning models.
They control the domain shift by constructing the domain and class shift to control losses.
Experiments show better performance in widely used continual TTA benchmarks.

### Strengths
* Utilizing CAV for the problem of continual TTA
* Proposing domain and class shift controlling losses
* Improving performance on the state-of-the-art benchmarks

### Weaknesses
 * Using pseudo-labels for prototype computation can lead to more error accumulation in real-world
* Motivation for why CAV makes sense for continual TTA and not any deep learning problem, in general, is lacking
* Comparisons with recent approaches such as EcoTTA [1], and BeCoTTA [2] are missing
* The paper does not sufficiently justify the specific choice of Concept Activation Vectors (CAV) over other interpretability methods for controlling domain and class shifts. The connection between the properties of CAVs and the specific requirements of continual test-time adaptation is not clearly established.
* The method's reliance on controlling shifts via losses might be sensitive to the choice of loss functions and their hyperparameters. There is a lack of discussion on the robustness of the proposed approach to different loss functions.
* The paper lacks a thorough analysis of the computational overhead introduced by the CAV computation and the proposed loss terms. This is especially important for test-time adaptation where efficiency is crucial.



### Questions
* How are the hyperpaprameters lambda_1, lambda_2 tuned? Is any validation corruption used?
* Can you report numbers for the two settings when i. lambda_1 = 0, and ii. lambda_2 = 0 to analyze the contribution of different losses.
* Is the paper not just an application of CAV for continual TTA? Is it non-trivial to apply CAV for settings such as TTA?
* Are the DSCL and CSCL losses not applicable to domain adaptation problems in general? If not, why does it make sense for TTA?

**Minor Comments**
* Line 82-83: Typo "Concept Ativation Vectors" --> "Concept Activation Vectors"
* Algorithm 1 does not define p^t_i 
* Some other typos, please proofread

**References**
1. Junha Song, Jungsoo Lee, In So Kweon, and Sungha Choi. Ecotta: Memory-efficient continual test-time adaptation via self-distilled regularization. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 11920–11929, 2023.
2. Lee, Daeun, Jaehong Yoon, and Sung Ju Hwang. "BECoTTA: Input-dependent Online Blending of Experts for Continual Test-time Adaptation." International Conference on Machine Learning, 2024.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Continual Test-Time Adaptation (CTTA) - While most CTTA methods focus on suppressing domain shifts, this paper introduces an approach that aims to guide rather than suppress these shifts. They propose Controllable Continual Test-Time Adaptation (C-CoTTA), designed to maximise inter-class distances while minimising inter-domain distances.

### Strengths
The method demonstrates empirically plausible results, though with reservations that I describe in the weaknesses.

Since this area is outside my expertise, I would defer to my fellow reviewers on the following:

- The relevance of the benchmark tasks and datasets used in this work
- The significance of the reported results
- Any potential biases or issues in the experimental setup

### Weaknesses
The terms "guide" and "control" are vague. More precise language is needed to clearly convey the conceptual mechanism of C-CoTTA. Specifically, could the authors clarify whether the method is fundamentally maximising inter-class distances and minimising inter-domain distances in the representation space? This objective appears consistent with the aims of many test-time adaptation methods. Detailed technical explanation on how C-CoTTA differs from prior approaches would be beneficial, especially avoiding abstract terms like "suppress," "guide," or "control."

It may not be fair to summarise all baseline methods (Tables 1, 2, and 3) as merely "suppressing the shift." Is it accurate to say that these methods do not involve any "guiding" or "controlling" aspects? Further technical support for this claim would strengthen the paper. Perhaps the authors could include an analysis in §4.5 and Figure 4 for all baseline methods listed in Tables 1, 2, and 3.

The terms "guiding" and "controlling" remain ambiguous, especially given that Equation 7 still seems focused on "suppressing the shift" as well. Clear definitions of these terms within the context of C-CoTTA are recommended.

Since many methods are compared in the benchmark with rather small performance gaps, I wonder about the possibility of test-set overfitting. This is especially important given the low-resource nature of the setup (where information about the test distribution is supposed to be only partially available to the learner). It would be helpful if the authors could describe their efforts to minimise this risk (e.g., by confirming if the hyperparameters and design choices in §C were tuned without reference to the test/evaluation split). This would impact the fairness of the empirical comparisons, given the small performance gaps (15.3 vs 14.7 in Table 1, 30.2 vs 29.9 in Table 2, 59.9 vs 59.4 in Table 3).

nit: please run spell/grammar checker
- "Ativation" --> "Activation"
- "only suppress domain shift is insufficient" --> "only suppressing domain shift is insufficient" 
- "explicit control" --> "explicitly control"

### Questions
The conceptual contribution of this work remains unclear. As described, it appears to be a rephrasing of the inter-class distance maximisation and inter-domain distance minimisation approach commonly used in CTTA. How does this approach differ meaningfully from existing methods in CTTA?

While the results slightly outperform previous approaches on average, I have concerns about whether hyperparameter tuning was conducted in a way that avoids overfitting to the evaluation benchmark. Please clarify this in the rebuttal.

My current assessment leans toward rejection. I encourage the authors to address these points in their response.

### Soundness
3

### Presentation
3

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
The paper presents a novel framework for continual test-time adaptation (CTTA), aiming to control domain shifts dynamically during model inference without access to source data or labels. The approach, named C-CoTTA, introduces mechanisms to guide domain shifts to maintain clear class boundaries and minimize error accumulation.

### Strengths
1. The paper addresses a significant challenge in CTTA by proposing a method to control domain shifts, which is crucial for applications in dynamic environments.
2. The approach uses Concept Activation Vectors (CAVs) to represent and control shift directions, which is a well-founded technique in interpretable AI.

### Weaknesses
1. Marginal Improvements: The reported improvements in classification accuracy are relatively marginal (0.6%, 0.4%, 0.5% on CIFAR-10C, CIFAR100-C, and ImageNet-C, respectively). This raises concerns about the practical significance and robustness of the proposed method.
2. Inconsistency in Compared Methods: There is a lack of consistency in the methods compared across different datasets. For instance, ViDA is only included in the ImageNet-C experiments but not in CIFAR experiments. Additionally, the paper does not include comparisons with more recent and potentially more effective methods in segmentation tasks.
3. Metric Validity and Relevance Concerns: The paper uses inter-class and inter-domain distances as metrics to assess class separability and sensitivity to domain shifts. However, the relevance and validity of these metrics are questionable. For instance, the paper does not account for the potential scaling of feature values; if feature vectors $p_i^t$ and $p_j^j$ in line 414 are simply scaled up by a factor (e.g., doubled), the computed distances would also increase, suggesting greater separability without actual improvement in class distinction. This is illustrated by the example where different domains with similar inter-class and inter-domain distances exhibit significant accuracy disparities, such as between the 'Brightness' and 'Contrast' conditions of ImageNet-C, which have a roughly 20% gap in accuracy despite similar distance metrics.
4. The paper does not discuss several relevant works such as [1-5]. This comparison is crucial for situating the novelty of the proposed method within the existing literature.
5. Given the use of labeled source data in the adaptation process, the experiments may not offer a fair comparison to results from methods that do not use labeled source data, rely only on statistics of source data, or do not use source data at all. Clarifying the conditions under which each method is evaluated is essential for understanding and interpreting the experimental results accurately. The evaluation also does not consider the impact of varying amounts of source data used to derive class prototypes, which could significantly impact the method's practical applicability. Furthermore, the paper does not address the potential impact of only using a subset of classes present in each batch during the calculation of domain shift, which could lead to biased adaptation and suboptimal performance across all classes.

### Questions
1. Could you clarify how "random order" is defined and implemented in the experiments mentioned in section 4.8?
2. Does the availability of source data impact the performance of your method? Testing with varying amounts of source data could provide insights into its practical utility when labeled source data is limited.
3. The computation symbol "cov[]" used in formula (1) is unclear. Could you provide a definition or explanation?
4. Can you elaborate on the relationship between formulas (7) and (8)? What is the underlying intuition linking these formulas?
5. Considering practical constraints where not all classes may appear in each batch (e.g., batch sizes less than 1000), how might this affect the calculation of domain shift direction and the applicability of formula (9)?
6. Typo in lines 71 and 73. DSCL $\rightarrow$ CSCL?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes Controllable Continual Test-Time Adaptation (C-CoTTA), a method that enables models to adapt to continuously changing domains during test time without access to the original source data. 

Unlike traditional CTTA approaches, which primarily focus on suppressing domain shifts to mitigate error accumulation, this approach controls the direction of domain shifts to prevent category confusion. By leveraging Concept Activation Vectors (CAV), the method controls the feature shift direction for each class, while domain- and class-level shift control loss functions enhance classification performance.

### Strengths
The strength of this paper lies in introducing a new loss function to actively control domain shifts within the CTTA framework. This approach not only tackles error accumulation but also provides a way to maintain clear boundaries between classes during continual adaptation.

### Weaknesses
1. There are a lot of grammatical errors that hinder readers from concentrating on the paper.
For example

- Line 109: focuses ⇒ focus

- Line 112: they are designed ⇒ they designed

- Line 124: Andres et al. (2022). no parenthesis in the reference.

- Line 157: refer to ⇒ refers to

- Line 225: calculates ⇒ is calculated

- Line 231: weird sentence

- etc.

Also, there are quite a lot of notational errors

- eq 2: $\mathcal{X}_t$ and $\mathcal{X}_s$ are undefined

- eq 3 and 4: inconsistent notation (both subscripts and superscripts are used to indicate the same objects)

- Line 216: $i$ is undefined

Poorly structured English and inconsistent symbols can indeed make the core concepts harder to follow, even if the underlying ideas are strong. Improved clarity in language and notation would make it easier for readers to fully appreciate the novel approach to CTTA and better understand the implementation of the new loss functions for domain control.

I recommend that the authors thoroughly revise the grammar and notation before resubmitting the paper to a new venue.

2.The idea of using a domain prototype was originally proposed in the UDA task, so it’s not a new concept. However, it has not been actively utilized in TTA because it’s challenging to obtain an accurate domain prototype given the nature of TTA, which receives online mini-batches as input. What is the mini-batch size used in this experiment? Mini-batch size is considered a significant issue in TTA.

3. It still inherits the weaknesses of previous works that use pseudo labels. Depending on the accuracy of the pseudo labels, there is a possibility that the class shift may be inaccurately estimated.

### Questions
1. Why the symmetric cross-entropy loss is used rather than KL or reverse KL in eq. 10?

2. What happens if a batch contains samples from multiple domains? I wonder how much performance degradation would result from that scenario.

3. Figure 3 is quite intuitive. Can you show similar figures for different target domains over time?

4. The performance of RMT recorded in this paper is lower than the results reported in the original RMT paper, with a noticeable difference. What is the reason for this?

### Soundness
3

### Presentation
1

### Contribution
3
