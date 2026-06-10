## Summary

LOIRE presents a framework for lifelong learning of PLMs via incremental model growth across all four Transformer dimensions (hidden, FFN, MHA heads, layers). It contributes (a) a plug-in layer growth operator with residual gating that preserves function at initialization, (b) a growth schedule combining all four dimensions, and (c) an iterative distillation strategy using previous-stage models as teachers to mitigate forgetting. Experiments on GPT-style and BERT-style models across five domains report a 29.22% FLOPs reduction versus retraining baselines with comparable or better downstream performance.

## Strengths

- **Plug-in layer growth operator (φ_layer)**: The paper introduces a novel depth-growth operator that replicates a selected layer and inserts it with residual gating (Equation 12). Setting λ=1 at initialization skips the new layer entirely, achieving strict function preservation — a property theoretically proven in Equation 13. The empirical evaluation shows only a 0.09 PPL gap for this operator (Table 2), the smallest among all growth dimensions, and the paper provides what it claims is the first empirical verification of function preservation in this setting. This is the paper's clearest technical contribution.

- **Iterative distillation with role-switching**: The method maintains all previous-stage models as a teacher set and allows intermediate models to switch between student and teacher roles across stages (Section 2.6). This directly addresses the teacher-student capacity gap problem (Mirzadeh et al., 2020) for the model-growth scenario where model size changes at each stage — a clean and well-motivated design.

- **Scalability demonstrated at 1.1B parameters**: LOIRE-1.1B grows from 177M to 1.1B parameters across five stages, achieving only ~6.22% AP increase over a same-sized model trained from scratch (Table 3). This shows the method works at a practically relevant scale, not just on toy models.

- **Operator initialization ablation**: The ablation (Figure 4) cleanly shows that function-preserving initialization yields substantially lower AP and AP+ at initialization than random or zero initialization for the extended parameters, providing causal evidence that the function-preserving design reduces the initial performance gap after growth.

## Weaknesses

### Fatal
None.

### Major

- **LiGO comparison is invalid**: The paper states (lines 282–285) that it could not reproduce LiGO's results and resorts to comparing against LiGO's published numbers. Cross-paper comparisons with different training setups, hyperparameters, and data mixtures are unreliable. The BERT-style evaluation (Table 6) therefore provides no meaningful evidence about LOIRE's relative performance against LiGO. The GPT-style evaluation against ELLE, Token-KD, and ER is independently valid, but this still compromises a significant portion of the experimental validation and weakens the claim that LOIRE is validated on two architecture families.

- **Function preservation gap contradicts the theoretical claim and is left unexplained**: The paper claims "strict function preservation" for all growth operators (Section 2.3), meaning the enlarged model should produce identical initial outputs to the smaller one. Yet the empirical evaluation (line 270) reports a 0.76 PPL gap for φ_hidden and a 0.09 PPL gap for φ_layer. The paper's only explanation is "there are still deviations in the outcomes of the experiment" — a restatement, not an explanation. If the operators are truly function-preserving, any non-zero gap demands an account (e.g., LayerNorm interactions, residual connections, or floating-point precision). This undercuts a core theoretical claim that the paper's framework rests on.

- **FLOPs savings claim is unverifiable on the critical question**: The 29.22% FLOPs reduction over GPT R (Table 4) is the headline efficiency result. However, the paper never clarifies whether these FLOPs include the forward passes through all previous teacher models during iterative distillation. Since the distillation loss (Equation 16) computes KL divergences against every prior model M^(1)...M^(t-1), the teacher forward-pass cost grows linearly with stages — by stage 5, the student is being distilled from 4 teachers simultaneously. If this overhead is excluded from the FLOPs accounting, the true computational cost could be substantially higher than reported, potentially eroding the claimed savings.

- **Growth schedule ablation is insufficient to support the "optimal" claim**: The abstract claims "the optimal expansion sequence," but the schedule ablation (Section 3.3, Table 7) tests exactly one alternative (full reversal) out of 24 possible permutations of the four growth dimensions. Two data points cannot determine optimality. The paper later acknowledges this is "empirical optimization" and defers theory to future work (line 202), but the abstract overclaims relative to the evidence presented.

### Minor

- **No statistical reporting**: Every result (pre-training perplexity, downstream accuracy, FLOPs) is reported as a single number with no variance, multiple runs, or confidence intervals. While single-run PLM training is common in the field, the absence of any uncertainty estimate makes it impossible to assess whether reported improvements (e.g., "AP+ decreases by 6.97 compared to ELLE") are meaningful or within training noise.

