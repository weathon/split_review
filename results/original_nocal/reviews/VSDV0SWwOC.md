Now I have all the evidence needed. Let me compose the final consolidated review.

---

## Summary

LS-Merge proposes a framework for merging LLMs by encoding their weights into a learned latent space via a Transformer VAE with structured layer-aware chunking, performing merging operations (interpolation, barycenters) in that space, and decoding back to weights. The method supports self-merging (single-model augmentation), homogeneous expert merging, and — via Optimal Transport alignment — heterogeneous cross-architecture merging between models of different sizes and families. Experiments on Gemma, LLaMA, and LoRA experts show that latent-space merging outperforms weight-space baselines and competes with activation-based methods.

## Strengths

- **Latent-space merging consistently outperforms weight-space baselines across diverse tasks.** Table 3 shows LS-Merge(soup) achieves 56.0 on MMLU and 60.1 on HellaSwag while the best weight-space method (SLERP) obtains 52.5 and 50.4 respectively, and Greedy Soup obtains 50.8 and 54.6. The gains are substantial (3–10 points) and consistent across benchmarks.

- **OT-based alignment enables heterogeneous cross-architecture merging with measurable gains.** Table 5 shows that OT alignment followed by interpolation improves over the base model on WinoGrande (57.75 vs. 56.83) and ARC-C (43.34 vs. 42.78), whereas OT-only or raw interpolation without alignment degrades performance. This demonstrates that distributional alignment is both necessary and effective for cross-architecture merging — a capability no prior weight-space method provides.

- **LS-Merge competes with activation-based methods without requiring activations.** Table 4 shows LS-Merge achieves 55.07 on MMLU and 36.41 on IFEval, outperforming Task Arithmetic (52.18, 25.10) and matching or exceeding AIM (54.18, 32.00). This is significant because activation-based methods (AIM, Task Arithmetic) require running the model to obtain activations, while LS-Merge operates purely on weights.

- **Ablation shows non-linear latent space is essential and that PCA collapses.** Table 8 compares PCA and VAE at compression ratios 1.6×, 2.0×, and 4.0×. PCA collapses to near-random MMLU (25.50 at r=1.6) while the VAE retains 39.89 (96% of base), and this gap persists across all ratios. This cleanly validates the paper's central claim that pretrained weights lie on a non-linear manifold.

- **VAE generalizes to unseen models at low compression.** Table 7 shows that a VAE trained on Gemma-3-4B-it, when applied to unseen Gemma-3-1B-it at r=1.6, loses less than 1% on MMLU (39.98 vs. 40.76) and comparably on LLaMA-3.2-1B-it (46.06 vs. 46.55), demonstrating transferable weight representations.

- **Weight distribution analysis motivates encoder design.** Table 1 reports kurtosis values up to 15.2 for Gemma-3-4b-it self-attention layers, confirming heavy tails. These non-Gaussian statistics justify the choice of a non-linear VAE over simpler Gaussian-assumption encoders.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Training data composition is vaguely described.** The paper states "pretrained weight snapshots for Gemma-3-1B-it and Gemma-3-4B-it, plus LoRA experts" (line 159) but does not specify how many distinct checkpoints or training snapshots are used. While the chunking mechanism (line 95) ensures that even a single checkpoint provides many thousands of chunk-level training examples, the lack of exact counts makes it difficult for others to reproduce or assess the diversity of the training distribution. This matters because the VAE's ability to learn a generalizable latent manifold depends meaningfully on the breadth of the training data.

- **No ablation of the two-stage training curriculum.** The paper introduces a two-stage curriculum (deterministic autoencoder first, then KL fine-tuning) to stabilize VAE training on heavy-tailed weights (line 107), but never ablates this design choice. It is unclear whether the two-stage procedure is critical, or whether training with the KL term from scratch would suffice. This is a straightforward ablation the authors should provide.

- **No statistical significance testing or confidence intervals.** Several tables (e.g., Table 2, Table 8) report standard deviations, but some values are suspiciously small (0.00 or 0.01), suggesting rounding artifacts or very few repetitions. No hypothesis tests, bootstrap intervals, or effect-size measures are provided. While many gains are large enough to be convincing (e.g., Table 3 differences of 3–10 points), the cross-architecture results in Table 5 (57.75 vs. 56.83, 43.34 vs. 42.78) are small enough that significance would strengthen the claims considerably.

- **Greedy Soup implementation in latent space is underspecified.** The paper states "Uniform and Greedy Soup correspond to different choices/updates of {λ_i}" (line 151), but greedy soup in weight space requires validation-set performance feedback. It is not explained how the greedy selection is performed in latent space without decoding every candidate. If decoding is required for selection, the efficiency claim is weakened. The paper should clarify this procedure.

