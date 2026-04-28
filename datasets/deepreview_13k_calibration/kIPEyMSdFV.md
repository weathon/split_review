# Reverse Diffusion Monte Carlo

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
We propose a Monte Carlo sampler from the reverse diffusion process.
Unlike the practice of diffusion models, where the intermediary updates---the score functions---are learned with a neural network, we transform the score matching problem into a mean estimation one.
By estimating the means of the regularized posterior distributions, we derive a novel Monte Carlo sampling algorithm called reverse diffusion Monte Carlo (rdMC), which is distinct from the Markov chain Monte Carlo (MCMC) methods. We determine the sample size from the error tolerance and the properties of the posterior distribution to yield an algorithm that can approximately sample the target distribution with any desired accuracy. Additionally, we demonstrate and prove under suitable conditions that sampling with rdMC can be significantly faster than that with MCMC. 
For multi-modal target distributions such as those in Gaussian mixture models, rdMC greatly improves over the Langevin-style MCMC sampling methods both theoretically and in practice. 
The proposed rdMC method offers a new perspective and solution beyond classical MCMC algorithms for the challenging complex distributions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers a diffusion modelling approach to the classical problem of sampling from an unnormalised density.

### Strengths
Sampling with reverse diffusions seem to have multiple advantages (compared to usual Langevin dynamics) in terms of how the algorithms behave. This paper builds on this observation and tries to bring the diffusion modelling methodology into regular Monte Carlo sampling.

### Weaknesses
 Unclear writing and claims not supported rigorously. See more below in the questions part.

My questions are as follows.

1) at multiple points, the paper claims that the SDE resulting from the diffusion approach has better behaviour, e.g., the last sentence of Section 2.1 claims that the isoperimetric constant of this SDE is better. Right after Lemma 1, another claim is made "It is important to point out that the property of $q_{T-t}(\cdot | x)$ is better than $p_*$". Here as well, the sentence is badly written (what property?) But in any case, these claims, as far as I am able to see are not rigorously proven.

2) Theorem 1 *assumes* that $q_{T-{k\eta}}$ is log-Sobolev, instead of proving something about it. As such I think the whole motivation is unclear as authors didn't show how ill-posedness is tackled by reverse diffusion approach.  Can authors show, if $p_*$ has a log-Sobolev constant, then $q$ does actually have a better behaviour in terms of this constant?

Small comments:

- In Lemma 1, point out where the proof is in Appendix

### Questions
My questions are as follows.

1) at multiple points, the paper claims that the SDE resulting from the diffusion approach has better behaviour, e.g., the last sentence of Section 2.1 claims that the isoperimetric constant of this SDE is better. Right after Lemma 1, another claim is made "It is important to point out that the property of $q_{T-t}(\cdot | x)$ is better than $p_*$". Here as well, the sentence is badly written (what property?) But in any case, these claims, as far as I am able to see are not rigorously proven.

2) Theorem 1 *assumes* that $q_{T-{k\eta}}$ is log-Sobolev, instead of proving something about it. As such I think the whole motivation is unclear as authors didn't show how ill-posedness is tackled by reverse diffusion approach.  Can authors show, if $p_*$ has a log-Sobolev constant, then $q$ does actually have a better behaviour in terms of this constant?

Small comments:

- In Lemma 1, point out where the proof is in Appendix

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the problem of reverse diffusion Monte Carlo and shows that the score estimation can be viewed as a mean estimation problem by exploiting a decomposition of the transition kernel. The theoretical properties of the proposed method are extensively analysed. The performance of the proposed method is assessed on the Gaussian mixture models; it is illustrated that the proposed approach performed better than existing Langevin-type MCMC methods.

### Strengths
-	Extensive theoretical analysis of the proposed method.

-	Good performance on (a single) toy example.

### Weaknesses
-	It is quite hard work to verify the theory. I would expect nothing less from such a paper, so by itself, it is, of course, not a problem. However, I believe there is room for improving the clarity and flow of the proofs. 

-	With the current presentation of the results, it is hard to verify the reproducibility of the results; in the experiments, the robustness of the algorithms to the input hyperparameters (for example, the choice of step size \eta in Algorithms 1/2).

-	 In D2 (proof of lemma 2 and 3): the paper refers to Proposition 2 in Ma et al. (2019). However, I cannot find the Proposition 2 in Ma et al. (2019).

