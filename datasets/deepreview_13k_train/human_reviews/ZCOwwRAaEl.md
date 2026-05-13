# Latent Bayesian Optimization via Autoregressive Normalizing Flows

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Bayesian Optimization (BO) has been recognized for its effectiveness in optimizing expensive and complex objective functions.
Recent advancements in Latent Bayesian Optimization (LBO) have shown promise by integrating generative models such as variational autoencoders (VAEs) to manage the complexity of high-dimensional and structured data spaces.
However, existing LBO approaches often suffer from the value discrepancy problem, which arises from the reconstruction gap between latent and input spaces.
This value discrepancy problem propagates errors throughout the optimization process, which induces suboptimal optimization outcomes.
To address this issue, we propose a Normalizing Flow-based Bayesian Optimization (NF-BO), which utilizes normalizing flow as a generative model to establish accurate and one-to-one mappings between latent and input spaces.
To deal with sequence-based inputs, we introduce SeqFlow, an autoregressive sequence-specialized normalizing flow model designed to maintain one-to-one mappings between the input and latent spaces. 
Moreover, we develop a token-level adaptive candidate sampling strategy that dynamically adjusts the exploration probability of each token based on the token-level importance in the optimization process.
Through extensive experiments, our NF-BO method demonstrates superior performance in molecule generation tasks, significantly outperforming traditional optimization methods and existing LBO approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper addresses the value discrepancy problem in latent Bayesian optimization, where improvements to the latent variable objective value can fail to translate to improvements to objective value of the actual decision variables after decoding. The authors propose to address this issue by parameterizing the generative model as an invertible mapping, specifically a normalizing flow.

### Strengths
- The authors tackle an important problem in the latent BayesOpt literature, a problem which has been previously been observed since at least [1].

- The TACS procedure for selecting token positions to vary is very sensible and closely resembles a similar technique employed by MaskGIT [2] and LaMBO-2 [3], albeit with some minor differences in what signal is normalized into a sampling distribution

References

- [1] Stanton, S., Maddox, W., Gruver, N., Maffettone, P., Delaney, E., Greenside, P., & Wilson, A. G. (2022, June). Accelerating bayesian optimization for biological sequence design with denoising autoencoders. In International Conference on Machine Learning (pp. 20459-20478). PMLR.

- [2] Chang, H., Zhang, H., Jiang, L., Liu, C., & Freeman, W. T. (2022). Maskgit: Masked generative image transformer. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 11315-11325).

- [3] Gruver, N., Stanton, S., Frey, N., Rudner, T. G., Hotzel, I., Lafrance-Vanasse, J., ... & Wilson, A. G. (2024). Protein design with guided discrete diffusion. Advances in neural information processing systems, 36.

### Weaknesses
This is a reasonable paper, if somewhat incremental and with an incomplete view of previous literature on the topic. For an example of a good literature review on this area, see [4].

While more test functions and baseline experiments could always be added, I want to focus my feedback on the lack of a key experiment that verifies the authors are correctly attributing their improved performance to the elimination of value discrepancy. I find it to be a reasonable hypothesis, but the current comparisons to baselines do not prove the hypothesis to be correct because the experiment is confounded by all the other differing implementation choices in those baselines. This is not about proving that your program _as a whole_ outperforms other programs on the benchmarks, this is about critically testing your hypothesis that value discrepancy is the causal factor in this experiment. I would encourage you to think carefully about how you might design an ablation to evaluate this hypothesis. It could be as simple as making the smallest possible change to your current code to intentionally reintroduce the value discrepancy problem, while minimizing any other potential confounders in the experiment.

It is also a bit concerning that the value gap between actual and latents does not seem to have been systematically measured and reported, although that could simply be a choice of presentation. Unless I am mistaken the only place the value gap is quantified at all is in an illustrative figure in the intro.

You should also compare to the simplest possible solution to the value discrepancy problem which was employed by [1] and [3], which is simply decoding frequently and checking the actual objective value [1], and reinitializing the latent variables from actual improved solutions [3].

### Questions
- The tradeoff of the restrictive parameterization of a normalizing flow is typically a loss of expressivity. I believe this is why normalizing flows have largely been abandoned by most of the generative modeling community. Are the authors at all concerned about this tradeoff?

- Have used techniques like TACS for some time, I've noticed it has a weakness in the exploration context, namely that it will tend not to choose positions that have not been varied in the past, and is thus heavily reliant on a relatively complete characterization of the search space in the initial data package. Have you considered how you might "cold start" your solver when only a small local region of the input space is represented in the initial dataset?

- Similarly the choice of temperature in the TACS procedure is a critical hyperparameter that was presumably tuned by the authors by looking at performance curves on the evaluation tasks. While this is common practice in the literature, it tends to cause the actual performance of these algorithms to be overestimated when turned to real consequential tasks where little or no tuning budget is available. Have the authors considered any heuristics for choosing this hyperparameter, perhaps in an adaptive way?

