# Asymptotic Analysis of Two-Layer Neural Networks after One Gradient Step under Gaussian Mixtures Data with Structure

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
In this work, we study the training and generalization performance of two-layer neural networks (NNs) after one gradient descent step under structured data modeled by Gaussian mixtures. While previous research has extensively analyzed this model under isotropic data assumption, such simplifications overlook the complexities inherent in real-world datasets. Our work addresses this limitation by analyzing two-layer NNs under Gaussian mixture data assumption in the asymptotically proportional limit, where the input dimension, number of hidden neurons, and sample size grow with finite ratios. We characterize the training and generalization errors by leveraging recent advancements in Gaussian universality. Specifically, we prove that a high-order polynomial model performs equivalent to the non-linear neural networks under certain conditions. The degree of the equivalent model is intricately linked to both the "data spread" and the learning rate employed during one gradient step. Through extensive simulations, we demonstrate the equivalence between the original model and its polynomial counterpart across various regression and classification tasks. Additionally, we explore how different properties of Gaussian mixtures affect learning outcomes. Finally, we illustrate experimental results on Fashion-MNIST classification, indicating that our findings can translate to realistic data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a theoretical framework to study the training and generalization errors of a two-layer neural network under a more realistic assumption of Gaussian mixture data with additional low-dimensional structures and shows that a finite-degree polynomial model serves as an equivalent performance model, which can simplify the analysis of neural networks. Lastly, the paper compares the model performance using the “Hermite model” with Relu, Tanh, and Sigmoind functions in simulation data and real data generated with generation models and studies the impact of data spreading.

### Strengths
1. Theoretical framework of a two-layer neural network for more realistic data assumption;
2. A finite-degree polynomial model serves as an equivalent performance model.

### Weaknesses
Finding the weakness of the paper is beyond my current ability.

### Questions
No

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
1. This paper establishes a theoretical framework for characterizing the training and generalization errors of two-layer neural networks under Gaussian mixture data, while previous work mainly focuses on Gaussian data. 

2. This paper demonstrates that a finite-degree polynomial model serves as an equivalent performance model, simplifying the analysis of neural networks under the Gaussian mixture data assumption. 

3. Through extensive simulations, including classification tasks on Fashion-MNIST, this paper validates the findings and highlights the significant impact of data structure on learning outcomes.

### Strengths
1. The framework provides a novel lens for understanding neural networks trained on Gaussian mixture data with structured covariances, marking a clear advancement over previous works that lacked these structural considerations.

2. The paper includes a compelling mix of theoretical insights and numerical experiments, with applications to Fashion-MNIST classification. These experiments effectively validate the theoretical claims and underscore the significant impact of data structure on neural network learning outcomes.

### Weaknesses
1. The primary weakness lies in Assumption (A.3), which requires all Gaussian components in the Gaussian mixture model to be zero-centered. In my view, such a Gaussian mixture model does not introduce significant challenges, thus providing limited theoretical advancement in understanding neural network training. Specifically, $ E_{x\sim P}f = E_{x\sim N(0,\sigma_1^2)}f + E_{x\sim N(0,\sigma_2^2)}f + \cdots $; since $ x $ is always multiplied by the trainable weights $w$, a linear transformation of a zero-mean Gaussian can be reduced to the isometric case. This observation leads me to believe this analysis could be a straightforward extension of existing works that consider the isometric case.


2. The theoretical insights intended to guide the practical training of neural networks are unclear. Specifically, the connection between the proposed data model and real-world applications needs to be clarified. The motivation for extending beyond existing Gaussian distribution assumptions to study this particular type of data model also remains ambiguous.


3. The numerical experiments would be more compelling if implemented on larger-scale datasets, e.g., ImageNet.

### Questions
What prevents the analysis from covering cases with non-zero mean Gaussian components?

### Soundness
2

