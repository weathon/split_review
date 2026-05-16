Now I have a thorough understanding of the paper. Let me compile the review.

## Final Consolidated Review

## Summary
This paper proposes Causal Differential Networks (CDN), a method that decouples causal graph inference from intervention target prediction. It first uses a pretrained amortized causal discovery model (SEA) to independently featurize observational and interventional transcriptomics datasets into paired graph representations, then trains an axial-attention classifier to predict which genes were intervened upon. CDN achieves state-of-the-art perturbation target prediction across five Perturb-seq and two Sci-Plex datasets without using any external domain knowledge, and outperforms six causal discovery algorithms on synthetic benchmarks while running orders of magnitude faster.

## Strengths
1. **Novel decoupled architecture that directly addresses scalability limitations of joint causal discovery.** By separating causal graph featurization (via a frozen pretrained module) from target classification (via a learned axial-attention network), CDN avoids the combinatorial joint search over graphs and intervention targets that makes prior causal discovery algorithms intractable on transcriptomic data (thousands of variables). This is a principled and practical design choice.

2. **Strong and consistent empirical results on real biological benchmarks without domain knowledge.** On five Perturb-seq and two Sci-Plex datasets, CDN outperforms all baselines (GEARS, GenePT, PDGrapher, Linear, MLP) across the majority of settings, including both seen and unseen cell lines, while using *no external knowledge*. This is noteworthy because all baselines incorporate domain knowledge (gene ontologies, language embeddings, protein interaction networks), yet CDN achieves better target prediction from the data alone.

3. **Ablation cleanly demonstrates that graph-level features are necessary for soft interventions.** When the axial-attention differential network is replaced with a per-node MLP, performance on hard interventions remains high but drops significantly on soft interventions (e.g., mAP from 0.88 to 0.77 in the nonlinear setting). This directly validates the core design claim: graph-level (as opposed to node-level) features are needed for the more realistic soft-intervention setting.

4. **Dramatic scalability advantage over existing causal discovery methods.** CDN runs in seconds on synthetic benchmarks where DCDI and BaCaDI require hours on only 10–20 variables. This is a crucial engineering contribution—it makes causally-informed target prediction feasible at the scale of modern transcriptomics.

## Weaknesses
### Fatal
None.

### Major
1. **The causal featurizer is accepted largely on faith rather than validated on real data.** The core of the method is a pretrained amortized causal discovery model (SEA) that was trained exclusively on synthetic Erdős–Rényi graphs. Its features are presumed to capture meaningful causal structure, yet the paper provides no direct evidence that the inferred graph features correspond to actual causal relationships in real biological data. The authors acknowledge this ("we cannot 'prove' that a pretrained model extracts correct graphs on real data, as the true graphs are unknown"), and the strong downstream task performance provides indirect support. However, this remains a structural concern: without diagnostic experiments (e.g., stability across bootstrap samples, negative controls using random splits of control cells, or checks that predicted graph differences cluster by known biological pathways), it is unclear whether CDN's success arises from causal reasoning or from statistical shortcuts in the data that happen to correlate with intervention targets. The synthetic ablation already shows that on *hard* interventions, an MLP without any graph information achieves near-perfect performance—suggesting that strong performance does not automatically imply meaningful causal reasoning.

### Minor
2. **Training procedure on real data is underspecified.** The paper states that on real data, training starts from the synthetic checkpoint with batch size 2 and learning rate 1e-5, but it does not describe how individual training examples are constructed from the real datasets. Are all control cells shared across perturbations from the same cell line? How exactly is each (control, perturbed) pair formed? The filter to top-1000 differentially expressed genes per perturbation is described, but the mapping from raw data to training instances is not. This makes the work harder to reproduce and assess for potential data leakage.

3. **Baseline comparisons are confounded by multiple asymmetries that are acknowledged but not analyzed.** CDN is trained across many perturbations (often across multiple cell lines) on the target-prediction task directly, while baselines like GEARS predict expression (not targets) and GenePT uses a per-cell-line logistic regression with fewer labeled examples. Conversely, baselines use domain knowledge that CDN does not. The paper acknowledges the domain-knowledge asymmetry but does not discuss the supervision asymmetry—the fact that CDN sees far more supervised examples from related perturbations. A controlled experiment (e.g., training CDN on the same per-cell-line data as GenePT/GEARS) would clarify how much of the gap comes from the architecture versus from access to more training data.

