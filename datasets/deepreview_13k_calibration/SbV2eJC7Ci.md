# Faster Rates for Private Adversarial Bandits

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
We design new differentially private algorithms for the problems of adversarial bandits and bandits with expert advice. For adversarial bandits, we give a simple and efficient conversion of any non-private bandit algorithm to a private bandit algorithm. Instantiating our conversion with existing non-private bandit algorithms gives a regret upper bound of $O\left(\frac{\sqrt{KT}}{\sqrt{\epsilon}}\right)$, improving upon the existing upper bound $O\left(\frac{\sqrt{KT \log(KT)}}{\epsilon}\right)$ for all $\epsilon \leq 1$. In particular, our algorithms allow for sublinear expected regret even when $\epsilon \leq \frac{1}{\sqrt{T}}$, establishing the first known separation between central and local differential privacy for this problem. For bandits with expert advice, we give the first differentially private algorithms, with expected regret $O\left(\frac{\sqrt{NT}}{\sqrt{\epsilon}}\right), O\left(\frac{\sqrt{KT\log(N)}\log(KT)}{\epsilon}\right)$, and $\tilde{O}\left(\frac{N^{1/6}K^{1/2}T^{2/3}\log(NT)}{\epsilon^{1/3}} + \frac{N^{1/2}\log(NT)}{\epsilon}\right)$, where $K$ and $N$ are the number of actions and experts respectively. These rates allow us to get sublinear regret for different combinations  of small and large $K, N$ and $\epsilon.$

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the problem of adversarial MAB with differential privacy guarantee. Specifically, the authors propose a reduction framework which updates the classic MAB strategy every $N_0$ steps with the feedback as the aggregated losses plus a Laplacian noise. With this framework, they obtained $\tilde{O}(\sqrt{KT/\epsilon}+1/\epsilon)$ regret when combining this framework with EXP3, Heavy-tailed Tsallis INF, and FTPL. The authors also consider the bandits with expert advice (or contexual case) using this framework and obtain various bounds using different base algorithms.

### Strengths
- This paper first proposed an algorithm with $O(\sqrt{KT/\epsilon}+1/\epsilon)$ regret with DP guarantee, improving upon the previous SOTA algorithm with $O(\sqrt{KT}/\epsilon+1/\epsilon)$. This reduction is applicable for both MAB and its contextual variant.

- The proposed framework is simple and easy to be implemented.

### Weaknesses
 - This algorithmic framework, which updates the strategy only after a fixed 𝑁 rounds, is not the first to be used in achieving DP for MAB. [Tossou & Dimitrakakis 2017] also considers this batched update algorithm but with EXP3 as the subroutine, while the author claims that the results are buggy. From a technical perspective, the proofs seem to be adopted from existing bandit analysis without much challenge. Maybe the authors can highlight more on the technical challenge in achieving the DP guarantee with this reduction since the negative loss and heavy tail loss do not seem to be critical using these base algorithms. The core of the technical contribution appears to be in adapting existing regret bounds to handle negative and heavy-tailed losses, which, while necessary, is not a fundamentally novel approach. The authors should clarify the specific challenges in adapting these bounds, beyond the standard modifications.

- There are some places (actually many) that the author claims "not too hard" to obtain, which I think requires more explanations or at least some derivations.
  - Line 2077 and below: please provide more details on why the given sequences leads to very different $P_t(2)$. It is hard for me to understand why a single change in the loss at the first round will make $P_t(2)$ to be close to 1 in the first case but close to 0 in the second case. The explanation should include a more detailed analysis of how the weight updates propagate through the algorithm, causing the probabilities to diverge so significantly. A step-by-step breakdown of the weight changes and their impact on the probability distribution would be beneficial.
  - Line 2187: can the authors provide more explanations on this?

### Questions
See "Weakness" section. In addition, I wonder whether the lower bound mentioned in the last section (or Appendix G.2) applies to Algorithm 1 with EXP3 and other base algorithm choices?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The authors study the problem of adversarial multi-arm bandits under central differential privacy constraints. They propose a new algorithm  and establish regret bounds that improve over previous results. They then consider the problem of learning from expert advice under privacy constraints, again providing algorithms and regret bounds.

### Strengths
The problem studied is indeed interesting, and the regret rates that the authors claim to achieve would improve over previous rates if the authors could fix the proofs.

---

Edit : The authors propose a natural reduction scheme to adapt classical adversarial bandit algorithms to scenarios with batched losses augmented by Laplace noise. Their results improve upon previous regret bounds and shed light on an interesting distinction between the central and local demographic parity settings.

### Weaknesses
I believe that some proofs are false.

The most important mistake I found is perhaps the following : in Theorem 1, the authors assume that they have access to an algorithm with bounded regret 
$$\tilde{R} = \sup_{l_{1:T}} \left(\mathbb{E}\left(\sum_{t\leq T} l_t(I_t) + Z_t(I_t)\right) - min_i \sum_{t\leq T} l_t(i) + Z_t(i)\right)$$
where $Z_t(i)$ are i.i.d. Laplace variables, and the first expectation is taken with regards to all randomness (note that the right hand side of the expression is a random variables, and since the Laplace variables are unbounded, it seems to me unlikely that there exists an algorithm with a finite bound on this random quantity that holds a.s.)

