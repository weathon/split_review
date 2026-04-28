# COLEP: Certifiably Robust Learning-Reasoning Conformal Prediction via Probabilistic Circuits

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 6, 8

## Abstract
Conformal prediction has shown spurring performance in constructing statistically rigorous prediction sets for arbitrary black-box machine learning models, assuming the data is exchangeable.
    However, even small adversarial perturbations during the inference can violate the exchangeability assumption, challenge the coverage guarantees, and result in a subsequent decline in prediction coverage.
    In this work, we propose the first certifiably robust learning-reasoning conformal prediction framework  (\name) via probabilistic circuits, which comprises a data-driven \textit{learning component} that trains statistical models to learn different semantic concepts,
    and a \textit{reasoning component} that encodes knowledge and characterizes the relationships among the statistical knowledge models for logic reasoning. To achieve exact and efficient reasoning, we employ probabilistic circuits (PCs) to construct the reasoning component.
    Theoretically, we provide end-to-end certification of prediction coverage for \name under  $\ell_2$ bounded adversarial perturbations. We also provide certified coverage considering the finite size of the calibration set.
    Furthermore, we prove that \name achieves higher prediction coverage and accuracy over a single model as long as the utilities of knowledge models are non-trivial.
    Empirically, we show the validity and tightness of our certified coverage, demonstrating the robust conformal prediction of \name on various datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
COLEP is a learning-reasoning framework for conformal prediction that provides improved certified prediction coverages under adversarial perturbations. The framework is composed of a learning/sensing component followed by a knowledge-enabled logical reasoning component. The learning component consists of several deep learning models while the reasoning component consists of one or more probabilistic circuits. Alongside the main classification task, the deep learning models are used to predict and estimate the probabilities of other concepts in the input e.g. shape, color etc. The PCs in the reasoning component encode domain knowledge specified as propositional rules over the class and concept variables and helps to ensure robustness against $\ell_2$ bounded adversarial perturbations to the input variables. The experiments show that COLEP achieves higher prediction coverages as well as smaller prediction set sizes compared to other SOTA methods.

### Strengths
The paper presents a novel idea to improve certified robustness of conformal prediction using deep learning models. To the best of my knowledge, this is the first work on using tractable probabilistic circuits to improve the coverage of conformal prediction.
   
A positive side of the work is its theoretical analyses. The authors have derived certified coverage for COLEP under both $ell_2$ and finite calibration sample size. And then show that COLEP received higher certified coverage compared to a single model. 

Experimental results are also promising.

### Weaknesses
 The manuscript is strong overall, but there are areas where it could benefit from further elaboration and additional empirical support. 

1. The reasoning part seems to be missing significant details to understand how the PCs are working together to reduce the error produced by the main classifier. The paper makes a strong assumption that the reader will be familiar with semantics of PC structures. There should be some brief introduction to these models. 

2. The leaf weights (factor weights) are assumed to be prespecified and then there are also the Bernoulli parameters estimated by the neural networks.  It is unclear how these estimated parameters, predictions (classes and concepts) and user defined knowledge rules are combined together to make robust decisions. The coefficients of the component PCs $\beta_k$ should be more clearly specified in the main manuscript.  

3. The theorems in the main paper need a more detailed discussion. Having only a short paragraph for each theorem doesn't fully explain the complexities and nuances involved, which doesn't give the paper's theoretical contributions their due.

4. To make the empirical evaluation stronger, the authors could consider using more datasets or testing against different types of attacks. This will help confirm that COLEP is robust and works well in various situations.

### Questions
1. How many PCs were considered in each of the experiments? Can the authors give an idea on the complexity of the PCs? 

2. Can the scope of the evaluation be extended to include the performance of COLEP against  other forms of adversarial attacks? 

3. Why wasn't the effect of varying the parameter $\alpha$ and $\rho$ on COLEP's performance analyzed?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors applied conformal prediction to a conformity score incorporating logic reasoning based on prior knowledge graphs and demonstrated that the resulting prediction intervals achieved desired coverage while being narrower compared to RSCP on three real data sets under l2 norm perturbations.

