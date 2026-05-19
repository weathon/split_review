- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3
Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual text. Let me produce the final consolidated review.

## Summary

This paper proposes R², an LLM-based framework for novel-to-screenplay generation (N2SG). The framework has two key technical components: a hallucination-aware refinement method (HAR) that iteratively detects and corrects inconsistencies in LLM outputs, and a causal plot-graph construction method (CPC) that uses a greedy cycle-breaking algorithm to build directed acyclic graphs of event causalities. R² mimics the human screenwriting process with a Reader module (extracts events and builds causal plot graphs) and a Rewriter module (generates scene outlines and screenplays). The paper reports large absolute win-rate gains over three baselines (ROLLING, Dramatron, Wawa Writer) using GPT-4o as the primary evaluator, with partial corroboration from human evaluation.

## Strengths

1. **Novel task formulation and clear overall framework design.** The paper identifies a concrete and practically motivated task (novel-to-screenplay generation) that existing work does not directly address. The two-module Reader-Rewriter architecture that mimics the human screenwriting process is well-motivated and clearly described (Section 3). The integration of causal plot graphs as an intermediate representation is a reasonable design choice.

2. **Quantitative ablation study showing large effects of HAR and CPC.** Table 3 reports that removing HAR causes drops of 38.4% (Dict & Gram) and 46.1% (Consistency), while removing CPC causes drops of 64.2% (Interesting) and 71.4% (Consistency). These large magnitudes provide empirical evidence that both proposed techniques contribute meaningfully to the framework's performance.

3. **Human evaluation provides partial independent corroboration.** Table 2 shows that human evaluators also prefer R² over all three baselines on overall win rate, particularly on Interesting and Transition aspects. This provides some evidence beyond the GPT-4o evaluation, which is important given the known limitations of LLM-as-judge.

4. **Data-driven tuning of refinement rounds.** Figure 4(b) empirically shows that suggestions increase through round 4 and then decline, the adoption rate stabilizes around 60% in rounds 2–4, and time cost grows with each round. This provides a principled rationale for setting the refinement round to 4.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation rests on only 5 novels — too small to support strong quantitative claims.** The paper states (line 99) that the test set consists of five novels. For a long-form generation task where narrative structures, genres, and writing styles vary dramatically, five samples cannot support claims of "substantially outperforming" baselines by 20–57% absolute margins. No confidence intervals, statistical significance tests, or per-novel breakdowns are reported. This undermines the headline quantitative results.

