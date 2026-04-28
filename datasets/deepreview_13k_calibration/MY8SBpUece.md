# A Theory of Non-Linear Feature Learning with One Gradient Step in Two-Layer Neural Networks

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Feature learning is thought to be one of the fundamental reasons for the success of deep neural networks. 
It is rigorously known that in two-layer fully-connected neural networks  under certain conditions, one step of gradient descent on the first layer can lead to feature learning; characterized by the appearance of a separated rank-one component---spike---in the spectrum of the feature matrix.
However, with a constant gradient descent step size, this spike only carries information from the linear component of the target function and therefore learning non-linear components is impossible.
We show that with a learning rate that grows with the sample size,
such training in fact introduces 
multiple rank-one components, 
each corresponding to a specific polynomial feature.
We further prove that the limiting large-dimensional and large sample training and test errors of the updated neural networks are fully characterized by these spikes. 
By precisely analyzing the improvement in the training and test errors, we demonstrate that these non-linear features can enhance learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studied the spikes in the feature map matrix of a two-layer neural network with large step gradient descent (GD) on mean square loss. When learning rate $\eta=n^\alpha$ with $\frac{\ell-1}{2\ell}<\alpha<\frac{\ell}{2\ell+\ell}$, there will be $\ell$ large spikes in the feature map matrix (or the Conjugate Kernel matrix) and these spikes are correlated to the degree $\ell$ Hermite components of the target function. The asymptotic training errors for ridge regression of this trained feature map matrix has been presented in the proportional limit. This paper fills the gap in the learning rates, when $1\ll\eta\ll\sqrt{n}$, in Ba et al. (2022).

### Strengths
Despite its technical nature, the paper is very well written. The particular setting the authors study is novel and interesting for both the random matrix theory community and deep learning theory. The detailed analysis of the scaling of learning provides us with a more comprehensive understanding of the features learned in GD training processes, although the authors only consider one step of GD. The result is precise and clean, showing the asymptotic improvement in the loss for potential feature learning.

### Weaknesses
1. A limitations section is missing. In the conclusion section, the authors should state the limitations of the assumptions and the results. The authors only proved the improvement of training loss in this two-stage training process for neural networks (NNs). There is a lack of analysis for generalization errors, although I understand there may be some difficulty with this kind of theoretical result. There should be some remark or discussion on this, or providing some conjectures related to the generalization error. Specifically, the analysis focuses on the training loss, which is an important first step, but it does not address how these learned features will perform on unseen data. The paper should discuss the potential for overfitting, especially given the large learning rates considered, and how this might impact the generalization performance. A discussion of the bias-variance trade-off in this context would be valuable.

2. Additional simulations are needed. In Section 5, there are only cases for linear and quadratic target functions. It would be better to provide more simulations for training and testing errors with more complicated target functions to show the feature learning when $\eta$ is sufficiently large. There is no empirical simulation for the staircase phenomenon in Figure 3 (Right). The simulations are limited in scope, and it is unclear how well the theoretical results translate to more complex scenarios. The absence of the staircase phenomenon in the simulations is a significant gap, as this is a key prediction of the theory. The authors should also consider including simulations with different activation functions to assess the robustness of their findings.

3. Theorems 4.4 and 4.5 rely on Conjecture 4.3. However, this conjecture is not well stated in the main text. It would be also better to explain the difficulty of the proof and why this conjecture cannot be proved by previous results like Hu&Lu, (2023) and Ba et al. (2022). The conjecture is a critical component of the analysis, and its lack of justification weakens the theoretical claims. The authors should provide more insight into why existing techniques cannot be directly applied and what specific challenges are involved in proving this conjecture. The connection to prior work should be made more explicit, highlighting the novel aspects of the conjecture and the technical hurdles it presents.

### Questions
1. In Section 2.1, the scaling of the neural network is different from Ba et al. (2022). In Ba et al. (2022), they used a mean-field regime with learning rate $\eta\sqrt{N}$ and there is an extra $1/\sqrt{N}$ for the second layer $\mathbf{a}$. Is this regime the same as the setting of this paper?

2. The initialization of $\mathbf{W}_0$ is sampled from a uniform distribution on the unit sphere, which is different from the Gaussian initialization of Ba et al. (2022). I guess this initialization will make the analysis simpler, e.g. Lemma B.1 can be applied directly. This should be mentioned somewhere in the paper and explain why you use this initialization.

3. Condition 2.3 assumes that $\sigma$ has bounded first three derivatives but this won't be true if you consider the general polynomial activation function, which is set in Theorem 3.3. For Theorems 3.4, 4.1-4.2, and 4.4-4.5, do you only consider $\sigma$ as a polynomial or center ReLU function? I am confused why Theorem 3.3 needs polynomial activation functions which may contradict with Condition 2.3.

4. For Figure 2, are the locations of the spikes and the alignments empirically simulated or can you predict them from your theory? From Theorem 3.4, these alignments should converge to one, right?

