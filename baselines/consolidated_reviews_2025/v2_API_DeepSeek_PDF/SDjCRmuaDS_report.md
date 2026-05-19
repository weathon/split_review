## Summary
# Final Review Report

## Summary

This paper presents MolMiner, a transformer-based autoregressive model for fragment-based molecular generation. The key idea is to decompose molecules into a sequence of discrete "molecular stories" where fragments (rings and bond units) are added one at a time in a semi-order-agnostic manner, with chemical validity enforced at each step. The model incorporates: (1) a symmetry-aware fragment standardization procedure to avoid vocabulary duplication issues present in prior work like HierVAE, (2) a geometry-aware attention mechanism that biases attention weights by 3D pairwise distances from force-field conformers, and (3) conditional generation guided by multi-target properties (solubility, redox potential, synthetic accessibility). Experiments on the RedDB dataset (12,185 molecules) show that MolMiner achieves 79-86% novelty in generated molecules versus 43-56% for HierVAE, while maintaining comparable calibration accuracy.

The paper addresses a relevant problem and the "molecular story" framing is appealing. However, several weaknesses limit the current version: the novelty claims are insufficiently differentiated from HierVAE, the hyperparameter search is performed on only 1.6% of the dataset, the calibration evaluation uses surrogate model predictions rather than experimental/DFT validation, and the ablation evidence does not isolate the contribution of individual design factors. The geometry awareness — one of the five claimed contributions — yields only a ~1% accuracy gain. Despite these issues, the fragment standardization procedure (resolving symmetry-induced vocabulary duplicates) is a demonstrable technical improvement over prior fragment-based methods.

## Strengths
1. **Well-motivated problem framing.** The paper identifies five concrete design requirements for generative molecular models (multi-step generation, variable size, chemical validity enforcement, coarse-graining, 3D awareness) and correctly notes that no existing method satisfies all five. This framing provides a clear design space for MolMiner.

2. **Elegant symmetry-aware fragment standardization.** The procedure for resolving attachment-point ambiguities in canonical SMILES (Section 2.2) is technically sound. By recognizing that fragments from Algorithm 1 are single-cyclic graphs, the authors exploit the cyclic-permutation property of canonical SMILES to recover the "lost map" between atom indexings. The standardization map that collapses symmetric attachment configurations into a single canonical form is a genuine improvement over HierVAE, where duplicate vocabulary entries exist.

3. **Significant novelty improvement over HierVAE.** The reported novelty ratios (79-86% for MolMiner vs 43-56% for HierVAE on the RedDB dataset) are substantial and consistent across all three property experiments. This is the paper's strongest empirical result.

4. **Transparent generation process.** The "molecular story" concept — building molecules in discrete, chemically validated steps — is a clear and interpretable framework that allows human intervention. The sequential visualization of stories (Figures 5d, 12-33) effectively communicates this transparency.

5. **Well-documented hyperparameter and ablation studies.** The appendix includes a grid search (81 models), geometry ablation on reduced and full datasets, and a comparison of top-k fragment initialization strategies. This level of documentation aids reproducibility.

## Weaknesses
1. **Insufficient evidence for causal attribution of gains (Major).** The Conclusion attributes MolMiner's novelty improvement to three specific factors: semi-order-agnostic decoding, symmetry-aware fragment handling, and 3D geometry. However, no ablation study isolates the contribution of any single factor to the *novelty ratio* (the paper's headline metric). The only controlled ablation (geometry vs. no-geometry, Appendix A.4) measures *reconstruction accuracy*, not novelty, and shows only a ~1% improvement (81.17% vs 80.31% test accuracy). The semi-order-agnostic and symmetry-aware components are never independently ablated. Without such ablations, the attribution is speculative.

2. **Calibration evaluation uses surrogate model predictions as ground truth (Major).** The calibration plots compare prompted properties against *predicted* properties from surrogate models (AqSolPred, QuantumDeepField) — not against experimental measurements or DFT calculations. This means the evaluation measures consistency between the generative model and the surrogate predictor, not actual chemical property control. For out-of-distribution prompts (where both models may share systematic biases), the calibration metrics may be misleading. This is a critical unaddressed caveat.

