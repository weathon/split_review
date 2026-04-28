# Activation Gradient based Poisoned Sample Detection Against Backdoor Attacks

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
This work studies the task of poisoned sample detection for defending against data poisoning based backdoor attacks. Its core challenge is finding a generalizable and discriminative metric to distinguish between clean and various types of poisoned samples (\eg various triggers, various poisoning ratios). Inspired by a common phenomenon in backdoor attacks that the backdoored model tend to map significantly different poisoned and clean samples within the target class to similar activation areas, we introduce a novel perspective of the circular distribution of the gradients \wrt sample activation, dubbed \textit{gradient circular distribution} (GCD). And, we find two interesting observations based on GCD. One is that the GCD of samples in the target class is much more dispersed than that in the clean class. The other is that in the GCD of target class, poisoned and clean samples are clearly separated. Inspired by above two observations, we develop an innovative three-stage poisoned sample detection approach, called \textit{Activation Gradient based Poisoned sample Detection (AGPD)}. First, we calculate GCDs of all classes from the model trained on the untrustworthy dataset. Then, we identify the target class(es) based on the difference on GCD dispersion between target and clean classes. Last, we filter out poisoned samples within the identified target class(es) based on the clear separation between poisoned and clean samples. Extensive experiments under various settings of backdoor attacks demonstrate the superior detection performance of the proposed method to existing poisoned detection approaches according to sample activation-based metrics.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present an approach for backdoor sample detection based on the angle of the activation gradients between samples and a reference clean sample for each class.
The paper observes that, within the target class, the activation gradient angles exhibit greater dispersion compared to samples from the clean class. Furthermore, the distribution of angles of backdoor and clean samples within the target class are somewhat distinct, providing a basis for differentiating between clean and poisoned samples.

Building on this observation, the authors introduce the concept of the Gradient Circular Distribution (GCD), a distribution of angles between the activation gradient of samples and that of a reference sample. They propose two key metrics based on this distribution:
CVBT: A metric designed to measure the dispersion of the GCD.
Sample Closeness: A metric that evaluates how close a given sample is to  reference clean sample.

These metrics are then utilized to develop a filtering algorithm, which first identifies the target class and subsequently filters out the poisoned samples. The paper validates the proposed method through experiments on a range of backdoor attack scenarios.

### Strengths
1. The paper identifies a previously unexplored phenomenon in backdoor samples, highlighting greater dispersion in activation gradient angles within the target class compared to clean samples.
2. The authors provide extensive experiments on various backdoor attacks across two architectures (PreAct ResNet18 and VGG-18 BN),
3. Some initial analysis on adaptive attacks is presented, though further exploration could strengthen the findings.
4. The writing is clear and well-structured, making the main arguments easy to follow.

### Weaknesses
1. I am giving low scores to soundness due to the reported  low performance of ASSET, AC. The performance in the original paper of ASSET is close to 90% for all attacks. Additionally, 0 F1 scores for AC also does not look right. For example, in the aforementioned paper, the average TPR of AC is around 50%. 

2.  Please provide sensitivity of various thresholds like $\tau_z$ , $w, \beta$ (Stage 3). What is the rationale behind the choice of $\tau_z$ ? 

3.  Please comment on or provide results for these additonal adaptive attacks: 
a. Can an adversary add  perturbations to the clean samples (different perturbations to different samples) such that their dispersion increases ? 
b. Given a clean set with 100 images, the adversary adds the same noise to 50 images and keeps the other images the same. Will the  dispersion increases of clean sample increase ? 
c. The backdoor trigger is optimized such that the dispersion of the target class decreases.

### Questions
1. Can you please elaborate on this : "It is inspired by phenomenon that a backdoored model tends to map both poisoned and clean samples within the target class to similar areas in its activation space" ? - I believe this is true only for self-supervised training, whereas the current paper focuses on supervised training.

2. At which h,w is the activation getting sliced for calculating the activation gradient ? Is it the same for all layers considered ? Why ?

3. Can we simply use the difference in the angles from 0 in the distribution $\rho$ instead of the sample closeness metric ? Why do we need to use it ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose to detect poisoned examples from an activation-gradient circular distribution perspective. The authors draw two novel observations by studying the GCD of poisoned/clean examples, based on which they introduce an algorithm named AGPD to do backdoor example detection.

### Strengths
(1) Understanding the activation gradient of poisoned examples with circular distribution is interesting. The two observations of GCD are novel.

(2) The algorithm shows strong performance within the evaluation setting of this paper.

(3) The paper is overall well written and the logic is easy to follow. The empirical experiments are mostly comprehensive and valid.

### Weaknesses
(1) My main concern about the proposed algorithm is its scalability. It requires training on the entire dataset to determine the detection state, which might be too expensive given web-scale data and the extreme probability of the data being poisoned. Also, while the authors claim the GCD computation is $O(N)$, the process of calculating the angles between all pairs of activation gradients still appears to have a quadratic component, making it infeasible for large datasets. The repeated computation of these angles for every sample against all other samples will dominate the runtime, even if the individual angle calculation is linear.

