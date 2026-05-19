- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 8, 5
Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes a stagewise training framework called **progressive subnetwork training**, and a concrete instantiation **RAPTr** (Random Part Training) for efficient pretraining of LLMs. The key idea is to train on progressively larger random subnetworks of the model over stages (starting small, ending with the full network), instead of dropping more layers later (as in PLD) or growing the model (as in stacking). The paper provides a theoretical analysis of loss stability at stage transitions — the first such analysis for dropping-based training — and claims strong empirical results: up to 33% FLOP reduction on BERT, 1.2× speedup on UL2-1.6B, and 1.5% downstream improvement.

## Strengths

- **First theoretical analysis of stage-transition stability for dropping-based training.** Theorem 1 (informal) and Lemma 1 in §4 characterize conditions under which RAPTr yields smooth loss transitions. The analysis connects stability to architectural components (residual connections, layer normalization) and shows the loss gap scales as O(1/√L) for linear residual networks with layernorm. This is a genuinely novel theoretical contribution for a class of methods that previously lacked any formal transition analysis.

- **Clear and principled framework that generalizes prior dropping methods.** The paper formalizes progressive subnetwork training with explicit definitions of (p, F)-subnetworks and stagewise schedules (§2). The framework subsumes prior layer dropping as special cases and extends naturally beyond depth to other model axes (width, etc.), providing a foundation for future work.

- **Honest and thorough limitations discussion.** Section 7 explicitly acknowledges that the theory does not explain the observed loss decrease at transitions, that schedule selection is not well understood, and that the role of initial full-model warmup and the desirable inductive biases remain unexplained. This transparency is rare and valuable.

- **Practical wall-clock speedup strategies.** The paper notes implementation techniques for translating FLOP savings into actual speedups in distributed settings (contribution bullet 4), addressing a real pain point where naive skipping implementations fail to accelerate training.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The theoretical analysis addresses a secondary question (stability), not the primary claim (superiority over stacking).** The theory in §4 shows that the loss gap between stages is bounded under reasonable conditions. This is useful for establishing the method's plausibility, but it does not directly support the paper's headline claim that dropping strategies can be "competitive, if not better, than stacking methods." A theoretical comparison to stacking (e.g., relating the dynamics or convergence properties) is absent. The authors acknowledge this in the limitations section ("the current analysis provides insights into loss stability at stage boundaries but does not explain the observed decrease in loss during transitions"), which mitigates the concern, but the gap between the theoretical contribution and the paper's central empirical thesis remains a structural weakness.

- **RAPTr is a modest modification of stochastic depth.** RAPTr is essentially stochastic depth where the keep-probability increases over stages instead of remaining fixed. The paper correctly notes this distinction in the related work (§6), but the conceptual advance is incremental. The novelty of the paper rests primarily on the framework, the theoretical analysis, and the empirical validation — the method itself is straightforward. A well-tuned constant-probability stochastic depth baseline at an equivalent average FLOP budget would help isolate whether the *progressive* element specifically provides the claimed benefits. This ablation is not present in the available text.

- **The "loss improvement" claim is empirical, not theoretically supported.** The boxed text (§4, lines 164–167) states that "L₂(F) is lower than L₁(F)" — meaning the loss *improves* at stage transitions, going beyond mere loss preservation. This is presented as an observation without formal proof or theoretical justification. The theory only bounds the loss gap; it does not predict directional improvement. As an empirical finding this is interesting, but it is framed in a way that could be mistaken for a theoretical result. Clarifying its empirical status would help readers calibrate expectations.

- **No comparison against constant-probability stochastic depth at matched FLOP budget.** Since RAPTr is so closely related to stochastic depth, a direct comparison would clarify whether the increasing schedule (vs. fixed) is responsible for the reported gains, or whether any subnetwork training at those FLOP levels would yield similar results. This is the most actionable missing experiment.

### Trivial

- The paper does not discuss whether or how the learning rate is adjusted at stage transitions. Stagewise training methods often require warmup or LR reset at boundaries; this silence is a minor oversight given that the paper mentions "initial full-model warmup for UL2" in the limitations without elaboration.

## Nice-to-Haves

- An ablation comparing RAPTr to fixed-probability stochastic depth at matched average FLOP budget to isolate the effect of the progressive schedule.
- Extending the theoretical analysis to at least sketch why the method might improve downstream *generalization* beyond perplexity (currently only stability is addressed).
- Discussion of learning rate schedule management across stage transitions.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Experimental evidence is unavailable in the provided text"** (from harsh critic): The experimental sections (`\input{bert_expts}`, `\input{ul2_expts}`, etc.) are absent from the text extraction, but this is a parser artifact. The content exists in the original submission. The paper's empirical claims about BERT and UL2 should be evaluated from the full submission, not from an incomplete extraction.
- **"The polynomial toy setting is insufficient"** as a criticism about missing content: The polynomial analysis is in a `\input` section not extracted. The paper uses it as motivating intuition, not as proof. Any judgment about its sufficiency requires seeing the actual analysis.
- **Missing related works** (potential): Not included as I cannot verify the existence of omissions independently.
- **Formatting nitpicks** (inconsistent `\layerdrop` usage, etc.): These are parser extraction artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not reveal a perspective on the paper that the authors have not already identified or addressed. The harsh critic's main actionable concern — the method's closeness to stochastic depth and the missing fixed-probability ablation — is a valid point the authors should address, but it is not a novel framing the authors would be unaware of. The strength finder's emphasis on the theoretical stability analysis as a genuinely first-of-its-kind contribution is worth highlighting, but it directly reflects the paper's own framing.

## Suggestions

1. **Add a direct ablation:** Compare RAPTr against a version with *fixed* random path probability at the same average FLOP budget. This is the single most informative experiment for establishing that the progressive (increasing) schedule is the source of benefit rather than subnetwork training in general.

2. **Clarify the status of the "loss improvement" claim.** The boxed text in §4 states that L₂(F) < L₁(F) as an empirical finding. Make explicit whether this is consistently observed or varies across runs, and whether it has any theoretical basis or is simply an observed phenomenon.

3. **Discuss learning rate management across stages.** Even a brief note on whether the LR is reset, warmed up, or held constant at stage boundaries would address a natural concern about confounding factors in stagewise training.
