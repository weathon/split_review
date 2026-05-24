## Summary

This paper introduces NuSA-CL, a memory-free continual learning framework for vision-language models. The core idea is to identify an approximate null space of the current weights via SVD before each new task, then persistently constrain all low-rank updates to that subspace throughout training. After each task the update is merged into the backbone, maintaining a fixed parameter budget with zero storage growth. Experiments on the MTIL benchmark and CIFAR-100 CIL show that NuSA-CL achieves performance competitive with storage-based methods while using 40× fewer parameters (1.5M vs. 59.8M) and 3× less training time (1.21 vs. 3.42 GPU-hours), decisively outperforming other storage-free methods.

## Strengths

1. **Novel and principled mechanism: persistent null-space constraint.** Unlike prior SVD-guided methods (e.g., MiLoRA) that use the low-energy subspace only for initialization and let updates deviate, NuSA-CL freezes the null-space bases \(U_n, V_n\) throughout training. Table 4a verifies this design choice: unfreezing these bases drops Transfer from 68.58% to 62.60%, confirming that the persistent constraint is essential.

2. **Superior efficiency–performance trade-off.** NuSA-CL uses 1.5M parameters (40× fewer than MoE-Adapters' 59.8M), zero additional storage, and 1.21 GPU-hours, while achieving 82.8% Last accuracy — the best among all storage-free methods and competitive with expensive storage-based approaches (Table 1). This is not an incremental improvement; it is a step-change in resource efficiency.

3. **Thorough empirical validation of the core design.** The paper validates the null-space choice through subspace selection ablations (Figure 3a: *Tail* consistently yields lowest forgetting across ranks), hyperparameter robustness (Transfer varies by <1% across \(\rho=0.80\) to \(\rho=0.99\), Table 4b), and the null-space dynamics analysis (Figure 2) which shows that NuSA-CL accumulates knowledge by expanding into low-energy directions rather than overwriting principal components.

4. **Long-sequence scalability.** On the 50-step CIFAR-100 benchmark (Table 3), NuSA-CL achieves 71.85% Last accuracy, outperforming ZSCL by +4.49%. Appendix analysis confirms that the null-space ratio remains stable even after 50 highly correlated tasks, demonstrating that spectral collapse does not occur.

5. **Practical SVD overhead.** The SVD initialization takes under 1 minute per task, compared to ~81 minutes for InLoRA's data-dependent subspace computation (Table 4b). This makes the method practical for deployment.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No variance estimates for main results.** The paper reports only single-run point estimates for Tables 1, 2, and 3. Given that task order and random seeds can affect results (especially for the CIFAR-100 splits), providing standard deviations or confidence intervals over 3–5 runs would substantially strengthen the evidence for the reported improvements. This is the most significant methodological gap.

2. **Theoretical bound is well-scoped but does not directly control forgetting.** Lemma 1 and Theorem 2 bound the parameter-space inner product between successive weights and updates. The paper honestly acknowledges this is a "local stability condition rather than a full function-level guarantee" (Section 4.2). This is not a flaw in the paper — the theory supports intuition rather than proving forgetting bounds — but the theoretical section is appropriately modest rather than a central contribution.

3. **Missing explanation for "—" entries in Table 2.** The Aircraft Transfer row is blank for all methods. This is almost certainly because Aircraft is the first task (zero-shot CLIP accuracy: 24.3), but the paper does not note this, which may confuse readers.

### Trivial

- The "-" entries in Table 2 should be explicitly footnoted (Aircraft is the first task, so no prior transfer measure exists).

## Nice-to-Haves

- A small experiment on task-order sensitivity (e.g., swapping two tasks or permuting the MTIL order) would strengthen the claim of robustness. The paper already identifies this as future work.

- A brief discussion of why the Transfer metric (zero-shot on unseen tasks) remains high under null-space adaptation — connecting the spectral analysis to representation-level generalization — would be informative but is not required for the current claims.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Missing comparison to RanPAC/DAP baselines** — Removed: These methods modify the classifier head (random projections + prototypes) rather than the backbone encoder. The paper explicitly scopes itself at the "feature-encoding level" (Section 2.1, lines 52–53). Criticizing the absence of head-level methods under the "storage-free" umbrella is a category mismatch.
- **Transfer metric definition unclear** — Removed: The paper defines Transfer as "the zero-shot accuracy on unseen tasks" in Section 5.1. This is unambiguous.
- **Request for 100/200-step experiments** — Removed: Scope creep. The paper already evaluates up to 50 steps on CIFAR-100, which is substantially longer than most benchmarks in the literature.
- **Parser artifacts in figure captions** — Removed: These are PDF extraction artifacts, not author errors.
- **Theoretical analysis is underwhelming** — Downgraded to minor: The paper acknowledges the limitation, and the empirical results (not the theory) carry the contribution.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation that is not already present in the paper.

## Suggestions

1. Add standard deviations over multiple runs (3–5 seeds) to the main result tables. This is the single change that would most increase confidence in the results.
2. Add a footnote explaining the "—" entries in Table 2 (Aircraft is the first task).
3. Consider a brief task-order sensitivity study (at minimum, two permutations of the 11-task MTIL order) to address the acknowledged limitation.

## Score and Decision

**Calibration summary.**

**Round 1 (bracketing):** Queried for papers on continual learning for vision-language models with null-space or SVD-based adaptation.
- Weak anchors (avg <3.5): scores 2.0–3.0 — thin, poorly executed papers. NuSA-CL is far stronger.
- Mid anchors (avg 3.5–7.5): scores 4.67–6.50 — solid CL/VLM papers. NuSA-CL sits comfortably above most.
- Strong anchors (avg >7.5): scores 8.0–9.0 — truly exceptional papers with deep theoretical contributions or paradigm-shifting results. NuSA-CL is not at this tier.
- **Round-1 bracket: 5–7.**

**Round 2 (narrowing):** Searched within the bracket for CL papers using null-space, orthogonal projection, or SVD techniques.
- ICL-TSVD (5.50): Uses SVD truncation for CL classifiers. Less novel mechanism, weaker efficiency story. NuSA-CL is clearly stronger.
- Divide & Orthogonalize / LMSP (6.00): Orthogonal projection CL method. Comparable approach quality but weaker experimental rigor. NuSA-CL is somewhat stronger.
- RDAC (5.25): Null-space analysis framework, not a practical method. NuSA-CL is much stronger.
- C-CLIP (6.50): VLM CL via LoRA + contrastive distillation. Similar scope; NuSA-CL has a more novel core mechanism and more dramatic efficiency gains. Comparable or slightly stronger.
- PROOF (5.67): Task-specific projections for VLM CIL. Weaker evaluation, known inference-mismatch issues. NuSA-CL is stronger.
- **Narrowed bracket: 6.0–7.0.** The paper is clearly better than most anchors in the 5–6.5 range and comparable to the strongest (C-CLIP at 6.5). It does not reach the depth of EFC (7.0) or the theoretical+empirical breadth of the Function Vectors paper (9.0).

**Final score: 6.5** — a solid Accept. The paper introduces a genuinely novel mechanism, validates it thoroughly, and demonstrates a compelling efficiency–performance trade-off. The main actionable weakness (missing variance estimates) is addressable and does not undermine the core contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>