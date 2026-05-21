Now I have enough calibration data. Let me draft the final review.

## Anchors Retrieved

**Round 1 (bracketing):**
- IqGVIU4rvM (2.50, Reject) — Dual-token VQ-VAE+diffusion; weak.
- TDzAqTqDHV (3.00, Reject) — Quantized codebooks for retrieval; out of domain.
- orG37FHN4b (3.00, Reject) — Data-free quantization; unrelated.
- 2HdZPEQUig (3.00, Reject) — Object-centric video learning; off-topic.
- nS2DBNydCC (4.75, Reject) — **Wasserstein VQ (Fang et al. 2025), the direct predecessor**: highly relevant.
- yGnsH3gQ6U (5.75, Accept) — Binary Spherical Quantization (BSQ): closer domain match.
- mb2ryuZ3wz (5.75, Accept) — "How many tokens is an image worth": tokenizer paper.
- HYyRwm367m (6.50, Accept) — Neural Language of Thought.
- GMwRl2e9Y1 (8.00, Accept) — Rotation Trick for VQ-VAE: high quality VQ work.
- CxXGvKRDnL (8.00, Accept) — Quantized diffusion compression.
- 2dnO3LLiJ1 (8.00, Accept) — ViT Registers; off-topic.
- gU58d5QeGv (8.00, Accept) — Würstchen; off-topic.

Round 1 bracket: between ~4.5 and ~6.0 (paper sits between Wasserstein VQ predecessor and BSQ/ImageFolder-tier accepted tokenizer papers).

**Round 2 (narrowing):**
- RVPZJpmyGU (4.60, Reject) — VQ for SMoE routing.
- sfTsvy05MX (4.75, Reject) — Lattice VQ-VAE.
- Pf85K2wtz8 (5.75, Accept) — MMD Gradient Flow generative model.
- 49Tn5mfTy5 (5.00, Reject) — Codebook of Encoders for UQ.
- QE1LFzXQPL (6.25, Accept) — ImageFolder, autoregressive folded tokens.
- zkMRmW3gcT (4.80, Reject) — LM design for image gen.
- jQP5o1VAVc (5.75, Reject) — Continuous-token AR scaling.

The current paper builds directly on the Wasserstein VQ (4.75) work, addresses its Gaussianity critique with MMD, and adds a genuinely practical framework. But it has overclaimed headline numbers, indistinguishable MMD-vs-Wasserstein empirics in most rows, and no downstream generation evaluation. Sits between Wasserstein VQ (4.75) and BSQ/ImageFolder (5.75–6.25). Closer to the former because the secondary contribution (MMD-VQ) is empirically weak vs. Wasserstein VQ at matched settings.

---

## Summary
The paper proposes **VQ-Transplant**, a framework that replaces a pre-trained tokenizer's VQ module with an arbitrary alternative while freezing the encoder/decoder, followed by 5 epochs of decoder-only adversarial fine-tuning, applied primarily to the VAR tokenizer. A secondary contribution, **MMD-VQ**, replaces Wasserstein VQ's Gaussian-based moment matching with kernel-MMD distribution alignment between encoder features and codebook entries. Experiments cover ImageNet-1k, FFHQ, CelebA-HQ, and LSUN-Churches reconstruction.

## Strengths
- **Concrete, useful framework idea.** Transplanting a VQ module into a frozen pre-trained tokenizer with 5 epochs of decoder adaptation is a practical recipe that lowers a real barrier for resource-constrained VQ research. The framework is conceptually simple and broadly applicable.
- **Decoder adaptation is empirically validated.** Table 3 cleanly shows that distribution-aligned VQ substitution alone underperforms the source tokenizer in r-FID (e.g., 1.52 → 0.92) despite lower quantization error, but 5 epochs of decoder adaptation recovers and slightly exceeds the original (0.91 vs 0.92 at K=4096). The mechanism — fix the encoder priors, retrain only the decoder — is well-isolated.
- **Cross-dataset reconstruction is strong.** Tables 8–10 show that the transplanted tokenizer achieves r-FID of 1.21 on FFHQ (vs. 3.81 for VQGAN-LC) and competitive numbers on CelebA-HQ and LSUN-Churches, suggesting the framework generalizes beyond ImageNet-1k.
- **Continued adaptation shows monotonic gains.** Table 5 / Figure 3 show stable improvement of r-FID from 5 → 20 adaptation epochs (0.91 → 0.79 at K=4096; 0.81 → 0.74 at K=8192), evidence that the adaptation stage is well-behaved.

## Weaknesses

### Fatal
None — the contribution is real and the experimental story is coherent at matched budget.

