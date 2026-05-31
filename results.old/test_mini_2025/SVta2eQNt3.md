Now I have sufficient anchors for calibration. Let me write the final consolidated review.

## Summary

The paper presents a NeRF-based method for learning animatable human avatars from monocular video. The core contribution is a "locality-sensitive deformation" that decomposes motion into skeletal rigid motion (inverse LBS) plus a non-rigid offset predicted per body part using a GNN and window function — combining canonical-space rendering with part-local deformation. The method is evaluated extensively on ZJU-Mocap, ActorsHQ, SynWild, and in-the-wild videos, reporting strong results across novel view synthesis, novel pose animation, and shape reconstruction, outperforming a large set of baselines including HumanNeRF, MonoHuman, Vid2Avatar, NPC, PM-Avatar, 3DGS-Avatar, and GoMAvatar.

## Strengths

- **Locality-sensitive non-rigid deformation is well-motivated and clearly operationalized.** The paper identifies a genuine gap: canonical-space methods (HumanNeRF, MonoHuman) model non-rigid offsets globally, losing detail; part-space methods (NPC, PM-Avatar) lack canonical-space generalization. The proposed solution — projecting points into per-part local frames, encoding part relationships via GNN, aggregating with a learnable window function, and predicting a Cartesian offset Δx in canonical space — is a principled design that fills this gap. Section 3.2 (Eq. 2–8) describes the mechanism clearly, and the "Relation to baselines" paragraph honestly acknowledges connections to prior work.

- **Simultaneous improvement across all three tasks, demonstrated on multiple datasets with many baselines.** Table 2 shows that Ours achieves the best perceptual metrics (LPIPS, FID, KID) on both novel view and novel pose on ZJU-Mocap, and the best or second-best Chamfer Distance and Normal Consistency on shape reconstruction. Table 3(a) shows consistent advantages on ActorsHQ. The baseline set is extensive (7+ methods including both NeRF-based and 3DGS-based), and results are reported on 5 datasets — substantially more thorough than many papers in this area. The FID and KID improvements (which are not used as training losses) are particularly strong evidence of architectural benefit, e.g., 22% better FID and 35% better KID on novel view over the next best.

- **Components validated through informative ablation.** Table 3(b) and Fig. 8 ablate five components: removing canonical pose, removing locality (no Δx), removing window function, removing GNN features, and removing offset regularization. Each ablation degrades results, and the "w/o window" and "w/o GNN" ablations produce specific failure modes (e.g., distorted hands, overfitted wrinkles) that match the design intuition. The offset regularization (ℒ_Δx) is shown to prevent distortions in challenging poses (Fig. 8, left arm).

- **Convincing qualitative generalization to loose clothing and out-of-distribution poses.** On ActorsHQ (Fig. 2) and the Youtube-to-AIST++ motion retargeting (Fig. 5), the method preserves body contours and details (e.g., cloth buttons) where baselines distort or blur. These scenarios (loose garments, extreme unseen poses) are where the locality-sensitive design should help most, and the results deliver.

## Weaknesses

### Major

- **LPIPS is used both as a training loss (Eq. 17) and as an evaluation metric, creating a confound for the headline LPIPS gains.** The paper explicitly states "we employ the LPIPS metric for network training" (line 162) and LPIPS is one of the primary evaluation metrics in Table 2 where the method shows ~9–10% improvement over the next best. While the method also wins on FID and KID (which are not training losses) — establishing genuine architectural benefit — the LPIPS-specific claims are weaker than a reader would infer. The paper would be substantially strengthened by either: (a) retraining the model and best baselines without LPIPS loss and reporting both sets of numbers, or (b) at minimum, acknowledging this confound directly in the conclusions rather than positioning LPIPS improvements as pure architectural wins.

### Minor

- **Shape reconstruction metrics are essentially tied with Vid2Avatar.** On ZJU-Mocap, Ours achieves CD=0.041 (vs. Vid2Avatar 0.042) and NC=0.845 (vs. Vid2Avatar 0.852). On SynWild, Ours has CD=0.485 (vs. 0.499) and NC=0.690 (vs. 0.687). The paper acknowledges this honestly (line 271: "pseudo ground truth smoothes out many desired surface details"), but the positioning as "state-of-the-art across all three tasks" is slightly oversold for geometry — the improvements here are marginal, and the geometry claim relies heavily on qualitative figures.

- **The "validity test" for {x̄_i} is mentioned but never described** (line 136: "perform a validity test for {x̄_i}"). Presumably it prunes points far from any part, but the procedure, threshold, and impact on training are unspecified. This is a missing reproducibility detail.

- **No training time, GPU memory, or convergence speed reported.** The paper mentions "SMLP-based weight computation can improve GPU memory consumption and convergence speed" (line 92) but provides no actual numbers. Given the method uses uniform-only sampling and a per-bone architecture, understanding the computational trade-off is important, especially when compared to 3DGS-based methods that render at interactive rates.

- **No error bars or standard deviations in main tables.** The main quantitative results (Table 2, Table 3) report means without variance. Given that ZJU-Mocap has only 8 sequences and ActorsHQ has 4, per-sequence variability could be large. The paper references per-sequence tables (Tab. I, J) in supplementary, but the main paper would benefit from summarizing this variability.

