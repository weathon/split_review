Now let me run the calibration search — bracketing pass first.**Round 1 bracket:** Based on the retrieved anchors, the paper sits between **5.5 and 7.5**. It's stronger than the rejected fractal-nodes paper (5.5) due to more rigorous theory and broader experimental scope, likely comparable to the oversmoothing-theory paper (7.0). Let me narrow within [5.5, 7.5].Now I have sufficient data to write the full review. Let me compile everything based on the paper reading and calibration.

---

## Summary
FROND replaces integer-order derivatives with Caputo fractional derivatives of order β ∈ (0,1] in continuous GNN frameworks, enabling memory-dependent (non-Markovian) feature dynamics. The paper's central theoretical contribution is proving that F-GRAND-l converges to its stationary distribution at an algebraic rate Θ(t⁻ᵝ) versus the exponential rate of integer-order models (Theorem 2), which is validated experimentally as oversmoothing mitigation up to 128 layers. The framework is applied to five existing integer-order continuous GNNs (GRAND, GRAND++, CDE, GREAD, GraphCON) and evaluated across ten node-classification datasets, consistently improving over the integer-order baselines.

---

## Strengths

- **Non-Markovian random walk interpretation with explicit memory mechanism (Theorem 1, Eq. 10):** The paper constructs transition probabilities that explicitly depend on the walker's entire path history via coefficients c_k and b_n (Eq. 10), and proves (via the technique of [gorenflo2002time]) that the continuous limit satisfies the fractional diffusion equation (Eq. 12). The limiting case β→1 recovers the Markovian walk exactly (Eq. 14). This gives a concrete, interpretable mechanism for the memory effects in FROND — not merely a substitution of a derivative symbol.

- **Algebraic convergence theorem directly validates oversmoothing claim (Theorem 2, §3.2.1, Figure 1):** The proof that ‖P(t)−πᵀ‖₂ ~ Θ(t⁻ᵝ) contrasts sharply with the exponential O(e⁻ʳᵗ) rate for integer-order models, and the experiment in Figure 1 shows F-GRAND-l maintaining essentially constant accuracy up to 128 layers on Cora and Airport while GRAND-l degrades significantly. The theory-experiment coupling here is the clearest evidence in the paper.

- **Consistent and large gains on tree-structured datasets (Table 1):** F-GRAND-l achieves 98.1%±0.2 on Airport vs. GRAND-l at 80.5%±9.6 (+17.6 pp) and 92.4%±3.9 on Disease vs. GRAND-l at 74.5%±3.4 (+17.9 pp). These large and consistent margins on fractal-structured data provide the most striking evidence that β < 1 captures something structurally meaningful about such graphs, not just a tuning artifact.

- **Demonstrated generality across five base architectures (Tables 2, appendix):** FROND is applied to F-GRAND, F-GRAND++, F-CDE, F-GREAD, and F-GraphCON. F-CDE improves on CDE on 5 of 6 large heterophilic datasets (Table 2), with Questions (β=1.0 optimal, identical score of 75.17%) correctly confirming the fallback behavior. This positions FROND as a framework rather than a one-off adaptation.

- **β ablation connects fractional order to graph topology (Table 3):** Tree-structured Airport prefers small β (0.1) with accuracy 97.09%, while citation-graph Cora prefers large β (0.9) with accuracy 82.68%. This monotonic relationship between β and dataset structure provides direct empirical grounding for the fractal-structure motivation.

---

## Weaknesses

### Fatal
None.

### Major

- **The β-tuning advantage is not disentangled from the fractional-dynamics mechanism.** The central empirical claim is that non-Markovian dynamics *per se* are beneficial. However, since GRAND is a special case of F-GRAND at β=1, F-GRAND is guaranteed to match or exceed GRAND whenever β is selected on a held-out validation set — not because the memory mechanism helps, but simply because GRAND lies within the search space. The paper itself acknowledges: "Consistent with our expectations, F-GRAND surpasses GRAND across nearly all datasets, *given that GRAND represents a special case of FROND with β=1*" (§4.1). This framing implicitly concedes the point. The results are equally consistent with the hypothesis that any additional scalar hyperparameter (e.g., a tunable integration time T applied to standard GRAND) would yield comparable gains. An ablation comparing F-GRAND with a fixed, uniform β (e.g., β=0.9 across all datasets) against GRAND would separate mechanism benefit from tuning benefit and is absent from the paper.