(2) The defense algorithm appears to be highly correlated with the specific class labels, potentially limiting its applicability. In the real world, the attackers can adopt a different set of labels than the defenders. The attackers could label the dataset more fine-grained/coarse-grained than the defender. (e.g. Imagine there is a dataset consisting of snacks and drinks and the target class of the attacker is Coca-Cola. However, the defenders just want to classify the images as soft drinks no matter whether it is Coca-Cola or Pepsi. Or the reverse situation can also happen.) Will the observations about GCD hold under such misalignment?

(3) Table 7 is not organized well, please have a double-check.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

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
The paper presents a new approach to identifying poisoned samples in datasets used for deep neural network training. The core proposal, termed Activation Gradient-Based Poisoned Sample Detection (AGPD), leverages a novel metric called Gradient Circular Distribution (GCD) to detect discrepancies between clean and poisoned samples. Key insights include observing that in backdoor attacks, models often map poisoned samples and clean samples to similar activation regions, which AGPD detects by analyzing gradient direction distributions. This method involves three main steps: calculating GCD for each class, identifying target classes based on dispersion, and filtering out poisoned samples.

### Strengths
(1) Introducing GCD as a novel measure adds a unique, technical depth to the approach, potentially applicable to various attack scenarios.

(2)  AGPD shows high detection performance with minimal additional clean data, a notable advantage for real-world applicability, where such data may be limited.

### Weaknesses
 (1) The proposed method is founded on two core observations: (i) the Gradient Circular Distribution (GCD) of the target class exhibits greater dispersion than those of clean classes, and (ii) poisoned and clean samples are distinguishable by their clear clustering in separate regions. However, it remains unclear whether these observations hold consistently for clean-label attacks, where the mapping directions of poisoned and benign samples could exhibit higher similarity given their similar input-space characteristics. Further discussion on this aspect would strengthen the paper’s analysis.

(2) The choice of baseline methods appears limited to older techniques. A broader comparison with more recent, state-of-the-art defense methods would provide a more thorough assessment of the proposed method’s performance relative to the latest advances in poisoned sample detection.

(3) Attack Success Rate (ASR) is a key metric commonly used in backdoor detection evaluations. Its omission from Table 1 raises questions about the comprehensiveness of the evaluation metrics chosen. Including ASR would provide a clearer view of the method's efficacy against backdoor attacks.

(4)   In the main evaluation, a poisoning ratio of 10% is used for non-clean label attacks and 5% for clean-label attacks. Since clean-label attacks are generally more challenging, lower poisoning ratios are typically applied to non-clean label attacks in real-world scenarios. This discrepancy between the paper’s experimental setup and actual attack contexts calls for further clarification. Additionally, practical attack scenarios often employ very low poisoning ratios (1% or 0.5%), feature separability-based defenses tend to be less effective in this setting. More discussion should be included.

### Questions
(1) The proposed method is founded on two core observations: (i) the Gradient Circular Distribution (GCD) of the target class exhibits greater dispersion than those of clean classes, and (ii) poisoned and clean samples are distinguishable by their clear clustering in separate regions. However, it remains unclear whether these observations hold consistently for clean-label attacks, where the mapping directions of poisoned and benign samples could exhibit higher similarity given their similar input-space characteristics. Further discussion on this aspect would strengthen the paper’s analysis.

(2) The choice of baseline methods appears limited to older techniques. A broader comparison with more recent, state-of-the-art defense methods would provide a more thorough assessment of the proposed method’s performance relative to the latest advances in poisoned sample detection.

(3) Attack Success Rate (ASR) is a key metric commonly used in backdoor detection evaluations. Its omission from Table 1 raises questions about the comprehensiveness of the evaluation metrics chosen. Including ASR would provide a clearer view of the method's efficacy against backdoor attacks.

(4)   In the main evaluation, a poisoning ratio of 10% is used for non-clean label attacks and 5% for clean-label attacks. Since clean-label attacks are generally more challenging, lower poisoning ratios are typically applied to non-clean label attacks in real-world scenarios. This discrepancy between the paper’s experimental setup and actual attack contexts calls for further clarification. Additionally, practical attack scenarios often employ very low poisoning ratios (1% or 0.5%), feature separability-based defenses tend to be less effective in this setting. More discussion should be included.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
With the inspiration that a backdoored model is apt to map significantly different poisoned samples and clean samples of the backdoor target to similar activation areas, this paper introduces a novel measurement, i.e., the circular distribution of the gradients w.r.t sample activation, namely GCD, which works to identify the target class of the backdoor and consequently separate poisoned and clean samples within the target class. Accordingly, this paper proposes a sample detection approach called AGPD to achieve dataset purification. Extensive experiments show AGPD's advanced performance in detecting and isolating poisoned samples.

### Strengths
- This paper proposes a novel measurement to show the dispersion of poisoned and clean samples in the model's activations

- This paper is well-written and enforces a high readability with variant and helpful illustrations 

