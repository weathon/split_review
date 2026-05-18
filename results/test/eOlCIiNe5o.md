Here is my consolidated review:

---

## Summary

This paper proposes SVFCL, a few-shot class-incremental learning method that fine-tunes only the singular values of pre-trained ViT weight matrices, keeping the left/right singular vectors frozen. The approach adds lightweight task-specific adapters (one per session) consisting of the original SVD factors with learnable diagonal singular-value updates, aiming to balance representational flexibility against overfitting in few-shot sessions. Experiments are conducted on CIFAR-100, CUB-200-2011, and miniImageNet.

## Strengths

- **Novel singular-value fine-tuning as a lightweight adaptation strategy.** The core idea — decomposing each pre-trained weight matrix via SVD, freezing U and V, and learning only the diagonal singular values per session (Eq. 6, Section 4) — is clean and principled. It directly addresses the overfitting problem in few-shot sessions by strictly limiting the number of learnable parameters while allowing the backbone representation to shift.

- **State-of-the-art accuracy on three benchmarks.** SVFCL achieves 83.5% (CIFAR-100), 83.5% (CUB-200-2011), and 96.3% (miniImageNet) in final-session Top-1 accuracy with the smallest performance drops (6.9, 4.5, 2.3 respectively). The results on CUB-200-2011 (83.5% vs. 67.0% for CodaP) and miniImageNet (96.3% vs. 82.8% for ASP) are particularly striking.

- **Strong performance against foundation-model-based methods that use additional textual priors.** Table 5 shows SVFCL outperforming CPE-CLIP by 12.7% and PriViLege by 6.0% on CUB-200-2011, *without* leveraging CLIP's language modality. This suggests the singular-value tuning strategy itself provides substantial benefit independent of multi-modal information.

- **Extremely short training schedule (3 base epochs / 2 few-shot epochs).** The method converges in very few epochs while outperforming methods that train for orders of magnitude longer, supporting the claim of computational efficiency.

- **Ablation studies on where to apply SVFCL within ViT and on low-rank approximation.** Figures 4–5 investigate which blocks (Q, K, V, FFN) benefit most and how rank reduction affects accuracy, providing practical deployment insights. Rank-500 approximation maintains strong performance.

## Weaknesses

### Major

1. **Missing controlled comparison to LoRA and other PEFT methods on the same backbone.**  
   The paper pitches SVFCL as a lightweight fine-tuning alternative, yet the experiments include no comparison to LoRA (Hu et al., 2021), adapter tuning, or bias tuning applied to the same ViT-B/16 backbone under the same FSCIL protocol. LoRA is the most natural competitor — it also fixes a decomposition and learns two factors — so comparing against it directly would either validate or undermine the claim that tuning only singular values (rather than learning both low-rank factors) is advantageous. Without this control, the reader cannot tell whether the observed gains come from the specific singular-value constraint or simply from having *any* parameter-efficient adapter attached to a ViT backbone.

2. **The fixed-U,V modeling assumption is not justified.**  
   The method's central design choice is to freeze the left and right singular vectors U and V from the original pre-trained SVD and only update the singular values. This constrains all weight updates to the singular-vector subspace of the *original* pre-trained weight matrix. The paper offers no theoretical reasoning or empirical analysis for why this subspace is appropriate for adapting to new classes in later sessions. An experiment comparing three conditions on the same backbone — (a) full SVD fine-tuning (tune U, S, V), (b) SVFCL as proposed (tune S only), and (c) LoRA (tune A, B) — would directly test whether the frozen-vector constraint is beneficial or limiting. This is a gap at the core of the contribution.

3. **Mixed-backbone comparisons in the main results tables conflate backbone strength with method performance.**  
   Tables 1–3 compare SVFCL (ViT-B/16) against conventional FSCIL methods (iCaRL, CEC, FACT, TEEN) that are built on ResNet-18 in the published literature, side-by-side as equally comparable baselines. The 5–15% margins over these methods cannot be attributed to SVFCL alone, since the switch from ResNet-18 to ViT-B/16 is itself known to produce large gains on these benchmarks. The paper does include a separate foundation-model comparison (Table 5), which partly addresses this, but the headline figures in Tables 1–3 remain the primary results presented, and they do not isolate the effect of the method from the effect of the backbone. This weakens the paper's central SOTA claim.

### Minor

1. **No statistical reliability measures (error bars / multiple seeds).**  
   The paper reports point estimates without variance. Few-shot settings are inherently high-variance due to random task splits and small sample sizes. While single-run evaluation is not uncommon in the FSCIL literature, the large claimed margins (e.g., 96.3% vs. 82.8% on miniImageNet) would be much more convincing with confidence intervals or results over multiple splits.

