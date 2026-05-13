# Last-Iterate Convergence of Smooth Regret Matching$^+$ Variants in Learning Nash Equilibria

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Regret Matching$^+$ (RM$^+$) variants have been widely developed to superhuman Poker AIs, yet few studies investigate their last-iterate convergence. Their last-iterate convergence has been demonstrated only for games with strong monotonicity or two-player zero-sum matrix games. A primary obstacle in proving the last-iterate convergence for these algorithms is that their feedback is not the loss gradient of the vanilla games. This deviation results in the absence of crucial properties, \eg, monotonicity or the weak Minty variation inequality (MVI), which are pivotal for establishing the last-iterate convergence. To address the absence of these properties, we propose a remarkably succinct yet novel proof paradigm that consists of: (i) recovering these key properties through the equivalence between RM$^+$ and Online Mirror Descent (OMD), and (ii) measuring the the distance to Nash equilibrium (NE) via the tangent residual to show this distance is related to the distance between accumulated regrets. To show the practical applicability of our proof paradigm, we use it to prove the last-iterate convergence of two existing smooth RM$^+$ variants, Smooth Extra-gradient RM$^+$ (SExRM$^+$) and Smooth Predictive RM$^+$ (SPRM$^+$). We show that they achieve last-iterate convergence in learning an NE of games satisfying monotonicity, a weaker condition than the one used in existing proofs for both variants. Then, inspired by our proof paradigm, we propose Smooth Optimistic Gradient RM$^+$ (SOGRM$^+$). We show that SOGRM$^+$ achieves last-iterate convergence in learning an NE of games satisfying the weak MVI, the weakest condition in all known proofs for RM$^+$ variants. The experimental results show that SOGRM$^+$ significantly outperforms other algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper provides a proof to show the last-iterate convergence of SExRM+ and SPRM+ algorithms, which are smoothed variants of RM+ in general monotone games, and proposes a new algorithm SOGRM+ that further has last-iterate convergence in games with Weak MVI.

### Strengths
- The result in this paper generalizes those in previous works by Meng et al. (2023) and Cai et al. (2024). The new technique in their analysis might be interesting for future work.

### Weaknesses
- In terms of presentation, I think more space should be used to explain the high-level ideas and comparison with previous work, especially Cai et al. (2023). 
- I do not understand the strong claim in the technical novelty section saying that "Neither of these techniques can be used alone to prove the last-iterate convergence of RM+ variants."  For example, there remains the possibility to prove similar results without going through tangent residual argument. 
- The OMD update in this paper seems non-standard due to the f_i(x_i) term in Eq.(5).  Calling it OMD might be misleading.

### Questions
See the weakness section.

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
3

### Summary
The authors study last-iterate convergence  for smooth variants of Regret Matching+ introduced by [Farina et al.,2023], Smooth Extragradient RM+ (SExRM+) and Smooth Predictive RM+(SPRM+) in smooth games. They show asymptotic last-iterate convergence. They also show ($1/\sqrt{t})$ best-iterate convergence. 

References:
Farina, Gabriele, et al. "Regret matching+:(in) stability and fast convergence in games." Advances in Neural Information Processing Systems 36 (2024).

### Strengths
1) Their main techniques capitalize and build on the equivalence to Optimistic Mirror Dsecent and then using this they are able to recover monotonocity and then by measuring the distance to the NE via the tangent residual [Cai et al., 2022] and show that this is the distance between accumulated regrets.

2) The established equivalence to OMD is definitely useful.

3) Using this equivalence they propose a new algorithm Smooth Optimistic Gradient Regret Matching+ (SOGRM+), which has last-iterate convergence guarantees and seems to perform well in their conducted experiments, better than SExRM+ and SPRM+, which were proposed in [Farina et al., 2023].

### Weaknesses
1) Their paper is restricted to the class of smooth games. It would be great to get a clarity of how far these techniques can be stretched without the smoothness assumption?

2) Is it possible to obtain asymptotic rates of convergence for the last-iterate analysis shown here?

3) Could the authors also compare their algorithm SOGRM+ on games such as Kuhn Poker and Goofspiel etc, to get a better idea of the performance of their proposed algorithm, aside from the random zero-sum games?

Minor comment:
To make the paper self-contained, please describe the algorithms being analyzed as they are quite recent developments.

