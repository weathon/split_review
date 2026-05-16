Now I have thoroughly verified all claims against the paper. Let me produce the final consolidated review.

## Summary

This paper proposes Text2Data, a two-stage diffusion framework for text-to-data generation under low-resource conditions where labeled text-data pairs are scarce. Stage 1 trains an unconditional diffusion model on all available (unlabeled) data using NULL-token conditioning to capture the marginal data distribution. Stage 2 finetunes this model on the limited labeled data using a lexicographic constrained-optimization objective that keeps parameters close to the pretrained space, mitigating catastrophic forgetting. Experiments across molecules (QM9), motions (HumanML3D), and time series (Yahoo Finance) with varying label proportions (2%–40%) show that Text2Data generally outperforms direct training on labeled data and naive finetuning without the constraint.

## Strengths

1. **Novel two-stage pipeline with a principled constrained-optimization objective.** The paper cleanly separates distribution learning (pretraining on all unlabeled data via Eq. 5) from controllable generation (finetuning with a lexicographic constraint). The constraint explicitly prevents catastrophic forgetting by keeping the finetuned parameters close to the pretrained space, which is a well-motivated design.

2. **Theoretical justification via generalization bounds.** Theorem 1 provides a confidence bound (derived from sub-Gaussian concentration) showing that the empirical optimal set from constrained finetuning covers the true optimal set with high probability. This directly supports the constraint formulation and its relaxation via hyperparameter ρ, giving the approach a theoretical grounding that goes beyond engineering intuition.

3. **Demonstrated effectiveness across three qualitatively different low-resource modalities.** The method is tested on molecules (graph-structured), motions (sequential 3D joint coordinates), and time series (1D numeric), each with a distinct baseline diffusion model (EDM, MDM, DiffTS). On molecules, Text2Data achieves up to 58% improvement in negative log-likelihood and 19% better validity over EDM-finetune. On time series, it consistently achieves lower MAE across all six properties and all label proportions in Table 2. On motions, it outperforms both MDM and MDM-finetune at most label proportions (8% and above), with average R Precision gains of 5.57% over MDM.

4. **Problem formulation that directly addresses a realistic and under-explored challenge.** The low-resource text-to-data setting (|D_p| ≪ |D|) is prevalent in scientific and structured-data domains but receives far less attention than high-resource text-to-image or text-to-speech. The paper clearly articulates why standard remedies (data augmentation, semi-supervised learning, transfer learning) each have specific limitations in this setting.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison against simpler regularization baselines.** The core claimed novelty is the lexicographic constrained-optimization objective. Yet the experimental comparison against "finetune" baselines (EDM-finetune, MDM-finetune, DiffTS-finetune) is effectively a comparison against unconstrained finetuning only. The paper does not compare against standard, well-known regularization strategies that could achieve similar effects with less complexity, such as:
   - L2 penalty on the parameter deviation from pretrained weights
   - Elastic Weight Consolidation (EWC)
   - Low-learning-rate finetuning (which already limits parameter drift)
   
   Without these baselines, it is impossible to determine whether the improvements come from the specific lexicographic constraint formulation (with its adaptive Lagrange multiplier λ) or simply from the generic benefit of preventing large parameter deviations from a good pretrained initialization. This is the most significant gap — it weakens the paper's central claim about the constraint optimization itself. A paper whose main contribution is a novel learning objective should demonstrate that this specific formulation outperforms simpler alternatives.

### Minor

2. **Naming inconsistency in Algorithm 1 between the defined losses and their computation.** In Eq. (8)–(9) (lines 92, 99), the losses are defined as: $\hat{\mathcal{L}}_1'(\theta) = \mathbb{E}[\|\epsilon_\theta(x^{(t)}, t) - \epsilon\|^2]$ (unconditional, the constraint) and $\hat{\mathcal{L}}_2(\theta) = \mathbb{E}[\|\epsilon_\theta(x^{(t)}, c, t) - \epsilon\|^2]$ (conditional, the objective). However, in Algorithm 1 (line 120), the computation is the reverse: it computes $\hat{\mathcal{L}}_2$ using the unconditional form $\|\epsilon_\theta(x^{(t)}, t) - \epsilon\|^2$ and $\hat{\mathcal{L}}_1'$ using the conditional form $\|\epsilon_\theta(x^{(t)}, c, t) - \epsilon\|^2$. The gradient update direction in line 101 then uses $\nabla\hat{\mathcal{L}}_2 + \lambda\nabla\hat{\mathcal{L}}_1'$, which — under the swapped naming — would put the unconditional loss (mislabeled as L₂) as the primary direction and the conditional loss (mislabeled as L₁') as the adaptively weighted term. This contradicts the intended optimization where L₂ (conditional) is the primary objective and L₁' (unconditional) is the adaptive constraint. This does not invalidate the method (the intent is clear from context), but it will confuse readers trying to implement the algorithm.

3. **Distributional mismatch in the constraint: the paper's justification relies on an unquantified approximation.** The constraint in Eq. (3) evaluates the unconditional loss on the labeled subset D_p's marginal, while the pretraining target ξ is the infimum on the full dataset D. The paper justifies this via the approximation in Eq. (6): $p_\theta(x) \approx \int p_\theta(x|c) p_{\mathcal{D}_p}(c) dc$, arguing that the unconditional model on D approximates the marginal of the conditional model on D_p. This is a reasonable heuristic, but the gap is not quantified. When the labeled subset's marginal distribution differs significantly from the full data distribution (which is plausible at very low label proportions), the constraint may be poorly calibrated. The paper would benefit from either an empirical analysis of this gap or a discussion of when it may become problematic.

