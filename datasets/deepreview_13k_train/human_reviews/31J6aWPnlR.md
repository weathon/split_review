# Which Network is Trojaned? Increasing Trojan Evasiveness for Model-Level Detectors

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
Trojan attacks can pose serious risks by injecting deep neural networks with hidden, adversarial functionality. Recent methods for detecting whether a model is trojaned appear highly successful. However, a concerning and relatively unexplored possibility is that trojaned networks could be made harder to detect. To better understand the scope of this risk, we develop a general method for making trojans more evasive based on several novel techniques and observations. In experiments, we find that our evasive trojans reduce the efficacy of a wide range of detectors across numerous evaluation settings while maintaining high attack success rates. Surprisingly, we also find that our evasive trojans are substantially harder to reverse-engineer despite not being explicitly designed with this attribute in mind. These findings underscore the importance of developing more robust monitoring mechanisms for hidden functionality and clarifying the offense-defense balance of trojan detection.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a method to increase the evasiveness of backdoor attacks in neural networks, making these compromised models much harder to detect with standard defenses. Using a distribution-matching loss and additional specificity and randomization losses, the approach crafts trojaned networks that closely resemble clean ones, significantly lowering detection success. Interestingly, the enhanced evasiveness also hinders reverse-engineering efforts, making it challenging to identify attack targets or triggers. These findings underscore the urgent need for more advanced detection and reverse-engineering methods in light of evolving backdoor threats.

### Strengths
+ Simplicity and Effectiveness: The proposed method is straightforward yet effectively increases the evasiveness of backdoor attacks, making detection by conventional methods significantly more challenging without overly complicating the attack strategy.

### Weaknesses
- Outdated References: The paper's references are somewhat outdated, particularly given the rapid advancements in the field of backdoor detection and defenses. More recent studies would provide a fairer and more comprehensive baseline for comparison.

- Lack of Clarity on Model Distribution: The paper reports using over 6,000 models, but it does not clearly explain how these models are structured, distributed, or how they vary. This lack of clarity makes it difficult to assess the robustness and representativeness of the findings.

- Limited Statistical Insights: Despite the high number of models trained, the results are presented as single values rather than as mean ± standard deviation, which would better reflect the consistency and generalizability of the method across the large sample size.

- Narrow Scope of Backdoor Types: The method is tested primarily on standard backdoor attacks, without exploring its applicability to more complex backdoors, such as frequency-based or invisible backdoors, which limits the generalizability of the findings.

- Simplistic Model Architectures and Datasets: The experiments focus on simpler models and datasets, leaving it unclear how well the method performs with complex architectures, like deep networks or Vision Transformers, and on more challenging datasets or tasks, such as CelebA or face recognition.

- Outdated Baseline Detectors: The baseline detectors used in the study are not the most recent in the field. Incorporating newer techniques like Unicorn, Rethinking Reverse-Engineering, and Symmetric Feature Differencing would strengthen the paper’s contribution and provide a more rigorous evaluation.

### Questions
1. Literature Update: The field of backdoor attacks is evolving rapidly, yet the most recent baseline references and comparisons in this paper are two years old. Incorporating more recent research would ensure fairer and more rigorous comparisons, thus enhancing the study’s relevance and comprehensiveness.

2. Clarification of Model Counts: The paper mentions training over 6,000 models, but the distribution and structure of these models are not clearly explained. Questions arise about whether the models are homogeneous in architecture and backdoor methodology. The sheer volume of models used would be more insightful if accompanied by concrete conclusions or comparative insights about the models' effectiveness and evasiveness.

3. Statistical Reporting: Given the large number of models tested, it would be beneficial to report the results as mean ± standard deviation rather than as single values. This would provide additional insight into the method’s consistency and generalization.

4. Generalizability Across Backdoor Types: It remains unclear whether the proposed method is effective against other types of backdoor attacks, such as frequency-based or invisible backdoors. Expanding the study to cover these variations would increase the paper’s contribution to the field.

5. Complexity of Models and Datasets: The paper primarily tests on relatively simple models and datasets. Evaluating the method’s performance on more sophisticated architectures (e.g., very deep networks, Vision Transformers) and more complex datasets (e.g., CelebA or face recognition tasks) could further strengthen its impact.

6. Baseline Detector Relevance: The baseline detectors used are somewhat outdated. Including recent works such as Unicorn, Rethinking Reverse-Engineering, and Symmetric Feature Differencing would improve the rigor and relevance of the evaluation. Suggested references include:

