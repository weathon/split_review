- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 8, 5
Now I have a thorough understanding of the paper and all the claims. Let me produce the consolidated review.

---

## Summary

This paper defines "Expected Adversarial Robustness" for graph neural networks, derives upper bounds on this quantity for GCNs and GINs under node-feature attacks (Theorems 1–3), and proposes GCORN — a GCN variant that uses iterative orthonormalization of weight matrices (Björck iteration) to improve robustness. The paper also introduces a probabilistic, attack-independent evaluation method for estimating expected robustness via stratified sampling. Empirical results on five datasets show GCORN outperforming several baselines (GCN-k, RobustGCN, AIRGNN, ParsevalR) on node classification under feature attacks.

---

## Strengths

1. **Novel theoretical framework for expected robustness on graphs.** The paper defines *expected* (average-case) robustness for graph functions, as opposed to the standard worst-case certificates. This is a genuine conceptual contribution — it provides a lens for understanding a model's typical behavior under attack rather than just its worst-case guarantees. The definition in Eq. (1) and Definition 1 is clearly laid out and appropriately connects to the broader robustness literature.

2. **Explicit upper bounds on expected robustness for GCNs and GINs under feature attacks.** Theorem 1 gives γ = ∏||W⁽ⁱ⁾||₁ · ε · (∑ ŵᵤ) / σ (and a similar L∞ version), directly linking robustness to weight-matrix norms and graph walk structure. Theorem 3 extends the analysis to GINs. These bounds are concrete and go beyond prior heuristic defenses by identifying *which architectural factors* influence robustness — weight matrix norms, number of layers (through walk length), and graph density (through walk counts).

3. **Theory-motivated defense (GCORN) with strong empirical results.** The paper uses the bound's dependence on weight norms to motivate orthonormalization via Björck iteration. The empirical evaluation is the strongest part: Table 1 (described in text) shows GCORN outperforming four feature-attack defenses (GCN-k, RobustGCN, AIRGNN, ParsevalR) across Cora, CiteSeer, PubMed, CS, and OGBN-Arxiv under random, PGD, and Nettack attacks, often by double-digit margins (e.g., ~12% average improvement over GCN-k). This provides compelling evidence that the approach works in practice.

4. **Attack-independent probabilistic evaluation metric.** Section 5 introduces a sampling-based estimator for Adv⁽α,β⁾_ε[f], serving as a model-agnostic robustness metric. Unlike existing worst-case evaluations that are attack-specific, this provides a more comprehensive view. The idea of stratified sampling over the ε-ball is sensible and fills a gap noted by the authors in graph representation learning.

---

## Weaknesses

### Fatal
None.

### Major

1. **Lemma 1 (expected robustness ⇒ worst-case robustness) is unsupported and likely incorrect as stated.** The lemma claims: if f is ((d, ε), (d_𝒴, γ))-robust in the *expected* sense (i.e., Adv ≤ γ), then f is also ((d, ε), (d_𝒴, γ))-robust in the *worst-case* sense. This does not follow from any reasoning presented. A bound on the probability of failure does not imply a bound on the maximum possible output change — a model can have very low average failure probability while still having pathological worst-case inputs. The paper puts "worst-case" in scare quotes and does not provide a formal definition of what it means, making the claim ambiguous. The surrounding text ("by adjusting σ we can isolate worst-case examples") does not resolve this. This undermines the paper's claim that its expected-robustness framework *subsumes* the standard worst-case formulation.

2. **The theoretical connection between orthonormalization and the derived bounds is not formally established.** The bounds in Theorem 1 involve ||W||₁ and ||W||_∞ (matrix 1-norm = max column sum, matrix ∞-norm = max row sum). The orthonormalization procedure via Björck iteration constrains the spectral norm (||W||₂ = 1 for orthogonal matrices), but the paper provides no argument that orthonormalization reduces L₁ or L∞ norms. An orthogonal matrix can have large L₁ and L∞ norms (e.g., a dense Hadamard-like orthogonal matrix). The paper's claim that "any orthonormalization method can theoretically enhance the underlying model's robustness" (line 123) — based on Theorem 1 — is not justified by the mathematics presented. The GCORN method may work well empirically (the results suggest it does), but the *theoretical* motivation as presented is incomplete.

### Minor

1. **The bounds (γ values) can exceed 1, making them potentially vacuous as probability upper bounds.** Since Adv is a probability (≤ 1), a bound γ > 1 is mathematically valid but uninformative. The paper does not discuss this, nor does it provide any scaling or normalization to ensure γ ∈ [0,1]. This does not invalidate the theory — many ML theory papers have loose bounds that still capture correct functional dependencies — but it means the bounds are not practically useful as guarantees without further tightening. The paper should acknowledge this limitation.

