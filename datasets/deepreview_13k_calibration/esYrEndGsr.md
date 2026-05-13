# Influence Functions for Scalable Data Attribution in Diffusion Models

- Decision: Accept
- Avg Score: 8.00
- Scores: 6, 8, 10

## Abstract
Diffusion models have led to significant advancements in generative modelling.
    Yet their widespread adoption poses challenges regarding data attribution and interpretability.
    In this paper, we aim to help address such challenges in diffusion models by developing an \textit{influence function} framework.
    Influence function-based data attribution methods approximate how a model's output would have changed if some training data were removed.
    In supervised learning, this is usually used for predicting how the loss on a particular example would change.
    For diffusion models, we focus on predicting the change in the probability of generating a particular example via several proxy measurements.
    We show how to formulate influence functions for such quantities and how previously proposed methods can be interpreted as particular design choices in our framework.
    To ensure scalability of the Hessian computations in influence functions, we systematically develop K-FAC approximations based on generalised Gauss-Newton matrices specifically tailored to diffusion models.
    We recast previously proposed methods as specific design choices in our framework, and show that our recommended method outperforms previous data attribution approaches on common evaluations, such as the Linear Data-modelling Score (LDS) or retraining without top influences, without the need for method-specific hyperparameter tuning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper extends influence functions for data attribution of diffusion models. With an exposition focusing on approximating a Hessian with a generalized Gauss-Newton matrix (GCN), this paper justifies specific design choices (linearizing the neural networks combined with K-FAC-expand approximation) that lead to better performing influence functions. The theoretical framework also subsumes previous work such as Journey-TRAK and D-TRAK. Empirically, influence functions perform similarly to D-TRAK on CIFAR-2 and CIFAR-10, with lower sensitivity to the choice of the damping parameter. Finally, empirical observations are made to show the challenges when applying influence functions to diffusion models.

### Strengths
- A theoretical framework is shown to unify influence functions, Journey-TRAK, and D-TRAK for diffusion models. This provides some clarity to the field of data attribution for diffusion models, which currently seems rather empirical.
- The theoretical framework motivates the design choices for approximating influence functions, which actually lead to better performance (as shown in Figure 4).
- Empirical observations (Section 4.1) are made to better understand how to apply influence functions to diffusion models.

### Weaknesses
 - The LDS and counterfactual evaluations are limited to DDPM on CIFAR. The paper would be strengthened if K-FAC Influence is also evaluated on LDM and LoRA-fine-tuned Stable Diffusion (as in the Journey-TRAK and D-TRAK papers). Furthermore, since the observations in Section 4.1 are empirical, not theoretical, they need to be validated in other model architectures and datasets to make the claims more general.
- The proposed method K-FAC Influence is also sensitive to the choice of the damping parameter (LDS can range from ~15% to ~5% on CIFAR-10). This range of variation seems not much different from D-TRAK.
- Observation 3 might be sensitive to the amount of training data removed. For example, if 90% of the data are removed, there could be more variation in the retrained diffusion models, as suggested by Kadkhodaie et al. (2024; Figure 2 in particular). In this sense, the claim in Observation 3 might need to be adjusted to be less general.
- This is minor: It would be useful to include a brief summary of Grosse and Martens (e.g., the reduce vs. expand settings), perhaps in the Appendix.

### Questions
- In practice, how would we tune the damping parameter for K-FAC Influence? How would the tuning procedure differ from that for D-TRAK?
- Observation 2 shows that F-FAC Influence overestimates the impact of data removal, whereas Koh et al. (2019) show that influence functions underestimates the impact of data removal. What are possible explanations for these differing observations?
- Observation 3 seems to have been shown in Kadkhodaie et al. (2024; Figure 2 in particular). What additional insights are provided? For example, does Observation 3 only hold for ELBO, or does it also hold for the simple diffusion loss?


References
- Koh et al. (2019) - On the Accuracy of Influence Functions for Measuring Group Effects.
- Kadkhodaie et al. (2024) - Generalization in Diffusion Models Arises from Geometry-Adaptive Harmonic Representations.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this work the authors adapt influence functions to work with diffusion models. Computing influence functions typically requires one to compute the inverse of the Hessian, which is intractable for deep learning models. Therefore the authors make use of a series of approximations. Firstly, they approximate the Hessian with the generalized Gauss-Newton matrix (GGN). Then they approximate the GGN with a block diagonal matrix, where the diagonal blocks are defined by layers. Finally, they approximate each block as a kronecker product.

