Based on round 1, my initial bracket is **between 4 and 6**. LoLoRA is more theoretically grounded than weak LoRA variants (3.0–3.33), but its empirical gains vs. LoRA-FA (EVA) are limited. Let me read a couple of key anchors and narrow with round 2.Now I have enough to write the full review.

**Calibration comparison notes:**
- *EVA paper* (DM6Q45HWSk, avg 4.75, rejected): LoLoRA directly provides the theoretical justification EVA was criticized for lacking, and runs deeper experiments — clearly stronger.
- *LoRA-FA* (RbKThNNFxr, avg 5.33, rejected): LoLoRA adds theory + online adaptation + more experiments — stronger.
- *PaCA* (iYkhxre0In, avg 6.0, accepted): PaCA shows concrete, quantified training-speed and memory improvements over LoRA; LoLoRA's practical advantage over its primary baseline (LoRA-FA + EVA) is minimal — weaker than PaCA.

**Round 1 bracket: 4–6. Round 2 narrows to ~5.0** — better than the EVA/LoRA-FA rejected papers, but not at PaCA's level of demonstrated practical benefit.

---

## Summary

LoLoRA proposes to update the LoRA adapter matrix A during the forward pass via local Hebbian Principal Component Analysis (HPCA) rules, eliminating the need to store input activations for backpropagation through A. The paper provides a theoretical justification (Theorem 4.4) showing that the optimal A initialization — when target weight updates are unknown — spans the dominant eigensubspace of the input covariance, which is exactly where HPCA converges. Experiments across GLUE (RoBERTa-large), GSM8K (LLaMA-3.1-8B), LLaVA-v1.5-7B, and ablations on TinyLlama-1.1B show that LoLoRA matches or slightly exceeds LoRA-FA with uniform initialization, and performs roughly on par with LoRA-FA + EVA initialization.

---

## Strengths

- **Theorem 4.4 provides a genuine theoretical gap-fill:** The EVA paper (Paischer et al., 2024) lacked a theoretical justification for why PCA initialization of A is beneficial; LoLoRA provides an exact characterization: under random regression (Assumption 4.1), `arg min g(A) = {CQ_{*,r}^T | C nonsingular}`, i.e., the PCA subspace of inputs. This is a concrete, formal result that addresses a real open question in the LoRA literature.

- **Theorem 4.6 for the AE variant extends theory coherently:** The autoencoder loss `l(A) = E_z ||z - A^T Az||^2` is shown to have no spurious local minima and to converge to the dominant eigensubspace (Theorem 4.6 parts i, ii), directly supporting the HPCA/AE equivalence observed empirically in Table 6.

- **Experimental coverage is broad and honest:** The method is evaluated on three qualitatively different settings (NLU, reasoning, multimodal), with memory measurements and ablations. The results are reported with standard deviations over three seeds, and the paper is candid about LoLoRA not always outperforming full LoRA (Summary sections after Tables 1–2).

- **Table 6 ablation confirms the theoretical prediction cleanly:** HPCA, HPCA (svd first), and AE all reach essentially the same perplexity at every rank, consistent with Theorem 4.4's prediction that any method reaching the PCA subspace is equivalently good, while SoftHebb (which does not converge to PCA) is clearly inferior.

- **Online adaptation eliminates the EVA pre-computation pass:** On LLaVA (Table 4), LoRA(EVA) adds ~39 minutes vs LoRA(uniform), while LoLoRA HPCA adds only ~7 minutes — a meaningful practical advantage for practitioners who need PCA-quality initialization without a separate pass.

---

## Weaknesses

### Fatal
None.

### Major

- **The claimed "further reducing memory" in the abstract is contradicted by Table 4.** The abstract states LoLoRA "further reduc[es] the memory required for fine-tuning" (relative to LoRA-FA being the natural reference). In Table 4 (LLaVA), LoLoRA HPCA uses **24.1 GB** while LoRA-FA (uniform) uses **23.9 GB** and LoRA-FA (EVA) uses **23.9 GB** — LoLoRA is slightly *worse*. The conclusion acknowledges extra optimizer state for local updates, but this acknowledgment does not recalibrate the abstract's unqualified claim. The memory claim only holds in Table 3 (LLaMA) where both LoLoRA and LoRA-FA tie at 26 GB vs. 30 GB for full LoRA. The abstract must be corrected to: "LoLoRA achieves memory savings comparable to LoRA-FA" — not "further reducing."

