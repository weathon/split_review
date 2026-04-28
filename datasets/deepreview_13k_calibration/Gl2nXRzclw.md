# Robust Gaussian Process Regression with Huber Likelihood

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Gaussian process regression in its most simplified form assumes normal homoscedastic noise and utilizes analytically tractable mean and covariance functions of predictive posterior distribution using Gaussian conditioning. Its hyperparameters are estimated by maximizing the evidence, commonly known as type-II maximum likelihood estimation. Unfortunately,  Bayesian inference based on Gaussian likelihood is not robust to outliers, which are often present in the observational training data sets. To overcome this problem, we propose a robust process model in the Gaussian process framework with the likelihood of observed data expressed as the Huber probability distribution. The proposed model employs weights based on projection statistics to scale residuals and bound the influence of vertical outliers and bad leverage points on the latent functions' estimates while exhibiting a high statistical efficiency at the Gaussian and thick-tailed noise distributions. The proposed method is demonstrated by two real-world problems and two numerical examples using datasets with additive errors following thick-tailed distributions such as Student's t-, Laplace, and Cauchy distribution.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel method for robust gaussian process regression by using huber likelihood, which can deal with outliers in both covariate and output spaces. For covariate outliers, the paper introduces a projection pursuit weights to adjust their influence. For output outliers, the paper uses the huber likelihood. The posterior distribution, while intractable, is shown to be unimodal. Two approximate inference methods are proposed for this model, one based on MCMC and another based on Laplace approximation. Both methods are tested on a range of synthetic datasets and a real-world application on transmission spectroscopy, demonstrating their robustness and effectiveness.

### Strengths
- The proposed method is well-motivated to address previous approaches' sensitivity to heavy outliers. 

- The choices of Huber likelihood and 

- The presented model and inference procedure are easy to follow. 

- the proposed Laplace approximation (LA) inference method seems to have favorable empirical and runtime performance.

### Weaknesses
The biggest advantage of the paper is that the advantage of the proposed approach is unclear. 

First, while the use of huber likelihood is natural, there seems be a lack of discussions on the theoretical properties of Huber likelihood when compared to other robust likelihoods, e.g. student t, and their implications in Gaussian processes framework. Making this point clear would make the paper's contribution more significant other than just combining Gaussian process with any existing robust likelihood model. Specifically, a discussion on the conditions under which Huber likelihood provides a better fit than alternatives like Student's t, particularly in the context of non-Gaussian noise and heavy-tailed distributions, is missing. The paper should also address the potential impact of the Huber loss's non-differentiability at zero on optimization and convergence. 

On the empirical side, more thorough experimental details need to be presented. For each of the table presented, how many random simulations are run and what are the standard errors? See more comments on empirics in the questions below. 

Finally, it would be great of have a -brief introduction of the RCGP approach, which is served as an important baseline in the paper.

### Questions
- In the motivating figure 1, what is the result from your proposed approach? Also can you plot the true sinc function?

- the paper claims that no additional hyperparameters need to be chosen. But there are indeed threshold parameters $b$ and contamination parameters $epsilon$ required for the Huber model. The last paragraph in section 4 discusses  one particular configuration, is this what the authors meant by eliminating the need for setting them?

- Experiment 6.1, can you elaborate the difference between Case 1 v.s. Case 3 (or Case 4)? Is is just that in case 3 & 4, outliers in y space are closer to the main cluster of the data?

- In table 1 (and other tables), no standard errors are reported. Also, in the first row of Tbale 1, Huber LA with RMSE 0.25 is better than Huber MCMC with RMSE 0.37, but why the latter is bolded. Same question regarding the first MAE row. Please go through the table to make sure the bolded numbers are indeed the best performance.

- Figure 2: where is the result for HuberMCMC? Also it would be nice to have a more concrete description on each method's qualitative performance. 

- Figure 3.a: How are the mean function and GP-Huber curves obtained? 

- Figure 3.b: Describe the red bands and the dots. 

- Exp 6.4: Did the authors compare the GP-Huber model to other approaches?

