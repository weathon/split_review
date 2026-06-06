## Summary
Insertion Language Models (ILMs) learn to generate sequences by iteratively inserting tokens at jointly-predicted positions, combining the relative-position flexibility needed for out-of-order generation with the ability to produce variable-length sequences. The core claim is that ILMs overcome structural failure modes of both ARMs (rigid left-to-right order) and MDMs (fixed-length masking, simultaneous unmasking), supported by planning experiments and text generation benchmarks.

---

## Strengths

1. **Strong and convincing planning task results**: On Star_medium and Star_hard (variable-length star graphs), ILM achieves 100% and 99.1% exact match accuracy, respectively, versus MDM's 36.5%/21.0% and ARM's 75.0%/23.0% (Table 1). The explanation — that MDMs rely on absolute token positions making variable-length prediction intractably hard in one pass — is internally coherent and well-supported by the architectural analysis. Example trajectories in Appendix Figure 7 further reinforce the qualitative argument.

2. **Zebra puzzle results approaching oracle performance**: ILM achieves 90.0% on Zebra puzzles versus ARM's 81.2%, MDM's 82.6%, and even approaching ARM_oracle's 91.2% (oracle decomposed ordering). This is notable because ILM uses no oracle information about solution ordering, yet nearly matches a model given the optimal left-to-right order.

3. **Principled formulation and efficient parameterization**: The joint insertion distribution (Eq. 3–4) and the biased denoising objective (Eq. 2) are clearly motivated and practically tractable. The paper honestly characterizes the approximation's rationale (variance reduction over Monte Carlo trajectory sampling) and uses a single shared transformer backbone for both insertion and stopping decisions.

4. **Natural arbitrary-length infilling without specialized training**: Table 3 demonstrates ILM consistently outperforms MDM on ΔNLLgt across all three infilling settings (TinyStories single-segment: +12.27% vs. +14.36%; LM1B single-segment: +20.47% vs. +25.31%; LM1B multi-segment: +23.52% vs. +25.64%), and does so without requiring mask-count specification, which is a genuine practical advantage.

---

## Weaknesses

### Fatal
None.

### Major

- **Length confound in text generation evaluation**: Table 2 shows ILM generates sequences of mean length 119 on Stories (training mean: 205) and 21 on LM1B (training mean: 28). The paper correctly diagnoses MDM's severe over-generation (985 on Stories) as causing its poor NLL, but applies no symmetric scrutiny to ILM's systematic under-generation. Per-token NLL under a left-to-right LLM (Llama-3.2-3B) is not length-neutral: shorter text provides less opportunity for incoherence to accumulate, and the model evaluates fewer tokens, biasing NLL downward. The Prometheus judge scores (Figure 5) may similarly favor shorter, simpler texts on coherence and grammaticality. The paper does not attempt any length-controlled comparison, making it impossible to disentangle ILM's quality advantage over MDM from its length advantage. This doesn't necessarily invalidate the qualitative superiority over MDM, but the quantitative margin should be treated with caution.

- **Overclaimed competitiveness with ARM on text generation**: The abstract states ILMs "perform on par with ARMs" in unconditional text generation. Table 2 shows ILM achieves 4.67 vs. ARM's 3.94 on LM1B — an ~18.5% NLL gap that is substantial, not marginal. Only the Stories result (2.14 vs. 2.11) is genuinely competitive. Claiming uniform parity with ARMs, where the LM1B gap is material, overstates what the experiments show. The paper's Discussion more honestly acknowledges ILMs "still perform slightly worse than ARMs," which contradicts the abstract and introduction framing.

### Minor

- **Figure 6 comparison uses ARM without KV cache**: Figure 6 explicitly labels the baseline as "ARM (w/o KV cache)." ARM with KV cache — the standard deployment baseline — would be significantly faster per token, shifting ARM's curve leftward and making ILM's inference cost look less competitive in practical terms. The Discussion acknowledges "ILMs also do not allow caching of hidden states," but does not quantify the gap or reconcile it with Figure 6.

- **Stopping mechanism is underanalyzed given systematic under-generation**: ILM under-generates substantially on text tasks (119 vs. 205 tokens on Stories). The stopping classifier (trained via the `<stp>` token loss, Eq. above Eq. 3) is a novel component that controls sequence length but receives no ablation. Whether early termination comes from classifier miscalibration or from the generative model losing confidence is not explored. This weakens the paper's claim that flexible-length generation is a core advantage of ILMs over MDMs.

- **No confidence intervals on text metrics**: Tables 2 and 3 report point estimates with no variance or confidence intervals on relatively small evaluation sets (3,500 and 3,300 examples). For the Stories NLL comparison (2.14 vs. 2.11) — which the paper uses to support competitiveness with ARM — the margin is within plausible noise, and error bounds would meaningfully affect interpretation.

