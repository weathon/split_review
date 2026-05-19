Now let me do the calibration search — Round 1 bracketing.Let me read the most topically similar anchor paper to get a better comparison:Round 1 bracket: The paper likely sits in the **5.5–7.5** range. The dehazing adaptation paper scored 5.6; our paper is methodologically more novel (novel noise-space DA), has broader scope (3 tasks), and stronger ablations. Let me narrow.Let me read two key anchor papers within the narrowed bracket:Now I have enough to write the final review. Let me synthesize everything.

---

## Summary
This paper proposes **Denoising as Adaptation (DAA)**, a novel noise-space domain adaptation framework for image restoration. A diffusion model is jointly trained with a restoration network so that its denoising loss acts as a distribution-alignment signal, guiding restored outputs from both synthetic and real-world inputs toward a clean target distribution. Two anti-shortcut strategies — a channel-shuffling layer and a residual-swapping contrastive loss — prevent the diffusion model from trivially distinguishing the two input conditions. The diffusion model is discarded after training, leaving only the restored network for inference.

---

## Strengths

- **Genuinely novel adaptation space.** The paper is the first to perform domain adaptation in the diffusion noise space for image restoration, a conceptually distinct departure from both feature-space (DANN, DSN) and pixel-space (CyCADA, PixelDA) approaches. The diffusion loss in Eq. (1) provides a stable, compact signal without requiring a domain classifier or adversarial training.

- **Strong denoising performance.** Table 1 shows the method achieves 34.71 dB / 0.9202 SSIM on SIDD, outperforming the best prior DA method (CyCADA: 30.81 / 0.8067) by +3.90 dB and the vanilla synthetic baseline by +8.13 dB. This is a large margin on a well-established benchmark.

- **Thorough shortcut learning analysis and fixes.** Section 3.2 and Fig. 3 systematically identify a three-stage collapse mode during joint training and motivate channel shuffling (CS) and residual-swapping contrastive learning (RS) as principled solutions. The ablation in Table 4 verifies their individual and joint contributions: [1,1000] → 32.07 dB; +CS → 32.91; +RS → 34.71 dB.

- **Compelling scalability evidence.** Fig. 6 (PSNR vs. GMACs) shows that as vanilla networks grow larger they overfit synthetic data and degrade on SIDD, while the proposed method monotonically improves across all network sizes (U-Net-T through Uformer-B). This is the clearest mechanistic evidence that diffusion loss acts as a generalization regularizer.

- **No inference overhead.** The diffusion model is discarded after training; only the restoration network is used at test time, making the method practically advantageous over diffusion-based methods that require multi-step inference.

---

## Weaknesses

### Fatal
None.

### Major

- **Deblurring result is a near-null outcome, but the abstract and comparison section claim uniform effectiveness across three tasks.** Table 3 shows only +0.19 dB PSNR over the vanilla baseline on RealBlur-J, and the LPIPS metric is worse for "Ours" (0.1363) than for CyCADA (0.1340). The paper states "the proposed method leads the comparison methods on three image restoration tasks" (Section 4.1), which is misleading because: (a) the gain over vanilla is within noise on a single run, and (b) the best LPIPS is not achieved by the proposed method. The Limitation section does acknowledge that diffusion models are less sensitive to low-frequency blur artifacts, but that acknowledgment is not reflected in the scope claim in the abstract and comparisons section. The paper should either narrow the scope claim to high-frequency degradations or provide additional evidence that the method helps on deblurring.

### Minor

- **The "Only real" ablation (Table 4, row 8, 32.60 dB) is unexplained.** The diffusion objective in Eq. (1) uses $\tilde{y}^s = \sqrt{\bar{\alpha}_t} y^s + \sqrt{1-\bar{\alpha}_t}\epsilon$, which requires paired synthetic ground truth $y^s$. If only real data is used, this target is unavailable. The paper never explains what the training objective becomes in this configuration (does it use the COCO extension with $\tilde{y}^c$?). The value 32.60 dB is notably high for a no-paired-supervision setting, making the omission consequential: the ablation is meant to demonstrate that real data is necessary, but without specifying the mechanism, it is hard to interpret. The explanation (Section 4.2) simply says "excluding each of them would lead to dramatic degradation" without clarifying the setup.

