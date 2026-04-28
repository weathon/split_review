# MaskTwins: Dual-form Complementary Masking for Domain-Adaptive Image Segmentation

- Decision: Reject
- Avg Score: 5.33
- Scores: 8, 3, 5

## Abstract
Recent works have correlated Masked Image Modeling (MIM) with consistency regularization in unsupervised domain adaptation. However, they merely treat masking as a special form of deformation on the input images and neglect the theoretical analysis, which leads to a superficial understanding of masked reconstruction and insufficient exploitation of its potential in enhancing feature extraction and representation learning. In this paper, we reframe masked reconstruction as a sparse signal reconstruction problem and theoretically prove that the dual form of complementary masks possesses superior capabilities in extracting domain-agnostic image features. Based on this compelling insight, we propose MaskTwins, a simple yet effective learning strategy that integrates masked reconstruction directly into the main training pipeline. MaskTwins uncovers intrinsic structural patterns that persist across disparate domains by enforcing consistency between predictions of images masked in complementary ways, enabling domain generalization in an end-to-end manner. Extensive experiments verify the superiority of MaskTwins over baseline methods in natural and biological image segmentation. These results demonstrate the significant advantages of MaskTwins in extracting domain-invariant features without the need for separate pre-training, offering a new paradigm for domain-adaptive segmentation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a new methodology based on masked image modeling for unsupervised domain adaptation. The paper shows theoretically that the complementary masking strategy outperforms random masking on information preservation, generalization and feature consistency. The proposed methodology is evaluated on natural image segmentation, mitochondria semantic segmentation and synapse detection.

### Strengths
The paper is overall very enjoyable to read. In particular, i find that:

* The paper is clearly written, well-situated in the literature and is easy to read and understand.
* The proposed methodology is original and constitutes and important bridge between SSL and UDA.
* The proposed methodology excels in its simplicity, in particular compared to adversarial UDA frameworks. In particular, i find it noteworthy that the proposed methodology is effective on 3D input (synapse detection), in which it is generally notoriously hard to stabilise UDA training.
* The evaluation is thorough and includes comparisons to a wide range of UDA baselines.
* The theoretical foundation is sufficient for the study’s objectives, but could be strengthened to enhance rigor.

### Weaknesses
The main short comings of the paper seems to be the limited scope of the theoretical analysis and the ablation study.

* First the theoretical analysis does not connect the proposed methodology to the vast literature on the theory for unsupervised domain adaptation, in particular [1], [2], [3]. Instead the theoretical results relate the methodology to a naive masking strategy, which might still provide benefits over other methodologies. The analysis should discuss how the complementary masking strategy affects the domain discrepancy, and how it relates to the generalization bounds in the context of domain adaptation. The current theoretical analysis is limited to information preservation, generalization and feature consistency, which are not sufficient to justify the effectiveness of the proposed method in the context of unsupervised domain adaptation.

* Second, the ablation study does not study the effectiveness of individual parts of the methodology. I find that it is central to include a comparison to a simpler masking strategy, such as the random baseline from the theoretical analysis and to study the impact of each element in the loss. Instead the authors choose to only ablate details on the patch size, mask type and masking ratio. Specifically, it is unclear how much each loss term contributes to the overall performance, and whether the complementary masking strategy is indeed superior to a simpler random masking approach when used within the same training framework. The ablation study should also investigate the impact of the EMA teacher and the AdaIN layers, as these are crucial components of the proposed method.

### Questions
Ablation study:

* How does the framework perform if the naive masking strategy is used compared to complementary masking? (I.e. no complementary loss). And more generally, what is the performance gain of each element in the loss? (i.e. complementary vs. consistency vs. supervised loss.)
* What is the benefit of using an EMA teacher-student framework and what is the effect of not including AdaIN?

Evaluation:

*  How many folds/runs are the evaluation results based on?
*  How stable is the training? (i.e. the variance of the runs.)


Overall i find that the paper is important and I am inclined to reconsider my score if above points are addressed in the rebuttal.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes MaskTwins for unsupervised domain-adaptive image segmentation. The key method is dual-form complementary masking, where masked image modeling (MIM) is used to generate dual complementary views of images. This approach enables robust feature learning by enforcing prediction consistency across complementary masked images, allowing for adaptation to target domains without additional learnable parameters. MaskTwins demonstrates strong performance improvements over previous unsupervised domain adaptation (UDA) techniques, achieving state-of-the-art results on diverse datasets, including both natural and biological images.

### Strengths
- This paper provides a solid theoretical basis for the use of dual-form complementary masks.  

- The method could be easily integrated into existing frameworks with minimal overhead.

### Weaknesses
 - This paper is similar to [1]. Therefore, it seems that the complementary masking techniques are not novel.

(1) Both papers propose complementary masking techniques to promote robustness. 

(2) Both methods use consistency mechanisms to enforce feature learning. 

[1] Shin U, Lee K, Kweon I S, et al. Complementary random masking for rgb-thermal semantic segmentation[C]//2024 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2024: 11110-11117.

- The method relies on pseudo-labels generated by an exponential moving average (EMA) teacher model for unsupervised target domain training. This dependence on pseudo-label quality could introduce noise into training if the initial pseudo-labels are inaccurate.

- The ablation study of different components in the model should be provided.

### Questions
See section weakness

### Soundness
3

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
This paper addresses the image segmentation problem in the context of unsupervised domain adaptation (UDA). Instead of using the random masks, authors design a dual-form complementary masked images to enhance the generalization of the overall framework. Authors argue that robust, domain-invariant features by enforcing consistency learning upon masked images can be learned. Extensive experiments on six experiments demonstrate the effectiveness of the proposed method.

### Strengths
-- The presentation of this paper is clear.

-- The idea of this paper is easy to understand.

-- The results look good on multiple datasets.

### Weaknesses
 -- It is difficult to justify the contribution of this paper. The overall framework is based on many well-structured techniques, such as AdaIN, EMA-based pseudo label, consistency learning loss, and so on. There lacks an effective ablation study to clarify the gain that is actually taken by the envisioned dual-form complementary masked method. In the ablation study section, only the patch size and the mask type and mask ratio are reported. The reported ablation results show only marginal gains from the proposed complementary masking strategy compared to random masking, making it hard to isolate the specific contribution of this component.

-- The contribution is a bit incremental and over-claimed. At a high level, the envisioned dual-form complementary masked method can be regarded as the constrained entropy minimization like MEMO (Test Time Robustness via Adaptation and Augmentation) . Meanwhile, it seems that the proposed dual-form complementary masked method can also be applied to general classification problem, where we can mask the image in a same manner.  This can verify the authors' first contribution, "This perspective bridges the gap between masked image modeling and signal processing theory, potentially opening new avenues for future research". Applying the proposed method to more general tasks can further show the effectiveness of the proposed method.

-- In the introduction section, the authors clarify that "This insight is grounded in the principles of compressed sensing" and "We provide a theoretical foundation for masked reconstruction by reframing it as a sparse signal reconstruction issue". However, in the method section, there is no any presentation about these descriptions, which is very vague. Authors may reorganize the manuscript carefully. The connection to compressed sensing and sparse signal reconstruction is not clearly articulated in the methodology, making the theoretical claims unsubstantiated.

### Questions
Please the weakness.

### Soundness
2

### Presentation
3

### Contribution
2
