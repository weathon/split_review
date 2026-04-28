# Online Fractional Knapsack With Predictions

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
The well-known classical version of the online knapsack problem decides which of the arriving items of different weights and values to accept into a capacity-limited knapsack. In this paper, we consider the online fractional knapsack problem where items can be fractionally accepted. We present the first online algorithms for this problem which incorporate prediction about the input in several forms, including predictions of the smallest value chosen in the optimal offline solution, and interval predictions which give upper and lower bounds on this smallest value.
We present algorithms for both of these prediction models, prove their competitive ratios, and give a matching worst-case lower bound.  Furthermore, we present a learning-augmented meta-algorithm that combines our prediction techniques with a robust baseline algorithm to simultaneously achieve consistency and robustness.
Finally, we conduct numerical experiments that show that our prediction algorithms significantly outperform a simple greedy prediction algorithm for the problem and the robust baseline algorithm, which does not use predictions.  Furthermore, we show that our learning-augmented algorithms can leverage imperfect predictions (e.g., from a machine learning model) to greatly improve average-case performance without sacrificing worst-case guarantees.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the online fractional knapsack problem in which items arrive online. Upon the arrival of a new item, we need to decide what fraction of the item to accept. In turn, we incur some weight and gain some value both proportional to the fraction of the item we accepted. Items come as a pair of values for their unit weight and value numbers. 

Although the knapsack problem is to some extent motivated by the applications mentioned in the paper, the assumption that a fraction of an item can be accepted makes the problem less interesting and not very applicable to these settings. When serving online traffic (queries or tasks), it is not acceptable to serve a subset of tasks. Load assignment is different from knapsack optimization. In online advertising, it is not reasonable to ask the sales team of an advertisement company to spend a fraction of their budget on your framework.

Also in online advertising, many times we are not facing a truly online problem. Negotiations may occur when we have access to all or a big subset (batch) of the requests/items.

Most of the results are focused on providing competitive ratio algorithms in settings that relatively strong prediction signals are provided. For example when the exact value of the cutoff threshold for the offline optimum algorithm is known. There is some novelty in the analysis when they want to figure out how to allocate their budget to items above this threshold and the ones at this threshold to get a better than 2 approximation. But the rest of the analysis is relatively straightforward given they need to plug in the previous algorithms in the literature and see what happens. 

The comparison benchmarks are optimum offline which is standard for online algorithms. However given the strong assumptions such as knowing exactly the cutoff threshold (Theorem 3.1), it may make sense to study the optimum online algorithm and use it for comparison.

The experiments are based on synthesized data.

### Strengths
The paper introduces some framework to add predictions to the online fractional knapsack problem.

### Weaknesses
Although the knapsack problem is to some extent motivated by the applications mentioned in the paper, the assumption that a fraction of an item can be accepted makes the problem less interesting and not very applicable to these settings. When serving online traffic (queries or tasks), it is not acceptable to serve a subset of tasks. Load assignment is different from knapsack optimization. In online advertising, it is not reasonable to ask the sales team of an advertisement company to spend a fraction of their budget on your framework.

Also in online advertising, many times we are not facing a truly online problem. Negotiations may occur when we have access to all or a big subset (batch) of the requests/items.

Most of the results are focused on providing competitive ratio algorithms in settings that relatively strong prediction signals are provided. For example when the exact value of the cutoff threshold for the offline optimum algorithm is known. There is some novelty in the analysis when they want to figure out how to allocate their budget to items above this threshold and the ones at this threshold to get a better than 2 approximation. But the rest of the analysis is relatively straightforward given they need to plug in the previous algorithms in the literature and see what happens.

The comparison benchmarks are optimum offline which is standard for online algorithms. However given the strong assumptions such as knowing exactly the cutoff threshold (Theorem 3.1), it may make sense to study the optimum online algorithm and use it for comparison.

The experiments are based on synthesized data.

### Questions
Read the weaknesses part for the main questions. The rest are here:

