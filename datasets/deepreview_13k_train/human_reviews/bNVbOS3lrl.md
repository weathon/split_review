# Bridging the Gap between Variational Inference and Stochastic Gradient MCMC in Function Space

- Decision: Accept
- Scores: 5, 8, 6, 6, 6

## Abstract
Traditional parameter-space posterior inference for Bayesian neural networks faces several challenges, such as the difficulty in specifying meaningful prior, the potential pathologies in deep models and the intractability for multi-modal posterior. To address these issues, functional variational inference (fVI) and functional Markov Chain Monte Carlo (fMCMC) are two recently emerged Bayesian inference schemes that perform posterior inference directly in function space by incorporating more informative functional priors. Similar to their parameter-space counterparts, fVI and fMCMC have their own strengths and weaknesses. For instance, fVI is computationally efficient but imposes strong distributional assumptions, while fMCMC is asymptotically exact but suffers from slow mixing in high dimensions. To inherit the complementary benefits of both schemes, this work proposes a novel hybrid inference method for functional posterior inference. Specifically, it combines fVI and fMCMC successively by an elaborate linking mechanism to form an alternating approximation process. We also provide theoretical justification for the soundness of such a hybrid inference through the lens of Wasserstein gradient flows in the function space. We evaluate our method on several benchmark tasks and observe improvements in both predictive accuracy and uncertainty quantification compared to parameter/function-space VI and MCMC.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method for functional posterior inference in BNNs, combining the best of functional variational inference and functional MCMC. It alternates the two, with an additional step of fitting a parametric transformation to the MCMC samples to form the analytic approximate posterior for the next round. Experiments show that the method achieve better performance than other BNN techniques.

### Strengths
The method seems technically sound. 

The comparisons to other BNN methods are reasonably broad ranging and convincing.

### Weaknesses
The method seems technically sound.

The comparisons to other BNN methods are reasonably broad ranging and convincing.

The method and general area are technically very involved. While I have not checked everything, things do make sense at high level though there are some notational inconsistencies.

The write-up is very involved as a result. I think the method can probably be applied in the more simple non-functional setting, which can make the description more easy to understand and get across.

Experiments show that the method achieve better performance than other BNN techniques. However the paper did not compare against other baselines that are "not as Bayesian", though these are often simpler, computationally more efficient, and more performant empirically. These include deep ensembles, SNGPs, DUE, epinets, temperature scaling, or even conformable prediction methods.

It would also be nice to see experimental results on uncertainty quantification, e.g. reporting expected calibration error for classification, given as UQ is one of the selling points of Bayesian methods.

My worry with the paper is the technical complexity and computationally expense, that while shown to be better than simpler BNN baselines, has not been shown to be better than non BNN methods on a representative benchmark (e.g. uncertainty quantification). This calls into question the practical impact and usefulness of the method.  Granted this criticism can perhaps be directed at many papers in this area, but I think as researchers it is good for us to be able to answer the question of why/under what circumstance somebody should use the methods/tools that we have developed.

### Questions
1. Which specific fVI method do you use? I didn't find any details of this in the paper, while the algorithm in appendix is quite inpenetrable with some notation undefined etc. This seems quite an important question, as I don't know how the algorithm works with the complex posterior forms composed of the transformations with Q_fs1.

2. I think Q_fsK in Prop 3.1 should be Q_fs1?

3. The forms of the invertible transformations are very simple. Can they really capture sufficiently complex posteriors? It would be nice to demonstrate this in a simple 2D toy example?

4. I don't think there's a precise statement of Prop 3.2. Can you furnish this? I think it's saying that if you look at gradient flow of the ELBO, you also get the evolution of the marginal distributions under Langevin SDE. I don't think it really says that for a particular (implementable) fVI method, that they are the same, right? I feel that Prop 3.2 is just saying that the fVI and fMCMC are "going in the same direction". 

5. The transformation step will probably introduce errors, and if we want to careful it is important to quantify these errors, and whether they are controlled or will compound as the algorithm runs.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a Bayesian inference method for determining the posterior distribution of neural networks that assume a prior distribution over functions rather than parameters. The specific method introduced is a hybrid between functional variational inference and functional Markov Chain Monte Carlo. This is done by alternating between maximizing the functional ELBO in conjunction with a parametric approximate posterior and taking MCMC samples. The gap between these two paradigms are smoothed over by approximating the empirical distribution of posterior samples with a learned, parametric transformation of the variational distribution.

### Strengths
The proposed method does a good job of ameliorating the downsides to both fVI and fMCMC while seemingly retaining the benefits of both. I found the learning of a parametric representation of the empirical distribution (in the T-Stage) with a normalizing flow to be particularly clever at bridging the gap between VI and MCMC. The proposed approach makes a solid contribution towards Bayesian methods for neural networks, as functional priors in general are an attractive approach in this space but previously have been plagued with practical downsides that this technique improves upon.

