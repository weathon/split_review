# Rethinking Audio-Visual Adversarial Vulnerability from Temporal and Modality Perspectives

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
While audio-visual learning equips models with a richer understanding of the real world by leveraging multiple sensory modalities, this integration also introduces new vulnerabilities to adversarial attacks.
 In this paper, we present a comprehensive study of the adversarial robustness of audio-visual models, considering both temporal and modality-specific vulnerabilities. We propose two powerful adversarial attacks: 1) a temporal invariance attack that exploits the inherent temporal redundancy across consecutive time segments and 2) a modality misalignment attack that introduces incongruence between the audio and visual modalities. These attacks are designed to thoroughly assess the robustness of audio-visual models against diverse threats. Furthermore, to defend against such attacks, we introduce a novel audio-visual adversarial training framework. This framework addresses key challenges in vanilla adversarial training by incorporating efficient adversarial perturbation crafting tailored to multi-modal data and an adversarial curriculum strategy. Extensive experiments in the Kinetics-Sounds dataset demonstrate that our proposed temporal and modality-based attacks in degrading model performance can achieve state-of-the-art performance, while our adversarial training defense largely improves the adversarial robustness as well as the adversarial training efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies audio-visual adversarial vulnerability, and proposes two kinds of adversarial attacks which deals with the temporal consistency and intermodal correlation. Furthermore, a new audio-visual adversarial training framework is also designed to defend against above attacks.

### Strengths
1. The two kinds of proposed adversarial attacks are novel and important for the topic of audio-visual adversarial vulnerability.
2. The experiments shows the effectiveness of the proposed attacks.

### Weaknesses
1. The proposed defending method seems not designed exactly towards the proposed attacks. In particular, the modality-misalignment-based attack is not specifically addressed.

### Questions
Maybe it is better to show the effectiveness of the method by some real audio-visual samples, i.e., applying the proposed attacks can indeed attack existing methods while the proposed defending method can handle/alleviate it.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces two novel audio-visual adversarial attacks, the Temporal Invariance-based Attack (TIA) and the Modality Misalignment-based Attack (MMA), along with an adversarial training framework that enhances robustness and efficiency. The experiments demonstrate the effectiveness of these methods in benchmarking audio-visual model robustness and improving both adversarial robustness and training efficiency.

### Strengths
(1) The paper proposes innovative adversarial attacks tailored to audio-visual models, specifically the Temporal Invariance based Attack (TIA) and the Modality Misalignment-based Attack (MMA). These proposed  attacks leverage the unique properties of audio-visual data, such as temporal redundancy and intermodal correlation.

(2) The paper introduces an audio-visual adversarial curriculum training framework that incorporates efficient adversarial perturbation crafting and an adversarial curriculum strategy, which achieves a balance between robustness and efficiency.

### Weaknesses
(1) The experiments related to the proposed method are not sufficiently comprehensive.    In Section 5.3, Adversarial Curriculum Training is introduced, which includes two strategies: the Data-level strategy and the Model-level strategy. The core of Adversarial Curriculum Training involves the iterative adjustment of the data masking ratio ( ) and the model dropout ratio ( ). However, the paper does not present corresponding experimental results to substantiate the significance of this iterative design.    Therefore, it is recommended to add experimental results to support the validity of this design.
(2) The paper evaluates unimodal adversarial attack methods (such as FGSM, I-FGSM, and MI-FGSM in the image domain). However, studies such as [1,2] have proposed multimodal attacks. It remains unclear whether the proposed defense method is effective against multimodal adversarial attacks similar to the Audio-Visual attacks discussed in [1].    I suggest adding experiments to evaluate the method's performance under multimodal attack scenarios.

[1] Zhang J, Yi Q, Sang J. Towards adversarial attack on vision-language pre-training models[C]//Proceedings of the 30th ACM International Conference on Multimedia. 2022: 5005-5013. 
[2] Lu D, Wang Z, Wang T, et al. Set-level Guidance Attack: Boosting Adversarial Transferability of Vision-Language Pre-training Models[J]. arXiv preprint arXiv:2307.14061, 2023.

### Questions
Please refer to the questions raised in the Weakness section. Additionally, the reviewer is interested in the following questions:
(1) What's the selection criterion when choosing datasets for the experiment?
(2) Could the proposed method be incorporated into the pre-trained multi-modal models, such as CLIP or BLIP?

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
The paper presents two powerful adversarial attacks: 1) a temporal invariance attack that exploits the inherent temporal redundancy across consecutive time segments and 2) a modality misalignment attack that introduces incongruence between the audio and visual modalities. To defend against such attacks, the paper introduces a novel audio-visual adversarial training framework. Extensive experiments illustrate the effectiveness of the proposed method.

### Strengths
The paper exhibits two powerful adversarial attacks: a temporal invariance attack and a modality misalignment attack. These attacks show their ability to obtain the robustness of audio-visual models.

### Weaknesses
The temporal invariance attack is realized by setting consecutive time segments. The modality misalignment attack introduces incongruence between the audio and visual modalities. Regarding the novelty of the two methods, it seems fair. It is encouraging that two attacks achieve SOTA performance.

### Questions
1. In experiment comparison, some figures use TMA to represent the proposed method, while some of them use Ours. It is suggested to use the same. 
2. For Table 2, does the ablation study use the proposed method TMA? If yes, it is suggested to add the information in the caption.
3. According to Table 2, the successful defense rate continuously increases with the addition of sampling ratio. Where is the change point? The experiment of the ablation study needs to show the sampling ratio value from where the result performance will drop down.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper propose two adversarial attack methods for audio-visual data. Audio-visual data has two main characteristics: the temporal consistency (i.e., between nearby time step, the data is similar) and the modality alignment (i.e., audio and visual data has alignment). The attack exploits these two main characteristics: temporal invariance-based attack and modality misalignment-based attack. In addition, this paper propose the defense mechanism that has lower computational cost in comparison to the naive adversarial training. With lower computational cost, the model can be trained with various strength of the attack, improving its robustness. The way to do lower the computational cost is by only attacking sampled frames instead of attacking all frames. Another additional way is to use curriculum learning by masking out the data and the model's weight from low rate (easy) to high rate (hard). The number of steps to generate attacks also go from low steps (easy) to more steps (hard).

### Strengths
1. The method of attacking audio-visual data based on the temporal consistency and modality alignment seems to be original.

2. The empirical experiments in Section 3 as motivation is interesting to prove how breaking the temporal consistency and modality alignment (by masking out the data) reduce the audio-visual model performance and increase the attack success rate.

### Weaknesses
Several unclear information. Please see Questions.

### Questions
1. What is the meaning of (a)synchronous in context of Line 138?

2. Is "contact" in line 411 and 415 is "concat"?

3. Line 366: Is the masking done synchronously or asynchronously?

4. Figure 3. What does it mean minimizing prediction $p_{av}$, $p_a * p_v$ ?

5. Based on Eq. (4), loss in Eq. (2) will be minimized. However, if we want to exploit the temporal consistency (line 52), why not maximizing this Eq. (2) loss? I think, maximizing variation of the extracted features between time step would make the temporal more inconsistent, which can make the attack more efficient.

### Soundness
3

### Presentation
2

### Contribution
3
