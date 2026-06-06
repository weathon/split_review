---

## Summary

ProteinVista is a 3D convolutional neural network that voxelizes full-atom protein structures at 1 Å resolution and is pre-trained on ~500,000 AlphaFold-2 structures via contrastive alignment to ESM-2 embeddings. The paper evaluates it on enzyme-substrate classification, transporter-substrate classification, and IC₅₀ regression, claiming that despite using orders of magnitude less compute and data than large protein language models, it matches or exceeds ESM-2 on structure-sensitive tasks, and that ensembling with ESM-2 further boosts performance. An open-source implementation is provided.

---

## Strengths

- **Compelling IC₅₀ regression improvement**: ProteinVista achieves R² = 0.69 vs. ESM-2₆₅₀ₘ's R² = 0.61 on BindingDB (Table 2), a 13% relative improvement backed by a highly significant Wilcoxon test (p < 10⁻³⁰⁴). This is the most convincing evidence that full-atom 3D geometry encodes drug-target affinity information that sequence transformers cannot recover.

- **Well-supported complementarity between sequence and structure**: The ESM-ProteinVista ensemble raises transporter-substrate accuracy from 89.3% to 91.5% (Table 1), with McNemar p < 10⁻¹³. Stratification by sequence identity and TM-score (Figure 2a–b) confirms this complementarity holds across all bins, strengthening the claim that structure adds orthogonal signal to sequence.

- **Substantial pre-training compute efficiency**: ProteinVista pre-trained in 48 GPU-hours (4× A100, 2 days) versus ~21,500 GPU-hours for ESM-2₆₅₀ₘ (128× H100, 7 days), using only ~0.5M structures versus 250M sequences. This is a genuine practical advantage documented concretely in Section 4.3.

- **Informative ablation and stratification studies**: Section 4.2 isolates the effect of multi-view inference (−6.4% R² with a single view), pre-training objective (Rosetta vs. contrastive: ~1% gap), and voxel resolution (1.5Å vs. 1.0Å: −1.1%). Figure 2 shows that ProteinVista is most advantageous at high sequence identity and high pLDDT, informatively scoping where the approach works best.

---

## Weaknesses

### Fatal
None.

### Major

- **Pre-training confound in the primary ESM-2 vs. ProteinVista comparison**: ProteinVista's contrastive pre-training objective explicitly pulls its structural embeddings toward ESM-2's sequence embeddings (Section 2.3, Figure 1d): "the loss encourages paired structure–sequence embeddings from the same protein to be close." The paper's central comparative claim — that 3D geometry outperforms sequence — therefore compares a model distilled from ESM-2 against ESM-2, not a purely structure-trained model against a sequence model. The ablation in Section 4.2 shows the Rosetta-pretrained variant (no ESM-2 signal) is only ~1% worse on IC₅₀, which partially mitigates the concern, but this variant is **never evaluated on TSP/ESP classification** or against the SOTA baselines in Table 1. The paper cannot establish that "3D geometry alone" outperforms sequences without this comparison, yet it repeatedly makes that claim (e.g., abstract: "full-atom 3D CNNs are…superior than protein transformers for structure-dependent tasks"). The core argument survives the ablation evidence on IC₅₀ but is unproven for classification.

- **Inference efficiency claims are inconsistent with 5-view multi-view averaging**: Section 4.3 states that ProteinVista "processes 1,000 proteins on one A100 GPU in 20 seconds during training" (also confirmed by Figure 3c caption: "training time to process 1,000 proteins"). However, Section 4.2 states that inference uses five randomly augmented views averaged together ("Reducing the ensemble to a single view lowered R² by 6.4%"). This means inference — the operationally relevant comparison for deployment — costs ~5× the training pass rate, yielding ~100 seconds per 1,000 proteins rather than 20 seconds. That shifts the claimed ~10× advantage over ESM-2₁₅₀ₘ (215 s) to roughly 2×. Compute efficiency is one of the three stated contributions, and the presented numbers apply to training throughput, not inference throughput.

### Minor

- **Abstract overclaims ensemble benefit**: The abstract states "A simple ensemble with ESM-2 can further improve accuracy," without qualification. Table 2 shows the ensemble **hurts** on IC₅₀ (R² 0.68 vs. 0.69 for ProteinVista alone). The ensemble helps on classification but harms affinity regression. The blanket abstract statement is inaccurate and should be qualified.

