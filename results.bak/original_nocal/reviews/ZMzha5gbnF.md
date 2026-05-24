Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper identifies a vulnerability specific to Masked Diffusion Language Models (MDLMs): if tokens from a harmful response appear at intermediate denoising steps (the "priming vulnerability"), they can steer generation toward harmful outputs even in safety-aligned models. The authors design the anchoring attack to quantify this vulnerability and show that it can be exploited even without direct denoising-process intervention through First-Step GCG, an optimization-based attack that exploits a theoretical lower bound. They then propose Recovery Alignment (RA), which trains models to generate safe responses from contaminated intermediate states, and demonstrate that RA substantially reduces attack success rates across three MDLMs while preserving general task capability.

## Strengths

- **Identification and quantification of a novel MDLM-specific vulnerability.** Section 4.1 and Figure 2 systematically demonstrate that injecting tokens from a harmful response at even the first denoising step raises ASR from 2% to 21% (LLaDA Instruct), and ASR exceeds 80% by step 16. This characterization of a failure mode unique to MDLMs (absent in autoregressive models) is a genuine contribution.

- **First-Step GCG provides an efficient and effective non-intervention attack.** Theorem 4.1 derives a tractable surrogate objective. Table 1 shows First-Step GCG is ~20× faster and achieves up to 4× higher ASR than Monte Carlo GCG (e.g., LLaDA 1.5: 12.5% → 49.5%), demonstrating both practical utility and that the vulnerability is exploitable without direct denoising-process access.

- **Recovery Alignment robustly mitigates the vulnerability.** Table 2 shows RA reduces ASR to near 0% for early intervention steps across three models — e.g., LLaDA at t_inter=4: from 44.0% (original) to 1.3% (RA) — substantially outperforming SFT, DPO, and MOSA. The RA w/o inter ablation confirms that training from contaminated intermediate states is essential.

- **General task capability is preserved.** Table 4 shows RA maintains average accuracy within 0.5 percentage points of the original model across 11 diverse benchmarks (e.g., LLaDA original 52.2% vs. RA 52.6%), indicating no substantial utility cost.

- **Improved robustness to conversational jailbreak attacks.** Table 3 shows RA reduces ASR on PAIR from 44.3% to 10.0% (LLaDA) and on Crescendo from 81.3% to 45.0%, demonstrating generalization beyond the priming vulnerability.

- **Systematic ablation of design choices.** Section 6.4 and Figures 3a/3b isolate the impact of the max intervention step and scheduling strategy, grounding hyperparameter choices in empirical evidence.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The "affirmative tokens" claim is imprecise relative to the experiments.** The paper repeatedly states that the vulnerability is driven by "affirmative tokens" (e.g., "Sure," "I'd be happy to") that "endorse or advance a harmful intent" (Section 4). However, the anchoring attack (Section 4.1) injects the **full harmful response** at the intervention step, not isolated affirmative tokens. At t_inter=1, only ~1 token survives re-masking, but the paper does not analyze whether this surviving token is linguistically "affirmative" or whether a neutral token from the same harmful response would produce the same effect. The core finding — that contamination from harmful-response tokens biases generation — is well-supported, but the specificity to "affirmative" tokens is an overclaim that should be either experimentally validated or the framing should be generalized (e.g., "contamination from harmful response tokens").

- **Theorem 4.1's monotonicity assumption is not empirically grounded in the main text.** The assumption that $\log \pi_\theta(\tilde{\mathbf{r}}_{t+1}=\mathbf{r} \mid \mathbf{q}, \mathbf{r}_t) \geq \log \pi_\theta(\tilde{\mathbf{r}}_1=\mathbf{r} \mid \mathbf{q}, \mathbf{r}_0)$ is stated as "compatible with the current denoising process" with a rationale, but the paper defers empirical validation to Appendix C.2. While the practical success of First-Step GCG (Table 1) does not depend on the theorem being perfectly tight, the theorem as presented would benefit from a brief summary of the empirical check in the main text.

### Trivial
None.

## Nice-to-Haves
- An experiment at t_inter=1 that compares tokens from the harmful response that are semantically "affirmative" vs. neutral content tokens would tighten the conceptual framing.
- A brief summary (1-2 sentences) of the Appendix C.2 empirical check on the monotonicity assumption, included in the main text, would strengthen Theorem 4.1.
- Evaluating RA against adaptive attacks (e.g., an attacker aware of RA who crafts contaminated states designed to be harder to recover from) would be a natural extension.
- A concrete side-by-side denoising trajectory showing the original model vs. RA recovering safety from the same contaminated state would improve intuitive understanding.

## Removed Points
These points are flagged to be removed; treat them with caution.

- *"Validate the reward model (e.g., report accuracy on a safety classification benchmark)."* — The paper uses DeBERTaV3 without additional fine-tuning. This is a reasonable practical choice, and the results demonstrate its effectiveness. Asking for a separate safety-classification benchmark evaluation is a rigor request that goes beyond standard practice for reward model usage in alignment papers.
- *"Characterize which tokens are effective beyond affirmative tokens."* — This is a deeper-analysis suggestion that extends beyond the paper's scope; the paper already demonstrates the vulnerability exists and can be mitigated.
- *"Show a concrete example of RA recovering safety."* — A nice illustration, but not a weakness of the current work.
- *"Evaluate RA against adaptive attacks."* — This is a future work direction, not a flaw in the presented work.
- *Strength Finder strengths about the problem being important / addressing an important gap.* — These are generic and not specific to the paper's evidence; however, they are also not wrong, so they are merely set aside rather than contradicted.

## Novel Insights
None beyond the paper's own contributions. The two reviews largely converge on the same assessment: the paper makes a solid empirical contribution with a clear vulnerability analysis and effective mitigation, with the main conceptual imprecision being the "affirmative tokens" framing relative to the experimental evidence.

## Suggestions
1. **Reframe or validate the "affirmative tokens" claim.** Either (a) run a control experiment at t_inter=1 comparing tokens that are semantically affirmative (e.g., "Sure," "I'd be happy to") vs. neutral content tokens from the same harmful response, or (b) reframe the vulnerability more generally as "contamination from harmful response tokens" to align the terminology with the evidence.
2. **Briefly summarize the empirical check of the monotonicity assumption in the main text** (1-2 sentences + a reference to the appendix). This would give readers confidence in Theorem 4.1 without needing to consult the appendix.
3. **Acknowledge the "affirmative tokens" imprecision explicitly** as a limitation, noting that the anchoring attack injects the full harmful response and the surviving tokens may not all be linguistically "affirmative."

## Score and Decision

The paper makes a clear, well-supported contribution: it identifies a genuine MDLM-specific vulnerability, provides both intervention-based and optimization-based attacks to demonstrate it, and proposes an effective mitigation that preserves general capability. The experiments are thorough (three models, two benchmarks, three evaluators, multiple baselines with essential ablations). The two identified weaknesses are minor: a conceptual imprecision in the "affirmative tokens" framing (which does not undermine the core findings) and a deferred empirical check for a theoretical assumption. Neither threatens acceptance.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>