### Strengths
The authors adapted conformal prediction to a new scenario where a reliable knowledge graph is available and showed empirically that incorporating this side information can improve the efficiency of conformal predictions.

### Weaknesses
1. Is the F(mu) prefixed function with H rules? Is mu observed only for the training? (the knowledge graph encodes the relationship between, e.g.,  "stop" and shape info, but the goal is to predict if it is a stop sign).  I am confused about how pi_j(x) is calculated when mu is unknown.

2. It seems that the gain of COLEP originates from utilizing the prior knowledge graph through F(u) and u: The knowledge graphs incorporated are side information with both the graph relationship and u remained true against attacks. How robust does the method perform against contaminated graphs/u? More specifically, what happens when the relationships in the knowledge graph are not universally true, but hold with some probability, such as 70%? For example, the rule IsStopSign->IsOctagon might not always hold, and how does this affect the method's performance and the choice of the weight w?

3. Is it easy to calculate max|η|2≤δ ˆ πj (x + η) and min|η|2≤δ ˆ πj (x + η) for general probability assignment function pi_j(.)? The two main Theorems are from a brute-forth search of the worst-case scenario under perturbations, which are intuitively correct but it seems more important to show the feasibility of achieving this for general functions.

4. How are the weights w chosen in F(mu)? It seems that the choice of w is critical to the performance of the method, and it is unclear how practitioners should choose this value without overfitting to the test set. Some guidelines for choosing w are needed.

### Questions
1. Is the F(mu) prefixed function with H rules? Is mu observed only for the training? (the knowledge graph encodes the relationship between, e.g.,  "stop" and shape info, but the goal is to predict if it is a stop sign).  I am confused about how pi_j(x) is calculated when mu is unknown.

2. It seems that the gain of COLEP originates from utilizing the prior knowledge graph through F(u) and u: The knowledge graphs incorporated are side information with both the graph relationship and u remained true against attacks. How robust does the method perform against contaminated graphs/u?

3. Is it easy to calculate max|η|2≤δ ˆ πj (x + η) and min|η|2≤δ ˆ πj (x + η) for general probability assignment function pi_j(.)? The two main Theorems are from a brute-forth search of the worst-case scenario under perturbations, which are intuitively correct but it seems more important to show the feasibility of achieving this for general functions.

4. How are the weights w chosen in F(mu)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper offers a new construction for a conformal prediction pipeline that offers guaranteed coverage both in the exchangeable and in the adversarial perturbations case, and generally should offer improved adaptivity and set size whenever domain-specific learning-reasoning rules are provided. The main new component is the integration of probabilistic circuits into the construction of a nonconformity score of the APS (Romano et al) type, where an underlying model's class probabilities output is postprocessed according to a collection of reasoning rules, which help correct each class's predicted probability before plugging it into the APS score. The benefits of the reasoning components are investigated theoretically, by means of a theorem stating that under some assumptions marginal coverage will be strictly better with than without these components, as well as experimentally over three datasets and compared to two benchmark conformal method (one with adversarially robust guarantees).

### Strengths
This paper essentially constructs a novel type of score for conformal prediction; rather than the simple softmax layer-based constructions of some recent nonconformity scores like APS and RAPS, the idea here is to take such a softmax output from e.g. a neural net and, using domain specific learning-reasoning rules, postprocess each individual class's predicted probability to become appropriately corrected, and only then use them in an APS score-like fashion.

These corrections imply both the robustness properties (at least to l2 perturbations), as well as offer (subject to mild assumptions) theoretically guaranteed improvement over just using the underlying model's softmax outputs.  It is also more generally easy (as the authors show) to propagate estimation uncertainty through the learning-reasoning pipeline. This type of provable guarantees is, to my knowledge, novel and has not come up in the conformal literature before.

Moreover, the proposed technique is more flexible than standard conformal prediction, in that it can provide guarantees not just over all classes, but also for each class separately (at its own coverage threshold).

