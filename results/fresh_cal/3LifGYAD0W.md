Now I have all the information needed. Here is the consolidated final review.

---

## Summary

This paper proposes QueRE (Question Representation Elicitation), a method that extracts black-box representations from LLMs by feeding elicitation questions about the model's own output and using the resulting yes/no token probabilities as features for a linear predictor. The method is lightweight (requires only output probabilities, not internal states), and the paper demonstrates its effectiveness across three applications: (1) instance-level performance prediction on QA tasks, (2) detecting adversarially-influenced system prompts, and (3) distinguishing between different model sizes/architectures. The key finding is that these low-dimensional black-box representations often match or outperform white-box linear probes (RepE, Full Logits) that require internal model access.

## Strengths

- **Black-box representations competitive with white-box probes**: Across multiple QA benchmarks (NQ, SQuAD, HaluEval, BoolQ, DHate) and multiple model families (LLaMA2 7B–70B, Mistral 7B/Mixtral 8x7B, GPT-3.5-turbo, GPT-4o-mini), QueRE's linear predictors match or exceed RepE (hidden-state probes) and Full Logits (full-vocabulary probes), despite operating with strictly less information. See Figures 2 and 3. This is a genuinely surprising and practically important result for API-only scenarios.

- **Novel applications enabled by the approach**: QueRE is used to (a) detect adversarial system prompts that cause GPT-3.5 to answer incorrectly (Figure 5, Tables 1–2), achieving near-perfect AUROC in several settings, and (b) distinguish model sizes (e.g., LLaMA2-7B vs 13B vs 70B) with high accuracy (Figure 4), both in a purely black-box setting. Prior work on these tasks required white-box access (MacDiarmid et al., 2024; Zou et al., 2023a).

- **Practical sampling approximation validated theoretically and empirically**: Proposition 1 provides a convergence rate for logistic regression trained on sampled probability estimates, and Figure 7 shows less than 2 AUROC points degradation when replacing true probabilities with k samples. This makes the method usable even through APIs that do not expose token probabilities.

- **Low-dimensional representations yield well-calibrated predictors with non-vacuous generalization bounds**: QueRE-based predictors achieve substantially lower expected calibration error (ECE) than answer-probability baselines (Figure 6), and Table 3 reports non-vacuous generalization lower bounds — both rare for black-box probes.

## Weaknesses

### Fatal
None.

### Major

- **Main comparison figures lack error bars or variance measures**. Figures 2 and 3 — the core evidence for the claim that QueRE "matches or outperforms white-box linear predictors" — report AUROC as single points without any measure of variance, confidence intervals, or statistical significance tests. While the ablation in Figure 8 does include standard error shading, the main results do not. This makes it impossible for the reader to assess whether the observed differences between QueRE and baselines are meaningful or within noise. Given that the method involves training linear models on different data splits and sampling from LLMs, variance could be nontrivial.

### Minor

- **Abstract over-reaches with an untested example**. The abstract claims the method can detect "if GPT-3.5 is supplied instead of GPT-4" through an API. The model distinction experiment (Section 4.2, Figure 4) only tests different sizes within the same architecture family (LLaMA2 7B vs 13B vs 70B; Mistral 7B vs Mixtral 8x7B) and only on BoolQ. The specific GPT-3.5 vs GPT-4 scenario is not evaluated. The broader claim about distinguishing architectures and sizes is supported, but the concrete example in the abstract oversells the evidence.

- **Proposition 1's convergence analysis is sketchy and incomplete**. The rate \(O(1/\sqrt{n} + \sqrt{n}/k)\) is stated without a formal proof, without precise assumptions (e.g., boundedness of features, well-specification of logistic regression), and without a citation to a specific theorem in the cited reference (Stefanski & Carroll, 1985). The statement that "if \(k\) grows with \(n\), we observe that the naive MLE... results in a consistent... estimator" is imprecise — the rate actually requires \(k = \omega(\sqrt{n})\) for the second term to vanish. This section would benefit from being either made rigorous (with a proof sketch and explicit assumptions) or moved to an appendix with only a qualitative summary retained in the main text.

