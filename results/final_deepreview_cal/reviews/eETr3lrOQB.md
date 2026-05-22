Now I'll write the final consolidated review.

## Summary

2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
// List only reasonable points. Rank by severity.
// Not every paper has weaknesses at every tier. Leave a tier empty (or write "None") if nothing qualifies.

### Fatal
// Errors that invalidate the paper's core claims or results.
// Examples: fundamentally flawed methodology, unsupported central claim, incorrect proofs, data fabrication concerns.
// Most papers have none. Leave empty if none apply.

### Major
// Issues that a reviewer would weigh against acceptance, and that the authors should fully resolve in a rebuttal.
// Examples: missing critical baseline, overclaimed scope unsupported by experiments, significant methodological gap.
// Not every paper has major weaknesses. Do not invent them to fill this section.

- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
// Issues worth the authors' attention but unlikely to change an accept/reject decision.
// Examples: addressable in rebuttal, limited scope of one experiment, unclear phrasing of a claim, missing ablation that would strengthen but not invalidate.

- weakness 1 — why it matters

### Trivial
// Small issues the authors should fix but that carry no weight in evaluation.
// Examples: typos, minor notation inconsistencies, suboptimal figure choices, small presentation issues.

- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Include something like this "These points are flagged to be removed, treat them with caution"
Weaknesses that are removed keep the details of the S/W just in case they are useful 

## Novel Insights
One paragraph synthesizing genuinely novel observations.
If no genuinely novel insight emerges from the reviews beyond the paper's own contributions, write
"None beyond the paper's own contributions."

## Suggestions
- specific actionable suggestion

DO differentiate between papers of varying quality clearly.

Do evaluate the paper on these axis using language first.
Originality, importance of research question addressed, whether the claims are well supported, soundness of experiments, clarity of writing, and value to the research community

## Score and Decision
After you finish writing a review, assign a score to the review. 

Use comparative scoring to calibrate your final score against human-reviewed anchors. Retrieval is iterative: first a wide bracketing pass to find which score range the paper plausibly sits in, then one or two narrowing passes to anchor inside that range.## Summary

This paper proposes **VQ-Transplant**, a framework that replaces the native VQ module of a pre-trained visual tokenizer (e.g., VAR) with a new VQ module while keeping the encoder and decoder frozen, then performs lightweight decoder adaptation (5 epochs on ImageNet-1k) to resolve the resulting decoder–quantization mismatch. A secondary contribution is **MMD-VQ**, a VQ method using maximum mean discrepancy for distributional alignment. Experiments show that VQ-Transplant with MMD-VQ achieves reconstruction fidelity (0.81 r-FID) competitive with or exceeding the original VAR tokenizer (0.92 r-FID) at substantially lower training cost (~44 GPU-hours vs. 960 GPU-hours for VAR from scratch).

## Strengths

1. **Well-motivated and practically useful framework.** The core idea—decoupling VQ module development from full tokenizer retraining by fixing encoder-decoder weights and cheaply adapting only the decoder—is clearly motivated and addresses a real bottleneck in VQ research. The two-stage design (substitution then decoder adaptation) is cleanly described and the decoder-quantization mismatch is convincingly demonstrated (Table 3: substitution alone yields 1.52 r-FID, adaptation improves to 0.91).

2. **Decoder adaptation is convincingly shown to resolve the mismatch.** Tables 3 and 7 systematically compare 5 VQ methods (Vanilla, EMA, Online, Wasserstein, MMD) × multiple codebook sizes × two phases (substitution vs. adaptation) within the *same* VAR backbone. Every method improves after decoder adaptation, and distribution-aligning methods (Wasserstein, MMD) consistently surpass the original VAR tokenizer's r-FID. This internal control is the strongest evidence for the framework.

