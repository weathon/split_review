# Efficient Gradient-Based Algorithm for Training Deep Learning Models With Many Nonlinear Activations

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
This research paper presents a novel algorithm for training deep neural networks with many nonlinear layers (e.g., 30). The method is based on backpropagation of an approximated gradient, averaged over the range of a weight update. Unlike the gradient, the average gradient of a loss function is proven within this research to provide more accurate information on the change in loss caused by the associated parameter update of a model. Therefore, it may be utilized to improve learning. In our implementation, the efficiently approximated average gradient is paired with RMSProp and compared to the typical gradient-based approach. For the tested deep model with numerous stacked fully-connected layers featuring nonlinear activations on MNIST and Fashion MNIST, the presented algorithm: $\quad$ (a) generalizes better, at least in a reasonable epoch count,$\quad$ (b) in the case of optimal implementation, learning would require less computation time than the gradient-based RMSProp, with the memory requirement of the Adam optimizer,$\quad$ (c) performs well on a broader range of learning rates, therefore it may bring time and energy savings from reduced hyperparameter searches,$\quad$ (d) improves sample efficiency about three times according to median training losses. On the other hand, for a deep sequential convolutional model trained on the IMDB dataset, sample efficiency is improved by about 55%. However, in the case of the tested shallow model, the method performs approximately the same as the gradient-based RMSProp in terms of both training and test loss. The source code is provided at [...].

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents an algorithm using an average gradient to improve deep neural network training, paired with RMSProp. It claims better generalization, sample efficiency, and robustness across learning rates, with notable gains in deep models but limited improvements in shallow ones.

### Strengths
The motivation of the paper is clearly articulated, and based on the example in Figure 1, I believe that considering the use of average gradients is indeed a worthwhile alternative to traditional gradients. This paper makes an interesting attempt to explore the integration of concepts from another field (see Weaknesses part) into training.

### Weaknesses
1. Lack of contribution. The core idea of using average gradients is not new, as it closely aligns with the concept of "integrated gradient" in the literature. It is a direct shift of the integrated gradient [1] in the field of explainable AI.

> [1] Sundararajan, M., Taly, A., & Yan, Q. (2017, July). Axiomatic attribution for deep networks. In ICML.

2. The first main weakness of the paper is that computations based on average gradients are typically costly as mentioned by authors. If all gradients are replaced with average gradients, this would require calculating an integral for each neural network parameter in addition to its gradient at every iteration, resulting in an intractable complexity in practice. The authors also seem to have not reported the computation times in their experiments.

3. The theoretical foundation of the proposed average gradient approximation appears to be incorrect. The method proposed in this paper is based on the chain rule in Eq. (1). However, this chain rule for average gradients is incorrect, and it is easy to construct counterexamples. Looking at the proof, Eq. (17) is obviously incorrect; the integral of a product of functions does not equal the product of their integrals. Therefore, the authors must either provide a characterization of the class of integrand functions that satisfy Eq. (1) or measure the error of the chain rule approximation and demonstrate that its impact is negligible. Otherwise, despite the authors presenting some special cases, the theoretical foundation of this paper cannot be justified.

4. Experiments only contain toy examples. Both theoretically and empirically, there is a concern that the proposed method may not scale effectively to moderately larger problems. Furthermore, there is a notable absence of comparisons with established benchmarks.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This research paper introduces a novel algorithm for training deep neural networks with numerous nonlinearities. The proposed approach involves estimating the average gradient over the range of a potential parameter update, offering a method to enhance learning. In the implementation, the efficiently approximated average gradient is combined with RMSProp and evaluated against standard gradient-based techniques.

### Strengths
1. The underlying assumption of averaging is intriguing. 
2. The observation in Figure 1 is noteworthy.

### Weaknesses
1. The paper is generally hard to follow, making it difficult to grasp the contribution and novelty of the work.

2. There is a significant amount of irrelevant information of the algorithm and writing typos. For example, several areas in the paper lack clarity:

   - In the abstract, there is *[...]* which is weird.
   - The start of the introduction is nearly a rephrasing of the abstract.
   - The introduction primarily repeats points from the general conclusion (e.g., RMSDrop performs well for deep models), diminishing the value of the information.
   - The introduction reads like a collection of related work, making it difficult to follow and affecting the logical flow.
   - Line $112$ contains a vague statement without added insight.
   - The figure provides limited information and is challenging to interpret.

3. There are three algorithms, all of which rely solely on descriptive text without any mathematical representation.

4. The algorithm is validated only on MNIST and Fashion MNIST data, which are relatively simple, toy examples for deep learning tasks.

