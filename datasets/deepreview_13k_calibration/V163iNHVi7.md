# Feynman-Kac Operator Expectation Estimator: An Innovative Method for Enhancing MCMC Efficiency and Reducing Variance

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
The Feynman-Kac Operator Expectation Estimator (FKEE) is an innovative method for estimating the target Mathematical Expectation  $\mathbb{E}_{X\sim P}[f(X)]$ without relying on a large number of samples, in contrast to the commonly used Markov chain Monte Carlo (MCMC) algorithm. This method uses Physically Informed Neural Networks (PINN) to approximate the Feynman-Kac operator. It enables the incorporation of existing diffusion bridge models into the expectation estimator, and significantly improves the efficiency of using Markov chains while substantially reduces the variance. Additionally, this method mitigates the adverse impact of the curse of dimensionality, weakening the assumptions on the distribution of $X$ and $f$ in the general MCMC expectation  estimator. In the algorithm implementation, the first step involves constructing a diffusion bridge over the target distribution or known data by matching the coefficients of the diffusion bridge from the random flow trajectories or a Markov chain. Subsequently, we employ PINN to solve the Feynman-Kac equation, and the solution of this equation provides the mathematical expectation in analytical form. Finally, we demonstrate the advantages and potential applications of this method through various concrete experiments, including the challenging task of approximating the partition function in the random graph model  such as the Ising model.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes to estimate expectations w.r.t. some target distribution $P$ by 
1. running some Monte Carlo algorithm to generate *some* samples approximately from $P$;
2. constructing a diffusion process in such a way that its stationary distribution approximately matches the target distribution; this is done by parameterising the drift and diffusion coefficients by neural networks which are then trained on the samples generated in Step 1;
3. approximating the solution in the Feynman--Kac formula via a deep learning method which represents the solution by a neural network whose training relies on $N$ paths sampled from the diffusion process constructed in Step 2.

Some limited numerical results are shown in the appendix.

### Strengths
The specific approach involving a seems novel. And any attempt at circumventing brute-force Monte Carlo approximation of expectations of interest would certainly be useful to the community.

### Weaknesses
 **1. Lack of clarity**

I'm afraid this work is not ready for publication purely on the basis of presentation alone.

* Most of the text is much too informal/needs to be more precise; and having the pseudo code only in the appendix is making this problem worse. For example, the description of the diffusion process lacks mathematical rigor, making it difficult to understand the precise dynamics being proposed. The use of terms like 'approximately matches' without quantifying the approximation error is problematic. Furthermore, the description of the neural network parameterization is vague, with no clear explanation of the network architecture or training procedure.
* Section 2 cites a number of works in which diffusions are employed in disparate contexts (summarising these works as discussing the same "diffusion model" seems strange). It would be more appropriate to clarify the specific type of diffusion model being used and how it relates to the cited works, as the term 'diffusion model' is very broad. The current presentation suggests that all these works are interchangeable, which is not accurate.
* Section 3.1 is a mess: I have now read it multiple times but I am still not sure which methods are actually used to find the parameters of the diffusion process and which methods are just "alternative" possibilities that the authors are not actually implementing. The lack of a clear distinction between the proposed method and alternative approaches makes it difficult to evaluate the contribution of the work. The authors should clearly specify the exact algorithm used for parameter estimation.
* There are many key terms whose lack of explanation/definition makes the paper difficult to understand, "sample collection process", "well-sampled points", "high-quality samples", "partial observations", "resampling", "moments" (from the context, I think the authors mean something like "time steps"), "RelMeanEst" ... For instance, what constitutes a 'well-sampled point' needs to be defined precisely in the context of the target distribution. The term 'partial observations' is also unclear, and the authors should specify what exactly is being observed and how these observations are used.
* The text reads like a first draft with numerous typos, randomly capitalised Words, some notation left undefined (or only defined in the appendix). The lack of attention to detail makes the paper difficult to read and understand.
* Similarly, the references/bibliography is full of errors/typos. This lack of care in the bibliography further undermines the credibility of the work.
* The headings in the tables in the appendix make it very difficult to understand what is actually being shown there. The experimental results are difficult to interpret due to the unclear presentation of the data.

**2. Lack of substantiation of claims**

