Now I have all the information needed. Let me write the final consolidated review.

## Summary

The paper proposes **VQ-Transplant**, a framework that enables plug-and-play replacement of VQ modules in pre-trained visual tokenizers while keeping the encoder-decoder frozen, followed by a lightweight 5-epoch decoder adaptation step. The key idea is to decouple VQ module development from costly end-to-end tokenizer retraining. The paper also introduces **MMD-VQ**, a distribution-aligned quantizer using maximum mean discrepancy. The framework is evaluated by integrating several VQ methods into the pre-trained VAR tokenizer, achieving 0.81 r-FID on ImageNet-1k reconstruction (vs. VAR's 0.92) with a 21.8× GPU-hour speedup.

## Strengths

- **The VQ-Transplant framework is a useful and practically-motivated contribution.** Decoupling VQ module development from full tokenizer retraining is a genuinely valuable idea. The two-stage design (substitution + decoder adaptation) is clean and well-motivated. The paper demonstrates that after only 5 epochs of decoder adaptation, the transplanted VQ modules outperform the original VAR tokenizer (0.81 r-FID vs. 0.92), validating the core thesis that VQ innovation need not require full retraining.

- **Table 1 provides compelling efficiency evidence.** VQ-Transplant completes in 22 hours on 2×A100s (44 GPU-hours), compared to VAR's 60 hours on 16×A100s (960 GPU-hours). This 21.8× (95%) reduction is well-documented with clear hardware specifications, making the efficiency gain concrete and verifiable.

- **Consistent improvement across diverse VQ algorithms.** Experimentation with five VQ methods (Vanilla, EMA, Online, Wasserstein, MMD) in both multi-scale and fixed-scale configurations, and across multiple codebook sizes, provides robust evidence that the framework is general rather than tied to a specific quantizer.

- **Cross-dataset evaluation (Tables 8-10) is genuinely informative.** Even the VQ Module Substitution phase (without any dataset-specific adaptation) outperforms fully-trained baselines on FFHQ (r-FID 2.09 vs. VQGAN-LC's 3.81), CelebA-HQ, and LSUN-Churches. This demonstrates that the framework's encoder retains strong generalization, and the additional decoder adaptation further improves results.

## Weaknesses

### Major

- **MMD-VQ's advantage over Wasserstein VQ is not empirically demonstrated.** The paper motivates MMD-VQ as being distribution-free and more compatible with non-Gaussian features than Wasserstein VQ, but Tables 3 and 7 show near-identical performance between the two methods across nearly all metrics and configurations. Wasserstein VQ occasionally wins (e.g., better PSNR/SSIM in several rows of Table 3). No experiment isolates when features are non-Gaussian, and no ablation separates the effect of the MMD loss from Wasserstein loss. The claim that MMD-VQ "improves compatibility with VQ-Transplant" is not supported by the data — both distribution-aligning methods work equally well, and the observed gains come from the VQ-Transplant framework itself, not from MMD.

- **The cross-dataset experiments do not specify the adaptation dataset.** Tables 8-10 report both "Substitution" and "Adaptation" phases for FFHQ, CelebA-HQ, and LSUN-Churches, but the paper never states whether the decoder adaptation was run on ImageNet-1k (as in all other experiments) or on each target dataset. If adaptation was done on each target dataset, the results are fine-tuning rather than a test of cross-dataset generalization. If done on ImageNet-1k, that would be a genuine cross-dataset result and would strengthen the paper, but the reader cannot determine which is the case. This ambiguity undermines the cross-dataset claim.

### Minor

- **Efficiency claims lack explicit caveats about the pre-trained model assumption.** The paper states "reducing training cost by 95%" (Abstract) and "21.8× faster" (Table 1) without clearly stating that this benefit is realized only when a pre-trained VAR tokenizer is already available. VQ-Transplant is a VQ-development framework that presupposes access to a pre-trained encoder-decoder — this is a reasonable framing, but the headline numbers could mislead a casual reader into thinking the total cost to replicate the full tokenizer is 95% lower. A single sentence acknowledging this assumption would resolve the issue.

- **Baseline comparisons in Table 2 mix cited and own numbers without unified re-evaluation.** Results marked † and * are cited from VQGAN-LC and Llama GEN, respectively. It is well-known that r-FID can vary with evaluation protocol (image size, number of real samples, Inception version). The paper does not state that baselines were re-evaluated under a unified protocol. While this practice is common in the field, the paper would be strengthened by either a controlled re-evaluation or a clear statement that comparisons are drawn from published numbers and may not be strictly comparable.

- **VQ-Transplant is only demonstrated on one pre-trained tokenizer (VAR).** All experiments use the VAR tokenizer as the backbone. The LDM-16 experiment (deferred to the appendix) shows lower compatibility. The paper would benefit from demonstrating the framework on at least one additional pre-trained tokenizer (e.g., VQGAN) in the main text to establish generality across tokenizer architectures.

### Trivial

- In the first paragraph of Section 4.1: "Our method has two parts: (1) VQ module substitution and (2) decoder adaptation" — these should be labeled Stage I and Stage II for consistency with the rest of the section.

- The "uniqueness-enhancing loss" $\mathcal{L}_{\text{unique}}$ in Equation (3) is defined as the MMD or Wasserstein loss, which are distribution-matching losses rather than explicit uniqueness losses. The naming could be clarified, e.g., as "distribution-alignment loss."

## Nice-to-Haves

- A synthetic or real-data experiment demonstrating a scenario where feature distributions are clearly non-Gaussian, and showing that MMD-VQ outperforms Wasserstein VQ in that setting, would substantiate the claimed advantage of MMD-VQ.

- A brief analysis of how the sub-vector partitioning strategy (for fixed-scale VQ) affects reconstruction quality — e.g., comparing different ways to partition the 32-dimensional features — would help assess the framework's generality.

- Reporting worst-case per-class r-FID on ImageNet-1k would strengthen the evidence that the 5-epoch adaptation does not cause selective degradation on rare or high-frequency classes.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Critic Point 5 (SOTA claim unsubstantiated):** Removed. The paper says "near state-of-the-art" in the abstract, not "state-of-the-art." Table 2 does compare against a reasonable set of baselines (VQGAN, VAR, RQVAE, etc.). While additional comparisons with the newest tokenizers would strengthen the paper, the results (0.81 r-FID) are clearly competitive, and the claim as written is appropriately qualified.

- **Critic's critique of codebook size disparity (MMD VQ uses 65536 vs VAR's 4096):** Removed. The paper's main comparison for multi-scale VQ (MMD VAR at K=4096 and K=8192) is directly comparable to VAR (K=4096). The fixed-scale MMD VQ results with larger codebook sizes are presented alongside VQGAN-family baselines that also use large codebooks (e.g., VQGAN-LC with K=100000).

- **Critic's "training instability" claim from Figure 3 fluctuations:** Removed. The paper acknowledges the fluctuations and correctly characterizes the overall downward trend. Minor epoch-to-epoch variation is expected in adversarial training and does not indicate instability.

- **Critic's point about lack of Limitations section:** Removed. While a limitations section would be nice, its absence is not a substantive flaw. The paper's framing makes the pre-trained model assumption sufficiently clear.

- **Critic's "Wasserstein VQ performance on par" as a weakness of the method:** This is retained but reframed — the issue is that MMD-VQ's differentiation from Wasserstein VQ is unsubstantiated, not that MMD-VQ performs poorly (it performs fine).

## Novel Insights

None beyond the paper's own contributions. The key insight — that VQ modules can be developed independently from full tokenizer training using a lightweight substitution-and-adaptation pipeline — is the paper's core contribution and is well-articulated.

## Suggestions

1. **Explicitly state the adaptation dataset in cross-dataset experiments (Section 5.3).** If adaptation was done on ImageNet-1k, say so and emphasize that the results are genuinely cross-dataset. If done on each target dataset, reframe the experiment as "domain adaptation with limited compute" rather than "cross-dataset generalization."

2. **Add a controlled re-evaluation** of the strongest baselines (at least VAR and VQGAN-LC) under a unified protocol on ImageNet-1k validation, or clearly state in the caption that comparisons are drawn from different evaluation settings.

3. **Either strengthen or de-emphasize MMD-VQ.** Either provide an experiment demonstrating MMD's advantage under non-Gaussian features, or explicitly acknowledge that MMD-VQ and Wasserstein VQ perform similarly in practice and reposition MMD-VQ as a complementary variant rather than a primary contribution.

4. **Acknowledge the pre-trained model assumption** explicitly in the Abstract and Introduction with a sentence such as: "This efficiency gain is realized when a pre-trained tokenizer is already available, which is the typical scenario for researchers developing new VQ methods."

5. **Demonstrate VQ-Transplant on a second pre-trained tokenizer** (e.g., a VQGAN from Llama GEN) in the main paper, or at minimum discuss why VAR was chosen and what aspects of generality remain untested.

## Score and Decision

### Anchor Calibration

**Round 1 (Bracketing):**
- Weak anchors (avg 2.5–3.0): VideoDiT (2.5, Reject), PyramidDrop (3.0, Reject), LVM-NET (3.0, Reject). These papers had weak evaluations or unclear contributions. VQ-Transplant is clearly stronger.
- Middle anchors (avg 3.5–6.25): How Many Tokens (5.75, Accept), BSQ (5.75, Accept), ImageFolder (6.25, Accept), Channel-wise Quantization (4.0, Reject). These papers have clear contributions with some evaluation concerns.
- Strong anchors (avg 7.5+): Vision Transformers Need Registers (8.0, Accept), FSQ (6.50, Accept), Vision-RWKV (8.0, Accept). These are clearly stronger papers.

**Round 1 bracket:** Narrowest plausible range is 4.5–6.5.

**Round 2 (Narrowing):**
- FSQ (6.50, Accept): Cleaner, simpler contribution with extensive experiments. VQ-Transplant is slightly weaker.
- BSQ (5.75, Accept): Comparable — both have a clear contribution with some reporting gaps. VQ-Transplant is at a similar level.
- How Many Tokens (5.75, Accept): Comparable — interesting contribution with some evaluation concerns.
- ε-VAE (5.67, Reject): Mixed reviews on novelty and metrics. VQ-Transplant is stronger.
- LL-VQ-VAE (4.75, Reject): Weaker evaluation, missing generative modeling results. VQ-Transplant is clearly stronger.

**Final Score:** 5.5. The paper has a genuinely useful contribution (VQ-Transplant), solid empirical validation of the core idea, and the efficiency gains are well-documented. However, the secondary contribution (MMD-VQ) is not differentiated from prior work, the cross-dataset experiments suffer from an ambiguity in the reported protocol, and the efficiency claims lack necessary caveats. These issues are fixable and do not invalidate the core contribution, but they prevent the paper from reaching the top of the middle band.

### Anchors Considered

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| IqGVIU4rvM (VideoDiT) | 2.50 | R1 | Weaker — limited contribution |
| 5ncdKonxd4 (PyramidDrop) | 3.00 | R1 | Weaker — different subfield, less novel |
| bEvI30Hb2W (LVM-NET) | 3.00 | R1 | Weaker — less established method |
| YlWvQSBCgl (Channel-wise Quant.) | 4.00 | R1 | Weaker — less comprehensive eval |
| sfTsvy05MX (LL-VQ-VAE) | 4.75 | R2 | Weaker — evaluation gaps, missing generative results |
| mb2ryuZ3wz (How Many Tokens) | 5.75 | R1/R2 | Comparable — similar evaluation rigor |
| yGnsH3gQ6U (BSQ) | 5.75 | R1/R2 | Comparable — similar strengths/weaknesses |
| 8ROIRnKloJ (ε-VAE) | 5.67 | R2 | Mixed — higher score variance, rejected |
| CP6CAqxAGJ (UnifyVocab) | 5.67 | R2 | Different domain (NLP), limited comparability |
| QE1LFzXQPL (ImageFolder) | 6.25 | R1/R2 | Slightly stronger — more thorough experiments |
| 8ishA3LxN8 (FSQ) | 6.50 | R2 | Slightly stronger — cleaner contribution |
| 2dnO3LLiJ1 (ViT Registers) | 8.00 | R1 | Stronger — top-tier paper |
| 7gUrYE50Rb (EQA-MX) | 8.00 | R1 | Stronger — different domain |
| nGiGXLnKhl (Vision-RWKV) | 8.00 | R1 | Stronger — different domain |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>