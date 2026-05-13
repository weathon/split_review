# Towards Reliable Backdoor Attacks on Vision Transformers

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
Backdoor attacks, which make Convolution Neural Networks (CNNs) exhibit specific behaviors in the presence of a predefined trigger, bring risks to the usage of CNNs. These threats should be also considered on Vision Transformers. However, previous studies found that the existing backdoor attacks are powerful enough in ViTs to bypass common backdoor defenses, \textit{i.e.}, these defenses either fail to reduce the attack success rate or cause a significant accuracy drop. This study investigates the existing backdoor attacks/defenses and finds that this kind of achievement is over-optimistic, caused by inappropriate adaption of defenses from CNNs to ViTs. Existing backdoor attacks can still be easily defended against with proper inheritance from CNNs. Furthermore, we propose a more reliable attack: adding a small perturbation on the trigger is enough to help existing attacks more persistent against various defenses. We hope our contributions, including the finding that existing attacks are still easy to defend with adaptations and the new backdoor attack, will promote more in-depth research into the backdoor robustness of ViTs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The article identifies shortcomings in existing defense methods against backdoor attacks on Neural Networks, specifically focusing on Vision Transformers (ViT). It highlights deficiencies in fine-tuning-based defense and pruning-based defense on ViT and proposes adjustments to enhance their performance. Additionally, the authors introduce a new backdoor attack method, CAT, designed to bypass these defenses with increased robustness. CAT involves adding special adversarial perturbations to the trigger pattern to minimize noticeable channel activation differences between benign and triggered input.

### Strengths
- This paper is easy to understand.
- The article observes the use of different optimizers for training Convolutional Neural Networks (CNNs) and ViTs, suggesting a potential overstatement of ViTs' vulnerability to attacks with defense.
- The CAT attack seems effective in attacking the ViT models.

### Weaknesses
 - The contributions of this paper seem incremental, especially in the defense part. The experiments indicate that optimizing the choice of optimizer, adjusting epoch numbers, and selecting appropriate granularity for pruning can improve defense performance on ViT. To apply fine-tuning-based methods to ViT, the authors adjust optimizers and epochs. However, these improvements are based on experimental trials, and there is no methodology to guide us on how to pick good hyperparameters.
- In Section 3.2, the impact of the epoch on fine-tuning defense is explored. The curve for the first 20 epochs differs significantly from the first 20 epochs when setting the experiment to 100 epochs, particularly in the left plot of (a) left. The variability in experimental results raises concerns about the reliability of the findings, considering the potential instability.
- Table 4 illustrates that the CAT attack method improves ASR, but the enhancement is limited, as most unsuccessful attacks do not become successful.
- Some symbols used in the formulas lack explanations. Appendix C Figure 7 should refer to Table 7.

### Questions
See my comments above.

### Soundness
2 fair

### Presentation
2 fair

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
This paper study backdoor attack on Vision Transformers. They show that existing defenses successfully defend against backdoor attacks in ViT-B and CIFAR10 dataset. Moreover, they proposed Channel Activation attack (CAT). They show that CAT attack is more effective on CIFAR10 dataset.

### Strengths
[+] CAT attack can transfer to other Vision transformers on Table 4 in CIFAR10 dataset.

### Weaknesses
[-] Study of backdoor attack with only CIFAR10 and single vision transformer architecture is not convincing, and any conclusion based on these limited settings won’t be accurate. Note that study of backdoor attack on the Vision Transformer has been conducted before.

[-] What is your thread model in your proposed attack? Do you assume that adversary have access to the model during training? Current setting is confusing to me since there are two thread models: 1. Both source and target being same model 2. Source and target are different


[-] In ImageNet experiments, both source and target are ViT-B. Does this means that adversary has access to model architecture and its parameters. This is not a practical scenario in my opinion and limits the impact of the paper.

### Questions
-

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper first conducts a comprehensive evaluation of existing backdoor attacks on ViT and reveals the reason they can bypass existing defense is due to the inappropriate use of optimizer, e.g., SGD. After refining the existing backdoor defense, the experiment results show that existing backdoor attacks on ViT will no longer achieve effective attack after defense. Therefore, the authors propose a more reliable attack by adding special adversarial perturbations into the trigger pattern. The results show their method can achieve a stable attack after some type of defense.

