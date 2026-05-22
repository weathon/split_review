Now I'll construct the final consolidated review.

## Summary

This paper presents ProteinVista, a 3D CNN that voxelizes full atomic protein structures at 1Å resolution and is pre-trained contrastively against ESM-2 embeddings on ~500K AlphaFold2 structures. Despite 5× fewer parameters than ESM-2₆₅₀M and roughly 1% of its pre-training GPU-hours, ProteinVista achieves an R² of 0.69 on BindingDB IC₅₀ prediction (vs. 0.61 for ESM-2₆₅₀M, p < 10⁻³⁰⁴), matches or slightly exceeds ESM-2 on transporter/enzyme substrate classification, and shows consistent complementarity when ensembled with ESM-2.

## Strengths

- **Strong IC₅₀ regression result with statistical significance.** On BindingDB (Table 2), ProteinVista (123M params, 500K pre-training examples) achieves R² = 0.69 vs. ESM-2₆₅₀M's 0.61 (650M params, ~250M sequences). A one-sided Wilcoxon signed-rank test confirms p < 10⁻³⁰⁴. This is the paper's cleanest evidence that a full-atom 3D CNN outperforms sequence transformers on a task requiring fine structural detail.

- **Dramatic pre-training efficiency.** Section 4.3 and Figure 3 report ProteinVista finished pre-training in 48 hours on 4 A100 GPUs (~500K structures) versus ~7 days on 128 H100 GPUs for ESM-2₆₅₀M (~250M sequences). This represents roughly 1% of the GPU-hours, using over two orders of magnitude less data — a practically useful trade-off for many labs.

- **Proven complementarity with sequence models.** The ESM-ProteinVista ensemble (simple prediction averaging) consistently improves over either model alone across all classification metrics (Table 1), with McNemar's tests yielding p < 10⁻¹³ (TSP) and p < 10⁻¹⁷ (ESP). The similarity binning analysis (Section 4.1, Figure 2a–c) further shows that the ensemble outperforms both single models in every bin of sequence identity, TM-score, and pLDDT, providing robust evidence that structure and sequence signals are genuinely non-redundant.

- **Informative similarity analysis and ablation studies.** The stratification by sequence identity, TM-score, and pLDDT (Section 4.1) gives practical insight into when structure-based models help most. The ablation study (Section 4.2) cleanly quantifies the importance of multi-view inference (6.4% R² drop with 1 view), contrastive vs. Rosetta pre-training (1.0% difference), and voxel resolution (1.1% drop at 1.5Å).

## Weaknesses

### Fatal
None.

### Major

