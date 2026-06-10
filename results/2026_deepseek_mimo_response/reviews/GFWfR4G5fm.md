Now I have strong calibration data. Let me compare:

**Against TICL (5.5, rejected)**: Very similar topic (TTT+SCL). TICL got dinged for confused presentation, too many contributions, only semi-synthetic experiments. Our paper has cleaner focus, better real-world results, clearer framework.

**Against Zero-Shot Learning of Causal Models (6.25, rejected)**: More theoretical novelty but limited scalability, strong assumptions. Our paper has stronger empirical validation and real-world results.

**Against Out-of-Variable Generalisation (6.75, accepted)**: More theoretically novel but limited experiments. Our paper is more empirically complete but less theoretically deep.

**Against CausalRivers (7.33, accepted)**: Different kind of contribution (benchmarking), but shows what a strong causal discovery paper looks like at 7+.

My initial bracket was 6.0-7.0. The paper is clearly better than TICL (5.5) and comparable to or better than Zero-Shot (6.25), but probably not as novel as OOV (6.75). The paper's strength is its complete empirical story (three limitations + TACTIC + real-world results), but its weakness is the missing mechanism explanation for the SCL uplift.

I'll finalize at 6.5 — comparable to Zero-Shot but with better empirical validation.

Let me now write the final review and assign the score.


Now I have solid calibration data. Let me synthesize everything into the final review.

**Round 1 bracket**: Between 5.0 (rejected "Demystifying amortized causal discovery" — bivariate only, limited scope) and 7.33 (accepted "CausalRivers" — comprehensive benchmarking). The paper clearly outperforms the 5.0–5.5 anchors (TICL, "Demystifying") which were rejected for limited scope/presentation issues, and is comparable to "Zero-Shot Learning of Causal Models" (6.25, rejected) and "OOV Generalisation" (6.75, accepted).

**Round 2 narrowing**: Comparing against TICL (5.5, very similar topic but rejected) and OOV (6.75, accepted, more theoretical), I place this paper at 6.5 — it has cleaner focus and stronger real-world results than TICL, and more complete empirical validation than OOV, though less theoretical novelty.

**Final score**: 6.5.

---

## Summary
This paper introduces TTT-SCL (Test-Time Training for Supervised Causal Learning), a framework that dynamically generates training data aligned with each test instance at inference time, replacing the static pre-training paradigm of SCL. The concrete instantiation, TACTIC, performs stochastic graph search optimizing an Alignment of Distribution (AD) metric and a sparsity constraint to find high-quality candidate causal graphs, generates synthetic training data via Structure-Induced Mechanism (SIM), trains an SCL model, and predicts the test graph. The paper also provides a systematic diagnosis of three limitations of existing SCL: fragility to distribution shifts, failure of compositional generalization, and a synthetic-to-real generalization gap.

## Strengths
- **Well-designed diagnostic experiments exposing SCL limitations**: The compositional generalization experiment (Section 3.1) is carefully constructed — training contains all individual components seen in isolation but excludes test-time combinations. Figure 2 shows consistent AUROC drops from "i.i.d" to "Component-mixed" across all six settings (e.g., RFF_G drops from 100 to 91, Chebyshev_G from 93 to 83), providing concrete evidence that SCL models memorize configurations rather than learning modular causal representations.
- **Two-stage improvement clearly demonstrated via stage-wise analysis**: Table 4 shows meaningful gains at both stages: seed → highest-score graph (search improvement, e.g., RFF_G: 80.5→88.9) and highest-score graph → final SCL output (learning improvement, e.g., RFF_G: 88.9→91.8, Sachs: 66.6→78.9). This is the paper's key empirical evidence that the SCL phase adds genuine value.
- **Substantial real-world and pseudo-real dataset improvements**: TACTIC (Notears) achieves AUROC of 78.9 on Sachs (vs. 62.3 for AVICI, 67.1 for PC) and 80.1 on SynTREn (vs. 65.4 for AVICI) — the largest margins over all baselines.
- **Sparsity ablation validates design necessity**: Table 3 shows removing the sparsity penalty (TACTIC Notears-s) causes consistent performance drops (Chebyshev_G: 83.0→69.7, Sachs: 78.9→63.5), confirming that AD alone produces degenerate dense solutions.

## Weaknesses

### Fatal
None

### Major
- **Unexplained mechanism for SCL uplift over best search result**: Table 4 shows the SCL phase adds ~3–12 AUROC points over the highest-score graph found during search. This is the paper's central evidence that TTT-SCL adds value beyond score-based causal discovery. However, the paper never explains *why* training an SCL model on data generated from multiple candidate graphs (all optimized to match D_test) produces better predictions than any single candidate — is it an ensemble/averaging effect, error correction, or inductive bias? The paper states the two-stage process "constitutes the fundamental distinction between TACTIC and classical score-based causal discovery" (Section 4.4), but this describes the pipeline without explaining the mechanism. A targeted analysis (e.g., error correction patterns, comparison against graph-averaging) would significantly strengthen the paper's core claim.
- **Key hyperparameters λ and K are not specified or ablated**: The sparsity weight λ in Eq. 5 is described only as "a hyperparameter balancing the trade-off" (line 166). Its value is never stated in the main text, and there is no sensitivity analysis. Similarly, K=200 is stated but never ablated. The paper's own Table 3 ablates λ=0 vs. the full method — extending this to show a sensitivity curve would be natural and important for reproducibility and practical guidance.