### Strengths
The authors revisit the existing backdoor defense methods on ViT and find that these defense methods don’t work well because of the misuse of the optimizer, i.e. SGD.

The authors conduct comprehensive experiments and ablation studies.

### Weaknesses
The hypothesis lacks enough evidence. Firstly, the authors claim “ViTs are typically trained by AdamW while its fine-tuning defense is trained by SGD (NOT AdamW, maybe inheriting from CNNs). This discrepancy in optimizers raises the possibility that the perceived vulnerability of ViTs (with defense) might be overstated, i.e., the success of attacks on ViTs with defense may be questionable.” However, the authors don’t cite papers that use SGD to mitigate backdoors in ViT. And when transferring the defense methods on CNN to ViT, the most straightforward scheme is to use the same optimizer as when training the model, i.e., SGD for CNN and AdamW for ViT. Secondly, the authors claim that the misuse of the optimizer in fine-tuning leads to suboptimal defense performance and conduct experiments in Table 2 to show the effect of optimizers. However, the attack methods used in Table 2 are all CNN-specific attack methods. Authors should conduct experiments on ViT-specific backdoor attacks [2,3,4] because they are investigating backdoor defense on ViTs.

The “backdoor defense” in the paper only denotes the “mitigation” aspect. And the design of their reliable attack is based on “the difference in the intermediate-level representations between the inputs with and without triggers”. It is not clear if this attack can bypass detection technologies that don’t rely on the difference in activation, such as Neural Cleanse[1] which is based on reverse engineering and outlier detection.

### Questions
Is the proposed attack only effective on ViT? Is it possible that it also works well on CNN, since the proposed method doesn’t leverage ViT’s unique features compared to CNN? 

Same with weakness 2, is it possible that the authors can provide results of the attacks against backdoor detection techniques such as Neural Cleanse [1]?

[1] B. Wang et al., "Neural Cleanse: Identifying and Mitigating Backdoor Attacks in Neural Networks," 2019 IEEE Symposium on Security and Privacy (SP), San Francisco, CA, USA, 2019, pp. 707-723, doi: 10.1109/SP.2019.00031.

[2] Zheng, Mengxin, Qian Lou, and Lei Jiang. "Trojvit: Trojan insertion in vision transformers." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2023.

[3] Zheng, Runkai, et al. "Data-free backdoor removal based on channel lipschitzness." European Conference on Computer Vision. Cham: Springer Nature Switzerland, 2022.

[4] Akshayvarun Subramanya, Aniruddha Saha, Soroush Abbasi Koohpayegani, Ajinkya Tejankar, and Hamed Pirsiavash. Backdoor attacks on vision transformers. arXiv preprint arXiv:2206.08477, 2022a.

### Soundness
2 fair

### Presentation
3 good

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
This paper examines the prevalent backdoor attacks and defenses, revealing an over-optimistic perception arising from the improper adaptation of defenses from CNNs to ViTs. With appropriate inheritance from CNNs, existing backdoor attacks can be effectively mitigated. Additionally, the paper introduces a more robust attack method: a minor perturbation on the trigger significantly enhances the resilience of existing attacks against diverse defenses.

### Strengths
It reveals an over-optimistic perception arising from the improper adaptation of defenses from CNNs to ViTs. 

This paper introduces a more robust attack method against ViTs.

### Weaknesses
When testing existing backdoor attacks against ViT, the authors only use CNN-based backdoor attacks without ViT-specific backdoor attack methods. Thus, the possibility exists that existing ViT-specific backdoor attacks can also evade well-adapted backdoor defenses.

When testing existing backdoor defenses, the authors only consider purified-based backdoor defenses. How about the detection-based backdoor defenses? Are they also over-estimated?

Lack of enough baselines to prove the effectiveness of the proposed attack method. After proposing a new backdoor attack, the authors should compare it with SOTA backdoor attacks, especially advanced ViT-specific backdoor attacks, to show its superiority.

There is insufficient evaluation to explore whether the proposed attack can evade the SOTA backdoor defenses designed for ViT.

There is a lack of enough complex datasets, such as Imagenet, to evaluate the effectiveness of the proposed attacks.

### Questions
See the concerns in weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