Other comments: 
Page 1: “It is well known that no deterministic …”, what about randomized algorithms? 

Section 2.2, “The threshold-based algorithm is shown in Algorithm 1.” I suggest adding a citation to Sun et al. in this sentence to make it clear that Alg 1 is their algorithm and not yours. 

Paragraph after Prediction Model II: “The quality of prediction in this c u - ell …”. There seems to be a typo here.

Algorithm 3 pseudocode: in line 10, add a comment that at this point \hat{w} is revealed since it is the weight of this new item. BTW, do you have any justification that the values of items are distinct? Line 12 seems to have some extra parenthesis, you probably get a compilation error with this.

### Soundness
2 fair

### Presentation
3 good

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
This paper discusses the learning-augmented version of online fractional knapsack problem under different prediction models. In the classical version of the problem, the online algorithm is given the unit value $v_i$ and maximum weight $w_i$ of the $i$-th item at each step. It’s goal is to select the appropriate quantity $x_i\leq w_i$ from each item, such that the total value is maximized without the total weight exceeding the capacity of the knapsack (assumed to be 1 wlog). The authors propose algorithms that utilize predictions on the least valuable item chosen by the optimal (and greedy) offline algorithm to achieve a constant competitive ratio, which ,according to lower bounds in prior work, is impossible without these predictions or other assumptions. 

Specifically, in the first prediction model, the algorithm is given the minimum unit value $\hat{v}$ among all items chosen by the offline algorithm, but does not have any knowledge of the quantity that the optimal offline algorithm takes from that item. Because of this, the online algorithm still does not know what decision to make when this particular item appears. The authors address this by having the online algorithm allocate only half of the maximum capacity for each item, while making the decision according to the advice leading to a 2-competitive algorithm. This is later improved to an $(1+\hat{w})$-competitive algorithm, where $\hat{w}$ is the available quantity of the item with unit value $\hat{v}$. The way this is done is by utilizing the fact that the quantity $\hat{w}$ becomes known after the item with unit value $\hat{v}$ arrives. 

Subsequently, a different prediction model is considered, in which the prediction is given as an interval $[\ell,u]$ where the item with the lowest unit value that is chosen by the optimal offline algorithm lies. Using this model, and assuming black box access to an $\alpha$-competitive algorithm that works on the promise that all unit values are within a given interval, the authors get a $2+ln(u/\ell)$-competitive algorithm. This is also generalized by adding an error probability for the prediction interval. Finally, the results are supported by experiments comparing the different algorithms and prior work.

### Strengths
Overall, I believe the paper is an interesting addition to the learning-augmented algorithms and does address a problem that had not been studied in this context before. The possibility of unreliable predictions is also addressed using interval predictions and introducing prediction error probability.

### Weaknesses
There is some sloppiness in the presentation, which can be improved (see below):

-In the end of section 2.1, it’s not clear to me why a linear program formulation for the offline fractional knapsack problem is given, since that problem can be solved by a greedy algorithm and the linear program does not seem to be used elsewhere in this paper. Perhaps it should be emphasized that it is provided only for the purpose of defining the problem. 
- Algorithm 2 seems to be suboptimal, since replacing line 7 with “$x_i=w_i$” can only increase the value of the solution. I do realize that this would not affect the worst case competitive ratio of 2 though.


Minor comments:
-In page 4, line 24: part of the sentence is missing
- In Algorithm 2, there is no initialization for the variable z (i.e setting $z=0$ before the while loop)
- In Algorithm 3, line 12: I haven’t checked thoroughly, but something looks wrong here. The reason is that to the left of the minus sign, the expression represents per unit of weight, while it should be representing just cost like the expression on the right of the minus sign.

### Questions
Can you comment on the performance on the algorithm when the single value prediction in the first model is not completely accurate?

