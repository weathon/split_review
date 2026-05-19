- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3
Now I have a complete picture of the paper. Let me write the consolidated review.

## Summary

This paper proposes Free-MoE, a framework that creates domain-specific "experts" from a frozen pre-trained LLM by purifying/zeroing out less important weights in its hidden layers (the DOWP algorithm), then uses a trainable multi-level router to assign inputs to the relevant purified subnetwork. The core claim is that this is "tuning-free" and requires "no extra model parameters." Experiments on LLaMA-2 and Gemma models show DOWP yields 2–3% absolute gains on MMLU, MBPP, GSM8K, and MathQA, while the full Free-MoE system (DOWP + router) achieves ~1.1% average gain.

## Strengths

1. **DOWP yields consistent, non-trivial improvements across multiple models and benchmarks.** Table 1 reports +1.98% (MMLU), +2.08% (MBPP pass@1), and +1.97% (GSM8K) for LLaMA-2-7b-chat, with similar gains on LLaMA-2-13b-chat, Gemma-7b, and Gemma-2-9b. A peak of 6.8% is reported in Section 4.2. These gains are achieved without modifying the base LLM weights.

2. **Model-agnostic design validated across two model families and four sizes.** Results are reported for LLaMA-2-7b-chat, LLaMA-2-13b-chat, Gemma-7b, and Gemma-2-9b, supporting the claim of portability across transformer-based LLMs.

3. **Systematic ablation studies.** Tables 2–5 examine purification ratio, sublayer type, patch size, and K-means cluster count with concrete accuracy numbers, showing the method's sensitivity to design choices is empirically explored.

## Weaknesses

### Fatal
None.

### Major

1. **The central claim of "tuning-free" and "no extra model parameters" is contradicted by the paper's own method.** The abstract states Free-MoE "requir[es] no extra model parameters" and is "completely tuning-free," while Section 3.2 introduces a "multi-level trainable router" that is explicitly trained via cross-entropy loss (Equation 9) and adds new parameters (classifier layers). The conclusion repeats that Free-MoE achieves "tuning-free" and "parameter efficiency." This is not a minor wording issue — the paper's core framing directly contradicts what the method actually does. The DOWP weight-purification component is genuinely tuning-free for the LLM backbone, but claiming the entire Free-MoE framework is "tuning-free" while it contains a trained router is misleading.

2. **No experimental comparison against any other MoE method.** Figure 1 positions Free-MoE as superior to "Sparse MoE with top-1 gating" and "Domain Mapping & Random Gating MoE," and Section 1 claims purification "significantly enhances both the accuracy and effectiveness of expert selection" compared to Sparse MoE. Yet the experiments compare only against the unmodified base model — none of the claimed advantages over existing MoE methods are empirically validated. Without comparisons to Switch Transformer-style routing, Expert Choice, or other gating mechanisms on the same LLM backbones, the paper's central contribution narrative is unsubstantiated.

3. **Free-MoE (with the router) underperforms DOWP alone, undermining the value of the trained router.** DOWP alone achieves an average gain of ~2.04%, while Free-MoE (DOWP + router) achieves only ~1.11% (Section 4.2). Since Free-MoE subsumes DOWP plus a router, the router's addition should help, not hurt. This suggests the router's domain classification is noisy enough to degrade performance. The paper offers no explanation for this degradation and frames Free-MoE positively despite the clear drop from DOWP.

### Minor

4. **The posterior probability \(P(\mathcal{D} \mid \mathcal{T})\) used for main-domain selection (Equation 1) is never defined.** Section 3.1 states the algorithm "comput[es] the posterior probability" but gives no model, estimator, or procedure. This is a critical gap in the method description, as the entire domain selection pipeline hinges on this computation. (The paper later describes K-means clustering on embedding features for subdomain assignment, suggesting that domain identification might rely on centroid distances, but the posterior probability for main-domain selection remains unspecified.)

5. **Reported gains (1–3%) lack confidence intervals, error bars, or significance tests.** Given the small absolute improvements, it is impossible for the reader to determine whether the gains are stable or within noise range. This is especially important since the paper acknowledges the method is sensitive to hyperparameters (e.g., 3% purification ratio matches the baseline while 5% gives a gain).