- **Pre-training / test set overlap is not analyzed, leaving the main comparisons partially unguarded.** ProteinVista is pre-trained on >500K AlphaFold2-predicted structures from Swiss-Prot. The downstream test sets (TSP, ESP, BindingDB) involve proteins that plausibly appear in Swiss-Prot and therefore could also appear in the pre-training set. The paper reports no sequence or structural identity analysis between pre-training data and test sets, nor does it run a controlled experiment excluding overlapping proteins. The similarity binning analysis in Section 4.1 concerns the *training* set of the downstream tasks, not the pre-training set, so it does not address this. While pre-training overlap is unlikely to fully explain the results (pre-training is unsupervised contrastive, not supervised on the downstream tasks; and ESM-2's pre-training data has comparable or greater overlap potential), the missing analysis is a gap that the authors should close.

- **The SOTA comparison (Section 3.3) is an ensemble that includes ESM-2, and the single-model comparison to specialized methods is not evaluated fairly.** The "optimized pipeline" (ESM-ProteinVista_OP) achieves 93.2%/94.4% accuracy on TSP/ESP by combining ProteinVista *and* ESM-2₂ with a contrastive network and joint molecule embedding updates, surpassing SPOT (92.4%) and ProSmith-ESP (94.2%). From Table 1, ProteinVista alone (90.8% TSP, 91.8% ESP) is *worse* than both SPOT (92.4%) and ProSmith-ESP (94.2%). The paper is transparent about this (the ensemble is called "ESM-ProteinVista_OP"), but the framing in Section 3.3 ("surpasses the current best models") and the abstract ("outperforms sequence transformers") could mislead a casual reader into conflating the standalone and ensemble results. The strongest standalone claim — outperforming sequence transformers — is well-supported for IC50 but more marginal for classification.

### Minor

- **No significance tests for single-model classification comparisons.** On TSP, ProteinVista's accuracy (90.8%) exceeds ESM-2₆₅₀M (89.3%). On ESP, they are essentially tied (91.8% vs. 91.9%). The paper reports McNemar tests only for the *ensemble* vs. ESM-2, not for ProteinVista alone vs. ESM-2. Given the small margins, significance tests or confidence intervals would strengthen the single-model claim for classification tasks.

- **Which ESM-2 variant was used for contrastive pre-training is not specified.** Section 2.3 says ESM-2 embeddings are used as targets for the InfoNCE loss, but the variant (150M? 650M? 3B?) is not stated. This matters because the quality of the target embeddings could affect the pre-training quality.

- **The 5-ensemble inference cost is not factored into the efficiency claims.** Section 4.3 reports inference time as "20s for 1,000 proteins on an A100," but inference actually requires 5 forward passes (five augmented views). The reported number appears to be per pass. The 5× multiplier should be acknowledged when comparing runtime to ESM-2 (which does not require multiple views).

- **No results or baselines for the GO prediction task from the structure-model literature.** Section 3.4 shows ProteinVista underperforms ESM-2 on GO term prediction (Fmax 0.57 vs. 0.62), which is consistent with the paper's narrative. However, comparing against other structure-based methods (e.g., GearNet) on this task would help contextualize whether the underperformance is specific to this architecture or general to structure-based models.

### Trivial
- The formula for Gaussian density in Section 2.1 writes `exp(-||v - r|| / σ²)` but the arguments suggest the exponent should be `||v - r||² / σ²`. The units and normalization of the density contribution per voxel are not stated.
- The paper says "23 Rosetta scores" in Section 2.3 but "33 Rosetta scores" in the Discussion (Section 5). This discrepancy should be reconciled.

## Nice-to-Haves
- A self-supervised 3D pre-training objective (masked voxel prediction, rotation prediction) could more directly enforce geometric learning and better align with the paper's motivation. The paper already acknowledges this in the Discussion, but a preliminary experiment would strengthen the narrative.
- Reporting the batch size and computational details (framework, precision, batch sizes) for all experiments would aid reproducibility.

## Removed Points

These points were identified by reviewers but are being moved here — treat with caution:

- **"Contrastive pre-training is conceptually inconsistent with capturing structure-specific information"** (Harsh Critic Critical Issue 3): This is a philosophical concern, not a demonstrated flaw. The ablation shows Rosetta pre-training yields similar performance (-1.0% R²), and the ensemble still improves over either model alone, demonstrating that the contrastive objective does not eliminate complementarity. The paper also acknowledges alternative objectives. Removed because it is speculative and not supported by the evidence on the page.

- **"Missing detailed voxelization implementation questions (how atoms are assigned when multiple map to same voxel)"**: Standard practice for continuous density representations — each atom contributes to its own channel, and contributions within the same channel are additive. Not a meaningful weakness.

- **"Parameter count not broken down by block"**: Not necessary; the total count is given and the architecture is described clearly enough for reproduction.

- **"Missing appendix / supplementary content / proofs"**: The PDF parser strips these sections from all papers; they exist in the original submission.

- **"Reproducibility nitpicks about undisclosed hyperparameters or training details"**: The paper searches for optimal learning rates and reports early stopping; this is a reasonable level of detail for this type of work.

- **"Formatting, typo, grammar, and presentation style nitpicks"**: Parser artifacts, not author errors.

- **Generic strength finder claims about "addressing an important problem"** dropped as too generic.

## Novel Insights

None beyond the paper's own contributions. The insight that a 3D CNN using ~1% of the pre-training resources of a large PLM can outperform it on a binding affinity regression task while providing complementary signals on classification tasks is useful and well-documented, but the reviews do not surface a qualitatively new observation beyond what the paper itself provides.

## Suggestions

1. **Analyze pre-training / test set overlap.** Report sequence identity and UniProt accession overlap between the 500K Swiss-Prot pre-training set and each downstream test set. If nontrivial overlap exists, run a controlled experiment (exclude overlapping proteins and re-fine-tune) to confirm the performance gap is not driven by pre-training leakage.

2. **Add significance tests for the single-model comparisons** on TSP and ESP (e.g., McNemar's test or bootstrapped confidence intervals for accuracy differences). This would clarify whether the small observed gaps on classification tasks are reliable.

3. **Separate the standalone and ensemble results more explicitly in the framing.** The abstract and introduction should note that the SOTA comparison (Section 3.3) is an ensemble method, and the standalone results already beat ESM-2 on IC50 while being competitive on classification.

4. **Specify the ESM-2 variant used for contrastive pre-training** and report the batch size used for the InfoNCE loss.

5. **Acknowledge the 5-view inference multiplier** when reporting runtime efficiency.

Now let me compute the score relative to anchors.

Anchors from calibration search:
1. **FoldFlow** (avg 8.00) — Exceptional paper with strong theory + experiments. ProteinVista is less novel methodologically and has weaker evaluation rigor in some dimensions. → ProteinVista scores lower.
2. **AtomSurf** (avg 6.75) — Solid structural representation paper with clear experiments and honest benchmark comparisons. ProteinVista is comparable in quality but has one more significant gap (pre-training overlap). → Slightly lower.
3. **ProteinWorkshop** (avg 6.25) — Benchmark paper with clear contribution. ProteinVista has a stronger original method contribution but more evaluation gaps. → Comparable.
4. **ProteiNexus** (avg 3.67) — Rejected with novelty and data leakage issues. ProteinVista is substantially stronger: cleaner experiments, better-motivated architecture, and no evidence of significant data leakage (only missing the analysis). → Much higher.
5. **DTI-DA** (avg 2.50) — Nonsensical/pseudoscientific paper. ProteinVista is in a completely different league. → Far higher.

Other anchors (not read in full):
- **BEH4mGo7zP** (avg 5.75) — Protein structure/surface pre-training. ProteinVista has stronger efficiency claims. → Slightly higher.
- **iBAWiEjogY** (avg 3.67) — Already discussed as ProteiNexus.
- **xcMmebCT7s** (avg 5.80) — PPI design. Different task. Comparable quality.
- **ZuU4mZILBB** (avg 4.38) — Docking benchmark critique. Different paper type.
- **AXbN2qMNiW** (avg 5.67) — Binding representation learning. Comparable.
- **zDC3iCBxJb** (avg 6.75) — Group docking. Strong method. ProteinVista is slightly lower due to the overlap gap.
- **xNDydjYBmC** (avg 4.60) — PPB affinity prediction with data integration. Slightly lower quality. ProteinVista is stronger.
- **wRkfniZIBl** (avg 4.33) — RNA contrastive learning. Different domain.
- **ZlEtXIxl3q** (avg 6.00) — Contrastive losses for epistasis. Different domain but similar quality level.
- **hiciJQdmpw** (avg 4.75) — Protein design with flows. Different domain.
- **760br3YEtY** (avg 5.60) — Enzyme promiscuity prediction. Different domain but similar quality tier.
- **gHLWTzKiZV** (avg 8.00) — Protein docking with flow matching. Stronger than ProteinVista.
- **0ctvBgKFgc** (avg 8.00) — Protein structure generation. Stronger.
- **zMPHKOmQNb** (avg 8.00) — Protein generation with discrete sampling. Stronger.
- **GDDqq0w6rs** (avg 4.75) — Gene property benchmark. Different topic.
- **8pYNdmwGAO** (avg 4.00) — Mutation effect prediction. Lower quality than ProteinVista.
- **Et0SIGDpP5** (avg 4.25) — Long-context protein LM. Lower quality.
- **ZyAwBqJ9aP** (avg 2.00) — CYP prediction. Significantly lower quality.
- **IEZjjDX0iC** (avg 3.00) — Comparing PLMs for phages. Lower quality.
- **1S8ndwxMts** (avg 3.00) — Evaluation metrics for protein generative models. Different topic.

Based on this calibration, ProteinVista is clearly stronger than papers in the 2-5 range, comparable to papers in the 5.5-6.5 range, and weaker than the 8.0 papers. I'll place it at 6.0.

Score: 6.0
Decision: Accept

This paper has a genuine contribution (compute-efficient 3D CNN that works and complements sequence models), strong evidence on the IC50 task, compelling efficiency data, and informative analysis. The main gap (pre-training overlap analysis) is a reasonable request that can be addressed in a rebuttal but does not invalidate the core findings.## Summary

This paper introduces ProteinVista, a 3D CNN that voxelizes full-atom protein structures at 1Å resolution and is pre-trained contrastively against ESM-2 embeddings on ~500K AlphaFold2 structures. Despite 5× fewer parameters and roughly 1% of the pre-training GPU-hours, ProteinVista achieves an R² of 0.69 on BindingDB IC₅₀ prediction (vs. 0.61 for ESM-2₆₅₀M, p < 10⁻³⁰⁴), matches or slightly exceeds ESM-2 on transporter/enzyme substrate classification, and provides complementary information when ensembled with ESM-2 — demonstrating that a carefully designed 3D CNN can be both compute-efficient and structurally informative.

## Strengths

- **Strong IC₅₀ regression result with statistical significance.** On BindingDB (Table 2), ProteinVista (123M params, ~500K pre-training examples) achieves R² = 0.69 vs. ESM-2₆₅₀M's 0.61 (650M params, ~250M sequences). A one-sided Wilcoxon signed-rank test confirms p < 10⁻³⁰⁴. This is the paper's strongest and cleanest evidence that a full-atom 3D CNN can outperform sequence transformers on a task requiring fine structural detail.

- **Dramatic pre-training efficiency.** Section 4.3 reports ProteinVista finished pre-training in 48 hours on 4 A100 GPUs (500K structures) versus ~7 days on 128 H100 GPUs for ESM-2₆₅₀M (250M sequences). This represents roughly 1% of the GPU-hours, using over two orders of magnitude less data.

- **Proven complementarity with sequence models across similarity regimes.** The ESM-ProteinVista ensemble consistently improves over either model alone across all classification metrics (Table 1), with McNemar's tests yielding p < 10⁻¹³ (TSP) and p < 10⁻¹⁷ (ESP). The similarity binning analysis (Section 4.1, Figure 2a–c) further shows the ensemble outperforms both single models in every bin of sequence identity, TM-score, and pLDDT — strong evidence that sequence and structure signals are genuinely non-redundant.

- **Informative similarity analysis and ablation studies.** The stratification by sequence identity, TM-score, and pLDDT (Section 4.1) gives practical insight into when structure-based models help. The ablation (Section 4.2) cleanly quantifies the importance of multi-view inference (6.4% R² drop with 1 view), contrastive vs. Rosetta pre-training (1.0% difference), and voxel resolution (1.1% drop at 1.5Å).

- **Adaptive boxing design minimizes memory waste.** Section 2.1 embeds each protein in the smallest of four cubic grids (64³, 96³, 128³, or 160³ voxels), directly addressing a known limitation of prior 3D CNN approaches for proteins.

## Weaknesses

### Fatal
None.

### Major

- **Pre-training / test set overlap is not analyzed.** ProteinVista is pre-trained on >500K AlphaFold2-predicted structures from Swiss-Prot. The downstream test sets (TSP, ESP, BindingDB) involve proteins that plausibly appear in Swiss-Prot and therefore could also appear in the pre-training set. The paper reports no sequence or structural identity analysis between pre-training data and test sets, nor does it run a controlled experiment excluding overlapping proteins. The similarity binning analysis in Section 4.1 concerns the *training* set of the downstream tasks, not the pre-training set. While pre-training overlap is unlikely to fully explain the results (pre-training is unsupervised contrastive, not supervised on the downstream tasks), the missing analysis is a gap the authors should close to fully establish their core empirical contributions.

- **The state-of-the-art comparison uses an ensemble that includes ESM-2, while the standalone model is weaker than specialized methods.** ESM-ProteinVista_OP (Section 3.3) combines ProteinVista *and* ESM-2₂ with a contrastive network and joint molecule embedding updates, achieving 93.2% TSP / 94.4% ESP (surpassing SPOT's 92.4% and ProSmith-ESP's 94.2%). However, ProteinVista alone (90.8% TSP, 91.8% ESP) is *worse* than both SPOT (92.4%) and ProSmith-ESP (94.2%). The paper is transparent about the ensemble construction, but the framing in the abstract ("outperforms sequence transformers") and Section 3.3 risks conflating the standalone and ensemble results. The standalone claim is strongly supported for IC50 but substantially weaker for classification.

### Minor

- **No significance tests for single-model classification comparisons.** On TSP, ProteinVista (90.8%) exceeds ESM-2₆₅₀M (89.3%). On ESP, they are essentially tied (91.8% vs. 91.9%). The paper reports McNemar tests only for the *ensemble* vs. ESM-2, not for ProteinVista alone vs. ESM-2. Given the small margins, significance tests would strengthen the single-model classification claims.

- **Which ESM-2 variant was used as the target for contrastive pre-training is not specified.** Section 2.3 does not state whether it was the 150M, 650M, or 3B-parameter variant. This affects interpretation of what quality of representation is being distilled.

- **The 5-view inference cost is not factored into runtime efficiency claims.** Section 4.3 reports "20s to process 1,000 proteins on an A100," but inference averages predictions from five randomly augmented views. If this is per-pass rather than per-protein, the actual per-protein inference time is 5× higher. This should be acknowledged when comparing to ESM-2 (which does not require multiple views).

- **GO prediction lacks structure-based baselines.** Section 3.4 shows ProteinVista underperforms ESM-2 on GO term prediction (Fmax 0.57 vs. 0.62). Comparing against other structure-based methods (e.g., GearNet) on this task would help distinguish whether the underperformance is general to structure-aware models or specific to this architecture.

### Trivial

- The Gaussian density formula in Section 2.1 writes `exp(-||v - r|| / σ²)`, but from context the exponent should be `||v - r||² / σ²`. The units and normalization of the density contribution are not stated.
- Section 2.3 says "23 Rosetta scores" but the Discussion says "33 Rosetta scores." This discrepancy should be reconciled.

## Nice-to-Haves

- A self-supervised 3D pre-training objective (masked voxel prediction, rotation prediction) could more directly enforce geometric learning. The paper already acknowledges this in the Discussion, but a preliminary experiment would strengthen the narrative.
- Batch size and additional training infrastructure details (framework version, precision) would aid reproducibility.

## Removed Points

These points were flagged by reviewers but are being moved here with justification:

- **"Contrastive pre-training is conceptually inconsistent with capturing structure-specific information"** (Harsh Critic Critical Issue 3): This is a philosophical concern, not a demonstrated flaw. The Rosetta pre-training ablation yields similar performance (-1.0% R²), and the ensemble still improves over either model alone, showing complementarity is preserved. The paper also explicitly discusses alternative objectives. *Removed because it is speculative and contradicted by evidence on the page.*

- **"Missing detailed voxelization implementation questions"** (e.g., how atoms are assigned when multiple map to same voxel): Continuous density representations sum contributions within each channel — this is standard practice. *Removed as a trivial implementation detail.*

- **"Parameter count not broken down by block"**: The total is given and the architecture description (5 blocks, specified kernel sizes and channels) is sufficient. *Removed as unnecessary nitpick.*

- **"Missing appendix / supplementary content / proofs"**: The PDF parser strips these sections from all ICLR submissions. *Removed — they exist in the original.*

- **Formatting, typo, grammar, and presentation nitpicks**: Parser artifacts, not author errors. *Removed per hard rules.*

- **Reproducibility nitpicks about undisclosed hyperparameters or training details**: The paper reports learning rate search and early stopping; this is a reasonable level of detail for this type of work. *Removed.*

- **Strength Finder generic claims** (e.g., "addresses an important problem"): Dropped as lacking concrete, paper-specific content.

## Novel Insights

None beyond the paper's own contributions. The observation that a 3D CNN can match or exceed a much larger PLM on structure-dependent binding tasks while using ~1% of the pre-training resources is well-documented, but the reviews do not surface a qualitatively new insight beyond what the paper itself provides.

## Suggestions

1. **Analyze pre-training / test set overlap.** Report sequence identity and UniProt accession overlap between the 500K Swiss-Prot pre-training set and each downstream test set. If nontrivial overlap exists, run a controlled experiment (exclude overlapping proteins and re-fine-tune) to confirm the performance gap is not driven by pre-training leakage.

2. **Add significance tests for the single-model classification comparisons** on TSP and ESP (e.g., McNemar's test or bootstrapped confidence intervals). This would clarify whether the small observed differences are reliable.

3. **Separate standalone and ensemble claims more explicitly.** The abstract and introduction should note that the SOTA comparison in Section 3.3 is an ensemble that includes ESM-2, while the standalone results beat ESM-2 on IC50 and are competitive on classification.

4. **Specify the ESM-2 variant used for contrastive pre-training** and report the InfoNCE batch size.

5. **Acknowledge the 5-view inference multiplier** when reporting runtime (Section 4.3) so that efficiency comparisons to models that do not require multiple views are accurate.

---

## Score and Decision

### Calibration Anchors

**High-scoring anchors (avg ≥ 6):**
- **FoldFlow** (`kJFIH23hXb`, avg 8.00) — Strong theoretical + empirical contribution to protein backbone generation. ProteinVista has a weaker theoretical component and one significant evaluation gap (overlap analysis), placing it below this tier.
- **AtomSurf** (`ARQIJXFcTH`, avg 6.75) — Solid structural representation paper with honest benchmarking. ProteinVista is comparable in quality but has one more evaluation gap → slightly lower.
- **ProteinWorkshop** (`sTYuRVrdK3`, avg 6.25) — Benchmark paper with clear contribution. ProteinVista has a stronger method contribution but more evaluation gaps → comparable.
- **GroupBind** (`zDC3iCBxJb`, avg 6.75) — Strong docking method. ProteinVista is slightly lower.

**Medium-scoring anchors (avg 3.5 – 6.0):**
- **BEH4mGo7zP** (avg 5.75) — Protein surface/structure pre-training. ProteinVista has stronger efficiency claims → slightly higher.
- **xcMmebCT7s** (avg 5.80) — PPI design. Comparable quality.
- **AXbN2qMNiW** (avg 5.67) — Binding representation learning. Comparable.
- **760br3YEtY** (avg 5.60) — Enzyme promiscuity prediction. Comparable quality tier.
- **ZlEtXIxl3q** (avg 6.00) — Contrastive losses for epistasis. Similar quality level.
- **xNDydjYBmC** (avg 4.60) — PPB affinity prediction. ProteinVista is stronger.

**Low-scoring anchors (avg ≤ 3.5):**
- **ProteiNexus** (`iBAWiEjogY`, avg 3.67) — Rejected due to data leakage and novelty concerns. ProteinVista is substantially stronger: cleaner experiments, better-motivated architecture, no evidence of data leakage (only missing the analysis).
- **DTI-DA** (`i3f2N3iHl0`, avg 2.50) — Nonsensical paper. ProteinVista is in a completely different league.
- **ZyAwBqJ9aP** (avg 2.00) — CYP substrate prediction. Significantly lower quality.
- **8pYNdmwGAO** (avg 4.00) — Mutation effect prediction. Lower quality.

**Additional anchors returned:**
- **gHLWTzKiZV** (avg 8.00) — Flexible docking. Stronger than ProteinVista.
- **0ctvBgKFgc** (avg 8.00) — Protein structure generation. Stronger.
- **zMPHKOmQNb** (avg 8.00) — Protein generative model. Stronger.
- **ZuU4mZILBB** (avg 4.38) — Docking benchmark critique. Different paper type.
- **GDDqq0w6rs** (avg 4.75) — Gene property benchmark. Different topic.
- **Et0SIGDpP5** (avg 4.25) — Long-context protein LM. Lower quality.
- **IEZjjDX0iC** (avg 3.00) — Comparing PLMs for phages. Lower quality.
- **1S8ndwxMts** (avg 3.00) — Metrics for protein generative models. Different topic.

**Score position:** ProteinVista is clearly stronger than papers in the 2–5 range, comparable to papers in the 5.5–6.5 range, and weaker than the top-tier theory+experiment papers (8.0). The main contribution is genuine and well-supported on the IC50 task with compelling efficiency data. The primary gaps (overlap analysis, single-model classification significance) are addressable in revision rather than fatal.

**Score: 6.0** — A solid paper with a real contribution that is weakened by one significant empirical gap (pre-training overlap) and some minor evaluation issues. The core claims about compute efficiency and complementarity are well-supported; the claims about outperforming sequence transformers are strongly supported for IC50 regression and modestly supported for classification.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>