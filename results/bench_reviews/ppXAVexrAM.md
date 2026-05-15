Now I have a thorough understanding of both the paper and the calibration landscape. Let me synthesize the final review.

---

## Summary
ARSS proposes the first framework that applies a GPT-style causal decoder-only autoregressive transformer to single-image novel view synthesis with explicit camera trajectory control. It combines three components: a causal video tokenizer (VidTok) for temporally consistent discrete tokens, a dedicated camera autoencoder that compresses Plücker raymaps into 3D positional guidance tokens, and a hybrid token permutation strategy that randomly shuffles spatial tokens within each frame while preserving temporal order across frames. The method is trained on RealEstate10K and ACID, evaluated zero-shot on DL3DV, and shows competitive results against the diffusion-based SEVA baseline, with notably slower error accumulation over long trajectories.

## Strengths
- **First decoder-only autoregressive transformer for NVS with camera control.** This is a genuinely novel combination. Prior AR visual generation work (LlamaGen, VAR, etc.) addresses only single-image generation; ARSS extends the paradigm to multi-view sequences with explicit 3D camera conditioning, which is a non-trivial conceptual step.

- **Well-ablated hybrid token permutation strategy.** The paper demonstrates that spatial-only permutation (while preserving temporal order) yields +2.93 dB PSNR over raster order and +0.46 dB over full permutation (Table 2), with qualitative differences visible in Figure 7. The reasoning — that spatial context is bidirectional while temporal context must remain causal — is clearly articulated and empirically validated.

- **Convincing ablation on video tokenizer vs. per-frame VQ tokenization.** Table 3 shows that replacing VQ image tokenization with the causal video tokenizer reduces FVD from 137.68 to 52.56 (−62%) and improves PSNR by +3.53 dB, directly validating the claim that temporal tokenization is critical for multi-view consistency.

- **Slower error accumulation over long trajectories.** Figure 6 provides per-frame PSNR/SSIM/LPIPS curves showing ARSS maintains higher quality and degrades more gradually than all compared baselines. This is a direct and well-motivated consequence of the causal autoregressive design, and it is the paper's most distinctive empirical contribution.

- **Competitive results against SEVA**, which is a strong diffusion-based multi-view NVS method. On RealEstate10K, ARSS achieves better PSNR (19.02 vs. 18.73) and LPIPS (0.269 vs. 0.349), though worse SSIM (0.624 vs 0.670) and FID (47.60 vs 46.98). On ACID the pattern is similar. This supports the claim of overall comparability to a genuine SOTA diffusion approach.

## Weaknesses

### Major
- **No dedicated ablation of the camera autoencoder.** The camera autoencoder is presented as a core contribution — it encodes Plücker raymaps into latent tokens that serve as 3D positional guidance. However, there is no experiment that isolates its contribution: e.g., training a variant that uses a simpler positional encoding (learned per-frame embeddings, Fourier features, or raw Plücker coordinates) without the autoencoder. This makes it impossible to determine whether the autoencoder's geometry-constrained latent space actually improves generation quality, or whether any camera signal would suffice. Given that the camera autoencoder is one of three claimed technical contributions, this is a significant gap.

### Minor
- **Baseline set could be broader, and some baselines are weak matches for the task.** MotionCtrl is primarily a video camera-motion control method, not designed for single-image NVS. Genwarp is a warp-and-inpaint approach that depends heavily on depth estimation quality. ViewCrafter and RayZer underperform heavily on these benchmarks. LVSM is a feed-forward method known to produce blurry results. Only SEVA is a strong, directly comparable diffusion-based NVS method. While the SEVA comparison does support the "comparable to SOTA" claim, a broader set of strong single-image NVS baselines would substantially strengthen the paper's empirical case. The claim of being "comparable to state-of-the-art view synthesis approaches based on diffusion models" (plural) is only partially supported by one strong diffusion comparison.

- **The acknowledged tokenizer limitation is stated but not analyzed.** The paper notes (Section 5) that the video tokenizer "is hard to adapt to significant view changes thus would lead to the generation of inferior discrete tokens." Since NVS inherently involves view changes, this is an important limitation, but the paper provides no quantification: what constitutes a "significant" view change? At what camera displacement does tokenizer quality degrade? Are there visual examples? Without this analysis, the practical scope of the method's applicability remains unclear.

- **FID/FVD computation methodology is under-specified.** It is unclear whether these distributional metrics are computed at the dataset level or per-scene, how the reference distribution of real images/videos is constructed, and whether all methods' outputs are aligned to the same number of frames and resolution. This matters because FID/FVD are sensitive to these choices.

- **Error accumulation analysis (Figure 6) lacks methodological detail.** The paper does not specify how per-frame alignment between generated and reference frames is performed across different methods that may produce outputs at different frame rates or with different trajectory sampling. Without a clear alignment protocol, the per-frame curves are not strictly comparable.

- **The parallel decoding claim (Section 3.2.3) is asserted but never evaluated.** The paper states that random spatial token permutation "allows parallel decoding" and that "the system has the capacity to predict multiple tokens at one time," but no experiment measures decoding speedup, token-level parallelism, or trade-offs between parallel and sequential sampling.

### Trivial
- The camera autoencoder's reconstruction accuracy is not reported (e.g., PSNR of reconstructed Plücker raymaps), making it hard to assess whether the latent camera tokens faithfully encode 3D geometry.

