# Navigating Neural Space: Revisiting Concept Activation Vectors to Overcome Directional Divergence

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
With a growing interest in understanding neural network prediction strategies, Concept Activation Vectors (CAVs) have emerged as a popular tool for modeling human-understandable concepts in the latent space.
Commonly, CAVs are computed by leveraging linear classifiers optimizing the \emph{separability} of latent representations of samples with and without a given concept. However, in this paper we show that such a separability-oriented computation leads to solutions, which may diverge from the actual goal of precisely modeling the concept direction.
This discrepancy can be attributed to the significant influence of distractor directions, \ie, signals unrelated to the concept, which are picked up by filters (\ie, weights) of linear models to optimize class-separability.
To address this, we introduce \emph{pattern-based CAVs}, solely focussing on concept signals, thereby providing more accurate concept directions.
We evaluate various CAV methods in terms of their alignment with the true concept direction and their impact on CAV applications, including concept sensitivity testing and model correction for shortcut behavior caused by data artifacts. 
We demonstrate the benefits of pattern-based CAVs using the Pediatric Bone Age, ISIC2019, and FunnyBirds datasets with VGG, ResNet, and EfficientNet model architectures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors propose a pattern-based concept activation vectors (CAV), which focuses on concept signal and provides accurate concept directions. Previous CAV methods are designed to compute by leveraging linear classiifers optimizing the separability of latent repsresentations of samples, which is harmful for accurately modeling the concept direction. The authors evaluate various CAV methods in terms of their alignment with the true concept direction and their impact on CAV applications.

### Strengths
- The paper is well written and easy to read. Related work includes several key papers.
- CAVs is widely explored to improve the interpretability of model and this paper tackles an important issue of the current CAV studies and propose a new CAV method named pattern-based CAV.
- The authors measure the alignment of CAVs with the true concept direction by setting controlled environment and the results show that the pattern-CAVs align with the true concept direction.
- The authors show the impact of directional alignment/shift in testing with CAV and model correction.
- Experimental design with real-world datasets look interesting.

### Weaknesses
 - Some relevant papers are missing. It would be informative to clarify the contribution of the proposed method and discuss the pros and cons of the proposed method to better find better position of this paper. Specifically, the paper by Fel et al. should be included in the related work discussion, as it also addresses the unsupervised detection of concept directions, which is relevant to the current work's discussion of unsupervised concept directions. A more detailed comparison highlighting the differences and similarities in methodology and application would be beneficial.
- The paper looks many overlaps with Dreyer et al. It would be great to clarify the novel contribution of this study and add discussion with Dreyer et al. The overlap is not just in the general area of concept activation vectors, but also in the specific application of pattern-based CAVs. The authors should clearly articulate what differentiates their approach from the work of Dreyer et al., particularly in the context of how pattern-based CAVs are derived and utilized.
- The method is evaluated on BoneAge, ISIC2019 datasets. Evaluation on ImageNet/CelebA will make the paper more strong as in Dreyer et al. The current evaluation is limited in scope and does not fully demonstrate the generalizability of the proposed method. Testing on larger, more diverse datasets like ImageNet or CelebA would provide a more robust assessment of the method's performance and its applicability to a wider range of real-world scenarios.

### Questions
- Would it be possible to apply the proposed method on a large realworld dataset like ImageNet?
- Would it be possible to add statistical significance of the results in Table 1?

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
3

### Summary
Concept Activation Vectors (CAVs) is a tool in explainable AI for understanding neural network prediction strategies through human-understandable concepts in latent space. This paper argue that current CAV computation methods, which focus on class separability, often diverge from the actual goal of modeling the concept direction accurately. To address this, the authors propose "pattern-based CAVs," which emphasize concept signals while disregarding distractors. They evaluate their method against various model architectures and datasets, demonstrating that pattern-based CAVs align more closely with the true concept direction and yield improved results in applications like concept sensitivity testing and model correction.

### Strengths
1. The authors clearly identify the limitations of traditional CAV methods, specifically the influence of distractors in filter-based CAVs.
2. The authors conduct extensive experiments on multiple datasets and architectures, providing both quantitative and qualitative results that support their claims. The improved CAV method is demonstrated to benefit important applications, such as TCAV for concept sensitivity testing and ClArC for model correction.

### Weaknesses
1. My main concern is on the limited novelty, it seems that the key idea of pattern-CAV has been proposed, and the paper puts more efforts on evaluation. 
2. The pattern-based CAV method, while precise in modeling concept directions, lacks the boundary optimization and transformation capabilities of traditional linear classifiers (e.g., SVM), which may limit its robustness in complex or noisy datasets. Specifically, the absence of separation-focused optimization could lead to inconsistencies in concept direction in cases with overlapping or ambiguous boundaries. This is particularly concerning in scenarios where the concept boundary is not clearly defined or when the data distribution is highly non-linear. The method's reliance on a direct pattern extraction, without any explicit mechanism to handle such complexities, could result in less reliable concept vectors.
3. The authors focus on achieving high alignment with the true concept direction but acknowledge that in some applications (e.g., post-hoc concept bottleneck models), class-separability may be more critical. A clearer guideline on when to use pattern- vs. filter-based CAVs based on application needs would be helpful. This lack of guidance could lead to misapplication of the proposed method in scenarios where a clear separation of concepts is more important than precise directionality.

