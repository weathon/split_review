## Summary

RADAR proposes a neural framework for solving asymmetric vehicle routing problems by combining two complementary components: (1) an SVD-based initialization that produces compact, generalizable node embeddings encoding static directional asymmetry from the distance matrix, and (2) Sinkhorn-normalized attention that replaces row-wise softmax to model dynamic asymmetry during encoding. The paper evaluates RADAR across 17 synthetic and 3 real-world VRP variants, demonstrating consistent outperformance over prior neural solvers on both in-distribution and out-of-distribution instances, with particularly strong size-generalization results (e.g., ATSP1000 gap of 4.13% vs. 7.24+% for competitors).

## Strengths

- **Principled SVD initialization with theoretical grounding**: The paper defines *asymmetry-aware embeddings* (Definition 1) and proves the SVD-based construction satisfies this property via Equation (5), showing that the concatenated embedding can reconstruct the asymmetric distance matrix through two distinct linear projections. This provides a non-trivial theoretical justification for why the initialization captures static directional information, going beyond ad-hoc embedding schemes.

- **Comprehensive and convincing empirical evaluation**: RADAR is tested on a broad spectrum — synthetic ATSP/ACVRP at sizes 100–1000 (Table 1), 16 multi-task asymmetric VRP variants (Table 2), and 3 real-world datasets with in-distribution and out-of-distribution shifts (Table 3). It outperforms all neural baselines in nearly every setting, including strong recent methods like ReLD and RRNCO. The out-of-distribution generalization from size-100 training to size-1000 testing is particularly strong and well-supported.

- **Clean ablation isolating each component's effect**: Table 6 cleanly separates the contributions of SVD initialization and Sinkhorn normalization across four instance sizes. Adding Sinkhorn improves the ATSP1000 gap from 7.24% to 4.13%, and the combination of both components produces the best result. The ablation of alternative SVD variants (EVD, MDS, QR — Appendix D.2) and the rank parameter study (Figure 3, Section 6.1) provide thorough design justification.

- **Practical robustness demonstrated on real-world data**: On three real-world benchmarks (Table 3), RADAR consistently outperforms the strongest baseline RRNCO across all distribution settings, and Table 4 shows RADAR without coordinate information still beats RRNCO *with* coordinate augmentation — a strong signal that the distance-matrix encoding captures meaningful structural signal independent of geometric priors.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Overclaimed mechanism for Sinkhorn normalization**: Section 4.2 states that Sinkhorn "ensures that each attention score \(A_{i,j}\) reflects a more complete characterization … by incorporating the full set of distance-based relations directly connected to them." Sinkhorn operates on already-computed attention logits (which include \(D_{i,j}\) and \(D_{j,i}\)) and enforces a doubly stochastic constraint through iterative row/column normalization. While column normalization does couple \(j\)'s neighborhood context into \(A_{i,j}\) indirectly, the phrase "full set of distance-based relations" overstates what is mechanistically happening. The empirical gains from Sinkhorn are real and well-demonstrated, but the explanatory framing — why it works rather than just that it works — would benefit from either tempering the language or adding a diagnostic analysis (e.g., attention-matrix visualization, Frobenius distance to the original distance matrix under softmax vs. Sinkhorn). This does not threaten the core contribution.

- **No variance or stability information in results**: All tables report mean objective values over 1,000 test instances without standard deviations, confidence intervals, or interquartile ranges. Some performance margins are modest (e.g., ~0.9% gap between RADAR and ReLD on ATSP100), and the reader cannot gauge whether these differences are reliable above instance-level noise. While reporting only means is standard practice in the NCO literature, including variance would substantially strengthen an otherwise strong empirical case.

### Trivial

- The paper lacks a dedicated Limitations section. The conclusion gestures at future work but does not examine assumptions such as the low-rank requirement of SVD or computational bottlenecks at extreme scales.

## Nice-to-Haves

- A diagnostic study (e.g., attention matrix visualization with and without Sinkhorn, or measuring how well the effective attention approximates the original distance structure under each normalization) would ground the Sinkhorn interpretation and elevate the conceptual contribution beyond "it works."

- A brief acknowledgment of scenarios where SVD-based initialization may be challenged (e.g., when the distance matrix is not well-approximated by a low-rank factorization) would demonstrate awareness of scope.

## Removed Points

