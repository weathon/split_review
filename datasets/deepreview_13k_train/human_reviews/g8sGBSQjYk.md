# On the Parameterization of Second-Order Optimization Effective towards the Infinite Width

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Second-order optimization has been developed to accelerate the training of deep neural networks and it is being applied to increasingly larger-scale models. In this study, towards training on further larger scales, we identify a specific parameterization for second-order optimization that promotes feature learning in a stable manner even if the network width increases significantly. Inspired by a maximal update parameterization, we consider a one-step update of the gradient and reveal the appropriate scales of hyperparameters including random initialization, learning rates, and damping terms. Our approach covers two major second-order optimization algorithms, K-FAC and Shampoo, and we demonstrate that our parameterization achieves higher generalization performance in feature learning. In particular, it enables us to transfer the hyperparameters across models with different widths.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors derive scaling laws for two second-order optimization methods (K-FAC (Martens & Grosse, 2015) and Shampoo (Gupta et al, 2018)), based on the muP approach from (Yang & Hu, 2021). This approach has previously been used for first-order methods, including with momentum. It is used to determine how the weight initialization and per-layer learning rate for deep neural networks should scale based on layer width. This allows 'parameter transfer', where good hyperparameters can be trained on small networks and suitably scaled up for wider networks. The derived scalings are successfully tested on some simple example problems.

### Strengths
This is a new application of the muP framework to a useful class of methods. I think the new scaling laws are useful and beneficial to the community. The authors apply a successful approach for deriving scaling laws to the case of specific second-order networks. The results are clearly stated and yield new insights into the merit of existing choices of damping parameter for K-FAC, and the use of zero initial weights for the last layer. The paper is reasonably clearly written and the presented experiments thorough.

### Weaknesses
I found the mathematical presentation fairly informal, both in terms of the exposition of the approach (Prop 4.1 has "the optimization becomes valid for...", for example) and the actual derivation in Appendix A. This is a presentational comment, not a critique of the correctness of the work. 

Theory is only given for least-squares losses, although the numerics suggest the results hold for other losses. If the authors could derive these laws - and Appendix A seems to suggest it might not be a huge piece of work - this would help the paper. 

While the empirical results show merit, their real benefit would only be clear if applied for larger-scale networks than those tested. I understand the practical issues around doing this and recognize that it isn't feasible for all researchers, but those results would strengthen the paper.

### Questions
To me, it appears that the extent of the theoretical contribution is not huge (largely based on combining existing methods), and I take the main benefit of the paper to be the actual derived scaling laws (i.e. choices of $a$, $b$, $c$, etc) rather than the overall approach/techniques.  Does this work introduce any new theoretical results/mathematical techniques of wider interest/applicability, or is the theoretical approach quite restricted to the specific methods being considered?

=========== AFTER REBUTTAL ===========
The new version of the work includes a mild strengthening of the mathematical formatlity in Appendix A, plus new results deriving scaling laws for layer-wise Gauss-Newton and other loss functions such as cross-entropy. This I think improves the paper by showing that their adaptation of muP to second-order methods yields a systematic approach rather than needing ad-hoc approaches, giving it wider interest.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper is a continuation of [1] in the context of second-order optimization. The initial idea consists in tuning simultaneously several hyperparameters (HPs) related to neural network (NN) training based on the following heuristic: after one training step, the pre-activations of each layer should have made a move of order $1$. More specifically, this heuristic should hold when the number of neurons of each layer tends to infinity. In order-$1$ optimization, the HPs include: variance of the initialization distribution of the weights, scaling of the weights, scaling of the learning rate. In the present work, the authors propose to tune the HPs specific to order-$2$ optimization, such as the damping parameters.

In practice, the authors focus on two order-$2$ optimization techniques (K-FAC and Shampoo), and test experimentally their heuristic with multilayer perceptrons (MLPs), convolutional NNs (CNNs) and ResNets. The authors find out that their method leads to better test losses, especially for NNs with very large layers. Moreover, one choice of learning rate seems to lead to results stable w.r.t. the size of the layers.

