Now I have all the information I need. Let me construct the final review after carefully cross-checking all reviewer claims against the paper.

---

## Summary

The paper proposes SRank, a reranking method for code generation that clusters solutions by their execution outputs on model-generated test inputs and then computes an "interaction matrix" quantifying functional overlap between clusters. The final ranking score combines this matrix with cluster-level features (size, pass rate, or Coder-Reviewer scores). The method is evaluated on HumanEval and MBPP across 9 CodeLLMs and compared against CodeT and Coder-Reviewer.

## Strengths

- **Novel inter-cluster modeling via a principled interaction matrix.** The paper introduces a quantitative functional-overlap metric between clusters (Eq. 1, Section 3.3) that captures pairwise output agreement across test inputs. This goes beyond prior work (AlphaCode, CodeT, Coder-Reviewer) that ranks clusters in isolation, and the intuition that incorrect solutions are unlikely to functionally agree (Fischler & Bolles, 1981) is well-motivated.

- **Ablation studies show consistent gains from the interaction matrix.** Table 2 demonstrates that adding the interaction matrix **I** to any cluster feature (cluster sizes, pass rates, or both) improves pass@1. The interaction matrix also boosts Coder-Reviewer scores (Table 3). These controlled comparisons *within the paper's own experimental setup* provide genuine evidence that the inter-cluster modeling contributes positively — independently of the cross-paper comparisons.

- **Evaluation across diverse CodeLLMs (9 models, 6B–34B).** The paper tests on a broader set of models than either CodeT or Coder-Reviewer originally evaluated, including Codex, WizardCoder (15B, 34B), StarCoder, CodeGen, and CodeGen2.5-Instruct, which provides a useful empirical landscape for the community.

- **Qualitative validation of cluster quality.** Figure 5 shows concrete examples where CodeT's clusters contain functionally inconsistent solutions (passing the same test cases but semantically different), while SRank's execution-output-based clustering yields more coherent clusters. This supports the method's design rationale.

- **No additional training required.** SRank operates purely at inference time, requiring only sample execution — a lightweight, general-purpose enhancement that can be plugged into existing pipelines.

## Weaknesses

### Fatal

None.

### Major

- **Unfair baseline comparisons undermine the headline improvement claims.** The paper states (line 118): *"We refer directly to the number reported in CodeT and CoderReviewer to compare with SRank."* For models beyond Codex002 and CodeGen16B (where artifacts from Chen et al. 2023 are used), the baseline numbers were likely obtained under different sampling budgets, temperatures, test-case generation strategies, and post-processing steps. Pass@1 is sensitive to all of these factors. The claimed "≈6.1% improvement on average" and the specific numbers in Table 1 are therefore not credible as direct comparisons — the experimental conditions are not held constant. This is the most significant weakness because it casts doubt on the paper's central comparative claims. The paper cannot convincingly claim to "outperform" CodeT or Coder-Reviewer without apples-to-apples re-implementation under identical settings.