- If you are interested in more potential test functions and baselines you may want to check out the [poli](https://github.com/MachineLearningLifeScience/poli) and [poli-baselines](https://github.com/MachineLearningLifeScience/poli-baselines) project. In particular you may be interested in Ehrlich test functions [5], which are available [standalone](https://github.com/prescient-design/holo-bench) or as part of the poli package. Ehrlich functions are inexpensive yet relatively difficult closed-form test functions for rapid prototype development and more extensive ablation experiments.


References

- [5] Stanton, S., Alberstein, R., Frey, N., Watkins, A., & Cho, K. (2024). Closed-Form Test Functions for Biophysical Sequence Optimization Algorithms. arXiv preprint arXiv:2407.00236.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors focus on latent-space Bayesian Optimization (LBO), which in recent years has emerged as an important area of research. The authors' main contribution is two-fold. (i) To remove the discrepancy between the encoder and decoder of the VAE models commonly used in LBO approaches, they learn a normalizing-flow model that preserves a one-to-one mapping and thus a loss-less mapping from observed to encoded space. (ii) an improved approach to sample new candidates from the latent space based on their relative importance. 
The method is evaluated on a range of benchmarks with strong performance improvements upon the baselines.

### Strengths
- The paper is well-written and the proposal is well-motivated. 
- The evaluation is extensive and demonstrates a strong improvement
- Each of the parts, the autoregressive flow as well as the sampler seem straightforward to implement and use for further applications

### Weaknesses
The weaknesses listed below are only minor.

- Unless I am mistaken, the final acquisition function used is never specified in the text or appendix.
- In l255 the relation to Ho et al. (2019) remains unclear in the text
- The embedding e is never fully specified.

### Questions
- Q1: The paper contains the ablation of running the method with and without TACS, showing a clear improvement when including it. Can the authors speculate (or provide if time permits) on the expected results of a second ablation that combines TACS with a VAE model instead of a flow? Would its relative performance improve to a similar extent as in the proposed approach, or more/less?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
&nbsp;

The authors present the first architecture featuring a normalizing flow as the encoder-decoder model for latent space Bayesian optimization. The invertibility of the normalizing flow is important in addressing the value discrepancy problem, namely that encoded points are not guaranteed to be reconstructed perfectly by the decoder. This pathology in latent space Bayesian optimization has been identified in recent work [11] under the name of the "misalignment problem". It should be noted that [11], to the best of my knowledge is not yet publicly available, and hence the authors should not be required to consider this work. Furthermore, the authors introduce a token-level adaptive sampling scheme (TACS) and demonstrate that it improves performance of the NF-BO method in an ablation study. I think the method is innovative and the empirical results are impressive. However, I have major concerns about the reproducibility of the results, given that the codebase is not provided. I believe crucial details to reproduce the experiments are missing as detailed below. If these issues can be addressed during the rebuttal phase I will be more than happy to increase my score and recommend acceptance.

&nbsp;

### Strengths
&nbsp;

1. The work is the first to introduce normalizing flows as an encoder-decoder model in latent space Bayesian optimization. This represents a novel departure to existing work.

2. The authors methodology addresses an important pathology in latent space Bayesian optimization by enforcing invertibility on the encoder-decoder architecture.

3. The authors demonstrate strong empirical results and obtain state-of-the-art performance on a widely-used benchmark (PMO) where they demonstrate that NF-BO outperforms a suite of other optimization approaches including RL, genetic algorithms, and other Bayesian optimization methods. As such, the current work is of very broad interest to the optimization community.

&nbsp;

### Weaknesses
 
**MAJOR POINTS**

1. My principal concerns relate to the reproducibility of the empirical results since the authors do not provide their code. An Anonymous GitHub link or similar could be provided during the rebuttal phase. In its current form, I don't believe the results are reproducible from the manuscript alone since crucial details such as the GP surrogate model (vanilla GP/sparse GP) and the choice of acquisition function (EI, PI, Thompson sampling) appear to be missing. Furthermore, the specific kernel used within the GP is not defined, and the optimization procedure for the GP hyperparameters is also absent. The lack of these details makes it difficult to reproduce the results.

2. I experienced difficulty navigating Section 4.2 as the notation is very confusing. On line 239, what is L, the number of tokens in a sequence? If so why is each token a vector? In the case of SMILES or SELFIES strings of molecules each token will be an alphabetic character which should not be a vector quantity? What is F? The dimension of the embedding space? What is Equation 8 implying? In other words what does choosing the j that maximizes sim(v_i, e_j) entail? The argmax variable is not clear as only the index is given. A similar point is applicable for the definition of a_i(v). How are the embeddings e computed? Perhaps a glossary of notation would be beneficial for clarity?

**MINOR POINTS**

1. In the abstract, with reference to the sentence, "accurate and one-to-one mappings between latent and input spaces". Is the term "accurate" redundant since a one-to-one mapping implies perfect reconstruction?

2. When introducing Bayesian optimization, it may be worth citing the originating papers for the method [1, 2] as discussed in [3].

3. In the first paragraph, some citations are not parenthetical \citet in LateX vs. \cite and should be parenthetical.

4. The sentence on line 50, "This makes the value discrepancy problem more and makes
the searching challenging." Should be revised.

5. In the related work section on latent space Bayesian optimization, it would also be worth discussing the following papers [4-8] and their relationship to the current work e.g. [8] explicitly considers the diversity in the candidate solutions in a similar fashion to the Token-level Adaptive Candidate Sampling (TACS) employed by the authors.

6. There are some missing capitalizations in the references e.g. "Bayes" instead of "bayes" in the citation for Kingma and Welling, 2014.

7. On line 147, it would be worth changing the notation for the label y to be a scalar since f is defined as a scalar quantity.

8. Missing full stop at the end of Equation 4.

9. The decision to use the variable v in Equation 3 is slightly confusing. Why not just use x?

10. The problem formulation of latent space Bayesian optimization in Equation 5, differs from that in e.g. [9] where the goal is to identify z^* that maximizes the expected f(p(z)) under a probabilistic decoder. I'm assuming that the formulation presented assumes a deterministic decoder since the normalizing flow is capable of producing a bijective mapping. It may hence be worth emphasizing the distinction between the problem formulation with normalizing flows (deterministic decoder) and the problem formulation with VAEs (probabilistic decoder). Furthermore, the implications of using a deterministic decoder on the optimization process should be discussed.

11. Typo line 200, y^(i) should be a scalar, similarly line 201.

12. For the contrastive loss in Equation 13, it would be good to discuss the intent in relation to deep metric learning in [9]. The goal of the contrastive loss would appear to be to structure the latent space. As found in [9] it might be an idea to leverage label information y to structure the normalizing flow latent space. This could yield improvements to the GP fit. The authors should discuss the potential benefits of incorporating label information into the contrastive loss.

13. In Table 1, what is the score? The sum of the scores of each individual task constituting the PMO benchmark? It would be worth specifying this directly in the main paper in addition to the appendix (I only found this information later when I read the appendix.). Additionally, it would be worth mentioning that the full breakdown of results from the PMO benchmark [10] is provided in the appendix.

14. Typo line 484, the number of the referenced table is missing.

15. Typo line 485, "metrics".

16. In Figures 5 and 7, the method for computing the errorbars should be reported e.g. is the standard error or the standard deviation over 5 trials being depicted? It would also be worth stating the number of trials directly in the figure captions.

17. Typo line 893, "number of query points".

### Questions
&nbsp;

1. What is the relationship between the similarity loss in Equation 13 and deep metric learning [9]? Do the authors think that incorporating label information y into the similarity loss could yield a better surrogate fit as in [9]? Did the authors consider incorporating label information into the loss formulation?

2. For Equation 14, did the authors consider coordinate ascent on the two terms in the objective as opposed to scalarization with the lambda parameter? Coordinate ascent may be more efficient and would avoid setting an arbitrary scaling parameter.

3. On line 331, the authors state, "In practice, sampling the full posterior function from the GP posterior distribution is infeasible". What do the authors mean by this and why is it relevant. Do the authors assume an acquisition function like Thompson Sampling is being used?

4. In Appendix C, do the authors have any intuition for why lower temperature yields reduced diversity for the rano task?

5. In Appendix F, how is the embedding dictionary specified?

6. In Algorithm 1, what is topK on line 2?

&nbsp;

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a Latent Bayesian Optimization (L-BO) method, called NF-BO, that aims to improve BO performances by avoiding the value discrepancy problem typical of existing L-BO methods.
This method uses a sequential normalizing flow-based model to ensure a 1 to 1 injective mapping between latents and input data points, therefore avoiding the value-discrepancy problem. The authors also introduce TACS, an adaptive sampling methods for candidate points to increase the efficiency of the search by better focusing on areas with higher potential impact.
The effectiveness of NF-BO is demonstrated on a wide range of molecule generation tasks.

### Strengths
1. Efficient BO methods are key to finding optimal solution to a wide range of complicated problems with expensive and black-box objective functions. Many of these problems have inherently discrete components, and as such it's key to develop methods like NF-BO that can effectively deal with discrete spaces in a principled manner.
2. The authors give a good overview of the limitations of current methods, and the reason why normalizing flows are a better choice for this task.
3. To the best of my knowledge, this method is novel in the usage of NF, the SeqFlow architecture and the TACS sampling. 
4. In the experimental benchmarks NF-BO  together with TACS sampling greatly outperforms competing methods, leading to much better solutions in a fraction of the oracle calls

### Weaknesses
1. Overall, I found some of the SeqFlow explanations in section 4.2 a bit too abstract to be easily understood by the reader. I think the section could benefit from using a simple running example to show in practice (a) how an embedding dictionary could look like (b) a sample surrogate model and acquisition function
2. In the paper you claim that current L-BO methods fail because of the value discrepancy problem. Are you sure that the issues are due to the value discrepancy problem itself, and not for example due to a "poor" learned latent space? In other words, is "perfect reconstruction" a must, or "good enough reconstruction" would also work?
3. How sensitive is the method to different values of $\lambda$  in the similarity loss in (14)?

### Questions
See weaknesses section.

### Soundness
4

### Presentation
3

### Contribution
4
