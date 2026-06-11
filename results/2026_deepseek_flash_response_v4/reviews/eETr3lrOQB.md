Now I have all the information needed to write the final consolidated review. Let me compile everything.

## Summary

This paper proposes VQ-Transplant, a framework for plug-and-play replacement of VQ modules in pre-trained visual tokenizers without full end-to-end retraining. The framework operates in two stages: (1) substituting the VQ module while freezing the encoder and decoder, followed by (2) lightweight decoder adaptation (5 epochs on ImageNet-1k) to resolve distributional mismatch. The paper also introduces MMD-VQ, which uses Maximum Mean Discrepancy for distributional alignment between feature and codebook vectors. Experiments on ImageNet-1k and cross-dataset evaluations (FFHQ, CelebA-HQ, LSUN-Churches) show competitive or superior reconstruction fidelity with substantially reduced compute relative to training from scratch.

## Strengths

1. **Practical, well-motivated framework.** VQ-Transplant addresses a genuine resource bottleneck in VQ research. The paper's core insight — that one can swap VQ modules into a frozen pre-trained encoder-decoder and then adapt only the decoder — is sensible and well-articulated. The two-stage design (Tables 3, 7) cleanly isolates the contribution of each stage: Stage I reduces quantization error but initially hurts reconstruction, and Stage II converts that lower quantization error into improved r-FID. This step-by-step diagnosis is a clear methodological strength.

2. **Cross-dataset generalization is convincingly demonstrated.** The paper evaluates on FFHQ, CelebA-HQ, and LSUN-Churches (Tables 8–10), which are structurally distinct from the pre-training data (OpenImages) and the adaptation data (ImageNet-1k). Wasserstein VQ and MMD VQ achieve competitive r-FID scores (e.g., 1.21 on FFHQ), showing the transplant approach is not overfit to ImageNet-1k. The paper explicitly acknowledges the potential concern about ImageNet-1k being a subset of OpenImages (line 277) and uses these cross-dataset experiments to address it.

3. **Controlled from-scratch comparison quantifies the pre-training benefit.** Table 6 directly compares VQ-Transplant (22 hours) with training the same MMD VAR architecture from scratch for 5–7 epochs (25–35 hours). The transplant variant achieves substantially better r-FID (0.91 vs 1.40 at K=4,096; 0.81 vs 1.26 at K=8,192), demonstrating the value of leveraging pre-trained initialization.

## Weaknesses

### Fatal
None.

### Major

1. **Headline efficiency claims are built on an uncontrolled comparison.** The paper claims "95% training cost reduction" and "21.8× faster" by comparing VQ-Transplant (ImageNet-1k, 2×A100, 22 hours, decoder-only fine-tuning) against the original VAR training (OpenImages, 16×A100, 60 hours, full end-to-end training). These differ on three confounded axes simultaneously: dataset (ImageNet-1k vs OpenImages), GPU count (2 vs 16), and training paradigm (fine-tuning vs from-scratch full training). The 21.8× figure is the product of all three differences, not a controlled speed comparison of the proposed method vs an alternative on equal footing. The framing as a "speedup" is misleading. A clean comparison would hold dataset and GPU count fixed and vary only the training approach.

2. **The best MMD VAR result (0.81 r-FID) uses a larger codebook than the baseline.** The paper's headline reconstruction improvement (0.81 r-FID for MMD VAR vs 0.92 for original VAR) uses K=8,192 for MMD VAR while the original VAR uses K=4,096. At the same codebook size (K=4,096) and same token count (680), MMD VAR achieves 0.91 vs 0.92 r-FID — a marginal 1% relative improvement that could be within noise (no confidence intervals are reported). The claimed benefit therefore conflates the effect of a larger codebook with the effect of the VQ method and transplant framework.

3. **Missing critical control: fine-tuning the full pre-trained model (encoder, decoder, and VQ jointly) on ImageNet-1k for the same budget.** The paper compares VQ-Transplant against training from scratch (Table 6), which is expected to be much worse. But it does not compare against the simplest alternative: take the full pre-trained VAR, replace its VQ module, and fine-tune *all* parameters (encoder, decoder, VQ) on ImageNet-1k for the same 22 hours. If this full fine-tuning baseline matches or exceeds VQ-Transplant's results, then the claimed benefits of the two-stage frozen-encoder design are not demonstrated. This is the single most important missing experiment for validating the framework's design.

### Minor

