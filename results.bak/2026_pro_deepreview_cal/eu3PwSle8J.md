## Summary

This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks that injects instruction hierarchy (IH) signals into *every* decoder layer of an LLM rather than only at the input layer. The authors argue that input-only IH signals (used by prior defenses like delimiter tokens and ISE) degrade as representations propagate through the decoder stack. AIR adds a small, per-layer trainable embedding table indexed by token privilege level, with negligible parameter overhead (0.4M params for Llama-3.1-8B). Evaluated across three models (3B–8B), two training paradigms (SFT, DPO), and multiple attack types (static + gradient-based GCG/Astra), AIR achieves 1.6×–9.2× lower ASR against white-box attacks while preserving utility within 2% of non-adversarial baselines.

## Strengths

- **Simple, principled architectural change with negligible cost.** AIR adds one trainable embedding table per decoder layer, totaling 0.4M parameters (0.005%) for Llama-3.1-8B. The design is clean, easy to reproduce, and the analogy to how RoPE distributes positional information across layers is apt.

- **Comprehensive, multi-faceted evaluation.** The paper tests 3 model families, 2 training methods (SFT, DPO), 4 static attacks, 2 gradient-based attacks (momentum-boosted GCG, Astra), and 2 evaluation frameworks (AlpacaFarm, SEP). This breadth goes substantially beyond prior work like ISE, which evaluated only static attacks with SFT.

- **SEP provides independent, generation-based corroboration.** The SEP benchmark (Figure 8) uses string-matching (presence/absence of a witness token) and confirms that AIR achieves the best utility–separation tradeoff across all models, particularly with DPO training. This evidence does not depend on the likelihood-based ASR metric and strengthens confidence in AIR's advantage.

- **Loss curves (Figure 7) offer transparent evidence.** The attacker's optimization loss plotted across GCG steps shows AIR models consistently incur higher loss than Delim and ISE throughout the optimization process, with shaded standard deviation regions. This is a direct, interpretable metric of defense effectiveness.

- **Clear positioning against prior work.** The paper correctly identifies that existing IH defenses (delimiters, ISE, SecAlign) all inject IH signals only at the input layer, and systematically compares against these methods within a controlled experimental setup.

## Weaknesses

### Fatal
None.

### Major
- **White-box ASR metric is insufficiently specified.** For gradient-based attacks, the paper states that ASR is "measured using the likelihood (from model's logits) of generating the target phrase `hacked!`" (line 302). The exact procedure — whether it uses average log-probability, a threshold on sequence probability, or some other summary — is not described. Since the headline 1.6×–9.2× reduction claims rely on this metric, the ambiguity weakens confidence in the precise magnitudes reported in Table 1. That said, the claim of AIR's superiority is not solely dependent on this metric: Figure 7 reports the raw optimization loss curves (which are directly interpretable), and the SEP results (Figure 8, Table 1) use string-matching and confirm the same pattern. This is a significant presentation gap that should be resolved, but multiple lines of evidence make it unlikely that the qualitative conclusion would change.

