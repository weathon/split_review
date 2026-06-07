Now let me produce the final, consolidated review.

## Summary

This paper proposes TAK (Task Arithmetic with KFAC regularization), a regularizer for task-vector fine-tuning that connects representation-drift penalties to the generalized Gauss-Newton matrix, approximated via Kronecker-Factored Approximate Curvature (KFAC). The method is designed to be *dataless* (no batch-level access to other tasks' data during fine-tuning), *O(1) in the number of tasks* via a Kronecker-factor merging heuristic, and *robust to task-vector rescaling* (eliminating held-out tuning). Experiments span vision (CLIP ViT-B/32, B/16, L/14 on 8 tasks), language (T5-base on 6 tasks), task addition, task negation, OOD detection, and efficiency analyses.

## Strengths

- **Dataless regularization matches or exceeds data-dependent baselines on both task addition and negation.** On ViT-L/14 task addition (Table 1), TAK achieves 91.6/99.3 (Abs./Norm.) at α=1 without any other-task data, surpassing the data-dependent τ-Jp at 90.9/98.3. On task negation (Table 2, ViT-B/32), TAK drives target accuracy to 3.4% while preserving control accuracy at 62.4%, beating τ-Jp's 6.7%/60.8%. This directly demonstrates that the KFAC approximation does not sacrifice performance relative to methods that require batched data access during training.

- **O(1) complexity via Kronecker accumulation with negligible empirical gap to O(T).** Section 3.4's merged regularizer (Eq. 8) aggregates per-task KFAC factors into a single surrogate. Table 3 validates this: the gap between the O(T) "Naïve Multi-Task FT" and O(1) "TAK" is at most 0.6 absolute points (ViT-B/32 best α: 86.6 vs 86.0), and on T5-base TAK actually edges ahead (78.7 vs 78.5).

- **Robustness to α eliminates held-out validation tuning.** Fig. 4a shows TAK maintaining near-peak accuracy across α ∈ [0, 2], while unregularized linear FT peaks sharply at α≈0.5 then declines. Table 1 quantifies this: TAK's gap between α=1 and best α is ≤0.3 points, vs 2.1 points for Linear FT and 41.5 points for Non-linear FT. No other method achieves this scale-invariance.

- **Practical efficiency.** KFAC estimation for all 8 vision tasks takes only 4 minutes (Fig. 6b, MC=1), using 128–256 examples per task (≈0.3% of the dataset). The paper also provides a thorough analysis of compression strategies (87% memory reduction with ~1-point accuracy loss, Fig. 7b) and scheduling (every 16 training steps with modest degradation, Fig. 8).

- **Clean theoretical reduction of representation drift to GGN curvature.** Sections 3.1–3.2 derive that the representation-drift regularizer simplifies to a quadratic form of the Jacobian Gramian, then identify this Gramian as an instance of the GGN matrix. This connects task arithmetic to the established second-order optimization literature (KFAC, Martens & Grosse, 2015), providing a principled foundation that prior dataless approaches (e.g., the diagonal GGN of Porrello et al., 2025) lack.

## Weaknesses

### Major

- **No statistical uncertainty in main results.** Tables 1, 2, and 3 report only point estimates without confidence intervals, standard deviations, or the number of random seeds. Variance *is* reported in the KFAC-estimation analysis (Fig. 7a: "variance across seeds increasing as the number of MC samples grows"), confirming the authors had multi-seed infrastructure but did not apply it to the headline tables. This is a meaningful gap because several comparisons are close: on ViT-B/16 Best α (Table 1), τ-Jp scores 88.6 vs TAK's 88.3; on normalized accuracy the gap is 98.7 vs 98.1. Without error bars, it is impossible to tell whether these differences reflect meaningful method-level variation or noise. This weakness is somewhat mitigated by the consistent pattern across three architectures and two settings (addition and negation), but the absence of variance reporting limits the precision of the central competitive claim.

### Minor

- **The "dataless" framing is overstated.** The abstract and contributions describe the method as "dataless" and "without using external data," but KFAC factors are computed from 128–256 examples per task (Section 4, Fig. 7a). The paper is transparent about this in the experimental section, and the key advantage is genuine: unlike τ-Jp, TAK does not need *batched access* to other tasks' data *during fine-tuning*. However, "dataless" as the headline term could mislead a casual reader into thinking zero data from any source is needed. More precise language — e.g., "decouples data access from fine-tuning" or "requires only a small pre-computation set" — would better match what the method actually does.

- **The accumulated regularizer heuristic (Eq. 8) lacks theoretical analysis.** Replacing ∑(B_t ⊗ A_t) with (∑B_t) ⊗ (∑λ_t A_t) is presented without any bound, condition, or analysis of approximation error. Table 3 shows that the empirical gap is small in the tested settings, but there is no discussion of when it might break down (e.g., when tasks have very different input statistics, making the averaged A factors unrepresentative). The paper calls this a "heuristic" and validates it empirically, which is reasonable for an engineering contribution, but the lack of any diagnostic (even a Frobenius-norm comparison) is a missed opportunity to guide future use.

- **Language results show a clear gap behind τ-Jp.** On T5-base (Table 3/Fig. 3), TAK achieves 78.7 vs τ-Jp's 81.3. The paper acknowledges this honestly ("textual domains may still benefit from even more accurate curvature estimation"), but the abstract and conclusions do not reflect this boundary on the claim of state-of-the-art performance. The paper is SOTA in vision but not in language, and this should be stated more explicitly in the high-level summaries.

### Trivial

- The GGN interpretation uses squared-error loss while training uses cross-entropy (Section 3.2, line 105). The paper is transparent about this approximation, but it means the "curvature" interpretation is not exact for the actual training dynamics. This is well-understood in the KFAC literature and is not a flaw of this paper in particular.

## Nice-to-Haves

- A diagnostic measuring the Frobenius-norm difference between the two sides of Eq. (8) across tasks would provide useful guidance for practitioners.
- A discussion of whether intermediate levels of forgetting (for task negation) are achievable by tuning β would be interesting, though the goal of negation is indeed to erase task information completely.
- The β regularization strength and exact checkpoint schedule are likely in the appendix (stripped from this version); if not, adding them to the main text would improve reproducibility.

## Removed Points

- **"Very low target accuracy (3.4%) raises question of whether method is too aggressive"** — The goal of negation is to erase task information; lower target accuracy is better. This does not indicate a problem. Removed.
- **"TaLoS results are partially indirect (taken from original paper)"** — This is standard practice when the baseline code is not available; the paper properly marks these with †. Removed.
- **"β hyperparameter not reported" and "checkpoint schedule unclear"** — These details are likely in the appendix (which was stripped per ICLR review format). Removed following instructions about missing appendix content.
- **"Scope of dataless claim relative to model size"** — The paper already discusses KFAC compression (Fig. 7b) and acknowledges quadratic scaling. Removed.
- **"Cross-entropy vs squared loss mismatch"** — The paper is transparent about this approximation (Section 3.2). Removed as the paper already addresses it.
- Generic strengths about "addressing an important problem" — Removed as lacking specific anchor in paper content.

## Novel Insights

The most interesting observation to emerge from the reviews is the tension between the paper's headline "dataless" claim and the reality that KFAC factors are data-derived — but this tension is productive rather than disqualifying. The paper's real contribution is a *new access pattern*: decoupling data usage from the fine-tuning step (pre-compute curvature statistics once, then fine-tune without data access). This is a genuinely useful design point that sits between fully data-dependent methods (τ-Jp) and purely parameter-space methods (TIES, TSV). The reviews' emphasis on the accumulated regularizer heuristic also highlights an underexplored direction: can the sum-of-Kronecker-products approximation be given theoretical grounding, perhaps via matrix nearness or operator norm bounds? The empirical results suggest the approximation is reliable in practice, which itself raises an interesting question about when and why Kronecker factors from different tasks share compatible spectral structure.

## Suggestions

1. Add multi-seed (3–5) statistics to Tables 1–3. The KFAC-estimation experiment (Fig. 7a) shows you have the infrastructure; apply it to the headline results.
2. Replace or qualify "dataless" in the abstract and conclusions with more precise language (e.g., "requires no data access during fine-tuning after a lightweight pre-computation step").
3. Include at least a simple diagnostic of the Eq. (8) approximation (e.g., Frobenius-norm ratio across tasks) to guide practitioners on when the heuristic is safe.
4. Acknowledge the language gap more prominently in the abstract/conclusions — the method is SOTA in vision but not in language.

## Score and Decision

### Calibration Process

**Round 1 (Bracketing):** I queried for task-arithmetic papers in bands (score<3.5), (3.5–7.5), and (>7.5).

- Low band: ATM (3.00), Compatible Specialization (3.40), Projected Subnetworks (2.00), Unified Delta Editing (2.33) — all clearly weaker, rejected.
- Middle band: τJp (6.00, Accept), Attention-only FT (6.25, Accept), Submodule Linearity (6.00, Accept), Realistic Evaluation (5.33, Reject).
- High band: Training on Test Task (8.00), Transformers Reasoning (7.60), ViT Registers (8.00), Strong Model Collapse (8.00) — fundamental-discovery papers not comparable in type.

**Round 1 bracket: 5.5–7.5.**

**Round 2 (Narrowing):** I queried for KFAC/curvature papers in (4.5–7.5) and task-arithmetic/dataless papers in (5.5–8.0).

Key anchors and comparisons:
- **τJp (6.00, Accept):** Direct predecessor. TAK addresses its main weaknesses (dataless, O(1), broader evaluation, cost analysis). **TAK is stronger.**
- **Attention-only FT (6.25, Accept):** Direct competitor. TAK has deeper theoretical grounding and broader experiments. **TAK is comparable or stronger.**
- **Submodule Linearity (6.00, Accept):** Similar topic. TAK has comparable quality. **TAK is comparable.**
- **TATR (5.75, Reject):** Marginal improvements, controversial claims. **TAK is clearly stronger.**
- **SINGD/KFAC-Inverse-Free (5.50, Reject):** Different focus (optimization, not task arithmetic). **Not directly comparable.**

**Final score: 6.5**

This reflects that TAK is a clear improvement over its accepted predecessors (τJp, Attention-only FT) — it solves real limitations (dataless regularization, O(1) complexity, broader evaluation) — but has presentation gaps (no error bars, slightly overstated "dataless" framing) that prevent it from reaching the 7.5+ tier of fundamental-discovery papers.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>