3. **Extensive evaluation across methods, codebook sizes, and datasets.** The paper evaluates 5 VQ algorithms at codebook sizes from 4K to 65K, on both multi-scale and fixed-scale variants, and demonstrates cross-dataset generalization to FFHQ, CelebA-HQ, and LSUN-Churches (Tables 8–10). The ablation on adaptation epochs (Table 5, Figure 3) further shows continued improvement from 5 to 20 epochs, supporting the flexibility of the approach.

4. **Clear exposition.** The problem is well-framed, the two-stage pipeline is easy to follow, and the paper honestly acknowledges limitations (e.g., that from-scratch tokenizers need hundreds of epochs, that the LDM-16 tokenizer shows lower adaptability).

## Weaknesses

### Fatal
None.

### Major

1. **The headline speedup claim (21.8×) confounds dataset, initialization, and method.** Table 1 compares VQ-Transplant (2×A100, 22h, ImageNet-1k, fine-tuning from a pre-trained backbone) against VAR (16×A100, 60h, OpenImages, trained from scratch). The 21.8× GPU-hour ratio conflates three simultaneously varying factors: (i) dataset size (OpenImages is larger than ImageNet-1k), (ii) training paradigm (from scratch vs. fine-tuning), and (iii) hardware scaling efficiency. The paper discloses these conditions in the table, so this is not a fatal omission, but the reader cannot determine how much of the speedup is attributable to the VQ-Transplant method itself versus these uncontrolled factors. A controlled baseline—e.g., fine-tuning the full pre-trained VAR (encoder + decoder + native VQ) on ImageNet-1k for matched GPU-hours—would isolate the benefit of freezing the encoder.

2. **MMD-VQ's advantage over Wasserstein VQ is very small.** After decoder adaptation at K=4096, MMD VAR achieves 0.91 r-FID vs. Wasserstein VAR at 0.93 (Table 3). At K=8192, MMD VAR = 0.81 vs. Wasserstein VAR = 0.83. These 0.01–0.02 r-FID differences are tiny, and no error bars or multiple-run statistics are reported anywhere in the paper. Without statistical grounding, the claimed superiority of MMD-VQ over Wasserstein VQ is not demonstrated. The paper's secondary contribution is weakened as a result.

3. **No variance or confidence intervals reported for any metric.** Reconstruction metrics (r-FID, PSNR, SSIM, LPIPS) are reported as point estimates with no indication of run-to-run variation. Since differences as small as 0.01 r-FID are used to compare methods (e.g., MMD VAR 0.91 vs. original VAR 0.92), the absence of any error quantification makes it impossible to assess whether observed improvements are meaningful or within noise. This is a standard expectation for empirical papers and its absence is a notable gap.

### Minor

1. **Missing ablation: decoder fine-tuning with the original VQ module.** The paper does not include a control experiment where the decoder is adapted for 5 epochs *without* changing the VQ module (i.e., fine-tuning the original VAR tokenizer on ImageNet-1k). This would separate the benefit of VQ module replacement from the benefit of any decoder fine-tuning, and would strengthen the claim that VQ-Transplant's gains come from the new VQ method rather than simply from additional training.

2. **Cross-dataset comparisons are against from-scratch baselines, not fine-tuned baselines.** Tables 8–10 show VQ-Transplant (which leverages a pre-trained backbone) outperforming methods like VQGAN-LC trained from scratch on each target dataset. While impressive, a fairer comparison would be against a baseline that also starts from a pre-trained generic tokenizer and fine-tunes it on the target dataset (with either the native VQ or a replacement) for matched compute. The current comparisons demonstrate generalization of the backbone more than superiority of the VQ method.

3. **Stage I training budget (epochs) is not specified in the main text.** The paper specifies exactly 5 epochs for Stage II (decoder adaptation), but does not state how many epochs or iterations are used for Stage I (VQ module substitution). The appendix is referenced but not available for inspection. This is needed for reproducibility.