- **Primary comparisons in Tables 1–3 are against methods not designed for image restoration.** The paper itself notes in the Related Work that "aligning high-level deep representations in feature space may overlook low-level variations essential for image restoration." Yet DANN, DSN, PixelDA, and CyCADA — all designed for high-level vision — are the primary comparators. The more informative comparison appears in Table 5 (C2N vs. Ours), where the proposed method (34.71 dB) underperforms C2N (35.35 dB) in its default configuration. The paper reasonably addresses this by noting it is not a specialist method, but this context belongs in the main comparison section, not the scalability section.

### Trivial

- The paper mentions "Peformance vs. Complexity" as a section heading (Section 4.4) — minor presentation issue.

---

## Nice-to-Haves

- **Quantitative results on unseen datasets (DND, Real-Internet).** Fig. 8 shows only qualitative results on DND and Real-Internet. Including PSNR/SSIM where reference images are available (DND has a benchmark server) would meaningfully strengthen the generalization claim.
- **Clarify whether the COCO extension is used by default or only in "Ours\*."** The relationship between "Ours" (34.71 dB), "Ours\*" (35.52 dB), and the COCO extension ($\tilde{y}^c$ replacement) is never made explicit. A one-line clarification in the experimental setup would resolve ambiguity about what the default method is.
- **Variance estimates for small margins.** Tables 2 and 3 show margins of +1.35 dB and +0.19 dB respectively. Since the method involves stochastic components, confidence intervals or repeat-run standard deviations would help readers assess the reliability of these margins.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **"Vanilla baseline for denoising appears poorly calibrated" (Harsh Critic).** The vanilla U-Net is trained on AWGN and tested on SIDD (real sensor noise). Achieving 26.58 dB in this cross-domain setting is entirely plausible — the claim that "standard DnCNN-trained models achieve higher values" is unverified and depends on external data not available in the review. This criticism depends on knowledge the reviewer cannot confirm and could be factually wrong. **Removed.**

2. **"Fig. 1a motivating experiment is nearly definitional" (Harsh Critic).** While the observation that cleaner conditions → lower diffusion error is intuitive, the key point — that a restoration network's outputs can receive gradient signals through this mechanism — is non-trivial and the experiments validate it. The motivational experiment is standard practice in such papers. **Removed (scope creep).**

3. **"Channel shuffling cannot prevent content-similarity shortcuts" (Harsh Critic).** The paper explicitly addresses this via the COCO extension (Section 3.2), which replaces $\tilde{y}^s$ with $\tilde{y}^c$ from an unpaired clean corpus. The criticism implies this extension is "optional," but the paper offers it as a solution. The criticism ignores a directly addressed concern. **Removed (paper addresses it).**

4. **Asking for C2N / AINDNet comparisons in the main table (Harsh Critic).** These are named external references that may or may not exist; per hard rules, missing related work comparisons cannot be verified. The paper includes relevant self-supervised comparisons (Ne2Ne, MaskedD, NLCL). **Removed.**

5. **Denoising gains are "carried by a possibly under-tuned vanilla baseline" (Harsh Critic).** This is speculative — the paper provides no evidence of under-tuning, and the reviewer cannot confirm that the baseline is misconfigured based on the paper alone. **Removed (speculative).**

---

## Novel Insights

The most underappreciated insight in the paper is the scalability result (Fig. 6): vanilla networks exhibit inverse scaling on real-world data (larger → more overfitting), while the proposed method reverses this trend, achieving consistent real-world improvements as model capacity grows. This observation — that diffusion-based distribution matching acts as a scale-friendly regularizer — is a non-obvious, practically important finding that deserves more prominence. The shortcut learning analysis (three-stage collapse, Fig. 3) is also a genuine contribution that could inform other joint-training frameworks beyond image restoration.

