# Consistency Flow Matching: Defining Straight Flows with Velocity Consistency

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Flow matching (FM) is a general framework for defining probability paths via Ordinary Differential Equations (ODEs) to transform between noise and data samples. Recent approaches attempt to straighten these flow trajectories to generate high-quality samples with fewer function evaluations, typically through iterative rectification methods or optimal transport solutions. In this paper, we introduce Consistency Flow Matching (\method), a novel FM method that explicitly enforces self-consistency in the velocity field. \method directly defines straight flows starting from different times to the same endpoint, imposing constraints on their velocity values. Additionally, we propose a multi-segment training approach for \method to enhance expressiveness, achieving a better trade-off between sampling quality and speed. Experiments demonstrate that our \method significantly improves training efficiency by converging 4.4x faster than consistency models and 1.7x faster than rectified flow models while achieving better generation quality

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes integrating a consistency model with a flow matching model by applying an additional velocity field consistency loss alongside the standard sample-space consistency loss. Additionally, it introduces a multi-segment approach to balance sampling quality with efficiency. Experimental results suggest that this method outperforms selected baselines across several benchmarks, demonstrating improved performance.

### Strengths
- The paper is clearly written and easy to follow.
- The approach of enforcing consistency in the velocity field is novel.
- The proposed multi-segment Consistency-FM model is a well-considered design intended to balance sampling quality with efficiency.

### Weaknesses
 - The paper claims that the proposed Consistency-FM model enforces consistency in the velocity field space, unlike the latent consistency model, which applies it directly in the sample space. However, the final consistency loss in Consistency-FM still minimizes the difference in sample space, specifically as $|f_{\theta} - f_{\theta^-}|$. Furthermore, examination of the source code reveals that the weight parameter $\alpha$ for the velocity difference is set to a minimal value (1e-5), calling into question the strength of this claim. These observations suggest that the difference from the standard consistency model is marginal, which may limit the novelty of the approach.
- While flow matching models are generally reported to outperform diffusion models [1], the paper shows only a minor improvement in FID score in Table 1 when compared to the consistency model. It is therefore unclear whether this performance gain arises from replacing the diffusion model with the flow matching model. To clarify this, a baseline using a standard consistency loss (sample space only) in combination with the flow matching model is needed.
- The paper lacks a comprehensive quantitative comparison against prior work. For instance, the CIFAR-10 experiments omit the distillation sampling variant, and the ImageNet 64x64 experiments do not include a direct consistency training variant. Additionally, the ImageNet 64x64 experiments lack a 2 NFE configuration for Consistency-FM. Both the CIFAR-10 and ImageNet experiments omit several key baselines [2][3][4].
- Although the paper introduces a multi-segment Consistency-FM to balance between sample quality and sampling efficiency, it lacks a thorough analysis of how varying NFE steps impact sample quality.

### Questions
- Can the authors provide empirical or theoretical evidence illustrating how velocity-space consistency improves model performance compared to traditional sample-space consistency? Additionally, clarifying the impact of velocity-based consistency on the model’s stability or efficiency could strengthen this argument.
- The source code reveals that the weight $\alpha$ for velocity difference is set to 1e-5, a very small value. What was the reasoning behind selecting this weight, and how does it impact the model’s performance?
- The reported FID score improvements over diffusion models appear marginal. Can you provide insights into whether these improvements are statistically significant, or are due to the flow matching model itself?
- Include aforementioned key benchmarks to facilitate a more comprehensive comparison. 
- Include an analysis of how sample quality changes with different NFE steps, especially for the multi-segment Consistency-FM model.

### Soundness
2

### Presentation
3

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
The paper proposes Consistency-FM, a method to train generative models in the flow matching framework with an explicit regularization that imposes consistent learned vector fields and hence enables faster inference. The method can be both trained from scratch and distilled from a pre-trained generator. Additionally, self-consistency can be enforced on disjoint trajectory segments to improve the expressiveness of the trained generator. Through experiments the method is empirically shown to converge faster than prior work and produce better quality samples with fewer denoising steps.

### Strengths
The proposed approach is novel and interesting. It produces great results even without distillation, which is a significant step forward in making iterative denoising methods efficient at inference. Theoretical analysis of the proposed loss is provided.

### Weaknesses
The presentation of the paper can be improved. Certain points are rather unclear, as some details are missing from the paper (see Questions section). The paper does not provide any ablation studies or highlight the significance of certain design choices in any form except for motivation (e.g. lines 283-286 for multisegment consistency-fm). This makes it difficult to understand what exactly leads to the results reported in the paper. Nevertheless, I am slightly leaning towards acceptance of the paper, as the strengths outweigh the above weaknesses. However, I expect the authors to address my concerns below in the rebuttal and edit the manuscript accordingly by providing more details. I will update my final rating based on the rebuttal and the other reviews.

Here are some questions and concerns:

