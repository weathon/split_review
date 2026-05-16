Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces Mixture-of-Instructions (MoI), a multi-task supervised fine-tuning method that combines three components: (1) task-specific system prompts, (2) balanced sampling for instruction packing, and (3) chunk-based attention masking to limit cross-contamination between different domains. Applied to Qwen-7B-chat, the resulting model (Qwen-SFT-MoI) shows improvements across coding (HumanEval, MBPP), mathematics (GSM8K, MATH), tool use (T-Eval), and dialogue (MT-Bench) compared to several baselines.

## Strengths

1. **Demonstrates that system prompts can resolve knowledge conflicts during SFT.** The paper provides concrete evidence via attention map analysis (Figure 2) showing that changing the system prompt from a general one to "You are a programmer" shifts the model's attention from irrelevant operations to the correct algorithmic concept. Table 3 further quantifies the benefit of prompt engineering on code benchmarks.

2. **Systematic ablation with independent validation of each component.** Individual components are validated through separate experiments: balanced sampling improves GSM8K and stabilizes code performance (Figure 5), and chunk-based attention masking preserves code/math gains from packing while improving complex reasoning on T-Eval (Table 8). Table 2 shows the combined method achieves the highest average score across seven benchmarks.

3. **Generalization across model families and sizes.** The method is tested on Llama2-7B, Llama3-8B, and Qwen1.5 (1.8B, 4B) in Tables 6 and 7, demonstrating applicability beyond the primary Qwen-7B-chat model.

4. **Weight-swapping analysis provides mechanistic insight.** Table 9 shows that replacing attention weights from the chat model with MoI-trained weights causes a performance drop not seen with other SFT models, supporting the claim that MoI produces a qualitatively different attention distribution.

## Weaknesses

### Fatal
None.

### Major

1. **System prompt confound in the main multi-task comparison (Table 2).** The paper assigns custom system prompts to each task domain (line 120: "providing a specific system prompt for each"). MoI uses these custom prompts as part of its method. However, the paper **never states whether the "Sequence", "Packing", and "Balance" baselines in Table 2 also used the same task-specific system prompts during training or a single default prompt.** If the baselines used a single prompt while MoI used custom prompts, the performance gain attributed to chunk-based attention masking could be partially or largely due to the multiple system prompts — especially since Table 3 shows that changing prompts alone can boost code benchmarks by several points. This is the single most important confound in the paper, and resolving it (e.g., adding "Balance + custom prompts" and "MoI with default prompt" conditions) would substantially strengthen the core claim. *This is not fatal — the individual components are independently validated — but the central comparison as presented is ambiguous.*

2. **Loss function notation is unclear and may contain inconsistencies.** Equations (3)–(7) in Section 2.4 are difficult to parse. Specifically: (a) In Eq. (3), the notation `|y_i|` where `i` iterates over token positions is confusing — if `y_i` is a single token, `|y_i| = 1` makes the division vacuous; if it means the response length of the containing instruction, this needs explicit definition. (b) The relationship between the general form (Eq. 4/6) and the "ideal scenario" reduction (Eq. 7) is not mathematically clean — the constants don't obviously cancel to yield the claimed equivalence. (c) The MoI loss (Eq. 8) uses indexing `L_n / n_mix` as summation bounds, which mixes index types. These issues make faithful reimplementation harder than it should be. A pseudocode listing or cleaner derivation would resolve this.

### Minor

1. **Knowledge conflicts demonstrated via a single example.** The Boyer-Moore example (Section 2.1) is compelling but is the only quantified instance of the "knowledge conflict" phenomenon the paper claims to address. The paper would be stronger with a broader analysis of how often such conflicts arise and how reliably system prompts resolve them.

2. **No comparison to established multi-task SFT recipes.** The paper cites Flan-T5 (Chung et al., 2024), MixInstruct-adjacent work, and Liu et al. (2024) but does not include a temperature-based mixing or multi-task loss-weighting baseline. Since the paper's contribution is a method for multi-task SFT, a controlled comparison against a standard multi-task fine-tuning approach (same data, same model) would better establish the significance of MoI over existing paradigms, not just over single-task or packed baselines.