3. **Hyperparameter optimization on a non-representative sample (Major).** The hyperparameter grid search trained 81 models on only 200 molecules (1.6% of the dataset). The selected configuration (largest embedding size, highest head count, 3 transformer layers) may simply reflect overfitting to a tiny sample rather than optimal performance at scale. No verification experiment on the full dataset comparing alternative hyperparameter configurations is reported beyond the chosen one.

4. **Narrative cohesion and introduction effectiveness (Moderate).** The first Introduction paragraph reads as a dense literature catalog rather than a focused motivation. The five design requirements (A-E) are listed in running text without a systematic comparison of how prior methods fail at the combined challenge. This reduces the perceived strength of the gap analysis.

5. **Novelty boundary with HierVAE is unclear (Moderate).** Several claimed contributions overlap significantly with HierVAE's design (autoregressive fragment-based generation, chemical validity enforcement, coarse-graining). While MolMiner has genuine improvements (symmetry handling, geometry-aware attention), the paper does not crisply delineate what is genuinely new versus an incremental modification. The "single classification task" simplification (C2) is presented as a contribution but no experiment shows it improves over HierVAE's nested classification.

6. **Sample efficiency concern (Moderate).** The authors themselves note that MolMiner is less sample-efficient than HierVAE, requiring more epochs to achieve comparable calibration (Appendix A.7). This trade-off between novelty rate and sample efficiency is acknowledged but not deeply analyzed. For practitioners, this could be a practical disadvantage.

## Key Issues
### Issue 1: Uncontrolled attribution of novelty gains to individual design factors
**Severity: Major | Page 10 - Conclusions**

The Conclusion states that the novelty improvement comes from three factors (semi-order-agnostic decoding, symmetry handling, 3D geometry), but no experiment isolates any factor's contribution to the novelty metric. The geometry ablation (Appendix A.4, Table 3) shows only ~1% reconstruction accuracy improvement on the full dataset, and the "No Geometry" model still achieves 80.31% test accuracy. The sample-efficiency comparison (Appendix A.7) shows MolMiner takes more epochs to reach comparable calibration, suggesting potential confounds in the training procedure that may affect the comparison with HierVAE. **Fix:** Add factor-level ablations measuring each component's impact on novelty ratio, not just reconstruction accuracy.

### Issue 2: Calibration evaluation lacks ground-truth validation
**Severity: Major | Page 9 - Results / Section 3.1**

The calibration experiments evaluate consistency between the generative model and surrogate property predictors (AqSolPred, QuantumDeepField), not against experimental measurements or DFT calculations. The paper claims "the model can effectively bias the generation distribution according to the prompted multi-target objective" (Abstract), but this claim is only validated against computational proxies that may share systematic biases. **Fix:** Explicitly state this caveat, and ideally validate a subset of generated molecules with DFT or known experimental data.

### Issue 3: Hyperparameter selection based on 1.6% of the dataset
**Severity: Major | Page 8 - Results**

The grid search (81 models, 100 epochs each) was conducted on only 200 molecules (100 training + 100 validation). This sample is too small to reliably select architectural hyperparameters (embedding size, heads, layers) for the full 12,185-molecule dataset. The selected configuration is at the upper end of the search space, suggesting the search simply favored larger models. **Fix:** Acknowledge this limitation explicitly and verify the chosen configuration against at least one alternative on the full dataset.

### Issue 4: Geometry contribution is modest and based on approximate conformers
**Severity: Moderate | Page 17 - Appendix A.4**

The geometry-aware attention contributes only ~1% improvement in reconstruction accuracy. Moreover, the 3D coordinates come from classical force-field conformer searches (MMFF94/UFF), which introduce their own approximation errors. The paper does not discuss how sensitive the geometry signal is to conformer quality. **Fix:** Add uncertainty quantification for the geometry benefit and discuss reliance on force-field approximations.

### Issue 5: Introduction and contribution framing lacks focus
**Severity: Moderate | Pages 1-2 - Introduction**

