- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6
Now I have all the information needed. Let me synthesize the final consolidated review.

## Summary

PuzzlePlex introduces a benchmark of 24 puzzles (single-player and competitive two-player, deterministic and stochastic, text-only and text-image) designed to evaluate LLM reasoning and planning in multi-turn adversarial environments. The benchmark is novel in its inclusion of multi-turn competitive two-player puzzles and multimodal variants, and it provides baseline strategies, difficulty scaling, and a structured evaluation framework. Experiments across many LLMs reveal that current models struggle substantially, with high illegal move rates and limited planning capability.

## Strengths

- **First benchmark to include multi-turn competitive two-player puzzles.** Table 1 systematically compares PuzzlePlex against eight existing benchmarks (SmartPlay, AgentBench, etc.) and shows it is the only one that includes multi-turn competitive two-player games. The experiments in Table 3 provide concrete evidence that the benchmark can produce differentiated results across models (GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro, etc.) at two difficulty levels in this underexplored setting.

- **24 diverse puzzles with careful categorization and baseline strategies.** The puzzle set spans four categories (single-player deterministic/stochastic, competitive two-player deterministic/stochastic) with customized baselines including SMT solvers, DP, search algorithms, MCTS, and greedy methods (Section 3.3). This provides calibrated reference points for interpreting LLM performance — enabling concrete findings such as "LLMs lose to legal-random-move opponents" or "FIR exceeds 50% in deterministic puzzles."

- **Detailed error analysis with actionable findings.** Section 4.6 classifies errors across 100 runs per text game (Reasoning & Planning 63%, Comprehension 12%, Memorization 11%, etc.) and identifies that 76% of successful plays were not due to genuine reasoning but to random moves or opponent mistakes. This goes beyond aggregate scores to diagnose *why* LLMs fail.

- **Demonstrated sensitivity to prompting methodology.** Section 4.4 and Table 5 show that the benchmark detects differential effects of prompting strategies (one-shot, Tree-of-Thought) across puzzle types, and that gains from ToT diminish as state space grows — evidence that PuzzlePlex is useful for more than just model ranking.

- **Multimodal (text+image) puzzles.** PuzzlePlex includes text-image variants (SudokuM, SudoKillM, SuperplyM), an underexplored dimension in puzzle benchmarks. The finding that no model completes any instance of SudokuM/SudoKillM highlights real limitations of multimodal LLMs in interactive settings.

## Weaknesses

### Fatal
None.

### Major

- **Small sample sizes for deterministic games undermine comparative claims.** Section 4.2 specifies 5 instances for deterministic two-player games and 10 for single-player deterministic. No confidence intervals, standard deviations, or significance tests are reported. With 5 instances and binary outcomes, the 95% binomial CI for a reported win fraction of 0.49 (GPT-4o on intermediate deterministic, Table 3) spans approximately [0.14, 0.86], making it impossible to distinguish systematic differences from noise. The core finding that "LLMs are poor at puzzles" is supported by other evidence (FIR > 50%, qualitative error analysis), but granular comparative claims such as "GPT-4o outperforms other models" rest on much weaker statistical ground. The paper explicitly increases stochastic game runs to 50 "to ensure statistical significance" (Section 4.2) but does not extend comparable rigor to deterministic games.

### Minor

- **Normalization of single-player scores obscures raw performance.** Section 3.4 caps normalized scores at 1 when an LLM exceeds the baseline and uses the ratio LLM_score/baseline_score otherwise. Raw scores and baseline scores are not reported in the main tables. Two models with very different raw behaviors could receive the same normalized score (e.g., a model that barely edges out a weak baseline and a model that solves puzzles optimally both get 1.0). The FIR column provides partial disambiguation, but reporting raw scores alongside normalized ones would allow readers to interpret what the normalized values actually represent.

