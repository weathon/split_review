- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5
Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

The paper proposes SRank, a reranking strategy for code generation from CodeLLMs that models inter-cluster functional overlap via an interaction matrix **I** (Eq. 1), quantifying the fraction of execution outputs on which two clusters agree. Clusters are formed by grouping solutions with identical execution outputs on model-generated test inputs. The final ranking score is **R = I·V**, where **V** encodes cluster features (size, pass rate). The paper evaluates on HumanEval and MBPP across 9 CodeLLMs (Codex, WizardCoder 15B/34B, StarCoder, CodeGen, etc.) and reports pass@1 improvements over CodeT and Coder-Reviewer.

## Strengths

1. **Novel inter-cluster interaction metric.** The interaction matrix **I** (Section 3.3, Eq. 1) is a principled departure from prior reranking methods that score clusters in isolation. It formalizes the intuition that clusters whose execution outputs agree with many other clusters are more likely to contain correct solutions. The ablation in Table 2 confirms that adding **I** consistently improves performance over using cluster features alone (cluster size, pass rate), validating that the interaction matrix provides non-redundant signal.

2. **Consistent pass@1 gains across a diverse set of 9 CodeLLMs on both HumanEval and MBPP.** The paper evaluates SRank against CodeT and Coder-Reviewer on models ranging from 6B to 34B parameters, including base and instruction-tuned variants (Table 1). The reported average improvement of ≈3.63% over CodeT and ≈8.81% over Coder-Reviewer on HumanEval, with a combined average of ≈6.1%, is backed by per-model numbers cited in the text (e.g., WizardCoder 34B: 75.31% vs Coder-Reviewer's 66.9%; StarCoder: 53.99% vs Coder-Reviewer's 42.44%).

3. **Ablation studies isolate the contribution of the interaction matrix.** Table 2 systematically varies which features (**V**) are combined with **I**, demonstrating that the interaction matrix improves performance regardless of the cluster features used. Figure 4 further shows that **I** systematically raises the rank of valid clusters. This internal validation is the strongest evidence for the paper's core claim.

4. **Demonstrated complementarity with Coder-Reviewer.** Table 3 shows that SRank's interaction matrix can be combined with Coder-Reviewer's likelihood-based scores to improve Coder-Reviewer's own performance (e.g., HumanEval CodeGen 16B: 44.29% → 49.16%). This shows the method is not a standalone replacement but a generalizable technique.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison to AlphaCode — the closest prior method — makes it impossible to isolate the interaction matrix's benefit.** The paper acknowledges AlphaCode (Li et al., 2022) in the Background (Section 2.2) as using the *same clustering approach* (grouping solutions by identical execution outputs on model-generated test inputs) but ranks by cluster size rather than by an interaction matrix. Despite AlphaCode being the most directly relevant baseline for isolating what the interaction matrix adds, it is never compared experimentally. Without this comparison (or an ablation that sets **I = identity**, reducing SRank to a cluster-size-based ranker), a reader cannot tell whether SRank's reported gains come from the interaction matrix or from the underlying clustering itself, which differs from CodeT's clustering-by-passing-test-cases. The paper's core claim is that *inter-cluster modeling* drives improvement, yet the baseline needed to support this claim is absent.

2. **Ambiguous sourcing of baseline numbers undermines experimental credibility.** The paper states (Section 4, Baselines): "We refer directly to the number reported in CodeT and CoderReviewer to compare with SRank." However, CodeT (Chen et al., 2023) and Coder-Reviewer (Zhang et al., 2023) evaluated primarily on Codex and similar early models — they did not evaluate on WizardCoder (released 2023) or StarCoder (released 2023). The implementation details (Section 4) only specify that for Codex and CodeGen the authors use CodeT's artifact, while for "the remaining models" they use HuggingFace. It is unclear whether the Table 1 baseline numbers for these newer models are:
   - (a) numbers taken directly from the original CodeT/Coder-Reviewer papers (which would be impossible for models those papers never evaluated),
   - (b) numbers from a reimplementation by the current authors (which should be explicitly stated and validated against known results), or
   - (c) numbers from some other source.

   The paper must clarify this and, if baselines were reimplemented, validate the reimplementation against reported results on Codex to ensure faithful reproduction. **This ambiguity directly affects the paper's central claim** ("surpass the state-of-the-arts … with significant margin").

3. **No statistical significance or variance reported.** Table 1 reports pass@1 on HumanEval (164 problems) without confidence intervals, error bars, or variance across random seeds. Given the small problem count, a difference of 1–3 percentage points may not be statistically significant (e.g., WizardCoder 34B on MBPP: 51.03% vs 50.3% — a 0.73% gain). The paper should report whether results are averaged over multiple sampling runs and provide confidence intervals or bootstrap estimates.

### Minor

4. **Cluster-to-solution selection rule is unspecified.** When the top-ranked cluster is identified, the paper does not specify how a *single* solution is selected for pass@1 evaluation. All solutions within a cluster produce identical execution outputs (by construction), but they may differ syntactically and could have different pass/fail outcomes on the *hidden* test set. The paper should state the selection rule (e.g., first solution, solution with highest model likelihood, random selection) as this affects reproducibility.

