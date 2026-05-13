# Randomized Feature Squeezing against  Unseen Attacks without Adversarial Training

- Decision: Reject
- Scores: 3, 8, 3, 5

## Abstract
Deep learning has made tremendous progress in the last decades; however, it is not robust to adversarial attacks.  
Perhaps the most effective approach for this is adversarial training, although it is impractical as it needs prior knowledge about the attackers and incurs high computational costs.
In this paper, we propose a novel approach that can train a robust network only through standard training
with clean images without awareness of the attacker's strategy. We add a specially designed network input layer,
which accomplishes a randomized feature squeezing to reduce the malicious perturbation. 
It achieves the state of the art of robustness against unseen ${l_1,l_2}$ and $ {l_\infty} $ attacks at one time in terms of the computational cost of the attacker versus the defender through just 100/50 epochs of standard training with clean images in CIFAR-10/ImageNet. Both experiments and Rademacher complexity analysis validate the high performance. Moreover, it can also defend against the ``attacks" on training data, i.e., unlearnable examples, seemingly being the only solution for the One-Pixel Shortcut without any data augmentation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes to inject noise into the input image with randomized Gaussian noise and learns to perturb the image to near binarized values in order to promote robustness against test-time adversarial attacks.

### Strengths
The results appear to be good. It is also interesting to see papers that work on adversarial attacks with unseen threat models. However there are major concerns regarding its trained model robustness.

### Weaknesses
The results of the proposed method appear to be largely influenced by obfuscated gradients. This paper cites this issue in Line 224, but only for the training phase. The paper fails to recognize that Athalye et al.'s key contribution is they highlighted that the models themselves may not be robust because of gradient obfuscation. There are no result in this paper to lessen my worries regarding this concern.

Regarding unseen threat models, recent works typically employ other attacks that go beyond the $\ell_p$ boundaries. For instance, JPEG corruption [a], ReColorAdv [b], LPA [c], StAdv [d], FSA [e] and even methods that generate realistic natural adversarial examples [f].

### Questions
- Could you address the major concern regarding gradient obfuscation?
- Could you test your model on existing attacks beyond the $\ell_p$ confines?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new robust training method that does not require adversarial training. The proposed method utilizes a special input layer that processes the input in two ways: the first way corrupts the input with dependent Gaussian noise, and the second one convolves the input with a 3x3 2d kernel and applies ReLU, then the values of the resulting convolution are inverted. The results of two ways are multiplied, and sigmoid activation is applied to the resulting multiplication. Then, the output of the input layer is forwarded to a standard image classification network. The loss function is modified in a way that convolution output ($\hat{x}$) is small. Therefore, it has an additional term besides weighted standard cross entropy loss. During inference, the second way in the input layer, convolution is dropped and sigmoid activation is replaced with sign function. Experiments are carried out on CIFAR-10 and ImageNet datasets with AutoAttack (AA) on different norms. The results show that clean accuracy slightly dropped and robust accuracy on AA $\ell_\infty$ is slightly behind the adversarially trained (AT) models. However, the proposed method outperforms AT models on other norms $\ell_\infty$, $\ell_1$ and $\ell_2$. In addition, the paper also shows that this proposed robust training has less impact on unlearnable examples (one-pixel shortcut).

### Strengths
- The paper provides a new perspective on randomization in the adversarial defense, although randomization is notoriously known to be vulnerable in defense research.
- The paper justifies the design choices with intuition that gives good insights.
- The paper highlights the last move strategy not to have wrong robust accuracy.
- The paper also shows unlearnable examples less impact the proposed training method.
- The paper clearly presents the limitations of the proposed training.
- Overall, this new way of robust training is interesting and brings many educational values.

### Weaknesses
 - The second contribution says the proposed method is the only work that does not require prior knowledge about the attacks with standard training with clean images. That is not completely true. Please refer to BaRT[1] and LINAC [2].
