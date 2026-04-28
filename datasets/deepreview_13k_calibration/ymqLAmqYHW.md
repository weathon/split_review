# K&L: Penetrating Backdoor Defense with Key and Locks

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 5, 6, 1

## Abstract
Backdoor attacks in machine learning create hidden vulnerability by manipulating the model behaviour with specific triggers. Such attacks often remain unnoticed as the model operates as expected for normal input. Thus, it is imperative to understand the intricate mechanism of backdoor attacks. To address this challenge, in this work, we introduce three key requirements that a backdoor attack must meet. Moreover, we note that current backdoor attack algorithms, whether employing fixed or input-dependent triggers, exhibit a high binding with model parameters, rendering them easier to defend against. To tackle this issue, we propose the Key-Locks algorithm, which separates the backdoor attack process into embedding locks and employing a key for unlocking. This method enables the adjustment of unlocking levels to counteract diverse defense mechanisms. Extensive experiments are conducted to evaluate the effective of our proposed algorithm. Our code is available at: https://anonymous.4open.science/r/KeyLocks-FD85

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the problem of backdoor attacks and defenses. The authors begin by listing three requirements that a successful backdoor attack should satisfy. Next, they point out the 'high binding' effects and propose a new attack algorithm named Key-Locks to generate backdoor data. Experiments are conducted to evaluate the effectiveness of the proposed algorithm.

### Strengths
- The topic of backdoor attacks and defenses is important.
- The writing in the paper is easy to follow.
- The experimental setups are comprehensive, and the results look good with appropriate replications.

### Weaknesses
I have two major concerns:

1. First, I suspect that there are already previous theoretical results [1, 2] that can explain your proposed "high binding" phenomena and why your method works well. Considering that the literature on backdoors in computer vision is well developed, I think all the points listed in your paper have been somehow mentioned (although in different forms) in previous work; however, there seems to be a lack of discussion on this. Specifically, the paper does not adequately address how the proposed 'Key-Locks' method relates to existing understandings of backdoor triggers and their embedding within the model's parameter space. The concept of 'high binding' needs to be more rigorously defined and differentiated from similar concepts in the literature, such as the 'low-rank' nature of backdoor triggers or the 'subspace' hypothesis of backdoor embedding. It is unclear if the proposed method offers a fundamentally new mechanism or is simply a variation of existing techniques.

2. Second, more defenses are needed. I think your proposed method can potentially be defended against detection-based algorithms (originally designed for OOD detection). I would like to see how your proposed methods perform under the two more recent strong defenses [4, 5]. Specifically, the paper should evaluate the robustness of the proposed attack against defenses that leverage input transformations or spectral analysis to detect backdoors. The current evaluation primarily focuses on model-level defenses, which may not be sufficient to demonstrate the practical threat posed by the proposed attack. Furthermore, the paper needs to consider adaptive defenses, where the defense mechanism is specifically designed to counter the proposed attack strategy.

### Questions
Please check my previous comments.

### Soundness
2

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
5

### Summary
This paper introduces a novel backdoor attack mechanism based on keys and locks. The primary concept is to reduce the high binding of backdoors to model parameters, thereby enhancing robustness against defenses. Extensive experiments demonstrate the effectiveness of this approach, showing its superiority over existing methods.

### Strengths
1. Proposes a novel and effective backdoor attack strategy.

2. Provides in-depth analysis of the backdoor properties contributing to vulnerability against defenses.

3. Includes extensive evaluations across various models, datasets, and ablation studies.

### Weaknesses
1. Insufficient support for design choices and key hypotheses.

2. Potential vulnerability to detection by existing trigger inversion methods.

3. Lack of latest baseline attacks and defenses in the evaluation.

4. Concerns regarding the practicality of the trigger pattern.

5. Some writing issues.

### Questions
This paper introduces an interesting backdoor attack mechanism using keys and locks. The authors highlight that the vulnerability of existing backdoors stems from their strong binding to model parameters, making them susceptible to defenses based on normal model updates. To enhance robustness, the paper proposes a new backdoor attack. The core technique is similar to adversarial attacks, where a keyhole is generated and embedded using gradient descent towards the target class. During inference, a trigger (the key) is generated using a similar algorithm. The paper includes extensive evaluations, comprising various analyses and ablation studies, to demonstrate the effectiveness of the proposed attack, which outperforms existing methods.

