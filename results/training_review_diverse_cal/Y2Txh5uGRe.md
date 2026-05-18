Now I have a thorough understanding of the paper and all reviewer inputs. Let me compile the final consolidated review.

---

## Summary

This paper proposes Text2Data, a two-stage framework for text-conditional data generation in low-resource settings. The method first learns an unconditional diffusion model on all available data (including unlabeled), then finetunes on labeled data using a lexicographic constraint optimization objective that penalizes deviation from the pretrained parameter space to mitigate catastrophic forgetting. Experiments are conducted on molecules (QM9), motion (HumanML3D), and time series (Yahoo Finance) across multiple labeled-data proportions.

## Strengths

1. **Clean two-stage design that separates distribution learning from controllability.** Unlike semi-supervised methods that attempt label inference, Text2Data first captures the marginal data distribution via unsupervised diffusion, then finetunes for controllability with an explicit regularization constraint. This is a principled approach that avoids the ambiguity of pseudo-labeling and is architecture-agnostic (the paper notes it can extend beyond diffusion models).

2. **Lexicographic optimization with dynamic gradient descent is technically sound for balancing competing objectives.** The formulation in Algorithm 1 provides a principled mechanism for prioritizing constraint satisfaction (preserving the pretrained distribution) while minimizing the conditional loss (controllability). The adaptive λ that depends on whether the constraint is currently satisfied is a reasonable design choice.

3. **Theoretical generalization bounds for constraint selection (Theorem 1).** The paper provides confidence bounds (ε_N, ε_{N_p}) showing that the empirical constraint set covers the true optimal set with high probability, and that the empirical solution does not violate the constraint excessively. Such guarantees are uncommon in the low-resource generative modeling literature.

4. **Multi-modal evaluation across three diverse data types.** The paper tests 2%–40% labeled proportions on molecules, motion, and time series with both controllability metrics (MAE, R Precision, multimodal distance) and qualitative visualizations. The consistent pattern of improvement across modalities and most label proportions strengthens the case that the method generalizes.

5. **Qualitative demonstration of fine-grained controllability.** Figure 2 show generated molecules progressively becoming less symmetrical as polarizability increases from "very low" to "very high," providing visual evidence that the model learns property-specific semantics.

## Weaknesses

### Major

1. **Text label construction for molecules and time series is not disclosed, which is a critical omission in the experimental setup.** The paper extracts numerical property values (polarizability, HOMO, LUMO, etc.) from QM9 and computed features (frequency, skewness, mean, etc.) from Yahoo Finance, but never explains how these become natural language text descriptions. Neither QM9 nor Yahoo Finance has natural language annotations. The only plausible construction method is converting numerical values into predetermined textual phrases (e.g., "very low polarizability"), but this is not stated. The paper frames its motivation around "expensive annotations" for real language, yet two of three modalities appear to use synthetic, template-based labels that directly encode the target property. This does not invalidate the method — the comparisons between methods on the same labels remain fair — but it undermines the "low-resource" framing and leaves unclear how the method would perform with genuinely noisy, diverse human language. The authors must disclose the label construction procedure and discuss this limitation.

2. **Generation quality metrics are reported only as average-margin percentages in prose, with no per-proportion breakdowns or standard deviations.** For molecules, the paper states percentage improvements for NLL (19.07%), validity (1.98%), molecular stability (2.34%), and atom stability (0.29%) as single averages across all label proportions. For motion, FID (2.73%) and diversity (0.81%) are similarly reported. No tables with per-proportion values or variability estimates are provided. This makes it impossible for readers to assess whether these improvements are consistent, meaningful, or statistically significant. Given that the controllability results (Tables 1–2, Figure 1) show many improvements that are modest with overlapping error bars, the absence of detailed generation quality data is a significant gap.

3. **Promised data augmentation baseline is absent.** Line 187 states: "Additionally, we conduct ablation study where each baseline is still finetuned but without the constraint... or directly applied to augmented text-data pairs." However, no data augmentation results appear in any table or figure. Since data augmentation is a standard and directly competing strategy for low-resource settings, its omission leaves the comparison incomplete and weakens the claim that the constraint optimization approach is preferable.

### Minor

4. **Controllability gains for motion are modest and the baseline wins at low label proportions.** For motion (Table 1), MDM-finetune outperforms Text2Data at 2% and 4% labeled data (R Precision: 0.37 vs. 0.34, 0.42 vs. 0.39). At higher proportions, Text2Data's advantage is often ≤0.01 in R Precision with overlapping standard deviations of ±0.01. The paper acknowledges this but still claims "consistently superior" performance, which overstates the case. The average margins of 2.31% (R Precision) and 0.93% (Multimodal Distance) over MDM-finetune are computed across proportions where several individual comparisons favor the baseline. The contribution is clearest at the highest label proportions (30–40%), not universally.

5. **No comparison against simpler regularization baselines (e.g., L2 penalty on parameter distance).** The core technical contribution is a constraint optimization that keeps finetuned parameters near the pretrained space. The natural baseline is a simple L2 penalty: adding ‖θ − θ_pretrain‖² to the finetuning loss. The -finetune baselines (without any regularization) do not test this. Without this comparison, it is unclear whether the dynamic gradient descent in Algorithm 1 provides meaningful gains over a simpler, well-understood alternative.