Is there a smoothness type result where the competitive ratio that depends on additive prediction error (rather than multiplicative, which is in some sense addressed with the second prediction model)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the online fractional knapsack problem in the context of three novel prediction models.  For this problem, the optimal solution is characterized by two parameters $\hat v$ and $\hat \omega$, which are the smallest unit value in the optimal solution and the total weight of items with unit-value $\hat v$ in the optimal solution, respectively.  Given this information up front, the online algorithm can simulate OPT exactly - just accept all items with value $> \hat v$ fully and only the first $\hat \omega$ weight of items with value $\hat v$.  The three models considered in this paper assume no knowledge of $\hat \omega$ and progressively noisier information about $\hat v$.

The first model assumes perfect knowledge of $\hat v$.  In this case, the challenge is that we don't know $\hat \omega$ so we don't know how much to allocate to items with value $\hat v$.  A lower bound of $1+ \hat \omega$ is shown for this version of the problem for any (possible randomized) online algorithm.  In the worst case we have $\hat \omega \leq 1$, so this motivates the following strategy for a 2-competitive algorithm.  For each item with value $> \hat v$, allocate half of it.  For items with value $= \hat v$, allocate at most half of these items, up to a total weight of 1/2 the knapsack.  In the case that there is a unique item with value $\hat v$ and weight $\hat \omega$ an improved algorithm with competitive ratio $1+ \hat \omega$ can be given.

