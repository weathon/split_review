Now I have a thorough understanding of the paper and can verify each claim. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me compose this now.

---

Let me carefully cross-check all the reviewer's specific claims one more time.

**Claim 1 (Critical Issue 1): Eq. 14 is nonsensical.** 
The paper says: E_r "extracts relations from the triplets." For a triplet t = (x,r,y), E_r(t) returns the relation(s). Since a triplet has one relation, E_r(t) returns {r}. Then r1 ∈ {r} ∧ r2 ∈ {r} means r1 = r and r2 = r, so r1 = r2 = r. So C(r1 ⇒ r2) = 1 if r1 = r2 and 0 otherwise. This is not the intended meaning. The intended meaning (co-occurrence at the entity level) is standard in KG rule mining but the formula is incorrectly written.

The reviewer says "this is not a minor typo—it is a formal error that makes the core edge-denoising component undefined." This is an overstatement. The intended meaning is clear to anyone familiar with KG rule confidence (e.g., from AMIE+). It's a notational imprecision that should be fixed, but it doesn't make the component "undefined." I'll keep this as Minor.

**Claim 2 (Critical Issue 2): Path scoring conflates path evaluation with node evaluation without justification.**
The paper acknowledges this is an approximation (line 107: "Therefore, we approximate the evaluation of paths by evaluating the nodes"). The scoring function incorporates path information through current and remaining path scores. The reviewer says this is "precisely the same node-score strategy the paper criticizes" — this is inaccurate. The paper criticizes methods that evaluate nodes based on node-level features only. DDLR's scoring is path-aware (current + remaining path scores). I'll keep the concern about insufficient justification as Minor but reject the claim that it's the same as what's criticized.

**Claim 3 (Critical Issue 3): No non-GNN baselines compared.**
FALSE. The paper compares against RuleN, NeuralLP, and DRUM — all non-GNN methods. REMOVE this claim.

**Claim 3: No confidence intervals.**
True. Common in KGC but a valid minor weakness. Keep as Minor.

**Other observations:**
- "No analysis/case study showing difference from node-score approach" — Valid Minor concern.
- "Remaining path score construction is unclear" — Valid Minor concern.
- "No ablation on p_e and p_τ" — Valid Minor concern.

**Missing parts:**
- "Missing description of how negative triplets are generated" — The paper describes multi-class log-loss following Lacroix et al. (2018), which uses all entities as negatives in a softmax. This IS a description. REMOVE.
- "No code release or reproducibility checklist" — REMOVE per hard rules about reproducibility nitpicks.
- "No analysis of computational cost" — Valid Minor point.

Now for the Strength Finder output - let me filter:

1. "Dual denoising yields consistent SOTA across diverse inductive splits" — This is supported by Table 1 results. KEEP.

2. "Path-scoring mechanism that jointly models current and remaining path scores" — This is a genuine contribution supported by ablation. KEEP.

3. "Triplet-level single rules for edge sampling with Bernoulli distribution" — This is a valid contribution supported by Table 4. KEEP.

Supporting strength about ablation studies — KEEP, since these isolate contributions.

Now let me write the review.Now I have thoroughly verified every claim against the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes DDLR, a dual denoising framework for inductive knowledge graph completion that combines (1) path-based sampling using a path-scoring mechanism that considers both current and remaining path scores, and (2) edge-based sampling using single-rule confidence with Bernoulli-distributed sampling. Experiments on WN18RR, FB15k-237, and Nell-995 across 12 inductive splits show consistent improvements over eight baselines. Ablation studies confirm the contribution of each component.

## Strengths

- **Consistent empirical gains across diverse inductive splits.** DDLR achieves the best or second-best filtered MRR and Hits@10 on all 12 inductive splits (v1–v4 for WN18RR, FB15k-237, Nell-995) against six strong GNN-based baselines (GraIL, NBFNet, RED-GNN, Adaprop, GraPE) and three non-GNN rule-based methods (RuleN, NeuralLP, DRUM), as shown in Table 1. This directly supports the core claim that dual denoising improves inductive KGC.