BaRT uses a set of random transforms with random parameters and standard training, it does not require prior knowledge about the attacks. LINAC uses implicit neural representation with secret key and standard training (no prior knowledge about the attacks). The proposed method may be more related to LINAC.
- The paper does not explicitly define a threat model, unlike adversarial training. It seems the proposed method is robust against AA under $\ell_\infty$, $\ell_1$ and $\ell_2$. I am a bit skeptical of the robustness. The reason is that there must be some bound that the Gaussian noise simulation in the training can cover. This is not clearly known from the current experiments. It would be better to know what type of noise and how much noise the proposed method is robust against.
- The paper does not compare with other attack agnostic defenses such as [1] and [2].
- The paper does not consider any adaptive attack apart from EoT, which is important for a defense evaluation. Please consider parametric bypass approximation (PBA) and discuss potential adaptive adversaries.
- Experiments are limited to AA attacks. Randomized defenses should especially be intensively evaluated with more black-box attacks. Please consider SPSA, N-Attack, and one pixel attack.
- The robustness of the proposed defense is unclear, particularly regarding the role of obfuscated gradients. The reliance on a non-differentiable sign function and the specific form of Gaussian noise injection raise concerns about potential vulnerabilities to attacks that exploit these non-linearities. A more thorough analysis of the gradient landscape is needed to ensure the defense is not merely masking vulnerabilities.
- The evaluation lacks a clear methodology for assessing the robustness against adaptive attacks. The use of BPDA with sigmoid is mentioned, but the specific implementation and its effectiveness are not sufficiently analyzed. The paper should include a more rigorous evaluation of the BPDA approximation, including a comparison with other approximation techniques and a discussion of its limitations.
- The paper does not explore the potential for low-frequency attacks, which have been shown to be effective against defenses that rely on high-frequency noise removal. The experiments should include an evaluation of the proposed defense against low-frequency perturbations to ensure its robustness against a wider range of attack strategies.

### Questions
I am still skeptical of the robustness. If you provide more evidence of robustness, I will increase the score.
- In the AA framework, there are two versions: standard and random. What version did you use for evaluation?
- Experiment results are shown on noise budget 8/255, 16/255 for CIFAR-10, and 4/255 for ImageNet. What happens if you increase the noise budget? Is there any relation between noise simulation in the training and attack noise budget?
- Square attack alone for the black box is not enough. What about at least SPSA [3] and N-Attack [4].
- Will the proposed method be robust against attack methods with masked perturbation? For example, you can apply PGD only on certain region and mask the other out. I am curious about the proposed noise simulation generalizability.
- It is important to consider adaptive attacks. At the very least, parametric bypass approximation (PBA) from LINAC [2] should be considered.
- From the results, the robustness of the proposed training is comparable to adversarial training. Will the proposed robust model have generative gradients as in adversarially trained models? It would be better if you could provide some analysis/visualization of the proposed robust model.

[3] https://proceedings.mlr.press/v80/uesato18a.html
[4] https://proceedings.mlr.press/v97/li19g/li19g.pdf

Minor Comment
In Section 5.1.1, the end of second last paragraph is missing the full stop.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors propose a novel approach to train a robust network without the need for prior knowledge about attackers or adversarial training. It achieves this by adding a specially designed network input layer that performs randomized feature squeezing on clean images. The method shows state-of-the-art robustness against various unseen attacks in terms of computational cost in CIFAR-10 and ImageNet datasets.

### Strengths
1.	The topic of this paper, i.e., defending against adversarial examples solely via training with clean samples, is both meaningful and challenging.
2.	The designed input layer can be easily integrated into different networks like WideResNet and ConvNeXt to boost their performance, demonstrating its potential for wide application across various network architectures.
3.	This paper is easy to follow.

