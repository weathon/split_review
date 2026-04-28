# Anti-Correlated Noise in Epoch-Based Stochastic Gradient Descent: Implications for Weight Variances

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
Stochastic gradient descent (SGD) has become a cornerstone of neural network optimization, yet the noise introduced by SGD is often assumed to be uncorrelated over time, despite the ubiquity of epoch-based training. In this work, we challenge this assumption and investigate the effects of epoch-based noise correlations on the stationary distribution of discrete-time SGD with momentum, limited to a quadratic loss. Our main contributions are twofold: first, we calculate the exact autocorrelation of the noise for training in epochs under the assumption that the noise is independent of small fluctuations in the  weight vector, and find that SGD noise is anti-correlated in time. Second, we explore the influence of these anti-correlations  on SGD dynamics. We find that for directions with a curvature greater than a hyperparameter-dependent crossover value, the results for uncorrelated noise are recovered. However, for relatively flat directions, the weight variance is significantly reduced, and  our variance prediction leads to a considerable reduction in loss fluctuations as compared to the constant weight variance assumption.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the correlation of gradient noise in the later training phase of SGD. They show that SGD noise will be anti-correlated over time, assuming the weights do not change. They also show that weight variance is small in flat directions, i.e., eigendirection corresponding to small eigenvalues of loss hessian. This result is obtained by assuming quadratic loss. They further implement experiments to verify their theoretical results.

### Strengths
1. Understanding SGD noise is an important topic in the optimization. This paper analyzes the SGD noise by connecting the covariance matrix to the Hessian of the loss and further connects the flat directions to the weight variance. I believe these insights are nice.

2. The paper is well-written and the logic is easy to follow. The experiments are nicely done to verify the theory.

### Weaknesses
1. I am not sure if it is reasonable to assume the fixed weights to analyze the gradient noise. It is almost trivial to obtain Theorem 4.1 under such an assumption since some probability arguments are sufficient. Additionally, if the weights are fixed, or almost fixed at the end of training, the effect of gradient noise is minimal. It should make more sense to understand the gradient noise at the beginning of training, where the weights change significantly. 

2. About the assumptions in Section 4.3, I do not see why Hessian and noise covariance commute in general. It seems like they commute when the loss is quadratic in weights, which is assumed in Assumption 1. Then analyzing quadratic loss seems less interesting and I believe there should have been many results regarding this setting. Could you comment on this?

3. I suggest that the authors avoid using $\gg$ or $\approx$ in mathematical statements. These symbols are not precise, and it is unclear which terms are considered small. Furthermore, simply stating the expressions (Eqs. (8) and (9)) makes it difficult to understand how the variance of weights and velocity changes. Adding some discussion would be beneficial.

### Questions
1. In line 319, it is claimed that if these conditions are not met, the weight fluctuations would diverge. How to see that?

2. Is the momentum necessary in your arguments? Do the results still hold for vanilla SGD?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper analyzes the behavior of SGD(m) without replacement (RandomReshuffle) and its implicit bias when the iterates reach a basin of some minimum. Theoretically, they derive the exact anti-correlation of the gradient noise for static weight. Then, under additional assumptions, they prove a connection between such anticorrelations and the variance of the weight fluctuations. Qualitatively speaking, this implies that the weight variance is decreased *only* in the flat directions, showing that without replacement provides a benign implicit bias towards flat minima. Their theoretical results are complemented with various experiments.

### Strengths
- An important gap in the SGD dynamics literature was considered by considering batched SGD without replacement in finite learning rate, showing explicit geometry-dependent implicit bias compared to replacement.
- The theory is general enough to include momentum SGD.
- Sufficient experimental results supporting the theories

### Weaknesses
 - IMHO, the biggest point preventing me from giving a higher score (along with my questions below) is that *some (not all)* of this paper's main conclusions seem to overlap with the preprint [1] for SGD without replacement (without momentum). Given that the authors could provide a satisfactory answer, I'm open to raising my score further.
To my knowledge, [1] showed that in-expectation, for both **ShuffleOnce** and **RandomReshuffle**,
    - SGD without replacement = SGD with replacement along larger curvature "+" Shrinking the tr(cov of gradients) along flatter directions (see their Theorem 1; "+" means decoupling)
    - Actually, SGD without replacement adds an implicit regularize that penalizes a weighted tr(cov of gradients) over single data points (see their Theorem 3)
    - In all their derivations, they do not make any restrictive assumptions (e.g., quadratic loss, anti-correlated noise for changing state, $[C, H] = 0$, etc)

- (continuing from above) All in all, given how the problem that [1] is tackling (behavior of SGD without replacement) and the qualitative general conclusion (greater curvature is similar to uncorrelated noise (with replacement), and flatter curvature decreases the fluctuation) both seem similar, I'm curious on what additional intuitions and results this paper adds compared to [1], and how the results presented here are related to [1]. I feel this should be much more emphasized, given that this paper relies on several assumptions that [1] does not consider: quadratic loss, anti-correlated noise even under dynamically changing weights, and $[C, H] = 0$. Especially the last assumption is critical for all of the theories presented in this paper, which allows for the use of common eigenbasis.

