## Summary
This paper identifies and analyzes the *priming vulnerability* in Masked Diffusion Language Models (MDLMs): when affirmative tokens for a harmful query appear at any intermediate denoising step, subsequent generation is strongly biased toward harmful outputs—even in safety-aligned models. The authors introduce an "anchoring attack" to quantify this vulnerability, derive a tractable lower-bound surrogate (First-Step GCG) that enables efficient optimization-based attacks without direct process intervention, and propose *Recovery Alignment* (RA), which trains models using RLHF with intentionally contaminated intermediate states, teaching them to recover to safe responses. Experiments on three MDLMs show RA dramatically reduces attack success rates while preserving general capability across 11 benchmarks.

---

## Strengths

- **Novel, well-motivated vulnerability analysis.** The priming vulnerability is genuinely distinct from ARM-based prefilling attacks: in MDLMs, bidirectional parallel decoding causes affirmative tokens appearing anywhere in the sequence at any step to exert a suppressive, bidirectional effect on subsequent generation. The paper clearly articulates the mechanism via Equation (6): minimizing harm probability from the fully-masked start does not bound it from contaminated intermediate states, which precisely explains why existing alignment methods fail.

- **Principled theoretical contribution.** Theorem 4.1—that the first-step log-likelihood $\frac{1}{T}\log\pi_\theta(\tilde{r}_1 = r | q, r_0)$ is a lower bound on the full denoising log-likelihood under a monotonicity assumption—is non-trivial and practically valuable. It connects the priming vulnerability to a fully differentiable, stochasticity-free objective, yielding ~20× speedup over Monte Carlo GCG and up to 4× higher ASR (Table 1).

- **Comprehensive empirical evaluation.** Three MDLMs (LLaDA Instruct, LLaDA 1.5, MMaDA MixCoT), four priming-exploiting attacks (Anchoring at five intervention levels, PAD, DiJA, First-Step GCG), three conversational jailbreak attacks (PAIR, ReNeLLM, Crescendo), three evaluators (GPT-4o, LLaMA Guard 3, keyword matching), and 11 capability benchmarks. This breadth is markedly above the norm for a safety paper at this venue.

- **Strong defense results with minimal utility cost.** RA reduces ASR under anchoring (t=16) from ~88% to ~8% on LLaDA models, reduces First-Step GCG ASR from 58% to 11% on LLaDA Instruct, and cuts PAIR ASR from 44% to 10%—all with average capability differences of less than 0.5 pp across 11 benchmarks (Table 4). The ablation study demonstrates that the linear curriculum schedule and intermediate-state training are both essential components.

- **Addresses a timely problem.** As MDLMs approach ARM parity in capability and move toward deployment, safety-specific analysis of their inference mechanisms is critical. The paper motivates and frames this niche clearly.

---

## Weaknesses

### Fatal
None.

### Major

1. **Monotonicity assumption (Theorem 4.1) is empirically asserted without main-text evidence.** The inequality $\log\pi_\theta(\tilde{r}_{t+1}=r|q,r_t) \geq \log\pi_\theta(\tilde{r}_1=r|q,r_0)$ is the cornerstone of First-Step GCG's theoretical grounding. The paper states it "holds across a broad range of models" in Appendix C.2 (removed), but offers no intuition beyond the observation that fixed tokens reduce entropy over time. An important edge case: early in training or for highly safety-aligned models, might the mask predictor suppress harmful completions even with more context? A brief main-text argument or plot of the monotonicity ratio over steps would significantly strengthen this claim.

2. **Residual vulnerability at late-step interventions is substantial.** For t_inter=32, RA leaves ASR at 50.7% (LLaDA), 43.0% (LLaDA 1.5), and 79.3% (MMaDA). While the paper correctly notes this is partially inevitable ("contextually safe response is impossible with many anchors"), there is no analysis of where the transition from recoverable to unrecoverable states lies, nor any proposal to detect or block such deep interventions. This gap is significant if an adversary gains even partial access to the sampling process.

3. **ReNeLLM remains largely unaddressed.** After RA, ReNeLLM ASR is still 72.3% / 71.7% for LLaDA models—comparable to the original baseline for some models and significantly above other defenses on absolute scale. The paper attributes this to harmfulness "not detectable from the surface form," but provides no analysis of what makes ReNeLLM qualitatively different. This represents a genuine outstanding vulnerability.

### Minor

1. **The practical threat model for intervention-based attacks is underspecified.** The anchoring attack and PAD/DiJA require access to internal denoising states at inference time. In typical API deployments this is implausible; the paper could clarify under what deployment settings (e.g., open-weight models, local inference, model distillation pipelines) the intervention threat model is realistic.

2. **MMaDA results are substantially weaker than LLaDA models.** Post-RA, MMaDA still shows 24.3% ASR under PAD and 70% under DiJA. The paper does not analyze whether this is because MMaDA was initially unaligned (baseline ASR ~79%), making alignment harder, or due to an architectural difference. Understanding this degradation would be informative for practitioners.

3. **GRPO reward hacking at large t_max mentioned but not analyzed.** The paper states "reward hacking, where the model generates responses that are meaningless" occurs for very large t_max values. How this is detected and handled is not discussed in the main text; it is a known failure mode of RLHF methods and deserves at least a brief treatment.

### Trivial

- The 1/T factor makes the lower bound in Theorem 4.1 numerically loose (factor of 128 for typical T=128). While the paper acknowledges this and justifies attack performance via Figure 2, a clearer statement of what "looseness" means for the gradient signal would be cleaner.

---

## Nice-to-Haves

- A visualization of the response transition (e.g., probability of safe vs. harmful token over denoising steps) with and without RA would make the recovery mechanism more interpretable.
- An analysis of the minimum number of contaminated tokens needed to trigger the vulnerability at each step level would help practitioners set detection thresholds.
- A DPO-style instantiation of RA is discussed in limitations; even preliminary results or a cost analysis would be useful.

---

## Novel Insights

Beyond its own contributions, this paper reveals an architectural invariant: the bidirectional context window that makes MDLMs efficient (all tokens see all other tokens at each step) is precisely what makes them susceptible to context pollution from any individual token. This is a non-obvious duality—efficiency and vulnerability arise from the same mechanism—and suggests that any MDLM defense must grapple with the full denoising trajectory, not just the initial or final state. The lower-bound derivation (Theorem 4.1) further implies that gradient-based attacks on MDLMs need not track stochastic paths; a single-step oracle is theoretically sufficient and practically superior. This insight may generalize to other masked-diffusion-based systems beyond language.

---

## Suggestions

- Provide at least a main-text figure or table summarizing the empirical verification of the monotonicity assumption across models (currently in removed Appendix C.2), since this underpins the entire First-Step GCG derivation.
- Analyze the "recoverable/unrecoverable" threshold as a function of the number of anchored tokens and their semantic role (e.g., structural tokens vs. content tokens), to give clearer guidance on what intervention levels RA can and cannot be expected to handle.
- Investigate whether RA's recovery capability can be adapted to detect late-step contamination as an anomaly-detection signal, providing a complementary runtime defense for the t_inter≥32 regime where RA's recovery fails.

---

## Score and Decision

The paper makes a clear, timely, and well-executed contribution to the emerging field of MDLM safety. The vulnerability identification is principled, the theoretical treatment is non-trivial, and the experimental evaluation is unusually thorough for a safety paper. The main weaknesses—residual vulnerability at late intervention steps, incomplete addressing of ReNeLLM, and an unverified (in the main text) theoretical assumption—are honest limitations that do not undermine the core claims. The work will be of direct value to researchers and practitioners as MDLMs approach real deployment.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>