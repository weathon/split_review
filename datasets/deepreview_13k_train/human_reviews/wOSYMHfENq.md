# Batch normalization is sufficient for universal function approximation in CNNs

- Decision: Accept
- Scores: 5, 8, 3, 8

## Abstract
Normalization techniques, for which Batch Normalization (BN) is a popular choice, is an integral part of many deep learning architectures and contributes significantly to the learning success. We provide a partial explanation for this phenomenon by proving that training normalization parameters alone is already sufficient for universal function approximation if the number of available, potentially random features matches or exceeds the weight parameters of the target networks that can be expressed. Our bound on the number of required features does not only improve on a recent result for fully-connected feed-forward architectures but also applies to CNNs with and without residual connections and almost arbitrary activation functions (which include ReLUs). Our explicit construction of a given target network solves a depth-width trade-off that is driven by architectural constraints and can explain why switching off entire neurons can have representational benefits, as has been observed empirically. To validate our theory, we explicitly match target networks that outperform experimentally obtained networks with trained BN parameters by utilizing a sufficient number of random features.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides a proof that a convolutional multi-layer perceptron with batch normalization is an universal function approximator even when only the batchnorm parameters are trainable and everything else is fixed to its random initialization.
The claim is proved by providing a practical construction for a number of common activation functions and parameter random distributions.

Minimum model widths and depths are provided for the task of reproducing an arbitrary convolutional MLP.

The approach is validated by experiments on image classification of the CIFAR10 and CIFAR100 datasets.

### Strengths
Interesting theoretical contribution.

### Weaknesses
Unclear practical relevance. The contribution is marginal compared to known results about approximation with models with random fixed parameters. The paper does not sufficiently address the limitations of only training batch normalization parameters, particularly in scenarios where the initial random weights are not well-suited for the target function. While the theoretical construction is interesting, the paper lacks a clear explanation of how these specific architectural constraints translate into tangible improvements in real-world applications beyond the provided experiments. The experiments themselves, while demonstrating the theoretical claim, do not explore the practical limitations of the approach, such as sensitivity to the random initialization or the computational cost of the required network width and depth.

### Questions
N/A

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
They provide explanation for the normalization by proving that training normalization layers alone is already sufficient for universal function approximation if the number of available, potentially random features matches or exceeds the weight parameters of the target networks that can be expressed.

### Strengths
1- The effectiveness has been well supported by experiments.

2- Well organized and clearly written.

3- The paper is appropriately placed into contemporary literature.

### Weaknesses
I read the whole paper excluding the appendix, I acknowledge the importance of their study and appreciate the detailed information.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper shows that, under certain conditions, training just the batch normalization (BN) parameters is enough to make a CNN a universal function approximator.

### Strengths
The paper practices experimental method really well (has hypothesis, describes experiments and shows results).

### Weaknesses
 The work describes BN as a subset of a Layer Normalization (LN).
I'd note that they are both normalization layers, but BN is NOT a type of LN.
(I'm effectively rejecting the paper because it needs to be rewritten based on this)

BN, LN, GroupNorm, etc are all normalization layers, the only difference is the dimension along which normalization is done; GroupNorm (https://arxiv.org/abs/1803.08494) paper has a pictorial depiction of this.
Furthermore, given BN aggregates statistics across samples, the neural network (NN) output of BN changes if the set of images changes; during training this makes a NN with BN a statistical operator. LN operates within a sample; the NN output does NOT change depending on input samples; during training this makes a NN with LN a function (not statistical). The Online Normalization paper (https://arxiv.org/abs/1905.05894) does a good job talking about this.



- Reference are broken (there are things like "Theorem ??" in the paper).
- Paper's experiments are really small scale for modern Deep learning leaving the reader wondering if they will scale.

### Questions
-

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper explores the role of normalization techniques, particularly Batch Normalization (BN), in deep convolutional neural networks (CNNs). The authors provide a theoretical analysis to demonstrate that training normalization layers alone is adequate for universal function approximation, assuming a sufficient number of random features. This result applies to various CNN architectures, including those with or without residual connections and different activation functions, such as ReLUs. The authors also explain how this theory can elucidate the depth-width trade-off in network design and the empirical observation that disabling neurons can be beneficial.

### Strengths
- The paper provides a solid theoretical foundation for its claims, offering mathematical proofs and a well-structured argument.

- This paper is written in a clear and easily comprehensible manner, making it easy for readers to follow.

### Weaknesses
 - In the introduction, I'm a bit confused about the normalization being explored in this paper. The title mentions batch normalization, but the statement "we delve into the role of layer normalization" suggests layer normalization. Is this a typo?

- I'm puzzled by the assertion in Section 2 regarding the existence of $f_t$, which the author claims is due to the universal function approximation. Perhaps the author meant to refer to the Universal Approximation Theorem. However, such approximations in neural networks are typically conditional. Has the author considered these conditions? Generally, these conditions are not mild and are idealized. Does this affect the theory presented in this paper? The author should provide an explanation and discussion on this.

- I'm not entirely sure why throughout the paper, normalization is reduced to just a linear transformation and shift, i.e., $\gamma \mathbf{h} + \beta$. This includes batch norm, layer norm, instance norm, etc. They all have this form, so is their significance solely in the learnable parameters $\gamma$ and $\beta$? Of course, I understand that $[(x - \mu) / \sigma] \times \gamma + \beta$ can be equivalent to $\gamma \mathbf{h} + \beta$" in the end, but why emphasize batch normalization in the title? Where does "batch" come into play?

- Can the analysis apply to the existing advanced batch normalization improvements like IEBN [1] and SwitchNorm [2]. These missing works should be considered and added to the related works or analysis.

- The author needs to clarify the above questions. If these issues are addressed, I will consider these clarifications along with feedback from other reviewers in deciding whether to raise my score.

### Questions
- In the introduction, I'm a bit confused about the normalization being explored in this paper. The title mentions batch normalization, but the statement "we delve into the role of layer normalization" suggests layer normalization. Is this a typo?

- I'm puzzled by the assertion in Section 2 regarding the existence of $f_t$, which the author claims is due to the universal function approximation. Perhaps the author meant to refer to the Universal Approximation Theorem. However, such approximations in neural networks are typically conditional. Has the author considered these conditions? Generally, these conditions are not mild and are idealized. Does this affect the theory presented in this paper? The author should provide an explanation and discussion on this.

- I'm not entirely sure why throughout the paper, normalization is reduced to just a linear transformation and shift, i.e., $\gamma \mathbf{h} + \beta$. This includes batch norm, layer norm, instance norm, etc. They all have this form, so is their significance solely in the learnable parameters $\gamma$ and $\beta$? Of course, I understand that $[(x - \mu) / \sigma] \times \gamma + \beta$ can be equivalent to $\gamma \mathbf{h} + \beta$" in the end, but why emphasize batch normalization in the title? Where does "batch" come into play?

- Can the analysis apply to the existing advanced batch normalization improvements like IEBN [1] and SwitchNorm [2]. These missing works should be considered and added to the related works or analysis.

- The author needs to clarify the above questions. If these issues are addressed, I will consider these clarifications along with feedback from other reviewers in deciding whether to raise my score.


[1] Instance Enhancement Batch Normalization: An Adaptive Regulator of Batch Noise, AAAI

[2] Differentiable Learning-to-Normalize via Switchable Normalization, ICLR

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
