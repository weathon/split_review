Now I have a thorough understanding of the paper and have verified each claim. Let me produce the consolidated review.

## Summary

This paper addresses causal discovery under LiNGAM with both latent variables and "complex" causal relations (i.e., settings that violate the purity, measurement, and no-triangle assumptions). The authors propose an algorithm that operates in two stages — bottom-up latent variable identification followed by top-down causal relation inference — and achieves cubic time complexity, which the authors claim is the first polynomial-time algorithm for this setting. They further prove a "trustworthiness" guarantee: under an additional assumption (Assumption 2), if the primary pure-children assumption (Assumption 1) is violated, the algorithm raises an error rather than returning an incorrect graph.

## Strengths

- **First polynomial-time algorithm for a genuinely hard setting.** The paper targets a practically relevant problem (LiNGAM with latent variables and none of the three common simplifying assumptions) where prior work (Jin et al., 2024) requires exponential time. The cubic-time complexity analysis is stated clearly, and the paper demonstrates the efficiency gap concretely on a case example (power-set traversal vs. linear traversal). The theoretical framing of the contribution is sound.

- **Novel theoretical machinery extending pseudo-residual methods.** Theorem 1 is explicitly distinguished from Theorem 2 of Cai et al. (2019). Without the purity and measurement assumptions, the paper shows that only "identifiable pairs" (rather than pure children directly) can be located via correlations and pseudo-residual independence — a nontrivial extension. The chain from identifiable pairs → classification into S₁/S₂/S₃ → pure child identification (Theorems 1–3) is a genuine technical contribution.

- **Trustworthiness guarantee is a conceptual advance.** While qualified, the ability to provably detect when the key assumption fails (Theorem 13) goes beyond prior work, which offers no such safeguard. The idea of leveraging the two-stage architecture to surface hidden risks from stage 1 during stage 2 is clever, and the experiments on violating cases (Figures 10, Section 5) show that the mechanism works in practice some of the time.

- **Two-stage (bottom-up then top-down) design is clean and well-motivated.** The paper clearly explains why this design avoids the exponential complexity of PO-LiNGAM's alternating approach, and the progression from leaves to roots in stage 1 and roots to leaves in stage 2 is intuitive and easy to follow at the conceptual level.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental validation is far too thin to support the practical claims.** The synthetic evaluation uses only four small graphs (Figure 9), each with only 10 sample sets per condition. No confidence intervals, standard deviations, or error bars are reported for any metric. Without knowing the variance of the results, the reader cannot assess the reliability of the method. The comparison with PO-LiNGAM would be far more convincing with scaling experiments on larger graphs (tens to hundreds of variables) to demonstrate that the polynomial complexity translates to practical efficiency at realistic scales. As it stands, the experiments demonstrate feasibility on toy problems but do not establish the algorithm's practical value.

2. **The trustworthiness guarantee is heavily qualified by Assumption 2, which includes conditions that are not verifiable from data.** Theorem 13 requires Assumption 2, whose conditions (1) and (2) are cited from Adams et al. (2021) as "necessary for identifiability." The paper acknowledges that "it might be unreasonable to expect trustworthiness without them" — but this means the practical scope of the trustworthiness guarantee is unclear. If the data are unidentifiable (conditions 1 or 2 fail), the algorithm may return an incorrect result without error, since the trustworthiness theorem does not apply. The paper provides no way for a practitioner to check whether Assumption 2 holds, making it difficult to know whether the guarantee is operative. This significantly limits the advertised trustworthiness.

3. **The error detection rate in practice is low (70–80%), and the paper does not explain why.** On finite samples (10k), the algorithm raises an error only 8/10 and 7/10 times on the two violation cases (Section 5). While the theory is asymptotic ("in the limit of infinite data"), a 20–30% failure rate on 10k samples is practically concerning and deserves analysis. Is this due to independence test errors? Is it structure-dependent? The paper offers no discussion, leaving a significant gap between the theoretical guarantee and the practical behavior.

### Minor

4. **The pure child definition (Definition 1) is restrictive and limits the method's scope.** Condition (ii) requires that *all descendants* of a pure child have exactly one parent. This excludes structures where a latent variable's influence propagates through any variable that later acquires multiple parents (branching, merging). While this is part of the stated assumption, the paper does not discuss how restrictive this is relative to real-world scenarios or how often it is likely to hold. The remark about Jin et al. (2024) having a *less* restrictive definition actually highlights the restrictiveness of the current approach.

5. **The abstract and title overstate trustworthiness by omitting the Assumption 2 qualification.** The abstract states "we prove trustworthiness of our algorithm, meaning that when the assumption is invalid, it can raise an error" — but this is only true under Assumption 2, which is not mentioned in the abstract. A reader could reasonably infer a stronger, unconditional guarantee. The body of the paper is transparent about this, but the front matter is misleading.