---

## Suggestions

1. Rewrite the abstract and comparison-section claim "demonstrates the effectiveness of the proposed method" to acknowledge the asymmetric results: strong on high-frequency degradation tasks (denoising, deraining), marginal on low-frequency (deblurring).
2. Add a paragraph to Section 4.2 explaining the "Only real" configuration — specifically, what serves as the diffusion target when no paired synthetic ground truth is available.
3. Move the C2N comparison (currently in the scalability section) to a position within or directly adjacent to Table 1, with a clear statement that the proposed method is intentionally general-purpose and that task-specialized methods achieve higher PSNR.
4. Elevate the scalability/generalization regularization observation (Fig. 6) to the Introduction or Abstract as a key empirical finding.

---

## Evaluation on Key Axes

- **Originality:** High. Noise-space DA via diffusion loss is genuinely new; channel-shuffling and residual-swapping contrastive loss are creative solutions to a specific training pathology.
- **Importance:** Moderate-high. Synthetic-to-real domain gap is a real problem in image restoration; a task-agnostic, inference-free solution is practically valuable.
- **Claims vs. support:** Partially overstated. Strong support for denoising; weak support for deblurring; the scope claim "three classical image restoration tasks" is the main mismatch.
- **Experimental soundness:** Mostly sound. Ablation is thorough; scalability study is convincing; "Only real" is the primary unexplained gap.
- **Clarity:** Good overall; a few ambiguities around the COCO extension and "Only real" setup.
- **Value to community:** Solid. The framework is reusable, practical, and motivates further work on noise-space adaptation.

---

## Score and Decision

**Calibration anchors:**

| Paper | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| D3AD anomaly detection | 7jUQHmz4Tq.md | 3.0 | R1 weak | Much weaker; limited novelty |
| VIPaint inpainting | dAavOuxZvo.md | 3.0 | R1 weak | Much weaker |
| DiffAD dehazing | f4aMqhYG7z.md | 5.6 | R1/R2 mid | Similar domain; our paper is more novel, training-only |
| Patch-based diffusion OOD | 7SFTZwNUQA.md | 5.2 | R1 mid | Less novel framing |
| sRGB Noise Modeling (NAFlow) | 2XBBumBGeP.md | 6.5 | R2 | Comparable scope; our paper has broader tasks and more novel framing |
| Video Inverse Problems DM | TRWxFUzK9K.md | 6.5 | R2 | Comparable novelty and execution |
| PnP Prior Mismatch | HXjXPQU3yJ.md | 6.25 | R2 | Comparable; more theoretical |
| GAN Noise Injection Analysis | sLregLuXpn.md | 5.0 | R2 | Weaker than our paper |
| Random Noise Injection RNINet | z8PcUSKXXN.md | 5.75 | R2 | Less novel; simpler method |
| One-Step Shortcut Diffusion | OlzB6LnXcS.md | 8.0 | R2 | Stronger; broader impact, cleaner results |

**Round 1 bracket:** 5.5–7.5, based on similarity to DiffAD dehazing (5.6) which is a rejected paper in the same space with less novelty.

**Round 2 narrowing:** The two closest accepted anchors at 6.5 are sRGB Noise Modeling (NAFlow) and Video Inverse Problems with Image DMs. Our paper is comparable to both: it has a more novel framing than NAFlow and broader task scope; it matches the "novel application of diffusion to a non-generation task" profile of the video inverse paper. The main differentiators relative to these 6.5 anchors are: (a) the deblurring null result constrains scope, and (b) the primary baseline comparisons are against methods not designed for image restoration — weakenesses that pull toward 6.0 rather than 7.0. On the other hand, the +8.13 dB denoising result and the scalability finding are strong positive signals. On balance, the paper lands at the 6.5 level.

**Final score: 6.5**

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>