Now let me compose the final review.

## Summary

This paper proposes TAK (Task Arithmetic with KFAC regularization), a method for weight disentanglement in task arithmetic that eliminates the need for external task data during training. The key insight is that representation drift regularization — which normally requires data from other tasks — can be reframed as a curvature matrix approximation problem. By connecting the Jacobian Gram matrix to the generalized Gauss-Newton (GGN) matrix, the authors apply Kronecker-Factored Approximate Curvature (KFAC) to build a practical regularizer. A Kronecker-factor aggregation scheme further reduces per-task storage and computation to O(1) in the number of tasks. Experiments on vision (8 Vision benchmark with CLIP) and language (6NLI with T5-base) show that TAK matches or exceeds the data-dependent state-of-the-art method τJp in task addition while being dataless, and outperforms it in task negation (unlearning). Additional analyses demonstrate robustness to α-scaling, task localization, and memory-efficient KFAC compression.

## Strengths

- **Elegant theoretical connection enabling a dataless regularizer**: The paper formally connects representation drift regularization to the GGN matrix (Section 3.2), showing that the Jacobian Gram matrix used to penalize drift is an instance of the GGN. This link allows the authors to leverage the well-studied KFAC approximation from second-order optimization — a transfer that is both principled and practical. The concrete value is demonstrated in Table 1: diagonal GGN achieves only 80.1% on ViT-B/32 versus TAK's 85.8%, confirming that structured curvature approximation matters.

- **Competitive performance without task data**: TAK matches or exceeds the data-dependent τJp on vision task addition (Table 1: ViT-B/32 85.8 vs 85.0 at α=1; ViT-L/14 91.6 vs 90.9) while being strictly dataless during training. On task negation (Table 2), TAK achieves lower target accuracy (better forgetting) and higher control accuracy than τJp across all three ViT backbones — a genuine advantage over the leading data-dependent method.

- **O(1) complexity via Kronecker-factor aggregation**: The accumulated regularizer (Eq. 8) merges per-task KFAC factors into a single surrogate, eliminating linear scaling with the number of tasks. Table 3 confirms marginal performance loss (86.0 vs 86.6 on ViT-B/32) relative to the idealized O(T) multi-task formulation, making the approach practical for many-task settings.

- **Robustness to task vector rescaling**: Figure 4a shows TAK maintains stable accuracy across a wide α range (0.25–1.75) on ViT-B/32, while competing methods (TSV, ISO, TIES) degrade sharply. This eliminates the need for validation-set tuning of α — a practical advantage when cross-task validation data is unavailable.

- **Thorough analysis supporting the method**: The task-localization analysis (Fig. 5, Fig. 13) provides clear empirical evidence that the regularizer confines each task vector's influence to its own input distribution. The extensive ablations on KFAC estimation (Fig. 7), MC samples, compression strategies (App. F.6), and the ImageNet-KFAC variant (Tab. 6) give a well-rounded picture of the method's practical behavior and robustness.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **No variance reporting on headline results**: Tables 1, 2, 3, 4, 6, and 8 report single-point accuracy numbers without seed-to-seed variability. The λ-ablation in Table 5 shows non-negligible variance can exist (e.g., ViT-B/32 at λ=1: 81.7±0.648). While this practice is common in the task arithmetic literature (the companion works cited follow the same pattern), for a paper making state-of-the-art claims, the absence of confidence intervals on the main results makes it impossible to assess whether margins over baselines are statistically significant. This is the most significant gap in an otherwise well-executed experimental section.

- **Non-linear regime extension lacks quantitative justification**: The paper acknowledges (line 613) that "our regularization is not theoretically exact in the non-linear regime" and justifies pairing with Attention-Only Fine-Tuning by citing that it "has been shown to induce approximately linear fine-tuning dynamics." However, no quantitative measure of how close attention-only fine-tuning is to linearization is provided (e.g., relative norm of the second-order term in the Taylor expansion). The empirical results on 8 Vision (Table 1, Fig. 2) suggest the combination works, but the hypothesis depends on the underlying fine-tuning method being sufficiently close to linear, which is not independently verified. The paper would benefit from either a quantitative characterization or tempering the claim about applicability outside the linearized regime.

- **"Dataless" framing is slightly overstated**: The method pre-computes KFAC factors from each task's data. While this can be done once and shared instead of raw data (and the paper acknowledges this in Sec. 3.1: "pre-computation – does not require further data access"), the abstract and introduction state "dataless approach" and "dataless regularization." Readers may infer that no data access is ever needed. The paper's own ImageNet-KFAC experiment (Tab. 6) shows that even a task-agnostic curvature prior works well, which actually strengthens the dataless claim, but the headline terminology could mislead. A more precise framing like "data-free during training" or "data-agnostic after pre-computation" would be more accurate.

