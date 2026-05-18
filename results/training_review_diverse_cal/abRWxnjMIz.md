Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper studies the problem of "scoping" LLMs — restricting a general-purpose model to only respond to queries in specific task domains (e.g., sentiment analysis) while refusing out-of-scope queries. It adapts several existing methods (System Prompting, SFT, DPO, Probes, and Circuit Breakers) to this task and introduces a simple SFT→CB layering. The paper runs an extensive empirical evaluation across three broad accept tasks (classification, generation, reasoning), seven black-box adversarial attacks, and studies rejection-set diversity, multi-task acceptance, and data efficiency. The central finding is that Circuit Breaker-based methods, especially when layered with SFT, are more robust than standard fine-tuning or preference learning approaches for scoping, particularly when rejection data is scarce.

## Strengths

- **Comprehensive empirical comparison across multiple tasks and adversarial settings.** The paper systematically evaluates five methods (Sys., SFT, DPO, Probe, CB, SFT→CB) on three distinct accept tasks (Sentiment Analysis, Summarization, Program Execution) under seven black-box adversarial attacks. This provides the broadest head-to-head benchmark for LLM scoping methods to date. The results (Figures 2–4) show large and consistent differences between methods — e.g., CB and SFT→CB substantially outperform Sys. and SFT on OOD rejection across nearly all settings.

- **CB generalizes from very narrow rejection data.** Section 4.2 (Figure 3) demonstrates that CB and SFT→CB maintain strong OOD rejection (>80%) even when the rejection set contains only a single category. By contrast, DPO and Probe require 2–3 categories to match this performance. This is a practically important finding for low-resource deployment scenarios and is backed by clear experimental evidence.

- **SFT→CB layering improves accept-task performance without sacrificing rejection.** Section 3.3 introduces this simple combination, and experiments (Figures 2–4) consistently show it yields higher accept scores than CB alone while maintaining comparable or better rejection rates. For example, in Summarization under adversarial attacks, SFT→CB achieves accept scores ≈0.4 with near-zero accept-set rejection, whereas CB alone scores ≈0.3.

- **Honest documentation of CB limitations.** The paper documents that CB performance degrades when the rejection set becomes too diverse (Section 4.2), unlike DPO which improves with diversity. This counterpoint strengthens credibility.

- **Principled formalization of the scoping task.** The problem is formally stated as a constrained optimization (minimize accept-set rejection, maximize OOD rejection, subject to accept-task performance), providing a clear framework for future work.

## Weaknesses

### Fatal

None.

### Major

- **Method-specific rejection detection limits comparability of headline claims (Section 3.4).** The paper uses different detectors to decide whether a completion counts as "rejected": string matching for SFT, DPO, and System Prompt; repetition detection for CB; and the trained binary classifier for the Probe. Each detector is calibrated on only 90 completions (30 per accept/reject/OOD set). While the paper reports near-perfect agreement with manual judgments on this calibration set, the small sample cannot bound differential accuracy across methods in deployment. String matching could systematically miss rejection phrasings that differ from the synonym list, while the repetition detector for CB may flag degenerate outputs that are not refusals. Since every experiment's central metric (rejection rate) depends on these detectors, the comparative rankings are less precise than the paper implies. The concern is somewhat mitigated by the large differences observed (e.g., CB at ~80% OOD rejection vs. Sys. at ~20%), but it remains a significant methodological gap that a rebuttal should address — e.g., by reporting a human-annotated held-out set across all methods.

- **Single-model evaluation for the full experimental suite (Section 4).** All main experiments (adversarial evaluation, diversity study, multi-task acceptance) are conducted only on Mistral-7B-Instruct-v0.2. The teaser figure includes Granite results for one setting (Sentiment Analysis adversarial evaluation), and the text defers "results for Granite to Figure~\ref{fig:granite}" (line 160), but no Granite results appear in the extracted text's main experimental body. The paper acknowledges this limitation (line 101, line 140) and notes that the methods have been validated on multiple models in prior work. However, the interaction of each method with the *scoping* task specifically could be model-dependent (e.g., sensitivity of CB to representation geometry in different architectures, effectiveness of DPO with different base models). The central claim that CB "broadly performs more robustly" would be substantially strengthened by showing consistent results on at least one additional model (e.g., Llama-3-8B-Instruct) for the adversarial evaluation and diversity study.

### Minor

