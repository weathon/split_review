## Summary

LoLoRA is a parameter-efficient fine-tuning method that modifies LoRA by replacing gradient-based updates to matrix A with forward-pass-only local (Hebbian PCA) updates, thereby eliminating the need to store A's input activations during backpropagation. The paper proves (Theorem 4.4) that under an i.i.d. Gaussian random regression model, the optimal frozen-A initialization is a nonsingular transformation of the top-r eigenvectors of the input covariance, theoretically grounding the EVA approach and motivating online HPCA adaptation. Experiments across RoBERTa-large (GLUE), LLaMA-3.1-8B (GSM8K), LLaVA-v1.5-7B (Visual Instruct), and TinyLlama-1.1B (Alpaca ablations) show LoLoRA matches or slightly exceeds LoRA-FA (EVA) while saving activation memory relative to full LoRA.

---

## Strengths

- **Theorem 4.4 provides a concrete theoretical grounding for PCA-based A adaptation.** The proof formally establishes that under the random regression model, the optimal A spans the dominant eigensubspace of the input covariance, directly justifying EVA-style initialization and HPCA convergence. The asymmetry result (Theorem 4.5, showing no analogous "good" initialization exists for B) is a useful complementary insight.
- **Memory savings are real and replicated across settings.** Table 3 (LLaMA-3.1-8B, GSM8K) shows both LoRA-FA and LoLoRA reduce extra memory from 30 GB → 26 GB (~13% reduction) compared to standard LoRA, while matching full LoRA accuracy (0.829 ± 0.004 vs. 0.821 ± 0.005).
- **LoLoRA avoids EVA's separate pre-computation pass.** Table 4 shows EVA initialization adds ~39 minutes of run time (3h 24m vs. 2h 45m for uniform LoRA); LoLoRA HPCA with uniform init runs in 2h 52m while reaching the same final loss as LoRA-FA (EVA). This is a practical, concrete advantage that the paper demonstrates.
- **Ablation (Table 5) corroborates Theorem 4.4.** EVA beats uniform, orthogonal, and PiSSA initializations for frozen-A across all tested ranks on TinyLlama/Alpaca, consistent with the theoretical prediction that PCA subspace initialization is optimal.
- **Ablation (Table 6) establishes that any PCA-convergent rule (HPCA, AE) works equally well**, ruling out sensitivity to the specific Hebbian rule. SoftHebb, which does not converge to the PCA subspace, is clearly worse, providing a meaningful negative control.

---

## Weaknesses

### Fatal
None.

### Major

- **The abstract overclaims performance relative to full LoRA.** The abstract states LoLoRA "maintains performance comparable to standard LoRA." Across Tables 1–2 (GLUE), LoLoRA HPCA is consistently below full LoRA on most tasks: CoLA 66.3 vs. 69.6, MRPC 89.9 vs. 90.9, MNLI 90.3 vs. 90.8. In Table 4 (LLaVA), LoLoRA achieves 2.93 perplexity vs. full LoRA's 2.90. Only Table 3 (GSM8K) shows a tie, and there LoLoRA ties with LoRA-FA (EVA) — not exclusively with full LoRA. The natural and honest framing is that LoLoRA is competitive with LoRA-FA (EVA), not with standard LoRA. This distinction matters because LoRA-FA (EVA) already exists and is simpler (no online update optimizer state). The abstract and conclusion should be recalibrated to match the actual comparison level.

- **The "further memory reduction" claim does not hold against LoRA-FA.** Table 4 shows LoLoRA HPCA at 24.1 GB while LoRA-FA (uniform/EVA) uses 23.9 GB — LoLoRA is *slightly worse* than LoRA-FA on memory in this setting due to the extra local optimizer state. The conclusion acknowledges "our method introduces a small amount of extra optimizer state," but the abstract claims "further reducing the memory required for fine-tuning" without qualification. The claimed advantage over LoRA-FA on memory is not consistent across all experiments and the framing is therefore misleading.

- **Unexplained failure of EVA for LoRA-FA on GLUE.** Table 1 shows LoRA-FA (EVA) at CoLA 64.7 vs. LoRA-FA (uniform) 67.9, and RTE 83.6 vs. 86.4 — EVA initialization clearly *hurts* on these smaller RoBERTa tasks. The paper notes "EVA initialization underperforms on this setting" but offers no analysis. This is surprising given Theorem 4.4 and Table 5's ablation, which find EVA best for frozen-A. A plausible explanation (small dataset size leading to unreliable covariance estimation, or mismatch between pre-train activations and fine-tuning distribution) would significantly strengthen the paper's narrative coherence. As written, this anomaly undermines confidence in the EVA/PCA theoretical story as a general principle.

### Minor

- **The online-adaptation advantage of LoLoRA over EVA is asserted but not empirically tested.** The paper's thesis for preferring online HPCA over offline EVA is adaptation to input distribution shifts during fine-tuning (mentioned in the abstract and Section 6). Table 6 shows HPCA (svd first) — equivalent to EVA — performs identically to HPCA (uniform), meaning no measurable benefit from online adaptation is detectable in the experiments performed. The claimed advantage is plausible but remains a hypothesis. A simple test under non-stationary conditions (sequential tasks, domain shift) would strengthen this claim considerably.

- **LLaVA validation is measured on a held-out slice of the same training pool** (Section 5.3: "1.5k samples held for validation" from the same 20% subset). This measures in-distribution fit rather than generalization. Given that the perplexity differences between methods are small (2.89–2.97), a downstream benchmark (e.g., MMBench, VQAv2) would clarify whether these differences matter for real capability.

