Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper investigates the vulnerability of safety-aligned LLMs and MLLMs to out-of-distribution (OOD) inputs. The authors propose JOOD, a black-box jailbreak attack that uses simple, off-the-shelf text-mixing and image-mixup transformations to generate OOD-ified harmful inputs. The key empirical finding is that JOOD achieves a 63% attack success rate against GPT-4V in the Bombs or Explosives scenario, far exceeding the 23% of the best baseline (FigStep-Pro), while ablations confirm that the transformation (especially the mixing coefficient α) directly reduces refusal rates and increases harmfulness.

## Strengths

- **Novel insight and approach**: The paper identifies that safety alignment which is robust to in-distribution harmful inputs can be bypassed by OOD-ifying inputs via simple mixing transformations — an attack vector that is conceptually simple but empirically effective against SOTA proprietary models. The core observation is supported by Figure 4, which shows a sharp drop in refusal rate and corresponding rise in ASR as the mixing coefficient moves from 0 (vanilla) to small positive values.

- **Strong empirical results against SOTA proprietary models**: JOOD achieves 63% ASR on GPT-4V in Bombs or Explosives (vs. 23% for the best baseline), +42% ASR improvement in Hacking, and exclusively jailbreaks 10 instructions that all baselines fail on (Table 2). These are striking results against models (GPT-4, GPT-4V) that are generally considered robust to existing jailbreak methods.

- **Simplicity and black-box practicality**: The method requires no access to model gradients, internal representations, or advanced optimization. It only requires the ability to query the API with mixed text or images, using off-the-shelf techniques (text-mixing, image-mixup, CutMix, ResizeMix). This makes the attack immediately practical against closed-source production systems.

- **Thorough ablations supporting the OOD mechanism**: Figures 3–5 and Table 3 provide extensive analysis: (a) various mixing variants consistently outperform vanilla attacks with marginal variance, (b) the α ablation in Figure 4 directly links the degree of mixing to jailbreak success, (c) Figure 5a shows a strong negative correlation between auxiliary image similarity and harmfulness, and (d) JOOD remains effective even under defensive system prompts (only 3% ASR drop vs. 10% for FigStep-Pro).

- **Generalization across models**: JOOD achieves >80% ASR on MiniGPT-4 and LLaVA-1.5 in multiple scenarios, demonstrating that the vulnerability is not specific to GPT-4V.

## Weaknesses

### Fatal
None.

### Major

- **The uncertainty mechanism claim is asserted but not directly validated.** The paper repeatedly states that OOD-ifying "highly increases the uncertainty of the model to discern the malicious intent" (Abstract, Section 1, Section 3.2, Conclusion) and frames this as the central explanation for why JOOD works. However, no direct uncertainty metric is ever measured or reported — no logit entropy, no refusal probability distributions, no representation-space analysis of confidence. The paper reports refusal rate (via substring matching on phrases like "I'm sorry") in Figure 4, which is a reasonable behavioral proxy, but this is not the same as measuring model uncertainty. The correlational evidence (mixing → lower refusal → higher ASR) is consistent with the uncertainty story but equally consistent with alternative explanations (e.g., the mixing operation produces prompts that the safety filter simply does not recognize as harmful for surface-level reasons unrelated to model uncertainty). This weakens the paper's explanatory contribution: the attack *works*, but the paper does not demonstrate *why* it works via the claimed mechanism. The paper's contribution would be stronger if it either (a) directly measured uncertainty (e.g., entropy of the next-token distribution over safe vs. continuation paths, contrast between refusal-token and compliance-token probabilities for OOD vs. vanilla inputs), or (b) tempered the mechanistic claims and framed the contribution as an empirical finding about mixing-based jailbreak effectiveness rather than a validated explanation of safety-alignment failure.

- **Baseline adaptation details are not provided.** The paper compares against CipherChat, PAIR, FigStep, and HADES on GPT-4 and GPT-4V (Table 1), but never describes how these baselines were adapted to the black-box API setting. Several of these methods were designed for different settings (PAIR uses iterative optimization, HADES uses diffusion-based image synthesis, CipherChat uses encryption). The paper does not state: (i) whether each baseline was used with its original prompts adapted to the multimodal setting, (ii) the number of attempts allowed per instruction for each baseline, (iii) whether hyperparameters were tuned for the target models, or (iv) whether some baselines required access to model logits or local computation that is impossible in a black-box API setting. Without this information, the large performance gap (e.g., many baselines achieving 0% ASR while JOOD achieves 63%) could partly reflect implementation gaps or asymmetric query budgets rather than inherent superiority. Given that this is an empirical comparison paper, the missing details are a significant reproducibility gap.

### Minor