### Weaknesses
I mainly found parts of the experimental results to be a bit lacking. In the abstract, the paper claims that the proposed method improves upon the restrictive posterior of fVI and the slow mixing times of fMCMC; however, as far as I can tell only the former has been showcased. A more expressive posterior can shown with visualizations (Fig 1) or could be argued with improved predictive performance (rest of Section 5), whereas the mixing times, especially in high dimensions, requires a stand alone investigation. Having another synthetic experiment where the posterior distribution is known (e.g., Gaussian Process) and comparing how many iterations is required to converge to arbitrary precision would demonstrate this well. Additionally, showcasing some loss-curves and other metrics throughout training for the real-world experiments could also showcase this.

### Questions
I do not believe this general approach has been taken for parametric Bayesian neural networks, is this the case? If not, do you see any potential for also adapting this scheme (V->M->T->...) for parameter-based inference?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors studied Bayesian Neural Networks (BNNs) and proposed a new inference method by combining two existing ones: the functional variational inference (fVI) and functional Markov chain Monte Carlo (fMCMC). Their hybrid approach alters between two stages: a V-stage that performs fVI to maximize the ELBO, and a M-stage that performs stochastic gradient fMCMC. They provide theoretical justification that the functional Langevin SDE and the probability flow ODE share the same probability evolution marginals. In the experimental evaluations, the authors show that their approach outperform against baselines and improved predictive accuracy and uncertainty characterization in multiple tasks.

### Strengths
The idea from this paper is well-motivated and to my best knowledge, this combination of functional variational inference and functional MCMC is a novel approach. In general, this paper is well-structured, and they provided detailed derivation to show that the functional Langevin stochastic differential equation in the fMCMC and the probability flow ordinary differential equation share the same probability marginals. The math derivation is sound in my opinion.

### Weaknesses
I am a bit confused about how to validate the iterations between the V-stage and the M-stage. As the paper mentioned in the page 4, there is a problem when altering between these two stages, because the M-stage outputs a non-parametric distribution while the V-stage requires a parametric one as its input. I wonder how the transformation from $Q_{fs1}$ to $Q_{fs2}$ is defined specifically.

### Questions
In the section 5.1, the authors said they make fair comparison between their iterative method and the non-iterative methods by specifying certain number of epochs and iterations. I wonder how those number are determined in terms of the same computational budget between all methods?

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
This paper proposes a novel hybrid posterior inference method that combines the advantages of both functional variational inference and functional MCMC. To frame these two update schemes as an alternating approximation process, the authors aim to learn a bijective transformation of the variational distribution updates by maximizing the log-likelihood functions of the samples collected from functional MCMC steps.
Moreover, since using KL divergence in functional variational inference (fVI) may be potentially problematic, the authors propose replacing it with the Wasserstein distance in their method, fVIMC. 
In experiments, the authors validate their method on several benchmark tasks, including the Bayesian neural networks on UCI datasets, exploration-exploitation performance in contextual bandits and classification tasks on MNIST and Fashion MNIST datasets. The results indicate that fVIMC outperforms the primary baseline, like fVI and fMCMC.

### Strengths
- The paper proposes an interesting framework that combines variational inference and MCMC in functional space.
- The details of toy experiments are well-explained, and the real-data tasks are comprehensive. The discussion of related work is also very clear.

### Weaknesses
The fVIMC method proposed in this paper is natural and interesting, but I have some specific concerns about fVIMC:
- The mechanism of using the 1-Wasserstein distance to replace KL divergence in functional priors seems appropriate. However, this may cause the variational distribution update in fVI step no longer corresponding to the gradient flow of the functional $KL[q(w)|p(w|D)]$. In that case, would the result in Proposition 3.2 still hold? Specifically, the theoretical justification for using the Wasserstein distance instead of the KL divergence in the functional variational inference step needs further clarification. The paper should provide a more detailed analysis of how this change affects the convergence properties and the theoretical guarantees of the method. It is unclear if the nice properties of the KL divergence, such as its connection to the evidence lower bound (ELBO), are preserved when using the Wasserstein distance.
- In the results for BNNs, the RMSE scale seems inconsistent with previous BNN results reported in [1] and [2]. The paper should provide a more detailed explanation of the experimental setup, including the specific network architectures, training epochs, and hyperparameter settings used. This would help to clarify the differences between the results reported in this paper and those reported in previous work.
- In the experimental results, an ablation study comparing KL divergence and 1-Wasserstein distance in fVIMC would be helpful. It would be beneficial to see a direct comparison of the performance of fVIMC when using KL divergence versus the 1-Wasserstein distance, particularly in the V-stage. This would help to isolate the impact of this design choice on the overall performance of the method.

### Questions
- Typo: 1. 
In line 132, the term $\mathcal{X}^n = \bigcup \\{\mathbf{X} \in \mathcal{X}^n \mid \mathcal{X}^n \in \mathbb{R}^n \\}$ is confusing.

