# Approximating Full Conformal Prediction for Neural Network Regression with Gauss-Newton Influence

- Decision: Accept
- Scores: 6, 3, 8, 6

## Abstract
Uncertainty quantification is an important prerequisite for the deployment of deep learning models in safety-critical areas. Yet, this hinges on the uncertainty estimates being useful to the extent the predictive prediction intervals are well-calibrated and sharp. In the absence of inherent uncertainty estimates (e.g. pretrained models), popular approaches that operate post-hoc include Laplace’s method and split conformal prediction (split-CP). However, Laplace’s method can be miscalibrated when the model is misspecified and split-CP requires sample splitting, and thus comes at the expense of statistical efficiency. In this work, we construct prediction intervals for neural network regressors post-hoc without held-out data. This is achieved by approximating the full conformal prediction method (full-CP). Whilst full-CP nominally requires retraining the model for every test point and candidate label, we propose to train just once and locally perturb model parameters using Gauss-Newton influence to approximate the effect of retraining. Coupled with linearization of the network, we express the absolute residual nonconformity score as a piecewise linear function of the candidate label allowing for an efficient procedure that avoids the exhaustive search over the output space. On standard regression benchmarks and bounding box localization, we show the resulting prediction intervals are locally-adaptive and often tighter than those of split-CP.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors developed a new and scalable full-CP method considering the Gauss-Newton influence. The paper is well-organized.

### Strengths
The theoretical analysis is thorough.

### Weaknesses
Some more state-of-the-art algorithms are expected to be adopted for comparison to illustrate the effectiveness.

 A complexity analysis of the proposed method should be included to demonstrate its efficiency relative to the standard Full-CP approach.

### Questions
1. A complexity analysis of the proposed method should be included to demonstrate its efficiency relative to the standard Full-CP approach.
2. Several state-of-the-art algorithms from the past three years are expected to be compared to further demonstrate the advantages of the proposed method.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes to use influence function to approximate full conformal prediction for regression tasks. Like a recent literature, it perturbs the model in the prediction space, and allows for training the model once instead of carrying out the actual costly full conformal prediction procedures.

### Strengths
This paper extends a recent work on approximate FCP on classification to regression. FCP is indeed expensive and, if to be applied on large modern datasets with NNs, needs to be made more efficient one way or another.

### Weaknesses
1. Inappropriate literature review: This paper didn't cite important (although un-sound, see Appendix C of https://dl.acm.org/doi/abs/10.5555/3540261.3540902) previous research https://proceedings.mlr.press/v119/alaa20a.html despite the very similar idea (and they are also studying regression). Similarly, even though (Martinez et al. 2023) is classification, the current draft severely underplays the clear similarity. While this probably does not constitute a research integrity issue yet, in my opinion this MUST be fixed.

2. Validity of the method: Although I'm very glad that the authors didn't make claims about validity of the approximated FCP method, this paper also lacks an appropriate discussion on the *invalidity* like (Martinez et al. 2023, section title "Validity of ACP"). I highly recommend the authors include a similar section, as in my opinion, the whole point of conformal prediction is about "validity", and approximate CP methods are, to some extent, closed to a "calibrated" non-CP method. Alternatively, I'm hoping to see some "worse case" guarantee when we make additional assumptions about the data distribution. Either way, a discussion on validity is needed. 

3. Experiments: 
	a. While it is obvious that for very small datasets SCP is very wasteful (due to the sample splitting), I think to use half of the training data as the calibration set is also misleading. Yes, this was what was proposed decades ago, but in practice no one actually reserve half of the data as the calibration set. I suspect with a more appropriate data splitting, we wouldn't see much difference between SCP and ACP on bike.
	b. The lack of validity of ACP is very concerning, as it lacks both theoretical and empirical validity. 
	c. I don't see why SCP-GN is related to this paper. It seems the same as "Locally-Weighted Conformal Inference" in (Lei et al., 2018).

### Questions
1. Do the author have any thoughts on the validity?

