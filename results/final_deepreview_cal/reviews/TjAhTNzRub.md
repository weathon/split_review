Now I have all the information needed to write the consolidated review. Let me synthesize everything.

---

## Summary

MoRE proposes a training-free framework for feature-level machine unlearning that combines three innovations: (i) prototype-orthogonal projection to decorrelate forget and remain class prototypes before erasure, preventing collateral damage to remain utility; (ii) remapping of forget prototypes into remain prototypes to break feature-space separability; and (iii) a mixture of remapping experts with stochastic routing to scatter forget features across multiple remain clusters, making recovery through linear probing substantially harder. The method is computationally efficient (O(Nd) time, O(dk) memory, requiring only a single forward pass). Experiments span CIFAR-10, CIFAR-100, and Tiny-ImageNet for class-wise unlearning, plus an extension to concept unlearning in Stable Diffusion.

## Strengths

- **Principled and well-motivated methodology.** The prototype-orthogonal projection (Eq. 2–5) is mathematically clean, and the ablation in Table 3 directly demonstrates its necessity: without PO projection, erasure alone leaves forget accuracy at 14.38% and remain accuracy at just 24.24%; with PO, forget accuracy drops to 0.00% while remain accuracy rises to 91.67%. This is compelling, actionable evidence.

- **Comprehensive and well-structured ablation.** Tables 3, 5, 6, and 7 systematically isolate the contributions of PO projection, expert count, routing strategy, and layer depth. Figure 7 shows stable HM performance across expert counts (2–80), supporting robustness. The cosine-similarity heatmaps in Figures 3 and 6 provide clear qualitative validation that PO projection achieves the intended decorrelation.

- **Strong empirical results on standard benchmarks.** Across CIFAR-10, CIFAR-100, and Tiny-ImageNet, MoRE achieves near-zero forget accuracy while preserving remain accuracy at or above original-model levels (Table 1 standard setting). Under the Knowledge Retention (KR) evaluation, MoRE dramatically suppresses forget recovery compared to ESC and training-based baselines — most notably on CIFAR-100 where HM_f drops to 0.07.

- **Training-free efficiency substantiated.** Figure 5 shows MoRE completing unlearning in ~9.5 seconds with ~540 MB GPU memory on CIFAR-scale tasks, orders of magnitude faster and lighter than training-based methods. The O(Nd) compute / O(dk) memory scaling argument (§3.4) is clear and plausible.

- **Broad applicability demonstrated.** The out-of-the-box application to Stable Diffusion for artistic style erasure (Table 2, Figure 4) achieves the best LPIPS trade-off (LPIPS_d = 0.25 for Van Gogh), showing the framework generalizes beyond discriminative models without architecture-specific tuning.

## Weaknesses

### Major

- **The "irreversible" claim is overstrong relative to the evidence provided.** The paper's title, abstract, and conclusion repeatedly describe MoRE as achieving "irreversible" feature-level unlearning. However, the only recovery attack tested is a linear probe trained on frozen features (the KR setting, lr=0.1). The paper itself acknowledges in §1 (line 93) that ESC's forget features remain "vulnerable to recovery through light fine-tuning" and states in §3.3 (line 223) that single-expert remapping leaves "residual cohesive structure [that] can be exploited by carefully tuned linear probes." But MoRE is never evaluated against fine-tuning-based recovery, non-linear probes, or any stronger adversary. The gap between testing only linear probing and claiming "irreversibility" is structural: irreversible would require evidence that forgotten information cannot be recovered by any plausible means. The paper should either (a) test against at least one stronger recovery attack (e.g., fine-tuning the feature extractor with a small MLP head) and show MoRE resists it, or (b) recalibrate the claim to what the evidence actually supports — e.g., "strongly resists linear-probe recovery" or "significantly impedes feature-level recovery."

### Minor

- **Table 1 notation is confusing and impairs independent interpretation.** The column headers use D_r(↑) twice with different referents (likely training vs. test remain accuracy), alongside D_R(↓) and D_f(↓). The metrics are reportedly defined in Appendix §B.3, but the main text alone does not disambiguate them, making it difficult for a reader to independently verify which numbers correspond to which claim. This is a presentation issue that should be resolved, not a flaw in the results themselves.