2. **LLM-as-judge discrepancies with humans are acknowledged but not analyzed or resolved.** GPT-4o serves as the "main evaluator" (line 101), yet the paper reports (line 120) that on some aspects R² "has a slightly poor performance" per human evaluators while GPT-4o shows R² winning. The paper attributes this to "human preference for long-form narrative" without reporting any agreement metrics (e.g., Cohen's κ) between GPT-4o and humans. If the automatic evaluator disagrees with human judgments on specific dimensions, it is unclear which dimensions can be reliably interpreted from the GPT-4o evaluation alone. The paper needs to calibrate the automatic evaluation against human judgments per aspect.

3. **Baseline input setup is inconsistently described.** Dramatron is designed to work from loglines but here receives R²-extracted plot events (line 105). ROLLING also uses R²-extracted plot events as input. This makes ROLLING effectively a partial ablation (Reader output + naive generation vs. full R²), which is informative but conflates multiple differences. For Dramatron, the modification of its input interface is not discussed in terms of how well the system adapts to this non-standard input. Adding a simple direct-prompting baseline (same backbone, no causal graph) would help isolate the value of the causal graph structure.

### Minor

4. **Ablation study comparison target is ambiguous.** The ablation results (Table 3, lines 129–131) report "lose" percentages (e.g., "38.4% lose") but never explicitly state what the ablated version is compared against — the full R² system? A fixed baseline? The caption says "win rate evaluated by GPT-4o" without specifying the opponent. While the pattern of drops is clear, the exact experimental setup needs clarification.

5. **HAR's hallucination detection mechanism has limited independent validation.** HAR relies on the same LLM to both generate initial extractions and then identify inconsistencies in them (Section 2.1 description and line 76). This self-refinement loop inherits the known circularity issue of self-refinement methods (the model judges its own outputs). While the ablation study shows HAR helps overall, the paper does not report hallucination detection accuracy, provide correction examples, or evaluate whether HAR introduces false positives (correcting things that were not actually errors).

6. **Human evaluators judge only 1000-token excerpts.** For a task where cross-scene consistency over long screenplays is a central claim, the human evaluation protocol (line 99) using excerpts cannot fully assess whether the method maintains long-range plot coherence. GPT-4o evaluation presumably faces a similar context-length limitation.

### Trivial

7. **Seven evaluation aspects are listed but not defined** (line 101). Terms like "Interesting," "Coherent," "Human-like," and "Transition" are used without precise definitions or rubrics.

8. **The five test novels are not named** (line 99). Readers cannot assess whether the test set covers diverse narrative styles or has potential confounds.

## Nice-to-Haves

- An additional simple baseline using the same backbone (GPT-4o-mini) with a direct prompt (e.g., "generate a screenplay from this novel chapter by chapter") without access to R²'s extracted events would help isolate the value of the causal graph and extracted event structure.
- A per-novel breakdown of results would help assess whether R²'s gains are consistent across different types of novels or driven by a subset.
- Reporting the total API call cost per novel would help assess the practical trade-off of the multi-round HAR refinement.

## Removed Points

- **"Baseline comparison is an ablation in disguise" (harsh critic).** ROLLING uses R²-extracted plot events, but this is a natural and informative comparison — it shows what a simple iterative generator achieves with the same underlying event data. For Dramatron, giving it structured plot events rather than loglines is a reasonable adaptation to the N2SG task; if anything it favors the baseline. The criticism is overstated.
- **"Cycles always arise from hallucinations" (harsh critic).** The paper says cycles "often" arise from hallucinations (line 53), not "always." The critic misrepresents the paper.
- **"Missing appendix content, prompts, reproducibility details" (harsh critic).** Per instructions: the PDF parser strips images and appendix sections; these exist in the original submission. This criticism is inadmissible.
- **"No limitations section" (harsh critic).** Minor formatting preference, not a substantive weakness.
- **"Missing related work" (harsh critic did not raise this, but for completeness).** Per instructions, I cannot mention missing related works.
- **Strength Finder: "High overall win rates."** This is factual (the numbers exist) but the evaluation weakness limits their reliability. Kept in strengths with implicit caveat.
- **Strength Finder: generic/superficial praise about problem importance.** Dropped. The paper correctly identifies a gap in existing work, which is a reasonable strength.
- **Strength Finder points that conflict with verified weaknesses.** None directly conflict — the strengths describe what the paper does, the weaknesses describe limitations of how it does it.

## Novel Insights

None beyond the paper's own contributions. The reviews surface methodological concerns about evaluation validity that are more severe than the paper itself acknowledges, but do not offer new analytical perspectives on the technical approach.

## Suggestions

1. **Expand the evaluation to at least 20–30 novel-screenplay pairs** and report per-novel results with confidence intervals or bootstrap significance tests for pairwise preferences.
2. **Calibrate the GPT-4o evaluation against human judgments per aspect.** Report Cohen's κ or similar agreement metrics, and either restrict claims to dimensions where agreement is acceptable or adjust the evaluation protocol.
3. **Clarify the ablation comparison target** (full R² vs. ablated version? or vs. a fixed baseline?) and report full win/lose/tie distributions rather than just "lose" percentages.
4. **Add a direct-prompting baseline** that generates screenplays chapter-by-chapter without the causal graph structure, using the same backbone model, to isolate the contribution of the graph.
5. **Include a small qualitative analysis of HAR corrections** — examples of hallucinations detected and corrected vs. false positives — to demonstrate that HAR is not simply making random changes.