1) According to Lemma 1 both conditions are equivalent. While lines 246-247 provide an explanation of why Condition 1 cannot be used alone, the intuition why Condition 2 cannot be used alone is missing. Why is there a need to use both in the loss? Some ablation studies on this could be helpful.
2) In Lemma 1 both conditions are imposed with arbitrary $t$ and $s$. Why in the loss only neighboring points are considered? How does the performance depend on the choice of $\Delta t$?
3) Based on the proof in the Appendix A.3, in Theorem 1, $x_t$ and $x_{t + \Delta t}$ are points on a generative trajectory induced by the ground truth velocity field $u_t$. However, during training, especially in the non-distillation case, this ground truth probability path is unavailable and $x_t$ and $x_{t + \Delta t}$ are sampled from the conditional probability paths. Because of this difference, it seems that Theorem 1 cannot provide intuition on why training from scratch works. Could the authors clarify this?
4) Based on Theorem 1, there is a trade-off between consistency and matching the ground truth vector field. However, this trade-off is not observed in the experiments, where Consistency-FM is always strictly better than the prior work. Could the authors comment on this?
5) Multi-segment Consistency-FM is an interesting extension of the proposed method. Unfortunately, its effect on the results is not demonstrated in the paper. Some ablation studies, e.g. on the number of segments and their sizes, would definitely improve the presentation quality.
6) From the paper and the implementation details in section 4 it is not clear, which configuration of the method was used for the experiments. E.g. what is the value of $\Delta t$? Was multi-segment consistency-fm used? Is the number of the segments equal to the NFE in Tables?
7) Assuming that the models are trained with the multi-segment approach, can a model trained with $K$ segments be used with a different number of NFE at inference?
8) How exactly is the GAN loss integrated in the training?
9) Some points in the proofs could be expanded. E.g. step 3 in line 829.

Some typos:
1) L093 - sample with one NFE, ~~but~~ they fail
2) L097 - While CMs ~~is~~ are able
3) L107 - Further ~~text-ti-image~~ text-to-image experiments
4) L172 - However, these ~~method~~ methods
5) L298 - First, we ~~analysis~~ analyse
6) L299 - provide ~~a~~ an explicit formula

### Questions
Here are some questions and concerns:

1) According to Lemma 1 both conditions are equivalent. While lines 246-247 provide an explanation of why Condition 1 cannot be used alone, the intuition why Condition 2 cannot be used alone is missing. Why is there a need to use both in the loss? Some ablation studies on this could be helpful.
2) In Lemma 1 both conditions are imposed with arbitrary $t$ and $s$. Why in the loss only neighboring points are considered? How does the performance depend on the choice of $\Delta t$?
3) Based on the proof in the Appendix A.3, in Theorem 1, $x_t$ and $x_{t + \Delta t}$ are points on a generative trajectory induced by the ground truth velocity field $u_t$. However, during training, especially in the non-distillation case, this ground truth probability path is unavailable and $x_t$ and $x_{t + \Delta t}$ are sampled from the conditional probability paths. Because of this difference, it seems that Theorem 1 cannot provide intuition on why training from scratch works. Could the authors clarify this?
4) Based on Theorem 1, there is a trade-off between consistency and matching the ground truth vector field. However, this trade-off is not observed in the experiments, where Consistency-FM is always strictly better than the prior work. Could the authors comment on this?
5) Multi-segment Consistency-FM is an interesting extension of the proposed method. Unfortunately, its effect on the results is not demonstrated in the paper. Some ablation studies, e.g. on the number of segments and their sizes, would definitely improve the presentation quality.
6) From the paper and the implementation details in section 4 it is not clear, which configuration of the method was used for the experiments. E.g. what is the value of $\Delta t$? Was multi-segment consistency-fm used? Is the number of the segments equal to the NFE in Tables?
7) Assuming that the models are trained with the multi-segment approach, can a model trained with $K$ segments be used with a different number of NFE at inference?
8) How exactly is the GAN loss integrated in the training?
9) Some points in the proofs could be expanded. E.g. step 3 in line 829. 

Some typos:
1) L093 - sample with one NFE, ~~but~~ they fail
2) L097 - While CMs ~~is~~ are able
3) L107 - Further ~~text-ti-image~~ text-to-image experiments
4) L172 - However, these ~~method~~ methods
5) L298 - First, we ~~analysis~~ analyse
6) L299 - provide ~~a~~ an explicit formula

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents Consistency Flow Matching (Consistency-FM) for defining probability paths to transform between noise and data samples. Consistency-FM enforces self-consistency in the velocity field, defining straight flows from different times to the same endpoint with velocity constraints. A multi-segment training approach is proposed to enhance expressiveness, optimizing the trade-off between sampling quality and speed. Experiments demonstrate that Consistency-FM improves training efficiency while delivering better generation quality.

### Strengths
The design approach based on velocity consistency introduces novel methods for optimizing, distilling, and sampling diffusion-based models in detail.

The idea of multi-segment optimization is very novel and effective. Additionally, the theoretical derivation of the training objectives is provided in detail. Experimental results, including FID and CLIP scores, demonstrate the superiority of the proposed methods.

### Weaknesses
The comparison of visualized samples does not show the advantages of the proposed method clearly. Visual quality is judged by humans based on a few samples, and diversity is also a critical metric.

Comparisons of training time to model convergence are important for a comprehensive evaluation but are missing in this paper. Furthermore, I suggest the authors provide a unified metric to measure both quality and speed.

In Theorem 1, the authors consider no exponential moving average, and the ground truth velocity field is assumed to be known. I recommend discussing the impact of these assumptions on practical applications.

The role of the second term in Equation 6 needs further explanation. The first term's role in striking a balance between exact velocity estimation and adhering to consistent velocity constraints is well explained in Remark 1. A similar explanation is needed for the second term.

### Questions
In Theorem 1, the authors consider no exponential moving average, and the ground truth velocity field is assumed to be known. I recommend discussing the impact of these assumptions on practical applications. 

The role of the second term in Equation 6 needs further explanation. The first term's role in striking a balance between exact velocity estimation and adhering to consistent velocity constraints is well explained in Remark 1. A similar explanation is needed for the second term.

### Soundness
3

### Presentation
3

### Contribution
3
