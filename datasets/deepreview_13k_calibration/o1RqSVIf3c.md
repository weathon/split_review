# Bayesian Preference Elicitation for Personalized Prefactual Recommendation

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3

## Abstract
A prefactual recommendation, also known as an algorithmic recourse, provides actionable guidance to an individual to overturn a machine learning prediction at a minimal cost of efforts. Existing methods impose an explicit assumption on the cost function, but in reality, different individuals may possess diverse and unique cost preferences. Failing to adapt the guidance to an individual's cost preference can lead to irrelevant and inefficient recommendations. To personalize the guidance to the individual cost, we propose a Bayesian preference elicitation framework that learns the cost function from the individual's feedback on a small number of pairwise comparisons. This framework relies on a sequential, mutual-information-maximization question-answering scheme to obtain a posterior distribution of an individual's cost weighting matrix. We then deploy this posterior to recommend a graph-based sequential guidance with minimal expected cost, leading the individual to achieve the desired algorithmic outcome. Numerical experiments on synthetic and real-world datasets demonstrate the power of our method in capturing the individual's preference and recommending personalized recourse.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes the so-called Prefactual Recommendation by Bayesian Preference Elicitation algorithm for personalized recommendation.

### Strengths
Personalized recommendation is an important question in the field of learning to rank.

### Weaknesses
1. Presentation is poor (see my questions below)
2. The paper focuses on binary class only, which constraints the application of this algorithm
3. No significant improvement in comparison with the baseline.
4. The theoretical analysis may not be enough (see my questions below)

### questions:
------------------------- For Presentation -------------------------

1. It's not clear enough why this paper applies Mahalanobis distance is selected. Why does this distance make sense to serve as the cost function? How is it compared with many other distance functions and other cost functions?

2. The main message of the main theorem of this paper is hard to follow. In (2) of Theorem 3.2, I don't believe any author could easily figure out the asymptotic manner of this probability (either it's a constant, close to 0, or close to 1?).

3. Following 2, the complexity of the proposed algorithm is unclear and there is no analysis on how many samples (how large $M$) are needed for the algorithm.

4. It's not clear what is the difference between the proposed algorithm with FACE. Does FACE also use shortest path? If so, what's their cost?

------------------------- For Experiments -------------------------

1. I don't think the proposed algorithm is better than the baselines because it has almost the same cost as FACE if using $\ell_1$ as the true cost. The improvement in Mahalanobis distance as the true cost is not compatible because this is the same distance used in the algorithm and to some extent, the algorithm cracks the ground truth.

2. Why the baselines are not compared in Section 6.3?

3. (Minor) I suggest moving other baselines (Appendix D.2) to the main text.


------------------------- For Theoretical Analysis -------------------------

1. The complexity analysis of the whole proposed algorithm is missing or lacks discussion.

2. (Minor) Asymptotic mutual information is missing citation.

### Questions
------------------------- For Presentation -------------------------

1. It's not clear enough why this paper applies Mahalanobis distance is selected. Why does this distance make sense to serve as the cost function? How is it compared with many other distance functions and other cost functions?

2. The main message of the main theorem of this paper is hard to follow. In (2) of Theorem 3.2, I don't believe any author could easily figure out the asymptotic manner of this probability (either it's a constant, close to 0, or close to 1?). 

3. Following 2, the complexity of the proposed algorithm is unclear and there is no analysis on how many samples (how large $M$) are needed for the algorithm.

4. It's not clear what is the difference between the proposed algorithm with FACE. Does FACE also use shortest path? If so, what's their cost?

------------------------- For Experiments -------------------------

1. I don't think the proposed algorithm is better than the baselines because it has almost the same cost as FACE if using $\ell_1$ as the true cost. The improvement in Mahalanobis distance as the true cost is not compatible because this is the same distance used in the algorithm and to some extent, the algorithm cracks the ground truth.

 2. Why the baselines are not compared in Section 6.3?

3. (Minor) I suggest moving other baselines (Appendix D.2) to the main text.


------------------------- For Theoretical Analysis -------------------------

1. The complexity analysis of the whole proposed algorithm is missing or lacks discussion.

2. (Minor) Asymptotic mutual information is missing citation.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
An approach for personalized algorithmic recourse based on Bayesian
preference elicitation. The apprach selects queries to the user that
maximize mutual information between the response and the cost
function, and provides an efficient solution to choose queries and
compute the posterior of the cost distribution.