6. **Connection between theory (Theorem 1) and practice (hyperparameter ρ) is loose.** Theorem 1 provides confidence bounds ε derived from Bernstein's inequality, but in practice the constraint is relaxed using a free hyperparameter ρ, with no formal guidance on how to set ρ from ε. The theoretical analysis does not drive practical decisions, which limits its contribution.

7. **Key hyperparameters not reported.** Algorithm 1 lists α, β, γ, ρ, ω, p_uncond as inputs, but no typical values or search ranges are provided. Model architecture details (e.g., the 1D CNN for DiffTS) are not described. This hinders reproducibility.

### Trivial

- None.

## Nice-to-Haves

- Report per-proportion tables for all generation quality metrics (NLL, validity, stability, FID, diversity) with standard deviations, mirroring how controllability results are presented.
- Include a data augmentation baseline where additional labeled samples are synthesized for comparison.
- Ablate the constraint relaxation parameter ρ to show the trade-off between controllability and generation quality.
- Compare against a simple L2 regularization baseline on parameter distance to isolate the benefit of the dynamic gradient descent formulation.

## Removed Points

The following points from the reviewers were removed or downgraded per the rules:

- **"The novelty of the constraint optimization is modest and its relationship to prior work is understated"** — The critic's claim that this is similar to EWC/knowledge distillation is a genuine point about positioning, but the claim that the paper "does not discuss or compare against any regularization-based approach" veers into a "missing related work" criticism. Removed the "missing related work" framing but kept the substantive concern about missing simpler baselines (L2 penalty) in Minor weakness #5.
- **"Hyperparameters and reproducibility (missing typical values)"** — Kept under Minor (#7) but downgraded from the critic's framing. Missing hyperparameter values are a reproducibility concern but not a structural flaw.
- **"The unconditional pretraining baseline shows simple pretraining+finetuning itself is a strong baseline"** — This is a generic observation, not a weakness. If pretraining+finetuning were weak, the paper would have no baseline. The -finetune comparison is actually good experimental design that isolates the constraint's effect. Removed.
- **"Data augmentation cannot always replicate genuine data fidelity"** from the harsh critic's Other Observations intro — This is the paper's own argument, not a weakness. Removed.
- **Critic's point about "error bars overlapping" for time series frequency** — Partially valid but the paper shows clearer improvements on skewness and other properties. Downgraded from the critic's framing of "small and inconsistent" to a more nuanced Minor item (#4) focusing on motion where the issue is most pronounced.
- **Strengths from Strength Finder** — All five strengths were verified as substantive and specific; none were dropped as generic.

## Novel Insights

Beyond the paper's own contributions, the review process surfaces an important observation: the paper's constraint optimization is effectively a *parameter-space regularizer* for catastrophic forgetting during domain-specific finetuning, which is an underexplored approach in the text-to-data generation literature (most work focuses on architectural conditioning or data augmentation). However, the paper's lack of comparison to simpler regularization methods and the undisclosed label construction procedure prevent the reader from assessing how much of the observed gain comes from the sophisticated dynamic gradient descent versus simply keeping parameters close to the pretrained initialization.

## Suggestions

1. Disclose in detail how text descriptions are constructed for QM9 and Yahoo Finance. If they are template-based (e.g., converting numerical values to phrases), state this explicitly, provide the templates, and discuss the limitation relative to truly natural language.
2. Add full per-proportion tables for all generation quality metrics (NLL, validity, atom/molecular stability, FID, diversity) with standard deviations.
3. Include a data augmentation baseline as promised.
4. Compare against a simple L2 parameter-distance regularization (‖θ − θ_pretrain‖²) to isolate the benefit of the dynamic gradient descent.
5. Provide the ranges or typical values used for hyperparameters (α, β, γ, ρ, ω, p_uncond).

## Score and Decision

The paper addresses a real problem and proposes a technically sound approach with theoretical grounding. However, three major empirical gaps (undisclosed label construction, unreported generation quality tables, missing data augmentation baseline) significantly weaken the evidence for the paper's claims. The modest and sometimes non-significant improvements for motion further temper enthusiasm. The paper has clear potential but is not ready in its current form.

**Originality**: Moderate — the two-stage framework with constraint optimization is a reasonable combination of existing ideas, though the specific instantiation (lexicographic optimization with dynamic gradient descent) is novel in this application context.

**Importance**: Medium — low-resource text-to-data generation is a relevant problem, but the paper's focus on modalities where labels must be synthetically constructed weakens the direct practical applicability.

**Soundness**: Below threshold — the undisclosed label construction and missing data for generation quality metrics are significant empirical gaps.

**Clarity**: Adequate — the method description and theoretical section are clear, but the experimental section has important omissions.

**Value**: Moderate — the method and theoretical analysis could be useful after addressing the empirical gaps.

Score: 5.0 (marginally below acceptance threshold; would need the major weaknesses addressed to be a strong 6).

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>