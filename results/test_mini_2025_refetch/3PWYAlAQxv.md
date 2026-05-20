Now I have all the information I need. Let me compile the final consolidated review.

---

## Summary

This paper proves universal approximation theorems for two-layer ReLU networks whose weights are permuted (never freely updated) rather than trained by gradient descent. The key technical innovation is a four-pair construction that builds step-function approximators using only the fixed weight values, combined with an annihilation method for unused parameters and a pseudo-copy technique that removes the need for a learnable output layer. The results span three theorems: UAP with a linear layer, UAP without it (at the cost of greater width), and a probabilistic extension to random pairwise-structured initializations. Experiments on 1D regression tasks validate aspects of the theory and explore which random initializations are compatible with permutation training.

## Strengths

- **Novel theoretical problem and clever construction.** Proving universal approximation under the constraint that weights are only permuted (never changed in value) is a genuinely new question. The four-pair construction (Sec. 3.1, Eq. (4), Fig. 1(c)) is a non-obvious technique that builds a step-function approximator from fixed signed weight values, directly enabling the UAP proof. No prior work attempted this theoretical characterization.

- **The pseudo-copy refinement (Sec. 3.3, Fig. 1(d)) cleanly extends the result.** The technique of partitioning the equidistant biases into refined subgroups and stacking near-identical approximator copies eliminates the need for the learnable output layer (Theorem 2), yielding a stronger result where only permutation suffices. The width scaling trade-off is explicitly characterized.

- **Honest and informative initialization study (Sec. 4.4, Fig. 3).** The paper systematically tests 8 initialization schemes and transparently shows which ones work (pairwise uniform) and which fail (He, Xavier). This provides a concrete practical insight — that standard initializations are incompatible with permutation training — which was not previously reported and identifies a clear direction for future work.

- **Convergence rate analysis with empirical validation (Sec. 3.4, Sec. 4.3, Fig. 2).** The derived O(n^{-1/2}) rate (in L²) for the construction is matched by the experimental L^∞ error curves, providing quantitative corroboration of the theory beyond pointwise convergence.

## Weaknesses

### Fatal

None.

### Major

- **The annihilation argument in the main text is incomplete regarding the intercept term.** The paper states that controlling the L^∞ norm of the summed linear function S_ℓ(x) = Σ a_i p_i (x − b_i) from unused weight pairs "can be achieved by bounding the slope Σ a_i p_i" (lines 128–130, Sec. 3.2). However, S_ℓ(x) = (Σ a_i p_i)x − Σ a_i p_i b_i has both a slope and an intercept. Lemma 2 provides sign selection for a *single* sequence (bounding Σ a_i c_i), but the problem requires controlling *two* different linear combinations (Σ a_i p_i and Σ a_i p_i b_i) with the *same* sign vector. The main text gives no argument for why the same signs can simultaneously make both sums small — this is a 2D sign-selection problem that Lemma 2 does not address and the paper does not discuss. The paper's line 98 mentions "controllable slope and intercept," implying the authors are aware of both, but the actual argument in the main body only treats the slope. Given that the appendices are stripped, the full proof (App. D) may resolve this, but as presented in the main text, the argument is insufficient. If this gap cannot be closed, the theoretical core of all three theorems is compromised. This is the most significant concern.

### Minor

- **Practical relevance is sharply bounded by the required initializations.** The proofs require highly structured initializations: biases must be equidistant (or drawn from U[0,1]), and weights must be in pairwise signed form (±b_i or ±p_i). The paper's own experiments (Fig. 3) show that standard schemes (He, Xavier) fail entirely. While the paper acknowledges this "incompatibility," the abstract and introduction do not qualify the scope — a reader could easily overestimate the generality. Theorem 3 partially relaxes this but still requires pairwise structure and uniform bias sampling.

- **Theorem 2 (UAP without the linear layer) is never tested experimentally.** All experiments include the freely trainable (α, γ) linear layer, so they validate only Theorem 1. The claim that UAP can be achieved purely by permutation (without a learnable output layer) remains experimentally unsupported. Since this is the stronger and more distinctive claim, the omission is notable.

- **Convergence rate error propagation is not fully theorized.** The O(n^{-1/2}) rate is derived for a single step-function approximator in L², then carried to the full construction and observed empirically in L^∞. The paper does not discuss how the L² → L^∞ gap is bridged in the theory, nor how errors propagate through stacked pseudo-copies to the final piecewise-constant approximation. The experimental validation partially covers this, but the theoretical derivation has a gap.

- **Observation of permutation-active patterns (Sec. 4.5) is preliminary and speculative.** The four-stage classification is purely post-hoc visual, with no quantitative assignment or ablation. The links to pruning, continual learning, and cycle decomposition are stated without evidence or analysis. This section does not detract from the core contribution but is not a supported strength either.

### Trivial

- Fig. 3 legend is nearly unreadable due to the density of 8 overlapping series labels; the reference to the figure caption is essential but the figure itself is hard to parse.

## Nice-to-Haves

- A test of Theorem 2 (no linear layer) at sufficient width would substantially strengthen the experimental validation.
- An explicit bound for the probability parameter δ in Theorem 3 would make the random initialization result more concrete.
- A brief explanation or hypothesis for *why* He/Xavier initializations fail under permutation training (e.g., scale mismatch, sign imbalance) would strengthen Sec. 4.4 beyond empirical reporting.
- A discussion of the computational overhead of the Adam-based inner loop vs. the savings from fixed weights would help situate the practical contribution.

