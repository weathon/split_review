## Summary

This paper identifies the "priming vulnerability" in Masked Diffusion Language Models (MDLMs): if an affirmative token appears at an intermediate denoising step, it can steer even safety-aligned models toward harmful responses. The paper (1) quantifies this vulnerability via the anchoring attack (a single-token injection at step 1 raises ASR from 2% to 21% on LLaDA Instruct), (2) proposes First-Step GCG, a theory-grounded attack that achieves ~20× speedup and 4× higher ASR than Monte Carlo GCG, and (3) develops Recovery Alignment (RA), which trains models to generate safe responses from contaminated intermediate states, reducing ASR to near zero at early intervention steps while preserving general capability.

## Strengths

1. **Controlled, quantitative measurement of the priming vulnerability (Section 4.1, Figure 2).** The anchoring attack precisely measures ASR as a function of intervention step. A single-token injection at step 1 jumps ASR from 2% to 21% on LLaDA Instruct; by step 16/128, ASR exceeds 80% across all three models. This cleanly and reproducibly establishes that the vulnerability exists and is severe.

2. **First-Step GCG attack with theoretical grounding (Theorem 4.1, Table 1).** The paper derives a lower bound connecting first-step log-likelihood to full denoising likelihood, enabling a tractable surrogate objective. First-Step GCG achieves 4× higher ASR and ~20× faster runtime than Monte Carlo GCG (e.g., LLaDA Instruct: 58.0% vs 20.0% ASR; 0.2h vs 4.3h per prompt). This bridges the gap from hypothetical intervention attacks to realistic attacker settings.

3. **Recovery Alignment effectively mitigates the vulnerability while preserving general capability (Tables 2 and 4).** On LLaDA Instruct, RA drops ASR from 17.3%→0.0% at t_inter=1 and from 68.7%→3.0% at t_inter=8, while 11-benchmark average capability is essentially unchanged (52.2→52.6). The ablation "RA w/o inter" (standard RLHF without contamination training) retains high ASR, cleanly isolating why training on contaminated intermediate states is essential.

4. **Curriculum scheduling ablation (Section 6.4, Figure 3b).** Linear scheduling of the intervention step consistently outperforms uniform and constant alternatives, providing a non-obvious design choice backed by empirical evidence.

5. **Evaluation breadth across three MDLM architectures and three safety judges.** Results span LLaDA Instruct, LLaDA 1.5, and MMaDA MixCoT, using GPT-4o, LLaMA Guard 3, and keyword matching, reducing concern that findings are model- or metric-specific.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **SFT baseline behavior is unexplained.** On LLaDA Instruct, the SFT baseline increases "No Attack" ASR from 2.0% to 8.3% (Table 2), making the model less safe than the original. The main text does not explain this behavior or specify the SFT training data/objective (only referencing Appendix D.6). While this does not undermine RA's primary claims — RA also outperforms DPO, MOSA, and the RA w/o inter ablation — it weakens confidence in the baseline comparisons of Tables 2 and 3.

2. **Theorem 4.1's monotonicity assumption has thin main-text justification.** The assumption that log π_θ(r̃_{t+1}=r | q, r_t) ≥ log π_θ(r̃_1=r | q, r_0) for all t is critical to the theoretical grounding of the First-Step GCG attack (which claims 20× speedup and 4× higher ASR). The main text provides only a brief intuitive argument and references Appendix C.2 for empirical verification. A main-text empirical figure showing the log-likelihood across t for several (q, r) pairs would substantially strengthen confidence in this core theoretical claim.

3. **MMaDA results conflate safety alignment with general improvement.** MMaDA MixCoT is not safety-aligned (original no-attack ASR: 79.7%). Applying RA reduces ASR to 3.3% but also improves general capability (33.2→35.0 average, Table 4), suggesting RA's effect on MMaDA blends safety with general instruction-following improvement. Conclusions for the safety-aligned LLaDA models and the unaligned MMaDA should be more clearly separated.

4. **Mixed robustness on one attack/model pair.** While RA generally improves robustness against conventional jailbreak attacks (Table 3), on MMaDA for ReNeLLM, RA's ASR (81.7%) is slightly worse than the original (79.3%) and MOSA (75.7%). The paper's hedge ("often leads to stronger robustness") is appropriate but this exception should be discussed more directly rather than relegated to the last sentence of Section 6.2.