4. **The term "uniqueness-enforcing loss" is imprecise for MMD.** Equation (3) defines \(\mathcal{L}_{\text{unique}}\) as a general term, and Section 4.2 sets \(\mathcal{L}_{\text{unique}} = \mathcal{D}^2_{\text{MMD}}\). MMD encourages distribution *matching*, not "uniqueness" per se. The naming is inherited from the Wasserstein VQ context, but for MMD-VQ it would be clearer to call it a distribution-alignment loss.

### Trivial
None.

## Nice-to-Haves

- An ablation adapting the decoder with the *original* VQ module for the same 5 epochs would cleanly separate the effect of VQ replacement from decoder fine-tuning.
- Visualizing feature distributions or quantifying their non-Gaussianity (e.g., skewness, kurtosis) would empirically motivate the claim that MMD handles non-Gaussian features better than Wasserstein VQ.
- Reporting variance across multiple training seeds, at least for the main comparisons (Table 3, K=4096 and K=8192), would significantly strengthen the empirical claims.

## Removed Points

*These points were raised in the reviews but are not included as weaknesses in the main review. They are recorded here for reference.*

- **"from-scratch training for 5–7 epochs is a strawman"** (Harsh Critic). The paper explicitly acknowledges "discrete tokenizers typically require hundreds of epochs when trained from scratch" (Section 5.1). The comparison is presented to show that VQ-Transplant offers a favorable trade-off, not to claim that from-scratch training is a serious competitor at that budget. The paper is transparent about this.
- **"The paper does not discuss how the discriminator is initialized."** The paper states "We follow Tian et al. (2024)...and employ an identical frozen DINO-S discriminator" (Section 4.1). This sufficiently addresses the point.
- **"The r-FID curves show fluctuations but no explanation."** The paper notes "Despite some fluctuations, there is a clear overall downward trend." Explaining individual epoch-level fluctuations in adversarial training is not necessary for the paper's claims and is well within expected training dynamics.
- **"The paper mentions Joint Optimization in Appendix C but does not include the table in the main text."** Appendix content is standard practice for secondary experiments. The paper appropriately summarizes the finding in the main text.
- **"Novelty is not new in spirit—many fine-tuning pipelines involve partial retraining."** This is a generic criticism that applies to any fine-tuning method. The paper's specific contribution (replacing VQ modules in frozen encoder-decoders with decoder-only adaptation) is concretely novel and well-delineated.
- **Strength about "95% training cost reduction."** While the speedup is directionally correct, the confounds in the comparison (as discussed in Major weakness #1) make the precise percentage difficult to interpret. The direction of the result is solid, but the exact number should be treated as approximate.

## Novel Insights

None beyond the paper's own contributions. The core research insight—that the decoder in a pre-trained VQ tokenizer can be cheaply re-aligned to a new quantization space via 5 epochs of adaptation—is well supported and is the paper's main novel finding. The review process did not surface additional insights beyond what the paper itself articulates.

## Suggestions

1. **Add a controlled speedup comparison.** Fine-tune the full pre-trained VAR (encoder + decoder + native VQ) on ImageNet-1k for the same 22 GPU-hours used by VQ-Transplant, and report r-FID. This would directly isolate the benefit of freezing the encoder.
2. **Report error bars.** At minimum, run the main comparisons (Table 3, K=4096 and K=8192) with 3 random seeds and report mean ± std. This is critical given the small metric differences used to assert method superiority.
3. **Add the missing decoder-only-adaptation control.** Show the result of adapting the decoder for 5 epochs *without* replacing the VQ module. This would make the benefit of VQ replacement unambiguous.
4. **Reconsider the prominence of the MMD-VQ contribution.** Given the marginal (0.01–0.02 r-FID) improvement over Wasserstein VQ, consider either presenting MMD-VQ as an incremental improvement over Wasserstein VQ, or strengthening the empirical demonstration of its advantages (e.g., showing cases where non-Gaussian feature distributions materially harm Wasserstein VQ but not MMD-VQ).
5. **Specify the Stage I training budget** (epoch count, iterations) in the main text for reproducibility.

## Evaluation Summary

- **Originality:** Good. The VQ-Transplant framework is a novel and pragmatic solution to a real problem. MMD-VQ is less novel (incremental over Wasserstein VQ).
- **Importance of research question:** High. Reducing the computational barrier to VQ method development is practically important.
- **Claims support:** Moderate. The core claim (VQ-Transplant enables cheap VQ integration) is well supported by internal comparisons. The stronger claims about speedup magnitude and MMD-VQ superiority are less well supported.
- **Soundness of experiments:** Adequate but improvable. The internal comparisons are sound; the cross-dataset and speedup comparisons have confounds. Lack of error bars is a concern.
- **Clarity of writing:** Strong. The paper is well-organized and clearly written.
- **Value to community:** Positive. The framework enables rapid VQ prototyping, and the code release will be valuable.

## Score and Decision

**Calibration:** Round 1 bracketing compared against weak anchors (avg 2.50–3.20, rejected tokenization papers), middle anchors (avg 5.75–6.33, accepted tokenization/adaptation papers), and strong anchors (avg 7.67–8.00, breakthrough papers). Initial bracket: 4.5–6.5. Round 2 narrowing compared against BSQ-ViT (5.75, accepted), "How many tokens" (5.75, accepted), ElasticTok (6.00, accepted), and LaVIT (6.25, accepted). VQ-Transplant is comparable to BSQ-ViT (5.75) in scope and quality, with a stronger framework contribution but a weaker-specific VQ method and more confounded speedup comparisons. Final score: **5.5**.

**Anchors retrieved:**
| Anchor ID | Score | Round | Comparison |
|-----------|-------|-------|------------|
| IqGVIU4rvM | 2.50 | R1 low | Much weaker (VQ+diffusion tokenizer, rejected) |
| TDzAqTqDHV | 3.00 | R1 low | Much weaker (retrieval quantization, rejected) |
| vK8C37eHXM | 3.20 | R1 low | Much weaker (diffusion autoencoders, rejected) |
| orG37FHN4b | 3.00 | R1 low | Much weaker (data-free quantization, rejected) |
| mb2ryuZ3wz | 5.75 | R1 mid / R2 | Comparable (variable-length tokenization, accepted) |
| FlvtjAB0gl | 6.25 | R1 mid / R2 | Slightly stronger (LaVIT, dynamic tokenization, accepted) |
| 0Nui91LBQS | 6.33 | R1 mid | Slightly stronger (SEED tokenizer for LLMs, accepted) |
| 3TnLGGHhNx | 6.00 | R1 mid | Slightly stronger (BPE image tokenizer, accepted) |
| 2dnO3LLiJ1 | 8.00 | R1 high | Much stronger (breakthrough ViT paper, accepted) |
| GMwRl2e9Y1 | 8.00 | R1 high | Much stronger (VQ rotation trick, accepted) |
| CxXGvKRDnL | 8.00 | R1 high | Much stronger (diffusion compression, accepted) |
| QQBPWtvtcn | 7.67 | R1 high | Much stronger (view synthesis, accepted) |
| yGnsH3gQ6U | 5.75 | R2 | Comparable (BSQ-ViT, new VQ method, accepted) |
| tFV5GrWOGm | 6.00 | R2 | Slightly stronger (ElasticTok, adaptive tokenization, accepted) |
| CjPt1AC6w0 | 6.25 | R2 | Different topic (synthetic data), rejected on other grounds |
| MNShbDSxKH | 5.75 | R2 | Different topic (neuro-symbolic reasoning, accepted) |
| kZvor5aaz7 | 6.25 | R2 | Different topic (slot-guided diffusion, accepted) |
| kcmK2utDhu | 5.80 | R2 | Different topic (multi-view adapter), rejected on other grounds |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>