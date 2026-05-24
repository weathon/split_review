Now I have a good calibration picture. Let me construct the final review.

**Bracket summary:** Round 1 placed the paper between weak anchors (avg 3.0-3.33) and strong anchors (avg 7.75-9.50). Narrowing pass found papers in the 5.25-6.75 range, with the most topically similar being PFT (4.25, Reject), SPIN (5.50, Reject), RA-LLM (5.33, Reject), and I-GCG (6.25, Accept). The current paper is clearly stronger than the 4-5.5 reject papers (more thorough evaluation, clearer motivation, better baselines) but has a significant methodological gap (logit-based ASR) that prevents it from reaching the 6.5+ tier. The loss curves and SEP provide supporting evidence, so the gap is not fatal. I position the paper at 6.0.

---

# Final Review

## Summary

This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks in LLMs. The key insight is that prior work injects instruction hierarchy (IH) signals only at the input layer, and these signals degrade through deeper layers. AIR addresses this by injecting trainable IH embeddings at every decoder layer. Experiments across three model sizes (3B, 7B, 8B), two training methods (SFT, DPO), and multiple attack types (static, GCG, Astra, SEP) show consistent robustness improvements — 1.6×–9.2× ASR reduction on gradient-based attacks — with negligible overhead (~0.4M parameters for an 8B model) and minimal utility loss.

## Strengths

- **Well-motivated by an empirical finding (Figure 3).** The paper directly demonstrates that input-only IH signals (Delim, ISE) degrade through decoder layers (cosine similarity between privilege levels approaches 1.0), while AIR maintains lower similarity (~0.85 throughout). This gives the reader a clear reason to believe that layer-wise injection could matter, independent of the ASR results.

- **Consistent improvement across a thorough evaluation grid.** The paper evaluates 3 models × 2 training methods (SFT/DPO) × multiple attack types. The relative ordering AIR > ISE/Delim holds nearly uniformly in Table 1, Figure 7 (loss curves), and Figure 8 (SEP separation). The SEP evaluation is particularly valuable because its separation score is computed from actual model generations, providing evidence orthogonal to the logit-based metric concern.

- **Minimal computational and architectural overhead.** AIR adds 0.4M parameters (0.005%) for Llama-3.1-8B and negligible inference cost. This makes the defense practical for deployment, which is a meaningful advantage over approaches that require multiple inference passes or large architectural changes.

- **Precise connection to prior work.** Section 5.3 clearly maps Delim → (Wallace et al., 2024; Chen et al., 2024a) and ISE → (Wu et al., 2024), and evaluates combinations (e.g., Delim+DPO) that prior works did not explore, providing a systematic comparison under a unified training pipeline.

## Weaknesses

### Fatal
None.

### Major

- **The primary evidence for the headline claim uses a logit-based metric that conflates optimization objective with evaluation.** Section 5.4 states that for gradient-based attacks (GCG, Astra), ASR is "measured using the likelihood (from model's logits) of generating the target phrase 'hacked!'" — but for static attacks, ASR is properly measured by checking if the *generated response* contains the phrase. The gradient-based evaluation therefore evaluates the same quantity the attack is minimizing, rather than measuring whether the attack actually succeeds at generation time. The paper does not specify how the likelihood is converted to a binary success/failure decision (what threshold? product of token probabilities?). **This gap directly affects the core quantitative claim** (1.6×–9.2× reduction in Table 1). The loss curves in Figure 7 and SEP results in Figure 8 provide supporting evidence that the relative ordering is real, but the headline ASR numbers for gradient attacks are on uncertain footing without a generation-based evaluation.

### Minor

- **No statistical uncertainty for the main results.** Table 1 (ASR values), Figure 6 (win rates), and the SEP scores in Figure 8 are reported as point estimates without error bars, confidence intervals, or significance tests. Given that many static-attack ASR values are extremely small (0.0, 0.5), even a single misclassification could materially change the reported numbers. This is common in the literature but reduces the informativeness of the comparisons, especially for the gradient-based ASR values that are the paper's headline result.

- **"State-of-the-art" language in the abstract mildly overstates the evidence.** The abstract claims improvement "compared to state-of-the-art methods," but the experiments compare only against re-implementations of Delim and ISE. The paper body (Section 5.3) is transparent about the mapping to prior work, so this is not a fatal flaw, but the abstract's framing implies a more direct comparison with published checkpoints/results than is actually provided.

- **Incomplete specification of the gradient-based ASR computation.** The paper states ASR is "measured using the likelihood" but does not specify (a) how the likelihood of the multi-token phrase "hacked!" is computed (product of conditional probabilities? average?), (b) what threshold (if any) converts the continuous likelihood to binary success/failure, or (c) why 4.1% is the cutoff. This makes the results difficult to reproduce or interpret.

### Trivial

- **Figure 3 is shown only for Llama-3.2-3B.** The paper acknowledges this is a correlational observation used as motivation. Showing the same analysis on at least one other model would strengthen the generality of the motivation, though the current presentation is acceptable.

## Nice-to-Haves

