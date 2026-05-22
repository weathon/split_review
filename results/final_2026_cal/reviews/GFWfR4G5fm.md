Now I have all the information I need. Let me compose the final review.

## Calibration Summary

**Round 1 — Bracketing:**
- **Low band** (< 3.5): query `supervised causal learning test time training` → anchors at ~3.0 (ADAG paper, rejected). The current paper is substantially stronger.
- **Middle band** (3.5–7.5): queries on causal discovery + test-time adaptation → anchors at 5.0–6.67. Most relevant: "When Shift Happens" (6.00), "Learning Dynamic Causal Graphs" (6.00), "Foundation Models for Causal Inference" (6.67).
- **High band** (> 7.5): quantum computing, rotation estimation — topically irrelevant.

**Initial bracket:** 5.5–7.0

**Round 2 — Narrowing:**
Queried `causal discovery supervised learning real world` (4.5–6.5) and `test time training distribution shift causal graph` (5.5–7.5).
Read full reviews of:
- CausalAffect (5.00, Reject) — fundamental causal framing issues; current paper is clearly stronger
- Learning Dynamic Causal Graphs (6.00, Accept) — single dataset, missing baselines; current paper has more comprehensive evaluation
- Foundation Models for Causal Inference (6.67, Accept) — strong theory but limited real-world validation; current paper has real-world results but less theoretical depth

**Final score:** 6.5. The paper sits between the 6.00 anchors (which had significant weaknesses like single-dataset evaluation or purely theoretical contributions) and the 6.67 anchor (which had strong theoretical grounding but no real-world validation). The current paper offers a genuine methodological contribution with convincing empirical results across synthetic, pseudo-real, and real-world data.

---

## Final Review

## Summary

This paper identifies three fundamental limitations of static pre-training in Supervised Causal Learning (SCL)—fragility to distribution shifts, failure in compositional generalization, and a gap between synthetic and real-world performance—and proposes a Test-Time Training framework (TTT-SCL) to address them. The key technical contribution is an Alignment of Distribution (AD) metric combined with a sparsity constraint to guide a stochastic search over candidate graphs, producing training data tailored to each test instance. The instantiation, TACTIC, achieves strong results on synthetic benchmarks and state-of-the-art performance on the real-world Sachs dataset (78.9 AUROC vs. 62.3 for the best SCL baseline).

## Strengths

1. **Clear empirical diagnosis of three SCL limitations.** Section 3 systematically demonstrates that static SCL models degrade under categorical distribution shifts (Figure 2), cannot compositionally generalize to unseen combinations of seen components (Figure 2, Component-mixed vs. i.i.d.), and exhibit a stark performance collapse from synthetic to real-world data (Table 1: AVICI drops from 97.8 AUROC on RFF_G to 62.3 on Sachs). This goes beyond prior work (Montagna et al., 2024) and provides a compelling motivation for the proposed approach.

2. **Novel TTT-SCL framework with a principled optimization target.** The AD metric (Eq. 3) operationalizes distributional alignment via likelihood under Structure-Induced Mechanisms, and the joint score with sparsity (Eq. 5) enforces causal minimality—a novel combination that distinguishes this work from both static SCL and classical score-based causal discovery.

3. **TACTIC achieves state-of-the-art performance where static SCL fails.** On Sachs (78.9 AUROC) and Syntren (80.1), TACTIC substantially outperforms the best SCL baseline AVICI (62.3 and 65.4, respectively) and also surpasses traditional methods like PC (67.1, 58.1). This directly validates the core thesis that test-time adaptation closes the real-world generalization gap.

4. **Stage-wise analysis isolates the contribution of the SCL phase.** Table 4 shows clear, consistent improvement from the seed graph → highest-scoring search graph → final SCL output (e.g., Chebyshev: 52.2→75.8→83.0). This evidence supports the claim that the SCL model adds value beyond the score-based search, addressing a natural concern about the framework.

5. **Sparsity ablation confirms its necessity.** Table 3 demonstrates that removing the sparsity penalty degrades performance across all settings (e.g., Sachs drops from 78.9 to 63.5), validating the design choice.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Missing variance for real-world results.** Table 2 reports standard deviations for all methods on synthetic data but not for Sachs and Syntren (e.g., TACTIC(Notears) on Sachs: 78.9 with no s.d.). The same issue appears in Table 1. Without variance estimates, the reader cannot assess whether the large reported gaps (e.g., TACTIC 78.9 vs. AVICI 62.3 on Sachs) are statistically reliable or reflect a single favorable run. The authors could report variance by varying the SCL training seed or bootstrapping the test data.

2. **AD metric implementation details are underspecified.** Eq. 3 defines AD as `(1/d) Σ log p(X_i | f_i^k)`, but the paper does not specify (a) the distributional form of the likelihood (implied to be Gaussian but never stated), (b) the regression method used to fit `f_i^k` (linear regression? neural network? Gaussian process?), or (c) whether and how the likelihood is normalized. These details are critical for reproducibility.

3. **The generality claim about identifiability assumptions is unsubstantiated.** The paper states that TTT-SCL "is applicable to any assumption that guarantees the identification of the underlying causal graphs, such as LiNGAM, the nonlinear Additive Noise Model, or the Post-NonLinear model." All experiments use Gaussian or Uniform noise with well-behaved mechanisms (Linear, RFF, Chebyshev). No experiments test non-Gaussian noise, non-additive noise, or scenarios that violate the Gaussian likelihood assumption implicit in the AD metric. The claim should be qualified or supported with additional experiments.

4. **Figure 2 axis labels are unexplained.** The dataset names `RFF_G_62.3`, `RFF_G_97.8`, etc., include numeric suffixes that likely denote graph sparsity or expected edge counts, but this is never clarified in the caption or text. The caption references ER and SF graph types from Section 3.1 but doesn't explain the mapping to the plotted labels.

