# Solving Multiplayer Partially Observable Stochastic Games by Divergence-Regularized Discounted Aggregation

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
This paper presents Divergence-Regularized Discounted Aggregation (DRDA), a multi-round learning system for solving partially observable stochastic games (POSGs), which unify normal-form games (NFGs), extensive-form games (EFGs) with perfect recall, and Markov games (MGs). In each single round, DRDA can be viewed as a discounted variant of Follow the Regularized Leader (FTRL) under a general value function for POSGs concerning imperfect information and an infinite horizon. While previous studies on this FTRL variant have demonstrated its last-iterate convergence towards quantal response equilibrium (QRE) in NFGs, this paper extends the theoretical results to POSGs by defining a generalized Nash distribution (GND), which extends the QRE concept of Nash distribution in NFGs through divergence regularization. The linear last-iterate convergence of single-round DRDA to its rest point is proved under a general assumption of hypomonotonicity. When the rest point is unique, it induces the unique GND, which has a bounded deviation with respect to Nash equilibrium (NE). Under multiple learning rounds, DRDA keeps replacing the base policy for divergence regularization with the policy at the rest point in the previous round. It is further proved that the limit point of multi-round DRDA must be an exact NE rather than a QRE under the unique rest point assumption. In experiments, the last iterates of multi-round DRDA converge to NE at a near-exponential rate in NFGs, outperforming existing baselines including moving-magnet magnetic mirror descent (MMD) in multiplayer EFGs. In an infinite-horizon MG, DRDA significantly outperforms the applicable algorithms based on best-response computations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a new variant of multi-round discounted FTRL (called DRDA) which works in general (n-player, general-sum, partially observable, simultaneous or sequential action) games. The paper shows that the new algorithm converges (last-iterate) to a generalized Nash distribution (a Nash equilibrium of a regularized version of the game). Under an assumption (unique rest point), multi-round DRDA is proved to converge to an NE.

### Strengths
General games are hard. Any work that attempts to learn and prove convergence in this setting is important to the community.

Last-iterate convergence is valuable, especially compared to average-iterate algorithms that are common in the field.

Experimental results look impressive.

### Weaknesses
No discussion on the assumptions.

Tabular.

Single experiment seed runs.

### Questions
Q1: Can you say anything about what equilibria is being selected by DRDA compared to other methods?

Q2: How realistic is the local hypomonotonicity assumption?  I don’t think this is addressed in the text.

Q3: How realistic is the single rest point assumption? Is the single rest point a feature of the game, learning dynamics, or both? Do the games in the  experiments section have this property? What happens if they do not have this property?

Q4: The experiments look like single seed runs. Did you run a parameter sweep?

Minor:

* Line 16: “General value function”. I was unsure what this meant at first read through. A Non-zero sum value function?
* Line 39: Go is more naturally formulated as an EFG. Is there a more natural example for MGs?
* Line 69: If I am reading this right, “Nash distribution” is distinct from “Nash equilibrium”?
* Line 109: Is the set of all joint observations ever used? It seems like a strange quantity.
* Line 169/184/203/…: Please use inline math styling.
* Line 169: I am curious if using sum over player convs (rather than max) is important? I realize both would be zero at equilibrium. 
* Line 183: Should a have a superscript: a^i? Because it is player i’s action, rather than a joint action?
* Line 225: Is this not more like a q-value? Why use v rather than q for the notation?
* Line 299: Does a GND always exist? It is not clear to me since any perturbation away from pi_base will result in: u^i(pi^i, pi^01_*) - u^i(pi_*) <= epsilon * (some negative value)

Score:

I am willing to raise the score after discussion with co-reviewers. Although I like the results, my main concern is how novel the contributions are compared to previous works. I would also like to be reassured that the method routinely converges -- I do not have a good intuition of how strong of an assumption single-resting point is. Furthermore, any answers to the questions I have asked will also likely improve my understanding and appreciation of the work.

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
This paper introduces a new algorithm for finding a Nash equilibrium in partially observable stochastic games (POSGs), which include setting with an infinite horizon. 
The algorithm, abbreviated DRDA, is inspired by previous work on finding epsilon-regularized Nash equilibria, which have limitations of a finite horizon and may not always have convergence guarantees in a multi-player setting.
They generalize the epsilon-regularized Nash equilibria to include the discounting factor of infinite-horizon POSGs, to form what they call a generalized Nash distribution (GND).
DRDA can be formulated as an ODE, which is solved repeatedly in multiple rounds to converge to an NE in the limit.

