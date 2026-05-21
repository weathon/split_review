Now I have all the information needed to synthesize the final review.

## Summary

This paper identifies and characterizes the "priming vulnerability" in Masked Diffusion Language Models (MDLMs): a single affirmative token at an intermediate denoising step can steer generation toward a harmful response, even in safety-aligned models. The authors design the anchoring attack to quantify this vulnerability (ASR jumps from 2% to 21% with one-token intervention at step 1), derive a theoretical lower bound enabling First-Step GCG (a non-intervention optimization attack that is 20× faster and up to 4× more effective than Monte Carlo GCG), and propose Recovery Alignment (RA), which trains models to generate safe responses from contaminated intermediate states. Experiments across three MDLMs show RA reduces ASR to near zero for early intervention steps, outperforms baselines including SFT, DPO, and MOSA, preserves general capability across 11 benchmarks, and improves robustness against conversational jailbreak attacks.

## Strengths

- **First systematic quantification of priming vulnerability in MDLMs**: The anchoring attack (Section 4.1) provides a clean, controlled measurement. Figure 2 shows that even a single affirmative token at step 1 raises ASR from 2% to 21% on LLaDA Instruct, establishing a clear causal link between intermediate-token injection and harmful outputs. This is the first principled analysis of this MDLM-specific vulnerability.

- **First-Step GCG dramatically improves efficiency and effectiveness**: Table 1 shows First-Step GCG is approximately 20× faster (0.2h vs. 4.1–4.3h per prompt) and achieves up to 4× higher ASR (58.0% vs 20.0% on LLaDA Instruct) compared to Monte Carlo GCG. This demonstrates that the priming vulnerability is exploitable even by attackers who cannot intervene in the denoising process.

- **Recovery Alignment reduces ASR to near zero for early-to-moderate intervention steps**: Table 2 reports RA drops ASR at t_inter=1 from 17.3% (original LLaDA Instruct) to 0.0%, and at t_inter=4 from 44.0% to 1.3%. The RA w/o inter ablation confirms that explicitly training on contaminated intermediate states is necessary — all baselines (SFT, DPO, MOSA, RA w/o inter) remain well above RA across nearly all settings and models.

- **Consistent outperformance of baselines across three MDLMs and multiple attack types**: Table 2 and Table 3 show RA achieves the lowest ASR across anchoring attacks at multiple intervention steps, PAD, DiJA, First-Step GCG, PAIR, ReNeLLM, and Crescendo. The improvement generalizes beyond the exact training pattern.

- **General capability is preserved with no substantial degradation**: Table 4 reports average accuracy for LLaDA moves from 52.2% (original) to 52.6% (RA), and for LLaDA 1.5 from 52.7% to 52.8% across 11 diverse benchmarks, with slight improvements on TruthfulQA and MBPP.

- **Ablation studies validate the linear curriculum design**: Figure 3b demonstrates that linear scheduling of the intervention step consistently outperforms constant and uniform scheduling, confirming that gradual exposure to harder contamination states is crucial for learning robust recovery.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported by the evidence.

### Minor

- **Theorem 4.1's monotonicity assumption is not validated in the main text**: The lower bound for First-Step GCG (Equation 3) relies on the assumption that $\log \pi_\theta(\tilde{r}_{t+1}=r \mid q, r_t) \ge \log \pi_\theta(\tilde{r}_1=r \mid q, r_0)$ for all $t$. The paper provides a plausibility argument about probability mass concentrating in later steps but defers empirical validation to Appendix C.2 (stripped from the submission). The paper's plausibility argument is reasonable, and the empirical success of First-Step GCG does not depend on the bound being tight — it works well regardless. However, the theorem is presented as a key theoretical contribution, and the paper would be strengthened by including direct empirical evidence of the assumption's validity in the main text, or by reframing First-Step GCG as an empirically motivated heuristic rather than a theoretically grounded surrogate.

