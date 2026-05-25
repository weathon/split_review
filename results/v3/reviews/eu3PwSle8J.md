Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes Augmented Intermediate Representations (AIR), a defense against indirect prompt injection attacks that injects instruction hierarchy (IH) signals into every decoder layer of an LLM, rather than only at the input layer as in prior work (Delimiters, ISE). The key idea is to add per-layer trainable embedding tables indexed by privilege level, so the IH signal is maintained throughout the model's depth. Evaluations on Llama-3.2-3B, Qwen-2.5-7B, and Llama-3.1-8B under both SFT and DPO training show consistent ASR reductions under gradient-based attacks (GCG, Astra) compared to input-only defenses, with at most a 2% utility drop.

## Strengths

1. **Consistent and often large ASR reductions under strong gradient-based attacks.** Across all six model/training combinations in Table 1, AIR achieves the lowest ASR under GCG and Astra attacks. The margins are substantial in many settings (e.g., Llama-3.2-3B SFT GCG: 38% (Delim) → 4.1% (AIR); Qwen-2.5-7B SFT Astra: 39.2% (ISE) → 2.4% (AIR)). This directly validates the core claim.

2. **Empirical diagnostic supporting the multi-layer motivation.** Figure 3 provides direct evidence that input-level IH signals degrade across layers for Delim and ISE (cosine similarity between privileged representations rises to 0.9+), while AIR maintains better separation (stays below ~0.88). This diagnostic is a genuine analytical contribution beyond the method itself.

3. **Thorough evaluation across models, training paradigms, and attack types.** The experiments span three model families (3B/7B/8B), two training methods (SFT/DPO), four static attacks, two gradient-based attacks (GCG, Astra), and the SEP benchmark. This breadth exceeds prior work on IH injection (which typically tests fewer combinations) and supports generalizability.

4. **Utility is well-preserved.** AIR does not degrade AlpacaEval win rates beyond 2% relative to the non-adversarial baseline, and in several settings actually achieves the highest win rates among IH-based methods (Figure 6). This is important for practical deployment.

5. **Practical efficiency.** The method adds only 0.4M parameters (0.005% of the model) and negligible inference cost.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **The claimed improvement range (1.6×–9.2×) is imprecise when applied to all gradient-based attacks.** The abstract and conclusion state that AIR yields "between 1.6× and 9.2× reduction in attack success rate on gradient-based prompt injection attacks." However, the Astra results in Table 1 include settings where the improvement factor is as low as ~1.2× (Llama-3.1-8B DPO: 1.2/1.0) and as high as 145× (Llama-3.2-3B SFT: 14.5/0.1). Even for GCG, one setting (Llama-3.1-8B DPO: 4/2.8 = 1.43×) falls below 1.6×. The paper acknowledges the high end ("up to 145×") in Section 6.1 but the abstract and conclusion do not reflect the full variability. The authors should either (a) restrict the claim to GCG attacks (where 5/6 settings are within 1.6×–9.2×), or (b) report the actual observed range (~1.2×–145×) with appropriate qualifiers.

2. **No parameter-matched ablation to isolate the multi-layer benefit.** AIR adds 0.4M trainable IH parameters (~33× 3 × 4096), while Delimiters add ~8K (2 token embeddings) and ISE adds ~12K (3 segment embeddings). The improvement attributed to per-layer injection could partly come from having substantially more capacity dedicated to the IH signal. The paper does not run a controlled baseline that matches the additional parameter count at the input layer (e.g., multiple segment embedding vectors per token or a small MLP processing the IH signal before the first layer). Without this, the causal claim that "multi-layer injection *per se* drives the gains" is weakened. This is an important direction for future work but does not invalidate the empirical result that AIR outperforms existing methods as-is.

3. **ASR values in Table 1 lack variance estimates.** The main robustness results (Table 1) report single ASR values without confidence intervals or standard deviations across runs. Gradient-based attacks are sensitive to initialization, and showing mean ± std over 3–5 random seeds would strengthen confidence. (Figure 7 does plot mean loss with standard deviation shading over the 208 test instances, but this is not the same as run-level replication.)

4. **Inconsistent "None" baseline labeling.** In Table 1, "None" refers to a model that underwent adversarial training (SFT or DPO) without any IH injection mechanism. In Figure 6, "None" refers to a model trained only non-adversarially. This inconsistency could confuse readers and should be clarified.