However, I have several concerns regarding the design and evaluation:

(1) The attack appears to focus on reducing the class distance between the target class and other classes, as indicated by the poisoning loss in Equations (3) and (4). Without a fixed backdoor generation function, the model learns perturbations from any class towards the target class in each iteration. Once convergence is achieved, generating an effective trigger using a similar function, as described in Equations (5) and (6), becomes straightforward. While this is intriguing, it raises certain issues.

First, the necessity of the poisoning process is questionable. Why not directly generate natural backdoor sample, e.g., [1]? This would simplify the process while maintaining a reasonable ASR.
Second, the corrupted target class might be easily detectable using existing trigger inversion methods, such as [2] and [3], since generating adversarial perturbations to flip the label to the target class becomes easier than for other classes.

(2) The paper lacks sufficient support to validate its hypotheses, particularly those in Lines 211-215. Recent work [4] models backdoor learning as a special case of continual learning, identifying the orthogonal nature between backdoor behaviors and normal classification. There appears to be a connection between this claim and the authors' hypothesis, which should be explored and discussed.

(3) The baseline attacks and defenses used in the paper are not actually up-to-date. For instance, state-of-the-art attacks such as [5,6,7,8] demonstrate robustness against various defense methods. It is important to clarify how the proposed attack differs from these approaches. Additionally, FST [9], a latest defense effective against a wide range of attacks, should be included in the comparison.

(4) The triggers illustrated in Figures 19-30 appear misaligned with the original images, even if the L-2 distance metrics are favorable. These measurements may not align with human perception. Moreover, adversarial perturbations might be challenging to implement practically, requiring careful tuning of pixel values. They may also be vulnerable to input purification techniques, such as those used in [10], where diffusion models are leveraged to reconstruct inputs and reduce trigger effectiveness. It is suggested to provide a discussion about this issue.

(5) The paper's structure could be improved. Several important details are relegated to the appendix without proper referencing in the main text. For example, Line 237 mentions Algorithm 1 without a clear link and description to it. Properly integrating and referencing content from the appendix would enhance the paper's clarity and flow.

--------------------------
Reference:

[1] Tao, Guanhong, et al. "Backdoor vulnerabilities in normally trained deep learning models." arXiv preprint 2022.

[2] Wang, Bolun, et al. "Neural cleanse: Identifying and mitigating backdoor attacks in neural networks." IEEE S&P 2019.

[3] Wang, Zhenting, et al. "Unicorn: A unified backdoor trigger inversion framework." ICLR 2023.

[4] Zhang, Kaiyuan, et al. "Exploring the Orthogonality and Linearity of Backdoor Attacks." IEEE S&P 2024.

[5] Zeng, Yi, et al. "Narcissus: A practical clean-label backdoor attack with limited information." CCS 2023.

[6] Qi, Xiangyu, et al. "Revisiting the assumption of latent separability for backdoor defenses." ICLR 2023.

[7] Cheng, Siyuan, et al. "Lotus: Evasive and resilient backdoor attacks through sub-partitioning." CVPR 2024.

[8] Huynh, Tran, et al. "COMBAT: Alternated Training for Effective Clean-Label Backdoor Attacks." AAAI 2024.

[9] Min, Rui, et al. "Towards stable backdoor purification through feature shift tuning." NeurIPS 2024.

[10] Shi, Yucheng, et al. "Black-box backdoor defense via zero-shot image purification." NeurIPS 2023.

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
The paper introduces the Key-Locks (K&L) backdoor attack algorithm, designed to bypass existing defenses. Unlike traditional backdoor attacks that show high binding with model parameters, making them vulnerable to defenses, the K&L algorithm decouples the backdoor process from model parameters. This decoupling allows the method to adjust the unlocking levels of backdoor activation, enhancing its robustness against a diverse set of defenses. The paper also introduces the Accuracy-ASR Curve (AAC) as a new metric for evaluating backdoor attacks.

### Strengths
+ Analysis of the concept of high binding between backdoor triggers and model parameters.
+ Extensive experiments using various datasets and neural network architectures.

### Weaknesses
 - First of all, the paper requires improvements in editorial quality. There are instances where terms more characteristic of language models are used, such as "assaults" instead of the more appropriate "attacks." A thorough human proofreading is recommended to ensure precise usage of terminologies and enhance overall clarity. In addition, the paper excessively relies on the appendix, making it difficult to follow without constant cross-referencing.

