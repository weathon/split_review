Now I have a clear picture. Let me compose the final consolidated review.

---

## Summary

This paper derives closed-form leading-term approximations for the weights of attention-based transformers trained on natural language data under next-token prediction. The key theoretical contribution is a characterization of how learned weight matrices (output, value, query-key, positional encoding) decompose as compositions of three interpretable corpus-statistic basis functions: bigram, interchangeability, and context mappings. The theory is validated on a 3-layer attention-only transformer trained on TinyStories, achieving cosine similarity >0.998 between theoretical and learned weights, and extended to Pythia-1.4B through a covariance-based comparison.

## Strengths

- **Novel theoretical characterization of all attention-based transformer weights**: Theorem 4.1 provides explicit leading-term approximations for the output matrix, value matrix, query-key matrix, and positional encoding as compositions of corpus-derived basis functions, with Frobenius-norm error bounds. This moves beyond prior work that relied on synthetic data or simplified architectures by incorporating natural language data, residual connections, causal masking, and relative positional encodings.

- **Interpretable decomposition into semantically meaningful basis functions**: Section 4.2 defines bigram (\(\bar{\mathbf{B}}\)), interchangeability (\(\Sigma_{\bar{\mathbf{B}}}\)), and context (\(\bar{\Phi}\)) mappings, and Figure 5 demonstrates that top-correlated tokens under these mappings recover meaningful lexical-semantic relationships (e.g., "fish" links to "pond", "lake" under context mapping; "red" associates with "balloon", "truck" under bigram).

- **Strong quantitative validation on TinyStories**: Table 1 reports minimum cosine similarities of >0.998 across all weight types for the small learning rate, and Figure 4 shows that similarities remain above 0.7 even after 100 epochs. These findings demonstrate that the theoretically predicted directions align closely with what the model actually learns.

- **Extension to a real-world large language model**: On Pythia-1.4B, Figures 6–7 show that the covariance matrices of attention and embedding representations exhibit high cosine similarity with the leading-term features derived from OpenWebText across most layers at early training steps. The layer-wise and head-level analysis provides insight into how different model components converge to or diverge from these associative features.

- **End-to-end mechanistic interpretation of weight cooperation**: Section 4.2.3 consolidates the individual weight characterizations into a coherent picture of the forward pass (Equations 12–13), showing how the attention matrix's token-token correlations align with the value/output projections to selectively focus on context that improves next-token prediction.

## Weaknesses

### Major

- **Narrow theoretical regime vs. broad empirical claims**: Theorem 4.1 bounds the approximation to hold only while \(s \leq \eta^{-1} \min(5/(8\sqrt{T}), 1/(12L))\). With the reported \(T=200\), \(L=3\), and \(\eta=0.005\), this gives \(s \leq 5.56\) gradient steps — fewer than 6 updates. The paper nonetheless frames the theorem as characterizing the early phase of training and uses empirical results across 100 epochs to argue that the derived features remain relevant. The theory provides no explanation for why the leading-order direction should persist once higher-order terms dominate the error bounds (indeed, the error bounds themselves — e.g., \(3s^2\eta^2\) — grow beyond the leading term after very few steps). The gap between the mathematical guarantees and the empirical claims is a significant limitation that the paper does not adequately address.

- **Direction-only validation cannot verify the specific theoretical form**: All comparisons between theory and experiment use cosine similarity, which is magnitude-invariant. The high similarities demonstrate that learned weight matrices are directionally correlated with the proposed basis matrices, but they do not verify that the step-dependent coefficients (e.g., \(s\eta\), \(\binom{s}{2}\eta^2\), \(\binom{s}{4}\eta^4\)) match the actual weight magnitudes or that the functional form of the leading terms is uniquely correct. Any matrix proportional to the same data statistic would produce the same cosine similarity. The theory makes specific predictions about how weights scale with step count and learning rate — none of this is tested. This substantially weakens the evidence for the gradient expansion itself, though the corpus-statistic alignment remains informative.

