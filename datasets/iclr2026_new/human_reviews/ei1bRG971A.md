## Human Reviewer 1

### Summary
The paper presents a new heuristic method using token-conditional dynamic depth, applied post-training for improving accuracy at a low additional training and inference cost. The paper is aimed at LLM system engineers and inference optimization researchers, people who modify or extend pretrained transformer architectures to trade off accuracy and compute efficiency.

- Introduces Dynamic Nested Depth (DND): a router selects “hard” tokens, which are reprocessed once through the same transformer block; the outputs are fused with the original states via a normalized gate.
- Adds a router-control loss (to keep scores separable yet non-saturated) and a threshold-control loop (buffer proportional control + EMA) to stabilize the selected-token ratio.
- Applies DND to mid-layers of Qwen3-1.7B (dense) and Qwen3-30B-A3B (MoE) models; reports modest average accuracy gains with ~6 % FLOPs overhead and negligible parameter growth (< 0.1 M).

### Strengths
- Simple, reproducible architecture with minimal parameter overhead.
- Clear ablation analysis separating router and threshold controls.
- Good methodological transparency (layer range, selection ratios, FLOPs estimate).

### Weaknesses
- Small performance improvements, both in an absolute sense and relative to known model variants. Even fine tuning or just random variation might yield performance improvements similar to those shown in the paper.
- Weak experimental support: only within-model deltas, no compute-matched baselines, and no wall-clock profiling.
- Incremental and heuristic: conceptually similar to existing adaptive-depth ideas (MoD, MoR, ITT, early-exit) and lacks deeper theoretical insight.

### Questions
- Clarify whether base model weights were frozen or lightly fine-tuned during DND training.
- Include compute-matched comparisons with other adaptive-compute methods.
- Discuss failure modes—cases where DND reduces accuracy or increases instability.

### Soundness
4

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper introduces a method called Dynamic Nested Depth (DND) which adaptively identifies “difficult” tokens for layer in an LLM and allocates extra computation to those tokens by re‑processing them through the same layer in a nested way, while easier tokens receive standard processing. This token‑level routing is managed by a lightweight router that assigns each token a probability of being selected using hidden state of each token in the seqeunce; if the score exceeds a threshold, the token undergoes a “nested” pass. Once processed, the outputs of the first pass and the subsequent passes are merged together before moving to the next layer.

### Strengths
- The problem formulation is compelling, as allocating additional computation to difficult tokens could improve model accuracy at the cost of additional compute.
 - Experiments are adequate and includes evaluations across diverse benchmarks (knowledge, reasoning, coding).
 - Analysis is insightful, with clear plots and ablations that illustrate how token-level nested depth impacts performance.

### Weaknesses
- The reported accuracy improvement over regular SFT is only 0.87 on average in table 1, which appears minimal. The proposed method involves processing the input multiple times for some tokens in the given layers. Such process would increase the compute overhead. But this table does not include the computational overhead introduced to bring the 0.87 avg accuracy improvement. This makes the experimental results incomplete.
 -  Experiments are conducted on only a single LLM (Qwen), raising concerns about the generalizability of the method to other architectures.

-  Based on the method description and experiments, it is unclear whether DND fine-tunes all components of the transformer blocks in the selected layers (L_s to L_e) or if it fine-tunes all model parameters like standard SFT. 

- The router-level losses and their underlying motivation are not clearly explained. Moreover, their overall contribution appears minimal, as reflected by the similar values in Table 2 (60.54, 60.58, 60.64) where these losses are not included.

 - Overall, the approach seems largely heuristic and does not demonstrate a substantial improvement in accuracy.

### Questions
Based on the method description and experiments, it is unclear whether DND fine-tunes all components of the transformer blocks in the selected layers (L_s to L_e) or if it fine-tunes all model parameters like standard SFT.

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper proposes Dynamic Nested Depth (DND) — an efficient method to enhance pre-trained LLMs by selectively deepening computation. Instead of uniformly processing all tokens, DND identifies critical tokens that require more reasoning effort. Within each transformer layer, a lightweight router marks these important tokens after a standard forward pass. Only those tokens undergo an additional "nested" pass through the same layer, and their outputs are then fused with the initial results. DND can be applied in post-training (e.g., fine-tuning), making it compatible with existing models.

### Strengths
S1: While adaptive computation is an established research area, DND mechanism is a novel implementation. Instead of skipping layers or routing to different experts, the idea of re-processing a selected subset of tokens through the same transformer layer ("nested pass") is an elegant formulation, reminding me of recent looped Transformers. Furthermore, the decision to apply this technique during a post-training (SFT) phase is a highly original and pragmatic choice.

S2: Thorough Empirical Evaluation: The experiments are comprehensive and convincing. The method is validated on two different model scales and architectures (a dense 1.7B and a sparse MoE 30B model), and tested across 17 diverse benchmarks. The performance gains, especially in complex reasoning domains like coding and mathematics, are significant and consistently positive.

S3: The significance of this work is substantial, as it addresses one of the most pressing challenges in the development of LLMs: the trade-off between performance and computational cost.

### Weaknesses
W1: While this paper presents a promising direction,the paper does not quantitatively demonstrate why the selected tokens are "critical." The visualizations could be the result of cherry-picking or confirmation bias. It is unclear if the router has learned a meaningful selection strategy or is simply responding to surface-level statistical patterns. To strengthen this claim, the authors should perform a quantitative analysis correlating token selection with intrinsic properties of the tokens or the model's state. 

For instance: Correlation with Model Uncertainty: Are the selected tokens ones for which the model has high prediction entropy or low softmax probability in the initial pass? This would suggest DND is focusing computation on "hard" decisions.

W2: The paper claims a "minimal parameter and computing increase," basing its efficiency analysis on a theoretical calculation of FLOPs.  FLOPs are a poor proxy for actual inference speed (latency and throughput) on GPUs. The DND architecture, with its Pack and Unpack operations, breaks the massive parallelism that GPUs are optimized for, potentially leading to significant latency increases that are not captured by FLOP counts. They should report: Wall-clock latency (ms per generated token) and throughput (tokens per second) on a standard benchmark GPU (e.g., A100 or H100).

### Questions
Q1: All experiments are conducted on a single family of models (Qwen3). While the results are positive, this makes it impossible to know if the DND approach is a general-purpose technique or if its effectiveness relies on specific, undocumented properties of the Qwen architecture.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3