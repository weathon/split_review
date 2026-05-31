## Human Reviewer 1

### Summary
The article studies the problem of learning latent representations of categorical variables. In particular, it examines the role of the softmax function, which maps a score vector to a valid categorical probability vector. The paper shows that this function leads to a dense Fisher Information Matrix (FIM) for a categorical random variable and argues that such dense matrices can introduce geometric distortions that may hinder gradient-based optimization.

To address this, the authors propose a new parameterized function, catnat, for learning categorical probability vectors. This function is designed to yield a diagonal FIM, potentially mitigating the aforementioned issues. Experimental results on three different tasks are presented to illustrate the performance of the proposed method.

### Strengths
The strengths of the paper are:
1. The paper examines the widely used softmax function from an Information Geometry perspective, which provides an interesting theoretical viewpoint.

2. A novel parameterized function (catnat) is proposed and analyzed as an alternative to softmax.

3. The experimental results appear to demonstrate improved performance compared to the softmax baseline.

### Weaknesses
1. The proposed function introduces additional hyperparameters, which may complicate training and tuning.

2. The advantages and underlying mechanisms of the new function are not clearly articulated.

3. The numerical results are difficult to interpret and do not strongly support the claimed benefits.

### Questions
Overall, the paper is well written and offers an interesting new perspective on the softmax function. However, several aspects of the current version need clarification and improvement.

1. Practical Relevance of the Approach:

The paper focuses on the softmax function and proposes a new parameterization for categorical random variables in the context of Information Geometry and Natural Gradient Descent. However, most modern machine learning and AI methods rely on standard gradient descent or stochastic gradient descent (SGD) due to the large scale of neural networks, where computing or inverting the FIM is infeasible. It is therefore unclear whether the proposed analysis and the new function are practically useful.

How does the catnat function perform when used with standard GD or SGD rather than natural gradients?

2. Justification of Claims about FIM and Geometry:

The paper claims that a dense FIM introduces geometric distortions, but it does not adequately explain why this occurs or what these distortions entail. The rationale behind why a diagonal FIM would alleviate this issue is also unclear.

Furthermore, since the activation functions a() and ν() used in catnat can take zero values, the resulting FIM could be singular.
Overall, the motivation for the new function is not fully convincing.

3. Hyperparameters and Computational Cost:

Softmax is simple, widely adopted, and free of hyperparameters. The proposed catnat function introduces parameters A and C, which must be tuned.

The paper should discuss the sensitivity of results to these hyperparameters and the computational cost compared to softmax, especially for large numbers of categories.

The computation of each probability entry in catnat involves multiple products of powers of activation functions, which could be expensive. A complexity analysis would be helpful.

4. Experimental Details and Interpretation:

Several details are missing or unclear in the numerical experiments:

(i) In Table 2, information about the graph sizes and GNN architectures is missing.

(ii) In Table 3, the reported negative log-likelihood values (e.g., 97.8 ± 0.2 vs. 97.5 ± 0.3) are very close, with overlapping error ranges. It is unclear whether such differences are statistically or practically significant.

Similarly, in Table 4, results such as 406 ± 34 vs. 398 ± 25 do not convincingly demonstrate improvement.

Overall, the empirical results do not clearly establish that the proposed function provides a meaningful advantage over softmax, especially given the added complexity and tuning effort.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Summary
The authors suggest an alternative to the Gumbel-softmax trick for the stochastic gradient estimator of the latent categorical random variables. The proposed catnat is an alternative parameterization of the softmax function, consists of sequential hierarchical binary splits, based on the concept called information geometry and natural gradient. The authors provide theoretical backup for the proposed method, and conduct wide range of experiments.

### Strengths
- The algorithmically proposed methodology makes sense.
- The theoretical basis was also appropriately presented.

### Weaknesses
- With the current shape of the paper, it is hard to understand how to apply the suggested method practically. Please provide the pseudo-code or algorithm of the proposed method.
- The experiments are wide, but very shallow. It is very hard to tell whether the suggested method is superior to the baselines. Thorough experiments against various stochastic gradient estimators for the categorical random variables should be conducted.

### Questions
- How can we implement the proposed method when num_category $\neq 2^n$?
- What is the computational complexity for the suggested method?
- Also, the computation cost should be compared against various baselines. Why are all the baselines missing?
- The following is missing baselines [1,2,3,4], at least for the VAE experiment.
- How does the variance of the stochastic gradient differ from the baselines?

[1] Mnih et al., Neural variational inference and learning in belief networks
[2] Gu et al., Muprop: Unbiased backpropagation for stochastic neural networks
[3] Tucker et al., REBAR: Low-variance, unbiased gradient estimates for discrete latent variable models
[4] Grathwohl et al., Backpropagation through the void: Optimizing control variates for black-box gradient estimation

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
5

---

## Human Reviewer 3

### Summary
The paper introduces a parameterisation of Categorical random variables aimed at inducing a diagonal Fisher information matrix, which, the paper argues, is poised to address many of the pitfalls of the typical softmax parameterisation. This works by parameterising the categorical probabilities as the result of a binary branching process (somewhat akin a stick breaking procedure).

The idea is tested on some latent variable modelling problems, though in rather simple settings of graph structure learning, categorical VAE, and an RL setting. Through different performance metrics in these tasks, the paper argues that the proposed approach (catnat) is better suited than softmax.

### Strengths
1. I find the parameterisation elegant
2. The paper is mostly rather clear

### Weaknesses
1. The paper argues that the proposed technique addresses challenges that countless other papers addressed by various other means, yet none of those, it seems, are relevant for the empirical section. I find this a big omission. Catnat is a novel parameterisation and, as far as the reader can tell, there's so much to be established: stability, computational tradeoffs, performance against other parametrisation aimed at similar issues, performance against reasonable gradient estimators, etc.

2. The paper misses an entire body of literature on sparse parameterisations (I'm thinking of the sparsemax family) for which a lot of work on inducing structure has been published (e.g., entmax, sparsemap, etc.). I'm listing only a fraction of the relevant papers in this line of work below: 

- https://proceedings.mlr.press/v48/martins16.html
- http://papers.neurips.cc/paper/6926-a-regularized-framework-for-sparse-and-structured-neural-attention.pdf
- https://proceedings.mlr.press/v80/niculae18a.html

It also misses other sparse parameterisations, for example those based on 'stretch and rectify' principle: 

- https://openreview.net/forum?id=H1Y8hhg0b
- https://openreview.net/forum?id=WAid50QschI

Are there worthwhile connections between these techniques and catnat? Do they address similar issues? Are they addressed by fundamentally different things? How do they fare in comparison, etc. The reader cannot tell.

3. The paper claims the proposed parameterisation is poised to address problems of the softmax parameterisation, and that the essence of the solution is that the Fisher information matrix is diagonal, but the paper does not discuss why this is expected to matter for the stability of the techniques used to train LVMs in this paper (ie, policy gradient, PPO, and the gumbel-softmax relaxation). I don't think this can be left for the reader to infer, the paper has to spell out the arguments clearly.

For the reasons above my judgment of soundness is as is.

### Questions
Other than the weaknesses above, I have a small question. 

Does something like the stick breaking construction, which the paper also fails to acknowledge, induce a Fisher information matrix somewhat like catnat's?

https://openreview.net/pdf?id=S1jmAotxg

### Soundness
1

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3