- **Per-query ASR and query budget not reported.** The paper evaluates ASR as the fraction of instructions where *at least one* of 45 attempts (n=5 auxiliaries × m=9 mixing coefficients) succeeds, explicitly measuring "maximum potential risk." This is a defensible metric for security vulnerability assessment. However, the paper does not report per-query success rate or low-query-budget ASR (e.g., 1, 3, 5 attempts), making it difficult for practitioners to gauge how easily the attack can be executed with limited query budget. Additionally, the paper does not specify whether baselines were given a comparable number of attempts, which compounds the concern about fair comparison (see Major #2).

- **Harmfulness judge not validated or fully specified.** The evaluation uses "another LLM θ^hf (OpenAI, 2023)" as a harmfulness scorer and "binary-judging LLM θ^bj (Inan et al., 2023)" (likely an Llama-Guard variant) for determining ASR. The exact model versions, the prompt templates used, and the agreement with human raters are not reported. Given known biases in LLM-as-judge evaluations (position bias, verbosity bias, self-enhancement bias), this is a nontrivial gap. A small human validation subset would substantially increase confidence in the metrics.

- **Text-based LLM attack is weakly explored.** The LLM attack (Section 3.1) uses a single, specific text-mixing template to create one mixed word (e.g., "baopmpble"). The paper reports ASR for only a few scenarios (e.g., 24% in Firearms on GPT-4) and does not ablate the prompt design, template phrasing, or the number/distribution of constituent words. It is unclear whether this attack generalizes beyond the particular word-mixing strategy shown. The MLLM attack is clearly the stronger and better-analyzed contribution; the LLM portion adds breadth but lacks depth.

### Trivial
- The paper does not include a responsible disclosure statement or discussion of ethical considerations in the main text (only potentially in a missing appendix section).
- Figure descriptions credit "(Niu et al., 2024) dataset" in the Figure 1 caption, which appears to be a stray citation.

## Nice-to-Haves

- A failure analysis of instructions that resisted JOOD (e.g., instructions with specific sensitive terms that survive mixing) would inform future defense research.
- Ablation on the number of auxiliary images (n) — does one auxiliary image suffice, or is the full set of 5 needed?
- Reporting per-query ASR (or ASR@k for small k) alongside the max-over-attempts metric.

## Removed Points

- **"ASR metric overstates per-query effectiveness" (as a critical issue):** The paper is transparent about using max-over-attempts to measure *maximum potential risk* (Section 3.3). This is a standard and defensible practice in security research for assessing worst-case vulnerability. The paper's stated goal is not to measure expected per-query success but to characterize the attack's ceiling. The underlying concern about asymmetric baseline comparison budgets is valid and moved to Major Weakness #2; the per-query concern is downgraded to Minor.

- **Criticism that the text attack is "much weaker and less explored":** This is an observation about scope, not a weakness. The paper's primary contribution is the MLLM attack; the LLM attack is presented as a complementary extension. A paper is not required to be equally strong in all its components. The paper could be stronger by expanding it, but presenting a weaker variant does not constitute a flaw.

- **"Ethical considerations are missing" (as a weakness):** The user instructions note that the parser strips appendix content. The ethical considerations may exist in the full submission's appendix. Additionally, many jailbreak papers at top venues do not include explicit ethical disclaimers in the main text.

## Novel Insights

The reviews surface an important tension: the paper makes strong mechanistic claims about uncertainty as the causal pathway for jailbreaking, but provides only behavioral evidence (refusal rate, ASR) rather than direct uncertainty quantification. This gap between the framing and the evidence is the paper's most significant weakness and may reflect a broader pattern in the jailbreak literature — it is far easier to demonstrate that an attack works than to rigorously establish *why* it works, especially when operating through black-box APIs that do not expose logits or internal states. If the authors could find a way to measure uncertainty without requiring logit access (e.g., measuring variability across multiple responses with the same input, or using refusal-token proxy distributions), it would substantially differentiate this paper from a standard attack demonstration.

## Suggestions

1. Add direct uncertainty quantification for the proposed mechanism: report the probability of refusal tokens, the entropy of next-token predictions (for models where logits are accessible, e.g., open-source MLLMs), or at minimum a distributional analysis of response variability across repeated queries with the same OOD input.
2. Provide complete baseline implementation details: for each baseline, specify the adaptation method, query budget, prompt template, and whether hyperparameters were tuned for each target model.
3. Report per-query or low-budget ASR (ASR@1, ASR@3, ASR@5) alongside the max-over-attempts metric to improve practical interpretability.
4. Validate the harmfulness judge by reporting agreement with human raters on a small subset (e.g., 50–100 responses).
5. Either validate the uncertainty mechanism directly, or reframe the paper's explanatory claims to avoid overclaiming — the empirical finding that mixing bypasses safety alignment is valuable even without a fully validated causal explanation.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>