### Soundness
2

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
5

### Summary
The paper proposes a robust Gaussian process regression model in covariates and outputs. For the output outliers, the authors propose to use the Huber likelihood, reducing deviations caused by outliers in output data. This likelihood yields a non-conjugate posterior, so the authors propose to use two standard ways to deal with intractable posteriors: Laplace approximation and Gibbs sampling. The paper employs a distance-based down-weighting scheme for outliers in the input space.

### Strengths
Input and output outliers are a relevant problem in the GP community, and I think the method could have a real impact on that.

### Weaknesses
I find it challenging to identify the main contribution of this paper. On the one hand, it presents a method for handling output outliers using the Huber likelihood. On the other, it proposes a process to guard against covariate outliers.

However, the authors treat both methods as a single approach in the experiment section, which is surprising since the projection technique could be applied to other GP models to make them similarly robust to covariate outliers. This treatment blurs the paper’s contribution and makes it challenging to follow. I would recommend distinguishing between the two methods more clearly, as this could clarify each contribution's unique impact and utility.

I find Figure 1 not easy to understand. I don't see the real benefits of using a 3D example here since the position of a 2D example will be much clearer. 

The authors claim that 'Our approach does not introduce Huber likelihood specific parameters in the posterior inference, avoiding the need for additional model-specific tuning'. However, I think this is somehow misleading since the model introduces two extra parameters $\beta$ and $\epsilon$. While the authors suggest a heuristic to set both parameters (which assumes that you want to guard against 10% outliers ), the method doesn't indeed add extra parameters.

The comparison in Table 1 seems unfair, as none of the methods compared account for covariate outliers. I believe this is the primary reason the Huber methods outperform the others. This becomes more evident in Tables 2 and 4, where it's unclear whether the proposed method consistently outperforms the rest. 

Similarly, if the authors propose a method to handle covariate outliers, it should be compared with other methods that address the same issue.

### Questions
- I find Figure 1 not easy to understand. I don't see the real benefits of using a 3D example here since the position of a 2D example will be much clearer. 

- The authors claim that 'Our approach does not introduce Huber likelihood specific parameters in the posterior inference,
avoiding the need for additional model-specific tuning'. However, I think this is somehow misleading since the model introduces two extra parameters $\beta$ and $\epsilon$. While the authors suggest a heuristic to set both parameters (which assumes that you want to guard against 10% outliers ), the method doesn't indeed add extra parameters.

- The comparison in Table 1 seems unfair, as none of the methods compared account for covariate outliers. I believe this is the primary reason the Huber methods outperform the others. This becomes more evident in Tables 2 and 4, where it's unclear whether the proposed method consistently outperforms the rest. 

- Similarly, if the authors propose a method to handle covariate outliers, it should be compared with other methods that address the same issue.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a Gaussian Process regression that is robust towards extreme output outliers. The GP is based on a Huber likelihood leading to GP-Huber posterior distribution that is estimated using Laplace approximation. The authors also propose to address the input  outliers by introducing a projection pursuit weights that alleviates their influence on the model performance. The efficiency of the method is demonstrated on simulated data and real-world data, compared to the Robust Gaussian Process introduced by Altamirano et al (2024). The authors also provide some numerical results on transmission spectroscopy experiments.

### Strengths
Overall, the paper reads well and is easy to follow. The paper makes some good contributions to the field of robust GP regression research.

- The authors propose to use a Huber likelihood which leads to a GP-Huber posterior distribution. Theorem 1 ensures that the GP-Huber posterior is unimodal, which enables to perform inference and hyperparameter optimization. Using Huber loss to address robustness is known, but its use for GP regression seems to be new. 

- The authors also introduce some weight pursuit to address the issue of having both corrupted output and corrupted input. The method seems to be efficient and easy to implement. 

- The authors propose to use the Laplace approximation and MCMC approximation to compute the intractable integral. This enables to compute predictive points and to optimize the marginal likelihood. Although this approach is standard in variational inference for GP regressions, the paper addresses the subtleties that come from the choice of Huber density. In particular, they use the pseudo-Huber loss to ensure continuity of the derivatives. 

