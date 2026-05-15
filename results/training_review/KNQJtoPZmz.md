Now I have a thorough understanding of the paper and can verify each claim properly. Let me compose the final consolidated review.

---

## Summary

This paper argues that **simplicity bias** — the tendency of randomly constructed models to be simple functions — is a universal, optimizer-independent phenomenon that can explain generalization in overparameterized models. It presents three theoretical analyses: (1) random Boolean trees that interpolate training data generalize without overfitting (Theorem 1); (2) wide neural networks in the NTK regime are equivalent to Gaussian process regression regardless of whether one uses gradient descent or a rejection-sampling "naive algorithm" (Proposition 2); and (3) deep narrow networks exhibit a different simplicity mechanism via dynamical-system convergence to a fixed point (Theorem 2), with trained interpolators behaving as nearest-neighbor classifiers (Theorem 3). The paper also identifies two distinct biasing mechanisms — central-limit theorem in wide networks vs. fixed-point convergence in deep networks — and argues that insights from the former may not transfer to the latter.

## Strengths

- **Rigorous bound for Boolean trees (Theorem 1).** The paper provides a closed-form bound showing that randomly constructed binary trees that interpolate the sample will generalize (agreement > 1/2+ε out-of-sample) with high probability when \(L_f \le b\,s/\log n\). This is a clean, self-contained result that directly demonstrates how a uniform construction process yields a non-uniform distribution over functions, and how this can lead to generalization without explicit regularization. Despite some technical murkiness in the asymptotic quantification, the core argument is sound and the example is well-chosen.

