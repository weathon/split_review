Now I have sufficient calibration. Let me write the final consolidated review.

## Summary

This paper proposes **Augmented Intermediate Representations (AIR)**, a defense against indirect prompt injection attacks for LLMs. The key idea is to inject instruction hierarchy (IH) signals—encoding whether a token belongs to system/user instructions, data, or model response—into every decoder layer via small trainable embedding tables, rather than only at the input layer as prior methods (delimiters, ISE) do. Evaluated across 3 model sizes (3B, 7B, 8B), two training schemes (SFT, DPO), and multiple attack types, AIR achieves 1.6× to 9.2× reduction in attack success rate on gradient-based attacks over state-of-the-art methods with minimal utility loss (<2%).

## Strengths

- **Clear, well-motivated architectural improvement with strong empirical backing.** The paper identifies a genuine limitation in existing IH defenses (input-only injection) and proposes a simple fix. Table 1 shows consistent and often large ASR reductions on gradient-based attacks across all 3 models and both training methods (e.g., GCG on Llama-3.2-3B SFT: 38% for Delim vs. 4.1% for AIR; Astra on Qwen-2.5-7B SFT: 39.2% for ISE vs. 2.4% for AIR). The loss curves in Figure 7, which include standard deviation bands, further corroborate that AIR sustains higher attacker loss throughout optimization—arguably the most persuasive evidence in the paper.

- **Minimal utility degradation.** Figure 6 shows that AIR's win rate on AlpacaEval 2.0 stays within 2% of the non-adversarial baseline across all settings, demonstrating that the robustness gain does not come at the cost of instruction-following quality.

- **Extremely lightweight in terms of added parameters.** Section 4 reports only 0.4M additional parameters for Llama-3.1-8B (0.005% increase) with 3 privilege levels, making the defense practical for deployment.

- **Thorough evaluation scope.** The paper evaluates 3 model scales, 2 training techniques (SFT and DPO), 4 static attacks, 2 gradient-based attacks (GCG and Astra), and the SEP benchmark, providing good evidence of generalizability. The comparison is uniformly fair: all methods share the same training data and procedure.

## Weaknesses

### Major

- **No variance estimates on the primary ASR table (Table 1).** All ASR numbers in Table 1 are single-run point estimates without confidence intervals, standard deviations, or multi-seed reporting. While the loss curves in Figure 7 include standard deviation bands (a welcome detail), the headline comparison that drives the paper's main claim lacks this rigor. Some comparisons are close enough (e.g., Astra on Llama-3.1-8B DPO: ISE 1.2 vs. AIR 1.0; GCG on the same model: ISE 4.0 vs. AIR 2.8) that variance could affect the ranking. This is the single most significant weakness and should be addressed (e.g., 3 random seeds with error bars) to make the quantitative claims fully trustworthy.

### Minor

- **Causal mechanism is hypothesized, not isolated.** The paper argues that input-level IH signals degrade through layers (Figure 3) and that AIR maintains better separation. The empirical robustness results are consistent with this story, but the paper never directly demonstrates that multi-layer injection is the *cause* of improved robustness rather than a side effect. An ablation varying the depth of IH injection (e.g., every other layer, or only the first/last few layers) would strengthen the causal claim. The paper does acknowledge this as a hypothesis ("We hypothesize," "We posit"), so the gap is in evidence depth, not overclaiming.

- **No discussion of limitations.** The paper lacks a limitations paragraph. Important points to acknowledge include: (a) the defense requires architectural modification and retraining (not a plug-in post-hoc filter); (b) effectiveness depends on correctly assigning privilege levels—if an attacker can inject at the user/instruction level, the hierarchy breaks; (c) scaling behavior beyond 8B parameters is unexplored.

### Trivial

- None.

## Nice-to-Haves

- A layer-depth ablation (inject IH at layers 0–5, 0–10, 0–20, and all layers) would directly test whether the benefit saturates or requires full depth, and would strengthen the causal story.
- A diagnostic analysis of *why* AIR works—e.g., gradient norms or attention patterns under attack for different IH methods—would elevate the paper from "empirically effective" to "demonstrated mechanism."
- Reporting training FLOPs or wall-clock time compared to prior methods would help practitioners assess the practical overhead.

