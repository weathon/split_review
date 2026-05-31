Now let me write the final review.

## Summary

The paper identifies a genuine limitation of SSL (label dependency) and proposes CaPT, a co-training framework that integrates CLIP into SSL via an asymmetric-modalities design. CaPT jointly trains a fully fine-tuned unimodal network and an adapter-tuned CLIP model, aggregating their predictions through entropy-weighted co-pseudo labels. The method achieves strong results, notably 21.38% improvement over the second-best method on CIFAR-100 with one label per class.

## Strengths

1. **Dramatic empirical gains in extreme low-label regimes.** On CIFAR-100 1-shot, CaPT achieves 82.51% vs. FreeMatch's 61.13% (Table 3). On ImageNet with 10 labels/class, CaPT beats RegMixMatch by 9.33% (Table 2). These margins are far larger than typical SSL improvements and convincingly demonstrate that incorporating CLIP's prior knowledge helps break SSL's label dependency.

2. **Thorough and well-designed ablation.** Table 6 systematically isolates each design choice by removing components (CaPT-Ada, CaPT-Deb, CaPT-Uni, only UPM, only MPM, w/o feat aug., equal weights). The controlled degradations make it clear which components contribute what, including the honest finding that the bidirectional flow adds 0.88–1.49% on the tested settings.

3. **Efficiency demonstration with concrete overhead numbers.** Table 4 shows CaPT uses only 8.00% more memory (5050 vs. 4676 MiB) and 11.18% more training time than FreeMatch on CIFAR-100 2-label. This directly addresses the practical concern that integrating CLIP would be prohibitively expensive.

4. **Comprehensive evaluation across diverse settings.** The paper evaluates on USB benchmarks, ImageNet, extreme low-label regimes (1-shot), and 6 fine-grained datasets (Table 5). This breadth strengthens the portability claim.

## Weaknesses

### Major

- **The core empirical gains are primarily attributable to adding CLIP, not to the bidirectional co-training loop.** The ablation (Table 6) shows that CaPT-Uni (unidirectional CLIP→vision flow) achieves 83.95% on CIFAR-100 2-label vs. CaPT's 84.83% — a gain of only 0.88% from bidirectional information exchange. On EuroSAT the gain is 1.49%. By contrast, the gap between only-UPM (78.60%) and CaPT-Uni (83.95%) is 5.35% — i.e., simply adding CLIP's prior in a one-way fashion accounts for the vast majority of the improvement. The paper's framing ("asymmetric-modalities co-training... enables richer cross-model information exchange") exaggerates the role of the mutual learning mechanism. The real contribution is the practical integration framework (adapter-tuning + fusion for leveraging CLIP in SSL), and the paper would be strengthened by reframing accordingly.