- **Target-class sensitivity is more than "mild" and underdiscussed.** Table 5 shows that remapping a forgotten class to different remain targets on CIFAR-10 produces HM_f values ranging from 29.26 (target class 9) to 69.78 (target class 0) under KR — a factor of >2× variation. The paper describes this as a "mild preference" and defers to future work. In deployment where the optimal target is unknown, this sensitivity could meaningfully affect outcomes, and a more forthright discussion (or a simple heuristic for target selection, such as choosing the most dissimilar remain class) would strengthen the paper.

- **ImageNet results are mentioned but not shown in the main text.** The experimental setup (§4) states evaluation on "ImageNet using ViT-base-16," but all ImageNet results are deferred to Appendix §C.1. Given that scalability is an explicit claim, the absence of even a summary row for ImageNet in the main paper weakens that claim for the reader. A compact table or a few key numbers should be surfaced.

- **Random forgetting adaptation is underspecified.** Section 4.3 describes adapting MoRE to instance-wise (random) forgetting by computing prototypes "separately for the forget and remain sets, and then remap each forget prototype to its counterpart from the remain set." When the forget set comprises arbitrary samples across classes, the notion of a "counterpart" remain prototype is ambiguous, and the description does not clarify how this mapping is constructed.

## Nice-to-Haves

- Testing at least one non-linear or fine-tuning-based recovery attack would substantially strengthen the irreversibility evidence and align the claims with the evaluation.
- A discussion of limitations — sensitivity to layer choice (Table 7 shows degradation at shallower layers), dependence on well-structured feature spaces for activation-mean prototypes, and the assumption that prototype count equals class count — would improve completeness.
- A simple heuristic for target-class selection (e.g., maximally dissimilar remain class) would address the sensitivity concern pragmatically.

## Removed Points

These points were raised by reviewers but are removed from the final review with justification:

- **"Opaque and uninterpretable experimental reporting" as a fatal issue:** The table notation is genuinely confusing (kept as Minor), but the core results are interpretable — MoRE achieves 0.00 forget accuracy in the standard setting and very low HM_f under KR across all datasets. This is not a fatal flaw.

- **Demand for non-linear recovery attacks as a fatal omission:** Kept as Major (overclaim) but not fatal — the linear-probe results are still meaningful and show strong resistance compared to baselines. The paper's contribution in suppressing linear-probe recovery is real and valuable even if "irreversibility" is too strong.

- **Criticism that Finetune/NG baselines collapse to 0% remain accuracy implying unfair comparison:** The paper does not claim these baselines are tuned optimally; they are standard baselines from the literature. MoRE outperforming them is a legitimate finding. The baselines' poor performance on remain accuracy actually strengthens the case for MoRE's utility preservation.

- **Criticism about the "mixture of experts" label overselling architectural novelty:** The paper is clear that the MoE terminology is borrowed from conditional computation literature (§3.3) and that the stochastic router is simple. This is a naming choice, not a substantive weakness.

- **Criticism that LPIPS gains in diffusion model experiments are small:** The paper achieves best LPIPS_d (trade-off), which is the appropriate composite metric. The qualitative result (Figure 4) is compelling. The claim of "outperforming SOTA" is defensible on the trade-off metric.

- **Demand for confidence intervals, theoretical proofs, or user studies:** These are not standard requirements for empirical MU papers in this setting. The paper's evaluation follows community norms.

- **Speculative claims about what the stripped appendix might or might not contain:** Per rules, all references to missing appendix content are disregarded; the review evaluates what is in the main paper.

- **Strength Finder claims dropped:** "Full-rank transformation preserves information outside the prototype span" — this is a correct technical detail but is essentially bookkeeping (Eq. 5 simplifies to I − P_f D), not a substantive contribution. It is merged into the broader methodology strength.

## Novel Insights

