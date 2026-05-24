Now I have enough calibration data. Let me synthesize my findings and write the final review.

**Bracket from Round 1:** Between 5.5 and 8.0. The most similar prototype-refinement paper scored 5.50, but PIRN is substantially stronger. The 8.00 hypersphere paper has theoretical contributions PIRN lacks.

**Narrowing from Round 2:** Between 6.5 and 7.5. The 6.40 few-shot AD paper has more methodological concerns and missing experiments. The 7.50 multimodal few-shot paper is closest in quality — well-motivated modules, comprehensive evaluation, minor weaknesses. PIRN has comparable or slightly better evaluation breadth (3 benchmarks + efficiency analysis vs 2 benchmarks).

**Final Score:** 7.0. The paper makes a solid, well-executed contribution with strong empirical results and coherent methodology. The weaknesses are minor: no variance reporting, no experimental verification of APR stability under anomalies, and the Real-IAD experiment is full-shot (stated explicitly). These are addressable and don't undermine the core claims.

---

## Summary

PIRN proposes a prototype-driven reconstruction framework for few-shot multimodal anomaly detection. It introduces three complementary modules: Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) to adapt prototypes at inference time via a GRU, and Multimodal Normality Communication (MNC) for cross-modal prototype-level knowledge exchange. The method is evaluated on MVTec 3D-AD, Eyecandies, and Real-IAD benchmarks, showing consistent and substantial gains over strong baselines in few-shot settings (e.g., +3.9 pp AUROC_I at 5-shot on MVTec 3D-AD) while maintaining computational efficiency.

## Strengths

- **Clear problem diagnosis and well-motivated design.** The paper identifies three specific failure modes of existing MAD methods under few-shot settings (alignment collapse, memory-bank brittleness, modality isolation) and maps each to a concrete module (BPA, APR, MNC). The motivation is grounded in observable failure patterns (Fig. 1), not just generic claims.

- **Strong and consistent empirical gains.** Table 1 shows PIRN outperforms all baselines — including INP-Former, CFM, M3DM, and 3D-ADNAS — across 5-, 10-, 50-, and all-shot settings on both MVTec 3D-AD and Eyecandies. Gains are largest where the paper claims they should be (5-shot: +3.9 pp AUROC_I on MVTec, +3.6 pp on Eyecandies) and shrink as data increases, which is consistent with the few-shot motivation.

- **Effective cross-modal communication validated by modality ablation.** Table 3 shows that combining RGB and surface normals yields the largest relative gain in the 5-shot setting (AUROC_I rises from 0.854/0.794 single-modal to 0.900 multimodal), directly validating MNC's value when per-modality representations are weakest.

- **Comprehensive ablation and analysis.** Each module (BPA, APR, MNC) is ablated (Table 2), codebook size and decoder depth are studied (Tables 5-6), APR aggregation strategies are compared (Table 7), and qualitative analyses (Figs. 3-4) show sharper anomaly maps and better normal/anomalous score separation. The efficiency comparison (Table 4) is a welcome bonus — PIRN achieves the best AUROC_I (0.922) with ~7× fewer FLOPs and ~4.4× lower latency than FIND.

- **Evaluation across three diverse benchmarks.** Results on MVTec 3D-AD, Eyecandies, and the challenging Real-IAD D3 dataset (20 categories, Table 8) demonstrate generalization. On Real-IAD, PIRN achieves best pixel-level AUROC (0.961) despite using fewer modalities than D³M.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **No variance estimates for few-shot experiments.** All reported results are single numbers. In few-shot settings with 5–50 training samples per class, the specific draw of normal samples can materially affect performance. Reporting standard deviations over multiple random seeds or cross-validation folds would strengthen the evidence. This is a standard practice that would increase confidence in the reported gains, though the consistent trends across benchmarks and shot counts partially mitigate the concern.

- **APR stability under anomalous test images is not experimentally verified.** The paper argues that anomalous patches are assigned diffusely in the OT-based context extraction and that the GRU gate suppresses their influence (Section 3.3). While the overall results support the design, a targeted analysis — e.g., measuring prototype codebook drift (cosine distance before/after APR) separately for normal vs. anomalous test images — would close the evidential loop and make the mechanism more convincing.

- **Real-IAD experiment uses full training data, not few-shot.** The paper's core contribution targets few-shot settings, but the Real-IAD evaluation (Table 8, line 325) uses the full dataset. The paper explicitly states this ("in the full-data training setting"), so there is no misrepresentation, but the experiment does not directly test the few-shot advantage on this benchmark. This is a minor narrative misalignment.

