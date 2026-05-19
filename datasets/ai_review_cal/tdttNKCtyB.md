- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5
Now I have thoroughly read and analyzed the paper. Let me construct the final consolidated review by carefully verifying each claim against the paper content.

---

## Summary

ROSE proposes a lightweight pre-trained time series foundation model with two key innovations: (1) Decomposed Frequency Learning, which applies multiple random low/high-frequency masks via FFT to decouple coupled temporal patterns for generalized representation learning, and (2) a Time Series Register (TS-Register), a learnable codebook that clusters domain-specific information during pre-training and enables adaptive transfer to downstream tasks via Top-K selection and low-rank fine-tuning. After pre-training on ~887M time points across diverse domains, ROSE achieves SOTA full-shot results across all 7 benchmarks, competitive few-shot performance (within ~1-2% of full-data baselines using only 10% data), and strong zero-shot results against larger foundation models, with only 7.4M parameters.

---

## Strengths

1. **Consistent state-of-the-art across all full-shot benchmarks.** Table 1 (lines 214-228) shows ROSE achieving the lowest MSE on all 7 datasets (ETTh1, ETTh2, ETTm1, ETTm2, Weather, Electricity, Traffic), with non-trivial margins on several (e.g., ETTh1: 0.391 vs next-best 0.406; Electricity: 0.155 vs 0.159). On ETTh2, ROSE ties with PatchTST at 0.331. This is a clean sweep.

2. **Few-shot performance competitive with full-data baselines.** ROSE fine-tuned with only 10% of training data (Table 1, "ROSE (10%)") achieves MSE within 0.006 of the best full-data baseline on 5 of 7 datasets. On ETTh2, ROSE (10%) at 0.335 actually beats all full-shot baselines except PatchTST's 0.331. Figure 2 (described in line 239) shows pre-trained ROSE surpasses full-shot SOTA with just 1-2% training data on ETTh1 and ETTm2.

3. **Strong zero-shot performance with dramatically smaller model size.** Table 2 shows ROSE achieves best MSE on 6 of 7 zero-shot datasets (all except ETTm1, where TimesFM wins), while having only 7.4M parameters and millisecond inference — roughly 1/10th the size and speed of the next smallest foundation model (Timer). This demonstrates that strong generalization does not require massive scaling.

4. **Ablation studies confirm each component's contribution.** Table 3 (lines 308-322) systematically ablates TS-Register, prediction task, reconstruction task, and masking strategies. Removing TS-Register degrades MSE on all 4 ETT subsets (e.g., ETTh1: 0.397 → 0.418). Removing the prediction task hurts ETTh2 substantially (0.335 → 0.372). Multi-frequency masking consistently outperforms single-frequency and time-domain alternatives. The "From Scratch" row (0.370-0.470 MSE) demonstrates that pre-training provides significant gains over training the same architecture from scratch.

5. **TS-Register visualization shows domain-aware selection.** Figure 5 (described in lines 285-289) demonstrates that datasets from the same domain (e.g., ETT subsets) select similar register vectors, while different domains select distinct vectors, empirically validating that the register captures meaningful domain structure.

---

## Weaknesses

### Fatal
None.

### Major

1. **TS-Register training mechanism is underspecified and potentially incorrect.** The register loss (Equation 7, line 140) is defined as $\|\mathbf{x}_e - \mathbf{e}_\delta\|^2_2$ with $\delta = \arg\min_j \|\mathbf{x}_e - \mathbf{e}_j\|_2$. The paper states (line 144): "use the stop gradient operation to pass the gradient of $\mathbf{e}_\delta$ directly to $\mathbf{x}_e$." This description is incoherent. In a standard VQ-VAE-style codebook, you would either (a) use a commitment loss with stop-gradient on $\mathbf{x}_e$ to pull $\mathbf{e}_\delta$ toward $\mathbf{x}_e$, or (b) use EMA to update codebook vectors. The paper's formulation — minimizing $\|\mathbf{x}_e - \mathbf{e}_\delta\|^2$ with stop-gradient applied such that gradient flows only to $\mathbf{x}_e$ — would never update the codebook vectors $\mathbf{e}_i$, leaving them at their random initialization. The paper provides no alternative update mechanism (EMA, separate codebook loss, etc.). This renders the core TS-Register component irreproducible as described.

2. **Prediction task gradient handling is contradictory.** Line 182 states: "To avoid prediction training affecting the generalization performance of the model, the gradients of the prediction heads are skipped at back-propagation." If gradients of the prediction heads are stopped, then no gradient from $\mathcal{L}_{\text{prediction}}$ propagates backward through the prediction decoder to the encoder. This means the prediction task cannot update any shared parameters. Yet the paper claims (line 75) that the prediction task "enhance[s] the model's few-shot and zero-shot abilities." It is unclear how a loss whose gradients are entirely blocked can influence encoder representations. This requires clarification: either the gradient flow is different from what is described, or the prediction task's role in pre-training is not what is claimed.

3. **Zero-shot evaluation has unexplained missing entries and asymmetry.** In Table 2 (lines 252-264), MOIRAI and Chronos have blank entries for Traffic with no explanation. The paper excludes TimesFM from Weather, Electricity, and Traffic because its pre-training includes those datasets (line 241), which is appropriate — but the same standard should be documented for all baselines. Additionally, while the paper claims dataset disjointness (line 67), it does not list the specific pre-training datasets, making this claim unverifiable. Given that the pre-training data is described as "publicly available datasets" (line 192) from domains that clearly overlap with the evaluation datasets (energy, weather, transport), the community would benefit from explicit dataset disclosure.