The list of contributions on Page 2 makes some very strong claims. Among these are that the proposed methodology
* "can estimate expectations without succumbing to the limitations imposed by thecurse of dimensionality";
* "often exhibits superior efficiency" (compared to what?); The authors need to provide a clear benchmark for comparison. Is the claim that the method is more efficient than standard MCMC, or some other specific method? The lack of a clear comparison makes this claim unsubstantiated.
* "leads to a more efficient utilization of Markov chains. Notably, it necessitates fewer assumptions since it does not rely on the law of large numbers and the Markov ergodic theorem". The claim that the method does not rely on the law of large numbers and the Markov ergodic theorem is not entirely clear. While it might not directly use the ergodic theorem in the same way as standard MCMC, it is still based on sampling from a diffusion process which, under certain conditions, would be ergodic. The authors need to clarify this point and provide a more precise explanation of the assumptions their method relies on.

As far as I can tell, the manuscript does not actually provide convincing evidence in support of these claims. Indeed, the proposed methodology likely introduces approximation errors at numerous stages because

* the constructed diffusion only *approximately* admits $P$ as stationary distribution; The authors need to provide a quantitative analysis of the error introduced by this approximation. What are the conditions under which the approximation is valid, and what is the magnitude of the error?
*  sample paths generated from the diffusion (which are needed for approximately finding the solution of the Feynman--Kac formula) suffer from discretisation error; The authors need to address the specific type of discretization error and provide some theoretical bounds or empirical analysis of its impact on the overall approximation.
* the solution of the Feynman--Kac formula is only approximated via deep learning. The authors should provide details on the neural network architecture used to approximate the solution of the Feynman-Kac formula, as well as theoretical or empirical evidence of the accuracy of this approximation.

### Questions
It seems to me that the proposed method requires to run at least one MCMC chain long enough to obtain *some* samples from the target distribution $P$. 

Have we then not already solved the problem? I mean, I understand the argument from the manuscript that MCMC samples may be highly autocorrelated so that an approximation via the Feynman--Kac formula would be preferable. However, can the authors demonstrate that their approach (which incurs substantial additional computations needed for training the SDE parameters and solving the PDE) outperforms running the MCMC chain for just a while longer?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to compute the expectation under a distribution in a two-step approach. First, a diffusion bridge model is trained such that starting at an initial distribution at time 0 and evolving along an SDE till time T, the marginal distribution at time T follows approximately from the target distribution. Second, the computation of expectation can be transformed into the PDE given by Feynman-Kac equation, which is then solved with physically informed neural network. Some numerical experiements are given.

### Strengths
1. The presentation and writing is clear.
2. Adequate background and preliminaries are provided.

### Weaknesses
1. The claimed advantage of the proposed method seems to be doutable, or at least not supported in this paper. It is said that standard MCMC approaches suffer from long burn-in period, but the proposed approach requires training of neural network models at both the diffusion bridge model stage and the PDE solving stage, which to me seems a much higher cost. The computational cost of training these neural networks, especially for high-dimensional problems, is not negligible and could easily outweigh the cost of burn-in for many MCMC applications. Furthermore, the paper does not provide a clear comparison of the computational time required for their method versus standard MCMC, making it difficult to assess the practical advantage of the proposed approach.

2. The claim of reduced variance from the proposed approach seems not supported, and the approximations due to imperfect training of neural networks, discretization of PDE, etc, would cause a systematic bias towards the computed expectation. How much the bias is, and whether it can be bounded are also not discussed. The paper lacks a rigorous analysis of the error introduced by these approximations. Specifically, the impact of neural network training error on the accuracy of the expectation estimate is not quantified, and the discretization error of the PDE solver is also not addressed. Without such analysis, it is difficult to assess the reliability of the proposed method.

3. While it is claimed that the proposed approach can reduce the curse of dimensionality, the numerical experiments are all very low-dimensional examples. A simple Metropolis-Hastings/Gibbs sampler, or even an accept/reject or importance sampler could give very efficient and stable estimates of expectations. The experiments presented in the paper do not demonstrate the claimed advantage in high-dimensional settings. The low-dimensional examples used are not representative of the complex, high-dimensional problems where MCMC methods typically struggle. The lack of experiments in higher dimensions makes it difficult to assess the practical applicability of the proposed method.

4. Most MCMC samplers are targeted for generating samples from the distribution, which could be used for posterior inference etc. The proposed approach, however, can only be used to compute the expectation of one function. Say we want to compute the posterior mean, posterior variance and a 95\% posterior credible interval, then the proposed approach have to be used repeatedly for each quantity, while standard MCMC approaches only require one sampling chain. This limitation significantly reduces the versatility of the proposed method compared to MCMC. The need to retrain the neural networks for each different function makes it computationally expensive to obtain a full picture of the target distribution, which is a standard task in Bayesian inference.

