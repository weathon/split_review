## Summary

OF-Diff proposes a diffusion-based layout-to-image generation framework for remote sensing images. The core idea is an online-distillation architecture: a mix-feature teacher decoder (trained with real image features) and a shape-feature student decoder (trained to only use shape features at inference), connected by a consistency loss that transfers fidelity from teacher to student. On top of this, the paper adds an Enhanced Shape Generation Module (ESGM) that extracts object masks via RemoteCLIP + RemoteSAM with random rotation augmentation, and DDPO fine-tuning to improve diversity. On DIOR and DOTA, OF-Diff achieves competitive or best results across 13 metrics covering generation fidelity, layout consistency, shape fidelity, and downstream detection utility.

## Strengths

1. **Online-distillation framework is a clean, well-motivated technical contribution.** The teacher decoder sees mix-features (image + shape) during training with stop-gradient on the shape component, while the student decoder only sees shape features. The consistency loss (Eq. 6) transfers the teacher's fidelity advantage to the student, enabling the student to generate high-quality images at inference *without* requiring real image references. This directly addresses a key limitation of prior instance-level methods like CC-Diff, which need real instances at sampling time. (Section 3.2, Figure 3)

2. **Thorough experimental evaluation across multiple dimensions.** The paper evaluates on 13 metrics spanning generation fidelity (FID, KID, CMMD), layout consistency (CAS, YOLOScore), shape fidelity (IoU, Dice, CD, HD, SSIM), and downstream detection utility (mAP), on two major RS datasets (DIOR, DOTA) plus HRSC2016 in the appendix. Tables 1–3 show OF-Diff achieving best or near-best results on most metrics, with notable gains on shape fidelity (e.g., DOTA IoU 0.1205 vs. AeroGen's 0.0863, Table 2). The unknown-layout generalization experiment (Table 3) is a particularly strong piece of evidence.

3. **Clean ablation isolating each module's contribution.** Table 4 shows ESGM alone provides the largest performance jump (YOLOScore from 41.20 to 55.08), online-distillation (L_c) adds a meaningful further improvement (55.08→57.83), and DDPO adds a smaller but positive increment. The non-redundant contribution of each module is clearly demonstrated.

4. **Domain-motivated design leveraging RS object properties.** The paper correctly identifies that RS objects have quasi-invariant shapes (rectangular courts, circular tanks, symmetric airplanes) — a property not true for natural images. ESGM exploits this via RemoteCLIP + RemoteSAM for mask extraction with random rotation augmentation. The per-class analysis (Figure 5) shows meaningful gains on precisely the hardest categories: airplanes (+8.3% AP50), ships (+7.7%), vehicles (+4.0%).

## Weaknesses

### Fatal
None.

### Major

1. **ESGM's inference mechanism is characterized deceptively.** Section 3.3 states that "at sampling time, it employs learned shape priors to **synthesize** diverse masks of object shape." Two sentences later: "at sampling, it selects enhanced shapes from a lightweight mask pool collected during or after training. In our experiments, we use masks generated during training." This is retrieval from a pre-computed pool of training-set masks (with random rotation), not synthesis from learned priors. The method still works as a retrieval+augmentation mechanism, but the description substantially overstates what ESGM actually does. The paper would be much stronger if it honestly described the mask pool mechanism and characterized the diversity as coming from augmentation (rotation) rather than learned generation of novel shapes. This gap between how the method is described and how it actually operates undermines the stated contribution of "reducing reliance on real images."

2. **DDPO fine-tuning provides marginal improvement relative to its complexity, and the claims are overstated.** From Table 4, adding DDPO to the ESGM+L_c configuration improves YOLOScore from 57.83 to 58.99 (+1.16), mAP50 from 54.31 to 54.44 (+0.13), and FID from 24.98 to 24.92. These are marginal gains from a complex RL fine-tuning procedure that introduces several hyperparameters (k for KNN, ω for KL, reward formulation). The paper lists DDPO as a core contribution ("fine-tune the diffusion process, making the generated remote sensing images more diverse and semantically consistent") but the evidence does not support this level of claim. Additionally, the reward function (Eq. 9) uses the notation KNN(x₀, x₀) which is ambiguous — KNN with the same point as query and implicit reference set is not well-specified, and the KL term does not specify which distributions are being compared. While details may be in Appendix A.2, the main text formulation should be self-contained.

### Minor

3. **Ablation table has an ambiguous duplicate row.** In Table 4, rows 7 and 8 both show ESGM=✓, L_c=✓, DDPO=✓ but report drastically different numbers (Row 7: FID 37.98; Row 8: FID 24.92). Row 8 matches the main result in Table 1, so Row 7 presumably represents a different condition (likely with captions enabled, since the surrounding text discusses how captions degrade fidelity). But there is no column for caption input. The paper states "the ablation experiments for each module were conducted based on the absence of caption input" — if Row 7 used captions, the table should label this clearly. This makes the table ambiguous and looks like a presentation error.

4. **Not all metrics show uniform superiority.** On DIOR, OF-Diff is not best on KID (GLIGEN 0.010 vs. Ours 0.011) and CAS (CC-Diff 82.61 vs. Ours 82.55). While no method is expected to dominate all metrics, the paper's framing in the abstract ("outperforms state-of-the-art methods") could more precisely acknowledge these exceptions.

### Trivial

5. **No confidence intervals or variance reported.** Given the stochastic nature of diffusion sampling, single-run metrics are standard in this literature, but noting the absence would help contextualize results.

## Nice-to-Haves

- A sample-diversity analysis (e.g., LPIPS between images generated from the same layout) would strengthen the DDPO claim, since the current evidence for diversity improvement is indirect.
- The discussion of how captions degrade fidelity (Section 4.5) is interesting and could be expanded — it raises a subtle trade-off between aesthetics and distributional fidelity that is rarely discussed in L2I papers.

## Removed Points

- **Harsh Critic: "Eq. 4 contradicts text about c_i at inference"** — Removed. The paper says at inference, c_i comes from ControlNet processing the layout input (not from a real image). Eq. 4 shows the shape decoder conditions on both c_i and c_s, which is consistent: at inference, both are derived from the layout. No contradiction.
- **Harsh Critic: "computational cost comparison missing"** — Removed. This is outside the paper's stated scope and would be a nice-to-have, not a weakness.
- **Harsh Critic: "KNN(x₀, x₀) is identically zero"** — Weakened/demoted. The notation is sloppy (reference set unspecified), but KNN in practice measures distance to neighbors in a reference set, not self-distance. The real issue is the ambiguous notation, which is addressed in Major weakness 2.
- **Strength Finder: generic strengths about "important problem" / "interesting"** — Removed. These are too generic to serve as evidence-based strengths.
- **Strength Finder strength #2 claiming "consistent superiority across 13 metrics"** — Refined. The paper is best on most but not all metrics; the strength is now worded more precisely.

## Novel Insights

The online-distillation framework in OF-Diff represents an interesting paradigm for L2I generation: rather than requiring real image patches at inference (like CC-Diff) or relying purely on layout-to-image conditioning (like AeroGen), it learns to *distill* real-image fidelity into a shape-only student during training, then discards the teacher at inference. This "distill then decouple" strategy is conceptually clean and could be applicable beyond remote sensing. A notable finding in the ablation is that adding captions *hurts* generation fidelity while improving aesthetics — suggesting that for detection-oriented data augmentation, distributional fidelity to the target domain matters more than human-perceived quality. This is a nuanced insight that could inform future work on task-specific generation.

## Suggestions

1. **Honestly describe the ESGM inference mechanism** as a mask-pool retrieval with random rotation augmentation, rather than claiming it "synthesizes" shapes from learned priors. The mechanism is still useful and well-motivated by RS quasi-invariant shapes; the honest description will not weaken the paper.
2. **Fix the DDPO reward formulation** (Eq. 9) to clearly specify the reference set for KNN and the distributions for KL. Alternatively, de-emphasize DDPO as a minor enhancement consistent with the marginal evidence.
3. **Add a caption column to Table 4** or split the table to resolve the ambiguous Row 7/Row 8 duplication.
4. **Calibrate the language about DDPO** in the contributions and abstract to match the experimental evidence (small incremental gains rather than a major improvement).

## Score and Decision

**Score: 5.5**

**Decision: Accept**

**Calibration Details:**

*Round 1 (Bracketing, 3.5–7.5):* The paper sits between the weak band (<3.5, covering unrelated diffusion papers like floor-plan generation at 3.0, ancient buildings at 3.0) and the strong band (>7.5, covering high-impact papers like Würstchen at 8.0, shortcut models at 8.0). The middle band (3.5–7.5) contains the most comparable anchors.

*Key anchors in the middle band:*
- **GeoDiffusion (6.5)** — L2I for detection data. Cleaner presentation and simpler method, but less novel technically. OF-Diff has a more interesting technical contribution (online-distillation) but worse presentation and overclaim issues. → OF-Diff slightly weaker.
- **Adversarial Sup L2I (6.0)** — L2I diffusion with adversarial supervision. Comparable novelty level, similar concern about marginal gains from one component. OF-Diff's evaluation is more thorough. → Comparable to slightly weaker.
- **DiffusionSat (6.25)** — RS foundation model. Broader scope, some presentation issues. OF-Diff has clearer task focus. → Comparable.
- **GDCC (5.33)** — L2I+OD cycle consistency. Rejected due to instability concerns and limited evidence. OF-Diff has stronger experimental evidence and no instability issues. → OF-Diff stronger.
- **DODA (5.0)** — L2I for agricultural domain adaptation. Single dataset, limited generalizability claims. OF-Diff has broader evaluation. → OF-Diff stronger.

*Narrowing:* The online-distillation contribution is genuinely novel and well-executed, warranting a score above the rejected GDCC (5.33) and DODA (5.0). However, the ESGM overclaim, marginal DDPO evidence, and presentation issues prevent it from reaching the level of GeoDiffusion (6.5) or the cleanest L2I papers. The score 5.5 reflects a paper with a solid core technical contribution that is weakened by overclaiming in its secondary components and presentation sloppiness.

<score>5.5</score>
<decision>Accept</decision>