## Summary

This paper proposes StarCraft II Arena, a benchmark for evaluating LLMs in the real-time strategy game StarCraft II. The core idea is to move beyond simple win-rate metrics toward fine-grained capability metrics across three dimensions (strategic planning, real-time decision-making, adaptability) and to introduce a decision-tracking mechanism for behavioral analysis. The paper includes an empirical evaluation of several LLMs (GPT-4o, GPT-4o mini, DeepSeek-V2.5, Llama 3.1 70B, Llama 3.1 8B) that reveals distinct capability trade-offs (e.g., GPT-4o excels at strategic planning but lags in real-time response; Llama 3.1 8B shows the opposite pattern).

## Strengths

- **Fine-grained capability metrics with explicit formulas.** The paper defines quantifiable metrics for resource management (RPM/RMA, Eq. 2) and supply utilization (SUR, Eq. 3) in Section 4.2, going beyond the win-rate-only evaluations identified as the status quo in prior work (Section 2.2). This represents a genuine methodological contribution.

- **Controlled synchronous-vs-asynchronous comparison revealing a meaningful trade-off.** Section 5.2 documents that GPT-4o scores 62.01 in strategic planning (asynchronous) but only 21.12 in real-time decision-making (synchronous), while Llama 3.1 Instruct 8B scores 47.05 in real-time but 37.56 in strategic planning. This differential is exactly the kind of information a win-rate-only evaluation would miss, demonstrating the benchmark's capacity to distinguish distinct capability profiles.

- **Non-obvious finding about model size and real-time performance.** The finding that Llama 3.1 Instruct 8B (47.05) and GPT-4o mini (37.51) outperform GPT-4o (21.12) and DeepSeek-V2.5 in real-time decision-making (Section 5.2) runs counter to the assumption that larger models dominate across all dimensions. This result is empirically enabled by the benchmark's metric design.

- **Decision-tracking framework with structured trace components.** Section 4.3 defines a three-component decision trace (Action Type, Decision Context, Outcome) and illustrates it concretely in Table 3 with a staged trajectory. The qualitative metrics (Unit Construction Order, Key Building Completion Time, Strategy Innovation Rate) are also defined and provide a structured vocabulary for behavioral analysis.

## Weaknesses

### Fatal

None. The paper's conceptual contribution (the metric framework and evaluation dimensions) is not invalidated by its implementation gaps, though the gaps are serious.

### Major

- **The LLM–game interface is entirely unspecified, making the benchmark non-reproducible.** This is the paper's most critical omission. StarCraft II has a complex observation/action space, but the paper never explains how an LLM (text-in/text-out) interfaces with the environment. How is game state serialized into a prompt? What is the prompt template? How are LLM text outputs parsed into API commands? What is the observation frequency? Most critically, the "Async" and "Sync" operational modes (Table 2, lines 81, 160) — which anchor the central finding about real-time vs. strategic trade-offs — are never defined. Does "Sync" mean the game pauses for LLM inference? Does "Async" impose real-time constraints? Without this information, the results are uninterpretable: a low real-time score could reflect poor tactical reasoning, a slow inference pipeline, or a suboptimal prompt design. For a *benchmark* paper, this is a fundamental failing — the benchmark cannot be used or validated by others in its current form.

- **The experimental setup is critically underspecified.** Section 5.1–5.2 contains minimal experimental detail. The paper does not report: (a) number of games played per model per scenario; (b) which specific StarCraft II maps/scenarios were used; (c) the opponent's difficulty level (Very Easy, Medium, Hard, Elite, or a custom bot?); (d) any measure of variance or confidence intervals across runs. The aggregate scoring formula (Eq. 1) uses abstract weights \(W_i\), moderating factors \(\beta_i\), and normalization parameters \(\mu_j, \sigma_j\) whose values are never specified. The reference population for \(\mu_j, \sigma_j\) is unclear — if computed across the evaluated models, the scores are relative and zero-sum, making cross-study comparison invalid. Without these details, the reported aggregate scores (57,758 for GPT-4o, 46,825 for Llama 3.1 70B, etc.) are presented without interpretable scale or grounding.

- **The paper claims to improve on win-rate evaluation but never validates this claim.** The entire motivation is that fine-grained metrics capture information that win rates miss. Table 4 includes a "win rate" column, but the text never references or discusses the win-rate numbers, never shows a case where models have similar win rates but different fine-grained profiles, and never demonstrates that the fine-grained metrics are *not* simply recapitulating the win rate in a more opaque form. This is the paper's central empirical claim, and it goes unsupported.

