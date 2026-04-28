# Online Convex Optimization with Prediction Through Accelerated Gradient Descent

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
We study online convex optimization with predictions, where, at each time step $t$, predictions about the next $k$ steps are available, and with coupled costs over time steps, where the cost function at time step $t$ depends on the decisions made between time $t-a$ and time $t+b$ for some nonnegative integers $a,b$. 

We provide a general recipe to run synchronous update in an asynchronous fashion that respects the sequential revelation of information. Combined with existing convergence results for convex optimization using inexact first-order oracle, we show that acceleration is possible in this framework, where the dynamic regret can be reduced by a factor of $(1-O(\sqrt{\kappa}))^{\frac{k}{a+b}}$ through accelerated gradient descent, at a cost of an additive error term that depends on the prediction accuracy. This generalizes and improves the $(1-\kappa/4)^k$ factor obtained by Li & Li (2020) for $a+b = 1$. Our algorithm also has smaller dependency on longer-term prediction error. Moreover, our algorithm is the first gradient based algorithm which, when the strong-convexity assumption is relaxed, constructs a solution whose regret decays at the rate of $O(1/k^2)$, at a cost of an additive error term that depends on the prediction accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the problem of online convex optimization with predictions, where predictions about the next $k$ steps are available and the costs are coupled over time steps. Specifically, the authors propose two algorithms, namely online-PGM and online-AGM. Compared with the existing results, the author's analysis implies that their online-AGM algorithm can reduce a part of the dynamic regret when loss functions are strongly convex and smooth. Moreover, if the functions are not strongly convex, the authors also establish a theoretical guarantee on the dynamic regret bound of the proposed algorithms.

### Strengths
1) Two new algorithms, especially online-AGM, are developed for the problem of online convex optimization with predictions and coupled cost.
2) By utilizing some nice properties of the accelerated gradient descent method, the proposed online-AGM algorithm can improve the dynamic regret bound established by previous studies (note that the existing result holds only for a special case of the problem studied in this paper).
3) The authors also establish dynamic regret bounds for their algorithms in the case with smooth but not strongly convex functions.

### Weaknesses
1) The studied problem seems to be very complicated but is not well-motivated. The three motivating examples discussed in this paper are not convincing enough. Specifically, for the first example, it is unclear what applications the so-called aggregate information must be considered. For the second example, although the delayed decision making can be regarded as a special case of the studied problem, the delayed problem itself has been well studied, and it is not necessary to consider a more complicated setting unless some new insights can be derived. For the third example, its connection to online applications is unclear, and I especially cannot understand why it is related to online learning with prediction.
2) The contributions of this paper seem to be incremental, and actually are not described clearly. First, although two algorithms are proposed and analyzed in this paper, it seems that online-AGM is better than online-PGM in both theoretical guarantees and the experimental results. As a result, the significance of online-PGM seems to be questionable. Second, as discussed in Sections 1.2 and 1.3, the main theoretical improvement of this paper is achieved by the online-AGM algorithm, and limited to one of the two components of the dynamic regret bounds. More specifically, it seems that such an improvement is mainly achieved by refining the initialization by utilizing the accelerated gradient descent method, whose novelty is limited.
3) The assumptions on loss functions and predictions are too strong, which will limit the application of the proposed algorithms. Moreover, some assumptions are not described clearly. For example, according to the abstract, only the predictions about the next $k$ steps are available. However, according to lines 72 to 63, it seems that the predictions about all the future steps should be available.

### Questions
Besides the weaknesses discussed above, I am also concerned about the writing of this paper and would like to provide some suggestions in the following.
1) The latex environment utilized for *Figure* should be checked. For example, in this paper, the captions for Figures 1, 2, and 3 are presented above these figures.
2) The authors should first discuss the technical challenges of minimizing the dynamic regret of the problem studied in this paper, and provide more technical details of existing algorithms, which is helpful to understand the technical novelty of the proposed algorithm.
3) The authors should clearly explain whether the proofs of Theorems B.1 and B.2 belong to the contributions of this paper. If the answer is not, a simple reference to previous studies is sufficient for utilizing these results.
4) The meaning of $\kappa$ is unclear when we read the abstract, and the meaning of $L$ is unclear when we read Theorem 1.1.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies an online convex optimization setting in which 
the losses at time $t$ may depend on both a history of previous decisions, as 
well as future decisions, generalizing the standard OCO with memory setting.
Algorithms are designed for smooth+strongly-convex losses, as well as 
for losses which are only strongly convex. Dynamic regret guarantees of the form
[initialization error]+[prediction errors] are proven. An online update scheme is 
proposed to allow for more incremental computation.

### Strengths
- The proposed problem setting it is a very natural generalization of the usual OCO with memory setting.
- The results are novel and generalize those of prior works to a harder setting (access to only *inexact* predictions)

### Weaknesses
 - Typically dynamic regret guarantees scale with some measure of how 
much the comparator sequence varies, reflecting the "difficulty" of 
a given sequence. Here no such term appears in the bounds, and instead there 
are terms which involve prediction error of the future predictions given at the start of the round. 
This seems not very meaningful to me; it essentially just says that the performance of the algorithm 
will be roughly as good as the performance of the provided predictions. But there is no general strategy for 
choosing a good sequence of these predictions, because at time $t$ the predictions $t+1,\ldots,t+b$ are chosen 
at once, with no feedback. So the dynamic regret guarantee could be arbitrarily high,
even for "easy" comparator sequences.

