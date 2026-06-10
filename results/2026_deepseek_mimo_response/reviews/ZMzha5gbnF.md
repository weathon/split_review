Now I have enough data. Let me finalize the review.

The paper under review compares as follows:
- **vs hXA8wqRdyV (6.14, accepted):** Paper under review is stronger — it has both attack and defense with theoretical contribution, vs. attack-only.
- **vs r42tSSCHPh (7.00, accepted):** Comparable quality — both discover novel vulnerabilities, both propose defenses, both have comprehensive experiments. Paper under review has stronger theoretical grounding (Theorem 4.1).
- **vs Bo62NeU6VF (8.00, accepted):** Backtracking is simpler, more broadly applicable (works for ARMs), with cleaner evaluation. Paper under review is more theoretically rich but has a notable evaluation gap (no benign refusal rates). Somewhat weaker.
- **vs weak anchors (1.4-3.0):** Clearly much stronger.
- **vs middle anchors (3.67-5.75):** Clearly stronger.

**Round-1 bracket:** 5–8  
**Round-2 bracket:** 6.5–7.5  
**Final score:** 7.0 — comparable to the Catastrophic Jailbreak paper (7.00), with similar structure (vulnerability discovery + defense + comprehensive experiments) but stronger theoretical contribution, offset by the missing benign refusal evaluation.

---

## Summary
This paper identifies and characterizes a novel safety vulnerability in Masked Diffusion Language Models (MDLMs) — the "priming vulnerability" — where affirmative tokens at intermediate denoising steps steer generation toward harmful completions. The authors derive a theoretical lower bound enabling a practical optimization-based attack (First-Step GCG, ~20× faster and 4× higher ASR than MC GCG) and propose Recovery Alignment (RA), which trains models to recover from contaminated intermediate states using RLHF-style optimization. Experiments across three MDLMs demonstrate substantial ASR reduction with preserved general capability.

## Strengths
- **Novel, MDLM-specific vulnerability with compelling empirical evidence**: Injecting a single token at step 1 out of 128 raises ASR from ~0% to 40% on LLaDA Instruct (Table 2, anchoring attack). This is a non-obvious finding specific to the parallel iterative denoising mechanism with no direct ARM analog.
- **Theoretical contribution with direct practical impact**: Theorem 4.1 derives a tractable lower bound on the GCG objective (Equation 3), yielding First-Step GCG that achieves 58% ASR on LLaDA Instruct vs. 20% for MC GCG while being ~20× faster (Table 1). The theory directly enables a stronger, more practical attack method.
- **Contaminated-state training is the key ingredient (clean ablation)**: The "RA w/o inter" ablation (Table 2) shows ASR of 22% at step 4 on LLaDA Instruct (standard RLHF from fully masked states) vs. 1.3% with full RA, cleanly isolating the central design choice.
- **Comprehensive experimental design**: Three MDLMs, four priming-specific attacks, three conversational jailbreaks, and 11 capability benchmarks, with mean ± std over three runs and ablations on scheduling and max intervention step.
- **General capability preserved**: Table 4 shows average accuracy maintained or slightly improved across all three models after RA training (e.g., LLaDA 52.2→52.6, MMaDA 33.2→35.0).

## Weaknesses

### Fatal
None.

### Major
- **Missing evaluation of refusal behavior on benign queries**: For any safety mitigation, the question is not only "does it reduce ASR?" but also "does it refuse legitimate requests?" RA trains with a reward model on contaminated harmful states, which could plausibly cause over-cautious behavior. Table 4 reports 11 capability benchmarks, but none measure refusal rates on harmless queries. A method that refuses everything would score perfectly on ASR but be useless. This is the most impactful missing piece for validating the safety-utility trade-off.

### Minor
- **Uneven effectiveness across models and attacks**: Against ReNeLLM, RA still yields 72–82% ASR across all models (Table 3). On MMaDA, First-Step GCG ASR drops from 92.7% to 45.7% (Table 2) — substantial improvement but nearly half of attacks still succeed. The paper acknowledges this (line 243: "RA remains imperfect against strong attacks"), but the abstract's framing ("significantly mitigates the vulnerability") could be more explicit about these residual failure modes.
- **Theorem 4.1's monotonicity assumption scope could be better characterized in the main text**: The paper notes empirical validation in Appendix C.2 and provides intuition for why it holds (line 130), but the main text should briefly note conditions under which it may break (e.g., when fixed tokens are inconsistent with the target response), since this assumption underpins the theoretical result.
- **RA novelty slightly overstated**: The abstract calls RA a "novel safety alignment method," but it is GRPO applied with a specific training data strategy (contaminated intermediate states). The novelty is in the design choice of what states to train from, not the algorithmic framework itself. This is a framing issue — the contribution is still valuable.

### Trivial
None.