The paper's central insight — that unlearning at the feature level requires not just erasing forget prototypes but actively remapping forget features into the remain distribution to break residual cohesion — is genuinely novel. The realization that prototype-orthogonal projection is necessary because forget and remain prototypes are highly correlated in standard feature spaces (cosine similarity up to 0.77, shown in Figure 3), and that a pseudoinverse-based projection can decorrelate them surgically, is a clean and transferable observation. The stochastic multi-expert design for scattering features across clusters, inspired by MoE but repurposed for unlearning rather than prediction, is a creative adaptation.

## Suggestions

- **Recalibrate the irreversibility language.** Change "irreversible" to "highly resistant to linear-probe recovery" or "strongly impedes feature-level recovery." If stronger evidence is added (fine-tuning recovery experiments), "irreversible" could be retained with appropriate caveats.
- **Redesign Table 1 with unambiguous column labels.** Use distinct notation (e.g., Acc_f_train, Acc_r_train, Acc_f_test, Acc_r_test, HM, HM_f_KR) and add a compact legend.
- **Add a summary of ImageNet results to the main text.** A single sentence with key numbers (e.g., "On ImageNet with ViT-base-16, MoRE achieves X% remain accuracy with Y% forget accuracy") would substantiate the scalability claim.
- **Clarify the random-forgetting prototype mapping.** Explain how "counterpart" remain prototypes are selected when forget samples span multiple classes.
- **Propose a target-selection heuristic.** Based on Table 5 data, selecting the most dissimilar remain class (by prototype cosine similarity) appears to produce the strongest unlearning; formalizing this would make the method more practical.

## Score and Decision

**Round-1 bracket:** Based on comparison with anchors across three score bands, the paper clearly exceeds the weak band (2.5–3.0) and sits above the middle-band anchors:
- "Deep Unlearning" (5.25): MoRE has more methodological innovations (PO projection, remapping, MoE), better ablation, and broader evaluation.
- "Label-Agnostic Forgetting" (6.00): MoRE has a clearer, more principled methodology and better efficiency, though LAF has the advantage of label-free operation.

**Round-2 narrowing:** Compared to the 5.75 anchor ("Decoupling Class Label"), MoRE is stronger in methodology, presentation, and evaluation scope. MoRE is slightly stronger than the 6.00 anchor but held back from 7+ territory by the irreversibility overclaim. This places MoRE at **6.5**.

**All anchors retrieved:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Xagys9QD3T (PPU) | 3.00 | R1 | MoRE substantially stronger — better method, evaluation, scope |
| hwXUmwJAq5 (UGradSL) | 3.00 | R1 | MoRE substantially stronger |
| BJfIDS5LsS (MASIMU) | 2.50 | R1 | MoRE substantially stronger |
| 85X9awoVtv (Data Withdrawal) | 2.50 | R1 | MoRE substantially stronger |
| pUOesbrlw4 (Deep Unlearning) | 5.25 | R1/R2 | MoRE stronger — more innovations, better ablation, broader eval |
| SIZWiya7FE (Label-Agnostic Forgetting) | 6.00 | R1/R2 | MoRE slightly stronger — clearer methodology, better efficiency |
| OHOmpkGiYK (Decoupling Class Label) | 5.75 | R1/R2 | MoRE clearly stronger — more principled method, cleaner results |
| TLBPjECC5D (Sparse Repr.) | 5.25 | R2 | MoRE stronger |
| nb3VjILNVs (Low Compute Sparse) | 5.75 | R2 | MoRE stronger |
| wAemQcyWqq (Oblivious Unlearning) | 5.67 | R2 | MoRE stronger methodologically |
| 51WraMid8K (LLM Unlearning) | 8.00 | R1 | MoRE weaker — LLM paper has stronger theoretical framing |
| PBjCTeDL6o (UNI) | 8.00 | R1 | Different domain, not directly comparable |
| EUSkm2sVJ6 (Data Usage) | 7.60 | R1 | Different domain |
| Tzh6xAJSll (Scaling Laws) | 7.60 | R1 | Different domain |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>