Now I have sufficient calibration. Let me write the final review.

## Summary

This paper identifies and characterizes the **priming vulnerability** in Masked Diffusion Language Models (MDLMs): if an affirmative token for a harmful query appears at an intermediate denoising step, subsequent generation can be steered toward a harmful response, even in safety-aligned models. The authors (1) quantify this vulnerability via the anchoring attack (injecting tokens from a harmful response into the denoising trajectory), (2) derive a theoretical lower bound (Theorem 4.1) connecting the full-sequence attack objective to a tractable first-step surrogate, enabling First-Step GCG — a 20× faster optimization-based attack — and (3) propose **Recovery Alignment (RA)**, which trains the model to generate safe responses from intentionally contaminated intermediate states. Experiments across three MDLMs (LLaDA, LLaDA 1.5, MMaDA) show that RA reduces ASR near zero on early-intervention anchoring attacks, outperforms baselines (SFT, DPO, MOSA) on PAD and DiJA attacks, provides moderate gains on conventional jailbreaks (PAIR, ReNeLLM, Crescendo), and preserves general capability on 11 benchmarks.

---

## Strengths

- **Quantitative characterization of a novel vulnerability (Section 4.1, Figure 2):** The paper systematically measures the priming vulnerability via a controlled anchoring attack, showing that even a single-token injection at step 1 raises ASR from 2% to 21% on LLaDA Instruct. This clean experimental design isolates the vulnerability mechanism.

- **Theoretical lower bound connecting vulnerability to tractable optimization (Theorem 4.1, Section 4.2):** The monotonicity-based bound enables First-Step GCG, which circumvents the intractable gradient over stochastic denoising paths. While the assumption is strong, the bound provides a principled rationale for why optimizing the first-step log-likelihood serves as an effective surrogate.

- **First-Step GCG achieves strong practical gains (Table 1):** First-Step GCG raises ASR to 58.0% on LLaDA Instruct (vs. 20.0% for Monte Carlo GCG) while reducing per-prompt runtime from 4.3h to 0.2h (~20× faster). This demonstrates that the priming vulnerability is exploitable without intervention in the denoising process.

- **RA effectively mitigates the anchoring attack and generalizes to different injection patterns (Table 2):** RA achieves near-zero ASR on early intervention steps (e.g., 0.0%, 1.3%, 3.0% at steps 1, 4, 8 on LLaDA) and substantially outperforms all baselines including MOSA on PAD and DiJA — attack patterns RA was not explicitly trained on. The ablation (RA w/o inter) confirms that training from contaminated intermediate states is essential.

- **General capability is preserved across 11 diverse benchmarks (Table 4):** RA shows negligible degradation (LLaDA average 52.6 vs. original 52.2), with improvements on TruthfulQA and MBPP. This rules out the common concern that safety gains come at the cost of widespread utility loss.

---

## Weaknesses

### Major
None.

### Minor

1. **The monotonicity assumption in Theorem 4.1 is non-trivial and its empirical validation is deferred.** The assumption requires that the log-probability of the target harmful response at every step is at least as high as at step 1. While physically plausible (later steps have more context), the assumption could fail for responses that become inconsistent with partially fixed tokens. The paper states empirical validation exists in Appendix C.2 (stripped by the parser), but the main text would benefit from a brief validation example or a discussion of cases where the assumption might fail.

2. **Improvement on conventional jailbreak attacks is real but inconsistent, and the mechanism is hypothesized not proven.** In Table 3, PAIR drops substantially (e.g., LLaDA: 44.3% → 10.0%) but ReNeLLM remains high (92.7% → 72.3%). The paper speculates that conventional attacks "necessarily" cause harmful tokens to appear at intermediate steps, but provides no analysis verifying this mechanism. Without evidence that these attacks actually trigger the priming vulnerability, it is unclear whether RA's benefit on these attacks is due to its specific design or to generic alignment effects.

3. **No control experiment isolating the effect of "affirmative" tokens vs. other injected tokens.** The vulnerability definition centers on "affirmative tokens," but the anchoring attack always injects tokens from a harmful response (which includes both affirmative and content-bearing tokens). Injecting a neutral token, a refusal token, or a random token at the same step would clarify whether the effect is specific to affirmative/harmful-consistent tokens or is simply a general sensitivity to any injected token.

4. **Statistical granularity and significance.** The No Attack baseline ASR of 2.0% → 0.0% for RA (Table 2) on a 100-prompt dataset is within noise (standard error ~1.4% for a 2% estimate). The larger effects at non-zero intervention steps are meaningful, but the paper should clarify the statistical treatment of near-zero results.

5. **Training cost (GPU-hours, wall time) is not reported in the main text.** The paper states cost is in Appendix C.4 (stripped), but the main text would benefit from a brief summary of computational requirements for practitioners considering adopting RA.

### Trivial
- All main results are reported on JBB-Behaviors with GPT-4o as judge; results with other evaluators (LLaMA Guard 3, keyword) and the AdvBench dataset are deferred to the appendix.

---

