Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper studies differentially private domain discovery, where each user holds a subset of items from a shared but unknown domain. The authors show that the Weighted Gaussian Mechanism (WGM) provides near-optimal ℓ₁ missing mass guarantees on Zipfian data (Theorem 3.3), with a matching lower bound (Theorem 3.5), as well as a distribution-free ℓ∞ bound (Theorem 3.6). They then apply WGM as a domain-discovery precursor for existing known-domain algorithms for private top-k and k-hitting set, obtaining new unknown-domain utility guarantees (Theorems 4.3, 4.5). Experiments on six real-world datasets show that WGM-based methods are competitive with or outperform existing baselines.

## Strengths

1. **First absolute utility guarantees for DP set union.** The paper explicitly notes that prior DP set union results provide relative guarantees (bounds stated relative to other algorithms), while the WGM bounds in Theorems 3.3, 3.5, and 3.6 are absolute. The matching lower bound (Theorem 3.5) shows near-optimality up to logarithmic factors, which is a genuine theoretical contribution.

2. **Clean modular extension to downstream tasks.** Using the ℓ∞ missing mass guarantee (Theorem 3.6) as a building block, the paper obtains new utility guarantees for unknown-domain top-k (Theorem 4.3) and k-hitting set (Theorem 4.5) via a simple meta-algorithm (Algorithm 2). This modular approach is conceptually clean and practically useful.

3. **Matching lower bounds for all three problems.** The paper provides lower bounds for set union (Theorem 3.5), top-k (Corollary 4.4), and k-hitting set (Corollary 4.6), all under Assumption 1, which clarifies the fundamental difficulty of private domain discovery. The lower bounds for top-k and k-hitting set are genuinely new.

4. **Generalized missing mass objective.** Defining MMₚ for any p ≥ 0 (Equation 1) unifies the cardinality objective (p=0) of prior work with the frequency-based missing mass (p=1) and the ℓ∞ objective, providing useful conceptual framing.

5. **Empirical validation on real-world data.** The experiments evaluate on six diverse real-world datasets across all three problems, demonstrating that WGM-based methods are competitive with or outperform existing baselines.

## Weaknesses

### Fatal
None.

### Major

- **Misleading empirical claim about set-union experiments.** Section 5.1 states that "the WGM obtains MM within 5% of that of the policy mechanisms." The data in Figure 1 contradicts this: on Movie Reviews, WGM achieves MM ≈ 0.02 while Policy Gaussian achieves ≈ 0.12 (a 10-percentage-point difference, and WGM is substantially *better*, not "within 5% of"); on Reddit the difference is even larger. The paper undersells its own results, but the claim as written is factually inaccurate and must be corrected. This is a presentation error — the actual results are stronger than stated — but it damages the credibility of the empirical narrative.

### Minor

- **Missing variance information in Figures 1 and 2.** Only averages over 5 trials are reported without error bars, standard deviations, or confidence intervals. Figure 3 does include standard error, so the omission from Figures 1–2 is noticeable. While 5 trials may suffice for stable averages, the absence of variance information makes it impossible to assess whether observed differences between methods are statistically meaningful.

- **Legend confusion in Figures 2 and 3.** Figure 2 shows three "Limited-Delta" entries and one "Uniform" entry, but the text describes baselines with k̃ ∈ {k, 5k, 10k, ∞} — the mapping between legend entries and these configurations is unclear. Figure 3 shows "DP-Top-k" and "DP-Top-k with Pay-What-You-Get" as baselines, but the text describes "the non-private greedy algorithm and the private non-domain algorithm from Mitrovic et al. (2017)," and the figure also includes "Random Selection" which is not mentioned in the text. The text descriptions and figure legends need to be made consistent.

- **Limited scalability discussion.** The downstream peeling mechanisms (Algorithms 3 and 4) compute noisy scores for every item in the discovered domain D. The paper does not discuss computational cost when M = |⋃ᵢ Wᵢ| is large (e.g., millions of unique items), nor when the discovered domain is large. A brief complexity note would strengthen the presentation.

### Trivial
None.

## Nice-to-Haves