### Questions
See weaknesses.

### Soundness
3

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
4

### Summary
This paper studies the last-iterate convergence properties of smooth variants of the Regret Matching+ (RM+) algorithm. RM+ type algorithms differ from Extragradient (EG)/Optimistic Gradient (OG) algorithms since the feedback is not the loss function and can be non-monotone. The paper's main contribution is a new proof paradigm that addresses this challenge: (1) they show an equivalence between RM+ and Online Mirror Descent (OMD) with Euclidean regularizer; (2) using the equivalence, they relate the tangent residual to the distance between consecutive accumulated regrets, which can be easily bounded. By this proof paradigm and existing results for OG, they propose SOGRM+ and show asymptotic last-iterate convergence in the duality gap for games with weak MVI. They also show SPRM+ and SEXRM+ have asymptotic last-iterate convergence in the duality gap for monotone games. They also conduct numerical experiments on small random games to demonstrate the effectiveness of their algorithms.

### Strengths
1. This paper studies the last-iterate convergence properties of RM-type algorithms in games. This question has been studied only recently, and these first results only focus on zero-sum games. This paper extends previous results and presents asymptotic last-iterate convergence in the duality gap in monotone games and games that satisfy weak MVI.
2. This paper's proof paradigm incorporates several ideas in learning and games and is novel. It uses the existing idea of equivalence between RM+ and OMD to show that the operator's non-monotonicity can be addressed by rewriting the update rule in the OMD style. Then, by elegantly using the tangent residual, they show that the tangent residual can be bounded by the distance between consecutive accumulative regret vectors. This distance can be further bounded by extending existing results for OMD-type algorithms. This analysis is simple but powerful.

### Weaknesses
1. The paper's presentation could be improved. For the experimental results, for example, whether the algorithm is alternating or simultaneous should be provided. The OMD algorithm given in the paper seems non-standard: a standard OMD update (prox-mapping) does not contain a $ qt$ term, and the Bregman divergence is fixed with one generating function $q$. This should be explained in detail to reduce confusion. 
2. The meaning of asymptotic last-iterate convergence is confusing in this paper. Since the proof paradigm uses the tangent residual as a proxy, it gives asymptotic last-iterate convergence in the duality gap (i.e., $\lim_{t\rightarrow \infty} Gap(x^t) = 0$). But it does not give the stronger notion of point convergence of the iterates to a Nash equilibrium (i.e., $\lim_{t\rightarrow \infty} = x^*$ is a Nash equilibrium), which is proved in [1] for SExRM+ and SPRM+ in zero-sum games. This difference should be clarified in the text and acknowledged in Table 1.

[1] Yang Cai, Gabriele Farina, Julien Grand-Clément, Christian Kroer, Chung-Wei Lee, Haipeng Luo, and Weiqiang Zheng. Last-iterate convergence properties of regret-matching algorithms in games, 2023.

### Questions
1. It has been shown that restarting SExRM+ and SPRM+ has a game-dependent linear last-iterate convergence in zero-sum games. Do you think similar results hold for the proposed algorithm SOGRM+ and (non-restarting version) of SPRM+ and SExRM+?
2. Is it possible to prove point convergence of the iterates to a Nash equilibrium of these algorithms in monotone games?

### Soundness
3

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
2

### Summary
This paper studies last-iterate convergence of Regret Matching (RM+) variants to Nash equilibria. It introduces a proof method leveraging the equivalence between RM+ and Online Mirror Descent to restore essential properties like monotonicity. Then, the authors show that smooth RM+ variants, including a new algorithm, achieve convergence under MVI condition. Experiments show that the proposed new algorithm perform better than other algorithms.

### Strengths
The structure of this paper is clear and easy to follow. The literature review is done thoroughly. The paper seems to introduce an innovative proof paradigm that effectively addresses gaps in achieving last-iterate convergence for RM+ variants. It establishes last-iterate convergence to games under a weak condition, making it applicable to a wider class of games.

### Weaknesses
Although the paper shows SOGRM+’s effectiveness, the experiments focus on two-player zero-sum matrix games. Additional tests across different game structures would strengthen its applicability claims.

### Questions
Why the proposed algorithm allows large \eta compared to other methods? Can you provide some intuitions behind this?

### Soundness
3

### Presentation
2

### Contribution
3
