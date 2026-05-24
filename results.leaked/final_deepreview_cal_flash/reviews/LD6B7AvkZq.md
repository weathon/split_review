Now I'll write the final consolidated review.

---

## Summary

This paper introduces a framework for analyzing how language models learn probabilistic context-free grammars (PCFGs) by defining *inner* and *outer subgrammars* — structural components of a CFG corresponding to subtrees and simplified rule subsets. The central theoretical contribution is a set of theorems showing that the KL divergence between a target PCFG distribution and a language model decomposes recursively over subgrammars. Experimentally, the paper studies small transformers trained on synthetic PCFGs and reports that (i) subgrammar KL curves decrease in parallel during training, (ii) pretraining on a subgrammar can improve final loss and induce representations more aligned with grammatical structure (via CKA analysis), and (iii) models struggle with deep recursive contexts but handle long non-recursive sequences well — a difficulty that persists qualitatively even in large models.

## Strengths

1. **Novel subgrammar formalism for studying CFG learning dynamics.** The definitions of inner subgrammars (Definition 3.3) and outer subgrammars (Definition 3.5) are clean and principled. They capture two distinct and useful notions — compositional subtrees and simplified grammars — and connect the structure of the grammar to the language modeling objective in a way that prior work on CFG learning did not. This provides a vocabulary and a mathematical foundation for studying how learning interacts with grammatical substructure, a genuinely underexplored angle.

2. **The KL-divergence recurrence theorems (Theorem 4.3, Corollary 4.4, Theorem 4.6) articulate a nontrivial structural property.** The claim that the language-modeling loss decomposes into a sum over subgrammar contributions, and that this decomposition recurses through the grammar's DAG, is not an obvious consequence of the chain rule of KL divergence — it depends on the grammar's hierarchical structure. Corollary 4.5 (the context-insensitivity simplification) and Theorem 4.6 (the expected-recurrence blow-up formula) give concrete, testable predictions about how loss should scale with grammar parameters. These formal results, while requiring assumptions (context-insensitivity), provide a clear framework for subsequent empirical work.

3. **The depth-vs-length generalization experiment (Section 6, Figure 3) is clean and compelling.** The controlled comparison between contexts `(a)^i` (depth 0) and `(^i` (depth i) isolates recursion depth as the source of difficulty, holding vocabulary and average length constant. Prediction error rising to 0.173 at depth 200 for recursive contexts versus staying at 0.017 for flat contexts is a unambiguous demonstration. The anecdotal extension to GPT-5.1, while not rigorous, adds plausibility that the limitation is not specific to tiny transformers. This experiment is the paper's most methodologically solid empirical contribution.

4. **The CKA and cosine-similarity analyses (Section 5.2, Tables 1 and 3), while preliminary, point toward an interesting phenomenon.** The finding that pretrained models show higher CKA alignment across attention layers (+21.7% on full-grammar sequences after 20 pretraining epochs) and better segregation of subgrammar vs. non-subgrammar sequences suggests that subgrammar pretraining induces lasting representational changes. This provides a testable hypothesis about how inductive biases from substructure training affect internal representations.

## Weaknesses

### Fatal
None.

### Major

1. **The main-text derivation of the KL decomposition contains a clear mathematical error that undermines confidence in the theoretical presentation.** Equation (4) writes
   \[
   \frac{\log P_G(\alpha|\epsilon)}{\log Q_\theta(\alpha|\epsilon)} + \sum_a P_G(a)\frac{\log P_G(a)}{\log Q_\theta(a|\alpha)} + \dots
   \]
   where quantities of the form \(\frac{\log P(\cdot)}{\log Q(\cdot)}\) appear. These should be terms like \(P(\cdot)\log\frac{P(\cdot)}{Q(\cdot)}\) — standard KL divergence terms. The expression as printed divides logs rather than summing additive KL contributions and is not mathematically coherent. Since this derivation is the main text's only walk-through of the central theoretical claim, this error is significant. The theorem statements (4.3, 4.6) are stated correctly, and the full proofs are deferred to the appendix, but readers who only consult the main text may reasonably question whether the framework is sound.