## Nice-to-Haves
- A sensitivity analysis showing whether the effect holds when injecting non-affirmative tokens (neutral, refusal, random) at step 1 would sharpen the claim that "affirmative" tokens are the causal mechanism.
- An analysis verifying whether conventional jailbreak attacks (PAIR, ReNeLLM, Crescendo) actually induce affirmative tokens in intermediate MDLM states would clarify the mechanism behind RA's generalization.
- Reporting GPU-hours and wall time for RA training in the main text would help practitioners assess practical overhead.

---

## Removed Points
**These points were raised by reviewers but are flagged to be removed. Treat them with caution.**

1. **Data leakage claim (BeaverTails→JBB):** The critic claimed potential data leakage because RA is trained on BeaverTails and evaluated on harmful responses from that dataset. This is incorrect. Training uses BeaverTails; evaluation uses JBB-Behaviors (Section 4.1). The harmful responses injected in the anchoring attack are generated by a non-safety-aligned model (Appendix D), not from BeaverTails.
2. **Anchoring attack is "effectively prompting with a harmful response":** At step 1, only ~1 token (on average) is injected due to the masking schedule (L=T=128, re-masking prob 127/128). The paper explicitly states "inserts only a single token." This is not equivalent to providing the full harmful response as context.
3. **No comparison against GCG on first token only:** First-Step GCG is precisely GCG on the first-step log-likelihood. The critic's suggestion is already what the paper implements.
4. **Circular evaluation (entirely):** While the anchoring attack is the training distribution for RA, the paper also evaluates on PAD and DiJA (different injection patterns) and conventional jailbreak attacks (PAIR, ReNeLLM, Crescendo). The claim of circularity is substantially overstated.
5. **Missing appendix content / proofs / empirical validation:** Per meta-review policy, parser-stripped appendix content is not considered a weakness of the paper.
6. **Overclaiming in abstract:** The abstract claims "significantly mitigates the vulnerability" and "improves robustness against conventional jailbreak attacks." These are supported by the evidence (near-zero ASR on anchoring, reduced ASR on PAIR/Crescendo). The claim is not overblown.

---

## Novel Insights

The harsh critic treats the anchoring attack as a "circular evaluation" and the improvement on conventional attacks as "moderate." But the paper's most interesting finding — that RA also reduces ASR on **PAD** and **DiJA** (Table 2) — survives this criticism. PAD injects "Step1:" and "Step2:" tokens at fixed positions with all other positions masked; DiJA uses structured mask-text templates. Neither attack pattern was seen during RA training, yet RA reduces PAD ASR from 67.3% to 1.0% and DiJA from 92.0% to 35.7% on LLaDA. This suggests that RA learns a general capability — detecting and recovering from *any* contaminated intermediate state — rather than memorizing specific injection patterns. This generalization is the paper's strongest result, stronger than the anchoring attack results themselves. The paper understates this point, focusing more on the anchoring attack where the comparison to baselines is most dramatic.

---

## Suggestions
1. Add a control experiment injecting neutral or refusal tokens at step 1 to isolate the "affirmative token" hypothesis.
2. Include an analysis (even qualitative) of whether PAIR/ReNeLLM/Crescendo actually produce affirmative tokens in intermediate MDLM states, to substantiate the hypothesized mechanism for generalization.
3. Report training cost (GPU-hours) and statistical significance of near-zero ASR claims in the main text.
4. Move one appendix result (e.g., AdvBench or LLaMA Guard 3 evaluation) to the main text to broaden the evidence base.

---

## Score and Decision

**Calibration report:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| "The Devil behind the mask" (DIJA) | 5.0 | R1 | Attack-focused dLLM safety paper; this paper is stronger because it also proposes an effective defense. |
| "DiffuGuard" | 5.2 | R1 | Defense-focused dLLM paper; this paper's training-time defense is more principled. |
| "A2D" | 5.5 | R2 | Token-level alignment defense; similar scope, comparable quality. This paper covers more attack types. |
| "From Vulnerability to Defense" | 3.0 | R1 | Similar scope but had flawed proofs; this paper is substantially stronger. |
| SAMA (MIA) | 5.5 | R2 | Different sub-area (privacy); comparable thoroughness of evaluation. |
| "Safety Mirage" | 5.5 | R2 | Different domain (VLMs); comparable rigor. |

Round 1 bracket: 4.5–6.5. Round 2 narrowing placed it alongside A2D (5.5) and the MIA paper (5.5). This paper is slightly stronger than the DIJA paper (5.0) because it provides a full vulnerability-to-mitigation narrative, and comparable to A2D (5.5) in scope and rigor, though A2D achieves more dramatic ASR reductions on its target attack. I assess the paper at the upper end of its comparable anchors because the combination of vulnerability discovery, theoretical connection, First-Step GCG, and RA defense with generalization evidence constitutes a complete contribution.

**Score rationale:** The paper identifies a genuinely novel vulnerability, provides both attack and defense, and validates across multiple models, benchmarks, and attack types. The main weaknesses (strong theoretical assumption, inconsistent generalization to some conventional attacks, missing control experiments) are minor — they do not undermine the core claims. The paper is well-written and the experiments are largely sound.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>