### Trivial

- The component ablation in Table 2 is difficult to parse in the review copy due to formatting issues (all rows show identical checkmarks). While this is likely a parsing artifact, the authors should ensure the submitted table clearly distinguishes which components are active in each row.

## Nice-to-Haves

- A brief limitations paragraph discussing assumptions (e.g., availability of surface-normal maps, behavior when anomalies dominate the image) and failure modes would round out the paper.
- Extending few-shot evaluation to Real-IAD or explicitly noting it as future work would align the narrative with the core contribution.
- A simple baseline replacing MNC with concatenated prototype-aligned features would isolate the contribution of the gated cross-attention design.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic #1 — Ablation table formatting:** The garbled Table 2 with misaligned checkmarks and anomalous AUROC_I values is a parser artifact. Per hard rules, formatting issues introduced by the extraction process are not the authors' fault and do not constitute a real weakness.

- **Harsh Critic — Missing variance as "evidential gap":** While valid as a minor point, the harsh critic's characterization of this as an "evidential gap" that "cannot be assessed for reliability" is overstated. Single-run reporting is standard in the MAD literature (the compared baselines also report single numbers), and the consistent trends across three benchmarks and multiple shot counts provide cross-validation.

- **Strength Finder — "Interpretable prototype-based behaviour":** The feature displacement visualization (Fig. 4) is informative but calling it "interpretable" overstates the case — it shows that anomalous tokens move further, which is expected from the method's design rather than providing novel insight. Kept as supporting evidence but demoted from a core strength.

- **Harsh Critic — "Missing parts: per-category ablation results, hyperparameter sensitivity, noise contrast baseline":** The per-category results are stated to be in the appendix (line 207: "We further report per-category results in Appendix Tab. 11"), which is stripped. Hyperparameter sensitivity beyond K and L is a nice-to-have, not a weakness. The noise-contrast baseline suggestion is scope creep — the paper already includes a baseline without MNC (Table 2/Table 3 single-modal rows).

- **Harsh Critic — "Comparison with a noise contrast baseline":** This demands the paper evaluate a simpler alternative to MNC. MNC's contribution is already isolated in the modality ablation (Table 3, comparing multimodal vs single-modal) and component ablation (Table 2). Adding a concatenation baseline is a nice-to-have, not a weakness.

- **Harsh Critic — "Missing limitations section":** The appendix (which may contain limitations) is stripped. Per hard rules, we do not criticize missing content from stripped sections.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder largely corroborate the paper's claims without surfacing genuinely new observations about the work.

## Suggestions

- Run the few-shot experiments over 3–5 random seeds and report mean ± std. This is the single highest-impact improvement to the paper's rigor.
- Add a brief APR stability analysis: measure prototype codebook drift for normal vs. anomalous test images to validate the claim that anomalous patches are suppressed during refinement.
- Either run few-shot experiments on Real-IAD or add a sentence acknowledging that the Real-IAD evaluation is full-shot and that few-shot Real-IAD results are left for future work.

---

**Anchor comparisons:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Prototype-oriented Fast Refinement for Few-shot IAD | gTsLBDMZrL | 5.50 | R1 | PIRN is substantially stronger: clearer motivation, more complete solution (3 modules vs 1 EM refinement), better ablations, multimodal. |
| Prototype-based OT for OOD | J2we1sVd9m | 4.60 | R1 | Less relevant; PIRN has broader scope and stronger empirical validation. |
| Deep Orthogonal Hypersphere Compression | cJs4oE4m9Q | 8.00 | R1 | PIRN lacks the theoretical analysis of this paper; empirically strong but no proofs. |
| One-for-All Few-Shot AD | Zzs3JwknAY | 6.40 | R2 | PIRN is stronger: more cohesive method, more comprehensive ablations, three benchmarks, efficiency analysis. |
| Multimodality Helps Few-Shot 3D PCS | jXvwJ51vcK | 7.50 | R2 | Most comparable anchor. Similar quality: well-motivated modules, substantial gains, thorough experiments. PIRN has slightly broader evaluation (3 benchmarks, efficiency); the 7.50 paper has slightly cleaner presentation. |

**Bracket:** Round 1 placed the paper between 5.5 and 8.0. Round 2 narrowed to 6.5–7.5. The paper is clearly stronger than the 6.40 anchor and comparable to the 7.50 anchor. Given minor but real weaknesses (no variance reporting, no APR stability verification), the final score is set at 7.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>