The first Introduction paragraph enumerates many generative model families without establishing a focused motivation. The five design requirements (A-E) are presented as a list rather than as an analytical gap. The contribution list mixes architectural decisions (semi-order-agnostic, single classification) with methodological improvements (symmetry handling) and demonstrations (multi-target inverse design), making it hard to identify the paper's core technical novelty. **Fix:** Restructure the introduction to foreground the symmetry standardization contribution and position the geometry-aware transformer as the secondary contribution.

## Actionable Suggestions
### Suggestion 1 (Must): Add factor-level ablation for novelty ratio
Design three MolMiner variants and compare novelty at 80 training epochs:
- **Variant A (Full MolMiner):** geometry-aware + symmetry-standardized vocabulary + semi-order-agnostic training (current)
- **Variant B (No Geometry):** same as A but without geometry bias in attention (set a=0 fixed)
- **Variant C (No Symmetry Standardization):** same as A but using HierVAE-style fragment vocabulary (with possible duplicates)
- **Variant D (Fixed-Order Only):** same as A but with BFS/DFS fixed story order instead of random queue sampling

Report novelty ratio and calibration error for each variant on the three property experiments. This would disentangle which component drives the novelty improvement. Expected effort: ~2 GPU-days per variant.

### Suggestion 2 (Must): Acknowledge surrogate-model limitation
Add the following caveat to the Results section and the Conclusion:
"We caution that the calibration evaluation compares prompted properties against surrogate model predictions (AqSolPred, QuantumDeepField). These models may share systematic biases, especially for out-of-distribution molecules. Therefore, the calibration results primarily reflect consistency between the generative model and property predictors, not absolute chemical accuracy. Experimental or DFT validation would be needed to confirm true property control."

### Suggestion 3 (Must): Verify hyperparameter choice on full dataset
Train one additional configuration (e.g., fragment embedding 128, attachment 32, 4 heads, 2 layers) on the full dataset for 80 epochs, and report novelty ratio and accuracy. If the smaller configuration performs comparably, the paper's claims about architectural choices need revision. Expected effort: ~1 GPU-day.

### Suggestion 4 (Nice-to-have): Add statistical significance for geometry ablation
Run the geometry vs. no-geometry comparison on the full dataset with 3 random seeds each, reporting mean and standard deviation. This would determine whether the ~1% accuracy difference is statistically significant. Expected effort: ~2 GPU-days.

### Suggestion 5 (Nice-to-have): Quantify HierVAE duplicate vocabulary entries
Measure the percentage of duplicate attachment configurations in HierVAE's vocabulary on the RedDB dataset. Report vocabulary size reduction achieved by MolMiner's standardization map. This would strengthen one of the paper's strongest technical contributions. Expected effort: a few hours of scripting.

### Suggestion 6 (Nice-to-have): Restructure introduction
Replace the current first paragraph with a more focused version (see Storyline Options section for details). Reorganize contribution list to foreground symmetry handling and geometry-aware attention as the primary novelties.

## Storyline Options + Writing Outlines
### Abstract Outline

The current abstract (3-4 sentences) needs a compact 5-sentence structure with explicit quantitative results:

**S1 (Problem):** "Deep generative models for molecular discovery face unique challenges in chemical validity, interpretability, and variable molecular sizes that are often overlooked by methods adapted from NLP and computer vision."

**S2 (Gap):** "Existing fragment-based autoregressive models like HierVAE suffer from redundant fragment vocabularies due to unhandled symmetries and lack 3D geometry awareness, limiting their ability to generate novel valid molecules under multi-objective control."

**S3 (Solution):** "We propose MolMiner, a decoder-only transformer that generates molecules as a sequence of fragment attachment steps ('molecular stories'), with symmetry-aware fragment standardization to eliminate vocabulary redundancy and geometry-biased attention to incorporate 3D spatial structure."

**S4 (Key Results - Insert quantitative claim):** "On the RedDB dataset of 12,185 electroactive organic molecules, MolMiner achieves 79-86% novelty under simultaneous control of solubility, redox potential, and synthetic accessibility, compared to 43-56% for HierVAE."