4. **Synthetic evaluation is limited to very small graphs (N=10, 20).** While this is partly dictated by the intractability of competing causal discovery algorithms on larger graphs, synthetic experiments with larger N (e.g., 100, 500) using only CDN (and perhaps DCI) would better demonstrate scalability and robustness to graph sizes closer to the transcriptomics setting. The paper could also test robustness to non-Erdős–Rényi topologies (scale-free, hub-like) that better resemble biological networks.

5. **No confidence intervals or statistical tests for real-data metrics.** Given variance across perturbations and cell lines, reporting standard errors, bootstrapped intervals, or significance tests would help assess whether the reported improvements over baselines are robust.

### Trivial
6. The paper does not report how many perturbations were excluded by the ≥10 DE genes filter per dataset, nor whether all baselines were evaluated on the same filtered subset.

7. The informal claims in the theoretical context section (Section 3.4) add little to the paper and could be moved to an appendix.

## Nice-to-Haves
- A negative control experiment: apply CDN to a pair of control-split datasets (no real perturbation) to verify that the model does not predict spurious targets (i.e., that the false positive rate is well-calibrated).
- Larger-scale synthetic experiments (N=100–500) using only CDN and DCI to demonstrate scaling behavior.
- An ablation training CDN on a single cell line at a time to match the per-cell-line training setup of baselines like GenePT and GEARS, to isolate the effect of multi-perturbation training.

## Removed Points
*These points are flagged to be removed—treat them with caution.*
- **"Table 1 is not provided in the text"** — The tables use `\input{}` commands and exist in the original submission; the extraction is incomplete. Removed per rule (parser artifact).
- **"No dataset release URL is given"** — The paper states it has "prepared seven high-quality transcriptomics datasets"; per rules, cannot question existence/release status of cited resources. Removed per hard rule.
- **"The paper does not compare against Varici et al. and LiT"** — The paper explicitly justifies this: "The former strictly assumes linearity, while the latter requires data from multiple environments, which are not available here." The reviewer's criticism is addressed by the paper. Removed per rule (strawman weakness).
- **"The causal discovery algorithms' failure on transcriptomic data is only shown via runtime on toy-sized data"** — This is an unreasonable demand (running intractable methods on large data). The paper cites affirmative evidence of scalability limitations. Removed as a nitpick that demands the paper do the impossible.
- **"Heuristics like pairwise correlation are vague for reproducibility"** — The paper specifies: "we used inverse covariance as the global statistic on synthetic data, and correlation on transcriptomics data" (Section 3.3). This is sufficiently specific. Removed per rule (strawman).

## Novel Insights
The most interesting insight from these reviews is not about the paper itself but about how its evaluation strategy interacts with the causal discovery framing. The paper claims a "causality-inspired approach," but the reviews reveal tension: the causal featurizer is trained on synthetic data and never validated on real data, yet the downstream task clearly benefits from it (especially for soft interventions). This suggests that even imperfect, synthetic-data-pretrained graph representations carry useful signal for biological perturbation analysis. If this is true, it opens a practical path forward: frozen amortized causal discovery modules can serve as feature extractors for biological tasks even when their individual graph predictions are unreliable—analogous to how pretrained vision models transfer to domains very different from their training data. The community would benefit from a systematic study of when and why such transfer works for causal representations.

## Suggestions
1. Add diagnostic experiments for the causal featurizer on real data: (a) stability across bootstrap samples from the same perturbation, (b) a negative control using random splits of control-only data, and (c) visualization of whether predicted graph changes cluster by known biological pathways.
2. Clarify the real-data training protocol: specify how control cells are paired with perturbed cells for each training example, and whether control cells are shared or resampled.
3. Add a controlled experiment where CDN is trained on a single cell line's data (matching the per-cell-line setup of baselines) to isolate the effect of cross-perturbation supervision.
4. Report confidence intervals or bootstrap estimates for the main real-data metrics.
5. Include synthetic experiments with larger graphs (N=100–500) even without competing baselines, to verify scalability claims.
6. Report how many perturbations were filtered per dataset by the ≥10 DE genes threshold, and confirm all baselines were evaluated on the same subsets.

## Score and Decision

The paper presents a clever, well-motivated architecture with strong empirical results on real biological benchmarks and a clear scalability advantage over prior causal discovery methods. The core weakness—lack of direct validation of the causal featurizer on real data—is a genuine concern but is openly discussed by the authors and partially mitigated by the downstream results and the soft-intervention ablation. The remaining issues are clarifications and controlled experiments that strengthen but do not invalidate the contribution. The paper is a solid contribution to the intersection of causal inference and computational biology.

**Score:** 7.0

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>