1. **MMD-VQ shows only marginal and inconsistent improvements over Wasserstein VQ.** Across Tables 3 and 7, the differences between MMD-VQ and Wasserstein VQ are generally small (often <0.02 r-FID), and MMD sometimes underperforms Wasserstein (e.g., Table 7, K=16,384: MMD 1.05 vs Wasserstein 1.04 r-FID; Table 8 adaptation at K=16,384: MMD 1.99 vs Wasserstein 1.81 r-FID; Table 10: MMD 1.87 vs Wasserstein 1.79 r-FID). The paper's secondary contribution (MMD-VQ) therefore adds little beyond the prior work (Fang et al., 2025) it extends.

2. **No uncertainty quantification.** No confidence intervals, standard deviations, or significance tests are reported anywhere. Given the small margins between methods (e.g., 0.91 vs 0.92 r-FID), it is impossible to assess whether observed differences are meaningful.

3. **Table 1's "Speedup" column is not explicitly defined.** The column header reads only "Speedup" with no formula. It is inferable (GPU-hours relative to VQ-Transplant's 44 GPU-hours) but should be stated explicitly.

4. **The hyperparameter γ in the VQ loss (Equation 3) is not ablated.** The loss balance between L2 quantization error and the uniqueness-enforcing loss (e.g., MMD) could affect performance, but no sensitivity analysis is provided.

### Trivial
- Table 2 compares MMD VQ (512 tokens) against baselines that mostly use 256 tokens. While this favors the proposed method and is therefore not a fairness concern against the authors, the comparison should be noted.

## Nice-to-Haves
- Adding the full-model fine-tuning baseline (encoder + decoder + VQ jointly from pre-trained initialization).
- Controlling for codebook size when reporting headline improvements (i.e., compare at K=4,096).
- Reporting results with standard deviations or confidence intervals.
- Ablating the hyperparameter γ.
- An explicit definition of "Speedup" in Table 1.

## Removed Points

These points from the harsh critic were removed because they do not survive verification against the paper:

- **"Decoder adaptation undercuts the lightweight framing because it uses GAN + perceptual losses."** The paper is transparent about the adaptation losses and the compute budget (22 hours on 2 GPUs). This is genuinely lightweight compared to 60 hours on 16 GPUs. The criticism overstates the issue.

- **"The from-scratch comparison is not informative."** The comparison is informative: it shows that training the same architecture from scratch for similar or longer clock time yields substantially worse results. This is a valid baseline.

- **"Cross-dataset results are attributable to the pre-trained backbone, not the framework."** The paper acknowledges this and presents the cross-dataset experiments precisely to test whether the transplant approach works beyond the pre-training distribution. That VQ-Transplant achieves competitive results is still evidence for the framework.

- **"The paper conflates dataset size in the speedup comparison"** is already retained as a Major weakness above (point 1) but in a verified, specific form — the issue is the uncontrolled multi-axis comparison, not the dataset size per se.

- **"Speedup column is undefined"** was softened to a minor clarity issue since it is inferable from context.

- Claims about "missing appendix," "missing proofs," or "unreleased models" — these are parser artifacts or violations of the instruction not to question cited references' existence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the efficiency claims.** Provide a controlled comparison where dataset and GPU count are held fixed, and only the training approach varies (VQ-Transplant vs full fine-tuning vs from-scratch training on ImageNet-1k with 2 GPUs). Report both the controlled speedup and the total cost reduction as separate statements.

2. **Add the full fine-tuning baseline.** Fine-tune the pre-trained VAR (encoder, decoder, and a new VQ module jointly) on ImageNet-1k for the same 22-hour budget. If VQ-Transplant matches or outperforms this baseline, that is direct evidence for the two-stage design. If not, the contribution reduces to "you can swap VQ modules with minor adaptation."

3. **Control for codebook size when making headline claims.** Report MMD VAR at K=4,096 (same as the original VAR) alongside the K=8,192 result, with explicit acknowledgment that the larger codebook contributes to the improvement.

4. **Present MMD-VQ more modestly.** The improvement over Wasserstein VQ is small and inconsistent. Frame it as a variant that relaxes the Gaussian assumption, and provide an analysis of when the non-Gaussian alignment matters (i.e., where Wasserstein VQ empirically degrades relative to MMD-VQ).