- **The "first 5000 / first 1000" split may introduce ordering bias**. The paper takes the first 5000 instances from each dataset's training split and the first 1000 from the test split without random shuffling. If the datasets have any ordering structure (e.g., grouped by difficulty or source), this could bias the results. A random split would be standard practice.

- **Unfair comparison asymmetry not fully discussed**. The paper compares QueRE (which uses multiple forward passes — one per elicitation question plus the initial query) against RepE and Full Logits (which use a single forward pass). While the comparison is about information *type* (black-box vs white-box), the computational budget is not controlled. A brief discussion of this trade-off would strengthen the paper. (Note: this does not invalidate the comparison — QueRE's black-box nature is the central contribution — but the asymmetry deserves acknowledgment.)

- **Only one dataset shown for model distinction (Figure 4)**. The model architecture/size classification experiment is only reported on BoolQ. Showing results on at least one more dataset would strengthen this application.

### Trivial

- "Full Logits" for black-box GPT models is approximated by top-5 probabilities. The paper mentions this but the caption and text could be clearer about the degree of approximation. This is a practical limitation, not a flaw in the paper's reporting.

## Nice-to-Haves

- Providing the exact set of elicitation questions used (in an appendix or supplementary material) would aid reproducibility. The paper mentions GPT-4 generated 40 questions plus a small hand-crafted set but does not list them.
- A baseline using multiple black-box queries *without* elicitation questions (beyond the "random sequences" ablation) could more directly test whether the value comes from elicitation or from diverse prompts.
- Statistical significance tests (e.g., paired bootstrap) on the core comparisons would address the error-bar concern without requiring multiple runs.

## Removed Points

These points were flagged for removal. Treat them with caution:

- **"QueRE acronym not defined"** — Removed because the paper explicitly defines it on line 75: "We refer to our approach as QueRE (Question Representation Elicitation)." Factually incorrect.
- **"Random sequences ablation undermines the motivation"** — Removed because the paper handles this openly as an "interesting result" and discusses it in the discussion section. The method still works; the finding is a scientific insight, not a flaw.
- **"Missing appendix content / proofs / questions list"** — Removed per instructions; the parser strips appendix content from all papers; it exists in the original submission.
- **"Generalization bound assumption not verified"** — Removed as a standalone fatal point because the paper *explicitly acknowledges* this limitation: "A limitation of these results is that they require an assumption that the representations extracted by a LLM are independent of the downstream task data; this assumption is verifiable via works in data contamination." The paper is transparent about the assumption. (It remains a valid area for future work, but not a weakness of the current paper.)
- **"Pure formatting/style nitpicks"** — Removed per instructions (typos, capitalization, whitespace, garbled characters, etc. are parser artifacts).

## Novel Insights

The most interesting meta-insight from the reviews is that the method's effectiveness does not seem to depend on the *semantic content* of the elicitation questions. The finding that random sequences of natural language can match or exceed purpose-built questions (Table 4) suggests the value comes from extracting diverse probability vectors from the model's output distribution — a form of output-space probing — rather than from the model's ability to introspect about correctness. This is acknowledged in the paper but could be foregrounded more; it connects QueRE to a broader principle that *diversity of conditioning context* (not just "self-querying") is what makes the representations informative. The convergence analysis for sampling-based approximation (Proposition 1) is also a nice theoretical complement for practitioners who lack API probability access.

## Suggestions

1. **Add error bars or confidence intervals to Figures 2 and 3**, or report the variance across multiple train/test splits. This is the single most impactful change for strengthening the paper's evidence.
2. **Either run the GPT-3.5 vs GPT-4 distinction experiment or tone down the abstract** to match what is actually tested (distinguishing model sizes and architectures).
3. **Provide a proof sketch or proper citation for Proposition 1** with explicit assumptions, or move the theoretical analysis to an appendix.
4. **Use random splits** (rather than the first N examples) for dataset construction to avoid ordering bias.
5. **List the elicitation questions** in an appendix for reproducibility.

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>