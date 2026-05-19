- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes Stable-Transformer, a set of three theoretically motivated architectural modifications—StableInit, StableNorm, and StableAtten—aimed at improving Transformer training stability. The paper provides mathematical analysis of initialization (via random matrix theory), normalization (Jacobian analysis identifying the √d scaling factor), and attention (logit bound analysis of QKNorm). StableNorm (Eq. 2) replaces √d in normalization with d^α (α∈[0,0.5]) and is clearly defined and empirically tested. StableInit (Eq. 1) and StableAtten (Eq. 3) are referenced but their definitions are absent from the extracted text. Experimental results on GPT-2 (124M, 350M) and ViT (Large, Huge) show modest improvements.

## Strengths

- **StableNorm is clearly defined with a simple, tunable α knob.** Eq. 2 provides a concrete modification: replacing √d with d^α. The paper quantifies the gradient scale reduction (e.g., for d=4096, α=0.45 reduces the Jacobian scale by a factor of ~0.66 compared to α=0.5). This is a simple, practical intervention with a clear mathematical form.

- **Controlled ablation of α values demonstrates the trade-off.** Figure 3 shows StableNorm evaluated with five α values on both GPT and ViT without learning rate warmup, illustrating the trade-off between gradient vanishing (small α) and instability (large α). This controlled isolation is a legitimate empirical contribution.

- **The QKNorm logit bound derivation is mathematically sound.** Section 3.3.1 algebraically expands the QKNorm logit and shows that the √d₁ factor cancels in the resulting expression, providing a theoretical explanation for why QKNorm stabilizes attention. This is a valid, nontrivial observation.

- **Improved validation metrics on standard architectures.** Figure 1 shows consistent improvements: validation loss 2.827 vs. 2.848 (GPT-S 124M), 2.569 vs. 2.579 (GPT-M 350M), and accuracy 82.4% vs. 81.3% (ViT-L). Gains are modest but consistent across settings and architectures.

## Weaknesses

### Major

- **The paper claims 1B-parameter and 200-layer experiments but presents none.** The abstract states experiments on "large model (1B parameters) and deep model (200 layers)." The introduction (line 30) repeats this claim. Yet the experimental section (§2, lines 33-34) tests only GPT2-Small (124M), GPT2-Medium (350M), ViT-Large (~304M), and ViT-Huge (~632M). No 1B-parameter or 200-layer result appears anywhere in the extracted text. This is a direct mismatch between the paper's headline claim and the evidence provided. Even if such experiments exist in a stripped appendix, claiming them in the abstract without presenting them in the main body is misleading. The authors must either present these experiments or honestly revise the scope statement.

- **The theoretical motivation for StableNorm is imprecise.** The paper argues (line 73) that the √d term in the normalization Jacobian causes gradients to grow with hidden dimension d. The reviewer correctly notes that ‖y‖₂ also scales with √d for typical inputs, making the ratio √d/√(‖y‖²₂) ≈ 1/σ roughly independent of d in practice. The paper focuses on the maximum Jacobian value (√d/√ε when std(x)=0), but it does not clearly distinguish between worst-case and typical-case behavior, and it draws a causal connection ("may lead to larger gradients...harder to train larger models") that is not fully supported by the presented analysis. This does not invalidate StableNorm as an empirical design (the α knob remains useful), but the paper's claimed theoretical grounding for it is substantially weaker than presented.

- **No comparison against established stabilization baselines.** The evaluation compares StableGPT/StableViT only against the original GPT-2 and ViT implementations. It does not compare against DeepNorm (Wang et al., 2022), ReZero (Bachlechner et al., 2021), Fixup (Zhang et al., 2019), LipsFormer (Qi et al., 2023b), or QKNorm (beyond the theoretical discussion). The paper's own related work section mentions these as relevant stabilization methods, yet none are included as baselines. Without this, the claimed advantage cannot be attributed to the specific Stable-Transformer design rather than generic architectural changes.

- **Individual results for StableInit and StableAtten are not shown.** The paper states (line 35) that "when evaluating each of StableInit, StableNorm and StableAtten, we only replace the corresponding module." Yet only StableNorm receives individual evaluation (Figure 3). The Stable-Transformer evaluation (§3.4.1) combines all three components. No separate results demonstrate that StableInit or StableAtten individually improve stability or performance.