-	Lemma 9: not an obvious mismatch between the statement of the lemma and the final line in the proof (RHS of inequality is d/mu for the former, 1/mu for the latter);

-	The proof of lemma 9 starts with “It is known that LSI implies Poincare inequality with the same constant,…”. Perhaps a reference would help.

### Questions
It’s ok that for a non-expert in the specific topic, it may be hard to go over the proofs. However, I believe that a good and precise presentation of the theoretical results can lead to even a non-expert with enough theoretical background to follow and verify the results. Some representative things which could be improved:
-	 In D2 (proof of lemma 2 and 3): the paper refers to Proposition 2 in Ma et al. (2019). However, I cannot find the Proposition 2 in Ma et al. (2019). 
-	Lemma 9: not an obvious mismatch between the statement of the lemma and the final line in the proof (RHS of inequality is d/mu for the former, 1/mu for the latter);
-	The proof of lemma 9 starts with “It is known that LSI implies Poincare inequality with the same constant,…”. Perhaps a reference would help.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper explores reverse diffusion in Monte Carlo sampling, transforming score estimation into mean estimation. The algorithm claims to approximate the target distribution accurately, especially for Gaussian mixture models, outperforming Langevin-style MCMC methods. They claim that this algorithm offers a fresh solution for complex distributions.

### Strengths
- It is an extremely interesting problem to investigate. 
- It is easy to follow.
- Theoretical results seem to support most of their claims.

### Weaknesses
 - Lack of practical and experimental results for complex distributions e.g. high-dimensional multimodal distributions. The method's performance is based on empirical observations and may not generalize well across diverse datasets or problem domains. Its effectiveness might be limited to specific scenarios and may not be universally applicable. Specifically, the paper lacks experiments on distributions with non-trivial geometry, such as those with narrow bottlenecks or high curvature regions, which are known to be challenging for MCMC methods. The absence of such experiments makes it difficult to assess the practical utility of the proposed approach in real-world scenarios.
- Lack of complexity analysis. The combination of different sampling techniques (importance sampling, ULA) adds algorithmic complexity. Managing the interactions between these techniques and ensuring their proper integration can be challenging.  Also, The method might demand significant computational resources, especially when dealing with large sample sizes and high-dimensional spaces. This could limit its practicality for resource-constrained applications.  The sample size required for accurate estimation scales exponentially with the dimension due to the KL divergence between distributions. This exponential growth can make the method computationally infeasible for high-dimensional spaces. Could the authors please elaborate on these issues? The paper does not provide a rigorous analysis of how the computational cost scales with the dimensionality of the problem, the number of samples, and the number of iterations. A detailed breakdown of the computational bottlenecks and a comparison with existing methods would be beneficial. Furthermore, the interplay between the inner loop (ULA) and outer loop (importance sampling) is not clearly analyzed in terms of computational cost.
- The accuracy of the estimation relies heavily on the dimensionality of the problem. High-dimensional spaces exacerbate the sample size requirement, making it challenging to apply the method effectively in real-world applications. The paper should discuss the theoretical limitations of the method in high dimensions, particularly how the error bounds scale with the dimensionality and the number of samples. It is crucial to understand the conditions under which the method will become impractical due to the curse of dimensionality.
- Creating n Monte Carlo samples at each iteration can be computationally expensive, especially if n is large. This might limit the method's scalability and efficiency for high-dimensional or complex distributions. The paper should provide a detailed analysis of the computational cost associated with generating these n samples, including the cost of evaluating the score function for each sample. The authors should also discuss strategies for reducing the computational burden of this step, such as using parallel computing or more efficient sampling techniques.
- The method uses random samples $\xi$ at each iteration. The quality of these random samples is crucial; if they are not truly random or are biased in some way, it can introduce errors in the sampled results. Furthermore, the way the samples are generated and combined in the update equation (step 6) could introduce bias if not done correctly. Biased estimators can lead to incorrect conclusions about the target distribution. The paper should provide a more detailed discussion on the properties of these random samples, including their distribution and how they are generated. It should also include an analysis of the potential bias introduced by the sampling process and how it affects the accuracy of the method.
-  The method's performance might degrade in high-dimensional spaces. Monte Carlo methods often face challenges in high-dimensional settings due to the curse of dimensionality, where the sampling space becomes sparse, making it harder to obtain representative samples. The paper should discuss the theoretical and practical limitations of the method in high-dimensional spaces, including how the sampling efficiency degrades as the dimensionality increases. It should also provide a comparison with other MCMC methods in terms of their performance in high dimensions.
- How sensitive is this framework to initial distribution $p_0$?

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work takes a very well-known reformulation of the score in VP-SDEs (see [1,2,3]) that is admissible to the sampling setting where one only has access to the density of the target distribution up to a constant unlike in standard diffusion models where one has access to samples. The authors propose estimating the score via MC, 100% akin to the heat-semigroup (Schroedinger Foellmer Sampler) approach in [4], which rather than time reversing a VP-SDE it can be seen as time reversing the h-transform of a pinned Brownian motion [9].

