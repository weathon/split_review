# Requery old Merger checkpoint

- old call id: `019e4df1-df33-76dd-bc69-8e5029859f8e`
- old response id: `gen-1779424157-fG8t5s745dTsydhVFmBz`
- new response id: `gen-1779490650-8cVgWJ0co7pR2gUcHfGL`
- model arg: `deepseek-v4-flash`
- input items: `49`
- tools: `read_paper, grep_paper, read_anchor, calibration_search`
- old text chars: `13314` sha256 `f5249a64cb82f9ddb43ae8621506d7890bbb83e820b4d1e2c3aecb8847015e88`
- new text chars: `9380` sha256 `87c172e65a4f914f1874b0eb2ba1d6979911c6e094b3bbb4488bd1fb5b257dc9`
- SequenceMatcher ratio: `0.1660`
- old score / decision: `6.0` / `Accept`
- new score / decision: `6.0` / `Accept`

## Diff first 260 lines

```diff
--- old_2026_05_22_0429_final_merger
+++ new_requery_final_merger
@@ -1,127 +1,97 @@
-Now I have all the information I need. Let me write the consolidated review.
+Now I have all the information needed. Let me write the consolidated review.
 
 ## Summary
-2-3 sentence summary of the paper's contribution.
 
-## Strengths
-- strength 1 with evidence
-- strength 2 with evidence
-
-## Weaknesses
-
-### Fatal
-### Major
-### Minor
-### Trivial
-
-## Nice-to-Haves
-
-## Removed Points
-
-## Novel Insights
-
-## Suggestions
-
-## Score and Decision
-
-Let me write the review now.
-
-**Review of INP-Former criticism (Claim 1):** The harsh critic claims adapting INP-Former via two independent streams "entirely discards INP-Former's core contribution: its test-time prototype extraction from the same image." This is incorrect. INP-Former's core mechanism is extracting intrinsic normal prototypes directly from a single test image. In the paper's adaptation, each stream independently does exactly this on its respective modality (RGB or surface normals). The core contribution is preserved per modality. The critic's suggestion to add cross-modal fusion to INP-Former would give it capabilities it was never designed for, making the comparison unfair in the opposite direction. I will REMOVE this criticism.
-
-**Review of FIND missing (Claim 5):** The harsh critic claims FIND is missing from Table 1. From the paper, FIND is cited for surface normal generation (line 159) and compared only in Table 4 (efficiency) as achieving 0.921 AUROC_I on 10-shot. It is indeed absent from the main few-shot comparison in Table 1. This is a valid concern. KEEP as major.
-
-**Review of error bars (Claim 2):** The paper reports no variance across multiple trials. This is a valid concern for few-shot settings. KEEP as major.
-
-**Review of APR (Claim 3):** The paper provides theoretical justification but no empirical validation. The ablation shows APR is responsible for about 0.6% improvement, so this is not fatal. KEEP as minor.
-
-**Review of Real-IAD (Claim 4):** The paper clearly states these are full-shot results, and acknowledges D³M uses tri-modal data. Some claim over "cherry-picked" categories is overstated - the paper reports the full table. KEEP as minor - the comparison is less clean but this is supplementary evidence.
-
-Let me finalize.## Summary
-
-PIRN proposes a prototype-driven intra-modal reconstruction framework with cross-modal normality communication for few-shot multimodal anomaly detection. The core innovations are: (1) Balanced Prototype Assignment (BPA) using balanced optimal transport to prevent codebook collapse, (2) Adaptive Prototype Refinement (APR) for test-time prototype updates via GRU, and (3) Multimodal Normality Communication (MNC) that exchanges prototypical normality knowledge across RGB and surface-normal modalities. The method consistently outperforms baselines across MVTec-3D-AD, Eyecandies, and Real-IAD under 5/10/50-shot settings, while being 4.35× faster and using 85% fewer FLOPs than the recent SOTA FIND.
+This paper presents PIRN, a prototype-driven reconstruction framework for few-shot multimodal anomaly detection. It introduces three components: Balanced Prototype Assignment (BPA) using optimal transport to prevent codebook collapse, Adaptive Prototype Refinement (APR) for test-time adaptation to unseen normal variations, and Multimodal Normality Communication (MNC) for cross-modal knowledge exchange. The method is evaluated on MVTec-3D-AD, Eyecandies, and Real-IAD D3 across 5/10/50-shot and full-shot settings, achieving consistent improvements over baselines while being substantially more efficient (4.35× faster than FIND at comparable accuracy).
 
 ## Strengths
 
-1. **Consistent and substantial few-shot gains across multiple benchmarks**: Table 1 shows PIRN outperforms the strongest baseline on MVTec-3D-AD by +3.9 AUROC_I (5-shot), +3.7 (10-shot), and +2.4 (50-shot), and on Eyecandies by +3.6, +4.0, and +2.2 AUROC_I in the same settings. This is direct, replicated evidence that the method succeeds in data-scarce regimes where prior work degrades.
+- **Consistent few-shot gains across multiple benchmarks.** Table 1 shows PIRN outperforms the strongest baseline on MVTec-3D-AD by +3.7 AUROC\_I (10-shot) and +2.4 (50-shot); on Eyecandies by +4.0 and +2.2 in the same settings. The gains hold across shot levels and both datasets, providing direct evidence that the method succeeds in data-scarce regimes.
 
-2. **Ablation confirms all three innovations contribute independently**: Table 2 isolates BPA, APR, and MNC; removing each produces a measurable drop (e.g., removing APR drops AUROC_I from 0.922 to 0.883, removing MNC from 0.922 to 0.916), proving that balanced assignment, adaptive refinement, and cross-modal communication each play a distinct role in the reported gains.
+- **Component-wise ablation confirms all three innovations contribute.** Table 2 isolates BPA, APR, and MNC; removing each produces a measurable drop (e.g., removing APR drops AUROC\_I from 0.922 to 0.883, removing MNC drops to 0.916). This validates that balanced assignment, adaptive refinement, and cross-modal communication each independently contribute.
 
-3. **SOTA accuracy at drastically lower computational cost**: Table 4 shows PIRN achieves 0.922 AUROC_I with 103.36G FLOPs and 17.49ms latency, while FIND (0.921 AUROC_I) requires 728.46G FLOPs and 76.09ms — a 4.35× speedup and 85% fewer FLOPs. This convincingly demonstrates that strong few-shot AD performance does not require expensive architectures.
+- **SOTA accuracy at drastically lower cost.** Table 4 reports PIRN achieves 0.922 AUROC\_I with 103.36G FLOPs and 17.49ms latency, while FIND (0.921 AUROC\_I) requires 728.46G FLOPs and 76.09ms — a 4.35× speedup and 85% fewer FLOPs. This demonstrates that better few-shot MAD need not be more expensive.
 
-4. **Design-space validation via systematic ablations**: Tables 5 and 6 ablate codebook size K and decoder depth L across multiple shot settings. Optimal K=10 and L=2 are consistent, and performance degrades with too many/few prototypes (K=100 gives 0.901 AUROC_I vs. 0.963 at K=10), showing design choices are empirically grounded.
+- **Design-space validation via systematic ablations.** Tables 5 and 6 ablate codebook size K and decoder depth L across multiple settings; optimal choices (K=10, L=2) are consistent, and performance degrades with too few or too many prototypes/layers, showing design choices are empirically grounded.
 
-5. **Interpretable evidence of discriminative prototype encoding**: Figure 4 visualizes token displacements in PCA space and shows anomalous tokens undergo larger shifts than normal tokens during reconstruction, with clear separation in histograms — directly supporting the claim that prototypes act as normality anchors.
+- **Interpretable evidence of prototype-based normality encoding.** Figure 4 plots token displacements in PCA space and shows anomalous tokens undergo larger shifts than normal tokens during reconstruction, with histogram separation — directly supporting the claim that prototypes act as normality anchors.
 
 ## Weaknesses
 
 ### Major
 
-1. **Missing FIND baseline in the main few-shot comparison table.** FIND (Li et al., 2025) is cited for surface normal generation and compared in the efficiency table (Table 4), where it achieves 0.921 AUROC_I on the 10-shot MVTec-3D-AD setting — almost matching PIRN's 0.922. Yet FIND is absent from the main few-shot results in Table 1, where readers would naturally look for a comprehensive comparison. Given that the paper itself calls FIND "the recent SOTA," its omission from the primary comparison is a notable gap that weakens the central claim of "consistently superior performance."
+- **Missing SOTA baseline from main few-shot comparison.** FIND (Li et al., 2025) is cited for surface normal generation and compared in the efficiency table (Table 4) where it achieves 0.921 AUROC\_I on the 10-shot setting — nearly matching PIRN's 0.922. Yet FIND is absent from the main few-shot comparison table (Table 1). As FIND is explicitly described as "the recent SOTA" on MVTec-3D-AD, this omission weakens the paper's central claim of "consistently achieving superior performance." The authors should include FIND in Table 1 or explain why a fair comparison is infeasible.
 
-2. **No error bars or variance reporting for few-shot results.** The paper reports single-run results without standard deviations or confidence intervals. In few-shot anomaly detection, the specific training samples chosen can dramatically affect outcomes (Table 1 margins on pixel-level metrics are often 0.2–0.6% absolute). Without multiple seeds (at least 3), it is impossible to assess whether the reported improvements are statistically significant or within the noise of the sampling procedure.
+- **Lack of error bars for few-shot results.** Few-shot anomaly detection is known to be sensitive to which specific training samples are drawn. The paper reports no variance across random seeds or few-shot splits. Some margins over baselines are small (e.g., AUROC\_P differences of +0.002–0.006), making it impossible to assess statistical significance. Reporting mean and std over at least 3 random trials with different few-shot splits is standard practice and essential given these margins.
 
 ### Minor
 
-3. **The APR's robustness assumption is theoretically motivated but empirically unvalidated.** The paper argues that anomalous patches are assigned diffusely across prototypes via optimal transport and thus contribute weakly to the context vector. However, no experiment validates this claim — e.g., there is no analysis of what happens when anomalies span large contiguous regions or consist of subtle global shifts. The ablation (Table 2) does show that removing APR drops AUROC_I only from 0.922 to 0.916, meaning the core method does not collapse without it, but the paper would be strengthened by demonstrating empirically when the robustness assumption holds and when it breaks.
+- **APR's robustness assumption is unvalidated.** The paper argues that anomalous patches are assigned "diffusely" across prototypes during OT-based context extraction, contributing only weakly to prototype updates. This is a plausible theoretical claim, but no empirical analysis is provided (e.g., statistics on prototype update magnitudes for normal vs. anomalous inputs, or a synthetic experiment injecting known anomalies). The ablation ("wo APR") shows APR contributes ~0.6 AUROC\_I, so this is not fatal, but validating the claimed robustness mechanism would strengthen the paper.
 
-4. **Real-IAD D3 evaluation is supplementary but less cleanly controlled.** This experiment uses the full-data (not few-shot) setting and compares against D³M which employs a tri-modal representation (2D+Pseudo-3D+3D). There are no baselines using exactly the same inputs (RGB+surface normals) as PIRN. The paper acknowledges these differences, and this result is positioned as auxiliary evidence, but claims of "significantly outperforming" in specific categories should be tempered given the modality mismatch.
+- **Real-IAD comparison is supplementary but not perfectly controlled.** The Real-IAD D3 results use the full-data (not few-shot) setting and compare against D³M which uses tri-modal inputs (RGB+Pseudo-3D+3D) versus PIRN's dual-modal (RGB+surface normals). The paper acknowledges these differences, but the section would benefit from including baselines that use the same input modalities. The claim that PIRN "significantly outperforms D³M in specific categories" is cherry-picked from 2 out of 20 categories and should be contextualized.
+
+- **FIND could appear in more places.** Beyond the main table, the paper compares FIND only on the 10-shot setting in the efficiency table. Showing FIND's performance across all shot settings (5-shot, 50-shot) would strengthen the evaluation.
 
 ### Trivial
 
-None.
+- None of consequence.
 
 ## Nice-to-Haves
 
-- Include FIND and other recent SOTA methods in the main few-shot comparison table (Table 1), or explain why they cannot be fairly compared.
-- Add variance bars over at least 3 random few-shot splits for all main results.
-- Provide a synthetic experiment that measures context vector deviation from the true normal prototype when known anomalies of varying spatial extent are inserted into test images.
-- On Real-IAD, note the absence of same-modality baselines and frame the comparison as suggestive rather than conclusive.
-
-## Removed Points
-
-- **INP-Former baseline adaptation is unfair (from Harsh Critic)**: The critic claimed the two-stream adaptation "entirely discards INP-Former's core contribution: its test-time prototype extraction from the same image." This is factually incorrect. INP-Former's core mechanism — extracting intrinsic normal prototypes from a single test image — is preserved per modality in each independent stream. The two-stream architecture with element-wise fusion is the most natural and faithful adaptation of a 2D method to the multimodal setting. Adding cross-modal fusion (as the critic suggests) would give INP-Former capabilities it was never designed for and would be unfair in the opposite direction. **Removed: factually wrong.**
-
-- **"Paper should compare against a more thoughtful adaptation of INP-Former" (from Harsh Critic)**: As noted above, any adaptation with cross-modal fusion would deviate from INP-Former's original design. The paper's adaptation is already reasonable. **Removed: builds on factually incorrect premise.**
-
-- **"Table 8 is difficult to interpret due to missing metrics and incomplete baselines" (from Harsh Critic)**: Table 8 reports two standard metrics (AUROC_I/J and AUROC_P) for all methods, which is standard. The paper clearly states the modality differences. This is not a genuine weakness — it is an acknowledged limitation of the comparison. **Removed: problem is already addressed by the paper's own framing.**
-
-- **"Cherry-picked categories" on Real-IAD (from Harsh Critic)**: The paper reports the full table with all 20 categories, not selected ones. The text highlights a few examples as illustrations. This is standard practice, not cherry-picking. **Removed: mischaracterization.**
-
-- **"Clarification of training procedure" and "60 epochs may lead to overfitting" (from Harsh Critic)**: 60 epochs on 5–50 samples is not unusual for few-shot AD methods, and the paper achieves strong results without early stopping concerns being evident. This is speculative. **Removed: speculative.**
-
-- **Strength Finder's generic strengths**: Claims such as "the paper addressed an important problem" and "the motivation is clear" are generic and not specific to this paper. **Removed: generic.**
+- An ablation of the APR's inference-time adaptation with APR disabled at test time (comparing training-only vs. adaptive prototypes) is partially done in Table 2 but would benefit from a dedicated study across shot settings with error bars.
+- The paper could clarify whether early stopping or a validation split is used during few-shot training (60 epochs with 5-10 samples could lead to overfitting without monitoring).
 
 ## Novel Insights
 
-The key insight that emerges from reading the paper alongside the reviews is that PIRN's design successfully decouples the "what is normal" representation (learnable prototypes with balanced OT) from the "is this specific patch normal" decision (reconstruction error), while using cross-modal communication at the prototype level (rather than dense feature alignment). This design choice — exchanging high-level prototypical knowledge rather than raw features — is a principled way to avoid the brittleness of cross-modal alignment methods in data-scarce regimes. The paper also demonstrates a rarely-seen dual benefit: better performance at lower cost, because using a compact codebook of K=10 prototypes avoids the expensive memory bank lookups that methods like FIND require. The efficiency result (Table 4) is arguably as significant as the accuracy gains for practical deployment.
+None beyond the paper's own contributions.
 
 ## Suggestions
 
-- Add FIND (and any other recent SOTA multimodal AD methods) to the main few-shot comparison table. Report results under the same 5/10/50-shot splits.
-- Report mean and standard deviation over at least 3 random few-shot splits for all main results.
-- Add an experiment that directly measures APR's robustness: inject synthetic anomalies of varying size/intensity into test images and measure the deviation of the OT-derived context vector from the ground-truth normal prototype.
-- Add a brief discussion of when APR might fail (e.g., large-area anomalies, global color shifts) to acknowledge the limitation transparently.
-- For Real-IAD, either add baselines with the same input modalities or explicitly frame the comparison as indicative rather than directly competitive.
+1. Add FIND to the main few-shot comparison table (Table 1) across all shot settings, or justify its exclusion.
+2. Report mean and standard deviation over at least 3 random seeds for all few-shot results.
+3. Provide an empirical analysis of APR's robustness: e.g., measure context vector deviation when known anomalies are inserted, or compare prototype update magnitudes for normal vs. anomalous test samples.
 
 ## Score and Decision
 
-**Calibration procedure:**
+### Round-1 bracket
 
-**Round 1 (Bracketing):** Queried three bands on topics related to few-shot AD, prototype-based AD, and multimodal AD.
-- Weak band (score < 3.5): CLIP-LAD (3.00), Generalized AD (2.50) — clearly weaker than PIRN.
-- Mid band (3.5–7.5): PTAD (4.25), Prototype-oriented Fast Refinement (5.50), H-PAD (5.60), One-for-All Few-Shot AD (6.40), MMAD (6.50), AnomalyCLIP (6.17).
-- Strong band (score > 7.5): Deep Orthogonal Hypersphere (8.00), Test-time Adaptation (8.00) — clearly stronger than PIRN.
-- **Round 1 bracket: 5.0–7.0.**
+I first searched three score bands: weak anchors (avg < 3.5), middle anchors (3.5–7.5), and strong anchors (7.5+). The weak anchors (e.g., CLIP-LAD at 3.00, Generalized AD at 2.50) are clearly below PIRN. The middle anchors include closely related few-shot AD papers (prototype-oriented fast refinement at 5.50, One-for-All few-shot AD at 6.40). Strong anchors (8.00) are cleaner papers with minimal evaluation gaps. This bracketing placed PIRN between roughly 5.5 and 7.0.
 
-**Round 2 (Narrowing):** Queried within (4.5–6.0) and (6.0–7.5) on more specific topics.
-- Prototype-oriented Fast Refinement (5.50, reject) — PIRN is significantly stronger: more thorough evaluation, cleaner method, better efficiency analysis.
-- H-PAD (5.60, accept) — PIRN is stronger: larger-scale evaluation, better ablation, more novel methodology.
-- One-for-All Few-Shot AD (6.40, accept) — comparable quality: both have strong evaluations and clear contributions; One-for-All addresses a novel paradigm while PIRN addresses multimodality.
-- MMAD (6.50, accept) — benchmark paper, different contribution type.
-- AnomalyCLIP (6.17, accept) — comparable quality: both have clear contributions and thorough evaluations.
-- **Narrowed bracket: 5.5–6.5.**
+### Round-2 narrowing
 
-PIRN is clearly stronger than the 5.50 prototype refinement paper and comparable to the 6.0–6.5 papers. However, the missing FIND baseline in the main comparison table and the absence of error bars are evaluation gaps that prevent scoring at the top of this band. The paper's core technical contributions are novel, well-ablated, and produce consistent SOTA results with substantial efficiency gains.
+I then searched within the (4.5, 6.0) and (6.0, 7.5) bands for more topically similar anchors. Key comparisons:
+
+- **Prototype-oriented Fast Refinement (gTsLBDMZrL, 5.50, Reject):** Uses OT for prototype refinement in few-shot industrial AD. PIRN is clearly stronger — more thorough evaluation (3 datasets vs. 3), better ablation design, clearer writing, and addresses the harder multimodal setting.
+- **H-PAD (8TBGdH3t6a, 5.60, Accept):** Prototype-based time series AD. PIRN has more thorough evaluation and clearer motivation but both papers have comparable evaluation rigor.
+- **PTAD (Vi6p2TeujL, 4.25, Reject):** Prototype tabular AD. PIRN is substantially stronger in clarity, evaluation breadth, and result consistency.
+- **One-for-All Few-Shot AD (Zzs3JwknAY, 6.40, Accept):** Multi-class few-shot AD. PIRN has more comprehensive ablations and broader evaluation (3 datasets × multiple shots), though both have some evaluation gaps (missing baselines).
+
+### Final calibration
+
+PIRN is stronger than the 5.5-level papers and comparable to the 6.0–6.5 papers. The missing FIND baseline and lack of error bars are real weaknesses that prevent a higher score. A score of **6.0** reflects a solid paper with genuine contributions and a generally strong evaluation, held back by specific evaluation gaps that are addressable in revision. The core technical contributions (BPA via balanced OT, APR with gated GRU updates, MNC with prototype alignment) are novel and well-validated by the ablation study.
+
+### Anchors consulted
+
+| Anchor | Score | Round | Comparison to PIRN |
+|--------|-------|-------|-------------------|
+| bESxQeXTlo (CLIP-LAD) | 3.00 | 1 | Much weaker |
+| MbtUctg3KW (Gen. AD) | 2.50 | 1 | Much weaker |
+| O0vy7hHqyU (Fake News) | 3.00 | 1 | Different domain, weaker |
+| 3ZdGSTxKuy (Harry Potter) | 2.00 | 1 | Different domain, much weaker |
+| Vi6p2TeujL (PTAD) | 4.25 | 1 | Weaker method/evaluation |
+| gTsLBDMZrL (Proto. Refine.) | 5.50 | 1,2 | Weaker in evaluation breadth and method clarity |
+| J2we1sVd9m (Proto. OT OOD) | 4.60 | 1,2 | Different task, weaker |
+| 8TBGdH3t6a (H-PAD) | 5.60 | 1,2 | Comparable rigor, different domain |
+| 3P87ptzvTm (Multi OT) | 5.00 | 2 | Different task, less relevant |
+| 3WB5hT27zf (Partial OT) | 5.33 | 2 | Different task, less relevant |
+| Zzs3JwknAY (One-for-All) | 6.40 | 2 | Comparable strength, different paradigm |
+| JDiER86r8v (MMAD) | 6.50 | 2 | Different focus (benchmark, not method) |
+| buC4E91xZE (AnomalyCLIP) | 6.17 | 2 | Comparable strength, some evaluation gaps |
+| ybFRoGxZjs (ThermalGaussian) | 6.60 | 2 | Different domain, less relevant |
+| ENv1CeTwxc (Segment3D) | 6.50 | 2 | Different task, less relevant |
+| cJs4oE4m9Q (Orthogonal HS) | 8.00 | 1 | Stronger, cleaner evaluation |
+| TPZRq4FALB (Test-time Adapt) | 8.00 | 1 | Stronger, different task |
+| 9Cu8MRmhq2 (Norton) | 8.00 | 1 | Stronger, different domain |
 
 MY FINAL SCORE: <score>6.0</score>
 MY FINAL DECISION: <decision>Accept</decision>
```