### Trivial

- The conclusion states "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups." This is technically accurate (LoLoRA beats LoRA-FA *uniform* in GLUE and LLaVA) but potentially misleading since LoRA-FA (EVA) — the most relevant baseline — matches or beats LoLoRA in all three settings. The conclusion should clarify which LoRA-FA variant it is comparing against.

---

## Nice-to-Haves

- A wall-clock breakdown isolating the per-step HPCA overhead (beyond the aggregate run time in Table 4) would help practitioners understand how LoLoRA compares to both EVA (front-loaded cost) and uniform LoRA-FA (no extra cost).
- A non-stationary fine-tuning experiment (e.g., multi-domain sequential tuning or progressive domain shift) would directly test the theoretical motivation for online A adaptation over frozen EVA initialization — the one scenario where LoLoRA would have a structural advantage.
- Exact per-component memory accounting (activation memory, optimizer state for A, etc.) rather than single peak-GPU figures would make the memory trade-offs auditable.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's claim that "the specific mechanism of online HPCA adaptation provides no demonstrated benefit over offline EVA initialization."** This is a real empirical observation (Table 6 shows HPCA svd-first ≈ HPCA uniform), but framing it as a damaging weakness misrepresents the paper's stated contribution. The paper explicitly states "online methods have the advantage of not requiring a separate incremental PCA pass before training" — a practical benefit demonstrated in Table 4's run-time comparison. The paper does not claim HPCA is better than EVA in steady state; it claims it reaches the same subspace without pre-computation. This is addressed, not ignored.
- **Harsh critic's concern about gradient flow interaction between newly-updated A and B's gradient within the same forward-backward pass.** This is a reasonable implementation detail to clarify, but Algorithm 1 is self-consistent as written (u = Az is computed from A before local update, but used in line 5 after the update — the paper could clarify which A generates u; re-reading line 1-5, u is computed from old A, then A is updated, but B's gradient is computed w.r.t. u which was from old A). This is a minor notational gap, not a correctness issue.
- **Harsh critic's framing of Assumption 4.1 as "essentially incompatible with fine-tuning" and therefore a "fundamental issue."** The paper is transparent that this is a simplifying assumption; the conclusion acknowledges "isolated with stationary targets." The Gaussian assumption on ΔW₀ is a standard random-regression prior used to derive worst-case-optimal initializations when target structure is unknown. It does not claim ΔW₀ is actually Gaussian — it derives what to do when you have no information about the target. This is a limitation of scope, retained as a minor theoretical caveat, not a flaw invalidating the contribution.
- **Strength finder's claim about "consistent performance across diverse tasks."** While the paper covers three model/task combinations, the performance story is not uniformly consistent (EVA hurts on GLUE, memory gains are modest on LLaVA). This generic strength is partially contradicted by verified weaknesses and is therefore dropped.

---

## Novel Insights

The most genuinely novel observation is the theoretical characterization of the asymmetry between adapters A and B under information constraints (Theorems 4.4–4.5): when target structure is unknown, there exists an optimal class of A initializations (PCA eigenvectors) but no analogous preferred initialization for B. The corollary — that online PCA adaptation of A via HPCA reaches the same optimal subspace as offline EVA without a pre-computation pass — is a useful practical insight. The ablations (Tables 5–6) confirm this prediction cleanly: any rule converging to the PCA subspace works equally well, and SoftHebb (which does not) is clearly inferior. Together these results provide a coherent, testable theoretical framework for A initialization in frozen/locally-updated LoRA variants.

---

## Suggestions

1. **Recalibrate the abstract and conclusion** to compare primarily against LoRA-FA (EVA) as the natural baseline; claim parity with full LoRA only for GSM8K where it holds, or remove the claim.
2. **Address the EVA-hurts-on-GLUE anomaly**: discuss why EVA initialization degrades LoRA-FA on small RoBERTa tasks — likely covariance estimation noise with small data — and characterize when PCA initialization helps vs. hurts.
3. **Add a non-stationary experiment** (sequential or domain-adaptive fine-tuning) to test the distribution-shift motivation for online HPCA over frozen EVA.
4. **Provide per-component memory breakdown** to reconcile the "further reduction" claim with Table 4 results.
5. **Clarify in Algorithm 1** whether u (line 1) is computed from the pre- or post-update A for the purpose of B's gradient in line 5; a one-line comment suffices.

---

## Score and Decision

**Originality:** The combination of local Hebbian learning with LoRA is novel in the PEFT space, and the theoretical characterization of optimal A initialization is a genuine contribution. Score: 3/5.

**Importance:** Memory-efficient LLM fine-tuning is a highly relevant research direction. The advantage over EVA (no pre-computation) is practically meaningful. Score: 3/5.

**Claims well-supported:** The core claim (LoLoRA ≈ LoRA-FA EVA with no pre-computation overhead) is well-supported. The weaker claim (LoLoRA ≈ full LoRA) is not. Score: 3/5.

**Soundness:** Theory is mathematically clean under stated assumptions. Experiments are multi-setting and ablated. Score: 3/5.

**Clarity:** Paper is generally well-written and organized; Algorithm 1 and Figure 1 are clear. Score: 4/5.

**Community value:** Provides a useful theoretical lens on EVA and a practical variant; ablation results are directly usable. Score: 3/5.

The paper makes a real and publishable contribution, but the overclaiming in the abstract and the unexplained GLUE anomaly both need to be resolved in a revision. It is an accept-borderline paper that should be revised to match its claims to its results.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>3</community_value>
</subscores>