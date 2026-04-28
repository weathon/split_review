# REAL: Rectified Adversarial Sample via Max-Min Entropy for Test-Time Defense

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 3, 8

## Abstract
Adversarial attacks expose the vulnerability of neural networks. But it is difficult for existing defense methods to defend against all attacks, which leads to the lack of generalization in adversarial robustness. Inspired by test-time adaptation which leverages model’s prediction entropy to generalize naturally distributed samples during testing, we try to rationally utilize adversarial samples’ entropy for sample rectification, and then achieve test-time defense. In this article, we investigate the entropy properties of adversarial samples and obtain two observations: 1) adversarial samples are often confidently misclassified despite having low prediction entropy and 2) samples with higher attack strength typically show lower prediction entropy. Therefore, we believe directly minimizing the entropy of adversarial samples is not reasonable and propose a two-stage self-adversarial rectification approach: \underline{Re}ctified \underline{A}dversaria\underline{l} Sample via Max-Min Entropy for Test-Time Defense (REAL), consisting of a max-min entropy optimization scheme and an attack-aware weighting mechanism, which can be embedded in the existing models as a plugged-played block. Experiments on several datasets show that REAL can greatly improve the performance of existing sample rectification model.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the properties of prediction entropy in adversarial samples and presents several strategies for adversarial defense. Specifically, it introduces a max-min entropy optimization scheme and an attack-aware weighting mechanism. The results demonstrate that these approaches are compatible with existing models and exhibit strong performance.

### Strengths
- The starting point is novel and the proposed attack-aware weighting mechanism is technically sound.
- The paper is generally well-written and easy to follow. The authors have illustrated their settings and motivations using bullet points to provide a clear understanding of their objectives.

### Weaknesses
 - The limitation of selecting the detection threshold and auxiliary tasks is crucial yet challenging. Besides, in numerous real-world attack scenarios, the specific attack methods are often unknown.
- The motivation behind employing a max-min optimization scheme is unclear. Why is a mask loss necessary in this context?
- Additionally, the experiments conducted seem insufficient, and it would be beneficial to observe more results obtained on ImageNet.
- In the text, $L_{ent}$ and $L_{cls}$ are not consistent. 
- In the preliminary, you'd better provide more introduction and explain about the $\delta$.

### Questions
- If entropy is related to error rate, what about mutual information or signal-to-noise ratio (SNR)? Do they have a similar effect?
- The effectiveness of the max-min optimization scheme lacks convincing evidence. Could you please include a comparison of the robust accuracy of $x_{mask}$ to support your claim further?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a test-time adversarial defense that uses a combination of auxiliary task loss thresholds, entropy thresholds, and two sets of self-adversarial rectification rounds. The method is applied to adversarial defense on MNIST, CIFAR-10, and CIFAR-100, and it is observed that the method can provide robustness to an unsecured classifier.

### Strengths
* The method investigates an ambitious and relevant task of test-time adversarial defense.
* A wide variety of ideas from many different defenses are integrated into a novel method.

### Weaknesses
 * The presentation of the method and the motivation of the difference aspects is somewhat difficult to follow. 
* The primary weakness is that the method appears to be built upon a broken defense, namely the SOAP model. The work [a] reports breaking the SOAP defense using BPDA. I expect that a similar attack could be used against this method. Although this work does present an adaptive attack, from what I can tell the attack does not differentiate through the purification. BPDA provides an efficient way to do this approximately. Re-evaluation of this defense using the methodology in [a] is essential, especially given that this methodology has broken the SOAP defense this work is based on.
* The method does not compare with recent diffusion-based purification defenses such as [b], which generally obtain stronger results than those reported in this work.

### Questions
Can the authors re-evaluate their defense using the adaptive attack used against SOAP in [a]?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Improving adversarial robustness against adversarial attacks is an important but challenging task. This paper presents a critical problem that generalizing to numerous unseen adversarial attacks is difficult but paid less attention in the community, and proposes a new concept, i.e. generalizable robustness. Inspired by test-time adaptation, this paper proposes a new test-time defense methodology in robustness and overcomes the non-reasonable prediction entropy assumption in defense, and designs a two-stage rectification approach, i.e, REAL, through a max-min entropy optimization with attack-aware weighting mechanism. This submission brings some new perspectives that will promote adversarial robustness against unknown attacks. Experiments on benchmark datasets show the proposed REAL greatly improves the robustness of previous sample rectification models.

### Strengths
1. The idea of REAL is interesting, rational, and novel. First, it is valuable to explore new generalizable adversarial defense approaches against unseen attacks. Second, considering that adversarial perturbations are diverse and unseen in real applications, it is rational to establish a test-time training paradigm for removing perturbations. Third, since such a paradigm is still seldom studied in this field, the proposed test-time adversarial sample rectification approach is novel in multiple aspects, which may produce a high impact in related fields.
2. The proposed max-min entropy optimization strategy is new. The authors clearly claim that in conventional test-time adaptation for natural image classification, the entropy loss is commonly used for training unlabeled target data, and successfully reveal that this is not appropriate for adversarial samples as shown in Fig.1. Therefore, the authors propose a natural and novel idea to maximize the entropy of adversarial samples (stage 1) instead of minimization. For the final objective of accurate recognition, stage 2 is formulated for minimizing the entropy of rectified adversarial samples. The two-stage rectification paradigm achieves test-time defense on the fly.
3. Another merit of this paper is the proposed attack-aware weighting mechanism, which is simple but useful. The intuition behind this is clear because each sample should be treated unequally due to the differences in their attacking power. This paper contributes a simple metric of attack strengths by assessing samples' prediction entropy.
4. Experiments on benchmark datasets fully prove the superiority of the proposed REAL method, by plugging and playing in the classical SOAP model.

### Weaknesses
1. Since the auxiliary task is leveraged during test-time optimization, the authors could discuss some choices of different auxiliary tasks, although one may not decide which one is better without empirical observation. Specifically, the paper lacks a discussion on how the choice of auxiliary task impacts the overall performance and robustness. For instance, different auxiliary tasks might lead to varying degrees of alignment with the primary task, and this could affect the effectiveness of the rectification process. A more detailed analysis of this aspect would strengthen the paper.
2. Since this work aims to improve generalization, a more complete setting toward attack generalization can be implemented in the future and produce a higher impact. The current evaluation, while demonstrating improvement, could be further enhanced by considering a wider range of attack types and severities. For example, evaluating the method's performance against adaptive attacks or attacks with varying perturbation budgets would provide a more comprehensive understanding of its generalization capabilities. Furthermore, the paper could benefit from a discussion on the limitations of the proposed approach in the context of highly adaptive or sophisticated attacks.
3. It is better to clarify which module is frozen and noted in Figure 2. The current description of the model architecture and the test-time optimization process lacks clarity regarding which components are updated and which are kept fixed. Specifically, it is unclear whether the feature extractor, classifier, or auxiliary task network are frozen during the max-min entropy optimization. This lack of clarity makes it difficult to fully understand the proposed method and its implementation details.

### Questions
1. Is the code of the proposed REAL approach available? This is also important to improve the impact on the open-source community.  
2. In Fig.2, are the C and E frozen during test-time max-min optimization? 
3. In Eq. 3b and 4b, what is "S" ? which is not defined. I guess this is a typo error, which may be "C".

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
