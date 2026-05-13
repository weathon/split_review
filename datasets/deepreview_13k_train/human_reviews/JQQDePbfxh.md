# Private Mechanism Design via Quantile Estimation

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
We investigate the problem of designing differentially private (DP), revenue-maximizing single item auction. Specifically, we consider broadly applicable settings in mechanism design where agents' valuation distributions are **independent**, **non-identical**, and can be either **bounded** or **unbounded**. Our goal is to design such auctions with **pure**, i.e., $(\epsilon,0)$ privacy in polynomial time. 

In this paper, we propose two computationally efficient auction learning framework that achieves **pure** privacy under bounded and unbounded distribution settings. These frameworks reduces the problem of privately releasing a revenue-maximizing auction to the private estimation of pre-specified quantiles. Our solutions increase the running time by polylog factors compared to the non-private version. As an application, we show how to extend our results to the multi-round online auction setting with non-myopic bidders. To our best knowledge, this paper is the first to efficiently deliver a Myerson auction with **pure** privacy and near-optimal revenue, and the first to provide such auctions for **unbounded** distributions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper investigates the problem of designing differentially private (DP) mechanisms for single-item auctions that maximize revenue while ensuring ($\epsilon$, 0)-pure privacy. The authors propose two auction learning frameworks for both bounded and unbounded valuation distributions that privately estimate specific quantiles to achieve near-optimal revenue. Notably, the proposed frameworks maintain computational efficiency with only polylogarithmic overhead relative to non-private versions. Extending the approach to multi-round online auctions, the paper introduces mechanisms to limit strategic behavior from non-myopic bidders, demonstrating effectiveness in both bounded and unbounded distribution settings. The authors claim the method is the first efficient DP Myerson auction model under pure privacy and applicable to unbounded distributions.

### Strengths
The paper addresses a critical gap in differential privacy for revenue-maximizing auctions, especially in providing efficient algorithms that ensure pure DP, a stringent privacy model often overlooked in mechanism design. The focus on both bounded and unbounded distributions adds further novelty, and the integration with online auctions for non-myopic bidders is an innovative extension.

### Weaknesses
1. Experimental Validation: While the theoretical framework and proofs are robust, the paper lacks empirical validation. Demonstrating practical performance via simulation or real-world data could strengthen the results, showing real-world applicability of the bounded and unbounded auction mechanisms. Specifically, the paper does not provide any information on how the proposed mechanisms perform with different distributions, sample sizes, or privacy parameter settings. This makes it difficult to assess the practical relevance of the theoretical findings.

2. Complexity for Practitioners: Although theoretically sound, the use of pure DP and quantile estimation could be challenging for practitioners to implement in real auction settings. The paper might benefit from guidance on parameter selection or case studies showing how to configure the model in practical scenarios, particularly for choosing ε and handling non-i.i.d. bidder distributions. The quantile estimation process, while theoretically efficient, may require careful tuning of parameters that are not immediately obvious to practitioners, potentially leading to suboptimal performance if not configured correctly.

3. Assumptions in Non-Myopic Bidder Models: The assumption of a commitment mechanism to prevent strategic bidding in online auctions may be limiting, as real-world non-myopic behavior could vary significantly. A sensitivity analysis on bidder behavior assumptions could improve robustness and applicability to broader settings. The current model assumes that bidders are either fully committed or behave myopically, which may not reflect the nuanced strategic considerations of real-world bidders who might adapt their bidding strategies over time based on observed outcomes.

### Questions
1. Experimental Validation: While the theoretical framework and proofs are robust, the paper lacks empirical validation. Demonstrating practical performance via simulation or real-world data could strengthen the results, showing real-world applicability of the bounded and unbounded auction mechanisms.

2. Complexity for Practitioners: Although theoretically sound, the use of pure DP and quantile estimation could be challenging for practitioners to implement in real auction settings. The paper might benefit from guidance on parameter selection or case studies showing how to configure the model in practical scenarios, particularly for choosing ε and handling non-i.i.d. bidder distributions.

3. Can the authors clarify how sensitive the revenue guarantee is to variations in the privacy parameter $\epsilon$? For instance, what level of revenue tradeoff might practitioners expect for specific values of $\epsilon$?

4. In the online auction application, how does the mechanism handle scenarios with highly irregular bidder participation, such as sporadic or bursty bidding behavior?

5. Could the approach be adapted or extended to multi-item auctions? If so, are there foreseeable challenges specific to quantile estimation or revenue guarantees?

6. What is the impact on revenue performance if the quantile estimation accuracy deviates from the bounds established in the paper? Would empirical validation potentially show scenarios where revenue significantly underperforms due to quantile estimation errors?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies how to learn the optimal single-item auction (Myerson auctions) from samples of non-iid bidders' values in a pure differentially private (pure DP) way. The authors reduce this problem to private quantile estimation of the bidders' value distributions. By doing that, they improve previous works in DP mechanism design in several aspects.  The authors also apply their results to online auction design with non-myopic bidders, obtaining a learning algorithm that is approximately truthful for the bidders and approximately revenue-optimal for the seller.

### Strengths
(S1) Previous attempts to integrate DP with prior-dependent auction design were all computationally inefficient or only guaranteed approximate DP.  This work is the first to achieve both computational efficiency and pure DP, which is a significant conceptual and technical contribution.

(S2) The authors show that their approach can be applied to online auction with non-myopic bidders, ensuring that bidders are approximately truthful and the seller can obtain approximately optimal revenue.  This generalizes the iid setting of Huang et al (2018a) to the non-iid setting, answering their open question. This is a novel contribution to the online auction design literature.