5. **No analysis of generated test input quality.** The interaction matrix and clustering both depend critically on the quality and diversity of the model-generated test inputs **Z**. The paper does not report statistics on how many generated test inputs are valid, discriminative, or diverse across problems. If the test inputs are largely identical or trivial, clusters would collapse and the interaction matrix would carry little signal. This analysis would strengthen confidence in the method's general applicability.

6. **Robustness claim is partially contradicted by the ablation on limited test cases.** The abstract claims "robustness even with limited test inputs," but Figure 3 (and the text, line 163) shows that with few test cases (e.g., 10–20), SRank *with* the interaction matrix can underperform the version *without* it. The paper acknowledges this as a "potential negative impact" but does not investigate when or why this occurs. The robustness claim should be qualified accordingly.

### Trivial

7. **No limitations section.** The paper would benefit from a discussion of failure modes (e.g., when all solutions produce similar outputs despite being incorrect, or when generated test inputs are too few/poor), which is standard practice.

8. **Section numbering inconsistency.** Section 3.1 ("Overview") is followed by Section "2" (line 83) instead of 3.2.

## Nice-to-Haves

- A comparison against a variant of SRank with **I = identity** (i.e., ranking by cluster features alone or by cluster size, as AlphaCode does) would cleanly isolate the interaction matrix's contribution.
- Reporting ablation results for the number of test inputs **M** vs. the number of clusters **K** would clarify the method's behavior.
- Quantitative analysis of within-cluster functional consistency (e.g., percentage of clusters where all solutions pass the hidden test set) would complement the anecdotal case study.

## Removed Points

- **"Interaction matrix is circular because it uses the same execution outputs as clustering"** (Harsh Critic #3): Removed. The interaction matrix measures *inter-cluster* agreement on test inputs, which is a second-order relationship over the clustering output (where each cluster has a unique output vector). This is not circular — it is a refinement. The ablation study (Table 2) empirically confirms it provides non-redundant information. The critic's concern is a reasonable analytical question but the paper already addresses it with evidence.

- **"6.1% improvement claim is misleading"** (Harsh Critic, Abstract/Introduction section): Removed. The paper reports ≈3.63% over CodeT and ≈8.81% over Coder-Reviewer, which average to ≈6.22%. The individual example the critic cites (WizardCoder 34B on MBPP: 51.03% vs 50.3%) concerns a single model-benchmark pair where gains are small, but the *average* claim is about all models combined. The claim is not misleading.

- **"Critique of CodeT is a known limitation"** (Harsh Critic, Background section): Removed. A paper can validly identify a limitation of prior work even if that limitation was acknowledged elsewhere; this does not weaken the current paper.

- **"Hard threshold clustering without discussing noisy test inputs"** (Harsh Critic, Approach section): Removed. Identical-output clustering is standard in this line of work (AlphaCode uses it). The critic's concern about "all identical inputs collapsing clusters" is a speculative edge case without evidence that it occurs in practice.

- **"Case study is anecdotal"** (Harsh Critic, Case Study section): Removed. The case study is presented as illustrative support, not as primary evidence. The paper's main evidence is Table 1 and the ablations.

- **"Strengthening the Paper on Its Own Terms"** (Harsh Critic): These are merged into appropriate weakness/suggestion sections above rather than listed separately.

- **Strength Finder points about "Robustness with limited test cases"**: Weakened to Minor weakness #6 since the paper's own data partially contradicts this claim.

- **Strength Finder point about "Comprehensive evaluation across 9 models"**: Kept as Strength #2, an actual concrete contribution.

- **Strength Finder point about "Case study"** : Removed. The case study is illustrative but not a rigorous strength — it provides anecdotal support at best.

## Novel Insights

The reviews surface an important meta-point: the paper's core contribution (the interaction matrix) addresses a genuine gap in cluster-based reranking — prior methods treat clusters as independent units, losing information about their relative functional relationships. However, the harsh critic's observation that AlphaCode uses identical-output clustering (same as SRank) and differs only in the ranking rule reveals that the paper's experimental design cannot fully isolate the claimed improvement. The interaction matrix is best understood as a *generalization* of cluster-size-based ranking (since if **I** were the identity, **R = V** would rank by cluster features alone). The missing baseline is not just about completeness — it's about whether the paper's single novel component, the interaction matrix, actually drives the reported gains beyond what a trivial baseline of "rank by cluster size, then by pass rate" would achieve. This is the central empirical question that the current evaluation leaves partly unanswered.

## Suggestions

1. **Clearly state how baseline numbers were obtained.** If CodeT and Coder-Reviewer were reimplemented for models they did not originally evaluate (WizardCoder, StarCoder), say so explicitly and validate the reimplementation by reproducing their reported results on Codex.

2. **Include AlphaCode as a baseline**, or equivalently, provide an ablation where SRank sets **I = identity** and **V = [cluster size]** — this would show whether the interaction matrix provides benefit beyond cluster-size-based ranking (which is exactly AlphaCode's approach).

3. **Report confidence intervals or bootstrap estimates** for the main results (Table 1), especially for HumanEval where the problem count is only 164 and small differences may not be significant.

4. **Specify how a single solution is selected** from the top-ranked cluster for pass@1 evaluation.

5. **Add a limitations section** discussing when the method might fail (e.g., all solutions incorrect but producing agreeing outputs; few/discriminative test inputs).
