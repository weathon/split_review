## Human Reviewer 1

### Summary
This work exposes weaknesses in existing backdoor attacks on object detection models and proposes **BadDet+**, a unified and more practical attack framework. BadDet+ uses a log-barrier penalty to force triggered objects to disappear or be misclassified, achieving **position- and scale-invariance**, **robustness to physical triggers**, and **consistent attack behavior**. Experiments show it transfers well from digital to real-world settings and outperforms prior methods without harming clean performance. Theoretical analysis explains how it operates in a trigger-specific feature space, highlighting overlooked vulnerabilities in object detection and the urgent need for better defenses.

### Strengths
1. This paper is well-written. It is easy to follow the key idea of this paper and follow the proposed scheme.

2. Physical benchmark evaluation. BadDet+ achieves stronger synthetic-to-physical transfer than prior work, outperforming existing RMA and ODA baselines while preserving standard performance.

### Weaknesses
1. Lack of evaluation of robustness. In line 92, the authors claim that the proposed scheme has improved the robustness. However, the experimental section only evaluate the fine-tuning defense to support this claim, which is really insufficient. There are plenty of defenses including image transformation, image detection, model pruning defenses to evalute the robustness.

2. Lack of visual demonstrations. I am curious about the proposed backdoor attack's visual demonstrations, which are more direct to show its effectivensss.

3. Lack of intuition behind the proposed loss penalty. Why the sigmoid function can achieve the proposed effect? It needs to be further clarified. 

4. Lack of technical contribution of the proposed scheme. The only design of the proposed backdoor attack lies in the sigmoid function, which seems less challenging and lacks of novelty.

### Questions
1. Where is the formulation of the loss $\mathcal{L}_{det}$?

2. The "ICLR 2025" should be "ICLR 2026".

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
0

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper argues that existing backdoor attacks in object detection are inadequate in terms of inconsistent evaluation and/or unrealistic assumptions. They propose a method that unifies RMA and ODA attacks with a mechanism that suppresses true class predictions. Experiments demonstrate generally improved performance compared to prior approaches.

### Strengths
The paper argues that there are issues with current evaluation approaches, e.g. ASR overstating success and mAP results being skewed by duplicate detections. The proposed TDR is a sound measure to help alleviate some of the issues.

BadDet+ itself is well motivated, and while the underlying idea is simple, unifying untargeted ODA and RMA under a single mechanism is attractive, and the comprehensive experimental results demonstrate its effectiveness.

Overall, this is a good contribution, though perhaps quite incremental.

### Weaknesses
As the authors themselves identify, the approach assumes that training is controlled by the adversary. This is a very strong assumption, though it is not unreasonable to assume such a worst case in some scenarios.

The idea is quite simple and incremental on prior work.

Minor:
- The poor performance compared to BadDet on YOLO for MTSD and PTSD is not adequately highlighted in the main text, where it is stated as "on par with BadDet". Some discussion is in the appendix, but this main text mention feels a bit understated.

- The caption on figure 1 reads a bit confusingly

### Questions
A couple of minor weaknesses above could perhaps be addressed.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper introduces BadDet+, a penalty-based backdoor attack framework for object detection, unifying region misclassification and object disappearance with log-barrier penalties, achieving strong physical robustness and transferability while maintaining clean accuracy, revealing critical security vulnerabilities in detection models.

### Strengths
1. The authors provide a clear and comprehensive related work.
2. The authors identify the incomplete success of traditional backdoor attacks and propose a new loss function to optimize these bad cases, making the backdoor more robust and effective.

### Weaknesses
1. The paper actually adopts a stronger attacker assumption — the ability to manipulate the loss function (i.e., the training process) — which is clearly different from traditional data poisoning attacks. Although I acknowledge the validity of this threat model, I believe the authors should clearly explain these points before introducing their method. Otherwise, comparing it with other data poisoning–based backdoor attacks is, in my view, of limited significance. 
2. The paper does not clearly explain in the methodology section how it becomes “a single formulation that generalizes to RMA and untargeted ODA settings.” I believe providing concrete examples would help make this point much clearer.

### Questions
1. I’m still not quite clear on how Section 4.1 FORMULATION demonstrates that ODA and RMA can be unified under a single framework — I couldn’t find a clear explanation of this point. Also, what if more types of attacks are considered? Can they also be incorporated into this unified framework? In other words, why are ODA and RMA specifically chosen?

2. Why does the paper claim that BadDet+ bridges the synthetic-to-physical performance gap and achieves position- and scale-invariant backdoor behavior? These benefits don’t seem to come from the core method described in Section 4.1 but rather from common data augmentation techniques. If that’s the case, any backdoor attack could be similarly enhanced. In other words, these advantages are not intrinsic to the proposed method itself.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper proposes novel backdoor poisoning attack BadDet+, which includes a loss into the training objective that penalizes the appearance of the true label in top classes (at prediction time).
Using this regularization, the methodology ensures that the scores of the true label drops in presence of the trigger.
Also, the paper proposes novel evaluation metrics, since other attacks could still exhibit the real label as one of the most likely class during prediction, and this is confirmed by the experiments.

### Strengths
+ the simplicity of a training time regularizer makes this technology easy to understand and also to stage
+ the paper also propose an ablation study on the parameters of the methodology, highlighting the depth of the study
+ novel metrics show that previous work might have overfitted the goal of mislabelling rather than being sure that the true label is not considered

### Weaknesses
- the fact that the paper is presenting a new metric, and with this the performances of the proposed methods are way way better than the literature might rise the doubt on the metric being overfit by BadDet+. Hence, it would be better to show some examples also on regular metrics, or ablation studies also on the 0.5 that has been deemed threshold on the IoU. 
- there is no clear technical description of the nature of the trigger, could its shape and color change the entire method? Like triggers that, by chance, are similar to the object on which they are applied, thus being less effective. The paper should better discuss how scenarios like these were avoided.
- even with a different metric, it is different to compare results: were the methods trained in the same settings? Same poisoning ratios? Same trigger sizes? Results might change a lot, considering that the paper states that default parameters have been used for the techniques of state of the art. The appendix provides some insights, but they are not incredibly clear and should be moved to the main paper to some extent.
- limitations are not discussed, the paper draws conclusions without considering possible issues of the proposed approach.

### Questions
1) what happens in same backdooring conditions, i.e. same ratio of poisoning samples, same trigger sizes, etc?
2) what happens whether the metrics AS@50 changes ratio? Like 10 to 90? How this is can be connected to the standard ASR when varying these quantities?

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