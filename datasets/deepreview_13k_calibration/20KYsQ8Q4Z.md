# High-dimensional Bayesian Optimization with Group Testing

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Bayesian optimization is an effective method for optimizing expensive-to-evaluate black-box functions.
High-dimensional problems are particularly challenging as the surrogate model of the objective suffers from the curse of dimensionality, which makes accurate modeling difficult.
We propose a group testing approach to identify active variables to facilitate efficient optimization in these domains.
The proposed algorithm, Group Testing Bayesian Optimization (\method), first runs a testing phase where groups of variables are systematically selected and tested on whether they influence the objective.
To that end, we extend the well-established theory of group testing to functions of continuous ranges.
In the second phase, \method guides optimization by placing more importance on the active dimensions.
By exploiting the axis-aligned subspace assumption, \method is competitive against state-of-the-art methods on several synthetic and real-world high-dimensional optimization tasks.
Furthermore, \method aids in the discovery of active parameters in applications, thereby enhancing practitioners' understanding of the problem at hand.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces GTBO which introduces ideas from feature selection literature and Group testing theory to the problem of selecting relevant features to reduce dimensionality of high dimensional BO problems and reduce the effect of pathology of curse of dimensionality for such problems. The total budget is divided into two halves, first the relevant features are identified using first set of function evaluations to create an active subspace of features, and then by assigning different priors on lengthscales for each set of relevant and irrelevant features the remaining budget is used for BO. Experiments are carried out on simulated popular datasets and two real world datasets and the performance of proposed method is compared against existing algorithms. The proposed model is probabilistic and can handle noisy observations. The method seems to do well and with the inherent advantage being that it is more interpretable than projection based dimenionality reduction methods.

### Strengths
1. The paper is mostly well written.
2. The baselines and relevant literature is well covered and duly introduced to the readers.
3. The results from the experiments suggest that the nmethod works well as compared to baselines both on simulated and real world datasets.
4. I think it is a strenght of the method that it combines the advantages of interpretibility which come along with feature selection compared to projection based approaches so the user gets to understand his data as he is performing BO. 
5. The math and equations look fine to me. 
6. It is great the authors carry out and report sensitivity analysis and ablation study in Appendix and main paper.

### Weaknesses
1. The model makes many assumptions that the features are relatively independent, since for highly correlated features, it might not be possible to break them into sets of active and inactive features without knowing their correlations beforehand. Assuming that the probabilities of dimensions to be active are independent, is rather a strong simplifying assumption and will not hold in many practical datasets and situations. This is a critical weakness, as the method's performance could degrade significantly when applied to real-world datasets with complex feature dependencies. The assumption of independent probabilities for feature activation is particularly concerning, as it neglects the potential for synergistic or antagonistic relationships between features, which are common in many scientific and engineering applications. For example, in a biological dataset, the expression levels of certain genes might be highly correlated, and treating them as independent could lead to misleading results. 
2. The paper does not list its own limitations properly. 
3. Certain choice of parameters for instance :  $\\sqrt(D)$ to be the value of active dimensions, choice of prior: logNormal with particular values of location and scale parameters can be better motivated. Why logNormal and not Gamma for instance, which is common hyperprior for lengthscale ? The justification for using $\\sqrt(D)$ as the number of active dimensions is weak; a more thorough analysis of the impact of this parameter is needed. The choice of a log-normal prior, while common, should be more rigorously justified. The authors should consider exploring the impact of other priors, such as the Gamma distribution, which is also frequently used as a hyperprior for lengthscales, and provide a comparative analysis. The lack of a detailed sensitivity analysis for these parameters raises concerns about the robustness of the method. 
4. Maybe have one more real world dataset.
5. The writing of the Experiment section can be improved, because somehow the flow of information is not good, as the authors introduce the figures in a weird order (Minor) and do a bit of back and forth. 
6.. Maybe make the lines in plots thicker.

### Questions
Minor comments and questions:
1. What is the value of $C_{lower}$ and $C_{upper}$, apologies if I missed it.
2.  Why did the authors use the particular acquistion function which they did ?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an algorithm for high-dimensional Bayesian optimization (BO), called GTBO (Group Testing Bayesian Optimization). The algorithm explicitly divides high-dimensional BO into two steps: in the first, a set of group testing experiments are run to probabilistically identify inactive input dimensions. In the second, BO is run with a relatively standard method (Matern 5/2 with qLogNEI acquisition function), while applying different length-scale priors for active vs. inactive dimensions.

------ AFTER AUTHOR RESPONSE -----

Thanks for these clarifications. I definitely misunderstood how the GT iterations were treated in the computational results, which the authors have pointed out. I have raised my Contribution and Overall scores to account for this mis-judging of the results.

There are still some points I believe could be improved--the authors also note both points in their response. Firstly, the presentation could focus on this as a feature selection method rather than a BO algorithm. It is a great feature that GTBO actively selects sampling points in contrast to "traditional feature selection methods," but the entire GT step is still de-coupled from the latter BO step, unless I am mistaken here. Secondly, it would be nice to see some more realistic benchmark problem(s).

### Strengths
1. The presentation of the group testing methodology clearly explains the mathematical foundation and practical implementation details of the proposed algorithm.
1. The computational tests are evaluated on several synthetic problems and also real-world benchmarks.

