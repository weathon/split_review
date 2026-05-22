Now I have a thorough understanding of the paper and all claims. Let me write the final consolidated review.

---

## Summary

This paper proposes VQ-Transplant, a framework that enables plug-and-play replacement of VQ modules in frozen pretrained visual tokenizers (specifically VAR), followed by lightweight decoder adaptation (5 epochs on ImageNet-1k). This avoids costly end-to-end retraining. The paper also introduces MMD-VQ, a distribution-aligned quantization method using maximum mean discrepancy. Experiments across five VQ methods in both multi-scale and fixed-scale configurations show that VQ-Transplant can match or exceed the reconstruction fidelity of the original VAR tokenizer at a fraction of the training cost (21.8× speedup in GPU-hours, from 960 to 44).

## Strengths

- **Clear practical motivation and well-designed framework**: The core idea — decoupling VQ module development from full encoder-decoder retraining — addresses a genuine bottleneck. The two-stage pipeline (VQ substitution → decoder adaptation) is cleanly described and intuitively sound. The paper correctly identifies and resolves the decoder-quantization mismatch that arises after module substitution, as evidenced by the ablation (Table 3: r-FID improves from 1.52 to 0.91 after adaptation with MMD VAR K=4096).

- **Real and documented computational savings**: Table 1 shows VQ-Transplant requires 2×A100 GPUs for 22 hours (44 GPU-hours), versus 16×A100 for 60 hours for VAR from scratch (960 GPU-hours). This 21.8× speedup is a raw comparison of GPU-hours for achieving the final model and is correctly reported. Table 6 further validates efficiency by comparing VQ-Transplant to from-scratch training at similar compute budgets (22h vs 25h), where VQ-Transplant achieves r-FID 0.91 vs 1.40.

- **Comprehensive evaluation across five VQ methods**: Tables 3 and 7 systematically compare Vanilla VQ, EMA VQ, Online VQ, Wasserstein VQ, and MMD VQ under both multi-scale and fixed-scale configurations, at multiple codebook sizes, measuring quantization error, codebook utilization, and six reconstruction metrics. This provides a useful reference for the community.

- **Controlled comparison at matched settings shows genuine improvement**: MMD VAR with K=4096 (same 680 tokens, same codebook size as original VAR) achieves r-FID 0.91 vs VAR's 0.92, demonstrating that VQ-Transplant can match or slightly exceed the original at the same configuration.

## Weaknesses

### Major

- **MMD-VQ does not empirically distinguish itself from Wasserstein VQ**: MMD-VQ is presented as a secondary contribution that "makes no parametric assumptions" compared to Wasserstein VQ's Gaussian assumption. Yet across every experiment (Tables 3, 7, 8–10), the differences between MMD VQ and Wasserstein VQ are marginal (e.g., r-FID 0.91 vs 0.93 for multi-scale K=4096; 0.81 vs 0.83 for K=8192). The paper provides no experiment — synthetic or real — where non-Gaussian feature distributions cause Wasserstein VQ to degrade while MMD VQ succeeds. Without this, the claimed advantage of MMD-VQ is unsubstantiated. This does not undermine the VQ-Transplant framework itself (which works with either method), but weakens the secondary contribution significantly.

### Minor

- **Missing baseline: original VAR tokenizer on cross-dataset tasks**: In the cross-dataset generalization study (Section 5.3, Tables 8–10), VQ-Transplant variants are compared against fully-trained baselines (VQGAN, RQVAE, etc.) on FFHQ, CelebA-HQ, and LSUN-Churches. However, the performance of the *original frozen VAR tokenizer* (with its native VQ module) on these datasets is never reported. Since the paper's claim is that VQ-Transplant generalizes effectively, knowing whether the original tokenizer already performs well (or poorly) on these OOD datasets is essential context — otherwise the reader cannot tell if the transplantation improves, maintains, or degrades cross-dataset reconstruction. Given that VQ-Transplant outperforms full-training baselines, this omission is not fatal, but it is a meaningful gap in the evaluation.

- **"5 epochs suffice" is undersold by the paper's own extended results**: The paper emphasizes that decoder adaptation requires only 5 epochs. However, Table 5 and Figure 3 show that continuing adaptation to 20 epochs steadily improves r-FID (from 0.91→0.79 for K=4096, 0.81→0.74 for K=8192). The paper is transparent about this, but the framing ("only 5 epochs") should be qualified with the observation that 5 epochs is a pragmatic trade-off rather than a convergence point.

- **Decoder adaptation still requires GAN training**: While lighter than full retraining, the decoder adaptation stage uses adversarial training (DINO-S discriminator, DiffAug, consistency regularization) for 5 epochs on ImageNet-1k. This is acknowledged but somewhat undercuts the "democratization" narrative — the adaptation stage still requires non-trivial compute and GAN-specific tuning.

### Trivial

- In Equation (2), the variable name `\mathcal{L}_{Perf}` is unusual (likely "perceptual loss" abbreviated), though the description on line 80 clarifies what it computes. Minor typographical inconsistency.
- Table 1's "Speedup" column would benefit from an explicit formula (GPU-hour ratio) in the caption.

## Nice-to-Haves

