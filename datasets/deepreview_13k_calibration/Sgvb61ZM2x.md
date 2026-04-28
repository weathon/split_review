# Effective Learning by Node Perturbation in Deep Neural Networks

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Backpropagation (BP) is the dominant and most successful method for training parameters of deep neural network models. However, BP relies on two computationally distinct phases, does not provide a satisfactory explanation of biological learning, and can be challenging to apply for training of networks with discontinuities or noisy node dynamics. By comparison, node perturbation (NP) proposes learning by the injection of noise into the network activations, and subsequent measurement of the induced loss change. NP relies on two forward (inference) passes, does not make use of network derivatives, and has been proposed as a model for learning in biological systems. However, standard NP is highly data inefficient and unstable due to its unguided, noise-based, activity search. In this work, we investigate different formulations of NP and relate it more directly to the concept of directional derivatives as well as combining it with a de-biasing mechanism for layer outputs. We find that a closer alignment with directional derivatives, and induction of decorrelation of node outputs significantly enhance performance of NP learning making it competitive with BP.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors present an approach to improve the efficiency and stability of node perturbation (NP) as an alternative, biologically plausible method to backpropagation (BP) for credit assignment in deep neural networks. Their main contributions include reframing NP in terms of computing directional derivatives and proposing a decorrelation procedure to mitigate input bias. Specifically, they suggest using a decorrelation matrix initialized as the identity matrix and subsequently updated to reduce correlations. For gradient approximation, they perturb one layer at a time using a noise vector, measuring the resultant change in loss, and thereby estimating the gradient respective to each layer.

### Strengths
**Novelty in Approach**: The manuscript's primary strength lies in its enhancement to NP by directional derivatives calculated from neural activity measurements. This offers a fresh lens to potentially harness NP more effectively in deep learning contexts -- perhaps also spur methods utilizing a hybrid NP_noise and NP_activity update.

**Clarity in Gradient Approximation**: The iterative node perturbation method introduced offers a transparent and logical pathway to approximate gradients. By perturbing one layer at a time and measuring the resultant loss changes, the approach provides both intuition and efficacy in gradient estimation.

### Weaknesses
 **Learning Rate Optimization**: The approach to learning rate optimization might introduce inadvertent biases. By optimizing the learning rate specifically for NP and then using this optimized rate for BP without independent optimization, the results might not reflect the accurate comparison with BP. This is further underscored by references like Hiratani et al., which hint at nuances between NP and BP at different learning rates. It is crucial to ensure that each method is evaluated at its respective optimal learning rate to avoid skewed comparisons. The paper does not provide sufficient detail on how the learning rate optimization was performed for each method, raising concerns about the validity of the comparative results.

**Concerns Over Biological Plausibility**: The introduction of the decorrelation mechanism, while effective, does raise eyebrows regarding its biological realism. If the overarching goal of the research is to be in harmony with biologically plausible learning paradigms, then not sure how the decorrelation step fits in. The paper should address the biological plausibility of this decorrelation mechanism, perhaps by discussing potential biological counterparts or limitations of the approach.

**Ambiguous Visual Interpretation**: Interpretation of Figure 2 seemed ambiguous to me. With training curves of three methods appearing quite similar without decorrelations, the clarity of conclusions derived becomes muddied. The paper needs to provide a clearer explanation of the significance of the results in Figure 2, particularly regarding the ranking of different NP methods. The lack of clear performance differences makes it difficult to discern the advantages of the proposed activity-based method over the iterative and noise-based methods.

**Scope Limitation with Network Types**: The research seems to overlook certain types of networks, notably the absence of comparisons for NP iterative in convolutional networks on established benchmarks like CIFAR100. The study would benefit from an evaluation of the proposed methods on convolutional networks, as these are widely used in deep learning applications. The absence of results on CIFAR100 and other standard benchmarks limits the generalizability of the findings.

**Formatting and Implementation Details**: The paper contains formatting discrepancies, notably in equation numbering. Such inconsistencies can be distracting and hinder smooth comprehension. Additionally, the omission of granular details about the implementation, such as the underlying framework, time metrics, and codebase accessibility.

### Questions
1. Do the authors plan to release the code base? If so, could you please share the link to an anonymized repository?

2. What exactly does figure 2 convey? The authors say “ranking” is important here – for layer 2 NP iterative is slightly better, whereas for output NP activity is slightly better. Overall it’s difficult to see what should be the conclusion since the training curves for these 3 methods without decorrelations is very similar. 

