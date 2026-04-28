# Teaching with Uncertainty: Unleashing the Potential of Knowledge Distillation in Object Detection

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Knowledge distillation (KD) is a widely adopted and effective method for compressing models in object detection tasks. Particularly, feature-based distillation methods have shown remarkable performance. Existing approaches often ignore the uncertainty in the teacher model's knowledge, which stems from data noise and imperfect training. This limits the student model's ability to learn latent knowledge, as it may overly rely on the teacher's imperfect guidance. In this paper, we propose a novel feature-based distillation paradigm with knowledge uncertainty for object detection, termed "\textbf{U}ncertainty Estimation-Discriminative Knowledge \textbf{E}xtraction-Knowledge \textbf{T}ransfer (\textbf{UET})", which can seamlessly integrate with existing distillation methods. By leveraging the Monte Carlo dropout technique, we introduce knowledge uncertainty into the training process of the student model, facilitating deeper exploration of latent knowledge. Our method performs effectively during the KD process without requiring intricate structures or extensive computational resources. Extensive experiments validate the effectiveness of our proposed approach across various distillation strategies, detectors, and backbone architectures. Specifically, following our proposed paradigm, the existing FGD  method achieves state-of-the-art (SoTA) performance, with ResNet50-based GFL achieving 44.1\% mAP on the COCO dataset, surpassing the baselines by 3.9\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a method (UET) for improving knowledge distillation on object detection. UET leverages the MC dropout to estimate the teacher’s knowledge uncertainty, which allows the student to distill diverse knowledge from the teacher. Comprehensive experiments demonstrate the effectiveness of UET.

### Strengths
1.The motivation is convincing, i.e., multiple teachers can provide more diverse and informative supervision to the student.
2.UET can be seamlessly integrated with the existing KD methods and achieve a new state-of-the-art result with FGD [1] on COCO. 
[1]. Focal and Global Knowledge Distillation for Detectors, 2022, CVPR.
3.	UET is successfully extended into classification and semantic segmentation tasks.

### Weaknesses
1.The idea is similar to [1], weakening the overall novelty of this paper, and the major difference with [1] is that the UET also included the original teacher in the distillation process. However, an ablative study on w/ and w/o the original teacher is not given, and the direct comparison with [1] is limited (only Table 3).
2. The superior results in Table 1 and Table 2 are obtained with FGD, which is a strong approach in distilling detectors. Therefore, the comparison with the SOTA KD methods seems to be unfair.
3. The generalization of the proposed method is not fully evaluated. It is expected to embed UET to multiple detectors across different KD methods.
4. In Table 6, what is the student’s knowledge uncertainty (denoted by S). I cannot find relevant statements in the Methods section. Would the authors clarify this.

### Questions
See weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
On this paper, the authors develop a new knowledge-distillation method targeted at the task of object detection. The method works by measuring the uncertainty of the teacher (using MC-dropout) before passing the knowledge to the student, with the idea that this should reduce the amount of noise passed to the student. The method is quite general (it works in both feature and logit distillation, and is trivially extended to classification and segmentation tasks) and is measured in MS-COCO using several convolutional-based backbones, showing that it outperforms other baselines.

### Strengths
I think the paper has the following strengths:

1) The idea is extremely simple, and seems to work okay in practice. In general, I tend to like papers that find gaps in literature, and are obvious in hindsight. So, while it can look A (knowledge distillation) + B (MC-dropout) = C (better results), I actually think that this is a strength rather than weakness of the paper, and are quite happy to see that at times simple ideas can outperform more complex ones.

2) The paper is relatively well written. There are some concerns about the writing (see the weaknesses section), but in general after reading the paper, I think that I understood it quite well, and would be able to reproduce it from scratch without many issues.

3) The paper for most part outperforms the other methods in several detectors, using generalized focal loss, Faster-RCNN, Retina-Net (focal loss) and FCOS, with a ResNet101 teacher and ResNet-50 student, showing a relative completeness of results in both one-stage and two-stage detectors. Furthermore, the authors show results with smaller backbones (Res18/Res-34) in Appendix, and results in classification and segmentation at the end of the paper.

### Weaknesses
I think the paper has the following weaknesses:

1) While the paper is relatively well-written, it still has some writing issues:

a) I feel like the writing in the Method part is slightly obfuscated and gives the feeling that the method is more complex than it is. For example, I find the equations 2 and 3 quite superflous and the writer could have directly gone to equation 4 with minimal changes. I think that the authors should be proud of their simple idea that works well, instead of making it deliberately look more complex.

b) The big claim in the first page 'Why rely on a single teacher's deterministic knowledge when both teachers or even additional ones, may offer diverse insights?' while completely true, is something that is well known in the distillation literature and has been extensively studied in the past. The authors should cite at this sentence previous works:

[A] Son et al., Densely Guided Knowledge Distillation using Multiple Teacher Assistants, ICCV 2021.

[B] Wu et al., One Teacher is Enough?Pre-trained Language Model Distillation from Multiple Teachers, ACL 2021