The second model assumes that the algorithm is given $\ell \leq u$ s.t. $\ell \leq \hat v \leq u$.  In this case, they treat the items with value in the range $[\ell , u]$ as a separate instance and give these algorithms to a worst-case robust algorithm (the best such algorithms due to prior work have competitive ratio $\alpha = 1+ \ln(u/\ell)$.  The allocation is then split between the two "sub-instances" ($\alpha/(\alpha + 1)$ given to items with value in $[\ell, u]$ and $1/(\alpha + 1)$ given to items with value $> u$.  The overall competitive ratio becomes $1 + \alpha = 2 + \ln(u/\ell)$.

The third model is similar to the second, but the guarantee only holds with probability at least $1-\delta$.  If the guarantee doesn't hold, then the predictions can be arbitrarily wrong (i.e., $\hat v$ could be $\ll \ell$ or $\gg u$).  Thus, the authors propose combining the prior result with the robust algorithm applied to the entire instance (which has values in the range $[L, U]$).  This gives a robust and consistent algorithm for this case.

Finally experiments on simulated instances with values and weights each drawn from a  (bounded above and below) heavy tailed distribution.

### Strengths
- The problem and prediction models are well motivated.
- The paper is clearly written and easy to follow.
- The experimental results are promising.

### Weaknesses
 - Many of the algorithmic ideas are standard in the learning-augmented algorithms literature, e.g., reserving some of the allocation for a robust algorithm as used in Algorithms 4 and 5. While the specific combination and analysis are novel, the core techniques of splitting the allocation between a prediction-based algorithm and a robust fallback are well-established. The paper could benefit from a more detailed discussion of the specific novelty in their approach compared to existing techniques.
- The comparison with prior work could be clarified further, see below. Specifically, the relationship to the results of Im et al. 2021 should be more thoroughly explored. This paper also extends their results to generalized one-way-trading, and it is not immediately clear why their model could not be extended to the fractional setting. A more detailed comparison of the prediction models and algorithmic techniques would be beneficial. Additionally, it might be nice to compare their algorithm experimentally.
- Some details for the experiments could be clarified. Real data and more realistic predictions could be considered in the experiments. Specifically, the method for generating the prediction intervals for models 2 and 3 should be described in more detail. It is unclear if the intervals are generated in a way that is favorable to the proposed algorithms. For example, if the critical value is always at the edge of the interval, this could lead to overly optimistic results. It would be useful to see results with the critical value at different locations within the interval and with different interval sizes. In Figure 2 (a) and (b), the figure seems to cutoff the maximum lines for some of the box plots, can you provide the empirical worst-case results for these experiments as a table or clarify this in the caption.

### Questions
## Major Comments and Questions
- Can you provide a more clear comparison with Im et al. 2021?  This paper also extends their results to generalized one-way-trading and it seems possible to extend their model to the fractional setting.  Additionally, it might be nice to compare their algorithm experimentally.
- The probabilistic predictions model is interesting.  Do any lower bound results hold for this model?  In particular is this the optimal tradeoff between robustness and consistency?  Finding optimal trade-offs between robustness and consistency has been of interest lately, see e.g. [1, 2] below.
- Can you clarify exactly how the predictions were created for the experiments for prediction models 2 and 3?  There are many ways to satisfy the promise each of these models guarantee but it seems to me that some ways could be more favorable for your algorithms than others.  For example do we observe different behavior for IPA if $\ell = \hat v < u$ or if $\ell < \hat v = u$?
 - In Figure 2 (a) and (b), the figure seems to cutoff the maximum lines for some of the box plots, can you provide the empirical worst-case results for these experiments as a table or clarify this in the caption?
 - It would be nice to see experiments on real data or with less synthetic predictions derived from the data.

## Minor Comments
 - In Algorithm 3, Line 3 the markup for $b$, $s$ looks different from the rest of the algorithm


### References

[1] - Alexander Wei and Fred Zhang. Optimal robustness-consistency trade-offs for learning-augmented online
algorithms. Advances in Neural Information Processing Systems, 33:8042–8053, 2020.

[2] - Jin, B. and Ma, W. Online bipartite matching with advice: Tight robustness-consistency tradeoffs for the two-stage model. In Oh, A. H., Agarwal, A., Belgrave, D., and Cho, K. (eds.), Advances in Neural Information Processing Systems, 2022.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This document discusses the online fractional knapsack problem, where items can be fractionally accepted into a capacity-limited knapsack. The authors present online algorithms for this problem that incorporate predictions about the input, including predictions of the smallest value chosen in the optimal offline solution and interval predictions that give upper and lower bounds on this smallest value. They prove the competitive ratios of these algorithms and provide a matching worst-case lower bound. Additionally, they introduce a learning-augmented meta-algorithm that combines prediction techniques with a robust baseline algorithm to achieve reasonable consistency and robustness. The authors conduct numerical experiments that demonstrate the superiority of their prediction algorithms compared to a simple greedy prediction algorithm and the baseline algorithm. They also show that imperfect predictions can greatly improve average-case performance without sacrificing worst-case guarantees.

### Strengths
1.	It is interesting to consider predictions in the online fractional knapsack problem. 
2.	Based on the prefect prediction of the smallest value in the optimal offline solution, the paper provides matched upper bound and lower bound of the competitive ratio. 
3.	The intuition of proof is clear, and it is convenient to understand for the reader.

### Weaknesses
1. Random order model is mostly studied in the online (fractional) knapsack problem, since the adversary model is too strong to obtain good results. In the adversary model, we must know some prior information about the input in advance, otherwise it is impossible to expect reasonable competitive ratio. In other hands, fractional knapsack problem is often studied as a relax of knapsack problem. Therefore, the model to consider online fractional knapsack problem under adversary model is in some sense artificial.  What was worse, the prediction model in the paper requires the algorithm to predict the smallest unit value in the optimal solution. This is not natural since the algorithm does not just know the information of the input (like the interval of all unit value of items), but also know some information of the optimal solution. The paper does not explain the motivation of the model setting.
2. The technology used in the paper is relatively simple, it is just a simple linear combination of two models, and there is not much technical innovation.
3. The paper contains complex mathematical equations and notations that may be difficult for readers to understand. The lack of clear explanations and simplifications could make it challenging for readers to grasp the concepts and follow the arguments presented. For example, the A algorithm in Algorithm 4 and Algorithm 5 does not refer to the same algorithm, which will confuse readers.

### Questions
1.	Is there any motivation to study the online fractional knapsack problem based on adversary model and the prediction model discussed in the paper? 
2.	The related work of the online knapsack problem with prediction is not very clear. Is it possible to compare the results of the online knapsack problem with prediction and the online fractional knapsack problem with prediction from different perspectives?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