- The draft suffers from several issues in writing quality
    -   The paper is incomplete, ending abruptly after the numerical experiments
        section with no conclusion / summary. 

    - There are many instances of oddly structured, difficult-to-parse sentences 
    (see, e.g., the first line of the abstract)

    -   The paper is somewhat oddly structured, with the main results preceeding
        the contributions section
        
- Figure 3 is pretty hard to follow, and the color coding is never really explained.
  Perhaps this would fit better in an appendix, wherein a proper concrete explanation of 
  what's happening in the figure could be given. Ideally with some simple numerical values
  so the reader can more easily trace what's happening

-   Suggestion: the theory takes up the vast majority of the paper, and the experiments
    are not particularly interesting other than providing a sanity check that
    the algorithm works. I suggest positioning 
    this work as a theory paper, and moving the experiments to the appendix entirely, so that
    there is room to provide a proper discussion of the results and conclusion at the end of the paper.

### Questions
- At time $t$, the learner suffers a loss which depends on $[x_{t-a},\ldots,x_t, \ldots,x_{t+b}]$, 
and also receives feedback which is a function of these values. This implies that the learner must either commit to
$x_{t+1},\ldots, x_{t+b}$ ahead of time, on round $t$, or is allowed to rescind their choice and change their 
choice of these variables on the next round. Which protocol is being used exactly?

### Soundness
3

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
4

### Summary
This paper studies online convex optimization with predictions. The prediction means that at each time step t, predictions about the next k steps are available to the decision maker. The cost is a (strongly) convex function that not only depends on the current decision, but also depends on the actions chosen in the past and in the future. Based on the question proposed and studied in Li & Li (2020) and on the algorithms designed in (Li & Li, 2020; Li et al., 2021), this papers proposes an algorithm to solve this problem, and they show that the dynamic regret of the algorithm can be reduced by a exponentially decayed factor through accelerated gradient descent, at a cost of an additive error term that depends on the prediction accuracy.

### Strengths
1. Considering predictions in online convex optimization is interesting and important.
2. The proposed algorithm in this paper extends existing results in several meaningful directions.
3.  Proofs of the theoretical results are provided, and numerical experiments support the author's claims.

### Weaknesses
1. Although the paper mainly focuses on the theory, could you provide more concrete examples for the meaning of predictions in online convex optimization settings? Specifically, you could 1-2 specific real-world examples of how predictions could be used in online optimization problems, such as in energy systems or supply chain management.
2. In my opinion, it does not seem to be practical for the present cost function to be related to future decisions, since the future decision is a time-varying variable that can be independent of the decision in the present moment. In general, the decision maker will only make the current moment decision $x_t$ at time t. Could you please give a practical example detailing how the current cost function relates to future decisions? 
3. About the parameter $\theta$: It seems that this paper considers the full information case rather than the bandit information case in online convex optimization, since both the cost function f_t and its gradient are used in the proposed algorithm. Regarding this point, could you clarify that after predicting $\theta$, is the specific expression of the cost function f_t() revealed to the decision maker or not? I suggest that the authors explicitly state in Section 1.1 whether the full cost function f_t is revealed after predicting θ, or if only gradient information is available.
4. In Li et al. TAC 2021, there is an initialization step in their algorithms that can effectively reduce the initialization error ||x^(init)-x^*||. The initialization step together with the gradient update step in their algorithms yield the overall regret bound of the algorithms. In this paper, the regret bounds of the proposed algorithm directly depend on R_0=||x^(init)-x^*|| which can scale as O(T) and in turn makes the overall regret bounds large. Could you comment on this point regarding why R_0 shows up in the regret bounds?
5. Compared to the existing papers, could you please describe/summarize the major novelty/technical difficulties in the algorithm design and regret analysis in this paper? In particular, it seems that the regret analysis follows closely from those in Devolder et al 2013a,b. 
6. All the text sizes in the figures/algorithms/tables are too small; please try to improve the presentation/display of the relevant content.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigate online convex optimization where the loss $f_t$ is incurred with decision made through a time window [t-a, t+b]. This framework improves dependence on the side information accuracy and is a generalization of Li & Li (2020), thus echoes the open question among improved long term robustness on side information accuracy.

### Strengths
- The proposed set-up is a generalization of many problems beyond Li & Li, (2020). Which are motivated through 3 examples.
- due to the more generalized framework, the handling of unsynchronized update is more complex. Nevertheless, the paper provides detailed illustration on the update and its implication of  generalization to "fill the table" approach.
- The experimental results follows the derived bound in terms of side information prediction error and condition number

### Weaknesses
 - One of the main claim: more robust to long term prediction error than previously established results. It would be interesting to have experimental comparison especially the experiment set-up is the same as the previous result.

- the unsynchronized update generally requires each node to wait for all necessary information from descendants and neighbours, thus the output $x_s^{l}$ is not exactly the sense of  ``online prediction'' where the decision variable $\bar{x}_{l}$ needs to be made in a timely manner regardless of the feedback. So I feel a bit concerned with the claim that this framework belongs to online prediction when motivated from the delayed decision making prospective

- it is a bit hard to established the improvement of this paper compared to previously established results, or its' optimality. Since the only trackable comparison is through motivating example 1 when $(a, b) = (1,0)$. and

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
2
