Now let me run calibration searches to anchor the score.Now I have enough to write the final review. Let me synthesize everything.

---

## Summary

This paper identifies and characterizes a **priming vulnerability** specific to Masked Diffusion Language Models (MDLMs), wherein affirmative tokens appearing at intermediate denoising steps can steer subsequent generation toward harmful content even in safety-aligned models. The paper provides a controlled anchoring attack (intervention-based) to measure the vulnerability, a First-Step GCG attack (realistic, no-intervention) grounded in a theoretical lower bound exploiting the vulnerability, and a defense called **Recovery Alignment (RA)** that trains models to recover safe responses from adversarially contaminated intermediate states. Experiments span three MDLMs, two safety benchmarks, multiple attack methods, and eleven general capability benchmarks.

---

## Strengths

- **Concrete quantification of a novel MDLM-specific vulnerability**: Figure 2 and the accompanying data table show that injecting a single token at step 1 raises ASR from 2% to 21% on LLaDA Instruct, and ASR exceeds 80% by step 16 across all models. The step-by-step structure of MDLMs provides a uniquely exploitable surface not present in ARMs.

- **Principled, effective First-Step GCG attack**: Theorem 4.1 provides a formal lower bound justifying maximizing first-step log-likelihood as a surrogate for the intractable full denoising objective. Table 1 shows this achieves 58% ASR on LLaDA Instruct versus 20% for MC GCG, while being ~20× faster — demonstrating the vulnerability is exploitable by realistic adversaries, not just hypothetical ones.

- **Well-motivated defense grounded in analysis**: The paper correctly formalizes why existing alignment fails (inequality (6): conditioning on contaminated state $r_t$ raises harmful generation probability above the fully-masked baseline $r_0$). This directly motivates RA's training on contaminated intermediate states, making the connection between diagnosis and treatment unusually tight.

- **Comprehensive evaluation**: RA is evaluated across 3 MDLMs, 4 priming-vulnerability attacks, 3 conversational jailbreaks, and 11 general capability benchmarks. RA dramatically reduces ASR (e.g., from 44.0% to 1.3% at $t=4$ for LLaDA Instruct) and preserves general capability within ±0.5 average points. The ablation studies (Figure 3a/3b) provide clear, actionable insight into the role of curriculum scheduling.

- **Clear ablation validating design choices**: The comparison of linear, uniform, and constant scheduling in Figure 3b shows that constant scheduling fails at both extremes while linear curriculum succeeds — providing concrete practical guidance.

---

## Weaknesses

### Fatal
None.

### Major

- **Unacknowledged regression in Table 3 (MMaDA + ReNeLLM)**: Section 6.2 claims "RA achieves superior robustness against such attacks and outperforms baselines" for conversational jailbreaks. However, Table 3 shows that for MMaDA under ReNeLLM, RA achieves 81.7% ASR — *higher* than both MOSA (75.7%) and RA w/o inter (77.0%). This is a concrete counter-example to the uniformly positive framing and should be addressed. The general claim should be qualified to reflect this non-uniformity.

- **Transfer mechanism from anchoring-attack training to conventional jailbreaks is asserted, not demonstrated**: Section 6.2 proposes a "plausible mechanism" — that "harmful tokens necessarily emerge at intermediate steps regardless of the specific attack." This is stated as the causal explanation for why RA generalizes to PAIR, ReNeLLM, and Crescendo, but no empirical evidence supports it. Tracing intermediate denoising states during a successful PAIR or Crescendo attack to confirm that affirmative tokens indeed appear early would either validate the explanation or reveal a different mechanism. The Table 3 improvements are real, but the stated causal explanation is unverified.

### Minor

- **Monotonicity assumption in Theorem 4.1 is empirically validated (Appendix C.2) but not derived in the main text**: The main-text argument (Section 4.2) is intuitive heuristic reasoning about probability concentration, not a derivation. The paper correctly labels it an assumption and references empirical validation. The framing ("effective surrogate, valid in expectation") would be more accurate than the implicit strength of "lower bound," since monotonicity failures on a minority of harmful prompts are not ruled out. This does not threaten the empirical results, but marginally overstates the theoretical guarantee.