While the theory for convergence requires an assumption that is not clear if it can be satisfied in all games (rest point of DRDA is unique => GND has bounded deviation from NE) and the theory of multi-round DRDA converge is not well established, experiments show that the DRDA converges to a high precision in small games, at a near-exponential rate.
Moreover, they provide linear convergence bounds under some hypomonotonicity assumptions.

### Strengths
- Paper is well written, given the high complexity of the topic.
- They show linear convergence if epsilon > lambda, the hypomonotonicity constant. I find the hypomonotonicity intriguing. I think it's likely to  see future follow-ups on this work.

### Weaknesses
 - The theorems 1, 2 and 4 look similar to the results found in [Sokota] and [Perolat], extended to the POSGs. I did not investigate the exact differences, but these links deserve more highlights. Connection to MMD is written about in the Appendix, but as the update equations are written in two different notations I found it hard to follow in a limited time.
- Connected to previous the previous point, in experiments they compare with moving-magnet version of MMD, as L431 "MMD is close to DRDA", which they also abbreviate as MMD, while this version is substantially different from the non-moving-magnet base case. (Perhaps MMM would be a better abbreviation.) This makes me concerned that the real innovation of this paper is showing linear convergence under the hypomonotonicity assumption. 
- I would enjoy more thorough discussion of the experiment results, see also the questions.
- Appendix E: The Euler method used for single-round DRDA -- SDRDA -- has a learning rate whose schedule is not mentioned in the paper and its relation to the rest point convergence in Theorem 2 is not clear. Also, in experiments they used MDRDA, which uses the Euler-based SDRDA. At first, based on the main paper text, I was under the impression that the discretization of Eq (6) is used for DRDA in the experiments, but the actual algorithm used is different. What is considered as an iteration exactly? One step of the Euler algorithm? It would be helpful to correctly label the algorithm in experiments as MDRDA.

### Questions
- How does multi-round DRDA depend on the gap of single-round DRDA from its rest point? If I understand correctly, this is unknown?
- How do you explain the "spikes" in Figure 1/2 at the beginning of each new round?
- In Figure 2, 3-player Kuhn, the "levels" (ignoring the spikes) are not monotonic for DRDA. I find it surprising. How is it possible it converges overall? Is there a measurable quantity that is monotonic? (perhaps regret? or gap from regularized eq?)
- Finding NE outside of constant-sum games is PPAD-hard as I'm sure the authors are well aware of. Perhaps it is hard to remove the uniqueness assumption because of that?
- Can you please run the algorithm on typical POSG games like the tiger, and compare to methods like HSVI?
- Can you please compare the algorithm also with Smoothed Predictive Regret Matching+ (with restarts)? 
- How much tuning did the experiments require? The discussions is missing.

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
This paper introduces Divergence-Regularized Discounted Aggregation (DRDA), a multi-round learning method designed for partially observable stochastic games. DRDA builds on a discounted version of Follow the Regularized Leader, adapting it for POSGs to address imperfect information and infinite horizons. The authors expand on previous work showing last-iterate convergence to quantal response equilibrium by defining a generalized Nash distribution, which extends the QRE concept to POSGs via divergence regularization.

### Strengths
1. This paper builds on prior work by extending last-iterate convergence from NFGs and EFGs to POSGs, with theoretical proofs, broadening the method's applicability.
2. It introduces the concept of a generalized Nash distribution, enhancing the QRE framework through divergence regularization.
3. Convergence proofs are provided for both single-round and multi-round DRDA, strengthening the method's theoretical foundation.
4. Experimental results demonstrate that DRDA outperforms existing methods across various benchmarks.