### Trivial
None identified.

---

## Nice-to-Haves

- A length-controlled comparison (e.g., truncating or length-conditioning generated sequences to the training mean before computing NLL) would cleanly separate generation quality from length artifacts and validate or qualify the claimed quality gap over MDMs.
- An ablation of the stopping threshold or a calibration analysis of the stopping classifier would strengthen the claim of flexible-length generation.
- Including ARM with KV cache in Figure 6 (even as a dashed "projected" line based on known speedup factor) would make the inference time trade-off more interpretable.
- For the text generation results, reporting NLL values at matched generation lengths would provide a cleaner apples-to-apples comparison.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Biased training objective incompletely characterized (harsh critic, framed as "major")**: The paper openly acknowledges the approximation in Section 3 ("we use a biased training objective...") and refers the reader to Appendix D for variance analysis. While the theoretical implications on the learned distribution are not fully characterized, this is a known practical necessity honestly disclosed. The empirical results provide sufficient evidence that the approximation works. Demoted from major to background context; not retained as a weakness because the paper is transparent about the choice.

- **MDM overstated as a structural failure vs. inference-time choice**: The critic argues that greedily unmasking one token at a time (a decoding strategy) would address the dependency-violation problem, making ILM's advantage less "fundamental." The paper does acknowledge inference-time approaches (Gong et al., 2024; Zheng et al.; Campbell et al.) in related work. However, the paper's MDM baseline uses the standard tau-leaping sampler (Sahoo et al., 2024) rather than greedy decoding, and the point about one-at-a-time MDM decoding being slow is explicitly made. This is a valid framing choice, not an error — removed as noise.

- **Strength Finder claim "ILM superior on coherence across all metrics" (generic)**: The Prometheus judge scores in Figure 5 do show ILM above ARM and MDM on most dimensions, but given the length confound, this is partially conflated with length. Retained as a conditional strength (ILM shows better judged quality than MDM), but the framing of "outperforms ARM" via judge scores should be read cautiously.

---

## Novel Insights

The most genuinely novel insight this paper contributes — beyond the method itself — is the diagnosis of MDM failure on variable-length planning tasks as a consequence of absolute positional encoding, not merely simultaneous unmasking. On Star_medium and Star_hard, MDM's failure is not fixed by greedy decoding because the underlying problem is that variable arm lengths make predicting absolute token positions equivalent to solving the puzzle in one pass. ILM's use of relative positional encoding (RoPE) combined with iterative single-token insertion side-steps this entirely. This provides a principled explanation for why relative-position insertion is architecturally superior for this class of problems — a theoretical point that goes beyond empirical comparison and could inform future design of non-autoregressive models for combinatorial tasks.

---

## Suggestions

1. **Address the length confound directly**: Report NLL comparisons at matched generation length (e.g., by condition-stopping at training-mean length, or using a length-normalized metric). This single change would substantially strengthen or clarify the text generation claims.
2. **Diagnose early stopping**: Add a brief analysis of stopping classifier calibration (e.g., precision/recall on the stop decision, or calibration curves) to explain and potentially correct ILM's systematic under-generation on text tasks.
3. **Revise the abstract/intro claims for text generation**: Change "perform on par with ARMs" to "approach ARM performance on Stories and are within ~20% on LM1B" — a more defensible claim consistent with what Table 2 shows.
4. **Add error bars**: For Tables 2 and 3, bootstrap confidence intervals over the evaluation sets are straightforward to compute and would materially improve the interpretability of the NLL comparisons.

---

**Originality**: The insertion-based generation paradigm is revisited rather than invented here, but the combination of relative positional encoding, the normalized-count denoising objective, the joint stopping classifier, and the empirical framing against MDMs is a novel and coherent contribution. *Score: 4/5*

**Importance of research question**: Overcoming the complementary failure modes of ARMs and MDMs for variable-length, dependency-constrained generation is a genuine and important problem. *Score: 4/5*

**Claims well-supported**: Planning claims are very well-supported. Text generation claims are moderately supported but contain overclaiming ("on par with ARMs") that the experiments do not fully back. *Score: 3/5*

**Soundness of experiments**: Planning experiments are clean and well-designed. Text generation experiments are methodologically weaker due to the length confound and lack of confidence intervals. *Score: 3/5*

**Clarity of writing**: The paper is well-structured. The formulation in Section 3 is clear. The discussion of limitations in Section 6 is honest, though it doesn't reconcile with the more optimistic abstract. *Score: 4/5*

**Value to research community**: ILMs provide a practically trainable alternative to both ARMs and MDMs with demonstrated advantages on constraint-satisfaction tasks. The formulation is accessible and the code/experiments are sufficiently described. *Score: 4/5*

---

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>