[1] *Tensor programs IV: Feature learning in infinite-width neural networks*, Yang and Hu, 2021.

=== Edit ===
I acknowledge the other reviews and the authors' answers. I keep my rating (8: Accept).

### Strengths
## Originality

Generalizing the heuristic of [1] to second order methods is new.

## Clarity

Overall, the paper is clear for a reader who is already aware of the works of Greg Yang (see [1]). 

## Quality

* This work is technically correct.
* The initial heuristic is tested (Fig. 1): $\Delta h$ behaves as expected when using $\mu \mathrm{P}$.
* In order to compare fairly $\mu \mathrm{P}$ with SP, the authors have performed a sanity check (Fig. 5): the results are stable for a wide range of learning rates.
* The experiments show that $\mu \mathrm{P}$ is better than SP, especially when the number of neurons per layer tends to infinity. This result was expected and is explained by the "infinite width limit assumption".

### Weaknesses
## Section 5.2 and Figure 6

There is a mix of lack of clarity and unconvincing results in this section.

First, the authors claim in Section 5.2 that $\mu \mathrm{P}$ allows better "transfer" of learning rate than SP. The term "transfer" is not so clear to me, but apparently, it means that the optimal learning is stable by width change. But, when looking at Figure 6, this is barely true: actually, the transfer is better with K-FAC SP than with $\mu \mathrm{P}$ in the MLP case. More specifically, the optimal learning rate for K-FAC SP with a width of 16384 is within the range of optimal learning rates for smaller widths, which is not the case for $\mu \mathrm{P}$. For $\mu \mathrm{P}$, the optimal learning rate seems to shift towards smaller values as the width increases, indicating that the learning rate is not truly transferable across different widths.

Second, in the legend of Figure 6, the authors claim something else: according to the context, "transferring the learning rate" means that, with a fixed l.r., the results get better and better as the width of the layers increases. This claim is more convincing, but differs substantially from the claim provided in Section 5.2. While the performance does improve with increasing width for a fixed learning rate, the optimal learning rate itself is not stable, which contradicts the initial claim about transferability in Section 5.2.

## Significance

The narrowness of the focus on K-FAC and Shampoo is a limitation of this work. What do the authors think about Newton, Gauss-Newton and generalized Gauss-Newton? 

Besides, the results presented in Table 1 are somewhat disappointing: basically, the usual NTK scaling corresponds to $\mu \mathrm{P}$ for all the hidden weights, in all the settings (SGD, Shampoo, K-FAC). The only difference lies in the input and output weights. Naturally, the authors cannot do anything about that.

### Questions
What do the authors think about apply $\mu \mathrm{P}$ to other second order methods, such as Newton, Gauss-Newton and generalized Gauss-Newton? 

Could the authors clarify the meaning of "transferring the learning rate" in Section 5.2 and in Figure 6, and clarify the claims of the corresponding paragraphs?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers finding the optimal hyperparameters for two second-order methods KFAC and Shampoo when training a neural network with a large width or when the width is infinite. These hyperparameters include the learning rate and the initialization hyperparameters. This optimal setting could help the network to learn features in a stable manner. This work is built upon the previous works that find the optimal setting for the first-order optimization methods.

### Strengths
Analyzing the optimal hyper-parameters for the second-order methods is provided in this work for the first time. Empirically they show that their suggested values for the hyperparameters help to find useful features when they increase the width of the layers i.e. their experimental results confirm their theoretical analysis. As a side contribution, they show that for a specific parameter setting KFAC has an implicit bias toward NNGP.

### Weaknesses
The paper mentions some conditions for the stable feature learning that comes from the previous works. However, I think it needs more context for a reader who is not aware of previous work. 
In the experiments, for example in Table 3, there isn’t any standard deviation next to the accuracies.

### Questions
I was wondering if we change the layer width for different layers what part of your analysis would change?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
