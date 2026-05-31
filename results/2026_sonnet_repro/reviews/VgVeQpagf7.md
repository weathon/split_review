Now let me read the calibration samples to properly anchor my score.Round 1 bracket: **6.5 – 8.5**. The paper is substantially stronger than the low/mid band anchors (avg 2.5–6.0 on DP+synthetic-data topics) and broadly comparable to the high-band DP generative approach (avg 8.0, text domain). Let me narrow within this range.Now I have sufficient calibration. Let me compile the final review.

**Calibration summary:**
- Round 1 bracket: **6.5–8.5**
- Round 2 anchors (inside bracket):
  - `YEhQs8POIo` (avg 6.25, accepted): DP synthetic images via foundation model APIs — similar contribution but weaker (no downstream classification vs DP-SGD comparison). Paper under review is clearly better.
  - `1NHgmKqOzZ` (avg 6.33, accepted): progressive dataset distillation — no privacy, marginal gains, mixed reviews. Paper under review is clearly better.
  - `oZtt0pRnOl` (avg 8.0, accepted): DP few-shot generation for LLMs — comparable landmark contribution, unanimous 8s, clean results. Paper under review has more novel technique but also more verifiable weaknesses (overclaim, missing ablation).
  - `C8niXBHjfO` (avg 6.0, accepted): synthetic data privacy study — empirical, limited novelty. Paper under review is better.

Paper under review is **above** the 6.0–6.33 cluster and **just below** the 8.0 anchor. Final score: **7.0**.

---

## Summary

SPS and SPS+ are differentially private dataset distillation algorithms that replace DP-SGD's iterative gradient perturbation with a one-shot privatization of activation statistics collected via a publicly pretrained model. Two key algorithmic innovations—grouped pseudo-classes and multistage clipping—dramatically improve performance on high-class-count tasks, lifting CIFAR-100 accuracy from 48.9% (SPS, ε=1) to 71.0% (SPS+, ε=1) and making this the first generation-based approach to match gradient-based DP training on image classification. Because the method produces a distributable synthetic dataset rather than a trained model, it unlocks free ensembling, federated aggregation, and continual learning that are infeasible under DP-SGD's composition constraints.

---

## Strengths

1. **Landmark single-number result — first generation-based method to match DP-SGD on images.** Table 1 shows SPS+ WRN34-10 ensemble at ε=1 reaching 96.2%/76.6% on CIFAR-10/100, versus DP-SGD's 94.8%/70.3% under the same privacy budget. This claim is verifiable from Table 1 and closes a long-standing gap in the DP literature.

2. **Grouped pseudo-classes and multistage clipping produce a large, quantified improvement on hard tasks.** At ε=1 on CIFAR-100, SPS (basic) reaches 48.9% while SPS+ reaches 71.0% (Table 1) — a 22-point gap attributable to the two algorithmic innovations described in Section 4. The contribution is not just conceptual; the effect size is large.

3. **Free ensembling and practical flexibility with genuine experimental backing.** Because the privatized dataset can be reused without additional privacy cost (post-processing property, Section 5.1), the paper demonstrates model ensembling (Table 1), asynchronous federated aggregation (Figure 5d–e, 86%→89.5% with 1→5 parties at ε=1), and class-incremental continual learning (Figure 5c, 68.1% at ε=4 vs 76.9% non-continual). Each is demonstrated with numbers, not just claimed.

4. **Dimensionality reduction argument for improved SNR.** Section 3.2.2 gives a principled justification: by tuning D_G and D_C, the privatized statistic vector has dimensionality ~10⁵ vs ~10⁷ for DP-SGD gradients, yielding higher SNR under the same privacy budget. This is a concrete technical reason for the method's advantage at tight budgets.

5. **Robustness under domain shift.** On CAMELYON17 histopathology (Table 2), SPS achieves 92.6% at ε=8, outperforming DP-Diffusion (91.1% at ε=10) and DP-SGD (90.5% at ε=10). The comparison is actually more favorable than stated: SPS achieves better accuracy at a strictly tighter privacy budget.

6. **Clean privacy analysis.** Theorem 4.1 gives the M-fold composition of Gaussian mechanisms as an explicit (α, ε)-RDP bound, enabling transparent conversion to (ε,δ)-DP. The privacy-sensitive step is confined to a single statistic collection phase, making the analysis simpler than DP-SGD.

---

## Weaknesses

### Fatal
None.

### Major

- **The "every setting" claim in Section 5.1 is directly contradicted by Table 1.** The paper asserts "SPS+ matches or exceeds DP-SGD in every setting." For the matched-architecture (WRN28-10 vs WRN28-10) single-model comparison on CIFAR-100, SPS+ trails DP-SGD at ε≥2: −0.4% at ε=2, −3.0% at ε=4, −4.3% at ε=8. The advantage holds only at ε=1 (and is marginal there: +0.7%). On CIFAR-10, SPS+ is generally on par or better, so the dataset-level picture is split, not uniform. The paper should either restrict this claim to ensembles or to ε=1 settings, or acknowledge the single-model CIFAR-100 limitation explicitly. This is an evidential overclaim that misrepresents the paper's own Table 1.

