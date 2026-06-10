## Summary

This paper proposes LLM-Streamline, a two-stage layer pruning method for LLMs: (1) identify and remove a contiguous block of low-importance layers using cosine similarity between input/output hidden states, and (2) train a lightweight network (FFN, SwiGLU, or Transformer layer) on an MSE objective to approximate the pruned layers' function. Additionally, the paper proposes a "stability" metric that weights prediction consistency by the original model's prediction confidence, arguing that standard accuracy can overestimate compression quality. Experiments on Llama2-7B/13B across 12 classification and 3 generation benchmarks show competitive or superior results relative to LLM-Pruner, SliceGPT, and concurrent layer-pruning methods, while requiring substantially less training data (30K samples) and GPU memory.

## Strengths

- **Layer replacement is clearly more resource-efficient than LoRA-based fine-tuning while achieving better or comparable accuracy.** The LoRA comparison (Table 6, labeled `tab:PostTraing_PPL`) shows Layer-First consumes 27.8 GB GPU memory vs. LoRA's 56.4 GB (roughly 2× less), yet achieves 46.7% accuracy and 85.7% stability vs. LoRA's 44.5% and 82.1%. This directly supports the paper's efficiency claim.

- **The method requires dramatically less training data than concurrent layer-pruning approaches.** Table 7 reports 30K samples from SlimPajama, compared to Shortened Llama's 627B tokens + 50K Alpaca samples and LaCo's 1B unpublished samples. This is an important practical advantage that the paper demonstrates concretely.

- **The analysis of accuracy's blind spots is empirically grounded.** The paper shows (Section 3, Table 1a/b) that on datasets like Race-M and Race-H, accuracy increases after pruning, and that FP (originally wrong, now correct) samples have lower PPL standard deviation — indicating lucky guesses. This motivates the stability metric with real evidence rather than just speculation.

- **Broad and informative evaluation.** Results span 12 classification benchmarks and 3 generation benchmarks across two model scales (7B and 13B), with comparisons against LLM-Pruner, SliceGPT, LaCo, and multiple ablations. The inclusion of both accuracy and stability metrics provides a more complete picture than either alone.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The "pioneer work" framing in the abstract is an overclaim.** The paper itself cites five concurrent layer-pruning works (SLEB, ShortGPT, UIDL, LaCo, Shortened Llama) at lines 42–43 and in the Related Work section, and acknowledges that Ours (None) is equivalent to ShortGPT/UIDL (line 217). Calling LLM-Streamline "a pioneer work on layer pruning" is inconsistent with the paper's own cited literature. While the specific layer-replacement approach is novel, the blanket claim should be corrected.

- **On Llama2-13B classification, the lightweight replacement network underperforms direct layer removal in accuracy**, and the paper's explanation is incomplete. Table 1 shows Ours (None) at 54.5 (95.6% RP) vs. Ours (FFN) at 53.2 (93.3%) and Ours (Layer) at 53.1 (93.2%). The paper attributes this to accuracy overestimation (line 361–362), and stability does favor the replacement variants (84.9% vs. 81.1%). However, the paper never explains *why* this happens specifically for 13B classification but not for 7B classification or for generation tasks. Since the central claim is that replacement "mitigates performance loss" (abstract), this discrepancy warrants a clearer mechanistic explanation.

- **Training hyperparameters for the lightweight network are not reported.** No learning rate, optimizer, batch size, or training details are provided beyond "10 epochs" mentioned in the validation loss discussion (line 372). This makes the work harder to reproduce. Given that the lightweight network training is a core contribution, these details should be included.

- **The claim that cosine similarity is "highly stable" and "always leads to the same pruned layers on different pre-training data" (Discussion II, line 88) is asserted without empirical evidence.** The paper provides no experiment showing that pruning decisions remain invariant under different data sources. This weakens an otherwise reasonable argument for preferring cosine similarity over perplexity.

