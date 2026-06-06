## Summary

VQ-Transplant is a two-stage framework for decoupling VQ module development from expensive end-to-end encoder-decoder retraining. Stage I substitutes a new VQ module into a frozen pretrained tokenizer (e.g., VAR); Stage II applies lightweight decoder adaptation (5 epochs on ImageNet-1k) to close the decoder-quantization mismatch. The paper also proposes MMD-VQ, a companion quantization method using Maximum Mean Discrepancy for distribution alignment. The system achieves r-FID of 0.81 on ImageNet-1k using VAR as the backbone, surpassing the original tokenizer's 0.92.

---

## Strengths

- **Framework addresses a real and demonstrably costly bottleneck.** Table 1 documents that current industry-level tokenizers require 44–12,800 A100-GPU-hours for training. The two-stage design (substitution + lightweight adaptation) offers a principled alternative that enables rapid VQ iteration without full retraining.

- **Decoder adaptation is well-validated.** Table 3 shows that after VQ substitution alone, MMD VAR (K=8192) has r-FID=1.49; after 5 epochs of decoder adaptation, it improves to 0.81—surpassing the original VAR tokenizer's 0.92. Figure 2 provides visual confirmation that decoder adaptation recovers high-frequency detail lost after substitution.

- **Generality across five VQ algorithms demonstrated.** Tables 3 and 7 show the framework works for Vanilla, EMA, Online, Wasserstein, and MMD VQ in both multi-scale and fixed-scale configurations, confirming the framework's algorithm-agnostic character.

- **Distribution-alignment VQ methods (Wasserstein, MMD) consistently achieve the best compatibility.** Across Tables 3 and 7, both attain lower quantization error and 100% codebook utilization compared to Vanilla, EMA, and Online VQ, providing a systematic insight for future VQ algorithm design.

---

## Weaknesses

### Fatal

None.

### Major

- **Efficiency framing excludes the prerequisite pre-training cost.** The abstract claims "95% reduction in training cost" and Table 1 shows a "21.8× speedup over VAR." However, VQ-Transplant starts from a fully pre-trained VAR tokenizer that itself required 16 × A100 × 60 hours = 960 GPU-hours, while VQ-Transplant uses 2 × A100 × 22 hours = 44 GPU-hours. The 21.8× figure compares only the adaptation cost against full VAR training, treating the 960-GPU-hour prerequisite as free. The legitimate value proposition is amortization: across N VQ experiments, total cost is 960 + N×44 vs. N×960, which is a strong argument *that the paper does not make explicitly*. The abstract's standalone "95% reduction" claim is materially misleading as written and affects the central efficiency narrative.

- **Cross-dataset comparisons are confounded by token count.** In Tables 8, 9, and 10, all VQ-Transplant variants use **512 tokens**, while all baselines (RQVAE, VQGAN, VQGAN-LC, VQGAN-EMA, VQGAN-FC, VQ-WAE, MQVAE) are listed with **256 tokens**. Doubling the token count mechanically increases representational capacity and reduces r-FID independently of the framework. The headline result of 1.21 r-FID on FFHQ vs. 3.81 for VQGAN-LC is claimed as state-of-the-art in Section 5.3, but no token-matched baseline exists to disentangle the framework's contribution from the larger token budget. Even on ImageNet (Table 2), RQVAE at 512 tokens achieves 2.69 r-FID vs. 1.83 at 1024—showing token count matters substantially. The "state-of-the-art" claim across all three cross-domain benchmarks is thus unsupported as written.

### Minor

- **MMD-VQ's empirical advantage over Wasserstein VQ is marginal and inconsistent, and the non-Gaussianity motivation is undemonstrated.** In Table 3 (K=4096 post-adaptation), MMD VAR gets 0.91 vs. Wasserstein's 0.93 (Δ=0.02). In Table 8 (FFHQ, K=32768), Wasserstein VQ outperforms MMD VQ post-adaptation (1.21 vs. 1.37 r-FID). The paper motivates MMD over Wasserstein by arguing that real visual feature distributions are non-Gaussian ("multi-modal, heavy-tailed, or otherwise non-Gaussian"), but no empirical evidence is provided that the actual distributions produced by the frozen VAR encoder deviate meaningfully from Gaussian in ways that affect quantization. The theoretical motivation remains conjectural.

- **LPIPS degrades for all adapted configurations relative to the original VAR.** Table 3 shows the original VAR tokenizer achieves LPIPS=0.100, while all adapted MMD VAR variants achieve 0.104–0.108 LPIPS (K=4096: 0.108; K=8192: 0.104). Table 2 confirms the same: the original VAR has LPIPS=0.100, whereas all transplant configurations have higher LPIPS (0.104–0.115). This is inconsistent with the "superior reconstruction fidelity" framing in the abstract and Section 5.1. The paper should clarify that the superiority claim is scoped to FID/IS metrics, not perceptual similarity.

### Trivial

None.

---

## Nice-to-Haves