5. **Single target phrase for attacks.** All robustness evaluations use the target phrase "hacked!". While this is a common simplification, evaluating on a handful of different target strings would strengthen the evidence that the defense does not rely on quirks of one output.

### Trivial
- The paper's initial framing (Section 2) mentions "attention mechanisms" as part of the defender's action space, but the proposed intervention only touches layer-level IH injection, not attention. Minor scope mismatch.

## Nice-to-Haves
- A parameter-matched ablation (e.g., adding comparable IH capacity through multiple input-layer segment embeddings) would significantly strengthen the causal interpretation. See Weakness 2.
- An analysis of the learned IH embeddings across layers (e.g., do they diverge or specialize in deeper layers?) would deepen the understanding of why per-layer injection helps.
- A discussion of adaptive attacks that specifically target the per-layer injection mechanism (e.g., an attacker aware of AIR might try to suppress the IH signal through prefix optimization) would improve thoroughness.

## Removed Points

The following points from the reviewer inputs were removed because they are factually incorrect, misunderstand the paper, or are nitpicks:

- **"Figure 3 Delim cosine similarity constant 1.0 is suspicious"** — The constant 1.0 for Delim across all layers is not necessarily an artifact; it reflects the paper's thesis that input-only delimiter tokens fail to propagate IH information through the model. The fact that Delim achieves some robustness (per Table 1) does not contradict this — the cosine similarity metric measures a specific property (representation overlap of content tokens from different privilege regions), which may differ from how Delim's robustness operates (e.g., through attention patterns or positional cues). The paper's claim is that input-level signals degrade, which this figure visualizes. The reviewer's speculation about the metric being "less informative for Delim" is a nuance, not a weakness, and the figure purposefully illustrates the paper's motivation.

- **"No variance reported for Figure 7"** — Figure 7 *does* include shaded regions representing standard deviation across the 208 test instances. The reviewer missed this. The caption explicitly states this.

- **Formatting/style nitpicks** about "exact point of injection" in Section 5.3 needing justification — the paper describes adding the embedding before each decoder block, which is sufficiently precise for reproducibility.

- **The suggestion that the abstract's scope mentions "attention mechanisms" that aren't addressed** — this is a standard framing of the defender's action space and not a commitment. It's a trivial scope mismatch.

- **The comment about missing appendix content** — the appendix exists in the original submission; the parser stripped it.

## Novel Insights

The most genuinely novel observation from the reviews is the parameter-count confound between AIR and input-only methods. This is not a fatal weakness but it is the most substantive analytical gap in the paper's otherwise clean causal narrative. A reviewer insightfully noted that the improvement could be decomposed into (a) more IH capacity and (b) distributed placement, and the paper currently conflates them. This frames a precise follow-up experiment (input-layer capacity-matched baseline) that would substantially strengthen the paper. Separately, the observation that the 1.6×–9.2× range does not uniformly hold for Astra attacks provides a concrete example of how even careful empirical claims can overreach when the claim is stated as a range rather than with distributional qualifiers.

## Suggestions
1. **Fix the improvement range claim.** Either (a) explicitly tie the 1.6×–9.2× range to GCG attacks only (where it holds for 5/6 settings), or (b) report the full observed range (~1.2× to 145×) with appropriate context. At minimum, add a qualifier like "on most settings" or "on GCG attacks."
2. **Add a parameter-matched ablation.** Augment the ISE baseline with additional trainable IH capacity at the input layer (e.g., a bank of K×L embedding vectors summed into token representations) that uses the same total parameter count as AIR (0.4M). If AIR still outperforms, the multi-layer hypothesis is strongly supported.
3. **Report variance for Table 1.** Run the gradient-based attacks with 3–5 random seeds and report mean ± std ASR.
4. **Clarify the "None" baselines.** Rename in Figure 6 to avoid confusion with Table 1's "None" (e.g., "No Adversarial Training" in Figure 6).
5. **Evaluate on multiple target phrases.** Add 2–3 different target strings (e.g., "ACCESS GRANTED", "pwned") to demonstrate the defense is not target-specific.

## Score and Decision

### Calibration Anchors

