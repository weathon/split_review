# Training-time Neuron Alignment for Improving Linear Mode Connectivity and Model Fusion

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
In deep learning, Stochastic Gradient Descent (SGD) will find different solutions that are functionally similar but far away from each other in the parameter space. The loss landscape of linearly connecting two SGD solutions is called Linear Mode Connectivity (LMC), which often shows barriers. Current neuron alignment methods seek to find a network permutation that can map two SGD solutions into the same loss basin to improve LMC and model fusion. However, these methods are post-hoc and usually require large computations due to the astronomical number of permutation matrices. Can we realize training-time neuron alignment? In this paper, we first hypothesize that it can be realized by learning into an effective subspace. First, we provide a preliminary theoretical result to support the hypothesis. We further propose a subspace algorithm for partially fixing neuron weights to reduce the potential permutation symmetries without hurting accuracy. It is found that by applying our training-time alignment method, the LMC is largely improved and the required computation for post-matching is reduced. Interestingly, we also find random pruning at initialization can improve connectivity, which validates our subspace hypothesis. Lastly, we propose two algorithms, incorporating training-time neuron alignment in federated learning, to showcase its prospects in boosting model fusion even under heterogeneous datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new method for reducing symmetries in a neural network. By keeping a $1-\rho$ fraction of the parameters fixed after initialization and running gradient descent, they find a neural network that has good interpolation behavior (i.e., convex combinations of good parameters lead to parameters that are also good).

This enables federated learning and other applications, as models can be averaged without loss in performance.

### Strengths
- The main advantage of the method is that it is performed during training time, and is not a post-processing step. This allows for easier averaging of models.

- Extensive experiments and ablation studies.

- Applications and extensions to federated learning and interesting and possibly impactful.

### Weaknesses
 - Some of the claims are a little overhyped, such as ``training in a subspace'' meaning keeping some set of parameters frozen and optimizing the rest. 

- The theory result is weak -- it doesn't imply much for the proposed method. it states that given Gaussian initialized neural networks, the gradient and the curvature of the convex combinations of these networks are bounded by the dimension, and hence lowering the dimension is desirable.

- The algorithmic novelty is also limited, and most of the strengths lie in the empirical studies on the effect of width, etc.

### Questions
See weaknesses section

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce a subspace algorithm aimed at enhancing Linear Mode Connectivity (LMC) during the training. They begin by establishing a preliminary theorem to explore the possibility of LMC improvement through the reduction of the search space. Building on the insights gained from this theorem, they proposed a mask-based training scheme. To empirically validate the efficacy of their proposed methods, the authors conduct numerical experiments.

### Strengths
The paper studies an important problem that is how to improve the LCM during the training. LCM is significant in terms of training dynamics and generation and model fusion. The paper is well written and without so many typo and errors. It is easy to follow and read.

### Weaknesses
I have a few concerns about the novelty and results of this paper. Firstly, the authors propose a mask-based training scheme, which has already been explored in the literature. While there are variations in the masking details, such as random weight initialization for untrained weights, the overall approach resembles dropout regularization, where different subsets of neurons are masked during each iteration. The core idea of masking weights and re-initializing them is not novel, and the specific implementation details, such as the random initialization of masked weights, do not sufficiently differentiate it from existing regularization techniques. Furthermore, the method's reliance on a fixed mask throughout training, while different from the dynamic masks in dropout, still shares the fundamental concept of restricting the network's capacity during training.

Furthermore, the results presented in the paper strike me as somewhat expected. The authors themselves acknowledge in Theorem 3.2 that improving Linear Mode Connectivity (LMC) is achieved by reducing the number of neurons, denoted by $d$. This essentially means using a simpler model, and the neural network is not necessarily overparameterized. Consequently, the number of minima is reduced, leading to a reduction in barriers between different solutions. The paper does not adequately address the potential trade-off between improved LMC and reduced model capacity, which could lead to diminished performance on complex tasks. The theoretical justification, while present, does not fully explain why this specific masking approach leads to better LMC compared to other methods that also reduce effective model size.

### Questions
1. Assume weight matrix $W$ are randomly initialized as IID standard Gaussian, which is a common practice in neural network initialization. Then $W$ follows a Matrix Normal distribution, i.e., $W\sim MN(0, I, I)$. By applying permutation matrices $P$ and $Q$ to $W$, the result distribution has the same Matrix Normal form, i.e., $PWQ \sim MN(0, I, I)$. Hence, the permutated weight matrix maintains the same distribution as the original $W$. This suggests that permuting the weight matrix is equivalent to reinitializing it. Given this equivalence, it raises the question of how to consider all permutations, given that the search space is uncountable.
2. The "mask ratio" is not precisely defined, and it seems to be related to the ratio of untrained neurons to the total number of neurons. 
3. Is it possible to express the results in Theorem 3.2 in terms of "loss barrier" or "accuracy barrier"?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
When training a neural network with SGD, different solutions in the parameter space can be obtained. The linear connection between two different solutions is called Linear Mode Connectivity (LMC). One commonly used approach to achieve LMC is to align the neurons of two network parameters through parameter permutation after training so that they are in the same loss basin. However, the number of permutation matrices is very large, and it requires a lot of computation because it is post-hoc. Therefore, the authors propose Training-time Neuron Alignment by Partially Fixing Neurons (TNA-PFN), which can align neurons at training time to create LMC. TNA-PFN is a method that learns in the parameter subspace by fixing part of the network parameters as initialization, based on the hypothesis that learning a network in an effective subspace with less permutation symmetry can lower the LMC barrier between trained networks. The authors support this hypothesis through both theoretical and experimental results. Also, the authors propose two algorithms, FedPFN and FedPNU, which adapt TNA-PFN to federate learning, and show that they have the potential to improve model fusion on different datasets.