- **The decision-tracking analysis (Section 5.3) is purely narrative and adds no quantitative analytical value.** The qualitative description of "Game 3" (lines 162–164) documents standard StarCraft II gameplay: building basic units early, transitioning to advanced units later, completing key buildings before producing high-tech units. These observations describe what any minimally competent StarCraft II agent would do. The "Strategy Innovation Rate" is named but never given a formula, measurement protocol, or numerical value. The analysis reads as game commentary, not as an analytical evaluation. The paper promises that decision tracking provides "deeper insight into the decision-making process" (abstract, Section 4.3), but the current analysis does not fulfill this promise — no cross-model comparisons, no quantitative measurements, no systematic pattern extraction.

### Minor

- **Inconsistency between the paper's stated framework and Table 4's listed dimensions.** The paper's entire structure is organized around three dimensions: Strategic Planning, Real-Time Decision-Making, and Adaptability. Yet the caption of Table 4 (line 156–157) lists "win rate, strategic planning, social reasoning, real-time decision making, teamwork, learning ability, and overall score" — three additional dimensions (social reasoning, teamwork, learning ability) that appear nowhere else in the paper and are never defined. This undermines the coherence of the capability framework.

- **Finding (2) in the introduction is not supported by the evaluation.** The introduction lists as a key finding that "most existing LLMs struggle with handling incomplete information and adapting to rapidly evolving opponent strategies" (line 19–20). However, no metric in the paper explicitly measures "handling incomplete information," and the evaluation does not test this claim. The finding appears to be asserted rather than demonstrated.

- **No calibration against known StarCraft II AI baselines.** The paper reports fine-grained scores but provides no reference points. How does a strategic planning score of 62.01 compare to AlphaStar, or to the built-in StarCraft II AI at various difficulty levels? Without calibration, the reader cannot assess whether the scores reflect meaningful strategic competence or random baseline performance.

### Trivial

None.

## Nice-to-Haves

- Including cost and latency analysis would strengthen the real-time decision-making evaluation, since inference latency directly affects in-game responsiveness.
- Specifying the prompt template and discussing sensitivity to prompt variations would improve reproducibility.
- Reporting confidence intervals or error bars across multiple game runs would clarify the reliability of the point estimates.

## Removed Points

These points were raised in the reviews but are excluded from the main assessment:

- **"Missing dedicated Section 5 heading"**: This appears to be a parser artifact from PDF extraction. The content transitions directly from Section 4.3 to Section 5.1, and the heading may have been dropped during parsing. Removed as a formatting artifact.
- **"Win rates are never reported"**: Table 4 includes a "win rate" column (visible in the table image), so win rates are reported even though they are not discussed in the text. The criticism is factually inaccurate on the "never reported" claim, though the broader point that win rates are not used to validate the fine-grained metrics remains valid.
- **"The paper may have been assembled from disparate components"**: This speculation about the cause of the Table 4 inconsistency is removed; the inconsistency itself is retained as a minor weakness.
- **"No discussion of prompt engineering"**: Demoted to Nice-to-Have since prompt details, while useful, are not strictly necessary for the conceptual contribution of the metric framework.
- **Criticisms about the paper's generic or survey-like related work sections**: While the related work is not deeply engaged, demanding more substantive engagement with prior StarCraft II AI work is scope-creep. The paper is about LLM evaluation, not about advancing StarCraft II AI.
- **Several generic strength finder claims** (e.g., "this paper addressed an important problem") are removed as superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews surface known issues with underspecified benchmarks but do not generate novel synthesis beyond what the paper's own content reveals. The central empirical observation — that the synchronous-vs-asynchronous comparison reveals a capability trade-off across model families — is already in the paper.

## Suggestions

1. **Specify the full LLM-game interface**: provide the prompt template, observation serialization format, action parsing logic, operational definition of Async/Sync modes, and observation frequency. Without this, the paper cannot function as a benchmark.
2. **Complete the experimental specification**: report number of games, opponent difficulty, specific maps/scenarios, and variance across runs. Provide concrete values for \(W_i\), \(\beta_i\), and the normalization reference distribution in Eq. 1.
3. **Validate the fine-grained metrics against win rates**: show at least one case where two models have similar win rates but different fine-grained profiles, or vice versa, to demonstrate that the metrics capture distinct information.
4. **Ground the decision-tracking analysis quantitatively**: report cross-model comparisons of unit construction order statistics, building completion times, and strategy innovation rates with numerical measurements across multiple games.
5. **Fix the framework inconsistency**: either align Table 4's dimensions with the paper's three-dimensional framework, or explain the additional dimensions (social reasoning, teamwork, learning ability) and integrate them into the evaluation.
6. **Remove or support Finding (2)**: either provide explicit metrics testing "incomplete information" handling, or drop this finding from the introduction.

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>