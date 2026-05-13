Now I have enough information to write the final review. Let me synthesize everything I've read.

Key findings from paper verification:
1. **Table 1 (LRA)**: Confirmed — the table contains rows for DSS, S4++, Reg. S4D, Spectral SSM, Liquid S4, S5, S4, and S4D, **but no row for HOPE-SSM**, despite the caption explicitly claiming it reports "our HOPE-SSM and other models" and the text claiming HOPE-SSM outperforms most. This is a genuine and significant problem.

2. **Memory trade-off**: The paper explicitly says in the footnote (line 365): "We acknowledge that when t ≥ n, we have H̄_{0,t} = 0, which means the LTI system has essentially no memory after time n." The harsh critic is right that this creates an asymmetry that deserves more analysis, especially for the noisy-sCIFAR experiment where with Δt=0.1 and n=64, the non-decaying window is only 640 of 2048 discrete steps — and the image pixels are in steps 0–1023, which lies outside the window seen from step 2047.

3. **Theorem 1 scope**: Correctly applies to random diagonal initializations (init₂-like), not to HiPPO-LegS (init₃) which is confirmed high-rank at initialization. The dynamic rank collapse for init₃ is only empirically observed; the theorem provides indirect motivation but not a direct explanation.

4. **Computational complexity**: Algorithm 1 has a FOR loop of n iterations over L-length vectors; the Õ(L+n) claim is parallel PRAM-model, not wall-clock FLOPs.

---

## Summary

HOPE-SSM proposes to parameterize LTI systems in SSMs via the Markov parameters of a finite Hankel matrix instead of (A, B, C), motivated by a theoretical framework connecting Hankel singular value decay to SSM expressiveness. The paper proves that random Hankel initializations have Ω(n) numerical rank almost surely (vs. O(n^β), β<1, for random (A,B,C) parameterizations), and that perturbation sensitivity is bounded by √n‖h−h̃‖₂ independent of parameter values (vs. a bound that scales with |b_jc_j|/|Re(a_j)|² for S4D). These results are empirically corroborated on sCIFAR-10 and noisy-sCIFAR-10. A third claimed benefit—performance on Long-Range Arena—is referenced in the text but **absent from the table in the submitted paper**.

---

## Strengths

- **Unified theoretical diagnosis via Hankel singular values**: The connection from ε-rank to ROM approximation error (via the Glover/Adamyan bound) provides clean, quantitative grounding for why rank matters and explains all three initialization behaviors (init₁/init₂/init₃) in a single framework. This is a genuine conceptual contribution not present in prior SSM literature.

- **Contrasting perturbation bounds (Theorems 2 and 4)**: The S4D bound depends on |b_jc_j|/|Re(a_j)|², which can be large for near-imaginary poles, while the HOPE bound is √n‖h−h̃‖₂, independent of parameter values. The lower-bound tightness result (Theorem 2b) strengthens the argument materially. These are mathematically concrete and directly contrasted.

- **Experiment II (noisy-sCIFAR) is a well-designed diagnostic**: The noise-padded sCIFAR-10 task is explicitly designed to isolate the memory property, and the impulse response decay plot (Figure 5, right) directly visualizes the theoretical prediction from eq. (10) — HOPE-SSM shows flat |y(t)| over [0,64] while S4D decays exponentially. This is one of the cleanest empirical demonstrations of an architectural property in recent SSM literature.