5. In Theorem 3.3, how about the case when $\alpha=(\ell-1)/(2\ell)$? Any observations in this critical regime?

6. [1] and [2] also studied the initial feature matrix $\\mathbf{F}_{0}$. And [1] also presented the limit of training error for random feature ridge regression but with a slightly different definition than yours.

7. Above Theorem 3.4, vector $\mathbf{w}_i$ is not defined.

8. Below (4), why does $c_{>1}$ also include $c_1$?

9. For Theorems 4.4 and 4.3, can you say something about some extreme cases? For instance, $n\gg N,d$ or $N\gg n,d$. 

10. In Section 4.2, why not present the theory of training loss for general $\ell$ like Appendix L? Can Appendix L directly cover Theorems 4.4 and 4.3? Besides, using Appendix L, can you plot Figure 3 (Right) and show that the training loss is always decreasing?

11. I cannot see how Figure 3 (Left and Middle) matches Theorems 4.4 and 4.3 for training loss with $\log\eta/\log n<1/4$ or $1/4<\log\eta/\log n<1/3$. You may need to point out the threshold in the figures. Besides, in the middle figure, why is the testing error increasing for setting 1 with a large learning rate? Can you explain this phenomenon here? It seems like in this case, we do not have improvement for feature learning. Besides, there should be a benchmark, the prediction risk for the best linear model in this figure to compare with the feature learning.

12. In Appendix A, a typo for the definition of $\mathbf{R}_{0}$.

13. Lemma B.1, do you need to require $\\|a\\|=\\|b\\|=1$?

14. In the proof of proposition 3.1, how do you use Lemma J.1 to derive the limit of $\boldsymbol{\beta}^\top\boldsymbol{\beta}_{\*}$?

15. In the proof of Theorem 3.4, how do you show the rank of the sum of the spikes is exactly $\ell$? Is it easy to see that $(\tilde{\mathbf{X}}\boldsymbol{\beta})^{\odot k}$ are linearly independent for different $k$?

16. In the final result of Appendix L, why is $c_{\*,0}$ also included in the asymptotic difference of the training errors? In $\ell=1,2$, there is no $c_{\*,0}$; see (5) and (6). And What is $M$ in the summation? There should be some discussion about this result.



==================================================================================================

[1] Louart, et al. "A random matrix approach to neural networks."  

[2] Fan and Wang. "Spectra of the conjugate kernel and neural tangent kernel for linear-width neural networks."

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors studied the effect of feature learning in a two-layer neural network, where the first-layer weight matrix receives one gradient update with large learning rate, and the target function is a single-index model. The main contribution is a spike decomposition of the feature matrix, where the corresponding singular vectors contain polynomial features of different degrees
depending on the scaling of step size $\eta$. This allows the authors to compute the asymptotic training error under a Gaussian equivalence conjecture and quantify the improvement in the loss due to feature learning.

### Strengths
This submission generalizes the result in (Ba et al. 2022) to step sizes that scales with $\eta\asymp n^\alpha$ for $\alpha\in (0,1/2)$, and provides a precise description of the nonlinear feature learning after one gradient update. Moreover, the authors identified a sequence of phase transitions with respect to the learning rate scaling, where a degree-$\ell$ spike appears when the exponent of the step size exceeds $\alpha^2>1-\frac{1}{\ell}$. This finding may motivate random matrix theory research on similar nonlinear spiked matrix models.

### Weaknesses
My main concern is that unlike (Ba et al. 2022), the theoretical results in the current submission does not translate to learning guarantees for the studied single-index teacher. As a result, it is unclear if a larger learning rate provides any statistical benefits, so the claim that *"for large enough step sizes, the model can learn non-linear components of the teacher function"* is not supported.  
In Figure 3 the authors plotted the test error which exhibits improvement due to the learning of the quadratic component, but such improvement is not proved, and the experimental setting is only for target function with information exponent $s=1$. In fact, by inspecting the formulae for $\Delta$, it appears that the test error cannot improve for $s>1$.   
This limitation needs to be explicitly mentioned in the main text.

I have the following questions regarding the figures in the main text. 

1. In Figure 2, do the crosses represent the theoretical predictions of the spike location? If so, how are these values obtained? 

2. In Figure 3, do the solid lines correspond to the analytic predictions based on Theorems 4.4 and 4.5? If so, why do we observe fluctuations in the curve?

### Questions
I have the following questions regarding the figures in the main text. 

1. In Figure 2, do the crosses represent the theoretical predictions of the spike location? If so, how are these values obtained? 

