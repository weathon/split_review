# Test-Time Adversarial Defense with Opposite Adversarial Path and high Attack time cost

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
Deep learning models are known to be vulnerable to adversarial attacks by injecting sophisticated designed perturbations to input data. Training-time defenses still exhibit a significant performance gap between natural accuracy and robust accuracy. In this paper, we investigate a new test-time adversarial defense method via diffusion-based recovery along opposite adversarial paths (OAPs). We present a purifier that can be plugged into a pre-trained model to resist adversarial attacks. Different from prior arts, the key idea is excessive denoising or purification by integrating the opposite adversarial direction with reverse diffusion to push the input image further toward the opposite adversarial direction. For the first time, we also exemplify the pitfall of conducting AutoAttack (Rand) for diffusion-based defense methods. Through the lens of time complexity, we examine the trade-off between the effectiveness of adaptive attack and its computation complexity against our defense. Experimental evaluation along with time cost analysis verifies the effectiveness of the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a test-time adversarial defense method that utilizes diffusion-based purification along Opposite Adversarial Paths to excessively denoise adversarial inputs, pushing them away from decision boundaries. The proposed plug-and-play purifier can be integrated into pre-trained models, improving their robustness against adversarial attacks.

### Strengths
1. The proposed plug-and-play purifier can be integrated into pre-trained models, improving their robustness against adversarial attacks. 
2. The method increases the time required for attackers to generate adaptive adversarial examples. 
3. The paper also critiques the use of AutoAttack (Rand) for evaluating diffusion-based defenses and highlights the trade-off between attack effectiveness and computational complexity in adversarial robustness evaluations.

### Weaknesses
1.  The author's explanation of his method is not clear enough. There is no overall algorithm description (e.g. for section 3.3), making the reader difficult to follow. 
2.  The explanation in Table 2 is not persuasive. Why with the increase of K, the robustness decreases?   It seems that this is contrary to the assumption in Figure 1.  Could you provide a more detailed explanation of this apparent contradiction and discuss potential reasons for the decrease in robustness as K increases? 
3.  The algorithm is too complex to be applicable. For example, it uses several diffusion paths. From Table 6, it seems that the purification time will be doubled.  Could you discuss the trade-offs between complexity and performance? Are there ways to simplify the algorithm while maintaining its effectiveness? Additionally, it would be helpful to provide a more detailed analysis of the computational costs and how they scale with the number of diffusion paths.
4. The improvements are little compared with DiffPure regards the transferability. Moreover, this paper did not compare with the latest work, such as
[1] Robust Evaluation of Diffusion-Based Adversarial Purification,ICCV2023
[2] Adversarial Purification with the Manifold Hypothesis,AAAI2024
5.  References should be enclosed in parentheses. For example, it should be In DiffPure (Nie et al. 2022) rather than In DiffPure Nie et al. (2022).
6. Some typos. For example, in Figure 2, it should be Sec 3.xx.

### Questions
1. What is the aim of Color OT?
2. Why does the robustness decrease with the increase of K in Table 2?  
3. How does the number of diffusion paths influence the purification time?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a preprocessing-based test time defense against adversarial attacks. The proposed method relies on the minimization of training loss and adversarial purification using the diffusion model. The adversarial inputs are pushed towards the opposite adversarial direction via the reverse diffusion process. The proposed purifier can be plugged into a pre-train model, which means the proposed method is easily combined with different types of defenses, such as adversarial training.

### Strengths
- The idea of reducing the effects of adversarial perturbations by perturbing the input in a way that minimizes training loss makes sense. This process pushes the adversarial input to non-adversarial area. This idea cannot be applied directly because because the ground truth label is not available during inference. The proposed method is able to emulate this process through an inverse diffusion process and achieve efficient denoising.
- The effectiveness of the proposed method is empirically demonstrated by the experimental results. It also shows superior results compared to existing methods against the strong attacks such as EOT and BPDA , which are designed to defeat randomized defenses.

### Weaknesses
 - To demonstrate that the proposed method is effective against various attacks, it would be better to experiment with methods that converge to adversarial examples that differ from PGD and APGD, such as ACG and PGD-ODI. This is because PGD-based attacks highly depend on the initial point of the attack. 
