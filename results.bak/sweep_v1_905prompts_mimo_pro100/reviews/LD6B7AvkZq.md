Now let me write the consolidated review based on my careful reading and calibration analysis.

## Summary

This paper introduces a framework for understanding how language models learn context-free grammars (CFGs) by decomposing the KL divergence loss over the grammar's subgrammar structure. The authors prove that autoregressive language model loss obeys recursive relations over subgrammar hierarchies (Theorem 4.3, Theorem 4.6), demonstrate empirically that small transformers learn all subgrammars in parallel, show that subgrammar pretraining produces structurally aligned representations and can improve final loss for small models, and reveal that models struggle specifically with recursion depth rather than sequence length.

## Strengths

- **Novel theoretical framework connecting KL-divergence to subgrammar structure.** The paper defines inner and outer subgrammars (Definitions 3.3, 3.5), proves that KL divergence decomposes as a recursive sum over subgrammar hierarchies (Theorem 4.3), and derives a closed-form expression with blow-up factor 1/(1−E[R]) under context-insensitivity (Theorem 4.6). These provide a new mathematical lens for studying how language modeling loss interacts with CFG compositional structure — a genuinely new contribution in the study of formal language learning dynamics.

- **Empirical validation of the KL decomposition.** Figure 1 provides direct visual evidence that the theoretical decomposition holds throughout training for two-layer transformers — the full grammar loss equals the sum of subgrammar losses, and scaling by probability yields a clean decomposition for the asymmetric-probability case (Figure 1b). This validates the core theoretical claim with experimental data.

- **Depth-vs-recursion generalization experiment (Figure 3).** This is the paper's cleanest empirical result. Prediction error stays flat for long non-recursive contexts ((a)^i) but grows sharply for deep recursive contexts (^i), even though the ground-truth next-token distribution is identical. This cleanly isolates recursion depth as the specific failure mode, providing strong evidence that models do not genuinely internalize hierarchical syntax.

- **Parallel subgrammar learning observation.** Figure 2a shows that all four subgrammars at varying depths of recursion are learned simultaneously throughout training, rather than sequentially from simpler to more complex. Corollary 4.7 provides a formal sufficient condition (gradient independence) under which this occurs, opening a concrete research direction.

- **Alignment analysis (Table 1).** Pretrained models exhibit 8–22% higher CKA similarity across attention layers compared to models trained from scratch, with the effect increasing with longer pretraining. This is concrete evidence that subgrammar pretraining induces representations that reflect the grammar's compositional structure, not merely improved loss.

## Weaknesses

### Major

- **Gap between framing and evidence.** The title ("How Language Models Learn Syntax"), abstract, and introduction invoke children's language acquisition and natural language repeatedly (e.g., "small transformers learn subgrammars in parallel, unlike children — who first master simple substructures before progressing to more complex constructions," line 19). However, every experiment uses tiny synthetic CFGs (parentheses, simple arithmetic expressions) with small 2-4 layer transformers. The children-vs-models comparison is evocative but purely qualitative and unsupported by controlled analysis. The paper does not demonstrate or argue that the phenomena observed (parallel learning, depth sensitivity) generalize to grammars of realistic complexity, let alone natural language. This is not a framing nitpick — it determines whether the contribution is a genuine insight about language acquisition or an observation about small models on toy problems.

- **The context-insensitivity assumption is strong, central to the most elegant results, and largely unexamined.** Corollary 4.5 and Theorem 4.6 — the most elegant theoretical results — require that Q_θ's predictions for a subgrammar are the same regardless of surrounding context (line 131: "for two contexts s, s' for which P_G(A_i|s)P_G(A_i|s') > 0, Q_θ(A_i|s) = Q_θ(A_i|s')"). The empirical argument for this assumption is that "varying the prefix did not result in qualitatively different results" (Figure 1 caption, line 153), checked only on the simplest grammars. The paper does not quantify how much Q_θ actually varies across contexts, or under what conditions the assumption approximately holds. For grammars with genuine context-dependence — which includes most non-trivial natural language phenomena — the elegant decomposition breaks down, and the paper does not characterize this breakdown.

- **No confidence intervals or statistical tests reported despite 30 random seeds.** The paper reports using 30 random seeds for CKA analysis (line 255) but presents only point estimates in Table 1. For a paper about learning dynamics, where dynamics could be highly variable across seeds, this is a significant omission. The reader cannot assess whether the reported 8–22% CKA differences are robust or could arise from noise.

### Minor

- **Theorem 4.3's derivation is algebraically straightforward.** The core result — that KL divergence decomposes over subgrammar structure — follows naturally from the chain rule of probability applied to the autoregressive factorization and the non-terminal structure of the PCFG. Equations (1)–(5) are a sequence of standard algebraic manipulations. The paper calls this "the most important contribution" (line 37) but an honest framing would acknowledge the mathematical naturalness of the result.

- **The parallel learning condition (Corollary 4.7) is not verified empirically.** The paper identifies a sufficient condition for parallel learning — gradient independence — but never tests whether this condition holds in the experiments. The authors explicitly acknowledge this as future work (line 183), but verifying even a simple version of this condition would substantially strengthen the key observational contribution.

- **GPT-5.1 anecdote adds little.** The GPT-5.1 Instant experiment (line 306) is explicitly flagged as anecdotal with a footnote warning against overinterpretation. While consistent with the depth finding, it dilutes the stronger controlled evidence and contributes little given its uncontrolled nature.

- **Table 3 is referenced but not accessible.** The paper references Table 3 as evidence that pretrained models cluster subgrammar sequences closer together and better segregate subgrammar from non-subgrammar sequences (line 268), but this table does not appear in the parsed paper text, making the argument in Section 5.2 partially unverifiable.

