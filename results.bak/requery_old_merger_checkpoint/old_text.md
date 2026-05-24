Now I have all the information I need. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses

### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves

## Removed Points

## Novel Insights

## Suggestions

## Score and Decision

Let me write the review now.

**Review of INP-Former criticism (Claim 1):** The harsh critic claims adapting INP-Former via two independent streams "entirely discards INP-Former's core contribution: its test-time prototype extraction from the same image." This is incorrect. INP-Former's core mechanism is extracting intrinsic normal prototypes directly from a single test image. In the paper's adaptation, each stream independently does exactly this on its respective modality (RGB or surface normals). The core contribution is preserved per modality. The critic's suggestion to add cross-modal fusion to INP-Former would give it capabilities it was never designed for, making the comparison unfair in the opposite direction. I will REMOVE this criticism.

**Review of FIND missing (Claim 5):** The harsh critic claims FIND is missing from Table 1. From the paper, FIND is cited for surface normal generation (line 159) and compared only in Table 4 (efficiency) as achieving 0.921 AUROC_I on 10-shot. It is indeed absent from the main few-shot comparison in Table 1. This is a valid concern. KEEP as major.

**Review of error bars (Claim 2):** The paper reports no variance across multiple trials. This is a valid concern for few-shot settings. KEEP as major.

**Review of APR (Claim 3):** The paper provides theoretical justification but no empirical validation. The ablation shows APR is responsible for about 0.6% improvement, so this is not fatal. KEEP as minor.

**Review of Real-IAD (Claim 4):** The paper clearly states these are full-shot results, and acknowledges D³M uses tri-modal data. Some claim over "cherry-picked" categories is overstated - the paper reports the full table. KEEP as minor - the comparison is less clean but this is supplementary evidence.

Let me finalize.## Summary

PIRN proposes a prototype-driven intra-modal reconstruction framework with cross-modal normality communication for few-shot multimodal anomaly detection. The core innovations are: (1) Balanced Prototype Assignment (BPA) using balanced optimal transport to prevent codebook collapse, (2) Adaptive Prototype Refinement (APR) for test-time prototype updates via GRU, and (3) Multimodal Normality Communication (MNC) that exchanges prototypical normality knowledge across RGB and surface-normal modalities. The method consistently outperforms baselines across MVTec-3D-AD, Eyecandies, and Real-IAD under 5/10/50-shot settings, while being 4.35× faster and using 85% fewer FLOPs than the recent SOTA FIND.

## Strengths

1. **Consistent and substantial few-shot gains across multiple benchmarks**: Table 1 shows PIRN outperforms the strongest baseline on MVTec-3D-AD by +3.9 AUROC_I (5-shot), +3.7 (10-shot), and +2.4 (50-shot), and on Eyecandies by +3.6, +4.0, and +2.2 AUROC_I in the same settings. This is direct, replicated evidence that the method succeeds in data-scarce regimes where prior work degrades.

2. **Ablation confirms all three innovations contribute independently**: Table 2 isolates BPA, APR, and MNC; removing each produces a measurable drop (e.g., removing APR drops AUROC_I from 0.922 to 0.883, removing MNC from 0.922 to 0.916), proving that balanced assignment, adaptive refinement, and cross-modal communication each play a distinct role in the reported gains.

3. **SOTA accuracy at drastically lower computational cost**: Table 4 shows PIRN achieves 0.922 AUROC_I with 103.36G FLOPs and 17.49ms latency, while FIND (0.921 AUROC_I) requires 728.46G FLOPs and 76.09ms — a 4.35× speedup and 85% fewer FLOPs. This convincingly demonstrates that strong few-shot AD performance does not require expensive architectures.

4. **Design-space validation via systematic ablations**: Tables 5 and 6 ablate codebook size K and decoder depth L across multiple shot settings. Optimal K=10 and L=2 are consistent, and performance degrades with too many/few prototypes (K=100 gives 0.901 AUROC_I vs. 0.963 at K=10), showing design choices are empirically grounded.

