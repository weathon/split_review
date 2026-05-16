Now I have a thorough understanding of the paper and can verify each reviewer claim against the actual text. Let me compile the final review.

---

## Summary

This paper analyzes the ability of message-passing GNNs to count graph substructures (cycles, cliques, quasi-cliques, connected components) by studying GNNs with random node inputs. It shows that proper choices of activation (polynomial powers) and normalization (expectation) generate node features corresponding to statistical moments, which are then shown to count substructures. The analysis is constructive, leading to the Moment-GNN architecture that achieves strong empirical results on cycle detection (100% accuracy for 4-,6-,8-cycles), cycle counting on ZINC (MAE ~10⁻³), state-of-the-art logP prediction (MAE 0.055), and graph classification.

## Strengths

- **Constructive architecture with strong empirical validation.** The Moment-GNN (based on the closed-form expression in Equation 14) achieves 100% accuracy on cycle detection for 4-,6-,8-cycles across all tested graph sizes, outperforming seven baselines including RP and PPGN. On ZINC logP prediction, Moment-GNN achieves MAE 0.055 (with edge features), surpassing the previous best (GSN with cycle features, 0.108) — and does so without precomputed substructure counts. These results demonstrate that the polynomial moment features translate into practical gains.

- **Novel analysis linking GNN outputs to high-order moments of the node representation distribution.** The paper systematically studies how elementwise square, cubic, and quartic activations combined with expectation normalization yield features corresponding to variance, skewness, and kurtosis of the GNN output. Proposition 5.1 provides a general closed-form expression (Eq. 14) for multi-layer GNNs with polynomial activations, unifying the analysis across all moment orders.

- **Demonstrates that the GNN can count cycles up to size 8 and generalize to arbitrary graphs.** Theorems 4.2–4.5 and 6.3 claim existence of a GNN that counts cycles of sizes 3–5, 6, 7, and 8, with Remark 4.6 emphasizing that this holds for *any* graph, not just the training distribution — a generalization guarantee.

- **Strong performance on multiple diverse tasks.** The approach is evaluated on four distinct tasks (cycle detection, cycle counting, graph classification, molecular property prediction), showing versatility beyond the specific theoretical claims.

## Weaknesses

### Fatal
None.

### Major

- **The random-input distribution used in the theoretical derivations is not a valid probability distribution.** The paper assumes i.i.d. node features with 𝔼[xᵢ]=0, 𝔼[xᵢᵖ]=1 for all p≥2, and gives a characteristic function ϕ(t)=e^{j t}−j t. These conditions are mathematically inconsistent: 𝔼[xᵢ²]=1 and 𝔼[xᵢ⁴]=1 together imply xᵢ²=1 almost surely, which forces xᵢ∈{+1,−1} and hence 𝔼[xᵢ³]=0≠1, contradicting the requirement that all moments beyond the first equal 1. The characteristic function is also not valid (|ϕ(t)| grows unbounded for large t, violating the necessary |ϕ(t)|≤1 property of characteristic functions). This undermines the rigorous probability-theoretic framing of Sections 3–6. **However**, the actual Moment-GNN architecture (Section 7.1) is deterministic and uses the closed-form expression in Equation 14 directly — it does not sample random inputs. The practical architecture and its empirical performance are not affected by this flaw, but the paper's central theoretical claim that "*a GNN operating on a random input* can count substructures" rests on an unsound foundation as presented. The paper should either provide a valid random variable with the needed moment properties, or reframe the theory as formal algebraic manipulations without invoking probability.

- **Experiments do not test all claimed substructures.** The paper makes theoretical claims for counting cycles of sizes 3–8, 4-node cliques, quasi-cliques, and connected components. Yet the experiments only test: cycle detection for lengths 4, 6, 8 (Table 1); cycle counting for pentagons and hexagons on ZINC (Table 3a); and logP prediction (which does not directly test any counting capability). There are no experiments validating the counting of 3-cycles, 5-cycles, 7-cycles, 4-node cliques, quasi-cliques, or connected components. While the theoretical proofs are deferred to the appendix and cannot be assessed here, the empirical gap between what is claimed and what is tested is noticeable.

### Minor

- **Expressivity claims about the FWL test are not adequately justified.** Proposition 5.2 claims the GNN is "strictly more powerful than 1-FWL," and Section 6 is titled "Beyond 2-FWL." Proposition 6.1 states that there exist substructure families where 2-FWL is no stronger than the described GNN. However, the paper does not substantiate what 1-FWL or 2-FWL can or cannot count, nor does it engage with known expressivity results for these tests. The claim of breaking 2-FWL limits is asserted rather than argued from prior literature or explicit analysis, making this portion of the contribution difficult to evaluate.

