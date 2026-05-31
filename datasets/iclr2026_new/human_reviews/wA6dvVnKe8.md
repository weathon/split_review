## Human Reviewer 1

### Summary
This paper investigates the robustness of Vision-Language-Action (VLA) models under adversarial attacks. The authors propose a method called Disruption Patch Attack (EDPA), which learns adversarial patches by enlarging the distance between adversarial and original images, as well as between adversarial images and their corresponding text descriptions. Experimental results show that the proposed method degrades VLA performance.

### Strengths
1. The paper focuses on an important and timely topic, i.e., evaluating the robustness of VLA models. 
2. Experimental results demonstrate that the proposed method can successfully reduce the performance of VLA systems.

### Weaknesses
1. The novelty of the proposed method is limited. Learning adversarial examples by maximizing the distance from the original data is a common approach in adversarial attack literature [1-3].
2. Although the work targets VLA systems, it does not analyze how visual perturbations affect the action generation process. As a result, the proposed attack closely resembles conventional vision-language model attacks.
3. While the authors claim that their method does not require access to target models, it still relies on the use of encoders.
4. Experiments are conducted on a single benchmark with only a few baseline comparisons.

[1] Jiaming Zhang, Qi Yi, and Jitao Sang. Towards adversarial attack on vision-language pre-training models. In Proceedings of the 30th ACM International Conference on Multimedia, pp. 5005-5013, 2022.
[2] Zhou Z, Hu S, Li M, et al. Advclip: Downstream-agnostic adversarial examples in multimodal contrastive learning[C]//Proceedings of the 31st ACM International Conference on Multimedia. 2023: 6311-6320.
[3] Zhang, Peng-Fei, Zi Huang, and Guangdong Bai. "Universal adversarial perturbations for vision-language pre-trained models." Proceedings of the 47th International ACM SIGIR Conference on Research and Development in Information Retrieval. 2024.

### Questions
Please refer to Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper introduces a model-agnostic adversarial attack against vision-language-action (VLA) models that is designed to elicit task failure. By using an attack that only targets the image and language encoders, this attack requires less information than previous state-of-the-art attacks designed to elicit the same objective. Finally, the authors present a method to fine-tune the visual encoder to improve robustness.

### Strengths
This paper is technically sound and well presented. The proposed attack does improve the feasibility and ease of optimization compared to previous methods, and achieves better ASR than previous work. Additionally, this is the first (to my knowledge) work that introduces a feasible defense to the proposed adversarial attack. Such defenses are incredibly useful to the field, given the growing number of papers evaluating adversarial attacks against VLAs.

