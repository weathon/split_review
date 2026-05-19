- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 3, 6
Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper introduces a transfer learning paradigm for GNN-based physics simulators on unstructured meshes. It proposes SGUNET, a scalable graph U-net with DFS-based pooling that adapts to different mesh resolutions; mapping functions (Uniform and First-N) to transfer parameters between differently-sized pre-trained and fine-tuned models; and the ABCD pre-training dataset of 20,000 3D contact simulations. The central empirical claim is that pre-training on ABCD and fine-tuning on as little as 1/16 of downstream training data yields an 11.05% improvement in position RMSE over training from scratch, and that fine-tuned models converge faster.

## Strengths

- **Quantified transfer learning improvement**: The paper presents a specific, measurable result — an 11.05% improvement in position RMSE on the 2D Deformable Plate when fine-tuning on 1/16 of the training data versus training from scratch (abstract, Section 4.4, Figure 6). On the 3D Deforming Plate, fine-tuning on 1/8 of the data reaches the same validation RMSE in 200k steps that requires 500k steps from scratch — a 60% reduction (Section 4.4, Figure 10c). These are concrete, reproducible claims.

- **DFS-pooling enabling architectural flexibility**: The Scalable Graph U-net introduces a depth-first search pooling that supports variable pooling ratios and node-proximity clustering, making the model adaptable to different mesh resolutions (Section 3.3, Algorithm 1, Figure 1b). This is a concrete architectural innovation that enables the same model class to serve both pre-training and diverse downstream tasks.

- **Explicit parameter mapping functions for heterogeneous architectures**: The paper defines Uniform and First-N mapping functions (Section 3.4.1, Equations 3–5, Figure 2b-c) that align parameters between pre-trained and fine-tuned models with different numbers of GUnet stages and message-passing blocks. This directly addresses the core challenge that prior GNN physics simulator work had not attempted — transferring knowledge when source and target architectures differ.

- **Creation of a pre-training dataset for mesh-based simulation**: The ABCD dataset provides 20,000 physics simulations from randomly selected 3D CAD shapes (Section 4.1, Figures 3–4). This is the first dataset designed specifically for pre-training mesh-based GNN simulators and enables the entire transfer learning pipeline.

- **Transfer learning generalizes beyond SGUNET**: The paper shows that applying the same fine-tuning strategy to MGN also yields better performance with less data and shorter training time (Section 4.4, Figures 5, 8). This indicates the transfer learning approach has broader applicability beyond the proposed architecture.

## Weaknesses

### Fatal
None.

### Major

- **No confidence intervals or variance on test metrics despite multiple seeds**: The paper states that "all experiments are repeated 5 times with different random seeds" (Section 4.4), yet the headline results (e.g., the 11.05% improvement) and all test-set comparisons in Tables 3–4 are reported as point estimates with no error bars, standard deviations, or statistical significance tests. Without variance, the reader cannot assess whether the reported improvements are robust or within the noise of the training procedure. This is the paper's most significant evidential gap.

- **Ablation of the regularization term is missing**: The paper introduces a Frobenius-norm regularization term (Eq. 5, Section 3.4.2) intended to "constrain the difference between the pre-trained weights and target model weights for better generalization performance." The hyperparameter λ is never varied, and no experiment compares performance with and without this term. Without this ablation, the contribution of the regularization component to the overall results is unknown.

### Minor

- **Baseline for the 11.05% claim is ambiguous**: The paper states the fine-tuned model on 1/16 data achieves "an 11.05% improvement compared to the model trained from scratch" (abstract, Section 4.4). It does not explicitly state whether "trained from scratch" means on the full dataset, on the same 1/16 subset, or refers to MGN. The surrounding context ("comparable to that of the model fine-tuned on the full dataset") strongly implies the comparison is against scratch on full data, but the phrasing should be clarified to eliminate ambiguity.

- **MGN transfer learning mechanism is not described**: The paper shows MGN-FT results (Figures 5, 8, Tables 3–4) and claims the transfer learning approach generalizes to MGN. However, the mapping functions (Uniform/First-N) in Section 3.4.1 are designed for SGUNET's Processor + GUnet stage hierarchy. MGN has no GUnet stages. The paper never explains which components are shared and how the mapping is applied to MGN's architecture, making the MGN fine-tuning results difficult to interpret.

