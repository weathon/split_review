# Context-Aware Unsupervised Domain Adaptive Lane Detection

- Decision: Reject
- Scores: 6, 3, 3, 5

## Abstract
This paper focuses on two crucial issues in domain-adaptive lane detection, i.e., how to effectively learn discriminative features and transfer knowledge across domains. Existing lane detection methods usually exploit a pixel-wise cross-entropy loss to train detection models. However, the loss ignores the difference in feature representation among lanes, which leads to inefficient feature learning. On the other hand, cross-domain context dependency crucial for transferring knowledge across domains remains unexplored in existing lane detection methods. This paper proposes a Context-aware Unsupervised Domain-Adaptive Lane Detection (CUDALD) method, consisting of two key components, i.e., cross-domain contrastive loss and domain-level feature aggregation, to realize domain-adaptive lane detection. The former can effectively differentiate feature representations among categories by taking domain-level features as positive samples. The latter fuses the domain-level and pixel-level features to strengthen cross-domain context dependency. Extensive experiments show that CUDALD significantly improves the detection model’s performance and outperforms existing unsupervised domain adaptive lane detection methods on datasets, TuLane, MuLane, and MoLane, especially achieving the best accuracy of 92.24\% when using RTFormer on TuLane.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, author target the domain adaption in lane line detection, identifying two specific problems in prior work and proposes corresponding solutions. Firstly, prior work only focus on pixel level feature and ignore inter-lane feature presentation. Secondly, prior work don’t adopt cross domain representation for adoption. Authors propose Context-aware Unsupervised Domain-Adaptive Lane Detection (CUDALD) framework, including a contrastive learning function by redesign the sampling method, and a pixel-domain feature aggregation model to enrich representation. Authors shows that the proposed method achieved SOTA on multiple dataset.

### Strengths
1. Author have targeted a very specific, often ignored problem, domain adaption for lane line detection, which is a critical problem in modern ADAS. 
2. Author identify two problems in prior work adopting solution from a general domain(eg, domain adaption for segmentation), and propose solution specific designed for laneline domain adaption, showing improvement over prior art.

### Weaknesses
1. There’s limited discussion, comparison and analysis over prior work that also target specifically on laneline domain adaption, for instance, MLDA(Li et al., 2022). The statement in introduction that 'Unfortunately, achieving cross-domain context dependency in domain-adaptive lane detection remains unexplored.' is also less accurate as prior works like MLDA already explored this domain.
2. Author only conduct experiment on TuLane, MuLane, and MoLane, three simulated lane datasets proposed from one single work, the result would be more convincing if authors could conduct domain transfer experiments between Tusimple and Culane, which are more commonly used dataset for the community. 
3. This work is a bit hard to follow, for instance, in 3.3, author use ‘features from a whole domain is more beneficial’ as a core argument over prior work, without clearly pointing to ‘what is whole domain and how does the method align with whole domain’ in the following implementation. The implementation is also hard to follow without clearly define ‘lane feature and domain feature’ in the first place. 
4. The conclusion of ‘with more advanced lane detection methods, e.g., anchor-based methods’ is also lack of context. Firstly, in the related work, author stated that ‘In this paper, we consider segmentation-based domain-adaptive lane detection.’, which contradict with the conclusion. Secondly, author hasn’t provide why context why ‘author based’ method is superiority over other method’. 
5. Author mentioned the term PSMMs for multiple time in the introduction and related work, without explicitly explain its functionality. It would be easier to follow if author could briefly explain its functionality earlier in the paper. 
6. Please also include proper citation of work for table4/5, and the last two page of the paper.

### Questions
it's still less clear to me what the motivation and implementation of cross-domain contrastive loss. It seems like the only change author proposed is a novel sampling method, please make this clear.

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
This paper proposes that ineffectively learning discriminative features and transferring knowledge across domains are two crucial issues in domain-adaptive lane detection task, and introduces a method named context-aware unsupervised domain-adaptive lane detection which is consisted of cross-domain contrastive loss and domain-level feature aggregation to tackle these issues.

### Strengths
1.	The incorporation of contrastive loss and feature aggregation strategies, as evidenced by the experimental results, appears to be a valuable addition to the paper.
2.	The experiment is sufficient.

