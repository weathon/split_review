Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper introduces PtychoFormer, a hierarchical transformer-based model (using a Mix Transformer encoder and convolutional decoder) for ptychographic phase retrieval. The key ideas are: (1) grouping multiple overlapping diffraction patterns into separate channels to preserve their 2D spatial relationships, (2) using an MiT encoder to capture long-range dependencies between patterns, (3) a feathering-based stitching technique to eliminate grid artifacts, and (4) a hybrid approach (ePF) that uses PtychoFormer's output to initialize iterative refinement with ePIE. The paper reports substantial speed improvements over the iterative ePIE algorithm (2100–3600× faster), robustness to sparse scan patterns, and reconstruction quality improvements over two earlier CNN-based methods (PtychoNN, PtychoNet).

## Strengths

- **Massive speed advantage over iterative methods.** PtychoFormer completes reconstruction in 0.14 seconds vs. 5–8.5 minutes for ePIE (2100–3600× speedup), directly supporting the claim of enabling real-time imaging. This speed gap is too large to be explained by hardware differences.

- **Robustness to extremely sparse scans.** At only 14.9% spatial overlap (60-pixel offset), PtychoFormer maintains structural integrity and achieves lower error than ePIE, which exhibits significant artifacts. This is a meaningful practical advantage for reducing acquisition time.

- **Effective spatial-aware input scheme.** Grouping multiple diffraction patterns as separate channels (preserving their relative scan positions and 2D structure) is a sensible design that addresses a genuine limitation of single-pattern methods. The paper clearly motivates why this is superior to vectorizing patterns or using coordinate embeddings alone.

- **Feathering stitching demonstrably removes grid artifacts.** The ablation in Fig. 2c cleanly shows that feathering eliminates stitching artifacts. This is a simple but practical contribution applicable to other patch-based reconstruction methods.

- **Hybrid ePF reduces global phase shifts.** The paper provides both quantitative (MAE vs. NRMSE comparison) and visual (line profiles) evidence that ePF mitigates the global phase shift problem that plagues ePIE, with NRMSE reductions of 73.59% (amplitude) and 47.30% (phase) over ePIE.

## Weaknesses

### Fatal

None.

### Major

- **Missing experimental comparison against PtychoDV (Gan et al., 2024), the most directly relevant prior work.** The paper discusses PtychoDV in Section 3 (Related Work) as a method that also processes multiple diffraction patterns using a ViT. Yet the experimental comparison only includes PtychoNN (2020) and PtychoNet (2019)—older CNN-based methods that process one pattern at a time. The abstract claims "achieving state-of-the-art phase retrieval in ptychography," but this claim is unsubstantiated without comparison to the most directly comparable modern method. This is the single most consequential gap.

- **Unclear whether the DL baseline comparison is fair.** The paper states that PtychoNN and PtychoNet were "trained to convergence on the pre-training set" (line 186) but never clarifies whether these models received single diffraction patterns (their native input format) or were adapted to multi-pattern inputs. If they were given only single patterns while PtychoFormer receives nine patterns per inference, the comparison is asymmetric by design—PtychoFormer inherently has access to more information. This ambiguity undermines the headline improvements (e.g., 61.05% phase NRMSE reduction).

- **Missing ablations for core architectural decisions.** The paper motivates several design choices: MiT encoder over ViT (hierarchical features, spatial-reduction attention, Mix-FFN), convolutional decoder over MLP decoder, and the number of input patterns. Yet only feathering vs. no-feathering is experimentally isolated (Fig. 2c). Without ablation of the encoder choice, decoder choice, or input grouping size, it is impossible to attribute the reported improvements to any specific component. This is a significant gap for a methods paper.

### Minor

- **No error bars or variability measures for the main DL comparison.** The results in Fig. 3 (25.93%, 41.18%, 61.05%, 55.33% NRMSE reductions) are reported as point estimates averaged over 3100 test samples without standard deviations, confidence intervals, or significance tests. While single-run evaluation on large test sets is common in this domain, the lack of any variability measure makes it impossible to assess whether these differences are statistically reliable.

- **Zero-shot generalization results lack baseline context.** The paper reports NRMSE values of 0.18±0.06/0.51±0.26 (Flower102) and 0.28±0.09/0.97±0.65 (Caltech101) without providing comparable numbers from ePIE or any baseline on the same datasets. A phase NRMSE of 0.97 on Caltech101 may or may not be reasonable, but the reader has no way to interpret this. This weakens the generalization claim.