- **Key hyperparameters unspecified**: The λ decay schedule for the residual gate (Equation 12) — linear? cosine? stepwise? — and the β weights for multi-teacher distillation (Equation 16) — equal? decaying with teacher age? — are never specified, which hurts reproducibility and prevents readers from judging the method's sensitivity to these choices.

- **Novelty framing could be clearer**: Three of the four growth operators (φ_mha, φ_ffn, φ_hidden) are explicitly adopted from Gesmundo & Maile (2023) with no modification (line 136). The paper's introduction and abstract frame the operator set as a unified contribution, which could mislead readers about the scope of novel technical work. The genuine novelty is the layer operator, the schedule combining all dimensions, and the distillation strategy — but the presentation does not clearly delineate these boundaries.

### Trivial

- Training configuration details (optimizer, learning rate, batch size, warmup steps, total steps per stage) are absent from the main text, making reproduction difficult without guessing standard defaults.

## Nice-to-Haves

- A brief analysis of how the distillation cost scales with the number of stages (e.g., 20+ domains) would strengthen the practical applicability claims, since the method's efficiency motivation could be eroded in longer lifelong learning settings.
- Testing 3–4 schedule permutations (rather than just one reversal) would substantially strengthen the schedule claim without requiring a full factorial design.

## Removed Points

The following points from the input reviews were removed per filtering rules:
- "No separate Related Work section" — removed per rule against criticizing missing section structure; the paper does cite relevant work in the introduction and method sections.
- "The notation is unclear — the constraint notation is garbled by parsing" — removed as a parser artifact issue.
- "The column of bracket-enclosed equations is difficult to parse" — removed as a parser/formatting artifact that does not reflect the original submission.
- Criticisms about "no limitations section" — removed as a low-value structural observation, not a substantive weakness.
- The harsh critic's distillation scalability point was moved to Nice-to-Haves since the paper focuses on 5-stage growth, which is sufficient for the reported experiments.
- Several duplicate or overlapping critic points were merged into single entries (e.g., multiple mentions of missing hyperparameters were consolidated into one minor weakness).
- "Strengthening the Paper on Its Own Terms" items that duplicated already-listed weaknesses were removed.
- Generic strength-finder entries (e.g., "the paper addresses an important problem") were removed as superficial or not concretely evidenced.

## Novel Insights

The most striking observation emerging from the reviews is the tension between the paper's strict function-preservation theory and its own empirical evidence of non-zero PPL gaps (0.76 for φ_hidden, 0.09 for φ_layer). The paper treats this discrepancy as a casual observation rather than a problem to be resolved, yet the pattern is informative: φ_layer's residual-gating design yields near-perfect preservation (0.09 PPL) while φ_hidden's zero-padding approach produces a noticeably larger gap (0.76 PPL). This suggests the deviation source is operator-specific and likely diagnosable — possibly LayerNorm statistics being affected by the zero-padded dimensions in φ_hidden, whereas φ_layer's clean residual bypass is more robust. This is a research opportunity the paper misses. Separately, there is a genuine tension in the paper's architecture: iterative distillation using all previous teachers is expensive by design, yet efficiency is the paper's headline claim. Resolving how much of the 29.22% FLOPs savings is consumed by teacher forward passes would determine whether the claimed efficiency holds in practice.

## Suggestions

1. Report exactly which computational costs are included in the FLOPs calculation, especially whether teacher forward passes during distillation are counted. If they are not, recompute with them included.
2. Investigate and explain the function-preservation deviation — the 0.76 PPL gap for φ_hidden needs a root-cause analysis (LayerNorm? floating-point accumulation? implementation detail?).
3. Either reproduce LiGO properly with matched settings or remove the cross-paper comparison. The GPT evaluation against ELLE/Token-KD/ER is sufficient support for the main claims.
4. Reframe the schedule claim from "optimal expansion sequence" to "empirically effective schedule" given the minimal ablation, or add 3–4 more permutations.
5. Report results with at least 2–3 seeds, or provide a justification for why single-run reporting is acceptable at this scale.
6. Specify the λ decay schedule and β distillation weights in the final version.

## Score and Decision

Based on the above assessment: the paper has a genuinely interesting core idea (the plug-in layer growth operator with residual gating) and a coherent framework. However, the experimental validation has several significant gaps — an invalidated LiGO comparison, an unexplained function-preservation contradiction, unverifiable FLOPs accounting, a schedule claim unsupported by the ablation, and no statistical rigor. These problems are real but not individually fatal; the GPT-style evaluation (against ELLE, Token-KD, ER) is valid and shows promise. The paper would need major revisions to address these issues before being ready for a top venue.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>