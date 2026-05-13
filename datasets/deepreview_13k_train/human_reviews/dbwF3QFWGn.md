# Stochastic Online Conformal Prediction with Semi-Bandit Feedback

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Conformal prediction has emerged as an effective strategy for uncertainty quantification by modifying a model to output sets of labels instead of a single label. These prediction sets come with the guarantee that they contain the true label with high probability. However, conformal prediction typically requires a large calibration dataset of i.i.d. examples. We consider the online learning setting, where examples arrive over time, and the goal is to construct prediction sets dynamically. Departing from existing work, we assume semi-bandit feedback, where we \textit{only observe the true label if it is contained in the prediction set}. For instance, consider calibrating a document retrieval model to a new domain; in this setting, a user would only be able to provide the true label if the target document is in the prediction set of retrieved documents. We propose a novel conformal prediction algorithm targeted at this setting, and prove that it obtains sublinear regret compared to the optimal conformal predictor. We evaluate our algorithm on a retrieval task, an image classification task, and an auction price-setting task, and demonstrate that it empirically achieves good performance compared to several baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- The paper studies the problem of conformal prediction in an online setting with semi-bandit feedback. The semi-bandit feedback is conditioned on whether or not the true label was present in the confidence set, if it is the true label is given back (and used for computing the score) for further refinement otherwise we only recieve that the true label is not present. 
- The main contribution of this paper is an algorithm which performs online conformal prediciton, which the authors show achieves sub-linear regret upto a constant factor. 
- The authors use the DFW inequality to construct upper bounds for the empirical CDF of the coverage parameter and adaptively update this upper bound using the semi bandit feedback.
- The authors show experiments on three different tasks including an image classification task, a document retrieval task and a second price auction task for three key metrics regret, coverage rate, undercoverage count. The tasks are benchmarked with 2 techniques: ACI and DLR.

### Strengths
1. To the best of my knowledge, the paper is the first to deal with the problem of online conformal prediction with semi bandit feedback. Therefore there is originality to the work. 

2. The quality of some aspects of the paper is decent, especially the mathematical notation used is clean and easy to understand. The coverage of conformal prediction is sufficient. The introduction section is also well-written and provides intuitive exposure to conformal prediction. 

3. The applications of the paper, especially in document retrieval, can be significant in a contemporary interactive document setting and even the annotation example for the image classification setting could be potentially useful in an active learning setting. Conformal prediction is also useful in creating prediction sets for black box models in general, and such a problem set has sufficient motivation in general. 

4. The three metrics in the results are complementary to each other and match well with the claims of the paper.

### Weaknesses
1. The writing, in general, is a bit unclear and sloppy. Here a few examples:
- a. What is the source of randomness in the two levels of probability decomposition (The pac and the coverage)? 
- b. The proof of theorem 1 can use some intuition
- c. The description of the Experiment is not well-written, for example, the desired coverage rate or other parameters? Does the paper use all the samples from imagenet or is their a subsampling?
- d. The theorem is not self-complete, everything referenced in the theorem should be defined the assumptions should be mentioned, 
- e. The full form of PID and ACI is not mentioned in their first reference.
2. Assumption 2.2 might not hold in practice, especially in an active learning setting, where the loss function might be ill-defined for the first few rounds when the model lacks confidence.
3. In an active learning setting, do you ideally want a coverage set to decrease with time? Also in general, in active learning there is a constraint on the size of the samples that can be annotated. How much effort will be spent in identifying if the true label is there or not? 
4.  The PAC bound does not reappear again in the paper or the theoretical results, what is the point of presenting it? Usually, there is a relation between the number of samples and the error probability, what is the relation in this case?
5. There are no margin-of-errors mentioned in the experimental results, therefore, it is difficult to establish the significance of these results. Also, the ACI line on cumulative regret is not discernible.

### Questions
1. What happens to the algorithm in practice if assumptions 2 and 3 are unsatisfied? Where does the regret analysis fail?

2. “As a consequence, our algorithm converges to the true \tau^*” Is the convergence a consequence of tau being a monotonic increasing sequence?

3. Are there changes to the aci algorithm that can achieve the same thing? What is the advantage of giving \tau_t as a feedback?

4. Why does the coverage rate increase and then decrease for ACI?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes an online conformal prediction method with semi-bandit feedback. The algorithm is based on an upper estimate of the score function's CDF, with sublinear regret bound under certain loss functions. Several experiments are conducted to show the effectiveness of the algorithm.

### Strengths
The algorithm enjoys a sublinear regret bound. It constructs compact prediction sets, while ensuring high coverage probability. The experimental results show significant improvement over the other baselines.

### Weaknesses
1. The theoretical result seems not very sufficient. From my understanding, coverage rate and the size of the prediction set are the two key metrics of practical interest. However, it is unclear how the result in Theorem 3.1 relates to these two metrics. Specifically, the regret bound is defined in terms of the loss function \(\phi\), which is an abstract measure of the quality of the chosen threshold \(\tau_t\). It is not immediately obvious how minimizing this regret directly translates to achieving a desired coverage rate or minimizing the prediction set size. A more explicit connection between the regret bound and these practical metrics is needed.
2. The sizes of the prediction sets are not reflected in the experimental results either. The experiments focus on the average loss, but do not provide any information about the distribution of the prediction set sizes, or how they evolve over time. It would be beneficial to see the average size of the prediction sets, or even better, a histogram of the sizes, to understand the trade-off between coverage and set size. This is crucial to validate the practical utility of the proposed method.
3. The presentation quality can be improved. For example, in Fig. 1, error bars can be added, and I only observe 3 curves while 4 algorithms are in the legend. There are also some typos. For example, in line 429, "our our".

