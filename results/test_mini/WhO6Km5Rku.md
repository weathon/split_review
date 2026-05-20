Now let me write the final consolidated review.

## Summary

QubitCache proposes a KV-cache compression framework that reframes the problem from "which tokens to keep" to "how to preserve attention relationships between tokens." The method retains ~15% of tokens in classical storage while encoding attention patterns of the remaining 85% into 9-qubit amplitude-encoded quantum states (simulated classically). During inference, the compressed tokens' attention weights are reconstructed probabilistically from the quantum states via measurement, creating a hybrid hard+soft attention mechanism. The paper reports 7× memory reduction with 92–97% of baseline performance across multiple models.

## Strengths

- **Paradigm shift from token selection to relational preservation is empirically validated.** The ablation study (Table 4) is the paper's strongest piece of evidence: removing critical tokens (selected by accumulated attention) causes a 20.4% performance drop, while removing position-based heuristics (anchor/recent) degrades only 0.6% each. Random token retention with quantum encoding achieves only 68% of QubitCache's F1 (0.335 vs. 0.491). This cleanly demonstrates that *attention-pattern preservation* drives compression effectiveness, not which specific tokens are retained.

- **7× compression at 92–97% of baseline performance is demonstrated across five models and multiple benchmarks.** Table 1 shows consistent results: e.g., Mistral-7B retains 97.6% of FullKV PG19 performance (0.121 vs. 0.124) and 99.2% of PIQA accuracy (0.904 vs. 0.911). The method also scales to larger models (Table 2: Llama-70B retains 96.9% of baseline).

- **Superior multi-hop reasoning results despite 3.3× more aggressive compression.** On HotpotQA (Table 1), QubitCache at 15% token retention outperforms H2O at 50% retention across all models — e.g., Qwen2-7B: 0.604 vs. 0.487 F1 (24% higher). This supports the claim that preserving relational structure is more important than token quantity for complex reasoning.

- **Comprehensive ablation cleanly separates contribution sources.** The component ablation (Table 4) is well-designed: it isolates the effects of attention-based selection, position heuristics, quantum encoding, and random baselines, allowing the reader to see exactly what drives performance.

## Weaknesses

### Fatal
None.

### Major

- **The quantum framing is oversold relative to the classical implementation.** The abstract claims "logarithmic compression beyond classical information-theoretic limits," but the method is implemented as a classical simulation of a 9-qubit circuit, which requires storing 2⁹ = 512 amplitudes per segment — exactly the same storage as a classical attention distribution of the same size. The memory savings come from token eviction (discarding 85% of KV pairs), not from any quantum storage advantage. The paper acknowledges the classical simulation on line 104, but the rhetorical framing throughout the abstract and introduction implies a fundamentally different compression regime. This mismatch between the claims and the actual implementation undermines the core novelty narrative.

- **No baseline is evaluated at the same compression ratio.** QubitCache operates at 7× compression (15% token retention), while H2O, ScissorHands, and StreamingLLM are evaluated at 2× (50% retention) and GEAR at 6.7× (Table 3). The headline claims of "15-25% higher F1 on multi-hop reasoning" compare methods at different token budgets, making it impossible to determine whether the advantage is due to relational preservation or simply because QubitCache's token-selection heuristic is more effective at the same budget. The paper should evaluate baselines at matched compression ratios (e.g., forcing H2O and StreamingLLM to retain only 15% of tokens) or at fixed performance budgets.

- **Figure 3(b) has an unspecified task and unexplained y-axis scale.** The main text reports the 9-qubit configuration achieving F1=0.531, and Table 4 shows scores around 0.49. Yet Figure 3(b) plots F1 scores ranging from ~0.7 to ~0.85 against circuit depth, and the caption does not specify which dataset or task this corresponds to. The paper says the circuit depth "achieves 103% of baseline performance" — but 103% of what baseline? Without task identification and consistent scaling, the figure's informativeness is compromised.

### Minor

- **PG19 is evaluated with F1 instead of the standard metric (perplexity).** PG19 is a language modeling benchmark; the field standard is perplexity or bits-per-character. Reporting F1 is unusual and makes comparison with existing literature difficult. The paper should either report perplexity or justify why F1 is appropriate for this task.

- **The quantum component contributes only 3.9% to overall performance.** The ablation (Table 4) shows Full QubitCache at 0.491 vs. No Quantum at 0.472. While this is honestly reported, the paper's central narrative heavily features quantum-inspired encoding, yet the evidence suggests the primary driver of performance is the attention-based token-selection heuristic (which is conceptually close to existing methods like H2O). The quantum encoding is a marginal additive improvement.

- **The IDW interpolation (Eq. 6) assumes locality for value reconstruction, while the paper argues that non-local dependencies matter for multi-hop reasoning.** The paper uses inverse-distance weighting between preserved token neighbors to reconstruct the value vectors of compressed tokens. This assumes nearby tokens have similar values, which is a locality assumption — yet the paper's main argument is that preserving non-local attention relationships is essential. While the attention weights themselves come from the quantum state (not the interpolation), the tension between the locality assumption for value reconstruction and the non-locality claim for attention is not addressed.

