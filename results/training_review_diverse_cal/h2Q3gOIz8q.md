Now I have all the information needed. Let me synthesize the review.

## Summary

This paper presents INSEC, the first black-box adversarial attack on LLM-based code completion engines. INSEC injects a short, optimized comment string (5–10 tokens) into the completion input, crafted via a genetic algorithm with diverse initialization strategies. Tested across 16 CWE types, 5 programming languages, and multiple engines (StarCoder, CodeLlama, GPT-3.5-Turbo-Instruct, GitHub Copilot), INSEC increases the vulnerability rate by ~50% absolute while causing at most a 22% relative drop in functional correctness. The attack costs under $10 per CWE and requires only black-box query access, making it practically realizable.

## Strengths

- **First black-box attack on code completion under a realistic threat model.** Prior attacks (Schuster et al., He & Vechev, Aghakhani et al.) require white-box access to weights, training data, or logits. INSEC operates with only black-box query access and successfully targets deployed commercial services (GPT-3.5-Turbo-Instruct, Copilot), which is a clear advance in scope and realism.

- **High attack success with thorough ablation.** Figure 2 shows ~50% absolute vulnerability-rate increase across all tested engines while functional correctness degrades at most 22% relatively, with stronger models (GPT-3.5, larger StarCoder2 variants) retaining more functionality under attack. The design is well-validated: ablation studies confirm the comment-format and line-above insertion position (Figure 3), the necessity of optimization + initialization (Figure 5), the effectiveness of 5–10 token attack lengths (Figure 6), and generalization via proxy tokenizers (Figure 7).

- **Comprehensive evaluation scope.** 16 CWE types across 5 programming languages — substantially broader than prior poisoning-attack evaluations (3–4 CWEs). The dataset construction and automated vulnerability assessment via CodeQL follow established methodology from Pearce et al. and He & Vechev.

- **Practical cost and replicability details.** Concrete optimization costs ($5.80 per CWE on GPT-3.5-Turbo-Instruct), hyperparameter analysis (pool size, temperature, attack length), and proxy tokenizer experiments are provided, enabling independent verification and extension.

## Weaknesses

### Fatal
None.

### Major

- **Vulnerability and functional correctness are evaluated on disjoint datasets without joint verification on the same completions.** The paper measures vulnerability rate on $\mathbf{D}_{\mathrm{vul}}$ (security-critical tasks) and functional correctness on $\mathbf{D}_{\mathrm{func}}$ (HumanEval-based line-removal tasks), then presents them as side-by-side plots (Figure 2). The central threat claim — that INSEC produces *stealthy* vulnerable code likely to be adopted — implicitly requires that the vulnerable completions themselves be functionally correct. The paper partially addresses this by designing $\mathbf{D}_{\mathrm{vul}}$ tasks such that "functionality can be achieved by either secure or unsafe completions" (Section 2), meaning both the secure and vulnerable versions implement the same intended functionality (e.g., a hash function via SHA256 vs. MD5). However, this is an *assumption built into the dataset design*, not an empirical verification. The paper never actually measures whether the specific completions flagged as vulnerable by CodeQL also pass unit tests. While the separate functional-correctness measurement on $\mathbf{D}_{\mathrm{func}}$ shows the attack string doesn't broadly break functionality, it does not directly confirm that the vulnerable outputs on security-critical tasks are functional. This gap weakens, but does not invalidate, the paper's threat characterization — the dataset design mitigates the concern, but empirical evidence would be far stronger.

### Minor

- **No error bars, confidence intervals, or significance tests on main quantitative results.** Figure 2 reports average vulnerability-rate increases of ~50% across 16 CWEs without any indication of variability. Given that each CWE uses 12 tasks × 100 samples, sampling variability and per-CWE heterogeneity are not negligible. The qualitative conclusion (~50% increase) is unlikely to change with proper uncertainty quantification, but the lack of rigor is a presentation weakness for a paper making strong quantitative claims.

- **Vulnerability assessment relies solely on CodeQL without manual or dynamic validation.** The genetic algorithm optimizes against CodeQL judgments, raising the possibility that INSEC produces completions that "fool" the static analyzer rather than introducing genuinely exploitable vulnerabilities. CodeQL is a standard and respected tool in security research, and this concern applies equally to prior work, but the paper would benefit from at least a small-scale manual review or dynamic testing of a sample of completions flagged as vulnerable.

