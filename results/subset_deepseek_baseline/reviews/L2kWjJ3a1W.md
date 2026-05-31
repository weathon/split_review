## Summary

The paper proposes Text-Guided Decision Transformer (TG-DT), an offline meta-RL framework that achieves zero-shot generalization to unseen tasks using only natural language task descriptions. TG-DT employs a dual alignment mechanism combining contrastive learning (TBC) and matching-based objectives (TBM) to embed task descriptions and behavioral trajectories into a shared latent space, then conditions a Decision Transformer on these aligned representations to generate actions. Experiments on MuJoCo and MetaWorld benchmarks show TG-DT performs comparably to or better than baselines that require test-time interaction, while operating in a strictly harder zero-shot setting.

## Strengths

- **Novel problem formulation**: The paper tackles a practically important and under-explored setting—zero-shot offline meta-RL with only natural language descriptions, no test-time interaction or task-specific data. This is a meaningful step toward language-grounded generalization in sequential decision-making.
- **Technically sound alignment design**: The dual alignment (contrastive for cross-task separation + matching for within-task quality distinction) is a reasonable extension of vision-language alignment ideas to behavior sequences, addressing the unique challenges of temporal dynamics and trajectory quality variation.
- **Comprehensive experiments**: Evaluation across multiple environments (MuJoCo, MetaWorld), dataset qualities (Medium, Expert, Mixed), and generalization settings (zero-shot, few-shot) provides solid empirical support. Ablation studies and analysis of alignment quality (t-SNE, cosine similarity) strengthen the paper.

## Weaknesses

### Major

- **Potential oracle information leakage through templated descriptions**: Task descriptions include metadata fields such as expected return and episode length (e.g., "yield an expected reward of 6,000"). At test time the paper claims to use "approximate statistics inferred from the training distribution" rather than ground-truth values, but no details or validation are provided for how these approximations are computed or how robust the method is to inaccurate estimates. If test-time descriptions inadvertently reflect oracle task information, the zero-shot claim is undermined. This is the most critical weakness and must be fully addressed.
- **Unfair or weakly controlled baseline comparisons**: DT-based baselines (Prompt-DT, Meta-DT, DPDT, etc.) are designed for few-shot settings with test-time demonstrations, but the paper compares them in zero-shot setting by simply not providing demonstrations. These methods were not originally intended for zero-shot without interaction, so the comparison is informative but not conclusive. Additionally, the description-guided data sharing mechanism (retrieving training trajectories at test time) gives TG-DT an advantage that standard baselines do not have—this should be controlled by comparing against a version of baselines that also get access to similar training data in a comparable manner.
- **Insufficient detail on test-time prompt construction**: The paper states that test prompts follow the same templated format with approximate statistics, but the exact procedure for computing these approximations is absent. Without knowing how expected return and episode length are estimated (e.g., averaged over all training tasks? weighted by similarity?), the reproducibility of the results and the validity of the zero-shot setting remain unclear.
- **Performance variability and statistical significance**: Tables report only mean returns without standard deviations or confidence intervals (delegated to appendix, which is stripped). Given that some differences between TG-DT and baselines are small (e.g., Ant-dir zero-shot: TG-DT 328.3 vs MDT 357.5), it is unclear whether TG-DT’s performance is statistically distinguishable. The paper claims "compatible performance" but should provide error bars to support this.

### Minor

- **Misalignment between BLIP pre-training and the task**: BLIP is pre-trained on image-text data, but TG-DT uses only text inputs (templated descriptions) without any visual modality. The motivation for using BLIP’s text encoder is not well justified; a standard language model (e.g., BERT) would be a more natural choice. The paper should explain why BLIP’s cross-modal attention patterns transfer to trajectory-text alignment.
- **Missing analysis of description-guided data sharing baselines**: The data sharing strategy is ablated for TG-DT (varying K), but the paper does not apply the same data sharing to baselines to provide a fair comparison of its benefit. It is unclear whether the gains come from the alignment mechanism or simply from having more training trajectories at test time.

### Trivial

- Minor citation formatting issues (e.g., "Eslamí & de Melo 2025" should be "Eslami & de Melo"; "Haldrup et al., 2024" should be "Haldar et al."), but these do not affect evaluation.

## Nice-to-Haves

- An analysis of how sensitive TG-DT is to the accuracy of the approximate test-time metadata (e.g., sweeping over different perturbation levels of expected return) would greatly strengthen the zero-shot claim.
- A comparison against a simpler baseline that uses the same templated descriptions but only a single contrastive loss (without TBM) would help isolate the contribution of matching.
- Discussion of how the approach could extend to free-form natural language (as noted in limitations but not explored).

## Novel Insights

None beyond the paper’s own contributions—the idea of aligning text descriptions with behavior trajectories via dual contrastive and matching objectives for zero-shot offline meta-RL is the primary novelty. The empirical observation that moderate representation gap (~0.3 cosine similarity) still enables effective policy learning aligns with findings in multi-modal representation learning, but is not deeply analyzed.

## Suggestions

- Clearly specify how test-time expected return and episode length are estimated from the training distribution. Provide an ablation where these values are deliberately misspecified to test robustness.
- Report standard deviations or confidence intervals for all main results, preferably in the main tables.
- Add a controlled experiment where baselines are also allowed access to the same retrieved training trajectories (through fine-tuning or prompt conditioning) to isolate the effect of the alignment mechanism.
- Justify the use of BLIP’s text encoder over a simpler alternative, or ablate the choice of text encoder initialization.

## Score and Decision

The paper addresses a novel and important problem with a reasonable technical approach and extensive experiments. However, the major weakness regarding potential oracle information leakage in test-time descriptions and the insufficient validation of the zero-shot setting significantly undermine confidence in the claims. The baseline comparisons are also not fully equitable. These concerns prevent acceptance at ICLR in the current form.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>