- **Generation-based ASR for gradient attacks** (the most impactful improvement): evaluating GCG and Astra by greedy-decoding the model after inserting the optimized prefix and checking the output for "hacked!" would resolve the main methodological concern.
- **Adversarial training baseline without any IH signal:** a comparison against a model trained on the same adversarial data but without encoding privilege levels (i.e., standard SFT/DPO on attack data) would isolate what AIR adds beyond simply training on adversarial examples.
- **Parameter-matched ablation:** comparing AIR against an input-only injection that adds the same total number of extra parameters (by increasing input-layer embedding dimension) would cleanly attribute the benefit to layer-wise distribution rather than increased capacity.
- **Hyperparameter sensitivity** for the gradient-based attacks (e.g., varying prefix length, optimization steps).

## Removed Points

These points from the inputs are flagged for removal; they are listed here for completeness but should be treated with caution.

- **Section 4 clarity concern (Harsh Critic):** The critic questioned whether embeddings are shared across token positions. Equation (1) makes this explicit: `x'_ij = x_ij + s_j^k` where `s_j^k = S_j[k_i]`. Tokens with the same privilege level index the same embedding. The paper is clear on this. *Reason for removal: misunderstanding of the paper's exposition.*
- **Reproducibility of baseline implementations (Harsh Critic):** The critic questioned faithful reproduction of prior work. The paper clearly states the mapping to prior methods in Section 5.3 and evaluates all methods under a unified pipeline for fair comparison. *Reason for removal: the paper transparently scopes its comparison; requiring published checkpoints for every re-implementation is a standard concern that is addressed by clear methodology disclosure.*
- **Section 6.1 nuanced discussion request (Harsh Critic):** The critic asked for more discussion of cases where AIR's improvement is marginal. The data is fully reported in Table 1, and the paper focuses on the overall trend. *Reason for removal: the paper's presentation choices about narrative emphasis are not weaknesses, and the data is transparently available for readers to assess.*
- **Some strengths from Strength Finder:** Generic or conflicting strengths removed per filtering rules. Specifically, the strength about "systematic evaluation" is retained but partially undercut by the metric concern; the strength about "consistent ASR reductions" is retained but with the caveat that the metric for gradient-based attacks is logit-based.

## Novel Insights

None beyond the paper's own contributions. The paper's core insight — that IH signals degrade through layers and that layer-wise injection improves robustness — is the main novel finding. The reviews surface no additional unforeseen observations.

## Suggestions

- **Replace or supplement the gradient-based ASR with a generation-based measure.** Compute ASR for GCG and Astra by greedy-decoding the model after inserting the optimized adversarial prefix and checking whether the output contains "hacked!". This directly measures what the defense is supposed to prevent and would resolve the most significant methodological concern. If computational constraints prevent running full generations for all test instances, provide a clear justification for why the logit-based measure is a reliable proxy (e.g., by showing that it correlates well with generation-based ASR on a subset).
- **Add error bars.** Even simple bootstrapped 95% confidence intervals for the ASR values in Table 1 would substantially improve the informativeness of the comparisons.
- **Clarify the ASR computation details.** Specify the exact formula used to compute likelihood from logits, the threshold (if any) applied, and how missing tokens are handled. This is essential for reproducibility.
- **Soften the abstract's language.** Change "compared to state-of-the-art methods" to "compared to input-only IH injection methods (Delim and ISE)" to match what is actually measured.

## Score and Decision

**Calibration:**

*Round 1 (Bracketing):*
- Weak band (score < 3.5): 3MDmM0rMPQ (3.00), lUyYX9VFgA (3.00), 5kMwiMnUip (1.40), 6QBHdrt8nX (3.33) — all rejected papers on LLM safety/security, much weaker evaluation than AIR.
- Middle band (3.5–7.5): V01FPV3SNY (5.33), 0VZP2Dr9KX (5.25), l3bUmPn6u5 (4.25), PNHGYziAsL (5.50) — all on LLM defense/robustness. AIR is clearly stronger than PFT (4.25) and SPIN (5.50) in evaluation breadth and contribution clarity.
- Strong band (>7.5): syThiTmWWm (7.75), tTPHgb0EtV (8.00), SnDmPkOJ0T (8.00), 6Mxhg9PtDE (9.50) — all accepted, but on different topics (benchmark cheating, fine-tuning safety, model fingerprinting). Not directly comparable.

*Round 2 (Narrowing within 5–7 bracket):*
- Lower sub-band (4.5–6.5): V01FPV3SNY (5.33), 0VZP2Dr9KX (5.25), hXA8wqRdyV (6.14, Accept), PNHGYziAsL (5.50). AIR is stronger than SPIN (5.50) and RA-LLM (5.33) in evaluation thoroughness, but weaker than the adaptive attacks paper (6.14) in terms of tightness of evidence.
- Upper sub-band (6.0–8.0): e9yfCY7Q3U (6.25, Accept), YzxMu1asQi (6.50, Accept), eC4WlSZc4H (6.75, Reject), sULAwlAWc1 (7.00, Accept). AIR compares reasonably with I-GCG (6.25) but has a more significant methodological gap.

*Initial bracket:* 5.0–7.0.
*Final narrow:* After reading SPIN (5.50), I-GCG (6.25), PFT (4.25), the paper sits above the 4–5.5 reject-level work but the logit-based ASR gap is a real concern that prevents it from reaching 6.5+. The paper is between SPIN (5.50) and I-GCG (6.25) — clearly stronger than SPIN in evaluation and contribution clarity, but with a more significant methodological weakness than I-GCG (which was an attack paper where the metric is well-established).
*Final score:* 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>