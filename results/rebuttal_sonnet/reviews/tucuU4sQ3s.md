## Summary

NuSA-CL proposes a memory-free continual learning framework for CLIP-based VLMs. The method uses a three-stage cycle—SVD-based null space identification, constrained low-rank adaptation (ΔW = U_n M V_n^T with U_n, V_n frozen), and weight merging—repeated per task. It achieves state-of-the-art among storage-free methods on the MTIL benchmark with only 1.5M trainable parameters and 1.21 GPU-hours, while remaining competitive with storage-based methods at dramatically lower cost.

---

## Rebuttal Assessment

### Weakness 1: Missing matched-parameter-count baseline
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly points to Figure 3a as a within-framework parameter-matched control: Tail, Top, and Random subspace variants share the exact same architecture (frozen basis, trainable M ∈ ℝ^{r×r}) and therefore the same parameter count at every rank. The paper confirms this at r=128: Tail achieves 2.57% forgetting vs. 4.44% (Top) and 4.57% (Random). Since parameter count is held constant, this isolates subspace choice as the driver. This is a genuine partial refutation — the subspace choice does matter independently of capacity. However, the author honestly concedes the cross-architecture comparison (standard LoRA at r≈16 matching NuSA-CL's ~1.5M count) is absent, and this remains the more directly interpretable control for the claimed advantage over LoRA/MiLoRA in Table 1.
- **Score impact:** Weakness downgraded (from the only major weakness to a partially resolved concern)

### Weakness 2: Cross-task protection mechanism not made explicit
- **Author's response:** Partially address
- **Assessment:** Partially convincing — Verified in paper: Section 3.3 states the model "is always adapting in directions that are least disruptive to its full, accumulated knowledge" and Section 6.1 states NuSA-CL "integrates new knowledge by expanding into low-energy subspaces rather than overwriting dominant principal components." Figure 2's empirical signature (progressive rank increase) is present. However, the causal chain—that merging ΔW_t = U_n M_t V_n^T promotes those directions into W_t's principal spectrum, making the next null space geometrically disjoint from task-t's encoded directions—is not written out step-by-step anywhere in the paper. The author acknowledges this explicitly. Promises to add 2–3 sentences do not count.
- **Score impact:** Weakness unchanged

### Weakness 3: 10-step CIFAR-100 Avg. result not discussed
- **Author's response:** Partially address
- **Assessment:** Partially convincing — Author correctly verifies the numbers from Table 3 (ZSCL 82.15% vs. NuSA-CL 80.25% Avg. at 10 steps) and acknowledges Section 5.2's one-sided framing. The data is in the paper (Table 3 is fully visible) but the discussion in Section 5.2 never acknowledges the case where ZSCL wins on Avg. The author's explanation—that NuSA-CL wins on Last at 10 steps and catches up at 20+ steps—is consistent with the data. This is an honest acknowledgment of a transparency gap in the writing, not a methodological flaw.
- **Score impact:** Weakness unchanged (writing-level issue, no new experiments)

### Weakness 4: "Null space" vs. "approximate null space" terminology
- **Author's response:** Partially address
- **Assessment:** Convincing — Author correctly identifies the inconsistency: Section 3.1 heading uses "Intrinsic Null Space," Sections 3.3 and 6.1 use "intrinsic null space," while the abstract and Section 3.2 use "approximate null space." The paper text confirms this (Section 3.1: "Identifying the Intrinsic Null Space"; Section 3.3: "identify a new intrinsic null space"). The fix is a terminology replacement with zero impact on any result. Author acknowledges it straightforwardly.
- **Score impact:** Weakness unchanged (trivial terminology, acknowledged but not yet fixed)

---

## Strengths
- **Novel persistent constraint formulation**: Eq. 3 freezes U_n, V_n and trains only M ∈ ℝ^{r×r}. Table 4a confirms this is critical: unfreezing both bases drops Transfer from 68.58% to 62.60%, a 6-point gap that directly validates the design.
- **Strong efficiency-performance tradeoff**: Table 1 shows NuSA-CL reaches 68.6/75.1/82.8% Transfer/Avg./Last at 1.5M parameters and 1.21 GPU-hours, outperforming all storage-free competitors and approaching MoE-Adapters at 40× fewer parameters.
- **Scalability in long sequences**: Table 3 shows consistent improvement over ZSCL at 20-step (Last: 73.84% vs. 69.58%) and 50-step (Last: 71.85% vs. 67.36%), with the gap compounding with sequence length.
- **Empirical spectral signature**: Figure 2 shows monotonically increasing effective rank (text: 57.9%→58.8%; vision: 51.8%→52.4%) across tasks for NuSA-CL, while LoRA and Full-FT remain essentially static (LoRA's vision output projection: 447.42→447.58). This quantitatively supports the "knowledge accumulation" rather than "overwriting" interpretation.
- **Well-controlled subspace ablation**: Figure 3a shows Tail consistently achieves the lowest forgetting at every tested rank (32, 64, 128, 196, 256), providing within-framework evidence that the null-space choice matters.
- **Honest theory framing**: Section 4.2 explicitly limits guarantees to parameter space and acknowledges the absence of function-level bounds.

---

## Weaknesses

### Fatal
None.

### Major
- **Absent cross-architecture matched-parameter LoRA baseline**: The paper does not run standard LoRA at r≈8–16 to match NuSA-CL's ~1.5M parameters. Figure 3a partially addresses this within the NuSA-CL framework (same parameter count, different subspace), showing subspace choice matters. But the direct comparison—standard LoRA at the same capacity as NuSA-CL—is missing. The rebuttal honestly concedes this gap. Without this experiment, the gap between NuSA-CL (68.6% Transfer) and LoRA (63.9% Transfer) in Table 1 is attributable jointly to subspace quality and reduced capacity, and cannot be cleanly separated. Figure 3a helps but does not fully close this.

### Minor
- **Implicit cross-task protection argument**: The geometric mechanism—merging ΔW_t promotes those directions into W_t's principal subspace, making subsequent null spaces structurally disjoint from prior-task knowledge—is not stated explicitly in Section 3.3 or Section 4. Figure 2 provides the empirical evidence, but the causal interpretation is left to the reader. Rebuttal acknowledges this and proposes a fix but does not implement it.
- **10-step CIFAR-100 Avg. case undiscussed in text**: Section 5.2 claims "The advantage of our method becomes increasingly pronounced as the task sequence lengthens" without acknowledging that at 10 steps, ZSCL achieves 82.15% Avg. vs. NuSA-CL's 80.25%. The full Table 3 is presented, so the result is not hidden, but the discussion is one-sided.

### Trivial
- **Inconsistent "intrinsic" vs. "approximate" null space terminology**: Section 3.1 heading and Section 3.3 use "intrinsic null space"; abstract and Section 3.2 use "approximate null space." The latter is more precise given ρ=0.95. Author acknowledges, promises fix.

---

## Nice-to-Haves
- Run LoRA at r≈8–16 to match NuSA-CL's ~1.5M parameter count; add as controlled baseline in Table 1 or an ablation. This single experiment would resolve the main attribution ambiguity.
- Add 2–3 sentences in Section 3.3 or 4.2 articulating the cross-task protection mechanism explicitly: after merging, null-space directions gain spectral energy and become part of the principal subspace of W_t, making the task-(t+1) null space geometrically disjoint from task-t's encoded knowledge.
- Add one sentence in Section 5.2 acknowledging the 10-step Avg. result and noting that NuSA-CL's advantage on Avg. materializes at 20+ steps.

---

## Novel Insights

The most genuinely novel mechanistic insight—present in the paper's results but not in its theoretical framing—is the spectral promotion loop: each merge step converts null-space directions into principal-subspace directions, ensuring that subsequent updates are structurally disjoint from all previously accumulated task knowledge. Figure 2's progressive rank increase is the empirical signature of this loop, and it constitutes a stronger and more elegant explanation of NuSA-CL's forgetting mitigation than the current theoretical framing (which bounds parameter-space interference without explaining the structural disjointness). The author's rebuttal correctly identifies this gap and concedes it is not written out explicitly in the paper. The within-framework subspace ablation (Figure 3a) is also a clean scientific contribution: by holding parameter count constant and varying only which spectral directions are used, it provides the clearest evidence in the paper that subspace geometry—not reduced capacity—drives forgetting reduction.

---

## Suggestions
1. Run standard LoRA at r≈8 or r≈16 (~1.5M parameters) and add to Table 1 or Figure 3b as the "LoRA-matched" baseline. If NuSA-CL still outperforms same-parameter LoRA, the null-space mechanism claim is substantially strengthened and the major weakness is resolved.
2. Add explicit cross-task protection mechanism in Section 3.3: "After merging ΔW_t into W_{t-1}, the update directions enter the principal spectrum of W_t; consequently, the null space of W_t is disjoint from the directions encoding task t's knowledge, and the cycle structurally prevents overwriting."
3. Revise Section 5.2 to acknowledge the 10-step CIFAR-100 Avg. result (ZSCL: 82.15% vs. NuSA-CL: 80.25%) and note that NuSA-CL's Avg. advantage materializes at 20 steps and compounds at 50 steps.

---

## Score and Decision

**Rebuttal impact assessment:**

The rebuttal is honest, measured, and technically accurate. On the major weakness (missing matched-parameter baseline), the author makes a legitimate partial refutation via Figure 3a—the within-framework subspace ablation does genuinely control for parameter count and isolates subspace choice. This was overlooked in the original review. This partially, but not fully, resolves the concern: Figure 3a compares Tail vs. Top vs. Random within NuSA-CL, not NuSA-CL vs. standard LoRA at matched capacity. The cross-architecture comparison is honestly conceded as absent.

On the other weaknesses, the author acknowledges but does not resolve: the cross-task protection mechanism is still implicit, the 10-step CIFAR-100 Avg. discussion is still one-sided, and the terminology is still inconsistent (promises to fix do not count). None of the rebuttal responses reveal new problems with the paper.

**Net effect:** The major weakness is slightly less severe given Figure 3a's within-framework evidence, but the cross-architecture experiment is still absent. The original score of 6.5 is appropriate; if anything, recognizing Figure 3a as a partial response to the parameter-count concern gives a slightly more favorable view, but not enough to move to 7.0 given the gap remains real.

**Final score: 6.5** — the rebuttal provides a legitimate but partial response to the key methodological concern via Figure 3a, confirms the paper's other strengths are real, and honestly acknowledges remaining gaps. The method is principled, the results are strong, and the efficiency story is genuine. The absence of a cross-architecture matched-parameter baseline remains the binding limitation.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>