- **Novel path-scoring mechanism combining current and remaining path scores.** The scoring function (Eqs. 8–10) jointly models the path score from the source to an intermediate node and the estimated remaining path score. Ablation in Table 3 shows that removing either component degrades performance across all datasets, confirming this joint evaluation is more effective than prior node-score-only approaches.

- **Principled edge-level denoising via triplet-level rule confidence with Bernoulli sampling.** Rather than deterministic top-K or entity-level relevance measures, DDLR extracts single rules at the triplet level (Eq. 14) and samples edges using a Bernoulli distribution derived from rule confidence. Table 4 shows this outperforms cosine similarity, KL divergence, and JS divergence for measuring relation relevance, providing a principled alternative to prior node-only sampling methods.

- **Systematic ablation isolating each component.** Table 2 separately ablates edge sampling, path sampling, and triplet-level granularity, with each removal causing a clear performance drop. This provides direct empirical evidence that both denoising modules and the triplet-level formulation are necessary.

## Weaknesses

### Fatal

None.

### Major

None. The verified weaknesses are real but do not threaten the paper's core claims or conclusions.

### Minor

- **Imprecise notation in the rule confidence formula (Eq. 14).** The equation writes  
  `C(r₁ ⇒ r₂) = Σ_{t∈E} 𝟙(r₁ ∈ E_r(t) ∧ r₂ ∈ E_r(t)) / Σ_{t∈E} 𝟙(r₁ ∈ E_r(t))`  
  where E_r(t) extracts the relation from a single triplet. Since each triplet has exactly one relation, the condition r₁ ∈ E_r(t) ∧ r₂ ∈ E_r(t) is only satisfied when r₁ = r₂. The intended meaning — counting *entities* that appear in triplets with both relations — is standard in KG rule mining (cf. AMIE+) but is not correctly expressed by the formula as written. This does not invalidate the method (the intended computation is clear from context and downstream usage), but it should be corrected for precision.

- **The path-to-node approximation (Eq. 7) lacks rigorous justification.** The paper acknowledges that evaluating all paths is computationally prohibitive and therefore "approximate[s] the evaluation of paths by evaluating the nodes." The scoring function (Eq. 10) is path-aware (combining current and remaining path scores), so it is not the same as the simple node-score approach criticized in Section 1. However, the paper does not theoretically or empirically demonstrate that this approximation avoids the failure mode illustrated in Fig. 1 (where node-score top-K selects the wrong entity). A case study or analysis showing that the new scoring would select the correct path in that example would substantially strengthen the argument.

- **The "remaining path score" construction (Eq. 8) is under-explained.** The representation r_q^{(t)}(x,v) is computed using only h_q^{(t)}(u,x) and the query relation q, with no explicit dependence on the future entity v. The paper states it "utilize[s] the query relation q as an approximation," but does not clarify why this combination meaningfully represents the remainder of the path from x to an unknown answer. This is a reasonable design heuristic — and the empirical results support it — but the conceptual justification is thin.

- **No confidence intervals, standard deviations, or significance tests reported.** Many of the performance differences over baselines like NBFNet and Adaprop are within a few percentage points. Without measures of variance, it is difficult to assess whether these gains are statistically meaningful. While single-run evaluation is common in KGC, reporting variance (even over a few seeds) would strengthen the empirical claims.

- **Missing sensitivity analysis for hyperparameters p_e and p_τ.** The edge sampling module has two hyperparameters (a probability multiplier p_e and a truncation probability p_τ) with ranges specified in the experimental setup, but no ablation or sensitivity study is provided to show how performance varies with these choices.

- **No computational cost comparison.** Training and inference times relative to baselines are not reported, making it difficult to assess the efficiency cost of the dual sampling framework.

### Trivial

- Minor presentation issues typical of conference submissions (e.g., "remain" where "retain" is intended in the caption of Fig. 2).

## Nice-to-Haves

- A case study or attention visualization demonstrating that DDLR's path-aware scoring correctly selects the entity overlooked by node-score top-K in the Fig. 1 example.
- Sensitivity analysis for hyperparameters p_e and p_τ.
- Confidence intervals or standard deviations for all main results.
- Computational cost (training/inference time) comparison with baselines.

## Removed Points

These points are flagged to be removed; treat them with caution. They were not included in the Weaknesses above because they are factually incorrect, parser artifacts, or violate the review guidelines.