- **No limitations section.** The method has clear limitations (dependence on SMPL pose estimation, monocular setup, fixed skeleton, loose clothing handling), and discussing these would strengthen the paper's scientific rigor. This is a standard expectation for ICLR papers.

### Trivial

- The paper uses the notation "SMLP" (line 92) without defining it — presumably "SMPL" is intended, but the term appears as "SMLP-based weight computation."
- "Zhou representation" (B_i ∈ R⁶) is cited without describing the conversion to a 4×4 transformation matrix, but this is standard practice (Zhou et al., 2019) and not a real barrier.

## Nice-to-Haves

- Ablate the window function parameters (α=2, β=6) or compare with learned scales. The paper tests removing the window entirely but not sensitivity to these specific hyperparameters.
- Include GauHuman in the ZJU-Mocap table (Table 2) for completeness, since it appears in the ActorsHQ table (Table 3a). If not applicable, state why.
- Report the GNN architecture details (number of layers, hidden dimensions, how the per-node MLP weights differ from standard GNN weight-sharing).

## Removed Points

- **"Novelty is incremental" framing as a weakness** — Removed. The paper honestly acknowledges connections to prior work in the "Relation to baselines" section (line 138). The contribution is clearly scoped: applying locality to the non-rigid offset prediction in canonical space, which prior work did not do. A paper does not need to invent an entirely new mechanism to make a valid contribution; the empirical results demonstrate the value of this specific combination.

- **"Several baselines have unexpectedly bad numbers"** — Removed. The paper does not state whether numbers are from re-implementations or original code. Without evidence that the numbers are wrong (they are consistent with running published code on this specific protocol), this is speculation. The paper uses standard datasets and splits following established protocols.

- **"Table 1 framing sharply distinguishes 'local deformation' (only Ours) from other methods"** — Removed as misleading. Table 1 has a "Local deformation" column where only Ours has a checkmark, which is factually correct — no prior method predicts a non-rigid offset conditioned on local part information for canonical-space avatars. The distinction is legitimate.

- **"GNN with individual MLP weights is not standard GNN practice"** — Removed. The paper provides a rationale ("irregular nature of human skeleton can be better considered"), and this is a design choice, not an error. The paper could specify it more concretely (which is noted as a minor weakness above), but the design itself is not problematic.

- **"No statistical significance reported"** — Merged into minor weakness (no error bars) rather than treated as a separate point.

- **"Eq. 3 doesn't specify how B_i converts to 4×4 matrix"** — Removed. This is a standard detail for anyone working in this area (Zhou et al., 2019).

- **"Comparison to concurrent work GauHuman only in Table 3(a)"** — Moved to nice-to-have; this is a completeness suggestion, not a flaw in the paper's claims.

- **Strength Finder's generic strengths** (e.g., "addressed an important problem") — Removed. Only kept strengths that cite specific evidence from the paper.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Disentangle the LPIPS training loss from the architectural contribution.** Retrain the full model and a top-performing baseline (e.g., GoMAvatar or 3DGS-Avatar) without LPIPS loss and report both sets of results. If the LPIPS gains persist without the loss, the claim is ironclad; if they shrink considerably, acknowledge that the contribution is a combined pipeline rather than purely architectural.

2. **Add a limitations section** discussing failure cases (extreme poses, occlusions, loose clothing beyond SMPL's capability, pose estimation failures).

3. **Provide training time, GPU memory, and convergence speed** for the full model and key ablations.

4. **Describe the validity test** (line 136) in detail — what threshold, how it affects training, and its impact on quality vs. speed.

**Calibration anchors used:**

| Path | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| QhoehDVFeJ (EMA) | 5.75 | R1, R2 | Weaker evaluation (fewer baselines/datasets), more disputed novelty; this paper is clearly stronger |
| gY08Ou8EL7 (LIFe-GoM) | 7.00 | R1, R2 | Stronger novelty (iterative feedback mechanism), no LPIPS confound; this paper is somewhat weaker |
| KQ2i6jazVK (Articulated Objects) | 6.60 | R2 | Different domain but similar evaluation thoroughness; this paper is comparable |
| sPUrdFGepF (Consistent4D) | 6.80 | R2 | Strong 4D generation results but some reviewer scores were mixed (10,6,6,6,6); this paper is slightly weaker |
| hkWHdI8ss5 (SITTO) | 2.33 | R1 | Much weaker paper; this paper is substantially stronger |
| 7ERQPyR2eb (Real3D-Portrait) | 8.50 | R1 | Much stronger paper (spotlight); this paper is clearly weaker |

**Round 1 bracket:** Initial bracketing placed the paper between scores of ~5 and ~7.5.

**Round 2 narrowing:** Inside the (5.5, 7.5) range, the paper compares favorably to EMA (5.75, reject) on evaluation breadth and result strength, but falls below LIFe-GoM (7.00, poster) due to the LPIPS confound and less novel architecture. The final score of 6.5 reflects that the paper has a clear, well-validated contribution with genuinely convincing results (especially on FID/KID and qualitative generalization) but is held back by the LPIPS training-vs-evaluation confound and several incomplete reproducibility details.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>