- **Scratch model training budget not explicitly stated**: Fine-tuned models are trained for 20k steps (Deformable Plate) or 500k steps (Deforming Plate) (Section 4.4). The paper does not explicitly state whether the "trained from scratch" baselines use the same step budget. While the shared validation curves (Figures 7, 10) imply identical budgets, the text should state this directly. Additionally, for the Deformable Plate (20k steps), the paper does not verify that scratch models have converged; the reviewer notes that Figure 7c shows the scratch model's loss still decreasing at the end of the plotted range, which would conflate initialization advantage with genuine knowledge transfer.

- **No computational cost reporting**: The paper reports pre-training for 1M steps (Section 4.3) and describes efficiency benefits from transfer learning, but never reports GPU-hours, wall-clock time, or hardware configuration. This limits practitioners' ability to assess the practical trade-offs.

### Trivial
- The unpooling operation (up-sampling) in the GUnet is mentioned (Section 3.3) but not described — the paper focuses on the down-sampling (DFS pooling) in detail.
- The "first time transfer learning has been adapted and applied to GNNs predicting physics simulations" claim (Section 3.4) is too broad — there is prior GNN transfer work in molecular and physical domains — though the claim may be defensible if narrowly scoped to mesh-based simulation specifically.

## Nice-to-Haves
- A control experiment analyzing what knowledge is transferred (e.g., freezing pre-trained weights and only fine-tuning the decoder) would strengthen the scientific contribution by distinguishing improved initialization from learned physics features.
- A baseline comparing the mapping functions against naive weight averaging or random re-initialization of unmatched parameters would isolate the benefit of the proposed Uniform/First-N mappings.
- An experiment with an unrelated downstream task (e.g., fluid dynamics) would test whether the improvement is task-specific or generic parameter initialization.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Pre-training domain mismatch as a major weakness** (Harsh Critic #4): The reviewer claims the ABCD pre-training data (3D contact simulations) differs fundamentally from downstream tasks (2D/3D plate indentation). However, the paper explicitly acknowledges that downstream tasks "represent a subspace of simulations relative to our generalized pre-training dataset" (Section 4.1). Cross-domain transfer is standard practice; the paper's claim is empirical (transfer improves results), not mechanistic. This does not threaten the core claims.

- **Missing dataset release / reproducibility concerns** (from Harsh Critic's "Missing Parts"): These are removed per the hard rule that criticisms about the existence or release status of cited resources are not valid. The paper cites the ABC dataset and describes the data generation pipeline; the ABCD dataset is a contribution described in the paper.

- **Missing tables/appendix content** (from Harsh Critic's "Missing Parts"): The parser strips tables and appendices. These exist in the original submission.

- **"First time" claim overstatement** (Harsh Critic's Section-by-Section notes on intro): Removed as a nitpick about framing rather than a substantive technical weakness. The claim is qualified as applying to mesh-based GNN physics simulators specifically.

- **DFS pooling detail questions** (Harsh Critic's Section-by-Section notes on Section 3): Questions about how element nodes of the same material are identified and how edge features within clusters are handled are implementation details appropriate for the appendix. The paper references Algorithm 1 for the pseudo-code.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not surface an observation that the paper itself does not make.

## Suggestions

1. **Report error bars for all test-set metrics.** With 5 random seeds already collected, this requires minimal additional effort and would substantially strengthen the paper's quantitative claims.

2. **Clarify the baseline for the 11.05% claim.** State explicitly: "Fine-tuned on 1/16 data achieves RMSE X, while SGUNET trained from scratch on the full dataset achieves RMSE Y, and SGUNET trained from scratch on 1/16 data achieves RMSE Z."

3. **Add an ablation of the Frobenius regularization term** (vary λ and include a λ=0 baseline) to validate its claimed benefit.

4. **Describe how the mapping functions are applied to MGN** (which has no GUnet stages), or limit the transfer learning claims to SGUNET.

5. **Explicitly state the training budget for scratch models** and verify convergence (e.g., train until loss plateaus) to ensure the comparison is fair.

---
