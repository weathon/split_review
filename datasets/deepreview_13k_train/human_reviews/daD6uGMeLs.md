# Gaussian-Based Instance-Adaptive Intensity Modeling for Point-Supervised Facial Expression Spotting

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Point-supervised facial expression spotting (P-FES) aims to localize facial expression instances in untrimmed videos, requiring only a single timestamp label for each instance during training. To address label sparsity, hard pseudo-labeling is often employed to propagate point labels to unlabeled frames; however, this approach can lead to confusion when distinguishing between neutral and expression frames with various intensities, which can negatively impact model performance. In this paper, we propose a two-branch framework for P-FES that incorporates a Gaussian-based instance-adaptive Intensity Modeling (GIM) module for soft pseudo-labeling. GIM models the expression intensity distribution for each instance. Specifically, we detect the pseudo-apex frame around each point label, estimate the duration, and construct a Gaussian distribution for each expression instance. We then assign soft pseudo-labels to pseudo-expression frames as intensity values based on the Gaussian distribution. Additionally, we introduce an Intensity-Aware Contrastive (IAC) loss to enhance discriminative feature learning and suppress neutral noise by contrasting neutral frames with expression frames of various intensities. Extensive experiments on the SAMM-LV and CAS(ME)$^2$ datasets demonstrate the effectiveness of our proposed framework.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper treats facial expression spotting as a point-supervised temporal action localization (P-TAL) problem. Drawing from existing P-TAL techniques, the authors propose a two-branch framework for localizing facial expressions. One branch, known as the action-classification branch, predicts the category scores of the facial expression $S$, while the other branch predicts its intensity score $a$.

The framework utilizes a proposed Gaussian-based Instance-Adaptive Intensity Modeling approach to establish soft pseudo-labels for each frame based on the predicted intensity and the given point label. The expression intensity branch is optimized by minimizing the difference between the predicted intensity and the soft pseudo-label, while the action-classification branch employs cross-entropy loss, with class labels also derived from the soft pseudo-label. To reduce neutral noise further, the authors introduce an intensity-aware contrastive loss.

The proposed method is evaluated on two datasets containing both macro and micro facial expressions. Experimental results indicate that this approach surpasses state-of-the-art P-TAL methods in the task of facial expression spotting.

### Strengths
1. The setting of point-supervised facial expression spotting is more practical than fully-supervised facial expression spotting.

2. The proposed intensity-aware contrastive learning is interesting. Rather than simply pulling together the same-class instances and pushing apart the different-class instances, the authors consider the influences of intensity, i.e., less attention should be paid to the same-class instances with large intensity differences, and to the different-class instances with small intensity differences.

### Weaknesses
1. In the proposed method, the intensity score is shared across all facial expression classes. However, two or more facial expressions may occur within a short clip, each with distinct apexes. This raises a concern: what happens if the method is applied to an untrimmed video containing two closely timed apexes of different facial expressions? It would be beneficial to discuss how the model handles this scenario. Furthermore, the intensity score is treated as 'class-agnostic', but it is unclear if this refers to the basic emotional classes (e.g., 'happy', 'sad') or the MaE/ME categories. A clear definition of 'emotional-class-agnostic' intensity is needed, as the intensity of different emotional expressions might vary significantly.

2. The presentation of the inference lacks sufficient detail. Specifically, it would be helpful to clarify what the outer-inner-contrastive score is and how these scores contribute to determining the temporal range and position of the facial expressions. The description of how multiple thresholds are used to generate proposals is vague, and it is unclear how these proposals are then refined using the OIC score. The process of discarding redundant proposals needs more elaboration.

3.  The soft pseudo-label is established based on the predicted intensity scores. However, these predicted intensity scores can fluctuate throughout the training process. It would be helpful to clarify how the soft pseudo-label is updated in response to these changing intensity scores. The method of updating the pseudo-apex frame and the range for assigning soft pseudo-labels based on updated features and intensity output is not clearly explained, and how this iterative process converges is not discussed.

4. The legend of Fig 4 is unclear. The marks of ground-truth boundary frame are missing.

5. The 'random selection' strategy for handling multiple soft pseudo-labels is interesting, but the results in the table do not convincingly demonstrate that 'random' is the best approach. It is not clear why 'random' would outperform other strategies, such as using the accumulated values of the MaE and ME. The intuition behind choosing a random label over other options is not adequately explained.

### Questions
Please refer the the questions.

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
5

### Summary
In this paper, the author introduced a two-branch framework for Point-supervised facial expression spotting (P-FES) task. 
The proposed framework consists of two main branches: (1) Expression Intensity branch with a proposed Gaussian-based instance-adaptive Intensity Modeling (GIM) to model the intensity distribution of expression proposals; and (2) Action-Classification branch to classify the expression class from the proposals.
An Intensity-Aware Contrastive Learning on pseudo-labeled frame is also presented to enhance the discriminative feature learning process.
Experiments on SAMM-LV and CAS(ME)2 have shown the advantages of the proposed approach.

### Strengths
- The paper addresses interesting issue of facial expression spotting.
- Ablation study has shown some contributions of the proposed terms.

### Weaknesses
Although the soft-label is well-motivated, it has been widely used as a label smoothing technique in literature.
Moreover, the training process is complicated and ad-hoc with 3 training stages. However, the improvement is minor and cannot out-perform F-FES techniques.


1. During the training process, warm-up epochs are very important as both features and scores are not reliable for mining steps (i.e. extract pseudo-apex frame, gaussian modeling and reliable pseudo-neutral frames). Then, hard label technique is required. As a result, the proposed framework can only give a minor improvement on top of hard label technique. 

2. In the proposed framework, one of the mining step is to extract pseudo-neutral frames. This will be challenging for ME classes as the micro-expression frames will be very similar to neutral frames and their feature difference is minor. How can the proposed framework extract reliable pseudo-neutral frames and achieve better performance on ME classes ?

3. How can the duration of each expression class be chosen?

4. More analysis on the pseudo-apex frame is recommended. 
For example, How are the pseudo-apex frames changing during different training epochs?

### Questions
Please address the concerns in the Weaknesses section.

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
4

### Summary
The article proposes a two-branch framework for Point-supervised Facial Expression Spotting (P-FES), which includes a Gaussian-based Instance-Adaptive Intensity Modeling (GIM) module for soft pseudo-labeling. This framework aims to address the problem of locating facial expression instances in untrimmed videos, requiring only a timestamp label for each instance during training.

### Strengths
1、The motivation of this article is well-founded, and the proposed method effectively addresses the problem of point-supervised facial expression recognition.

2、The experiments are quite comprehensive, and the comparisons with other methods are reasonable.

### Weaknesses
Some details are unclear; see the "Questions" section below for more information.

1、Not all facial expression instances conform to a Gaussian distribution in every situation, such as when someone is suddenly startled. The authors do not seem to address how to handle this special case.

2、I hope that Figure 4 can provide a clearer explanation.

### Questions
1、Not all facial expression instances conform to a Gaussian distribution in every situation, such as when someone is suddenly startled. The authors do not seem to address how to handle this special case.

2、I hope that Figure 4 can provide a clearer explanation.

### Soundness
3

### Presentation
3

### Contribution
3
