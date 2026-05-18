Now I have all the information I need to write the final consolidated review.

## Summary

The paper proposes **Prompt Diffuser**, a method that reframes prompt tuning for pre-trained offline RL policies as a conditional generative modeling problem. It uses a diffusion model to generate trajectory prompts from random noise, thereby eliminating sensitivity to prompt initialization — a well-documented limitation of prior prompt-tuning methods. A gradient projection technique is introduced to incorporate downstream task guidance during diffusion training without conflicting with the diffusion loss. Experiments on four meta-RL benchmarks (Cheetah-dir/vel, Ant-dir, Meta-World reach-v2) show that Prompt Diffuser achieves the best average return among parameter-efficient fine-tuning methods (474.4 vs. 450.3 for Prompt-Tuning DT) while using only 1.24% of the PLM's parameters, and demonstrates robustness to prompt/dataset quality.

## Strengths

- **Novel and well-motivated formulation of prompt tuning as generative modeling.** The paper identifies a genuine limitation of existing RL prompt-tuning methods (initialization sensitivity, documented in §3.3 Fig. 2) and directly addresses it by generating prompts from random noise via a conditional diffusion model, eliminating the need for expert-prompt pre-collection.

- **Robustness to prompt and dataset quality is empirically convincing.** Table 2 shows that Prompt Diffuser maintains stable performance (~−33.5) across Expert, Medium, and Random prompts and datasets, while Prompt-Tuning DT degrades to −90.4. This is the strongest evidence for the core claim and is supported by a clean ablation design.

- **Strong few-shot performance with high parameter efficiency.** Prompt Diffuser achieves the best average return (474.4) among all parameter-efficient methods in Table 1, outperforming Prompt-Tuning DT (450.3), Soft Prompt (431.6), and Adaptor (412.7), while using only 0.17M trainable parameters (1.24% of the PLM). It approaches the full-data upper bound (496.6).

- **Gradient projection technique is a principled contribution.** The method of projecting the downstream-task gradient onto the orthogonal subspace of the diffusion gradient (§3.3) prevents performance degradation from naive loss combination, and Figure 3 shows consistent improvements over baselines (DM-only, DT-only, simple sum) across all environments.

- **Comprehensive ablation structure.** The paper systematically separates the effects of prompt initialization (Table 2), diffusion guidance (Fig. 3), and out-of-distribution / zero-shot capability (Table 3), providing clear evidence for each design choice.

## Weaknesses

### Fatal
None.

### Major

- **Zero-shot experiment is not adequately explained, making the result difficult to interpret.** The paper reports that Prompt Diffuser achieves 329.2 ± 21.8 in the Ant-dir-OOD zero-shot setting versus 52.7 for baselines (Table 3), but never specifies what conditions y(τ^*) are used for generation when "no additional trajectories from the target tasks are available" (line 446). The algorithm (Alg. 1, lines 291-294) prescribes constructing y(τ^*) from τ_i^* sampled from D_test, but this is the few-shot procedure — the zero-shot case is never described. Without knowing whether default conditions from the training distribution are used, or some other mechanism, this headline result is underdetermined. The claim of "zero-shot generalization" requires a clear description of how the prompt is generated in this setting to be meaningful.

### Minor

- **Comparison with baselines is asymmetric in pre-training data.** Prompt Diffuser pre-trains its diffusion model on the full training task distribution (e.g., 45 tasks for Meta-World), while baselines like Prompt-Tuning DT and Soft Prompt optimize prompts using only target-task few-shot data. This is inherent to the method's design, but the framing as a direct "few-shot fine-tuning" comparison (line 393-394) is somewhat misleading — the ∼5% average gain could partially reflect additional pre-training data rather than the generative approach itself. A control experiment (e.g., training Prompt Diffuser without full-task-distribution pre-training, or multi-task pre-training Prompt-Tuning DT) would strengthen the causal claim.

- **The gradient projection notation is confusing.** Line 242 defines S_{DM}^{⊥} as "the subspace spanned by ∇L_{DM}^{⊥}" but ∇L_{DM}^{⊥} itself is never defined — it's circular because S_{DM}^{⊥} uses the ⊥ superscript that (⋅)^{⊥} is supposed to denote. The overall procedure is understandable from context, but the mathematical description lacks precision.

- **Number of few-shot trajectories is not reported.** The paper states "prompts of length K^*=5 are utilized" and "few-shot expert data collected from the target task with three different seeds" (line 324) but never specifies how many trajectories constitute the "few-shot" set. This detail is critical for reproducibility and fairness of comparison.

- **Few-shot OOD gains are modest.** In the Ant-dir-OOD few-shot setting (Table 3), Prompt Diffuser achieves 546.8 vs. 540.8 for Prompt-Tuning DT — only a ∼1% improvement. While the zero-shot OOD gain is large (329.2 vs. 52.7), this asymmetry should be discussed.

### Trivial

- **Figure 3 y-axis only says "relative performance" without specifying units or baseline value.** The caption says Equation (ab:dm) is the baseline, but its absolute performance is not reported, making the magnitude of improvement unquantifiable from the figure alone.