- **The theoretical analysis (Theorem 1.1) provides plausible motivation for why SSL fails but does not connect to the proposed method.** The theorem bounds pseudo-label error under a Gaussian mixture / nearest-prototype classifier model. It shows that increasing prototype bias B or reducing labeled sample size increases the bound — a clean formalization of the label-dependency problem. But the paper never extends this analysis to show how CaPT specifically reduces the bound (e.g., by reducing B through CLIP's prior, or changing the effective margin). As presented, the theory and the method sit in separate compartments: the theory motivates *why* we need to break label dependency, but any method that provides external prior knowledge would equally benefit from this motivation.

### Minor

- **The "pattern-homogeneity bottleneck" claim relies on qualitative evidence.** Figure 3 shows attention maps for 8 images, illustrating that two unimodal ViTs attend similarly while CLIP attends differently. The paper cites Appendix B for more evidence, but the main-text support is thin. A quantitative similarity metric (e.g., CKA, representation similarity) between the unimodal ViTs vs. between ViT and CLIP would substantially strengthen the motivation for the asymmetric-modalities design.

- **CaPT slightly underperforms CLIP zero-shot on STL-10** (96.07% vs. 97.18%, Table 1). This suggests that adapter-tuning + co-training can degrade CLIP's zero-shot knowledge on datasets well-covered by CLIP's pre-training. The paper does not comment on this, which would be informative for practitioners deciding whether to use CaPT on their dataset.

### Trivial

- **The entropy-based weighting (Eqs. 11–12) operates at the batch level** (average entropy across the batch determines one weight per module), not per sample. This is a deliberate design choice, and the paper has a separate per-sample mechanism (threshold-based zero-vector replacement), but calling it "adaptive weight adjustment" is somewhat misleading since all samples in a batch share the same module weights. A per-sample weighting scheme would be a more natural alternative.

- **The bound in Theorem 1.1 contains \(2^{d/2}\), making it vacuously large for any realistic input dimension d** unless the exponential term is astronomically small. The paper acknowledges this is an upper bound and the qualitative insight (margin shrinks with bias/sample size) is what matters, but the practical meaning of the numerical bound is questionable.

## Nice-to-Haves

- Quantifying the pattern-homogeneity bottleneck using a representation similarity metric (e.g., CKA) would significantly strengthen the core motivation.
- A brief comment on why CaPT underperforms CLIP zero-shot on STL-10 would improve practical utility.
- Demonstrating portability by plugging in a different VLM (e.g., SigLIP) would substantiate the "portable framework" claim beyond what is mentioned as future work.

## Removed Points

- **FGVCAircraft limitation discussed only in removed appendix**: The paper explicitly acknowledges this case and references Appendix N. Since the parser strips appendices, flagging this as a weakness is unfair — the limitation is acknowledged in the original submission.

- **"Training time comparison should report GPU type"**: The paper already states "10GB RTX 3080 GPU" (line 220). This criticism is factually wrong.

- **"Comparison to RegMixMatch seems cherry-picked"**: The paper also compares to FreeMatch in Table 4.

- **"Missing comparison on SVHN"**: SVHN results are reported in Table 5.

- **"Pseudo label retention threshold is vague"**: The paper states "We adopt the adaptive threshold strategy from FreeMatch to filter pseudo labels" (line 206). This is a specific reference to an existing method.

## Novel Insights

The harsh critic correctly identifies that the paper's central framing overstates the contribution of the bidirectional co-training loop. The real strength is the practical engineering: combining adapter-tuned CLIP with a fully fine-tuned unimodal network via co-pseudo labels produces strong results with modest overhead. The pattern-homogeneity argument — while qualitatively plausible — lacks quantitative backing and the theoretical analysis, while clean, is disconnected from the method. What emerges is a well-validated integration framework rather than a fundamentally new learning principle, and the paper would benefit from presenting itself in those terms.

## Suggestions

1. **Reframe the contribution**: Emphasize CaPT as a portable framework for incorporating VLMs into SSL (adapter-tuning + entropy-weighted fusion + co-training), rather than positioning the bidirectional co-training loop as the primary innovation.
2. **Add quantitative similarity analysis** (CKA or similar) comparing representations of unimodal ViTs vs. ViT+CLIP to support the pattern-homogeneity claim.
3. **Comment on STL-10 underperformance** relative to CLIP zero-shot.
4. **Clarify the threshold mechanism** by specifying whether FreeMatch's adaptive threshold is applied exactly as in the original work.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
| Path | Avg Score | Comparison |
|------|-----------|------------|
| FwkYeLovHk.md | 3.33 | Weak-to-strong generalization for CLIP; substantially weaker paper |
| HfJxXbXlYJ.md | 3.00 | LLM2CLIP; weaker novelty and results |
| 97D725GJtQ.md | 5.80 | SemiCLIP: similar topic (CLIP+SSL), accepted; comparable quality but less dramatic results |
| 1rgMkDWfYV.md | 4.50 | Cleaning label noise with CLIP; similar concern about gains from pretraining, weaker overall |
| 3i13Gev2hV.md | 8.00 | HyCoCLIP: clearly stronger in novelty and completeness |

**Round 2 (Narrowing):**
| Path | Avg Score | Comparison |
|------|-----------|------------|
| dnqPvUjyRI.md | 6.00 | SemiReward: SSL reward model, comparable quality, similar acceptance level |
| 97D725GJtQ.md | 5.80 | SemiCLIP: CaPT has stronger results but similar method novelty concerns |
| WPsnH6875d.md | 6.00 | SSL unseen-class re-evaluation; good analysis paper |
| ptCIlV24YZ.md | 5.80 | Image clustering with pretrained models; similar use of pretrained CLIP |

**Round-1 Bracket:** 5.0 – 7.0

**Narrowing:** The paper is stronger than the 4.50-5.33 cluster (more comprehensive evaluation, more dramatic results) and comparable to the 5.80-6.00 cluster. It does not reach the 8.00 level of HyCoCLIP, which demonstrates substantially more method novelty. Within the 5.80-6.00 band, CaPT stands out for empirical thoroughness and result magnitude but is held back by the disconnect between its claimed innovation (bidirectional co-training) and where the gains actually come from (adding CLIP). The SemiCLIP (5.80) and SemiReward (6.00) papers had similar evaluation quality and were accepted.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>