2. **The experimental validation of the additive KL decomposition is claimed but not made explicit.** The paper states that Figure 1 shows "the KL divergence (loss) is the sum over the corresponding loss for each subgrammar." The axis values in the figure description (77, 25, 21, 19, 12) are consistent with the additive claim (77 = 25+21+19+12), but the paper never explicitly plots the sum of subgrammar KLs against the total, nor provides a numerical table comparing measured total KL with the sum of estimated subgrammar contributions. The reader must infer validation from axis values and the caption's qualitative statement that "scaling the divergences by their probabilities give a perfect decomposition." Given that this decomposition is the paper's central contribution, a direct quantitative comparison (e.g., a scatter plot or a table with discrepancies across checkpoints) is needed.

3. **The "parallel learning" claim (Section 4.2) is over-interpreted from the available evidence.** The paper asserts that all subgrammars are learned "in parallel" based on the observation that KL curves for different subgrammars decrease simultaneously from early epochs. Simultaneous decrease does not distinguish genuine parallel learning (non-interfering gradient updates) from sequential learning that merely appears parallel because different subgrammars converge at different rates but all start improving early. Corollary 4.7 provides a theoretical condition for parallel learning but is stated informally and is not empirically tested (it requires verifying an independence condition on gradient updates). The intended contrast with child language acquisition is not substantiated — children and language models operate under entirely different learning regimes, and no experiment bridges this gap.

### Minor

1. **Several experimental details are absent from the main text.** The specific grammars used across experiments, model architectures (beyond "2-layer, 2-head transformer"), hyperparameters (learning rate, batch size, training epochs, optimizer), and the procedure for computing KL divergences over potentially infinite PCFG languages are not described. Grammar definitions are deferred to the (stripped) appendix. While these details likely exist in the full submission, their omission from the main text makes the paper's empirical section difficult to assess independently.

2. **The CKA analysis (Table 1) reports numbers without variance or significance measures.** The reported percentage changes (e.g., +21.7% for attention layers) are presented across 30 seeds but no error bars, confidence intervals, or statistical tests are provided. The reader cannot tell whether these differences are reliable across runs. The description of what is being compared ("alignment across attention layers" — across seeds? across different inputs?) could also be more precise.

3. **Definition 4.2 uses notation that is not clearly introduced.** The expression
   \[
   D_{\text{KL}}(P_G \parallel Q)_A = \sum_{s \in \Sigma^*} P(s|\epsilon) P_G(A|s) \sum_{a \in \Sigma^*} D_{\text{KL}}(P_G \parallel Q | \neg s)
   \]
   involves \(D_{\text{KL}}(P_G \parallel Q | \neg s)\) which is not defined elsewhere, and the role of the double-sum structure is ambiguous. This definition is critical for Theorem 4.3 and its corollaries, so its opacity harms readability.

4. **Corollary 4.7's "independence condition" is stated informally and not empirically verified.** The corollary says that if gradient updates on one subgrammar do not harm performance on others, then subgrammars are learned in parallel. This is close to a tautology — the condition essentially defines away the interesting question of whether parallel learning actually occurs. The paper acknowledges this is a "future direction" but the framing in Section 4.2 overstates the result.

### Trivial

- The label "Theorem 4.2" appears where "Theorem 4.3" is meant in the text following Corollary 4.4.
- The paper references "Appendix 4" for a visual representation of Theorem 4.6, which appears to be a numbering inconsistency.

## Nice-to-Haves

- **Explicit numerical verification of the KL decomposition:** For a trained model, compute the total KL divergence via Monte Carlo sampling and compare it to the sum of estimated subgrammar KL contributions for several checkpoints, with sampling error bounds. This would directly validate Theorem 4.3.
- **A concrete example of the subgrammar DAG** for one of the experimental grammars, showing how the abstract decomposition maps to a specific grammar. This would bridge the theory and experiments.
- **Ablation on the CKA analysis:** Show whether the increased alignment after pretraining is robust to different random seeds and whether it correlates with performance gains.
- **Test the depth generalization finding more systematically:** Compare shallow-deep vs. deep-shallow sequences to separate the number of recursive invocations from depth at the point of prediction.

## Removed Points

These points were raised by one of the input reviewers but are removed under the filtering rules (see rationale below). They are listed here for transparency.

