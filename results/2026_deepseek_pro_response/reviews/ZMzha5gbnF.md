Now I have a clear calibration picture. Let me write the final review.

**Calibration summary:**

| Round | Anchor | Score | Comparison |
|-------|--------|-------|------------|
| R1 | Safety Alignment Should be Made More Than Just a Few Tokens Deep | 9.50 | Clearly much stronger — more comprehensive, cleaner story |
| R1 | Backtracking Improves Generation Safety | 8.00 | Moderately stronger — cleaner defense, simpler mechanism |
| R1 | Diffusion Attacker | 4.75 | Clearly much weaker — significant methodological issues |
| R2 | Catastrophic Jailbreak of Open-source LLMs | 7.00 | Comparable — both identify vulnerability + propose defense; ours has more novel mechanism, theirs has fewer framing issues |
| R2 | Multilingual Jailbreak Challenges | 6.40 | Weaker — smaller scale, simpler defense, less mechanism-driven |
| R2 | Simple Adaptive Attacks | 6.14 | Weaker — attack-only, limited novelty |
| R2 | Endless Jailbreaks with Bijection Learning | 6.25 | Weaker — attack-only |
| R2 | Injecting Universal Jailbreak Backdoors | 6.67 | Harder to compare (backdoor focus); ours is defense-oriented with clearer contribution |
| R2 | One Model Transfer to All | 7.00 | Attack-only, strong but narrower contribution |

**Bracket:** 5.5–7.5 → narrowed to **6.5**. The paper is above the 6.14–6.40 cluster (attack-only or smaller-scale papers) but below the cleaner 7.0–8.0 cluster. RA is well-motivated and effective, the vulnerability is genuinely novel for MDLMs, but the loose theorem, abstract-level overclaiming, and residual vulnerability (ReNeLLM 72%) prevent it from reaching the 7.0+ tier.

---

## Summary
This paper identifies and quantifies a previously unexplored safety vulnerability in Masked Diffusion Language Models (MDLMs) — the "priming vulnerability," where affirmative tokens at intermediate denoising steps steer aligned models toward harmful outputs. The authors demonstrate this through a controlled anchoring attack (diagnostic) and a First-Step GCG attack (practical, non-intervention), then propose Recovery Alignment (RA), which trains models to generate safe responses from intentionally contaminated intermediate states. RA substantially reduces attack success rates across multiple MDLMs while preserving general capability across 11 benchmarks.

## Strengths
- **Convincing empirical demonstration of the priming vulnerability (Figure 2, Table 1).** The anchoring attack cleanly isolates the effect of intermediate-step token injection: a single token at the first denoising step raises ASR on LLaDA Instruct from 2% to 21%, with the effect compounding at later steps. This provides direct, falsifiable evidence for the claimed vulnerability.
- **First-Step GCG is an effective, efficient attack that exploits the vulnerability without intervention (Table 1).** The attack achieves 58.0% ASR vs. 20.0% for Monte Carlo GCG on LLaDA Instruct while being ~20× faster. This demonstrates the vulnerability has practical consequences even for realistic attackers who cannot intervene in the denoising process.
- **RA achieves substantial mitigation across aligned models (Table 2).** On LLaDA Instruct, RA reduces anchoring-attack ASR from 96.7% to 50.7% at t_inter=16 and from 88.7% to 8.3% at t_inter=8, dramatically outperforming baselines including MOSA (the only existing MDLM-specific alignment method).
- **The RA w/o inter ablation cleanly isolates the mechanism (Table 2).** Training with the same RLHF objective but without contaminated intermediate states yields ASR close to the original model, confirming that the benefit of RA is specifically attributable to training on contaminated states, not merely to additional RLHF fine-tuning.
- **General capability is well-preserved across 11 diverse benchmarks (Table 4).** Average accuracy remains essentially unchanged (52.2%→52.6% on LLaDA), and no single benchmark shows catastrophic degradation.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **The abstract overstates the practical severity of intervention-based attacks.** The paper body is clear that the intervention-setting attacker is "hypothetical" and used for diagnosis (lines 35, 84, 88), but the abstract states "simply injecting such affirmative tokens can readily bypass the safety guardrails" without qualification. The non-intervention results (First-Step GCG, PAIR, ReNeLLM) provide a more grounded picture of practical risk. Framing should be aligned throughout the paper.
- **The anchoring attack uses model-generated harmful completions as anchors (line 106), which may inflate the apparent ease of exploitation.** The anchors come from a non-safety-aligned model's harmful responses, which the aligned model might plausibly have generated without alignment. An external attacker without access to a capable unaligned model would need to construct harmful prefixes from scratch — a potentially harder task that is not evaluated. This does not invalidate the vulnerability (it is corroborated by non-intervention attacks), but the severity implied by Figure 2 may be overstated for practical adversaries.
- **Theorem 4.1 provides a loose bound with limited theoretical insight.** The bound relates full-denoising log-likelihood to first-step log-likelihood with a factor of 1/T (T=128), placing almost no constraint on the relationship between surrogate and true objective. The paper acknowledges this indirectly (line 136: "helps compensate for the looseness of the lower bound"). The empirical demonstration that First-Step GCG works is valuable on its own and does not depend on the theorem; the theorem provides formal cover rather than illumination.
- **No comparison of the first-step surrogate against alternative tractable surrogates (Table 1).** The paper shows First-Step GCG outperforms Monte Carlo GCG but does not ablate whether the first step is uniquely effective or whether any early-step surrogate (e.g., summing log-likelihoods over first-k steps) would work similarly well. This leaves open whether the first step per se or the tractability advantage drives the improvement.