### Presentation
2

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
This manuscript investigates the training and generalization performance of two-layer neural networks after a single gradient descent step, under a structured covariate model given by a Gaussian mixture with finite-rank + identity covariance. The analysis is conducted in the proportional high-dimensional limit where the covariate dimension, hidden-layer width, and sample size diverge at constant rate. Leveraging recent progress in the Gaussian universality literature, the authors show that:

- After a single-gradient step on the first layer weights, the gradient admits a decomposition in terms of a rank-1 spike and a correction which is asymptotically small in operator norm.
- A conditional Gaussian equivalence theorem showing that the training and generalization errors after a single-gradient step are asymptotically equivalent to conditional Gaussian covariate model. This equivalence can be further written in terms of a Hermite decomposition of the non-linear activation.

Finally, the authors provide empirical validation via simulations on Fashion-MNIST classification tasks, supporting the theoretical predictions and highlighting how data structure influences learning outcomes.

### Strengths
This work is inscribed in the recent literature seeking to quantify feature after a single but aggressive gradient step in two-layer neural networks (Damien et al., 2022; Ba et al., 2022; Dandi et al., 2023a; Moniri et al., 2023; Cui et al., 2024). The main difference with respect to these works is in the data model, which includes a multi-modal model with structured covariance. The manuscript is well-written.

### Weaknesses
The main weakness is the lack of a close comparison with the related literature on the technical part of the work. Indeed, the authors do a good job in situating their contribution to the related literature in the general discussion (introduction, related works), but this falls short in the following. This is particularly problematic since the technical results heavily builds on previous work (in particular, the proofs in the appendix are based on reductions to previous results of Ba et al., 2022 and Dandi et al., 2023a,b). In the *Questions* below, I give a few pointers where I missed a discussion.



### Questions
- **[Q1]**: In L199-200:
> *"Notably, (Ba et al., 2022) established that a learning rate $\eta$ exceeding $\tilde{O}(\sqrt{k}) is necessary to surpass the performance of the linear model represented in equation (8)."*

In my understanding, (Ba et al., 2022) showed that the maximal learning rate is rather *sufficient* to achieve to surpass the performance of the best linear model. Indeed, (Moniri et al., 2023) showed that an intermediate scaling leads to partially learning non-linear components of the activation.

- **[Q2]**: You assume that all the means of the GMM are zero *"to simplify the analysis"* (Assumption A.3). While on a high-level I can see how the means can play a similar role to the spikes in the covariance (as you mention in the discussion that follows), this is an important simplification which should be better discussed. In particular, do you expect to see any effect of multi-modality which are not captured by the spiked covariance? If yes, it would be good to add a discussion on this. If not, please provide quantitive evidence of that.

- **[Q3]**: From the discussion of the conditional Gaussian equivalence (cGET, Theorem 3), it is not very clear how this result differs from the cGET proved by Dandi et al., (2023a,b). Only by going to Appendix B, one sees a more detailed discussion of how Thm 3 builds on previous results from Hu and Lu (2023) and Dandi et al. (2023b), and hence what are the key differences. I believe that it would be beneficial to the reader to have this discussion summarized in the main - in particular what results from (Hu and Lu 2023; Dandi et al., 2023b) are used and clearly stressing how Thm 3 extends / differs from them.

- **[Q4]**: Another point which I missed is a closer discussion on the relationship between the regime studied here and the ones from (Ba et al., 2022; Dandi et al., 2023a; Moniri et al., 2023; Cui et al., 2024). In particular, these works can be split in three different regimes:

    1. A regime where Gaussian universality holds and there is effectively no feature learning (performance is lower-bounded by a linear method) (Ba et al., 2022)
    2. An intermediate regime where there is partial feature learning (Moniri et al., 2023).
    3. Maximal update / critical step size: (Dandi et al., 2023a, Cui et al., 2024)

My understanding is that your Lemma/Theorem 1-3 holds covers all the regimes, while Theorem 4 is for an intermediate regime similar to Moniri et al., 2023. Is this correct? Would be good to add a more explicit discussion on that point. 

