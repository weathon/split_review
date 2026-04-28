# Last-Iterate Convergence Properties of Regret-Matching Algorithms in Games

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Algorithms based on regret matching, specifically regret matching$^+$ (RM$^+$), and its variants are the most popular approaches for solving large-scale two-player zero-sum games in practice.
    Unlike algorithms such as optimistic gradient descent ascent, which have strong last-iterate and ergodic convergence properties for zero-sum games, virtually nothing is known about the last-iterate properties of regret-matching algorithms. 
    Given the importance of last-iterate convergence for numerical optimization reasons and relevance as modeling real-word learning in games, in this paper, we study the last-iterate convergence properties of various popular variants of RM$^+$. First, we show numerically that several practical variants such as simultaneous RM$^+$, alternating RM$^+$, and simultaneous predictive RM$^+$, all lack last-iterate convergence guarantees even on a simple $3\times 3$ game.
    We then prove that recent variants of these algorithms based on a \emph{smoothing} technique do enjoy last-iterate convergence: we prove that \emph{extragradient RM$^{+}$} and \emph{smooth Predictive RM$^+$}  enjoy asymptotic last-iterate convergence (without a rate) and $1/\sqrt{t}$ best-iterate convergence. Finally, we introduce restarted variants of these algorithms, and show that they enjoy linear-rate last-iterate convergence.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors study last-iterate convergence  for Regret Matching + (RM+) algorithm and its recent variants PRM+ (Predictive RM+), ExRM+ (Extragradient RM+) and Smooth Predictive RM+(SPRM+) in two-player zero-sum bimatrix games. They show asymptotic last-iterate convergence of these variants (linear last-iterate with restarts). They also show ($1/\sqrt{t})$ best-iterate convergence.

### Strengths
1) The paper is generally well written .

2) They show that RM+ and PRM+ have last-iterate convergence (asymptotically) only in the case of having a strict-NE and provide a numerical example that this assumption is necessary.

3) Moving on to the smooth variants of RM+ introduced in [Farina et al., 2023], they show that the operators corresponding to these algorithms are non-monotone and satisfy only a weak condition known as the Minty condition.

4) Furthermore, they provide structural analysis on the limit points of the dynamics and show last-iterate convergence and this can be extended with additional regularity assumptions (metric-subregularity) and with restarts to show linear last-iterate convergence as well.

References:
Farina, Gabriele, et al. "Regret matching+:(in) stability and fast convergence in games." Advances in Neural Information Processing Systems 36 (2024).

### Weaknesses
1) Their paper is restricted to two-player zero-sum games (bimatrix) games. It would be great to get a clarity as to if these techniques can be extended for general convex-concave games? (And also for general convex sets).

2) Is it possible to obtain asymptotic rates of convergence for the last-iterate analysis shown here?

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Learning algorithms for games is one of the fundamental research areas in algorithmic game theory. In this direction the authors of the paper study the (variants of) Regret Matching+ (RM+) algorithms in terms of last/best-iterate convergence.

Firstly, the authors give instances that (variants of) the RM+ algorithm diverges for last/best-iterate convergence even if the Nash equilibrium of the game is unique, so quasi-strict NE. On the other hand, interestingly enough, if there is a unique Nash equilibrium that is strict, so pure NE, they give a Theorem that PM+ converges in last-iterate, but without giving any rate guarantee.   

After this analyzing properties of the operator, they give last-iterate convergence and best-iterate convergence for the EXRM+ algorithm giving also convergence rate for the duality gap matching the state of the art O(1/sqrt{t}) for last-iterate algorithms. Similarly, they prove last/best-iterate convergence for the SPRM+ algorithm with same rate of convergence guarantee. Furthermore, they give, in my opinion a very interesting, variant of them that achieves linear last iterate convergence.

Finally the authors give experiments to give evidence for their results.

### Strengths
In my opinion I think that the problem of learning algorithms in games is one of the fundamental problems in algorithmic game theory. Thus, the contribution of this paper is significant since not only the authors give results for variants of the RM+ algorithm (a well-known algorithm), but also give nice and novel techniques and directions, such as the algorithms with the restart, that can potentially help the research to go further on the learning algorithms. All these along with the quality of the paper make it a nice piece of research work.