5. **Interpretable evidence of discriminative prototype encoding**: Figure 4 visualizes token displacements in PCA space and shows anomalous tokens undergo larger shifts than normal tokens during reconstruction, with clear separation in histograms — directly supporting the claim that prototypes act as normality anchors.

## Weaknesses

### Major

1. **Missing FIND baseline in the main few-shot comparison table.** FIND (Li et al., 2025) is cited for surface normal generation and compared in the efficiency table (Table 4), where it achieves 0.921 AUROC_I on the 10-shot MVTec-3D-AD setting — almost matching PIRN's 0.922. Yet FIND is absent from the main few-shot results in Table 1, where readers would naturally look for a comprehensive comparison. Given that the paper itself calls FIND "the recent SOTA," its omission from the primary comparison is a notable gap that weakens the central claim of "consistently superior performance."

2. **No error bars or variance reporting for few-shot results.** The paper reports single-run results without standard deviations or confidence intervals. In few-shot anomaly detection, the specific training samples chosen can dramatically affect outcomes (Table 1 margins on pixel-level metrics are often 0.2–0.6% absolute). Without multiple seeds (at least 3), it is impossible to assess whether the reported improvements are statistically significant or within the noise of the sampling procedure.

### Minor

3. **The APR's robustness assumption is theoretically motivated but empirically unvalidated.** The paper argues that anomalous patches are assigned diffusely across prototypes via optimal transport and thus contribute weakly to the context vector. However, no experiment validates this claim — e.g., there is no analysis of what happens when anomalies span large contiguous regions or consist of subtle global shifts. The ablation (Table 2) does show that removing APR drops AUROC_I only from 0.922 to 0.916, meaning the core method does not collapse without it, but the paper would be strengthened by demonstrating empirically when the robustness assumption holds and when it breaks.

4. **Real-IAD D3 evaluation is supplementary but less cleanly controlled.** This experiment uses the full-data (not few-shot) setting and compares against D³M which employs a tri-modal representation (2D+Pseudo-3D+3D). There are no baselines using exactly the same inputs (RGB+surface normals) as PIRN. The paper acknowledges these differences, and this result is positioned as auxiliary evidence, but claims of "significantly outperforming" in specific categories should be tempered given the modality mismatch.

### Trivial

None.

## Nice-to-Haves

- Include FIND and other recent SOTA methods in the main few-shot comparison table (Table 1), or explain why they cannot be fairly compared.
- Add variance bars over at least 3 random few-shot splits for all main results.
- Provide a synthetic experiment that measures context vector deviation from the true normal prototype when known anomalies of varying spatial extent are inserted into test images.
- On Real-IAD, note the absence of same-modality baselines and frame the comparison as suggestive rather than conclusive.

## Removed Points

- **INP-Former baseline adaptation is unfair (from Harsh Critic)**: The critic claimed the two-stream adaptation "entirely discards INP-Former's core contribution: its test-time prototype extraction from the same image." This is factually incorrect. INP-Former's core mechanism — extracting intrinsic normal prototypes from a single test image — is preserved per modality in each independent stream. The two-stream architecture with element-wise fusion is the most natural and faithful adaptation of a 2D method to the multimodal setting. Adding cross-modal fusion (as the critic suggests) would give INP-Former capabilities it was never designed for and would be unfair in the opposite direction. **Removed: factually wrong.**

- **"Paper should compare against a more thoughtful adaptation of INP-Former" (from Harsh Critic)**: As noted above, any adaptation with cross-modal fusion would deviate from INP-Former's original design. The paper's adaptation is already reasonable. **Removed: builds on factually incorrect premise.**

- **"Table 8 is difficult to interpret due to missing metrics and incomplete baselines" (from Harsh Critic)**: Table 8 reports two standard metrics (AUROC_I/J and AUROC_P) for all methods, which is standard. The paper clearly states the modality differences. This is not a genuine weakness — it is an acknowledged limitation of the comparison. **Removed: problem is already addressed by the paper's own framing.**

