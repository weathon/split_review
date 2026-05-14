Now I have thoroughly read the paper and the calibration anchors. Let me produce the final consolidated review.

---

## Summary

This paper identifies and quantifies a "priming vulnerability" in Masked Diffusion Language Models (MDLMs): when affirmative tokens appear at intermediate denoising steps, generation is steered toward harmful responses even in safety-aligned models. The authors design two attacks exploiting this vulnerability — an Anchoring Attack (intervention-based, for controlled evaluation) and First-Step GCG (a practical, optimization-based attack using a theoretically-derived lower bound that is ~20× faster than Monte Carlo alternatives). Building on this analysis, they propose Recovery Alignment (RA), an RLHF-style defense that trains models to recover safe responses from adversarially contaminated intermediate states. Experiments across three MDLMs on two benchmarks show RA substantially mitigates the vulnerability while preserving general capability on 11 benchmarks, and also improves robustness against conventional conversational jailbreaks.

## Strengths

- **Novel vulnerability identification and characterization in an underexplored area.** The priming vulnerability is specific to MDLMs' iterative parallel denoising and is clearly distinct from ARMs' prefilling attacks. The vulnerability is quantified systematically via the Anchoring Attack across intervention steps and models (Figure 2, Table 2), showing ASR rises from 2% to ~21% at t_inter=1 and exceeds 80% by t_inter=16 on LLaDA Instruct.

- **Theoretically grounded attack design with practical significance.** Theorem 4.1 provides a lower bound connecting the first-step predictor log-likelihood to the full generation probability. First-Step GCG achieves 58% ASR on LLaDA Instruct (vs. 20% for Monte Carlo GCG) while being ~20× faster (Table 1), demonstrating the vulnerability is exploitable by realistic adversaries.

- **Effective and well-motivated defense.** RA directly addresses the root cause — that standard training only conditions on fully masked starting states — by training on contaminated intermediate states. On LLaDA Instruct, RA reduces ASR under Anchoring Attack at t_inter=4 from 44.0% to 1.3%, and under First-Step GCG from 58.0% to 11.3% (Table 2). The ablation "RA w/o inter" confirms that training on contaminated states (not just RLHF) is crucial for the gains.

- **Comprehensive evaluation.** Three MDLMs (LLaDA Instruct, LLaDA 1.5, MMaDA MixCoT), seven attack methods (four priming-based, three conversational), three safety judges (GPT-4o, LLaMA Guard 3, keyword matching), two datasets (JBB-Behaviors, AdvBench), and 11 capability benchmarks — a thorough empirical picture. Results are consistent across models and evaluators (main paper + Appendix C).

- **Well-designed ablation studies.** The linear scheduling curriculum vs. constant/uniform (Figure 3b) cleanly isolates the benefit of the curriculum. The max intervention step analysis (Figure 3a) shows a clear robustness-vs-stability trade-off.

- **Side benefit of improved robustness against conventional jailbreaks.** RA reduces PAIR ASR from 44.3% to 10.0% on LLaDA Instruct (Table 3), suggesting the recovery capability generalizes beyond priming-specific attacks.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **HumanEval degradation under-discussed.** On LLaDA Instruct, HumanEval drops from 22.0% to 17.1% after RA, a ~22% relative decline. The paper claims "no substantial degradation" (line 775) and attributes PIQA's smaller drop to "potential forgetting," but the HumanEval drop is the largest single-benchmark change and goes unmentioned. The average across 11 benchmarks is indeed flat (52.2 → 52.6), and part of the drop already appears in the RA w/o inter ablation (20.7%), suggesting it stems partly from the RLHF process rather than the intervention training specifically. Still, this should be acknowledged and discussed rather than glossed over.

- **First-step approximation used in RA training is relegated to the appendix.** The GRPO loss in RA replaces the full generation probability over T−t_inter steps with the first-step mask predictor probability (Appendix D.4.1, line 2410–2412). This is a reasonable computational shortcut, but it is a non-trivial design choice that should appear in the main text with a brief justification, since it affects how faithfully the loss reflects the actual generation process. Importantly, this does *not* create a confound with First-Step GCG evaluation — RA's first-step approximation operates from the contaminated state r_t_inter (not from r_0) and computes the probability of the model's own generated response (not the harmful target), so the two are distinct mathematical objects.

- **Abstract slightly overstates the anchoring-attack claim.** The abstract says "simply injecting such affirmative tokens can readily bypass the safety guardrails." At t_inter=1, the Anchoring Attack inserts a full harmful response and re-masks, retaining ~1 token. Appendix C.1 provides good mechanistic evidence that single affirmative tokens suppress refusal probabilities, but no end-to-end ASR experiment with a single standalone token (e.g., "Sure") is reported. The claim is substantially correct — ASR does rise sharply at t_inter=1 — but the abstract's phrasing could be more precise about what was injected. The paper already acknowledges this is a controlled evaluation tool (Section 4.1), so this is primarily a presentation issue.

### Trivial

- Minor numerical inconsistency: the abstract/Figure 2 indicate ~21% ASR at t_inter=1 for LLaDA Instruct, while Table 2 reports 17.3% ± 4.6. These are likely from different runs/evaluations and the difference is within noise, but consistency would improve clarity.

