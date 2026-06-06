## Summary
This paper identifies and quantifies a "priming vulnerability" in Masked Diffusion Language Models (MDLMs): when affirmative tokens for harmful queries appear at intermediate denoising steps, subsequent generation is steered toward harmful responses even in safety-aligned models. The authors design two attacks to expose this vulnerability—an intervention-based "anchoring attack" for characterization, and a non-intervention "First-Step GCG" for realistic exploitation grounded by a theoretical lower bound. They then propose Recovery Alignment (RA), which trains MDLMs to produce safe responses from deliberately contaminated intermediate states, achieving substantial ASR reductions across three models and eleven benchmarks.

---

## Strengths

- **Quantitative characterization of a genuinely novel vulnerability (Figure 2)**: The anchoring attack directly demonstrates a step-dependent effect on LLaDA Instruct, with ASR rising from 2% at step 0 to 21% at step 1 (a single injected token) and exceeding 80% by step 16. This is a concrete, measured discovery, not a conceptual claim.

- **Realistic exploitation via First-Step GCG (Table 1)**: The theoretical lower bound in Theorem 4.1 motivates a fully tractable surrogate. First-Step GCG achieves 58% ASR on LLaDA Instruct (vs. 20% for Monte Carlo GCG) with ~20× speedup, confirming the vulnerability is exploitable without any intervention in the denoising process.

- **Principled and effective defense with clear motivation (Eq. 6, Table 2)**: The informal inequality (6) precisely identifies the gap in standard alignment—conditioning only on fully masked initial states cannot constrain behavior at contaminated intermediate states. RA closes this gap directly: on LLaDA Instruct, anchoring ASR drops from 44% to 1.3% at t=4, and from 68.7% to 3.0% at t=8.

- **Generalization to conventional jailbreaks (Table 3)**: RA also improves robustness under PAIR, Crescendo, and (for LLaDA models) ReNeLLM without being specifically designed for those attacks—a useful practical property.

- **General capability preservation (Table 4)**: Across 11 benchmarks, average performance changes remain within ±0.5 points. TruthfulQA and MBPP improve slightly. PIQA degrades modestly. The safety-utility tradeoff is well-managed.

- **Informative ablations (Figure 3a, 3b)**: The linear curriculum scheduling of t_inter is empirically justified—constant scheduling fails at both extremes, while linear scheduling dominates uniform sampling.

---

## Weaknesses

### Fatal
None.

### Major

- **Unacknowledged regression in Table 3 (MMaDA + ReNeLLM)**: Section 6.2 claims "RA achieves superior robustness against such attacks and outperforms baselines," but for MMaDA under ReNeLLM, RA attains 81.7% ASR versus 75.7% for MOSA and 77.0% for RA w/o inter—RA is the *worst* among those three on this specific combination. The paper does not mention or explain this exception, which undermines the generality of the claim as stated. The claim should be scoped or the anomaly explicitly acknowledged.

- **Transfer mechanism from RA to conventional jailbreaks is asserted, not verified**: Section 6.2 speculates "A plausible mechanism is that the model acquires a new recovery capability. Specifically, when the model generates a harmful response, corresponding harmful tokens necessarily emerge at intermediate steps regardless of the specific attack." This causal chain—that conventional jailbreaks (PAIR, Crescendo) incidentally trigger the same priming dynamic that RA was trained to counter—is never empirically verified. For example, inspecting intermediate denoising states during a successful PAIR attack to check whether affirmative tokens appear early would either confirm or refute this hypothesis. Table 3 results show improvement but do not distinguish between this explanation and simpler explanations (e.g., better general alignment from GRPO-based training on BeaverTails). The mechanism matters because it has implications for RA's scope and failure modes.

### Minor

- **The monotonicity assumption in Theorem 4.1 is given only heuristic justification in the main text**: The theorem requires that `log π_θ(r̃_{t+1} = r | q, r_t) ≥ log π_θ(r̃_1 = r | q, r_0)` for all intermediate steps. The main text offers an intuitive probability-concentration argument, which is plausible but not a proof. Empirical validation is deferred to Appendix C.2. The paper could be clearer that Theorem 4.1 provides a conditional lower bound whose practical status depends on empirical checking, rather than an unconditional guarantee. In practice, this does not invalidate the results, since the theorem motivates a surrogate that empirically works very well.

- **The anchoring attack injects the entire harmful response, then re-masks all but one token (at t_inter=1)**: The conceptual point—a single token biasing the remainder—is compelling and well-reported. But the paper does not address whether an adversary who can inject only an *arbitrary* token (not drawn from a known harmful response) would achieve comparable ASR. This scoping matters for threat model completeness.