5. **The SCL improvement mechanism is not analyzed.** Table 4 convincingly shows that the SCL model improves over the highest-scoring graph, but there is no analysis of *what* the SCL model corrects. An edge-level error analysis (e.g., structural Hamming distance or precision/recall breakdown between the highest-scoring graph and the SCL output) would help clarify whether the SCL model is averaging, denoising, or genuinely correcting structural errors.

6. **No direct ablation of the AD term.** The sparsity term is ablated (Table 3), but the AD term is not. A natural control would compare TACTIC's AD-guided search against generating training data from random candidate graphs (without the AD score). While the stage-wise analysis in Table 4 shows that the search guided by AD+sparsity improves over the seed, this does not isolate AD's contribution from sparsity's.

### Trivial
- The acceptance probability formula in Figure 3 uses a ratio `score(G^{k+1})/score(G^k)`. Since AD is a log-likelihood (negative-valued) and sparsity subtracts a penalty, the positivity and proper normalization of the score should be explicitly clarified.
- The proposal distribution for edge additions/deletions/reversals in the stochastic refinement is not described (e.g., uniform over valid changes?).
- No limitations paragraph in the conclusion (computational cost, dependence on regression quality for AD).

## Nice-to-Haves
- A brief runtime analysis showing how TACTIC scales with the number of nodes and samples (the paper references Appendix F, which was stripped).
- Sensitivity analysis for the number of generated training instances (K=200 used throughout).
- An experiment testing TACTIC under non-Gaussian noise or non-additive mechanisms to support the generality claim.

## Removed Points
The harsh critic's claim that "Table 1 reports s.d. for Sachs and Syntren—why not Table 2?" is factually incorrect — Table 1 also does not report standard deviations for Sachs/Syntren. The underlying concern (missing variance) is retained as a Minor weakness, but the specific framing is removed.

The critic's demand for "structural Hamming distance" analysis between the highest-scoring graph and the SCL output is retained as a reasonable suggestion but downgraded from a "Critical Issue" to Minor, since Table 4 already provides substantial evidence of the SCL improvement using a standard metric (AUROC).

Criticisms about missing related work sections, appendix content, or reproducibility concerns that stem from stripped appendix sections are removed per the review guidelines.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Report standard deviations for Sachs and Syntren in Tables 1 and 2 (e.g., by training multiple SCL models with different random seeds or bootstrapping the test data).
2. Explicitly state the likelihood distribution (Gaussian) and regression method used to compute AD.
3. Qualify the generality claim or add experiments under non-Gaussian noise / non-additive mechanisms.
4. Clarify the meaning of the numeric suffixes in Figure 2's axis labels.
5. Add an edge-level error analysis to explain what the SCL phase corrects (precision/recall, Hamming distance to ground truth for highest-score vs. final graph).
6. Add a limitations paragraph to the conclusion discussing computational cost, dependence on regression quality, and scope of validation.

## Score and Decision

| Anchor | Avg Score | Round | Comparison to Current Paper |
|--------|-----------|-------|----------------------------|
| vSAWV43kvs (ADAG) | 3.00 | 1 | Much weaker — fundamental flaws in generalization; current paper is substantially stronger |
| r4BjURAEN2 | 3.00 | 1 | Topically unrelated (latent-confounded shift in fine-tuning) |
| p0kabcRgJZ | 3.00 | 1 | Topically unrelated (robust optimization in causal models) |
| NIA4qmseAd | 2.50 | 1 | Topically unrelated (causal effect estimation) |
| 5d7prMWHNF (Delta Embeddings) | 6.00 | 1 | Comparable score tier; current paper has stronger empirical validation across multiple datasets |
| kEzy6TAV0x (Causal-Adapter) | 5.00 | 1 | Topically unrelated (counterfactual image generation) |
| sFjxg8cyJS (When Shift Happens) | 6.00 | 1,2 | Comparable; that paper is purely theoretical, current paper has a novel method + experiments |
| BhyVA99U4b (DISCO) | 4.50 | 1 | Topically unrelated (bias mitigation) |
| 248ysaRatx | 8.00 | 1 | Topically unrelated (quantum computing) |
| VaS6xcDrTb | 8.50 | 1 | Topically unrelated (rotation estimation) |
| Ahdsg2nkNH | 8.00 | 1 | Topically unrelated (Monte Carlo) |
| DM0Y0oL33T | 8.00 | 1 | Topically unrelated (multimodal reasoning) |
| s0nYSwlV3I | 5.00 | 2 | Weaker — single dataset focus; current paper has broader evaluation |
| PJ29BlwG7w (CausalAffect) | 5.00 | 2 | Weaker — unclear causal framework; current paper has clearer methodology |
| DZjbL9BuHs | 4.67 | 2 | Topically unrelated (RLVR generalization) |
| Pa7oHHhqFa | 5.00 | 2 | Topically related but different approach (LM-based); current paper has cleaner framework |
| 4bnCXOtHTm (Dynamic Causal Graphs) | 6.00 | 2 | Comparable; that paper had single-dataset evaluation, current paper more comprehensive |
| ta8BKRa1bl | 6.00 | 2 | Topically related (identifiability) but different contribution (theoretical) |
| d2L1ndOKjq (CausalFM) | 6.67 | 2 | Slightly stronger overall — strong theory + comprehensive framing, but also lacked real-world validation |

**Round 1 bracket:** 5.5–7.0  
**Round 2 narrowing:** paper sits near the upper end, comparable to or slightly above the 6.00 anchors and below the 6.67 anchor, reflecting a genuine methodological contribution with convincing results but some presentation and validation gaps.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>