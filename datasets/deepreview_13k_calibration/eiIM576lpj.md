# Robustness through Random Activation: Adversarial Training with  Bernoulli Rectified Linear Units

- Decision: Reject
- Avg Score: 3.40
- Scores: 3, 5, 1, 5, 3

## Abstract
Despite their considerable achievements across a range of domains, deep learning models have been demonstrated to be susceptible to adversarial attacks.
In order to mitigate this vulnerability, adversarial training has become a prevalent defense strategy. 
In this context, we propose Bernoulli Rectified Linear Units (BReLU), an activation function designed to further enhance the effectiveness of adversarial training. In contrast to conventional activation functions, BReLU modulates activation probabilities in accordance with input values, thereby introducing input-dependent randomness into the model.
The experimental results demonstrate that the incorporation of BReLU into adversarial training significantly enhances the robustness of the model against adversarial attacks. Specifically, on the CIFAR-10 dataset using the ResNet-18 model, BReLU improved robustness by 15\% under FGSM, by 8\% under PGD-20, and  by 54\% under the CW attack compared to ReLU.
Our findings indicate that BReLU represents a promising addition to adversarial training techniques for strengthening deep learning models against adversarial threats.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes Bernoulli Rectified Linear Units (BReLU), a novel activation function that introduces input-dependent randomness to enhance adversarial robustness in deep learning models.  Experiments using CIFAR-10 and ImageNet-100 datasets demonstrate that BReLU outperforms conventional activation functions like ReLU in adversarial robustness, showing large improvements under various attack scenarios, including FGSM, PGD, and CW attacks.

### Strengths
1. BReLU introduces a unique stochastic mechanism that actively strengthens adversarial robustness
2. The authors present comprehensive experiments on CIFAR-10 and ImageNet-100.
3. Authors show comparison with Dropout.

### Weaknesses
1. Authors only show their method in a limited range of networks without architectures used in this community, such as PreAct-ResNet-18, WideResNet.
2.  The authors do not evaluate their method against stronger and more adaptive attacks, such as AutoAttack [1], which combines multiple adversarial attack methods. Testing against such comprehensive attacks could offer a clearer picture of BReLU’s robustness under rigorous conditions [1].

### Questions
1. How does BReLU impact clean accuracy on CIFAR-10? Given that robustness gains often come with trade-offs in clean accuracy, it would be useful to see a detailed comparison.
2. Have the authors explored the effectiveness of BReLU on transformer-based architectures, such as Vision Transformers (ViTs)? Extending the evaluation to transformer models could demonstrate the generality of this approach across diverse network structures.
3. Can BReLU be effectively incorporated into FGSM-based adversarial training? Given that FGSM is often used for faster adversarial training, insights into BReLU's compatibility with single-step attacks would be valuable.
4. ow is BReLU implemented during inference? Since BReLU introduces randomness, are there architectural discrepancies between the adversarial training phase and the testing phase? Clarification on how to maintain consistency during adversarial example generation and testing would be helpful.

### Soundness
3

### Presentation
3

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
This paper proposes to replace the existing activation units with Bernoulli Rectified Linear Units (BReLU) to incorporate randomness into the model and improve robustness against adversarial attacks. Experiments are conducted on ResNet-18 using various attacks and datasets, showcasing the effectiveness of BReLU to improve the robustness of ResNet/VGG/EfficientNet on these datasets.

### Strengths
1. Although embodying randomness into training to boost adversarial robustness is not a refreshing idea, the proposed BReLU still provide an interesting point of view regarding modifying network architecture as a defensive play. 
2. The presentation of the method is clear and simple, making it easy to follow the core idea of BReLU.
3. BReLU seems to bring certain performance gains w.r.t. some CW attacks.

### Weaknesses
1. One of the key problems of this paper is its unclarified motivation. The selection of sigmoid as the activation function lacks either clear explanations or theoretical analysis. The authors stated that "the sigmoid function was found to yield superior performance" without going deeper to investigate the origin of such superiority, making the work empirical-oriented. This shortcoming significantly undermines the scientific soundness of the paper.
2. Many experiments that could demonstrate the effectiveness of BReLU are missing. For example, auto attack is not included in the evaluation of adversarial robustness. The results of ImageNet-100 across different models are also missed. Larger models such as WideResNet are also not included for comparison, making the claims weak to hold.
3. The scientific contribution of this paper is also lacking. Including randomness can certainly improve robustness for models with limited capacity such as ResNet-18. However, for larger models, the replacement of activation units might have marginal or even degraded influences. As presented in Table.1&3, there is a clear degradation of the increase brought by BReLU when model size increases.

### Questions
1. See Weakness.
2. Can the author also provide results for larger models on larger datasets, and also include the results evaluated using AutoAttack?
3. Changing the entire network and training from scratch seems to be a costly method for improving robustness, making this method less applicable in reality and on larger models. It seems more practical to use BReLU as an additional/addable module and only train this module for robustness gain. If it is a viable option, what is the performance of ReLU under this setting?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces **Bernoulli Rectified Linear Units (BReLU)**, an activation function designed to increase model robustness against adversarial attacks by introducing input-dependent randomness. 
BReLU determines the probability of activation based on input values, unlike conventional deterministic functions like ReLU. 

The authors hypothesize that BReLU’s stochastic nature makes it harder for adversarial attacks to find precise perturbations, thereby improving robustness. 
Through empirical testing on CIFAR-10 and a subset of ImageNet (ImageNet-100), BReLU significantly outperforms standard activation functions like ReLU, Leaky ReLU, and GELU in robustness, especially against traditional adversarial attacks. 
The experiments use ResNet-18, VGG-16, and EfficientNet-V2 models, and the results suggest that BReLU is promising for adversarial defense in deep learning models.