### Trivial
None.

## Nice-to-Haves
- Evaluating externally crafted anchors (e.g., template-based "Sure, here is how to...") to distinguish "model is vulnerable to its own latent completions" from "model is vulnerable to any affirmative signal."
- Deeper analysis of why ReNeLLM still achieves 72.3% ASR against RA on LLaDA — this is the most concerning residual vulnerability for practical deployment and warrants more attention than it currently receives.
- Reporting evaluator agreement rates (GPT-4o vs. LLaMA Guard 3 vs. keyword matching) in the main text to increase confidence in ASR measurements.
- MMaDA's inclusion provides limited additional insight for safety claims since its baseline no-attack ASR is already 79.7%; focusing the main evaluation on the two aligned models would sharpen the paper.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Naming inconsistency between "LLaDA" and "LLaMA" in tables:** This is a parser artifact (the original submission does not have this issue). Formatting artifacts are parser errors that should not be attributed to the authors.
- **"Absence of error bars on capability benchmarks (Table 4)":** Standard practice for these benchmarks is single-run evaluation; demanding error bars here is a generic nitpick that does not reflect a real weakness.
- **Demand for a concrete deployment scenario for intervention-based attacks:** The paper already explicitly labels these as hypothetical/diagnostic (lines 35, 84, 88). Criticizing the paper for not specifying a deployment scenario when it already acknowledges the setting is diagnostic is unreasonable. The non-intervention threat model is separately and thoroughly evaluated.
- **"The paper never specifies who can perform such injection" / "white-box access to model internals":** The paper says "hypothetical attacker who can directly intervene" (line 88) — this is sufficient for a diagnostic setting. Demanding a fully specified threat model for a diagnostic tool is scope creep.

## Novel Insights
The paper's insight that MDLM safety alignment trained from fully masked sequences leaves intermediate denoising states unconstrained (Equation 6) is genuinely novel and well-articulated. This explains why existing alignment methods fail against the priming vulnerability and directly motivates the RA design. The recognition that the priming vulnerability can be exploited without intervention — through query optimization that leverages the first-step surrogate — is also a non-obvious extension beyond prior concurrent work that only considered intervention-based attacks.

## Suggestions
- Recalibrate the abstract and introduction to clearly separate diagnostic claims (intervention setting) from practical-threat claims (non-intervention setting). The paper's non-intervention results are strong enough to stand on their own.
- Consider ablating whether First-Step GCG's advantage comes from the first step specifically or from any tractable early-step surrogate (e.g., averaging over first-k step log-likelihoods). This would strengthen the theoretical story.
- Deepen the analysis of the ReNeLLM residual (72.3% ASR) — this is the most important practical failure case and warrants more attention than it currently receives.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>