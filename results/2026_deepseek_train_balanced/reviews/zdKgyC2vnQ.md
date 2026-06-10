## Summary

MiniDrive proposes a lightweight vision-language model (83M parameters for the smallest variant) for autonomous driving, using a convolutional backbone (UniRepLKNet) instead of a Transformer-based vision encoder, and two modules: FE-MoE (a mixture-of-experts on 2D feature maps) and DI-Adapter (cross-attention between visual and text embeddings). The core claim is that this system achieves competitive results on the DriveLM benchmark at a fraction of the computational cost of prior models, and outperforms much larger general VLMs on the CODA-LM driving perception benchmark.

## Strengths

- **Competitive performance at extreme parameter efficiency**: On DriveLM, MiniDrive_{224} (83M params, 5.9B FLOPs) matches or exceeds EM-VLM4AD_Base (345M params, 9.9B FLOPs) on all four metrics (BLEU-4, METEOR, ROUGE-L, CIDEr), while using ~40% fewer FLOPs and ~48% less memory. This is a concrete and practically valuable efficiency gain, verified from Table 1 and Table "flops".

- **Ablation confirms both proposed modules contribute additively**: Table 2 shows a clear stepwise improvement from baseline (45.70 BLEU-4) → +FE-MoE (48.30) → +DI-Adapter (48.00) → both (49.70), with consistent gains across the other three metrics. The additive nature is cleanly demonstrated.

- **Multi-image handling with spatial grounding**: Unlike most prior AD VLMs (e.g., DriveGPT4) that only handle single images, MiniDrive processes the standard 6-camera autonomous driving setup. The qualitative examples (Figure "cam_examples") demonstrate that attention maps correctly activate for the camera view matching spatial terms in the user query (e.g., "back left", "CAM_FRONT"), providing interpretability for perception/planning/prediction tasks.

- **Trainable on a single consumer GPU**: At 1.03 GB memory with 83M params, multiple instances can be trained simultaneously on a single RTX 4090. This lowers the barrier to entry for AD VLM research.

## Weaknesses

### Major

- **The CODA-LM comparison is between a domain-specialized model and general VLMs evaluated zero-shot, which does not support architectural superiority claims.** Table 3 compares MiniDrive (83M, trained on the DriveLM driving dataset) against LLaVA1.5-7B and Qwen-VL-Chat-7B — general-domain VLMs that were *not fine-tuned on driving data*. The paper claims to "outperform general open-source VLMs (7B) ... by an average of 13.2 points" (Contribution 4), but this conflates domain specialization (training on driving data) with architectural advantage. MiniDrive being stronger on a driving benchmark after being trained on driving data is expected. To substantiate a claim of architectural superiority, a controlled comparison (e.g., fine-tuning LLaVA1.5 on the same DriveLM training split) is necessary. As written, Table 3 does not support the conclusions drawn from it about MiniDrive's relative quality or innovation.

### Minor

- **The ablation baseline is underspecified.** Table 2 reports results when both FE-MoE and DI-Adapter are absent ("--", "--") at 45.70 BLEU-4, but the paper never describes the baseline architecture. What replaces the modules when they are removed? Do features go directly from UniRepLKNet through a projection to T5? Without this specification, the reader cannot assess what the incremental gains are measured against, and the baseline's competitiveness (45.70 BLEU-4 already exceeds EM-VLM4AD_Base's 45.36) is left unanalyzed.

- **No inference speed measurement despite "response efficiency" being a central claimed advantage.** The abstract and contribution list emphasize "real-time response" and "response efficiency," yet the paper reports only FLOPs, parameter count, and GPU memory (Table "flops"). Wall-clock inference speed (ms/query, tokens/second) is not reported. For autonomous driving deployment — the stated motivation — real-time latency is the binding constraint, and FLOPs alone do not guarantee fast inference (they depend on hardware, implementation, and memory-bandwidth factors).