### Weaknesses
My only minor concern is that in Theorem 4 and 7 I think that η must be constant (not function of t) since β must be upper bounded by a constant strictly less than 1 in order to have linear (geometric/inverse exponential) convergence. Thus, I think, if I am correct, that this should be explicitly stated in the Theorems.

### Questions
Do you have any insight about the rate of convergence of the result of the Theorem 1? I think this will be a good direction for future work.

### Soundness
3

### Presentation
4

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
The paper studies the last iterate convergence of regret matching and its variant in two-player zero-sum games. The results show that RM+ and its predictive variants may not converge, but the extra gradient and optimistic gradient varients can converge.

### Strengths
The last iterate convergence of RM algorithms is important and the nonconvergence results are new and interesting. The paper is well-written and the results are sound.

### Weaknesses
The main weakness i that RM+ and its variants are mainly applied in EFGs, and so is the paper introduced and motivated. However, the results in the paper only hold for normal-form games. It is hard to be convinced that the results can be extended to EFGs without major revisions, so the motivation to study RM+ in NFGs is insufficient. 

The other major problem is that ExtraRM+ is not no-regret, this somewhat contradicts the purpose of regret-matching.

### Questions
1. Can you elaborate on the motivation behind considering RM+ algorithm in NFGs? Why are they important in NFGs, given that there are convergence algorithms like EG/OG. 
2. How can the results be extended to EFGs?
3. Is it possible to modify EXRM+ to be no regret? Is SPRM+ no regret? ( i believe OG is no regret, so does this extend to SPRM+?)

### Soundness
3

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
This paper investigates the last-iterate convergence rate of RM+ algorithms. Firstly, they provide numerical evidence that RM+ and PRM+,may fail to have asymptotic last-iterate convergence and best-iterate convergence. Secondly, they prove that ExRM+ and SPRM+ exhibit asymptotic last-iterate convergence. Lastly, they prove an $O(1/T)$ best-iterate convergence for ExRM+ and SPRM+, and use this best-iterate convergence to introduce new variants of ExRM+ and SPRM+, which achieve linear last-iterate convergence.

### Strengths
This paper was previously submitted to ICLR 2024. This paper investigates the convergence of RM+ algorithms, an important topic that has been missing in prior research. It offers valuable insights for future studies. To the best of my knowledge, this is the second paper to explore the convergence properties of RM+ algorithms.

### Weaknesses
1. Although this paper considers a different game from [Meng et al., 2023], its analysis of the convergence of RM+ largely depends on the analysis of the convergence of RM+ in [Meng et al., 2023]. More precisely, the proofs of RM+ convergence in this paper and in [Meng et al., 2023] are identical. The primary novelty of convergence results of RM+ of this paper relative to [Meng et al., 2023] lies in the properties of strict NE. Therefore, the authors should revise the introduction to remove the claim that [Meng et al., 2023] is "incomparable to our matrix game setting" and instead explicitly acknowledge that the convergence proof of RM+ of this paper largely depends on [Meng et al., 2023].

2. The second, and most critical, weakness of this paper is the lack of clarity in its explanation of the convergence of the iterates.
   - Convergence in the Duality Gap indicates that the iterates converge to the set of NE. For solving NE, this is sufficient, as the goal is merely to find one NE.
   - The metric used in the first author's previous works about the  last-iterate convergence of OMD-based algorithms, Tangent Residual means the upper bound of Duality Gap. In other words, the convergence in the tangent residual means the convergence in the duality gap. Why the convergence in the tangent residual is this sufficient to claim the last-iterate convergence in the earlier works but not in this paper?
   - In Section 7 Conclusions, the authors claim “linear-rate convergence in iterates.” However, the metric for linear-rate convergence is also the Duality Gap.

### Questions
1. What is the exact difference between "Convergence of the iterates" and "Convergence in the Duality Gap"? What are the advantages of "Convergence of the iterates" compared to "Convergence in the Duality Gap"?

2. Why does the first author in prior works use tangent residual to claim "last-iterate convergence," while this paper distinguishes between "Convergence of the iterates" and "Convergence in the Duality Gap"?

3. Is the claim in the conclusion about "linear-rate convergence in iterates" correct?

If the authors can address my concerns regarding the "Convergence of the iterates," I would be willing to increase my score.

### Soundness
3

### Presentation
3

### Contribution
3
