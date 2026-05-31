## Human Reviewer 1

### Summary
The paper introduces a semi-supervised learning approach based on an asymmetric teacher–student scheme that uses CLIP as the guidance model. To mitigate known CLIP biases, the method combines consistency regularization with a lightweight fine-tuning strategy to keep compute overhead modest. A theoretical analysis explores learning with scarce labels, linking label quantity/quality to training dynamics and expected performance. Experiments cover multiple image-classification datasets, with ablations and visualizations that examine the contribution of each component.

### Strengths
- Coherent design and solid empirical gains: The integration of CLIP within an SSL pipeline is thoughtfully engineered; ablations suggest each component contributes meaningfully, and the reported results surpass the listed baselines.
- Clear exposition and positioning: The manuscript is generally easy to follow, and the related-work section situates the method well among comparable SSL approaches.
- Comprehensive experimentation: The empirical section is broad, includes analyses of the proposed regularization and fine-tuning, and emphasizes practical efficiency.
- Interesting theoretical motivation: The analysis connecting pseudo-label quality to labeled-data quality—and to how prototypical the labeled samples are—is insightful and adds value to the overall contribution.

### Weaknesses
- Questionable generality of the “framework” claim: CLIP differs meaningfully from modern VLMs, and CLIP itself is comparatively dated. Without evidence that the approach transfers cleanly to stronger/modern VLMs—or to other tasks—the contribution feels more like a targeted CLIP-based recipe than a broadly applicable framework. Demonstrating adaptability (e.g., with a second teacher family or a distinct task) would strengthen the novelty and impact.
- Scope limited to CLIP-based image classification: While effective in this setting, the study does not explore alternative tasks beyond classification. The paper does not claim multi-modality; however, discussing or lightly probing extensibility (even in a small-scale study) would strengthen the practical generality of the approach.
- Theory presentation could be clearer (minor but actionable):
    - Introduction: grammar around **line 50** needs a pass.
    - Symbols should be explicitly defined when first used: $\epsilon_n$ ,  $r$ , and  $\hat{y}$ 
    - Tightening these points would make the connection between assumptions and the training pipeline more transparent.

### Questions
- Teacher swapability: How readily can the teacher be replaced with stronger CLIP variants or contemporary vision–language models? Are there stability or calibration issues when doing so?
- Beyond classification: What modifications (if any) are needed to extend the method to detection/segmentation or image–text retrieval? Were any preliminary attempts made?
- Sensitivity to prompts and thresholds: How sensitive is performance to text-prompt choices, pseudo-label thresholds/temperatures (if applicable), and augmentation strength?

### Soundness
3

### Presentation
2

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper attempts to address a well-known problem in SSL: the model's performance is heavily dependent on the quantity and quality of the limited labeled data. The authors claim to break this dependency by introducing CaPT. The core idea is to concurrently train a fft unimodal network on images and a parameter-efficiently fine-tuned (PEFT) CLIP model. These two models supervise each other via an entropy-weighted co-pseudo label. The results show that CaPT achieved state-of-the-art (SOTA) performance across multiple SSL benchmarks, especially in extremely low-label settings.

### Strengths
1. The authors have tested CaPT on a wide range of benchmarks, including USB, ImageNet, and several fine-grained datasets, covering various scenarios of label scarcity, label noise, and class imbalance.

### Weaknesses
1. The core contribution of this paper is severely overclaimed. The CaPT, is, in my opinion, nothing more than a simple combination of several existing ideas, such as co-training, adapter-tuning, and mixup.
2. The authors make the assertion that their work breaks the label dependency. In reality, they have merely replaced the dependency on high-quality labels with a dependency on high-quality CLIP prior. This is laid bare in Appendix N: when CLIP performs poorly on the FGVCAircraft dataset, CaPT's performance is low as well.
3. Entropy-based weighting is naive. Did you explore any other, more robust weighting strategies?