- The paper claims "state-of-the-art robustness" in the narrative (Section 6.2), but RA still leaves substantial ASR under strong attacks like ReNeLLM (72% on LLaDA Instruct, Table 3). The paper does acknowledge this imperfection (line 762–763), so tempering the "state-of-the-art" language would better match the actual results.

## Nice-to-Haves

- An end-to-end ASR experiment with a single affirmative token (e.g., "Sure" or "Step 1:") injected at t_inter=1, to directly validate the abstract's claim without reliance on the Anchoring Attack's oracle response. This would strengthen the practical significance of the vulnerability.

- A deeper analysis of the HumanEval degradation (e.g., qualitative inspection of generated code, gradient similarity between safety and coding tasks) to understand whether it is an inherent cost of safety alignment or addressable through better training recipes.

- Evaluating RA against an attack that optimizes a later-step objective (e.g., t=4 log-likelihood) would test whether the defense generalizes beyond the first-step regime used in training, though the strong results against non-first-step attacks (Anchoring, PAD, DiJA) already provide evidence of generalization.

## Removed Points

*These points are flagged to be removed, treat them with caution.*

1. **Harsh Critic claim: RA uses the same surrogate objective as First-Step GCG, directly confounding evaluation.** REMOVED — This is factually incorrect. RA's GRPO loss approximates π_θ(r_T | q, r_t_inter) — the probability of the model's own generated response from the contaminated state at step t_inter. First-Step GCG maximizes log π_θ(r̃_1 = r_harmful | q ⊕ s, r_0) — the probability of the harmful target from the fully masked initial state r_0. These operate on fundamentally different states (r_t_inter vs. r_0) and different targets (model's response vs. harmful target). The paper's results against Anchoring Attack, PAD, DiJA, and conversational attacks (none of which use first-step surrogates) further demonstrate that RA's effectiveness is not limited to First-Step GCG.

2. **Strength Finder claim: "RA achieves these safety gains without harming general capability" —** PARTIALLY SOFTENED (moved to minor weakness). The average across 11 benchmarks is flat, but the HumanEval drop is notable and under-discussed. The general capability preservation is still a genuine strength, just qualified.

3. **Harsh Critic claim about formatting/typo issues** — REMOVED per hard rule. These are parser artifacts.

4. **Strength Finder generic claims** — REMOVED. Generic statements like "this paper addressed an important problem" without specific citation or evidence are dropped.

## Novel Insights

The paper's key novel insight is that MDLM safety alignment fails because standard training only optimizes behavior from the fully masked initial state r_0 — a narrow slice of the generation trajectory. By explicitly constructing and training on contaminated intermediate states, RA teaches the model a *recovery trajectory* that generalizes surprisingly well: it not only mitigates the targeted priming vulnerability but also improves robustness against conventional conversational jailbreaks. This suggests a broader principle: training models to recover from partially harmful states may be a generally useful safety strategy beyond MDLMs, since any jailbreak that elicits harmful content necessarily passes through states where harmful tokens have begun appearing.

## Suggestions

- Move the first-step approximation discussion from Appendix D.4.1 into the main text (Section 5 or 6.2), with a brief justification of why this approximation is reasonable and why it does not confound the First-Step GCG evaluation.
- Add a sentence in Section 6.3 specifically addressing the HumanEval drop on LLaDA Instruct, noting that part of it appears in the ablation (RA w/o inter) and that the average across benchmarks remains flat.
- Temper the abstract phrasing from "simply injecting such affirmative tokens can readily bypass" to something like "injecting tokens from a harmful response can readily bypass, and even single affirmative tokens substantially suppress refusal behavior."

## Score and Decision

**Anchor comparison:**

| Path | Paper | Avg Score | Comparison |
|------|-------|-----------|------------|
| zBPzxhso8M | DiffuGuard (dLLM training-free defense) | 5.20 | Our paper has a more principled training-based defense, broader attack evaluation, and capability benchmarks; stronger |
| rIPeatvPy3 | DIJA (dLLM attack only) | 5.00 | Attack-only paper with missing ablations; our paper adds a defense and has more complete experiments; stronger |
| jKQQb8uClw | MASK-based dLLM defense | 3.00 | Had critical theoretical proof errors; our paper's theory is simpler and correct; much stronger |
| akbtPEZnDZ | Self-Jailbreaking (RLM discovery) | 5.50 | Discovery paper with limited defense; comparable novelty but our paper provides an actionable defense with stronger empirical validation |
| GpBo97z6GH | Deep Safety Alignment (ARM prefilling) | 3.50 | Questionable novelty and weaker evaluation; our paper is stronger |
| 4YgvVRoSnF | JailbreakLoRA | 4.00 | Different threat model (LoRA supply chain); our paper's attack+defense contribution is more complete |
| f9BuANYtJf | GRAF (multi-turn jailbreak) | 4.40 | Attack-only on ARMs; our paper addresses a new model class with both attack and defense |

The paper under review is clearly stronger than the topically similar dLLM papers (DiffuGuard at 5.20, DIJA at 5.00) because it provides both vulnerability discovery with theoretical grounding AND an effective, well-ablated defense with comprehensive evaluation. The minor weaknesses (HumanEval under-discussion, abstract precision, appendix-deferred detail) are presentational and addressable, not threats to the core claims. The paper sits above the 5.0–5.5 range of comparable dLLM safety papers and merits a score reflecting its completeness and empirical rigor.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>