## Removed Points

The following points from the inputs were removed per the filtering rules:

- **Static-attack evaluation provides no differentiation.** (Harsh Critic) — Factually correct, but this is a natural property of all IH-based defenses once trained on adversarial data. The paper's contribution is on gradient-based attacks; static attacks are ceilinged out. Not a weakness of the paper or its method.
- **"The paper would be stronger by including another benchmark (e.g., BIPIA)."** (Harsh Critic) — This is scope creep; the evaluation already covers 3 benchmarks (AlpacaFarm, AlpacaEval 2.0, SEP) across 8 attack variants, which is extensive by community standards.
- **"No analysis of the trade-off between ASR reduction and training cost."** (Harsh Critic) — Nice-to-have but not standard for empirical defense papers of this type; the paper does note overhead is similar to prior works.
- **Strengths about "addressing an important problem" or generic framing.** (Strength Finder) — Removed as generic; only concrete, paper-specific strengths were retained.
- **Reproducibility nitpicks about undisclosed hyperparameters or missing appendix.** (Harsh Critic) — The main text provides LRs, optimizer, epochs, and training procedure. Appendix details were stripped by PDF parsing but assumed present in the original.
- **Criticism that the core hypothesis is "black-box improvement whose mechanism is asserted but not fully isolated" framed as a fatal flaw.** (Harsh Critic) — Demoted from potential fatal to Minor because the paper explicitly frames it as a hypothesis and the empirical evidence stands on its own.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation is the parallel drawn between AIR and Rotary Position Embedding (RoPE): both distribute critical per-token information (positional or privilege) across all decoder layers rather than injecting only at the input. This analogy reframes the prompt injection defense problem as an architectural insufficiency—the signal placement, not just the training—and opens up the possibility that other input-level security signals (e.g., source authentication markers, integrity hashes) could also benefit from per-layer injection. The paper does not fully explore this implication, but it is a fruitful direction the framing surfaces.

## Suggestions

1. **Add error bars to Table 1.** Rerun experiments with at least 3 random seeds and report mean ± std for ASR values. This is the most impactful change the authors can make.
2. **Add a limitations paragraph** to the conclusion, addressing the scope (models ≤8B, architectural retraining required, dependency on correct privilege assignment).
3. **Add a brief ablation on IH injection depth** (e.g., layers 0–5, 0–10, all layers) using the most discriminative setting (one model × one training method × GCG) to directly test the core mechanistic claim.
4. **Clarify in the abstract and contributions** that the primary empirical advantage is against optimization-based (white-box/gradient) attacks, since static attacks are ceilinged for all IH methods.

## Score and Decision

**Calibration:**

| Anchor | Path | Avg Score | Round | Comparison to current paper |
|--------|------|-----------|-------|---------------------------|
| Instructional Segment Embedding (ISE) | sjWG7B8dvt | 6.00 | R1,R2 | Weaker — same topic, less novel method, narrower evaluation |
| Catastrophic Jailbreak | r42tSSCHPh | 7.00 | R2 | Comparable — similar experimental breadth, attack vs. defense framing |
| Robustness Over Time | eC4WlSZc4H | 6.75 | R2 | Slightly weaker — less technical novelty, rejected |
| ArrAttack | sULAwlAWc1 | 7.00 | R2 | Similar level — mixed reviews (8,5,8), less clear novelty |
| Safety Alignment Depth | 6Mxhg9PtDE | 9.50 | R1 | Stronger — more comprehensive theoretical+empirical contribution |
| NEMESIS (jailbreaking) | 5kMwiMnUip | 1.40 | R1 | Much weaker — flawed methodology |

**Round 1 bracket:** 5.5–7.5.  
**Round 2 narrowing:** Compared directly against the ISE anchor (6.00), which is the closest topical match. The current paper is a clear step beyond ISE: it identifies a genuine limitation of input-only injection, proposes a novel architectural fix, and evaluates more thoroughly (3 models, 2 training methods, gradient-based attacks). However, the lack of error bars on Table 1 and the absence of a depth ablation prevent it from reaching the 7+ tier occupied by papers with stronger experimental rigor.  
**Final score:** 6.5 — a solid contribution that advances the state of the art in prompt injection defenses, with manageable weaknesses to address.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>