## Summary

The paper studies differentially private domain discovery under the lens of *missing mass* rather than cardinality. The core result (Theorem 3.3 + Corollary 3.4) is a near-tight utility guarantee showing the simple Weighted Gaussian Mechanism (WGM) achieves near-optimal ℓ₁ missing mass on Zipfian datasets, with a matching lower bound (Theorem 3.5). A complementary distribution-free ℓ∞ bound (Theorem 3.6) is then used as a building block to derive utility guarantees for unknown-domain variants of DP top-k selection and k-hitting set via a composition-based meta-algorithm. Experiments on six real-world datasets confirm that WGM-based methods are competitive with significantly more computationally expensive baselines.

---

## Strengths

- **First absolute utility guarantees for DP set union.** Prior work (Desfontaines et al., 2022; Chen et al., 2025) only established relative guarantees comparing against other algorithms. Theorem 3.3/Corollary 3.4 fill this foundational gap with a concrete bound in terms of Zipfian parameters, privacy budget (ε, δ), and dataset statistics.

- **Near-tight bounds.** Theorem 3.5 shows a lower bound matching the ε and N dependence of Corollary 3.4 for any (ε, δ)-DP algorithm satisfying the soundness assumption. The argument exploiting Assumption 1 to prevent output of low-frequency items is elegant.

- **Meaningful objective reframing.** Replacing cardinality with missing mass is well-motivated: it captures the fraction of empirical mass recovered rather than the raw count, making the objective invariant to the number of rare items and more informative for downstream utility. The ℓ_p generalization (Definition 2.2) is a clean unification that recovers cardinality (p=0) and max-missing-mass (p=∞) as special cases.

- **Practical relevance of the meta-algorithm.** Algorithm 2 (WGM → known-domain algorithm) is a clean, implementable pipeline that does not require prior knowledge of the domain, and the composition is tight. The resulting guarantees for both top-k (Theorem 4.3) and k-hitting set (Theorem 4.5) are the first for the fully unknown-domain setting of these problems.

- **Empirical validation.** WGM achieves MM within 5% of the computationally expensive policy mechanisms on set union, and consistently outperforms all limited-domain baselines on top-k selection. The k-hitting set results match or exceed Mitrovic et al.'s private greedy algorithm that assumes public knowledge of the domain, which is a striking finding.

- **Six diverse real-world datasets** spanning different sizes and domains provide convincing evidence that the theoretical insights translate to practice.

---

## Weaknesses

### Fatal
None.

### Major

- **Potential error in Theorem 4.5 approximation factor.** The guarantee reads "Hits(W, S) ≥ (1 − 1/ε)Opt(W, k) − …". When ε < 1 (common in practice), the factor 1 − 1/ε is negative, making the bound trivially satisfied and the theorem content-free for standard privacy regimes. The standard greedy approximation for submodular maximization is (1 − 1/e); if that is what was intended, the theorem's multiplicative bound carries no meaningful privacy-related degradation, and the approximation quality is entirely captured by the additive error term. The authors should clarify whether this should be (1 − 1/e) or whether there is a genuinely ε-dependent approximation factor with a different derivation.

- **Potential sign error in Corollary 4.6.** The corollary states "there exists a dataset W such that E[Hits(W, S)] ≥ Opt(W, k) − Ω̃_δ(k/ε)", with a "≥". As a hardness/impossibility result, the intended meaning is surely that any DP algorithm achieves *at most* Opt(W, k) − Ω̃_δ(k/ε) on some hard dataset (i.e., the inequality should be ≤), analogous to how Corollary 4.4 shows MM^k ≥ Ω̃_δ(k/εN) on a hard dataset. As written, the statement claims the algorithm does well on that dataset, which would not constitute a lower bound.

### Minor

- **Gap between upper and lower bounds for top-k and k-hitting set.** Theorem 4.3 has a log(M) factor in the second term that is absent from the lower bound in Corollary 4.4. For k-hitting set, the gap is wider. The authors acknowledge this in the future work section, but the practical significance of this gap (which scales with log of the number of unique items) is not discussed.

- **The ℓ₁ upper bound (Theorem 3.3) vs. the ℓ∞ lower bound.** The paper proves ℓ₁ missing mass upper bounds for set union under Zipfian assumptions, but the lower bound (Theorem 3.5) is also in ℓ₁ (i.e., the standard missing mass). The ℓ∞ bound in Theorem 3.6 has no matching lower bound; some discussion of how tight this bound is would add value.

- **Choice of Δ₀.** Corollary 3.4 advises setting Δ₀ = max_i |W_i| (if publicly known), but in practice this quantity is unknown and must be treated as private. The paper provides no guidance on how to set Δ₀ privately, and the experiments fix Δ₀ = 100 without justification. A sensitivity analysis or a method to choose Δ₀ adaptively would strengthen the practical guidance.

### Trivial

- The hardness argument in Section 3 (showing MM ≥ 1 − δ for singleton datasets) is a clean motivation, but the transition from "this pathological dataset exists" to "Zipfian is the right assumption" is informal.

---

## Nice-to-Haves

- An explicit tighter lower bound for the ℓ∞ missing mass setting to assess how tight Theorem 3.6 is.
- A discussion of how the meta-algorithm's 50/50 budget split compares to optimal allocation, and whether adaptive splitting improves guarantees.
- Experiments varying ε to show how strongly the theoretical ε-dependence manifests empirically.

---

## Novel Insights

The most genuinely novel insight is that the WGM, despite being a simple non-adaptive single-pass mechanism, achieves near-optimal performance for DP set union when utility is measured by missing mass rather than cardinality. This reconciles the apparent empirical competitiveness of WGM (previously observed but unexplained) with theory, and it suggests that the large cardinality advantage of computationally expensive sequential methods is an artifact of optimizing for the wrong objective. The further observation that WGM domain discovery, by producing a *smaller* domain of high-quality items, can actually improve downstream peeling mechanisms (outperforming methods with access to the full domain) is subtle and practically important.

---

## Suggestions

- Verify and correct the approximation factor in Theorem 4.5: confirm whether it is (1 − 1/e) (the standard greedy approximation) or an ε-dependent factor, and provide the correct derivation.
- Fix the inequality direction in Corollary 4.6 to read "≤" if the intent is a hardness result.
- Add a brief discussion (or small experiment) on how to select Δ₀ adaptively or with public side-information.
- Provide a lower bound for the ℓ∞ missing mass to complement Theorem 3.6.

---

## Score and Decision

The paper makes a genuine and well-motivated theoretical contribution: the first absolute utility guarantees for DP set union, proven for a practically deployed mechanism under a realistic data assumption, with near-matching lower bounds. The extension to top-k and k-hitting set is clean and practically useful. The experimental results reinforce the theory. The two major concerns (approximation factor in Theorem 4.5 and inequality direction in Corollary 4.6) are likely typographic errors introduced in PDF extraction, but they should be verified and corrected. Assuming these are artifacts, the paper's core claims are sound and the contribution merits acceptance.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>