## Summary

LLMCO2 is a GNN-based regression model that predicts the energy (and, via a standard linear conversion, carbon footprint) of LLM inference. Its three key design choices—(1) representing each transformer layer as a DAG with **separate node feature sets for prefill and decode phases**, (2) incorporating each kernel's **Roofline-model performance** as a hardware-aware feature, and (3) a **focused sampling strategy** that preferentially collects data near real-world production configurations—are well-motivated by concrete shortcomings of prior methods. The ablation study cleanly validates the first two contributions, showing they achieve an 89% relative improvement in EBA(10%) over the best baseline (NNLQP) without the data-sampling component.

---

## Strengths

- **Separate prefill/decode feature sets per kernel node.** Each node in the transformer-layer graph carries two distinct feature vectors—one for the compute-bound prefill phase, one for the memory-bound decode phase (Section 4.1, lines 174–176). The ablation (Table 8, line 388) quantifies this: `+prefill/decode` alone achieves 34.3% EBA(10%) vs. NNLQP's 20.5%, a 67% relative improvement. This directly validates the paper's central claim that failing to model the two autoregressive phases degrades accuracy.

- **Roofline performance as a kernel-level hardware feature.** Each node includes its Roofline performance *P* (Equation 7, lines 222–230), encoding GPU peak throughput, memory bandwidth, and network bandwidth into the feature vector. The ablation (Table 8, line 389) shows this adds a further 13.1% EBA(10%) gain over the `+prefill/decode` variant and is shown to facilitate cross-GPU transfer (e.g., L4 → T4, a GPU unseen in training). This is a concrete mechanism absent from prior ML-based predictors (DeepEn, NNLQP).

- **Explicit closed-form equations for all-reduce kernels under tensor parallelism.** Equations 1–6 (lines 182–218) provide operation counts, memory footprints, and network transfer sizes for all-reduce kernels in both prefill and decode phases—something no prior baseline models. The case study (Section 6, line 428) demonstrates this captures the communication overhead that can make additional GPUs counterproductive for small-batch inferences.

- **Consistent advantage across 6 LLM families at multiple error bounds.** LLMCO2 achieves 15.5% average MAPE vs. 31.9% (DeepEn) and 28.5% (NNLQP) (Table 2, lines 332–338), and 45.7% EBA(10%) vs. 17.6% and 20.5% respectively (Table 3, lines 358–361), evaluated across Bloom, Gemma, Gemma2, Qwen2, Mixtral, and Llama3.1. Even the two ablation variants without focused sampling (34.3% and 38.8% EBA(10%)) substantially outperform both baselines, confirming the core architecture is genuinely more accurate.

- **Measured ground truth, not simulated.** Energy values are collected via NVML on real GPUs with 5-run averaging (line 319), and the test set includes the T4 GPU not present in training (line 317), providing a meaningful generalization challenge.

---

## Weaknesses

### Fatal
None.

### Major

1. **Focused sampling uses test-set errors to guide training data collection (Algorithm 1).**  
   Algorithm 1 (lines 237–286) evaluates the model on the test set TD, identifies points with high prediction error on TD, then samples additional training data near those points (via `FineGrainedSampling`). The new data can be added to either the training or test set (line 276). While the model never directly trains on test-set *labels*, the test set is used to adaptively shape where training data is collected—biasing the training distribution toward regions where the test set has high error. This violates the standard assumption that the test evaluation should be independent of the data collection process. The reported headline numbers (45.7% EBA(10%), 123% improvement) may therefore reflect adaptation to the test distribution rather than genuinely superior modeling.  

   **Mitigation:** The ablation study provides important partial relief—the `+Roofline` variant (38.8% EBA(10%)) does *not* use focused sampling and still substantially outperforms NNLQP (20.5%). So the core contributions (prefill/decode separation, Roofline features) are validated independently. However, the full-system numbers cannot be taken at face value without evaluation on a test set that was not used to guide data collection in any way.

2. **No variance or significance reporting.**  
   All results (Tables 2–4, Table 8) are point estimates with no error bars, confidence intervals, or statistical tests. With only 5 measurements per inference configuration and across 6 LLM families, 4 GPU types, and varied inference parameters, run-to-run and train-seed variance could be material. For example, LLMCO2's MAPE for Mixtral (19.4%) vs. DeepEn (23.2%) is a gap of 3.8 percentage points with no indication of whether this is stable across repeated evaluations. This is particularly important for a claim of "best accuracy" at a top venue.

### Minor

3. **Kernel extraction pipeline is under-specified.**  
   The paper states that for a given LLM config, it "extract[s] kernels in each transformer layer and global LLM features, following various kernel optimizations" (line 159). While the kernel *types* (Q_proj, K_proj, V_proj, fuse_atten, FF1, FF2, all-reduce, all-reduce) are described in Section 2 and the feature equations are provided, the paper does not specify a systematic procedure for mapping an abstract LLM architecture (hidden size, head count, GQA ratio, Flash Attention on/off, quantization format) to a concrete kernel-level graph with correct dimensions for each node. For example, how are the input/output dimensions of each kernel derived when using Flash Attention vs. standard attention, or under different GQA configurations? This is a reproducibility barrier for applying the method to a new LLM not already profiled by the authors.