However, when applying Theorem 1 to prove Corollary 1, the authors redefine $\tilde{R}$ as
$$\tilde{R} = \sup_{l_{1:T}} \left(\mathbb{E}\left(\sum_{t\leq T}l_t(I_t)\right) - min_i \sum_{t\leq T} l_t(i)\right).$$

Note that in general, we have 
$$\mathbb{E}\left(\mathbb{E}\left(\sum_{t\leq T} l_t(I_t) + Z_t(I_t)\right) - min_i \sum_{t\leq T} l_t(i) + Z_t(i)\right) = \mathbb{E}\left(\sum_{t\leq T} l_t(I_t)\right) - \mathbb{E}\left(min_i \sum_{t\leq T} l_t(i) + Z_t(i)\right) \geq \mathbb{E}\left(\sum_{t\leq T} l_t(I_t)\right) - min_i \mathbb{E}\left(\sum_{t\leq T} l_t(i) + Z_t(i)\right)  = \mathbb{E}\left(\sum_{t\leq T}l_t(I_t)\right) - min_i \sum_{t\leq T} l_t(i)$$
so bounding the second definition of $\tilde{R}$ is not enough to bound the first one, and thus to apply Theorem 1.

In general, the authors exchange "$\min$" and "$\mathbb{E}$" with too little caution. While some of the inequations hold, it would be helpfull to provide more details on this steps (rather than just saying "this holds because $Z_t(i)$ is centered"), and prevent making some mistakes. For example, in the proof of Theorem 3, $j^*$ is ambiguously defined : in Line 1209, it minimizes $\sum_{t} \tilde{l_t}(j)$.
 However, in Line 1220, to bound the regret compared to the best expert, $j^*$ on the right side of the equation should minimize $\sum_{t}\sum_i l_t(i)\mu_t^j(i).$

Some notations are not defined (for example, $\tilde{R}(\mathcal{B}, 1/\tau)$ in the proof of Theorem 1).

---

Edit : The authors have corrected their claims, which now hold. 

The paper somewhat lacks clarity in both its presentation and its proofs. The authors introduce a general reduction scheme, followed by a collection of results and algorithms, some of which differ only by minor factors. It is somewhat difficult to identify the assumptions and scenarios under which one algorithm should be preferred over another. I encourage the authors to more clearly highlight the main results for the two frameworks considered (with and without expert advice).

### Questions
If the authors could provide a rigorous proof that the algorithms presented in the corollaries verify the assumptions of Theorem 1 with the first definition of the regret bound $\tilde{R}$, or prove Theorem 1 under the assumptions on the regret bound $\tilde{R}$ verified by the algorithms studied in the corollaries, I would be happy to raise my score.

I also strongly encourage the authors to write all the steps when switching expectations and minimums.

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
This paper studies adversarial multi-armed bandits (adv. MAB) (with expert advice) under the central Differential Privacy (DP) constraint.

From the upper bound side, for adv. MAB, it proposes a generic conversion framework which achieves $O(\\sqrt{\\frac{KT}{\\epsilon}})$ regret and improves the best-known $O(\\frac{\\sqrt{KT}}{\\epsilon})$ (although the corresponding algorithm ensures the stronger local DP guarantee) when $\\epsilon$ is small ($\leq 1$), where $K$ is the number of arms, $T$ is the interaction horizon, and $\\epsilon$ is the privacy budget (smaller means stronger privacy protection). This is achieved through carefully utilizing tricks including local DP and batching.

For adv. MAB w/ expert advice, this paper gives the first set of regret upper bounds, each of which dominates for a different range of $K, N, \\epsilon$, where $N$ is the number of experts.

In the lower bound side, in the 2-arm case ($K=2$), it is shown that for a certain class of algorithms (characterized by some behavior over some loss sequence), they suffer $\Omega(\\sqrt{\\frac{T}{\\epsilon}})$, which matches the $O(\\sqrt{\\frac{T}{\\epsilon}})$ upper bound.

### Strengths
1.	Improved/first upper bounds in this setup are achieved through neat tricks.
2.	A matching $\\Omega(\\sqrt{\\frac{T}{\\epsilon}})$ lower bound is shown for a certain class of algorithms. This is an initial and important step towards characterizing the minimax regret in adv. MAB with central DP, which (if true) potentially implies a separation between stochastic and adv. MAB.

### Weaknesses
While I'm excited and happy to see that the authors are trying to approach the $\Omega(\sqrt{\frac{T}{\epsilon}})$ lower bound, in this paper, it is only shown for certain algorithms (which satisfy conditions (1) and (2) defined around Line 2108). It's hard to tell how broad algorithm classes these two conditions cover, and it's seems that we still have a large gap towards fully characterizing the $\Theta(\sqrt{\frac{T}{\epsilon}})$ regret. Specifically, the conditions (1) and (2) seem to impose a rather strong constraint on the algorithm's behavior, requiring it to quickly reduce the probability of playing the worse arm to a specific level and maintain it there. This feels like a very specific class of algorithms, and it is not clear if these conditions are necessary for achieving the lower bound or if they are an artifact of the proof technique. It would be beneficial to understand if these conditions are inherent to the problem or if they can be relaxed or removed to cover a broader class of algorithms.

### Questions
Could the authors please comment on any potential inspirations from Lemma 13? For example, is it possible to show the same lower bound using the same loss sequence ($\\ell^S_t$) while dropping those two conditions? (or they are tightly coupled?) Or we may need to construct completely different loss sequences?

### Soundness
3

### Presentation
3

### Contribution
2