- **Parameter reduction with provable high-rank guarantee at initialization**: The paper proves (Theorem 3) that random Hankel matrices are high-rank almost surely, eliminating the need for HiPPO-style initialization engineering. Using n instead of 3n parameters per LTI layer (with a clear footnote that this doesn't compress the full model by 1/3) is an honest, useful design contribution.

---

## Weaknesses

### Fatal

- **HOPE-SSM results are absent from Table 1 (LRA)**: The paper's third and headline contribution—"our HOPE-SSM outperforms most sequential models on many tasks" in the Long-Range Arena—is unverifiable. Table 1's caption explicitly reads "Test accuracies in the Long-Range Arena of **our HOPE-SSM** and other models," yet the table contains only eight competitor rows (DSS, S4++, Reg. S4D, Spectral SSM, Liquid S4, S5, S4, S4D) with no HOPE-SSM entry. The bold/underline markers in the table assign best performance to Liquid S4 and S5, not to HOPE-SSM. Whether this is a parser artifact or a submission oversight cannot be determined from the text alone, but the primary empirical claim of Contribution 3 cannot be evaluated as submitted. This is the most consequential issue in the paper.

### Major

- **Memory advantage is a trade-off, not strict dominance — and the noisy-sCIFAR explanation is incomplete**: The paper acknowledges in the body (not just a footnote) that "when t ≥ n, we have H̄_{0,t} = 0, which means the LTI system has essentially no memory after time n." However, the analysis of the noisy-sCIFAR experiment does not confront this limitation head-on. With Δt = 0.1 and n = 64, the non-decaying discrete window is n/Δt = 640 steps. At the final classification step (discrete step 2047), this window covers steps 1407–2047, which is entirely within the noise-padding region (steps 1024–2047). The image pixels occupy steps 0–1023, all outside the non-decaying window as seen from step 2047. Yet the paper attributes the strong HOPE-SSM performance to "non-decaying memory." The actual operative mechanism (possibly the higher-rank expressiveness, or cross-layer composition effects) is not analyzed, leaving the central claim of Advantage III poorly supported for the specific experiment that is meant to demonstrate it.

### Minor

- **Theorem 1 (low rank of random systems) does not directly cover the practically important case**: Theorem 1 requires diagonal entries drawn from a distribution near the unit circle and i.i.d. Gaussian b_jc_j — conditions that match init₂ (random) but not init₃ (HiPPO-LegS). The paper uses Theorem 1 to argue that "high-rank systems are only scarce in the space of S4D model parameters," but the key empirical observation — that init₃ loses rank during gradient training (Figure 3) — is supported only empirically, not by Theorem 1. An argument connecting gradient dynamics to rank collapse for structured initializations would substantially strengthen the motivation.

- **Computational complexity claim is misleading in practice**: The Õ(L+n) complexity claim (line 339) is valid only in the parallel PRAM model with L independent processors. In GPU practice, the inner FOR loop of n iterations over L-length vectors yields O(nL) total FLOPs — the same as S4D's kernel computation. No wall-clock timing comparison between HOPE-SSM and S4D is provided, so the efficiency claim is unverified empirically.

### Trivial

- None beyond the above.

---

## Nice-to-Haves

- **Ablation on the memory window size**: A systematic study of how varying n and Δt (and hence the effective discrete memory window n/Δt relative to sequence length L) affects performance on noisy-sCIFAR-10 would help disentangle the memory mechanism from other factors.
- **Analysis of gradient-induced rank collapse**: Even a heuristic argument for why gradient descent on (A, B, C) tends to collapse rank for structured initializations (init₃) would strengthen the motivation for HOPE beyond what Theorem 1 provides.
- **Recurrent-mode inference cost**: A brief discussion of the numerical cost and stability of system identification required for autoregressive inference (mentioned in line 339) would be valuable, given that this use case motivates the SSM family.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic — "LRA table missing is almost certainly a parser artifact"**: The critic acknowledges this is likely a parser artifact yet still rates it as a fatal evidential issue. While the concern about missing results is valid (and retained as Fatal), the critic's own acknowledgment of the likely cause suggests it should not be treated as data fabrication or author misconduct. Retained as Fatal because the claim is still unverifiable, but not attributed to author bad faith.

- **Harsh Critic — "The memory advantage is buried in a footnote"**: After reading the text, the acknowledgment that H̄_{0,t} = 0 for t ≥ n appears in the main body (line 365), not merely in a footnote. The weakness about the incomplete explanation is retained (as Major), but the characterization that it is "hidden" is inaccurate.

- **Harsh Critic — "Continuous-time LTI Γ's impulse response may not inherit flatness from the Hankel parameterization"**: The paper shows empirically (Figure 5 right) that the impulse response |y(t)| is flat for t ∈ [0, n]. The theoretical claim follows from the Hankel structure (eq. 10) and is directly verified. The harsh critic's concern that the bilinear transform argument is not formally derived is a minor presentation gap but does not undermine the empirical result.

- **Harsh Critic — "O(nL) FLOPs / misleading complexity"**: Valid, but the paper's claim is technically correct in the PRAM model and the paper's own framing is about matching S4D's complexity class. Retained as Minor rather than Major.

- **Strength Finder — "Same computational complexity as S4D"**: Weakened given the Õ(L+n) vs. O(nL) FLOPs issue. Removed from strengths.

- **Strength Finder — "This paper addresses an important problem"**: Generic, removed per rules.

---

## Novel Insights

The observation that the space of (A, B, C) parameterizations is structurally hostile to high-rank LTI systems — shown via Theorem 1 in a quantitatively precise way — and that this fundamental geometric mismatch explains decades of HiPPO engineering effort, is a genuinely synthesizing insight. The dual result (Theorem 3) that random Hankel matrices lie in the complementary regime almost surely unifies initialization robustness and stability in a single parameterization. This is a more principled explanation for why HiPPO helps than any prior geometric or approximation-theoretic argument. The impulse response visualization (Figure 5, right) as a direct empirical probe of memory structure is also methodologically transferable to other SSM analyses.

---

## Suggestions

1. **Include the HOPE-SSM row in Table 1** — this is non-negotiable for evaluating Contribution 3.
2. **Reconcile the noisy-sCIFAR geometry with the memory window claim**: Either show (analytically or empirically) how the 640-step non-decaying window enables the model to remember information from steps 0–1023 via intermediate layers, or attribute the performance gain to high-rank expressiveness rather than exclusively to non-decaying memory.
3. **Add a wall-clock training throughput comparison** to support the efficiency claim.
4. **Clarify the scope of Theorem 1** explicitly: it characterizes random initializations, not structured (HiPPO) ones. State that the dynamic rank collapse for init₃ is empirically observed and that Theorem 1 provides complementary motivation but not a direct explanation.

---

## Score and Decision

**Calibration anchor comparison:**

| Anchor | Path | Avg Score | Comparison |
|---|---|---|---|
| Robustifying SSMs via Approx. Diag. (DjeQ39QoLQ) | DjeQ39QoLQ.md | **6.50** (Accept) | Most similar paper: also theoretical analysis of S4D's instability, novel method, LRA benchmark. That paper provides full LRA results; this paper does not. |
| SSMs comparable to Transformers (QFgbJOYJSE) | QFgbJOYJSE.md | **5.75** (Accept) | Theoretical SSM paper with clean experiments. Contributions comparable; this paper has stronger math but weaker empirical completion. |
| StableSSM (BwG8hwohU4) | BwG8hwohU4.md | **5.33** (Reject) | Also addresses SSM memory via reparameterization; that paper has full empirical results and still received 5.33. |
| On interplay of learning/memory in SSMs (hgjpO0H0id) | hgjpO0H0id.md | **4.00** (Reject) | Theoretical deep SSM paper, rejected. Less polished theory than this paper. |
| S7 SSM (4wtcXV0kbi) | 4wtcXV0kbi.md | **3.50** (Reject) | Novel SSM variant with stability proofs, but weaker. |
| Long-Context Linear System ID (2TuUXtLGhT) | 2TuUXtLGhT.md | **6.25** (Accept) | Theoretical systems paper with strong sample complexity results and complete experiments. |
| Low-Rank Adaptation expressiveness (likXVjmh3E) | likXVjmh3E.md | **6.50** (Accept) | Theoretical contribution to expressiveness of a parameterization; similarly structured. |
| SPikE-SSM (4ILqqOJFkS) | 4ILqqOJFkS.md | **3.67** (Reject) | SSM applied to spiking networks; weak baseline. |

**Positioning**: The paper's theoretical contributions (Theorems 1–4, Hankel SV framework) are at the level of DjeQ39QoLQ (6.5, Accept). The empirical execution, however, falls well short: the missing LRA row is the decisive differentiator. DjeQ39QoLQ has complete LRA results (87.6% average); this paper claims LRA superiority but cannot demonstrate it from its own table. The memory analysis gap for noisy-sCIFAR is also a step below the DjeQ39QoLQ standard. BwG8hwohU4 (5.33, Reject) had full experimental results and still was rejected; this paper's experimental section is weaker (missing primary benchmark). However, the theoretical depth here is notably higher than BwG8hwohU4.

**Final assessment**: The theoretical framework is genuinely valuable, and Experiments I–II are sound. But the missing LRA table row, which contains the main quantitative claim, is a submission-level failure that prevents acceptance in current form. The memory mechanism gap (Major weakness) would also need revision. Score: **5.0**, Reject.

## Score and Decision
**5.0 / 10 — Reject**

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>