These above technical innovations, as well as the practical potential of learning-reasoning components to improve domain-specific performance of conformal prediction, lead me to conclude that the proposed paper would be a novel and interesting addition to the conformal literature.

### Weaknesses
1. Empirical evaluation is quite limited, which is quite unfortunate given that including more settings beyond datasets as simple as CIFAR-10, as well as more benchmarks, would likely let the guarantees afforded by the learning-reasoning setup shine even more: both in terms of the ability to construct rules specific to each considered setting, as well as the resulting adaptivity compared to other conformal scores/methods.

Relevantly, I was quite confused when the authors repeatedly call the APS score of Romano et al (2020) 'SOTA'. It is certainly one of the existing reasonable conformal approaches to use, but by no means state of the art when it comes to adaptivity and especially set size. For instance, its generalization and improvement, the RAPS nonconformity score introduced in "Uncertainty Sets for Image Classifiers using Conformal Prediction", may still be considered close to the SOTA frontier for many domains --- and it would be very pertinent to include it, along with further improved conformal methods developed thereafter. Also, CIFAR 10 not quite sounding like the natural domain to apply potentially highly complex learning-reasoning boosts, it'd be wise to show the performance of the framework on Imagenet; as a byproduct, it would help me convince myself of the tractability of useful learning-reasoning in more challenging settings. In any case, having just three relatively simple datasets and only two comparison methods, Romano et al and Gendler et al, appears insufficient to fully explore the relative advantages of learning-reasoning.

2. The main other weakness to me is the overbearing nature of the notation used, and the overall presentation. It took me many hours to internalize the type of the guarantees that learning-reasoning components lead to, and even the notation itself. Moreover, especially the multi-subscript-superscript notation involved in both theorem statements and proofs related to the learning-reasoning component was very hard to parse and even read. The notational review in the last appendix was a nice touch, but only marginally helpful as it only listed some of the relevant notation; Diagram in Figure 4, describing the overall certification flow, also felt confusing and didn't really help, making me resort to understanding text only. Instead of structured definitions of the main notations and concepts (using appropriate latex environments), everything was crammed into the paragraphs, thus diluting the structure of the presentation and making it hard to backtrack to the context in which a piece of notation was originally defined.

### Questions
1. The experimental section needs strengthening; please see above for suggestions/guidelines on directions.
2. In discussing experimental results, it is of especial interest to discuss which learning-reasoning components were used in each domain. Other details are quite standard and common in the conformal literature, but this one is novel and thus should be propagated to the main part rather than left in the appendix. The current running example is the stop sign example, but it would be very useful to have a walk-through of how the rules were implemented in actual experiments.
3. In the same vein, right now the experimental part only features plots of standard metrics (coverage, set size, ..) Meanwhile, I would like to see a visualization of what the learning-reasoning components do to the predictions of the underlying model --- e.g. which rules turned out to correct the initial estimates by the largest amount, etc.
4. Notation needs to be significantly improved and clarified to achieve readability.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
This paper introduces COLEP a certifiably robust learning-reasoning conformal prediction framework. Authors leverage probabilistic circuits for efficient reasoning and provide robustness certification. They also provide marginal coverage guarantees using conformal prediction methods. Finally, by performing several experiments, they highlight the relevance of their proposal.

### Strengths
First, I would like to make it clear that this paper is not in my area of expertise. That is why I had some difficulty understanding it. However,

1) the contributions of the paper seem to be significant.

2) experience suggests that COLEP is competitive with previous work.

### Weaknesses
The paper is very dense and difficult to read.

Citations are not appropriate. For example, in the related work on conformal prediction, the first sentence mentions articles from 2021, and the seminal articles, notably by Vovk and others, are not cited.

There is no "limitation" in the conclusion. This section should be added.

Minor:

"with the guarantee of marginal prediction coverage: ..." the inclusion should be a $\in$.

### Questions
Why is COLEP better suited to conformal prediction than already existing methods?