### Strengths
A solid work presenting a methodologically sound and novel solution to
bayesian preference elicitation of cost functions, complemented with
an efficient implementation.

The manuscript is complemented with an extensive supplementary section
detailing proofs, extensions from pairwise to listwise comparisons,
and additional experimental results.

### Weaknesses
From an algorithmic recourse perspective, the approach builds on the
FACE algorithm, that achieves recourse by selecting a
recourse-achieving instance from the training set. This can be badly
suboptimal for users that are not similar enough to any specific
training user. While experimental results in the appendix indicate
competitive results with some alternatives using different strategies,
this limitation should be mentioned in the main paper. As far as I
understand, this limitation is not due to the proposed Bayesian
approach, but rather to the recourse strategy employed, so that
adapting the approach to deal with other recourse strategies could
further strenghten the contribution.

There is a recent research line in the algorithmic recourse community
that advocates the need for a causal perspective in algorithmic
recourse, where the effect on a action on causally dependent features
of the user state is accounted for.  Karimi et al. "(Algorithmic
Recourse: from Counterfactual Explanations to Interventions", 2020)
demonstrated that optimal algorithmic recourse cannot be achieved if
this causal perspective is ignored. This aspect is ignored in the
manuscript, making the overall approach (which is perfectly fine for
generic personalized recommendations) less appealing in the
algorithmic recourse context.

### Questions
Can the approach be adapted to work with recourse strategies that generalize beyond training examples?


Can you comment on the impact of the lack of a causal perspective on recourse achievement and cost minimization?

### Soundness
4 excellent

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In recourse recommendation the system suggests a sequence of feature realizations that leads from a negative classification to a positive one. Each step in the sequence is associated with personalized cost. The goal of the agent is to learn the user's cost (preferences) while simultaneously directing them to a positive state, incurring minimal overall cost on the way.
This paper proposes an approach for recourse recommendation which uses Bayesian preference elicitation for learning the user's preferences. An approximate procedure for transition selection is presented as well as an approximate posterior update. Numerical results on a few datasets are included.

### Strengths
* Personalized recourse recommendation is an interesting problem
* A Bayesian preference elicitation approach to personalization is plausible
* The paper is clearly written and I did not find any errors in the derivations

### Weaknesses
 * Missing complexity analysis
* Missing comparison to sampling and evaluation of approximation quality
* Some technical issues (eg, kappa goes to inf)

* Theorem 3.2 assumes that kappa goes to infinity which corresponds to noiseless responses.
  * How to understand Eq (3) (and the rest of section 4) with kappa=inf?
  * Also, the link function is approximated by a linear function (section 4.1), so how would that work when kappa=inf?
  * May be good to show empirically how this assumption affects the results vs using final kappa.
* There are several layers of approximation (eg, kappa=inf, approximating sigmoid with a linear function, finite iterations for the projection in Alg 1), it would be helpful to clearly state all of them in a single place before giving all the details. It may also be helpful to do some ablation studies and see how each level of approximation affects the overall performance.
* How does sampling compare to the analytical solution?
  * A comparison to sampling is missing from the experiments. This is important for validating the quality of the approximate analytical solution as well as the computational efficiency claims.
* Complexity:
  * It would be good to state the overall complexity of: pair choice, posterior update, and recourse generation
  * Solving an optimization problem for each possible value of m (|m_{t-1}-d| values) seems expensive
  * Comparing N^2 pairs each turn seems expensive
  * Problem 7b is an integer linear program, which is NP-hard in general, so the statement about the solution being computationally efficient seem exaggerated (especially with no detailed complexity analysis). It should be at least possible to show empirically which problem sizes can be handled and at what cost.
* Choice of x points:
  * Does it make sense to consider negative-negative pairs? Or choosing unlabeled points for comparison? It would be good to justify the positive-positive choice.
  * The graph-based approach of section 5  considers only transitions between points from the training data, but it may be possible to transition to new points not in the data (possibly unrealizable). Can such transitions be accommodated in your framework? If we have access to the classifier we can know the label of any point.
  * What are typical path lengths in the experiments?
* Section 6.1:
  * What is the dimension d?
  * The model seems rather small (90 neurons in 3 MLP layers)
  * What is the justification for the choice \tau\kappa=1?

