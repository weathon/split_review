## Summary

This paper introduces Conditional Activation Steering (CAST), a framework that extends activation steering by adding *condition vectors* — steering vectors extracted from hidden states that serve as triggers for selectively applying behavioral steering (e.g., refusal) only when the input matches a target condition. The method is evaluated across 7 LLMs, demonstrating selective refusal of harmful prompts while maintaining low refusal rates on harmless ones, logical composition of multiple conditions (OR, negation via flipped comparison directions), and domain-constraining behavior.

## Strengths

1. **Selective refusal demonstrated consistently across 7 models.** Table 1 shows, e.g., Qwen 1.5 Chat harmful refusal increasing from 45.8% to 90.7% while harmless refusal only rises from 0.0% to 2.2% — a discrepancy of 88.5% that exceeds both safety-aligned reference models. This pattern holds across architectures (Llama, Qwen, OLMo, Mistral, etc.), supporting the method's generality.

2. **Logical composition of conditions enables programmable refusal rules.** Figures 4–6 show OR-composition (e.g., hate *or* legal advice triggers refusal), negation via flipped comparison direction (duality), and concurrent addition/removal of refusal for different categories. Figure 6b further shows domain-constraining via negation generalizes to unseen harm categories (gambling, malware), with effectiveness correlating to semantic distance (Figure 6c).

3. **Data- and compute-efficient.** Figure 3a shows performance plateaus quickly with sample size, and Figure 3b shows linear time scaling. The paper notes most experiments are replicable within an hour, with grid search being the main cost (Section 3.1). No weight updates are needed.

4. **Duality and modulation properties provide systematic control.** Figure 3d (properties figure) shows flipping the comparison direction intervenes on the exact complement set. Threshold θ allows tightening or loosening the guardrail (Figure 3a–c). These are empirically demonstrated and add practical flexibility beyond prior activation steering.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Condition-checking token position during inference is underspecified.** The paper describes how condition vectors are *extracted* (average over all tokens, line 253), and describes that the condition is checked via `sim(h, proj_c h)` during inference (lines 146–148), with the behavior vector added "when the condition is activated" (line 143). However, it never specifies *which token position's hidden state* is used as **h** during the condition check at inference time — e.g., the last prompt token, the first generated token, or an average over prompt tokens. This ambiguity makes exact reproduction dependent on guessing this detail. The paper should make this explicit (likely the last prompt token, as is standard in activation steering work).

2. **No comparison of PCA-based condition detection to a trained linear probe.** The condition detector uses PCA's first principal component to define the direction for condition similarity. The critic's concern that PCA maximizes variance (not class separability) is technically correct; a trained linear probe on the same hidden states would be a natural baseline. While PCA is simple and does not require training data labels beyond the contrast pairs, and the paper demonstrates *that* the approach works well, it does not establish *how close to optimal* the PCA direction is. Including one such comparison (even on a single model/condition) would strengthen the evaluation.

3. **The "logical composition" description slightly overclaims.** The paper describes "logical composition of condition vectors" (Section 5), but the implementation checks each condition independently and applies the behavior if any trigger fires (OR of independent binary decisions, Section 3.1 "Multi-conditioning"). This is not a composition of the vectors *themselves* but rather a coordination of independent condition checks. The prose should clarify this to avoid implying vector-level algebraic composition.

### Trivial

- The claim that CAST "maintains normal responses to other content" (abstract) is supported by low harmless refusal rates, which is a meaningful proxy. However, since the method does not modify activations when the condition is not triggered (`f=0` means `h' = h`, lines 110–113), the model's standard forward pass is literally preserved for non-triggered inputs. A brief note clarifying this mechanism would preempt concerns about hidden quality degradation.

## Nice-to-Haves

- A sensitivity analysis comparing different token positions for condition checking (last-token-only vs. full-prompt average) would further strengthen reproducibility.
- Evaluating on one established non-synthetic harmful-prompt benchmark (e.g., AdvBench or a real-world moderation dataset) would test generalization beyond machine-generated categories — though Sorry-Bench is a reasonable and established benchmark.

## Removed Points

- **Harsh Critic Point 1** (insufficient evidence that non-refused responses remain normal): The critic's concern that condition-checking could "subtly alter hidden-state trajectories even when the condition is not triggered" is factually incorrect given the paper's mechanism — when `f=0`, the hidden state is unchanged (`h' ← h`, line 110). The paper additionally provides harmless refusal rates (Table 1) as evidence. This is not a structural flaw; the claim is well-supported by the method's design and the refusal-rate evidence.
- **Harsh Critic Point 3** (evaluated only on synthetic harmful prompts): Sorry-Bench is an established, published benchmark for harmful content. Demanding additional real-world benchmarks is scope creep — the paper's contribution is the framework, not a deployed safety system.
- **Formatting/style nitpicks** and **typos/grammar concerns**: These are parser artifacts, not author errors.
- **Missing related works**: Cannot be verified without external sources.

## Novel Insights

The most interesting observation from the reviews is the tension between the paper's clear *methodological* contribution (condition vectors enable programmable conditional steering simply and efficiently) and the valid reproducibility gap around the token-position detail for condition checking. This is a case where a single missing implementation detail could prevent exact replication despite the paper otherwise being well-specified. The fact that the condition detector uses PCA (unsupervised, no training labels) rather than a trained probe is also noteworthy — this is both a strength (simplicity, no extra training) and a limitation (unclear how close to optimal the direction is), and the paper could lean into this trade-off more explicitly.

## Suggestions

1. In Section 3.1, add an explicit statement of which token position's hidden state is used for the condition check during inference (e.g., "we use the hidden state at the last prompt token position at the chosen layer **l**").
2. Add a brief discussion or a single experiment comparing PCA-based condition detection to a trained linear probe on the same hidden states, even if only as an ablation.
3. Clarify in Section 5 that "logical composition of condition vectors" refers to composing *decisions* from independent condition checks, not composing the vectors algebraically.

## Score and Decision

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>