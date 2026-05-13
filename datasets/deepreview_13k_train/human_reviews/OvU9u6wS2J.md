# An Online Learning Theory of Trading-Volume Maximization

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
We explore brokerage between traders in an online learning framework.
At any round $t$, two traders meet to exchange an asset, provided the exchange is mutually beneficial.
The broker proposes a trading price, and each trader tries to sell their asset or buy the asset from the other party, depending on whether the price is higher or lower than their private valuations.
A trade happens if one trader is willing to sell and the other is willing to buy at the proposed price.
Previous work provided guidance to a broker aiming at enhancing traders' total earnings by maximizing the _gain from trade_, defined as the sum of the traders' net utilities after each interaction.
This classical notion of reward can be highly unfair to traders with small profit margins, and far from the real-life utility of the broker.
For these reasons, we investigate how the broker should behave to maximize the trading volume, i.e., the _total number of trades_.
We model the traders' valuations as an i.i.d. process with an unknown distribution.
If the traders' valuations are revealed after each interaction (full-feedback), and the traders' valuations cumulative distribution function (cdf) is continuous, we provide an algorithm achieving logarithmic regret and show its optimality up to constants.
If only their willingness to sell or buy at the proposed price is revealed after each interaction ($2$-bit feedback), we provide an algorithm achieving poly-logarithmic regret when the traders' valuations cdf is Lipschitz and show its near-optimality.
We complement our results by analyzing the implications of dropping the regularity assumptions on the unknown traders' valuations cdf. 
If we drop the continuous cdf assumption, the regret rate degrades to $\Theta(\sqrt{T})$ in the full-feedback case, where $T$ is the time horizon. 
If we drop the Lipschitz cdf assumption, learning becomes impossible in the $2$-bit feedback case.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies a online learning problem for the brokerage who aims to maximize the total trading volume by posting a single price to two sequentially arriving traders. In particular, at each round $t$, there are two traders arriving with their private valuations $V_{2t-1}$ and $V_{2t}$. The broker then posts a price $P_t$ for this round, and if this price $P_t$ is between $V_{2t-1} \vee V_{2t}$ and $V_{2t-1} \wedge V_{2t}$, then the trade happens. 
Instead of optimizing the total gain from trade discussed in previous works, the goal of the brokerage of this work is to maximizing the total trading volume — i.e., the total expected trading probability. 

The paper assumes that the two valuations of both traders are all independently and identically realized from an unknown distribution. The paper considers two feedback structure. One is full feedback where the brokerage can observe both traders’ valuations $V_{2t-1}, V_{2t}$, another is the 2-bit feedback where the brokerage can only observe indicators $\mathbb{I}\{V_{2t-1}\le P_t\}$ and $\mathbb{I}\{V_{2t}\le P_t\}$.

The paper first shows that in the full-feedback case, if the distribution of the traders’ valuations has a continuous cdf, then an $O(\ln T)$-regret algorithm exists and this is tight. They also show that if we dropthe continuous cdf assumption, then the regret degrades to $\Omega(\sqrt{T})$, and they also provide an algorithm for this regret bound. 

In the 2-bit feedback case, if the cdf of the traders’ valuations is M -Lipschitz, they show that  $O(\ln(MT)\lnT)$-regret algorithm exists and also provide a near-matching lower bound $O(\ln(MT))$. The problem becomes becomes unlearnable if one drop the Lipschitzness assumption.

### Strengths
The paper studies an online brokerage problem with adopting a new metric compared to current online bilateral trade problems. The new metric measures the expected probability of a successful trade which is motivated by a fairness concern: ``trading-volume maximization gives the same dignity to all traders, granting everybody the same opportunity to trade, independently of their buying power’’. I think taking a step to study the fairness issue in bilateral trade has solid motivation. The paper also provides complete results for this problem (though making some simplifying assumptions).

### Weaknesses
Although I agree with that studying the fairness issue in bilateral trade is an interesting problem, I found the paper lack of justifications on why the “trading-volume maximization” is indeed achieving certain fairness, as this only grants the same trading probability for each party. How does metric compared to the metric that is related trader’s welfare? I think more discussions here may be helpful to better motivate the current metric. 

Meanwhile, I think the current results are bit restricted given that they assume both traders’ valuations are all realized from a same distribution. This assumption seems to be a bit unpractical in real-world. Would current results/algorithms generalize to this setting?

### Questions
Please see above comments.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies trade volume maximization in brokerages through an online learning perspective. It considers bilateral trades where in each round two traders participate. The brokerage sets a price $p_t$, and the traders independently sample a private valuation from a fixed distribution. The trade happens if the brokerage price is between the two traders' sampled valuations, that is one trader values it below the price and is willing to sell it at this price, and one trader values it more than the price and is willing to buy at the price.

Previous works consider regret minimization aiming to maximize total profits, but this paper introduces a new objective where the goal of the brokerage is to maximize the number of trades. 

The authors motivate the objective by showing an example where profit maximization can lead to low trade volumes.  

They consider full feedback setting and partial feedback setting. 

For the full feedback setting, they show that having continuous CDF is enough to get $O(\ln T)$ regret upper bound. In contrast, for the profit maximization setting, prior work has shown that Lipschitzness of the CDF is required to achieve even $\tilde{O}(T)$ upper bounds. They also show a matching lower bound. For the non-continuous case, they show a $O(\sqrt{T})$ lower bound and give an algorithm that achieves a matching upper bound. 

For the partial feedback, the brokerage only learns if the valuations were lower or higher than the price. Under $M$ Lipschitzness of the CDF, the authors give an algorithm with $O(\ln(MT) \ln T)$ upper bound and show an $ \Omega( \ln(MT))$ lower bound. They also show that Lipschitzness is required to obtain sublinear regret in the partial feedback case.

