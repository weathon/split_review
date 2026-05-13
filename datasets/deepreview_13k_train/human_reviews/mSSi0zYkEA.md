# Initializing the Layer-wise Learning Rate

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
The standard method to assign learning rates has been to rely on the optimizer and to use a single, global learning rate across all its layers. We propose to assign individual learning rates as well, according to the layer-wise gradient magnitude at initialization. Even if individual layers are initialized to preserve gradient variance, architectural characteristics result in uneven gradient magnitude even when the network has not started training. We interpret this gradient magnitude as a measure of architecture-induced convergence bias, and adjust the layer-wise learning rate opposite to its gradient magnitude at initialization. This relative learning rate is maintained throughout the entire training scheme. Experiments on convolutional and transformer architectures on ImageNet-1k show improved accuracy and training stability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focused on the problem about initialization method of layer-wise learning rate. The authors use gradient magnitude as a
measure of architecture-induced convergence bias. Based on that, they try to adjust the layer-wise learning rate opposite to its gradient magnitude at initialization. The experimental results illustrate that the proposed initialization method can obtain a better performance on CIFAR, ImageNet.

### Strengths
1. This paper focus on an important problem. In my past experience about neurwal network training, layer-wise learning rate is very sensitive to the initialization method of each layer. For example, LAMB use the ratio between weight norm and gradient norm to determine the layer-wise learning rate. 
2. The proposed method is very easy to understand. We can estimate gradient magnitude and then determine the layer-wise learning rate.

### Weaknesses
 1. I'm not sure whether the proposed method can scale. Although the proposed method and intuition are easy to understand, the method is still not simple enough. So that make me consider the performance when we scale to a very large model, such as a language model, and whether this can be a general method. I know this is very difficult and I'm just considering. If possible, you could provide some results on NLP task. 
 2.  You need to compare the proposed method with more layer-wise optimization method, such as LARS and LAMB. I noticed that the main baseline is SGD and Adam. and these methods are not layer-wose methods. Although their performance is very strong, I think LRAS / LAMB can also further improve the performance of SGD / Adam. To better illustrate the performance gain of your method, maybe you should provide these results on layer-wise method.

### Questions
1. I would like to ask the training cost of Algorithm 1. Since the method need to estimate the gradient magnitude and other methods don't need it. Therefore, I would like to ask the cost, such as time. In addition, the proposed need to use T steps in Algorithm 1 and that means we need more steps to finish the training with the proposed method. If we add these T steps to the baselines, such as SGD and Adam, whether we can further improve their performance?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a systematic layer-wise learning rate adjusting scheme according to the layer-wise gradient magnitude at initialization, improving training performance and stability on convolutional and transformer architectures. Competitive results on convolutional and transformer architectures on CIFAR100 and ImageNet-1k validate the proposed hypothesis.

### Strengths
The method is easy to understand.
The experiment results are convincing, removing the fluctuations and improving accuracy.

### Weaknesses
1. Lots of typos and confusing statement. Such as "Figure 7: Train loss for 2-layer MLP trained on CIFAR-10 trained.", Sec.2: "Another direction previous works indirectly modified the learning rate is through the use of scale factors..." The writing needs a thorough revision for clarity and accuracy. The example given for Figure 7 is particularly problematic, as it seems to describe a different experiment than what is presented. The statement in Section 2 is also confusing and lacks specific examples of the 'scale factors' being referenced, making it difficult to understand the context.
2. In Algorithm 1, the reason of choice of T and corresponding ablation study is missing which may be vital to the performance of the proposed algorithm. The lack of justification for the hyperparameter T is a significant oversight. Without an ablation study, it's impossible to determine the sensitivity of the algorithm to this parameter and whether the chosen value is optimal or arbitrary. This undermines the robustness of the proposed method.
3. The novelty is limited; more theoretical analyses are needed. The method appears to be an incremental improvement over existing layer-wise learning rate adjustment techniques. A more in-depth theoretical analysis is needed to justify the approach and demonstrate its unique contribution beyond empirical observations. This would involve explaining why the proposed method works and under what conditions it is expected to be most effective.
4. Related works are not clear enough. The paper does not adequately discuss how the proposed method relates to existing techniques for layer-wise learning rate adjustment. A more comprehensive discussion of related works is needed to clarify the novelty and contribution of the proposed method.

### Questions
1. What is the motivation of proposed Algorithm 1?
2. Why layer-wise learning rate scheme performs not so good on Swin-T and ConvNeXt-T when using AdamW? ResNet-50 and SGD are no longer mainstream models or algorithms in 2023. What are the impacts of proposed algorithms on different model structures and modules?
3. Figure 6 is not intuitive, even seems that single way is better than proposed methods.
4. More ablation studies are needed to validate the influence of different hyper-parameters in Algorithm 1.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method to assign a learning rate to each layer. This layer-wise learning is computed by using the norm of the backpropagated gradients. Basically, the learning rate of assigned to a layer $l$ is inversely proportional to the square root of the $\mathcal{L}^1$-norm of the backpropagated gradient (according to the tensor of weights of $l$).

To evaluate their heuristic, the authors run two series of experiments: one with a single learning rate, and one with their heuristic. The tested setups include two optimizers: SGD and AdamW. In each tested case, the reported performance is greater with their method than with theit single learning rate counterparts.

### Strengths
## Originality

To my knowledge, the proposed heuristic for a layer-wise learning rate is new.

## Clarity