- **"Stability" is not empirically demonstrated.** The paper claims "more stable training" but does not present training loss curves, gradient norm histograms, or variance across runs. Only final validation loss/accuracy is shown (Figure 1). Stability is typically assessed via convergence behavior, loss/gradient variance, or sensitivity to hyperparameters — none of which are provided. The learning rate tolerance claim (line 161) is stated without supporting experiments.

### Minor

- **Experimental results lack statistical rigor.** Improvements are modest (loss 2.827 vs. 2.848; accuracy 82.4% vs. 81.3%) and reported as single values without error bars, confidence intervals, or multiple seeds. For gaps this small, it is unclear whether the difference is significant or due to random seed variation.

- **Missing definitions for two of three core contributions.** Eq. 1 (StableInit) and Eq. 3 (StableAtten) are referenced but not present in the extracted text. Section 3.1 ends abruptly before presenting StableInit; Section 3.3.1 cuts off before presenting StableAtten. While this may be a PDF extraction artifact, the extracted text as provided cannot be used to verify these components. This is noted as a minor issue because the paper's core defined contribution (StableNorm) is arguably the most substantive.

### Trivial

- The paper states "the training loss is reduced to 2.848" (line 34) when describing the baseline reproduction — "reduced" is a confusing word choice for establishing the baseline value.
- "StalbeGPT-S" typo in Figure 3 caption.
- Section numbering (3.2.1 under 3.2, but no similar subsections under 3.1 or 3.3) is inconsistent.

## Nice-to-Haves

- An ablation study isolating the individual contributions of StableInit and StableAtten would strengthen the paper.
- Training loss curves would help substantiate the "stability" claims.
- Including a comparison with DeepNorm, ReZero, or LipsFormer would clarify the paper's relative contribution.
- A discussion of how α should be chosen in practice for different model scales would be helpful.

## Removed Points

- **"The theoretical analysis contains a flawed core argument that invalidates the paper"** (from Harsh Critic, Issue 2, conclusion that StableNorm contribution "collapses"). Downgraded from Fatal to Major. The paper's theoretical motivation is imprecise (does not properly account for ‖y‖₂ scaling with √d in the typical regime), but the StableNorm modification itself is still a valid empirical design supported by experiments. The imprecision weakens but does not invalidate the contribution.
- **"The paper's core modules are unverifiable"** (Harsh Critic, Issue 3, calling missing Eq. 1 and Eq. 3 a "fundamental gap"). Downgraded from Fatal to Minor. The missing equations are likely a PDF extraction artifact — Eq. 2 (StableNorm) survived extraction, and the paper clearly references these equations. The paper as originally submitted presumably contains them. However, we note the issue for completeness.
- **"The theorem in §3.2 is an elementary inequality"** (Harsh Critic, Issue 5). Removed. The inequality is simple, but the paper does not claim it is a deep theoretical result — it is a supporting observation in the analysis. Labeling it a "theorem" is arguably over-formal but not incorrect.
- **"The paper incorrectly claims a theoretical advance"** (Harsh Critic, Issue 5). Removed. The paper's mathematical claims (the centering inequality, the QKNorm logit bound) are correct as stated. The reviewer's complaint about "trivially derived" is a matter of opinion, not factual error.
- **"Missing related works"** (implied). Removed per instructions — I cannot independently verify missing citations.
- **Formatting/style nitpicks** (various). Removed per instructions.

## Novel Insights

The most interesting observation from the cross-review is that the paper's central theoretical claim about √d causing instability in normalization is plausible in a worst-case sense (when activations are near zero, the Jacobian's √d/√ε term grows with d) but imprecise as a typical-case argument. This tension — between worst-case analysis and typical training dynamics — is a genuine methodological gap in the paper. A stronger framing would acknowledge that the typical gradient scale is independent of d (due to ‖y‖₂ ∝ √d) while arguing that α < 0.5 provides a safety margin against worst-case gradient spikes, which may occur near initialization or during training collapse. The paper's empirical results (Figure 3) are interesting precisely because they show that α functions as a meaningful knob even though the simple worst-case argument is incomplete.