- **Ties in competitive two-player games are treated identically to losses (score=0), and tie rates are not reported.** Section 3.4 assigns 1 for a win, 0 for a loss or tie. The Davidson variant of Bradley-Terry (which handles ties) is mentioned in Section 3.4 but only used for the strength metric relegated to the appendix (§C.1). In many deterministic board games where ties can arise from optimal play, assigning 0 conflates near-optimal play with poor play. Reporting win/loss/tie breakdowns separately or scoring ties as 0.5 would be more informative.

- **Instance counts for the legal-move analysis (Section 4.5) are ambiguous.** The text describes using an easy-level 4×4 Sudoku grid and limiting SudoKill's legal move list to 100, but does not explicitly state how many instances or seeds were used for this experiment, making it difficult to assess the reliability of the results in Table 4.

### Trivial

- Text-image puzzle results (Tables 14, 15) are referenced only in the appendix and are not summarized in the main paper's result tables, despite being discussed qualitatively in Section 4.3. A summary row or a brief main-paper table would improve accessibility.

## Nice-to-Haves

- **Expand difficulty scaling beyond two levels.** The paper emphasizes graduated difficulty as a key feature but only tests easy and intermediate. Demonstrating a third (hard) level for a subset of puzzles would substantiate the claim that PuzzlePlex can "evolve as LLMs become more sophisticated."

- **Use the benchmark more systematically to isolate specific failure modes.** The most informative experiments are the controlled ones (providing legal moves in Section 4.5, error analysis in Section 4.6). Comparing the same puzzle type (e.g., deterministic vs. stochastic variant of the same game, or text-only vs. text-image version) on the same models would yield sharper diagnostic insights about *what* specifically LLMs struggle with.

- **Report token counts or context usage alongside results.** The paper mentions average token counts per game in §C.3 but does not integrate them into the main analysis. Token consumption could help explain why some models fail (context length limits) and would be a useful diagnostic signal.

## Removed Points

These points were considered but removed with brief justification:

- **"Generator function is underspecified for reproducibility"**: The harsh critic notes that Section 3.1 describes G_p only at a high level. The paper states that details are in §A.1 and §A.3 (appendix). Since the parser strips appendix content from all papers, this criticism penalizes missing content that exists in the original submission. **REMOVED.**

- **"Generator should explain difficulty mapping with a concrete example in main text"**: This is a scope/nice-to-have point already covered in Nice-to-Haves. **REMOVED** from weaknesses.

- **"Error analysis (76% figure) should be presented as approximate rather than quantitative"**: The paper already says "Among the samples we analyzed, we found that in 76% of cases..." which implicitly acknowledges the sample-based nature. The sample sizes (100 per text game, 50 per text-image game) are reasonable for a qualitative typology. **REMOVED.**

- **"LLMs losing to random opponents is striking but not highlighted or explained"**: This is a missed-observation note, not a weakness of the paper. The paper does report these results in Table 3 and discusses FIR and legal move issues extensively. **REMOVED.**

- **"No limitations section in conclusion"**: A standard but non-critical omission that does not affect the paper's substance. **REMOVED.**

- **"Missing related works"**: Cannot be verified. **REMOVED** per instructions.

- **Strength Finder's generic/superficial strengths**: "This paper addressed an important problem" — generic. **REMOVED.**

## Novel Insights

No genuinely novel insight emerges from the reviews beyond what the paper itself contributes. The reviews largely corroborate the paper's findings (LLMs struggle with puzzle reasoning) while identifying a mismatch between the strength of the benchmark design and the statistical rigor of the experimental evaluation — a gap that is real but addressable and does not invalidate the core contribution.

## Suggestions

- Add confidence intervals (or at least standard deviations) to all reported normalized scores and win fractions, especially for the small-sample deterministic experiments. Report the win/loss/tie breakdown for competitive two-player games.
- Report raw scores alongside normalized scores for single-player puzzles, or provide a table in the appendix with raw and baseline scores.
- Increase the instance count for deterministic two-player experiments (from 5 to at least 20-30) or justify the current choice transparently and qualify comparative claims accordingly.
- Clarify the instance/seed count used in the legal-move analysis (Section 4.5).
- Include a brief summary of text-image results in the main tables (or as a supplementary row) rather than only in the appendix.
