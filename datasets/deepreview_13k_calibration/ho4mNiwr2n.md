# Mind Control through Causal Inference: Predicting Clean Images from Poisoned Data

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
Anti-backdoor learning, aiming to train clean models directly from poisoned datasets, serves as an important defense method for backdoor attack. However, existing methods usually fail to recover backdoored samples to their original, correct labels and suffer from poor generalization to large pre-trained models due to its non end-to end training, making them unsuitable for protecting the increasingly prevalent large pre-trained models. To bridge the gap, we first revisit the anti-backdoor learning problem from a causal perspective. Our theoretical causal analysis reveals that incorporating \emph{\textbf{both}} images and the associated attack indicators preserves the model's integrity. Building on the theoretical analysis, we introduce an end-to-end method, Mind Control through Causal Inference (MCCI), to train clean models directly from poisoned datasets. This approach leverages both the image and the attack indicator to train the model. Based on this training paradigm, the model’s perception of whether an input is clean or backdoored can be controlled. Typically, by introducing fake non-attack indicators, the model perceives all inputs as clean and makes correct predictions, even for poisoned samples. Extensive experiments demonstrate that our method achieves state-of-the-art performance, efficiently recovering the original correct predictions for poisoned samples and enhancing accuracy on clean samples.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a defense against backdoor attacks based on data poisoning.

A standard discriminative classification architecture can be expressed as $x\mapsto c_w(f_\theta(x))$, where $f_\theta$ is a feature extractor, and $c_w$ is a classification head: $c_w(z) = \operatorname{softmax}(W z + b)$.

The defense modifies the architecture into $x\mapsto c_{w'}(f_\theta(x)\operatorname{++} a_\phi(\operatorname{DCT}(x)))$, where $\operatorname{++}$ is concatenation, $\operatorname{DCT}$ is discrete cosine transform, $a_\phi$ (AIN) is an additional lightweight feature extractor. We can express $c_{w'}(z\operatorname{++} z_\text{f}) = \operatorname{softmax}(W_1 z + W_2 z_\text{f} + b)$. Training minimizes the standard classification NLL w.r.t. to the parameters $\theta$, $\phi$, and $w'=(W_1, W_2, b)$.

In inference, the defense replaces the input of $a_\phi$ with a clean input, which causes the model to predict the clean class of the input of $f_\theta$ even if the input contains a trigger.

Some of the most important assumptions of the defense are (approximately) as follows:
1. Images with triggers have frequency spectrums distinguishable from clean images (more pronounced high-frequencies).
2. The inductive biases are such that the modified model will separate clean (semantic) features into the output of $f_\theta$ (SFRN), and trigger features into the output of $a_\phi$ (AIN).