The effectiveness of random initialization, such as Output Diversified Sampling (ODS) in adversarial attacks, implies the high dependency of PGD-based attacks on initial points. It is natural to assume the same dependency in the minimization of training loss with respect to input because PGD-based attacks maximize the same loss to generate adversarial examples. 
However, the attacks used for training and evaluation of the proposed method are all derivatives of PGD. Thus, the adversarial examples subject to purification are likely to be similar to each other.
- It would be helpful if you could explain the difference between the solid and dashed lines in the arrows in the figures.

### Questions
- Does the proposed method show superior performance against attacks, such as PGD-ODI and ACG,  that converge to different adversarial examples from PGD?
- What do the differences in types and colors of lines mean in the figures?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a test-time adversarial defense method, which exploits the diffusion-based recovery through opposite adversarial paths (OAPs) to enhance robustness against adversarial attacks. This work proposes denoising along the opposite adversarial gradient and incorporating it with reverse diffusion. Experiments on three datasets are conducted to validate the effectiveness of the proposed method.

### Strengths
1. This paper introduces a new method to alleviate the influence of adversarial noise, which proposes to leverage the opposite adversarial path and reverse diffusion.

2. The experiments are performed on three popular datasets, which provides extensive evaluation results.

3. Multiple related works are considered for comparison to present the gains brought by the proposed method.

### Weaknesses
1. The statement in Section 3.1.2 is contradictory to the statement in Section 1.3, and the corresponding explanation is not convincing enough. In Section 1.3, the clean accuracy decreases at K=1, and the authors argue that “the process ‘-adv’ is still unstable, hence, some data points near the decision boundary may be perturbed to incorrect class”, but in Section 3.1.2, the model has better performance at K=1. Although the authors conjecture that this inconsistency is because the ground-truth labels are not used in Table 2, the training data $x^K$ is actually generated step-by-step using the ground-truth label y as well, and why this is not unstable. The authors can clarify the specific differences in methodology or experimental setup between these two terms or provide a more detailed analysis of the stability of the '-adv' process across different values of K.

2. In this work, the proposed method only consider the manner of non-targeted adversarial attacks. For the targeted attacks, the adversarial gradient is varied with the specified target class, and the proposed method with a single opposite adversarial path seems not to be able to handle this case.

3. The adversarial attacks used to evaluate the defenses mainly belong to gradient-based non-targeted methods, the optimization-based adversarial attacks (e.g., C&W, DDN), targeted attacks and black-box attacks can be considered to more comprehensively evaluate the effectiveness of the proposed method.

4. Some details of the experiment are unclear.

5. Some typos, for example, "To this end, according to (14) of guided diffusion described in Sec. 8 in Supplementary" (Line 264) → "To this end, according to Eq.(14) of guided diffusion described in Sec. 8 in Supplementary"

### Questions
1. The statement in Section 3.1.2 is contradictory to the statement in Section 1.3, and the corresponding explanation is not convincing enough. In Section 1.3, the clean accuracy decreases at K=1, and the authors argue that “the process ‘-adv’ is still unstable, hence, some data points near the decision boundary may be perturbed to incorrect class”, but in Section 3.1.2, the model has better performance at K=1.  Although the authors conjecture that this inconsistency is because the ground-truth labels are not used in Table 2, the training data $x^K$ is actually generated step-by-step using the ground-truth label y as well, and why this is not unstable. The authors can clarify the specific differences in methodology or experimental setup between these two terms or provide a more detailed analysis of the stability of the '-adv' process across different values of K

2. Some details of the experiment are unclear. In Tables 1-5, it is not clear whether the adversarial attack is against the target model only or against the target model and purifier as a whole. It seems that the described adaptive attack is against the target model only by using BPDA, EOT, etc., rather than a full white-box attack (e.g., C&W) against the target model and the purifier as a whole. The authors can explicitly state for each experiment whether the adversarial attacks are targeting only the model or both the model and purifier.

### Soundness
2

### Presentation
2

### Contribution
3