**Round 1 — Bracketing:**
| Anchor | Score | Source | Comparison |
|--------|-------|--------|------------|
| 3MDmM0rMPQ (Inverse Prompt Engineering) | 3.00 | topic-low | Weaker in evaluation breadth and clarity; rejected |
| lUyYX9VFgA (Code-of-thought prompting) | 3.00 | topic-low | Weaker evaluation and weaker contribution; rejected |
| 5kMwiMnUip (NEMESIS jailbreaking) | 1.40 | topic-low | Fundamentally weak; not comparable |
| 6QBHdrt8nX (SafetyAnalyst) | 3.33 | topic-low | Different task (content moderation); less thorough |
| sjWG7B8dvt (ISE — direct baseline) | 6.00 | topic-mid | **Most comparable anchor.** Same sub-area, similar evaluation scale. ISE was accepted; this paper improves on it with a more novel architectural insight (multi-layer injection) and stronger evaluation (gradient-based attacks). |
| l3bUmPn6u5 (PFT) | 4.25 | topic-mid | Weaker evaluation (no gradient-based attacks, missing strong baselines); rejected |
| Q3oAX9HoH2 (Nested Gloss) | 4.00 | topic-mid | Different focus (jailbreak, not defense); less comprehensive |
| 2VmB01D9Ef (AutoHijacker) | 4.25 | topic-mid | Attack paper, not defense; less directly comparable |
| tTPHgb0EtV (Booster, harmful fine-tuning) | 8.00 | topic-high | Stronger theoretical grounding and broader impact; different sub-area |
| SPS6HzVzyt (Context-Parametric Inversion) | 8.00 | topic-high | Stronger analytical depth; different sub-area |

**Round 1 Weakness-anchored queries:**
| Anchor | Score | Source | Comparison |
|--------|-------|--------|------------|
| 4zygH3k8Zr (Replacement Learning) | 4.40 | weakness-param | About parameter efficiency in vision; irrelevant topic |
| sl4hOq9wm9 (Knowledge Augmentation) | 5.50 | weakness-param | About in-context vs in-parameter knowledge; different topic |
| P5qCqYWD53 (MLP Re-weighting jailbreak) | 3.50 | weakness-param | About jailbreak attacks; different area |
| XjSfcJUcaA (Adversarial Null-Text) | 4.75 | weakness-target | About adversarial examples; different domain |
| KX5hd1RhYP (Average Certified Radius) | 4.67 | weakness-overclaim | About metric critique; different domain |

**Round 2 — Narrowing:**
| Anchor | Score | Source | Comparison |
|--------|-------|--------|------------|
| sjWG7B8dvt (ISE) | 6.00 | round2 | See above |
| iKgQOAtvsD (Deciphering the Chaos) | 5.75 | round2 | About jailbreak attacks, not defense; weaker presentation |
| JwoCs9O3QL (VLMGuard) | 5.00 | round2 | About VLM defense; weaker evaluation |
| kUH1yPMAn7 (Safety Layers) | 6.00 | round2 | About internal safety mechanisms; accepted. Similar evaluation depth |
| e9yfCY7Q3U (I-GCG) | 6.25 | round2 | About jailbreak attacks, accepted; similar level of contribution |
| r42tSSCHPh (Catastrophic Jailbreak) | 7.00 | round2 | Stronger empirical work; different sub-area |

**Round-1 bracket:** I initially bracketed this paper in the 4.5–7.0 range based on topic similarity to the ISE paper (6.0) and the PFT paper (4.25).

**How round-2 narrowed it:** The round-2 search placed the paper alongside ISE (6.00), I-GCG (6.25), and Safety Layers (6.00), confirming that the paper's quality level is in the solid-acceptable range (~6). The ISE paper — the most directly comparable baseline — scored 6.0 and was accepted. The current paper has a more novel idea (multi-layer injection vs input-level embedding), more comprehensive evaluation (gradient-based attacks, multiple models/training methods), and comparable presentation quality. Its weaknesses (imprecise range claim, missing ablation, no variance on Table 1) are all addressable and do not undermine the core empirical finding.

**What the low-band anchors failed at, and does this paper share those failures?** The low-band anchors (scores ≤ 3.5) failed due to unclear problem definitions, missing baselines, weak or narrow evaluation, poor presentation, or fundamentally flawed methodology. This paper shares none of those failures: it has a clear problem statement, appropriate baselines (Delim, ISE), a comprehensive evaluation spanning multiple models/attacks/training methods, and clear presentation. The weaknesses it does have (imprecise claim, missing control ablation) are common in mid-range papers and do not bring it into the low band.

**Score:** 6.0. The paper proposes a genuinely novel and well-motivated architectural improvement over existing input-only IH injection methods, supported by thorough empirical evaluation. The weaknesses are real but minor and addressable. The paper is of comparable quality to the ISE paper (score 6.0, accepted) and improves on it in both novelty and evaluation breadth.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>