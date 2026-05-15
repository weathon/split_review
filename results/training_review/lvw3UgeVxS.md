Now I have all the information needed. Let me construct the final consolidated review.

## Summary

The paper introduces gRNAde, a geometric deep learning pipeline for 3D RNA inverse design that conditions sequence generation on one or more backbone structures. The key contributions are: (1) a multi-state GNN architecture that processes conformational ensembles via independent message passing per state followed by order-invariant pooling, enabling both single-state and multi-state RNA design; (2) superior single-state sequence recovery (56%) over Rosetta (45%) and RDesign (43%) on a 14-RNA benchmark; (3) the first demonstration of multi-state RNA inverse design, with 3–5% improvement over single-state baselines; and (4) zero-shot ranking of mutants in a ribozyme fitness landscape.

## Strengths

- **First multi-state RNA inverse design pipeline.** gRNAde is the first explicitly multi-state ML pipeline for RNA inverse design, addressing a genuine gap — existing tools either ignore 3D structure entirely or handle only single conformations. The multi-state GNN encoder (independent message passing per state + average pooling) is simple, transparent, and described as a plug-and-play extension for any geometric GNN pipeline.

- **Improved single-state recovery over Rosetta and RDesign.** On the 14-RNA benchmark from Das et al. (2010), gRNAde achieves 56% native sequence recovery vs. 45% for Rosetta and 43% for RDesign (Figure 1a, Section 4.1), with orders-of-magnitude faster inference. This demonstrates that a learned geometric GNN approach can outperform physics-based and alternative GNN-based toolkits on a standard fixed-backbone design task.

- **Consistent multi-state improvement in flexible regions.** Multi-state gRNAde shows a 3–5% improvement over the single-state variant on the multi-state benchmark (Figure 2a, Section 4.2), with gains concentrated in nucleotides that undergo base-pairing changes or have high RMSD across states (Figure 2b). This provides evidence that the multi-state architecture captures conformational flexibility in a way single-state models cannot.

- **Rigorous data preparation.** The paper creates a large ML-ready dataset from RNASolo (4,223 unique RNAs, ~2.8M nucleotides), uses US-align structural clustering to create fair train/validation/test splits that test generalization, and reports standard deviations across three random seeds. This provides a reproducible foundation for future RNA inverse design research.

## Weaknesses

### Fatal
None.

### Major

- **Zero-shot fitness landscape ranking lacks meaningful computational baselines.** The retrospective study (Section 4.3, Figure 3) compares gRNAde perplexity-based ranking only against random selection from various pools (all mutants, single mutants, single+double mutants). No other computational method — Rosetta, RDesign, energy-based scoring, or any other inverse folding model — is evaluated. Showing that perplexity outperforms random draws does not demonstrate practical utility, as any reasonable computational score would be expected to beat random. This does not undermine the core inverse design contribution, but the fitness landscape claim is not supported by the evidence provided.

- **Multi-state vs. single-state training protocol is underspecified.** The paper states that "equivalent single-state and multi-state gRNAde models" were trained (line 309), but does not explicitly describe how the single-state model was trained on the multi-state split. Was it trained on each conformation as an independent data point, or on one conformation per RNA? If the former, the single-state baseline is fair (and potentially has more training examples); if the latter, the multi-state model has a data advantage. This detail is important for interpreting the 3–5% improvement claim. A brief clarification would resolve this.

### Minor

- **Rosetta comparison relies on 14-year-old published numbers without replication.** The authors admit they did not run Rosetta themselves (footnote, line 265), instead citing numbers from Das et al. (2010). Differences in backbone preprocessing, design protocol, or stochastic variation could affect the comparison. The concurrent comparison against RDesign (43% recovery) partly mitigates this concern, but the headline "56% vs 45%" claim would be strengthened by a controlled rerun.

- **All results reported at a single temperature (0.1).** The paper notes that temperature modulates the recovery-diversity tradeoff (lines 137–139) but only reports results at temperature 0.1. Showing how recovery, diversity, and self-consistency vary across temperatures (e.g., 0.1, 0.5, 1.0) would provide practical guidance for users and strengthen the analysis.

### Trivial

- The multi-state result (Figure 2a) is plotted for one random seed in the main text, with full results deferred to the appendix. Error bars in the main figure would improve readability.

## Nice-to-Haves

- **Self-consistency results in the main text.** While these may appear in the appendix (as referenced), the paper itself describes self-consistency as "a critical part of the overall pipeline." Showing even a summary (e.g., average MCC or scRMSD) in the body would strengthen the core claim of "3D RNA inverse design."
- **Controlled multi-state ablation with explicit training data description.** A table clarifying exactly what data each baseline saw (number of conformations per RNA, etc.) would eliminate ambiguity.
- **Resolution mismatch discussion in fitness landscape.** The 5Å cryo-EM structure used for fitness ranking differs from the ≤4.0Å training data (noted in a footnote). A brief discussion of how this might affect results would be helpful.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"No structural self-consistency validation"** — Removed per hard rule about appendix stripping. The paper references \Cref{app:ablation} for "collated results and ablations," which the parser strips.
- **"First geometric deep learning architecture claim is overstated"** — Removed per "DO NOT mention missing related works" rule, as I cannot independently verify prior art claims.
- **"US-align threshold not validated for RNA"** — Removed as factually inaccurate; US-align (Zhang 2022) is a universal aligner designed for both proteins and nucleic acids.
- **"Resolution mismatch not discussed"** — Removed as factually inaccurate; the paper explicitly notes this in a footnote (line 342).
- **Generic formatting/style nitpicks** — Removed per hard rules.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest contribution (multi-state RNA design) is evaluated primarily through sequence recovery, yet the metric most relevant to real-world utility — structural self-consistency — is apparently deferred to the appendix. Meanwhile, the weakest experimental section (zero-shot fitness ranking) has the most exciting real-world implications. This suggests the paper's evaluation priorities could be restructured: the fitness landscape study needs stronger baselines to be credible, while the core inverse design claims could be made more convincing by bringing self-consistency results into the main text.

## Suggestions

1. **Explicitly describe the single-state multi-state training protocol** — state whether the single-state baseline was trained on each conformation as an independent sample or on one state per RNA, and discuss how this affects the fairness of the comparison.
2. **Add at least one computational baseline to the fitness landscape study** — e.g., Rosetta's design score or RDesign perplexity on the same ribozyme data. This would substantially strengthen the zero-shot ranking claims.
3. **Bring key self-consistency results into the main text** — even a single summary metric (e.g., average scMCC or scRMSD across the single-state test set) would directly support the claim that gRNAde produces designable sequences.
4. **Report recovery/diversity/self-consistency at multiple temperatures** to guide practical use.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>