- **No empirical demonstration that DI-Adapter actually makes visual tokens "dynamic."** A central claim is that DI-Adapter "enables visual features to dynamically adapt to different textual instructions" (Section 3.5) and resolves "fixed visual tokens for the same image" (Contribution 3). Yet no experiment analyzes this: e.g., showing the same input image with different text queries and measuring how the visual features change (via cosine similarity, attention visualization, or feature-space analysis). The claim is asserted architecturally but never verified empirically.

- **No sensitivity analysis for key hyperparameters.** The paper sets N=4 experts and 16 tokens per image without any ablation or justification. Whether performance is robust to these choices, or whether a different configuration would improve results, is unknown.

- **Novelty framing overstates what is technically new.** FE-MoE is mixture-of-experts applied to 2D convolutional feature maps (each expert = deconv → ReLU → conv). DI-Adapter is cross-attention (text as K/V, visual as Q) with a residual connection. Both are standard techniques from the broader VLM literature, applied here in a new domain context. The paper's contribution is primarily *system-level engineering* — assembling these components into an efficient pipeline — rather than three novel methodological inventions. The framing should reflect this.

### Trivial

None.

## Nice-to-Haves

- A controlled CODA-LM comparison where a general VLM (e.g., LLaVA1.5) is fine-tuned on the same DriveLM training split before evaluation would greatly strengthen the claim that MiniDrive's architecture — not just its domain-specific training — drives the CODA-LM results.
- Inference latency measurements (ms per query on the reported hardware) would directly substantiate the "real-time" deployment claim.
- An analysis of how DI-Adapter output features vary with different text inputs for the same image would verify the "dynamic" claim empirically.

## Removed Points

The following criticisms from the harsh reviewer were removed after cross-checking against the paper:

- *"Only one dataset (DriveLM) for main evaluation"* — The paper also evaluates on CODA-LM, so this statement is factually incorrect.
- *"Training for only 6 epochs... paper does not discuss whether performance saturates"* — Speculative; no evidence that longer training would improve results. Not a valid weakness.
- *"Vision encoder is frozen... paper does not discuss whether fine-tuning would yield better results"* — The paper explicitly states this choice is for efficiency; demanding an ablation of the opposite design choice without a specific reason is beyond scope.
- *"Statistical significance is not reported"* — Not standard practice for benchmark evaluation in this community.
- *"Advantages are bought with a simpler LM (T5-Small) whose generation quality ceiling is lower"* — Pure speculation with no evidence presented.
- *"Generalization to other AD datasets (e.g., BDD-X, NuScenes QA) is not tested"* — The paper evaluates on DriveLM (NuScenes-based) and CODA-LM. Requesting additional datasets is a nice-to-have, not a weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent tension: the paper's strongest evidence (competitive DriveLM results at 83M params) is also its most straightforward claim, while the flashier comparison (CODA-LM vs 7B models) is the least methodologically sound. This is a common pattern in efficient-model papers — the core contribution is genuine but the paper reaches for comparisons that overstate what the evidence supports.

## Suggestions

1. **Clarify the ablation baseline**: Describe what the "--", "--" configuration actually is (direct projection of UniRepLKNet features into T5?).
2. **Add wall-clock latency**: Report inference speed in ms/query on the RTX 4090 used for training.
3. **Either control the CODA-LM comparison or reframe the claim**: Fine-tune LLaVA1.5/Qwen-VL-Chat on DriveLM data for a fair comparison, or explicitly state that MiniDrive's advantage comes from domain specialization rather than architectural superiority.
4. **Empirically demonstrate the "dynamic" behavior of DI-Adapter**: Show the same image with different text queries and report feature similarity or attention changes.
5. **Add hyperparameter sensitivity**: Vary N (experts) and token count to show the chosen values are near-optimal.
6. **Tone down the novelty claims for individual components**: Frame FE-MoE and DI-Adapter as efficient adaptations of standard techniques for the AD domain rather than as fundamentally new inventions.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>