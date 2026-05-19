- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3
Now I have all the information I need. Let me construct the final consolidated review by carefully verifying each claim.

---

## Summary

This paper proposes DynaEval, a framework for evaluating LLMs through dynamic multi-agent interactions (e.g., code generation with iterative review, machine translation with proofreading). The framework defines a standardized interaction process, links it notionally to extensive-form games to motivate fairness and stability conditions, and implements these through a "referee" (LLM judge), "message pool," and synchronous interaction algorithm. Four task implementations are presented, and experiments rank several LLMs (ChatGPT, GPT-4, Claude-2, PaLM) across them.

## Strengths

- **Empirical demonstration of interaction-driven performance variation (Figure 4):** The Code G&R results show that Pass@K improves across interaction rounds for all programmer LLMs, and that the magnitude of improvement depends on which model serves as the reviewer. This is the paper's most concrete evidence that dynamic interaction captures behavior that a single-turn static benchmark cannot — specifically, the ability to iteratively improve based on feedback. This directly supports the paper's core motivation.

- **Practical fairness mechanism via synchronous interaction:** The referee + message pool design (Section 2.3) enforces anonymity and synchronicity, addressing genuine concerns about information asymmetry and identity bias in multi-turn LLM evaluation. This is a nontrivial engineering contribution: ensuring that all participants receive messages simultaneously and that the referee cannot identify which LLM generated which output mitigates two specific sources of unfairness (targeted adversarial strategies and biased scoring).

- **Diverse task implementations covering symmetric and asymmetric settings:** Four tasks (PGG, Idiom Solitaire, Code G&R, Machine Translation) demonstrate the framework's generality across cooperative/adversarial and symmetric/asymmetric interaction types. This breadth provides preliminary evidence that the framework is adaptable to varied evaluation goals.

- **Cross-validation of referee scores against standard automatic metrics in two tasks:** In Code G&R (Table 2) and Machine Translation (Table 3), the paper reports both model-based referee ratings and established metrics (Pass@K, BLEU) for the same outputs. While the comparison is qualitative rather than quantitative, the fact that the ranking patterns are broadly consistent provides some reassurance that the LLM-as-referee is not producing arbitrary scores.

## Weaknesses

### Major

- **No baseline comparison demonstrating the value added by dynamic evaluation.** The paper claims that static benchmarks "fall short" (lines 14–15), but it never tests this claim. The experiments show only what DynaEval produces — rankings of LLMs — without comparing to the ranking from a non-interactive version of the same task. For example:
  - For Code G&R: how does the ranking from DynaEval compare to the ranking from single-turn code generation (no reviewer) on the same MBPP samples?
  - For Machine Translation: how does the ranking compare to single-turn BLEU-only evaluation?
  - Do the dynamic interaction results reveal something *different* from static evaluation, or do they simply reproduce the same ordering with higher cost?

  Without this comparison, the paper cannot substantiate its central claim that static methods "struggle to assess" (line 14) the abilities that DynaEval measures, or that DynaEval's outputs have diagnostic value beyond what existing methods already provide. This is the most significant weakness because it directly undermines the stated contribution.

- **Overclaimed game-theoretic grounding.** Proposition 1 (D⊆E) asserts that any DynaEval interaction process is an extensive game with perfect information. This is trivially true, since any sequential turn-taking process can be represented as an extensive-form game tree. The paper presents this as a substantive theoretical connection ("beneficial to the fairness and stability of evaluation," line 16), but:
  - No non-trivial game-theoretic result is invoked — no equilibrium analysis, no solution concepts, no regret bounds, no subgame perfection.
  - The fairness condition (anonymity + synchronicity) and stability condition (multiple independent runs until convergence) are reasonable practical desiderata that do not require game theory. The latter is standard Monte Carlo estimation via the law of total probability (lines 62–70).
  - Stripping away the game-theoretic framing would leave the same framework with the same properties. The paper would be more honest and equally strong if it simply motivated anonymity/synchronicity as practical fairness concerns without claiming a game-theoretic derivation.

- **Model-based referee scores are not validated against human judgments.** The referee is an LLM (e.g., GPT-4) that rates anonymized outputs on a 1–10 scale. These scores are used as evaluation results (Tables 2, 3). The paper never validates these ratings against human annotators on any subset of samples. Given known issues with LLM-as-judge (position bias, self-enhancement bias, verbosity bias), this is a critical gap: the paper's "evaluation" results may partly reflect the judging LLM's biases rather than the evaluated LLMs' true abilities. The comparison to Pass@K/BLEU in Tables 2–3 provides limited reassurance because these are automated metrics, not ground-truth quality assessments.

### Minor