### Weaknesses
While this attack claims to require less information than prior attacks to succeed, namely access to the encoders only, this remains a white-box attack. In table 1, the authors compare with attacks from [Wang et al.](https://arxiv.org/pdf/2411.13587) which require knowledge of the VLA's action space, robotic manipulator, and access to the encoder parameters, and LVLM parameters. However, unfortunately they do not sufficiently motivate a threat model where an adversary might have access to the encoder parameters and not the LVLM parameters, or knowledge of the other two requirements for UADA and UPA. Therefore, the main contributions of this paper are state of the art results in terms of ASR on the LIBERO datasets, and a feasible defense mechanism for this attack. However, UPA, the previous SOTA from Wang et al., already achieved near-perfect ASR on the "task failure" objective, making the small percentage increase not a sufficiently interesting result. 

Additionally, given the fact that none of the evaluated models can reliably complete every task in the LIBERO dataset, "task failure" is not a meaningful metric for evaluation. Further, unlike Wang et al., the authors do not present real-world results, which significantly weakens their claims. 

Finally, while their demonstration of adversarial fine-tuning is undoubtedly a useful addition to the paper, it is a technique that is already well represented in adversarial machine learning literature.

### Questions
1. Why do you think the proposed defense performs so poorly against UADA? 
2. Adversarial fine-tuning works better on some datasets (Spatial, Object) compared to others (Goal, Long). Do you have any intuition for why this might be the case?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes a model-agnostic adversarial patch attack method EDPA, requiring only access to the VLA's visual encoder parameters. EDPA generates a patch by  maximizing the discrepancy between the embeddings of clean and perturbed visual inputs and disrupting the semantic alignment between the visual embeddings and the language instruction's textual embeddings. The paper also provides an adversarial fine-tuning scheme for the visual encoder for defense, in which the encoder is optimized to generate similar latent representations for both clean and adversarially perturbed visual inputs. The results show that EDPA decreases the task success rate of VLA models, while the proposed defense mitigates this degradation.

### Strengths
1. The design of the EDPA loss function is well-conceived. Targeting the semantic alignment between visual and textual latent representations is a logical and novel way to attack the core mechanism of a VLA, rather than just its final action outputs.

2. The experiments are comprehensive, which evaluate against multiple, relevant SOTA models under different settings.

### Weaknesses
1. Limited Scope of Defense Evaluation: The proposed adversarial fine-tuning defense is only evaluated on the single-camera OpenVLA model. While the paper attacks multi-camera models (OpenVLA-OFT and $\pi_{0}$), it does not demonstrate whether the defense is effective for them. These models are more complex and, as the paper notes, already exhibit higher baseline robustness. It is unclear how the defense would be applied or how effective it would be.

2. Lack of Defense Baselines: The paper proposes an adversarial fine-tuning scheme but does not compare it against other defense methods.

3. Patch Occlusion Problem: The authors identify in their limitations that the patch "may occasionally occlude important objects". For example, this could cause the adversarial fine-tuning to train the model to ignore an object that the patch is covering. This is a non-trivial problem for the defense.

### Questions
1. Your defense evaluation was focused on the single-camera OpenVLA model. How would you adapt your adversarial fine-tuning scheme for a multi-camera model like $\pi_{0}$
​
2. You propose a hypothesis that VLA encoders overfit to the robotic arm's appearance. Have you considered an experiment to directly test this? For example, one could fine-tune a VLA model on a dataset where the robotic arm is masked out or digitally removed. If your hypothesis is correct, this model should be more robust to your patch attack, even without adversarial fine-tuning.

3. You note as a limitation that the adversarial patch may occlude important objects. In your current experiments, how is the patch placed? Is it at a fixed location (as in the Appendix attention visualizations ) or placed randomly? Could the EDPA attack be made stronger by jointly optimizing for patch location to maximize disruption (e.g., placing it near the arm) while avoiding occlusion of the target object mentioned in the instruction?

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

---

## Human Reviewer 4

### Summary
This paper proposes an adversarial patch attack for VLAs. The authors describe methods for crafting adversarial patches, and for fine-tuning models to be resistant against these patch attacks. Experiments are presented on LIBERO for a handful of models showing the effectiveness of the attack.

### Strengths
- I agree with the authors that this problem is understudied, and that patch attacks are a reasonable place to start.

### Weaknesses
- The related work on adversarial attacks on VLAs seems a bit sparse. There have been several works beyond (Wang et al., 2024) that tackle this problem; see, e.g., https://arxiv.org/pdf/2505.16640? and https://arxiv.org/abs/2506.03350. Additionally, while the authors cite related work from the adversarial examples community, there is work much closer to the robotics community on attacking LLM-based planners, see, e.g., https://arxiv.org/abs/2407.20242 and https://arxiv.org/abs/2410.13691. I think adding a discussion of these works, particularly those on VLA attacks, would give a better view of the literature, particularly because as written, one could reasonably infer that the only work on VLA attacks is Wang et al., 2024.
- I don't understand why the baselines differ between Table 2 and Table 3. The paper feels incomplete by selectively including these baselines. Furthermore, why did the authors not consider fine-tuning OpenVLA-OFT and pi0 to improve robustness?
- For a purely empirical paper, this paper is *very* light on results, so much so that I'm going to advocate for rejection. It is reasonable to expect that an accepted paper should offer more creative/fine-grained analysis. The paper, as written, doesn't make a compelling/strong case that this method is significantly stronger than the baselines due to a lack of evidence.
- The results also don't seem particularly compelling. It's somewhat hard to interpret the results in Table 3, because the authors use weak baselines (clean performance and random patches). And it looks like the baselines in Table 2 from Wang et al., 2024 do essentially the same. Perhaps there's an argument to be made that the patch attack uses a slightly more realistic threat model, but I think even this is arguable, given that it seems unlikely that a real adversary will apply patches in practice.
- Since we're talking about robotics, why not try this on real hardware? That would certainly result in further impact than showing that this works in simulation. If I remember correctly, the motivation behind patch attacks back in the 2010s was that someone could insert/place patches onto stop signs or t-shirts, causing AVs to perform unsafe actions (happy to provide references if helpful).

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4