4. **No per-GPU breakdown of results.**  
   Training uses L4, A100, and H100; testing includes all four GPUs (including T4, unseen during training). However, results are only reported aggregated across all GPUs. It is therefore impossible to assess whether LLMCO2 generalizes well to the unseen T4 or whether its accuracy is driven primarily by the seen GPU types. A per-GPU breakdown would substantially strengthen the generalization claims.

5. **No ablation of the graph architecture choice.**  
   The paper uses GraphSAGE (line 234) without justification or comparison to other GNN variants (GCN, GAT) or even a non-graph baseline (MLP with only global features). Given that the method's name emphasizes "graph neural network," an ablation varying the graph architecture would clarify whether the graph structure itself contributes beyond the careful feature engineering.

6. **Runtime overhead of prediction is not reported.**  
   The paper compares prediction accuracy but does not report prediction latency, training time, or the cost of the data collection process (the focused sampling loop involves hundreds of new GPU measurements per iteration). For a tool intended to be used *before* inference to guide decisions, prediction speed matters.

### Trivial
None.

---

## Nice-to-Haves

- **Evaluate on a truly independent test set.** Construct a test set from the initial 50K samples (or from a separate pool) and do not use its errors to guide data collection at any point. This would cleanly separate the value of the model architecture from the value of adaptive sampling.
- **Report per-GPU and per-LLM-family results with variance** (standard deviations or 95% CIs across multiple seeds/data splits).
- **Provide the kernel extraction pipeline** as pseudocode, system diagram, or open-source tool to enable reproducibility.
- **Compare to adapted baselines** (e.g., training separate DeepEn/NNLQP models for prefill and decode) to isolate the value of the architectural innovations from the baseline methodology differences.
- **Publish the code and dataset** given the complexity of the pipeline.

---

## Removed Points
*These are flagged to be removed per filtering rules; treat with caution.*

1. **Train-test adaptation claim is "fatal" / invalidates core contribution.** The critic's framing that the evaluation contamination "prevents the paper from making a clean empirical case" is overstated. The ablation study cleanly validates the core architectural contributions (prefill/decode + Roofline) without the problematic sampling component. The contamination only affects the full-system numbers.
2. **Table 1 is uncharitable to LLMCarbon about hardware features.** FLOPs counting is not the same as modeling GPU memory bandwidth, network bandwidth, and achieved throughput. The paper's characterization is accurate.
3. **"121 days calculation presented without derivation."** The numbers are cited from prior work and the reasoning is sketched in lines 16–17. This is not a substantive weakness.
4. **Roofline as feature creates nested predictor concern.** This is a design choice, not a flaw.
5. **EBA numbers show room for improvement.** Every predictor has room for improvement; this is not a weakness.
6. **Carbon conversion is trivial.** The paper explicitly uses the standard formula from Faiz et al. (2024) and the contribution is about energy prediction accuracy, which is where the difficulty lies. The title's "carbon footprint" framing is accurate.
7. **Figure label duplication.** Two figure captions share the same label `f:co2_train_infer` (lines 402, 409). This is a minor formatting artifact with no bearing on the scientific content.
8. **User case studies add limited value.** The case studies demonstrate practical applications of the tool; they are illustrative but not central to the contribution claim.

---

## Novel Insights

The reviews surface two observations that go beyond what the paper itself explicitly discusses. First, the Roofline feature operates as a form of *learnable calibration signal*: the GNN combines a first-principles performance estimate (Roofline *P*) with learned corrections based on other features. The paper could reframe this as an interpretable hybrid predictor. Second, the focused sampling algorithm is effectively active learning *for regression* using production trace priors—this design pattern could be disentangled and applied to other hardware measurement tasks. Neither insight is fully developed in the paper, but both point toward more principled evaluation and broader applicability.

---

## Suggestions

1. **Most important: re-run evaluation with a held-out test set that is never used to guide data collection.** Report both the full-system numbers and the ablation variants (without focused sampling) on this independent set. If the gap between 38.8% and 45.7% EBA(10%) holds on the clean test set, the focused sampling is validated; if it shrinks, the paper should adjust its claims accordingly.
2. **Add variance/uncertainty reporting** (error bars or confidence intervals) to all tables, at minimum for the headline metrics across multiple training seeds.
3. **Specify the kernel enumeration procedure** more concretely—even as a table mapping LLM architectural parameters to concrete kernel dimensions for each of the 8 kernel types.
4. **Provide per-GPU breakdowns** to substantiate the generalization claim, especially for the unseen T4 GPU.
5. **Add a non-graph baseline** (MLP on global features only) to quantify the value added by the graph structure itself.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>