### Questions
1. Can the framework be extended to non-i.i.d setting? Such as black-box optimization, where the optimal x is searched for.
2. In assumption 2.1, the definition of loss is a bit abstract. Can the authors elaborate a bit more on how to interpret this loss in different practical applications?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers the conformal prediction problem in the online learning setting with semi-bandit feedback. The authors proposed a new algorithm targeted at this setting and prove that it obtains sublinear regret bound. Then, the authors conduct some experiments to validate the high efficiency of the proposed algorithm over existing approaches based on conformal prediction in the online learning framework.

### Strengths
1. This paper studies an interesting and timely topic on conformal prediction with online learning.
2. I did not check the appendix in detail, but I feel the theoretical results are proper.
3. Several real-world experiments are conducted to validate the high performance of the proposed method.

### Weaknesses
1. I feel the presentation of this paper can be improved, The current version is still hard to follow. For example:
1.1 More background information on conformal prediction should be provided, such as the studies on conformal prediction in statistics and its recent applications on the online learning problem. Specifically, the paper should discuss the core ideas of conformal prediction, including the concept of exchangeability, the construction of prediction sets, and the distinction between inductive and transductive conformal prediction. Furthermore, it would be beneficial to discuss how these concepts translate to the online learning setting and what challenges arise when combining conformal prediction with online learning algorithms.
1.2 There are many definitions/notations in your work, and it is better to recall their definitions sometimes. For instance, in the second paragraph of page 3, it is better to define $\tau$ and $\tau_t$ there and I feel they are not previously defined. And in the pseudocode it is better to define $s_t$ there. The current version is hard to read. It's not just about defining them initially, but also reminding the reader of their meaning when they are used later in the paper, especially when there are many symbols involved. For example, when $\tau_t$ is used in the algorithm, a brief reminder of what it represents would significantly improve readability.

2. Running time of algorithms should be reported in the paper since conformal prediction may lead to heavy computation, e.g. providing runtime comparisons between their proposed method and the baselines for each of the experimental tasks. The computational cost of conformal prediction, especially in online settings, can be a significant bottleneck. The paper should include a detailed analysis of the runtime complexity of the proposed algorithm and compare it with the baselines. This should include not just theoretical complexity but also empirical runtimes on the experimental datasets. This is crucial for understanding the practical applicability of the method.

3. It is better to give some more real-world applications under your problem setting: a combination of conformal prediction and semi-bandit framework. The paper would benefit from a more thorough discussion of real-world scenarios where the combination of conformal prediction and semi-bandit feedback is relevant. For instance, in personalized medicine, one might want to predict treatment outcomes with confidence intervals (conformal prediction) while only observing the outcome of the chosen treatment (semi-bandit feedback). Another example could be in online advertising, where the goal is to select the best ad to display while also providing a prediction of the expected click-through rate with a specified level of confidence. These examples would help to motivate the problem setting and demonstrate its practical relevance.

### Questions
1. Are your assumptions made in the paper common in the conformal prediction setting and the semi-bandit setting?
2. What is the theoretical novelty of your paper compared with the existing work? The analysis seems not very difficult for me. It is better to summarize the theoretical contributions in a small paragraph since I feel most techniques or results are similar to existing work under your assumptions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors propose a novel conformal prediction algorithm for constructing online prediction sets under a novel setting called stochastic semi-bandit feedback. They prove that the developed algorithm can achieve sub-linear regret and demonstrate the applicability of their method in different tasks including a retrieval task, an image classification task, and an auction price-setting task.

### Strengths
1. Considered a novel setup where true label can be observed only when prediction set covers it

2. Established a regret bound for the problem of interest

3. Conducted experiments in different tasks demonstrating the utility of the proposed method

### Weaknesses
1. While authors established a regret bound for the problem of interest, the author didn't mention related regret bounds in the existing work. Besides, the author did not mention how good the regret bound is compared to the existing work. 

2. In the experiments, I observe the coverage rate is relatively conservative for the proposed method. Does the coverage rate stabilize if step is large enough? Is it possible to speed up the coverage convergence?

3. The connection to online conformal prediction literature, particularly adaptive conformal inference, is not sufficiently discussed. The method appears more aligned with i.i.d. settings with missing responses, where coverage guarantees might not hold under distribution shifts. The discussion of related literature in this aspect is limited.

4. The theoretical contribution, while providing a regret analysis, does not convincingly demonstrate any form of optimality. The discussion on the theoretical contributions is limited, and the optimality of the proposed method is not addressed.

### Questions
Can you provide results for longer time horizons to show if/when the coverage rate stabilizes?

Can you also discuss potential modifications to their algorithm that could accelerate convergence of the coverage rate, and any tradeoffs these modifications might introduce?

### Soundness
2

### Presentation
2

### Contribution
2