6. **The experimental section lacks key details about the graphs.** Beyond what is visible in Figure 9, the paper gives no information about the number of variables (observed and latent) in each test graph, the density of edges, or the degree of violation of the purity/measurement/no-triangle assumptions. This makes it difficult to assess whether the test cases adequately cover the claimed "complex relations" setting.

### Trivial

7. Several equations contain rendering artifacts (e.g., overbraced/garbled Theorem 10 header, broken subscripts in Theorem 5) that, while parser-related in the supplied text, the authors should ensure are clean in the camera-ready version.

## Nice-to-Haves

- A practical heuristic or simulation-based method for checking the plausibility of Assumption 2 conditions (1) and (2) would significantly increase the real-world value of the trustworthiness guarantee.
- Scaling experiments showing runtime vs. number of variables on synthetic graphs with 20–200 variables would strengthen the polynomial-time claim considerably.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Table 1 is garbled/unreadable so results cannot be assessed"** — The table is a parser artifact; the original submission contains it. Removed per hard rules.
- **"Real-world experiments deferred to unavailable appendix"** — The parser strips appendix content; this existed in the original. Removed per hard rules.
- **"Detailed algorithms and proofs deferred to unavailable appendix"** — Same reasoning. Removed per hard rules.
- **"70–80% error detection undermines asymptotic guarantee"** — The asymptotic guarantee (Theorem 13) is for the limit of infinite data. Finite-sample behavior does not undermine it. The practical concern is valid and reframed as Major #3 above, but the theoretical claim about "undermining the guarantee" is removed.
- **"The paper should include a discussion of missing related works"** — Hard rule prohibits inventing missing related works.
- **Several formatting/style nitpicks from the section-by-section notes** — Removed per hard rules.
- **"Why exactly two children in the augmentation?" and other minor exposition questions** — These are answered by the method's design (two surrogates needed for root identification in Stage 2); moved to minor/trivial.

## Novel Insights

The reviews reveal a gap between the paper's theoretical ambition and its empirical execution that is larger than the paper itself acknowledges. The core insight — that the two-stage architecture (bottom-up identification → top-down inference) enables both polynomial efficiency *and* error detection — is genuinely interesting and may influence future work. However, the reviewers collectively highlight that the trustworthiness guarantee, while novel, rests on an assumption (Assumption 2) that is essentially the identifiability condition for the entire class of models. This creates a structural tension: the guarantee is strongest exactly when the problem is already identifiable, and weakest (or inapplicable) when the problem is hardest. The paper does not fully grapple with this tension. Additionally, the finite-sample behavior of the error detection mechanism (70–80% on 10k samples) suggests that practical trustworthiness may require substantially more data than the recovery task itself — an observation worth investigating.

## Suggestions

1. **Significantly expand the experimental evaluation.** Include at least 5–10 graph structures of varying sizes (10–100 variables), report means and standard deviations across 50+ random trials, and include a scaling plot showing runtime vs. number of variables for both the proposed method and PO-LiNGAM on problems where PO-LiNGAM is feasible.

2. **Analyze the finite-sample behavior of the error detection mechanism.** Why does the algorithm fail to raise an error 20–30% of the time on 10k samples? Is this due to independence test power, and would larger samples close the gap? A power analysis or simulation study would address this.

3. **Add a discussion of how a practitioner might assess the plausibility of Assumption 2 (or at least the non-pathological-variable condition).** Even a qualitative discussion of what kinds of domain knowledge could rule out pathological variables would strengthen the paper.

4. **Revise the abstract and title to qualify the trustworthiness claim.** Add a phrase such as "under an additional identifiability condition" so that readers are not misled.

5. **Provide a worked example in the main text** showing the algorithm's decisions step-by-step on a concrete small graph (e.g., Figure 2), including how identifiable pairs are detected and classified.

## Score and Decision

**Originality:** 7/10 — The problem setting is not new, but the polynomial-time algorithm and trustworthiness guarantee are genuine advances over prior work (PO-LiNGAM, GIN).

**Importance of research question:** 8/10 — Causal discovery with latent variables under realistic (non-simplified) assumptions is an important and active area.

**Claims well-supported:** 4/10 — The theoretical claims are supported by proofs (deferred to appendix), but the experimental evidence is too weak to support the practical claims of efficiency and trustworthiness.

**Soundness of experiments:** 3/10 — Too few test cases, no error bars, no scaling analysis, and unexplained 20–30% failure rate on the trustworthiness task.

**Clarity of writing:** 6/10 — The high-level structure is clear, but the dense notation and deferred details make the paper hard to follow. Many theorems are presented without proof sketches or intuition.

**Value to research community:** 6/10 — The theoretical framework is valuable and will likely inspire follow-up work, but the weak evaluation limits immediate impact.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>