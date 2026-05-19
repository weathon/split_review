- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 5, 3, 1
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper introduces HyperPg, a prototype representation that models a truncated Gaussian distribution over cosine similarities on a hypersphere, with learnable mean μ and standard deviation σ. The authors also propose HyperPgNet, an architecture that learns concept-aligned prototypes using pixel-level annotations provided by an automated extraction pipeline built on Grounding DINO and SAM2. Experiments on CUB-200-2011 and Stanford Cars show that HyperPgNet achieves competitive accuracy with substantially fewer prototypes (300 vs 2000) and converges much faster (~40 epochs vs ~490) compared to ProtoPNet.

## Strengths

- **HyperPg representation jointly captures direction and spread in a principled way**: Section 3.3 defines HyperPg as a truncated Gaussian over cosine similarity with learnable mean μ and std σ. Figure 2 shows that for intermediate μ values the distribution forms a ring on the hypersphere, which would require many point prototypes to approximate — demonstrating increased representational capacity per prototype. This is a well-motivated and technically sound contribution.

- **Consistent accuracy improvements with far fewer prototypes and epochs**: Table 1 shows HyperPgNet (without L_RRC) reaches 76.5% on CUB-200-2011 (vs ProtoPNet 68%) using 300 prototypes (vs 2000), and 88.6% on Stanford Cars (vs ProtoPNet 86.4%) using 180 prototypes (vs 1960). Figure 3 shows convergence around epoch 40 versus ProtoPNet's ~490 epochs. The improvements are consistent across both datasets.

- **The "ProtoPNet + HyperPg" ablation isolates the effect of the prototype representation**: By swapping ProtoPNet's L2 prototypes with HyperPg in the same architecture (2000 prototypes), accuracy improves from 68.0% → 70.5% on CUB and 86.4% → 87.4% on Cars, providing direct evidence that HyperPg as a representation contributes positively independent of other architectural changes.

- **Concept extraction pipeline is a practical engineering contribution**: Section 5 describes a pipeline using SAM2 with dataset-provided part points for CUB, and Grounding DINO + SAM2 for Stanford Cars, labeling the entire Cars dataset in 2 hours on a single consumer GPU. This significantly lowers the barrier for concept-aligned training.

- **RRC loss qualitatively improves prototype localization**: Figure 4 (gradient maps) shows that adding L_RRC makes a "head" prototype focus almost exclusively on the head region, whereas the variant without L_RRC activates on other bright body areas. The qualitative evidence supports the claimed behavior.

## Weaknesses

### Fatal
None.

### Major

- **Non-standard training setup limits comparability with prior work and raises questions about baseline calibration**: The paper trains all models on full images (no bounding-box crops) with only 30 training images per class and no offline augmentation (line 304). ProtoPNet's published result on CUB is ~80% with the original setup (cropped, ~1200 images/class); here it achieves 68%. The Segformer baseline collapses to 17.7% on CUB and 1.9% on Cars (essentially random for the 196-class Cars task). While all methods are compared under identical conditions — and ConvNeXt at 74.2% shows the setup is not universally broken — the gap between published and reproduced numbers for ProtoPNet means the reader cannot assess whether the observed relative ordering reflects genuine superiority of HyperPgNet or differential robustness to a low-data, full-image protocol. The authors should either justify this setup as a deliberate low-data regime, or calibrate by showing that at least one baseline reaches within a few points of its published performance.

- **The specific contribution of concept alignment vs. the HyperPg representation is not disentangled**: The paper includes "ProtoPNet + HyperPg" (class-based training, 2000 HyperPg prototypes), which isolates the HyperPg effect. But no experiment isolates the concept-alignment effect: e.g., ProtoPNet with concept masks + RRC loss but using L2 prototypes, or HyperPgNet with class-based training (no concept masks) and 2000 prototypes. The best results come from the full HyperPgNet system; without these ablations, it is unclear whether the accuracy gains come primarily from the HyperPg representation, the concept-aligned training, or their combination. This matters because the paper's title and framing emphasize HyperPg, but the evidence for HyperPg (apart from concept alignment) is limited to the 2.5% and 1.0% gains in the "ProtoPNet + HyperPg" ablation.

- **No statistical significance or variance reporting**: All results in Table 1 are single accuracy numbers from a single run. Deep learning experiments exhibit non-trivial run-to-run variance, especially with small training sets (30 images/class). The gap between HyperPgNet-noRRC and CBM on CUB is only 0.8% (76.5% vs 75.7%), which is within typical run-to-run noise. The authors should report results over multiple seeds with mean and std, or at minimum acknowledge this limitation.

### Minor

- **No quantitative interpretability metric**: The RRC loss is claimed to "enhance transparency," and Figure 4 shows qualitative gradient maps, but there is no quantitative measure (e.g., fraction of prototype activation inside annotated concept regions, or intersection-over-annotation-region). The large accuracy drop on Cars when adding RRC (88.6% → 81.2%, a 7.4% drop) is attributed to "increased transparency" without any evidence that the RRC-trained model is measurably more transparent.