- **Identification of two distinct simplicity mechanisms.** The conceptual distinction between CLT-driven simplicity in wide networks and dynamical-system convergence in deep networks is a useful high-level perspective that is often overlooked. Theorem 2 establishes that, under i.i.d. zero-mean weights with variance \(< 1/(w\sigma_0'^2)\), the zero fixed point is asymptotically stable, covering both wide and fixed-width cases via Lyapunov exponent bounds. The clarification that shallow-and-wide network insights may not transfer to deep networks is a practically important cautionary note.

- **Optimizer independence demonstrated for the NTK regime (Proposition 2).** Proposition 2 shows that for wide networks in the NTK setting, the output distribution of the rejection-sampling "naive algorithm" (conditioned on fitting the data) is identical to that of gradient descent training. This cleanly establishes that the strength of simplicity bias in this regime does not depend on the specific optimizer, supporting one of the paper's central claims.

- **Bridging the "no Shannon effect" to machine learning.** The paper connects the well-known combinatorial fact (Genitrini et al., 2014) that randomly constructed Boolean functions are overwhelmingly simple — the "no Shannon effect" — to generalization in overparameterized models, providing a novel theoretical lens. This conceptual bridge is valuable even where the rigorous proof does not yet cover the full claimed scope.

## Weaknesses

### Fatal
None.

### Major

- **Theorem 3's Lemma 1 is unsubstantiated and the theorem's proof is not credible in its current form.** Lemma 1 asserts that after training (via rejection sampling that conditions weights on fitting the training set), the first-layer output for a new orthogonal input remains zero-mean normally distributed and independent of the training outputs and of the training-set first-layer outputs. This claim is stated without any proof or justification, and it is non-trivial: the conditioning event — weights must produce correct outputs on the training set — could plausibly break both the Gaussianity and the independence that would hold at initialization. The subsequent reasoning (Proposition 4, the extension to deeper layers) relies on this lemma. Because the entire conclusion of Theorem 3 depends on this unsubstantiated claim, the theorem is not established. The paper also acknowledges that even the Gaussian property fails at layer 2 (relying instead on "spherical symmetry" without proof), further underscoring the gap. **This is the most significant weakness in the paper.** *However, the paper's core contributions (Theorem 1, Proposition 2, Theorem 2, and the conceptual framework) do not depend on Theorem 3, so this undermines a supporting result rather than the entire paper.*

- **The abstract and discussion substantially overclaim relative to what the evidence supports.** The abstract claims that simplicity bias "can explain generalization in overparameterized learning models such as neural networks" and is "universal and nearly unavoidable." Theorem 1 applies to a specific class of Boolean trees with rejection-sampling "training." Proposition 2 covers wide networks in the linearized NTK regime. Theorem 2 addresses initialization (not training) and shows local stability, not generalization. Theorem 3 is not credible as submitted. The paper offers no rigorous bridge from these narrow cases to the sweeping claims about universality, optimizer independence, and explanation of generalization in standard deep networks trained with SGD. The discussion section reads as speculation on multiple fronts (the edge-of-chaos hypothesis, the claim that SGD solutions are "of similar nature" to rejection-sampling solutions, the Shannon effect). Claims made at this level of generality require commensurate evidence.

- **The connection between the "naive algorithm" (rejection sampling) and practical gradient-based training is established only for the NTK regime.** The paper's central argument — that simplicity bias is optimizer-independent and arises from random construction rather than from the optimizer — relies on the premise that the statistical properties of rejection-sampling interpolators match those found by SGD. Proposition 2 proves this for wide networks in the NTK regime, which is a special case where training is linearized. For deep networks and general overparameterized models, the paper provides no evidence. The paper explicitly flags this as a conjecture (e.g., "we conjecture that the solutions SGD finds are of similar nature") and acknowledges the naive algorithm is "non-constructive," but the framing throughout treats the equivalence as far more settled than the evidence warrants. This gap significantly limits the relevance of Theorems 1 and 3 to understanding practical neural network generalization.

### Minor

- **Theorem 1's asymptotic quantification is imprecise.** The condition "4s n→∞" appears garbled (likely a parser artifact), and the proof does not clearly specify whether the asymptotic is taken as \(s\to\infty\), \(n\to\infty\), or both jointly. The bound \(((1/2+\epsilon)(8n)^{b/\log n})^s \to 0\) requires \(s\) large and \(n\) sufficiently large for the limit \(n^{b/\log n}\to e^b\) to be approximately valid, but this joint dependence is not explicitly discussed. Clarifying the asymptotic regime would improve rigor.

- **Theorem 2 addresses initialization only, not training or generalization.** The paper correctly acknowledges this ("Theorem 2 does not address learning at all"), but the framing occasionally blurs the line between a property of random initialization and a property of learned solutions. The claim that the zero fixed point is a local attractor says nothing about what functions a trained network will learn, only about the random network before any data is seen.

- **The assumptions for Theorem 3 (S1: sample size < input dimension; S2: orthonormal samples; A1–A2: quasi-linear prologue, similar length mapping) are highly restrictive and stated to be "further discussed in the discussion section," where they receive only brief qualitative treatment.** The paper notes that these assumptions can be constructed (e.g., by inserting identity-mapping layers), but this is a construction argument that does not establish that typical learned solutions satisfy them. The practical relevance of Theorem 3 is thus unclear even setting aside the Lemma 1 issue.

- **Proposition 2 is a restatement of known NTK/GP results (Jacot et al., 2018; Williams & Rasmussen, 2006).** The paper's framing as a novel insight about simplicity bias is somewhat overstated; the novelty lies in the *interpretation* (optimizer independence), not in the mathematical statement. This does not detract from the paper's argument but should be acknowledged in any re-framing.

### Trivial
None.

## Nice-to-Haves

- Small-scale simulations validating Theorem 1 (finite n, s) would strengthen confidence that the asymptotic bound is meaningful at practical sample sizes.
- An empirical study on a toy deep network showing that SGD-found solutions and rejection-sampling solutions have similar statistical properties would make the optimizer-independence claim much more plausible.
- A side-by-side comparison of Theorem 3's predictions (nearest-neighbor behavior) with actual trained deep network behavior on a simple dataset would test whether the theory captures real phenomena.

## Removed Points

These points have been removed from the main review because they are factually incorrect, misunderstand the paper, or are parser-artifact nitpicks. They are listed here for completeness but should not influence the assessment.

1. *Critic claimed Theorem 2 "assumes local asymptotic stability implies global convergence to zero"* — **Removed (factually wrong).** The paper explicitly says "for any initial point **(close to 0)**" and labels 0 as a **(local)** attractor. The paper does not claim global convergence.

2. *Critic complained that "4s n→∞" is garbled* — **Removed (formatting artifact).** This is a parser corruption of the original text. The intended meaning (as \(s,n\to\infty\) jointly) is clear from context and the mathematics that follows.

3. *Critic claimed Theorem 1's derivation used "(1/2+ε)^8"* — **Removed (misread).** The paper uses \((1/2+\epsilon)^s\), consistent with standard union-bound reasoning.

4. *Critic described Proposition 2 as "presented as a novel insight about simplicity bias, but it is a well-known interpretation"* — **Partially removed as an overstatement.** This point is retained in weakened form under Minor weaknesses (restatement of known results) because the framing does oversell novelty, but the critic's stronger claim that this invalidates the paper's contribution is inaccurate — the paper's use of this result for the optimizer-independence argument is a valid interpretive contribution.

5. *Critic claimed "the paper acknowledges computational inefficiency but treats the statistical equivalence as given" for deep networks* — **Weakened and moved to Major.** The paper actually uses conjectural language ("we conjecture," "there is reason to think") for deep networks, not asserting equivalence as proven. The retained criticism correctly notes the gap between the NTK regime (proven) and deep networks (conjectural).

## Novel Insights

None beyond the paper's own contributions. The reviewers' insights largely converge with the paper's self-assessment (e.g., the gap between the naive algorithm and practical training is acknowledged by the authors) or are technical criticisms of unproven steps. The most useful observation that is not already in the paper is that Lemma 1's claim about distributional properties after conditioning requires careful justification that may not be straightforward — this connects to a broader methodological question about when rejection-sampling post-conditioning preserves Gaussianity.

## Suggestions

1. **Either provide a rigorous proof of Lemma 1 or remove Theorem 3 (or reposition it as a conjecture/hypothesis).** Lemma 1 is the linchpin of Theorem 3, and its current unsubstantiated status makes the theorem unsupported. If a proof exists in a stripped appendix, it must be brought into the main text. If no proof is available, the theorem should be presented as a conjecture with a clear statement of what would need to be proven.

2. **Tone down the abstract and introduction to match what is actually proved.** Replace claims of "universality" and claims that the paper "explains generalization" in neural networks with more precise statements about what the specific examples establish. The conceptual contribution (distinction between two mechanisms, connection to the no-Shannon effect, optimizer independence in the NTK regime) is genuinely interesting and does not need maximalist framing.

3. **Improve the asymptotic quantification in Theorem 1** by clearly specifying the asymptotic regime (joint \(s,n\to\infty\)? \(s\to\infty\) with \(n\) large?) and tightening the bound presentation.

4. **Add a limitations section** that explicitly discusses the gap between rejection-sampling and SGD-based training for deep networks, and the restrictiveness of Theorem 3's assumptions. The discussion already gestures in this direction but would benefit from a frank assessment.

## Score and Decision

The paper presents a conceptually interesting framework and one solid theoretical result (Theorem 1) that cleanly demonstrates simplicity bias in Boolean trees. The distinction between CLT-driven and dynamical-system-driven simplicity is a useful perspective. However, the paper's reach significantly exceeds its grasp: Theorem 3 is not credible as submitted, the abstract and discussion overclaim dramatically, and the connection between the rejection-sampling argument and practical neural network training is established only for the narrow NTK regime. These weaknesses are not fatal — the core conceptual contribution and Theorem 1 retain value — but they prevent acceptance at the advertised level of contribution. A version that dropped or rigorously proved Theorem 3, scaled back the claims, and acknowledged limitations could constitute a meaningful contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>