There is quite a bit of missing literature that has been already explored empirically over the last 2 years in the works of [1,2,3,4]  and also [5, 6, 7, 8].

The ULA-based estimators proposed in this work are the main novelty focus, furthermore, complexity guarantees are provided for these estimators and are shown to outperform vanilla ULA approaches, which is quite promising combined with the experiments added during the rebuttal. 

Notice that in contrast to parametric VI approaches the inner loop scheme proposed has theoretical guarantees for estimating the score that is practically feasible unlike [4,8] which is hindered nonpractical due to the. nonconvex objective required to train the NN estimators of the score.

[1] Vargas, F., Grathwohl, W.S. and Doucet, A., 2022, September. Denoising Diffusion Samplers. In The Eleventh International Conference on Learning Representations. https://openreview.net/forum?id=8pvnfTAbu1f

[2] Berner, J., Richter, L. and Ullrich, K., 2022. An optimal control perspective on diffusion-based generative modeling. In NeurIPS 2022 Workshop on Score-Based Methods.

[3] Zhang, D., Chen, R.T.Q., Liu, C.H., Courville, A. and Bengio, Y., 2023. Diffusion Generative Flow Samplers: Improving learning signals through partial trajectory optimization. arXiv preprint arXiv:2310.02679.

[4] Vargas, F., Reu, T. and Kerekes, A., 2023, July. Expressiveness Remarks for Denoising Diffusion Based Sampling. In Fifth Symposium on Advances in Approximate Bayesian Inference.

[5] Huang, J., Jiao, Y., Kang, L., Liao, X., Liu, J. and Liu, Y., 2021. Schrödinger-Föllmer sampler: sampling without ergodicity. arXiv preprint arXiv:2106.10880.

[6] Vargas, F., Ovsianas, A., Fernandes, D., Girolami, M., Lawrence, N.D. and Nüsken, N., 2023. Bayesian learning via neural Schrödinger–Föllmer flows. Statistics and Computing, 33(1), p.3.

[8]  Tzen, B. and Raginsky, M., 2019, June. Theoretical guarantees for sampling and inference in generative models with latent diffusions. In Conference on Learning Theory (pp. 3084-3114). PMLR.

### Strengths
The paper is well-written and formatted, and has the potential to become a theory-oriented paper with some extra work if the contributions are restructured,  and proper acknowledgments are made, this would require significant re-writing and further development and discussion of lemma 3 and proposition 2, and also theoretical comparison to other methods beyond ULA, simply the statement of these 2 results alone is not a strong enough contribution for ICLR. 

Note that the ULA-based estimators proposed in this work can be seen as a novel (e.g. Algorithm 2), however, without proper experimentation/numerics, this is still not a complete contribution either, currently, the paper is a lot of floating ideas without a concrete exploration of any particular, in part, this is due to the authors not being aware of the current state of the field. However, having to run a couple of inner ULA iterations every time one has to evaluate the drift is highly nonpractical, and claims made in the paper such as :

"
Via this combination, we are
able to efficiently obtain accurate score estimation by virtue of the ULA algorithm when t is close
to T. When t is close to 0, we are able to quickly obtain rough score estimates via the importance
sampling approach.
"

Are highly unvalidated as 2 dimensional toy examples without proper comparison to other diffusion sampling-based approaches.

### Weaknesses
I will break this down into 2 subgroups