**S5 (Bounded implication):** "These results demonstrate that symmetry-aware fragment handling and semi-order-agnostic training substantially improve the novelty of conditionally generated molecules while maintaining calibration accuracy for within-distribution prompts."

### Introduction Outline (Paragraph-by-Paragraph)

**Paragraph 1 (P1) - Establish territory and gap (Revised version):**
"Deep generative models have become integral to high-throughput screening for molecular discovery, creating candidate pools conditioned on target properties that are then refined through computational filters. Despite rapid progress across representations (SMILES, graphs, point clouds) and paradigms (VAEs, diffusion, flow matching), critical challenges remain unaddressed simultaneously: chemical validity is often only checked post-generation, molecular size is fixed a priori, the generation process is opaque, 3D geometry is ignored, and coarse molecular structure is not exploited. No existing method simultaneously satisfies all five requirements."

**Paragraph 2 (P2) - Five requirements as a design evaluation (Revised):**
"Table 1 (to be added) summarizes how representative prior methods fare against these five requirements. JTNN and HierVAE satisfy chemical validity enforcement and coarse-graining but lack 3D awareness. Diffusion models enable multi-step generation but fix molecular size and postpone validity checks. MARS and MoLeR handle variable size but ignore coarse molecular structure. A method satisfying all five requirements would enable more flexible, interpretable, and chemically valid inverse design."

**Paragraph 3 (P3) - Our approach:**
"We introduce MolMiner, a decoder-only transformer that grows molecules by sequentially docking molecular fragments — a 'molecular story.' Three design innovations enable simultaneous satisfaction of all five requirements: (1) a symmetry-aware standardization procedure that resolves attachment-point ambiguities present in prior fragment vocabularies, ensuring unique and non-redundant fragment representation; (2) a geometry-biased attention mechanism that incorporates 3D pairwise distances from force-field conformers; and (3) a semi-order-agnostic training procedure that allows the model to learn from diverse story orderings."

**Paragraph 4 (P4) - Contributions (Revised, trimmed):**
"Our core contributions are: (a) a symmetry-aware fragment standardization that eliminates vocabulary duplicates present in HierVAE, producing a compact non-redundant fragment vocabulary; (b) a geometry-aware autoregressive transformer incorporating spatial structure; and (c) demonstration that this combined approach achieves 79-86% novelty in multi-target inverse design on RedDB, substantially outperforming HierVAE (43-56%)."

### Alternative Storyline Candidates

**Candidate A (Current):** Problem background -> Five requirements -> Related work -> Contributions -> Method -> Results -> Conclusion. Weakness: The five requirements list is not used analytically to position MolMiner.

**Candidate B (Preferred - Gap-Driven):** Five requirements as explicit evaluation criteria -> Table showing no prior method meets all five -> MolMiner design to meet all five -> Ablation showing which requirements are hardest to satisfy. This positions the paper as a systematic solution to a known multi-requirement problem rather than a collection of incremental improvements.

**Candidate C (Contribution-Focused):** Lead with the HierVAE vocabulary duplication problem (strongest empirical differentiation) -> Show how this limits novelty -> Introduce symmetry-aware standardization as primary fix -> Position geometry-aware transformer as secondary enhancement. This would better highlight the paper's most novel contribution.

## Priority Revision Plan
The following table lists revision items by priority (P0 = critical for publication, P1 = important, P2 = desirable).

| Priority | Item | Effort | Expected Impact | Annotation Reference |
|----------|------|--------|-----------------|---------------------|
| **P0** | Add factor-level novelty ablation (Variant A/B/C/D) | ~6 GPU-days | Resolves Issue 1 - enables causal attribution of novelty gains | Ann 9 (Page 10 - Conclusions), Ann 10 (Page 17 - Appendix A.4) |
| **P0** | Add caveat about surrogate-model limitation | ~1 hour writing | Resolves Issue 2 - improves scientific honesty | Ann 8 (Page 9 - Results) |
| **P0** | Verify hyperparameter choice with alternative config on full dataset | ~1 GPU-day | Resolves Issue 3 - validates architectural decisions | Ann 7 (Page 8 - Results) |
| **P1** | Restructure introduction (see Storyline Options) | ~3 hours writing | Improves narrative clarity and gap positioning | Ann 2 (Page 1 - Introduction), Ann 3 (Page 2 - Design requirements) |
| **P1** | Run geometry ablation with multiple seeds for significance | ~2 GPU-days | Quantifies uncertainty around geometry contribution | Ann 10 (Page 17) |
| **P2** | Quantify HierVAE duplicate vocabulary entries | ~1 day scripting | Strengthens symmetry-standardization contribution | Ann 12 (Page 17 - Appendix A.5) |
| **P2** | Rephrase Conclusion attribution to remove speculation | ~30 min writing | Aligns claims with available evidence | Ann 9 (Page 10 - Conclusions) |

