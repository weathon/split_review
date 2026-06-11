## Summary
Spherical Watermark embeds bits into the diffusion latent prior via binary embedding with random padding, projection onto the unit sphere, orthogonal rotation, and chi-distributed radial scaling. The authors prove the resulting noise forms a spherical 3-design (matching the standard normal up to degree-3 moments) and report strong empirical undetectability, ~30,000× faster extraction than PRC, and improved robustness to WEvade attacks on SD v1.5/v2.1.

## Strengths
- Clean theoretical chain (Thm 3.1, 3.2, Lemmas 3.3–3.4) tracing the distribution through each transformation and connecting spherical t-design theory to lossless watermarking.
- FID parity with the unwatermarked baseline (46.81 vs 46.81) plus near-chance MLP latent-level and ResNet-18 image-level classifier accuracy (Fig 2, Table 1).
- Large extraction-speed gain over PRC (~10⁻³·⁵ s vs ~10¹ s, Fig 4) by replacing belief-propagation decoding with matrix inversion + majority vote.
- Strong robustness under WEvade (Table 2: 98.12% ACC vs ≤52.31% for lossy methods) and superior capacity scaling under JPEG-70 vs PRC (Fig 6a).
- Hypothesis-driven ablations of the binary embedding and spherical mapping modules (Figs 6b–6c).

## Weaknesses

### Fatal
None.

### Major
- **Mismatch between Eq. 2 and what is actually proved.** Eq. 2 states computational indistinguishability (a cryptographic notion), but Thm 3.2 / Lemmas 3.3–3.4 only establish a spherical 3-design and Gaussian convergence of marginals — i.e., agreement up to degree-3 moments. The joint distribution of z_w is supported on rays through a finite ±1/√l_x lattice scaled by a chi variable, which is statistically distinguishable from N(0,I) in principle. The paper's own Section 5 acknowledges "higher-order moments may deviate from the true prior," but the abstract and Section 3.3 still advertise indistinguishability without that caveat. The contribution should be framed as moment-matching plus empirical classifier-indistinguishability, not the cryptographic property Eq. 2 defines.
- **"Encryption-free" is a weakening of the security model, not a pure efficiency gain.** The key K=(T,C) is a single fixed secret reused across all users/images, with linear structure (T over F_2, orthogonal C over R). Per-image keys in Gaussian Shading and pseudorandom codes in PRC exist precisely to prevent an attacker from inferring structure from observed (m, z_w) pairs. The paper does not specify a threat model nor analyze any chosen-message/chosen-latent adversary, yet markets the loss of per-image keying as a strict improvement. The paper itself notes "with fixed keys, Gaussian Shading no longer achieves true losslessness," yet the proposed scheme is fundamentally fixed-key — an internal tension.
- **Headline undetectability comparison handicaps Gaussian Shading.** Section 4.1 explicitly runs Gaussian Shading with five fixed keys across 100 users — a configuration the paper acknowledges breaks Gaussian Shading's losslessness. The Fig. 2 gap then reflects this configuration as much as a method advantage. A matched comparison (per-image-keyed Gaussian Shading vs. fixed-key Spherical) is necessary to support the headline undetectability claim.

### Minor
- **Adversaries in Fig. 2 are blind to K.** The MLP/ResNet have no access to (T,C). The claim should be qualified — an adversary with C could project z_w and observe the ±1/√l_x lattice trivially. This is a reasonable practical threat model but should not be presented as confirmation of Eq. 2.
- **Effective dimension of C is l_c = ⌊√l_x⌋ = 128, not l_x.** How C is tiled across the 16384-dim latent (block-diagonal/per-channel?) is unstated, and the marginal-Gaussian convergence in Lemma 3.3 should be re-stated at l_c = 128, since this is the dimension that controls convergence.
- **Tight parameter regime for 3-wise independence.** Thm 3.1 requires l_r ≥ N·s; defaults l_r = 512, N = 31, s = 1 leave little slack. Behavior as s or N approaches the boundary deserves discussion.
- **WEvade ordering may depend on the surrogate detector.** A sensitivity check on the surrogate would strengthen the Table 2 claim vs PRC.

### Trivial
None retained.

## Nice-to-Haves
- Direct statistical tests on z_w (KS, MMD, higher-moment tests) to probe the 3-design vs. true Gaussian gap directly rather than only via learned classifiers.
- Explicit threat model with adversary capabilities (black-box, chosen-message, partial-key knowledge) and an informal recovery-of-C analysis given q known (m, z_w) pairs.
- Matched per-image-keyed Gaussian Shading comparison.

## Removed Points
These points are flagged to be removed; treat them with caution.
- "Authors must demonstrate explicit attacker recovery of C from few (m, z_w) pairs": kept at Major as a framing concern, but the specific "small number of pairs suffices" claim from the harsh critic is speculation without a concrete analysis. The retained version asks for a threat model, not a guaranteed attack.
- Strength Finder's "rigorous cryptographic guarantee" framing — conflicts with the verified Eq. 2 gap and is dropped.
- Generic Strength Finder claims about importance of the watermarking problem.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
- Reframe the contribution as moment-matched lossless watermarking + empirical classifier-indistinguishability; either prove Eq. 2 or drop its cryptographic phrasing.
- Add a threat model and adversary analysis for the fixed (T,C) scheme.
- Add a matched-condition Gaussian Shading comparison (per-image keyed vs. fixed-key Spherical).
- Clarify the block structure of C and revise Lemma 3.3 at l_c = 128.
- Add KS / MMD statistical tests on z_w.

## Calibration

Anchors retrieved:
- **Round 1**:
  - fkNsgI1nye (3.00, private inference for diffusion) — much weaker than this paper.
  - vK8C37eHXM (3.20), W4djmqKZC6 (3.00), dAavOuxZvo (3.00) — off-topic diffusion papers, all weaker.
  - T0ebbDO60R SuperMark (3.75) — watermarking, weaker; rejected.
  - HexshmBu0P "Recipe for Watermarking DMs" (5.33) — comparable scope; rejected.
  - jlhBFm7T2J "An undetectable watermark for generative image models" (6.50, accept) — PRC paper, with a genuine cryptographic undetectability proof that this paper falls short of.
  - ETFfXGM3e4 SAT-LDM (5.50) — provably generalizable latent diffusion watermarking; rejected.
  - CxXGvKRDnL (8.00), j7b4mm7Ec9 (7.60), 84n3UwkH7b (8.00), I5lcjmFmlc (8.00) — strong band, all stronger and more impactful than this paper.
  - Round 1 bracket: ~**4.5–6.0**.
- **Round 2** (narrowing in 4.0–7.0):
  - zqo2eKjSWH "Stable Signature is Unstable" (4.50, reject) — narrower contribution than this paper.
  - ll2nz6qwRG "Hidden in the Noise" (5.83, accept) — distortion-free initial-noise watermarking, comparable in scope and stronger in honest framing.
  - 1IwoEFyErz "Shallow Diffuse" (6.00, reject) — similar caliber, rejected.

Compared to HexshmBu0P (5.33, reject) and SAT-LDM (5.50, reject), this paper has stronger empirical results (speed, robustness, FID parity) but is weakened by the verified framing/security/comparison concerns. It is below jlhBFm7T2J (6.5, accept) — the PRC paper — whose proof actually delivers what this paper claims. It sits closer to Hidden in the Noise (5.83) but loses on baseline fairness and theoretical overclaim. Settle near 5.0.

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>