3. Grid search for learning rate optimization – lr is optimized for NP, and then BP is trained with this lr. Hiratani et al. have shown that NP approximates BP in low lr – for a fair comparison of the learning curves, BP curve should be for LR optimal for that? Also, the variance in performance with multiple seeds, across learning rates will be good to see. How does this scale with the network architectural parameters, such as the depth and width of a fully connected network?

4. Hiratani et al. have also shown that NP is unstable in higher learning rates, did you observe “crashes” in training – where the accuracy suddenly falls to chance? It would be interesting to see whether decorrelations help with this.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies node perturbation (NP), i.e. a category of learning algorithms that are different from BP, potentially more biologically-plausible, and possibly more suitable for efficient learning hardware, especially for noisy electronics. The work here formulates NP into a version that approximates directional derivatives with respect to a layer's activation, and also combines it with a method that decorrelates the activity among the neurons of a layer, resulting in faster and more stable learning.

### Strengths
The work is in an interesting field, namely that of alternative learning algorithms to backpropagation.

The paper is quite nicely written, making the reasoning for the design choices easy to follow.

The results seem potentially very useful to NP, stabilising and speeding up the learning process.

### Weaknesses
The work is only relevant to the niche of node perturbation, as the paper fails to contextualize the work more broadly, with literature review, experimental comparisons or otherwise.

The paper does not cite the state of the art (SOTA) within the NP subfield (Mengye Ren et al., ICLR 2023).

The methods that were used in that NP SOTA have not been incorporated in the experiments here, so it is hard to evaluate whether the advantages seen here could be combined with the previously seen progress in NP.

The authors do not cite any of the multiple other bio-plausible alternatives to BP than NP. The SOTA in such alternatives actually outperforms NP and is arguably more plausible and suitable for hardware (Journé et al., ICLR 2023).

The test accuracies reported here are significantly lower than that SOTA, and tests in more advanced datasets than CIFAR 100 have not been performed.

The paper's abstract concludes "making it competitive with BP", but this seems heavily exaggerated based on the actual demonstrations.





### Questions
Could the authors comment on the efficiency and the biological plausibility of the decorrelation method?

Similarly, how could the other aspects of the method be implemented in the brain?

For example, how could the "clean" (sic) version of the output be obtained in the brain, as it assumes the absence of noise?

Does the claim of the paper about suitability of noisy hardware hold, under the assumption of a clean forward pass?

How plausible is it biologically that for each training example, multiple forward iterations are needed before the full update? It seems that hundreds of such iterations were necessary in the simulation.

How energy efficient would this be in a hardware implementation? It seems to me that it would also increase the energy consumption by orders of magnitude.

The paper mentions that the convolutional architecture was very shallow. Why couldn't it be scaled up?

I could not find an experiment showing the impact of the decorrelation method on the results. Was it implemented in all versions of NP experiments?
Also, was it (or any other decorrelation method) used in experiments with backprop? Otherwise, could the authors comment on whether comparisons are fair?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper is about the node-perturbation approach to training artificial neural networks. The main claimed contributions of the paper are 1) reformulating the node perturbation (NP) methods in terms of directional derivatives (NP-iterative, section 2.1.2), and providing a simpler implementation (NP-activity, section 2.1.3) and 2) a decorrelation method (sec 2.2) applied on the input of each layer to speed up the convergence of training of node perturbation methods. The theory is then tested on classification tasks (CIFAR-10 and 100) with multi-layer perceptrons of three hidden layers (Sec 3.1, 3.2), and on convolutional networks (sec 3.3). An extension is also proposed based on two noisy forward passes instead of one clean and one perturbed pass (sec 3.4).

### Strengths
Strengths:

- **Clarity**. The paper is clearly written, and easy to follow. The concepts are well-explained, and the paper hierarchy is clear.

- **Ambition**. The paper is ambitious about the proposed method and test it only on more difficult benchmarks, CIFAR-10 etc, but it turns out to be also a weakness in this case (see weaknesses).

- **Importance**. The problem of finding alternatives to BP is important to reduce the energy cost of deep learning.

### Weaknesses
I see two main weaknesses:

- **Awareness of prior work**. The contribution of linking perturbations of forward passes to directional derivatives is not really a new contribution, it has been done before in e.g. [1], which I expected to see cited since it is extremely related. The activity-based updates can be thought of as a finite difference implementation of this approach. More generally, linking forward pass to directional derivatives means dealing with forward-mode differentiation, while BP is reverse-mode. Reverse mode is efficient because of the regime many-parameters/scalar loss, and forward mode is all the more inefficient if done exactly, hence the use of noise to probe multiple directions at once and make it more efficient, at the cost of more variance. It would be nice if the authors place their work clearly in this picture, and clarify their contributions after better literature review. The authors should also discuss the limitations of using finite difference approximations for directional derivatives, especially in high-dimensional spaces where the choice of perturbation magnitude can significantly impact the accuracy of the gradient estimate. Furthermore, the connection to other methods that use noisy gradients, such as those based on evolutionary strategies, should be explored to better position the proposed approach within the broader landscape of gradient-free optimization techniques.


- **Overfitting**. The decorrelation approach proposed in this work does help for training accuracy, but leads to massive overfitting compared to BP (Fig 3 and 5). I think this is very concerning since achieving small training error is not the hard part of training neural networks, what really matters is the held-out error. It is known e.g. that BP with SGD has an implicit bias that enables the network to generalize [2], and somehow the decorrelation method suppresses this bias, which is interesting. I think this important point should be addressed/solved by this submission. Maybe the authors should try to vary the amount of decorrelation to see whether it affects overfitting. For now, the claim in the abstract that decorrelation makes NP learning competitive with BP is not backed by the data given the overfitting. The authors should investigate the effect of the decorrelation method on the effective rank of the weight matrices, as this could provide insights into the loss of generalization. Additionally, exploring regularization techniques, such as weight decay or dropout, in conjunction with the decorrelation method could help mitigate the overfitting issue. The authors should also provide a more detailed analysis of the training dynamics, including the evolution of the training and validation losses over time, to better understand the source of the overfitting.

### Questions
Questions:

- How do the angles reported in Fig 2 evolve during learning? Do they become more aligned or less aligned?

- Why use the squared error loss when doing classification? Why not the cross-entropy loss? I can understand why the authors wanted to only use CIFAR-10/100 because these tasks are more difficult than MNIST or Fashion MNIST, but in this case it could be valuable to add experiments on MNIST to see whether the findings are the same regarding overfitting.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors combine the node perturbation (NP) algorithm with an activity decorrelation method and better gradient estimation to improve NP's performance.

### Strengths
1. The paper does a good job introducing note perturbation (NP), along with its motivation and caveates. 
2. The combination of the decorrelation method and NP is novel and speeds up training in some cases.
3. These ideas might be applied in other settings where learning is easier; e.g. weight perturbation was applied to finetuning LLMs https://arxiv.org/pdf/2305.17333.pdf

### Weaknesses
My main issue with the paper is that NP still performs very poorly, even with decorrelation (NP-D), and doesn't match backprop. The results do not justify the last line of the abstract, which says
> significantly enhances performance of NP learning making it competitive with BP.

Fig. 3 shows that with early stopping NP-D can slightly outperform NP, but the gap between the best performance for those two methods is smaller than the gap between BP and NP-D. Fig. 5 looks a bit more favourable, but NP-D still performs much worse than BP. Both figures show experiments on shallow networks, so it's reasonable to expect the gap will widen for deeper networks due to NP incorrectly estimating gradients. The core issue is that while decorrelation improves training speed, it doesn't address the fundamental problem of NP's inaccurate gradient estimation, which is especially problematic in deeper networks where errors can accumulate.

In addition, both Fig. 3 and Fig. 5 show that NP-D results in a very large, much larger than for ND, generalization gap. This suggests that while NP-D might be optimizing the training objective, it is overfitting to the training data, and the decorrelation method does not seem to mitigate this issue. The large generalization gap is a significant practical concern, as it limits the real-world applicability of the method.

The experiments are also rather limited: it's only two very similar datasets, and only shallow architectures. Convnets are also not used for cifar10 -- a few conv layers trained with BP can perform much better than ~56% with small MLPs, so seeing how NP-D performs there would be helpful. The lack of convolutional network experiments on CIFAR-10 is a significant oversight, as it prevents a thorough evaluation of the method's performance on a more complex and realistic task. Furthermore, the similarity of the two datasets used raises questions about the generalizability of the findings.

### Questions
Why is everything trained for so many epochs? 2000 epochs is a lot, and backprop should normally converge to very good performance on cifar10 within the first few dozen epochs. But here it takes hundreds. 

Beginning of page 2:  weight propagation (WP) -> perturbation?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