### Questions
1. Could the algorithm section be condensed, as it's challenging to identify which algorithm is most significant?
2. How does the proposed algorithm relate to models with *many* nonlinear layers?
3. How does the algorithm perform on larger datasets, such as ImageNet?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a new workflow for training neural networks by modifying both the gradient calculation and the update recursions of standard algorithms. The authors replace the current gradient with an averaged gradient along the potential update direction, which is predefined by the exact gradient. The paper also introduces a cost-effective propagation method for calculating the average gradient. Small-scale experiments are conducted to support the proposed algorithm.

### Strengths
The paper offers a valuable perspective on leveraging explainable AI techniques, specifically, *Integrated Gradient* [1], which the authors refer to as the average gradient, to support neural network training.

>[1] Sundararajan, M., Taly, A., & Yan, Q. (2017, July). Axiomatic attribution for deep networks. In International Conference on Machine Learning (pp. 3319-3328). PMLR.

### Weaknesses
The main weakness of the paper is that computations based on average/integrated gradients are typically costly, as mentioned by the authors, but the effectiveness of the proposed average gradient approximation for acceleration remains uncertain. The average gradient propagation algorithm in Eq. (1) relies entirely on the rough approximation in Eq. (17). However, it is highly dependent on the properties of the decomposed integrand, and as the neural network structure becomes more complex, this assumption becomes increasingly unreasonable. Although the authors present Fig. 5 to illustrate their motivation, it is still not difficult to find counterexamples that challenge such an approximation.

The experiments are generally weak and not sufficiently convincing, involving only toy datasets such as MNIST/Fashion-MNIST and shallow networks. Given that the algorithm uses approximations during training, it is essential to carefully evaluate its effectiveness using more representative datasets and complex model architectures. Additionally, there may be issues with the experimental setup that have led to the claimed conclusions. Please refer to the questions section for further details.

The presentation of the algorithm in this paper is somewhat unconventional, and the connections between multiple algorithmic blocks are unclear. It would be helpful if the authors could present these blocks in a more concise and mathematical format, clearly specifying their outputs.

### Questions
- Why are there two rows in Tab. 3 with guessed learning rates, while a hyperparameter search was conducted for other identical models or algorithms? Moreover, the range of the search differs between the proposed algorithm and the baseline. Hyperparameter selection could be conducted more comprehensively, as multiple locally optimal learning rates are observed in Tab. 3.

- The proposed algorithm shows similar performance to the standard algorithm on Model A, but on Model B, the authors claim it is three times faster. Could this be because the chosen learning rate is precisely three times that of the baseline?

- The authors mentioned the improvement in computation time achieved by this method. It would be more informative if results were provided showing the relationship between the algorithm's wall-clock time cost and its accuracy.

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
2

### Summary
The authors describe a modification to how gradients are computed for first order optimizers that uses a gradient-averaging technique that they claim generalizes better, would require less time in optimal implementation, is more robust over choice of learning rate, and improves sample efficiency according to their empirical benchmarks. They prove that the average gradient is directly proportional to the loss delta in their appendix. 