### Questions
1. how to address the unsupervised case? I see the descriptions in line 266 and Appendix, could you please provide more details, since the unsupervised is more important in real applications. 
2. In Table 1, why the results of Efficient Net-B0 are quite similar?

### Soundness
2

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
The paper proposed pattern-based CAVs based on Concept Activation Vectors (CAVs). The authors assume that the weight vector of the linear classifier may fail at precisely identifying the concept. To amend this, the proposed method slightly modifies the optimization objective from Eq. (1) to Eq. (2) called pattern-based CAV.

### Strengths
The paper performed a large number of experiments on both toy datasets and controlled datasets.

### Weaknesses
The writing and presentation make the paper hard to follow. It could be better to reorganize the paper to make it easier to understand. For example, it seems better to introduce the concept of TCAV in the Method rather than Experiment section.

The novelty of the paper seems to be somewhat limited. The main contribution Eq. (2) was proposed by a previous work. The authors made a commendable effort to design the dataset, but the technical contribution seems to be the slight modification to the CAV based on linear models.

The datasets used here mainly emphasize hand-crafted concepts ("band-aid", "ruler", "bird", etc.). Is it possible to evaluate the performance on real-world and more realistic datasets like ImageNet?

### Questions
On page 5, "we generate pairs of samples with and without the concept". Was this generation the same or different for different datasets? It could be clearer how a pair for a timestamped image or a bird image is generated (e.g., with examples).

In Figure 5, it seems the performance is heavily dependent on the network architecture, and the results of Logistic, SVM, and Patter, are all very similar to GT if the model is ResNet. Does this mean that if we stick to ResNet as the model, then previous methods like SVM and Logistic are already good enough?

Is there any theoretical analysis of how close the vectors can be to the ground truth concepts?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces pattern-based concept activation vectors (CAVs) that focus solely on concept signals to provide more accurate concept directions, addressing issues with distractor concept directions in filter-based CAVs. The proposed pattern-based CAVs are invariant to feature scaling and more robust to noise. 

The method is evaluated across different datasets and model architectures through both controlled and uncontrolled real-world experiments.

### Strengths
This work proposes a novel computation approach for CAVs, known as pattern-based CAVs, which are less sensitive to distractors compared to existing filter-based CAV methods.

The paper is well-written and well-structured, presenting multiple experimental results to validate the method’s effectiveness.

The authors objectively analyze the advantages, limitations, and suitable contexts for pattern-based CAVs, highlighting that while pattern-based CAVs offer more accurate concept signals, filter-based CAVs emphasize concept separability, which is important for tasks such as concept-based image classification.

This paper offers valuable insights by highlighting issues with existing filter-based CAVs in the presence of noise and feature rescaling, as well as potential challenges when using filter-based CAVs for TCAV and model explanation.

### Weaknesses
However, I have the following concerns:
1. In Table 1, the performance improvements of pattern-based CAVs on the real-world ISIC2019 dataset are not significant, particularly in reducing artifact sensitivity. Given that artifacts (e.g., textual elements in radiology reports or image discrepancies caused by different imaging equipment across medical centers) are hard to avoid in medical contexts, I am concerned that pattern-CAVs may not outperform filter-based CAVs in practical applications.
2. Many medical imaging modalities produce grayscale images, where lesions may be small, and inter-class visual features are often very similar (unlike in ISIC, where subtypes generally have distinct attributes like color or shape). It might be beneficial to include experiments on grayscale datasets, such as Bone Age or similar medical datasets, to better assess the effectiveness of pattern-based CAVs.
3. In the RelMax visualization, samples with the highest neuron activation values are presented. Why do the neurons in the pattern-CAV method have higher activation values than in other CAV methods? Could the authors provide the distribution of neuron activation values across different methods and analyze it? Additionally, could they quantify each CAV method’s ability to identify samples with artifacts (e.g., showing that a certain percentage of neurons with the top activations can identify 95% of samples)?
4. The experiments in the main text should include transformer-based architectures to evaluate the generalizability of the method across different model types.

### Questions
My primary concern is the effectiveness of pattern-based CAVs in real-world applications, including tasks with real artifacts and grayscale image classification, please refer to the weaknesses for more details.

here are some minor questions:

1. A brief introduction to RelMax should be provided for better understanding.

### Soundness
3

### Presentation
4

### Contribution
3