- **Input selection scheme is underspecified for reproduction.** The paper states that "up to nine spatially overlapping diffraction patterns" are grouped into channels (line 98) but does not specify how the nine patterns are selected (e.g., immediate 3×3 neighbors in the scan grid?). The receptive field of each local inference relative to the input group is also not described. This under-specifies the method for independent reproduction.

### Trivial

- **Speed comparison lacks hardware details.** The paper reports ePIE taking 0.34 s/iteration and PtychoFormer taking 0.14 s total, both "with GPU support," but never specifies the GPU model. While the 2100–3600× gap is too large for hardware to explain away, reporting the GPU model is standard practice.

## Nice-to-Haves

- An ablation comparing MiT encoder vs. standard ViT (with fixed PE) and convolutional decoder vs. MLP decoder would substantially strengthen the architectural claims.
- Running ePIE on the Flower102 and Caltech101 test sets would contextualize the zero-shot results and make the generalization claim more concrete.
- Training time, preprocessing/I/O time, and a breakdown of the 0.14 s inference time would aid practitioners in adopting the method.
- A discussion or analysis of failure cases (e.g., where phase NRMSE reaches 0.97 on Caltech101) would help define the method's limitations.

## Removed Points

*The following points from the reviewer inputs were flagged for removal:*

- **Criticism that the abstract's "spatial awareness" novelty is weakened by PtychoDV.** The paper explicitly differentiates its approach from PtychoDV: PtychoDV processes patterns as 1D latent vectors with coordinate embeddings, whereas PtychoFormer preserves full 2D patterns as separate channels. The differentiation is valid and already stated. **[REMOVED — paper already addresses this distinction]**
- **Criticism that the 100-iteration reduction by ePF is "vague" or "modest."** The paper reports this as a simple observation ("approximately 100 iterations") without overstating it. The value is stated straightforwardly. **[REMOVED — not a substantive weakness]**
- **Criticism about missing real-data experiments.** The paper explicitly acknowledges this as a limitation and discusses it as future work (Section 6). **[REMOVED — the paper scopes this out; falls under Nice-to-Have]**
- **Strength Finder strengths that conflict with verified weaknesses.** The strength about "quantitatively superior reconstruction over existing DL methods" is qualified because the comparison does not include PtychoDV and the baseline training protocol is ambiguous. This is kept but with caveats noted in the Weaknesses section. No strengths were dropped as generic/superficial.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation from the review process is the tension between the practical engineering contributions (the input grouping scheme, feathering stitching, and hybrid ePF initialization) and the insufficient experimental rigor needed to substantiate the architectural novelty claims. The paper's strongest assets—sparse scan tolerance and dramatic speedup—do not depend on the missing ablations or baselines. However, the specific architectural claims about why MiT is better than ViT for this task, and why a convolutional decoder outperforms an MLP decoder, remain empirically unsupported. This is a case where the paper would benefit from *narrowing* its claims (dropping "SOTA," focusing on speed + sparse-scan robustness as the primary contributions) rather than expanding its experiments.

## Suggestions

1. **Add comparison against PtychoDV (or another recent multi-pattern DL method).** This is the single most important improvement. Without it, the central claim of outperforming previous DL methods is unsupported.

2. **Clarify the baseline training protocol.** Explicitly state whether PtychoNN and PtychoNet were trained on single patterns (their native format) or adapted to multi-pattern inputs. If trained on single patterns, the comparison is unfair and should be reframed as showing the benefit of multi-pattern input rather than architectural superiority.

3. **Add ablations for at least the encoder choice (MiT vs. ViT) and decoder choice (convolutional vs. MLP).** This would substantiate the architectural motivation and is the minimum bar for a methods paper.

4. **Provide error bars or confidence intervals for the main DL comparison** (Fig. 3). Even standard deviations over the 3100 test samples would help assess reliability.

5. **Add ePIE baselines for Flower102 and Caltech101** to contextualize the zero-shot results.

6. **Specify the pattern selection protocol** (how are 9 patterns chosen for each local inference?) and the receptive field dimensions for reproducibility.

## Score and Decision

The paper presents practically relevant ideas (spatial input grouping, feathering stitching, hybrid ePF) with compelling advantages in speed and sparse-scan tolerance. However, the experimental evaluation has significant gaps: the most relevant modern baseline (PtychoDV) is absent from the comparison, the fairness of the DL baselines is unclear, and core architectural choices are unablated. These issues prevent the paper from supporting its "state-of-the-art" claim and weaken confidence in the attribution of improvements. The paper could be a strong contribution with revision, but in its current form the evaluation is insufficient.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>