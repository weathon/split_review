## Summary
The paper investigates why LLM safety alignment fails under jailbreak attacks, arguing that existing alignment relies on shallow refusal heuristics rather than deep reasoning. Through a causal intervention—identifying reasoning-critical attention heads via linear probing and deactivating them—the authors empirically show that safety performance remains stable while reasoning degrades, suggesting alignment does not depend on reasoning. Motivated by this finding, they (1) construct and release a Chain-of-Thought (CoT) safety fine-tuning dataset and (2) propose **Alignment-Weighted DPO (AW-DPO)**, a method that decomposes each response into reasoning and response segments and assigns data-driven preference weights to each, enabling more fine-grained alignment training.

---

## Strengths

- **Empirically motivated causal study**: The linear-probing + neuron-deactivation experiment is creative and well-executed. Showing that zeroing top-10% reasoning-critical attention heads strongly degrades reasoning accuracy (near-chance) while leaving alignment accuracy near 100% across both LLaMA-2-7B-Chat and Mistral-7B is a clean, reproducible result consistent across two model families and confirmed by t-SNE visualizations. The experiment cleanly formalises the "superficial alignment" hypothesis.

- **Novel, principled method**: AW-DPO is a genuine extension of DPO. Decomposing the DPO reward into separately masked reasoning and response sub-rewards and then reweighting them by the *relative* harmfulness improvement across those segments is a well-motivated, mathematically clean design (Eqs. 3–4). The approach targets the fine-grained failure modes identified empirically and is more interpretable than heuristic token-masking schemes.

- **Comprehensive experimental coverage**: Table 1 spans four model families (LLaMA-2-7B, LLaMA-3.2-3B, LLaMA-3.1-8B, Mistral-7B-v0.3) against six baselines, evaluated on SorryBench (20 jailbreak attacks, 44 harm categories). Table 2 includes strong recent baselines (SAFECHAIN, Representation Rerouting, STAIR). The comparison with Phi-4-Reasoning models (§5.3) is a particularly interesting negative result: general reasoning capability does not transfer to alignment-specific robustness.

- **Transferability analysis**: Table 3 shows that an AW-DPO preference dataset constructed with LLaMA-2-7B generalises to other architectures with only a minor performance drop. This is a practically useful contribution and reduces dataset-construction overhead.

- **Dataset release**: A long-form CoT safety fine-tuning dataset is open-sourced, which directly benefits reproducibility and downstream research.

---

## Weaknesses

### Fatal
None.

### Major

1. **Causal intervention conclusions are overstated.** The core claim is that alignment is "superficial" *because* it does not involve reasoning. However, finding that reasoning neurons (top-10% heads by reasoning probing accuracy in layers 0–11) are *different* from safety-representation neurons does not imply that refusals are shallow—it could simply mean that the two capabilities are laterally specialised. The experiment conflates "alignment and reasoning are separable in representational space" with "alignment lacks genuine understanding." A stronger version would show that the model, after neuron deactivation, still refuses prompts despite now being unable to correctly explain *why* they are harmful, which would require a semantic evaluation of the refusal rationale, not just a classification-accuracy probe.

2. **Utility gap versus STAIR is not adequately explained.** Table 2 shows that "Ours (Base)" achieves 0.81% average ASR—marginally better safety than STAIR-DPO-3 (1.13%)—but at 58.27% MMLU versus 73.34%, a gap of 15 percentage points. The authors attribute this to STAIR using an instruct model and three training rounds, but "Ours (Instmct)" still yields only 65.29% utility. A discussion of *why* the single-round approach substantially degrades MMLU despite comparable safety is missing and is a practical limitation users need to understand.

3. **The 15% failure-mode argument inadequately justifies the full AW-DPO mechanism.** Figure 3a shows that the targeted failure modes (correct reasoning + unsafe response, or incorrect reasoning + safe response) account for approximately 15% of jailbreak failures. The rest (85%) are standard full-response failures addressed by vanilla DPO. However, AW-DPO applies the weighted loss to *all* preference pairs, not just the 15%. The paper does not rigorously show that the weighting scheme specifically corrects the 15% marginal cases; the overall ASR improvement could equally result from better preference pair selection or other confounders.