### Major
- **The "21.8× faster than VAR" / "95% cost reduction" framing conflates amortized and absolute cost.** Table 1 contrasts 22 hours on 2×A100 with VAR's 60h × 16×A100, but VQ-Transplant *requires* VAR's pre-trained encoder/decoder checkpoints — the 21.8× number measures incremental cost given those weights, not training cost reduction. The abstract, intro, and Section 5 use the bigger number as the headline. The conclusion is defensible if reframed as "cheap iteration on a pre-trained tokenizer," but as written it overstates the contribution.
- **The "MMD VAR beats VAR" claim depends on a doubled codebook, not the method.** Table 2/3 headline 0.81 r-FID vs VAR's 0.92 is achieved at K=8192, double VAR's K=4096. At matched K=4096, MMD VAR is 0.91 and VAR is 0.92 — statistically indistinguishable with no variance reported. The honest matched-budget claim is "substitution is approximately lossless," which is still a useful result but materially weaker than what the abstract advertises.
- **MMD-VQ is not empirically differentiated from Wasserstein VQ.** Across Tables 3, 7, 8, 9, 10, MMD-VQ and Wasserstein VQ differ by 0.01–0.06 r-FID with no variance reported; on Churches Wasserstein VQ wins, on FFHQ Wasserstein VQ wins at K=32768 adaptation, on CelebA-HQ MMD wins. The motivation (MMD removes the Gaussianity assumption that limits Wasserstein VQ) is theoretically reasonable but never measured: there is no demonstration that VAR encoder features are non-Gaussian, no empirical MMD or moment statistics tracking distribution alignment quality, and no controlled setting where the Gaussianity assumption visibly fails. The "secondary contribution" status is overclaimed.
- **No downstream generation results.** The paper is motivated by "visual generation" and "democratizing quantization research," yet only reconstruction is measured. A transplanted VQ produces tokens with different statistics/indices than VAR's AR generator was trained against, so whether the substituted tokens are usable for generation without re-training the AR head is an open and important question. At minimum, gFID from a small AR model on transplanted tokens would establish usability — the absence is a real evidential gap for a framework sold as enabling VQ research for generation.
- **Table 2 fixed-scale comparison is not matched-budget.** MMD VQ is reported at 512 tokens against most baselines at 256 tokens (e.g., VQGAN-LC, Llama GEN, RQVAE). A 256-token / 16384-codebook row directly matched to Llama GEN would clarify whether the algorithm itself or the larger token budget drives the win.

### Minor
- **Decoder adaptation still uses heavy adversarial machinery.** Section 1/2 motivates the work by criticizing adversarial training as "computationally intensive" and "unstable," but Stage II uses a DINO-S discriminator, DiffAug, consistency regularization, LeCAM, and perceptual + GAN loss for 5 epochs. The savings are real (5 vs hundreds of epochs, decoder-only), but the writing would be more accurate as "shorter adversarial fine-tuning" rather than as avoidance of adversarial training.
- **Cross-dataset baselines train from scratch on smaller data; VQ-Transplant inherits an OpenImages-pretrained encoder.** The state-of-the-art framing in Section 5.3 partly reflects a transfer-learning advantage rather than VQ method/framework superiority. A baseline that fine-tunes VAR's native VQ on FFHQ/CelebA-HQ/Churches with the same 5-epoch decoder adaptation would isolate the contribution of changing the VQ method from the contribution of inheriting a stronger backbone.
- **No variance/seed reporting on tables where the "wins" are 0.01–0.05 r-FID.** Given that MMD vs Wasserstein and MMD-VAR vs VAR margins live in this range, the bolded rankings are not interpretable without error bars or repeated seeds.
- **LDM-16 compatibility is mentioned in one sentence as worse and deferred to appendix.** For a "plug-and-play with arbitrary tokenizers" pitch, the fact that the framework's adaptability is weaker on a different pretrained tokenizer deserves a direct discussion in the main text rather than a one-line deferral.
- **From-scratch comparison in Table 6 is not the right control.** Comparing 22h transplant to 25/30/35h from-scratch training only shows that you cannot train MMD VAR from scratch in 35h — which the paper itself agrees with. The right control is "fine-tune VAR's full pipeline for 22h with VAR's native VQ," to isolate the VQ-change contribution from the pretrained-backbone contribution.

### Trivial
None substantive.

