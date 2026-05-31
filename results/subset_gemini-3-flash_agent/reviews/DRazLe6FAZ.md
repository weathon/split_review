## Summary
The paper introduces the `PRO-DYN` nomenclature, a formal framework based on Allen’s interval algebra, to categorize components of time-series forecasting (TSF) models into "Processing" (PRO) and "Dynamics" (DYN). It hypothesizes that the ability to learn dynamics is the primary driver of performance in long-term TSF. Through systemic analysis and empirical experiments (RQ1 and RQ2), the authors demonstrate that adding learnable linear dynamics (DYN layers) to under-performing models improves their results, and that placing these dynamics at the end of the architectural chain (Pre-processing-then-Dynamics) is the optimal configuration.

## Strengths
- **Formal Taxonomy for TSF (PRO-DYN):** The paper provides a novel and rigorous way to categorize model blocks using Allen's interval algebra (Section 3.1, Figure 1). This allows for a structural comparison of diverse architectures (Transformers, CNNs, SSMs) under a unified framework.
- **Systemic Identification of Architectural Bottlenecks:** The authors analyze 16 models (Table 1) and identify that under-performing models often lack learnable dynamics or use non-learnable operations like 0-padding for prediction. This provides a structural explanation for observed empirical performance gaps in the literature.
- **Empirical Validation through Surgical Modifications (RQ1):** The paper shows that adding simple linear DYN layers to models like Informer, FiLM, and FEDformer consistently improves performance (Figure 4, Table 2). This supports the claim that learnable dynamics are a key performance driver.
- **Isolation of Performance Drivers:** The authors distinguish between the benefits of "learnable dynamics" and simple "parameter addition" by comparing DYN versions with PRO versions (feed-forward layers that do not change time dimensions). This analysis (Section 4.3, Figure 5) suggests the improvement is inherent to the temporal mapping for models like Informer and FEDformer.
- **Robustness of Evaluation:** The study utilizes the TFB benchmark with 25 diverse datasets and multiple horizons, ensuring that the observations are not limited to a few specific datasets.

## Weaknesses

### Fatal
None.

### Major
- **Confounding Factors in Baseline Selection:** The "under-performing" group identified in Table 1 (e.g., Informer, FEDformer) consists primarily of older models (2021-2022) compared to the "SOTA" group (e.g., iTransformer, PatchTST, 2023-2024). These SOTA models include many improvements beyond the PRO-DYN configuration, such as RevIN normalization, patching, and channel-independence. Attributing their success primarily to the DYN head ignores these significant confounding factors.
- **Definitional Fluidity of "Dynamics":** In practice, the authors equate "learnable dynamics" almost exclusively with a linear layer mapping input length $L$ to horizon $H$. While the nomenclature is formal, the empirical finding that a linear head improves older Transformers is well-established in previous work (e.g., DLinear/NLinear). The paper does not sufficiently explore whether the framework provides predictive power beyond justifying the use of a simple linear output head.

### Minor
- **Validity of the RQ2 Experimental Setup:** To test the "dynamics location" (Pre-processing vs. Post-processing), the authors add a linear layer at the *beginning* of SOTA models (Figure 3) and observe a drop in performance. However, adding a heavy linear transformation ($L \rightarrow L$) to the input of an architecture designed for specific embedding structures may inherently disrupt the model. A more controlled test would be to swap the locations of existing layers rather than prepending a new one that changes the input dimensionality and distribution significantly.
- **Triformer as a Counter-example:** The authors note that Triformer follows the "successful" PRE-DYN configuration but still under-performs (Table 1). This indicates that the PRO-DYN configuration is not a sufficient condition for high performance, which tempers the "Dynamics is what you need" claim.
- **Performance vs. NLinear:** Despite improvements from adding DYN blocks, the updated versions of older models (except FiLM) still largely under-perform compared to the simple NLinear baseline (Table 2). This suggests that the "PRO" components of older models might still be acting as "drags" on performance that the addition of dynamics cannot fully overcome.

### Trivial
None.

## Nice-to-Haves
- Comparison with non-linear dynamics blocks (e.g., small MLPs or RNNs) to see if the "Dynamics" benefit extends beyond linear projections.
- A more detailed analysis of why iTransformer is less sensitive to the DYN-location modification than PatchTST or Crossformer.

## Removed Points
These points were considered but removed as they either fell outside the paper's scope or reflected parser artifacts rather than author errors:
- Reproducibility concerns (hyperparameters/logs) were removed as they are typically present in a full submission (Hard Rule).
- Stylistic/formatting nitpicks (Hard Rule).
- Suggesting the paper should address missing related works (Hard Rule).

## Novel Insights
The application of Allen’s interval algebra to neural network blocks provides a unique formal vocabulary to discuss "series-to-series" mapping versus "representation learning" in time-series models. This allows for a deeper structural understanding of why simple linear heads are so effective: they perform the actual temporal "Dynamics" transition that sequence-to-sequence backbones often struggle to model directly.

## Suggestions
- Conduct a "swapping" experiment for RQ2: instead of adding a layer, try to adapt a model to use its main backbone *after* a linear projection of the input to the horizon size, ensuring the total parameter count and input dimensionality are controlled.
- Test whether the "Dynamics" block must be linear. If a non-linear but time-mapping block performs even better, it would significantly strengthen the claim that the *nature* of the operation (Dynamics) is what matters most.
- Clarify the role of other SOTA components (like RevIN) within the PRO-DYN framework. Are they considered PRO functions? Does their presence change the necessity of the DYN block's location?

## Score and Decision
The paper provides a valuable and formal taxonomic contribution to a known empirical phenomenon in time-series forecasting. While the "discovery" that linear heads improve Transformers is not new, the `PRO-DYN` framework offers a rigorous way to evaluate architectural configurations. The experiments are extensive across the TFB benchmark, though some methodological choices in RQ2 and the focus on linear layers limit the depth of the "Dynamics" claim.

Based on the calibration against similar investigative/meta-analysis papers (e.g., T97kxctihq at 5.0, FITS at 8.0, Time-LLM at 7.0), this paper sits in the middle range. It is stronger than simple re-evaluations because of the novel formal nomenclature, but weaker than papers proposing major new architectures or benchmarks.

**Initial Bracket (Round 1):** 5.0 to 7.0.
**Narrowing (Round 2):** Compared to `T97kxctihq` (5.0), this paper is more sound because it introduces a formal nomenclature (Allen algebra) rather than just empirical observations. Compared to `FITS` (8.0), it lacks a significant new model contribution. The paper is most comparable to a solid architecture/analysis paper that clarifies existing trends.

**Anchor Papers:**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/T97kxctihq.md` (Avg: 5.0, R1): Focuses on affine mapping/RevIN. This paper is higher due to better formalization.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/bWcnvZ3qMb.md` (Avg: 8.0, R2): FITS (cited in the paper). FITS introduces a new model; this paper explains existing ones. This paper is lower.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/wMXH8tTQE3.md` (Avg: 6.0, R1): Benchmark/Toolkit. This paper is similar in its "systematic study" nature.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>