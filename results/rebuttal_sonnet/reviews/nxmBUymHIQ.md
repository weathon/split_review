Now I have a thorough understanding of both the paper and rebuttal. Let me write the updated review.

---

## Summary

LoLoRA proposes gradient-free, forward-pass updates to the LoRA adapter matrix A via Hebbian Principal Component Analysis (HPCA), eliminating the need to store input activations for A's backward pass. Theorem 4.4 proves that, under random regression assumptions, the optimal A initialization spans the dominant eigensubspace of the input covariance — the same subspace HPCA converges to — providing the theoretical justification that the EVA paper (Paischer et al., 2024) lacked. Experiments on GLUE (RoBERTa-large), GSM8K (LLaMA-3.1-8B), and LLaVA-v1.5-7B show LoLoRA matches LoRA-FA (EVA) quality while eliminating EVA's offline pre-computation pass, saving ~32 minutes in the LLaVA experiment.

---

## Rebuttal Assessment

**Weakness: Abstract's "further reducing memory" claim contradicted by Table 4**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly argues the intended reading is "further reducing memory relative to standard LoRA," not relative to LoRA-FA. The Conclusion does disclose "our method introduces a small amount of extra optimizer state for the local updates, unlike standard LoRA-FA" (Section 6). However, the abstract as written is ambiguous at best and misleading at worst: after describing a LoRA-FA-like mechanism, the phrase "further reducing" naturally reads as claiming additional savings over LoRA-FA. I verified the Conclusion text: it does contain the disclosure the authors cite, but the abstract text (line 9) still says "further reducing the memory required for fine-tuning" with no qualification. The promised revision is not present in the paper.
- **Score impact:** Weakness downgraded (from major to minor) — the logical reading is fixable, and the Conclusion's disclosure partially mitigates it. But the abstract is still wrong in the current paper.

---

**Weakness: Online HPCA provides no demonstrated benefit over static EVA initialization**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors correctly redirect to the concrete runtime advantage: LoLoRA HPCA runs in 2h 52m vs 3h 24m for LoRA-FA (EVA) in Table 4, a verified 32-minute saving. This is a real, already-demonstrated practical advantage that does not require a distribution-shift experiment to be valid. The original review acknowledged this in the strengths section ("Online adaptation eliminates the EVA pre-computation pass"). The rebuttal clarifies that the paper's empirical thesis is "matches EVA quality without the offline pass" — not "outperforms EVA on distribution shifts." The abstract's claim that the method can "adapt to input distribution shifts" (line 9) remains unvalidated experimentally, and the rebuttal honestly concedes this is future work. The Introduction's Section 3.2 claim about "adapt[ing] to input distribution shifts" is correctly identified by the reviewer as an unvalidated motivational claim.
- **Score impact:** Weakness downgraded — the authors clarify that the core empirical claim is more modest than the reviewer interpreted, and the runtime advantage is real. The weakness around the unvalidated distribution-shift narrative remains but is now clearly scoped as a limitation.

---

**Weakness: LoRA-FA(EVA) underperforms LoRA-FA(uniform) on GLUE — unexplained**
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The authors' claim that LoLoRA HPCA outperforms LoRA-FA(EVA) on "six of eight tasks" is verified: from Tables 1–2, LoLoRA HPCA beats or ties EVA on 7 of 8 tasks (ties on QQP; beats on CoLA, RTE, STS-B, QNLI, SST-2, MNLI within rounding; marginally loses on MRPC: 89.9 vs 90.0). The robustness-over-EVA point is legitimate. However, the authors still provide no mechanistic explanation for *why* EVA degrades on small-data GLUE, which the reviewer correctly flagged. The reviewer's hypothesis (unreliable covariance estimation with small GLUE datasets) remains unaddressed.
- **Score impact:** Weakness unchanged — robustness of LoLoRA over EVA is confirmed, but the lack of explanation for EVA's anomalous GLUE performance remains.

---

**Weakness: Theorem 4.4's assumption provides equal support for EVA and LoLoRA**
- **Author's response:** Partially address
- **Assessment:** Convincing — The authors correctly point to the Conclusion (Section 6): "This is in line with an effective data-driven initialization EVA… while we propose an iterative algorithm LoLoRA that leads to a similar subspace during training." The paper explicitly frames the theoretical result as a unifying justification for the entire class of PCA-of-inputs methods, not as proof that HPCA is superior to EVA. The reviewer's reading was correct that Theorem 4.4 supports both equally — and the authors confirm this is the intended framing. The practical distinction (eliminating the pre-computation pass) is argued on operational, not theoretical, grounds. This weakness was always more about framing than substance.
- **Score impact:** Weakness removed — the paper's framing in Section 6 already states this; the reviewer's concern was valid but already addressed in the paper itself.

---

**Weakness: LLaVA evaluation uses in-distribution perplexity only**
- **Author's response:** Acknowledge
- **Assessment:** Honest but unconvincing as a defense — The author correctly notes that the runtime comparison in Table 4 is independent of the evaluation metric. This is true. But the weakness stands: perplexity differences in the range 2.89–2.97 on in-distribution data do not establish meaningful capability differences. Downstream VQA evaluation is promised for a revision but not present.
- **Score impact:** Weakness unchanged.

---

## Strengths

