## Summary

This paper investigates output length volatility in long-form LLM generation through three stages: (1) **VOLTBench**, a benchmark covering structured and unstructured tasks, multiple languages, and complexity levels, with stability metrics across 5 repeated runs; (2) **attention trace probing** to identify internal patterns (*Attention Collapse*, *Attention Instability*) linked to generation failure modes; (3) **SELB** (Structural Enforcement via Logits Boosting), a training-free decoding method that forces section transitions at target intervals and suppresses failure-mode tokens, reporting a 148% improvement in mean output length and 69% reduction in length variation.

---

## Strengths

- **Genuine and underexplored problem.** Length volatility across multiple generations is a practical reliability issue receiving little prior systematic attention. The paper makes the case convincingly with concrete evidence: LongWriter-8B's output standard deviation peaked at 103% of its mean length, and no model reliably generates beyond 50 sections as instructed.

- **Well-designed benchmark with automated evaluation.** VOLTBench's multi-dimensional structure (language × complexity × format × length scale up to 100k words) fills an evident gap. The use of execution-based verification for structured tasks (Python functions, LaTeX) and fine-grained keyword/theme constraints for unstructured tasks meaningfully sidesteps the subjectivity that plagues prior benchmarks. The introduction of LSD, LVC, MLA, and FAD as explicit stability metrics is a principled contribution.

- **Mechanistic analysis beyond observation.** Connecting attention traces to output failure modes (Attention Collapse, Attention Instability) is a meaningful step beyond simply cataloging phenomena. The visualization of periodic attention spikes as structural anchors and their degradation as a precursor to task deviation is an insightful empirical finding.

- **Strong empirical gains across multiple base models.** SELB shows consistent benefits on Qwen2.5-7B, Qwen3-8B, and Llama-3.1-8B. Achieving 100% Structured Content Accuracy on code generation tasks—compared to 32.6% for LongWriter-8B—is a concrete indicator that quality is not sacrificed for length.

---

## Weaknesses

### Fatal
None.

### Major

1. **Loose coupling between diagnosis and cure.** The paper's framing implies that SELB was designed to directly counter the identified attention patterns (Attention Collapse and Instability). However, SELB's mechanism—forcibly injecting section-header tokens once a length threshold is crossed and suppressing EOS tokens—does not directly address attention dynamics. The method would yield the same structural enforcement regardless of whether the failure mode is Attention Collapse or any other cause. The probing section is valuable independently, but as a motivating explanation for SELB's design it is overclaimed.

2. **Mechanical enforcement inflates length metrics.** SELB's 148% improvement in mean output length and 69% LVC reduction are largely driven by hard constraints that *prevent* the model from stopping prematurely rather than improving the model's intrinsic generation capability. The key question—whether generated content beyond the natural stopping point is coherent and non-repetitive—is partially addressed via the TTR analysis in Appendix G and UCA scores, but this analysis is not prominent in the main paper and the UCA scores (86.7%) are not notably better than strong closed-source baselines on shorter outputs (Deepseek-R1 achieves 93.3%). The benefit for very long targets (50k–100k words) is not critically interrogated for content quality.

3. **Statistical fragility of volatility estimates.** All stability metrics (LSD, LVC, FAD) are computed from only N=5 samples per prompt. With 5 samples, variance estimates are unreliable; a single outlier significantly skews LSD. The paper provides no confidence intervals or statistical significance analysis for the improvements reported in the main results table.

### Minor

1. **Attention averaging may obscure informative structure.** The layer-level attention $\bar{\alpha}^{(t)}$ is computed by averaging uniformly across all heads and then all layers. Attention patterns are known to be highly non-uniform across layers (early vs. late layers serve different functions). The choice to average without ablation or justification may smooth away the most informative signal; certain layers or head types may be far more predictive of collapse events.

2. **SELB-Hybrid results for free-form generation appear extreme but are in the appendix.** The claim of 97% MLA on a 20,000-word free-form novel, versus baselines generating fewer than 600 words, is a strong result whose evaluation details (judge methodology, quality assessment) are deferred to the appendix and not scrutinized in the main paper.

3. **Comparison set imbalance.** SELB is applied to open-source models (Qwen2.5-7B, Llama-3.1-8B, Qwen3-8B), but the primary qualitative comparison is against LongWriter-8B, a model specifically fine-tuned for long generation at the cost of quality. A comparison against applying SELB's hard constraints to LongWriter-8B itself would clarify how much of the gain is from SELB vs. simply switching base model.

### Trivial

- Figure descriptions are repeated verbatim two to three times each (parser artifact), which inflates apparent complexity without adding information.

---

## Nice-to-Haves

- An ablation separating the contribution of structural enforcement (M_struct) vs. failure prevention (M_fail) would clarify the importance of each component.
- Extending the N=5 sampling to N≥20 for at least a subset of prompts would make the stability estimates statistically credible.
- Including an analysis of whether SELB's forced sections introduce repetition artifacts *specifically at the injection points* would be valuable for practitioners.

---

## Novel Insights

The characterization of *Attention Collapse* and *Attention Instability* as distinct, measurable precursors to generation failure in long-form tasks is a genuinely new mechanistic framing. Prior work on long-form generation largely treats failure as an output phenomenon; the observation that periodic attention spikes to constraint tokens serve as structural anchor signals—and that their disruption or disappearance directly precedes specific failure modes—provides a diagnostic lens applicable to future work on generation controllability beyond just logit manipulation.

---

## Suggestions

- Provide confidence intervals for LSD/LVC/MLA, or increase N per prompt to ≥15 to make stability estimates statistically meaningful.
- Decouple the paper's narrative: present attention probing as an independent empirical finding and SELB as a pragmatic engineering solution, rather than framing SELB as mechanistically derived from the attention analysis.
- Include a rigorous quality evaluation (LLM-as-a-Judge with human spot-checks) on sections specifically generated past a model's natural stopping point to address the coherence question for long-range SELB output.
- Add an ablation study on SELB's two components (structural enforcement vs. proactive failure prevention) to clarify their relative contributions.

---

## Score and Decision

VOLTBench is a well-motivated, multi-dimensional benchmark that fills a real gap, and SELB demonstrates substantial and reproducible empirical gains across multiple models. The probing analysis offers a useful mechanistic perspective. The principal concerns—the loose theoretical link between attention analysis and SELB's design, the mechanical inflation of length metrics, and the limited statistical rigor of N=5—are significant but do not invalidate the core empirical contributions. The paper is above average for the venue: a solid problem framing, useful benchmark, and working solution with interpretable results.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>