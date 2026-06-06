## Summary

This paper studies differentially private domain discovery under a missing mass framework — measuring the fraction of total item mass not recovered, rather than the cardinality of items found. The authors prove the first absolute utility guarantees for DP set union via the Weighted Gaussian Mechanism (WGM), showing near-optimal ℓ₁ missing mass on Zipfian data (Theorem 3.3, Corollary 3.4) with a matching lower bound (Theorem 3.5), and a distribution-free ℓ∞ guarantee (Theorem 3.6). These are then leveraged in a modular Algorithm 2 to obtain the first utility guarantees for unknown-domain private top-k and k-hitting set. Experiments on six real-world datasets corroborate the theory.

---

## Strengths

1. **First absolute utility guarantees for DP set union** (Section 1.1, Corollary 3.4): Prior work (Desfontaines et al. 2022, Chen et al. 2025) only provided *relative* comparisons between algorithms. This paper provides concrete, explicit high-probability bounds on missing mass, filling a clear gap in the literature.

2. **Near-optimal ℓ₁ missing mass on Zipfian data with matching lower bounds** (Corollary 3.4, Theorem 3.5): The upper bound scales as `(max_i |W_i| / εN√q*)^{(s-1)/s}` and the lower bound as `(1/εN)^{(s-1)/s}`, matching up to log factors (using Lemma 3.1 which bounds max_i |W_i| ≤ (CN)^{1/s}). This tightness is the headline theoretical result.

3. **Distribution-free ℓ∞ missing mass bound with downstream consequences** (Theorem 3.6): The ℓ∞ guarantee — requiring no Zipfian assumption — enables novel utility guarantees for private top-k (Theorem 4.3) and k-hitting set (Theorem 4.5) in the unknown-domain setting, via clean algorithm composition.

4. **Modular algorithm design** (Algorithm 2): The WGM-then-known-domain-algorithm structure is simple, implementable, admits clean privacy proofs via basic composition, and generalizes across multiple downstream tasks.

5. **Comprehensive empirical validation**: Experiments span six diverse real-world datasets (Reddit, Amazon, MovieLens, Steam). WGM-based methods are competitive with computationally heavy sequential baselines for set union, outperform prior unknown-domain methods for top-k, and match or exceed a known-domain private baseline for k-hitting set on two of three datasets.

---

## Weaknesses

### Fatal
None.

### Major