### Revision Workflow Recommendation

1. **Week 1 (P0 tasks):** Start the factor-level ablation runs (Variants B, C, D) and the alternative hyperparameter verification in parallel. These are the highest-impact and most time-critical experiments.
2. **Week 1 (P0 writing):** Draft the surrogate-model caveat paragraph and insert it into the Results and Conclusion sections.
3. **Week 2 (P1 experiments):** Run multi-seed geometry ablation, analyze results.
4. **Week 2 (P1 writing):** Restructure introduction following the preferred storyline (Candidate B - Gap-Driven).
5. **Week 3 (P2 tasks):** Quantify HierVAE duplicate vocabulary and add to Appendix A.5. Polish Conclusion.
6. **Before resubmission:** Verify that all causal attribution claims in the Conclusion are backed by ablation evidence.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Hyperparameter grid search | 200 molecules, 81 models, 100 epochs | Fragment-level accuracy (train/val) | Best config: 256 frag emb, 64 att emb, 8 heads, 3 layers; 80.93%/80.09% | Architecture choices | Only 1.6% of dataset used |
| E2 | Full-dataset training | 12,185 molecules, best config from E1, 80 epochs | Fragment-level accuracy (train/test) | 81.96%/82.94% accuracy | Model can learn fragment predictions | No alternative config verified |
| E3 | Calibration: log-solubility | Fix redox+SAS at mean, vary solubility, 30 prompts x 30 gens | Prompted vs predicted property; Novelty ratio | MolMiner 79.19% novelty, HierVAE 55.56% | Conditional generation control | Uses surrogate predictions not experiments |
| E4 | Calibration: redox potential | Fix solubility+SAS at mean, vary redox | Same as E3 | MolMiner 85.59% novelty, HierVAE 43.19% | Same as E3 | Same as E3 |
| E5 | Calibration: SAScore | Fix solubility+redox at mean, vary SAS | Same as E3 | MolMiner 85.21% novelty, HierVAE 52.63% | Same as E3 | Same as E3 |
| E6 | Geometry ablation (reduced) | 200 molecules, 10 initializations, 100 epochs | Training/validation accuracy | All initializations ~80% acc; Constant=+1.0 best val | Geometry provides small benefit | Difference too small for conclusions |
| E7 | Geometry ablation (full) | Full dataset, Constant=+1.0 vs No Geometry | Training/testing accuracy | 81.98%/81.17% vs 80.58%/80.31% (~1% gain) | Geometry improves accuracy | No significance test; novelty not measured |
| E8 | Top-k fragment init. analysis | Compare top-1, top-3, top-5 start fragments | SAScore calibration spread | Top-3 and top-5 similar; top-1 worse at extremes | Diversity via top-k sampling | Only tested on SAScore |
| E9 | Sample efficiency (50 epochs) | Same protocol as E3-E5 but at 50 epochs | Novelty ratio + calibration | MolMiner 74-81%, HierVAE 39-59% novelty | MolMiner less sample-efficient | Only two checkpoints tested |

### Research-Theme Gap Diagnosis

1. **Causal attribution gap:** The paper claims three factors drive the novelty improvement, but no experiment tests this claim directly. The only component-level experiment (geometry ablation, E6/E7) measures reconstruction accuracy, not novelty — and shows a marginal effect.

2. **Validation gap:** The calibration experiments measure consistency between generative and surrogate models, not chemical accuracy. For a paper claiming "real world potential," the absence of DFT or experimental validation is a significant gap.

