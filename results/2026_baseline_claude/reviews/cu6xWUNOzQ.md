## Summary

The paper introduces a nonlinear, multimodal brain encoding model for naturalistic speech fMRI, combining audio features from Whisper and semantic features from LLaMA. Using PCA for dimensionality reduction followed by a single-hidden-layer MLP, the model achieves 17.2% and 17.9% relative improvements in mean voxelwise r² and normalized correlation (CC_norm) over the standard unimodal linear baseline (Antonello et al., 2024), and 7.7%/14.4% improvements over the prior SOTA linear ensemble. The paper also introduces a Relative Error Difference (RED) metric for joint spatiotemporal clustering and connects the observed cortical integration patterns to established neurolinguistic theories including the Motor Theory of Speech Perception, the Convergence-Divergence Zone model, and embodied semantics.

---

## Strengths

- **Principled ablation isolating nonlinearity from multimodality**: The paper systematically decouples multiple sources of gain through carefully designed controls: MLLinear (reduced-rank linear regression without nonlinear activations) rules out dimensionality reduction as the driver, and DIMLP (within-modality nonlinearity only) isolates the additional benefit of cross-modal nonlinear interaction. This is methodologically rigorous and rarely done so clearly in speech encoding work.

- **Substantial, reproducible performance gains with high parameter efficiency**: The multimodal MLP achieves 4.29% avg r² with only 5.64M parameters, compared to the 1.31B-parameter baseline at 3.66% r². The gains (17.2% relative over baseline, 7.7% over prior SOTA) are unusually large for incremental fMRI encoding work, as the authors themselves document in Appendix N.2 by surveying prior gains in the field.

- **Novel RED metric enabling spatiotemporal analysis**: Introducing RED—quantifying per-voxel, per-timepoint prediction advantage of one feature set over another—enables joint spatial and temporal analysis of cortical dynamics that static voxelwise correlation cannot provide. This is a genuine methodological contribution applicable beyond this paper.