It is intuitive (with some additional less load-bearing assumptions) that, if an intervention only replaces the input of $a_\phi$ with any clean input, $c_{w'}$ will classify the main input into its clean class.

The second assumption is confirmed empirically even though the loss function does not enforce it. That is, there exists a solution that $f_\theta$ learns both clean and trigger features, and $a_\phi$ learns nothing.

**Causal model**

The paper claims a correspondence with the causal model $\{I\to Y, A\to I, A\to Y\}$, where $I$ is the input, $A$ is the adversary, and $Y$ is the label. Then it claims that the replacement of the input of the corresponds to a causal intervention called backdoor adjustment that removes the edge $A\to I$, which breaks the confounding path $I\gets A\to Y$ and makes the prediction independent of the trigger.

### Strengths
- The method is simple and interesting. In inference, instead of the modified architecture, the standard classification architecture can be used. We can see this by expressing it as $x\mapsto \operatorname{softmax}(W_1 f_\theta(x) + b')$, where $b' = W_2 z_\text{f} + b$, is computed once from one or more clean inputs (using the notation from my summary).
- The experimental results are very interesting. Considering that the loss function is standard NLL, the training method is surprisingly successful in producing a model that is "blind" to trigger features and classifies inputs with triggers into their original class.
- The paper proposes evaluation of accuracy of recovery of the original label of poisoned inputs (which is analogous to robust accuracy for adversarial examples). I agree that this makes sense.
- The paper is well-structured and the quality of the writing is mostly good.

### Weaknesses
 
**Updates:** 
- minor corrections, 
- updated rating and soundness based on the discussion and paper updates.

The authors have addressed most of the weaknesses, including the ones that I considered most important.

---

1. Some things could be made more clear:
	1. The meaning of "(associated) attack indicator" is initially hard to understand and could be clarified earlier
	3. It is not clear whether "otherwise" in L175 is the negation of the whole antecedent or a part of it.
	4. Why does Proposition 3.4 use the expectation instead of a conditional probability distribution like in Eq. (6). Expectation seems to me to be less natural for a random variable that is a class and Eq. (6) is a more "direct", stronger statement.
	5. Definition 4.1 is not a formal definition.
	6. L258: meaning of "ideal".
	7. Fig. 4 and 5: What are DACC and ADCP?
2. The paper does not make it clear how and how well the proposed method corresponds to the causal model. I think that there are no theoretical guarantees for the assumption 2 in my summary. It seems like there is nothing preventing SFRN to learn the features that AIN learns. Perhaps a loss function that includes minimization of mutual information between the two branches of the model might make the method more robust.
3. The paper does not acknowledge the limitations of the assumptions about the backdoor attack sufficiently. The paper includes experiments with attacks that attenuate high frequencies by blurring, but the frequency spectrum remains distinguishable. I strongly suspect that attacks can be designed to have triggers that AIN does not learn. Perhaps the trigger could be more natural looking, blended and randomly positioned, or be the smooth trigger from Zeng et al. (2021), Refool by Liu et al. (2020), or something like a tennis ball [1]. Consider the a priori indistinguishability of triggers from natural features [1]. If such an attack exist and it is acknowledged clearly, I will not consider this to be a great weakness since the method still seems to be applicable to many practical triggers. I suggest devising stronger adaptive attacks.
4. The experimental evaluation should be improved:
	1. Table 1: Clean accuracies on CIFAR-10 are at most ~87%, which is about 7 percentage points lower than the original results in the ASD and DBD papers. Using stronger learning setups and clarifying the differences would make the results more valuable. Why are the standard CIFAR-10 hyperparameters not used, like in the used open-source implementations?
	2. All 4 baselines evaluate on 3 datasets, but the paper has only 2 datasets in the comparison.
	3. Related work [2] presenting a training-time defense is not cited and compared with.
5. Source code for reproducing the experiments is not provided.

To sum up, I find it most important to:
- improve clarity and relate the theory better with the machine learning algorithm,
- devise stronger adaptive attacks,
- express the limitations of the work more clearly,
- address the drawbacks of the experimental evaluation,
- provide source code for reproducing the experiments.

[1] Khaddaj et al., Rethinking Backdoor Attacks, https://arxiv.org/abs/2307.10163  
[2] Liu et al., Beating Backdoor Attack at Its Own Game, https://arxiv.org/abs/2307.15539

There are some errors and potential errors (which do not affect my rating):
- L088: "(4)SOTA".
- L247-L249 "Equations equation", "Equation equation", ...
- Eq. (4): "(x))" is missing.
- "methods works".
- L460: "mages".
- The descriptions in Appendix F should are not very clear and I think that it is not correct to say that perturbing the images in LC and TUAP is not part of conducting backdoor attacks.
- L1104-1119: "(more details can be found in the Appendix)" is in the Appendix. Check the paragraphs for redundancy.

I find the paper valuable and hope that my concerns can be addressed.

I apologize for any errors on my part.

### Questions
(See weaknesses.)

Suggestions:
- L068: A literature reference could be added for backdoor adjustment theory.
- Fig. 3: Make poisoned examples more distinguishable and consider clarifying why Fig. 3 (c) and Fig. 3 (a) look the same.
- Consider mentioning poisoning rates in subscripts of attack names in tables.
- Include a measurements for a single clean input in figures 4 and 5 for better supporting the claim of sufficiency of a single clean frequency spectrum?
- Consider quantitatively comparing $b'$ and $b$ (see the definition under Strengths).
- Do you know what causes the drop in accuracy under the ISSBA attack?

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
3

### Summary
This paper introduces a novel approach called MCCI, designed to defend against backdoor attacks. This approach employs causal inference techniques to effectively distinguish between clean and poisoned data. The primary objective of this approach is to train a robust model from a poisoned dataset by leveraging both the images and attack indicators, thereby enhancing the model's robustness against various backdoor attack methods. Furthermore, empirical evidence demonstrates that MCCI is highly adaptable for backdoor defense in large pre-trained models while maintaining minimal training overhead. Comprehensive experiments demonstrate the effectiveness of MCCI.

### Strengths
1.This paper applies causal reasoning to backdoor defense with theoretical proof.
2.The proposed approach is an end-to-end method, which is suitable for generalization to large pre-trained models.
3.This paper designed a more challenging and practical threat model. The defender in the threat model expects the model to predict the original, correct labels for backdoored samples.
4.This paper conducted comprehensive ablation studies to demonstrate the effectiveness of each component in MCCI.

### Weaknesses
1. This paper needs to demonstrate the effectiveness of the proposed approach on different model structures, such as VGG and MobileNet.
2. This paper needs to conduct more experiments to defend against advanced backdoor attacks designed from a frequency perspective, such as LF [1].

### Questions
Please refer to the weaknesses.

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
This paper addresses the anti-backdoor learning task by proposing to cut off the causal connection between backdoor attacks and input data. The authors introduce a method called MCCI, which identifies poisoned samples and rectifies them in the feature space to ensure correct predictions. MCCI transforms inputs into the frequency domain using DCT, enhancing the distinction between poisoned and clean samples. During training, MCCI employs the AIN model as an attack indicator to detect poisoned samples. In the inference stage, the AIN model generates a feature vector, which is concatenated with the SFRN model to recover accurate predictions on the original labels of poisoned samples. Experimental results demonstrate the superior defensive performance of MCCI in anti-backdoor learning.

### Strengths
- This paper is well-written and easy to follow with the assistance of all proper diagrams.
- This paper conducts extensive experiments including the consideration of large pre-trained models

### Weaknesses
 (1) Due to the high similarity to CBD defense, the intuition and the novelty of employing the causality requires better clarification.

(2) The elaboration about the optimization of AIN in the training is missing.

(3) Using clean images from the validation dataset conflicts with the threat model.

(4) Discuss using other frequency domain transformations, e.g., DFT, is omitted.

(5) Many details of the experimental setup are missing.

(6) Clean accuracy of the baseline is lower than state-of-the-art.

(7) Low Frequency attack is not considered in the evaluation.

(8) Some anti-backdoor learning defenses are mentioned but not considered in the final evaluation.

(9) Many citations (e.g., lines 255, 362–363, 382–383, 389–390) use either \citep{} or \citet{} incorrectly.

### Questions
Q-(1): This paper aims to apply the Backdoor Adjustment to cut off the causal connection between the adversary and the input data. However, all proofs end up with the conclusion in Equation (2) that it is crucial to identify poisoned samples (same as the task defined in [1] and its related methods) with an effective attack indicator, which, in a nutshell, is basically a conjunctive implementation of the input data transformation and the training of the identification model AIN. The prior work CBD [2] already addresses the defense with the inspiration of causality. Accordingly, it proposes to disentangle the confounding and causal effects in the hidden space by employing a backdoored model as the reference during the minimization of mutual information. In the context of the clean model training with a backdoor reference, can the author include a detailed comparison section highlighting the key technical differences between CBD and MCCI, especially regarding the training loss formulation?

Q-(2): In Algorithm 1, the training losses used for AIN and SFRN models are not formulated. To make the methodology more clear and reproducible, I suggest the authors provide the mathematical formulations for the two training losses.

Q-(3): In section 3.1, the threat model specifies that the defender lacks prior knowledge of the backdoor in the poisoned dataset. However, the AIN model requires clean images from the validation dataset to generate the (averaged) frequency spectrum, which, in my opinion, conflicts with the threat model. Meanwhile, using clean images from the validation dataset is an inappropriate setting. Most defenses assume the availability of a set of clean images, which are from the training dataset set rather than the validation set.

Q-(4): In Appendix D, the authors briefly discuss the selection of DCT. However, there is no detailed rationale for using DCT to realize the cut-off of the causal connection between the adversary and the input data. I suggest the authors provide an analysis of the functionality difference between DCT and DFT in the defense. In addition, more experiments on using DFT or DCT would be beneficial as well.

Q-(5): An elaboration on the experimental setup is necessary. In particular, the settings below require more details:

- The exact poisoning rate used in the experiments
- Specific configurations and hyper-settings for each considered attack method
- Hyperparameter settings for MCCI and baseline defenses
- Full specification of the ResNet architecture (e.g. ResNet18, ResNet50, etc.), rather merely mentioning ResNet as the baseline

Q-(6): In prior anti-backdoor learning, the baseline model ResNet18 achieves a clean accuracy on the CIFAR10 dataset, mostly above 93%. However, the clean accuracy in Table 1 is significantly lower. I suggest the authors verify their implementation and training procedure for the baseline model and provide a detailed comparison of their training setup to those used in prior work reporting higher accuracies. Based on them, the authors can discuss potential reasons for the discrepancy and its implications for interpreting the results.

Q-(7): The authors pick DCT as the transformation due to the inspiration of the low-frequency (LC) attack [2]. This attack is potentially very effective against MCCI defense, while it is not considered in the evaluation. I suggest the authors to include the LC attack in their main evaluation and discuss potential modifications to MCCI that could improve its robustness to LC attacks if weaknesses are found.

Q-(8): In section 2, the authors mentioned many advanced anti-backdoor learning defenses. However, only some of them (i.e., ABL, DBD, CBD, ASD) are considered in the evaluation. And other methods e.g. D-ST [5] are ignored. Can the authors provide explicit criteria for selecting these baseline defenses included in the evaluation? 

 
[1] Pal et al., "Backdoor Secrets Unveiled: Identifying Backdoor Data with Optimized Scaled Prediction Consistency," ICLR 2024.

[2] Zeng et al., "Rethinking the Backdoor Attacks’ Triggers: A Frequency Perspective," ICCV 2021.

[3] Zhang et al., "Backdoor Defense via Deconfounded Representation Learning," CVPR 2023.

[4] Chen et al., "Effective Backdoor Defense by Exploiting Sensitivity of Poisoned Samples," NeurIPS 2022.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors begin by analyzing backdoor attacks from the perspective of causal inference. They analyze that backdoor attacks play a role of confounder A and introduce the spurious path from I to Y. The misled backdoor prediction is attributed to the confounding bias brought about by the confounder. Consequently, to form a backdoor defense, they apply a do-calculus on I, thus cutting off the edge between A->I and preventing backdoor attacks. The do-calculus in this case is equivalent to including both the image and the associated attack indicator as the model input. In particular, they leverage an existing backdoor detection approach to serve as the attack indicator. Consequently, they take both the image and the associated attack indicator as input and train an end-to-end clean model.
Furthermore, in order to find out the original ground-truth labels of the input images, they use counterfactual outcome estimation and fix A=0. The output labels are regarded as the original labels.

### Strengths
1. The threat model they consider is more challenging and practical than existing ones because they require the training process be in an end-to-end fashion, instead of containing multiple stages; they require the trained model to output the original ground-truth labels even for poisoned images.

2. The idea of using causal inference to analyze backdoor is really novel and can reveal the essence of backdoor attacks to some extent. In particular, I appreciate the following views:

(1) They regard backdoor attacks as the confounder. Based on this view, the reason why backdoored models predict labels wrongly is that the confounder introduces a spurious path between I and Y.

(2) They regard backdoor defense as the do-calculus on I and derive that the do-calculus is equivalent to letting the model take both the image and the associated attack indicator as input. Based on this view, a end-to-end clean model could be trained by letting both of them as input.

(3) They regard asking models to give original labels as fixing the confounder as 0. Based on this view, by letting the attack indicator be 0, the trained model could output the original labels.

### Weaknesses
See questions.

### Questions
1. It seems that D-ST introduced in the NeurIPS 2022 paper [1] also shares the same threat model with this paper and the reported performance is superior to ABL and DBD (which are the baselines used in this paper). It would be interesting to know the performance of the proposed method compared to this one.

[1] Chen, W., Wu, B., & Wang, H. (2022). Effective backdoor defense by exploiting sensitivity of poisoned samples. Advances in Neural Information Processing Systems, 35, 9727-9737.

### Soundness
4

### Presentation
4

### Contribution
4