## Nice-to-Haves
- Directly measure empirical MMD between encoder features and learned codebooks during training across methods, and plot it against final r-FID to substantiate the "distribution alignment is the mechanism" claim.
- Add at least one downstream generation experiment (fit VAR's AR head on transplanted tokens; report gFID).
- Foreground the matched-budget Table 3 row (K=4096) where MMD VAR ties VAR at 0.91 vs 0.92 as the central result; this is a more defensible and more interesting story ("substitution is nearly lossless for free") than "we beat VAR."
- Report seeds / variance on the small-margin tables.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *(harsh critic) "Argument that Wasserstein VQ collapses to first/second-moment matching under non-Gaussian features is asserted rather than demonstrated."* — This is a fair theoretical observation but the paper does cite Fang et al. 2025 for the motivation and frames it as a reasonable theoretical extension. Demoted into the broader "no empirical isolation of the MMD mechanism" major weakness rather than kept as a separate point.
- *(harsh critic) "$\mathcal{L}_{\text{unique}}$ is left abstract in Eq. 3."* — The paper instantiates this loss in Section 4.2 (MMD) and points to Wasserstein VQ for that variant; this is presentational, not a substantive gap.
- *(strength finder) "Reconstruction fidelity matching or exceeding the original tokenizer (0.81 vs 0.92)."* — Removed because at matched codebook size the gap is 0.01 and indistinguishable; keeping this as a strength conflicts with the verified major weakness. The honest version ("substitution is approximately lossless at matched budget") is captured elsewhere.
- *(strength finder) "Dramatic reduction in training cost (21.8× speedup, 95% reduction)."* — Removed as a strength because the headline number conflates amortized and absolute cost; the verified weakness wins per the merger rules.

## Novel Insights
None beyond the paper's own contributions. The most genuinely novel observation — that decoder adaptation alone is sufficient to recover most of the r-FID gap after VQ swap — is the paper's own contribution and is clearly demonstrated.

## Suggestions
- Reframe the headline cost reduction explicitly as "incremental cost given a pre-trained tokenizer," and report total cost (pretraining + transplant) for honesty.
- Make Table 3 K=4096 Adaptation row the central result and state plainly that matched-budget substitution is approximately lossless. Reserve the K=8192 result as a "spending the freed budget" follow-up.
- Add a generation experiment: take an off-the-shelf AR head (VAR's, if possible) and report gFID with the original vs the transplanted tokenizer. This addresses the single biggest evidential gap and would significantly strengthen the practical case.
- Show empirical MMD/divergence between encoder features and codebook for each VQ variant during training, and correlate with final r-FID to substantiate the MMD-VQ mechanism.
- Add seeds / variance on the small-margin comparisons (MMD vs Wasserstein; transplant vs source tokenizer).
- Promote the LDM-16 result and its limitations into the main text rather than the appendix.

## Evaluation on Standard Axes
- **Originality:** Moderate. VQ-Transplant is a simple, sensible engineering recipe that has not been emphasized as a research direction. MMD-VQ is an incremental extension of Wasserstein VQ.
- **Importance:** Moderate-to-high. Lowering the cost of VQ iteration is genuinely useful for the community.
- **Claim support:** Mixed. The framework claim (substitution + brief adaptation works) is well supported. The "21.8× faster than VAR" and "outperforms VAR" framings overclaim what the matched-budget tables show; MMD-VQ's distinct value over Wasserstein VQ is not empirically isolated.
- **Soundness:** Reasonable for reconstruction; insufficient for the claimed mechanism (no MMD/distribution alignment measurement) and for downstream usability (no generation results).
- **Clarity:** Good overall; figures and tables are organized clearly. Framing in abstract and intro is too aggressive.
- **Value to community:** Useful framework worth disseminating once the cost narrative is honestly framed.

## Calibration Reasoning
- **Round 1 bracket:** 4.5–6.0. Below Würstchen/Rotation-Trick-tier work (8.0). Above clearly-weak rejects (2.5–3.0). Near the Wasserstein-VQ predecessor (4.75) and accepted tokenizer papers like BSQ (5.75) and ImageFolder (6.25).
- **Round 2 narrowing:** The paper has a real practical contribution that the predecessor lacked (the framework idea), and stronger cross-dataset coverage. But the headline numbers are demonstrably overclaimed at matched budget, and the secondary MMD-VQ contribution is empirically indistinguishable from Wasserstein VQ. Compared to BSQ (5.75) the experiments are narrower (reconstruction only, no generation) and the central differentiator is less crisp. Compared to ImageFolder (6.25) the paper does not reach the same level of generation-quality demonstration. Compared to Wasserstein VQ (4.75) the framework adds practical value but the empirical separation between MMD and Wasserstein VQ does not improve on the predecessor's marginal-gain critique.
- **Final placement:** Slightly above Wasserstein VQ predecessor due to the genuinely useful framework idea and broader dataset coverage; below BSQ/ImageFolder due to overclaimed headlines, missing generation evaluation, and unclear MMD-VQ value-add. Lands around 5.0 — borderline, leaning reject in its current framing, recoverable to a clear accept with the suggested revisions.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>