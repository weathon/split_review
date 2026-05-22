## Summary

This paper introduces INFO-SEDD, a method for estimating Kullback-Leibler divergence and mutual information (MI) on discrete data using Continuous Time Markov Chains (CTMCs). The key idea is to derive a KL estimator via Dynkin's formula (Equation 5) that leverages score functions from discrete diffusion models, and to show that with an absorbing-state rate matrix, a single score model trained on the joint distribution suffices for both joint and marginal scores (Equation 6). The method is evaluated on synthetic benchmarks, text summarization consistency and model selection, and DNA motif discovery in genomics.

## Strengths

- **Novel theoretical framework connecting CTMCs to KL estimation.** The derivation via Dynkin's formula (Section 2.2, Equation 5) is a principled and original approach that is the first to bridge CTMC-based discrete diffusion score models and information estimation without relying on continuous embeddings.
- **Single-model marginal computation via absorbing-state diffusion.** Section 3 (Equation 6) proves that with an absorbing-state rate matrix, a score model trained only on the joint distribution yields marginal scores, eliminating the need to train separate models for joint and marginals — a practical bottleneck for embedding-based approaches.
- **Strong synthetic benchmark results.** Table 1 shows INFO-SEDD produces estimates within 0.08–2.23 nats of ground truth across MI values 10–50 and dimensions 10–50, while all competitors (GAN-DIME, HD-DIME, KL-DIME, MINDE, MINE, NWJ, SMILE) deviate substantially, particularly at higher MI values.
- **Informative real-world applications on two discrete data domains.** The text summarization consistency test (Figure 1) shows INFO-SEDD tracking the 256ρ–303ρ reference range more closely than any competitor, and the DNA motif discovery experiment (Figure 5) demonstrates a concrete practical use case. The genomics low-MI consistency test (Figure 4) serves as a successful sanity check where the method correctly reports near-zero MI at ρ=0.
- **Useful downstream signal for summarization model selection.** Table 2 shows INFO-SEDD-C achieves Pearson r = 0.740 with human consistency scores, substantially higher than KL-DIME (0.214), HD-DIME (0.331), and SMILE (–0.074), suggesting the MI estimates carry meaningful information.

## Weaknesses

### Fatal
None.

### Major
- **The ρ=0 bias in the text consistency test (Figure 1) is not adequately explained.** INFO-SEDD reports MI ≈ 100 nats at ρ=0 (randomly paired text and summary), while the empirical derivation lines (256ρ–303ρ) imply near-zero MI at ρ=0. The paper acknowledges this in passing ("INFO-SEDD-C obtains MI estimates closer to zero than the joint variant, when ρ=0.0") but provides no explanation for the systematic offset. Although the "Empirical MI estimate" (grey line) exhibits a similar ~100-nat bias, the paper never defines what this estimate is, so the reader cannot judge whether the shared bias reflects a methodological limitation of INFO-SEDD or a genuine property of the data. This does not invalidate the core claim (the linear trend is what matters for the consistency test, and the genomics low-MI experiment in Figure 4 shows clean near-zero behavior), but it undermines the paper's assertion that the estimates "closely match the empirical derivation" — they match in slope but not in absolute value.

### Minor
- **Model selection experiment lacks comparison against standard summarization metrics.** The paper frames the SUMMEVAL analysis (Table 2, Figures 2–3) as demonstrating that MI is useful for model selection, but only compares against other MI estimators (KL-DIME, HD-DIME, SMILE). A meaningful assessment of whether MI is practically useful for model selection would require comparison with standard automatic metrics (e.g., ROUGE, BERTScore) or simple baselines (e.g., summary length, perplexity). A Pearson r of 0.74 with consistency is notable, but without context relative to existing metrics, the practical value of this signal is unclear.
- **No runtime or computational cost analysis despite scalability claims.** The paper claims scalability but does not report wall-clock time, number of score function evaluations, or training cost for INFO-SEDD versus competitors. The per-MC-step sum over all |χ| vocabulary candidates in Equation (5) is a practical concern for large vocabularies (e.g., 10k–50k tokens) that is acknowledged only in the structural decomposition discussion but not benchmarked.

### Trivial
- The theoretical error bound (Equation 7) depends on constants C₁, C₂, εₚ, ε_q that are not empirically quantified, making the bound a conceptual statement rather than a practical diagnostic. A brief empirical illustration on synthetic data would strengthen this contribution.

