# Shapley Value Approximation based on k-Additive Games

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 3, 3, 3, 5

## Abstract
The Shapley value is the prevalent solution for fair division problems in which a payout is to be divided among multiple agents. By adopting a game-theoretic view, the idea of fair division and the Shapley value can also be used in machine learning to quantify the individual contribution of features or data points to the performance of a predictive model. Despite its popularity and axiomatic justification, the Shapley value suffers from a computational complexity that scales exponentially with the number of entities involved, and hence requires approximation methods for its reliable estimation. In this paper, we propose SVA$k_{\text{ADD}}$, a novel approximation method that fits a $k$-additive surrogate game. By taking advantage of the assumption of $k$-additivity, we are able to compute the exact Shapley values of the surrogate game in polynomial time, and then use these values as estimates for the original fair division problem. The efficacy of our method is evaluated empirically and compared to competing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides a novel method to approximate the Shapley value. While no theoretical approximation guarantees are provided in this paper, an empirical evaluation is provided in the context of determining the contribution of different features to model accuracy / MSE in classification / regression problems through their Shapley values, i.e., the marginal contribution to model performance due to the features. The empirical approximation ratio of Shapley values obtained by different approximation algorithms are compared by computing the MSE with the true, exact Shapley values. The main takeaway the authors highlight is that the newly proposed method achieves a competitive MSE to other algorithms.

The main technical contribution is a novel approach for approximating the Shapley values of players in a cooperative game where a valuation function assigns a value to each coalition. Their approach involves:
- Sampling T coalitions and computing their exact Shapley interaction values exactly. 
- Then, a surrogate k-additive cooperative game, and corresponding valuation function, is "learned" using existing (to the Authors: please correct me if I am wrong here) techniques which provides an analytical solution which can be performed in polynomial time in a way that minimizes the MSE of (weighted) Shapley interaction values. Here, a k-additive game is one where the interaction values of coalitions of size greater than k is 0.
- Then, Shapley values of players in the k-additive game is known to be computable in polynomial time which will be used as estimates of the Shapley values of players in the original game.

In the empirical evaluations, the features in a machine learning problem are considered as the players in a cooperative game, and the goal is to determine or "explain" the contribution of each feature towards the performance of some learning algorithm.

### Strengths
- The technique of using k-additive games to approximate the Shapley values is novel and may be of interest beyond the use case highlighted by the authors. The paper makes a clever use of existing results. I find the problem of approximating Shapley values and the application of explaining feature importances to be well motivated.
- The method is well motivated and the different components seem sound and worth evaluating.
- The paper is overall well organized and it is easy to follow the high level ideas.
- The experimental results validate their approach and the proposed algorithms achieve a competitive approximation ratio with other algorithms under different "budget constraints" on the number of sampled coalitions.

### Weaknesses
 - A running time comparison of the different algorithms would have provided a useful way to compare against different approximation algorithms which seem to achieve a very similar approximation ratio.
- It is counterintuitive that the MSE of Shapley value approximations gets worse as the number of samples increase. There is a brief intuition provided in the paper, but it is concerning. As Figure 3 shows, for certain problems, competing algorithms obtain better approximations as number of samples increases, but the proposed method gets worse. It is not clear from the paper if this comes with some other benefit e.g. running time. Due to this, I am not confident about the significance of the new algorithm. There does not seem to be a clear takeaway for when a practitioner should use this algorithm.
- It is not clear what the real world importance of using a small number of samples is, which is the regime in which the proposed method outperforms others. This will likely need further experiments.

### Questions
- Could you address the main question of what the takeaway from this paper is? E.g. is there a clear running time or other resource usage advantage of practical relevance using the proposed method? Could you please share any experimental results?
- Could you elaborate on the motivation for focusing on the Shapley values of features, as opposed to e.g. the training data points? Was this evaluated?
- One of the claimed advantages is that the proposed method does not make any assumptions on the value functions. Could you elaborate on the practical importance of this? For example, are there examples of practically relevant games where the value functions result in poor approximations by other methods that are handled better by the proposed method?
- Could you elaborate on the downstream effect of better estimates of Shapley values on model performance on the machine learning task? I do not find any experiments on this. Maybe I am missing something, or could you discuss their exclusion?

### Soundness
3

