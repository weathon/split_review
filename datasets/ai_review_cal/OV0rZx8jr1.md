- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have all the information needed. Let me produce the consolidated review.

## Summary

This paper proposes PFP (Preference Feature Preservation), a framework that mitigates bias accumulation during online preference learning for LLMs. The key idea is to extract human preference features (e.g., tone, style, informativeness) from binary preference data, train a classifier to map input instructions to these features, and inject them via instruction-specific system prompts during response generation and preference judgment. The distribution of assigned features is preserved across iterations using a Sinkhorn-Knopp adjustment to match the seed data distribution. Experiments on AlpacaEval 2.0 and MT-Bench using Mistral-7B show that PFP outperforms Iterative DPO and SELFEE while almost eliminating length bias (1138→1187 tokens vs. 1852→2412 for SELFEE).

## Strengths

1. **Novel and well-motivated approach to an important problem**: The paper identifies a real issue — that online preference learning causes models to drift toward majority-preferred features (e.g., length, majority biases) — and proposes the clean idea of explicitly extracting and preserving preference feature distributions throughout iterations. The conceptual framing (Fig. 1) is effective.

2. **Strong empirical results with simultaneous bias reduction**: PFP achieves the highest AlpacaEval 2.0 length-controlled win rate (15.24%) compared to Iterative DPO (13.13%) and SELFEE (14.23%) (Table 1), while response length remains nearly constant across 4 iterations (1138→1187 tokens), unlike baselines which show large increases (SELFEE: 1852→2412) (Fig. 5a). This directly supports the claim that bias mitigation does not come at the cost of performance.

3. **Demonstrated distribution preservation across iterations**: Figure 4 shows that PFP maintains near-constant KL divergence of preference feature distributions from the initial model across all iterations, while Iterative DPO and SELFEE show steadily increasing divergence — direct empirical validation of the core mechanism.

4. **Thorough ablation studies isolating each component**: Tables 2 and 3 systematically ablate the classifier, distribution-preserving relabeling, double-prompt sampling, and scheduling, showing each contributes positively. Notably, the ablation reveals that random-feature system prompts (SP-only, 12.38) actually underperform SELFEE (14.23), while the classifier (14.8) and relabeling (15.24) progressively improve — this is informative internal evidence that the feature mapping, not just prompt injection, drives gains.

5. **Outperforms explicit length-bias mitigation baselines**: Table 4 shows PFP (15.24%, 1187 tokens) beats R-DPO and length penalty methods applied to Iterative DPO (best: 12.03%, 1758 tokens), demonstrating that the approach is more effective than heuristic length-control methods despite not being designed for length control.

## Weaknesses

### Fatal
None.

### Major

- **The comparison against baselines is confounded by the system prompt intervention.** PFP conditions response generation and preference judgment on instruction-specific system prompts derived from predicted preference features, while the baselines (Iterative DPO, SELFEE) operate with fixed/default system prompts. This means the main results (Table 1) compare methods that differ in two variables simultaneously: (a) the use of dynamic system prompts, and (b) the distribution-preserving feature mapping. The paper's ablations (Table 2) provide partial evidence that feature mapping drives the improvement — the SP-only random-feature condition (12.38 AlpacaEval) is *worse* than SELFEE (14.23), and adding the classifier (14.8) and relabeling (15.24) progressively improves. This suggests that prompts alone hurt and the feature mapping is the key contributor. However, the paper does not make this critical comparison explicit in the main results or directly test "SELFEE + the same system prompt injection mechanism but with random features." Cleaning this up would substantially strengthen the paper's core claim.

### Minor

- **The "debiasing" claim is narrower than it initially appears.** PFP preserves the preference feature distribution from the seed data (UltraFeedback), preventing *additional* drift during online iterations. But if the seed data itself contains biases (majority preference bias, length bias, etc.), preserving it does not remove existing bias — it only prevents further accumulation. The paper should clarify this scope distinction. The length bias results (Fig. 5a) show genuine improvement, but the "preference feature debiasing" is relative to the seed distribution, which may not be unbiased.