- **Confound between clustering strategy and interaction matrix not fully disentangled.** The paper clusters by *exact execution outputs* on model-generated test inputs, whereas CodeT clusters by *which test cases are passed* (a binary vector). The ablation study (Table 2) shows that adding **I** to cluster-size-based ranking improves performance, but it does not control for whether the benefit comes from richer execution-output clustering (vs. CodeT's pass/fail clustering) or from the interaction term itself. A controlled comparison that holds the clustering algorithm fixed (e.g., CodeT-style pass/fail clustering with and without **I**) would be needed to isolate the contribution of the interaction matrix. Without this, it is unclear how much of the gain is attributable to the claimed novelty.

### Minor

- **Ambiguity in feature combination.** The paper reports using "both" cluster sizes and pass rates (line 147) but never specifies how they are combined into a single scalar per cluster (sum? product? weighted average?). The final score is **R** = **I**·**V** (line 108), and the matrix-vector product is clear from dimensionality, but how **V** is constructed from multiple features is not defined. This hampers exact reproducibility.

- **Overclaim about limited test cases contradicts the paper's own ablation.** The conclusion (line 202) states the method is *"more applicable to realistic scenarios with a limited number of test cases,"* but Section 5.1 acknowledges *"with limited test cases, SRank sometimes underperforms due to each ranking feature's potential negative impact when interaction is considered"* (lines 163–164). The paper also recommends generating at least 30 test cases for optimal results. This overclaim weakens the conclusion's credibility.

- **No variance or confidence estimates.** Pass@1 numbers are reported as point estimates without confidence intervals, standard deviations across seeds, or statistical significance tests. This makes it impossible to assess whether the observed differences (e.g., 51.03% vs. 50.3% on MBPP WizardCoder) are meaningful or within noise. While single-run evaluation is common in this area, the lack of variance estimates is a limitation given the small number of problems in HumanEval (164) and MBPP (~1000).

- **Test-case generation prompt and quality not described.** The prompt used to generate test cases is not provided, and the quality of generated test inputs (coverage, correctness) is not evaluated beyond a scaling ablation on their quantity. This is relevant because poor test inputs degrade clustering quality, as the paper itself notes (line 165).

### Trivial

- **Computational cost of the interaction matrix is not discussed.** Computing **I** requires O(K²M) operations (K clusters, M test inputs), but this is not mentioned. While likely cheap relative to execution, a brief note would be useful for practitioners.

## Nice-to-Haves

- **Experimental comparison with MBR-exec (Shi et al., 2022) and LEVER (Ni et al., 2023).** The paper mentions these methods in Related Work but does not compare against them. While they differ in approach (MBR-exec minimizes a loss; LEVER trains a verifier), they address the same reranking problem. A discussion of why direct comparison is difficult, or even a limited comparison, would better position the contribution.
- **Code release.** Given the complexity of the pipeline (sampling, execution, clustering, matrix computation), releasing code would strengthen reproducibility and impact. (This is a wishlist item, not a weakness of the paper's current content.)

## Removed Points

- **Criticism about "no code or data release."** The paper does not mention code release, but this is not a standard critique of a submission; code is typically released upon acceptance. The point is moved here because it speculates on what the authors *will* release rather than evaluating what the paper *does* present.
- **"The interaction matrix could be replaced by a simpler centroid-based measure."** This is speculative and not a weakness of the method as presented. The paper's choice of a pairwise matrix is defensible and the reviewer provides no evidence that a simpler measure would work as well.
- **"Missing related work" on MBR-exec/LEVER.** The paper *does* discuss both methods in Section 6 (line 193). The reviewer's criticism about experimental comparison is addressed above in Nice-to-Haves; the claim that the paper fails to cite or discuss them is factually wrong.
- **Various formatting/typo nitpicks** (e.g., "ALATION STUDY" for "ABLATION STUDY", "MPPS" for "MBPP"). These are parser artifacts, not author errors.
- **"Cannot be independently verified" framing of the baseline issue.** The reviewer's substantive point (unfair comparisons) is kept as a Major weakness. The language about "cannot be independently verified" is removed because it implies the cited baselines don't exist, which violates the hard rule.
- **"The paper does not report reproducing CodeT or Coder-Reviewer under its own settings."** The paper states it uses CodeT's artifacts for Codex002 and CodeGen16B (lines 122–123). For other models, the criticism is valid and subsumed in the Major weakness above.

## Novel Insights

The reviews align on the paper's core weakness: the comparative claims against CodeT and Coder-Reviewer are untrustworthy because the baselines are drawn from published numbers under unknown, likely mismatched conditions. However, an interesting nuance emerges that neither reviewer fully articulates: the paper's *internal* ablation evidence (Table 2, Table 3, Figure 3, Figure 4) demonstrates that the interaction matrix provides consistent improvements over not using it, *independent* of the flawed cross-paper comparisons. This means the paper has a credible methodological contribution (the interaction matrix helps) sitting beneath a weak experimental presentation (the headline numbers are overclaimed). The paper would be stronger if it reframed its contribution around the within-pipeline controlled comparisons and de-emphasized the cross-paper absolute numbers.

## Suggestions

1. **Re-run CodeT and Coder-Reviewer under identical conditions** (same N=100 samples, same temperature, same test-case generation prompt, same post-processing) for all CodeLLMs. Report apples-to-apples comparisons. Without this, the headline improvement claims should be withdrawn or heavily caveated.

2. **Disentangle clustering from ranking.** Add an ablation comparing "cluster by execution outputs + rank by cluster size" vs. "cluster by passed test cases (CodeT-style) + rank by cluster size" vs. the same with **I**. This would isolate whether the interaction matrix itself drives the gains.

3. **Specify how "both" features are combined** into the validation vector **V**. Clarify whether features are normalized, weighted, summed, or multiplied.

4. **Tone down the overclaim about limited test cases.** Acknowledge directly that SRank can underperform with very few test cases and state the minimum recommended number more clearly.

5. **Add confidence intervals** (e.g., bootstrap over problems) for pass@1 estimates, or at minimum note the lack as a limitation.

## Score and Decision

**Originality:** The interaction matrix is a novel addition to the standard cluster-then-rank paradigm for code generation. The idea of measuring inter-cluster functional overlap is not present in CodeT, Coder-Reviewer, or AlphaCode.

**Importance of research question:** Reranking sampled solutions is a practically important problem in code generation. Better selection strategies directly improve usability.

**Claims support:** The core claim that the interaction matrix helps is supported by the internal ablations. However, the headline claim of outperforming CodeT and Coder-Reviewer is not supported due to the unfair baseline comparison.

**Soundness of experiments:** Weakened by the baseline comparison issue. Internal ablations are reasonably sound. The ablation missing the clustering-strategy control is a gap.

**Clarity of writing:** Generally clear. The method description is mostly well-specified, with the ambiguity about "both" feature combination being the main gap.

**Value to community:** Moderate. If the baseline issue is fixed, the interaction matrix is a useful addition to the reranking toolkit.

The paper has a genuine methodological contribution that is supported by internal evidence, but the experimental evaluation as presented is compromised by the unfair baseline comparisons. The weaknesses are fixable — the paper would become a solid contribution with proper re-evaluation of baselines. In its current form, the paper overclaims relative to the evidence.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>