S1.2 describes prior works and trends, delineating the work from momentum-based methods which maintain a moving average of gradients and from averaging gradients across a batch, which is common place. The authors instead are averaging the gradient over the range between the current parameter vector ($\theta_t$) and the parameter vector given by a vanilla RMSProp gradient updates step ($\theta_{t+1}$ or more commonly $\theta$' in this paper); as the authors point out, this average gradient can be computed by evaluating the model at $\theta_{t}$ and $\theta_{t+1}$ and dividing by the range.

They describe in great detail the average gradient and provide one-dimensional intuition (which is very appreciated). The algorithms are described in similar detail. Equation 7 describes a novel metric that the authors will use to evaluate their experiments, called the RD or relative difference, which measures the difference in change of loss at each step of the average gradient vs the vanilla gradient, normalized to the change in loss of the vanilla gradient. In Table 2, the authors argue that the average gradient is more robust over learning rates than vanilla gradients. 

They proceed to empirical methods and show that while the average gradient essentially does not improve upon vanilla gradients for a LeNet style architecture, it does seem to show improvements on a small sample of experiments using an (as the authors admit) impractical network architecture of 30 layers (mostly composed of repeated Linear layers of 10x10 size) on the MNIST and FMNIST dataset. The RD metric is used to argue that the average gradients of the architecture B significantly outperforms vanilla gradients. The visualize the loss cuvres of these experiments which corroborates that Model B does appear to train faster in terms of sample efficiency. 

The authors conclude by restating their main claims.

### Strengths
I think the presentation of the work is mostly good; I applaud the authors for attempting an innovative solution and attempting to provide both a theoretical and empirical foundation for their work. Clearly if the average gradient can be definitively shown to robustly outperform the vanilla gradient the work would be of tremendously high impact and appropriate for a major ML conference. I think if the authors were to submit a major revision which addresses my worries specifically regarding the empirical experiments, the paper could be accepted. As is, I think it is clearly a not accept.

I appreciate the authors making their code available and endeavoring to put their algorithms to great detail into their work. Reproducibility is important.

### Weaknesses
I believe that the RD metric is computed per step for each run, which leads to a large number of samples and is where you draw your ability to separate the performance between average and vanilla gradients. If that is correct, the RD metric samples being collected are not independent of one another in the context of a single experiment generating sequential gradient steps. Because of this, I do not think the empirical argument of demonstrated performance gain is sound. There are multiple ways to address this: I think one way would be to run the experiments many times with different seeds for initialization + batch order; then for each experiment, fit a power law curve (or similar) to the observed loss, collect the power law coefficients and perform your statistics on those samples. 

You write multiple times that the average gradient provides more information on the change in loss caused by the associated parameter update of a model; this is in fact the first claim in your abstract. From this I think you mean that you have proven that the average gradient can be shown to be proportional to the loss differences; however it seems like a logical leap to me that simply because the average gradient is proportional to loss deltas that this implies it is a robust improvement over vanilla gradients.  

One cynical perspective is that the vanilla RMSProp performed as well as your averaging gradient on model A which is similar to common CNN architectures, but only on the model that is as you admit impractical (26 x linear layers of shape 10 x 10) does your average gradient outperform. I am confused as to why you would include experiments on an impractical network and furthermore only include as a baseline the performance of RMSProp on that same impractical network. Overall I do not find the empirical evidence presented very conclusive that the average gradient in the context of models of great interest to the community. 

Minor: I would change the color of the point representing "before parameter update" figure 1 as the grey does not appear well in my print out or when viewed online. Perhaps consider a black star? Also on figure 1, what is the difference between the left and right plot represent? They should be titled.

the authors point out that there is an increased cost to running the average gradient that grows with the number of iterations, growing from 3x for 2-iterations and 8x for 5x iterations. I wanted to ask if this is a fundamental limitation or merely a limitation of the current implementation? If this can not be conceivably improved, it begs the question of whether vanilla gradients might be less sample efficient but overall more time (and therefore cost!) efficient. I think you are arguing through something you call the "optimal implementation" that you are in fact faster. Can you re-explain what this optimal implementation is? Is it a learning rate choice, is it a n-iterations choice?

### Questions
In figure 1, left side, you show how the gradient line is negative sloped and the average gradient line is positive sloped. The local minima of the loss function visualized is in the positive direction relative to the "before parameter update" point. A negative gradient is needed to move the parameter update using the traditional GD update rule: ($\theta_{t+1} = \theta_t - \eta \frac{\partial l}{\theta_t}$) in the positive direction, but seemingly replacing the gradient with the average gradient would give a positive slope moving the point in the wrong direction. Can you explain what the reader is meant to take away from figure 1? What is wrong with my thinking about this? 

Related to the above, you include an appendix titled "Loss minimization potential" but I believe the main proof is that the average gradient is proportional to the loss delta. I don't think that necessarily shows that the average gradient step would lead to loss minimization? More precisely, in figure one you seem to show a step where the average gradient is in the wrong direction, and if in fact if the loss delta is zero, then you seem to prove that the average gradient is zero and no update occurs -- i.e., if the chord intersecting the loss function is zero sloped, no update occurs. Where am I going wrong? Is it that the "n-iterations" are the number of gradients being averaged and so in practice these chords are unlikely to arise?

I guess related to the above, what specifically are the "n-iterations"?

In your introduction you reason that it is most fair to compare your research to models trained with RMSProp since by default the momentum of the RMSProp optimizer is zero and therefore comparing losses after each batch update is valid. Can you explain this reasoning and why comparing to SGD with momentum chosen to be zero, or Adam with momentum chosen to be zero would be less valid? Or more generally why comparing to optimizers that use momentum is invalid?

line 141; "Then it is assumed that the absolute value of the parameter delta of the RMSProp optimizer is good enough to retain it" can you explain what the assumption is and whether it is specific to RMSProp or needs to be assumed of other optimizers as well?

In historical works comparing optimizers, was the relative difference or (RD, equation 7) metric that you propose used? Are you the first to propose it? Why did you choose to use this metric, and are there other important measures that might matter to users? For example, RD treats steps that might take different amounts of compute time but cover the same number of update steps equally. How much longer do individual steps take with average gradient compared to vanilla RMSProp? How does this scale with the number of parameters, for example, can you roughly guess what hardware (specifically how much memory) and how much time would be required to run your algorithm on a model of 30 layers like model B but with order 1 Million model parameters?

### Soundness
2

### Presentation
3

### Contribution
2
