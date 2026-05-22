Now let me write the final consolidated review.

## Summary

CausalNovo is a model-agnostic framework that applies structural causal model (SCM) reasoning to de novo peptide sequencing. It introduces a Causality Extraction Module (CEM) that disentangles causal (signal ion) from non-causal (noise ion) representations using importance-score-based soft masking, trained with objectives derived from independence and sufficiency principles. The framework is applied to three baselines (CasaNovo, AdaNovo, π-HelixNovo) and evaluated on three benchmark datasets, showing consistent improvements and improved robustness to noise perturbations.

## Strengths

- **Comprehensive, consistent experimental gains across diverse baselines and metrics.** CausalNovo improves amino acid precision by +2.2% to +14.2% and peptide precision by +3.5% to +13.0% across three architecturally distinct baselines and three datasets (Table 1). PTM-level gains are also consistent (Table 2). This breadth of evaluation makes a strong empirical case.

- **Demonstrated noise robustness through multiple complementary analyses.** Figures 1 and 3 show CausalNovo-augmented models degrade far less under noise peak replacement (average +14.9% relative improvement on HC-PT). Figure 4 shows consistent gains across varying noise-signal ratios. Cross-species validation (Table 3) demonstrates transferability. These collectively support the practical value of the framework beyond standard accuracy metrics.

