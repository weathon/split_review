## Summary
The paper proposes LoLoRA, which augments LoRA-FA (frozen A, gradient updates only on B) with gradient-free Hebbian/PCA-style local updates of A during the forward pass, so that input activations need not be retained for A's backward pass. A theoretical result (Thm. 4.4) characterizes the optimal frozen A under an i.i.d. Gaussian random-regression assumption as a nonsingular linear transformation of the top-r eigenvectors of the input covariance — coinciding with the EVA initialization. Experiments span GLUE/RoBERTa-large, MetaMathQA/LLaMA-3.1-8B, LLaVA-v1.5-7B, and TinyLlama ablations.

## Strengths
- **Theoretical characterization of optimal frozen A.** Theorem 4.4 gives a clean closed-form description of the set of optimal A under random-regression assumptions, recovering the EVA principal-component subspace as a special case (Sec. 4, lines 222–228). Theorem 4.6 cleanly shows the symmetric autoencoder objective's minima coincide with the top-r eigensubspace.
- **Honest ablation in Table 6.** The paper reports that HPCA, HPCA (svd first), and AE all land at essentially identical perplexities, and that SoftHebb performs worst — i.e., the paper does not hide negative ablation outcomes (lines 376–386).
- **Breadth of evaluation regimes.** NLU (GLUE), math reasoning (GSM8K), and multimodal (LLaVA) coverage is broader than typical for an early-stage PEFT proposal.

## Weaknesses

### Fatal
None. The contribution is small but the paper is not invalid.

### Major
- **The empirical case for the proposed mechanism is essentially absent.** The paper's core novelty over LoRA-FA(EVA) is the *streaming* local update of A during fine-tuning. But: on GSM8K (Table 3), LoLoRA HPCA (0.829±0.004) ties LoRA-FA(EVA) (0.829±0.005) at three decimals; on LLaVA (Table 4) LoLoRA HPCA loss 1.075 is tied with / worse than LoRA-FA(EVA) 1.070; and on Alpaca (Tables 5–6), HPCA, HPCA(svd-first), AE, and LoRA-FA(EVA) all land within a fraction of a noise unit. No experiment establishes a regime where the streaming local update strictly helps over the simpler one-shot EVA initialization. The paper itself concedes this for LLaVA ("HPCA updates do not improve EVA-initialized adapters," line 354). This undermines the headline contribution as framed.
- **The abstract's memory claim is at best ambiguous and at worst incorrect.** The abstract states LoLoRA "further [reduces] the memory required for fine-tuning." The 20%/13% savings cited later (lines 317, 335) are vs. standard LoRA and are entirely attributable to the LoRA-FA freezing mechanism — not to the local-update contribution. The conclusion acknowledges LoLoRA "introduces a small amount of extra optimizer state … unlike standard LoRA-FA" (line 392), and Table 4 confirms LoLoRA uses *more* memory than LoRA-FA (24.1 vs 23.9 GB). The abstract should be tightened to "matches LoRA-FA memory" rather than "further reduces."
- **The theory targets a target-free regime that justifies EVA, not iterative updates.** Theorem 4.4 assumes ΔW₀ has i.i.d. Gaussian entries (Assumption 4.1) — i.e., the target carries no structural information about W. Under this assumption the optimal A is fixed (top-r eigenvectors of Σ_zz) and does not change during training. This is precisely the EVA prescription. The theory therefore motivates a *one-shot* PCA initialization but does not motivate the paper's proposed streaming local updates, which is the actual novelty. The empirical ties in Table 6 are consistent with this reading.
- **Self-contradictory conclusion.** "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" (line 390) is internally inconsistent ("consistently" vs. "two of three") and overstates the GLUE outcome, where on Tables 1–2 LoLoRA HPCA is beaten by LoRA-FA(uniform) on CoLA (66.3 vs 67.9), RTE (84.6 vs 86.4), and several other tasks. Comparison should be to LoRA-FA(uniform), the actually stronger LoRA-FA variant on GLUE, not selectively to LoRA-FA(EVA).

### Minor
- **Sec. 3.3 / Algorithm 1 is underspecified.** The local optimizer Opt_loc is named but its choice, learning rate, and interaction with the global AdamW LR are not described in the main text. Since the streaming update introduces hyperparameters LoRA-FA does not have (e.g., the 0.98 smoothing factor mentioned in Sec. 5.4), at least a sensitivity check belongs in the main paper.
- **Stationarity assumption is acknowledged but not addressed.** The theory assumes z is drawn from a fixed distribution per submodule, but during fine-tuning upstream LoRA parameters are themselves updating, so the input distribution is non-stationary. The paper notes this in the conclusion (line 392) but the theorems are still framed as supporting the deployed method.
- **No like-for-like memory accounting including Opt_loc state.** Tables 3–4 report aggregate "extra memory" but do not separately account for the local-optimizer state that LoLoRA adds over LoRA-FA. Given that the value proposition is largely about memory, this should be itemized.

### Trivial
None worth listing.

## Nice-to-Haves
- A controlled experiment in which streaming HPCA visibly *drifts* from the initial PCA subspace as training proceeds (e.g., subspace angle vs. training step) and in which that drift correlates with downstream gain. This is the cleanest way to demonstrate that iteration buys something over one-shot EVA.
- A distribution-shift / multi-domain fine-tuning setting where stationarity breaks down, which is the most plausible regime where iterative local updates should beat one-shot EVA.
- Reframe the contribution as "theoretical justification + practical implementation of EVA-style initialization under LoRA-FA, with negligible extra cost" — which is what the experiments actually support.