- **Computational overhead analysis is deferred to the appendix while all main experiments use the full-memory predictor.** The basic predictor (Eq. 7) at step k requires storing and evaluating F(W, X^(j)) for all j < k, making it O(K) times more expensive per iteration than the Euler step in GRAND. The paper notes that computational complexity is analyzed in §subsec:supp_computetime (appendix) and that the short-memory variant exists (Figure 1 right panel, §3.3), but all main-paper experiments use the full-memory predictor. Given that gains on several datasets are modest (CoauthorCS: 92.9%→93.0%, ogbn-arxiv: 71.9%→72.6%), practitioners cannot assess the cost-benefit tradeoff without this information in the main text.

### Minor

- **Theory-practice gap: Theorem 2 applies to F-GRAND-l, but the highlighted models often include nonlinear variants.** The algebraic convergence proof and the oversmoothing experiment (§4.3) are both for F-GRAND-l (the linear, fixed-attention variant). F-GRAND-nl and all other extended models (F-CDE, F-GREAD) involve time-varying nonlinear operators for which the convergence analysis does not directly carry over. The paper does not argue, even informally, that algebraic convergence holds in the nonlinear regime. The abstract and introduction state oversmoothing mitigation broadly; this should be scoped to the linear variant where it is proven.

- **Discrepancy between Table 1 and Table 3 on Cora.** Table 3 (β sensitivity, T=8) shows F-GRAND-l at β=0.9 achieving 82.68%±0.64 on Cora, while Table 1 reports 84.8%±1.1 for F-GRAND-l with the same β=0.9. The difference presumably reflects a different integration time T in Table 1, but this is not stated in the main text. Readers comparing the β ablation to the main results cannot interpret the gap.

### Trivial
None.

---

## Nice-to-Haves

- **Fixed-β ablation:** Setting β=0.9 uniformly across all datasets (eliminating dataset-specific tuning) and comparing against GRAND would directly show whether the fractional mechanism itself — not just the extra degree of freedom — drives improvements.
- **Quantitative fractality–β correlation:** Even a simple scatter plot correlating optimal β with an independently computed graph property (estimated fractal dimension, average path length, or degree distribution exponent) across the 10 datasets would sharpen the paper's most distinctive conceptual claim.
- **Clarify β as hyperparameter vs. learned parameter:** The statement "without introducing any additional training parameters to the backbones" (§4.4) is technically accurate but could confuse readers — β is a continuous hyperparameter tuned via grid search. A single sentence clarifying that β is grid-searched (not gradient-learned) would prevent misreading.
- **Main-paper runtime figure:** A simple wall-clock comparison of F-GRAND (short-memory variant) vs. GRAND, showing comparable gains at a fraction of the cost, would make the practical case clear.

---

## Removed Points

*These points are flagged for removal; treat with caution.*

- **"The random walk interpretation overstates generality because it depends on a specific discretization" (Harsh critic):** The paper explicitly constructs the walk in the discretized-time domain (step size σ, Theorem 1) and proves it converges to the FDE in the limit n→∞, nσ=t. Theorem 1 is a statement about a specific but well-defined discretization scheme (not a hand-wavy claim about F-GRAND-l in general), and this is standard practice in deriving continuous limits of random walks. The paper is appropriately scoped. REMOVED — not a valid criticism.

- **"Questions dataset result would be strengthened by non-continuous-GNN baselines" (Harsh critic):** The paper's stated aim is "not to achieve state-of-the-art results, but rather to demonstrate the additional effectiveness of the FROND framework when applied to existing integer-order continuous GNNs" (§4 intro). Demanding broader heterophilic landscape baselines is outside the paper's explicitly declared scope. REMOVED as a weakness; noted as a nice-to-have.

- **"Statistical significance is unclear due to high variance on Airport/Disease" (Harsh critic):** This is a generic concern not attached to a specific claim that is actually invalidated by the variance. On Airport, F-GRAND-l achieves 98.1%±0.2 vs. GRAND-l's 80.5%±9.6 — a 17.6 pp margin that is significant at any reasonable threshold. For Disease, F-GRAND-l at 92.4%±3.9 vs. GRAND-l at 74.5%±3.4 similarly withstands variance concerns. REMOVED.

- **"Fractal motivation is stated with overconfidence; β correspondence to fractality is unvalidated" (Harsh critic):** The fractal motivation is presented with appropriate hedging ("can pave the way," "potentially unearth insights," §1). The paper does not claim β IS the fractal dimension — it suggests a potential connection consistent with Table 3 results. This is moved to Nice-to-Haves. REMOVED as a weakness.

- **Strength: "Generality demonstrated by extending five different architectures."** Kept — this is specific and concrete, tied to Table 2 and appendix results.

