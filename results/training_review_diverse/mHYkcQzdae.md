Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes a dual-stream architecture for micro-expression recognition (MER). The main stream uses a Continuous Vertical Attention (CVA) block to model motion differences between onset and apex frames with vertical-only attention maps passed across layers. The auxiliary stream uses a Facial Position Focalizer (FPF) built on Swin Transformer to encode spatial position information. Action Unit (AU) annotations from the datasets are incorporated as auxiliary features. The model achieves state-of-the-art accuracy (94.35% on CASME II, 86.76% on SAMM) and F1-scores on both benchmarks, with extensive ablations comparing vertical vs. horizontal attention, Swin vs. ViT encoders, and single vs. dual-frame inputs.

## Strengths

- **Vertical attention design empirically validated.** Table 3 shows vertical-only attention outperforms both horizontal-only and both-direction attention by clear margins on both datasets, within the full architecture. This is the paper's most novel design choice and is backed by direct comparative evidence.

- **Swin Transformer-based FPF module outperforms ViT alternative.** Table 5 demonstrates that replacing ViT with Swin Transformer in the position encoding stream yields higher accuracy and F1-score on both datasets. The shifted-window mechanism is well-motivated for capturing long-range dependencies across facial regions.

- **Substantial SOTA improvements on two benchmarks.** The complete model achieves 94.35% accuracy on CASME II and 86.76% on SAMM. Against MMNet, it improves by 6% accuracy / 7.26% F1 on CASME II; against μ-BERT, it improves by 10.87% on CASME II and 1.98% on SAMM. These are non-trivial margins given the saturated nature of these benchmarks.

- **Continuous attention mechanism validated.** Table 4 shows that passing attention maps from previous layers (continuous) outperforms independent per-layer attention, justifying a core design choice of the CVA block.

- **Dual-frame input shown superior to single-frame.** Table 6 demonstrates that encoding both onset and apex frames separately (rather than only the apex) improves performance, validating the dual-stream design.

## Weaknesses

### Fatal
None.

### Major

- **No statistical reliability measures.** The paper reports single accuracy and F1 numbers for all experiments without standard deviations, confidence intervals, or any multi-run analysis. On datasets with 255 and 159 videos, and given that LOSO cross-validation is deterministic for a fixed seed, the reported 6% improvement on CASME II over MMNet could fall within noise range if the model is sensitive to weight initialization or data augmentation order. The paper does not state whether a fixed seed was used or how results vary across runs. This is the single most significant weakness: without variance estimates, the central empirical claim is unverifiable. This is a structural evaluation gap, not a missing experiment.

### Minor

- **Primary ablation (Table 2) builds on ResNet-18 rather than the full architecture.** Table 2 adds CVA, FPF, and AU embedding to a ResNet-18 baseline, but the actual model uses Swin Transformer + CVA stack, not ResNet-18. This makes it difficult to interpret the marginal contribution of each component *within the proposed architecture itself*. (That said, Tables 3–7 do perform proper within-architecture ablations by varying one design choice at a time while keeping the full model fixed, which partially mitigates this concern.)

- **Vertical attention motivation lacks prior-literature support.** The paper asserts that "vertical facial muscle movement plays a more significant role in micro-expression recognition" (Section 2) without citing any prior anatomical or computational evidence for this claim. The empirical result (Table 3) is valid, but framing the method as "identifying" this contribution rather than "hypothesizing and empirically confirming" it overstates the contribution.

- **Overfitting risk not addressed.** The model is large (Swin Transformer with depths [2,2,6]; four-layer CVA producing 512×14×14 feature maps; MLP classifier) trained on at most 255 videos. No training curves, validation loss trajectories, or regularization analysis are provided. While LOSO is the standard protocol, the paper does not discuss whether the model memorizes subject-specific artifacts given the large model-to-data ratio.