5. **No reporting of training cost.** The paper reports a 2,500-step training budget for RA but does not report GPU hours or wall-clock training time, unlike the detailed runtime reporting for First-Step GCG. This makes it difficult to assess the practical cost of the method relative to baselines.

### Trivial

None.

## Nice-to-Haves

- A main-text empirical plot validating the monotonicity assumption of Theorem 4.1.
- Reporting GPU hours / wall-clock training cost for RA and baselines.
- Sensitivity analysis of the t_min hyperparameter and schedule slope.

## Removed Points

- **Speculation that SFT was trained on harmful data (Harsh Critic).** The paper never states SFT was trained on the same data as RA; SFT details are in Appendix D.6 (which exists in the original submission but is stripped by the parser). The critic's inference that SFT "would reinforce harmful behavior, making it a straw-man baseline" is speculative and removed.

- **Claim that the paper's dismissal of concurrent work is undercut (Harsh Critic).** The paper's use of the anchoring attack for evaluation is entirely appropriate for measuring the vulnerability; the critic's suggestion that this invalidates the paper's critique of concurrent work is a non-sequitur. The paper also evaluates on non-intervention attacks.

- **Data composition details (Harsh Critic).** Criticisms about missing BeaverTails data composition details (number of pairs, harm-category distribution) are about information likely present in the stripped appendix and are removed per hard rules.

- **Critic's misreading of monotonicity reasoning (Harsh Critic).** The critic states the paper's justification "is the opposite of what the assumption needs." In fact, the paper's reasoning (broader distributions early → lower per-token probability; concentrated distributions later → higher probability) is internally consistent and supports the assumption. This criticism is factually incorrect and removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. In the main text, clarify the SFT training data and objective, and explain why its No Attack ASR exceeds that of the original model.
2. Add a main-text empirical figure validating the monotonicity assumption of Theorem 4.1.
3. Separate conclusions for the safety-aligned LLaDA models from the unaligned MMaDA model.
4. Report training GPU hours for RA and baselines to contextualize practical cost.

## Calibration

**Round 1 (Bracketing):** Queried three score bands. Low-band anchors (1.40–3.00: weak jailbreak papers) are far below this paper. Middle-band anchors (4.50–5.80: general DLM capability, diffusion-based attacks, safety debiasing) — this paper is clearly stronger in novelty, evaluation breadth, and principled contribution. High-band anchors (8.00: Backtracking, Booster, Curiosity-driven Red-teaming, etc.) — this paper is competitive but has a few more loose ends in experimental presentation. Initial bracket: [6.0, 8.0].

**Round 2 (Narrowing):** Compared to r42tSSCHPh.md (avg 7.0, catastrophic jailbreak via generation exploitation — vulnerability discovery + mitigation), this paper has a more principled mitigation (RA vs ad-hoc generation-aware training) but slightly less model breadth (3 vs 11). Compared to Bo62NeU6VF.md (avg 8.0, Backtracking — recovery-based safety method for ARMs), this paper's vulnerability discovery is more novel within its niche but its experimental presentation has unresolved questions (SFT baseline, assumption justification) that prevent reaching the same level of polish. Final score: 7.0.

**Anchors consulted (all rounds):** BeOEmnmyFu.md (2.50), 5kMwiMnUip.md (1.40), KyKTjRtyNG.md (3.00), 6Mxhg9PtDE.md (9.50), Qn4HEhezKW.md (5.00), u08UxVNdIo.md (4.75), G7gvaoX9AW.md (5.80), EEWpE9cR27.md (4.50), Bo62NeU6VF.md (8.00), tTPHgb0EtV.md (8.00), 4KqkizXgXU.md (8.00), SPS6HzVzyt.md (8.00), cQCrBJHy0C.md (5.75), hXA8wqRdyV.md (6.14), lm7MRcsFiS.md (6.00), r42tSSCHPh.md (7.00), vESNKdEMGp.md (6.40), 45rvZkJbuX.md (6.50).

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>