- **"Cherry-picked categories" on Real-IAD (from Harsh Critic)**: The paper reports the full table with all 20 categories, not selected ones. The text highlights a few examples as illustrations. This is standard practice, not cherry-picking. **Removed: mischaracterization.**

- **"Clarification of training procedure" and "60 epochs may lead to overfitting" (from Harsh Critic)**: 60 epochs on 5–50 samples is not unusual for few-shot AD methods, and the paper achieves strong results without early stopping concerns being evident. This is speculative. **Removed: speculative.**

- **Strength Finder's generic strengths**: Claims such as "the paper addressed an important problem" and "the motivation is clear" are generic and not specific to this paper. **Removed: generic.**

## Novel Insights

The key insight that emerges from reading the paper alongside the reviews is that PIRN's design successfully decouples the "what is normal" representation (learnable prototypes with balanced OT) from the "is this specific patch normal" decision (reconstruction error), while using cross-modal communication at the prototype level (rather than dense feature alignment). This design choice — exchanging high-level prototypical knowledge rather than raw features — is a principled way to avoid the brittleness of cross-modal alignment methods in data-scarce regimes. The paper also demonstrates a rarely-seen dual benefit: better performance at lower cost, because using a compact codebook of K=10 prototypes avoids the expensive memory bank lookups that methods like FIND require. The efficiency result (Table 4) is arguably as significant as the accuracy gains for practical deployment.

## Suggestions

- Add FIND (and any other recent SOTA multimodal AD methods) to the main few-shot comparison table. Report results under the same 5/10/50-shot splits.
- Report mean and standard deviation over at least 3 random few-shot splits for all main results.
- Add an experiment that directly measures APR's robustness: inject synthetic anomalies of varying size/intensity into test images and measure the deviation of the OT-derived context vector from the ground-truth normal prototype.
- Add a brief discussion of when APR might fail (e.g., large-area anomalies, global color shifts) to acknowledge the limitation transparently.
- For Real-IAD, either add baselines with the same input modalities or explicitly frame the comparison as indicative rather than directly competitive.

## Score and Decision

**Calibration procedure:**

**Round 1 (Bracketing):** Queried three bands on topics related to few-shot AD, prototype-based AD, and multimodal AD.
- Weak band (score < 3.5): CLIP-LAD (3.00), Generalized AD (2.50) — clearly weaker than PIRN.
- Mid band (3.5–7.5): PTAD (4.25), Prototype-oriented Fast Refinement (5.50), H-PAD (5.60), One-for-All Few-Shot AD (6.40), MMAD (6.50), AnomalyCLIP (6.17).
- Strong band (score > 7.5): Deep Orthogonal Hypersphere (8.00), Test-time Adaptation (8.00) — clearly stronger than PIRN.
- **Round 1 bracket: 5.0–7.0.**

**Round 2 (Narrowing):** Queried within (4.5–6.0) and (6.0–7.5) on more specific topics.
- Prototype-oriented Fast Refinement (5.50, reject) — PIRN is significantly stronger: more thorough evaluation, cleaner method, better efficiency analysis.
- H-PAD (5.60, accept) — PIRN is stronger: larger-scale evaluation, better ablation, more novel methodology.
- One-for-All Few-Shot AD (6.40, accept) — comparable quality: both have strong evaluations and clear contributions; One-for-All addresses a novel paradigm while PIRN addresses multimodality.
- MMAD (6.50, accept) — benchmark paper, different contribution type.
- AnomalyCLIP (6.17, accept) — comparable quality: both have clear contributions and thorough evaluations.
- **Narrowed bracket: 5.5–6.5.**

PIRN is clearly stronger than the 5.50 prototype refinement paper and comparable to the 6.0–6.5 papers. However, the missing FIND baseline in the main comparison table and the absence of error bars are evaluation gaps that prevent scoring at the top of this band. The paper's core technical contributions are novel, well-ablated, and produce consistent SOTA results with substantial efficiency gains.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>