- (continuing from above) Immediately I see two advantages: one is that this paper's framework encompasses momentum and that this has more realistic experiments supporting the theories. I'm looking for something like "under such additional assumptions, our paper provides a much more precise characterization of ..... compared to [1], which can only say that ....".

- [writing] Overall, the writing and organization should be improved. Many important discussions have been completely relegated to the Appendix. Space-wise, maybe move/reduce Sec 3?

- [writing] The authors should consider making all the assumptions explicit in the main text and collecting them in an orderly fashion, instead of using phrases such as "under general assumptions, stated in Appendix C" or ""With the above assumptions".




### Questions
- I'm a bit confused about the statement, "Next, we consider the probability that two batches $k$ and $k + h$, separated by $h$ update steps, belong to the same epoch". I understood this as follows: given two update step indexes $k$ and $k + h$, what is the probability of the corresponding batches belonging to the same epoch? I don't see any randomness in this statement. Yes, the batches are random, but if the indices are deterministically given, then the two indices are in the same epoch if there exists a $i \geq 1$ such that $M (i - 1) < k < k + h \leq M i$. I guess the randomness is supposed to be w.r.t. the randomness of the batches being sampled, but 
  - In my head, $\frac{M - |h|}{M}$ is the probability of two deterministic batches being in the same epoch when we uniformly randomly allocate their indices such that they are separated by $h$ steps.
  - Maybe I'm completely missing (or misunderstanding) something here, so please feel free to correct me here!
  - As a clarification, you are considering RandomReshuffling, where at each epoch, an ordered partition of $[N]$ is sampled at random, right? The author should consider making this precise, as there is another variant of without replacement sampling, namely, ShuffleOnce, where a single shuffle takes place at the beginning and the same batches are used in the same order for all the epochs.

- Although I agree that weights remain approximately constant near minima, theoretically, could one use appropriate perturbation arguments (e.g., Taylor expansion) to provide a more complete theory of anti-correlation with varying states? Or would such more intricate analyses not give any useful insights and thus be unnecessary?

- Does the current analysis extend to ShuffleOnce, or at least empirically?

- [low priority, did not affect my initial evaluation] If time allows, can authors try the similar experiments for small scale transformer?

- Section 4.2 is IMHO too sudden without proper motivation. Why are we suddenly interested in the weight and velocity variance? Why consider their ratio? What is the intuition of the quantity *correlation time*? Should it be understood as, 'after the correlation time, the weights and velocities are somehow correlated'...?
Moreover, Section 4.2 refers to the setup described in Section 4.3, making me think that for the sake of organization, Section 4.2 should come after 4.3?

### Soundness
2

### Presentation
2

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
The authors study the dynamics of SGD in a discrete-time regime while sampling without replacement which leads to correlations in the noise between different time steps. By invoking certain assumptions, they derive the correlation function of the noise and claim that the anti-correlations in the noise may cause better generalization ability.

### Strengths
This paper is well-organized and well-written. The definitions and assumptions are made clear. The auto-correlation function of the gradient noise between different time steps is an interesting topic. The theoretical findings are solid upon the assumptions and experiments are thorough.

### Weaknesses
While the overall quality of this paper is good, there are still several questions I would like to ask.

1. The main theorem is derived on the basis of three fundamental assumptions 1-3. Assumption 1 is a commonly adopted one if the discussion is limited to a local minimum. However, **Assumption 2** is newly invoked by the authors on the state-dependence of the noise. The validity of this assumption is discussed through mere words and a "look" at the experiment done in Appendix H.  It lacks a rigorous demonstration of when this assumption can be adopted and how large deviations it may lead to the main theorems. Also, the experiment and discussion provided in Appendix H are extremely specific to the very task, and a detailed connection to Assumption 2 is appreciated.

2. **Assumption 3** is about the commutation relation between the noise covariance and the Hession. The authors claim that "this assumption is not strictly necessary but it simplifies the analysis". They provide evidence in Appendix L that under the circumstances they are considering, these 2 matrices are almost aligned with each other. In Appendix L they calculate a 0.82 cosine similarity between them and claim that "it seems to be a good approximation" in the final sentence. The details in this calculation are not provided and a 0.82 similarity does not seem satisfactory to claim that two things are alike in a common sense.  Besides, "it seems to be a good approximation" sounds like the authors themselves are not very confident in this statement and it is not a rigorous manner to make an approximation. I would like the authors to elaborate more on this assumption. Could the authors provide more details about the cosine similarity of two matrices? What level of similarity would be considered sufficient? Is it possible to provide a quantitative analysis of the influence of this cosine similarity on the validity of Approximation 3? Finally, a minor question, if this assumption is "not strictly necessary", is it possible to just discard it and establish a more general theory?

