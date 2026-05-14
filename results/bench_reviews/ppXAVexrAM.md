## Summary
ARSS proposes the first decoder-only autoregressive (GPT-style) framework for single-image novel view synthesis with camera control. It combines an off-the-shelf video tokenizer (VidTok), a LlamaGen backbone, a spatial-only token permutation strategy (preserving temporal causality), and a Plücker-raymap camera autoencoder that produces per-token 3D positional instruction tokens. Results on RealEstate10K, ACID, and zero-shot DL3DV are reported as comparable to SOTA diffusion methods at smaller training scale.

## Strengths
- The spatial-only permutation ablation (Table 2 / Fig. 7) is informative: it cleanly separates the three regimes (raster fails at later frames; full permutation breaks temporal causality; spatial-only is best), with a +2.93 dB gain over raster.
- The tokenizer ablation (Table 3) provides a large, concrete signal (FVD 137.68 → 52.56) justifying the move from VQ image tokenization to a causal video tokenizer.
- The architectural composition — interleaving per-token camera tokens with visual tokens as a positional-instruction substitute for LlamaGen's class prefill — is a sensible adaptation of recent AR-image-generation techniques to view synthesis.
- The geometry-constrained Plücker autoencoder (unit-length and direction/moment orthogonality terms, Eq. 5) is a principled formulation for what a camera latent must preserve.

## Weaknesses

### Fatal
None.

### Major
- **Headline "outperforms SOTA" claim is contradicted by the authors' own Table 1.** The intro and §4.2 say ARSS "out-performs current state-of-the-art." But on RealEstate10K, SEVA beats ARSS on SSIM (0.670 vs. 0.624) and FID (46.98 vs. 47.60); on ACID, SEVA again beats ARSS on SSIM (0.664 vs. 0.623) and FID (33.16 vs. 47.76). ARSS wins by small margins on PSNR/LPIPS/FVD. The DL3DV column — where ARSS does lead — omits SEVA, ViewCrafter, and RayZer by the authors' own admission. The abstract's "comparable to" framing is accurate; the §1/§4 framing is not. This is a substantive overclaim, not a wording nit.
- **The AR-over-diffusion motivation is never tested.** The intro repeatedly justifies AR by appealing to "incrementally extending and reusing existing generations when the trajectory changes" and scaling to "long trajectories." No experiment in the paper does this. All evaluation uses the 17-frame training window. The "error accumulation analysis" (Fig. 6) extends only to frame index 16 — the end of the training horizon — so it cannot demonstrate long-horizon behavior beyond what diffusion baselines also saw during training. The paper's central reason for choosing AR is therefore unsupported.
- **The one genuinely novel module (camera autoencoder) is not ablated.** Components (a)–(c) — video tokenizer, LlamaGen backbone, spatial permutation with positional instruction tokens — are explicitly adopted from prior work (Tang et al. 2024; Sun et al. 2024; Pang et al. 2025; Yu et al. 2024a). The camera autoencoder is the only new piece, and the paper does not compare it to simpler alternatives (raw Plücker maps with a linear projection, learned pose embeddings, removal of the geometry losses). Combined with the previous point, this leaves the paper's quantitative claim resting on a module whose contribution is not isolated.

### Minor
- **Baseline configuration disclosure.** Training is at 256×256 / 17 frames on 8 H100s for 100K iterations; SEVA/ViewCrafter are designed for higher resolution and longer horizons. The paper does not state how baselines were re-configured or whether outputs were resized. RayZer's PSNR of 12.97/12.64 is conspicuously low and may reflect a misconfiguration. This makes "comparable to SOTA" harder to adjudicate. §4.2 partially acknowledges SEVA's scale advantage but does not document the matched-eval setup.
- **No inference-cost or latency comparison.** AR's well-known cost is sampling time; readers cannot assess the trade-off vs. parallel diffusion baselines without wall-clock / FLOPs / parameter-count numbers.
- **No pose-fidelity diagnostic for the camera autoencoder.** A simple "pose recovery error after autoencoding" would establish whether the bottleneck is lossless enough.
- **Permutation gap is small with no variance reported.** PSNR 18.76 → 19.22 (full perm. → ours) is informative but small; single-seed numbers leave run-to-run variance unaddressed. Similarly, SEVA vs. ARSS on Re10K PSNR (18.73 vs. 19.02) is within plausible seed variance.

### Trivial
- Eq. 7's loss expression appears to omit the target sequence in the CE second argument; Eq. 8's nested permutation index notation is hard to parse. (Some of this may be parser-induced, but the description of how camera tokens are visible to each visual-token target prediction could be clarified independently.)
- §3.2.2 introduces "m" as a "momentum term" via o×d but the surrounding text uses "d" in places where "m" appears intended; a one-line cleanup of the notation would help.