### Trivial

- **TruthfulQA improvement is attributed to reward-model alignment improving truthfulness** (Section 6.3)—this is plausible but speculative and stated with more confidence than the data warrants. This is a minor characterization issue.

---

## Nice-to-Haves

- Mechanistic verification of RA's generalization to conventional jailbreaks: trace intermediate denoising states during successful PAIR or Crescendo attacks on undefended models and check whether affirmative tokens appear early. This would either validate or refute the proposed recovery-capability hypothesis.
- Acknowledge potential overlap between BeaverTails (training set for RA) and behaviors covered by JBB-Behaviors and AdvBench. Even a brief discussion of whether evaluation behaviors are largely distinct from training harmful behaviors would address a standard data-leakage concern.
- A principled criterion or heuristic for choosing t_max without per-model empirical search; the current ablation (Figure 3a) provides practical guidance but stops short of a transferable rule.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: MC GCG may be underpowered due to insufficient variance reduction budget.** This is a speculative concern. The paper reports a 20× compute gap and a substantial ASR gap (58% vs. 20%). Requiring the authors to additionally run MC GCG with extra budget or different variance-reduction schemes is asking for experiments not standard in this field, and the concern assumes the gap is primarily variance-driven rather than conceptual. Demoted.

- **Harsh critic: RA is trained on BeaverTails and may not generalize to OOD harmful content patterns.** True in principle, but applies to essentially all safety alignment work. Without a concrete identified failure case, this is a generic concern rather than a specific verified weakness. Demoted to nice-to-have.

- **Harsh critic: The paper fixes L = T = 128 throughout, and performance at longer lengths may differ.** The paper notes Appendix C.5 covers this. Cannot penalize for appendix contents (stripped by parser). Removed.

- **Strength finder: "Effective mitigation via Recovery Alignment" (as a general strength).** Retained and refined above with specific table references rather than the generic framing.

---

## Novel Insights

The paper's most insightful observation—beyond the vulnerability itself—is the structural argument in Eq. (6): standard MDLM alignment, by training only from fully masked initial states, never constrains the model's behavior at contaminated intermediate states. This gap is not a training failure or data insufficiency; it is an architectural consequence of how MDLM training is set up. RA directly addresses this by including contaminated states in the training distribution. The secondary insight is that First-Step GCG can achieve strong attack performance precisely because the priming vulnerability means step-1 token probabilities are already strong predictors of the final denoising outcome—the attack doesn't need to optimize the whole trajectory because influencing step 1 is sufficient.

---

## Suggestions

1. **Explicitly acknowledge and discuss the MMaDA+ReNeLLM counter-example** (Table 3, RA = 81.7% vs. MOSA = 75.7%). Either narrow the claim or provide a hypothesis for the anomaly.
2. **Qualify the causal claim in Section 6.2** about intermediate-step tokens appearing during conventional jailbreaks. If resources allow, add a small empirical check (e.g., inspect 10–20 successful PAIR attack trajectories and report whether affirmative tokens appear in early denoising steps).
3. **Clarify in the main text that Theorem 4.1 is a conditional lower bound**: state explicitly that empirical validation in Appendix C.2 supports the monotonicity assumption across the tested models, so practitioners can check the condition before applying First-Step GCG to new MDLMs.
4. **Add a sentence to the Limitations section** noting that RA's training distribution is BeaverTails-bounded and robustness to novel, out-of-distribution harmful content patterns has not been verified.

---

**Evaluation on Key Axes**

- *Originality*: High. Priming vulnerability in MDLMs is a novel concept; First-Step GCG and Recovery Alignment are new contributions. No prior work provides the structured analysis combining intervention-based measurement, theoretical lower bound, and recovery-based defense.
- *Importance of research question*: High. MDLMs are emerging as alternatives to autoregressive models; MDLM-specific safety research is nascent and this paper opens a new direction.
- *Claims supported by evidence*: Mostly well-supported. The core vulnerability characterization and RA's mitigation of that vulnerability are strongly supported. The claim about RA's robustness to conventional jailbreaks is directionally supported but the mechanistic explanation is speculative, and one exception in Table 3 is unacknowledged.
- *Soundness of experiments*: Good. Three models, two benchmarks, three evaluators, multiple baselines, ablations. The main gap is the missing mechanistic verification.
- *Clarity of writing*: Good. The paper is well-structured, the threat models are clearly delineated, and the intuition for each component is clearly stated.
- *Value to research community*: High. Provides a framework (priming vulnerability characterization + RA) that should inform future MDLM safety work.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>