- **The online HPCA update provides no demonstrated benefit over static EVA initialization.** Across all experiments: Table 3 (LoLoRA HPCA 0.829 = LoRA-FA EVA 0.829), Table 4 (LoLoRA HPCA 2.93 vs LoRA-FA EVA 2.92, within error), Table 6 (HPCA ≈ HPCA svd-first ≈ AE). The paper's central argument for preferring LoLoRA over LoRA-FA+EVA is that online adaptation tracks input distribution shifts — but no experiment actually tests a distribution-shift scenario (e.g., multi-task sequential fine-tuning, domain-adaptive fine-tuning). The result that LoLoRA ≈ EVA is equally consistent with the interpretation that the subspace itself is what matters, not whether it was obtained online or offline. Without a non-stationary or distribution-shift experiment, the one structural advantage of LoLoRA over EVA is entirely unvalidated.

### Minor

- **LoRA-FA(EVA) underperforms LoRA-FA(uniform) on GLUE (RoBERTa).** Tables 1–2 show LoRA-FA(EVA) consistently below LoRA-FA(uniform) (CoLA: 64.7 vs. 67.9; RTE: 83.6 vs. 86.4; SST-2: 96.3 vs. 96.7), which contradicts both Theorem 4.4 and Table 5's ablation showing EVA as best. The paper mentions this briefly ("EVA initialization underperforms on this setting") but provides no explanation. A likely cause — that small GLUE datasets lack sufficient samples for reliable covariance estimation — is plausible but not discussed. This limits confidence in the PCA-subspace hypothesis for small-data fine-tuning regimes and should be addressed.

- **Theorem 4.4's assumption (i.i.d. Gaussian ΔW₀) provides equal support for EVA and LoLoRA.** The result proves that PCA-of-inputs is optimal *when ΔW₀ has no task-specific structure*. This is acknowledged as a limitation ("isolated submodule with stationary targets"), but the more fundamental point is that the assumption is exactly the setting where A's subspace choice most matters — and it equally supports static EVA initialization as online HPCA. The paper should state this limitation more directly rather than framing Theorem 4.4 as specific justification for LoLoRA over EVA.

- **LLaVA evaluation uses held-out validation perplexity on the same instruction tuning pool (Section 5.3).** As the paper states: "1.5k samples held for validation" from the same "LLaVA Visual Instruct 150K" subset. This measures in-distribution fit rather than visual QA generalization. The differences between methods in Table 4 (perplexity range 2.89–2.97) may not correspond to meaningful capability differences on downstream VQA benchmarks.

### Trivial
None (parser artifacts are not paper errors).

---

## Nice-to-Haves

- A direct experiment in a non-stationary fine-tuning setting (e.g., continual learning across tasks, long-context fine-tuning where early/late layers see different effective distributions) would be the single highest-leverage addition to validate the online-adaptation thesis.
- Wall-clock overhead per step for HPCA updates reported separately from the total run time would help practitioners choose between LoLoRA (small per-step overhead, no pre-pass) and EVA (large pre-pass, zero per-step overhead) depending on training duration.
- Downstream benchmark evaluation for LLaVA (e.g., MMBench, VQAv2) would strengthen the multimodal claims.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Harsh Critic: "LoLoRA is presented as competitive with standard LoRA when it is really competitive with LoRA-FA(EVA)"** — Partially removed/merged. The abstract's "comparable to standard LoRA" is indeed an overstatement, and this is retained under the memory claim weakness. However, framing the *entire empirical contribution* as a framing error overstates the case; the paper does honestly report results in tables and summaries. Moved to context.

- **Strength Finder: "consistent performance across diverse tasks validates generality"** — Removed as generic. The paper does run three settings, but the result is consistently "on par with LoRA-FA(EVA)" — this is not a strength independent of the major weakness above.