## Nice-to-Haves
- A negative control experiment where ground-truth MI is known to be exactly zero (e.g., independent random sequences of the same length) could further validate the estimator's calibration.
- Convergence plots showing how the Monte Carlo estimate stabilizes with the number of time steps would help practitioners understand the estimator's variance.
- An ablation quantifying the effect of vocabulary size on computation time would substantiate the scalability claim.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"No discrete-aware MI baselines"** (Harsh Critic Critical Issue 2): The paper explicitly scopes itself to high-dimensional discrete data (D=10–50, MI=10–50) where classical plug-in and shrinkage estimators are well known to fail (the paper cites Pinchas et al. (2024) on this point). The inclusion of such baselines would be uninformative and potentially misleading at the scales studied. The comparison against state-of-the-art neural estimators that use the "embedding trick" is appropriate for the paper's stated contribution.
- **"Synthetic data generation not in main text"**: Appendix C.1 is the standard place for such details; this is common practice and not a weakness.
- **"Missing negative control" (Harsh Critic)**: The paper does in fact include a negative control — the genomics experiment (Figure 4) where INFO-SEDD-C shows near-zero MI at ρ=0, validating the estimator in a low-MI regime.
- **"Synthetic results suspiciously clean"**: Table 1 reports standard deviations over 10 seeds, the trend is monotonic, and the estimator is directly computing KL via the diffusion score rather than fitting a variational bound — clean results are expected and internally consistent.
- **"Error bound should be empirically validated"**: While a nice addition, theoretical bounds with unquantified constants are standard in ML theory papers and not a flaw per se.
- Several generic strengths from the Strength Finder about "addressing an important problem" or "evaluating on real-world data" were removed as not being specific enough to constitute evidence of contribution.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Explain the ρ=0 bias in Figure 1.** Provide a clear explanation for the ~100-nat offset — is it a fixed bias from the score approximation, a data-level property of SUMMEVAL (e.g., shared vocabulary across all documents and BART-generated summaries), or a truncation effect? If it is systematic and subtractable, demonstrate this by subtracting the ρ=0 intercept and showing the corrected estimates. If the "Empirical MI estimate" also has this bias, define what it is and use it to contextualize the method's behavior.
2. **Add a comparison against standard summarization metrics (ROUGE, BERTScore) in the model selection analysis** to contextualize the practical value of MI for this task.
3. **Include a brief runtime comparison table** showing training time and inference time for INFO-SEDD versus competitors, as well as the effect of varying vocabulary size on computation time.
4. **Clarify how the sum over |χ| in Equation (5) scales in practice** for large-vocabulary settings (e.g., via sub-sampling, importance sampling, or efficient matrix operations) and whether this limits the method's applicability to certain domains.

## Score and Decision

**Anchor comparison for calibration:**

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| MINDE (0kWd8SJq8d.md) | 6.50 | Closely related continuous-domain MI estimator via diffusion; accepted at ICLR. The discrete-paper under review has a more novel theoretical framework (CTMC+Dynkin vs SDE+Girsanov) but weaker empirical calibration (ρ=0 bias). Slightly below MINDE overall. |
| Discrete Diffusion Convergence (pq1WUegkza.md) | 7.00 | Pure theory paper on discrete diffusion convergence; accepted at ICLR. More rigorous mathematically but no empirical evaluation. The paper under review has broader scope (applications) but less formal depth. |
| How Discrete/Continuous Meet (6awxwQEI82.md) | 7.00 | Comprehensive theory of discrete diffusion models; accepted at ICLR. Stronger theoretical analysis but no real-world applications. The paper under review trades some theoretical rigor for practical demonstration. |
| F-DIME (KC2MViQASx.md) | 5.60 | MI estimation via f-divergence; rejected. Similar topic but less novel theory and weaker experimental validation. The paper under review is clearly stronger in both theory and experiments. |
| InfoNet (PyHRUMxKbT.md) | 5.75 | Feed-forward MI estimator; rejected. Narrower scope and weaker theoretical contribution. The paper under review is substantially stronger. |
| Normalizing Flows DoE (vgQmK5HHfz.md) | 4.83 | MI via normalizing flows; rejected. Weaker novelty and narrower evaluation. The paper under review is stronger. |
| Feature Selection MI (lt6xKGGWov.md) | 2.33 | Minimal experiments, unclear methodology. The paper under review is far stronger on every dimension. |
| Discrete Diffusion CTMC (pq1WUegkza.md) | 7.00 | Strong theoretical contribution on discrete diffusion; accepted at ICLR. More rigorous proofs but no empirical validation on real applications. |

**Calibration decision:** The paper presents a genuinely novel theoretical contribution (CTMC-based KL estimation for discrete data), strong synthetic results, and interesting real-world applications. Its main weakness — the unexplained ρ=0 bias in the text consistency test — is a real concern but does not invalidate the core contributions (the slope behavior matches expectations, and the genomics experiment provides a clean low-MI validation). The missing baselines in model selection and the absent runtime analysis are addressable limitations. Compared to the accepted MINDE paper (6.50), this work is slightly weaker due to the residual empirical question. Compared to the rejected MI papers in the 4.8–5.8 range, it is clearly stronger in both theoretical originality and experimental breadth.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>