- Adding a short justification of the asymptotic parameter choices from Theorem 3.2 in the main text would improve readability, though the appendix derivation is acceptable.
- A brief comment on how the bound in Theorem 4.3 handles the case where M = |⋃ᵢ Wᵢ| is very large would be useful.
- The comparison with Durfee & Rogers (2019) could note that the present approach obtains a guarantee on missing mass, which is more stringent than their k-relative error, and that the experiments confirm this advantage.

## Removed Points

These points were raised by reviewers but are removed for the following reasons:
- *Overbroad claim about "first to prove absolute utility guarantees"*: The paper already acknowledges Desfontaines et al. (2022) and clarifies that their guarantees are relative (stated relative to other algorithms), while the present work provides absolute guarantees. This is a fair distinction.
- *Missing related works*: No external sources available to verify; default is to treat cited references as real. The paper's related work section is appropriately positioned.
- *Formatting/style nitpicks about typos and presentation*: Parser artifacts, not author errors.
- *Criticisms demanding the paper address problems outside its stated scope*: E.g., demanding theoretical proofs for empirical systems aspects, or requiring scalability analysis for billion-scale datasets.
- *Reproducibility concerns about undisclosed hyperparameters or missing appendix content*: The parser strips appendices; these exist in the original submission.

## Novel Insights

The key insight that emerges from combining the reviewer analyses is that the paper's modular approach — separating domain discovery (WGM) from downstream tasks — is more than a convenience: the ℓ∞ bound on missing mass (Theorem 3.6) acts as a transferable guarantee that makes the modular pipeline provably effective regardless of the data distribution, which is a genuinely stronger property than the distribution-specific ℓ₁ bound. This modularity is what enables clean extensions to top-k and k-hitting set without re-proving privacy or utility from scratch, and it suggests the WGM could serve as a generic domain-discovery primitive for other unknown-domain DP problems beyond those considered here.

## Suggestions

1. **Correct the set-union empirical claim.** Replace "within 5% of that of the policy mechanisms" with an accurate description, e.g., "achieves MM comparable to or better than that of the policy mechanisms" or quantify the actual differences observed.
2. **Add variance information to Figures 1 and 2**, even as a brief caption note (e.g., "error bars omitted for clarity; variance was < X across 5 trials"), or add error bars.
3. **Make figure legends consistent with text descriptions.** For Figure 2, map each "Limited-Delta" entry to the corresponding k̃ value. For Figure 3, either rename legend entries to match the text descriptions (e.g., "Private known-domain greedy"), or add the missing baseline descriptions to the text.

## Score and Decision

### Calibration Summary

**Round 1 (Bracketing, 5–7):** Searched for DP set union / domain discovery papers by score band. Weak anchors at 1.5–3.0 (withdrawn/rejected papers with serious flaws); middle anchors at 4.0–6.5 (papers with solid but imperfect contributions); strong anchors at 8.0 (unrelated topics). This paper clearly sits above the weak band and well below the unrelated 8.0s, giving an initial bracket of roughly 5–7.

**Round 2 (Narrowing within bracket):** Compared against four anchors:
- *DP-OPH* (avg 5.00): Straightforward combination of existing techniques with limited novelty. This paper has deeper theory (matching lower bounds, first absolute guarantees) and broader scope → **This paper is stronger**.
- *Skirting Additive Error Barriers* (avg 6.50): Clever theoretical DP results for stream problems, well-received (Accept Poster). Comparable in theoretical rigor, similar novelty level → **This paper is slightly weaker overall due to presentation issues**.
- *Gaussian Certified Unlearning* (avg 6.00): Theoretical DP unlearning framework, accepted as Oral. Similar depth of theory, but experiments limited to synthetic data → **Roughly comparable**.
- *Unified Privacy for Decentralized Learning* (avg 6.00): Solid unifying theoretical framework, accepted as Poster. Similar level of contribution → **Roughly comparable**.

The paper's theoretical contributions (first absolute guarantees, matching lower bounds, modular extensions) are genuinely novel and well-supported. The presentation issues (misleading empirical claim, figure legend confusion) are real but fixable and do not threaten the core contributions. The paper sits in the same band as the 6.0–6.5 anchors.

**Final Score:** 6.0

**Decision:** Accept (Poster)

<score>6.0</score>
<decision>Accept</decision>