- In Algorithm 1 for embedding locks, the backdoor samples are iteratively modified at each training epoch, where the learning rate $\eta$ is added or subtracted to the backdoor inputs based on the gradient's sign in the direction of the backdoor target. Unlike the inference stage, clipping is not applied during training. This lack of clipping over multiple iterations could result in less stealthy and significantly perturbed images. Such perturbations may potentially lead to distinguishable loss patterns compared to benign inputs. Such characteristics could be susceptible to in-training defenses, such as Anti-Backdoor Learning, which, notably, has not been considered in the evaluation.

- The paper attempts to distinguish K&L from adversarial attacks in Section 3.4. The K&L algorithm generates adversarial perturbations similar to the FGSM method using gradient signs and incorporates these examples during training. The claim is that this approach reduces the binding between the backdoor trigger and model parameters. However, as K&L uses adversarial perturbations as backdoor triggers, this approach shares similarities with adversarial training, which enhances the robustness of models against adversarial attacks. A more precise explanation would help to understand why this method reduces robustness to adversarial perturbation instead of improving it.

- The paper does not fully discuss the rationale behind introducing the new metric, the Accuracy-ASR Curve (AAC), alongside existing backdoor evaluation metrics. It would be beneficial to elaborate on AAC's added value to backdoor attack evaluations. Additionally, the meanings of AAC1, AAC3, and AAC5 are not clear without a proper definition of AAC, making it difficult to understand their relevance in the evaluation. Also, the definition of AAV is not sufficiently explained.

- The backdoor sample similarity rates presented in Table 2 could be potentially misleading, given that they are based on only two input examples, as illustrated in Figure 2. To ensure a robust and reliable evaluation, it would be more appropriate to compute the similarity attribution using multiple images across multiple runs to achieve statistical significance.

- All the results presented in the paper must be evaluated across multiple runs to ensure the statistical significance of the reported values.

### Questions
1. Why was clipping excluded during training? Has the potential impact of significant perturbations during the embedding locks of K&L been evaluated against in-training defenses such as Anti-Backdoor Learning?
2. Could you clarify how K&L differs from adversarial training?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes an adaptive attack designed to bypass existing backdoor defenses. However, the paper is underprepared, and several concepts are not well explained.

### Strengths
Large set of experiments: The authors re-implement eight defense methods and six attack backdoors across four datasets. Through these experiments, they demonstrate that the proposed approach can outperform the six existing attacks in bypassing defenses.

### Weaknesses
1.  Presentation needs improvement: Key concepts such as "high binding," "key," and "lock" are not explained clearly. For instance, what does "high binding" represent? On line 75, the authors state that it refers to the tight coupling between a backdoor and a specific trigger. However, on line 181, it appears to mean something different, namely, the binding between the backdoor and model parameters. The lack of a consistent definition makes it difficult to understand the core mechanism of the proposed attack and how it differs from existing methods.
2.  Unclear limitations of existing backdoor attacks: It is not clear why current defenses are successful against these attacks. Since "high binding" is ambiguous, it is difficult to understand why existing attacks fail. Additionally, according to Table 1, some existing attacks can also bypass these defenses. The authors should clarify why attacks sometimes succeed and other times fail in bypassing defenses. The paper needs to provide a more detailed analysis of the specific vulnerabilities exploited by different attacks and how defenses counteract them, rather than relying on a vague notion of "high binding."
3.  Distinction from adversarial examples: In the KL backdoor attack, the poisoned test sample is generated via gradient descent, similar to adversarial examples. The authors should explain how their approach differs from adversarial examples. Moreover, I suggest that the authors conduct further experiments to distinguish the effects of backdoor attacks from those of adversarial examples. For example, when the poisoning ratio is zero, they could apply the KL attack during testing to check the ASR (Attack Success Rate). If the ASR is not too low, this would suggest that adversarial examples, rather than backdoor attacks (which rely on poisoning training data), are the primary factor leading to successful backdoor injection. The current experimental setup does not sufficiently isolate the backdoor effect from the influence of adversarial perturbations.
4.  Summary of backdoor attack requirements: Summarizing the three requirements for a backdoor attack should not be considered a primary contribution, as many other papers have already discussed this. This section lacks novelty and does not provide a significant advancement in the field.

### Questions
NA

### Soundness
1

### Presentation
1

### Contribution
1