- **Small sample size for TAP attacks (Section 4.1).** The Tree of Attacks with Pruning (TAP) is evaluated on only 10 prompts per dataset. For a stochastic iterative attack that is the most expensive to run, 10 prompts per dataset yields a highly unstable estimate of jailbreak rate. The paper acknowledges the cost constraint, but the TAP-based comparisons (e.g., "Probe is best under TAP for Sentiment Analysis") carry very little weight. This is not fatal since TAP is one of seven attacks and the overall pattern is consistent across other attacks, but it should be noted.

- **No error bars or confidence intervals on any reported metric.** All figures (Figures 2–4) show point estimates without uncertainty. Given stochasticity in LLM generation and the binary nature of rejection decisions, reporting standard deviations over 3+ random seeds or evaluation splits would meaningfully strengthen the evidence. This is standard practice in comparable empirical benchmarks.

- **Rouge-L as the sole automatic metric for generation tasks (Section 3.2).** For text completion, story composition, and dialogue generation, Rouge-L measures n-gram overlap rather than semantic correctness, coherence, or instruction-following. The paper uses it as a "proxy" (line 95), which is acceptable for a broad automated benchmark, but the accept-score comparisons for generation tasks should be interpreted with this limitation in mind.

- **Two-stage baselines mentioned but not implemented.** The introduction motivates against "two-stage approaches like relevance classifiers" (line 15) but does not include one as a baseline. An external classifier + separate finetuned model is a natural alternative that would establish an upper bound on rejection performance. This gap is worth noting but not critical given the breadth of existing baselines.

### Trivial

- **Granite results referenced but not verifiable in the extracted main text.** The paper states "defer results for Granite to Figure~\ref{fig:granite}" but no such figure is present in the extracted text (it may be in the appendix). The teaser (Figure 1) shows Granite for one setting but is not discussed in the main experiments.

## Nice-to-Haves

- A unified rejection detector (e.g., a single classifier trained on labeled completions from all methods) would place the comparative claims on more solid footing than the current method-specific approach.
- A summary metric combining accept-task performance and rejection rates (e.g., an AUROC-style measure across thresholds) would reduce reliance on simultaneous inspection of multiple subplots.
- A "no attack" baseline within the adversarial robustness figures would make the impact of each attack immediately visible without cross-referencing other figures.
- Reporting training cost (compute time, memory) would be helpful for practitioners choosing between methods.

## Removed Points

- **"Unsupported claims in Additional Analysis (Section 4.4)"** — Removed because the appendix (which likely contains the supporting figures/tables for these analyses) was stripped by the parser. The weakness assumes these claims are unsupported in the original submission, which is not verifiable from the extracted text.
- **"Selection of default accept sets seems arbitrary"** — Removed because the three chosen tasks (Sentiment Analysis: classification, Summarization: generation, Program Execution: reasoning) provide a principled diversity of task types; this is a defensible design choice, not a weakness.
- **"Missing error bars" framing as a major weakness** — Downgraded to Minor since single-run evaluation is common practice for large-scale LLM benchmarks of this type, though error bars would strengthen the paper.

## Novel Insights

The most interesting synthesis from the reviews is the tension between the paper's two main findings: CB generalizes remarkably well from narrow rejection distributions (a strength) but breaks down under high rejection diversity (a documented limitation). This creates a clear research agenda: methods that combine CB's low-data generalization with DPO's scalability to diverse rejection sets would be the natural next step. The reviewers' critiques of the rejection-detection asymmetry also highlight a broader methodological challenge for the field — when different methods produce qualitatively different output behaviors (fluent refusal vs. degenerate repetition), it becomes difficult to measure "rejection" on a common scale, and this problem is not unique to this paper.

## Suggestions

1. **Address the rejection-detection asymmetry** by either (a) training a single classifier on diverse human-annotated completions from all methods, or (b) reporting human agreement on a held-out set large enough (e.g., 200+ per method) to bound differential accuracy. This is the single most impactful improvement.
2. **Add at least one additional base model** (e.g., Llama-3-8B-Instruct) to the adversarial evaluation and diversity study to test whether the Mistral-specific findings transfer. Even a subset of experiments would substantially strengthen the generality claims.
3. **Run TAP with more prompts** (e.g., 30–50) or augment it with bootstrap confidence intervals so the TAP-based comparisons are interpretable.
4. **Add error bars** (standard deviation over 3 seeds or evaluation splits) to the main figures, or at minimum report them in a table.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>