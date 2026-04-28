# Generating Likely Counterfactuals Using Sum-Product Networks

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 5, 5, 8

## Abstract
Explainability of decisions made by AI systems is driven by both recent regulation and user demand. These decisions are often explainable only \emph{post hoc}, after the fact. In counterfactual explanations, one may ask what constitutes the best counterfactual explanation. Clearly, multiple criteria must be taken into account, although ``distance from the sample'' is a key criterion.
    Recent methods that consider the plausibility of a counterfactual seem to sacrifice this original objective. 
    Here, we present a system that provides high-likelihood explanations that are, at the same time, close and sparse. 
    We show that the search for the most likely explanations satisfying many common desiderata for counterfactual explanations can be modeled using mixed-integer optimization (MIO).    
    In the process, we propose an MIO formulation of a Sum-Product Network (SPN) and use the SPN to estimate the likelihood of a counterfactual,
    which can be of independent interest.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper deals with the task of finding counterfactual explanations (x’) for a multi-class classification model (h(x)). Specifically, the authors aim to find a counterfactual set (C) satisfying desiderata specified in Guidotti (2022). i.e. apart from being a valid counterfactual, each x’ \in C must be similar to the original example x, involve changing as few features as possible (sparse), comply with domain constraints such as monotonicity of age (actionable), and not be an outlier (plausibility). Additionally, C must be as diverse as possible and follow causal domain knowledge. The authors approach this problem from a mixed integer optimization perspective and use sum-product networks to model the data distribution (P(X)). To this effect, they translate the desiderata into constraints and solve the optimization problem using the OMLT library (Ceccon et al., 2022). While the trained SPN cannot be encoded exactly in log-space, the authors develop an approximate encoding and bound the likelihood. The authors call their proposed counterfactual generation approach Likely Counterfactual Explanations (LiCE) and define two variants of LiCE, one based on likelihood (upper) threshold of train-set median (LiCE (median)) and the other on minimizing a linear combination of distance and likelihood (LiCE (optimize)). They evaluate the two variants by comparing them against a non-SPN variant (MIO) and on prior work including DiCE (Mothilal et al., 2020), C-CHVAE (Pawelczyk et al., 2020), FACE (Poyiadzi et al., 2020) and PROPLACE (Jiang et al., 2024) on 3 financial data sets focusing on plausibility (as measured by log-likelihood), similarity (counterfactual distance), and sparsity (number of modified features). Their experiments show that both LiCE variants outperform the baselines, and while LiCE (median) excels at plausibility of generated counterfactual sets, LiCE (optimize) is the best at similarity even beating MIO.

### Strengths
- LiCE is a principled method of inferring *plausible* counterfactual explanations that satisfy several desiderata. The MIO approach is flexible enough to accommodate additional criteria.
- The MIO formulation for SPN inference is itself a significant contribution. It opens up space for work on SPN inference tasks such as finding the entire Maximum a Posterori (MAP) set possible. Existing work has focused on finding single solutions (e.g., Poon and Domingos, 2011 and Arya et al., 2024).

Arya, Shivvrat, Tahrima Rahman, and Vibhav Gogate. "Neural Network Approximators for Marginal MAP in Probabilistic Circuits." AAAI 2024.

### Weaknesses
The Accuracy of likelihood assessment is limited by the expressivity of SPNs. This might be at least partially resolved by using PFCs (Sidheekh et al., 2023) to improve performance on high-dimensional domains. Furthermore, the approximation of the log-sum-exp function with the max function, while practical for MIO, introduces a potential source of error that is not fully explored. The tightness of this approximation and its impact on the quality of the generated counterfactuals should be analyzed more thoroughly, especially in cases where the inputs to the log-sum-exp have a wide range of values. Finally, the reliance on a fixed time limit of 2 minutes for the optimization process may not be sufficient to find optimal solutions, particularly for complex datasets or when the likelihood bound is restrictive. This could lead to premature termination and potentially suboptimal counterfactual explanations.

### Questions
- Would making structural assumptions (e.g., determinism) about SPNs make it easier to encode exactly? 
- Can you elaborate on the setup and significance of the VAE baseline from Mahajan et al. (2020)?
- The results mention that LICE (median) times out for some of the cases, and the appendix mentions that the time limit for each run was 2 minutes. Are these results sensitive to the time limit duration? Would they change drastically for a small increase in the time limit?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a novel method to model counterfactual explanation (CE) search that maximizes likelihood, closeness, and sparseness. The method leverages sum-product networks (SPNs) to estimate point likelihoods (or plausibility) and use mixed integer optimization (MIO) to optimize the different objectives simultaneously. The work includes empirical comparisons with state-of-the-art CE algorithms.