2. Why do we need to approximate FCP in "low-data regime"? Related to this, maybe an actual FCP baseline should be included for yacht, boston and energy.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors highlight in this paper the computational challenges associated with full conformal prediction (FCP), arguing that it is infeasible for practical applications due to needing to train a new instantiation of the model for every data point for every unique label. In an attempt to alleviate this issue and scale FCP to neural network (NN) regression, they attempt to approximate FCP through the use of Gauss-Newton influence and network linearization to form their method ACP-GN and an extension for split CP SCP-GN. The use of Gauss-Newton influence prevents the need to retrain the network as it allows an approximate solution to perturbation of the model parameters, while the use of network linearization prevents the need for an exhaustive grid search over the label space. The evaluation shows that ACP-GN provides a more well-calibrated method in terms of coverage compared to comparable methods in experiments tested.

### Strengths
- The proposed methodology to alleviate the issues with FCP is intuitive and logical. It is further backed up with well-written derivations provided in the appendix.
- Sections 1 to 4 are extremely well written: references and literature covered are correct/up-to-date and craft good motivation. Notation throughout is consistent and rigorous.
- The numerous datasets and evaluation splits tested upon are impressive and provide statistically rigorous results.
- Highlighting between Algorithms 1 & 2 is great for readability.
- It is clear originality is high.

### Weaknesses
 - The main motivation behind the method is that utilising FCP is computationally infeasible. It then feels detached to not comment on the possible/potential computational savings between FCP and ACP-GN. Calculating an approximate training time that FCP would take on an example dataset and comparing it to ACP-GN's training time would be helpful and insightful in Appendix E.
- Realistically, between the handful of proposed methods, the evaluation compares against two methods: a Laplace approximation, and the base split CP. This feels a little weak; I would have preferred to see comparisons against works that use influence functions, or homotopy.
- In the conclusion, the authors state - 'our approximate full-cp methods provide tighter prediction intervals in limited data regimes'. When looking at the small datasets, this statement is true when alpha=(0.1). But when alpha=(0.05 or 0.01), the Laplace method consistently outperforms all proposed variations.

Small weaknesses:
- Captions for tables and figures throughout the paper are used for discussion instead of describing what the table is showing specifically.
- Bolding in Table 1 is potentially misleading. Even though you declare what definition for bolded results. Typically, bolding is used for top-performing results. In Table 1, in numerous cases, bolded results are not best performing. This is a shame as it takes away from the great results reported in the 'coverage' column.

### Questions
Can the authors comment on the following:
- The lack of evaluation to previously proposed approximate FCP methods.
- The potentially misleading statement in the conclusion of the paper. 
- Why you did not approximate the saved training time between FCP and ACP-GN as computational infeasibility is the main motivation behind the paper.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes an efficient conformal prediction method for regression problems based on neural networks. To do so, the paper suggests to use Gauss-Newton influence in order to approximate how the residue of the NN changes, which allows for the CP intervals to be computed without performing NN training in full again.

### Strengths
- The paper is well-written, especially in providing enough background for those who may be unfamiliar with the CP methods already.

### Weaknesses
 - Although I think the paper is already well-written, I feel it would improve on the presentation further if more visualisations are provided, especially in trying to understand how the 

- Even though the paper claims that their method should be more efficient than existing naive CP methods for NNs, it would still be interesting to see more results on how this compares. In particular, since the algorithm requires the inverse of a Hessian, it would be interesting to see how the method can scale to larger NNs or to cases with more training data. In particular, some results on running time that compares the proposed methods to other methods would be interesting.

- To also verify the use of Gauss-Newton method, it may also be an interesting demonstration to directly compare the naive method in Algorithm 1 and the approximation in Algorithm 2, to show that even using the approximation the tradeoff in accuracy is not so large but more gained in the running time (I am unsure if this is already shown in the SCP benchmark case already though, in which case the discrepancy in result would be interesting to discuss).

### Questions
1. Are there any possible theoretical guarantees for the achieved CP bounds? Given that the Gauss-Newton influence seems like a well-studied theory, and that linearised NNs are also common assumptions in the NTK theory (which itself provides extensive theoretical guarantees for NN predictions), I am wondering if those results can be used to show how accurate the residual estimates would be, and how they would affect the quality of the resulting interval predictions. I am unsure if these theoretical bounds are typical in CP works but it would make the work more theoretically sound.

2. How sensitive are the conformal intervals with respect to the initialisation of the neural network?

3. In the related works section, you have mentioned some more recent methods for conformal prediction on regression problems. Why were these benchmarks unsuitable for comparison in the experiments section as opposed to some of the older methods that were used in the experiments?

### Soundness
3

### Presentation
3

### Contribution
2