- **Model-agnostic design with plug-and-play capability.** CausalNovo integrates into three different architectures (CasaNovo's Transformer encoder-decoder, AdaNovo's conditional mutual information training, π-HelixNovo's spectrum augmentation) without modifying base architectures (Section 3.3, Figure 2B). The consistent improvements across all three demonstrate genuine architectural independence.

- **Granular ablation isolating each component.** Table 4 shows incremental gains from independence (+1.2%), purification (+0.8%), and symmetric training (+0.4%). Table 5 ablates causal intervention components, showing replace+enhance is superior to random dropping. This granularity helps readers understand what drives improvements.

- **Interpretability evidence via attention analysis.** Table 7 shows CausalNovo reduces predictions with zero causal peaks among top-3 attended peaks from 12.73% to 10.76% and triples the fraction attending to all three causal peaks (19.26% → 32.87%), providing mechanistic evidence that the intervention redirects attention toward signal ions.

## Weaknesses

### Fatal

None.

### Major

- **Missing ablation that isolates the causal framing from standard training techniques.** The paper's central claim is that a *causal* framework drives improvements. However, the "causal intervention" (replacing noise peaks with other noise peaks + adding theoretical spectrum peaks) and the training objectives (contrastive invariance loss + cross-entropy on both causal and non-causal heads) have well-known non-causal analogues: random augmentation, contrastive invariance training, and auxiliary prediction heads. Tables 4 and 5 ablate components of the *causal* framework against no framework, but there is no experiment that replaces the causal noise identification (using theoretical spectrum) with a standard non-causal perturbation (e.g., random peak corruption) while keeping the same contrastive and auxiliary training machinery. Without this ablation, the reader cannot determine whether the SCM framing provides genuine insight or serves as a motivated wrapper around techniques that would work equally well without the causal vocabulary. This is the gap that most directly challenges the paper's claimed contribution. (Harsh critic §1, verified: no such ablation exists in the paper.)

- **The purification mechanism is asserted without empirical or theoretical support.** The paper claims that maximizing I(z_s; Y) "indirectly leads to the purification of z_c" (Section 3.3). This is the key intuition justifying the auxiliary cross-entropy loss on the non-causal head. However, there is no empirical measurement of what information z_s actually contains after training, no metric tracking z_c's "purity," and no theoretical argument with clear conditions under which purification occurs. The cross-entropy loss on z_s could equally mean the model learns to exploit noise patterns for prediction—directly contradicting the stated goal. A diagnostic experiment measuring mutual information between z_s and Y over training, or verifying that z_c becomes more informative and z_s less informative, would substantially strengthen this claim.

### Minor

- **Data leakage concern from injecting theoretical spectrum peaks.** When x_theory peaks are added to create x_intervene (Section 3.4.1), the encoder sees peaks that exactly match the ground truth signal. This injects ground truth information into training. While the ablation in Table 5 shows the "Enhance" component contributes only marginally (+0.6% amino acid precision), the paper should discuss this concern more explicitly—the model is partly learning from its answer.

- **Retrained baseline fidelity is inconsistent.** The retrained CasaNovo improves from 0.697 to 0.741 on Nine-species amino acid precision, while retrained AdaNovo *drops* from 0.698 to 0.681 (Table 1). This inconsistency complicates interpretation of relative gains. CausalNovo still substantially outperforms the original reported baselines, mitigating this concern, but the authors should discuss potential causes (different training sensitivity, hyperparameter mismatch).

- **Missing analysis of imperfect theoretical spectra.** The framework relies on theoretical spectrum accuracy to distinguish causal from non-causal peaks. When PTMs or unusual fragment ions cause the theoretical spectrum to mislabel signal peaks as noise, the framework's foundation degrades. This is particularly relevant given the paper's emphasis on PTM identification (Table 2), and should be acknowledged.

- **Key hyperparameters are not discussed.** The replacement fraction α (controlling intervention strength), the contrastive temperature τ = 0.1, and the number of added CEM parameters (3 Transformer layers + MLP) are either not reported or set without sensitivity analysis. For a "model-agnostic" framework, parameter overhead and hyperparameter sensitivity matter for adoption.

### Trivial

- The abstract claims "up to 10%" improvements; most gains are 2–6%, with 10%+ occurring mainly on the hardest dataset (HC-PT) for select metrics. This slightly overstates typical gains.

## Nice-to-Haves

- A "de-causaled" ablation: implement the same augmentation and contrastive framework but replace causal noise identification with random peak corruption. If CausalNovo still wins, the causal framing earns its keep definitively.

- Diagnostic experiments showing (a) mutual information between z_s and Y drops over training, (b) learned importance scores M correlate with known signal peaks, and (c) z_c is more transferable across datasets than the full representation z.

- A brief theoretical proposition showing under what conditions the contrastive loss bounds the deviation from independence, connecting Eq. 5 to the independence principle more formally.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The causal framework's distinct contribution is not established"** — This was framed as "structural" by the harsh critic but is actually a legitimate concern. Retained as a Major weakness above rather than removed, as it is the most important substantive criticism.

- **"The SCM assumption C ⊥ S is imposed by fiat"** — The paper explicitly derives the SCM from Reichenbach's Common Cause Principle (Section 3.2) and the independence is a structural assumption of the model. While real spectra may violate strict independence, this is a modeling assumption common to causal frameworks, not a flaw unique to this paper. Demoted to nice-to-have.

- **"The disentanglement mechanism is not particularly novel"** — Similar sigmoid-gated importance score mechanisms exist in attention-based methods, but the novelty claim is about the causal framework and training objectives, not the masking mechanism itself. This is a category-driven sweep rather than a specific identified problem.

- **Missing related works** — Per hard rules, not included.

- **Reproducibility concerns about model/dataset existence** — Per hard rules, not included.

- **Formatting/style nitpicks** — Per hard rules, not included.

## Novel Insights

The paper's genuinely novel observation is that existing de novo peptide sequencing models are demonstrably vulnerable to noise peak perturbation (Figures 1 and 3), and that this vulnerability can be systematically reduced through a causality-informed training framework. The vulnerability analysis methodology—systematically replacing noise peaks at varying thresholds and measuring degradation—is itself a useful contribution for evaluating robustness in proteomics models, independent of the causal framework's theoretical merits.

## Suggestions

1. **Add the de-causal ablation.** Implement CEM with random noise augmentation (replacing random peaks regardless of theoretical spectrum) + the same contrastive loss + auxiliary head. If CausalNovo outperforms this, the causal story is validated. This single experiment would address the most consequential criticism.

2. **Add purification diagnostics.** Plot the average cross-entropy loss on z_s and z_c over training epochs. If z_s's loss increases while z_c's decreases, this supports the purification claim empirically.

3. **Report CEM parameter count and α sensitivity.** A brief table showing performance vs. α ∈ {0.1, 0.2, 0.3, 0.5} and the total parameter overhead would help practitioners adopt the framework.

---

## Calibration Report

**Round 1 anchors (bracketing):**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Causal Structure Learning (AvXrppAS2o) | 3.0 | 1 | Weak causal framework paper with limited validation; CausalNovo is substantially stronger |
| Sparse Causal Model (fSxiromxAq) | 3.0 | 1 | Weak causal discovery paper; CausalNovo is far more rigorous |
| RankNovo (87B3zDRMjv) | 5.5 | 1 | Same domain (de novo sequencing reranking); CausalNovo has more thorough evaluation (3 baselines, robustness analysis, cross-species) |
| ReNovo (uQnvYP7yX9) | 6.5 | 1 | Same domain (retrieval-based de novo sequencing); comparable rigor but different contribution type |
| Cross-Entropy Is All You Need (hrqNOxpItr) | 8.0 | 1 | Strong theoretical causal representation learning; CausalNovo is less theoretically deep |
| CwA Multi-View (fPYJVMBuEc) | 6.0 | 2 | Model-agnostic contrastive framework; CausalNovo has clearer motivation and more consistent gains |
| ΔΔG Predictor (IxmWIkcKs5) | 6.75 | 2 | Robustness framework in biology with ablations; comparable rigor |
| Beyond Sequence RNA (9htTvHkUhh) | 6.33 | 2 | Systematic evaluation framework in computational biology; CausalNovo has broader evaluation |

**Round 1 bracket:** 5.5 to 7.0. CausalNovo is clearly stronger than RankNovo (5.5) due to more thorough evaluation and model-agnostic design, but faces the unresolved question of whether the causal framing adds value beyond standard augmentation.

**Round 2 narrowing:** Anchors in the 5.5–6.8 range confirmed that CausalNovo's experimental breadth (3 baselines × 3 datasets × multiple analysis types) places it above 6.0 anchors like CwA, but the missing de-causal ablation prevents it from reaching the 6.75+ range where contributions have cleaner validation.

**Final positioning:** The paper is solidly in the 6.0–6.5 range. The experimental work is extensive and consistently positive, the model-agnostic design is valuable, and the robustness analyses are compelling. However, the core causal claim—that the SCM framing drives improvements rather than the underlying training mechanisms—is not conclusively validated. The missing ablation is the single most important thing the authors can address. I score 6.0, below ReNovo (6.5, which has a cleaner methodological claim validated by its experiments) and above RankNovo (5.5, which has weaker evaluation).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>