- **Likely notation error in Theorem 4.5's multiplicative approximation factor** — Theorem 4.5 states Hits(W, S) ≥ (1 − 1/ε) · Opt(W, k) − err(·), where ε throughout the paper is the DP privacy parameter. For the standard regime ε ≤ 1, the factor (1 − 1/ε) ≤ 0, rendering the multiplicative part of the bound vacuous. The standard approximation ratio from the greedy submodular maximization procedure invoked (Mitrovic et al. 2017, Algorithm 1) is (1 − 1/*e*) ≈ 0.632, where *e* is Euler's number. The visual similarity between ε and *e* in LaTeX strongly suggests a typographic collision. If (1 − 1/ε) with ε = DP privacy parameter is genuinely the intended statement (e.g., the theorem is only claimed for ε > 1), the authors must add a clear parameter restriction and explain why this range suffices; otherwise this must be corrected to (1 − 1/*e*). The additive error term and Corollary 4.6 are unaffected. This must be resolved before publication.

### Minor

- **Near-optimality for Zipfian data is not presented as a clean matching theorem** — The abstract and introduction claim the WGM is "near-optimal" on Zipfian data, but to verify this the reader must themselves substitute Lemma 3.1 (`max_i |W_i| ≤ (CN)^{1/s}`) into Corollary 3.4 and reconcile with Theorem 3.5. A single corollary of the form "For (C,s)-Zipfian data, WGM achieves MM = Θ̃(C^{1/s}/(s−1)·(1/εN)^{(s-1)/s}) and this rate is optimal" would make the headline contribution immediately verifiable and substantially improve clarity.

- **Δ₀ sensitivity analysis absent for top-k and k-hitting set experiments** — Figures 2 and 3 fix Δ₀ = 100 with no sweep. The set union experiments (Figure 1) show strong dependence on Δ₀, and Theorem 4.3's bound depends on q* = min{Δ₀, max_i|W_i|}. Showing how Figure 2/3 results change as Δ₀ varies would make the experimental section as informative as Section 5.1.

- **"Within 5%" claim and Figure 1's visual description appear inconsistent** — Section 5.1 states "the WGM obtains MM within 5% of that of the policy mechanisms." However, Figure 1's caption (as parsed) describes WGM as dropping sharply and remaining flat while the Policy methods "remain relatively high," suggesting WGM substantially outperforms the baselines — a stronger finding than "within 5%." Since lower MM is better, the claim and the visual seem to point in opposite directions in magnitude. If WGM is genuinely better by more than 5%, that is a stronger result and should be stated directly; if not, the figure description requires clarification.

### Trivial
None.

---

## Nice-to-Haves

- A brief analysis or discussion of the optimal privacy budget split between the WGM stage and the downstream algorithm in Algorithm 2. The 50/50 split is clean for proofs but the practical optimal split likely depends on dataset parameters (N, k, Δ₀), and a short note on this would help practitioners.
- A formal remark or lemma quantifying why cardinality-optimal algorithms can have high missing mass on Zipfian data — the intuition is stated informally in the introduction but a brief formalization would sharpen the paper's motivation for the missing mass reframing.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — "WGM substantially dominates baselines" as a finding contradiction**: This was partially based on a parser-generated image alt text description that may not faithfully represent the actual figure. The claim of "within 5%" in the paper text is the authoritative statement; the alt text is a noisy proxy. Demoted to Minor for the internal consistency concern, but not accepted as evidence of a fundamental discrepancy.

- **Harsh Critic — top-k tested only on "small" datasets as a limitation**: The paper explicitly explains this choice ("All methods achieve near 0 top-k missing mass across all values of k on the three large datasets, as most mass is concentrated in a small number of heavy items"). This is a data characteristic, not a methodological weakness. Removed.

- **Harsh Critic — k-hitting set baselines are not truly comparable**: The paper already acknowledges this directly: "Note that the latter baseline is not a valid private algorithm in the unknown domain setting since, in reality, ∪_i W_i is private." The comparison is informative and the caveat is explicit. Removed as a weakness.

- **Strength Finder — "addresses an important problem" / "this paper targeted an interesting question"**: Removed as generic. Kept only concrete, evidence-backed strengths.

---

## Novel Insights

The central insight — that missing mass, not cardinality, is the right objective for evaluating DP set union on realistic (Zipfian) data — unlocks a tractable analysis of the WGM that cardinality-based approaches could not provide. The paper shows formally that WGM's behavior under missing mass is near-optimal precisely because it recovers high-frequency items preferentially; prior empirical results (where sequential methods recover ≈2× more items by cardinality) are recontextualized as measuring the *wrong* thing. The ℓ∞ missing mass bound (Theorem 3.6) is a technically elegant distribution-free result that converts domain uncertainty into additive suboptimality for downstream tasks, without requiring the downstream structure to be Zipfian.

---

## Suggestions

1. **Correct or clarify the (1 − 1/ε) factor in Theorem 4.5**: If it is a typo for (1 − 1/*e*), correct it and note that the standard greedy approximation factor carries through the composition. If it is intentional, add an explicit restriction ε > 1 and explain the practical validity range.
2. **Add a clean "matching bounds" corollary** combining Corollary 3.4 + Lemma 3.1 + Theorem 3.5 into a single statement that directly exhibits optimality.
3. **Add a Δ₀ sensitivity plot for Figure 2** (top-k) analogous to Figure 1, varying Δ₀ ∈ {50, 100, 150, 200}.

---

**Originality**: High — reframing DP set union via missing mass and proving the first absolute guarantees is a genuine conceptual and technical contribution.
**Importance**: High — set union / partition selection is a core component of deployed DP systems, and the lack of provable guarantees was a real open problem.
**Claims Supported**: Mostly — the theory is rigorous and experiments match predictions, but the approximation factor in Theorem 4.5 requires correction.
**Soundness**: Good — the proof architecture is clean and modular, pending resolution of the Theorem 4.5 notation issue.
**Clarity**: Good — the paper is well-organized; the one clear improvement is a unified near-optimality statement.
**Value to Community**: High — provides actionable guarantees for a practically deployed algorithm class.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>