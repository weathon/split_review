# Analysis of Learning a Flow-based Generative Model from Limited Sample Complexity

- Decision: Accept
- Avg Score: 6.33
- Scores: 3, 8, 8

## Abstract
We study the problem of training a flow-based generative model, parametrized by a two-layer autoencoder, to sample from a high-dimensional Gaussian mixture. We provide a sharp end-to-end analysis of the problem.
  First, we provide a tight closed-form characterization of the learnt velocity field, when parametrized by a shallow denoising auto-encoder trained on a finite number $n$ of samples from the target distribution. Building on this analysis, we provide a sharp description of the corresponding generative flow, which pushes the base Gaussian density forward to an approximation of the target density. In particular, we provide closed-form formulae for the distance between the means of the generated mixture and the mean of the target mixture, which we show decays as $\Theta_n(\sfrac{1}{n})$. Finally, this rate is shown to be in fact Bayes-optimal.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper in detail analyses the case of training a stochastic interpolation model on few samples from a bimodal Gaussian mixture model. All theoretic predictions are accompanied by experiments.

The first result 2.1 characterizes the solution that is obtained when training on a bimodal Gaussian mixture. It shows that the weight vector is contained in the span of $\mu$ (the displacement vector for the mixture components), $\xi$ (the mean of all latent points), and $\eta$ (the average offset of the data from the corresponding mean) and thus no other directions are relevant.

The second result 3.1 derives the resulting generative ODE and summarizes it in terms of the relevant space from result 2.1.

The third result 3.2 spells out the Euler integration of result 3.1.

The final result 3.3 shows that the distance and angle between the true $\mu$ and the estimated $\hat\mu$ reduce by $\Theta(1/n)$. This is the same as the Bayes optimal rate.

### Strengths
The paper considers an interesting question, how generative models generalize as a function of the number of training samples.

The solution for the bimodal Gaussian Mixture model appears sound and plausible.

All theoretical results are accompanied by experiments closely matching the prediction, increasing the credibility of the theoretical results.

### Weaknesses
I find the main technical result presented in a misleading way: Results 2.1 and 3.1 show that the weight vector and the ODE dynamic are not orthogonal to $\mu$. I think a better way to describe the behavior of the system would be to span the relevant space via $\eta$ and $\hat\mu_+$ and $\hat\mu_-$, corresponding to the empirical mean of the samples at $\pm\mu$. I assume that this is also sufficient to span the weight vector (please correct me if I’m wrong), and it would make clear that the model only has access to the empirical means. The remaining results could then be adapted to show how the sampling process is able to reproduce the empirical means of the two modes. Then, the Bayes-optimal baseline could be inserted to show that the empirical estimates go down with Theta(1/n), and that the flow is able to achieve the same rate.

I also find that the research question formulated in the beginning is not really addressed in the main text, whether the network architecture determines whether a generative model memorizes training data. If my above understanding is correct, then the model actually does learn the training data by heart (i.e. it predicts the empirical means), and the rate to the true solution is essentially given how fast empirical means converge to the mean of the generative distribution. Also, the rate $\Theta(1/n)$ is not affected by the regularization $\lambda$, and the network architecture is not varied so as to judge wether this particular setup has a particular convergence rate.

Minor points:
- Formatting of contributions via itemize
- Sentence? „Note that (9) is a special case of the architecture studied in Cui & Zdeborová (2023), and differs from the very similar network considered in Shah et al. (2023) in its slightly more general activation (Shah et al. (2023) address the case φ = tanh)“
- Result 3.1 Le X_t -> Let X_t
- finding that that the DAE on p. 9

### Questions
1. How many dimensions are needed to span $\hat w_t$ for all $t$? From a simple drawing of $\eta, \mu_+, \mu_-$ I conjecture that two dimensions are enough (similar to first weakness).

2. Why is $\mu \propto d$ a reasonable scaling? This seems like an unrealistic choice to me. In practice, data is often normalized say to a fixed range $[-1, 1]$ per dimension, so in order to obtain the scaling behavior the means have to be $\mu = (\pm 1, …, \pm 1)$, i.e. both mixture components are at the corners of the hypercube. Alternative question: Does the sample complexity also transfer to $\|\mu\|^2 < O(d)$, e.g. $O(1)$? I would guess that the other directions start playing a role then.

3. What is the solution to this simple setup intuitively? Can you provide a simple drawing of $0, \eta, \mu_+, \mu_-, \mu, \eta$ and a learnt trajectory? If the required dimension is indeed two, this should be easy.

4. What is the shape of the learnt distribution within the two clusters, i.e. what is the local density in each cluster?

5. Fig. 2: Why are the learnt means biased in one direction? Is more training data added sequentially?


Given the substantial weaknesses and the above questions, my *preliminary* vote for this paper is therefore not to accept it. I am happy to be corrected in any of the criticisms I raised and look forward to the authors' rebuttal.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors analyze a generative flow-based model to sample from a mixture of Gaussians, where at each timestep the vector field is parameterized by a two-layer neural network.
They consider a high dimensional finite sample regime with the number of samples scaling linearly in the dimension. 
Using tools from statistical physics they derive a precise characterization of the optimal performance.
Their experiments corroborate the theoretical findings.

### Strengths
- The strongest point is the exact characterization of all important quantities. 
- Clear and concise presentation of the results
- Solid experiments demonstrating the validity of the theoretical results

### Weaknesses
The approach seems to heavily rely on the gaussianity of the target distribution

### Questions
- Do you think this the same method could be used for more complex distributions, if yes what would be a concrete example?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies a certain asymptotic limit of a flow-based generative model that uses weight-tied fully connected network with skip connection to approximate the velocity field. In such scenario, under the isotropic gaussian mixture assumption the authors provide a characterization of training dynamics in the finite sample complexity regime. Notably, the resulting asymptotic behaviour of the learned cluster means enjoys the Bayes optimal rate of $O(1/n)$.

### Strengths
- a complete characterization of training dynamics of shallow generative flow under the isotropic mixture of gaussians assumption
- optimality of the resulting sample asymptotics
- a neat symmetric ansatz

### Weaknesses
 - lack of the correlation structure in the input data, which draws the conclusions to be less practical
- minor: the approach is still an ansatz

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