### Weaknesses
1. While this work is presented as a new BO algorithm, it is effectively a feature selection algorithm. The proposed group testing algorithm could select active dimensions to be optimized by any standard BO algorithm (e.g., ignoring the inactive dimensions). Likewise, a different feature selection method could be followed by the employed BO, which is relatively standard. The decoupling of the group testing phase and the BO phase is a key weakness, as it limits the potential for adaptive learning of the active subspace. The method does not leverage the BO phase to refine the active subspace identified by group testing, which could lead to suboptimal performance if the initial selection is not perfect. 
1. The motivation for the benchmark problems needs to be strengthened. The synthetic benchmarks have 2-8 active dimensions and approximately 300 active dimensions without justification for this setting. The real-world benchmarks have no noise, again without justification. The choice of these benchmarks does not adequately represent the challenges of real-world high-dimensional BO problems, where noise is often present and the number of active dimensions is not known a priori. The lack of noisy real-world benchmarks makes it difficult to assess the robustness of the proposed method.
1. From what I understand, the comparisons for GTBO do not include the 39-112 iterations for group testing, which are used as the initial sample points for BO. Therefore, in Figs 3-4, where the other algorithms are starting from 0 function evaluations, GTBO is already starting at many. This gives an unfair advantage to GTBO, as it benefits from the initial exploration phase without accounting for it in the total evaluation budget. The reported results may therefore be misleading.

### Questions
1. The description of batch evaluations on pg 6 needs significant clarification, i.e., how many is “several,” and how close is “close”? If batch sampling is available, why doesn’t the user just use the maximum number of batches for every group?
1. How are the log-normal length scales for inactive dimensions determined?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes GTBO, a high-dimensional Bayesian optimization method which first uses adaptive group testing to identify active dimensions and then optimize over the active variables. The authors extend the binary group testing method to continuous space via maximizing the multual information estimated from Gaussian process. Experiment on synthetic functions and two real-world benchmarks demonstrate the efficiency of GTBO.

### Strengths
1. The proposed group testing idea is clear and easy to follow.

2. The experiment shows that using group testing can efficiently identify active variables.

### Weaknesses
1. I think the experiment comparison is not fair, where the best initial point of GTBO is always better than baselines, which gives additional advantage to GTBO.

2. I think the work of MCTS-VS[1] is also a HDBO method using variable selection, which is a similar work as GTBO and should be added into the baselines. 



### Questions
1. As mentioned in weakness part, the initial points are different between GTBO and other baselines. Can you show the result when using same initial points in baselines?

2. Why choosing the search center as the default configuration? What is the performance of GTBO when choosing default configuration as other position (e.g. best point in the random sampled initial dataset)?

3. What is the search bound in the benchmark you used? Does GTBO utilize the advantage of symmetric search space as BAxUS?

4. What is the batch size used in the experiment? The paper mention that "GTBO integrates well with batch BO pipelines with little to no performance degradation". Is there any experiment result to support this statement?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission tackles the case of high-dimensional optimization using Bayesian Optimization (BO), a sample-efficient method that has shown great success for hyperparameter tuning of large deep learning models, or in more concrete applications such as recommender systems tuning. It is therefore relevant for a venue such as ICLR, in my opinion. More particularly, the authors propose to tailor the so-called *group testing* theory to the BO setting. This is achieved by 1) extending group testing to real-valued functions and 2) dividing a usual BO run into two steps, a first step of relevant variable identification through group testing, and a second step of conventional BO, with the learned variable relevance being encoded in the Gaussian process surrogate lengthscales. The proposed method, *GTBO*, not only achieves state-of-the-art results of synthetic and real-world experiments but also enlights the practitioner with a ranking of the relevant variables, thus enhancing its understanding of the problem.

### Strengths
- The paper is well-written and organized in an easy-to-follow manner.
- The approach is simple and works remarkably well.
- The benchmarks include many competing methods, although some recent ones could have been considered as well, e.g. [1,2]


[1] Sparse Bayesian optimization. AISTATS 2023.
[2] Are Random Decompositions all we need in High Dimensional Bayesian Optimisation? ICML 2023.

### Weaknesses
 - As often, the approach involves several hyperparameters, to determine whether a variable is deemed as relevant or not, and then incorporating this information in the BO statistical surrogate using carefully-designed priors. 

Other than that, I have to say I cannot really spot any weakness here. I am not very familiar with the group testing framework.

### Questions
I am genuinely surprised by how good *GTBO* is compared to other competitors, given that the proposed approach feels suboptimal. It performs in a sequential manner, where one first does not care about function maximization, only about variable relevance, even though finding out this information is costly, and then classical BO is performed.
As the group testing phase does not care about high function values, the design evaluated in this process can be associated with low function values. When this happens, the budget has been spent on a design that does not yield a high function value, and variable relevance is learned on a part of the space we do not really care about, as it does not yield a high function value.
Any insights as to why *GTBO* seems to work despite that? Perhaps the initial starting points provided by group testing provide an accurate approximation of the function. A more relevant one than that usually obtained by uniform/Sobol sampling?

Small typo:

I would write the r.h.s. of Eq. 4 as $H(Z_t) - H(Z_t|\boldsymbol{\xi}) = H(Z_t) - \sum_{\xi \in \{0,1\}^D} p(\xi)H(Z_t|\boldsymbol{\xi}=\xi)$ instead of $H(Z_t) - H(Z_t|\boldsymbol{\xi}) = H(Z_t) - \sum_{\boldsymbol{\xi} \in \{0,1\}^D} p(\xi)H(Z_t|\boldsymbol{\xi})$ (as is done in [1]).

[1] Noisy Adaptive Group Testing using Bayesian Sequential Experimental Design, arXiv.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