- **Strength Finder: "memory savings with competitive performance on LLaVA"** — Removed as contradicted by a verified weakness (LoLoRA uses 24.1 GB vs LoRA-FA's 23.9 GB in Table 4).

- **Harsh Critic: "gradient flow interaction between freshly-updated A and B's gradient is undiscussed"** — Removed. Algorithm 1 shows u = Az is computed before A is updated (line 1 precedes line 4), and B receives gradient through u (the old A output). This is consistent and correct behavior; no undiscussed subtle interaction exists.

---

## Novel Insights

The most genuinely novel contribution is the clean formal unification of EVA initialization and HPCA online adaptation under the same theoretical framework (Theorem 4.4), showing that both are instances of maximizing eigenspace coverage of the input covariance under random regression assumptions. This provides, for the first time, a principled analytical justification for why PCA-of-inputs is optimal for A in the frozen-A setting — filling the gap that the EVA paper left open. The ablation in Table 6 then provides surprisingly clean confirmation: any rule converging to the PCA subspace works equally well, while a rule that does not (SoftHebb) is clearly worse. Together, these results suggest that *which PCA-subspace method* one uses matters less than *reaching the PCA subspace at all* — a practically useful and underappreciated insight for the broader LoRA-with-frozen-A literature.

---

## Suggestions

1. **Rewrite the abstract and conclusion** to remove the "further reducing memory" claim or qualify it precisely: LoLoRA uses slightly *more* memory than LoRA-FA in Table 4 due to optimizer state for local updates.
2. **Add a distribution-shift or sequential fine-tuning experiment** to test the core claim for online vs. offline PCA adaptation. This is the primary experiment that would upgrade the paper's contribution from "matches EVA" to "beats EVA when it matters."
3. **Discuss the GLUE/EVA anomaly** (EVA underperforms uniform on RoBERTa). A brief analysis of when EVA is and isn't reliable (small dataset, large model) would be broadly useful.
4. **Reframe primary comparison** explicitly as LoLoRA vs. LoRA-FA(EVA) throughout, not vs. full LoRA, to make the honest contribution clearer.

---

## Score and Decision

**Originality:** Moderate. The method is novel (HPCA for A in LoRA), and the theoretical result is a genuine contribution, but the technique is a close neighbor of EVA.
**Importance:** The problem (memory-efficient fine-tuning) is important. The specific contribution (online vs. offline PCA for A) is moderate importance.
**Claim support:** The theoretical claims are well-supported. The central empirical claim (online adaptation is better) is not supported — experiments show parity, not advantage.
**Experimental soundness:** Reasonable. Multiple settings, seeds, ablations. But the LLaVA metric is in-distribution only.
**Clarity:** The paper is clearly written. Algorithm 1 and Figure 1 are well-presented.
**Value to community:** The theoretical result (Theorem 4.4) filling EVA's gap is valuable. The method is practical and easy to implement.

**Anchor comparison:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| L-MSA (xi3sDtf8A0) | 3.0 | 1 | LoLoRA is clearly stronger: theory + multiple experiments |
| ALLoRA (7X65yoKl3Y) | 3.33 | 1 | LoLoRA stronger: better framing, theory, breadth |
| HoLoRA (igGeaxOiFM) | 3.0 | 1 | LoLoRA stronger |
| MoRA (SxOrhLuuVz) | 4.75 | 1 | LoLoRA comparable, slightly weaker in empirical differentiation |
| LoRA-FA (RbKThNNFxr) | 5.33 | 1 | LoLoRA stronger: adds theory + online adaptation |
| ReLoRA (DLJznSp6X3) | 5.75 | 1 | Roughly comparable; ReLoRA shows larger practical gains |
| EVA (DM6Q45HWSk) | 4.75 | 2 | LoLoRA clearly stronger: fills EVA's theoretical gap |
| PaCA (iYkhxre0In) | 6.0 | 2 | PaCA shows clearer/larger practical gains; LoLoRA is weaker |
| fD8Whiy7ca | 5.5 | 2 | Comparable overall quality |
| EigenLoRA (KxGGZag9gW) | 5.0 | 2 | LoLoRA roughly comparable or slightly stronger |

**Round 1 bracket:** 4–6.
**Round 2 narrowing:** LoLoRA is better than EVA (4.75) and EigenLoRA (5.0) due to theoretical rigor and broader experiments. It sits below PaCA (6.0) because the practical benefit over the primary baseline (LoRA-FA + EVA) is minimal, the memory advantage claim is partially false, and the key thesis (online > offline) is untested. Closest peers are LoRA-FA (5.33) and EigenLoRA (5.0) — but LoLoRA is more complete than both. Final score: **5.0**.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>