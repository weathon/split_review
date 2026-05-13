# Boosting Perturbed Gradient Ascent for Last-Iterate Convergence in Games

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
This paper presents a payoff perturbation technique, introducing a strong convexity to players' payoff functions in games. This technique is specifically designed for first-order methods to achieve last-iterate convergence in games where the gradient of the payoff functions is monotone in the strategy profile space, potentially containing additive noise. Although perturbation is known to facilitate the convergence of learning algorithms, the magnitude of perturbation requires careful adjustment to ensure last-iterate convergence. Previous studies have proposed a scheme in which the magnitude is determined by the distance from a periodically re-initialized anchoring or reference strategy. Building upon this, we propose Gradient Ascent with Boosting Payoff Perturbation, which incorporates a novel perturbation into the underlying payoff function, maintaining the periodically re-initializing anchoring strategy scheme. This innovation empowers us to provide faster last-iterate convergence rates against the existing payoff perturbed algorithms, even in the presence of additive noise.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers multi-player monotone games and proposes a perturbed gradient ascent algorithm with improved performance in both deterministic and stochastic settings. Numerical simulations are provided.

### Strengths
The paper is well-organized and well-written. The proposed algorithm of Gradient Ascent with Boosting Payoff Perturbation is easy to implement and enjoys strong convergence guarantees. The numerical simulations are extensive and demonstrate the empirical performance of the proposed algorithm in various settings.

### Weaknesses
(1) Algorithmically, there is only one difference between the proposed algorithm and the Adaptively Perturbed Mirror Descent (APMD) from Abe et al. (2024): instead of directly using $\sigma_i^k$ as the anchoring strategy, a convex combination of $\sigma_i^k$ and $\sigma_i^1$ is used as the anchoring strategy. Surprisingly, with this seemingly minor modification, the resulting algorithms achieve improved performance guarantees. I did not quite follow why such a modification results in improved performance, despite the illustration from line 216 to line 225. What is the intuition behind this modification? Why does it help improve the performance guarantees? Are there intuitive and technical explanations behind it?

(2) In terms of the analysis, are there any major technical challenges in extending the approach from Abe et al. (2024) to that of this work? If so, how did the authors overcome it?

### Questions
(1) According to the definition, $\sigma_i^1=\pi^1$. Am I missing anything?

(2) Why are we not using the Nash Gap as a metric, which seems more natural?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper focuses on last-iterate convergence on smooth, monotone games for both the full feedback and noisy feedback settings. The authors propose a novel payoff perturbation term that dynamically interpolates the current anchoring strategy and the initial anchoring strategy. The interpolation achieves a trade-off between convergence speed and stability to gradient noise. The authors proved that the proposed algorithm achieves state-of-the-art last-iterate convergence rates for both the exact and noisy gradient feedback settings. Through experiments, it’s shown that the proposed algorithm achieves comparable or superior convergence speed in random payoff and hard concave-convex games, in noiseless and noisy gradient settings.

### Strengths
- The technical contribution is strong. The proposed GABP algorithm is well motivated and explained, and the authors have shown proof for the last iterate convergence rates.
- The paper is well-written. Proof sketches are shown for main theorems.

### Weaknesses
The paper does not discuss limitations.

### Questions
- In Figure 1, why is GAP shown for the random payoff game and the $r^{tan}$ shown for the hard concave-convex game? Can you show the other metric for these games as well?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a novel algorithm, Gradient Ascent with Boosting Payoff Perturbation, designed to improve last-iterate convergence rates in monotone games. The research builds upon the existing framework of payoff perturbation methods, which aid in stabilizing convergence in multi-player games where strategy profiles evolve iteratively. The authors address challenges posed by noisy feedback in gradient-based learning environments and achieve enhanced convergence rates with a boosting approach that periodically re-initializes a reference strategy, thereby maintaining strong convexity in the payoff function.

### Strengths
* The GABP algorithm leverages a perturbation term to enhance the stability and convergence rate.
* Theoretical analysis covers both full and noisy feedback settings.
* The study includes diverse game settings and benchmarks against state-of-the-art algorithms.

### Weaknesses
 * The proof strategy seems standard, and the technical contribution is not clarified in this paper.

### Questions
* It would be better to give more explanation on the intuition for the perturbation term (*) in Eq (3).
* Regarding the Hard Concave-Convex games in Appendix D.3, is there any reason that GABP uses a different step size (0.1) compared with other algorithms (0.5)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes GABP, which addresses the online learning tasks in games that are monotone with respect to gradient. The GABP algorithm uses a perturbation on policy update such that the policy anchors on a linear combination of the initial policy and the selected anchor policy, which is shown to accelerate convergence and stabilize performance. The last-iterate convergence to NE is provided.

### Strengths
Using the carefully constructed perturbation, the newly proposed GABP achieves a faster convergence rate compared to APMD. A good contribution to the literature.

The related literature is detailed and explains the

### Weaknesses
The notations in this paper is a bit confusing to the readers, a subsection dedicated for notations could be helpful. In addition, the subscripts and superscripts in section 4 can be simplified, such as the stationary point as well as $\hat{\sigma}$.

Although Section E.1 provided a discussion between the proposed GABP with AOG, with a different motivation, etc. However, the exact update still appears similar to the reviewer.

The experiments do not demonstrate a clear advantage of GABP compared to existing methods listed as benchmark. Perhaps more explanation could be helpful on why in some cases certain methods fail and why GABP is better overall.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