## Removed Points

These points from the inputs are flagged to be removed; treat them with caution:

- **Criticism about the relaxed LaPerm algorithm being "insufficiently described" (referred to App. N).** The appendix is stripped by the parser; the original submission contains it. Removed per the rule about missing appendix content.
- **Criticism that Theorem 3's δ is not characterized or bounded.** The paper states "The detailed proof along with an estimation of the probability introduced by randomness are given in App. I." Removed as this is about stripped appendix content.
- **Criticism about "no analysis of why Xavier/He fail."** This is kept as a nice-to-have rather than a weakness — the paper's honest reporting of failures is a strength, and explaining the cause is beyond the paper's stated scope.
- **Strength Finder's generic strengths about "addressing an important problem" and "targeting an interesting question."** These lack specific concrete content tied to this paper's contributions.
- **Strength Finder's claim about the annihilation method being a "critical obstacle" solved.** While the idea is novel, the actual execution has the intercept gap discussed above, so the strength partially conflicts with the verified weakness.
- **Criticism about the linear layer making the "trained by weight permutation" claim misleading.** The paper explicitly includes Theorem 2 to address this and Theorem 1 is correctly stated. The claim is not misleading.
- **Criticism that the paper overstates generality in the abstract.** The abstract's claim ("prove that the permutation training method can guide a ReLU network to approximate one-dimensional continuous functions") is consistent with what Theorem 1 proves.

## Novel Insights

The harsh critic identified a genuine technical gap in the main text's annihilation argument that the Strength Finder overlooked. The two reviews together reveal an interesting tension: the paper contains a genuinely clever construction (four-pair step approximator) for a genuinely novel problem, but the central proof mechanism for handling unused weights is incompletely argued in the main text, relying on a 1D sign-selection lemma where a 2D argument would be needed. Neither review fully engages with the question of whether a straightforward extension of Lemma 2 (e.g., applying it greedily to one sequence and then using the remaining degrees of freedom on the other) could salvage the proof — this remains an open question for the authors. The most useful insight from combining the reviews is that the paper's contribution is somewhat bifurcated: the constructive part (four-pair, pseudo-copy) is clean and novel, while the cleanup part (annihilation) needs a more rigorous treatment.

## Suggestions

1. **Address the annihilation gap explicitly.** Provide a sign-selection argument that controls *both* Σ a_i p_i and Σ a_i p_i b_i simultaneously, or explain why the 1D bound on the slope alone suffices (e.g., if the structure of S_ℓ(x) = Σ a_i p_i (x − b_i) allows bounding the intercept as a consequence). If the appendix already does this, move the key reasoning to the main text.
2. **Test Theorem 2 experimentally.** A simple experiment without the (α, γ) linear layer, using the pseudo-copy construction at large n, would verify whether the width trade-off is practical.
3. **Clarify scope in the abstract.** Add a qualification that the results require pairwise-structured weight initializations (e.g., "for networks with appropriately structured initial weights") to prevent readers from over-generalizing.
4. **Discuss the L² to L^∞ gap in the convergence rate derivation.** A brief note on whether the rate is expected to hold for L^∞ and why would strengthen Sec. 3.4.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (avg < 3.5): G2Lnqs4eMJ (avg 2.50), ZNMZdEQQga (avg 3.00), IqaQZ1Jdky (avg 2.50), vvROJOMYP8 (avg 2.50) — all clearly below this paper's quality.
- Middle band (3.5–7.5): 34STseLBrQ (avg 7.25, accepted), iT1ttQXwOg (avg 6.00, rejected), tJDlRzQh7x (avg 4.33, rejected), Ozo7qJ5vZi (avg 7.20, accepted) — this paper sits in this band.
- Strong band (avg > 7.5): SjufxrSOYd (avg 8.00), EO8xpnW7aX (avg 8.00), 4xWQS2z77v (avg 8.00), P7KIGdgW8S (avg 8.00) — all far stronger than this paper.

**Explicit bracket:** between 4 and 6.5.

**Round 2 (Narrowing):**
- awHTL3Hpto (avg 6.33, accepted) — Expressivity of ReLU-Networks under Convex Relaxations: cleaner execution with no proof gaps, clearly stronger than the current paper.
- sq5gkjC9jv (avg 5.67, rejected) — Topological Expressive Power: mixed reviews, some practical-relevance concerns. Comparable to the current paper but the current paper has a more novel problem framing.
- Vz5HgVwcdu (avg 5.00, rejected) — Complexity of Injectivity: competently executed but limited scope. Comparable in overall quality.
- hIpUwg8kAU (avg 4.25, rejected) — Estimation error of gradient descent: weaker theoretical foundation and experimental support. Below the current paper.

**Final position relative to anchors:** This paper is stronger than the 4.25 anchor (hIpUwg8kAU) and roughly comparable to the 5.00–5.67 anchors, but notably weaker than the 6.33 anchor (awHTL3Hpto) due to the unresolved annihilation gap. The novel problem and clever construction push it above the 4–5 range, but the incomplete proof and limited scope prevent it from reaching the 6+ level.

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**