What does "certified conformal prediction" mean? Is this different from saying that we have a marginal coverage guarantee?

The paper claims that it achieved "a certified coverage of COLEP" but, for example in Figure 2, the coverage obtained with COLEP is well below 0.9. Can you explain this in more detail?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose conformal prediction sets that are robust to adversarial perturbations -- they maintain the nominal coverage for any perturbed input in the threat model. The main idea is to leverage a learning-reasoning component which can improve the worst-case bounds on the predicted conditional class probabilities. Constructing the prediction sets using the worst-case scores derived from the worst-case (corrected) class probabilities yields adversarially robust coverage.

### Strengths
In terms of originality, the approach can be seen as the clever combination of two main ideas:
- improved worst-case bounds on the class probabilities using a reasoning component
- using worst-case bounds on the conformity scores to get robust sets 

Both ideas have been explored in the literature, but their combination leads to improved results. Specifically, more efficient (smaller) sets compared to RSCP while having the same guarantee, and larger worst-case lower bound.

The technical and theorethical components of the paper are sufficiently detailed and rigorous. Theorem 3 can be seen as a generalization of Theorem 2 by Gendler et al. The analysis in Section 6, while making stronger assumptions, is interesting and shows when we can expect improvement.

The exprimental results are expected since the derived bounds are tighter.

The contribution is significant, as is the improvement over the previous SOTA.

### Weaknesses
While the authors do consider the finite-sample error induced by the finite size of the calibration set, they fail to account for the finite-sample error due to the Monte-Carlo sampling (they use 10000 samples) when estimating the expectations under the randomized smoothing framework. Therefore, the resulting sets are only asymptotically valid. Specifically, the randomized smoothing procedure estimates the expected probability of a class under a Gaussian perturbation of the input. This expectation is approximated using a finite number of samples, introducing a statistical error that is not accounted for in the coverage guarantee. This means that the stated coverage is only valid in the limit of infinite samples, and the actual coverage for a finite number of samples may be lower than the nominal level. The magnitude of this error depends on the variance of the smoothed probabilities and the number of Monte Carlo samples, and should be explicitly bounded to provide a sound certificate.

As pointed out by a concurent ICLR submission (https://openreview.net/forum?id=BWAhEjXjeG) RSCP also suffers from the same issue and it is non-trivial to correct for this. The same issue is also discussed among the reviewers and the RSCP authors on their respective openreview page (https://openreview.net/forum?id=9L1BsI4wP1H). Naively, one would have to apply a union bound over all examples in the calibration set and the test example such that each of the randomized smoothing expectations hold simultaneously. There is also a subtler alternative solution. When correcting RSCP for this error the resulting sets end up returning all labels, i.e. they are useless. It is not clear to which degree COLEP suffers from the same issue. In any case, the "fix" proposed by the concurent submission is orthogonal and can be applied to COLEP as well. Still, this finite-sample issue needs to be addressed in the paper, especially given that the goal is to produce a sound certificate. 

The second weakness is in the PGD attack. The authors state "For fair comparisons, we apply PGD attack (Madry et al., 2018) with the same parameters on CP, RSCP, and COLEP". However, it is unclear whether the PGD attack is adaptive, i.e. it takes the learning-reasoning component into account. An adaptive attacker can in fact know that a reasoning component is used, and thus can try to perturb the input such that both the class and the concept probabilities are suitably changed as to fool the entire pipeline. For example, the attacker could try to maximize the cross-entropy loss of the final prediction, taking into account the gradients through both the learning and reasoning components. While this is not critical, not using adaptive attacks makes the conclusions drawn from Figure 3 less reliable.

### Questions
1. How does COLEP perform when accounting for finite-sample errors when estimating randomized smoothing expectations?
2. In section 3 you have "assume that the data samples are drawn i.i.d. (thereby exchangeably)". Is the i.i.d. assumptions necessary for the learning-reasonig component, or can this be relaxed to just exchangeability as with vanilla CP?
3. Is the PGD attack adaptive, i.e. takes the reasoning component into account?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