[C] Pham et al., Collaborative Multi-Teacher Knowledge Distillation for Learning Low Bit-width Deep Neural Networks, WACV 2023

[D] Liu et al., Adaptive Multi-Teacher Multi-level Knowledge Distillation, Neurocomputing 2020

The papers are sufficiently different to this one (ensembles instead of MC-dropout) so putting them in context of this work would strengthen, instead of weakening the paper.

2) The results while at the first look might look strong, there are a few inconsistencies there.

a) In Table 1, the results of CrossKD are not those from the paper, but results reproduced by the authors. It is unclear why the authors have done so, and when you look in the paper, the results are higher than those provided by the authors.

Method mAP AP50 AP75 APS APM APL

CrossKD_authors 43.6 61.9 47.4 26.1 47.9 56.4

CrossKD_paper 43.9 62.0 47.7 26.4 48.5 56.9

UET 44.1 62.3 47.8 26.6 48.2 56.9

As can be seen, the performance improvement from CrossKD (results reported in the paper) is marginal, only 0.2 percentage points in mAP score. Which makes the results of this paper look less impressive than what is reported.

b) Similarly, the results of FGD method reported in Table 2 under FCOS setting are not consistent with those in the paper.

Method mAP APS APM APL

FGD_authors 42.1 27.0 46.0 54.6

FGD_paper 42.7 27.2 46.5 55.5

UET 42.9 27.1 46.8 54.7

In fact, as can be seen, there is next to no improvement in this method when compared to official results of the FGD.

3) Lack of comparisons with Transformer models. While I appreciate the comprehensive evaluation done by the authors, I must say that I was disappointed to not see any Transformer-based method in this paper. Considering that Transformers are the de-facto state-of-the-art methods in virtually any machine learning task, it would have been interesting to see how this method works in Transformer setting. Some recent papers that do KD in Transformer settings:

[E] Miles et al., VkD : Improving Knowledge Distillation using Orthogonal Projections, CVPR 2024

[F] Song et al., Vidt: An efficient and effective fully transformer-based object detector (under Token matching setting), ICLR 2022

4) Lack of reporting in calibration. The entire idea of doing distillation adjusted for noise is to also ensure that the results of the detector are more reliable, not only better. To do so, the authors should have provided calibration results, where they show that their method is more precise than the others. Such an analysis would strengthen the paper and potentially offer new insights.

5) Timing performance. While discussed in Appendix A.5, it is completely unclear to me. If the authors are doing 5, 10 and 15 forward passes, how is it possible that the training time almost does not change at all. I know that backprop of the student takes more time than the forward pass of the teacher, but if you are doing k forward steps that should accumulate and increase the timing (the student will be waiting for the forward passes before the 'teacher knowledge' is passed to it).

Furthermore, it was unclear to me if the authors are doing MC-dropout in the student during inference, and if so, how much does that effect the timing.

### Questions
I have the following questions which the authors should ideally give a response on:

1) Please justify why the results provided in this paper are different to those reported in the original paper (weakness 2)

2) Would it be possible to have some comparison in Transformer models? (weakness 3)

3) Please provide calibration plots/results (weakness 4) and timing performance (weakness 5).

4) Please adjust the citation discussion with regards to weakness 1.

I like the idea of the paper, but I feel that the paper needs to address these issues before it is ready for acceptance. I am initially scoring the paper as (5) but will improve the score providing that the authors give satisfactory responses in my points.

### Soundness
3

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
In this work, we introduce a new strategy that explicitly incorporates knowledge uncertainty, named Uncertainty-Driven Knowledge Extraction and Transfer (UET). The author introduces a simple yet effective sampling method with Monte Carlo dropout (MC dropout) to estimate the teacher’s knowledge uncertainty, integrating knowledge uncertainty into the conventional KD process. The author estimates the proposed method on COCO dataset and achieves 44.1 mAP performance, surpassing baseline by 3.9.

### Strengths
- The paper introduces uncertainty estimation into object detection KD, which is kind novel in my view.
- The proposed UET achieves a SOTA performace on COCO dataset.

### Weaknesses
 - A minor weaknesses I think is that the Monte Carlo dropout needs to sample several times, which may slow down the training process.

 - As shown in Tab 7, LD+UET only increase performance by 0.2 mAP from the LD only model. I am curious about why logit-based KD methods seem to less benefit from UET.
- The UET method adds teacher uncertainty knowledge into the original teacher features. Can the student also generates a uncertainty features and direct imitate the feature uncertainty, which may be more proper in my view.

- The experiments comparing AKD and UET don't show significant difference. More discussion welcomes.

### Questions
- As shown in Tab 7, LD+UET only increase performance by 0.2 mAP from the LD only model. I am curious about why logit-based KD methods seem to less benefit from UET.
- The UET method adds teacher uncertainty knowledge into the original teacher features. Can the student also generates a uncertainty features and direct imitate the feature uncertainty, which may be more proper in my view.

### Soundness
2

### Presentation
2

### Contribution
2