- **Theorem 4.4 fills the EVA theoretical gap:** Proved that optimal A (under Assumption 4.1, i.i.d. Gaussian ΔW₀) must span the dominant eigensubspace of Σ_zz. Verified in paper: part (iii) gives `arg min g(A) = {CQ_{*,r}^T | C nonsingular}`, an exact characterization.
- **Theorem 4.6 (AE variant) is coherent and verified:** No spurious local minima (part i), global minimum at dominant eigensubspace (part ii). Table 6 empirically confirms HPCA ≈ AE ≈ HPCA(svd first), while SoftHebb (which does not reach PCA) is clearly worse.
- **Runtime advantage over EVA is real and verified:** Table 4 directly shows 2h 52m (LoLoRA HPCA) vs 3h 24m (LoRA-FA EVA) and 3h 30m (LoLoRA HPCA + EVA init). This 32-minute saving per training run is a genuine practical advantage.
- **Robustness over EVA on GLUE:** LoLoRA HPCA beats or ties LoRA-FA(EVA) on 7 of 8 GLUE tasks, recovering from EVA's anomalous degradation on this small-data setting.
- **Broad and honest experimental coverage:** Three qualitatively different settings, results with standard deviations over three seeds, candid reporting when methods tie.

---

## Weaknesses

### Fatal
None.

### Major

- **Online HPCA's "distribution shift adaptation" claim is stated but not experimentally validated.** The abstract (line 9) says the method "allowing it to adapt to input distribution shifts" and Section 3.2 frames the online update as the key advantage. No experiment tests a non-stationary or sequential fine-tuning scenario. The rebuttal honestly concedes this is future work. In all experiments, LoLoRA ≈ LoRA-FA(EVA) — consistent with the simpler explanation that reaching the PCA subspace is what matters, not how it was obtained. The paper's practical advantage is the runtime savings, but the stated motivating advantage (distribution adaptation) is unverified.

### Minor

- **Abstract "further reducing the memory" claim is misleading.** In Table 4 (LLaVA), LoLoRA uses 24.1 GB vs LoRA-FA's 23.9 GB. The intended meaning (further reducing relative to full LoRA) is clarified in the rebuttal and partially disclosed in the Conclusion, but the abstract as written creates a false impression. Revision is promised but not in the current paper.

- **EVA's anomalous underperformance on GLUE is unexplained.** The GLUE anomaly (EVA underperforms uniform on 7 of 8 tasks) is noted but not analyzed. No discussion of covariance estimation reliability with small datasets.

- **LLaVA evaluation is in-distribution perplexity only.** No downstream VQA benchmarks. Differences in the range 2.89–2.97 perplexity on held-out samples from the same instruction pool may not reflect meaningful visual QA capability differences.

### Trivial
None.

---

## Nice-to-Haves

- A distribution-shift or sequential fine-tuning experiment would validate the core design motivation for online vs. offline HPCA.
- An analysis of when EVA's covariance estimation is reliable vs. unreliable (e.g., as a function of dataset size) would be useful for practitioners.
- Downstream VQA evaluation (MMBench, VQAv2) for LLaVA.

---

## Novel Insights

The most genuinely novel contribution remains the formal unification of EVA initialization and HPCA online adaptation under Theorem 4.4, showing both are instances of maximizing eigenspace coverage of the input covariance under random regression assumptions. The rebuttal clarifies — and the paper's Conclusion confirms — that this unification is the stated theoretical goal, not a proof that one implementation is superior to the other. The ablation in Table 6 confirms the prediction cleanly: any rule converging to the PCA subspace (HPCA, HPCA svd-first, AE) performs equally; SoftHebb (which does not) is clearly worse. The practical upshot is that online HPCA provides PCA-quality initialization without a separate pre-computation pass, saving ~32 minutes per training run at modest per-step overhead — a useful, demonstrated, and verifiable operational advantage that the rebuttal correctly emphasizes as the primary practical claim.

---

## Suggestions

1. **Revise the abstract** to remove the misleading "further reducing memory" phrasing — the honest claim is "memory savings comparable to LoRA-FA, without a pre-computation pass."
2. **Add a non-stationary fine-tuning experiment** to validate the distribution-shift motivation, or revise the abstract/intro to remove the unsupported adaptation claim.
3. **Discuss the GLUE/EVA anomaly** — a brief analysis of covariance estimation reliability as a function of fine-tuning dataset size would be broadly useful.
4. **Add downstream LLaVA evaluation** (VQAv2, MMBench) to strengthen the multimodal claims.

---

## Score and Decision

**Post-rebuttal assessment:**

The rebuttal is honest, does not over-claim, and correctly points to the runtime advantage in Table 4 as the primary practical differentiator over EVA — which the original review already acknowledged. The rebuttal successfully:
- Clarifies that Theorem 4.4 is intended as a unifying result (weakness removed)
- Confirms the runtime advantage is real and already demonstrated
- Honestly concedes the distribution-shift experiment is missing

The rebuttal does not fix any weakness in the current paper. The abstract memory claim is still wrong. The distribution-shift experiment is still absent. The LLaVA evaluation is still in-distribution only. No revision is present in the paper.

The score remains at **5.0**. The paper is above the EVA paper (no theory, weaker experiments) and EigenLoRA (similar quality), below PaCA (clearer/larger demonstrated practical gains). The rebuttal clarifies without materially changing the assessment.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>