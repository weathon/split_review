Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks that injects Instruction Hierarchy (IH) signals into every decoder layer of a transformer LLM, rather than only at the input layer as in prior methods (Delimiters, Instructional Segment Embedding / ISE). The paper hypothesizes that input-only IH signals degrade as they propagate through layers, and AIR addresses this by adding a small, trainable embedding table to each decoder layer that augments token representations with privilege-level information. Evaluations across three model families (Llama-3.2-3B, Qwen2.5-7B, Llama-3.1-8B), two training methods (SFT, DPO), and multiple attack types show consistent robustness improvements — up to 1.6×–9.2× reduction in attack success rate on gradient-based attacks — with minimal utility degradation (<2%).

## Strengths

- **Clear, well-motivated architectural contribution with strong empirical support.** The idea of injecting IH signals across all layers (analogous to how RoPE distributes positional information across layers) is simple, principled, and addresses a genuine limitation of prior input-only methods. The empirical results show consistent and substantial ASR reductions across 3 model families, 2 training methods, multiple attack types, and 2 evaluation benchmarks (Tables 1, 2; Figures 6–9). The parameter overhead is negligible (0.005% increase).

- **Mechanistic evidence via linear probing.** Appendix E's probe experiment provides concrete, measurable evidence for the paper's core hypothesis: input-only IH signals (ISE) degrade from 100% to ~91% probe accuracy across layers, while AIR maintains near-perfect accuracy at all layers. This goes beyond outcome-level metrics and offers a genuinely informative analysis of *why* the method works, even if the causal link is not definitively proven.

- **Thorough and well-controlled experimental design.** The paper systematically evaluates IH injection mechanisms (Delim, ISE, AIR) under a shared training protocol, isolating the effect of the injection mechanism itself. Coverage across static attacks (Naive, Ignore, Completion, Escape Separation), two strong gradient-based attacks (GCG, Astra), SEP benchmark, and BIPIA dataset is comprehensive. The decomposition of defenses into IH injection + training procedure is a useful analytical framing.

- **Honest limitations discussion and reproducibility commitment.** Appendix A explicitly acknowledges the lack of formal guarantees and single-turn scope. Appendix K states code is provided in supplementary material. Appendix B.2 provides practical initialization guidelines for extending AIR to new model families.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core claims. The weaknesses below are substantive but addressable.

### Minor

- **Short optimization budget for gradient-based attacks.** Both GCG and Astra use only 50 optimization steps for SFT models and 200 for DPO models (line 520–521). The original GCG paper and subsequent work typically use 500–1000+ steps. With such a short budget, the attack may not have converged, potentially overstating the relative robustness of AIR. While the qualitative loss curves (Figure 7) show AIR maintaining higher loss throughout, the absolute ASR numbers could shift with longer optimization, and the comparative advantage could shrink. This is the most significant weakness in the evaluation.

- **Logit-based ASR for gradient-based attacks is a partial proxy.** For GCG and Astra, ASR is measured by whether the logits assign highest probability to "hacked!" (lines 522–523), rather than by actually generating and checking output. While greedy decoding would likely produce the same result, the paper does not specify the decoding strategy or confirm this equivalence. The static attacks and SEP evaluation (which use actual generation-based metrics) are cleaner. This concern is specific to the two gradient-based attack evaluations.

- **The causal link between IH signal persistence and robustness is correlational, not established.** The linear probe experiment (Appendix E) convincingly shows that AIR preserves linearly separable IH signals across layers while ISE degrades. However, the paper does not conduct intervention experiments (e.g., ablating AIR embeddings from specific layers to test whether robustness collapses) that would directly test whether this representational property *causes* robustness. The paper's language is appropriately hedged ("consistent with our hypothesis," "provides empirical evidence"), but the mechanism claim would be strengthened by causal tests.

### Trivial

- The initialization sensitivity for Qwen (needing σ=0.1 instead of 0.02, Appendix B.2) indicates some model-specific tuning is needed, though the paper provides practical guidelines.
- Table 1's presentation in the parsed version is garbled; this is a parser artifact, not an author error.

## Nice-to-Haves

- **Generation-based evaluation for gradient attacks:** Confirming that the logit-based ASR for GCG/Astra matches generation-based ASR (e.g., with temperature sampling) would cleanly resolve this concern.
- **Depth ablation:** Training AIR variants that inject IH signals into only a subset of layers (e.g., first 8, last 8, alternating) would directly test whether all-layer injection is what drives robustness, and would strengthen the mechanistic narrative.
- **Longer-horizon attacks:** Running gradient-based attacks for 500+ steps on at least a subset of examples would clarify whether AIR's advantage persists under stronger attacks.
- **Adaptive attack evaluation:** All attacks are generic GCG/Astra, not specifically optimized against AIR. Testing whether an adversary aware of AIR's architecture can find targeted weaknesses would strengthen robustness claims.