---

## Novel Insights

The paper's most distinctive conceptual contribution — beyond technical execution — is the suggestion that the fractional order β could serve as an implicit *graph characterization tool*: the optimal β tracks the dataset's topological structure, with hierarchical/fractal graphs (Airport, Disease) preferring small β (heavy memory) and citation networks preferring large β (near-Markovian). This connection between a dynamical parameter and an intrinsic graph property is independently interesting and is grounded in the well-established correspondence between fractional diffusion equations and anomalous transport on fractal media. If validated with independent measurements of fractality (e.g., box-counting dimension), this would reframe FROND not merely as a performance-enhancement toolkit but as a graph analysis instrument.

---

## Suggestions

1. Add a fixed-β ablation (e.g., β=0.9 fixed uniformly) to disentangle mechanism benefit from tuning benefit — this is the single most important revision.
2. Include a runtime table or figure in the main paper comparing F-GRAND (full memory) and F-GRAND (short memory) against GRAND in terms of wall-clock time and performance.
3. Clarify the Cora discrepancy between Tables 1 and 3 by stating the integration time T used in each experiment.
4. Scope the oversmoothing claim in abstract/introduction to F-GRAND-l where the algebraic convergence is proven; note informally for nonlinear variants.

---

## Score and Decision

**Calibration Summary — All Retrieved Anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| S3zKrEQpRr (GNN noisy channel) | 3.00 | R1 | Clearly weaker — no theoretical contributions comparable to FROND |
| zuuhtmK1Ub (Implicit PDE solver GNN) | 2.00 | R1 | Much weaker |
| xA25Ib7H8U (Ricci flow continuous-depth) | 2.33 | R1 | Much weaker |
| zPoW8CajCN (Fractal-inspired MPNNs) | 5.50 | R1/R2 | Weaker — no formal theory, less rigorous experiments |
| za9tj3izLn (Opinion dynamics GNN) | 4.33 | R2 | Weaker |
| i8vPRlsrYu (Residual connections prevent oversmoothing) | 7.00 | R1 | Comparable — rigorous theory+experiments; FROND is slightly weaker due to β-attribution gap |
| NLbRvr840Q (Hypergraph Dynamic System) | 6.00 | R1/R2 | Weaker — theoretical errors in stability analysis found by reviewers; FROND's theory is cleaner |
| l6eA8Srlqd (Long-range C-TDG propagation) | 5.50 | R2 | Weaker — less rigorous theory |
| duGygkA3QR (GNNs + DMD) | 6.60 | R2 | Comparable — similar profile; FROND's theory (new random walk, algebraic convergence) is more original |
| 03EkqSCKuO (Port-Hamiltonian GNNs) | 7.00 | R2 | Comparable — novel dynamics framework, theory+empirics, accepted with "incremental novelty" criticism; FROND has similar profile with additional β-attribution weakness |
| 7b2JrzdLhA (Graph Neural Ricci Flow) | 6.00 | R2 | Comparable in structure; FROND has more novel mathematics (fractional calculus is less explored in GNNs than curvature) |
| mkNVPGpEPm (Associative memory + ODEs) | 6.67 | R2 | Comparable scope and rigor |

**Round 1 bracket:** 5.5–7.5.

**Round 2 narrowing:** FROND is stronger than the 6.0 papers (HDS, Ricci flow) because its theoretical contributions are more original and its theory contains no identified errors. FROND is comparable to duGygkA3QR (6.60) in scope but has more original theory. The 7.0 papers (Port-Hamiltonian, residual oversmoothing) are the ceiling comparators — FROND has comparable depth, but the β-attribution gap and absent computational analysis are real methodological concerns that the 7.0 papers do not share to the same degree. This places FROND at **6.5** — clearly above the 6.0 floor, meaningfully below the 7.0 ceiling.

**Axes summary:**
- *Originality:* Good — fractional calculus in continuous GNNs is novel; the non-Markovian random walk construction is a genuine original contribution.
- *Importance of research question:* Good — oversmoothing in deep GNNs and memory-dependent dynamics are active problems.
- *Claims well-supported:* Moderate — the theoretical claims are proven for F-GRAND-l; the empirical claim that memory mechanism drives improvement is conflated with tuning benefit.
- *Soundness of experiments:* Good — broad coverage across 10 datasets and 5 models; honest reporting of null results (Questions dataset).
- *Clarity of writing:* Good — well-structured, logical progression from theory to experiments.
- *Value to research community:* Good — a general framework that can be applied to any continuous GNN as a drop-in enhancement.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>