- In line 166, "this factorized Gaussian will be modified later rather than being fixed, as in fVI, so it does not impose a strict restriction." I believe that the choice of variational distribution family $q_{s0}(\mathbf{w}_{s0},\boldsymbol{\theta}_{s0})$ does, in fact, constitute a restriction for fVI. Can you clarify this point more clearly?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a hybrid functional inference method called Functional Variational Inference MCMC (FVIMC) for posterior approximation. FVIMC alternatives between the V-phase, which optimizes a functional variational objective, and M-phase, which samples a functional Langevin dynamic. The method relies on a learnable transformation to transport the approximate posterior from the M-phase to a density function usable in the V-phase. The paper makes the following claims:
  1. FVIMC is a novel hybrid method that links functional variational inference (FVI) with functional Markov chain Monte Carlo (FMCMC).
  2. FVI and FMCMC share the exact evolution of marginals, which justifies the proposed alternating method.
  3. It provides strong empirical evidence that the proposed method improves predictive performance and uncertainty estimation compared to baselines.

### Strengths
- Proposition 3.2 is insightful, novel and sound.
- The evaluation is done against many baseline models, and the UCI results sustain the claim of improved predictive performance.
- The paper suggests a likelihood heuristic for selecting the transformation. The idea is simple and cheap and aligns with an MLE principle.

### Weaknesses
 - From the remarks in "Avoid the potential problematic KL divergence for fVI," the objective FVIMC optimizes is not from eq. 2 as the KL divergence is replaced with a Wasserstein-1 distance, and a variance constraint is introduced. It is not clear that proposition 3.2 still applies to FVIMC with these alterations. See question 9.
-  Proposition 3.2 connects FVI and FMCMC when the likelihood is evaluated on $\mathcal{D}$; however, the FVIMC uses data-subsampling. It is unclear whether proposition 3.2 holds with data subsampling. See question 1.
- The proposed method requires running an MCMC chain, optimizing the variational distribution and optimizing a transformation at each iteration. However, the computational cost of their proposed method is not discussed. It would improve the paper to include complexity analysis or empirical evidence comparing runtime and memory overhead to the baselines.
- The method uses several hyperparameters that interact in a complex manner. These include the kernel for the GP prior, the number of MCMC samples $N$, the convergence criteria for the V-phase, and the set of transformations and their architecture. However, the paper does not address how to choose these. It would greatly benefit from guidelines, supported by experiments or analysis, for specifying the hyperparameters.
- The paper does not clearly state that the T-stage preserves the shared evolution of posteriors between the V-stage and M-stage. Including a proposition that this holds would strengthen the claim that proposition 3.2 justifies the validity of FVIMC and would improve the paper's score.
- The extrapolation experiment has an unexplained variance collapse in Fig. 1 at $x=0$ for FVIMC. This is also present in the fig. 7 for the FVIMC posteriors. Notably, this collapse is not present in baseline models. It invalidates the claim that "The hybrid fig1(a) exhibits stronger ability than the pure variational fVI in Figure 1(e), e.g., the smoother fitting curves, and can capture critical features of the non-observed middle range [−0.25, 0.25]," because the collapse point is not on the actual curve. Importantly, there is not even posterior mass covering the curve.

### Questions
1. Proposition 3.2 connects FVI and FMCMC when the likelihood is evaluated on $\mathcal{D}$; however, the FVIMC uses data-subsampling. Could you clarify whether proposition 3.2 still holds with data subsampling? If this is the case, are there any constraints on the sampling scheme? If not, please justify that FVIMC still targets the same V- and M-Stage evolution of marginals with subsampling.  
  2. The paper states that FVIMC can incorporate meaningful prior information into the posterior. The experiments are done through empirical Bayes, i.e., using a GP learned from data as a prior; however, it is not done with BBB. Why can't you cannot use empirical Bayes to find the prior for BBB? If you can, consider including this to make the comparison on equal footing.
  4. Could you please clarify which pathologies "potential pathologies in deep learning" (line 147) are referring to? The statement as presented is vague and, therefore, hard to judge.
  5. On line 54, the paper calls the isotropic Gaussian prior non-informative. Should this be understood as non-interpretable in the sense introduced by Tran et al. (2022)? If so, consider changing it to non-interpretable instead. Otherwise, please show that an isotropic Gaussian is non-informative for BNNs, like a Jeffreys prior would.
  6. What is the size of the networks used for experimentation? It is only clear that they are two-layered.
  7. At what scale of BNNs can we use FVIMC feasibly? Can you make an inference on a ResNet-sized network (11-25k params)? 
  8. What model is used in the image classification and OOD detection experiments? This information should be made available in the article or appendix.
9. From the remarks in "Avoid the potential problematic KL divergence for fVI," the objective variational objective FVIMC optimizes is not from eq. 2 as the KL divergence is replaced with a Wasserstein-1 distance, and a variance constraint is introduced. Does Proposition 3.2 still apply to FVIMC with these alterations? If so, please add a sentence that proposition 3.2 still holds to the Avoid the potential... paragraph. Otherwise, what justifies the validity of FVIMC with the changed objective?
10. Why does the collapse occur in FVIMC Fig. 1a? Are there ways to address or mitigate it?

### Soundness
3

### Presentation
3

### Contribution
2