## Removed Points

- **"Baselines are unfaithful replications of prior work"** (Harsh Critic Critical Issue 1): The paper explicitly states "For a fair comparison, all models in our experiments undergo the same training procedure, regardless of the IH injection mechanism" (line 435–436) and clearly explains how prior work used specific (mechanism, training) combinations while this paper systematically evaluates a broader matrix (lines 481–487). Standardizing the training procedure to isolate the injection mechanism is standard ablation methodology, not a flaw. The paper does not claim to exactly reproduce prior systems — it compares injection mechanisms under a controlled setup, which is the correct way to evaluate a proposed architectural modification.
- **"Novelty is overstated — injecting auxiliary info at intermediate layers is standard"** (Section notes): The analogy to RoPE is explicit and acknowledged as a similarity in approach, not a claim of radical novelty. The paper's contribution is the specific application of this principle to IH signals for security, with the first empirical demonstration that layer-wise IH injection improves adversarial robustness.
- **"The comparison is not fair because training procedure differs"**: The paper *controls* for training procedure by making it identical across methods. This is the appropriate design for an ablation comparing injection mechanisms.

## Novel Insights

The most novel observation to emerge from the reviews — beyond the paper's own contributions — is the finding that the Delimiter method yields near-chance linear probe accuracy (~50–55%) for privilege-level prediction at *all* layers (Appendix E). This is striking because Delim models are non-trivially robust on SEP and some static attacks, yet their intermediate representations contain essentially no linearly decodable privilege information. This suggests that Delimiter-based defenses work through a fundamentally different (possibly nonlinear or positional) mechanism than ISE or AIR, and raises the question of whether the linear probe metric is the right diagnostic for all IH injection methods. The paper does not discuss this implication, but it is an interesting direction for future mechanistic analysis of prompt injection defenses.

## Suggestions

1. **Run gradient-based attacks for 500+ steps** on a representative subset (e.g., 50 examples) to confirm that AIR's advantage does not collapse under longer optimization. Report both logit-based and generation-based ASR.
2. **Add a depth ablation** (AIR embeddings in first-half, last-half, alternating layers) to test whether all-layer injection is necessary for the observed gains, or whether shallower injection suffices.
3. **Explicitly report the decoding strategy** used for gradient-based ASR evaluation and confirm that logit-based and generation-based metrics agree.

## Score and Decision

**Calibration anchors** (all from the human reviews directory):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `k5Sc3ageMW.md` (Reasoning Up Instruction Ladder) | 2.50 | Much weaker — limited evaluation, incremental contribution vs. this paper's clear empirical advance |
| `IeNXtofK6T.md` (PromptArmor) | 3.50 | Simpler method (prompting), less technical depth; this paper has stronger architectural contribution and analysis |
| `fF9alVesJ0.md` (IntentGuard) | 3.50 | Similar domain but this paper provides more thorough evaluation and a cleaner architectural contribution |
| `U3kxnDzuRz.md` (Deep-Cover Agents) | 4.00 | Observational analysis of attacks vs. this paper's constructive defense with mechanistic analysis |
| `qkGhc3l5py.md` (Checkpoint-GCG) | 4.50 | Attack paper on related topic; similar evaluation breadth but this paper provides stronger mechanistic evidence |
| `7B9mTg7z25.md` (The Attacker Moves Second) | 6.00 | Higher-level meta-evaluation paper with broader scope and stronger empirical claims; this paper has a more concrete constructive contribution but weaker adaptive-attack evaluation |
| `VKGTGGcwl6.md` (LLMs Get Lost In Multi-Turn) | 8.00 | Exceptional paper with clean methodology, large-scale evaluation, and novel framework; this paper is not at that tier |

The paper has a clear, practical architectural contribution, thorough evaluation spanning multiple models and training methods, and a mechanistic analysis (linear probing) that goes beyond outcome-level metrics. The weaknesses — short optimization budgets, logit-based ASR for gradient attacks, and correlational (not causal) mechanism evidence — are real but standard limitations for work in this area, and none invalidate the core claims. Relative to the anchors, the paper is clearly stronger than the 2.5–4.5 range of similar-topic papers and weaker than the top-tier 6.0+ papers that either have broader scope or cleaner methodology. A score of **5.5** appropriately positions it: a solid paper with genuine contributions and thorough evaluation, held back from a higher score by evaluation protocol limitations that are addressable in revision.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>