## Summary

This paper proposes Min-K%++, a method for pre-training data detection (membership inference) for LLMs. The core idea is to normalize each token's log-probability by the mean and standard deviation of the log-probabilities over the entire vocabulary at that position, then aggregate the lowest k% of these z-scored values. The method is motivated by a theoretical insight derived from score matching—that MLE training makes training samples local maxima of the log-likelihood along input dimensions—which the authors translate into a discrete-domain principle of identifying whether a token is a mode of the conditional categorical distribution. Empirically, Min-K%++ achieves substantial AUROC gains (6.2–10.5%) over prior methods on the WikiMIA benchmark across multiple model families, while being competitive with reference-based methods on the more challenging MIMIR benchmark without requiring a second model.

## Strengths

- **Consistent and large gains on WikiMIA across model families**: Min-K%++ outperforms the runner-up Min-K% by 6.2–10.5% absolute AUROC on WikiMIA across input lengths of 32, 64, and 128 tokens, and the improvement holds across all evaluated model families including the non-transformer Mamba architecture (Section 5.2). For Mamba-1.4B, it reduces the performance drop from short inputs from 4.6% (Min-K%) to just 1.6%.

- **Reference-free performance competitive with reference-based methods on MIMIR**: On the more challenging MIMIR benchmark (where training and non-training texts are drawn from the same dataset), Min-K%++ achieves results on par with the Reference method (Carlini et al., 2021) while requiring no extra LLM. The reference method required searching over 8 different reference models to obtain its best results, whereas Min-K%++ is a single-model approach (Section 5.2, Table 2). This is a practical advantage.

- **Decomposable ablation validates both components**: The ablation in Section 5.3 (Table 3) shows that each calibration factor (\(\mu\) and \(\sigma\)) individually provides a large boost (9.3% and 7.0%) over raw log probabilities, and combining them yields a 16.8% improvement, cleanly confirming that both components of the formulation are empirically meaningful.

- **Lower sensitivity to the k% hyperparameter**: Min-K%++ shows only 2.7% AUROC variation across k values versus 4.4% for Min-K% (Figure 4), indicating the method is more robust and easier to deploy in practice.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The theoretical connection between the score-matching insight and the proposed method is analogical rather than derivational.** The paper develops a formal argument about continuous input spaces (Section 4.1): MLE training drives first-order derivatives of log-likelihood toward zero and second-order derivatives toward negative values, implying training points are local maxima. The "translation" to the discrete LLM setting (Section 4.2) replaces "varying a continuous input dimension" with "comparing probabilities across different tokens in the vocabulary." These are mathematically different operations—one is about input-space geometry, the other about conditional distribution shape—and the paper provides no formal bridge. The method is well-motivated by its calibration interpretation (Interpretation 2) and works empirically, but the paper's framing as "theoretically motivated methodology" overstates the tightness of the connection. The authors should recalibrate this framing to acknowledge the inspirational nature of the insight rather than presenting it as a derivation.

- **No measures of uncertainty reported.** All AUROC numbers are presented as point estimates without confidence intervals, standard errors, or information about the number of trials or data splits. This is especially concerning for the MIMIR results, where gains are 0–3% (-0.2% to +2.8% relative to Min-K%). Without variance estimates, it is impossible to assess whether these improvements are statistically meaningful or within evaluation noise.

- **MIMIR baselines were not re-run under identical conditions.** The paper states "most numbers are taken from those reported by Duan et al. (2024)" (Section 5.2). This introduces potential confounds from different codebases, preprocessing, or evaluation pipelines. The authors should either re-run baselines or discuss the potential impact of this mismatch.

- **Ablation study is narrow in scope.** The hyperparameter and component ablations are conducted on a single model (LLaMA-13B) and a single benchmark (WikiMIA). While the results are informative, their generality is untested.

- **Online detection setting is underdeveloped.** This experiment is mentioned in one sentence with no details about setup, metrics, or results. It should either be developed with sufficient detail or removed.

- **Computational cost of computing μ and σ over the full vocabulary is not discussed.** Computing the mean and standard deviation of log-probabilities over the entire vocabulary at each token position involves a sum over potentially 32k–128k tokens per position. A complexity analysis or runtime comparison with Min-K% would be useful for practitioners.

### Trivial
None.

## Nice-to-Haves
- The paper would benefit from reporting absolute AUROC numbers for all methods in the MIMIR prose discussion (not just relative improvements over Min-K%), making cross-comparison easier.
- The "extrapolating this trend" speculation about larger models (Section 5.2) should be removed or clearly labeled as conjecture.

## Removed Points
These points were flagged by reviewers but removed for the reasons noted; they should be treated with caution.

- **Missing Section 5.1 (Experimental Setup).** The reviewer noted Section 5.1 appears missing. This is a PDF-parser artifact—the section exists in the original submission. **Removed: parser issue.**
- **"5 families of 10 models" claim not fully verifiable.** The reviewer observed only 3 families (LLaMA, Pythia, Mamba) are named in the available text. Model families and results are reported in tables and figures stripped by the parser; they exist in the original submission. **Removed: parser issue.**
- **Criticism about reference availability/reproducibility.** Any questioning of whether cited baselines, datasets, or models exist. Paper cites WikiMIA (Shi et al., 2024), MIMIR (Duan et al., 2024), and standard model families. **Removed: per hard rules, cited entities are assumed to exist.**
- **Criticism that Min-K%++ oversells itself as "new SOTA" when MIMIR gains are marginal.** The paper's abstract states "improves upon reference-free methods while performing on par with reference-based method," which accurately characterizes the MIMIR results. The main SOTA claim is supported by the WikiMIA results. **Removed: the paper's self-characterization is accurate.**
- **Formatting nitpicks about notation or presentation.** **Removed: per hard rules.**

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Recalibrate the theoretical framing: present the score-matching/local-maxima insight as **inspiration** that motivates the method, not as a formal derivation of it. The calibration interpretation already provides a self-contained justification.
2. Add confidence intervals, standard errors, or bootstrap estimates for all main AUROC results, especially the MIMIR results where margins are thin.
3. Either re-run MIMIR baselines under identical conditions or add a discussion of potential confounds from using previously reported numbers.
4. Expand the ablation to at least one additional model/benchmark pair to confirm generality.
5. Remove or substantially expand the online detection experiment.
6. Add a brief analysis of the computational overhead from computing \(\mu\) and \(\sigma\) over the full vocabulary.

## Score and Decision

The paper proposes a simple, intuitive, and empirically effective method. The WikiMIA results (6–10% absolute AUROC gains across model families) are genuinely strong and rare in this space. The ablation cleanly validates the design choices. The main limitations are (a) a slightly overclaimed theoretical connection, (b) missing uncertainty measures, (c) narrow ablation scope, and (d) reliance on previously reported MIMIR numbers. None of these are fatal; all are addressable in a revision. The method is a solid contribution that establishes a stronger baseline for pre-training data detection.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>