## Nice-to-Haves

- **Ablation removing reward tokens from the diffusion target.** The paper includes rewards in x^0(τ^*) (Eq. 3) even though they are not used in the prompt format (Eq. 1). An ablation that trains a variant where x^0 contains only states and actions would clarify whether modeling reward dynamics is helpful or irrelevant.

- **Sensitivity analysis for λ and diffusion steps N.** The paper fixes λ=1 for all environments without justification. A plot showing performance at different λ values (e.g., 0.1, 0.5, 1.0, 2.0) and different N values would strengthen the empirical analysis.

- **Evaluation on harder domains.** Testing on tasks with longer horizons or higher-dimensional observations (e.g., Kitchen, Adroit) would better demonstrate scalability.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Reward tokens are included in the diffusion denoising but never used in prompts (deep inconsistency)."** — The reviewer misread the paper. Line 195 says "denoising the entire transition process can introduce model bias" which the reviewer interpreted as arguing against the paper's own design. In context, the paper explains that this is a known concern, and they address it by using conditional diffusion (rather than a classifier-based approach requiring Q-functions, lines 196-198). The design choice is justified. The paper could benefit from a clearer explanation, but there is no inconsistency.

- **"The zero-shot experiment is invalid"** — The paper does not explain the zero-shot mechanism, which is a legitimate weakness (kept above as Major). However, this does not make the experiment "invalid" — the measurements are what they are. The missing explanation is the problem.

- **"Algorithm 1 is inconsistent with the zero-shot experiment"** — This is the same issue as the missing zero-shot explanation above. Merged into that entry.

## Novel Insights

None beyond the paper's own contributions. The reviews surface that the paper's strongest evidence (robustness to initialization, Table 2) is cleaner than its headline results (Table 1), and that the zero-shot claim is the most interesting but least explained finding. The tension between an elegant generative framing and an under-explained experimental condition is the most notable pattern across the reviews.

## Suggestions

1. **Clarify the zero-shot protocol explicitly.** Describe what y(τ^*) conditions are used in zero-shot generation (default returns-to-go from training? randomly sampled? average of training task conditions?), and explain how the generated prompt is used by the PLM without any target-task data.

2. **Add a controlled baseline.** Train a version of Prompt-Tuning DT that also leverages multi-task pre-training (e.g., pre-training prompt embeddings on the training task distribution) to isolate whether gains come from the generative approach vs. additional pre-training data.

3. **Report the exact number of trajectories** used in the "few-shot" setting, the training hyperparameters for all baselines, and the absolute baseline values for Figure 3.

4. **Fix the notation in §3.3** (Eq. 9-10 area) to avoid the circular definition of S_{DM}^{⊥} / ∇L_{DM}^{⊥}.

## Score and Decision

**Calibration anchors used (from retrieval batch):**

| Path | Avg Score | Comparison to paper under review |
|------|-----------|----------------------------------|
| /home/wg25r/.../WM5G2NWSYC.md | 2.00 | Severely flawed paper with unclear contributions; our paper is much better structured and has clearer results |
| /home/wg25r/.../FLOaCQfZe9.md | 2.50 | Meta-RL paper with missing baselines and presentation issues; our paper is more rigorous and complete |
| /home/wg25r/.../PH7ja3T0vN.md | 4.50 | Diffusion+RL paper rejected for missing baselines and unclear methodology; our paper has better experiments but narrower scope |
| /home/wg25r/.../2x1U8a3s7G.md | 5.00 | Prompt diffusion for CV, topically similar; our paper has stronger empirical grounding and clearer contribution |
| /home/wg25r/.../LfghnrSJNg.md | 5.80 | Diff-Prompt (diffusion for prompt generation in CV), accepted; similar spirit, our paper has comparable experimental quality in a different domain |
| /home/wg25r/.../TeeyHEi25C.md | 6.25 | Diffusion for RL rejected due to missing baselines and clarity; our paper is more complete empirically |
| /home/wg25r/.../7BQkXXM8Fy.md | 7.50 | Strong diffusion planning survey paper, accepted; our paper has a different contribution type (novel method vs. empirical analysis) and narrower scope |
| /home/wg25r/.../MtDd7rWok1.md | 7.20 | Strong theory+experiments paper on diffusion exposure bias; our paper's theoretical foundation is less deep |

The paper makes a genuinely novel contribution — framing prompt tuning as generative modeling for RL — and supports it with clean ablations on initialization robustness. The main weakness is an under-explained zero-shot experiment that prevents full interpretation of a headline result, and the lack of a controlled baseline for the pre-training data asymmetry. Compared to similar papers at ~5.0-6.0 (like 2x1U8a3s7G at 5.00 and LfghnrSJNg at 5.80), this paper's contribution is solid but the missing zero-shot explanation and modest OOD few-shot gains hold it back from being a stronger work. The paper is clearly a real submission with a well-defined method and reasonable experiments, but the missing zero-shot details and asymmetric comparison are issues that would need addressing.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>