### Strengths
I think the strengths are the simplicity of the method, the theoretical support, and the clean writing.
- The paper presents a new method to achieve LMC, and the idea of fixing a parameter to reduce permutation symmetry is novel.
- The paper is well written and easy to follow.
- The hypothesis and theoretical explanation are convincing.
- Experiments are extensive and show that TNA-PFN works in some practical applications.
- The paper proposes FedPFN and FedPNU, which can be used practically in Federated Learning, and shows that they work well in practice.

### Weaknesses
The biggest weakness seems to be the experimental results. The results are not promising enough to accept that TNA-PFN works effectively.

- As mentioned in the paper, the MNIST results in the second plot of Figure 3 and the experimental results of Entezari, et al. (2022) [1] show that the barrier actually decreases as the network width increases. According to the theorem presented in the paper, the barrier may decrease as the learned dimension decreases, but it does not apply well to these experiments. This discrepancy between the theoretical claim and empirical results raises concerns about the generalizability of the proposed method. Specifically, the paper's theoretical argument focuses on reducing the effective dimensionality of the parameter space through partial fixing of neurons, yet the observed behavior in wider networks contradicts this, suggesting that other factors may be at play that are not captured by the theory.
- In many experiments, the absolute barrier is too high when using TNA-PFN alone to be an LMC. Of course, it lowers the barrier compared to the vanilla train with no training, but many experiments show a non-negligible barrier. The practical significance of this reduction is questionable, as the remaining barrier still hinders effective linear mode connectivity. For instance, while a 20% reduction in barrier height might be reported, the absolute barrier might still be too large for practical model merging or ensembling.
- There is almost no difference in LMC performance between weight matching (WM) after training with TNA-PFN and directly using weight matching. Weight matching after TNA-PFN requires a few fewer iterations, but I don't know how much of a cost savings this provides. From a practical perspective, it introduces an additional hyperparameter, the mask ratio $\rho$, so I'm not sure how much benefit there is compared to the cost of tuning it. The marginal reduction in iterations for weight matching does not seem to justify the added complexity of introducing and tuning the mask ratio, especially when the final LMC performance is comparable.
- It's good to have a variety of experiments, but there are no experiments on large datasets like ImageNet. It would have been nice to see some experiments on larger datasets, as they generally have different characteristics than MNIST and CIFAR10.

### Questions
- In the experiments in the paper, the mask ratio was set to 0.4; was this an experimentally tuned value, or is there some underlying theoretical basis?
- Which of the three algorithms presented in Ainsworth et al. (2023) was used for weight matching (WM)? What is the approximate computational cost per iteration?
- Do FedPFN or FedPNU work in general learning situations other than federated learning, and can they be used for model ensembling?
- I'm not sure why the LoRA section was added to Appendix C.1 and what it is trying to say.
---
**Ainsworth et al.** [Git Re-Basin: Merging Models modulo Permutation Symmetries](https://openreview.net/forum?id=CQsmMYmlP5T). *ICLR*, 2023

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the problem linear mode connectivity(LMC), starting from the assumption that the optimal network weights lie in a lower dimensional subspace. To measure LMC they use the commonly used Accuracy Barrier as a metric. They study the setting where a subset of fixed network weights is frozen during training, which leads to better LMC compared to vanilla training for the case of a single model as well as the case of multi-model fusion.
They also consider the setting of federated learning where at each time step the server freezes a subset of networks weights of all the clients.

### Strengths
- The method seems to outperform vanilla pruning  in Figure 2
- In the setting of federated learning the proposed have similar performance to previous baselines and and some cases even has better performance

### Weaknesses
 - It is a bit hard to judge from the experimental results for what networks/settings one would prefer this method over other methods
- Lack of experiments at scale (e.g. ImageNet)
- The method is conjectured to perform better for wider networks and worse for deeper networks. It would be interesting to have a more quantitative result  i.e. plot the performance for varying width and depth.
- For the setting of a single network and multi-model fusion why is there only a comparison to vanilla training and not other methods for improving LMC?
- Why is the accuracy not reported in Figure 1?
- Could the authors elaborate a bit how pruning for mask ratio 0.7 in Figure 2 causes the model to be as bad as random guessing? Do they expect similar behavior for larger datasets and models?

### Questions
- The method is conjectured to perform better for wider networks and worse for deeper networks. It would be interesting to have a more quantitative result  i.e. plot the performance for varying width and depth.
- For the setting of a single network and multi-model fusion why is there only a comparison to vanilla training and not other methods for improving LMC?
- Why is the accuracy not reported in Figure 1?
- Could the authors elaborate a bit how pruning for mask ratio 0.7 in Figure 2 causes the model to be as bad as random guessing? Do they expect similar behavior for larger datasets and models?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
