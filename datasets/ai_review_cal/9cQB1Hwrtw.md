- Decision: Accept
- Avg Score: 6.75
- Scores: 5, 6, 8, 8
Now I have a complete picture of the paper and both reviews. Let me write the consolidated review.

## Summary

This paper investigates whether transformers can learn to perform search using graph connectivity (next-step prediction on DAGs) as a testbed. The authors find that transformers *can* learn to search when trained on a carefully balanced distribution that removes heuristic shortcuts, and they develop a novel mechanistic interpretability method to show that trained models implement an exponential path-merging algorithm. However, the paper's key negative findings are that learning difficulty increases steeply with graph size, that increasing model width (within the tested range) does not reliably overcome this difficulty, and that two chain-of-thought variants (DFS trace prediction and selection-inference) also struggle on larger graphs.

## Strengths

- **Clean demonstration that transformers can learn to search given the right training distribution.** Figure 2 (described in Section 3.1.1) shows that a model trained on the balanced distribution achieves near-perfect accuracy across all three test distributions (naïve, star, balanced) and generalizes to unobserved lookaheads, while models trained on naïve or star distributions fail. This is a clear, well-controlled result.

- **Novel mechanistic interpretability method that recovers the exponential path-merging algorithm without prior knowledge of the algorithm.** Section 4.1 describes a multi-step procedure (activation patching, perturbation analysis, computation-graph reconstruction) that goes beyond prior work by extracting the exact algorithm the model uses, not just correlational evidence. The method is applied to 2000 inputs and reveals that the model computes reachable sets per vertex and merges them layer-by-layer (Figure 4).

- **Scaling experiments showing that increasing model width does not alleviate difficulty on larger graphs.** Figure 6 shows that as input graph size grows, the probability of high accuracy becomes vanishingly small. Figure 7 shows that varying model dimension (with fixed depth) produces no consistent reduction in test loss across 14 seeds. This is a concrete negative result that challenges the assumption that scale alone yields robust search abilities within this regime.

- **Generalization to natural-language proof search.** Section 3.1.2 re-runs the experiment using implicational-propositional-logic sentences in natural language and reports qualitatively similar training behavior (Figure 9), strengthening the claim that the findings are not artifacts of the symbolic input format.

- **Systematic evaluation of two chain-of-thought variants.** Section 6 tests DFS trace prediction and selection-inference, finding that even with intermediate tokens, models struggle on larger graphs and scaling does not help (Figures 14, 16, 17). This extends the negative result to practically relevant prompting approaches.

- **Careful experimental design.** The use of streaming training, explicit control of heuristics via the balanced distribution, multiple random seeds to capture variance, and exact-match filtering of test examples demonstrates methodological rigor.

## Weaknesses

### Major

- **The scaling analysis does not vary the number of layers.** The experiments fix the number of layers (8 for graph-size scaling, Figure 6) and vary only hidden dimension (Figure 7). However, the identified path-merging algorithm predicts that each layer can double the reachable set — depth is the natural scaling dimension for this algorithm. The paper's conclusion that "increasing model scale does not alleviate this difficulty" is tested only along the width axis. The paper does not systematically investigate whether increasing depth (which directly affects the algorithm's capacity) changes the scaling behavior. This is a significant gap: a model with more layers might handle larger graphs even if a wider-but-shallow model cannot.

### Minor

- **Abstract overstates the strength of the negative findings relative to the evidence.** The abstract claims that "increasing model scale will not lead to robust search abilities" and that chain-of-thought "does not resolve this inability," presenting these as general conclusions. The conclusion section (line 165) appropriately acknowledges "It is possible that scaling to much larger model sizes may lead to emergent searching ability" and that only specific CoT variants were tested. There is a disconnect between the abstract's definitive tone and the body's more measured caveats. The experiments are conducted on small models (hidden dim 16–~128, ≤8 layers, graphs up to ~45 vertices), and the claims should be scoped to this regime.