- **Learning rate decay schedule is underspecified.** The paper states the learning rate is "exponentially decayed during the first 50 epochs out of 75 epochs total" without specifying the decay factor, decay frequency (every epoch? every batch?), or final learning rate. Weight decay of 0.6 is unusually high and is not justified or ablated. These details affect reproducibility.

- **No limitations or failure-case analysis in the conclusion.** The conclusion simply restates results. There is no discussion of dataset constraints, AU annotation dependency, class imbalance effects, or situations where the method underperforms.

### Trivial
None. (The typo-level and formatting criticisms were parser artifacts, not author errors.)

## Nice-to-Haves

- **Cross-dataset evaluation** (e.g., train on CASME II, test on SAMM) would be the strongest test of generalization and would substantially increase confidence in the method's robustness.
- **Failure mode analysis** including confusion matrices, per-class F1, and misclassified examples would help assess whether the model learns generalizable features or is driven by class imbalance (especially the "others" category).
- **Computational cost reporting** (inference speed, parameter count, GPU memory) would help practitioners assess practicality.
- **Hyperparameter sensitivity analysis** for the learning rate, the unusually high weight decay (0.6), and the CVA reduction ratio would be useful given the small data size.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Formatting criticism of `max :{8, C/32}` notation** (parser artifact from `max(8, C/32)` — not an author error).
- **Random rotation range "7° to 3°" as a typo** (likely a parser artifact where a negative sign was lost; the original submission does not have this issue).
- **"AU annotation source should be stated explicitly"** — the paper already states in Section 4.1: "more detailed annotations for Action Units (AUs) have been provided" for both datasets.
- **"10.87% improvement on CASME II seems inconsistent with earlier 6% claim"** — these are against different baselines (6% vs. MMNet; 10.87% vs. μ-BERT). No inconsistency exists.
- **Strength Finder's "Thorough component-level ablation establishing causality"** — this strength conflicts with the verified weakness that Table 2's ablation uses a ResNet-18 baseline rather than the actual architecture, reducing its evidential value for the proposed model.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the expected tensions (variance reporting, ablation design, overfitting risk on small data) but do not identify any additional insight about the method or the problem that the authors themselves did not articulate.

## Suggestions

1. **Report means and standard deviations over at least 5 runs with different random seeds** for all main results and ablations. This is the single highest-impact fix because it would establish whether the reported improvements are statistically robust.
2. **Add a within-architecture ablation** that removes CVA, FPF, and AU from the *full model* (start with the complete architecture and disable one component at a time), rather than adding them to a weaker baseline. This directly tests each component's contribution in the actual model.
3. **Expand Section 4.3** to specify the learning rate decay factor, decay frequency, and final learning rate; justify or ablate the weight decay of 0.6.
4. **Acknowledge limitations** in the conclusion: the small dataset sizes, reliance on ground-truth AU annotations, and the lack of cross-dataset validation — and suggest how these might be addressed in future work.

## Score and Decision

The paper proposes a well-motivated architecture with reasonable design choices (vertical attention, Swin-based position encoding, AU embedding) and runs extensive ablations that support most of its claims. However, the absence of variance reporting is a structural weakness that makes the central empirical claim unverifiable given the small dataset sizes. The primary ablation's use of ResNet-18 rather than the full architecture further weakens the evidence for component-level contributions. These issues are addressable but require non-trivial additional experiments.

**Originality**: Moderate — vertical-only attention is novel for MER, but the individual techniques (Swin Transformer, coordinate attention, AU embedding) are well-established.  
**Importance**: Moderate — MER is a niche but active area with practical applications.  
**Claims support**: Weak — the SOTA claims are not supported by statistical reliability measures.  
**Soundness**: Fair — the ablations are well-structured (Tables 3–7) but the primary evaluation protocol has a significant gap.  
**Clarity**: Good — the architecture and experiments are clearly described.  
**Value to community**: Moderate — the vertical attention finding and CVA module are interesting contributions.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>