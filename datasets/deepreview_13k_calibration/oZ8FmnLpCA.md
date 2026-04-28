# Knowledge Distillation via Flow Matching

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
In this paper, we propose a novel knowledge transfer framework that introduces Rectified flow into knowledge distillation and leverages multi-step sampling strategies to achieve precision flow matching. We name this framework Knowledge Distillation via Flow Matching (FM-KD), which can be integrated with a metric-based distillation method with any form (\textit{e.g.} vanilla KD, DKD, PKD and DIST), a meta-encoder with any available architecture (\textit{e.g.} CNN, MLP and Swin-Transformer), and achieves significant accuracy improvement for the student. We theoretically demonstrate that the training objective of FM-KD is equivalent to minimizing the upper bound of the teacher feature map's or logit's negative log-likelihood. Besides, FM-KD can be viewed as a unique implicit ensemble method that leads to performance gains. By slightly modifying the FM-KD framework, FM-KD can also be transformed into an online distillation framework OFM-KD with desirable performance gains. Through extensive experiments on CIFAR-100, ImageNet-1k, and MS-COCO datasets, we empirically validate the scalability and state-of-the-art performance of our proposed methods among relevant comparison approaches.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes diffusion-like distillation loss named FM-KD. In FM-KD, a meta-encoder converts student representation similar to teacher representation with a recursive process. FM-KD uses all representations during the recursive conversion for KD loss. FM-KD can be expanded to an online KD called OFM-KD. Experiments show the improvement of FM-KD in KD benchmark.

### Strengths
- Introducing a meta-encoder for inference is an interesting approach.

### Weaknesses
 - The method and presentation.

This paper attempts to improve feature representation matching from knowledge distillation. The proposed method FM-KD heavily relies on two existing works DiffKD (arxiv 2023) and Rectified Flow (ICLR 2023). Specifically, the authors directly use Rectified Flow to replace vanilla diffusion in DiffKD, making the diffusion of student representation (either feature or logits) to have straight paths between any two steps. In general, FM-KD is rather incremental. The authors try to claim FM-KD as a totally new knowledge transfer framework, which is applicable to different types of teacher-student architectures, different metric-based distillation methods and different representations. However, it is mostly misleading, as DiffKD has already attained this goal when putting it in the context of the authors' viewpoint. The core idea of using a rectified flow to guide the student's feature representation towards the teacher's is not novel, given DiffKD's existing framework.

Furthermore, the underlying reason for why applying diffusion process to augment feature representation matching in knowledge distillation in not clear enough. What is the reasonable new technical insight here? It's unclear why a diffusion process, even with rectified flow, should inherently improve feature matching beyond what simpler methods might achieve. The connection between the rectified flow's straight paths and the effectiveness of knowledge transfer is not well-established.

In addition, Rectified Flow assumes straight paths between any two steps during the diffusion, so is it reasonable when applying this design to feature representation matching in knowledge distillation? The original purpose of Rectified Flow is for faster diffusion but not more accurate performance. From Table 2 on ImageNet-1K, the proposed method FM-KD merely performs on par or worse than DiffKD. The justification for using rectified flow, which prioritizes speed, over other diffusion approaches that might offer better representational alignment is lacking. The paper does not adequately address whether the straight-path assumption of rectified flow is appropriate for the complex transformations involved in feature matching.

- The limitations.

The authors did not discuss the limitations of the proposed method.

- The experiments.

As the proposed method is closely related to DiffKD, diffusion with Rectified Flow (straight paths) vs. diffusion with vanilla diffusion (non-straight paths), DiffKD and DiffKD+RectifiedFlow should be always used as the baselines instead of others. The experimental design should have included a direct comparison between DiffKD with its original diffusion process and DiffKD with the proposed rectified flow to isolate the impact of this change. The absence of this comparison makes it difficult to assess the actual contribution of the rectified flow.