- **GSM8K evaluation protocol is unclear.** The dense Llama2-7B scores only 16.5% and Llama2-13B scores 29.0%, far below typical reported values (~30% and ~50% with 8-shot CoT). The paper states these results follow OpenCompass (line 214) but does not describe the evaluation protocol (few-shot, chain-of-thought, perplexity-based selection). Since all pruning methods score below 5%, the benchmark provides little signal for comparing methods, and the paper should clarify the setup.

- **The pruning ratio / compression rate definition is not explicitly stated.** The paper reports ratios like 24.0% (None), 25.0% (FFN), 24.0% (Layer) for Llama2-7B, which appear to be parameter-based (the lightweight network adds ~1% overhead). However, this is never stated explicitly, nor is it explained how many layers are removed. The tables compare against baselines at slightly different ratios (e.g., LaCo at 27.0%) without discussing whether the differences are meaningful. A clear statement of how ratios are computed would improve transparency.

- **Results for LaCo are cited from the original paper (marked with * in Tables 1 and 3) rather than reproduced.** Since LaCo is one of the most directly comparable methods (also layer pruning), differences in evaluation setup could affect the comparison. This is acknowledged in the tables but remains a limitation.

### Trivial

- The claim that "fine-tuning the model to make the original non-contiguous layers compensate for the performance degradation is not an easy task" (lines 44–45) is asserted as fact without supporting evidence. Either cite a source or soften the language.

- Line 363 has garbled text ("Baichuan2-13B.3B and OPT-2.7B}") — a formatting artifact in the extracted text.

## Nice-to-Haves

- Report error bars or multiple-seed results for key numbers, though single-run evaluation is standard for LLMs of this scale.
- Include results on the OPT and Baichuan models mentioned at line 363 in the main paper rather than only in the appendix.
- Provide a direct comparison with ShortGPT/UIDL plus LoRA under matched conditions, to strengthen the argument that layer replacement is preferable to fine-tuning the pruned model.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Stability metric is "inherently biased and methodologically unsound"** (Harsh Critic #1). *Reason for removal:* The method trains on MSE of hidden states (representation level), not on the stability metric (prediction level). LLM-Pruner uses gradient-based importance (also tied to preserving original outputs) and SliceGPT uses PCA (representation preservation). All pruning methods aim to preserve the original model's behavior. The critic's claim that the method "is designed to maximize this very quantity" is not accurate. Stability is a legitimate metric for any pruning method; the gap between Ours (None) at 73.2% and LLM-Pruner at 72.0% on Llama2-7B (Table 3) also shows that even without any training the proposed approach scores similarly, undermining the "inherent bias" argument. Removed per the rule: REMOVE criticisms that are factually wrong or misunderstand the paper, and WEAKEN strawman weaknesses.

- **Missing appendix results for OPT/Baichuan models** (Harsh Critic — part of #6 under Main Results). *Reason for removal:* Per hard rules: "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references. The parser strips those sections from all papers; they exist in the original submission."

- **No error bars / statistical uncertainty** (Harsh Critic — "No statistical uncertainty"). *Reason for removal:* Single-run evaluation is the standard for LLM pruning papers at this scale. Demoted to nice-to-have per soft rules: "MOVE TO NICE-TO-HAVE weaknesses that demand methodological practices not standard in the paper's field."

- **"The paper would need to substantially reframe its claims..." in Overall Assessment** (Harsh Critic). *Reason for removal:* This is an overall judgment that flows from the critic's rejected premises (stability bias as fatal, pioneer claim as decisive). Since those premises have been removed or downgraded, the conclusory paragraph is not usable.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Remove or soften the "pioneer work" language — the paper is a concurrent contribution to an active area, which is fine without the superlative.
2. Add a brief discussion of why the 13B classification accuracy anomaly occurs (e.g., does the lightweight network introduce a bottleneck for certain tasks at that scale?), and present it transparently rather than relying solely on the stability metric to explain it away.
3. Report training hyperparameters (learning rate, optimizer, batch size, number of epochs) for the lightweight network in the main text or a table.

## Score and Decision

**MY FINAL SCORE:** <score>6.5</score>
**MY FINAL DECISION:** <decision>Accept</decision>