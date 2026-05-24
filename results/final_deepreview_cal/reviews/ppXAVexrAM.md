I have now thoroughly read the paper, cross-checked all reviewer claims, and calibrated against human-reviewed anchors. Here is the consolidated review.

---

## Summary

ARSS introduces the first decoder-only autoregressive (AR) transformer framework for novel view synthesis from a single image conditioned on a camera trajectory. The method combines three components: a causal video tokenizer for temporal consistency, a camera autoencoder that compresses Plücker raymaps into 3D positional guidance tokens, and a spatially shuffled (but temporally ordered) token permutation strategy that lets the causal transformer exploit bidirectional image context within each frame. Experiments on RealEstate10K, ACID, and zero-shot DL3DV show the AR approach is competitive with SOTA diffusion-based NVS methods.

## Strengths

- **Novel AR formulation for scene-level NVS**: This is the first work to adapt a causal, decoder-only GPT-style transformer to novel view synthesis with explicit camera trajectory control. The integration of camera tokens as interleaved positional instructions within the AR sequence is a clean design that opens a new direction beyond diffusion-based NVS.

- **Well-validated spatial-only token permutation**: The proposed hybrid ordering—shuffling spatial tokens within each frame while preserving temporal order across frames—is clearly motivated (uni-directional attention vs. bi-directional images) and rigorously ablated. Table 2 shows it improves PSNR by +2.93 dB over raster-scan ordering, and Figure 7 provides compelling qualitative evidence that both "raster" and "full perm." alternatives degrade in distinct and interpretable ways.

- **Video tokenizer ablation is convincing**: Replacing a per-frame VQ image tokenizer with a causal video tokenizer yields a 62% FVD reduction (52.56 vs. 137.68, Table 3), directly quantifying the importance of temporal modeling in the tokenization stage.

- **Solid quantitative and generalization results**: The method achieves the best PSNR (19.02 on Re10K, 21.93 on ACID) and lowest LPIPS among all compared methods. Zero-shot results on DL3DV (Table 1) and on out-of-distribution AI-generated images (Figure 5) demonstrate genuine generalization beyond the training distribution.

- **Per-frame quality analysis**: Figure 6 shows that ARSS maintains the highest per-frame PSNR/SSIM and lowest LPIPS across a 17-frame trajectory with a visibly flatter degradation slope than all baselines.

## Weaknesses

### Major

- **The core motivation is not empirically demonstrated**: The introduction motivates AR by arguing that diffusion models cannot easily "impose a strictly causal structure" or "incrementally extend and reuse existing generations when the trajectory changes" (line 17). The abstract echoes this framing. Yet all experiments generate fixed-length 17-frame trajectories in a single pass—exactly the static-condition setting where joint-generation diffusion methods are known to work well. There is no experiment showing that ARSS can (a) generate beyond the training trajectory length, (b) condition on previously generated views to extend a trajectory, or (c) update partial trajectories without full recomputation. The per-frame analysis (Figure 6) shows quality degrades more slowly, which is evidence of good long-horizon behavior, but not of the incremental-extension capability that is the paper's stated *raison d'être* for an AR approach. Without such evidence, the paper demonstrates that AR *can* do NVS, not that it offers distinct advantages over diffusion.

### Minor

- **Camera autoencoder is under-ablated**: Section 3.2.2 describes the camera autoencoder architecture only in general terms (stacked 3D convolutional encoder-decoder with geometric losses in Eq. 5). No comparison is provided against a simpler baseline such as feeding normalized Plücker coordinates directly through an MLP, or using them as raw positional encodings without learned compression. The architecture dimensions, compression factors, pre-training data, and whether the autoencoder is frozen during AR training (line 100 says "pre-train" but no details follow) are unspecified, making the contribution opaque.

- **Overstated performance claims**: The introduction (line 114) and discussion (line 490) claim the method "out-performs current state-of-the-art methods," while the abstract more accurately says "comparable to state-of-the-art." The data in Table 1 support the latter: ARSS leads on PSNR and LPIPS, but SEVA achieves better SSIM (0.670 vs. 0.624 on Re10K; 0.664 vs. 0.623 on ACID) and substantially better FID on ACID (33.16 vs. 47.76, a 44% gap). These are not catastrophic failures—LPIPS and PSNR are arguably more important—but the claim of unambiguous out-performance is not supported by the full metric picture.

- **Figure 6 framing**: The figure is labeled "Error accumulation analysis." For non-AR baselines (LVSM, MotionCtrl, ViewCrafter), per-frame degradation is primarily due to increasing viewpoint distance from the input, not autoregressive error propagation. The analysis remains useful as a per-frame quality comparison, but the "accumulation" framing conflates geometric difficulty with the AR-specific error propagation the paper is motivated by.

### Trivial

- None beyond minor presentation issues already captured above.

## Nice-to-Haves

- An ablation replacing the learned camera autoencoder with raw Plücker coordinates (or an MLP encoding without reconstruction loss) would illuminate whether the autoencoder is necessary or merely convenient.
- Reporting decoding speed and analyzing the parallel decoding capability mentioned in Section 3.2.3 would strengthen the practical value proposition.
- Statistical significance or multi-seed variance for the main results table.

## Removed Points

These points from the input reviews were considered but removed:

- *"Omission of Zero-1-to-3, MVDream as baselines"* — These are object-centric NVS methods designed for single-object 3D generation (Objaverse-scale). The paper targets scene-level NVS (RealEstate10K, ACID) with long camera trajectories. The baseline set (SEVA, LVSM, Genwarp, MotionCtrl, ViewCrafter, RayZer) is appropriate for the scene-level setting and scope.