## Removed Points
*These points are flagged as removed; treat with caution.*
- Harsh critic flagged "Theorem 4.4 is essentially a re-derivation of EVA" as a structural weakness. Kept as Major (theory–method mismatch) but softened: rederiving EVA in a general theoretical frame is a legitimate contribution even if it doesn't justify the streaming variant.
- Strength Finder claim "demonstrates a practical advance in parameter-efficient fine-tuning" via 13% extra memory reduction on MetaMathQA: removed because the 13% saving is attributable to LoRA-FA freezing, not to LoLoRA's local-update contribution, conflicting with the Major weakness above.
- Strength Finder claim about ablations "validating the theoretical insight" partially kept (as honest reporting) but its framing as supporting the method is dropped: Table 6 actually shows the local updates do *not* improve over EVA initialization.

## Novel Insights
None beyond the paper's own contributions. The most interesting takeaway across the reviews — that the streaming local updates converge to and do not meaningfully diverge from the EVA subspace, so the proposed mechanism collapses to a known one-shot initialization — is essentially the paper's own Table 6 read honestly.

## Suggestions
- Rewrite the abstract: drop "further reduces" memory claim; replace with "matches LoRA-FA memory while attaining EVA-quality performance without an offline PCA pass."
- Recast the contribution: the genuine novelty supported by experiments is *eliminating EVA's offline PCA pass* via online streaming — frame the paper around removing the ~40 min EVA initialization overhead (Sec. 5.3) at equal quality, with a head-to-head wall-clock + memory comparison vs. LoRA-FA(EVA).
- Either find a fine-tuning regime where streaming updates strictly help (distribution shift, longer schedules, multi-task), or scope the claim down accordingly.
- Fix the conclusion's "consistently … two of three" phrasing and compare LoLoRA against the stronger LoRA-FA(uniform) baseline on GLUE rather than against LoRA-FA(EVA) selectively.
- Specify Opt_loc, its LR, smoothing 0.98, and interaction with AdamW in the main text; provide a sensitivity ablation.

---

**Axis evaluation.** *Originality*: modest — combining LoRA-FA + Hebbian/HPCA updates is a sensible composition but the local-update angle reduces empirically to EVA. *Importance*: the memory-efficient PEFT problem is real and well-motivated. *Claims supported by experiments*: weakly — the central claim (iterative local updates improve over LoRA-FA) is not demonstrated; results tie LoRA-FA(EVA). *Soundness of experiments*: reasonable scope and seeded; analysis is honest, but conclusions overreach. *Clarity*: generally clear, though Algorithm 1 and the local optimizer are underspecified. *Value to the community*: the theorem providing a closed-form justification for EVA-style initialization is the most likely lasting contribution.

---

**Calibration anchors retrieved (with comparison to this paper):**
- `s7DkcgpRxL.md` (LoRAM, avg 6.20, Accept) — memory-efficient LoRA via pruning-recover; demonstrates a concrete memory win with measured advantage. *Stronger than this paper.*
- `DLJznSp6X3.md` (ReLoRA, avg 5.75, Accept) — high-rank training via low-rank updates with measured savings and accuracy parity. *Stronger.*
- `RbKThNNFxr.md` (LoRA-FA, avg 5.33, Reject) — the very baseline this paper builds on; closest topical anchor. *Comparable conceptual ambition; this paper's empirical case over LoRA-FA(EVA) is weaker than LoRA-FA's over LoRA.*
- `SxOrhLuuVz.md` (MoRA, avg 4.75, Reject) — PEFT variant with mixed but more visible empirical gains. *Slightly stronger than this paper.*
- `VpeAsLmcvg.md` (SVD adaptation, avg 3.75, Reject) — theoretically-motivated PEFT with weak experiments. *Similar profile to this paper.*
- `0qexTTfnmH.md` (ME-LoRA, avg 3.75, Reject) — memory-efficient LoRA with marginal gains. *Closely comparable.*
- `6nZwOYDcQx.md` (NoRA, avg 4.00, Reject) — yet another LoRA variant with limited differentiation. *Similar.*
- `R0YGjmqiwB.md` (no-backprop learning, avg 3.50, Reject) — biologically-plausible learning with limited practical wins. *Lower than this paper.*
- `SI6zocV2SS.md` (CAN/Hebbian, avg 1.50, Reject) — very poor execution. *Far lower than this paper.*
- `5M0ic2RxQZ.md` (dEBORA, avg 6.67, Accept) — LoRA + bilevel rank selection, clean theory + gains. *Stronger.*
- `likXVjmh3E.md` (Expressive power of LoRA, avg 6.50, Accept) — strong pure-theory contribution. *Different lane; stronger.*
- `cWGCkd7mCp.md` (Sine-activated low-rank, avg 7.00, Accept) — strong theory + experiments. *Stronger.*
- `NmiFwEP8K5.md` (GE-PEFT, avg 4.50, Reject); `i2Ul8WIQm7.md` (PEFT privacy, avg 5.80, Reject); `6bAfAcuuZD.md` (local contrastive, avg 5.50, Reject); `9KatbAXLAq.md` (Certified PEFTSmoothing, avg 3.75, Reject); `jMJ9IRWmH9.md` (Privacy API fine-tuning, avg 3.50, Reject); `JeJ2uTQrF1.md` (FedAvg variant, avg 3.60, Reject) — variety of similar-tier or weaker rejects.

This paper sits closest to the cluster of LoRA-variant rejects (LoRA-FA at 5.33, ME-LoRA at 3.75, MoRA at 4.75, NoRA at 4.00, SVD-Adaptation at 3.75). Its contribution over the EVA + LoRA-FA combination is not empirically established and the theory does not motivate the actual deployed mechanism. It is more substantive than the very weak Hebbian/CAN paper (1.50) and somewhat more careful than ME-LoRA (3.75), but clearly weaker than the accepted-cluster anchors. Calibrated final score: 3.5.

MY FINAL SCORE: <pineapple>3.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>