[refA] Wang, Zhenting, et al. "Unicorn: A unified backdoor trigger inversion framework." ICLR (2023).

[refB] Wang, Zhenting, et al. "Rethinking the reverse-engineering of trojan triggers." Advances in Neural Information Processing Systems 35 (2022): 9738-9753.

[refC] Liu, Yingqi, et al. "Complex backdoor detection by symmetric feature differencing." CVPR (2022).

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
2

### Summary
This paper proposes a new evasive Trojan attack method. The attack is motivated by the distribution matching loss inspired by the Wasserstein distance along with specificity and randomization losses. The paper evaluates the new attack over 6, 000 trojaned neural networks and find that their evasive trojans considerably reduce the performance of a wide range of detection methods.

### Strengths
- The paper is easy to follow.
- Detailed experiments
- Open source

### Weaknesses
- The main idea (use Wasserstein distance) is not new
- Lack of some comparison and ablation study

Detailed comments below:

- The core idea of using Wasserstein distance for evasive trojan generation is not new. It would be better if this paper could be compared in detail with existing similar work.
- The paper could include comparisons with more recent evasive trojan methods, particularly those discussed in Section-2-RelatedWork-Evasive attacks. Although the paper compares the method with TaCT, it is not the most advanced Trojan attacks. Comparing and adapting more advanced evasive attacks will be appreciated.
- While the paper focus on model-level trojan detection, evaluating the performance against other types of trojan detection methods would be helpful.
- Lack of some ablation studies, e.g., poison rate.

### Questions
See weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a backdoor attack designed to enhance evasiveness against
detection methods for backdoored models. This increased evasiveness is achieved
by incorporating evasiveness loss into the backdoor planting process.
Experiments on MNIST, CIFAR-10, CIFAR-100, and GTSRB datasets demonstrate the
effectiveness of the proposed method.

### Strengths
1. The studied problem is interesting.

2. The proposed evasive trojan is harder to be detected than standard trojan.

3. This paper is well-written.

### Weaknesses
1. The novelty of this paper might be somewhat limited. For the Distribution
Matching module, several existing works, such as LIRA [1] and AdaptiveBlend [2],
already propose approaches sharing similar spirits. The specificity loss design
may also with limited novelty, as similar ideas have been explored in WaNet [3]
and Input-Aware Attack [4].

2. The defense methods used in this paper might be somewhat outdated.
Incorporating more advanced defenses [5,6] is suggested.

3. The experiments are conducted on small datasets with low-resolution images
(32x32), leaving the generalizability to larger datasets and higher image
resolutions (e.g., ImageNet) uncertain.


[1] Doan et al., LIRA: Learnable, Imperceptible and Robust Backdoor Attacks. ICCV 2021.

[2] Qi et al., Revisiting the Assumption of Latent Separability for Backdoor Defenses. ICLR 2023.

[3] Anh et al., WaNet -- Imperceptible Warping-based Backdoor Attack. ICLR 2021.

[4] Tuan et al., Input-Aware Dynamic Backdoor Attack. NeurIPS 2020.

[5] Huang et al., Distilling Cognitive Backdoor Patterns within an Image. ICLR 2023.

[6] Xu et al., Towards Reliable and Efficient Backdoor Trigger Inversion via Decoupling Benign Features. ICLR 2024.

### Questions
please refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new type of trojan attack for deep neural networks to increase the evasiveness of trojans against model-level detectors. The main idea of achieving this is to design a special loss which contains not only the task loss, but also two others that reflect the loss trojan loss to increase attack success rate and evasion loss to make the trojan harder to detect. The evasion loss contains three components, including distribution matching, specificity, and randomization. The experiments show that the proposed method can significantly increase the attack success rate and make the trojan harder to detect.

### Strengths
The paper is easy to follow and works on important problems in the field of adversarial machine learning.

### Weaknesses
The paper seems to be out-dated, not following recent advances in the field of adversarial machine learning. The designed loss function, in particular the evasion loss, is not very novel. There has been work on very similar ideas in the past, e.g., Gradient Shaping (NDSS'23) on distribution matching with both theoretical and empirical results. The idea of smoothing, normalization, and randomization is also not new. 

The experiments are not comprehensive enough to show the effectiveness of the proposed method. The used datasets are rather small, and the generalization of the proposed method to other datasets is not clear.

### Questions
Could you justfiy your novelty and experimental setup?

### Soundness
3

### Presentation
3

### Contribution
2
