# MeanSparse: Post-Training Robustness Enhancement Through Mean-Centered Feature Sparsification

- Decision: Reject
- Scores: 5, 3, 6, 3

## Abstract
We present a simple yet effective method to improve the robustness of both Convolutional and attention-based Neural Networks against adversarial examples by post-processing an adversarially trained model. 
Our technique, MeanSparse,  cascades the activation functions of a trained model with novel operators that sparsify mean-centered feature vectors. 
This is equivalent to reducing feature variations around the mean, and we show that such reduced variations merely affect the model's utility, yet they strongly attenuate the adversarial perturbations and decrease the attacker's success rate.
Our experiments show that, when applied to the top models in the RobustBench leaderboard, MeanSparse achieves a new robustness record of $75.28$% (from $73.71$%), $44.78$% (from $42.67$%) and $62.12$% (from $59.56$%) on CIFAR-10, CIFAR-100 and ImageNet, respectively, in terms of AutoAttack accuracy. 
Code: https://anonymous.4open.science/r/MeanSparse-84B0/

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a method called MEANSPARSE, which enhances the adversarial robustness of trained neural networks in a post-processing manner without compromising clean accuracy. The idea behind this method is to attenuate the reliance on non-robust features by modifying activation functions. Their experiments demonstrate a significant increase in the adversarial robustness of neural networks.

### Strengths
1. The idea of manipulating activation functions to enhance adversarial robustness is quite interesting.
2. Extensive experiments have been conducted to support the proposed method.
3. The intuition behind the idea is provided, making it easier to follow.
4. The paper includes a discussion of its limitations.

### Weaknesses
1. The explanation of the method in the Introduction is vague. On page 1, lines 37 and 44, you state: "In this work,..." twice, but the first sentence mentions "design of activation functions," while the second shifts to "sparsifying features to enhance robustness against adversarial attacks." These two sentences make it unclear what the key points of your work are and how investigating activation functions is related to sparsifying features. It would be better to provide a consistent expression for the main points and briefly describe the connection between them. I suggest a clear statement about your key contributions.

2. Lack of intuitive explanation of the proposed concept. On page 1, line 48, the proposed sparsity method "Mean-based Sparsification" is not well explained, and it’s followed only by a brief description of Figure 1. Without a clear explanation of the "sparsification operator", it is difficult to follow. I suggest adding a brief explanation of the "sparsification operation" you mentioned in line 90 and providing a concise mathematical definition or detailed description of how the sparsification operator works, perhaps with a simple example.

3. There are some writing errors in the paper. In Figure 2, "equation 3" appears at the end of the title, which is confusing. It would be better to remove it or rephrase the title.

### Questions
1. On page 6, in the first and second paragraphs, you mention two approaches and choose the second one. I am curious why you selected the second approach as your method. Is it superior? Can you provide evidence to support your choice and a brief comparison of the two approaches, highlighting the advantages and disadvantages of each?

2. In Section 4 on page 7, I did not find the experimental settings. You only mentioned that the experiments were conducted using an NVIDIA A100 GPU. For better reproducibility, it would be helpful to include detailed experimental settings. I suggest providing details such as the software versions used, hyperparameters, data preprocessing steps, and any other relevant configuration details that would allow others to replicate their experiments

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes a post-training method for enhancing the robustness of adversarially trained models. In particular, it inserts, at various layers, the MeanSparse modules which project the features (before activation) onto their mean computed over the training set if they are closer than a threshold to the mean itself. This has the goal of preventing an attacker from exploiting non-informative features to change the predicted class. In the experiments, several SOTA robust models are equipped with MeanSparse, which leaves clean performance unchanged while improving robustness.

### Strengths
- The proposed method is efficient, can be applied to any pre-trained model without additional training, and incurs in limited additional inference cost.

- The experiments include several architectures, datasets and threat models.

### Weaknesses
 - The main concern is about the possible presence of gradient masking. In fact, as mentioned in the paper, the MeanSparse operator induces zero gradients for the features which are projected. Since these are supposed to be the most common ones, and MeanSparse is applied in multiple points in the network, one can expect that the computed gradient might contain limited information, and thus the gradient-based attacks not work properly. While the paper tests black-box attacks, in this case the base model is (highly) robust, and the improvements given by MeanSparse are in the order of 1-3%, which might be of the same order or even smaller than the gap between white- and black-box (with standard query budget) attacks for the base model: then it is not clear that in this case this is sufficient to exclude gradient masking. A simple adaptive attack would consist in removing the projection operation when computing the gradient in the attacks, which would modify the backward pass of the model while preserving its predictions (a similar approach to BPDA). The fact that the projection is applied at multiple layers exacerbates this issue, as it could lead to a situation where gradients are effectively zeroed out across a significant portion of the network, severely hindering the effectiveness of gradient-based attacks. The evaluation should include a more rigorous analysis of the gradient landscape, for example by computing the norm of the gradient at different layers and comparing it with and without the MeanSparse module.

 - The discussion in Sec. 3.1 seems a bit disconnected from the final approach (also, $z_{k-1}$ in Eq. (7) is not defined).