- **Residual vulnerability at late intervention steps (t=32)**: RA still achieves 50.7% ASR under anchoring attack at $t=32$ for LLaDA Instruct (Table 2). The paper notes this is because "generating a contextually safe response is practically impossible due to many anchors," but provides no principled criterion for setting $t_{\max}$. Given that this is a critical hyperparameter, guidance beyond empirical grid-search would strengthen the method.

### Trivial

- The paper describes TruthfulQA improvement under RA as due to "reward-model-based alignment enhancing truthfulness" — a speculative attribution stated with more confidence than warranted. The observation itself is interesting but not analyzed further.

---

## Nice-to-Haves

- **Mechanistic verification of generalization**: Take a successful PAIR or Crescendo attack on an undefended model and trace the intermediate denoising states — do affirmative tokens appear early in the trajectory? This experiment would decisively confirm (or refute) the proposed causal mechanism linking RA's priming-vulnerability training to its conventional-jailbreak robustness, and is highly recommended.

- **MC GCG with enhanced variance-reduction budget**: The 20× speedup of First-Step GCG versus MC GCG arises partly because avoiding stochastic sampling eliminates variance. Showing that First-Step GCG succeeds on specific harmful prompts where MC GCG fails even with extra sampling budget would more cleanly credit the conceptual insight rather than just computational efficiency.

- **BeaverTails/evaluation overlap acknowledgment**: RA is trained on BeaverTails, and evaluation is on JBB-Behaviors and AdvBench. At least briefly acknowledging the potential for distributional overlap — and the risk that RA might not generalize to out-of-distribution harmful behaviors — would strengthen the limitations discussion.

- **Principled t_max selection criterion**: An analysis of whether t_max can be set based on model capacity or dataset characteristics (rather than grid search) would make RA more directly applicable across new MDLMs without per-model tuning.

---

## Removed Points

*These points are flagged as removed — treat them with caution.*

1. **Harsh critic's concern that the anchoring attack's "single token" is drawn from a known harmful response, not chosen optimally**: The paper is explicit about this (Section 4.1: "the attacker replaces the predicted response $\tilde{r}_{t_{\text{inter}}}$ with the harmful response $r$"). The conceptual point holds regardless of whether the anchor token is optimal — one token drawn from an actual harmful response is still a compelling single-token injection. Removed as nitpick.

2. **Concern that the primary evaluation relies on an unrealistic threat model**: The paper explicitly labels the anchoring attack as "hypothetical" and then separately demonstrates a realistic (no-intervention) threat via First-Step GCG. Table 3 further validates against black-box conversational attacks. The defense is evaluated under both settings. The critic's concern is partially valid (training is done from anchoring-style contamination), but the paper does address realistic attacks — this is retained only as the major weakness about the unverified transfer mechanism.

3. **Claim about Figure 2 showing 21% ASR for LLaDA Instruct at t=1**: The paper's main text says "ASR increases from 2% to 21%." The image description of Figure 2 shows LLaDA Instruct at 40% at 1/128, while Table 2 shows 17.3±4.6% for Anchoring at t=1. These apparent discrepancies are likely PDF-parsing artifacts across different experimental setups. Not penalized as author error.

4. **Missing related works suggestions**: Removed per review protocol — cannot verify existence of external works.

5. **Formatting/parsing artifacts** in the extracted text: Removed per hard rule.

6. **Strength finder's generic claim that this paper "underscores the need for DLM-specific safety research"**: Removed as generic framing, not a specific evidence-backed strength.

---

## Novel Insights

The central insight — that MDLM's parallel iterative denoising creates a structurally distinct safety failure mode relative to ARMs — is genuinely novel and well-articulated. The key observation is that standard alignment trains only from fully masked sequences, leaving the model unconstrained at contaminated intermediate states where inequality (6) becomes active. This means the priming vulnerability is not a model capacity problem but a *training distribution* problem: the contaminated intermediate states that enable harmful steering are simply never encountered during standard alignment. Recovery Alignment addresses this by making the contaminated state distribution part of the training data, which is a clean and principled fix. The further observation that this training also helps against conventional jailbreaks (even if the mechanism is incompletely verified) suggests that a richer training distribution may produce alignment generalizations not achievable through standard full-sequence training.

---

## Suggestions

