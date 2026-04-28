# Towards Reliable Backdoor Attacks on Vision Transformers

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
Backdoor attacks, which make Convolution Neural Networks (CNNs) exhibit specific behaviors in the presence of a predefined trigger, bring risks to the usage of CNNs. These threats should be also considered on Vision Transformers. However, previous studies found that the existing backdoor attacks are powerful enough in ViTs to bypass common backdoor defenses, i.e., these defenses either fail to reduce the attack success rate or cause a significant accuracy drop. This study investigates the existing backdoor attacks/defenses and finds that this kind of achievement is over-optimistic, caused by inappropriate adaption of defenses from CNNs to ViTs. Existing backdoor attacks can still be easily defended against with proper inheritance from CNNs. Furthermore, we propose a more reliable attack: adding a small perturbation on the trigger is enough to help existing attacks more persistent against various defenses. We hope our contributions, including the finding that existing attacks are still easy to defend with adaptations and the new backdoor attack, will promote more in-depth research into the backdoor robustness of ViTs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a backdoor attack against transformer-based models by exploiting the differences in the feature activations between the benign and poisoned samples. The paper first demonstrates that there are differences between responses of attacks on CNNs and ViTs, motivating them to propose a stronger attack for ViT. The proposed attack essentially involves an optimization process of finding the trigger patterns that reduce the activation differences between the benign and poisoned samples. The paper demonstrates the effectiveness of the proposed attacks across various base attacks, CIFAR10/Imagenet datasets and various versions of vision transformers in white-box and black-box settings.

### Strengths
The paper has the following strengths:
* The paper is well-written. The setup of the experiments to demonstrate the effectiveness of CAT is also well-planned.
* The optimization method is also reasonable, although it's not a surprise. 
* The experiments show that CAT enjoys favorable performance in attacks against ViTs

### Weaknesses
I think the paper is interesting, exposing an important threat yet against ViTs. However, there are several concerns about the contributions and rigorousness in the claims of the paper:

* I find that several claims are empirical, but the experiments are not rigorous enough. For example, the observed differences in the network's responses could exist for CNNs or other types of DNNs too. This means that the proposed attack could also work for other types of DNNs, not just ViTs. Focusing the specific technique to ViTs makes the scope of the paper pretty limited.
* Furthermore, observing the differences between poisoned and benign samples is not a new strategy to derive new attacks/defenses in the backdoor domain. By focusing on exploiting this difference to derive a new attack makes the novelty of the paper pretty limited. I would suggest that the paper should focus more on rigorous analyses of why this difference is specific to ViTs. Or perhaps, why overcoming this difference with the proposed attack still could not achieve high attack success rates in several cases. 
* I also find that the analysis on fine-tunning is limited. Why is AdamW more sensitive than SGD? In addition, there have been several fine-tuning based defenses which have been proposed in the last 1-2 years (e.g., super-fine-tuning, or FT-SAM); these works study the various settings of fine-tuning parameters but they are not evaluated in the paper (although super-fine-tuning is mentioned).
* I also suggest that the paper should include other types of defenses such as input perturbation (e.g., Strip is mentioned, and others such as adding noise, quantization, etc...). At the moment, most of the selected defenses are based on spotting the differences between clean and benign inputs, which makes the evaluation a bit biased.

### Questions
Please see the questions in Weaknesses!

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates backdoor attacks on ViT, identifying weaknesses in current defense methods, particularly fine-tuning and pruning-based defenses. It underscores the importance of using AdamW as the optimizer for fine-tuning defenses and limiting pruning to specific linear layer channels. the authors propose a new backdoor attack method, CAT, which includes adversarial perturbations in the trigger pattern to evade defenses by minimizing activation differences between benign and triggered inputs. Experimental results show that CAT achieves reliable, robust attacks even after defenses are applied.

### Strengths
The CAT seems effective in attacking the ViT models, and can transfer to other Vision transformers on Table 4 in CIFAR10 dataset.
Author observes the use of different optimizers for training ViTs.

### Weaknesses
It is not clear what is the threat model for CAT attack.

Table 4 shows that the CAT attack method increases ASR; however, this improvement is modest, as most previously unsuccessful attacks remain ineffective.

The authors modify optimizers and adjust the number of epochs to apply fine-tuning methods to ViT. However, these enhancements are derived from experimental trials, lacking a systematic approach for selecting optimal hyperparameters.

The attack effectiveness on CIFAR-10 can be less convincing. Are there any more baseline or datasets results demonstrating the effectiveness?

The paper lacks more baseline comparisons such as with the papers below. Since it investigates backdoor defense on ViTs, such comparison is important.
[1] Zheng, Mengxin, Qian Lou, and Lei Jiang. "Trojvit: Trojan insertion in vision transformers." Proceedings of the IEEE/CVF Conference on CVPR. 2023.
[2] Zheng, Runkai, et al. "Data-free backdoor removal based on channel lipschitzness." ECCV. Cham: Springer Nature Switzerland, 2022.

### Questions
Please refer  to my questions described in the Weakness part.

### Soundness
2

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
This paper studies backdoor attacks on ViTs, starting from the observation that previous finetuning-based and pruning-based defenses tend to fail on ViTs. The paper propose adjustments to improve these defenses' performance on ViTs and then introduce a more robust backdoor attack method called Channel Activation attack (CAT) that can bypass these defenses by adding small perturbations to triggers before training.

### Strengths
1. The paper is well-written and easy to follow, with clear explanations of concepts and methodologies.

2. The proposed CAT attack demonstrates effectiveness in attacking ViTs.

### Weaknesses
1. The paper's fundamental observation about existing backdoor defenses failing on ViTs appears to be based on a questionable premise. The authors attribute the failure to inappropriate optimizer usage (SGD instead of AdamW), but this seems like an implementation oversight rather than an inherent limitation of these defense methods. When applying CNN defenses to ViTs, it would be natural to use the standard ViT optimizer (AdamW) rather than CNN's typical optimizer (SGD).

2. The experimental evaluation could be more comprehensive. On CIFAR-10, only four simple attack methods were evaluated. On ImageNet, results were only shown for CAT combined with Badnets and Blended attacks. A broader range of attack methods would strengthen the paper's conclusions, especially on ImageNet.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes CAT framework for studying backdoor attacks on ViT-based models, which adds special adversarial perturbations to the existing trigger pattern to enhance the attack ability. Additionally, the authors discuss the deficiencies in finetuning-based defense and pruning-based defense on ViT and compare the difference between SGD and AdamW optimizers. Experiments conducted on two dataset to demonstrate the effectiveness of CAT.

### Strengths
1) The authors revisit the existing backdoor defense methods on ViT and discuss their issues.

2) Extensive experiments are conducted to evaluate the effectiveness of CAT.

### Weaknesses
1) The hypothesis of the utilization of the optimizer in CNN and ViT backbones is lacking demonstration.

2) According to Tabel 4, the improvement introduced by CAT on a series of ViT variants is limited. And the authors should report the clean data accuracy of these methods after being defended.

3) Comparison baselines are out-of-date. More recent backdoor attack and defense methods should be involved to test CAT.

4) Stealthiness of CAT is not evaluated. This criterion is crucial for backdoor attack methods to prevent malicious users to filter poisoned samples out.

### Questions
CAT mainly focuses on studying backdoor attacks on vision transformers. Is it possible to benchmark more vision transformer models (PVT, CVT, TNT, etc) to explore this security issues?

### Soundness
2

### Presentation
2

### Contribution
2