- **The distinction between the priming vulnerability and the ARM prefilling vulnerability is somewhat overstated**: The paper frames the priming vulnerability as fundamentally new to MDLMs (Section 1: "this stands in contrast to the vulnerability exploited by prefilling attacks on ARMs"). Both vulnerabilities share the core mechanism that "if the model sees affirmative context, it tends to continue harmfully." The real contribution is the specific study of *how* this manifests in MDLMs' iterative denoising process (intermediate-step injection + re-masking interaction) and the development of corresponding attacks and defenses, not the discovery that affirmative conditioning leads to harmful continuation. This does not affect the technical contributions but slightly overstates the novelty of the vulnerability concept itself.

- **Generalization scope of RA is not fully characterized**: While RA shows clear generalization to conversational attacks (PAIR, ReNeLLM, Crescendo), the paper does not test against attacks that avoid surface-level contamination (e.g., obfuscated prompts or encoding-based attacks). The paper partially acknowledges this ("the alignment can be circumvented when the harmfulness is not detectable from the surface form of the response"), but the scope limitation could be stated more explicitly upfront. The RA defense is trained on exact harmful-response injection, and its effectiveness against attacks that do not leave traceable affirmative tokens in the generation path remains unproven.

- **Results on the unaligned MMaDA model are less compelling**: RA reduces MMaDA's ASR substantially but still leaves non-trivial vulnerability (e.g., 34.3% at t_inter=16 for anchoring, 70.0% for DiJA, 81.7% for ReNeLLM). While this is expected for a model with no initial safety alignment, the paper could discuss whether RA is sufficient as a standalone alignment method for unaligned models or primarily effective as a supplement to existing alignment.

### Trivial

- The paper fixes $L = T = 128$ throughout; ablating over these hyperparameters (briefly mentioned in Appendix C.5) would strengthen robustness claims if included in the main text.

## Nice-to-Haves

- Direct empirical validation of the monotonicity assumption (Theorem 4.1) in the main text, or dropping the theorem framing and presenting First-Step GCG as an empirically effective heuristic.
- Testing RA against an adaptive attack specifically designed to avoid leaving surface-level contamination signals in intermediate states.
- Reporting variance or confidence intervals for the general capability results in Table 4 (currently reported as single-point accuracy values).
- Ablating over response length $L$ and step count $T$ in the main text rather than deferring to the appendix.

## Removed Points

These points were flagged by reviewers but are removed with justification:

- *RA trained on the exact attack pattern (anchoring attack) and may not generalize* — **Removed because the paper already tests generalization to PAD, DiJA, First-Step GCG, PAIR, ReNeLLM, and Crescendo, and explicitly acknowledges the limitation (RA "remains imperfect against strong attacks, such as ReNeLLM" and can be "circumvented when harmfulness is not detectable from the surface form"). The paper adequately addresses this scope concern.**
- *Missing variance for general capability results* — **Removed from weaknesses and moved to Nice-to-Haves; single-run evaluations on standardized benchmarks are standard practice for this type of evaluation.**
- *Availability of harmful responses for RA training as a practical limitation* — **Removed as a weakness because it is a reasonable assumption that such datasets exist (BeaverTails is cited and used); the paper does not claim RA works without any data.**
- *Strength Finder's generic strengths about the problem being important* — **Removed as they are generic/superficial; kept only concrete, evidence-grounded strengths.**
- *Defense does not require harmful responses (as a missing discussion)* — **Removed; the paper explicitly states it uses the BeaverTails dataset for harmful pairs and explains the data requirement.**

## Novel Insights