3. **Implementation details missing for reproducibility.** The description of how instructions are concatenated (order within packed sequences, handling of sequence-length cut-offs, how partial chunks are managed when instruction counts don't evenly divide) is absent. The chunk size is stated as 4 instructions for the 4-domain case, but the paper does not discuss how this generalizes.

4. **No discussion of limitations.** The paper does not address when MoI might fail, how it scales beyond 4 domains, how chunk size should be chosen, or what happens with domains that don't naturally map to distinct system prompts. A brief limitations paragraph would improve credibility.

5. **Comparison to open-source models is illustrative, not controlled.** Table 4 shows Qwen-SFT-MoI "matches the performance of contemporary code models" but training data size, compute budget, and base model pre-training are not matched. This is acknowledged implicitly ("despite the lack of extensive code pre-training") but the claim should be qualified more explicitly as a demonstration rather than a controlled comparison.

### Trivial
None.

## Nice-to-Haves

- A controlled ablation separating the effect of custom system prompts from chunk-based attention masking (the core confound described in Major weakness 1).
- A pseudocode or reference implementation for the loss function and chunk-based attention masking.
- Variance estimates or multiple-seed results for the main benchmarks.
- Report raw MT-Bench scores alongside the scaled values (the x10 scaling is explained but non-standard).
- Broader quantification of the "knowledge conflict" phenomenon beyond a single example.

## Removed Points

These points were flagged by reviewers but are removed from the main assessment for the reasons stated:

- *"No code release or reproducibility artifact"* — Removed per hard rule: requesting complete code release as a condition for evaluation is not standard for conference submissions; the paper describes sufficient methodology for a motivated practitioner to implement, even if the notation could be cleaner.
- *"The paper does not quantify 'knowledge conflict' beyond this single example" / "only one instance is shown"* — These were merged into Minor weakness 1 above (the single-example limitation is real but not a central flaw).
- *"Table 9 interpretation is speculative"* — The paper explicitly says "We hypothesize" (line 302), so there is no overclaim; the experiment is presented as a diagnostic, not a proof.
- *"Comparison with open-source models... should be qualified"* — The paper already qualifies with "despite the lack of extensive code pre-training" (line 281); kept as Minor weakness 5 with softened framing.
- *"Missing parts and places to improve" points about evaluation protocol ambiguities for the base model* — The paper states all evaluations used "You are a helpful assistant." This is applied uniformly, so there is no asymmetry harming the base model.
- *"No discussion of failure cases or limitations"* — Kept as Minor weakness 4 (genuine omission).
- *Generic strengths from Strength Finder* — Strength Finder's Core Strength 3 ("Ablation studies isolate the effect of each MoI component") is downgraded: it partially conflicts with the verified system prompt confound. While the independent ablations (Figure 5, Table 8) are clean, the Table 2 comparison is confounded. The strength is still acknowledged (Strengths point 2) but not in its original strong form.

## Novel Insights

The reviews surface one genuinely novel observation beyond the paper's own contributions: the interaction between system prompts and attention masking creates a non-obvious trade-off where full isolation (no cross-contamination) hurts code/math while helping reasoning, and chunk-based isolation is a practical compromise. This was present in the paper's Table 8 but the reviewers' focus on the confound inadvertently highlights that the *most robust* result in the paper is actually the attention mask ablation, not the final MoI comparison — which is a useful prioritization signal for the authors.

## Suggestions

1. **Add one controlled condition to Table 2**: Train "Balance" with the same custom system prompts used by MoI, or train "MoI" with a single default system prompt. This separates the contribution of chunk-based attention masking from system prompt engineering.
2. **Clean up the loss notation**: Replace the current equations with a pseudocode listing or a simpler mathematical formulation. Clearly define whether `|y_i|` means per-token or per-instance response length, and verify the "ideal scenario" reduction actually holds.
3. **Add a standard multi-task SFT baseline** (e.g., temperature-based mixing without packing) to ground the significance claim.
4. **Add a brief limitations paragraph** addressing scaling to more domains, chunk-size selection, and scenarios where MoI might not help.

## Score and Decision

The paper identifies a real problem (multi-task SFT often degrades some abilities while improving others) and proposes a plausible combination of ideas. The individual components are validated independently, and the method generalizes across model families. However, the central experimental comparison in Table 2 has a confound (system prompts not controlled) that muddies the interpretation of the main result. This is fixable but means the current evidence does not fully support the claimed advantage of the full MoI method over simpler alternatives. The paper is on the right track but needs one critical ablation to substantiate its core thesis.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>