# ASTrA: Adversarial Self-supervised Training with Adaptive-Attacks

- Decision: Accept
- Scores: 6, 8, 5

## Abstract
Existing self-supervised adversarial training (self-AT) methods rely on handcrafted
adversarial attack strategies for PGD attacks, which fail to adapt to
the evolving learning dynamics of the model and do not account for instance specific
characteristics of images. This results in sub-optimal adversarial robustness
and limits the alignment between clean and adversarial data distributions.
To address this, we propose ASTrA (Adversarial Self-supervised Training with
Adaptive-Attacks), a novel framework introducing a learnable, self-supervised
attack strategy network that autonomously discovers optimal attack parameters
through exploration-exploitation in a single training episode. ASTrA leverages a
reward mechanism based on contrastive loss, optimized with REINFORCE, enabling
adaptive attack strategies without labeled data or additional hyperparameters.
We further introduce a mixed contrastive objective to align the distribution
of clean and adversarial examples in representation space. ASTrA achieves
state-of-the-art results on CIFAR-10, CIFAR-100, and STL-10 while integrating
seamlessly as a plug-and-play module for other self-AT methods. ASTrA shows
scalability to larger datasets, demonstrates strong semi-supervised performance,
and is resilient to robust overfitting, backed by explainability analysis on optimal
attack strategies.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new method ASTrA for self-supervised training of adversarially robust features. Specifically, the paper introduces several novel and important components to boost the performance of adversarial self-supervised training: mixed contrastive loss and adaptive strategy network. With these two new component, the paper improves the robust accuracy by 1-2% on commonly used datasets like CIFAR10. Ablation study verifies the necessity on these components. Further experiments demonstrates the scalability and potential for wide applications when combining with other methods.

### Strengths
1. The paper studies an important topic, self-supervised adversarial training, and proposes novel components to improve the performance of the self-supervised AT.

2. The empirical experiments are extensive, showing improvement of ASTrA over existing method. The ablation study and analysis are thorough, demonstrating the necessity on each component.

### Weaknesses
1. Lacking of empirical experiments on larger scale to really reflect the effectiveness of self-supervised AT. As CIFAR10, CIFAR100 and STL-10 are all supervised datasets with clear label, supervised adversarial training may be enough to achieve good robust accuracy. Using unlabel data may be a good way to further improve the performance. However, the paper lacks of the experiments in this aspect.

2. The last term of reward (eq (4)) does not contain the optimized parameter $\theta$, why is it necessary to add it to the reward function?

3. As the number of parameters of ResNet 18 is already higher than the number of training example times the number of action space, is it possible to use the non-parametric modeling to replace the strategy network?

### Questions
1. The last term of reward (eq (4)) does not contain the optimized parameter $\theta$, why is it necessary to add it to the reward function?

2. As the number of parameters of ResNet 18 is already higher than the number of training example times the number of action space, is it possible to use the non-parametric modeling to replace the strategy network?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work attempts to improve the generation of adversarial examples for use in the adversarial self-supervised training (self-AT). Self-AT is made difficult by the fact that ground truth labels are not known. The first contribution of this paper consists of a Strategy Network, which is a module that can be incorporated during constrastive training to adaptively select parameters for adversarial example generation, conditioning on both the input sample and the contrastive model's current parameters. The Strategy Network is designed to balance adversarial contrastive loss, which encourages a high dissimilarity between perturbed representations, and clean contrastive loss, which ensures that the Target Network maintains high performance on the clean data distribution. For training the Target Network, a new Mixed Contrastive Loss term is introduced, which prevents robust overfitting by penalizing excess distance between clean and adversarial perturbations. While these modifications to contrastive training allow for an improved tradeoff between strong adversarial perturbations during training and high clean accuracy, they do introduce difficulties in training due to the non-differentiable nature of adversarial example generation. To remedy this, the REINFORCE algorithm is used to estimate the gradients of the Strategy Network's objective function. The complete method is evaluated by pretraining the ResNet18 architecture using three different datasets (CIFAR10, CIFAR100, and STL10), and then finetuning using one of three approaches (standard linear finetuning, adversarial linear finetuning, and adversarial full finetuning). Both clean and robust accuracy are computed, and compared against several other robust contrastive learning methods. ASTrA is shown to improve both robust and clean accuracy over the other training methods tested. An ablation study shows that the individual components each contribute to this improvement, and it is shown how ASTrA can be used as a plug and play component to improve the performance of the other methods.

### Strengths
- Using reinforcement learning to optimize adversarial attack generation is well motivated in this paper and seems like a powerful technique to improve robust training. I could imagine this technique being beneficial in applications beyond self-supervised contrastive training.
- The experimental section appears well designed. Several state of the art methods are used as comparison, and four datasets are utilized (CIFAR-10, CIFAR-100, STL-10, and Imagenet-100).
- The plug and play framework presented here could potentially offer a significant leap in robustness for self-supervised contrastive models.
- Code is provided for reproduction purposes.