The reviews surface an interesting tension in the paper's framing. The harsh critic correctly notes that Theorem 4.1's monotonicity assumption is unverified in the main text, but this does not invalidate the empirical results — First-Step GCG works well regardless. This suggests a broader observation about safety research on emerging model classes: theoretical bounds can serve as *design inspiration* for practical attacks without needing full rigor, as long as the empirical evidence is independently convincing. The paper implicitly demonstrates this: the most compelling evidence for the priming vulnerability is not the theorem but the stark Figure 2 (a single token at step 1 raising ASR to 21%) and the significant empirical gains in Table 1. Another notable point from synthesis is that the paper's dual-attack framing (intervention and non-intervention threat models) is a particularly strong design choice — it addresses the concern that the vulnerability might only be exploitable under unrealistic attacker assumptions, making the case for the defense more compelling.

## Suggestions

- **Strengthen Theorem 4.1**: Either provide a plot of $\log \pi_\theta(\tilde{r}_t = r \mid q, r_{t-1})$ across denoising steps in the main text to validate the monotonicity assumption, or remove the theorem framing and present First-Step GCG as an empirically motivated surrogate objective. The paper's empirical contributions are strong enough not to need a formal theorem that relies on an unproven assumption.
- **Sharpen the scope statement for RA**: Explicitly state in Section 5 or the Conclusion that RA is most effective against attacks producing detectable contamination signals in intermediate states, and that robustness against obfuscated/stealthy attacks remains open. The current acknowledgment is somewhat buried.
- **Add an adaptive attack experiment**: Evaluate RA against an attack that deliberately avoids leaving surface-level affirmative tokens in the generation trace, to characterize the defense's boundaries more precisely.
- **Consider reporting with variance for Table 4**: While single-run evaluation is standard, the claim that general capability is "preserved" would be strengthened by multiple runs or by explicitly noting that the slight fluctuations are within expected measurement noise.

## Score and Decision

**Calibration summary:**

**Round 1 — Bracketing (score bands):**
- Weak band (<3.5): Papers like "NEMESIS" (1.40) and "Playing Language Game" (2.50) — rejected, clearly weaker than the paper under review.
- Middle band (3.5–7.5): "Diffusion Attacker" (4.75, withdrawn), "Weak-to-Strong Jailbreaking" (5.40, rejected), "Catastrophic Jailbreak" (7.00, accepted spotlight), "h4rm3l" (6.75, accepted poster), "BadJudge" (6.75, accepted poster), "SoC Attacks" (6.25, accepted poster).
- Strong band (>7.5): "Safety Alignment Should be Made More Than Just a Few Tokens Deep" (9.50, oral), "Block Diffusion" (8.00, oral).

The paper is clearly above the weak band and below the top-tier oral papers. Initial bracket: **4.5–7.5**.

**Round 2 — Narrowing (5.5–7.5):**
- *Catastrophic Jailbreak* (7.00, spotlight): Both papers have a similar structure (vulnerability discovery + defense + utility preservation). The catastrophic jailbreak paper is cleanly executed and well-written. The MDLM paper under review is slightly more exploratory (newer model class, more complex defense mechanism) and has a minor theoretical looseness (Theorem 4.1 assumption). The MDLM paper is comparable in quality but a notch below the spotlight-level cleanliness.
- *Weak-to-Strong Jailbreaking* (5.40, rejected): Suffered from novelty concerns (method too similar to prior work) and a weak threat model. The paper under review has clearer novelty (first systematic study of this MDLM vulnerability) and a more realistic threat model (two threat models, both carefully scoped).
- *h4rm3l* (6.75, accepted poster): Strong engineering contribution but narrower in scope. The paper under review has a similar level of contribution — both are accepted-level work with specific novel contributions and solid experiments.
- *BadJudge* (6.75, accepted poster): Different topic but similar quality bar. The paper under review is at a comparable level.

The paper is closer to the 7.0 (Catastrophic Jailbreak) end of the bracket than the 5.4 (Weak-to-Strong) end. Considering the solid experiments, clear novelty in studying an under-explored model class (MDLMs), effective defense, and good writing — but discounted slightly for the theoretical looseness and overclaimed vulnerability distinction — the paper lands at **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>