### Presentation
2

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
This paper considers the problem of approximating the Shapley value in polynomial time. To do so the authors propose a novel approach of approximating the value by defining a surrogate $k$-additive game.They propose an algorithm that finds the Shapley values for a $k$-additive game in polynomial time and a method of sampling that helps us use this algorithm to approximate the Shapley value in the general case. They provide empirical evaluations to support this approach. Figure 1 presents a good summary of the whole contribution of this work.

### Strengths
The paper is well-written and the problem is very well-motivated and natural. The idea of using a $k$-additive surrogate game also seems novel.

### Weaknesses
 - It is not clear what the running time of the proposed algorithm is. You are presenting an algorithm to approximately solve a problem which we can exactly solve in exponential time, but it is not really clear what the running time is. How much is this better than exponential? I don't think that this algorithm is polynomial in terms of $k$ (which is fine) but you need to be more formal than just saying the algorithm runs in polynomial time. The least that I expect is to see the running time of the algorithm for different values of $k$ in the experiments.
- It is not clear how you sample $T$ coalitions in polynomial time. If you first find the probability of each coalition, then since we have exponentially many coalitions the running time is not polynomial. I think further details are needed here.
- I think it is necessary to mention what tool/mechanism you use to solve the optimisation problem. In addition it is better to clearly state how many variables and constraints you have in the optimisation.
- The plots are too small and hard to read. You should keep a few of them in the body and differ the rest to the appendix.

### Questions
Please explain how you sample a coalition in polynomial time, and how does the running time of Algorithm 1 depend on different parameters.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a fast heuristic for computing Shapley value. The idea is to restrict to k-additive games (i.e., just assume this structure applies), which leads to a polynomial time algorithm for computing the Shapley value. The overall algorithm uses limited number of coalitions to derive a k-additive game that best fits the studied game, and then derive the Shapley value of the k-additive game, which serves as a fast heuristic for estimating the true Shapley values.

### Strengths
The k-additive assumption seems to be a reasonable assumption for a lot of the settings, so it is likely that the proposed heuristic would perform well in those settings.

### Weaknesses
There are a few downsides of the proposed approach. First, it is not clear how to pick k. It seems fairly arbitrary to choose k=3. Second, the performance of the proposed approach does not consistently outperform the existing baselines. It appears that the baseline algorithms have the advantage that with more and more samples, they converge to accurate Shapley values, but the proposed algorithm does not have this property. Third, other than experiments, there is no discussion on when the k-additive game assumption (for the most part) holds and how to test for it. The choice of k=3 lacks theoretical justification and the paper does not explore the sensitivity of the results to different values of k. The lack of consistent outperformance against baselines is concerning, especially since the baselines are expected to improve with more samples, while the proposed method's accuracy seems capped by the k-additivity assumption. Furthermore, the paper does not provide any guidance on how to assess the validity of the k-additive assumption for a given problem, which limits the practical applicability of the method.

### Questions
I see that the number of function evaluations is sometimes a few hundred and sometimes 16k in Figure 3.

Why the different numbers? Why these numbers?

Is there any practical setting where we can only afford to sample a few hundred times?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes approximately computing Shapley values using limited (k) size of the interaction set in Shapley interaction index (on top of sampling of coalition). The authors evaluate their results in some standard datasets.

### Strengths
- The approach is simple and intuitive
- The approach is needed for the importance task for XAI.

### Weaknesses
This paper has many weaknesses. The most critical weakness is that there is no approximation guarantee, even as the paper presents an approximation algorithm. In game theory literature, abstractions of game (as done in this paper) are not very useful unless they come with some approximation bounds. Plus, I did a google search and found work that also restrict interaction to smaller sets such as https://proceedings.mlr.press/v206/bordt23a/bordt23a.pdf and other work on Shapley-Taylor index - how does this work compare to these works?

The experiments show only MSE results - how about showing the actual XAI result with feature importance? In fact, the experiments section starts by mentioning all these XAI datasets and global/local feature importance - but no results showing the feature importance?