4. **Missing key architectural and training hyperparameters.** The paper specifies $K_f$ (number of masks), $P$ (number of patches), and $L$ (look-back = 512), but omits: learning rate, optimizer, batch size, patch length, dimension $D$, number of register tokens $N_r$, register dimension $D_r$, number of register cluster centers $H$, number of Transformer layers, number of attention heads, $K_f$ value, Bernoulli probability $p$, and the threshold bound $a$. While some of these may reside in a stripped appendix, the methodology section as presented is not reproducible.

### Minor

1. **No statistical significance or variance reported.** All results in Tables 1-3 are single-point estimates. Several margins are small (e.g., ETTh2: ROSE 0.331 ties PatchTST 0.331; Electricity: ROSE 0.155 vs PatchTST 0.159). Without standard deviations or multiple seeds, it is impossible to assess whether these differences are meaningful. This is a common gap in the field but is worth noting.

2. **"From Scratch" ablation reveals architecture alone is not SOTA.** Table 3 (line 321) shows that ROSE trained from scratch (with 10% data) underperforms several full-data baselines on ETTh1 (0.470 vs iTransformer 0.439, PatchTST 0.413) and ETTm2 (0.261 vs PatchTST 0.256). While this is expected for a foundation model paper — the whole point is that pre-training helps — it should temper the "SOTA architecture" framing. The paper's strength is the *pre-trained model*, not the architecture alone.

### Trivial

- In the zero-shot table (Table 2), ETTm1 has the label "0.434" under TimesFM (best), but ROSE is listed as 0.525 — the paper says "competitive performance across most datasets" which is accurate but the claim of "best on 5 of 7" in the abstract/summary should be precise.

---

## Nice-to-Haves
- Provide an explicit list of pre-training datasets to verify the claimed disjointness from evaluation data.
- Compare against fine-tuned foundation models (Timer, MOIRAI, Chronos) in the full-shot setting, not just against single-dataset baselines.
- Include a sensitivity analysis of pre-training data scale (e.g., 10%, 50%, 100%) to disentangle data quantity effects from architectural benefits.
- Include standard deviations over multiple random seeds for main results.

---

## Removed Points

- **"Unfair comparison: pre-trained vs. from-scratch baselines (Structural flaw)"** — This is the standard evaluation paradigm for foundation models. Comparing a pre-trained general model against single-dataset specialized models is meaningful and standard practice (cf. Timer, MOIRAI, Chronos papers). The paper's claim is about the pre-trained model's performance, not the architecture's standalone superiority. The "From Scratch" ablation already provides the controlled comparison the critic asks for.

- **"No statement about dataset separation"** — Factually wrong. Line 67 explicitly states "$\mathbf{D}_\text{pre-train}$, $\mathbf{D}_\text{train}$ and $\mathbf{D}_\text{test}$ are pairwise disjoint." The paper addresses this concern. (The separate concern about not listing specific datasets is retained as part of Weakness #3 above.)

- **"Double standard with TimesFM exclusion"** — The paper excludes TimesFM from certain datasets because TimesFM's pre-training is known to include them, while claiming ROSE's pre-training is disjoint. If the claim is false, that's a separate problem; but there is no double standard in applying the exclusion criterion differently to models with different known pre-training data.

- **"t-SNE figure not shown"** — Parser artifact; figures are in the original submission.

- **"Incomplete Section 4.2"** — Parser artifact; the scalabilty/sensitivity content was in the original submission but lost during extraction.

- **"Missing related works"** — Per instructions, I cannot verify whether related works are missing without external sources.

- **"Statistical significance should be reported"** — Weakened to Minor (not a fatal flaw, as single-run evaluation is standard in this field).

- **"From Scratch shows architecture is weak"** — The paper doesn't claim architectural SOTA; it claims pre-trained model SOTA. The "From Scratch" row validates the need for pre-training, which is the paper's thesis.

- **"Missing hyperparameters"** — Weakened to Minor, as some may be in the stripped appendix. But basic architectural hyperparameters ($D$, $N_r$, $H$, number of layers) should be in the main text.

- **"Prediction task co-training contradiction about updating encoder"** — Absorbed into Major Weakness #2 above (the gradient description is contradictory).

---

## Novel Insights

None beyond the paper's own contributions. Both reviewers identified the same core tension that any foundation model paper faces: pre-training advantage must be disentangled from architectural innovation. The novel synthesis is that the TS-Register's underspecified training mechanism and the contradictory prediction-task gradient flow are the paper's two most actionable weaknesses — neither is fatal, but both must be resolved for the methodology to be reproducible.

---

## Suggestions

1. **Clarify the TS-Register optimization.** Provide an explicit update rule for the codebook vectors $\mathbf{e}_i$. If using standard VQ-VAE-style training, specify whether EMA or a separate codebook loss is used. If the current description is meant to update both $\mathbf{x}_e$ and $\mathbf{e}_\delta$, clarify the stop-gradient placement. Show that the codebook converges to meaningful clusters via quantitative metrics (e.g., cluster purity, silhouette score).

2. **Resolve the prediction task gradient contradiction.** Explain how the prediction loss influences the encoder if prediction head gradients are skipped. If the intended behavior is that prediction gradients update the encoder but not the prediction heads, clarify the gradient flow. If the prediction task truly does not update the encoder, provide evidence that it still contributes to zero/few-shot performance (or remove the claim).

3. **List pre-training datasets and confirm disjointness.** Provide a table of all pre-training datasets and explicitly confirm that none of the 7 evaluation datasets (or their variants) are included.

4. **Report standard deviations.** Add multiple-seed results for the main tables to allow readers to assess whether performance gaps are meaningful.

5. **Fill in missing hyperparameters.** Provide $D$, $N_r$, $H$, $D_r$, number of Transformer layers/heads, learning rate, optimizer, batch size, patch length, $K_f$, $p$, $a$, and training schedule in the main text or appendix.

---