### Minor

- **Pythia extension glosses over subword tokenization**: The theory constructs basis functions at the level of a fixed word-level token vocabulary (e.g., "fish", "pond"). Pythia uses a BPE tokenizer, splitting words into subword units. The paper does not discuss how bigram and context statistics over subword tokens relate to the word-level semantic associations it interprets (Figures 3, 5, 6, 7). Without addressing this, the claim that the theory generalizes to real-world LLMs is somewhat weakened, though the Pythia results remain suggestive and the core contribution stands on the TinyStories validation.

- **Ambiguity in Figure 4 / Table 1 presentation**: Table 1 reports results for the small learning rate (\(\eta=0.005\), minimum cosine >0.998), while Figure 4 shows a curve dipping to ~0.7. The text says results are provided "for both settings in Table 1 and Figure 4," but the figure caption does not specify which learning rate is plotted, creating unnecessary ambiguity. This is a presentation issue, not a data inconsistency — the dip to 0.7 is consistent with the larger \(\eta=0.05\) setting.

- **No baselines for cosine similarity**: The paper does not report similarity between learned weights and random matrices or permuted statistics, which would contextualize whether the observed >0.998 values are trivially high given the small vocabulary (3k most frequent words) and shared training corpus.

- **Limited vocabulary in TinyStories experiments**: Using only the 3,000 most frequent words from TinyStories may artificially inflate cosine similarity by reducing effective dimensionality and noise compared to a more realistic vocabulary, and the statistics are computed from the same data used to train the model.

### Trivial

- Key matrices \(\bar{\mathbf{Q}}\) and \(\Delta\) are not explicitly defined in the main text; the reader must consult the appendix for a complete understanding of the theory.

- The paper does not discuss the gap between full-batch gradient descent (assumed by the theory) and the mini-batch SGD used in experiments (batch size 2048).

## Nice-to-Haves

- Testing the predicted polynomial scaling of weight magnitudes with step count and learning rate (e.g., Frobenius norm of learned weights against predicted \(s\eta\), \(\binom{s}{2}\eta^2\), etc.) would move beyond direction-only comparisons and provide genuine validation of the gradient expansion.

- A control experiment comparing cosine similarity against random or permuted statistics would strengthen confidence in the TinyStories results.

- Discussion of how subword BPE statistics relate to the word-level semantic associations claimed for the Pythia experiments.

## Removed Points

These points from the input reviews were considered but removed from the final review:

- **Criticism about attention-only architecture**: The paper explicitly acknowledges this limitation in Definition 3.1 and cites Wang et al. (2025) showing attention-only models can be competitive. This is a scoped choice, not a flaw.

- **Claim that Figure 4 and Table 1 are internally inconsistent**: This is a misreading. Table 1 is for small \(\eta\) and Figure 4 likely shows large \(\eta\). The presentation is ambiguous but there is no actual data contradiction.

- **Claim that mechanistic insight is "overstated"**: The paper provides a substantive end-to-end analysis in Section 4.2.3 (Equations 12–13) showing how weights cooperate. The depth of mechanistic explanation, though not exhaustive, is genuine.

- **Demand for error bars, confidence intervals, and multiple random seeds**: Standard for the field is single-run evaluation for training dynamics studies of this type; the request is a nice-to-have rather than a weakness.

- **Complaint that \(\bar{\mathbf{Q}}\) and \(\Delta\) are not defined in main text**: Already captured as Trivial above; does not warrant a separate Major/Minor entry.

- **All formatting, typo, and grammar criticisms**: These are parser artifacts or presentation nitpicks that carry no evaluation weight.

## Novel Insights