- This paper comprehensively evaluates AGPD's performance by considering diverse poisoning attacks, comparing with different related defenses, and conducting experiments on variant datasets.

- This paper considers the ablation study on different hyper-settings of APGD and involves two reasonable adaptive attacks that have considered APGD's defense w.r.t the GCD distribution.

### Weaknesses
(1) The use of $arccos(\cdot)$ in Eq.(2) is ambigious as $cos(\cdot)$ is used in Eq.(3) and Eq.(4) as well. It is unclear if the angular representation provides any benefit beyond the cosine similarity, especially given the direct use of cosine similarity in subsequent calculations. The paper should clarify the motivation behind using the $arccos$ transformation, and whether it introduces any numerical instability or computational overhead.

(2) The calculation of GCD across all model layers is not clearly formulated for each sample. It is unclear how the channel-wise gradients $g^{(l)}$ from different layers are aggregated or combined to produce a single GCD value for each input sample. The paper needs to specify the exact procedure for combining these layer-specific gradients into a single, representative GCD, including any weighting or normalization steps.

(3) The influence of the clean sample by random sampling for the basic sample pair is not studied. The selection of the clean sample $x_0$ appears arbitrary, and the paper does not explore how different choices of $x_0$ affect the calculated GCD and the subsequent detection performance. A sensitivity analysis is needed to determine the robustness of the method to the choice of the clean sample.

(4) There is lacking the rationale for setting the hyper-parameter $\tau_z = e^2$. The paper provides no justification for this specific value, and it is unclear how this choice impacts the detection performance. A more detailed explanation, possibly including an empirical analysis of different values, is needed to justify this hyperparameter selection.

(5) For all-to-all attacks, a better explanation of how the dataset separation by APGD is achieved is required. The paper does not clearly explain how APGD distinguishes between different target classes in an all-to-all attack scenario, where multiple classes are simultaneously targeted. The mechanism for separating these classes and identifying poisoned samples within each target class requires further elaboration.

(6) The description of Adpative-Blend in Appendix B is incomplete and different from the default attack setting. The paper needs to clarify the exact differences between the Adaptive-Blend attack implementation in the appendix and the default attack settings used in the main experiments, especially regarding the poisoning ratio and the number of noisy samples added. This discrepancy raises concerns about the consistency of the experimental setup.

(7) It is unclear how the noisy and poisoned samples are separated against WaNet and Adaptive-Blend attacks. Given that these attacks incorporate noisy samples to enhance stealthiness, the paper should provide a detailed analysis of how APGD distinguishes between noisy samples and actual poisoned samples, and whether the noisy samples are misclassified as poisoned samples.

### Questions
Q-(1): The calculation of $\rho_{x_0}\(\mathcal{D}\)$ in Eq.(3) and $s_{x_0}\(x_i\)$ in Eq.(4) basically transforms e.g. $\theta_{x_0}\(x_i\)$ back to $\frac{g\(x_i\) \cdot g\(x_0\)}{||g\(x_i\)|| ||g\(x_0\)||}$. By simplifying the formulation in Eq.(3) and Eq.(4), does this mean it is essentially calculating the cosine similarity of the gradients between the basis pair and each input sample? If this is indeed the case, is the calculation of radian in Eq.(2) useful merely for the visualization in figures like Figure 1.?

Q-(2): In section 3, the channel-wise activation gradient $g^{\(l\)}$ is first introduced in Eq.(1). However, the formulating w.r.t the index of the model layer is missing in the consequent methodology description. Can the authors elaborate on how the channel-wise gradients in each layer are merged into the final GCD of an input sample $x_i$?

Q-(3): The basis pair is crucial to disperse samples; thus, a small clean set is necessary for APGD detection. As even a single clean sample per class has been proven effective, how does the selection of clean samples influence APGD's performance? Or is APGD resistant to any random sampling of clean samples?

Q-(4): Different from the study on the threshold $\tau_s$ in section 5.4, $\tau_z$ remains equal $e^2$. What is the rationale of setting $\tau_z = e^2$? 

Q-(5): In Figure 4, APGD detection on the target class works better against all-to-one attacks than all-to-all attacks. While detecting poisoned samples of all-to-all attacks, does APGD handle the separation of all-to-all attacks class by class via the implementation of Stage 3?

Q-(6): In the default setting of Adaptive-Blend, the poisoning ratio is relatively low (poisoned/total = 150/50000 = 0.3% for CIFAR10), where the same amount of noisy samples as poisoned samples are added by setting the conservatism ratio = 1.0, which is unfortunately missing in Table 7. Moreover, considering the default poisoning ratio = 5%, the ASR of 66.17% for Apat-Blend is much lower than that of the original paper. Does this imply that the Adptive-Blend in this paper has some biases from the default attack configuration?

Q-(7): Considering that both WaNet and Adaptive-Blend attacks involve noisy samples to improve the attack stealthiness, can the authors provide some visualization on the separation of APGD between the poisoned samples and noisy samples in both attacks?

### Soundness
3

### Presentation
3

### Contribution
3