### Strengths
1. The profit maximization objective in online trades is well-studied in recent literature, the new objective introduced in this paper considers trade volume maximization and is reasonably motivated. 

2. The insight that the i.i.d. assumption in trade volume maximization simplifies the setting into a median estimation problem is novel resulting in tighter upper/lower bounds than the profit maximization objective.

3. The paper provides tight upper and lower bounds in the full feedback setting, and strong results in the partial feedback setting with thorough analysis. 

4. The paper does a good job of explaining the related work in this domain.

### Weaknesses
1. Even though the authors motivate the trading volume objective, I would also benefit from some discussion on the potential drawbacks of aiming for trading volume maximization. Even in the motivating example in Section 3, when the price is optimized for trading volume maximization, even though it leads to more trades, the total profits the traders achieve are almost halved (from approx $\frac{\epsilon(1-\epsilon)}{2}$ to approx $\frac{\epsilon(1-\epsilon)}{4} + O(\epsilon^2)$) which is linear regret for total profit. 

2. Most insights and algorithms are based on the fact that trade volume is maximized at the median in the i.i.d. setting where buyers and sellers have the same valuation distribution. Thus, the techniques may not translate to the generally studied i.i.d setting where the buyer and seller have different and possibly correlated distributions. The authors mention it as a possible future work, but maybe they can motivate the i.i.d setting more.

### Questions
1. Can you please talk about the potential drawbacks of trade volume maximization?

2. Can you please discuss how the 2 distribution i.i.d. cases studied in the literature relate to the i.i.d. case with one distribution regarding problem difficulty?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors study the online learning to maximize trading volume. Two traders come with private valuation in pairs, and the brokerage posts a price. If the price lies in between the valuation of the pair of traders a trade takes place. They study full information and 2-bit feedback structure. In full information, the valuation of two traders are revealed, while in 2-bit feedback whether the trader's valuation is higher than the posted price are revealed. They study the regret guarantees in three settings - the cdf of the reward is  (a) Lipschitz, (b) Continuous, and (c) General. In full information they provide tight regret bounds for all three settings. In 2-bit feedback Lipschitz functions admit tight logarithmic regret bounds, while linear regret lower bounds are established for the other two settings.

### Strengths
- The characterization of regret in the different setting seems quite complete. 
- The study of the online trading-volume maximization is an interesting addition to online learning in bilateral trade.

### Weaknesses
 - The results though complete seems a bit lacking in terms of technical challenges. Simple median based algorithms suffice. 
    - Complementing the general setting with $\alpha$-regret (for some reasonable $\alpha$) would improve the paper. 
    -  Coverage of the 1-bit feedback (whether trade went through or not) would improve the paper.
- Incentive compatibility of the proposed technique is not discussed.
- There are some work in bandit learning in online Auctions/double auctions. Is there any connection to that work?

### Questions
See weaknesses.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper focuses on the bilateral trade problem in an online learning setting. Specifically, the authors consider a setting where, at each time step, a buyer and a seller arrive, and the algorithm, acting as the broker, needs to decide on a price for the trade. The trade is successful if the buyer's value is higher than the price, and the seller's value is lower than the price. Unlike prior works on bilateral trade that focused on optimizing **gain from trade**, the authors study the problem under a new measure of performance: **total number of trades**. The buyer's and the seller's values are drawn from an unknown distribution i.i.d. at each time step. The authors study two models of the algorithm's observation: after each time step, it observes either both players' values or their willingness to sell or buy at each time step. Under both models, and under different assumptions on the distribution of the values, the authors provide algorithms with guarantees on their regret and lower bounds on the regret of any algorithm. In most cases, the regret guarantees and lower bounds match each other asymptotically.

### Strengths
1. The models considered in this paper are natural, and the theoretical assumptions are mostly reasonable.
2. The theoretical results are mostly tight and elegantly shown in Table 1.
3. The paper is quite well-written and easy to follow.

### Weaknesses
1. **Impact.** The paper presents a number of theoretical results, and it is commendable that they are almost tight. However, these results are mostly derived from standard techniques. This makes it unclear how this work will inspire future research from a technical perspective. Specifically, while the analysis of regret bounds under different feedback models is valuable, the core algorithmic approaches seem to rely on well-established online learning methods, such as online gradient descent or similar techniques. The novelty, therefore, appears to be primarily in the problem formulation and the specific performance metric (total number of trades) rather than in the development of new algorithmic tools or analysis techniques. It would be beneficial to see a more detailed explanation of how the specific problem setting necessitates any novel technical contributions beyond the application of existing techniques.
2. **Related work.** The discussion on related work about the original (non-online-learning) bilateral trade problem is a bit limited from my perspective. Currently, it is mostly stacked citations in one paragraph without sufficient explanation (even Myerson & Satterthwaite, 1983). It would be helpful to have a bit more discussion on the original bilateral trade problem and how it is related to the setting in this paper. For example, the paper could elaborate on the core differences between the classical mechanism design perspective, which focuses on incentive compatibility and truthfulness, and the online learning perspective, which focuses on regret minimization. Moreover, a few references are missing, such as:
   - The Gains from Trade Under Fixed Price Mechanisms (Applied Economics Research Bulletin 2008)
   - Improved Approximation to First-Best Gains-from-Trade (WINE 2022)
   - Non-excludable Bilateral Trade between Groups (AAAI 2024)

### Questions
1. Both the buyer and the seller share the same value distribution. Can you further discuss the motivation behind this assumption? What would happen if they have different value distributions?
2. Does any prior work on bilateral trade consider the total number of trades as the performance measure?
3. How do you think the results in this paper will impact the community? Is it more about the techniques or the problem setting?

### Soundness
4

### Presentation
4

### Contribution
3