- **No ablation or sensitivity analysis for the λ hyperparameters**: The multi-objective loss includes λ_Den and λ_RRC (line 261), with the claim that different λ values trade off accuracy vs. interpretability. No values are reported, and no sensitivity analysis is provided. A reader cannot reproduce the results or understand how sensitive performance is to these choices.

- **Missing some recent prototype-learning baselines**: The paper compares only to ProtoPNet and CBM. More recent methods discussed in Related Work (ProtoPShare, ProtoPool, ProtoTree, PIPNet, ProtoGMM, MGProto) are not evaluated. While ProtoGMM is sufficiently different from HyperPg (Euclidean multivariate Gaussians with EM vs. hyperspherical 1D Gaussian with backprop) to make a direct comparison non-trivial, including at least one additional modern baseline would strengthen the claim of outperforming "other prototype learning architectures."

- **The Segformer baseline's near-random performance is not adequately investigated**: Segformer achieves 17.7% on CUB and 1.9% on Cars. The paper attributes this to "overfitting" (line 386), but 1.9% on 196 classes is near chance, suggesting a training configuration problem (e.g., learning rate, optimization setup) rather than simple overfitting. If the baseline is not properly trained, it undermines confidence in the overall experimental setup, even though the main comparisons are against ConvNeXt/ProtoPNet/CBM which perform reasonably.

- **Uncontrolled differences in prototype count, training objectives, and supervision**: HyperPgNet uses 300/180 concept-shared prototypes, density/RRC losses, and concept mask supervision, while ProtoPNet uses 2000/1960 class-specific prototypes, cluster/separation losses, and only class labels. The comparison conflates multiple design choices. The "ProtoPNet + HyperPg" ablation helps but only controls for prototype type. The paper would benefit from a systematic ablation controlling one variable at a time.

### Trivial
None.

## Nice-to-Haves
- A sweep of prototype counts for both ProtoPNet and HyperPgNet to show accuracy vs. prototype count trade-offs.
- Quantitative interpretability metrics (e.g., IoU between prototype activation heatmaps and concept mask annotations) to substantiate the transparency claims.
- Reporting λ_Den and λ_RRC values used, with brief sensitivity analysis.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The claimed improvements are small (0.8–1.2% over CBM or ProtoPNet+HyperPg)"** — Cherry-picks the smallest gaps. HyperPgNet vs ProtoPNet shows 8.5% (CUB) and 2.2% (Cars) improvements, which are substantial. The 0.8% gap over CBM on CUB is small, but this concerns only one of several comparisons. The core claim (improvement over ProtoPNet) rests on much larger margins.
- **"The reader cannot tell whether HyperPgNet is genuinely better or merely less broken under this protocol"** — Overly speculative framing. All methods face the identical protocol; if the protocol favored HyperPgNet disproportionately, one would need a specific mechanism. The ConvNeXt baseline at 74.2% shows the protocol is not universally broken. This concern is subsumed by the Major weakness about the non-standard setup.
- **"ProtoGMM is a natural competitor and its omission is a significant gap"** — ProtoGMM operates in Euclidean space with multivariate Gaussians and EM training, which is architecturally quite different from HyperPg (hyperspherical, 1D Gaussian, end-to-end backprop). The paper explains this distinction clearly (lines 46–48). Including it would strengthen the paper, but its omission is not a "significant gap."
- **"Figure 3 shows convergence but no error bars"** — Subsumed under the general lack of variance reporting. The convergence curves are illustrative and consistent with the tabular results.
- **Nits about the abstract over-claiming** — Over-stated but not a specific, verifiable weakness. The paper does outperform ProtoPNet, which is the most standard baseline in this space.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not articulate.

## Suggestions

1. **Run experiments with a more standard training setup (cropped images, offline augmentation) to calibrate against published numbers**, even as a supplementary experiment on a subset. This would clarify whether the relative ordering holds under conditions where all baselines reach their expected performance.
2. **Include a controlled ablation that isolates concept alignment**: train ProtoPNet (or a standard hyperspherical prototype network) with concept masks + RRC loss but without HyperPg, to measure the standalone benefit of concept supervision.
3. **Report results over at least 3 random seeds** (mean ± std) for all experimental conditions, especially since the HyperPgNet vs. CBM gap on CUB is only 0.8%.
4. **Add a quantitative interpretability metric**: compute the fraction of prototype gradient activation that falls inside the annotated concept mask, with and without RRC, to substantiate the transparency claims.
5. **Report the specific λ_Den and λ_RRC values used** and include a brief sensitivity analysis.
6. **Address the Segformer collapse**: verify that the learning rate and optimizer settings are appropriate for this architecture under the 30-image setup.
