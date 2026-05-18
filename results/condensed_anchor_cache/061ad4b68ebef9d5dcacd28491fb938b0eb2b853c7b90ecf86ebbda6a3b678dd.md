- Decision: Reject
- Scores: 6, 3, 3, 8

## Merged Review

### Summary

This paper proposes UniTST, a Transformer model for multivariate time series forecasting that uses a unified attention mechanism on flattened patch tokens to simultaneously capture inter-series and intra-series dependencies, along with a dispatcher module to reduce computational complexity. Reviewers’ assessments vary significantly: two reviewers (R1:6, R4:8) find the approach promising and well-motivated, while two others (R2:3, R3:3) consider the contribution incremental and the evaluation insufficient. The paper is generally well-written but raises concerns about novelty, baseline comparisons, reproducibility, and theoretical justification.

### Strengths

- The problem of jointly modeling inter- and intra-series dependencies in multivariate time series is important and worth investigating (R1, R4).
- The unified attention approach is a reasonable design choice to address this limitation, and the idea of directly modeling both dependencies is interesting (R1, R2, R4).
- The paper is well-written, well-organized, and reads smoothly (R1, R4). Reviewer 4 specifically praises the clear experimental section with newest benchmark methods.
- Experiments cover major datasets and include hyperparameter and efficiency analyses (R3). Reviewer 2 finds the experimental results reproducible, reliable, and credible (though code is not provided).
- The dispatcher module is an innovative addition to make the model scalable for a potentially large number of variates (R2, R4). R2 states: “This innovative design effectively enhances the handling of multivariate time series data.”

### Weaknesses

- **Lack of novelty and incremental design**: Multiple reviewers (R1, R2, R3) note that the proposed architecture closely resembles existing models. The attention+dispatcher mechanism is nearly identical to approaches in ETC and Crossformer (R1, R3), and the method is similar to PatchTST (R2). Reviewer 3 points out that “Different sEnsors at Different Timestamps (DEDT)” and “cross-correlation coefficient” in prior works are essentially the same ideas, and the dispatcher is the same as the router in Crossformer. The contribution is considered ordinary (R3). Reviewer 4 (positive) does not contest novelty directly but finds the unified attention interesting; overall, the lack of fundamental innovation is a major weakness cited by three reviewers.
- **Insufficient baseline comparisons**: The evaluation lacks comparisons with recent state-of-the-art methods, including TimeMixer, FITS, ModernTCN (R1), GNN-based methods such as CrossGNN and FourierGNN (R1), LLM-based methods like LLM4TS and GPT4TS (R4), and CATS (ICML 2024) which adopts a very similar idea to this paper’s goal (R4). The claim of achieving SOTA performance is not sufficiently supported with these missing comparisons (R1, R3). The improvements over iTransformer are minimal in many cases (Table 6) (R1). Reviewer 4 explicitly asks for inclusion of LLM-based baselines.
- **Reproducibility and code**: No code is provided (R1, R3), and reviewers express reservations about result authenticity (R1: “lack of details in reproducibility”; R3: “authenticity of the experimental results is reserved”). Although R2 considers the results reproducible, the absence of code undermines this claim.
- **Motivation and theoretical justification**: The motivation is not clearly articulated (R2), and the experiment in Figure 3 is not well justified—specifically, why patching is introduced when most existing models do not use it (R2). The claim that “each value at one time stamp has no semantic meaning” is oversimplified; each timestamp in stock prices or hourly temperatures carries important information (R2). The paper does not clearly explain how patching specifically enhances the unified attention’s ability to capture dependencies (R2). The two-stage problem described in the Introduction lacks experimental proof, and a two-stage method (arXiv:2402.19072) is not inferior to UniTST in effect (R3).
- **Ablation study inadequacy**: The ablation study evaluates the dispatcher only on memory usage, which is relatively uncommon (R2). It should compare the whole model’s memory impact with other SOTA models, including computational cost and parameter size (R2). The batch size in the ablation is not specified, and one out of four ablation experiments resulted in an OOM error (R2). Reviewer 1 also notes a lack of efficiency comparison (time/memory) with iTransformer.
- **Missing experimental details and analyses**: 
  - The value of \(t'\) corresponding to the correlations in Figure 3 is not clarified (R3).
  - The model’s ability to capture the claimed correlations is not verified—could the authors compute correlation values from the model’s predictions and compare with Figure 3? (R3).
  - The order of input series in the flattened sequence is not determined; if random, the encoder may not be time-aware (R4). The difference between constructing a unified sequence and simple concatenation is not explained (R4).
  - It is unclear whether the unified sequence is normalized, univariate or multivariate (R4).
  - A case study of variable prediction curves is needed (R1).
  - Reviewer 1 asks for publicly disclosed optimal parameters (batch size, hidden dimensions, etc.) for all models to ensure fair evaluation.
- **Missing relevant prior work**: The paper claims previous Transformer models lack ability to simultaneously capture inter- and intra-variate dependencies, but CATS (ICML 2024) adopts a very similar idea (R4). The literature review should be revised to acknowledge and differentiate from this work.
- **Presentation details**: The article uses the ICLR 2024 template, which makes it inconvenient to locate exact lines for review (R3).