- **The two CoT variants tested (DFS trace prediction and selection-inference) do not exhaust the space of in-context exploration approaches.** The abstract frames this as a finding about "chain-of-thought" generally, but the paper only tests two specific operationalizations. Other approaches (e.g., free-form CoT where the model generates its own intermediate reasoning tokens, or tree-of-thought variants) remain unexplored. The paper should explicitly acknowledge that the negative result applies to the tested variants, not to all possible CoT formulations.

- **Mechanistic interpretability thresholds lack sensitivity analysis.** The method uses three manually-set thresholds (α=0.4, κ₁=20, κ₂=10). The paper does not report how the proportion of "explained" operations varies with these thresholds, nor does it provide a quantitative breakdown of how many attention operations are classified as path-merge vs. copy vs. discarded. The conclusion that "almost all examples" are explained (line 165) would be strengthened by reporting the specific percentage and showing robustness to threshold choices.

- **The natural-language proof search experiment (Section 3.1.2) reports only training loss curves, not accuracy numbers.** The claim that "the model has increasing difficulty learning the task as the graph size increases" is supported by loss trajectories, but the degree of difficulty is not quantified. Reporting accuracy would allow direct comparison with the symbolic experiments.

- **Potential confound between search difficulty and input length in the DFS experiment.** In Section 6.1, the sequence of visited vertices (and the padding required to handle it) means input length grows with graph size. The paper does not fully disentangle whether the difficulty on larger graphs stems from the search requirement itself or from the increased input length. A control experiment (e.g., fixed input length with varying search difficulty) would strengthen the claim.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis for the interpretability thresholds (α, κ₁, κ₂).
- Varying the number of layers in the scaling experiments to test whether depth (not just width) alleviates the difficulty on larger graphs.
- An ablation validating the identified path-merge operations (e.g., corrupting them and measuring accuracy drop).
- Reporting accuracy for the natural-language proof search experiments.
- An error analysis characterizing the failure modes on large graphs (e.g., does the model output random vertices or default to a heuristic?).

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- The critic's claim that in the DFS task "the model never needs to represent the goal" is inaccurate. The DFS trace is generated from a randomly-selected start to a *random goal vertex* (line 143), so the model is trained on goal-directed search traces. The goal is not explicitly marked in the input, but the task structure inherently involves goal-directed search.
- The critic's claim about missing appendix content (balanced distribution details, etc.) is removed per the instruction that the parser strips appendix sections from all papers.
- The critic's suggestion that the paper should include non-transformer baselines (BFS/DFS) is removed as scope creep — the paper studies transformer capabilities, not algorithmic comparison.
- The critic's request for error analysis is removed as a nice-to-have rather than a weakness. The paper's claims are supported by loss and accuracy metrics.
- The critic's claim that "the paper does not report what proportion [of operations are explained]" — the paper states "almost all examples" (line 165). While a specific number would be better, this does not invalidate the analysis. This is subsumed under the minor weakness about missing quantitative breakdown.
- Several of the critic's "Strengthening the Paper" suggestions (scale up experiments, vary layer count) are moved to Nice-to-Haves since they improve but do not invalidate the paper.

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the core findings and limitations.

## Suggestions

1. **Temper the abstract** to match the evidence: replace "increasing model scale will not lead to robust search abilities" with a claim scoped to the tested regime (e.g., "within the range of model sizes tested, increasing width does not alleviate this difficulty").
2. **Add a depth-scaling experiment** — train models with varying number of layers (e.g., 4, 8, 12, 16) on fixed graph sizes and measure whether deeper models can handle larger graphs. This directly tests the path-merging algorithm's predicted bottleneck.
3. **Report sensitivity of the interpretability analysis** to the threshold parameters (α, κ₁, κ₂) and provide a quantitative breakdown of operation classifications.
4. **Acknowledge the limited scope of CoT variants tested** in the abstract and conclusions. Replace "chain-of-thought does not resolve this inability" with "two tested chain-of-thought variants (DFS trace prediction and selection-inference) do not resolve this inability."
5. **Add a control for input length** in the DFS experiment by fixing graph size and varying lookahead, or by controlling padding.