- The numerical experiments are well explained and they show the efficiency of the approach. Especially, the transmission spectroscopy experiment shows the relevance of the approach in a specific context.

### Weaknesses
Although I like the paper, I find that the paper presents some weaknesses.

- Although it looks like Huber likelihood has not been used for GP regression, the approach combines a number of known variational inference tools (MCMC and Laplace approximation). Here I am not questioning the relevance of the approach but rather I am just pointing out that the main results of the paper are somewhat expected.

- A naive comment: It seems that the approach performs better than the state-of-the-art on the extreme outlier cases. (Case 2) However, the performance does not seem better for milder outlier cases. (Case 4). It looks like the model is performing well on the extreme cases. However, in practice, these extreme outliers are often removed from the training set through a preprocessing step (using some basic thresholding). Could the authors discuss about the main differences between "extreme cases" versus "easier cases"?

- Of course, extreme outliers is an important issue and the presented model is highly relevant to treat such cases. However, identifying outliers is more challenging when the variance $\sigma^2$ increases and/or when the variance is heteroscedastic with some high variations areas. This would be interesting to observe the behavior of the model in such cases. A subsequent question is: Would it be possible to extend such model to heteroscedastic variance? Maybe the authors could discuss potential challenges that might raise from such a model extension?

- The choice of $\varepsilon$ and $b$ seems to be crucial and I like the paragraph explaining their impact. However, this leads to a naive question from a practitioner point of view. How would we know how to set such parameters? How does a conservative choice of $\varepsilon$ and $b$ impact the model efficiency when the presence of outliers is overestimated? The aim of this question is not to criticize the issues addressed by the model but rather to question the practical limitations. How should a practitioner proceed to set such parameters?

Minor comments:

- In first rows of Table 1, the numbers in bold are not the right ones.  
- It would have been interesting to see the posterior mean results of RCGP in Figures 2,5, 6 and 7. This would help to understand where this model fails in the mean reconstruction.
- I encourage the authors to provide a bit more details about the setting of experiments in Section 6.1 and Section 6.2.

### Questions
See the first questions in the previous section.

- It seems that HuberMCMC performs poorly on the Energy dataset (Section 6.2) for focused outliers. How would the authors explain it? 

- How do the authors generate cases 3 and 4 compared to cases 1 and 2? It seems that the output data are upper bounded in Figures 6 and 7.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper considers the problem of performing GP regression in the context of likelihood misspecification. More specifically, the paper considers the use of two tricks: (i) replacing the Gaussian likelihood with a Huber likelihood, (ii) standardising residuals to reduce the impact of outliers in covariate space. Combined, these trick lead to a method which seem to perform well (in terms of accuracy) on problems where outliers are present in covariate space. Unfortunately, the use of the Huber likelihood breaks conjugacy, and so the authors propose two approximations of their posterior: one based on MCMC and the other based on a Laplace approximation.

### Strengths
I found it particularly interesting that the present method can deal with outliers in covariate space as well as outliers in the response. As the authors correctly point out, this is something that some of the existing methods really struggle with.

### Weaknesses
Presentation:
- Overall, I found the paper to be poorly written. There are numerous times where there are clearly missing words or sentences which do not make much sense. For example, on l134-135: "and the resulting posterior distribution on f as where" or l232: "By retaining the optimization-friendly propertie of convex problems ensured by to unimodality". These are just two examples, but there are many more and the authors should really focus on polishing the paper much more than it currently is.

- The figures/illustrations in this paper are of poor quality. It is hard to see what these figures are presenting without zooming very strongly. Even after doing so, it is hard to intepret these figures, and the captions do not tend to be particularly helpful. For example, in Figure 1, What does the coloring mean? Why is there no scale for what the coloring refers to? Why are the axes not named?