- *"Statistical significance should be reported"* — Single-run evaluation on large-scale benchmarks is standard practice in the scene-level NVS literature (e.g., LVSM, SEVA). Moved to Nice-to-Haves.

- *"Tokenization ablation should compare against other video-capable tokenizers"* — The binary comparison (VQ image vs. video tokenizer) cleanly isolates the contribution of temporal modeling in tokenization. Comparing against alternative video tokenizers would add engineering value but is not essential for validating the core claim.

- *"The camera autoencoder should provide full architectural description, training data, pre-training details"* — Partially merged into the Minor weakness about under-ablation. The core concern is lack of justification and comparison, not missing implementation trivia.

- *"Parallel decoding claim is not validated"* — Moved to Nice-to-Haves. This is a forward-looking statement, not a core claim.

- *Strengths about "addressing an important problem" or "interesting question"* — Removed as generic; the kept strengths are grounded in specific evidence from the paper.

## Novel Insights

Beyond the paper's own contributions, a notable insight emerging from the review is that the spatial-only permutation strategy represents an elegant resolution of a fundamental tension in applying causal transformers to visual data: it preserves the temporal autoregressive structure (views farther from the source are always predicted after closer ones) while allowing the model to exploit full bidirectional spatial context within each frame. The ablation (Table 2, Figure 7) shows that both extremes—full spatiotemporal permutation and rigid raster ordering—fail for different, interpretable reasons (incorrect geometry vs. long-range distortion). This design principle may generalize to other tasks requiring causally ordered generation of spatially structured data.

## Suggestions

1. **Add an incremental generation experiment**: Generate views 1–8, then condition on those to generate views 9–16 using extended camera poses. Compare consistency against a diffusion baseline that must regenerate the full trajectory. This would directly validate the paper's core motivation.

2. **Add a camera encoding ablation**: Compare the full camera autoencoder against (a) raw Plücker coordinates passed through a small MLP and (b) direct Plücker encoding without compression. Report PSNR/LPIPS for each variant.

3. **Align claims with evidence**: Either soften the "out-performs" language to match the abstract's "comparable to" phrasing, or add the experiments that would justify the stronger claim.

## Score and Decision

**Round 1 bracket**: Compared the paper against three score bands. Weak anchors (2.33–3.40) were clearly below this paper. Middle anchors included AR-1-to-3 (5.00, AR-based object NVS, synthetic-only eval) and GST (6.25, AR for joint pose+view prediction). Strong anchors included LVSM (7.67, transformer NVS, directly compared in this paper). Initial bracket: ~5.5–7.5.

**Round 2 narrowing**: Compared against anchors in (4.5–6.5) and (6.0–8.0). ARSS is clearly stronger than AR-1-to-3 (5.00, Reject) which evaluated only on synthetic objects with limited baselines. It is comparable to GST (6.25, Accept) in novelty and experimental thoroughness, and somewhat stronger in evaluation breadth. It is below LVSM (7.67, Accept), whose contribution was cleaner (minimal 3D bias, directly validated) and whose central claim was fully supported by experiments; ARSS's strongest motivating claim (AR enables incremental extension) remains unvalidated. It is also below LARP (7.50, Accept), a more focused contribution with tighter validation.

**Final assessment**: The paper makes a genuine contribution—first AR paradigm for scene-level NVS, with well-executed technical components and solid empirical results. The disconnect between its strongest motivating claim and its experimental validation is a real limitation that prevents it from reaching the top tier, but this is addressable and does not invalidate the contribution. Score: 6.5.

**Anchor summary**:

| Anchor | Score | Round | Comparison |
|---|---|---|---|
| MI0UiWeqOl (PAR modeling) | 2.33 | 1 | Different domain; ARSS substantially stronger |
| I86z54CL2y (GeoGS3D) | 3.40 | 1 | 3D reconstruction; ARSS superior in evaluation |
| hWlCc7Iksi (ARVideo) | 3.40 | 1 | AR video pretraining; ARSS stronger contribution |
| 15lk4nBXYb (CCM-DiT) | 3.00 | 1 | Camera control for DiT; ARSS more novel |
| pOcGFvfgjS (AR-1-to-3) | 5.00 | 1,2 | Closest AR paradigm; ARSS has better eval breadth and real-scene results |
| dTGH9vUVdf (FreeVS) | 5.80 | 2 | Different domain (driving); ARSS more comprehensive |
| zDJf7fvdid (Zero-shot NVS) | 6.00 | 2 | Diffusion-based zero-shot NVS; ARSS has training + stronger results |
| NuHYh4YKNe (GST) | 6.25 | 1,2 | Most similar AR contribution; ARSS comparable novelty, slightly better evaluation |
| wkbx7BRAsM (AR video imitators) | 7.00 | 2 | AR for video; different task |
| Wr3UuEx72f (LARP) | 7.50 | 2 | Tokenizer design; cleaner contribution, better validated |
| QQBPWtvtcn (LVSM) | 7.67 | 1,2 | Directly compared; LVSM's claims fully validated, ARSS's strongest claim is not |
| P4o9akekdf (NoPoSplat) | 8.00 | 1 | Stronger contribution, more thoroughly validated |
| QQ6RgKYiQq (MovingParts) | 8.00 | 1 | Different domain; stronger paper |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>