- **Neuroscientific interpretations are grounded and differentiated**: The variance partitioning analysis (68.5% of significantly predicted voxels jointly explained by audio+semantic) and the ROI-level breakdowns (Broca's 88.2% joint, M1M 32.4% unique audio) yield specific, falsifiable claims that connect coherently to the dual-stream model, Motor Theory, and CDZ—not merely generic endorsements of existing theories.

- **Transparent acknowledgment of scope and interpretive limits**: The authors explicitly note that the observed sensorimotor effects might reflect quasi-semantic factors (lexical frequency, predictability, articulatory demands) rather than embodied simulation, and they state that their design cannot distinguish these. This epistemic honesty strengthens the scientific credibility of the interpretations.

---

## Weaknesses

### Fatal
None.

### Major

- **N=3 subjects limits generalizability of neurolinguistic claims**: While three subjects is standard for this dataset, the strong theoretical claims (Motor Theory, CDZ, embodied semantics) rest on patterns observed in only three individuals. Statistical corrections are applied (FDR at q<0.01 and p<0.05), but subject-level variance in Figures 2e and 29 is not fully discussed. The paper moves from "our model predicts better" to "this confirms neurolinguistic theory X" faster than three subjects warrants. Explicitly quantifying inter-subject consistency in the key ROI findings (e.g., Broca's 88.2% joint, M1M 32.4% unique audio) would substantially strengthen the theoretical conclusions.

- **Modularity improvement for RED-based clustering is marginal**: The central claim in Section 3.1.2 is that nonlinear RED-based clustering reveals "clearer functional groupings." The evidence is modularity Q=0.155 (nonlinear RED) vs. Q=0.145 (linear RED) vs. Q=0.068 (raw FC). The gap to FC is large and convincing, but the nonlinear vs. linear RED gap is only 0.010 (a ~7% relative difference in Q). This is a modest improvement that may not justify the strong claim about "previously hidden patterns of brain organization." No statistical test or confidence interval for the modularity difference is reported.

- **Layer selection for the multimodal model is underspecified**: The paper states LLaMA features use a dynamic context window and Whisper uses the encoder's final layer with a 16s sliding window, but the specific layer selected for the main multimodal experiments is not clearly stated in the main text. Since LLaMA and Whisper have distinct representational profiles across layers (Figure 16 shows layer-by-layer variability), the choice of layer could meaningfully influence how well each modality contributes and whether multimodal fusion helps. The reader needs to know whether the combined model uses the best per-modality layers or whether layer selection was done jointly, and if so, whether that jointly tuned configuration inflates the multimodal benefit.

### Minor

- **Generalization to a second dataset is absent**: All results come from a single dataset (LeBel et al., 2023). Demonstrating that the nonlinear multimodal MLP also outperforms linear baselines on even one other publicly available naturalistic speech fMRI dataset (e.g., the CMU fMRI corpus, the narratives dataset) would substantially increase confidence that the findings are not dataset-specific.

- **The absolute CC_norm improvement is modest despite large relative improvement**: CC_norm goes from ~29.12% (baseline) to 34.32% (proposed). While the ~17.9% relative improvement is real, the absolute improvement (~5.2 percentage points) means the model still explains only about a third of the noise ceiling-normalized variance. The paper emphasizes relative improvements throughout; adding a plain-language description of the absolute gap to the noise ceiling (which must be ~100% by construction) would help readers calibrate the practical significance.

- **Comparison with the full Antonello et al. (2024) ensemble is not entirely fair as stated**: Table 1 shows "text+audio Linear all voxels" as the SOTA competitor at CC_norm=31.36%, but the Antonello et al. SOTA uses multiple Whisper layers in a stacked regression. The proposed model uses only a single Whisper layer. If using the best single Whisper layer already beats the multi-layer ensemble, that is itself an interesting finding worth highlighting as a standalone claim.

### Trivial
- "unnormlized" typo in the abstract.
- Figure 1 caption is duplicated in the extracted text (likely a parser artifact).

---

## Nice-to-Haves

- A brief ablation on the number of PCA components (e.g., 128, 256, 512, 1024) to verify that 512 is not cherry-picked to benefit the MLP over the linear models.
- Reporting effect sizes (e.g., Cohen's d) alongside p-values for the ROI-level improvements in Figure 2e to allow readers to assess practical significance.
- A visualization of RED temporal profiles for a few key ROIs (e.g., AC vs. Broca vs. M1M) to concretely illustrate what the metric reveals about temporal dynamics, beyond the clustering summary.

---

## Novel Insights

The paper's most original empirical contribution is demonstrating that cross-modal nonlinear interactions—not merely within-modality nonlinearity—are a key driver of improved fMRI prediction accuracy during naturalistic speech. The DIMLP ablation cleanly shows that within-modality nonlinearity (DIMLP: +2.0% r² over linear) provides less gain than full cross-modal nonlinear interaction (MLP: +2.6% further), with motor and somatosensory regions specifically benefiting most from cross-modal nonlinearity. This finer-grained decomposition goes beyond prior nonlinear encoding work, which typically did not dissociate within- vs. cross-modal contributions. The RED metric, while conceptually simple, provides a new handle for studying how the relative predictive advantage of different feature types varies both across brain space and across time in a single unified framework, which could be generalized to encode other competing feature hypotheses in future work.

---

## Suggestions

- Provide subject-by-subject modularity scores for RED-based clustering in addition to the mean, and test whether the Q=0.155 vs. Q=0.145 difference is significant across the three subjects.
- For the main multimodal MLP results, explicitly state which LLaMA and Whisper layers are used, and include a supplementary table showing whether the best single-layer combination was selected based on validation performance (and if so, report held-out test performance for the selected configuration only).
- Consider adding a brief comparison on a second fMRI dataset to demonstrate generalizability, even if less extensive than the primary analysis.
- Report confidence intervals or bootstrapped standard errors for the main headline numbers (17.2%, 17.9%) rather than just the point estimates.

---

## Score and Decision

The paper makes a genuine contribution: it is the first systematic demonstration that nonlinear multimodal encoding is feasible and substantially beneficial for naturalistic speech fMRI, provides a clean ablation decomposing the sources of improvement, introduces a useful metric (RED), and connects the results to neurolinguistic theory in a principled way. The key limitation is that the N=3 design constrains how far the strong theoretical claims can be pushed, and the modularity improvement for RED-based clustering is modest. These are real weaknesses but do not invalidate the core engineering and neuroscientific findings.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>