### Weaknesses
See Questions.

### Questions
1. The paper uses a more general POSG setting compared to traditional EFGs. What are the core challenges unique to this choice, and how do they affect algorithm design?
2. Multi-round DRDA resembles a variant of Perturb-based methods from previous work [1]. What advantages does DRDA offer over these established approaches?
3. Can prior methods like R-Nad [2] or APMD [1] be directly applied to POSGs, or are there specific limitations in these algorithms that DRDA addresses?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The submission studies a regularized variant of FTRL for solving for equilibria. The submission derives continuous-time limit point results for convergence to Nash equilibria in general-sum settings and compares experimentally to a variety of baselines.

### Strengths
Converging to Nash in general-sum settings is a very difficult problem. Let me also say that I did not attempt to go through the submission's math. I evaluated the submission's soundness, presentation, and contribution as "fair" largely because I lack expertise to judge the novelty or correctness of the technical contribution. Similarly, I evaluated the submission as a 6 as I feel I lack the expertise to verify its value. Should other reviewers possess greater expertise I will defer to them, though I do feel confident saying that the writing is unclear in important places and the experimental results are weak. I'm also a bit concerned about the tension between the complexity results for computing equilibria in general-sum games and the claims made in the submission.

### Weaknesses
 > solving partially observable stochastic games (POSGs), which unify normal-form games (NFGs), extensive-form games (EFGs),
and Markov games (MGs).

This isn't correct. In contrast to EFGs, POSGs can neither express untimeable games nor imperfect-recall games.

> While a wide range of game-theoretic learning dynamics, including no-regret dynamics and best response dynamics, were primarily analyzed in static normal-form games (NFG), many real-world games are dynamic and thus require to be solved under a different game representation

Inconsistent tense. Also, the reason they require a different representation is because treating them as NFGs is too expensive, not because they involve state.

>  imperfect information game

Requires hyphen.

>  For example, the perfect information game of Go can be formulated as a Markov game (MG) by ignoring the action
of the waiting player. The imperfect information game of Texas Hold’em is commonly formulated as
an extensive-form game (EFG). In view of this requirement,

These sentences don't flow correctly.

> As an extension of MGs, partially observable stochastic games (POSGs) introduces imperfect information and is capable of unifying NFGs, EFGs, and MGs.

Again, not true re EFGs.

> forizon

> The existence of the rest point of single-round DRDA is thus proved.

It's not clear to me why this is a non-trivial result.

> Theorem 1. In a POSG, every GND ⃗π∗ under ϵ > 0 induces a rest point (⃗v(⃗π∗), ⃗π∗) in single-round
DRDA, and every GND ⃗π∗ under ϵ = 0 (i.e., Nash equilibrium) induces a DA rest point (⃗v(⃗π∗), ⃗π∗).

This also seems kind of trivial to me.

---

Other weaknesses:
- The results are continuous time, not discrete time.
- The games studied in the experiments seem quite limited.

### Questions
> On the other hand, 

On the other hand compared to what?

> For general-sum games, the last iterate of a “discounted” variant of FTRL, first examined in Leslie & Collins (2005), is proved to converge to the solution concept of Nash distribution (Coucheney et al., 2015; Gao & Pavel, 2021), a specific form of quantal
response equilibrium (QRE) (McKelvey & Palfrey, 1995)) defined in NFGs.

What's the catch here? Does this require exponential time for small quantal shocks?

>  Therefore, the hypomonotonicity assumption used in our convergence analysis should not be regarded as a strong
assumption.

Is this claim based on experimental results for Kuhn poker? That would strike me as far from comprehensive enough to make such a sweeping claim.

> These underestimates could reflect the order of magnitude of the true global hypomonotonicity value
λ, which must be an upper bound for the local hypomonotonicity required in Theorem 2.

Why does it matter to provide an underestimate of an upper bound?

How did you tune the parameters of the baselines for the experiments?

Did you use Q-values or counterfactual values for R-NaD and MMD for the experiments?

### Soundness
2

### Presentation
2

### Contribution
2