### Weaknesses
1.	Lack of inspiration. While the article focuses on unsupervised domain-adaptive lane detection, it makes me confused whether its proposed issues, i.e., ineffectively learning discriminative features and transferring knowledge across domains could be applied to all unsupervised domain-adaptive segmentation tasks. It prompts consideration of whether the issues discussed are universal or specific to this particular domain. Additionally, the introduction of contrastive loss and feature aggregation, while useful, may not fully justify the article's contribution, as these methods are well-established in domain-adaptation field.
2.	The quality of writing and diagrams in the paper requires improvement. Several definitions provided in the article lack clarity, hindering reader comprehension. For instance, in section 3.2, the term 'anchor' is introduced without a precise definition. Additionally, the role of modules is not adequately explained, such as how the introduction of PSMM ensures the appropriate assignment of positive samples. Furthermore, the figures lack detail and refinement, and the overall layout, as seen in Figure 2, does not appear to be carefully designed.
3.	Some conclusions of the article are exaggerated. For example, in section 4.3, the authors claim that their method performs significantly better than other methods when using ERFNet as the detection model, but choosing PyCDA (Accuracy/%: 86.73) and MLDA(Accuracy/%: 88.43) to compare instead of SGPCS with the accuracy of 89.28%.

### Questions
See the Weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a Context-aware Unsupervised Domain-Adaptive Lane Detection (CUDALD) to improve feature discrimination and cross-domain knowledge transferring in the domain-adaptive lane detection field. To this end, the authors introduce two key components: cross-domain contrastive loss and domain-level feature aggregation. The former aims to effectively distinguish feature representations among categories while the latter combines domain-level and pixel-level features to enhance cross-domain context dependency. Extensive experiments on TuLane, MuLane and MoLane datasets verify the effectiveness of the proposed method.

### Strengths
- Aggregating the contextual information from the whole domain for pixel feature enhancement is logically sound and interesting. Despite its simplicity, this concept yields significant performance improvements compared to current state-of-the-art baselines.
- The authors conducted comprehensive comparison and ablation experiments on a wide range of benchmark datasets, confirming the effectiveness of their proposed approach.
- This paper is well-structured and well-explained. The method is accompanied by sufficient details and illustrative diagrams, such as Figures 1 and 2. 
- Extensive visualization results and qualitative comparisons, e.g. Figures 4 and 5, further highlight the advantages of the proposed approach.

### Weaknesses
- Limited originality in cross-domain contrastive learning. This component heavily relies on the previous work (Wang et al., 2021; 2023) and provides an increment improvement (a positive sample selection). It doesn’t strike me as particularly novel. 

- Combinatorial contribution. Each contribution addresses a specific issue in the unsupervised domain-adaptive field. The entire paper lacks content coherence. 

- The title fails to effectively represent the contributions of the paper. 'Context' is a broad concept.
Here, the authors primarily propose aggregating domain-level context for pixel-level feature enhancement. Therefore, it is best to highlight this aspect.

### Questions
Please see the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an unsupervised domain adaptive approach for the lane detection task by utilizing a teacher-student framework and contrastive learning paradigm. Firstly, the method utilizes a positive sample memory module to retain domain-related lane features. Next, unlike existing methods, the authors propose cross-domain contrastive learning to improve feature discrimination. Additionally, a domain-level feature aggregation method is introduced to combine domain-level features with pixel-level features. The proposed unsupervised domain adaptive algorithm achieves the state-of-the-art performance on the TuLane, MuLane, and MoLane datasets.

### Strengths
1. Idea seems fundamentally sound, paper is well written.
2. Pixel-level feature aggregation module considers highly uncertain pixel of background class, which makes sense for me.
3. Experiementation results are provided to support the proposed method.

### Weaknesses
1. The experimentation settings in the paper are confusing as it is unclear which dataset is used as the source domain and which one is used as the target domain. This lack of clarity hinders proper understanding and evaluation of the proposed approach.
2. The paper fails to fully explore publicly available datasets from different domains. It lacks experimentation on datasets such as CuLane and OpenLane, which limits the generalizability and thoroughness of the findings.
3. The algorithm presented in the paper is only applicable to segmentation-based lane detection methods. This limitation reduces its potential contribution since most of today's algorithms tend to be either transformer-based or keypoint-based, making the proposed approach less relevant to current state-of-the-art techniques.

### Questions
While incorporating UBP into the feature aggregation module seems reasonable, the extent to which it contributes to the overall performance remains unclear.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