2. **Lemma 2 (sampling radius distribution) has a likely error in the exponent.** For Z ∈ ℝ^{n×K} sampled uniformly from {Z: max_i ||Z_i||_p ≤ ε}, the PDF of R = max_i ||Z_i||_p is p_ε(r) = nK · (1/ε) · (r/ε)^{nK-1} (since the ball factorizes over n rows, each in ℝ^K). The paper gives p_ε(r) = K(1/ε)(r/ε)^{K-1}, which drops the n factor. This affects the stratified sampling procedure, though the overall Monte Carlo approach (Eq. 6–7) remains valid as an unbiased estimator regardless of the stratification weights. The independence from p claimed in the lemma is actually correct (the volume ratio of L_p balls depends only on r/ε and dimension K, not p), so the critic's complaint about p-dependence is wrong — but the missing n is a genuine error.

3. **The distance metric in Eq. (1) (min over permutations) is acknowledged but its computational tractability is not discussed.** The paper says "without loss of generality" it works with the feature-only distance d^{0,1}, but does not discuss the practical difficulty of the permutation-min formulation for attributed graph comparisons. This is a gap in the exposition, not a fatal flaw.

### Trivial
None.

---

## Nice-to-Haves

- **Adversarial training as a baseline.** The experiments compare against GCN-k, RobustGCN, AIRGNN, and ParsevalR, but not against simple adversarial training on features (e.g., PGD-based adversarial training). This is a natural and strong baseline that would strengthen the empirical comparison.
- **Error bars / confidence intervals.** The paper states 10 repetitions but the text does not report standard deviations or confidence intervals in the summary of results. The tables/figures from the inserted .tex files are not visible in the parsed text, but the summarizing text should mention significance.
- **Discussion of limitations.** The paper does not discuss scenarios where GCORN might underperform (e.g., if the Björck iteration does not converge or if orthonormalization harms clean accuracy on datasets with particular structure).

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The bounds are not valid as probability upper bounds because they exceed 1."** → The critic claims this is "structural" and makes the bound "meaningless." This is overblown. A bound that exceeds 1 is mathematically valid (Adv ≤ 1 ≤ γ implies Adv ≤ γ). The issue is *tightness*, not validity. Many ML theory papers derive bounds that are not tight. The argument that "the entire theoretical motivation for GCORN rests on the bound being valid" is also overstated — even a loose bound that depends on weight norms provides motivation for controlling those norms. Demoted to Minor.

- **"Lemma 2 is 'highly suspect' because the geometry of ℓ_p balls changes with p."** → The critic's specific complaint (that the distribution depends on p) is actually wrong. The volume of an L_p ball in ℝ^K scales as r^K × C(p,K), so the ratio vol(B_p(r))/vol(B_p(ε)) = (r/ε)^K does *not* depend on p. The independence from p is correct. However, there is a *different* error (missing n factor) that neither reviewer identified. Removed the incorrect p-dependence criticism; kept the correct observation about the missing n factor under Minor.

- **"Missing proofs in appendix" / "appendix is stripped."** → Per instructions, criticisms about missing appendix content from the parser-stripped paper are removed.

- **"Comparison to GNNGuard/GNN-SVD is misleading because those methods handle structural attacks."** → The paper *also* evaluates on structural attacks (Table 2) and fairly compares GCORN against structural defense methods. This criticism is unwarranted — removed.

- **Strength Finder claims about the paper's "importance" / "gap-filling."** → Generic scope claims ("this paper addresses an important problem") are dropped per instructions. Concrete strengths (the bounds, the method, the evaluation metric) are retained.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface one genuine error not caught by either reviewer individually: Lemma 2's PDF misses the n factor (number of nodes) in the exponent, though the critic's p-dependence objection is incorrect. The more interesting observation is that Lemma 1 and the theory-method gap are the paper's true theoretical vulnerabilities, not the >1 bound issue that the critic emphasized most.

---

## Suggestions

1. **Clarify or remove Lemma 1.** If the intended claim is different from what is written, provide a precise definition of "worst-case robust" and prove the implication. If the claim is that expected robustness *relates to* worst-case through a σ-dependent parameterization (as hinted in the surrounding text), state this explicitly and drop the unqualified implication.
2. **Bridge the gap between the bounds and orthonormalization.** Either (a) derive bounds that directly involve spectral norms (e.g., using ||W||₂ ≤ 1 for orthogonal matrices) and show how orthonormalization reduces them, or (b) provide an argument (theoretical or empirical) that orthonormalization reduces L₁/L∞ norms in practice, or (c) explicitly acknowledge the gap and position GCORN as empirically motivated with the theory as inspiration rather than a direct consequence.
3. **Fix Lemma 2's exponent.** Correct the density to p_ε(r) = nK(1/ε)(r/ε)^{nK-1} (or clarify if the lemma intends something different from what it states). Verify that this does not affect the stratified sampling algorithm's correctness.
4. **Add adversarial training as a baseline** and report standard deviations / confidence intervals for the main results.
5. **Discuss bound tightness.** Acknowledge that γ can exceed 1 and discuss conditions under which the bound becomes non-vacuous.

---