### Strengths
- The use of SPNs to model plausibility in counterfactual explanations is a novel and creative approach, addressing limitations in handling mixed data that many existing methods struggle with. 

- The integration of SPNs and MIO to optimize multiple constraints simultaneously offers flexibility and the formulation of bounds for the output of SPNs that can be integrated as constraints into a MIO formulation is (as the authors mention) quite interesting on its own.

### Weaknesses
 - The key concept of plausibility, derived from the output of SPNs, is assumed to be correct without evaluation. This is a critical assumption, as it underpins the entire method, and its validity should be examined and justified. The lack of empirical evaluation of this concept weakens the overall contribution. Specifically, the paper defines plausibility as high likelihood according to the SPN model, which is then used to select counterfactual explanations. This creates a circular dependency where the method is evaluated based on its own internal plausibility metric, rather than an external, objective measure. This circularity is a major concern, as it biases the evaluation in favor of the proposed method.

 - The experiments appear to be biased in their evaluation of plausibility as the SPN distribution is taken as the true one, giving the proposed method an unfair advantage over the baselines. The baselines, which do not use SPNs for plausibility, are inherently disadvantaged in this setup. This makes it difficult to assess whether the proposed method truly generates more plausible counterfactuals or if it simply aligns better with its own internal model of plausibility. The evaluation should compare the plausibility of counterfactuals against an independent measure, not one derived from the method itself.

 - The clarity of the paper could be improved, particularly around the explanation of key terms and concepts like plausibility and outliers, which are not sufficiently defined when first introduced. The definition of an outlier, for example, is not explicitly stated, and its connection to the concept of plausibility is not clear. This lack of precise definitions makes it difficult to understand the motivation behind the method and its underlying assumptions. The paper should provide clear, unambiguous definitions of these terms early on.

 - The method appears computationally expensive, which could be a practical concern in real-world applications. This issue is not directly addressed in the paper, but the experiments suggest that the optimization process may be time-consuming, particularly for more complex scenarios. The paper would benefit from a discussion of the computational cost and potential ways to mitigate it, such as pruning strategies, approximations, or discussing scalability.

### Questions
Content-related: 

- L53: What is the definition of an outlier in your context? Are you suggesting that an epsilon-ball around the factual could contain outliers due to factor interactions and their joint distribution? Please expand on this. 

- L80: Table 1 is not explained. Why are the "other desiderata" important? 

- L97-107: A definition of plausibility is missing in this section. You claim that DiCE is the most plausible—what criteria support this claim? Additionally, LiCE changes installment/disposable income while keeping amount and duration constant, suggesting a change in income. Is this more "realizable" than borrowing less? MIO changes two features (duration and income); could you provide more details on how these changes are measured?  

- Later in the paper, it becomes clearer that your definition of plausibility stems from the joint probability distribution extracted from SPNs. However, this raises concerns about whether this plausibility measure should be evaluated independently. In your experiments, you assume that this probability distribution provides the correct measure of plausibility without empirical validation. Could you justify this assumption further, or better yet, provide an evaluation of plausibility as a standalone concept? This is crucial, as your entire method relies on the assumption that SPN-based plausibility is the most accurate or appropriate for counterfactuals. 

- L184: Why do you take the median for categorical values? Could you use their actual values instead? Taking the median for categorical variables may cause all of them to start from the same point. 

- L188: Why will at least one always be 0? Please provide intuition. Also, the citation is placed after the full stop—should be corrected. 

- L237: Outliers are mentioned again without a definition. Also, plausibility is referenced but not defined earlier. An intuition would help the reader follow the motivation more clearly. 

- L260: Why do you work in log-space? Is it to simplify handling products? Please provide a rationale for this choice. 

- L332: Taking a threshold of 0 on the raw output of a neural network implies a threshold probability of 0.5 after applying a logit. Are there dependencies on this, and can it be changed? 

- L461: You select CEs based on SPN output, which establishes plausibility in your results. Does this give your method an advantage over baselines? For example, on L484, you claim "unparalleled" plausibility. 

