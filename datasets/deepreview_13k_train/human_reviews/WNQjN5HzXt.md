# AUGCAL: Improving Sim2Real Adaptation by Uncertainty Calibration on Augmented Synthetic Images

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Synthetic data (\syn) drawn from simulators have emerged as a popular alternative for training models where acquiring annotated real-world images is difficult. However, transferring models trained on synthetic images to real-world applications can be challenging due to appearance disparities. A commonly employed solution to counter this \sr gap is unsupervised domain adaptation, where models are trained using labeled \syn data and unlabeled \real data. Mispredictions made by such \sr adapted models are often associated with miscalibration -- stemming from overconfident predictions on real data. In this paper, we introduce \augcal, a simple training-time patch for unsupervised adaptation that improves \sr adapted models by -- (1) reducing overall miscalibration, (2) reducing overconfidence in incorrect predictions and (3) improving confidence score reliability by better guiding misclassification detection -- all while retaining or improving \sr performance. Given a base \sr adaptation algorithm, at training time, \augcal involves replacing vanilla \syn images with strongly augmented views (\aug intervention) and additionally optimizing for a training time calibration loss on augmented \syn predictions (\calib intervention). We motivate \augcal using a brief analytical justification of how to reduce miscalibration on unlabeled \real data. Through our experiments, we empirically show the efficacy of \augcal across multiple adaptation methods, backbones, tasks and shifts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes AUGCAL to improve the confidence calibration and model reliability of existing unsupervised domain adaptation approaches. Specifically, the authors propose to replace the original images with strongly augmented ones and additionally optimize for calibration loss on the augmented images. Detailed analytical justification has been derived to show how AUGCAL can reduce miscalibration on real data. Extensive experiments on different datasets and different UDA backbones have been conducted to show the effectiveness of AUGCAL.

### Strengths
1. Extensive experiments on different tasks, datasets and UDA backbones are provided in the paper to evaluate the proposed method. 

2. Theoretical derivations have been provided to motivate the design of AUGCAL.

3. The proposed AUGCAL is simple, which only introduces two small changes to the existing UDA pipelines.

### Weaknesses
1. The technical contribution of this paper is a bit limited. The core idea of AUGCAL combines data augmentation and a calibration loss, both of which have been explored extensively in prior work. While the authors propose to use these techniques in a specific combination for unsupervised domain adaptation, the novelty of this combination is not clearly established. The data augmentation technique, while effective, is not novel in the context of domain adaptation, and the use of DCA for model calibration is also not a new contribution.

2. The evaluation of the proposed method is not sufficiently comprehensive. The paper primarily compares AUGCAL against different backbone UDA models, which does not provide a direct assessment of its calibration performance relative to existing calibration methods. A more rigorous evaluation would involve comparing AUGCAL with dedicated confidence calibration techniques, such as those based on temperature scaling or other post-hoc calibration methods. Without such comparisons, it is difficult to ascertain the specific benefits of AUGCAL over existing calibration approaches.

3. The paper exceeds the page limit of 9 pages.

### Questions
Please refer to the weaknesses.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper starts with a nice theory demonstrating that to achieve better calibration loss in target domain, one should minimize the miscalibration in source domain and reduce the distributional distance between source and target domains. Then, to address this, the paper proposes AUGCAL, which augments the source data and apply a calibration loss on it. Experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. The theory is nice and understandable.
2. The paper is well-written and experiments are extensive.

### Weaknesses
1. Usually adding calibration loss will have lower ECE but also lower accuracy (in your case mIoU). Can you give some intuition in why adding calibration loss on source give better mIoU as shown in Table 3 (a)?
2. This paper proposes two properties and empirically verifies PASTA and RandAugment satisfy the criterion. It would be good to give some intuition in the main text.
3. [1] uses StyleNet which learns a style transfer from source to target, it would be interesting to analyze whether this inherently satisfy the property 1.
[1] Donghyun Kim, Kaihong Wang, Kate Saenko, Margrit Betke, and Stan Sclaroff. A unified framework for domain adaptive pose estimation. In ECCV. Springer, 2022.
4. Do the two AUG choice meet the property 2? Is the \epsilon as small as before AUG?
5. Since equation 9 is the upper bound of calibration loss, how is this related to mIoU?

### Questions
please see weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a general Sim2Real adaptation framework, AUGCAL, for semantic segmentation and object recognition.
AUGCAL introduces synthetic data augmentation and model calibration on synthetic data to reduce miscalibration during synthetic training. Combining with standard unsupervised domain adaptation methods on unlabeled real-world data, those techniques further improve SIM2REAL performance on real-world data.
Especially, this paper provides theoretical analysis to show the target calibration loss can be bound by the source calibration loss. This is the reason that calibration on synthetic data is beneficial for the performance of real-world data. Also, it shows the necessity of introducing the augmentaiton.
Experiments are conducted on GTAV to Cityscapes and VisDA SIM2REAL, and show that the proposed framework can improve the baselines easily.

### Strengths
[Clarity] The paper is well structured, and I find myself easy to follow.

[Baseline] Baselines with AUGCAL outperform those without AUGCAL in all metrics.

[Implementation] The presented method looks straightforward yet effective and easily re-implementable.

[Novelty]
- Augmentation and calibration are complementary and can be integrated easily to achieve the goal.
- Miscalibration is an overlooked factor for unsupervised domain adaptation, and this paper proposes an easy way to handle it.
- The paper provides insights on how the calibration loss on synthetic data can reduce miscalibration on real data via a theoretical analysis. This is beneficial for other related research fields.

### Weaknesses
[Augmentation] The choice of augmentation should satisfy the property 1 in Sec. 3.2.2. Even Tab.1 shows that PASTA/R.Aug-SIM are closer to Real than SIM based on MMD, it is not intuitive. It would be better to clarify it more.
- For PASTA, it is designed to bridge the syn-to-real gap and maybe reduce the artifacts of synthetic data. But I am not sure why R.Aug even closer to Real. 
- Also, if we have large-scale unlabeled real-world data, I am wondering if style transfer-based augmentation will have better performance because it directly uses unlabeled real-world data.
- Last, as property 1 is a distribution distance, I am not sure how those appearance augmentations affected distribution.

[OC] After Eq.3 and in Sec.4, the paper introduces overconfidence (OC) as a metric. But I am not sure of the exact definition.

[Eq.9] Eq.9 shows a useful upper bound. It would be more interesting to provide more insights regarding this bound. For example, what issues (e.g., a large gap between syn and real) and why will those issues lead to the loose of the upper bound?

### Questions
[Augmentation] The choice of augmentation should satisfy the property 1 in Sec. 3.2.2. Even Tab.1 shows that PASTA/R.Aug-SIM are closer to Real than SIM based on MMD, it is not intuitive. It would be better to clarify it more.
- For PASTA, it is designed to bridge the syn-to-real gap and maybe reduce the artifacts of synthetic data. But I am not sure why R.Aug even closer to Real. 
- Also, if we have large-scale unlabeled real-world data, I am wondering if style transfer-based augmentation will have better performance because it directly uses unlabeled real-world data.
- Last, as property 1 is a distribution distance, I am not sure how those appearance augmentations affected distribution.

[OC] After Eq.3 and in Sec.4, the paper introduces overconfidence (OC) as a metric. But I am not sure of the exact definition.

[Eq.9] Eq.9 shows a useful upper bound. It would be more interesting to provide more insights regarding this bound. For example, what issues (e.g., a large gap between syn and real) and why will those issues lead to the loose of the upper bound?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