3. **Comparison fairness gap:** The HierVAE baseline is "modified" to enable conditional generation (concatenating conditions to latent vector), but the paper does not analyze whether this modification is optimal, potentially understating HierVAE's conditional generation capability.

### Proposed Research Experiments (P0/P1/P2)

| Priority | Experiment | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Expected Gain |
|----------|------------|-------------|------------|---------------|-------------------|---------|------------------|-----------|---------------|
| **P0** | Factor-level novelty ablation | C1-C3 attribution | Symmetry handling is primary driver; geometry is secondary | Train 4 variants (full, no-geo, no-sym, fixed-order) on full dataset | Full MolMiner as reference | Novelty ratio (%) + calibration error | Identify which variant causes largest novelty drop | ~6 GPU-days | Enables evidence-based attribution in Conclusion |
| **P0** | DFT validation subset | Real-world potential | Novel molecules have properties correlated with prompts | Select 20 novel molecules (5 per prompt range), compute redox + solubility via DFT | Same molecules evaluated by surrogate models | Correlation (R²) between DFT and surrogate predictions | R² > 0.7 for within-distribution prompts | ~2 weeks (DFT) | Validates surrogate reliability or reveals biases |
| **P1** | Multi-seed geometry significance | Geometry contribution | Geometry gain is statistically significant | Run No-Geometry vs Geo-aware with 3 seeds each | Same seeds for both configs | Mean ± std test accuracy | Non-overlapping confidence intervals | ~2 GPU-days | Quantifies uncertainty around geometry benefit |
| **P1** | Optimal HierVAE conditional tuning | Fair comparison | HierVAE conditional generation can be improved | Grid search over condition-concatenation strategies for HierVAE | HierVAE-80epochs as baseline | Novelty ratio + calibration error | Identify if HierVAE's gap narrows with better conditioning | ~1 GPU-day | Ensures fair comparison |
| **P2** | Out-of-distribution novelty analysis | Model generalization | Novel molecules explore undersampled regions | Cluster novel molecules by chemical space; measure distance from training distribution | Training set fragments as reference | Novelty types (valid/novel/unique); chemical diversity | MolMiner explores broader chemical space than HierVAE | ~2 days analysis | Strengthens novelty claim with chemical space analysis |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5/10**

The paper addresses a relevant problem (fragment-based molecular generation) with a technically sound approach (symmetry-aware standardization, geometry-biased attention). The novelty improvement over HierVAE (79-86% vs 43-56%) is substantial and consistent. However, several significant weaknesses prevent a higher score:

- The causal attribution of novelty gains to individual design factors is unsupported by ablation evidence (critical gap)
- The calibration evaluation relies on surrogate model predictions rather than experimental/DFT validation, limiting the strength of "real world potential" claims
- Hyperparameter optimization was conducted on only 1.6% of the dataset
- The geometry awareness contribution appears marginal (~1% accuracy gain) relative to the prominence it receives in contribution claims
- The novelty boundary with HierVAE is not crisply delineated

These issues affect both **research value** (uncertainty about which design choices actually drive improvement) and **validity** (calibration claims are not grounded in experimental measurements). The paper has solid technical foundations but needs additional experiments and more cautious claims to reach its potential.

**Post-Revision Target: [6.5, 7.5]/10**

If the authors complete the P0 items (factor-level ablation, surrogate-model caveat, hyperparameter verification), the paper could reach 6.5-7.5. The upper bound of 7.5 assumes that the factor-level ablation confirms symmetry handling as the primary driver and that the calibration caveat is adequately addressed. Without these additions, the score would remain around 5-6.

**Score Breakdown:**
- Novelty/Significance: 5/10 (solid improvement over HierVAE but incremental over related fragment-based methods; novelty attribution unclear)
- Validity/Soundness: 5/10 (calibration evaluation has unaddressed caveats; hyperparameter search is not representative)
- Reproducibility: 6/10 (good documentation of hyperparameters and ablation details; some key comparisons deferred to appendix)
- Clarity: 6/10 (technical content is clear; introduction and contribution framing need restructuring)
- Overall Evaluation: 5.5/10