### Weaknesses
1.	Even though the authors claim that the proposed method can effectively defend against adversarial samples based on the $l_{p}$ norm constraint, they have not demonstrated its performance against another mainstream type of generated adversarial examples, such as those from GAN-based attack methods [1, 2] and diffusion model-based attack methods [3, 4]. The authors are required to provide the corresponding defense results to prove the effectiveness of the proposed method. Specifically, the paper lacks experiments against attacks that manipulate the semantic content of the image, rather than just pixel-level perturbations. This is a critical omission, as many real-world attacks may not adhere to strict $l_p$ norm constraints, and the proposed method's robustness against such attacks is unclear.
2.	In the method section, the authors only provided the implementation steps for adding the input layer, without any analysis of the effectiveness of this method, such as theoretical derivations and experimental analyses. The paper lacks a clear explanation of why random feature squeezing at the input layer would lead to robustness. The authors should provide a theoretical justification, such as relating the proposed method to known robustness principles, or at least provide empirical evidence showing how the squeezing operation affects the network's internal representations and decision boundaries. Without this analysis, the method appears to be an ad-hoc approach.
3.	The experimental setup in this paper lacks persuasiveness. The attacks defended in this paper,  FAB-attack and Square Attack, are rather outdated. The authors need to supplement the experimental results of the most recently published adversarial attacks based on the norm constraint in top conferences within the past two years. For example, the authors should include attacks such as AutoAttack, which is a more comprehensive benchmark for evaluating robustness against $l_p$ norm bounded attacks. Furthermore, the paper should consider adaptive attacks, where the attacker has knowledge of the defense mechanism, to more rigorously evaluate the proposed method's robustness.
4.	As mentioned in the SUMMARY section, the defense method proposed in this paper does not even guarantee its effectiveness under the norm constraint. The overall performance, including both accuracy and robustness, is somewhat lacking. I find the claim that the proposed method can defend against samples merely through standard training with clean samples unconvincing. The commonly recognized understanding in the current community is that adversarial examples originate from the inherent vulnerability of deep learning models. Given that the authors propose to defend against adversarial samples under the settings of this paper, they should prove it through theoretical analysis on robustness rather than simply presenting some experimental results. The paper should provide a theoretical analysis of how the proposed input layer modifies the loss landscape of the network, and how this modification leads to robustness. Without such an analysis, the experimental results are not sufficient to support the claims.

### Questions
See Weakness

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors propose a novel approach that enables training robust networks using only standard training on clean images, without awareness of the attacker's strategy. They introduce a specially designed input layer that implements randomized feature squeezing to mitigate adversarial perturbations. This method demonstrates state-of-the-art robustness against unseen attacks while significantly reducing computational expenses. Experiments on CIFAR-10 and ImageNet validate its effectiveness, and it also defends against training data attacks, offering a potential solution for OPS attacks without data augmentation.

### Strengths
1.	The proposed approach allows for the training of robust networks solely using clean images without prior knowledge about the attacker's strategy. This makes it more practical and accessible for real-world applications.
2.	It achieves strong robustness against unseen attacks with lower computational costs and only requires 100/50 epochs of training on CIFAR-10 and ImageNet.

### Weaknesses
1.	The authors do not provide an explanation for why the proposed method (randomized feature squeezing) effectively defends against unseen attacks. Additionally, the designed loss function does not highlight aspects related to adversarial defense. The authors should theoretically or experimentally validate their defense principles from the perspective of features.
2.	The authors overlook comparisons with important defense methods such as image purification and denoising, including DiffPure [1] and NRP [2], which also do not need to train the classifier. They should include corresponding experiments.
[1] Nie W, Guo B, Huang Y, et al. Diffusion models for adversarial purification[J]. arXiv preprint arXiv:2205.07460, 2022.
[2] Naseer M, Khan S, Hayat M, et al. A self-supervised approach for adversarial robustness. In the proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. (CVPR’20) 2020: 262-271.
3.	The authors do not explain how the several parameters of  the Input Layer mentioned in Section 4.1 and 4.2 are selected, nor how these parameters affect the method's performance. More ablation experiments should be included to address this issue.
4.	The authors lack detailed analysis and explanation of the experimental results of defend against OPS. Additional key insights into these findings are needed to strengthen the discussion.

### Questions
All the questions are included in Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