## Nice-to-Haves
- A cross-dataset generalization experiment (e.g., training on RealEstate10K, testing on ACID, or vice versa) would strengthen the claim of learning general 3D reasoning rather than dataset-specific patterns.
- Quantitative evaluation of novel-view geometric consistency (e.g., pose accuracy of recovered cameras, reprojection error) beyond photometric metrics.
- Scaling behavior analysis: how does performance change with model size, tokenizer compression ratio, or trajectory length?

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"Numerous contemporary diffusion-based NVS methods that consistently outperform these baselines (e.g., Zero-1-to-3++, Cat3D, SynShot, MV-Adapter, etc.) are absent."** — Per instructions, I do not name or rely on uncited methods whose existence and applicability I cannot verify. The point about baseline breadth is preserved in weakened form above, without naming specific uncited works.

- **"The contrast with diffusion models is drawn too sharply: many diffusion-based NVS methods can be rolled out autoregressively."** — This is a critique of the motivation framing rather than a substantive weakness of the method. The paper's claim about causal structure being "less straightforward" in diffusion is a reasonable qualitative observation, not a factual error.

- **"The token order permutation is largely a reprise of known strategies."** — The paper explicitly cites Pang et al. and Yu et al. and acknowledges the lineage. The contribution is the adaptation to the multi-view temporal setting, which is novel and well-ablated.

- **"The video tokenizer is taken off-the-shelf; no analysis of reconstruction quality."** — Using off-the-shelf components is standard practice. The paper does ablate tokenizer choice (VQ vs. video tokenizer, Table 3), which is the relevant experimental question. Reconstruction quality reporting is preserved as a trivial suggestion.

## Novel Insights
The error accumulation analysis (Figure 6) reveals a genuinely interesting property: causal autoregressive generation along a camera trajectory produces not just competitive per-frame quality but a qualitatively different degradation profile — slower, more graceful quality loss — compared to methods that generate all views jointly. This insight connects the architectural choice (causal vs. joint) to a measurable behavioral property (error accumulation rate) and could motivate future work on autoregressive world models beyond NVS. The paper would benefit from a deeper investigation of *why* this happens (is it because the model conditions on its own previously generated tokens, creating a self-correcting feedback loop? Or is it simply that joint methods distribute errors more uniformly?).

## Suggestions
- Add a camera autoencoder ablation: train a variant that replaces the learned camera tokens with a simpler encoding (e.g., sinusoidal embeddings of the 6-DoF pose, or raw downsampled Plücker maps without autoencoder reconstruction) and report the performance gap.
- Specify the FID/FVD computation protocol (dataset-level vs. scene-level, reference distribution construction, frame count alignment).
- Clarify the frame-alignment methodology for Figure 6.
- Provide at least one qualitative failure case where the tokenizer breaks under large viewpoint change, to give the reader intuition about the practical limits.

## Score and Decision

**Anchor comparison:**

- `/home/wg25r/review_agent/human_reviews_2026/pIyADlhQsp.md` (CausNVS, avg 3.50, Reject): Also an autoregressive NVS paper. CausNVS had weaker novelty (integration of known diffusion components into causal masking), weaker results (comparable or inferior to SEVA), and no clear ablation story. ARSS is substantially stronger on all three dimensions.

- `/home/wg25r/review_agent/human_reviews_2026/O66RinTZTR.md` (avg 3.50, Withdrawn): Diffusion-based NVS with warping-and-conditioning. Weaker results and narrower contribution than ARSS.

- `/home/wg25r/review_agent/human_reviews_2026/fIPng6j4eM.md` (Kaleido, avg 4.50, Accept Poster): A larger-scale effort with video pretraining, but reviewers flagged limited viewpoint changes, flat geometry, and missing comparisons. ARSS has a cleaner, better-ablated contribution despite smaller scale.

- `/home/wg25r/review_agent/human_reviews_2026/PZQHihJlfm.md` (ArchonView, avg 5.00, Reject): Closest comparator — also the first AR model for NVS (object-centric). ArchonView had more benchmarks and thorough conditioning ablations but was limited to single object views. ARSS tackles the harder scene-level setting with camera trajectories and has a unique error accumulation analysis. Overall comparable quality; ARSS is slightly more ambitious in scope.

- `/home/wg25r/review_agent/human_reviews_2026/vjvwYexMQn.md` (avg 5.00, Accept Poster): Diffusion-based aligned NVS with cross-modal attention. Different approach but similar level of contribution quality — solid method with some missing baselines and ablations.

- `/home/wg25r/review_agent/human_reviews_2026/NnSiKYA1Jk.md` (Pensieve, avg 5.50, Reject): Strong results but rejected due to evaluation concerns (test-time optimization gave unfair advantage). ARSS is cleaner methodologically.

- `/home/wg25r/review_agent/human_reviews_2026/NQq9JLMfNN.md` (3WM, avg 6.00, Accept Poster): A unified 3D scene understanding framework. Broader scope and more thorough experiments than ARSS.

- `/home/wg25r/review_agent/human_reviews_2026/kI27Niy4xY.md` (VIST3A, avg 8.00, Accept Oral): Text-to-3D through model stitching. Significantly stronger paper — more thorough experiments, multiple model pairings, clear SOTA, broad applicability.

- `/home/wg25r/review_agent/human_reviews_2026/DTQIjngDta.md` (π³, avg 8.00, Accept Poster): Strong theoretical contribution with extensive validation. Well above ARSS.

- `/home/wg25r/review_agent/human_reviews_2026/DM0Y0oL33T.md` (avg 8.00, Accept Oral): Different domain entirely.

**Assessment:** ARSS sits between the rejected 5.0–5.5 papers and the accepted 6.0 paper. It has genuine novelty (first decoder-only AR for NVS), strong ablations on token permutation and tokenizer choice, and a distinctive empirical finding (error accumulation). The main weaknesses — missing camera autoencoder ablation, somewhat narrow baseline set, and underspecified methodology on a few points — are addressable and do not undermine the core contribution. The paper makes a real contribution to an interesting direction.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>