### Strengths
- Novel use of an input-dependent random activation function (BReLU) for adversarial training, potentially advancing the field of robust model design.

- BReLU demonstrates statistically significant improvements in robust accuracy across multiple attacks, including FGSM, PGD-20, and CW.
 
Experiments provide a quantitative basis for BReLU's effectiveness. It shows higher accuracy on adversarial examples compared to other activation functions.

### Weaknesses
 - **Use of Older Architectures:** The article evaluates ResNet-18, VGG-16, and EfficientNet-v2, which are fairly outdated in terms of robust architectures. Recently, evidence (https://robustbench.github.io/) supports that WideResNet is traditionally a more robust architecture, but the authors fail to review it in their evaluation. Moreover, transformer-based architectures have also been shown to be more robust. Thus, it is not evident whether using the proposed BReLU will also improve the robustness of these models.

- **Limited Adversarial Attack Evaluation:** The article proposes a stochastic method to defend against deterministic attacks. This is evaluating apples to oranges. The attacks used in the article, FGSM, PGD, and CW, are relatively mature adversarial attacks in the community, and there's enough evidence to support that they are not *adaptive*, limiting their efficiency against stochastic defenses. Authors should use adaptive attacks that can handle stochasticity and compare whether the activation still provides the desired robustness.

- **Black-Box Attacks:** The article exclusively evaluates white-box attacks and does not evaluate black-box attacks; thus, it is non-evident whether the method is useful against more potent attacks.

- **Compatibility with existing defenses:** The article fails to analyze whether the proposed activation is compatible with existing defenses. If I put an adversarial defense on top of an architecture modified with BReLU, does the proposed activation improve the performance of existing defenses? This is important in terms of the applicability of the proposed approach.

### Questions
- **Extended Analysis:** The authors exclusively sell the proposed activation for its adversarial robustness (which can be argued sufficiently based on their experimental setup). Another direction of analysis could be proposing the activation as a general activation method and checking whether it is a good enough activation function to replace the traditional ReLU activations in a wider scenario. 

Overall, the article is severely limited by its evaluation and analysis. It neither proposes a good activation function for a general case nor demonstrates its robust activation against potent adversarial attacks. 

Since the authors, main focus is on demonstrating improved robustness, I suggest the authors to read the good guide on evaluating adversarial robustness (Carlini et al. 2019), to improve their experiments and show concretely that the proposed activation function, improves the adversarial robustness in an undisputed manner. I also list some of the articles that are very related to the article but are not referenced (Gao et al. 2022; Däubener et al. 2022; Addepalli et al. 2021; Dhillon et. al 2018). 

---

Carlini, Nicholas, Anish Athalye, Nicolas Papernot, Wieland Brendel, Jonas Rauber, Dimitris Tsipras, Ian Goodfellow, Aleksander Madry, and Alexey Kurakin. "On evaluating adversarial robustness." arXiv preprint arXiv:1902.06705 (2019).

Gao, Yue, Ilia Shumailov, Kassem Fawaz, and Nicolas Papernot. "On the limitations of stochastic pre-processing defenses." Advances in Neural Information Processing Systems 35 (2022): 24280-24294.

Däubener, Sina, and Asja Fischer. "How sampling impacts the robustness of stochastic neural networks." Advances in Neural Information Processing Systems 35 (2022): 10230-10243.

Addepalli, Sravanti, Samyak Jain, Gaurang Sriramanan, and R. Venkatesh Babu. "Boosting adversarial robustness using feature level stochastic smoothing." In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 93-102. 2021.

Dhillon, Guneet S., Kamyar Azizzadenesheli, Zachary C. Lipton, Jeremy D. Bernstein, Jean Kossaifi, Aran Khanna, and Animashree Anandkumar. "Stochastic Activation Pruning for Robust Adversarial Defense." In International Conference on Learning Representations. 2018.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work tries to further enhance the robustness of adversarial training by improving the activation function. Specifically, the authors propose BReLU, which determines whether to retain each output component of a layer through a sigmoid function and Bernoulli sampling.

### Strengths
The idea and writing is easy to follow.

### Weaknesses
The effectiveness of BReLU lacks theoretical guarantees. The experiments are too weak; on one hand, there is a lack of stronger attacks to evaluate the effectiveness of BReLU, such as AutoAttack. On the other hand, since BReLU can be combined with any neural network, the authors should attempt to integrate it with state-of-the-art defense methods and validate the robustness on RobustBench.

The authors should implement white-box attacks specifically for BReLU to verify its adversarial robustness in worst-case scenarios.

### Questions
Please see weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors propose a new activation function BReLU which adds input-dependent bernoulli noise to the model.  They combine adversarial training with BReLU and evaluate these models with white box attacks and compare to other activation functions such as ReLU.

### Strengths
- presentation is clear
- idea of modifying activation functions for improving robustness is interesting

### Weaknesses
The biggest problem with the proposed approach is that since BReLU adds noise into testing there is a chance that the approach is just obfuscating the gradients and does not provide true robustness benefits.  To address this the authors should provide show some results with black box attacks and EOT [1].

Additionally, the authors can try training with BReLU but at test time use a deterministic version of BReLU (ie. after computing probabilities of the activation being 1, just apply thresholding and set the activation to 1 if the probability is at least 50% and using 0 otherwise).  The authors can compare this to training and testing with the deterministic version to see if the gains in performance are really due to preventing overfitting.  Also a transfer attack from this deterministic BReLU is also a good black box attack to try to see if the robustness gains come from the activation function or come from obfuscated gradients.

### Questions
See weaknesses.

### Soundness
1

### Presentation
3

### Contribution
2