Lastly, the writing is lacking in many places, to the extent that it makes the paper difficult to read. For example, takes these lines from the paper : "Hence, its exact computation does not only become practically infeasible for growing player numbers but it is also of interest that the evaluation of only a few coalitions suffices to retrieve precise estimates. For instance, a model has to be costly re-trained and re-evaluated on a test dataset for each coalition if one is interested in the features’ impact on the generalization performance." - here coalitions are not evaluated but used in the evaluation of Shapley values. The second sentence has grammatical errors.
- In Eq 11, what is M in denominator of p_A (this is just M, not calligraphic M)
- Algorithm 1 is written where it appears as if p_A is computed for all subsets A - that itself is exponential. The sampling must be written appropriately.

### Questions
Please respond to weaknesses.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a method to approximate the Shapley value of a coalition game. The computation of the exact Shapley value is known to be a computationally hard problem for general coalition games.

The paper proposes a sampling-based algorithm that consists in evaluating the value of T subsets and then finding a k-additive game whose valuation on this T subsets is as close as possible. The approximate Shapley value can then be deduced from this set by using that when a game is k-additive, the Shapley values can be computed by a polynomial (O(n^k)) algorithm.

The evaluation of the proposed method is purely experimental and consists in showing that the method provides a "good" approximation of the Shapley value on some datasets.

### Strengths
The paper is relevant to the community.

The algorithm is easy to implement and seems to perform relatively well.

### Weaknesses
I am not a specialist of the literature on the approximation of Shapley value but I found the contributions of the paper relatively limited:

1/ I did not find a major technical novelty nor difficulty for deriving the main algorithm of the paper:
- A large part of the main ideas of the paper seem to be inspired from [Pelegrina et al 2023a] regarding the links between k-additive games and easy-to-compute Shapley values.
- Once the idea of restricting the attention to k-additive game has been given, the algorithm is relatively straighforward.

2/ The evaluation of the algorithm is limited to an empirical evaluation whose main message is not clear:
- it somehow show that the method produces results that are reasonable but they are very hard to interpret (is an MSE of 20000 good? Bad?)
- the method is compared with other heuristics (Figure 3) but it is not clear if it performs better or worse.

The empirical result could be used to provide guidance on how to tune parameters (e.g., T vs k) or why the method work in this setting and not others but this is not done.

To summarize, it seems to me that this algorithm has potential for interesting future work but that the contributions of the present paper are not good enough for ICLR.

### Questions
I do not have very specific questions but I am wondering if the authors would have an explanation for why the performance of the algorithm is not monotone in T (in Figure 2). This is especially visible for small k but seems also true for larger values of T. The authors acknowledge that this is unexpected but is there some explanation?

Also, there seems to be an argument that using T=n(n^2+5)/3 sampled coalitions is good. Could this be proven? Could this be studied empirically? Is this true for larger / smaller models (i.e. with very different n). 

Finally, the studied model are relatively small (for these models, the Shapley values can be computed in close form). Is there room for larger experiments? For instance for models for which the Shapley value could be computed in close form? Would this method be comparable with other existing methods?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new algorithm SVAk_{ADD}, which leverages the Shapley information property of k-additive games to approximate the computation of Shapley values and avoid the exponential number of computation in the original version. The authors provided experiment results to show the performance of the new algorithm.

### Strengths
1. The efficiency improvement of Shapley value estimation is important
2. The background and preliminary are sufficiently discussed and the paper is in general easy to follow

### Weaknesses
1. There is no theoretical result on the estimation error bounds of the proposed algorithm
2. The computational advantage mainly works for k-additive when k=2 or 3, but probably not for higher k numbers and thus it might only have an efficiency advantage over baseline methods on particular datasets with well separated and curated features
3. The fact that the error curve is not monotonic raises questions regarding the properties of the optimization problem in SVAk_{ADD}, whereas the baseline methods all have monotonic deceasing properties. 
(1). It is important to specify such condition difference if possible, e.g., convexity, potential function existence, since it might be very helpful to re-design the algorithm to satisfy such conditions and also achieve efficiency improvement
(2). Having this nike shape curve means that without knowing the ground truth, people have to use heuristics to decide the early stopping point, which is not needed in baseline methods
4. The difference between the current work and k-add SHAP is not sufficiently explained, going into the algorithm details is important since the topics are very closely related

### Questions
1. Under what conditions, can we conclude that increasing k can have better approximation?
2. How to evaluate a dataset to tell how close a k-additive game formulation can approximate it?

### Soundness
3

### Presentation
3

### Contribution
2
