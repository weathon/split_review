# Leveraging characteristics of the output distribution for identifying adversarial audio examples

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Adversarial attacks can mislead automatic speech recognition (ASR) systems into producing an arbitrary desired output. 
This is easily achieved by adding imperceptible noise to the audio signal, thus posing a clear security threat. 
To prevent such attacks, we propose a simple but efficient adversarial example detection strategy applicable to any ASR system that predicts a probability distribution over output tokens in each time step. 
We measure a set of characteristics of this distribution: the median, maximum, and minimum over the output probabilities, the entropy of the distribution, as well as the Kullback-Leibler and the Jensen-Shannon divergence with respect to the distributions of the subsequent time step. 
Then, by leveraging the characteristics observed for both benign and adversarial data, we apply binary classifiers, including simple threshold-based classification, ensembles of these simple classifiers, and neural networks.
In an extensive analysis of different state-of-the-art ASR systems and language data sets, we demonstrate the supreme performance of this approach, receiving a mean area under the receiving operator characteristic (AUROC) for distinguishing adversarial examples against clean and noisy data higher than 99\% and 98\%, respectively.
To assess the robustness of our method, we propose adaptive attacks that are constructed with an awareness of the defense mechanism in place. This results in a decrease in the AUROC, but at the same time, the adversarial clips become noisier, which makes them easier to detect through filtering and creates another avenue for preserving the system's robustness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method to detect adversarial audio example by exploiting statistical features. Based on the selected features, accurate predictions can be made to differentiate adversarial audio examples and standard audio samples. An adaptive attack against proposed detection methods is also introduced, even though less effective against adversarial examples, the authors claim that the noise level of the adaptive attack is higher and the adaptive adversarial audio examples can be easily picked by the human ear.

### Strengths
The paper is very well presented and easy to follow. Extensive experimental results are provided to support the claims. The results demonstrate that the proposed detection is more generally more accurate than the existing TD detection method. Results on adaptive attacks also show that if an adaptive adversarial audio example targets the proposed detection, more audible noises will be included in the adversarial example.

### Weaknesses
 - The reason behind the selected statistics can be further motivated. Why are these statistical features selected? A related question is why the generated adaptive adversarial audio examples are noisier when optimizing with respect to relevant feature?
- Regarding the generalization of the proposed detection, the transferability of the detection can be further clarified. About intra-model generalization, will the detection model that is trained on one specific kind of adversarial example be generalizable to other types of adversarial examples? This point needs to be clarified since it may weaken the threat model that the detector needs to know the type of the adversarial attack beforehand. About inter-model generalization, will a detector trained on one ASR model be able to detect adversarial examples that are generated on a different ASR model? It would be great if the authors can clarify the generalization of the proposed method.
- About the adaptive attack, have the authors considered other types of attacks that may decrease the noise level of the adversarial audio examples?  I really appreciate that the authors provide experiments on adaptive attacks, which definitely makes the claims stronger. It would be great if the authors could clarify the specific efforts that have been made to control the noise level.

### Questions
See questions in the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the significant issue of adversarial attacks on automatic speech recognition (ASR) systems, a relevant topic in the field of machine learning and security.  The approach is based on analyzing the probability distribution over output tokens at each time step. This involves examining statistical measures like median, maximum, minimum, entropy, and divergence (KL and JSD). Moreover, the authors claims that their detector is resilience when it comes to dealing with noisy data, meaning they can still effectively detect adversarial attempts even when the audio quality is compromised by noise.

### Strengths
- The paper introduces a novel approach to identify adversarial attacks by using statistical characteristics of the output token distributions. 

- It has been demonstrated that specific statistical measures, like the mean of the median of probabilities, have an acceptable discriminative capabilities. This implies that the authors have done rigorous empirical analysis to identify which features are most effective.

- The authors mention empirical findings, which suggests that they have tested their approaches on real-world data or experiments, providing evidence for their claims.