(S3) The private quantile estimation technique used in this work does not directly follow from previous work like Kaplan et al 2022.  The authors generalize previous techniques for distinct data points to the case with potentially identical data points.  This is an interesting contribution to the DP literature. 

(S4) The writing is very good. For example, the results and contributions are clearly stated in the introduction. The proof sketches nicely summarize the main proof ideas.

### Weaknesses
(W1) The high level idea is not new. Huang et al (2018) and Abernethy (2019) have applied DP techniques to the problem of learning optimal auctions from non-myopic bidders. This paper is more of a refinement and generalization of previous works. While the shift to pure DP is a valuable contribution, the core approach of using DP for mechanism design in this context is not entirely novel. The paper could benefit from a more detailed discussion of the specific technical challenges overcome in achieving pure DP compared to prior approximate DP methods, highlighting exactly where the existing techniques fall short and how the proposed approach provides a more robust solution. Specifically, a deeper dive into the limitations of tree aggregation methods used in prior work when applied to unbounded distributions would be beneficial.

(W2) No experiments are given. Some experimental results might strengthen the work a lot, given the practical motivation of using DP mechanism in real-world auctions. The lack of empirical validation is a significant drawback. The paper would be much stronger with experiments demonstrating the practical performance of the proposed mechanism. It is crucial to show not only theoretical guarantees but also that the proposed approach performs well in practice, especially given the practical motivation of using DP in real-world auctions. The paper should include experiments comparing the revenue of the DP Myerson auction with the standard Myerson auction under various settings, including different distributions and sample sizes. The experiments should also evaluate the computational efficiency of the proposed approach.

### Questions
**Question:**

(Q1) Should the $V_{[i, :]}$ be $\hat V_{[i, :]}$ in Algorithm 1?  And what does $[i, :]$ mean? 



**Suggestions:**

- Definition 2.1: The allocation rule and payment rule notations $\bf x$ and $\bf p$ should be vector-valued functions, not vectors.

- Typo in Definition 2.3: $exp$ $\epsilon$. 

- Line 225: "increasing the sample size n from continuous value distributions naturally leads to points that are either very close or identical". Points sampled from a continuous distribution are identical with probability 0.

- The proof sketch of Theorem 3.2 and the formal proof (the proof of Theorem F.4 in the Appendix) didn't say why the QESTIMATE oracle is DP.  I guess it is given Lemma F.3.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the problem of differentially private Myerson auction design under a Differential privacy constraint. The model is that there are k “types” of users and in each round, we get k buyers sampled from the distribution (assumed to be i.i.d.). Myerson’s foundational result defines the revenue maximizing truthful auction when the seller knows the distributions that the valuations are drawn from. In this work, the authors ask if we can privately learn enough about these distributions from samples to be able to run a near-optimal auction.

The main contribution is to show that indeed this is feasible. Using samples, one can learn the approximate quantiles of the distributions. Given the quantiles, the authors show that one can get a good approximation to the Myerson prices. In the case that the range of valuations is bounded, one can use any of the many known quantile estimation algorithms. In the case of unbounded range, one can use a recent result to estimate the range and then run quantile estimation.

The authors also show how for non-myopic bidders in a repeated game setting, one can use this private learning algorithm along with a commitment algorithm to get near optimal revenue.

### Strengths
- This paper expands the set of settings where DP can be used for mechanism design
- It combines DP tools with an understanding of auctions to allow learning from buyer’s bids while preserving incentive compatibility even with non-myopic bidders.

### Weaknesses
 - No major weaknesses, perhaps with the exception of relavance to this conference. See questions below

### Questions
- It would be useful if the authors compared to the utility the exponential mechanism would offer in this case, ignoring computational constraints.
- It is also likely that the sampling from the continuous exp mech distribution can be done by being a little careful in understanding the distribution, especially since the structure of Myerson should allow you to independently sample each user’s price.
- The online mechanism designed in this work uses “greedy” by separating the explore and exploit phases. Can you do better by combining exploration and exploitation?

Nits:
- “Mechanism Design in the title seems too general for what the paper is doing. I would suggest putting Myerson Auction Design or at best Auction Design in the title.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper combines differential privacy with auction theory, specifically focusing on revenue-maximizing auctions under pure DP.  The authors propose frameworks that handle independent, non-identical, and both bounded and unbounded valuation distributions.

### Strengths
The paper provides auctions for unbounded distributions and establishes theoretical guarantees.

### Weaknesses
1. There is no experiment.
2. I have some concerns about motivation and novelty, see Questions part for details.
3. The notation is confusing like different $\epsilon$ and in Theorem 5.4 , "the regret is upper bounded by $\tilde{\Theta}$" where $\tilde{\Theta}$ should be $\tilde{O}$.

### Questions
1. In the multiple-dimension case, it is well-known that DP community considers approximate DP since it can help improve $\sqrt{d}$ factor in utility where $d$ is the dimension like in [1]. In this paper, the authors consider $k$-dimension but achieve pure DP. The motivation is weird. What is the advantage of pure DP compared with approximate DP in your setting? 
2. One should consider composition theorem for multiple rounds like in algorithm 3 to achieve central DP. Also, in lines 277-278, the final privacy guarantee should be $\epsilon$-DP and then divide it to each dimension.
3. I have some concerns about the novelty of the technical part since the paper just invokes and combines previous methods in other work.


[1].Daniel Kifer, Adam Smith, and Abhradeep Thakurta. Private convex empirical risk minimization and
high-dimensional regression. In Conference on Learning Theory, pages 25.1–25.40, 2012.

### Soundness
3

### Presentation
3

### Contribution
3