- A controlled experiment (synthetic or real) demonstrating a non-Gaussian setting where MMD-VQ meaningfully outperforms Wasserstein VQ would substantially strengthen the secondary contribution.
- Reporting the original VAR tokenizer's performance on FFHQ, CelebA-HQ, and LSUN-Churches would complete the cross-dataset evaluation.
- Ablation of the multi-Gaussian kernel bandwidths in MMD-VQ would improve reproducibility.

## Removed Points

- **Criticism about "misleading efficiency comparison" (Critic's Issue 1)**: REMOVED. The critic argues that the 95% cost reduction claim is misleading because it omits the pretraining cost of the VAR encoder-decoder backbone (960 GPU-hours). This criticism fundamentally misunderstands the paper's contribution. The VQ-Transplant framework assumes a *pretrained tokenizer is already available* — which it is (publicly released by Tian et al., 2024). The comparison is: to obtain a VQ-Transplant model with a new VQ module, you need 44 GPU-hours; to train a full VAR tokenizer from scratch with that same VQ module, you need 960 GPU-hours. This is exactly how transfer learning / fine-tuning papers report savings. The 95% figure is accurate for this scenario.

- **Criticism about "incomparable baselines" regarding token count/codebook size (Critic's Issue 2, first part)**: PARTIALLY REMOVED. The critic says MMD VQ uses 512 tokens while VAR uses 680 tokens. However, the paper also reports MMD VAR at 680 tokens with K=4096 (same as VAR) achieving 0.91 r-FID vs 0.92 — a fair comparison. The other configurations are additional results showing what is achievable with larger codebooks. The different token counts across rows are clearly labeled. The concern about missing ViT-VQGAN/MaskGIT baselines is removed as unsubstantiated — the paper compares against published results from VQGAN-LC and Llama GEN, which are standard references in this space.

- **Criticism about "marginal MMD-VQ contribution" being fatal to the paper (Critic's Issue 4, framing)**: WEAKENED from "structural flaw" to Major weakness. MMD-VQ is presented as a *secondary* contribution. The primary contribution (VQ-Transplant framework) is evaluated with multiple VQ methods including Wasserstein VQ. Even if MMD-VQ were removed, the VQ-Transplant paper would still stand on its Wasserstein VQ results. However, the weakness is retained at Major because the paper markets MMD-VQ as a contribution that does not deliver on its claimed advantages.

- **Strength Finder claims about "state-of-the-art" reconstruction**: REMOVED. The Strength Finder claimed "outperforming the original VAR tokenizer" and "achieving state-of-the-art reconstruction performance across all three benchmarks." The paper's results are competitive but the r-FID differences over VAR are small, and claiming "state-of-the-art" across cross-dataset benchmarks overstates the evidence given the missing original-tokenizer baseline.

## Novel Insights

None beyond the paper's own contributions. The synthesis of reviewer comments did not surface any observation about the paper that is both new and not stated in the paper itself.

## Suggestions

1. Add the original VAR tokenizer's performance on FFHQ, CelebA-HQ, and LSUN-Churches to Tables 8–10. This single addition would significantly strengthen the cross-dataset generalization claims.
2. Either provide an experiment demonstrating MMD-VQ's advantage in non-Gaussian settings, or reframe MMD-VQ as an instantiation of the VQ-Transplant framework rather than a separate contribution.
3. Qualify the "5 epochs suffice" claim with a note about the empirical trade-off, since extended adaptation yields continued gains.
4. Mention explicitly in the abstract/intro that the efficiency comparison assumes access to a pretrained tokenizer (as is standard in fine-tuning settings).

## Score and Decision

**Calibration anchors** (from `calibration_search`):

| Anchor Path | Avg Score | Comparison |
|---|---|---|
| `BSQ-ViT` (yGnsH3gQ6U) | 5.75 | Similar topic (tokenization), similar evaluation breadth. The BSQ paper has stronger novelty in quantization scheme; this paper has stronger practical impact (plug-and-play framework). Comparable quality. |
| `ImageFolder` (QE1LFzXQPL) | 6.25 | Similar evaluation scope. This paper is slightly weaker on novelty but stronger on practical contribution. |
| `Wasserstein VQ` (nS2DBNydCC) | 4.75 | Directly related prior work. The Wasserstein VQ paper has similar issues with marginal empirical gains but less experimental breadth. This paper is stronger overall due to the VQ-Transplant framework. |
| `SEED` (0Nui91LBQS) | 6.33 | More ambitious scope, but similar methodological rigor. |
| `"How many tokens"` (mb2ryuZ3wz) | 5.75 | Similar evaluation rigor. Both papers have clear contributions with some limitations in experimental design. |
| `Balancing Token Efficiency` (IqGVIU4rvM) | 2.50 | Fundamentally weaker — conceptual misunderstandings, poor results. This paper is clearly far above this level. |
| `LL-VQ-VAE` (sfTsvy05MX) | 4.75 | Similar space (lattice VQ). This paper has stronger empirical evaluation. |

Relative to these anchors, VQ-Transplant is a solid paper with a well-motivated contribution, a clean framework, and broad experiments. The main weaknesses (marginal MMD-VQ distinction, missing cross-dataset baseline) are addressable and do not undermine the core contribution. The paper is clearly above the reject-level papers (2.50–4.75) and comparable to accepted tokenization papers (5.75–6.25). I place it slightly below the strongest in this band due to the secondary contribution issue.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>