### Minor
- **Figure 3 measurement methodology is underdescribed.** The paper encodes 100 AlpacaEval prompts with two privilege levels and measures average cosine similarity of hidden representations across layers. The Delim line at exactly 1.0 for all layers is striking — the paper should explain what token pairs are being compared, how the average is computed, and why Delim stays at 1.0 (likely because delimiter tokens don't modify content token embeddings, so same-token representations remain near-identical). The key comparison — ISE (input-only) vs. AIR (per-layer) — shows a meaningful separation gap that is plausible and informative regardless, so this is a presentation issue rather than a threat to validity.

- **No ablation disentangling injection depth from parameter count.** AIR adds more trainable parameters than the input-only baselines (though the absolute increase is tiny: 0.4M). An experiment that keeps the total IH-parameter budget constant but injects it all at the input layer (e.g., a larger multi-head segment embedding) would strengthen the claim that the benefit comes specifically from per-layer recurrence rather than from additional capacity. Given the negligible parameter difference, this is a nice-to-strengthen rather than a critical omission.

### Trivial
None significant.

## Nice-to-Haves
- A brief discussion of how AIR might interact with adaptive attacks (an attacker aware of the per-layer embeddings) would round out the threat model discussion.
- Summarizing key properties of the adversarial training dataset in the main text (rather than referring entirely to the appendix) would help readers assess the training regime without consulting supplementary material.

## Removed Points
These points are flagged to be removed — treat them with caution:

1. **Harsh Critic claim that Figure 3 is "fabricated or seriously miscalibrated" and constitutes a fatal flaw.** The harsh critic asserts that Delim cosine similarity of exactly 1.0 across all layers is "not plausible" and that this "undermines the paper's framing." This is an overstatement. For the Delim method, which only adds boundary tokens without modifying content token embeddings, same-token representations can remain near-identical through layers — the result is plausible. The measurement methodology needs better documentation, but the data is not fabricated. The key comparison (ISE vs. AIR degradation) is unaffected and independently supported by downstream results. **Removed as a fatal claim; kept as minor (methodology underdescription).**

2. **Harsh Critic claim that the ASR metric "likely does not measure actual generation success" and that the headline results "cannot be taken at face value."** While the metric description is indeed vague (kept as Major), the harsh critic's framing that this fatally undermines the paper overstates the case. The paper provides: (a) loss curves (Figure 7) showing raw optimization dynamics, (b) SEP results using string-matching that confirm AIR's superiority, and (c) static attack ASR using string-matching. The qualitative conclusion is robust across metrics. **Weakened from fatal to Major.**

3. **Harsh Critic point about training datasets being "described only by reference to the appendix."** The appendix is stripped by the parser; the original submission includes these details. Per hard rules, this is removed.

4. **Harsh Critic demand for discussion of adaptive attacks.** This is scope creep — the paper is about introducing AIR as a defense, and adaptive attack analysis is future work. **Moved to Nice-to-Haves.**

5. **Strength Finder claims about "the problem is important" and other generic framings.** These are not concrete, evidence-backed strengths and are not included in the review.

## Novel Insights
None beyond the paper's own contributions. The core insight — that distributing privilege signals across all decoder layers (analogous to how RoPE distributes positional information) improves robustness — is the paper's contribution.

## Suggestions
- **Specify the white-box ASR computation precisely.** Define whether ASR = 1 if the target phrase probability exceeds a threshold, or if it uses average log-probability, and report both the threshold and rationale. Even better: report generation-based ASR (greedy decoding + string match) as a secondary metric alongside the likelihood-based one, and demonstrate correlation between the two.
- **Add a brief explanation of Figure 3's methodology.** Clarify what token pairs are compared, how averaging is done, and why Delim stays at 1.0. This would preempt confusion and strengthen reader confidence.
- **Include a parameter-controlled ablation.** An input-only variant with equivalent IH-parameter budget would cleanly isolate the benefit of per-layer injection, even if the parameter difference is tiny in absolute terms.

## Score and Decision

### Calibration anchors

| Anchor | Path | Avg Score | Round | Comparison |
|---|---|---|---|---|
| ISE (Instructional Segment Embedding) | sjWG7B8dvt.md | 6.00 | R1 | Direct predecessor; AIR extends ISE with per-layer injection, tests stronger attacks (GCG, Astra), adds DPO training, and includes SEP. AIR is clearly stronger. |
| PFT (Position-Enhanced Finetuning) | l3bUmPn6u5.md | 4.25 | R1 | Narrower scope, weaker evaluation, limited baselines. AIR is substantially stronger. |
| Safety Alignment Should be Made More Than Just a Few Tokens Deep | 6Mxhg9PtDE.md | 9.50 | R1 | Unifying framework across attack types, deeper analytical insight, multiple mitigation strategies. AIR is clearly weaker. |
| Baseline Defenses for Adversarial Attacks | 0VZP2Dr9KX.md | 5.25 | R2 | Broader but shallower evaluation of existing defenses; limited novelty. AIR is stronger. |
| Safety Layers in Aligned LLMs | kUH1yPMAn7.md | 6.00 | R2 | Novel architectural insight about safety layers; narrower threat model and evaluation. AIR has broader empirical support. |
| Jailbreaking with Simple Adaptive Attacks | hXA8wqRdyV.md | 6.14 | R2 | Strong attack paper with comprehensive model coverage. Different contribution type; AIR's evaluation rigor is comparable. |

### Bracket and scoring

**Round 1 bracket:** 5.5–7.5 (between ISE at 6.0 and the 9.50 strong anchor).

**Round 2 narrowing:** Anchors at 5.25, 5.33, 6.00, 6.00, 6.14, 6.25, 6.75, 7.33 confirm the upper half of the bracket. AIR is clearly stronger than the 5.25–6.00 cluster (better motivation, stronger attacks, more comprehensive evaluation) and clearly weaker than the 7.33+ papers (less unifying insight, narrower contribution scope). Within the 6.0–6.75 range, AIR sits above ISE (6.00) — its direct predecessor — due to substantially stronger evaluation and a more principled design. The likelihood-metric ambiguity and Figure 3 underdescription prevent it from reaching the 7.0+ tier.

**Final score: 6.5** — a solid accept. The method is simple, effective, well-evaluated, and builds clearly on prior work. The presentation gaps around the ASR metric and Figure 3 methodology should be addressed but do not undermine the core contribution, which is independently supported by multiple evaluation frameworks.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>