- **No computational complexity analysis of Moment-GNN.** The architecture involves Hadamard products of powers of the adjacency matrix (Sᵏ ⊙ Sᵐ), which can be expensive for large graphs. The paper notes that baselines like RP and PPGN have higher complexity, but does not provide its own complexity analysis (e.g., scaling with graph size N, maximum degree, filter order K). This limits assessment of practical applicability to large graphs.

- **The architecture-to-theory gap is not addressed.** The theory proves *existence* of specific filter parameters that yield cycle counts, while the architecture uses *learnable* parameters. The paper does not analyze whether training can recover the desired parameters, study the optimization landscape, or provide any learning-theoretic guarantees. This weakens the connection between the theoretical existence result and the empirical performance.

### Trivial
None.

## Nice-to-Haves

- Ablation study to isolate the contribution of the Moment layer (e.g., compare Moment-GNN vs. a GIN-only baseline on logP prediction).
- Sensitivity analysis of hyperparameters (number of moments, maximum filter order K, number of filters Fₘ).
- Out-of-distribution experiments beyond Table 2 (which lacks clear explanation of the IID vs. OOD setup).
- Discussion of prior polynomial graph filters (ChebNet, GPR-GNN, ARMA) in related work.

## Removed Points

These points are flagged to be removed — treat them with caution:
- **Criticism that the characteristic function "does not satisfy φ(0)=1":** This is factually wrong — φ(0) = e^{j·0} − j·0 = 1. The characteristic function does satisfy φ(0)=1, though other validity issues remain (see Major weakness above).
- **Complaints about missing proofs in the appendix:** The appendix was stripped by the parser; proofs exist in the original submission per venue formatting conventions.
- **Table 5 (REDDIT) appearing empty in extracted text:** This is a parser artifact — the table is an image in the original PDF; no judgment can be made about its content.
- **"No experiments on cliques/quasi-cliques/connected components" as an isolated complaint:** Kept as part of the broader experiment-theory gap, but the stronger version claiming results are entirely absent is softened above.
- **Missing related works:** Per instructions, the reviewer cannot confirm existence of unmentioned works.
- **Formatting nitpicks and stylistic complaints:** These are parser artifacts or matters of taste, not author errors.

## Novel Insights

The most interesting observation emerging across the reviews is the disconnect between the paper's theoretical framing (which invokes random inputs and probability to derive moment-based features) and its deterministic implementation (which directly computes polynomial features of the adjacency matrix). This tension suggests that the paper's real contribution may be better understood as a principled polynomial filter design — one that systematically constructs expressive substructure-counting features via Hadamard products of adjacency powers — rather than as a stochastic analysis of GNNs. Reframing the contribution along these lines would both fix the theoretical validity issue and more honestly represent what the architecture actually does.

## Suggestions

1. **Overhaul the theoretical framing in Section 3.** Either (a) drop the random-input pretense entirely and directly define the moment features as deterministic polynomial functions: y_f = Σ h_{i₁,…,iₙ} (S^{i₁}⊙…⊙S^{iₙ})1, or (b) construct an explicit valid random variable that satisfies the needed moment conditions (or prove that a valid distribution with 𝔼[x]=0, 𝔼[xxᵀ]=I, 𝔼[x∘x∘x]=I exists). The current middle ground — claiming a random input that cannot exist — undermines rigor.

2. **Directly test the claimed counting capabilities.** Provide experiments where Moment-GNN is trained to predict exact counts of 3-,5-,7-cycles, 4-node cliques, and quasi-cliques on synthetic graphs with ground-truth counts. This would close the gap between the theoretical claims and the empirical evaluation.

3. **Substantiate the FWL expressivity claims.** Either cite known results showing that 1-FWL/2-FWL cannot count the substructures in question, or provide a brief combinatorial argument. Currently the paper asserts superiority without engaging with the existing FWL literature on substructure counting.

4. **Add a computational complexity analysis.** Characterize the cost of computing Sᵏ⊙Sᵐ terms as a function of N, degree, and K, and discuss when this becomes prohibitive.

5. **Include a control/ablation experiment.** Replace the Moment layer with a linear layer of equivalent output dimension in the logP prediction task to verify that the structured moment features — not merely extra parameters — drive the performance gain.

## Score and Decision

**Originality:** 6/10 — The idea of using polynomial activations to generate moment-like features is novel, though the random-input framing is a well-known trick (previously used in Abboud et al., Sato et al.).

**Importance of research question:** 8/10 — Understanding what GNNs can and cannot count is a core problem in graph representation learning.

**Claims support:** 4/10 — The theoretical claims are weakened by the invalid random-input assumption, and the experiments do not cover all claimed substructures.

**Soundness of experiments:** 6/10 — The experiments that are present are well-designed and show strong results, but key ablations and coverage are missing.

**Clarity of writing:** 6/10 — The paper is generally well-structured, but the theoretical derivations rely on mathematically questionable assumptions.

**Value to community:** 6/10 — The Moment-GNN architecture and the idea of polynomial moment features are valuable, but the theoretical baggage needs cleanup.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>