Comparison to existing methods:
- The discussion of computational cost is really minimal. Sure, the methods seem to perform well in terms of accuracy on the problem studied, but it is of course important to acknowledge that their cost will typically be much larger than for standard GPs. Currently, you are only providing cost for a simple one dimensional problem, which doesnt seem very representative. The paper could therefore clearly do with a detailed section discussing computational cost, and then a detailled assessment of the computational cost in the numerical experiments.

- The comparison and representation of Altamirano et al. 2024 is not always fair and at times even misleading.

For example, l52-53 on p1 states: "compared to the earlier work of Altamirano et al 2024 [...] added hyperparameters (\beta, c), did not support maximum likelihood estimation of hyperparameters [...]".

Firstly, the method of Altamirano et al works with a general weighting function, and the authors happen to parametrise such a weighting function with \beta and c and explain how to set these parameters. This is exactly what the present paper does with b and \epsilon (in fact b acts very similarly to \beta, whilst c acts very similarly to \epsilon). So it is misleading to imply that RCGP has additional hyperparameters compared to the proposed method.

Secondly, since RCGPs use generalised Bayes, using the maximum likelihood does not make sense (since the model is misspecified) and they therefore propose to use cross-validation, which is very widely used in the GP literature. This is shown to perform well. In the present paper, the authors propose to maximise the marginal likelihood for a model they know to be misspecified, which does not make much sense. Therefore saying that RCGP do not use the marginal likelihood and presenting this as a weakness without any evidence that it is seems unfair.

I am also wondering if the implementation of RCGP is done in a fair way. RCGPs are specifically well suited for GP regression where the Gaussian likelihood is mostly correct up to a small number of corrupted observations. This is clearly not the case in some of the settings that are studied in the experiments, which explains why RCGP may perform poorly. As discussed in the paper (l224), the authors expect a large number of extreme observations and therefore select b/\epsilon accordingly (this is certainly the case for the first experiment when setting). Does this mean you selected \beta/c for RCGPs accordingly to the recommendations in Altamirano et al to ensure that the methods are comparable? Sadly I was not able to verify this by looking at the code submitted. Also, which prior mean function was used? As discussed in the paper RCGPs perform poorly with a poor prior mean, so it would be interesting to see how the impact of this choice changes the behaviour of the method and whether this impacts how competitive it is.

- Theory: Theorem 1 is stated without a single assumption, but presumably you do indeed need assumptions for the result to hold. For example, what value of n does this hold for? Are the limitations on the various parameters needed for this to hold? For example, the inverse of the Gram matrix must be well-defined for v to be well-defined. What conditions on the kernel are needed for this? I would strongly recommend that this is formulated and proved more formally.

### Questions
- Can we really say that Huber-likelihood methods are preferable to alternatives in the settings you have studied? The answer of course also depends on computational cost. Therefore, please provide a full comparison of computational cost between all methods and for all experiments. Without this, it is not possible to make broad claims about HuberMCMC and HuberLA being preferable to existing methods. Please also provide details of your implementation and computational resources used. For example, how many iterations of gradient descent did you do for selecting hyperparameters of RCGP, and is this comparable to what you use for other methods? 

- Have you considered using your standardised weights with other methods? Please provide an implementation of RCGP where the weights are selected according to your proposed standardised residuals instead of the weight proposed by Altamirano. This should be a straightforward modification of your existing code, and would allow us to check how much is gained by the Huber likelihood and how much is gained by the standardised residuals. 

- Have you looked at how the selection of hyperparameters b and epsilon impact the performance of your method? Please provide full algorithmic details for every method you are using, as well as details of how hyperparameters were selected in each case. I would also strongly recommend a study of how this choice of hyperparameter impacts the performance of the method, and how this compares to competitors.

- Why is the last experiment only performed with Huber-based methods? I think it would make sense to implement all competitors on it to get a full picture of what is happening here.

- Is it possible to prove theoretically the robustness of the approach? If not, this should probably be mentioned as a drawback. But if so, then it would be worth adding this result.

### Soundness
2

### Presentation
1

### Contribution
2