2. In Figure 3, do the solid lines correspond to the analytic predictions based on Theorems 4.4 and 4.5? If so, why do we observe fluctuations in the curve?

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper delves into the feature learning capabilities of two-layer fully-connected neural networks. It builds on the understanding that with a constant gradient descent step size, only linear components of the target function can be learned. The research introduces a varying learning rate that grows with sample size, which results in the emergence of multiple rank-one components in the feature matrix, each representing a specific polynomial feature. Through spectral analysis, it's shown that the feature matrix's spectrum undergoes phase transitions based on the learning rate, leading to the addition of separated singular values or "spikes". These spikes, as the paper demonstrates, are aligned with polynomial features of varying degrees, influencing the neural network's ability to learn non-linear components. The study establishes that the training and test errors of the updated networks are determined by the initial feature matrix and these spikes, with specific cases illustrating the network's capacity to learn quadratic components of the target function.

### Strengths
Strength:
1. Paper is well organized
2. I think this paper has a good contribution to understanding the learning dynamics of non-linear features by networks, with concrete improvements over Ba et al. 2022.

### Weaknesses
Weakness:
1. Based on my understanding, the core advantage of the proposed analysis is from the Hermite expansion of the activation layer, which can characterize higher-order nonlinearity and explain more non-linear behaviors than the orthogonal decomposition used in Ba et al. 2022. Please clarify this.
2. The required condition on the learning rate (scaling with the number of samples) is not scalable. I never see a step size grows with the sample size in practice, which will lead to unreasonably large learning rate when learning on large-scale dataset. I understand the authors need a way to precisely characterize the benefit of large learning rates, but this condition is not realistic itself.

### Questions
Question:
In Figure 3 left/middle: is the total number of training steps fixed? I.e. more iterations for small LR, and fewer iterations for large LR? This is important for a fair comparison between small and large learning rates.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies how neural networks learn the features with different learning rates. Specifically, this paper considers a setup of two-layer neural network under one-step GD with the step size $\eta=n^\alpha$, where $n$ is the number of training samples. 
This paper provides a theoretical characterization of how a specific choice of $\alpha$ influences the neural network's ability to learn various types of features.

### Strengths
The paper goes beyond the NTK region and characterizes the performance of the neural networks with a relatively large learning rate. Instead of doing lazy training, this paper shows the ability of neural networks to learn features and characterize the relationship between the learning rate and the learned features by the weights.

### Weaknesses
1. Assuming that the data follows a zero-mean Gaussian distribution is strong, and whether real-world data satisfies this assumption can vary. Specifically, when considering Gaussian data, it is assumed to exhibit symmetric properties, which are necessary for the proofs. However, it's important to recognize that not all real-world data inherently possesses such symmetrical properties.

2. The assumptions for the activation function are unclear. I had a hard time understanding Condition 2.3 and Condition 2.4. Could the authors directly tell us which activation functions satisfy these conditions? Specifically, the requirement of a Hermite expansion with a non-zero first coefficient ($c_1 \neq 0$) in Condition 2.3 seems restrictive. It would be beneficial to provide examples of common activation functions that meet this criterion and those that do not, along with a discussion of the implications.

3. More discussions are needed for the magnitude of $c_\star$. For example, for some common activation functions, like ReLU and Sigmoid,  where $M$ can go to infinity, I would like to learn about the dependence of the sample complexity. The current analysis does not clearly explain how the magnitude of $c_\star$ affects the convergence rate or the final performance of the network, especially in relation to the number of training samples.

4. I noticed that the theoretical results regarding the training loss are only provided for the cases where $\ell$ equals 1 and 2. While the authors mentioned that results for the general case of $\ell$ can be found in the Appendix, I believe it is essential to include and discuss these results in the main content. The absence of these results makes it difficult to assess the general applicability of the theory.

5. Show the decrease in training loss may not be surprising.  Instead, the focus should be on generalization and test error. The paper needs to address how the observed training loss behavior translates into generalization performance, which is a more critical metric for evaluating the practical utility of the proposed approach.

6. Emphasizing the technical challenges involved in deriving the proofs would make it easier to appreciate the technical novelty. Currently, it's challenging to discern these technical aspects when looking at the LONG proofs in the Appendix. The paper should highlight the specific mathematical tools and techniques used in the proofs and explain why they are necessary and non-trivial.

7. We need some experiments of higher-order feature learning to justify the theoretical findings in Theorem 4.1. The current experiments only validate the learning of linear and quadratic features. More experiments are needed to demonstrate the learning of higher-order features as predicted by the theory.

8. We need some numerical experiments on real data and deep neural networks to justify the theoretical findings. Currently, due to the strong assumptions on the input data and activation functions, it's challenging to envision practical applications. The paper should include experiments on real-world datasets to show the relevance of the theoretical results in practical scenarios.

### Questions
1. The setup of this paper and Zhenmei et al.2022 seems significantly different from my POV, but both are counted as feature learnings. It would be better to clarify the field of feature learning and how they are connected. 

2. The values of training error and test error are quite confusing. It would be helpful if the authors included some baseline measures to assess the algorithm's performance. Specifically, it's challenging to see the significance of studying an algorithm with a large test error.  While it may be caused by the scaling issue, the authors should consider making adjustments to avoid any misunderstanding.

3. How does Figure 2 change as the number of iterations increases?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