- **Grammars are very simple.** All experiments use grammars with minimal recursive structure (e.g., parentheses with simple nesting, arithmetic expressions). The paper does not test whether the subgrammar decomposition and parallel-learning phenomena survive when grammars have center-embedding, agreement dependencies, or multi-clause structure — i.e., the kind of recursive complexity found in natural language that the paper invokes.

## Nice-to-Haves

- Measure how much the model's next-token distribution for a subgrammar varies across different contexts for each grammar studied, to quantify the context-insensitivity assumption rather than relying on qualitative claims.
- Test the gradient-independence condition of Corollary 4.7 empirically, even with simple experiments measuring cross-subgrammar gradient interference.
- Include more complex synthetic grammars with richer recursive structure (center-embedding, long-distance agreement) to test the scope of the findings.
- Report standard errors or confidence intervals for all empirical results given the 30 random seeds available.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic's criticism of mathematical depth (Issue #2):** While the derivation of Theorem 4.3 is algebraically straightforward, Theorem 4.6's geometric series result is more interesting and the overall package of definitions + theorems + empirical validation constitutes a meaningful contribution. This criticism is partially valid but overstated — it reads more as "could be deeper" than as an actual flaw. Kept as a minor weakness above.

- **Missing related works and Gruska connection:** The harsh critic mentions the connection to Gruska (1971) is underdeveloped. The paper does acknowledge this connection (line 125) and states what is novel vs. classical. Without external sources, I cannot verify whether the paper's characterization of its novelty relative to Gruska is accurate or not, so this criticism is removed.

- **Criticisms about what's in the appendix vs. main text:** The harsh critic notes Table 3 and proofs are deferred. Per hard rules, I cannot verify what is in the appendix since it was stripped by the parser.

## Novel Insights

The depth-vs-length contrast in Figure 3 provides a genuinely novel insight: transformers that achieve very low loss on a nested parentheses grammar nevertheless fail specifically on deep recursion while handling long sequences at constant depth perfectly — even though the ground-truth next-token distribution is identical in both cases. This cleanly separates the concepts of "knowing the grammar" from "being able to use the grammar at depth," suggesting that current models capture surface-level statistical regularities rather than genuinely internalizing hierarchical syntax. The parallel subgrammar learning observation is also novel and opens concrete future work on understanding when and why gradient descent learns all subgrammars simultaneously rather than sequentially.

## Suggestions

- Reframe the abstract and introduction to honestly scope the contribution: this is a study of how small transformers learn synthetic CFGs, with theoretical results that illuminate the interaction between loss and subgrammar structure, rather than a study of "how language models learn syntax" in general.
- Add a quantitative measurement of context-insensitivity: for each grammar and model, measure the variance of Q_θ(A_i|s) across contexts s, and report how this changes with grammar complexity.
- Report confidence intervals and variance across the 30 random seeds for all results.
- Include at least one grammar with richer recursive structure (e.g., center-embedding with agreement) to test the decomposition's limits.
- Move the GPT-5.1 anecdote to the appendix or remove it; it weakens the paper's otherwise careful empirical methodology.

## Score and Decision

**Evaluation on multiple axes:**
- **Originality:** Moderate-high. The subgrammar decomposition framework and the parallel learning observation are genuinely new directions. The individual mathematical results are natural, but the overall framing is novel.
- **Importance of research question:** High. Understanding how LMs acquire structured syntax is a central open question.
- **Claims supported by evidence:** Mixed. The KL decomposition is well-validated (Figure 1). The parallel learning is observed but its mechanism is unexplained. The natural-language framing is unsupported. The depth result is clean and well-supported.
- **Soundness of experiments:** Adequate for toy settings, but lack of confidence intervals, simple grammars, and the context-insensitivity gap are concerns.
- **Clarity of writing:** Generally good, with clear definitions and well-structured exposition.
- **Value to the community:** Moderate. Opens a new research direction (subgrammar-structured learning dynamics) but does not yet establish that this direction leads to insights about realistic language acquisition.

**Calibration anchors (all retrieved across rounds):**
- "A Causal Study on The Learnability of Formal Languages" (5.75, Reject) — Our paper has a stronger novel theoretical framework and more compelling empirical observations.
- "How Transformers Implement Induction Heads" (6.20, Reject) — Similar theoretical depth, but our paper has more diverse and validated empirical work.
- "Training Neural Networks as Recognizers of Formal Languages" (6.25, Accept) — Comparable quality; our paper has stronger theoretical contribution but narrower empirical scope.
- "Grammar Reinforcement Learning" (6.60, Accept) — Different focus but comparable contribution level.
- "A Percolation Model of Emergence" (7.0, Accept) — Somewhat stronger empirical evidence and broader engagement, but comparable overall.
- "When can transformers reason with abstract symbols?" (7.60, Accept) — Stronger theoretical and empirical contribution.
- "Transformers Provably Solve Parity Efficiently with Chain of Thought" (8.67, Accept) — Significantly stronger.

**Round 1 bracket:** Between 5.5 and 7.0. The paper is stronger than the rejected formal-language papers at 5.75-6.20 due to its novel theoretical framework and clean empirical results, but weaker than the accepted "Percolation Model" (7.0) due to the framing gap, underexamined assumptions, and lack of statistical rigor.

**Round 2 narrowing:** Compared to "A Causal Study" (5.75), this paper is clearly better — it has a more substantive theoretical contribution and more interesting empirical findings. Compared to "A Percolation Model" (7.0), this paper has a narrower empirical scope, a larger framing gap, and less rigor, but a comparable theoretical contribution. The paper sits slightly below 6.5 — better than the rejected papers but with enough concerns to stay below 7.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>