- **Feature extraction reliability is not validated.** The entire pipeline depends on features extracted by GPT-4o from binary comparisons, but the paper provides no analysis of extraction quality — no inter-annotator agreement between LLM judges, no validation against human judgments, no discussion of ambiguous cases or edge cases where feature assignment is uncertain. This is a gap for a method whose core contribution hinges on the quality of these features.

- **The feature classifier's accuracy is not reported.** The classifier is a critical component — it maps instructions to preference features, and its outputs are adjusted via Sinkhorn-Knopp. The paper does not report held-out accuracy, generalization performance, or confusion matrices on the seed data. This makes it hard to assess whether errors in the classifier propagate to downstream performance.

- **The KL divergence metric (Eq. 8) for measuring feature distribution shift is partially circular with the design objective.** PFP is designed to preserve the initial feature distribution, and the metric measures how well the model's responses maintain that distribution relative to the initial model. While it provides useful internal consistency evidence, it does not independently measure bias reduction. The paper uses other independent metrics (AlpacaEval, MT-Bench, response length), so this is not a fatal issue, but the interpretation of Fig. 4 should note this.

### Trivial

- The paper does not discuss the computational cost of the Sinkhorn-Knopp algorithm per iteration (operating on 5K × 5 matrices). This is a minor implementation detail worth noting.
- The paper does not examine sensitivity to the number of online iterations (only 4 are reported). Whether performance plateaus or length bias eventually creeps in with more iterations is an open question.

## Nice-to-Haves

- A direct experimental comparison of "baseline (SELFEE/Iterative DPO) with the same double-system-prompt sampling but using random or shared-default preference features" would cleanly isolate the contribution of the feature mapping from the system prompt injection mechanism.
- Validating feature extraction with inter-annotator agreement (e.g., between GPT-4o and another LLM, or on a human-annotated sample) would strengthen confidence in the pipeline.
- Reporting feature classifier held-out accuracy would help assess error propagation.

## Removed Points

These points were considered but are not included in the main weaknesses above:
- **"The same LLM family (GPT-4) is used as evaluator in AlpacaEval 2.0, creating alignment between extracted features and evaluation judge preferences."** — AlpacaEval 2.0 uses GPT-4 as the evaluator by design (it is a standard benchmark). The feature extraction uses GPT-4o (a different model). This concern is speculative and would apply to any method evaluated with AlpacaEval. Removed.
- **"If the batch is small or heterogeneous, distribution matching could force arbitrary decisions per instruction."** — The paper uses 5K samples per batch, and the critic acknowledges this is likely fine. Speculative concern without evidence of a problem. Removed.
- **Strength: "This paper addressed an important problem"** (from Strength Finder's generic framing) — Already covered in the review's assessment of importance. The remaining strengths in the list above are concrete and specific.

## Novel Insights

None beyond the paper's own contributions. The two reviews did not surface any novel perspective not already present in the paper itself.

## Suggestions

1. **Make the ablation comparison to baselines explicit**: In the main results or a dedicated table, directly compare SELFEE against a version of PFP with random/shared features (SP-only). The data exists in Table 2 but is not connected to Table 1. This would directly address the confound concern.

2. **Clarify the scope of "debiasing"**: Explicitly state that PFP prevents *additional* drift during online learning, while acknowledging that the seed distribution may contain its own biases. Discuss what would be needed to address seed-distribution bias.

3. **Validate the feature extraction pipeline**: Report inter-model agreement rates for GPT-4o feature extraction, or at minimum provide qualitative examples with reasoning. If resources permit, include a small human-validated subset.

4. **Report feature classifier performance**: Include held-out accuracy and per-class metrics for the DeBERTa-v3-large classifier trained on the seed data.

5. **Consider longer iteration runs**: Showing that PFP remains stable beyond 4 iterations would strengthen claims about long-term bias prevention.