1. Add a mechanistic verification experiment: trace intermediate denoising states during successful conventional jailbreaks (PAIR/Crescendo) to confirm whether affirmative tokens appear at early steps, directly testing the proposed generalization explanation.
2. Acknowledge and discuss the MMaDA+ReNeLLM regression in Table 3 explicitly; qualify the claim of uniform superiority.
3. Provide a sensitivity analysis or rough principled guideline for t_max selection based on model scale or training set characteristics.
4. Clarify the epistemic status of Theorem 4.1 — explicitly note that it is a bound conditional on the monotonicity assumption and that the surrogate works empirically rather than with guaranteed lower-bound tightness.

---

## Score and Decision

### Calibration Anchoring

**Round 1 (bracketing):**

| Path | Avg Score | Band | Notes |
|---|---|---|---|
| BeOEmnmyFu.md | 2.50 | Weak | Simple jailbreak, no defense, limited analysis |
| 5kMwiMnUip.md | 1.40 | Weak | Very basic jailbreak, no real contribution |
| KyKTjRtyNG.md | 3.00 | Weak | Incremental conversational jailbreak, weak novelty |
| 6Mxhg9PtDE.md | 9.50 | Strong (misclassified in query, high score) | Shallow safety alignment — highly relevant, very strong |
| u08UxVNdIo.md | 4.75 | Mid | Diffusion-inspired attack on LLMs — one-sided attack only |
| hXA8wqRdyV.md | 6.14 | Mid | Adaptive jailbreaking of aligned LLMs — attack-only, broad coverage |
| plmBsXHxgR.md | 6.25 | Mid | Cross-modality jailbreak on VLMs — attack-only |
| j7ZWfqCYCY.md | 5.00 | Mid | Information-theoretic attack-defense tradeoff for VLMs |
| Bo62NeU6VF.md | 8.00 | Strong | Backtracking for LLM safety — closest thematic analog |
| 4KqkizXgXU.md | 8.00 | Strong | Curiosity-driven red-teaming — attack coverage |
| tTPHgb0EtV.md | 8.00 | Strong | Harmful fine-tuning defense — alignment robustness |

**Round 1 bracket: 6.0–7.5**. The paper is clearly above weak papers (real contribution, theory, defense). The Backtracking paper (8.00) is the closest thematic analog (recovery-from-partial-harm training), and our paper's contribution is comparable in ambition with somewhat more comprehensive threat analysis but less clean results and some acknowledged residual vulnerability.

**Round 2 (narrowing):**

| Path | Avg Score | Band | Notes |
|---|---|---|---|
| NzxCMe88HX.md | 5.75 | 5.5–7.5 | Diffusion model protection (images) — less relevant domain |
| tiJzOop4u6.md | 6.25 | 5.5–7.5 | Adversarial attacks on image diffusion — different domain |
| hXA8wqRdyV.md | 6.14 | 6–8 | Adaptive jailbreaks — attack-only, our paper has both attack+defense |
| s20W12XTF8.md | 6.25 | 6–8 | Runtime jailbreak antidote — defense for ARMs, comparable evaluation depth |
| HxKSzulSD1.md | 6.50 | 6–8 | Weak-to-strong deception alignment — safety, different mechanism |

Our paper vs. 6.14 (hXA8wqRdyV): Our paper adds a defense, addresses a specific structural vulnerability unique to MDLMs, and provides theory. Clearly stronger than 6.14.

Our paper vs. 6.25 (s20W12XTF8/tiJzOop4u6): Our paper has a more targeted, MDLM-specific contribution with theoretical grounding. Comparable or slightly above.

Our paper vs. 8.00 (Bo62NeU6VF): Backtracking is simpler and achieves near-zero ASR; our paper has a structural weakness (Table 3 regression, residual vulnerability at t=32). Our paper sits below Backtracking.

**Final score: 6.5** — The paper is clearly above the 6.14–6.25 cluster (it has attack + defense, novel vulnerability identification, theory, and multi-benchmark evaluation) and clearly below the 8.00 anchors (where Backtracking achieves cleaner results, simpler mechanism, and no unexplained regression). The Table 3 regression that is not acknowledged, the unverified generalization mechanism, and the residual vulnerability at late intervention steps hold the paper below 7.0.

**Decision: Accept** — The paper makes a genuine, well-scoped contribution to an understudied area (MDLM-specific safety). The core claims (vulnerability identification, attack design, defense effectiveness) are well-supported. The weaknesses are addressable and do not invalidate the contribution.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>