- **Unvalidated assumption behind the accumulated regularizer's error bound**: The error bound in Appendix C (Eq. 18) scales with T·σ_A·σ_B, where σ_A, σ_B measure variance of KFAC factors across tasks. The derivation relies on the assumption that per-task factors cluster tightly around their means. For CLIP backbones this may hold, but the paper does not empirically verify this assumption (e.g., by reporting σ_A, σ_B for representative layers across the 8 Vision tasks). An empirical measurement would strengthen confidence in the approximation.

### Trivial
- The main text does not explicitly state which KFAC variant (Exact vs. MC) is used for the headline experiments. The information is present — Appendix E states "a single Monte Carlo sample" and Fig. 6b labels "MC=1 (ours)" — but stating this clearly in the main experimental setup (Section 4) would improve readability.

## Nice-to-Haves
- Testing TAK+Attention-Only on a non-vision benchmark (e.g., language tasks) to determine whether the non-linear regime benefit generalizes beyond the 8 Vision setting.
- Analyzing the variance of KFAC factors across tasks to empirically validate the error bound in Appendix C.
- Applying TAK to parameter-efficient fine-tuning (LoRA, adapters), which the paper identifies as future work.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"KFAC variant not stated in main text"**: The paper does state MC=1 is used (line 803, Appendix E, Fig. 6b). Removed because the information is present, though it could be more prominent.
- **"Missing comparison with τJp on normalized accuracy"**: The paper is transparent about τJp winning on some normalized accuracy metrics and explicitly states on language tasks that "τJp yields additional gains." Removed because the paper already addresses this honestly.
- **Various formatting/style nitpicks** from Section-by-Section Notes: removed per hard rules.

## Novel Insights

The most interesting tension across the reviews and the paper itself is between the "dataless" framing and the reality of pre-computation. TAK truly is data-free *during training*, but the KFAC pre-computation step still requires task data. However, the paper's own ImageNet-KFAC experiment (Tab. 6) suggests that even this coupling can be broken: a single curvature prior computed on generic image data recovers 97-99% of the per-task KFAC performance. This finding — that curvature structure is largely task-agnostic for vision backbones — is itself a non-trivial insight with implications beyond task arithmetic (e.g., for second-order optimization and Laplace approximation). The reviews did not fully explore this result's significance; it suggests the method could be made truly data-agnostic at all stages with minimal loss, which is a stronger position than the paper itself stakes out.

## Suggestions
1. Report standard deviations over at least 3 seeds for the main results (Tables 1, 2, 3) in the final version.
2. Clarify the "dataless" terminology — e.g., "data-free during training" or include a short caveat in the abstract about pre-computation.
3. Either add a quantitative measure of linearization closeness for attention-only fine-tuning, or soften the claim about the non-linear regime.
4. Empirically verify the KFAC factor variance assumption (report σ_A, σ_B for a representative layer) to validate the error bound in Appendix C.

## Calibration Anchors

- **tcuaVzKm3e** (Task Vector Bases, avg 3.33): Task vector compression framework with weaker theoretical grounding and less thorough experiments than the current paper. The current paper is significantly stronger.
- **fObtmKj0Ok** (Model Merging beyond Image Classification, avg 3.60): Extends merging to non-classification tasks; solid but narrower contribution. Current paper has deeper theory and cleaner results.
- **IBRldWTC3F** (PAVE, avg 4.00): Data-dependent task vector purification for merging. Current paper's dataless property and curvature connection make it more novel.
- **4UQt76OlL6** (OTMF, avg 2.67): Continual merging via optimal transport; requires labeled data and has presentation issues. Current paper is substantially stronger.
- **iU026Hr90y** (One Model for All Tasks, avg 5.00, Accept): Multi-task planning with MoE; different domain but similar quality. Current paper is comparable or slightly stronger in theoretical depth.
- **yxEop1S5le** (Gauss-Newton for LLMs, avg 6.50, Accept): Curvature-theme paper on LLM optimization; establishes an oracle upper bound. Extremely well-executed. Current paper is similarly rigorous but on a different problem — both are accept-level work.
- **jdL6WB5jHZ** (Regularized Latent Dynamics, avg 6.50, Accept): Behavioral foundation models with representation regularization. Different domain; similar quality of exposition and experimentation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>