- **[Q4]**: Appendix A, L724-725 is confusing. Do you mean $f_{i}^{T}x$ is Gaussian distributed conditioned on the class?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors consider the problem of characterizing the hidden-layer features of a two layer neural network, after one gradient step on the first layer weights, in the asymptotic limit of comparably large dimension, width and number of samples. They consider (mixtures of) Gaussians with spiked covariance structure. They establish a conditional Gaussian equivalent map for the features, and further establish that the activation function can be replaced by a polynomial function with asymptotically equivalent test and train errors. Different aspects of the model (learning rate -to- data spread ratio, alignment between the spikes, cluster weights) are varied and their effect on the test error discussed. Many numerical experiments are performed to support or illustrate the discussion.

### Strengths
The paper is well written; results are sufficiently discussed and put in context. Section 6 provides ample intuition and discussion on the effect of the different parameters of the problem, allowing to illustrate and support the experimental results. Although I did not carefully check the proof, technical results seem sound.

Technically, the analysis of conditional Gaussian universality to structured covariances is interesting and relevant to extend the stream of recent related works to more realistic data distributions. In particular, the analysis of the joint scaling of $\eta, \lVert \Sigma\lVert$ is interesting, and provides a insightful picture of the tradeoff. I appreciated section 6, and in particular the discussion of the effect of the alignment between different covariance spikes.

### Weaknesses
 I do have a number of clarifying questions, which I list in the section below. Overall, I believe the work is sound and will be of interest to the community working on those topics. I do not give a higher score, because the paper leaves open rather natural questions which are naturally attached to its setting, beyond its current scope (namely establish Gaussian universality for the considered distribution). In particular :

- Can a description of the features spectrum be given in the case of a single-index target function, in the likeliness of Moniri et al. (2023)? Do the spikes persist, or are they altered by the presence of the structure in the covariances ?

- Is it possible to reach a tight asymptotic expression for the test and train errors?

In regards to this, I believe the title would gain to be slightly toned down slightly to be better representative of the scope of this paper, which the abstract accurately on the other hand reflects. I still stress however that the contribution is interesting and sound.

-  In (17), does $\hat{F}$ still refer to (12), namely the first layer weights after a gradient step on the _original_ network with activation $\sigma$, and not $\hat{\sigma}_l$? In other words, does the $\sigma\leftrightarrow \hat{\sigma}_l$ equivalence hold only when training the readout, or does it hold for the full training procedure, i.e. including when performing the gradient step on the first layer? This is not clear from the discussion in the main text.

- Can the authors add a discussion of why considering zero means (assumption A.3) is necessary, or if it can be relaxed to accommodate non-zero means ?  

- l. 410 : "This equivalence significantly simplifies our analysis by transforming the nonlinear activation into a polynomial form, thereby enhancing the tractability of the model while maintaining its performance characteristics." Can the authors be more specific on which point of the analysis this equivalence aids? This point, if any, is not sufficiently discussed in the current state of the manuscript.

### Questions
-  In (17), does $\hat{F}$ still refer to (12), namely the first layer weights after a gradient step on the _original_ network with activation $\sigma$, and not $\hat{\sigma}_l$? In other words, does the $\sigma\leftrightarrow \hat{\sigma}_l$ equivalence hold only when training the readout, or does it hold for the full training procedure, i.e. including when performing the gradient step on the first layer? This is not clear from the discussion in the main text.

- Can the authors add a discussion of why considering zero means (assumption A.3) is necessary, or if it can be relaxed to accommodate non-zero means ?  

- l. 410 : "This equivalence significantly simplifies our analysis by transforming the nonlinear activation into a polynomial form, thereby enhancing the tractability of the model while maintaining its performance characteristics." Can the authors be more specific on which point of the analysis this equivalence aids? This point, if any, is not sufficiently discussed in the current state of the manuscript.

### Soundness
4

### Presentation
4

### Contribution
2