- **"Figure 5 and Figure 6 are missing."** The parser strips figures from the extraction; they exist in the original submission. Removed as parser artifact.
- **"Proofs are deferred to an appendix."** The appendix exists in the original submission. Removed as parser artifact.
- **"Grammar definitions are given in the appendix."** Same rationale — appendix exists. Removed.
- **"The paper overstates its significance."** This is a subjective judgment without a concrete anchor in the text. Removed.
- **"The connection to child language acquisition is inappropriate."** The paper makes a limited comparison and qualifies it. This criticism does not affect the core technical contribution. Removed.
- **"The theoretical core may reduce to a straightforward application of the chain rule."** This speculation is not substantiated — the decomposition over subgrammars is not an immediate consequence of the chain rule and requires the subgrammar structure. Removed as unsubstantiated.
- Strength Finder claim that "Figure 1 validates the theoretical decomposition by showing total KL equals sum of subgrammar KLs." This overstates what the figure description confirms — the axis values are consistent with the claim but an explicit validation (sum curve or table) is not presented. This strength is demoted to acknowledge the incomplete validation.

## Novel Insights

The paper introduces the idea that the language-modeling loss on PCFGs can be decomposed recursively over subgrammars, providing a formal link between grammatical substructure and training dynamics. While the execution has gaps, this perspective — treating the grammar's internal DAG as an organizing principle for studying learning curves — is genuinely new and could be valuable beyond the synthetic setting. The finding that depth of recursion, not sequence length per se, is the bottleneck for generalization is consistent with prior work but is demonstrated with unusually clean controls.

## Suggestions

1. **Fix the theoretical derivation in the main text.** Replace equation (4) with correct KL terms, and provide a self-contained derivation for the simplest case (e.g., \(S \to \alpha A \beta\)) that cleanly shows how the subgrammar decomposition produces additive KL contributions. Define \(D_{\text{KL}}(P_G \parallel Q)_A\) with standard notation and give a concrete example.

2. **Add an explicit experimental validation of the core decomposition.** For a trained model, plot the sum of subgrammar KL estimates against the directly measured total KL, or provide a table with these numbers across training epochs. Show that the equality holds within sampling error.

3. **Strengthen the parallel learning analysis.** Instead of only showing simultaneous curve decreases, test the independence condition of Corollary 4.7 directly (e.g., by measuring whether gradients from different subgrammars interfere), or at minimum acknowledge that the current evidence is consistent with several alternative explanations.

4. **Include error bars or confidence intervals for all reported numerical results** (Tables 1 and 3, CKA numbers). Report the number of seeds and the variance across runs so readers can assess reliability.

5. **Provide a concrete subgrammar DAG example** for one experimental grammar, walking through how the decomposition applies.

## Score and Decision

### Calibration

**Round 1 — Bracketing:** Three queries on topics related to this paper returned anchors in the weak (avg 2.0–3.25, all reject), mid (avg 4.0–6.67, mixed accept/reject), and strong (avg 7.6–8.67, all accept) bands. The paper's combination of a novel theoretical framework with significant presentation and validation issues places it in the mid band.

**Round 1 bracket: 4.0 – 6.5**

**Round 2 — Narrowing:** I queried two bands within the bracket. The most comparable anchors were:
- **F0Zd3knG9j** (avg 5.00, reject): "How transformers learn structured data" — clear experimental setup and well-defined synthetic data, but questioned on novelty and insufficient mechanistic evidence. Our paper has stronger theoretical novelty but weaker empirical execution and a clear mathematical error in the main derivation. Our paper is slightly weaker overall.
- **fp77Ln5Hcc** (avg 4.50, reject): "Depth Extrapolation of Decoders" — interesting theoretical analysis of depth generalization but criticized for poor writing and weak experimental methodology. Our paper has similar structural issues: a novel theoretical idea with presentation problems that make the core hard to evaluate.
- **MO5PiKHELW** (avg 5.50, accept): "Sudden Drops in the Loss" — thorough empirical analysis of syntax acquisition dynamics with extensive experiments. Our paper is substantially weaker empirically, lacking the same level of experimental rigor and validation.
- **b5lXUwZiD3** (avg 5.25, reject): "On Limitation of Transformer for Learning HMMs" — clean experimental comparisons on formal language learning. Our paper has more theoretical ambition but less clean execution.

**Final score: 4.5.** The paper contributes a genuinely novel framework (subgrammar formalism and decomposition theorems) but is held back by (i) a clear mathematical error in the main-text derivation, (ii) incomplete experimental validation of the central claim, and (iii) several empirical analyses that lack rigor (no error bars, over-interpreted trends). It is stronger than the 3.0-range papers (which had minimal contributions) but falls short of the 5.0–5.5 anchors, which had either cleaner execution or more complete validation. The paper could become acceptably strong with a corrected derivation, explicit validation of the decomposition, and tightened empirical methodology.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>