3. The experiments are performed on CIFAR10 using the LeNet and the details are provided in Appendix H. From **Figure 8**, it seems that the model is severely overfitting and the authors make no comments about overfitting. Is overfitting related to any assumptions made in the paper? I'm curious about that is this severely overfitting situation chosen intentionally. If yes, why? If not, what will happen to the results if the model does not overfit?

### Questions
While the overall quality of this paper is good, there are still several questions I would like to ask.

1. The main theorem is derived on the basis of three fundamental assumptions 1-3. Assumption 1 is a commonly adopted one if the discussion is limited to a local minimum. However, **Assumption 2** is newly invoked by the authors on the state-dependence of the noise. The validity of this assumption is discussed through mere words and a "look" at the experiment done in Appendix H.  It lacks a rigorous demonstration of when this assumption can be adopted and how large deviations it may lead to the main theorems. Also, the experiment and discussion provided in Appendix H are extremely specific to the very task, and a detailed connection to Assumption 2 is appreciated.

2. **Assumption 3** is about the commutation relation between the noise covariance and the Hession. The authors claim that "this assumption is not strictly necessary but it simplifies the analysis". They provide evidence in Appendix L that under the circumstances they are considering, these 2 matrices are almost aligned with each other. In Appendix L they calculate a 0.82 cosine similarity between them and claim that "it seems to be a good approximation" in the final sentence. The details in this calculation are not provided and a 0.82 similarity does not seem satisfactory to claim that two things are alike in a common sense.  Besides, "it seems to be a good approximation" sounds like the authors themselves are not very confident in this statement and it is not a rigorous manner to make an approximation. I would like the authors to elaborate more on this assumption. Could the authors provide more details about the cosine similarity of two matrices? What level of similarity would be considered sufficient? Is it possible to provide a quantitative analysis of the influence of this cosine similarity on the validity of Approximation 3? Finally, a minor question, if this assumption is "not strictly necessary", is it possible to just discard it and establish a more general theory?

3. The experiments are performed on CIFAR10 using the LeNet and the details are provided in Appendix H. From **Figure 8**, it seems that the model is severely overfitting and the authors make no comments about overfitting. Is overfitting related to any assumptions made in the paper? I'm curious about that is this severely overfitting situation chosen intentionally. If yes, why? If not, what will happen to the results if the model does not overfit?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the consequences of anti-correlations of update steps which arise due to selection without replacement in SGD. The paper rests on the assumption that we are at the end of training, or that we are near enough a minimum of the loss that the landscape is quadratic. The analysis begins by characterizing the different-time covariance of the gradients in terms of the covariance at equal times, and verifying numerically that their formula is correct. They use this to derive the related formulas for the covariance of the weights, and the covariance of the updates to the weights. 

They define a correlation time, $\tau_i$ as the ratio of these two covariances, which becomes the central object of study. Using the results from before, they calculate $\tau_i$ in terms of the momentum hyperparameter, $\beta$ and hessian eigenvalue, $\lambda$, which reveals two distinct limits. When the eigenvalue is large they find that the correlation time decreases as $\lambda^{-1}$ while it is constant when $\lambda$ is small. These results are all confirmed numerically for the top 5000 eigenvalues of the spectrum of a LeNet model on CIFAR10.

### Strengths
This paper is clearly written with a transparent analysis. Mathematical analysis is generally paired with sufficient words to explain the meaning of the relevant equations, and is well-motivated in itself. They perform a deep analysis in a relatively common setting of sampling without replacement, which should carry over (at least heuristically) to all such algorithms. Though the experiments are at a small-scale this is not an issue in my opinion as the result is mathematically robust, and the experiments are illustrative. Because the setting is well-circumscribed, the applicability of this work could be tested on a case-by-case basis.

### Weaknesses
The primary weakness, which is why I did not recommend this paper for acceptance, is my concern about the relevance of this work to the practical setting. In my reading of the paper I did not understand the motivation behind studying the end point of training as a limit. Due to this, the contribution of this paper is limited due to the specific setting considered. I am glad to increase my rating if the authors could sufficiently clarify the following two questions:

1. How can we understand finite training time behavior from this analysis?
2. In the setting where some $\lambda_i = 0$ exactly, how can we make sense of the constant weight assumption?

### Questions
These questions are lower-priority. Answers to them are primarily towards understanding the implicit viewpoint of the paper

1. What happens in the case of a loss function like $L(x) = x^4$ which is not well-described by a quadratic approximation near its minimum?
2. Orvieto et al. 2022 consider adding noise which is independent from the data rather than data-dependent SGD noise. How can we know that the anti-correlations in that kind of noise behave the same way as anti-correlations in SGD noise?
3. Is it true that sampling without replacement is better than increasing batch size, assuming that both result in the same overall gradient variance? 
4. How do you justify subtracting the weight drift at late times for experiments when your assumptions don't require this?

### Soundness
3

### Presentation
4

### Contribution
2