6. **Computational efficiency is claimed but never measured.** The title and introduction frame Free-MoE as improving "computational efficiency," and Section 3 states the method "minimiz[es] unnecessary inference computations." No wall-clock times, FLOP counts, or parameter counts for the DOWP-processed models or the router are reported. The only evidence is the purification ratio ablation (5% of weights zeroed), but the overhead of the router's forward pass and the DOWP preprocessing pipeline is unaccounted for.

7. **The K-means cluster count ablation (K=12 on MMLU) may involve test-set leakage.** The paper varies K from 8 to 16 on the MMLU dataset and finds K=12 optimal. MMLU naturally divides into ~12 categories. If K was tuned by evaluating on the MMLU test set (rather than a held-out validation split), this constitutes data leakage. The paper does not clarify which split was used.

### Trivial
None (formatting issues are parser artifacts per instructions).

## Nice-to-Haves

- Compare DOWP against simple baselines like random weight pruning at the same ratio. This would test whether the domain-orientation in the importance metric is meaningful or if any pruning at the right ratio works.
- Compare the trainable router against a simpler alternative (e.g., a TF-IDF classifier or nearest-centroid assignment) to justify the added complexity.
- Report the computational overhead: wall-clock time per inference for the base model, DOWP, and Free-MoE.

## Removed Points

- *"DOWP requires reference data which is a form of adaptation"* — Removed. Computing importance statistics from validation-set activations is standard practice in pruning literature and is not "training."
- *"The importance metric has no justification"* — Removed. The metric (weight magnitude × activation norm) is a well-established heuristic in magnitude-based pruning, citing Han et al. (2015).
- *"The router must already know the domain at inference time"* — Removed. The router is designed to predict the domain from the input embedding; it does not require domain labels at inference.
- *"Missing comparison with in-context learning, zero-shot prompting, LoRA"* — Removed/weakened. The paper frames itself as an MoE method; comparing with parameter-efficient fine-tuning or prompting methods is outside its stated scope. However, a comparison against other tuning-free adaptation methods would strengthen the paper.
- *"Missing related works"* — Removed per instruction.
- *Various typos/formatting criticisms* — Removed per instruction (parser artifacts).

## Novel Insights

None beyond the paper's own contributions. The two reviewers' perspectives largely align on the paper's overclaimed framing and missing baselines. There is no insight from the reviews that the paper itself does not already surface, aside from the observation that the hierarchical structure of the critiques highlights an unusual pattern: the harsh critic correctly identifies the "tuning-free" contradiction as the most serious issue, while the strength finder's strongest claim (consistent 2–3% improvement) is genuinely supported by the data. This tension between a real contribution (DOWP) and an overclaimed packaging (Free-MoE as "tuning-free") is the core dilemma the paper must resolve.

## Suggestions

1. **Reframe honestly.** Drop the claim of "no extra model parameters" and "completely tuning-free" for the entire Free-MoE framework. Instead, state clearly: *the LLM backbone remains frozen (no gradient updates), but a lightweight router is trained on domain-labeled data.* The DOWP algorithm itself does not train the model, which should be the selling point.

2. **Add comparisons against other MoE gating methods.** To substantiate the claimed advantages over Sparse MoE and Domain-Mapping & Random Gating, include experiments with a standard top-1/top-2 router (trained on the same domain data) using the same frozen backbone and DSS-Experts.

3. **Acknowledge and explain why Free-MoE underperforms DOWP alone.** This is the most confusing result in the paper. Either the router needs better training/integration, or Free-MoE should be presented as a trade-off (slightly lower accuracy for the ability to handle multiple domains dynamically) rather than a pure improvement.

4. **Report error bars or variance across runs.** With 1–3% gains and sensitivity to hyperparameters, at least 3 random seeds with standard deviations would greatly increase confidence in the results.

5. **Specify the posterior probability computation** (Eq. 1) or remove the formalism if it is simply nearest-centroid assignment — the current presentation gives the appearance of a well-defined probabilistic model that does not exist.