### Weaknesses
 - The proposed defense method relies on statistical features like the mean, median, maximum and minimum extracted from the output token probability distributions over time. While these aggregated metrics can efficiently summarize certain characteristics of the distributions, they may miss more subtle adversarial manipulations. For example, an attack could alter the shape of the distribution while keeping the median relatively unchanged. Or it may flip the probabilities of two unlikely tokens, barely affecting the minimum. So only looking at the summary statistics of the distributions may not be enough to detect all possible manipulations by an adaptive adversary.


- While the proposed approach performs remarkably well empirically, it is mostly relying on simple aggregated features. Exploring more sophisticated methods to represent, compare and analyze

### Questions
- The adaptive attacks lower your detection accuracy considerably. Have you looked into ways to make the classifiers more robust? For example, by using adversarial training or adding noise to the features.

- Have you evaluated the computational overhead added by extracting the distributional features and running the classifiers? Is this method efficient enough for real-time usage in production systems?

- You use simple summary statistics to represent the output distributions. What prevents more sophisticated adaptive attacks that preserves these summary statistics but still fools the ASR system?

- Your defense relies on statistical metrics like median and maximum probability diverging for adversarial examples. Have you explored attacks that explicitly optimize to minimize statistical distance from the benign data distribution? This could make the adversarials harder to detect.

- Moreover, can the adversarial optimization problem be formulated to reduce divergence from the benign data distribution, while still fooling the ASR system? What are the challenges in constructing such "distribution-aware" attacks?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the issue of adversarial attacks on automatic speech recognition (ASR) systems, where imperceptible noise can manipulate the output. The authors propose a detection strategy applicable to any ASR system, measuring various characteristics of the output distribution. By employing binary classifiers, including simple threshold-based methods and neural networks, they achieve superior performance in distinguishing adversarial examples from clean and noisy data, with AUROC scores exceeding 99% and 98%, respectively. The method's robustness is tested against adaptive attacks, showcasing its effectiveness in detecting even noisier adversarial clips, preserving the system's robustness.

### Strengths
This paper works on important issues and is written clearly.

### Weaknesses
The types of attacks considered in this work appear to be limited, as it seems to primarily focus on the C&W attack. Why not consider other attack methods, such as PGD attacks or Transaudio transfer attacks? Being able to defend against transferable adversarial samples would make the paper more practically significant. I appreciate the presentation of the entire work, but the limited consideration of attack types makes it hard for me to be convinced.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new adversarial example detection method for any automatic speech recognition (ASR) system. Relying on the characteristics of the output distribution in ASR system over the tokens from the output vocabulary, the authors use a function to compute corresponding scores and then employ a binary classifier for adversarial detection. Empirical results have demonstrated the effectiveness of the detection method. In addition, to better analyze the robustness of the proposed detection method, the authors also perform adaptive attacks with aware of the defense mechanism.

### Strengths
1. This paper proposes a simple and effective method for detection adversarial examples for ASR systems.
2. The paper is presented with comprehensive experiments. The authors not only present the benign detection performance of adversarial attacks but also analysis the robustness under adaptive attacks with known detection method.

### Weaknesses
1. Detection performance is only evaluated on limited adversarial attack methods. The authors only evaluate their method on C&W attack and Psychoacoustic attack. More attack methods like Projected Gradient Descent (PGD) [1], the attack proposed in [2], and even some black box methods like FAKEBOB [3] are still needed to be included to prove the general performance of the detection method. For example, the paper could explore how the detection method performs when the perturbation is constrained in different ways, as is done in PGD attacks, or when the attack is generated without direct access to the model's gradients. Exploring the performance against black-box methods like FAKEBOB would demonstrate the robustness of the proposed detection method in more realistic scenarios where the attacker may not have complete knowledge of the ASR system.
2. Lack of comparison with other audio adversarial example detection methods like noise flooding [4]. The authors should provide a comparative analysis with existing detection mechanisms to highlight the advantages and disadvantages of their proposed method. Specifically, comparing the detection accuracy, computational overhead, and robustness against adaptive attacks would provide a clearer understanding of the proposed method's practical applicability.

### Questions
In Section5.1, four guiding principles are provided on selection process. Do such principles limit the adversarial attack implementation? For example, there should be an equal number of tokens in both the original and target transcriptions. Would there be other attack scenarios like tokens insertion or deletion?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