### Minor
- **Sachs and SynTREn lack standard deviations in Tables 2 and 3**: While synthetic datasets report standard deviations (e.g., "91.8 (3.1)"), Sachs and SynTREn entries are bare numbers (e.g., "78.9", "80.1"). This is consistent across all methods and likely reflects the single-instance nature of these datasets, but the paper should explicitly state the evaluation protocol (single run? random splits?).
- **SynTREn missing from stage-wise analysis**: Table 4 covers only 4 of 5 test domains, omitting SynTREn despite it being one of TACTIC's strongest results (80.1 vs. 65.4 for AVICI). Including it would strengthen the evidence.
- **Noise distribution assumption unexplored**: TACTIC sets noise to N(0,1) by default when generating training data (Section 4.2, step 3), without justification or ablation. For test instances where the true noise is non-Gaussian (e.g., Uniform in Linear_U settings), this creates a systematic mismatch. The paper does not discuss this.

### Trivial
None

## Nice-to-Haves
- A comparison against simply using the highest-scoring graph from TACTIC search as the final prediction, or averaging predictions from the K candidate graphs, would isolate the SCL model's contribution more clearly from the search contribution.
- Brief wall-clock time comparison in the main text would help practical assessment (complexity analysis is in Appendix F).
- Discussion of scalability to higher dimensions (d >> 20).

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Unfair comparison with AVICI"**: The harsh critic claims comparing TACTIC (test-time adapted) vs AVICI (scm-v0, static) is unfair. However, this comparison IS the paper's thesis — the paper argues that static pre-training is fundamentally limited. Comparing against the strongest static SCL baseline is the correct experimental design.
- **"Circularity as a fatal flaw"**: The critic frames the test→train→test pipeline as circular. While the circularity is inherent to TTT-SCL, it's a feature of the paradigm (analogous to TTA in general ML), not a bug. Table 4 provides empirical evidence that the SCL phase adds genuine value. The concern about unexplained mechanism is retained as a Major weakness.
- **"Computational cost completely undiscussed"**: The paper explicitly references Appendix F for complexity analysis (line 176). Appendix content exists in the original submission.
- **"Section 3 Issue 3 overclaims from Sachs"**: The critic says the Sachs comparison is too limited. However, Table 1 also includes SynTREn showing a consistent pattern.
- **"Stochastic refinement lacks specificity"**: The critic asks about the MH ratio. Figure 3 explicitly shows α = min[1, score(G_{k+1})/score(G_k)], which is a standard MH ratio — the paper addresses this.

## Novel Insights
The paper's genuinely novel contribution is the compositional generalization failure diagnosis for SCL (Issue 2): SCL models fail on novel *combinations* of individually-seen components, revealing that static pre-training cannot overcome combinatorial explosion. This is a stronger finding than simply showing distribution shift sensitivity (Issue 1). The TTT-SCL framework itself is a clean conceptual contribution, and the two-stage improvement pattern in Table 4 provides the key empirical evidence that generating aligned training data and training an SCL model adds value beyond simply using the best graph from search — though the mechanism remains unexplained.

## Suggestions
- Add a targeted analysis explaining WHY the SCL learning stage improves over the highest-score graph: compare against graph-averaging or ensemble baselines, and examine whether the SCL model corrects specific edge error types.
- Report the value of λ used and add a sensitivity plot showing AUROC vs. λ across datasets.
- Include SynTREn in Table 4's stage-wise analysis.
- Briefly justify the N(0,1) noise default and assess sensitivity to this choice.

## Reporting — Calibration Anchors

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Demystifying amortized causal discovery | lQYi2zeDyh.md | 5.00 | 1 | Bivariate only, limited scope — paper under review is more complete |
| Test-Time Learning of Causal Structure (TICL) | ZXs3pkmrRG.md | 5.50 | 2 | Very similar topic (TTT+SCL), rejected for confusion/limited experiments — paper under review has cleaner focus and real-world results |
| Robust agents learn causal world models | pOoKI3ouv1.md | 5.75 | 1 | Mainly theoretical contribution, high reviewer variance — paper under review is more empirical |
| Zero-Shot Learning of Causal Models | x3F8oPxKV2.md | 6.25 | 2 | More theoretical novelty but weaker real-world validation — paper under review has stronger empirical story |
| OOV Generalisation for Discriminative Models | zwMfg9PfPs.md | 6.75 | 1 | Novel problem + theory, limited experiments — paper under review has better experiments but less theoretical depth |
| Causal Modelling Agents | pAoqRlTBtY.md | 6.25 | 2 | LLM+DSCM framework for causal discovery, similar novelty level |
| CausalTime benchmarking | iad1yyyGme.md | 6.75 | 2 | Benchmarking contribution, different type of work |
| CausalRivers benchmarking | wmV4cIbgl6.md | 7.33 | 2 | Strong comprehensive benchmark — paper under review is less comprehensive but proposes a method |
| Zero-Shot Learning of Causal Models (R1) | x3F8oPxKV2.md | 8.00 | 2 | One reviewer gave high marks for novelty but overall rejected |
| Selection meets Intervention | xByvdb3DCm.md | 8.00 | 1 | More impactful, all 8s — paper under review is not at this level |
| Test-time Adaptation multi-modal | TPZRq4FALB.md | 8.00 | 1 | Mature TTA contribution — paper under review has comparable novelty in causal domain |

Round 1 bracket: 5.0–7.5. Round 2 narrowed to 6.0–7.0. The paper is clearly stronger than the rejected 5.0–5.5 anchors (TICL, Demystifying) due to cleaner contributions, complete real-world validation, and the three-issue SCL diagnosis. It is comparable to Zero-Shot (6.25) and OOV (6.75) but has stronger empirical validation at the cost of less theoretical novelty. Final score: 6.5.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>