- **GSAM ablation is absent from the main body.** Section 3.2.5 introduces GSAM as part of the downstream training pipeline and notes it is free under post-processing. However, no ablation is provided showing how much accuracy GSAM contributes to the headline numbers. Since DP-SGD cannot easily use GSAM (it requires two gradient evaluations per step in the private phase), part of the headline advantage may be attributable to the optimizer rather than the privatization method itself. A single ablation row (SPS+ with standard SGD vs. GSAM) would properly attribute the gain.

### Minor

- **Value of M not stated in Table 1.** Figure 2 shows M has a 2–5 percentage-point effect on CIFAR-100 accuracy. The caption for Table 1 does not specify M, so the reader cannot interpret the reported SPS+ numbers or understand the effective privacy budget per stage. Section 5.1 says M is varied but does not pin down the M used in Table 1. The caption or table footnote should state M for each SPS+ row. (Figure 3's caption does give M=2,4 for CIFAR-10/100, but this only applies to that specific figure.)

- **Performance plateau of SPS+ on CIFAR-100 with ε is unanalyzed.** SPS+ WRN28-10 on CIFAR-100 gains approximately 3.3/1.9/1.3 percentage points per doubling of ε, while DP-SGD gains 4.4/4.5/2.6. The divergence grows with ε, suggesting SPS+ converges to a lower ceiling than DP-SGD on harder tasks at looser budgets. The paper neither remarks on this nor analyzes it. Understanding whether the plateau is due to the dimensionality cap (D_G, D_C) or the Gaussian model assumption would sharpen the paper's scope claims.

- **Notation conflict in Theorem 4.1.** The theorem states ε = Mα/(2δ²), where δ is the noise multiplier. However, δ is already overloaded in the paper to denote the failure probability in (ε, δ)-DP (see Section 2.1 and Section 5.1 where δ=10⁻⁵). The noise multiplier is called b₀ in Section 3.2.2 but reappears as δ in Theorem 4.1. This collision in notation in a differential privacy paper should be resolved.

- **SPS vs SPS+ distinction not flagged for CAMELYON17.** Section 5.2 uses SPS (not SPS+), because the pseudo-class technique does not apply to binary classification. This fact is stated in parentheses but not prominently flagged. Readers comparing Table 1 (SPS+ results) to Table 2 (SPS results) may conflate the two.

### Trivial

- Generation cost is acknowledged as a limitation in Section 6 ("relatively heavy") but the reader is sent to the appendix. Even a rough order-of-magnitude comparison to DP-SGD wall-clock time in the main text would help evaluate practical deployability.

---

## Nice-to-Haves

- Analysis of *why* SPS+ plateaus faster with ε on CIFAR-100 (e.g., is it the D_G/D_C cap? The Gaussian assumption?). If the plateau is due to the dimensionality cap, increasing D at looser ε budgets might recover performance. This would transform an unexplained gap into a positive contribution.
- A brief characterization of computation cost in the main text. SPS generates 50,000 images by optimizing a loss through a deep network; even one sentence quantifying this relative to DP-SGD training time would be informative.
- For the federated learning ablation, comparing to standard (non-federated) SPS+ as an upper bound would clarify the privacy cost of fragmentation.

---

## Removed Points

*These points are flagged as removed; treat them with caution.*

- **Harsh Critic: "noise redistribution formula |v|_max = K_clip √(2LD_G^layer) assumes a specific choice of D_C and D_G rather than being a general result."** The paper's text in Section 3.2.4 reads: "Correspondingly, we clip according to |v|_max = K_clip√(LD_G^layer + S|L_C|D_C^layer) = K_clip√(2LD_G^layer)." The equality holds because S is defined as S = LD_G^layer / (|L_C|D_C^layer), making the substitution algebraically exact given S. This is a valid simplification, not an unjustified assumption. **Removed: the math is correct.**

- **Harsh Critic: "CAMELYON17 comparison is slightly unfavorable to SPS."** The critic misread this section. SPS at ε=8 outperforms DP-Diffusion and DP-SGD at ε=10, which is the favorable direction for the authors. **Removed: no issue here.**

- **Strength Finder: "Effective adaptation of dataset distillation to DP" citing ablation in Appendix B.1.** The ablation is in the stripped appendix and cannot be verified. The underlying design choice (class-conditional statistics to replace soft labels) is well-motivated in the main text, but the strength as stated partially depends on unverifiable appendix content. **Filtered: retained the design-choice logic without citing the stripped ablation.**

- **Strength Finder: "Robustness of SPS is validated by ablation in Appendix B.1."** Same as above — appendix stripped. **Removed as standalone strength.**

---

## Novel Insights

The paper's most surprising contribution is not the accuracy number itself but the *mechanistic* argument for why generation-based privacy can match gradient-based privacy: by releasing activation statistics rather than gradients, the privatized vector's dimensionality drops from ~10⁷ (DP-SGD) to ~10⁵, yielding a 100× improvement in SNR under the same noise budget. This reframing — privacy as a dimensionality-reduction problem at the representation level rather than the gradient level — suggests a broader principle: for any task where sufficient information about the data distribution can be summarized in a compact statistic, generation-based privacy will asymptotically dominate gradient-based approaches under tight budgets. The grouped pseudo-class technique is an independently interesting observation: constructing overlapping random groupings of classes allows each pseudo-class to pool more samples per statistic estimate, reducing per-class noise by a factor of N_{c/p} without changing privacy cost. This is a combinatorial trick that may be reusable in other high-class-count private estimation problems.

---

## Suggestions

1. **Correct the "every setting" claim in Section 5.1.** Replace with: "SPS+ matches or exceeds DP-SGD in every setting on CIFAR-10 and in ensemble configurations across all budgets on CIFAR-100; for single models on CIFAR-100, the advantage holds at ε=1 but DP-SGD is substantially better at ε≥4." This is honest and still a strong result.
2. **Add M to Table 1.** One column or a footnote stating "M=X for SPS+" removes an unnecessary reproducibility ambiguity.
3. **Add one GSAM ablation number.** Report SPS+ accuracy on CIFAR-100 (ε=1 or ε=4) with standard SGD vs. GSAM. This one data point properly attributes the headline numbers.
4. **Rename δ in Theorem 4.1.** Use b₀ or σ_n to avoid collision with (ε, δ)-DP notation. This is a one-line change.
5. **Flag SPS vs SPS+ in Section 5.2 prominently.** State clearly in the section heading or first sentence that CAMELYON17 uses SPS (not SPS+) due to binary classification.

---

## Score and Decision

**Calibration against anchors:**

| Anchor path | Avg human score | Round | Comparison |
|---|---|---|---|
| `TbOcySs6g8.md` | 2.50 | R1 | Clearly weaker — rudimentary DP+synthetic approach, rejected |
| `0rS9o1uKqu.md` | 2.50 | R1 | Unrelated (model inversion); much weaker |
| `sruGNQHd7t.md` | 3.00 | R1 | Weaker — no formal DP, heuristic privacy |
| `mJ8k81O5BF.md` | 3.00 | R1 | Unrelated (quantization); much weaker |
| `ckabXglfiT.md` | 4.75 | R1 | Weaker — related (DD + DP) but performance far below DP-SGD |
| `C8niXBHjfO.md` | 6.00 | R1/R2 | Weaker — no novel algorithm; empirical study only; single dataset |
| `F52tAK5Gbg.md` | 4.00 | R1 | Weaker — DP-SGD variant for contrastive loss; narrower contribution |
| `1NHgmKqOzZ.md` | 6.33 | R1/R2 | Weaker — dataset distillation without privacy, marginal improvement |
| `PjIe6IesEm.md` | 5.75 | R2 | Weaker — heuristic privacy defense for diffusion, no formal DP |
| `txZVQRc2ab.md` | 6.00 | R2 | Comparable but weaker — DP diffusion with utility loss, no milestone claim |
| `YEhQs8POIo.md` | 6.25 | R2 | Below — DP image synthesis via APIs, good but no downstream classification vs DP-SGD |
| `8rbkePAapb.md` | 6.20 | R2 | Below — privacy+fairness framework, narrower contribution |
| `sVNfWhtaJC.md` | 6.50 | R2 | Below — DP synthetic text for ICL, adaptive noise, competitive performance in text domain |
| `oZtt0pRnOl.md` | 8.00 | R1/R2 | Comparable — DP few-shot generation for LLMs, unanimous 8s, landmark result in text domain, but paper under review has more technical novelty and verifiable weaknesses |

**Round 1 bracket:** 6.5–8.5

**Round 2 narrowing:** The paper is clearly above the 6.0–6.33 cluster (which have narrower scope, no DP formal guarantees or weaker milestone claims). It is somewhat below the 8.0 anchor (`oZtt0pRnOl`): that paper received unanimous 8s with essentially no weaknesses flagged, while the paper under review has a verifiable evidential overclaim and a missing key ablation. Score: **7.0**.

**Axis assessment:**
- **Originality**: High. The framing of privacy as activation-statistic matching, grouped pseudo-classes as a combinatorial noise-reduction trick, and multistage clipping adapted from DP mean estimation are all novel combinations.
- **Importance of research question**: High. Closing the gap between generation-based and gradient-based DP approaches in images is a long-standing problem with direct impact on practical DP systems.
- **Claims supported**: Mixed. The ensemble results and CIFAR-10 results are well-supported; the "every setting" claim for single-model CIFAR-100 is not.
- **Soundness of experiments**: Generally good; GSAM ablation gap and unspecified M are the main issues.
- **Clarity of writing**: Good. Section structure is clear; notation collision in Theorem 4.1 is the main issue.
- **Value to the research community**: High. First generation-based milestone on images, plus a useful analysis of SNR framing and practical flexibility advantages.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>