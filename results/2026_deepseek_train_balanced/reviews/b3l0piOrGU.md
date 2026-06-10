Now I'll write the final merged review.

## Summary

This paper identifies and studies a "representation deficiency" in Masked Language Modeling (MLM): the [MASK] token consumes representational capacity in the encoder, leaving fewer effective dimensions for real token representations. The authors provide empirical evidence (effective rank analysis on a pretrained RoBERTa model) and theoretical analysis (showing that [MASK] token representations necessarily occupy subspaces disjoint from real token representations) for this phenomenon. They propose MAE-LM, which excludes [MASK] tokens from the encoder during pretraining (using a shallow decoder only for the prediction objective), and show consistent improvements over MLM baselines on GLUE and SQuAD.

## Strengths

- **Novel and well-motivated diagnosis of an underexplored issue.** Prior work noted the pretrain-finetune discrepancy of [MASK] tokens but focused on changing the training objective. This paper instead studies the *representation-level* consequence: by measuring the 0.9-effective rank of 5M tokens from a pretrained RoBERTa model with and without [MASK] tokens (Section 2.2), it demonstrates that dimensions active for [MASK] representations become inactive when [MASK] is absent, creating a measurable capacity reduction for real tokens.

- **Direct causal evidence via the δ-transition ablation.** The gradual-transition experiment (Section 4.3, lines 294–301) controls the fraction δ of [MASK] tokens included in the encoder and shows monotonic performance degradation as more [MASK] tokens are included. This provides strong causal evidence that the benefit of MAE-LM comes specifically from excluding [MASK] from the encoder, not from the auxiliary decoder.

- **Verification that the fix resolves the identified deficiency.** Section 4.4 (lines 303–309) directly measures the effective rank of MAE-LM's encoder representations and shows it closes the gap between "input with [MASK]" and "input without [MASK]" that existed in vanilla MLM. This links the proposed mechanism to the observed downstream gains rather than relying solely on aggregate benchmark numbers.

- **Comprehensive ablation studies.** The paper systematically ablates decoder size, attention configuration, position encoding strategies, and alternative ways of handling [MASK] tokens, clearly ruling out confounders (e.g., the "enc. w. [MASK] + dec." baseline confirming that simply adding a decoder without excluding [MASK] does not help).

## Weaknesses

### Fatal
None.

### Major
None. The core empirical claims are well-supported by the evidence presented.

### Minor

- **The theoretical proof in Lemma 1 contains a non-rigorous step.** The proof argues that rank(bs{P}) ≤ d − rank(bs{E}) because position and token embeddings "encode disjoint information and are learned in separate subspaces" (lines 141–142). The cited works (he2020deberta, Ke2021RethinkingPE) show empirical evidence for decoupled positional and content information but do not establish a formal rank inequality of this form. However, this does **not** undermine the paper's empirical findings or the MAE-LM method, and the conclusion (that bs{H}_ℳ^0 is low-rank) can be justified via a simpler argument: rank(bs{P}) ≤ sequence length (≤ 512) ≪ d = 768 regardless. The gap is in the presentation of the proof, not in its conclusion.

- **The "40% of pretraining time" claim is underspecified as to whether the final benefit is efficiency or representation quality.** The paper states that MAE-LM "takes slightly more time than RoBERTa when trained on the same amount of data, but to reach RoBERTa's MNLI accuracy, MAE-LM only needs about 40% of its pretraining time" (line 251). This is an efficiency advantage (converging faster) and does not by itself indicate that MAE-LM reaches a *higher* final accuracy. The paper should clarify whether the benefit is faster convergence, higher final accuracy, or both.

- **The empirical comparison for the base++ (160GB) setting is incompletely specified.** The paper clearly re-implements and fine-tunes RoBERTa under identical conditions for the base (16GB) setting (line 242). For the base++ setting, it is ambiguous whether the RoBERTa baseline numbers are from the original RoBERTa paper or were also re-implemented. Since the paper's core comparative claim is that MAE-LM "outperforms MLM-pretrained models," full transparency about which baselines are directly comparable is important.

- **The evaluation is restricted to 12-layer base-scale models.** The paper acknowledges this limitation (line 344) but does not discuss whether the representation deficiency amplifies or diminishes at larger scales (e.g., BERT-large or RoBERTa-large). Since rank is a function of model dimension, the severity of the identified issue at scale is an open question that would strengthen the paper's significance.

### Trivial

- None beyond the above.

## Nice-to-Haves

- Studying the relationship between masking ratio and the magnitude of representation deficiency (e.g., whether the effect scales proportionally with masking ratio or has a threshold behavior).
- Adding one or two more fairly re-implemented baselines (e.g., BERT under the same codebase) to strengthen the comparative claims.
- Providing confidence intervals or variance metrics for the main results in addition to medians.

## Removed Points

The following points from the input reviews were removed with justifications:

1. **"Missing main results table and inability to verify improvement magnitude"** — Removed because the tables are included via `\input{}` commands that the PDF parser strips; they exist in the original submission. This is a known parser artifact, not an author error.

2. **"Over-interpretation of effective rank finding as causal"** — Removed because the paper does not claim the effective rank analysis alone proves causality; it is presented as empirical evidence, and the theoretical analysis (Theorem 1) provides a separate formal argument for the causal mechanism.

3. **"Reproducibility concern about undisclosed hyperparameters / implementation details"** — Removed per instructions about parser-level reproducibility nitpicks. The paper describes pretraining and fine-tuning settings in adequate detail for its scale.

4. **"Missing out-of-domain or more recent benchmarks (SuperGLUE)"** — Removed as scope creep. The paper uses the standard benchmarks (GLUE, SQuAD) for the models and era it targets, and this does not undermine the core claims.

5. **Strength: "Formal theoretical proof"** — Weakened to "theoretical analysis providing a formal framework" because the non-rigorous step in Lemma 1 means the proof is not fully formal as presented. This does not detract from the overall value of the theoretical framing.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

- **Clarify the Lemma 1 proof.** The rank bound for position embeddings can be simplified: rank(bs{P}) is bounded by the number of positions (≤ 512), which is far less than the model dimension (768). This avoids the contested subspace argument while reaching the same conclusion.

- **Clarify the base++ comparison.** Explicitly state whether the RoBERTa (base++) numbers are from the original paper or were re-implemented, and if the latter, ensure the same pretraining budget, data, and fine-tuning protocol.

- **Clarify the "40% time" claim.** Specify whether MAE-LM converges faster to a similar final accuracy, reaches a higher final accuracy, or both. This distinguishes efficiency benefits from representation quality benefits.

- **Add a brief discussion of masking ratio's role.** Even a short comment on whether the deficiency scales with the masking ratio would help readers gauge the generality of the finding.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>