### Questions
See above.

### Soundness
2

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
3

### Summary
This paper seeks to improve adversarial training by inducing sparsity in the features of an adversarially-trained model. To achieve this, MeanSparse blocks variations in features within a given distance of the mean, which is intended to lessen the importance of non-robust features during training. Before describing their sparsification method, the authors provide intuition as to how non-robust features can be removed during training through regularizad optimization. Here, a regularization term is included in the training objective which penalizes the $\ell_0$ norm of mean-centered learned features. In theory, this would remove small deviations from the mean which don't result in significant reductions in loss. Inspired by this intuition, the authors then propose a sparsification operator, which is applied during forward propagation and explicitly blocks variation within a given distance of the feature mean. Severel implementation challenges are then addressed. Experimental results show that integrating MeanSparse into state of the art image classifiers can significantly improve robustness with negligible impact on clean performance.

### Strengths
- The results show meaningful improvement in the robustness of SOTA adversarially trained models. Since this method can be applied post-training, it has the potential to lead to a significant jump across the board in standards for robustness to adversarial examples.
- The experimental section appears well designed. Results are presented for CIFAR-10, CIFAR-100, and Imagenet, and a representative variety of model architectures and adversarial attacks are tested.
- The method is also shown to be robust against adaptive attacks, as shown in Appendix A.4.
- I quite like the visualizations provided in Figure 1, they simply and effectively convey how MeanSparse operates.

### Weaknesses
 - The description of the MeanSparse technique is somewhat ambiguous to me. The term "feature" is often used, but never specifically defined. What features are being used here? Are you referring to input features? Activations of the final layer? Activations of some internal layer?
- I don't entirely agree with the provided intuition for blocking minor variations around the feature mean. Based off of the provided explanation, I would expect this approach to work when minor variations are blocked around high-probability feature values. However, it's not clear to me that the feature mean would always be a high-probability point.
- Appendix A.2 does provide results looking at $\ell_2$ bounded attacks, rather than $\ell_\infty$ bounded attacks. However, I think the topic of how MeanSparse performs against different threat models does warrant additional study. Threat models have been studied in which the adversary can introduce perturbations that are unbounded in $\ell_p$ space (i.e. [1]), and it is not obvious to me whether these types of attacks would have similar impacts on the distributions of features. If the claims made in this paper are limited to $\ell_p$ bounded attacks, I think that should be made explicit.

### Questions
- Is the feature mean always a high-probability point? I would imagine that in certain multimodal distributions the mean is actually unlikely to occur. Might this occur in practice?
- One component of MeanSparse involves calculating the mean and standard deviations of features. Can you provide more information regarding what data is used to calculate these values? Specifically, are these statistics computed on benign or adversarially perturbed data? 
- How sensitive is the feature mean to class imbalances in the training set? If classes aren't evenly balanced (assuming feature distributions are different for different classes), could that result in changes in feature means?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces MeanSparse, a novel post-training method designed to enhance the robustness of convolutional and attention-based neural networks. MeanSparse works by sparsifying mean-centered feature vectors. This technique effectively decreases the success rate of adversarial attacks by minimizing the exploitable feature variations. The paper demonstrates that MEANSPARSE improves the robustness on datasets such as CIFAR-10, CIFAR-100, and ImageNet.

### Strengths
1. The application of sparsification to mean-centered features is an innovative approach, as it targets non-robust features in a unique way.

2. Authors provide comprehensive results across multiple datasets and models

3. The paper is well-organized and clearly describes the underlying motivation, methodology, and results

### Weaknesses
1.  whether its effectiveness generalizes across different types of attention-based models, such as ViT?

2.  Could you provide provide an analysis of how MEANSPARSE's effectiveness scales with model size? Authors only apply their method on large networks, like wrs-70. How about the performance of the method on smaller network, like ResNet-18, Swin-Small?

3.  After reading the codes provided, I found that the MeadSquare will calculate the mean and var of the input data to get running_mean and running_var. I do no think the model should change its any parameters according to the test data.

4.  The number of baselines in this paper is too few. Authors do not compare their methods with other sparsity methods.

### Questions
1. Could the method be used for adversarial training and accumulate the running mean and running var during training? Then during testing, fix the running mean and var.

2. Could you provide a detailed analysis of how MEANSPARSE's effectiveness changes as the attack strength increases, like 16/255?

### Soundness
3

### Presentation
3

### Contribution
3