- **No statistical significance or effect sizes reported.** For PGG (10 runs), Idiom Solitaire (30 initial idioms, no variance reported), Code G&R, and Machine Translation: no confidence intervals, standard deviations, or significance tests are reported. Box plots in Figure 3 show substantial overlap between conditions (e.g., GPT-4 and Claude-2 in Mode 2), yet the text draws firm comparative conclusions ("GPT-4 performs best," "Claude 2 is the most advanced"). Given the inherent variability of LLM outputs, this makes it difficult to distinguish signal from noise.

- **The "consistency" comparison between referee scores and standard metrics is stated but never quantified.** The paper says for Code G&R (line 131): "We then compare the two metrics to see whether there exists any consistency." Table 2 reports both scores side by side, but no correlation coefficient, rank agreement statistic, or scatter plot is provided. The text merely reads off apparent patterns qualitatively. This falls short of the stated goal.

- **No comparison to existing interaction-based evaluation approaches.** The paper claims existing multi-round evaluation methods "still fall short" (line 14) in multi-agent scenarios, but it neither cites nor empirically compares against any of them. Methods like MT-Bench (multi-turn single-agent), ChatEval (multi-agent debate), or AutoGen's evaluation capabilities are relevant points of reference that the paper does not discuss.

- **Idiom Solitaire and PGG are not "real-world scenarios."** The paper claims all four tasks "stem from real-world scenarios" (line 98), but PGG is an abstract economic game and Idiom Solitaire is a linguistic game. These are not real-world applications; they are controlled testbeds for specific capabilities (strategic decision-making, vocabulary retrieval). The paper would benefit from either re-framing them as such or replacing them with more ecologically valid tasks.

### Trivial

- **Typo on line 14:** "gruadually" should be "gradually"; "stablility" on line 16.
- **PaLM exclusion from Idiom Solitaire and MT (explicitly noted at lines 149, 186) shrinks the comparison set, but this is acknowledged.**
- **The stability condition (Condition 2) says to run "multiple times until results converge in distribution," but no convergence analysis is performed.** The paper runs 10 times for PGG without demonstrating that 10 is sufficient.

## Nice-to-Haves

- **A static vs. dynamic ablation** on Code G&R: compare the ranking and scores from a single-turn code generation run (no reviewer) vs. the multi-round DynaEval run. This would directly quantify the value added by interaction.
- **Human evaluation of referee scores on a subset of outputs** to establish whether the LLM-as-referee produces ratings that correlate with human quality judgments.
- **Convergence analysis** for the stability condition: show a learning curve of average score vs. number of independent runs to justify the chosen number.
- **Cost reporting:** API call counts, token usage, and wall-clock time per evaluation task to help users assess practicality.

## Removed Points

- *Strength: "Game-theoretic formalization is an advance over prior ad-hoc methods."* This is overstated. The formalization is D⊆E (trivially true), and the conditions derived do not depend on non-trivial game theory. The harsh critic's assessment of the game-theoretic connection is more accurate; this claimed strength conflicts with a verified weakness and is removed.
- *Harsh critic's claim that "Proposition 1 is not proven" and that "the paper does not prove the converse."* Proposition 1 only claims D⊆E (one direction), which it correctly states. The reviewer demands something the paper never attempts to prove.
- *Strength: "Explicit stability condition derived from sampling...grounding the stability requirement in the law of total probability."* The law of total probability justification (lines 62–70) is mathematically correct but essentially says "average over multiple runs," which is standard; this is not a strength worth highlighting.
- *Criticism that "Definition 1 is not novel."* The paper does not claim Definition 1 is novel; it standardizes the interaction process for the purposes of the framework. This is a common and acceptable practice.

## Novel Insights

The harsh critic and strength finder largely converge on the same observations: Figure 4 (Code G&R improvement over rounds depending on reviewer identity) is the single most informative result, and the game-theoretic framing is decorative rather than substantive. Neither reviewer surfaces an insight about the paper that goes beyond what the paper already states about itself.

## Suggestions

1. **Add a static-to-dynamic comparison as the primary experiment.** For Code G&R, run a single-turn baseline (no reviewer iteration) and compare the ranking, then show what interaction reveals that static evaluation misses. This directly validates the core claim.
2. **Downgrade or remove the game-theoretic framing.** Either justify why EGPI is more than a notational convenience (e.g., derive a non-trivial property), or simply present the fairness/stability conditions as practical design choices without claiming a game-theoretic derivation.
3. **Report confidence intervals or bootstrap estimates** for all main results, especially the PGG box plots where overlap is visible.
4. **Validate the LLM referee against human raters** on at least 50–100 samples from Code G&R or MT.
5. **Quantify the "consistency" between referee scores and standard metrics** with a rank correlation (e.g., Spearman's ρ) or scatter plot.