2. **Short training schedule confounds the claimed overfitting mitigation.**  
   Training for only 3 base epochs and 2 few-shot epochs is unusually short. The paper states this is "to alleviate overfitting," but this early stopping is itself a strong regularizer. It is unclear how much of the benefit attributed to the singular-value adapter design actually comes from the short schedule. An ablation training for more epochs would clarify this.

3. **The Grad-CAM visualization (Figure 1) is qualitative and not quantified.**  
   The figure shows that SVFCL produces more focused attention maps than full fine-tuning, but no metric (e.g., intersection-over-union with ground-truth object regions, or a quantitative measure of attention dispersion) is provided. This weakens the claim that SVFCL "learns critical features."

4. **No parameter counts or FLOPs reported for the low-rank approximation.**  
   Figure 4 shows that rank-500 achieves near-full performance, and the text says this "reduce[s] model parameters," but the actual parameter counts, FLOPs, or memory savings are not provided. The efficiency argument remains qualitative.

### Trivial

None.

## Nice-to-Haves

- **Ablation separating NCM classifier from the singular-value tuning.** The paper replaces the cosine classifier with NCM prototypes at session end — a standard technique — but never ablates this choice. A comparison of SVFCL with a learned linear classifier vs. NCM would clarify which component drives the gains.
- **Comparison to full fine-tuning of ViT under the same short-epoch schedule**, to directly test whether SVFCL's advantage over full fine-tuning is robust or an artifact of early stopping.
- **Analysis of how singular vectors change during full fine-tuning** (e.g., measuring the angle between original and fine-tuned singular vectors), to empirically justify freezing U and V.

## Removed Points

- *"The paper should compare to more PEFT methods (prefix tuning, SSF, etc.)"* — The request for LoRA is essential because it is the most directly comparable decomposition-based PEFT; broader PEFT comparisons go beyond what is necessary to validate the core claim. Moved to Nice-to-Haves in spirit.
- *"The paper does not report which ViT blocks were selected for tuning in the main results"* — The paper does report this in Figure 5, though the ablation chooses blocks incrementally. The main experiments use the best configuration found. This is standard practice; the reviewer likely missed the ablation figure.

## Novel Insights

The reviews reveal a fundamental tension in the paper's experimental design: the method introduces a novel parameterization constraint (tuning only singular values) but never runs the controlled experiments that would validate that this specific constraint — rather than the general presence of a lightweight adapter, a stronger backbone, or an aggressive early-stopping schedule — drives the reported gains. The paper presents SOTA numbers but the evidence chain linking the proposed design to those numbers is incomplete. This is a variant of a common pattern across FSCIL papers: comparing across different backbones is accepted practice in parts of the literature, but for a paper making a specific architectural claim (singular-value tuning), isolating that claim from confounders is essential.

## Suggestions

1. **Add a direct SVFCL vs. LoRA comparison on ViT-B/16** with matched parameter budgets. This is the single experiment that would most directly validate or refute the claim that tuning singular values (rather than learning arbitrary low-rank factors) is beneficial.
2. **Add a fixed-U,V ablation** comparing full SVD fine-tuning (U, S, V all learnable) vs. SVFCL (S only) vs. LoRA. This would quantify the cost of freezing the singular vectors.
3. **Report results over at least 3 random seeds/splits with confidence intervals** for all main experiments, especially given the few-shot setting.
4. **Acknowledge the backbone mismatch explicitly** in the discussion, and either (a) reproduce the conventional baselines on ViT-B/16 under the same protocol, or (b) clearly separate cross-backbone comparisons from same-backbone comparisons in the main tables.
5. **Add an ablation that trains for more epochs** (e.g., 30 base / 10 few-shot) to disentangle early stopping from the adapter design.

## Score and Decision

**Originality:** High — the singular-value tuning approach is novel within FSCIL.  
**Importance:** Medium-high — FSCIL is a practically relevant problem, and parameter-efficient adaptation of foundation models is timely.  
**Claims supported:** Low — the central claim of achieving SOTA via singular-value tuning is not adequately isolated from confounders (backbone, missing controls, short schedule).  
**Soundness:** Low-medium — the experimental design has gaps that prevent firm conclusions about the method's specific contribution.  
**Clarity:** Medium — the method description is clear, but the experimental presentation does not adequately separate different categories of comparison.  
**Value to community:** Medium — the idea is worth pursuing, but the empirical validation needs significant strengthening before the community can rely on the reported numbers.

The paper presents a novel and clean idea that addresses a genuine problem. However, the experimental evaluation does not isolate the effect of the proposed singular-value constraint from confounding factors (backbone strength, missing LoRA baseline, unjustified frozen-vector assumption, short training schedule). The reported SOTA numbers are impressive but cannot be causally attributed to the method on the evidence provided. Substantial additional controlled experiments are needed before the contribution can be fairly assessed.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>