These points were flagged by reviewers but are removed from the final review with justification:

- *"Sinkhorn does not inject any additional structural information beyond what is already present in the logits"* — This is partially incorrect. The Sinkhorn column normalization step does indirectly couple \(j\)'s neighborhood context into \(A_{i,j}\) through iterative row/column rebalancing, since column normalization makes each \(A_{i,j}\) depend on how other nodes attend to \(j\). The claim is about degree of overstatement, not factual error. Retained as a Minor weakness with tempered language.

- *"Definition 1 is very close to a restatement"* — This is a methodological judgment, not a factual error. The definition serves a clear purpose in formalizing what asymmetry-aware embeddings should achieve, and the SVD construction is demonstrably shown to satisfy it. Not a weakness.

- *"Missing comparison with additional baselines"* — The harsh critic did not raise this, but the strength finder notes thorough baselines. The paper compares against LKH, HGS, MatNet, ICAM, ELG, ReLD, UNICO, GLOP, UDC, RRNCO, and adapted RouteFinder variants. Coverage is comprehensive for this subfield. Removed.

- *Absence of confidence intervals for efficiency analysis* — The harsh critic flagged missing variance, which is retained as Minor. But the strength finder's claim about "modest margins" being "unreliable" is speculative — the margin on ATSP200 is 1.01% vs. 3.75% for the next-best neural solver, which is not a borderline result. Removed the speculative framing.

- *"The paper is silent on masking interaction with Sinkhorn"* — The harsh critic noted this and immediately retracted it, since Sinkhorn is used only in the encoder (no masking needed). Removed.

## Novel Insights

The paper's framing of asymmetry into *static* (distance-matrix-level) and *dynamic* (attention-level) components is a useful conceptual decomposition that organizes the solution design clearly. More concretely, the finding that SVD-based initialization enables strong out-of-distribution generalization without coordinate cues (Table 4 shows RADAR without coordinates outperforms RRNCO *with* coordinate augmentation) suggests that low-rank spectral structure in distance matrices may encode sufficient topological signal to replace geometric priors — an insight with implications beyond VRP to other relational-learning tasks where only pairwise asymmetric features are available.

## Suggestions

- Soften the Sinkhorn interpretation in Section 4.2: replace "full set of distance-based relations" with language that accurately reflects doubly stochastic normalization, e.g., "enforcing balanced row and column attention scores so that \(A_{i,j}\) is informed by both how \(i\) attends to its neighbors and how other nodes attend to \(j\)."

- Add standard deviations or interquartile ranges to the main result tables (Tables 1–3), even if placed in the appendix with a one-sentence note in the main text.

- Add a brief Limitations paragraph in the conclusion noting assumptions (low-rank SVD, moderate instance sizes for SVD overhead).

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| SrnTGdJKYG (Neural Deconstruction Search) | 3.00 | R1 | RADAR is **far stronger** — more novel, more comprehensive, real-world evaluation |
| iWCfiDxLIY (GREAT architecture) | 3.00 | R1 | RADAR is **far stronger** — cleaner method, far better evaluation, stronger results |
| CFLEIeX7iK (Neural Solver Selection) | 5.75 | R2 | RADAR is **stronger** — more novel contribution, more comprehensive experiments |
| yEwakMNIex (RedCO / Unified Neural Solvers) | 6.25 | R1 | RADAR is **stronger** — better real-world evaluation, cleaner methodology, stronger generalization |
| TbTJJNjumY (Boosting NCO for Large-Scale VRPs) | 6.25 | R1 | RADAR is **comparable in quality** — both have strong empirical results; RADAR has more comprehensive ablation and real-world testing |
| GM7cmQfk2F (Neat Weight Embedding for MOCO) | 7.00 | R2 | RADAR is **comparable, slightly stronger** — similar level of novelty and comprehensiveness; RADAR has stronger real-world evaluation and theoretical grounding |

**Round-1 bracket**: 5.5–7.5. **Round-2 narrowing**: Anchors at 5.75 and 7.00 confirm RADAR sits near the upper end. The paper is clearly stronger than the 5.75–6.25 range (more comprehensive evaluation, stronger theoretical grounding) and comparable to the 7.00 anchor, with an edge in real-world applicability and ablation depth. The Sinkhorn overclaim and missing variance are minor issues that do not diminish the strong empirical contribution. Score: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>