- L471: You mention that the failure to terminate worsens the results. How pronounced is this effect? 


Minor points: 

- L82: "This work combines the tradition ..."—what tradition are you referring to? Please include a reference to clarify. 

- Fig2: The heatmap legend is missing. Are the most likely points represented by the most yellow areas, particularly near 0 amount and 12 months? 

- L252: "SPNs are a strict generalization"—this statement is missing a reference. 

- L293: Typo: "the it" 

- L376: Why do you need $v^{cont}$ and $v^{bin}$? Could you elaborate on the correspondence between these values and their respective roles in your approach? Does this correspondence offer advantages or properties? 

- L468: What do you mean by "considering the differences between methods" when referring to finding the error acceptable? 

- L497: What do you mean by "the limitations of all MIO methods"?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the problem of generating counterfactual explanations for a fixed classification function, say $f(x)$. The explanation here refers to different input $x'$ to the classifier $f(x)$ (with a factual baseline $x$) such that they result in different classification outcomes $f(x') \neq f(x)$. In general, there are many such realizations of input $x'$. This paper studies the problem of finding the most likely counterfactual explanations $x'$ satisfying a set of selection desiderata, including validity, similarity, sparsity, and actionability. The authors evaluate the likelihood of an input $x'$ by fitting a sum-product network (SPN). Using the formalism of SPNs, the selection desiderata could be translated into a series of equivalent polynomial constraints. The explanation generation is then reduced to an equivalent mixed integer optimization (MIO) problem.

### Strengths
- The writing is generally clear. The paper is well-organized. While no main theorem is presented in the paper, the derivation of the mixed integer program is technically sound.
- Comprehensive simulations were performed. Simulation results support the proposed MIO formulation.
- The authors have clearly stated the limitations of the proposed methods, including the computational challenges of solving MIO programs.

### Weaknesses
 - The SPN models might be limited. First, it can only account for discrete features, while most prediction tasks in practice involve high-dimensional, continuous feature inputs. Also, SPNs require structural constraints. It could be challenging to learn SPNs that best fit with the observed data.
- The explanation generation problem is reduced to an MIO program, which is generally NP-hard to solve. This presents challenges in generalizing the proposed methods to more complex domains.
- The reduction of SPN to MIO programs is not surprising. It has been known that constrained optimization in Bayesian networks is generally equivalent to linear integer programming. This paper would be most improved by proposing an efficient approximation algorithm to solve the MIO program while leveraging the graphical structure of the learned SPN.

### Questions
1. Could the proposed method apply to other generative models measuring the likelihood, e.g., Gaussian processes?
2. For all variants of the proposed methods, LiCE (optimize) seems to perform the best. However, its implementation is somewhat ambiguous. The authors stated, "we optimize a combination of distance and likelihood with α = 0.1 and relax the plausibility constraint (Eq. 13)." Could the authors further elaborate on this statement? For instance, what is the "combination of distance" and how to "relax the plausibility constraint?" A pseudo-code description would be appreciated.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper proposed a method for computing plausible counterfactual explanations by using sum-product networks.

### Strengths
The paper addresses an important problem and proposes a novel and interesting approach. Its strength is its ability to handle categorical features (often encountered in real-world data sets).

### Weaknesses
Disclaimer: I have reviewed the paper before (Neurips 2024)—I hope that this does not disqualify me as a reviewer. In my opinion, the paper has improved significantly. In particular, the empirical evaluation is now done fairly, the notation and formalization are clear now, and the structure of the entire paper is now more accessible and more "scientific" compared to the previous version that I reviewed.

However, I still think that some more information on SPNs could be added: How powerful are SPNs? What types of distribution can they model? What are the assumptions? How to estimate SPN's parameters from data? Given the large number of existing methods (for computing plausible counterfactuals), this information would help practitioners select one of those existing methods. There is information given in the appendix but it might be also good to (briefly) answer some of those questions in the main text.

I understand that there is not enough space to fully introduce SPNs but I still think that it would be important to highlight what they can model and what they can not -- this would help practitioners to select an appropriate method for their particular use case. Currently, different methods exist for computing plausible counterfactuals based on Gaussian Mixture Models, Kernel Density Estimators, Neural Autoencoders, etc., and each of those methods has its advantages and disadvantages. However, I am happy to discuss this and step back if the authors or the other reviewers can convince me that this is not necessary or is somehow already in the paper. Thanks :)

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