The authors then evaluate their method on “linear data modelling score” and “retraining without top influencers”, and find their methods achieve state-of-the-art on both metrics.

### Strengths
This paper combines interesting ideas to tractably approximate influence functions for diffusion models, and achieve state-of-the-art performance on training data attribution on diffusion models, which is a challenging problem.

### Weaknesses
While it is clear that the proposed method is much more scalable than computing the raw influence function, it is difficult to assess how scalable this method actually is based on the main body of this paper (e.g. things like what is the runtime, how does it scale with the model size, what are the space requirements). A reader ought to have a good idea of how feasible this would be to implement for themselves.

It is not clear whether the proposed method outperforms the existing methods given the overlaps in standard error. Perhaps statistical significance could be reported here to give a better idea?

The experimental evaluation is only performed on CIFARs 2 and 10, so it is unclear how well this method scales to larger image generators, both in the quality of attributions and in terms of compute.

### Questions
You explicitly mention that K-FAC is defined for linear and convolutional layers (page 6), but this doesn’t seem to include attention layers, which all diffusion architectures that I’m aware of use. Is K-FAC also defined for attention in prior work, or could you define it?

Could you provide a runtime analysis, or some idea of what the runtime is (e.g. how much time would it take to compute a all influence values for a single sample on an A100)? How does this runtime (and possibly space requirement) scale with the complexity of the model? How much computational resources would I need if I wanted to run this on my favorite existing diffusion model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The paper provides a systematic treatment of tractable influence function (IF) estimation for generative diffusion models. Several forms of IFs are considered: IF of the ELBO, IF of the loss, IF of the path probabilities. These approaches are compared both conceptually and experimentally. The IF of the marginal probabilities of the images is discussed but not implemented.
A large fraction of the paper deals with the intractability of the Jacobian estimation involved in the calculation of the IF and offers and compares several approximate solutions.

The paper provides a thorough experimental analysis of the different IF approaches on several datasets and compares the results with the exact retraining method.

[edit] I increased my score due to the new analysis and results provided during the rebuttal phase, which answered some of the opened questions and provided links with the recent literature.

### Strengths
This work is very valuable for anyone interested in IF estimation in generative diffusion models. This is likely going to be a very important tool due to privacy and copyright concerns associated with image and video generation. 

Both the theoretical discussion and the experimental analysis is systematic and well executed. The paper is very easy to follow and it manages to both provide the intuition and the theoretical justification for its design choices.

I particularly appreciated the discussion of the results, which highlight both the strengths and weaknesses of each approach and also the limitation of the approximate IF estimation when compared with exact retraining.

### Weaknesses
Arguably, the marginal likelihood logp(x) is the ideal target for a IFa analysis. While it is somewhat challenging to compute using the deterministic integration formula with stochastic or deterministic  trace estimation, it is not intractable and in my opinion it should have been analyzed. For example, having the analysis of the IF of logp(x) would help to make sense of the counterintuitive behavior of the IF of the ELBO.

It would have also appreciated to see an analysis on more tractable low-dimensional models with small networks, where the Hessian can be computed exactly. This analysis can be used to evaluate the relative performance of the Hessian approximation techniques, at least in this simple regime.

In the last paragraph before the discussion (starting from line (507), the authors argue that the ELBO could be a poor proxy of the marginal probability due to the fact that it is rather insensitive to the resampling of up 50% of the dataset, meaning that such a resampling do not meaningfully change the ELBO of the generated images.

I think that this conclusion is incorrect. There is in fact evidence that diffusion training enters a 'generalization phase' after a finite dataset size, after which the generative probabilities remain approximately constant even under a non-overlapping split of the training set. This for example can be seen in (Zahra, 2023).

### Questions
In the last paragraph before the discussion (starting from line (507), the authors argue that the ELBO could be a poor proxy of the marginal probability due to the fact that it is rather insensitive to the resampling of up 50% of the dataset, meaning that such a resampling do not meaningfully change the ELBO of the generated images.

I think that this conclusion is incorrect. There is in fact evidence that diffusion training enters a 'generalization phase' after a finite dataset size, after which the generative probabilities remain approximately constant even under a non-overlapping split of the training set. This for example can be seen in (Zahra, 2023).

References:
Kadkhodaie, Zahra, et al. "Generalization in diffusion models arises from geometry-adaptive harmonic representation." arXiv preprint arXiv:2310.02557 (2023).

### Soundness
3

### Presentation
3

### Contribution
4