From Table 2 on ImageNet-1K, the proposed method FM-KD merely performs on par or worse than DiffKD. This raises a critical problem, is it necessary to replace vanilla diffusion (non-straight paths, e.g. DDIM) by Rectified Flow (straight paths)? Why? On the other hand, Rectified Flow assumes straight paths for any two steps during the diffusion, is it reasonable to feature representation matching in knowledge distillation? The experiments do not sufficiently demonstrate the advantage of using rectified flow over other diffusion methods, especially given that the core motivation of rectified flow is faster sampling, not necessarily improved accuracy.

How about the extra cost to the inference with the trained student model? As the architecture of the trained student model is no longer same to the baseline, which violates the basic purpose of knowledge distillation, namely model compression. The paper needs to clarify the computational overhead introduced by the proposed method during inference. If the student model's architecture is modified, it undermines the goal of model compression, which is a key benefit of knowledge distillation.

- Others

There is no discussion on related works in the main paper. I noticed that the authors put this part in the Appendix, but this is not proper, to the best of my understanding.

### Questions
.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses knowledge distillation through improving feature representation matching from the student model to the pre-trained teacher model. Specifically, the authors extend an existing work DiffKD via replacing vanilla diffusion in DiffKD by Rectified Flow (another existing work which makes diffusion process as a flow having straight paths between any two steps). Experiments on image classification (with CIFAR-100 and ImageNet-1K datasets) and object detection (with MS COCO dataset) tasks are provided to show the effectiveness of the proposed method. Different baselines and setups are considered in experiments.

### Strengths
+  Improving feature representation matching is a critical problem in knowledge distillation research.

+ Leveraging diffusion process to augment feature representation matching for knowledge distillation is interesting, although the insight behind it is not very clear.

+ Image classification and object detection with large scale datasets like ImageNet-1K and MS COCO are considered for experimental comparison.

### Weaknesses
•	This paper is similar to DiffKD where it is a combination of generative model and knowledge distillation, except that it replaces the diffusion model with the rectified flow, which has limited innovation.
•	The FM-KD method proposed in this paper modifies the structure of the student network and increases the cost during model inference, which is a shortcoming of a model compression algorithm. The computational cost during inference is not given in the paper, and if refer to Fig. 5, the increase in cost is obvious and there is some unfairness in comparison with other methods. Are there still significant advantages of the FM-KD approach over baseline models that increase the number of parameters to make time-consuming approximations?
•	The experimental performance is not outstanding enough. There is no significant advantage over other knowledge distillation methods in Table 3 of the experiments for object detection, and there are also several tests in the image classification experiments that do not perform as well as other existing methods.

### Questions
Please refer to my detailed comments in "Weaknesses" for details.

### Soundness
3 good

### Presentation
2 fair

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
This paper proposes a new knowledge distillation method FM-KD that combines rectified flow with knowledge distillation. It can be combined with any metric approach and meta-encoder structure, and can be converted to online distillation with minor modifications. The FM-KD method achieves interesting experimental results on the CIFAR-100, ImageNet-1k, and MS-COCO datasets.

### Strengths
•	The FM-KD method is flexible enough to be combined with any metric approach and meta-encoder structure, and can also be converted to an online distillation framework.
•	There are theoretical analyses to support the rationality of the methodological design.

### Weaknesses
My major concern is the generalization, given that distillation is a well-defined topic, but this method seems like doesn't work well in heterogeneous architecture settings. Especially when there is a big difference in size between teacher models and student models.

### Questions
see the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper,  the authors introduce rectified flow into knowledge distillation and leverage multi-step sampling strategies to achieve precision flow matching. It can be integrated with metric-based distillation methods. The authors offered theoretical analysis which demonstrates that the training objective of FM-KD is equivalent to minimizing the upper bound of the teacher feature map's or logit's negative log-likelihood.  And the authors also offered an online distillation version.

### Strengths
1. Distillation is an important topic to our community, the proposed method is simple.
2. Some of the "same architecture setting" results are promising.
3. The write-up is easy to understand.

### Weaknesses
My major concern is the generalization, given that distillation is a well-defined topic, but this method seems like doesn't work well in heterogeneous architecture settings. Especially when there is a big difference in size between teacher models and student models.

### Questions
Can you explain or verify why this method can't work well when the gap is big between teacher and student?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