- **The multi-CWE experiment (Figure 8) concatenates individually optimized strings without joint optimization, yet the paper calls the result "strongly composable."** The experiment is a useful sanity check showing that concatenation doesn't catastrophically fail, but "strongly composable" overstates what a simple concatenation demonstrates. Joint optimization across multiple CWEs could yield different (potentially stronger or weaker) results.

- **No comparison against a truly naive baseline** (e.g., a fixed non-optimized string of similar length, or randomly sampled tokens without the genetic algorithm). The paper compares optimization+initialization against initialization-only and optimization-only ablations, which is informative, but a trivial baseline would isolate the value added by the genetic optimization over and above any comment-based perturbation.

- **Withheld attack strings limit reproducibility.** The paper states it will not publish the optimized strings publicly but will provide them upon request. Combined with the randomness in the genetic algorithm, exact reproduction is difficult. Releasing the strings (or a representative sample) to reviewers and in a controlled-access repository would strengthen reproducibility without compromising the ethical rationale, which is thin given the strings target standard CWE patterns.

### Trivial
None.

## Nice-to-Haves

- **Per-CWE heterogeneity analysis.** A table or heatmap showing which CWEs are most/least affected would help readers assess which coding scenarios are at greatest risk and whether the average is driven by a few outlier CWEs.
- **Qualitative analysis of attack strings** beyond the brief note about low-resource tokens. Providing tokenization overlap analysis or concrete examples (even anonymized) would deepen understanding of *why* the attack works.
- **Detection countermeasure evaluation.** The paper mentions mitigations (frequency-based detection, prompt sanitization) but does not evaluate whether the optimized strings are detectable via simple statistical checks. Even a brief experiment would strengthen the urgency claim.

## Removed Points

- **Threat model plausibility ("why route through the LLM?"):** The paper explicitly addresses this in Sections 1 and 3 — the attacker uses the LLM because it generates natural-looking, functionally correct code that a developer is likely to adopt, and training/hosting a custom model is unrealistic. The reviewer acknowledges this is a reasonable answer. This criticism is already addressed by the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an independent insight about the method or results that the authors themselves did not already identify.

## Suggestions

1. **Empirically verify joint vulnerability+functionality on the same tasks.** Run unit tests (which $\mathbf{D}_{\mathrm{vul}}$ tasks should support by design, since both secure and vulnerable completions are intended to achieve the same functionality) on the specific completions that CodeQL flags as vulnerable, and report what fraction pass. This directly supports the threat model and addresses the most significant gap.

2. **Add error bars or bootstrapped confidence intervals** to Figure 2 and per-CWE breakdowns to show variability.

3. **Release the optimized attack strings** via a controlled-access repository (e.g., with automated access for researchers), to improve reproducibility without enabling misuse.

4. **Add a minimal baseline comparison** using a fixed, non-optimized string of the same length (e.g., `# insecure` or random tokens without genetic search) to isolate the optimization's marginal benefit.

## Score and Decision

**Originality:** High — first black-box attack on code completion engines, with a realistic threat model.  
**Importance:** High — code completion is widely used and this demonstrates a practical, low-cost attack surface.  
**Claims support:** Mostly good, with one significant gap (joint evaluation) that partially undermines the threat characterization but not the core empirical findings.  
**Soundness:** Solid overall methodology; missing statistical rigor and reliance on a single static analyzer are standard gaps for this type of work.  
**Clarity:** Well-written and well-structured.  
**Value to community:** High — raises awareness of a realistic attack vector and provides a reproducible evaluation framework.

The paper makes a clear, original contribution: the first black-box adversarial attack on deployed code completion engines, with strong empirical evidence that the attack works across multiple models and vulnerability types. The missing joint evaluation is the most substantive weakness, but it is partially mitigated by the dataset design (tasks are constructed so that vulnerable and secure completions achieve the same functionality). The paper does not need to be rejected on this basis — the core empirical finding (INSEC increases CodeQL-detected vulnerability rates by ~50% with modest functional-correctness impact) stands. However, the severity of the threat claim about *stealthy, adoptable* vulnerable code would be substantially strengthened by closing this gap.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>