The paper's most genuinely novel contribution is the identification that all four weight types in an attention-based transformer — output, value, query-key, and positional encoding — can be expressed through compositions of just three corpus-level statistics at early training. This unification across weight types is not present in prior work (e.g., Bietti et al. 2023 analyzed only specific components under more restrictive assumptions), and the fact that the same basis functions appear in different compositions for different weight matrices provides a principled account of how these weights cooperate. The interchangeability mapping \(\Sigma_{\bar{\mathbf{B}}}\) as a building block for both attention and positional encodings is a particularly clean insight.

## Suggestions

- Explicitly compute and report the number of gradient steps for which the theorem's error bounds remain below the leading term, and discuss the gap between this bound and the empirical observation of persistent alignment.
- Test the predicted polynomial scaling of weight magnitudes against step count and learning rate — this is the most direct way to validate the gradient expansion beyond direction.
- Add a baseline cosine similarity (e.g., against a random matrix or permuted bigram statistics) to contextualize the TinyStories results.
- Clarify in Figure 4's caption which learning rate is being plotted, or show both learning rates on the same figure.

## Score and Decision

**Round 1 bracket**: Based on comparison with anchors across weak (2.33–3.40), middle (3.75–7.33), and strong (7.60–8.67) bands, the paper plausibly sits in the 5.0–7.0 range.

**Round 2 narrowing**: Compared against "Locating Information in LLMs via RMT" (4.80, rejected — weaker theory, less insight), "Stagewise Development in Transformers" (5.50, rejected — less precise theoretical predictions, weaker validation), "Transformer Block Coupling" (6.25, accepted — comparable depth), "How Transformers Implement Induction Heads" (6.20, rejected — rigorous theory but more simplified setup), and "A Percolation Model of Emergence" (7.00, accepted — stronger theoretical framework).

This paper is stronger than the 4.80 and 5.50 anchors (more precise theory, stronger empirical validation on both controlled and large-scale models) and comparable to the 6.20–6.25 anchors (genuine theoretical contribution, interpretable results, but significant limitations in the narrow theoretical regime and direction-only validation). The paper is weaker than the 7.00+ anchors due to the disconnect between the narrow theoretical guarantee and the broad empirical claims, and the untested nature of the specific functional-form predictions.

**Anchors consulted across all rounds**:
- `kkVTeMvC9D` (3.40, round 1): Weaker — training Jacobian analysis without mechanistic interpretability.
- `2NwHLAffZZ` (2.33, round 1): Much weaker — linearization theory with limited transformer relevance.
- `q541p2YLt2` (2.50, round 1): Weaker — narrower focus on attention entropy.
- `NbbsRnPBoS` (2.33, round 1): Much weaker — deep linear networks, not transformers.
- `97rOQDPmk2` (7.33, round 1): Stronger — more complete theoretical analysis with convergence guarantees.
- `xEZiEhjTeq` (5.50, round 1): Comparable — stagewise development, interesting but limited model scale; our paper has stronger theory and validation.
- `GeUK3zGreN` (6.50, round 1): Stronger — clearer practical implications for transformer training.
- `hNkXTqDrfb` (3.75, round 1): Weaker — weak connection between proofs and claims, insufficient evidence.
- `d8w0pmvXbZ` (8.00, round 1): Much stronger — clear practical contribution with rigorous empirical methodology.
- `MmWkNmeDNE` (4.80, round 2): Weaker — RMT applied to weight matrices without mechanistic theory.
- `kvLenbZZgg` (6.25, round 2): Comparable — Jacobian-based coupling metric, interesting but limited interpretation.
- `1lFZusYFHq` (6.20, round 2): Comparable — induction head theory, rigorous but simplified setup.
- `zjAEa4s3sH` (6.50, round 2): Slightly stronger — novel perspective on LLM trajectories.

**Final assessment**: The paper makes a genuine theoretical contribution with interpretable results and solid (if imperfect) empirical validation. The two major weaknesses — the narrow theoretical regime and direction-only validation — are significant but do not invalidate the core contribution: the decomposition of early-stage transformer weights into interpretable corpus statistics is supported by both the theory and the empirical evidence. This is a solid contribution that would benefit the community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>