4. **The mapping from extracted properties to "text descriptions" for the time series and molecule datasets is underspecified.** The paper states that features are extracted via tsfresh and then used as "text descriptions" (conditioned via T5 encoder). For molecules, properties like α, ε_HOMO, etc. are the "text." For time series, frequency, skewness, mean, etc. are extracted. It is unclear how these numeric/scalar values are converted into the natural language strings that the T5 encoder expects (e.g., are they formatted as "alpha=78.0"? Are normalized values used?). This matters because it affects the generalizability of the claimed "text-to-data" framing to settings with genuine free-form natural language descriptions.

5. **Ablation on the hyperparameters α, β, γ, ρ is absent.** The method introduces four hyperparameters (plus the unconditional training probability p_uncond) that control the adaptive Lagrange multiplier λ and the constraint relaxation. The paper does not report sensitivity to these choices, nor does it show how λ evolves during training. This makes it difficult for practitioners to understand how robust the method is and how to tune it for new modalities.

### Trivial

6. **Statistical significance not reported for main comparisons.** The paper reports standard deviations but does not provide p-values or confidence intervals. Many entries differ by 0.01–0.02 (within one standard deviation), particularly at higher label proportions where performance converges. While significance testing is not standard practice in all subcommunities, its absence here makes it harder to evaluate whether the claimed advantages at converged proportions are meaningful.

7. **The finite hypothesis class assumption in Theorem 1 is standard but the connection to neural network parameter counts is imprecise.** The paper correctly notes that log|Θ| is manageable (14M parameters), but strictly, |Θ| for a neural network is exponential in the number of parameters, not equal to it. This is a minor technical imprecision common in ML theory papers and does not undermine the bound's qualitative message.

## Nice-to-Haves

- Add comparisons against EWC, L2-penalized finetuning, and low-learning-rate finetuning to isolate the value of the specific lexicographic formulation.
- Show the trajectory of λ during finetuning to verify that the adaptive mechanism behaves as intended (constraint tightening as training progresses).
- Report ablation over α, β, γ, ρ (e.g., grid search on one modality) to establish practical robustness.
- Clarify the exact string format used to encode scalar properties into text inputs for the T5 encoder.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength Finder's "Clear problem formulation" (Strength 3 from Finder):** Generic; every acceptable paper states its problem. This is a baseline expectation, not a distinguishing strength. Moved here to avoid inflating the strengths list.
- **Critique that the theoretical bound "does not add unique insight":** The bound is a standard sub-Gaussian concentration bound, but the reviewer's characterization that it "does not add unique insight" is too harsh — the bound does connect the constraint relaxation (ρ hyperparameter) to the confidence interval (ε) from Theorem 1, which is a non-trivial link. This is better reflected as a minor note than as a weakness.
- **Complaint about not discussing EWC/SI/replay in Related Work (Section 3):** The paper is not a survey of catastrophic forgetting prevention methods; it is a new-method paper. The missing discussion is a scope-creep request, not a weakness.
- **Strength Finder's "clear problem formulation":** Generic, removed. 
- **Weakness claiming the t-SNE plot is "not a rigorous evaluation":** t-SNE visualization is a standard qualitative evaluation in time series generation literature (as cited by the paper's references). This is a methodological taste issue, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a key methodological gap (missing comparison with simpler regularization baselines) and a naming inconsistency in the algorithm, but do not contribute any novel insight about the method that the authors themselves did not identify.

## Suggestions

1. **(Highest priority)** Run the motion and molecule experiments with three additional baselines: (a) L2 penalty on ‖θ − θₚᵣₑ‖² from the pretrained model, (b) EWC, and (c) finetuning with a 10× smaller learning rate. If the proposed constraint matches or exceeds these, the contribution is strongly validated. If not, reframe the contribution around the two-stage pretrain+finetune paradigm rather than the specific constrained-optimization formulation.
2. Fix the naming swap in Algorithm 1 between $\hat{\mathcal{L}}_2$ and $\hat{\mathcal{L}}_1'$ to match the definitions in Eq. (8)–(9).
3. Clarify how extracted molecular/time-series properties are formatted as text strings for the T5 encoder.
4. Add a brief empirical analysis of the constraint behavior — show a plot of $\hat{\mathcal{L}}_1'(\theta)$ vs. $\hat{\xi}$ during finetuning to verify the constraint is active and working as intended.
5. Add an ablation table for α, β, γ, ρ on at least one dataset.

## Score and Decision

**Originality:** Moderate. The two-stage design is not entirely new, but the lexicographic constraint formulation for this specific problem is novel.  
**Importance of research question:** High. Low-resource text-to-data generation is practically important and under-studied.  
**Claims supported:** Partially. The central claim about the constraint optimization is weakened by missing comparisons against simpler baselines.  
**Soundness of experiments:** Adequate breadth (3 modalities) but the control experiment is insufficient to isolate the claimed contribution.  
**Clarity:** Generally clear, except for the named inconsistency in Algorithm 1 and the underspecified text encoding for time series/molecules.  
**Value to community:** Moderate. The two-stage approach itself (pretrain on unlabeled, finetune with constraint) is a reasonable recipe, but the specific optimization needs stronger validation.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>