## Nice-to-Haves
- A real long-horizon experiment: extend the trajectory to ≥2× training length, or splice in a new trajectory mid-sequence with frozen prior generations, to operationalize the AR-vs-diffusion claim.
- A failure-mode case study under large viewpoint changes (the discussion admits the tokenizer struggles there).
- Report results at each baseline's native resolution alongside the matched-resolution numbers.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *"DL3DV omits SEVA/ViewCrafter/RayZer due to training-data overlap"* — the authors disclose this in Table 1's caption; it's standard practice. The legitimate criticism (that the in-domain Re10K/ACID numbers do not support "outperforms") is retained under Major.
- *Strength: "Slow error accumulation over long trajectories" (Fig. 6)* — moved out of strengths because Fig. 6 only runs to the training horizon (frame 16), so it does not actually demonstrate long-horizon behavior, conflicting with a verified Major weakness.
- *Strength: "First decoder-only AR model for NVS with camera control"* — kept implicitly in the summary; not promoted as a strength because novelty-by-framing alone, without the AR-specific advantages being validated, is weak evidence.
- *Strength: "+1.1% PSNR / −21% LPIPS over SEVA on RealEstate10K"* — true on those metrics, but selective; SEVA wins on SSIM/FID. Reframed as "comparable, not superior."
- Generic strength: "addresses an important problem in world models" — superficial.

## Novel Insights
None beyond the paper's own contributions. The most useful empirical observation in the paper — that spatial-only permutation strictly beats raster and full permutation for AR view sequences — is already articulated by the authors; reviewers do not add insight beyond that.

## Suggestions
- Reconcile §1/§4.2/§5 wording with Table 1. Either retract "outperforms" in favor of "comparable at much smaller training scale," or add experiments at matched scale that justify the stronger claim.
- Add a trajectory-extension experiment (frames beyond training length, or mid-generation trajectory change with reused prior tokens). This is the experiment that would actually motivate choosing AR over diffusion.
- Add a camera-conditioning ablation: raw Plücker → linear projection, learned pose embedding, and removal of the geometry losses in Eq. 5. Without this the camera autoencoder's contribution is not isolated.
- Report inference latency / FLOPs / parameter counts vs. SEVA and LVSM.
- Document baseline reconfiguration for the 256×256 / 17-frame evaluation grid, and report at-native-resolution numbers when feasible.

## Evaluation along requested axes
- **Originality:** Modest. The decoder-only AR framing for NVS is new in this combination, but the architectural building blocks (VidTok, LlamaGen, spatial permutation with positional instruction tokens) are all imported; the genuinely new module (camera autoencoder) is not ablated.
- **Importance of the question:** Reasonable. AR view synthesis is a sensible direction for world models, but the paper does not demonstrate the properties (long-horizon, incremental extension) that would make AR specifically valuable here.
- **Support for claims:** Weak. The "outperforms SOTA" claim is not supported by Table 1, and the long-horizon/causal claim is not tested at all.
- **Soundness of experiments:** Mixed. Permutation and tokenizer ablations are informative; the camera-autoencoder and long-horizon evaluations that the contribution most needs are absent.
- **Clarity:** Acceptable. The architectural figures and ablations are readable; Eqs. 5–8 could be tightened.
- **Value to community:** Modest. A clean composition baseline for AR-NVS, but without isolating the novel module or demonstrating AR's purported advantages, the contribution is mostly an existence proof.

## Score and Decision

Anchor comparison:
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pOcGFvfgjS.md` (AR-1-to-3, avg 5.00, Reject) — closest analogue: AR scheme for multi-view from single image. ARSS has similar overclaiming risk and weaker baseline novelty (no diffusion-prior backbone), but more careful tokenization choices. Sits around or slightly below this anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zDJf7fvdid.md` (Zero-shot NVS via adaptive modulating video diffusion, avg 6.00, Accept) — better-supported method with theoretical grounding; ARSS is weaker.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/VLuJL8cnGk.md` (3D-free meets 3D priors NVS, avg 5.00, Reject) — comparable: single-image NVS with mixed evidence; similar tier.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rWIrdAo2xC.md` (Generalizable Monocular 3D Human Rendering, avg 5.20, Reject) — divisive but landed at borderline reject; ARSS has clearer empirical contradiction with its own claims and sits a bit lower.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KI1zldOFz9.md` (Training-free camera control, avg 5.80, Accept) — well-scoped and supported; ARSS is below.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/0n4bS0R5MM.md` (VD3D, avg 6.20, Accept) — stronger camera-control evidence; ARSS below.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Z4evOUYrk7.md` (CameraCtrl, avg 6.50, Accept) — more careful empirical study; ARSS below.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AcAD4VEgCX.md` (I2VControl-Camera, avg 6.50, Accept) — stronger; ARSS below.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CFOQd4tqn1.md` (Ctrl123, avg 4.00, Reject) — closed-loop NVS with limited convincing evidence; ARSS is roughly between Ctrl123 and AR-1-to-3.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/j3rxIH0M9H.md` (MOVIS, avg 4.50, Reject) — comparable tier.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/U862lgKUgj.md` (Bootstrap3D, avg 3.75, Reject) — weaker than ARSS overall.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/QQBPWtvtcn.md` (LVSM, avg 7.67, Accept) — clearly stronger; ARSS well below.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2prShxdLkX.md` (MoDGS, avg 6.75, Accept) — stronger; ARSS below.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lnVPfgRnIV.md`, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/D1w3huGGpu.md`, `/home/wg25r/split_review/datasets/deepreview_13k_calibration/j5EbZEyK9I.md` — off-topic anchors, not directly comparable.

ARSS sits closest to the AR-1-to-3 / Ctrl123 / MOVIS cluster (avg 4.0–5.0, all Rejects): a clean but incremental composition whose headline claim is not borne out by its own table, and whose motivation for the design choice is not tested. It is clearly below the accepted 6.0+ anchors.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>