- **OT alignment empirical covariance estimation details are missing.** The closed-form OT map (line 149) estimates per-layer Gaussian parameters from empirical mean and covariance of chunk-level latents. The paper does not state the latent dimension $d$ or the number of latent samples per layer, making it unclear whether covariance estimates are reliable. While the empirical results suggest the OT alignment works, the missing details make it harder to assess potential degeneracy, especially for small layers.

- **Self-merging mechanism is conceptually unclear.** Self-merging encodes a single model and merges multiple latent samples from its posterior (line 111). The paper claims this improves performance, but it is not immediately obvious why merging stochastic samples from one model's posterior should yield better weights rather than simply approximating the original model. The improvement over "VAE reconstruction from a single latent sample" (Table 2) could indicate that the posterior sampling is beneficial, but the mechanism is not analyzed.

### Trivial

- Table 2 reports LS-Merge standard deviations of 0.00 on MMLU and HellaSwag for Gemma-3-4B-it. This appears to be a rounding artifact and should be reported with meaningful precision or justified.

- The two-stage curriculum description (line 107) refers to "Appendix 5" but the appendix is not accessible in the submission.

## Nice-to-Haves

- An ablation comparing the two-stage curriculum against end-to-end VAE training would strengthen the methodological justification.
- Visualizing the latent space structure (e.g., t-SNE of chunk-level latent codes) would help verify that the VAE has learned a meaningful manifold rather than memorizing the training instances.
- A breakdown of VAE reconstruction quality per layer type (early vs. late layers, attention vs. MLP) at different compression ratios could clarify the degradation patterns in Table 7.

## Removed Points

These points were raised by reviewers but are not included as weaknesses in the main review, for the following reasons:

- **"VAE training data is insufficient"** — Factually incorrect. The paper uses structured layer-aware chunking (line 95), which yields many thousands of training examples from a single model checkpoint (each weight matrix in each layer is partitioned into non-overlapping chunks). Additionally, the paper trains on weights from multiple models. The reviewer's assumption of "at most a handful of training examples" misunderstands the preprocessing pipeline.

- **"OT alignment covariance is rank-deficient"** — Speculative without knowledge of the latent dimension and per-layer chunk count. The paper reports successful empirical results (Table 5, Figure 3) using an existing OT library. The concern is about underspecification (which is kept as a minor weakness), not a proven degeneracy.

- **"PCA baseline is unfair because it is unsupervised while VAE uses training data"** — The comparison in Table 8 is deliberately designed to test linear vs. non-linear manifold structure. PCA is the canonical linear baseline for this question; its failure despite the low-rank structure of individual weight matrices is what validates the paper's claim. The asymmetry is the point.

- **"Section 3.1 analysis is well-known (LoRA)"** — The paper uses PCA to motivate the VAE design, not as a novel contribution. The analysis is appropriately scoped as motivation.

- **"Section 3.1 manifold embedding argument is misapplied"** — The paper makes an explicit assumption ("Assuming the collection of flattened weights W ⊂ ℝ^D concentrates near a smooth d-dimensional manifold") and uses it to justify the existence of a compressive encoder. This is a reasonable theoretical motivation, not a formal proof.

- **"Cross-architecture generalization to only one unseen model"** — The paper demonstrates zero-shot transfer to two unseen models (Gemma-3-1B-it and LLaMA-3.2-1B-it, Table 7) and also evaluates merging across architectures (Section 4.4). The scope is sufficient for the claims made.

## Novel Insights

The reviews surface an important distinction that the paper could address more explicitly: the VAE is trained on *chunk-level* weight fragments, not on full-model weight vectors. This means the effective training set size is much larger than the number of model checkpoints — a point the paper could make more clearly to preempt the concern. Conversely, this also means that the VAE learns local (per-chunk) structure rather than global model-level structure, and the OT alignment operates on per-layer distributions of chunks. The interplay between these two levels of analysis (chunk-level encoding, layer-level alignment, model-level merging) is a noteworthy feature of the framework that the reviews collectively highlight without fully resolving.

## Suggestions

- Specify the exact number of training checkpoints and the chunk size $c$ used, to clarify the effective training set size.
- Report bootstrap confidence intervals or paired tests for the main benchmark comparisons, especially for Table 5 where gains are small.
- Ablate the two-stage curriculum by training the VAE with KL from the start and comparing performance.
- Clarify how greedy soup selection is implemented in latent space — specifically whether it requires decoding candidate weight vectors for validation evaluation.
- Report the per-layer latent dimension $d$ and typical number of chunks per layer to substantiate the OT covariance estimates.

## Score and Decision
MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>