## Nice-to-Haves
- Analysis of why RA generalizes to conventional jailbreaks (e.g., tracking intermediate denoising trajectories under PAIR/Crescendo) would strengthen the generalization claim beyond the plausible mechanism suggested in Section 6.2.
- Discussion of why MMaDA remains more vulnerable after RA than LLaDA models, to help the community understand which model properties affect mitigation effectiveness.

## Removed Points
These points are flagged to be removed; treat them with caution.
- **"Comparison with vanilla RLHF on harmful data"** — The harsh critic requested a comparison with standard RLHF on BeaverTails without contaminated states. However, the "RA w/o inter" ablation already IS exactly this (line 237: "we set t_min = t_max = 0 and train the model only from the fully masked sequences without intervention, same as RLHF Ouyang et al. (2022)"). The critic overlooked this.
- **"RA novelty is overstated" — demoted**: While the abstract says "novel safety alignment method," the paper's contribution (contaminated-state training paradigm) is genuinely novel and specific to MDLMs. The framing is slightly inflated but the substance is there. Kept as minor.

## Novel Insights
The paper makes a genuinely novel observation that MDLMs' iterative denoising mechanism creates a distinct vulnerability class not present in autoregressive models: partial contamination of intermediate states can irreversibly steer generation toward harm, and this occurs because standard training (from fully masked states) creates a blind spot at intermediate denoising states. This insight — that the training initialization choice creates a gap in safety coverage — is non-obvious and has direct practical implications for how MDLMs should be safety-aligned as they become more widely deployed. The derivation of a tractable lower bound enabling First-Step GCG is also a non-trivial theoretical contribution.

## Suggestions
- Add a table or analysis of refusal rates on benign queries (e.g., benign subset of JBB-Behaviors) to demonstrate that RA does not introduce over-refusal.
- Briefly characterize in the main text when the monotonicity assumption in Theorem 4.1 may fail, even if detailed validation is in the appendix.
- Consider adding a brief analysis of intermediate denoising trajectories under conventional jailbreaks to explain why RA generalizes beyond priming-specific attacks.

## Score and Decision

**Anchors retrieved across all rounds:**

| Round | Path | Avg Score | Comparison |
|-------|------|-----------|------------|
| 1 | BeOEmnmyFu | 2.50 | Weak jailbreak attack paper; paper under review is much stronger |
| 1 | 5kMwiMnUip | 1.40 | Weak jailbreak paper; paper under review is far stronger |
| 1 | KyKTjRtyNG | 3.00 | Multi-round jailbreaking; paper under review is much stronger |
| 1 | lUyYX9VFgA | 3.00 | Probing AI safety; paper under review is much stronger |
| 1 | 1zt8GWZ9sc | 3.67 | Role-playing jailbreak; paper under review is clearly stronger |
| 1 | zf53vmj6k4 | 4.25 | Political correctness analysis; paper under review is clearly stronger |
| 1 | FD9sPyS8ve | 4.75 | Purple problem defense study; paper under review is stronger |
| 1 | HuNoNfiQqH | 4.75 | Latent space jailbreak analysis; paper under review is stronger |
| 1 | tyEyYT267x | 8.00 | SAR diffusion LM; different topic, but accepted paper quality comparable |
| 1 | 84n3UwkH7b | 8.00 | Memorization in diffusion models; different topic |
| 1 | Bo62NeU6VF | 8.00 | Backtracking for safety; similar spirit but cleaner evaluation, broader applicability |
| 1 | 4KqkizXgXU | 8.00 | Red-teaming; different topic |
| 2 | hXA8wqRdyV | 6.14 | Adaptive jailbreak attacks; attack-only, paper under review is stronger |
| 2 | V7PYbRzD0h | 5.33 | Image jailbreak; paper under review is stronger |
| 2 | RdGvvqjkC1 | 5.75 | Defense mechanism study; paper under review is stronger |
| 2 | r42tSSCHPh | 7.00 | Generation exploitation attack+defense; comparable structure and quality |
| 2 | vjel3nWP2a | 6.67 | Training data extraction; different topic |
| 2 | YauQYh2k1g | 6.25 | Agent robustness; different topic |
| 2 | sULAwlAWc1 | 7.00 | Robust jailbreak generation; attack-only, paper under review is stronger |

**Round-1 bracket:** 5–8 (clearly above weak/middle anchors, below the 8.0 accepted papers in adjacent areas)  
**Round-2 bracket:** 6.5–7.5 (stronger than 6.0–6.5 attack-only papers, comparable to 7.0 anchor r42tSSCHPh, somewhat below 8.0 Bo62NeU6VF)  

**Final score: 7.0.** The paper is comparable to the "Catastrophic Jailbreak" paper (r42tSSCHPh, 7.00), which similarly discovers a novel vulnerability and proposes a defense, with comprehensive experiments. The paper under review has stronger theoretical contribution (Theorem 4.1, First-Step GCG) and broader evaluation scope, offset by the missing benign refusal rate evaluation. It is somewhat below the "Backtracking" paper (Bo62NeU6VF, 8.00), which has cleaner evaluation and a simpler, more broadly applicable method.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>