### Trivial

- The figure caption for the amplitude encoding (Figure 2) gives the formula α_i = 2 arctan(√(w_right/w_left)) without defining w_left and w_right. The hierarchical amplitude encoding procedure is standard in quantum computing but would benefit from an explicit reference or derivation.

## Nice-to-Haves

- Evaluate all baselines at matched compression ratios (e.g., 7×) to enable controlled comparison.
- Report perplexity for PG19 alongside or instead of F1.
- Specify the task/dataset used for Figure 3(b) to resolve the y-axis discrepancy.
- Provide a wall-clock time comparison showing the overhead of the classical quantum simulation vs. direct attention computation.
- Report interpolation error statistics (distance between nearest preserved tokens during reconstruction) to validate the IDW assumption.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Baseline implementations are suspiciously poor" (ScissorHand PG19 F1=0.018 on DeepSeek-Coder).** The paper states that detailed baseline implementations are in Appendix A.1.7 (stripped by the parser), and evaluating baseline correctness without access to the appendix or original published results is not possible from the available text.
- **"Missing details on quantum circuit (α_i formula)."** This is a minor presentation nitpick about figure caption clarity; the hierarchical amplitude encoding procedure is standard and described in the quantum computing literature cited by the paper. The specific formula α_i = 2 arctan(√(w_right/w_left)) is a standard binary-tree amplitude encoding construction.
- **Strawman about IDW contradicting non-local dependency claims.** The IDW interpolation is for value vector reconstruction, while attention relationships (which carry non-local information) are preserved through the quantum state. The paper's claim about non-local dependencies refers to attention, not value interpolation.

## Novel Insights

The reviews surface a tension worth noting: the paper's strongest contribution — empirically demonstrating that attention-pattern preservation matters more than token identity for KV-cache compression — is partially independent of the quantum framing. The ablation study (Table 4) cleanly shows that what matters is how tokens are selected (attention-based vs. random) and whether relational structure is preserved. The quantum encoding is one way to preserve this structure, but the evidence suggests a classical attention-distribution cache could likely achieve similar results at lower complexity. The community might benefit more from the paper's core insight (relational preservation > token selection) if stripped of the quantum apparatus, which adds conceptual overhead without corresponding practical benefit.

## Suggestions

- Substantially tone down the quantum framing. The paper would be stronger as a classical method that stores attention distributions (whether via quantum-inspired amplitude vectors or simple probability tables) to enable soft attention over compressed tokens. The "logarithmic compression beyond classical limits" claim should be removed or reserved for an actual quantum-hardware implementation.
- Add a controlled experiment where H2O and ScissorHands are forced to 15% token retention (7× compression) to enable fair comparison at matched budgets.
- Resolve the Figure 3(b) y-axis discrepancy by clearly labeling the task and metric, or provide a unified scale.
- Report PG19 perplexity alongside F1 for comparability with the language modeling literature.

## Score and Decision

**Anchors for calibration:**

| Anchor | Path | Avg Human Score | Comparison |
|--------|------|----------------|------------|
| DefensiveKV | /home/wg25r/review_agent/human_reviews_2026/nJgS06sX3O.md | 5.60 (Accept Poster) | Cleaner execution, clearer contribution, stronger experiments. QubitCache has a more novel core idea but worse presentation and less rigor. |
| Identify Critical KV Cache | /home/wg25r/review_agent/human_reviews_2026/cZ74yWoKYr.md | 5.00 (Reject) | Mixed reviews; some saw formal contribution, others found it heuristic. QubitCache has stronger core insight but similar methodological concerns. |
| Pitfalls of KV Cache Compression | /home/wg25r/review_agent/human_reviews_2026/dDgoYv2f7Q.md | 4.00 (Withdrawn/Reject) | Both address real KV cache limitations. QubitCache has more extensive experiments but also more severe framing issues. |
| CompressKV | /home/wg25r/review_agent/human_reviews_2026/Eed6XsFNJ5.md | 3.50 (Withdrawn/Reject) | Methodological concerns about head identification. QubitCache has a more novel core idea but similar experimental gaps. |
| Quantum Attention | /home/wg25r/review_agent/human_reviews_2026/i75XGv8oqj.md | 2.00 (Withdrawn/Reject) | Purely theoretical, no experiments, impractical assumptions. QubitCache has actual experiments and empirical validation. |
| Quantum ML Advantages | /home/wg25r/review_agent/human_reviews_2026/on2lie43Kl.md | 6.00 (Accept Poster) | Rigorous theoretical paper with clear contributions. QubitCache targets a different type of contribution (empirical systems) and is less rigorous. |

QubitCache falls between the KV-cache rejection anchors (~3.5–4.0) and the accepted KV-cache papers (~5.5+). Its core insight is genuinely interesting and underexplored, and the ablation study provides real evidence. However, the oversold quantum framing, lack of controlled baseline comparisons, and figure quality issues prevent it from meeting the bar of an accepted paper in its current form. The paper's best evidence (relational preservation matters) could form the basis of a stronger submission if reframed honestly.

**Final Score:** 3.5/10

**Decision:** Reject

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>