5. **Add variance estimates** (e.g., multiple seeds) for at least the key comparisons to establish whether the reported differences are statistically meaningful.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing (all query results):**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| IqGVIU4rvM.md (VQ-VAE+Diffusion Tokenizers) | 2.50 | R1 | Much weaker: narrower evaluation, unclear contribution |
| TDzAqTqDHV.md (Quantised Codebooks for Retrieval) | 3.00 | R1 | Much weaker: different domain, limited scope |
| bEvI30Hb2W.md (LVM-NET) | 3.00 | R1 | Much weaker: different task, minor contribution |
| 6Mdvq0bPyG.md (EfficientQAT) | 3.00 | R1 | Much weaker: different domain (LLMs) |
| rwdeKOdAwY.md (RetFormer) | 3.00 | R1 | Much weaker: different task |
| sfTsvy05MX.md (LL-VQ-VAE) | 4.75 | R1 | Weaker: tested only on small datasets (FFHQ-1024), questionable loss formulation, no downstream evaluation |
| WNLAkjUm19.md (Discrete Tokenization Theory) | 7.00 | R1 | Stronger: principled theoretical contribution with rigorous analysis |
| yGnsH3gQ6U.md (BSQ-ViT) | 5.75 | R1 | Stronger: cleaner controlled evaluation, scalable to video, more novel quantization method |
| HYyRwm367m.md (Neural LoT) | 6.50 | R1 | Different scope: representation learning rather than tokenizer efficiency |
| FlvtjAB0gl.md (Unified Lang-Vision) | 6.25 | R1 | Different scope: vision-language pretraining |
| GMwRl2e9Y1.md (Rotation Trick VQ) | 8.00 | R1 | Much stronger: principled gradient propagation through VQ |
| 2dnO3LLiJ1.md (ViT Registers) | 8.00 | R1 | Different topic |
| CxXGvKRDnL.md (Progressive Compression) | 8.00 | R1 | Different topic |
| 84n3UwkH7b.md (Diffusion Memorization) | 8.00 | R1 | Different topic |
| SI2hI0frk6.md (Transfusion) | 7.60 | R1 | Different topic (multimodal model) |

**Round 2 — Narrowing:**

| Path | Avg Score | Round | Comparison to this paper |
|------|-----------|-------|------------------------|
| ZVe2k7mNAP.md (MQ-VAE) | 4.50 | R2 | Weaker: tested only on small datasets, compute-inefficient method |
| sfTsvy05MX.md (LL-VQ-VAE) | 4.75 | R2 | Weaker: limited evaluation, questionable loss |
| zkMRmW3gcT.md (Elucidating Design Space) | 4.80 | R2 | Different topic (AR image gen design space) |
| nS2DBNydCC.md (Wasserstein VQ) | 4.75 | R2 | Weaker: narrower scope, the current paper's VQ-Transplant framework is a clear addition and the evaluation is more thorough |
| yGnsH3gQ6U.md (BSQ-ViT) | 5.75 | R2 | Stronger: cleaner controlled comparisons, more novel quantization, comprehensive evaluation |
| FlvtjAB0gl.md (Unified Lang-Vision) | 6.25 | R2 | Different scope |
| 6VhDQP7WGX.md (Inference Optimal VLMs) | 5.80 | R2 | Different topic |
| n64NYyc6rQ.md (Semantic Equiv Tokenization) | 6.20 | R2 | Different topic |

**Round 1 bracket:** 4.0–6.5.

**Round 2 narrowing:** The paper is clearly stronger than MQ-VAE (4.50), LL-VQ-VAE (4.75), and the Wasserstein VQ paper (4.75) — the VQ-Transplant framework adds a practical dimension, the evaluation is more thorough, and the cross-dataset generalization is a strength. However, it is weaker than BSQ-ViT (5.75), which has cleaner controlled comparisons and a more novel quantization method. The current paper's evaluation issues (uncontrolled comparisons for headline claims, missing full fine-tuning baseline, codebook size confound) place it below BSQ-ViT. This positions the paper at approximately 5.0.

The paper has a practical and well-motivated framework, and the experimental evidence broadly supports that VQ-Transplant works. However, the central claims are overstated relative to the evidence as presented. The authors should reframe the efficiency claims, add the critical full-fine-tuning control, and control for codebook size. With these revisions, the paper could make a solid contribution.

**Final Score:** 5.0 — Borderline; the core idea is sound but the evaluation has significant uncontrolled comparisons that overstate the contribution. Major revisions are needed before acceptance.

**Decision:** Reject

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>