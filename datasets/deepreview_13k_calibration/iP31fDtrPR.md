# Learning Directed Graphical Models with Optimal Transport

- Decision: Reject
- Avg Score: 4.67
- Scores: 5, 6, 3

## Abstract
Estimating the parameters of a probabilistic directed graphical model from incomplete data remains a long-standing challenge. This is because, in the presence of latent variables, both the likelihood function and posterior distribution are intractable without further assumptions about structural dependencies or model classes. While existing learning methods are fundamentally based on likelihood maximization, here we offer a new view of the parameter learning problem through the lens of optimal transport. This perspective licenses a general framework that operates on any directed graphs without making unrealistic assumptions on the posterior over the latent variables or resorting to black-box variational approximations. We develop a theoretical framework and support it with extensive empirical evidence demonstrating the flexibility and versatility of our approach. Across experiments, we show that not only can our method recover the ground-truth parameters but it also performs comparably or better on downstream applications, notably the non-trivial task of discrete representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose to estimate the parameters of a Bayesian Network through minimization of the Wasserstein distance between the empirical distribution over observed variables and the marginal distribution of the observed variables of the model . They propose a method for computing this Wasserstein distance by introducing a collection of "reversed" kernels from observation to hidden variables.

### Strengths
The paper is clear.

### Weaknesses
It seems to me that gradient descent in equation 2 implies summing over all the parent nodes $PA_{X_O}$ , which seems very costly. If it is so, it is a limitation of the method. It would have been very nice to see how such a method compares to message passing algorithms for Bayesian Networks.

### Questions
How does the proposed gradient descent compare in terms of complexity with belief propagation?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the optimal transport framework for learning parameters of probabilistic models, called OTP-DAG. Authors show that minimizing the transport cost is equivalent to minimizing the data reconstruction error, with detailed proofs. Experiments on three models validate the effectiveness of the proposed OTP-DAG method in terms of both data reconstruction and parameter estimation. This validates the scalable and versatile feature of the OTP-DAG and implies the potential of its practicality.

### Strengths
* The proposed OPT-DAG is derived step-by-step with solid math proofs, makes the method clear and intuitive.
* The idea is versatile and scalable to different models and applications, which means broad practicality of the model
* The idea of combining the optimal transport and parameter learning of probabilistic models is interesting to me.

### Weaknesses
 * Some experiments are not that supportive and need to be improved. See questions.
* Latent variables inference is less discussed and compared in this paper.
* Page 2 line 8, "where the data distribution is the source and the true model distribution is the target". Do you mean that the data distribution is $p_{\theta}(x)$ and the true model distribution is $p_{\theta_{\text{true}}}(x)$? But VI is minimizing the KL divergence between the two posterior distributions, which is not the data distribution. These sentences are a bit confusing.
* For 4.1, could you please provide a table showing e.g. the mean error of the estimated parameters w.r.t. the true parameters from different methods? I know there are similar reports in Table 4 in the appendix, but could you find a problem where the estimated parameter is the best among all baselines?
* For 4.2, the synthetic dataset simulated from HMM is not credible to me. Why not really sample hidden $Z_t$ from the Markov process, but specify the state-changing points? Also, have you tried other settings (other true parameter sets, randomly sampled from a hyperprior distribution), and report metrics with means and error bars? In this way, we can be convinced that the proposed method is significantly better than others. Besides, why not also learn $p$, the transition probabilities? Since the traditional EM algorithm can also learn the transition matrix (as a learnable parameter) of HMM. If the proposed model is not even comparable to EM, this example application is only acceptable but not supportive.

### Questions
* Page 2 line 8, "where the data distribution is the source and the true model distribution is the target". Do you mean that the data distribution is $p_{\theta}(x)$ and the true model distribution is $p_{\theta_{\text{true}}}(x)$? But VI is minimizing the KL divergence between the two posterior distributions, which is not the data distribution. These sentences are a bit confusing.
* For 4.1, could you please provide a table showing e.g. the mean error of the estimated parameters w.r.t. the true parameters from different methods? I know there are similar reports in Table 4 in the appendix, but could you find a problem where the estimated parameter is the best among all baselines?
* For 4.2, the synthetic dataset simulated from HMM is not credible to me. Why not really sample hidden $Z_t$ from the Markov process, but specify the state-changing points? Also, have you tried other settings (other true parameter sets, randomly sampled from a hyperprior distribution), and report metrics with means and error bars? In this way, we can be convinced that the proposed method is significantly better than others. Besides, why not also learn $p$, the transition probabilities? Since the traditional EM algorithm can also learn the transition matrix (as a learnable parameter) of HMM. If the proposed model is not even comparable to EM, this example application is only acceptable but not supportive.