### Questions
See in Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces CaPT (CLIP as a Prior Teacher), a novel semi-supervised learning framework that leverages the strong generalization ability of CLIP to reduce the dependency of SSL methods on labeled data.
The key idea is to treat CLIP as a prior teacher, combining its zero-shot semantic knowledge with a unimodal visual learner through an asymmetric co-training mechanism.
The paper also provides theoretical insights into label dependency in SSL and demonstrates significant performance gains on standard benchmarks under extreme low-label conditions.

### Strengths
1. The paper formalizes label dependency in SSL and clearly articulates why existing methods fail when labeled data are extremely scarce.

2. The asymmetric co-training between CLIP and the visual model is simple yet well-motivated, enabling complementary learning between prior knowledge and data-driven adaptation.

3. Extensive experiments on CIFAR, STL, and ImageNet subsets show consistent improvements over strong SSL baselines (FixMatch, FreeMatch, RegMixMatch, etc.), especially in 1-shot and 2-shot settings.

### Weaknesses
1.	While some ablations are included, it would be useful to see results with other multimodal priors (e.g., SigLIP, EVA-CLIP) to confirm generality.
	2.	The paper focuses on SSL baselines but could better position itself against few-shot or distillation-based methods.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes a semi-supervised learning pipeline that leverages CLIP’s prior knowledge in a co-training framework where CLIP is updated with parameter-efficient fine-tuning (e.g., adapters) rather than full model tuning. Experiments on common SSL benchmarks show performance gains.

### Strengths
1. The paper is build on clear motivation with supporting theory showing pseudo-label error grows with prototype bias and fewer labels, formalizing a well-known intuition.

2. The paper proposes a practical strategy to incorporate CLIP in SSL that balances efficiency (adapter tuning, feature-level Mixup) and reliability (co-training + entropy-weighted labels)

### Weaknesses
1.Domain dependence of CLIP priors: where CLIP is strong (e.g., natural images like CIFAR), gains are intuitive; where CLIP is weaker or off-distribution (e.g., EuroSAT and many medical domains), benefits may diminish and are harder to guarantee.


2. Technical contributions feel like a careful combination of known pieces (co-training, PEFT adapters, entropy-weighted pseudo-labels, Mixup)

### Questions
NA

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 5

### Summary
This paper focuses on CLIP-based semi-supervised learning. First, the paper demonstrates through theoretical and empirical analysis that performance is limited by the quantity and quality of labeled data. Then, it proposes a new method called CLIP as a Prior Teacher (CaPT), encompassing three modules: a pseudo-label module based on ViT, an adapter tuning module, and an ensemble module that combines the predictions of the first two modules. Experimental results validate the effectiveness of the proposed method.

### Strengths
The studied problem of semi-supervised learning with CLIP is an important and interesting research topic.

The experimental results are very comprehensive and validate the effectiveness of the proposed method.

### Weaknesses
The proposed approach seems to be a direct combination of the FixMatch approach (module A) and the parameter-efficient fine-tuning approach (module B). Although the co-training technique is interesting, directly combining off-the-shelf approaches may weaken the paper's contributions.

The paper's layout can be improved. First, it is unusual to include a theorem in the introduction. Additionally, it is not rigorous to directly call the different modules "A," "B," and "C." Additionally, there are typos, such as "though" instead of "through" in line 229. Furthermore, the augmentation in Eq. (2) is an addition. However, this is not always true, as many augmentations cannot be implemented by simply adding a feature to another vector or tensor.

Although the co-training scheme is effective, involving a ViT and a CLIP model together is much more complex than the compared methods.

Theorems 1 seem irrelevant to the motivation and the proposed approach. First, it is obvious that the classifier's performance will be inferior with less data, without the need for any theoretical analysis. Second, accuracy is the nearest-prototype pseudo-label error, which is different from the classification model. Third, a larger upper bound does not necessarily indicate a smaller label error.

### Questions
Please see "weaknesses".

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3