Overall, the proposed method is easy to understand.

## Quality

The authors have well explained (introduction of Section 3) why one should look for a working and well-justified heuristic for layer-wise learning rates, computed *before* training. This problem deserves to be studied, both from a practical and a theoretical point of view.

The experimental results are very encouraging.

### Weaknesses
## Clarity

The idea behind Algorithm 1 is easy to understand, but several details are missing or seem to be erroneous:
 * line 4: replace $n$ by $t$;
 * apparently, the $G_i$ are incremented $T$ times, but they are not normalized by $T$ or any other quantity depending on $T$. So, two questions arise: how do we choose $T$? Or should we normalize the $G_i$ somewhere?

More importantly, many choices in Algorithm 1 are not explained by the authors:
 * line 8: why do the authors use the $\mathcal{L}^1$-norm over $\mathbf{g}$, and not the $\mathcal{L}^2$-norm or any other norm? The choice of the $\mathcal{L}^1$-norm seems arbitrary without a theoretical justification. Using the $\mathcal{L}^2$-norm would be more standard in the context of gradient-based optimization, as it relates directly to the magnitude of the gradient vector. This choice significantly impacts the computation of the layer-wise learning rates and needs a more thorough explanation.
 * line 10: why choosing the inverse of the square root of $G_i$, and to the inverse of $G_i$ or any other quantity? The relationship between the learning rate and $G_i$ is defined as $\eta_i = \eta \cdot \frac{1}{\sqrt{G_i}}$, but the reasoning behind using the inverse square root is not provided. It would be beneficial to understand how this specific function was derived and what its implications are for the learning process.
 * lines 11-13: what is the justification for such a computation? These lines describe a normalization step, but the rationale behind this specific normalization method is unclear. It is essential to understand why this particular normalization is necessary and how it affects the overall performance of the algorithm.

Overall, Algorithm 1, which describes the entire method proposed by the authors, is incomplete and lacks justification. This crucial weakness can be solved by adding subsections in Section 1, proving mathematically all the choices made in Algorithm 1 (at least in simple cases). Otherwise, these choices remain arbitrary.

### Questions
Could the authors provide at least a short analysis of their method in simple cases, or in extreme cases (layer size tending to infinity)? It would be interesting to observe what happens at the first training step.

What do the authors think about the paper *Neural tangent kernel: Convergence and generalization in neural networks*, Jacot et al., 2018? In this paper, each weight tensor is scaled by $1/\sqrt{f_{\text{in}}}$. This setting, combined with a unique learning rate for all layers, is equivalent to the "normal" setting (without scaling) with a learning rate per layer, proportional to $1/f_{\text{in}}$. How the learning rates computed by the authors compare to these?

Experimental results: are the results consistent when we change the learning rate? Does the proposed method perform better than the "single lr method" in any circumstance?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to set learning rates for each parameter individually in neural networks.
These learning rates are computed from the reciprocal of the gradient magnitude for each parameter at initialisation time.
Experiments on ImageNet and CIFAR-100 show promising results that confirm the hypothesis that learning rate initialisation can speed up training significantly.

### Strengths
- (clarity) The method and results are presented clearly.
 - (significance) Speeding up SGD with a simple learning rate initialisation could be a cost-effective alternative to adaptive optimisation algorithms.

### Weaknesses
 - (clarity) Layer-wise learning rates, which are probably also addressed in the first edition of tricks of the trade (1998), were probably the only way to make deep networks trainable.
   The main advantage of adaptive optimisers has always been that the painfull process of finding learning rates for each layer is no longer necessary.
 - (clarity) It is unclear how important the choice for $T$ in algorithm 1 is.
   In the experiments, $T$ is the number of batches in one epoch, but there are no ablations for different choices of $T$. 
 - (originality) This paper fails to mention its relation to Adagrad (Duchi et al., 2011).
   This is especially relevant because Adagrad can also be interpreted as dividing the learning rate by a running average of the norm.
 - (originality) Algorithm 1 looks a lot like running an adaptive optimiser with a learning rate of zero for a number of mini-batches.
   This connection is completely ignored in the current manuscript.
 - (quality) In this work, the hyper-parameters seem to be shared for the different methods.
   For a proper comparison, hyper-parameters should be tuned for each method individually.
 - (significance) The inspection of the assigned learning rates seem to provide more information about the model than about the method.
   I think these could provide more information when compared to the learning rates of adaptive optimisation algorithms.
 - (significance) The experimental setup is too complex to properly evaluate the merits of the proposed method.
   By evaluating on these large models, confounding factors like learning rate schedules become necessary, making it hard to evaluate the generality of the method.
   Furthermore, these large models typically make it impractical to provide error bars and establish the statistical significance of the presented results.

### Questions
1. Please, rewrite the motivation to better reflect the historical evolution of adaptive optimisation methods.
 2. How does this method relate to Adagrad and other adaptive optimization methods?
 3. Is it possible to include simple experiments (cf. Kingma et al., 2015) with error bars?
 4. How much does the learning rate schedule affect the performance of the proposed method?
 5. Is it possible to include a run where Adagrad (or other adaptive methods) iterates the data for one epoch with learning rate zero.
 6. How does the setting above compare to the baseline performance and the proposed layer-wise learning rate?
 7. How important is the choice for $T$ and does this relate in some way to learning rate warmup?
 8. Can you tune the hyper-parameters (most notably the learning rate) for each algorithm individually to provide a fair method comparison?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