### Weaknesses
 - The evaluation section could include more information on the impact of ASTrA on other metrics (like training time or training stability). I would assume that the additional complexity introduced by the strategy network might make the training process more difficult, although I would be interested in hearing if this wasn't the case. I do believe the effects on the training process warrant more explanation in the paper.
- I think one underexplored aspect of this approach is how the discretization of the attack parameters affects the downstream performance of the model. I imagine there would be some sort of tradeoff between training efficiency and performance as you vary the number of parameter choices that the strategy network can make. Were there any experiments where the discretization of the attack strategy was changed?

### Questions
- Would the methods in this paper (particularly the strategy network) be suitable for standard adversarial training in a supervised, non-contrastive setting? It seems that adaptively choosing attack parameters might be beneficial in adversarial training more generally.
- I'm not sure I understand what causes the exploration phase to end and the exploitation phase to begin. For example, in Figure 6, why are the dotted lines drawn where they are? The changes don't always seem consistent between the plots. I also found this plot somewhat difficult to understand in general, it wasn't immediately clear to me that the different colors represented different choices of attack parameters.
- Why is Figure 8 a line graph? It seems like it could be more effectively presented as a table.
- How do you think your work relates to the body of research studying adversarial curriculum learning (i.e. [1,2])? At a high level, these works seek to improve adversarial training by adjusting the strength of adversarial examples used during the training process. Do you see ASTrA as having similar motivation and design inspiration to these techniques? How does ASTrA differ from these kinds of curriculum approaches?
- What limitations does your approach have?

[1] Sitawarin, Chawin, Supriyo Chakraborty, and David Wagner. "Sat: Improving adversarial training via curriculum-based loss smoothing." In Proceedings of the 14th ACM Workshop on Artificial Intelligence and Security, pp. 25-36. 2021.

[2] Cai, Qi-Zhi, Min Du, Chang Liu, and Dawn Song. "Curriculum adversarial training." arXiv preprint arXiv:1805.04807 (2018).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel adaptive attack strategy for adversarial contrastive learning that autonomously discovers optimal attack parameters for generating adversarial examples. By leveraging these parameters in adversarial training, the proposed method enhances adversarial robustness while maintaining standard accuracy.

### Strengths
1. The proposed method generates effective adversarial examples by dynamically adjusting attack parameters based on the characteristics of the input data and the model's training dynamics. This adaptive approach outperforms existing methods relying on fixed attack strategies.
2. The proposed method serves as a play-and-play module, allowing seamless integration with existing adversarial contrastive learning methods.

### Weaknesses
1. The paper has several readability issues. For instance, equation (3) uses $\theta$ as an input for $L_{\text{clean}}$ while equation (4) switches to using $w^{\text{fixed}}$. This inconsistency causes confusion in understanding the proposed method. Additionally, Table 1 references an undefined [19], making it difficult to verify results. Overall, the writing lacks clarity.
2. The paper lacks clear explanations of the strategy network, a key component of the proposed method.
    - There is insufficient detail on how attack parameters are sampled from the conditional distribution $p(a|x;\theta)$. Since the effectiveness of the adaptive attack strategy depends on this process, a more thorough explanation of how the strategy network determines these parameters is crucial.
    - The interaction between the strategy and target networks is unclear, particularly how $\theta$ is optimized during training. More details are needed on how feedback from the target network and the REINFORCE algorithm update $\theta$ for learning optimal attack strategies.
3. The adaptive attack strategy introduces additional computational overhead. However, there is no analysis of its impact on overall training time compared to existing methods.

### Questions
1. Could you explain how attack parameters are sampled from the conditional distribution $p(a|x;\theta)$? Also, could you provide a step-by-step explanation of the interaction between the target and strategy networks? Particularly, it is unclear how $L_{\text{clean}}$ in the reward objective updates $\theta$, as it seems that $\theta$ is not involved in that loss.
2. Could you compare the computational complexity of the proposed method with existing methods? Additionally, could you analyze the computational costs of crafting instance-specific optimal attack strategies and training the strategy network?
3. Could you expand the experimental comparisons to include state-of-the-art methods like DynACL++ and DynACL-AIR++ for a more comprehensive evaluation of the proposed method's strengths and limitations? 
    - DynACL-AIR++ is proposed by Xu et al. in Enhancing Adversarial Contrastive Learning via Adversarial Invariant Regularization, NeurIPS 2023.

### Soundness
3

### Presentation
2

### Contribution
3