- **Explicit amortization break-even analysis.** The most honest and compelling version of the efficiency argument would quantify: "if a researcher runs N VQ experiments, the total cost is (960 + N×44) GPU-hours via VQ-Transplant vs. N×960 from scratch; break-even occurs at N≥2." This reframes the contribution as one of *amortized efficiency* rather than an absolute cost reduction, which is a more defensible and interesting framing.

- **Token-matched cross-dataset baseline.** Including at least one token-matched comparison (e.g., VQGAN-LC retrained with 512 tokens on FFHQ) would allow attribution of performance gains between framework design and token count.

- **Empirical evidence for non-Gaussianity in VQ feature distributions.** Measuring kurtosis or fitting Gaussian models to frozen VAR encoder outputs would either ground or undercut the MMD-VQ motivation. Even a histogram of encoder feature distributions would strengthen the theoretical narrative.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"From-scratch comparison as a strawman" (Harsh Critic, Section on Table 6).** The critic argues that 5–7 epochs from scratch is an unfair comparison since "discrete tokenizers require hundreds of epochs." However, the paper's point is not that from-scratch training *could* work given enough time—it is that given a *comparable compute budget* (22–35 GPU-hours), VQ-Transplant produces far better results (0.81 vs. 1.26–1.40 r-FID). This is a valid and well-scoped comparison. Removed.

- **"Stage II is just standard VQGAN training" (Harsh Critic).** The paper explicitly attributes the decoder adaptation procedure to Tian et al. (2024). The novelty is not in the adaptation mechanism itself but in the insight that adapting only the decoder (5 epochs) after VQ substitution is sufficient to recover reconstruction quality—decoupling VQ development from full encoder-decoder training. The observation that the paper borrows a known technique is not a weakness. Removed.

- **"Generalization claim weakened by OpenImages pre-training on faces" (Harsh Critic).** The paper proactively addresses this in Section 5.3: "raising a critical question: *Can the framework generalize to datasets structurally distinct from both ImageNet-1k and OpenImages?*" The encoder is frozen, and the test evaluates whether a VQ module trained on ImageNet-1k works on out-of-domain face and church datasets. This is a legitimate generalization setting. Removed.

- **"LDM-16 compatibility suggests architectural specificity" (Harsh Critic).** The paper explicitly acknowledges the lower effectiveness on LDM-16 (Section 5.1) and discusses it in the appendix (stripped by parser). This is a known limitation, not an undisclosed gap. Removed per hard rule on appendix content.

- **Strength: "Strong cross-dataset generalization achieves state-of-the-art" (Strength Finder).** Retained only partially—the generalization is real, but the "state-of-the-art" claim is compromised by the token-count confound identified above. Demoted to a qualified supporting result rather than a core strength.

---

## Novel Insights

The paper's most conceptually interesting finding is that decoder adaptation (Stage II) can recover nearly all reconstruction quality from a quantizer-decoder mismatch in just 5 epochs—far less than full training—because the decoder's learned priors are structurally close to the new quantized space when that space is obtained via distribution-aligning VQ methods. This suggests that the decoder's sensitivity to its input distribution is "soft": small distributional shifts can be corrected with very little adversarial fine-tuning, but only when the shift itself (quantization error) is minimized first. This has implications for transfer of pre-trained tokenizers in general: the decoder may be the most portable component, and quantizer compatibility is the binding constraint.

---

## Suggestions

1. **Restructure the efficiency claim** in the abstract and Table 1 to explicitly account for the pre-trained VAR prerequisite; present the amortization argument (break-even at N VQ experiments) rather than a raw speed comparison.

2. **Add a token-controlled comparison** for the FFHQ, CelebA-HQ, and LSUN-Churches benchmarks—either by reporting VQGAN-LC at 512 tokens or explicitly noting that the 512-vs-256 token difference is a confound.

3. **Clarify the scope of "superior reconstruction fidelity"** to FID/IS metrics only, given that LPIPS degrades relative to the original VAR in all adapted configurations.

4. **Report kernel bandwidth sensitivity** for the multi-Gaussian kernel in MMD-VQ (σ values), even if briefly. MMD estimates are bandwidth-sensitive, and this is relevant for reproducibility and understanding the method.

---

## Score and Decision

**Originality**: The framework concept (VQ-transplantation with lightweight decoder adaptation) is novel and practically motivated. MMD-VQ is a modest extension over Wasserstein VQ. *3/5*

**Importance**: VQ development costs are genuinely prohibitive; this approach could materially lower barriers in the field. *4/5*

**Claims supported**: Core ImageNet results are solid. The efficiency and cross-dataset "state-of-the-art" claims require reframing. *3/5*

**Soundness**: Two-stage procedure is methodologically sound; comparison fairness issues in cross-dataset experiments. *3/5*

**Clarity**: Well-organized and readable; figures and tables are informative. *4/5*

**Community value**: High practical utility for researchers developing VQ methods without large compute budgets. *4/5*

The framework contribution is real and clearly demonstrated on ImageNet. The two major issues—efficiency framing and token-count confound in cross-dataset evaluation—are correctable by reframing rather than by new experiments. The paper's core result (competitive reconstruction quality with ~4% of full retraining cost, when amortized properly) is genuine.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>