In summary, the score of 5 is not from the method part but from the experiments I mentioned above. I would like to increase the score, if authors are able to provide some extra competitive results from OTP-DAG with enough randomness of the choice of the true parameter when generating synthetic datasets.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a general approach to estimating the parameters of directed graphical models using Optimal Transport. The key idea is to relate minimization of reconstruction error with minimization of cost in OT. The approach has similarities to autoencoders and WAEs specifically. Three experimental evaluations are conducted showing that the approach is comparable to existing methods for parameter estimation in topic models, HMMs, and discrete representation learning.

### Strengths
- Optimal transport is a popular approach and there is broad interest in applications to various problems. 
- Parameter estimation in DAGs is a classic topic for which there is interest.

### Weaknesses
I find it hard to understand what the contribution of the paper is:
-- There are a number of relatively empty claims (a partial list is included below), which are a distraction.
-- The introduction seems relatively unrelated to the main contribution of the text. For example, the second paragraph contains related approaches that aren't systematically introduced in the main text. Why are we talking about these?
-- The contributions include: "showing that minimizing the transport cost is equivalent to minimizing the reconstruction error between the observed data and the model generation". This is not a clear statement of what is new. The authors themselves note that this has been used in VAEs for example, and that is not the only place.
-- The OT approach is introduced mathematically, but I didn't find useful insight into how it was or was not related to other approaches (aside from being OT).
-- The experimental setup is introduced before baselines. Any informative experimental setup should be chosen to expose interesting contrasts with baselines. The logic doesn't make sense.

Detailed comments: 
- The first sentence of the abstract isn't great. It is more informative to say what the problem is than to say it is a long standing challenge.
- "While existing learning methods are fundamentally based on likelihood maximization, here we offer a new view of the parameter learning problem through the lens of optimal transport." What is the new view? Is the intent to contrast OT with maximum likelihood?
- "Here we characterize them between two extremes." What is them?
- "As the complexity of the graph increases, despite the current advancements, parameter estimation in VI becomes less straightforward and computationally challenging." More details would be helpful here.
- "We present an entirely different view " In what way?
- I don't really understand the point of Figure 1.
- "laying a foundation stone for a new paradigm of learning and, potentially, inference of graphical models." What does this mean?
- "alternative line of thinking about parameter learning" What does this mean? Also, "Diverging from the existing frameworks"
- "We present theoretical developments showing that minimizing the transport cost is equivalent to minimizing the reconstruction error between the observed data and the model generation." Isn't this result already in the literature in multiple places? (It is fairly straightforward to show.)
- "While the formulation in Eq. (1) is not trainable," What does this mean?
- "for solving it efficiently " what is it?
- "Instead of achieving state- of-the-art performance on specific applications," Please say more. Why not?
- "We conclude with a more challenging setting: (3) Dis- crete Representation Learning (Discrete RepL) that cannot simply be solved by EM or MAP (maximum a posteriori). It in fact invokes deep generative modeling via a pioneering development called Vector Quantization Variational Auto-Encoder (VQ-VAE, Van Den Oord et al., 2017). " Please explain: what is challenging, why should we care about this model?
- "except the special setting of Discrete RepL" What makes this special?
- Not sure how I feel about the baselines appearing after the experimental setup. Shouldn't the setup be used to assess against the baselines?
- For LDA why isn't Gibbs sampling a baseline?
- The future research section is not particularly informative.

Overall the result is that I don't find the contribution clear or compelling. I believe there is something interesting here; however, I think there is a fair amount of work in repackaging (including possible new results) to have a compelling contribution.

### Questions
Please see the above comments. Perhaps the most important question to answer would be: What is the main contribution of the paper?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