1. Lack of Novelty (+ failure to acknowledge prior work)

    *  Lemma 1 is very straight-forward and non-practical as you cannot sample from q, instead in practice the authors do IS and sample from the OU-process' transition kernel which is available analytically, which in turn results in expressing the score as done in [1] ( see equation 84 in [1] and the line that follows it connecting it to the score, or the equation above Equation 24 of the same paper ... or equations 10-13 in [4] ). The core issue is that the paper presents this derivation as novel, when in fact it is a well-known reformulation of the score in VP-SDEs used for sampling, and has been explored in multiple prior works [1,2,3,4]. The authors fail to acknowledge that this specific form of the score has been used in the context of sampling, and that the core contribution of these works is to learn this score via a parametric approach, which is not the approach taken in this work, but the connection should be acknowledged.

2. The paper falls short as a sampling paper empirically

    * Evaluations in 2d simply do not meet the bar for a conference paper. Methodologies such as SMC among many other modern ML variants are able to do quite well in multimodal 2d examples. The paper lacks a comparison to other MCMC methods, and the chosen 2D examples do not provide a strong case for the proposed method.  
    * This MC-IS method for estimating the score will NEVER work well in high dimensions due to variance and thus why works such as [1,2,3,4] which are clearly aware of this formulation (as they either state it in their appendices or use it for subsequent calculation) pursue an optimization alternative to estimating the drift.  See [5] Figure 2 for how poor the performance of these estimators is compared to LMC and alternative NN approaches for learning the score as dimension scales.  The authors briefly allude to this issue and propose combining with an inner ULA loop, however as before the authors missed that previous and more practical approaches (based on score matching) have already been developed to address this same issue, thus without any empirical validation and careful comparison it is very unclear why one would select the proposed approach. The core issue is that the paper proposes an estimator for the score that is known to be high variance in high dimensions, and the proposed solution (inner loop ULA) is not sufficiently justified or compared to existing methods that tackle the same issue.

Note prior results establishing the exact same expressions for the OU-drift and similar expressions for score-matching SDEs applied to sampling have been public since late 2021.

### Questions
Here are some suggestions:  

1. For the MC estimator of the score of the forward SDE please cite [5] as the original work to propose this class of estimators for sampling with SDEs. This is not the score of an OU process it is instead the score of a "pinned Brownian motion" (A Brownian bridge like SDE which starts at the target distribution and maps it to a point mass). The authors might be tempted to argue that this is not the score however note that this quantity  (-logarithmic derivative of the value function) is related to the score by an additive term of $\nabla \ln p_t^{\mathrm{ref}}$ where $p_t^{\mathrm{ref}}$ is the marginal density of the associated reference process (in the case of an OU forward process this is just a linear term), see Remark 4 and its proof in [4].
2. The authors should cite and acknowledge that their Lemma 1 (or exactly equivalent versions thereof)  have already been discussed and derived in the works [1,4] in the context of sampling, and mathematical optimization objectives which aim to learn an estimator for this exact same score the context of sampling have been explored empirically and theoretically in [1,2,3] (also 4 but this is concurrent work).
3. Something that could strengthen the theory contribution is comparing to the Log Sobolev constant of the score in Schrodinger follmer samplers [5] (The score of a pinned brownian motion) and using this to quantify algorithmic design insights for the forward process.  
4. Overall these theoretical contributions can have a stronger impact if written with the state of the current field on diffusion-based samplers in mind, and contextualizing how these results apply to practically successful methodologies. 
7. Note that since the estimator for the score is a ratio of expectations computed via MC the resulting estimator is itself biased, there is no discussion of this in the paper.

**Update:** in the revised versions authors do a careful literature review of both prior and parametric methods which have already explored score-based time reversals for sampling, furthermore with the updated numerics found in the appendix the proposed schemes offer for a much more compelling story.

To justify the notable increase in score I will list a couple of points:

* The log Sobolev constants derived for the OU process and the overall context of the analysis could be of further use and impact to works that focus on time reversal and gen modeling or time reversal and sampling. So there is a potential for impact beyond the proposed algorithm.
* The assumptions in the work have been refined and the sketches are clearer to read in the revised versions.
* The authors have been responsive and very helpful in clarifying points throughout the discussion (albeit a bit combative ... which is not ideal but to a tolerable level).

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