4. **Weight formulation has unaddressed edge cases.** $W_{reasoning} = d_{reasoning}/(d_{reasoning}+d_{response})$ is undefined or numerically degenerate when both differences are near zero (pairs where reasoning and response quality are similar). Similarly, it is not discussed what happens when one difference is negative (e.g., the chosen response has a *worse* reasoning trace than the rejected one), which can occur if the full-response score difference exceeds threshold γ but the reasoning sub-scores are inverted.

### Minor

1. **Learning rate sensitivity is severe.** Table 5 shows that changing lr from 1×10⁻⁶ to 5×10⁻⁶ collapses MMLU utility from 48.52% to 26.09%. Without guidance on selecting the optimal lr, the practical utility of the method is uncertain; the good results in Table 1 depend heavily on hitting a narrow optimal hyperparameter.

2. **Judge model for harmfulness scoring is underspecified.** The paper states "another LLM as a judge" assigns harmfulness scores but does not name the model, provide the scoring rubric, or validate inter-rater agreement. The quality of preference pair construction and alignment weights depends entirely on this judge.

3. **Linear probing methodology conflates task difficulty and neural representation.** The fact that alignment probing achieves near-100% accuracy in all layers while reasoning probing improves only in later layers may reflect the intrinsic difficulty gap between binary toxicity classification and mathematical reasoning, rather than the depth of the model's alignment understanding.

### Trivial

- The denominator of the "15% failure cases" statistic is ambiguous—whether this is 15% of all responses or 15% of jailbroken responses changes the practical significance.

---

## Nice-to-Haves

- A semantic evaluation of the *quality* of the model's reasoning in safety refusals (e.g., does the model correctly articulate *why* a prompt is harmful after CoT training?) would make the causal claim and the CoT improvement more compelling.
- A wall-clock or FLOPs comparison with STAIR-DPO-3 would substantiate the efficiency argument.
- Clarifying how the weight formula handles near-zero or negative differences, and adding a small ablation (e.g., clipping or softmax normalisation) would strengthen the method.

---

## Novel Insights

The most genuinely novel observation is the dissociation between reasoning and alignment neurons demonstrated via causal intervention: deactivating the top-10% heads responsible for reasoning in early layers destroys reasoning probing accuracy (dropping to chance) while leaving alignment probing accuracy essentially unchanged. While the causal conclusions are overinterpreted, the *diagnostic fact* itself—that alignment representations are robust to severe reasoning-capacity degradation—is non-trivial and contributes to mechanistic understanding of LLM safety. Paired with the Phi-4 comparison (§5.3), which shows that general-purpose reasoning models with strong benchmark performance are *more* vulnerable to jailbreaks, this constitutes a useful empirical contribution: alignment-specific reasoning must be cultivated explicitly and cannot be outsourced to general reasoning capability.

---

## Suggestions

- Reframe the causal intervention section more precisely: it shows that safety representations are *decoupled* from reasoning neurons, not that refusals lack genuine understanding—these are distinct claims requiring different evidence.
- Add a semantic analysis (e.g., using a judge to rate refusal explanations) to directly demonstrate that CoT training produces more principled refusals, which would validate the mechanism rather than only the outcome.
- Provide explicit handling (and an ablation) of edge cases in the weight formula (near-zero denominator, negative differences).
- Report a compute-normalised comparison with STAIR-DPO-3 to justify the efficiency claim.
- Investigate the source of the MMLU gap vs. STAIR and discuss mitigation strategies; this is a meaningful practical limitation.

---

## Score and Decision

The paper tackles an important and timely problem, proposes a principled novel extension of DPO, covers experiments across four model families, and contributes an open-sourced dataset. These are meaningful contributions. However, the primary mechanistic claim (causal intervention → "alignment is superficial") is not as tightly supported as stated; the utility gap compared to the strongest baseline is large and underexplained; and the 15% motivation for the full AW-DPO weighting scheme requires stronger grounding. These issues collectively prevent a clear acceptance recommendation in the current form.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>