- **SOTA-beating margins are thin and lack statistical tests in Table 1**: ESM-ProteinVista_OP achieves 93.2% TSP accuracy vs. SPOT's 92.4% (0.8 pp), and 94.4% ESP accuracy vs. ProSmith-ESP's 94.2% (0.2 pp). Unlike the ESM vs. ensemble comparison (which correctly applies McNemar's test), no statistical test is reported for these SOTA comparisons. Given the small margins, the claim of beating state-of-the-art should be stated more cautiously.

- **BindingDB train/test split methodology is not described**: For IC₅₀ regression from BindingDB (Section 3.2), the splitting strategy is not mentioned in the main text. If multiple ligands for the same target span train and test sets, the task partly reflects protein-family affinity range memory rather than generalizable pocket recognition. Even if addressed in the (stripped) appendix, briefly stating the split strategy in the main text is important for interpreting the headline IC₅₀ result.

### Trivial

- **"Rotational invariance" is an overstatement**: Section 2.4 uses the phrase "enforce rotational invariance" for what is actually augmentation over 90° rotations and mirror reflections (the 48-element octahedral symmetry group), with five random views averaged at inference. This is rotational robustness via discrete augmentation, not true SO(3) invariance. A more precise phrase would be "rotation robustness via augmentation over a discrete symmetry group."

---

## Nice-to-Haves

- Report the Rosetta-pretrained variant across all benchmarks (TSP, ESP, IC₅₀) in a single table. Even if it closes only half the gap with ESM-2, it would substantially strengthen the core claim that 3D geometry provides structural signal independent of ESM-2 distillation.
- Report inference-time throughput (5-view) alongside training throughput in Figure 3c, and clarify the distinction in the text. This gives practitioners accurate deployment cost estimates.
- Analyze IC₅₀ performance broken down by protein family or pLDDT confidence (as done for TSP in Figure 2c) to check whether the advantage is broadly distributed or concentrated in well-predicted targets.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Density formula garbled equation (Harsh Critic, Section 2.3)**: The expression "$\vec{v} = \exp(-\|\vec{v} - \vec{r}\|/\sigma^2)$" is a PDF parser rendering artifact where the voxel index symbol and the density value overlap. Per the review rules, formatting artifacts from PDF extraction are not author errors and should not be penalized.

- **High-identity "template matching" alternative interpretation (Harsh Critic, Section 4.1)**: The suggestion that ProteinVista at high sequence identity may be doing "template-based feature matching" rather than learning generalizable binding geometry is speculative and not supported by a specific analysis in the paper. The pattern is just as consistent with the structural encoder correctly capturing subtle geometry shared among homologs. Removed as a speculative concern.

- **Strength: "marks an important problem" level framing**: The Strength Finder's generic framing around the importance of protein function prediction as a motivation has been stripped; only concrete, evidence-backed strengths were retained above.

---

## Novel Insights

The most genuinely novel observation arising from the analysis is the *decoupling of pre-training efficiency from downstream performance*: ProteinVista was trained on ~1% of the GPU-hours of ESM-2₆₅₀ₘ yet matches or exceeds it on binding tasks, suggesting that structural information from AlphaFold-2 structures is a highly compressed and information-dense substrate for pre-training. The ablation further reveals that multi-view test-time aggregation (not fine-tuning augmentation) is the operative mechanism for orientation robustness — rotation invariance is largely learned during pre-training and persists through fine-tuning, with the 5-view averaging acting as structured uncertainty reduction at inference. This insight has practical relevance for future 3D protein encoders.

---

## Suggestions

1. **Run the Rosetta-pretrained variant on TSP and ESP benchmarks** and include it as a separate row in Table 1. This single experiment would directly substantiate (or narrow) the "3D geometry outperforms sequence" claim without the pre-training confound.
2. **Report 5-view inference throughput** in Figure 3c alongside the training throughput figure, with a clear label distinguishing the two regimes.
3. **Qualify the abstract's ensemble claim**: Change "A simple ensemble with ESM-2 can further improve accuracy" to "A simple ensemble with ESM-2 improves accuracy on classification tasks, while detailed affinity regression relies primarily on structural embeddings."
4. **Add McNemar's test (or equivalent)** for the ESM-ProteinVista_OP vs. SPOT/ProSmith-ESP/Fusion_ESP comparisons in Table 1.
5. **State BindingDB split strategy** (protein-level or random) in Section 3.2.

---

## Assessment

**Originality**: High — applying full-atom 3D CNNs to protein-scale pre-training with contrastive alignment to PLMs is a novel design not previously demonstrated at this scale. The use of adaptive voxel boxing is a practical contribution.

**Importance**: High — structure-dependent protein-ligand prediction underpins drug discovery; showing that 3D CNNs are tractable and competitive addresses a real open question.

**Claims supported**: Moderate — the IC₅₀ result is strongly supported; the classification results are solid but the "3D geometry alone outperforms sequence" framing is not cleanly established given the ESM-2 pre-training entanglement. The efficiency claim needs to distinguish training vs. inference throughput.

**Soundness**: Moderate-to-good — the experimental design is careful (identical fine-tuning conditions, McNemar's tests, ablations), but the two major issues (pre-training confound, inference-time reporting) require correction.

**Clarity**: Good with notable exceptions — Table 1 and 2 are clearly organized, but the abstract contains an inaccurate blanket claim and Section 4.3 conflates training and inference throughput.

**Community value**: High — the open-source implementation and practical demonstration that 3D CNNs are viable for large-scale protein benchmarks will be useful to the community.

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>