1. **"The paper does not compare against any non-GNN inductive methods (e.g., TLogic or RLogic)."** — Factually incorrect. The paper explicitly compares against RuleN, NeuralLP, and DRUM, which are non-GNN rule-learning methods (Section 5.1). Removed.

2. **"Missing description of how negative triplets are generated for the loss function."** — The paper specifies a multi-class log-loss following Lacroix et al. (2018), which is a standard approach where all entities serve as implicit negatives via softmax normalization (Eq. 18, Section 4.4). Removed.

3. **"Table 1 appears garbled in the parsed text"** — This is a PDF parsing artifact, not an error in the original submission. Removed.

4. **"No code release or reproducibility checklist."** — Code release is not a requirement for review; hyperparameters are extensively documented (Section 5.1). Removed per reproducibility-nitpick guidelines.

5. **"The path scoring mechanism is precisely the same node-score strategy the paper criticizes."** — Inaccurate. The paper's scoring function (Eq. 10) explicitly incorporates path information through current and remaining path scores, which is fundamentally different from the simple node-level scores it criticizes. The concern about insufficient justification is kept as a Minor weakness above; the claim of equivalence is removed.

6. **Characterization of Eq. 14 as making the "core edge-denoising component undefined" and "the claimed contribution of edge-based sampling has no foundation."** — Overstatement. The intended computation is standard in KG rule mining; the formula has a notational imprecision that should be fixed but does not invalidate the method. The notational issue is retained as Minor; the fatal characterization is removed.

## Novel Insights

None beyond the paper's own contributions. The dual denoising perspective — combining path-level scoring with edge-level rule-based sampling — is the paper's own novel framing, and the reviews do not surface a fundamentally different insight about the work.

## Suggestions

- **Fix Eq. 14** to clearly express the intended entity-level co-occurrence counting. For example:  
  `C(r₁ ⇒ r₂) = |{e ∈ V | ∃x,y: (e,r₁,x) ∈ E ∧ (e,r₂,y) ∈ E}| / |{e ∈ V | ∃x: (e,r₁,x) ∈ E}|`  
  (or the symmetric version for object entities, depending on directionality).

- **Add a brief analysis or case study** showing that the proposed path-aware scoring function (Eq. 10) selects the correct entity in the Fig. 1 example, where simple node-score top-K fails. Even a small illustrative computation would bridge the gap between motivation and method.

- **Report confidence intervals or standard deviations** over at least 3–5 runs for the main results (Table 1) and key ablation studies.

- **Include a sensitivity study** for p_e and p_τ, or at minimum state how they were chosen.

- **Clarify the "remaining path score" construction** (Eq. 8): since there is no explicit v-dependence, the paper should explain more concretely how h_q^{(t)}(u,x) combined with q yields a representation relevant to the future path.

## Score and Decision

This paper addresses a genuine problem in inductive KGC (noise accumulation during multi-hop reasoning) with a well-motivated dual denoising framework. The core technical contributions are sound, the empirical evaluation is reasonably thorough (12 inductive splits, 8 baselines, component-level ablations), and the results are consistently positive. The main weaknesses are (a) imprecise notation in one equation, (b) under-explained approximations in the path-scoring design, and (c) missing experimental rigor elements (confidence intervals, hyperparameter sensitivity). None of these are fatal — they are addressable in revision. The paper represents a solid contribution to the inductive KGC literature.

**Originality:** Moderate. The dual denoising framing is novel, though it builds on established techniques (NBFNet-style path propagation, Adaprop-style sampling, AMIE-style rule confidence).

**Importance of question:** High. Inductive KGC is practically important, and noise management in multi-hop reasoning is a recognized bottleneck.

**Claims support:** Reasonable. Core claims are supported by consistent empirical results and ablations, though the path-scoring justification could be more rigorous.

**Soundness:** Good. The method is well-designed; the one notational issue (Eq. 14) does not undermine the framework.

**Clarity:** Moderate. Generally clear but Eq. 14 is imprecise and some design choices (remaining path score) could use better explanation.

**Value to community:** Moderate. The dual denoising approach and the ablation results are useful reference points for future work.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>