### Questions
Even if we don't want to use standard MCMC samplers that involves a burn-in period, we have the alternatives of training a normalizing flow / diffusion model / stochastic localization process to sample from the target distribution and then computing the expectation based on the samples. How does the proposed approach compare to these methods, and what are their connections?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a connection of MCMC expectation estimators with the Feynman-Kac equation and proposes to solve a bridge-matching problem to estimate the MCMC expectation.

### Strengths
* The paper proposed a novel approach to connect partial differential equations and Markov chain Monte Carlo.

### Weaknesses
The paper does not contain any of the experimental results in the main submission. The main text should be self-contained and present at least part of the representative results. Remember that the reviewers are not obligated to look into the supplementary material.

The current state of writing makes it very hard to grasp the gist of the proposed methodology. Let me elaborate on a few examples:
* For Section 2, the related work mixes up MCMC methods based on simulating the Langevin diffusion, score function modeling based on Langevin diffusion, and bridge matching. These are very different ideas for solving different problems. Thus, the way this section is written confused me rather than putting the work in the context of previous works.
* In Section 3.1, a key aspect of the methodology seems to solve a bridge-matching problem with respect to the samples of some MCMC chains. However, I could not find the specifics of the authors’ approach anywhere in the main text. Only after looking at Algorithm 1 in the appendix I found that some loss functions are being minimized. The definition of these loss functions should have been in the main text.
* For Section 3.2, the authors do not provide enough explanation/motivation/proof as to why the reverse solution of the Feynman-Kac equation is the right conditional expectation. Again, the paper is expected to be self-contained to a certain degree.

Furthermore, I have some concerns about the technical claims of the paper:
* The paper claims that the proposed methodology "necessitates fewer assumption since it does not rely on the law of large numbers and the Markov ergodic theorem." However, it does rely on a strong assumption: that we are able to solve the PDE! That is, the paper does not contain any proof of the accuracy of the solution of the proposed differential equation. Even if, mathematically, the differential equation's solution is the desired conditional expectation, discretizing and numerically solving this is a completely different story. This is crucial in an MCMC setting since empirically assessing the quality of samples/expectation estimates is very challenging.
* One of the key motivations seems to be replacing the need for discarding burn-in samples. However, I do not quite understand how this is true when the paper tries to match the output of an MCMC estimator. This will contain non-asymptotic bias that can only be resolved through burn-in. Then wouldn't trying to match this end up inheriting the bias?
* The paper claims that the method "enhances efficiency through one-time training." However, I do not quite see how this improves anything. Couldn't I run MCMC longer instead of solving a differential equation? In fact, if we assume that solving differential equations indeed provides the right expectation, couldn't MCMC be regarded as an efficient way to solve this equation without involving any solvers? How much faster, precisely, is solving the equation rather than running MCMC?

Lastly, the idea of connecting MCMC expectation estimators with partial differential equations is not new [1-4], and a literature is already building around it. While the approaches of these works are different, and I'm not saying that this work lacks novelty in that regard, I believe these works actually do what the paper seems to have attempted to do: post-process the output of an MCMC algorithm to improve the performance of the expectation estimator. Furthermore, they come with asymptotic and non-asymptotic consistency guarantees and work incredibly well in practice! Thus, I believe the paper should have compared and discussed these methods.

### Questions
no questions.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduced a Feynman-Kac model approach for estimating mathematical expectations.

### Strengths
The proposed approach can potentially lead to more accurate estimations for mathematical expectations.

### Weaknesses
1. The paper's presentation is poor, lacking the algorithm and numerical results in the main text. It makes the proposed method inaccessible to the readers. The absence of a clear, step-by-step algorithm within the main body of the paper makes it difficult to understand the practical implementation of the proposed Feynman-Kac model. Furthermore, the lack of numerical results directly in the main text prevents a quick assessment of the method's performance and effectiveness.

2. Some notation is used in Algorithm 1 without proper definition, e.g., MSE(.,0). The use of 'MSE(.,0)' within the algorithm without a prior definition introduces ambiguity and makes it challenging to follow the algorithmic steps. Specifically, it is unclear what the arguments of the MSE function represent in this context, and what the '0' signifies. This lack of clarity hinders the reproducibility and understanding of the method.

3. The proposed method lacks theoretical guarantees. The paper does not provide any theoretical analysis to support the convergence or accuracy of the proposed method. Without such guarantees, it is difficult to assess the reliability and robustness of the method, particularly in different scenarios or with varying parameters. The absence of theoretical proofs raises concerns about the method's general applicability and limitations.

### Questions
1. How is MSE(., 0) is defined? 

2. Add more explanations or theoretical proofs for the statement that ``the solution to the Feynman-Kac equation at the initial time is E(f(X_T)|X_0=x_0).

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