Minor/Typos:
==========
* Eq (2): I could not find b
* Eq (3): nit - missing “(“ for R_ij
* Why not define z_i and z_j earlier and simplify notation, for example in \sigma_i and \sigma_j, and in M_ij?
* Showing validity results in Tables 1 and 2 (and 4 and 5) seems redundant since they are always 1. This can be stated once in the text. Also, x_r is chosen such that it returns a positive prediction, so it is not clear when that would not be the case.
* Section 6.3: “consistent decrease as the number of questions increases” is a bit overstated, it seems that in most plots the rank increases initially before decreasing.

### Questions
* Theorem 3.2 assumes that kappa goes to infinity which corresponds to noiseless responses.
  * How to understand Eq (3) (and the rest of section 4) with kappa=inf?
  * Also, the link function is approximated by a linear function (section 4.1), so how would that work when kappa=inf?
  * May be good to show empirically how this assumption affects the results vs using final kappa.
* There are several layers of approximation (eg, kappa=inf, approximating sigmoid with a linear function, finite iterations for the projection in Alg 1), it would be helpful to clearly state all of them in a single place before giving all the details. It may also be helpful to do some ablation studies and see how each level of approximation affects the overall performance.
* How does sampling compare to the analytical solution?
  * A comparison to sampling is missing from the experiments. This is important for validating the quality of the approximate analytical solution as well as the computational efficiency claims.
* Complexity:
  * It would be good to state the overall complexity of: pair choice, posterior update, and recourse generation
  * Solving an optimization problem for each possible value of m (|m_{t-1}-d| values) seems expensive
  * Comparing N^2 pairs each turn seems expensive
  * Problem 7b is an integer linear program, which is NP-hard in general, so the statement about the solution being computationally efficient seem exaggerated (especially with no detailed complexity analysis). It should be at least possible to show empirically which problem sizes can be handled and at what cost.
* Choice of x points:
  * Does it make sense to consider negative-negative pairs? Or choosing unlabeled points for comparison? It would be good to justify the positive-positive choice.
  * The graph-based approach of section 5  considers only transitions between points from the training data, but it may be possible to transition to new points not in the data (possibly unrealizable). Can such transitions be accommodated in your framework? If we have access to the classifier we can know the label of any point.
  * What are typical path lengths in the experiments?
* Section 6.1:
  * What is the dimension d?
  * The model seems rather small (90 neurons in 3 MLP layers)
  * What is the justification for the choice \tau\kappa=1?

Minor/Typos:
==========
* Eq (2): I could not find b
* Eq (3): nit - missing “(“ for R_ij
* Why not define z_i and z_j earlier and simplify notation, for example in \sigma_i and \sigma_j, and in M_ij?
* Showing validity results in Tables 1 and 2 (and 4 and 5) seems redundant since they are always 1. This can be stated once in the text. Also, x_r is chosen such that it returns a positive prediction, so it is not clear when that would not be the case.
* Section 6.3: “consistent decrease as the number of questions increases” is a bit overstated, it seems that in most plots the rank increases initially before decreasing.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presents Bayesian PR, a method to generate prefactual recommendations by learning a personalized cost function by collecting pairwise feedback from a user. These recommendations lie in the algorithmic recourse field since they give actionable feedback to a user to overturn the prediction of a machine learning model. The authors provide a Bayesian framework to learn a posterior distribution given the user feedback, by looking at the mutual information. Lastly, this method is incorporated in a graph-based recourse method, that is evaluated on real-world datasets.

### Strengths
The paper explains the problem clearly and concisely, motivating the various methodological choices. It is also quite understandable and grounded in theory. The problem itself is very interesting and I think it has significant implications for the algorithmic recourse literature.

### Weaknesses
I think this paper fails to discuss and compare some important baselines, and this diminishes the novelty and soundness of the approach. [1] tries to give personalized recourse options by learning a cost function from experts, which would provide a strong baseline to begin with. Secondly, [2] provides a Bayesian framework for learning personalized cost functions for algorithmic recourse, via pairwise queries, robust to user uncertainty. 

More specifically, it is not clear to me the advantage or the originality of the proposed Bayesian PR over the method in [2], which is cited by the authors in the paper, but not discussed anywhere in the main manuscript.

The same concerns apply to the experimental section. I believe [1] and [2] are closely related baselines which the authors should consider testing against.

### Questions
- What is the difference between the proposed Bayesian PR and the method proposed in [2]? After a closer look, they are closely related and I would appreciate hearing how the proposed approach differs from the one presented in [2].

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
