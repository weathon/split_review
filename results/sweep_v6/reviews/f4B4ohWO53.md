## Summary

This paper proposes NVDP (Nonparametric Variational Differential Privacy), a method for sharing noisy transformer embeddings with differential privacy guarantees. The core idea is to insert an NVIB (Nonparametric Variational Information Bottleneck) layer into a transformer that learns a posterior distribution over multi-vector embeddings; sampling from this posterior provides a privatized embedding. The privacy guarantee is quantified via a Rényi divergence bound (Equation 7) and converted to Bayesian DP (BDP) values. Experiments on six GLUE tasks compare NVDP against non-private baselines and a VIB-based ablation (VTDP), showing that NVDP achieves better privacy-utility tradeoffs than the ablation while staying competitive with the non-private baselines.

## Strengths

- **Novel approach to learned noise injection for DP.** Using a nonparametric variational information bottleneck (NVIB) as a structured noise mechanism for transformer embeddings is genuinely novel. The architectural choice of removing the residual skip connection around the denoising MHA (Section 3.1, Figure 1) is well-motivated: it ensures no unsanitized information bypasses the bottleneck. This design is a clear conceptual advance over simple independent Gaussian noise or per-token VIB approaches.

- **NVDP consistently outperforms the VTDP ablation in privacy-utility tradeoff.** Table 1 shows that across five of six GLUE tasks, NVDP achieves higher accuracy at comparable or better BDP values than the VIB-based VTDP. On MRPC, for instance, NVDP reaches 83.0% accuracy with BDP=10.70, while VTDP at a similar budget (BDP=10.6) achieves only 74.8% (Figure 2). The advantage is especially clear on RÉnyi divergence: NVDP's RD is 0.34 vs. VTDP's 1.20 on MRPC. This empirically validates that the nonparametric structure better preserves task-relevant information while removing private information.

- **Competitive utility relative to non-private baselines.** On MRPC, NVDP (83.0%) matches or exceeds the +REG baseline (82.4%); on QQP (88.3% vs. 88.4%) and QNLI (89.5% vs. 89.7%), the gap is within 0.2 points. This demonstrates that the privacy mechanism does not catastrophically destroy utility.

## Weaknesses

### Fatal
None.

### Major

- **The DP analysis does not cover the training process, so the overall system does not satisfy its stated privacy claims.** The paper's differential privacy analysis applies only to the inference-time sampling step (drawing a noisy embedding from the learned posterior). The parameters of that posterior are themselves learned from potentially sensitive training data through a non-private training process (no DP-SGD, no noise added to gradients). The paper frames the method as a way to "share data" privately (Abstract, Section 1), but the entire training pipeline is unaccounted for in the privacy budget. This means the system as a whole does not provide a formal differential privacy guarantee for the data used to train the NVIB parameters. The paper needs to either (a) provide DP guarantees for the full training pipeline (e.g., via DP-SGD), (b) train the NVIB mechanism on a public hold-out set, or (c) explicitly reframe the contribution as a regularization technique with a side metric of output-distinguishability rather than a full DP system.

- **The Rényi divergence bound (Equation 7) is presented without derivation or validation, making the reported privacy numbers unverifiable.** Equation 7 is the central privacy formula, yet the paper provides no derivation, proof, or reference for its form. It mixes log-Gamma terms (from Dirichlet distributions over weights) and Gaussian terms (over vectors), but there is no argument that this expression is a valid upper bound on the Rényi divergence between the actual sampling distributions. The paper states it is an upper bound because "ordered tokens are more informative," but this heuristic justification is insufficient for a DP guarantee. Without rigorous justification, the RD and BDP values in Table 1 are uninterpretable. The paper should at minimum cite known formulas for Rényi divergence between Dirichlet distributions and provide a proof sketch of how the components compose.

- **No comparison with standard differential privacy baselines.** The experiments compare only against non-private models and the VTDP ablation. There is no comparison with established DP mechanisms such as (a) adding calibrated Gaussian noise directly to BERT embeddings with sensitivity analysis, (b) DP-SGD fine-tuning, or (c) the Laplace mechanism. Without these baselines, it is impossible to tell whether NVDP offers any practical advantage over simple, well-understood methods. The claimed "useful tradeoff" between privacy and utility is unsubstantiated without situating the results relative to known alternatives.

- **No adjacency definition is given, which renders the RDP definition vacuous.** The paper states "we do not assume any specific notion of adjacency between examples" (Section 3.2) and instead reports the maximum RD over all test-set pairs. Standard RDP (Definition 2.2) requires an adjacency relation to define what it means for two inputs to be "neighbors." Without this, measuring RD over all pairs is not a DP guarantee — it is a generic dissimilarity measure between instances. The paper needs to define adjacency (e.g., two examples differing by at most τ tokens) and compute RD only over adjacent pairs. The current approach conflates "all pairs are distinguishable" with "privacy leakage."

### Minor

- **The experimental evaluation selects the best of five runs for reporting results, inflating reported utility numbers.** The paper states: "we perform five independent runs and select the best-performing run on the validation set for final evaluation." This eliminates variance from the results, making the comparison unreliable. Standard practice is to report mean and standard deviation, or at minimum report the test performance of the run that was selected by validation. The lack of error bars makes it impossible to assess whether the observed differences are statistically significant.

- **The stated motivation (task-agnostic data sharing) is not reflected in the experiments.** Section 1 frames the contribution as enabling data to be "reused for multiple purposes and to train multiple models." However, the experiments train the entire model (BERT + NVIB + classifier) end-to-end on each individual GLUE task. This is task-specific privacy, not task-agnostic data sharing. The paper could simply reframe its contribution as a task-calibrated noise mechanism (which is what Section 3 already describes), but the mismatch between the aspirational framing and the actual evaluation should be resolved.

- **The reported BDP values (10–22) constitute very weak privacy by conventional DP standards.** In standard DP, ε=10 provides almost no meaningful protection. The paper claims "strong, practical privacy budgets" in the conclusion, which is overstated. While the paper shows tradeoff curves (Figure 2) that include stronger privacy points, the headline numbers in Table 1 are in a regime where the privacy protection is minimal. The claims should be tempered accordingly.

- **The BDP conversion process is not explained.** Section 3.2 mentions using "Theorem 2 of Triastcyn & Faltings (2020)" to convert RD to BDP, but provides no details on how this is applied in practice. Since BDP is the primary privacy metric used in Figure 2, the conversion should be explained or at least the specific settings (e.g., how the prior over X is defined) should be stated.

### Trivial

- None that survive the filtering rules.

## Nice-to-Haves

- A comparison with Gaussian noise added to BERT embeddings (at matching sensitivity) would be the most informative baseline for evaluating whether the structured NVIB noise provides genuine advantages.
- Extending the evaluation to a setting where NVIB is trained on a large public corpus and then applied to downstream tasks without further tuning would directly validate the "data sharing" framing.
- Reporting mean and standard deviation over multiple runs (with proper train/validation/test splits) would strengthen the empirical claims.
- Including a qualitative example (original vs. noisy embeddings with reconstruction attempts) would help illustrate the practical privacy protection.

## Removed Points

These points were removed from the main weaknesses because they do not survive the filtering rules or reflect misunderstandings:

- *"The paper's central claim is invalid because the privacy guarantee does not cover training."* This is reworded and retained above as a Major weakness, but not characterized as an outright invalidation. The paper's core technical contribution (NVIB-based noise mechanism) is still valid; the issue is with the scope of the claimed guarantees.

- *"The paper does not provide any formal privacy guarantee for the data it claims to protect."* Same issue as above; retained as a Major weakness but not elevated to Fatal, since the sampling mechanism itself does provide a formal (partial) guarantee for the inference step.

- *"No derivation, no proof, and no reference for Equation 7"* is partially mitigated by the fact that the equation decomposes into known Rényi divergence formulas for Dirichlet and Gaussian distributions. However, the absence of any derivation or citation for the Dirichlet component is a genuine gap, retained as a Major weakness.

- *"The method as evaluated is just a regularized fine-tuning procedure with a different noise model."* This is removed because it is not accurate — the privacy analysis (Equation 7, BDP conversion) goes well beyond standard regularization. The mismatch between motivation and evaluation is retained as a Minor weakness.

- *"Flawed experimental reporting: the privacy numbers seem too good relative to utility, suggesting very small noise."* This is speculative and removed. The paper explicitly reports the hyperparameter settings and tradeoff curves. There is no evidence of fabrication.

- *"The paper cannot claim a privacy-preserving data sharing system."* This is softened and retained within the Major weakness about training privacy. The paper can claim a privacy-preserving *embedding sharing* mechanism for inference, as long as the training limitation is acknowledged.

- *"Hyperparameters λ_D, λ_G are never specified."* These are part of the NVIB loss (Equation 5) and would typically be in the Appendix (which was stripped by the parser). Removed per the rule about missing appendices.

- *"The comparison between NVDP and VTDP conflates architectural differences with the nonparametric vs. parametric distinction."* This is a matter of interpretation — the paper's ablation is designed precisely to test the nonparametric component. Removed; the comparison is informative as designed.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface issues with the scope of the DP analysis and the validation of the privacy bound, which are standard concerns for papers proposing new DP mechanisms.

## Suggestions

1. **Provide a rigorous derivation of Equation 7 or cite its components.** At minimum, decompose the bound into a known Rényi divergence for Dirichlet distributions (reference needed) plus the Gaussian RD formula given in Equation 8, and provide a proof sketch showing that the ordering assumption yields an upper bound.

2. **Add standard DP baselines.** Compare against (a) adding calibrated Gaussian noise to BERT embeddings at the same dimensionality, with a sensitivity analysis, and (b) DP-SGD fine-tuning. Without these, the practical value of NVDP cannot be assessed.

3. **Define the adjacency relation explicitly.** The RDP definition requires a clear notion of adjacency (e.g., two sentences differing by at most k tokens). Compute RD only over adjacent pairs. Alternatively, reframe the metric as a "distinguishability score" rather than a DP guarantee.

4. **Acknowledge and discuss the training privacy gap.** Either remove the claim of being a privacy-preserving data sharing system and reframe as a regularization technique with a side metric of output-distinguishability, or add DP training guarantees (e.g., DP-SGD for the NVIB parameters).

5. **Report means and standard deviations** over multiple runs instead of selecting the best run, and use proper train/validation/test separation.

6. **Temper the claims about "strong, practical privacy budgets."** The BDP values of 10–22 are weak by conventional DP standards. Acknowledge this limitation and position the contribution relative to the privacy regime it actually operates in.

## Score and Decision

**Calibration anchors (all from /home/wg25r/split_review/datasets/deepreview_13k_calibration/):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| DF5TVzpTW0 (DPPN, embedding defense) | 6.00 | Stronger empirical evaluation, evaluated against inversion attacks, but also lacked formal DP guarantees. Our paper has more severe gaps in its DP analysis. |
| 3uITarEQ7p (DP Model Compression) | 5.50 | Has real DP guarantees through DP-SGD, so its privacy claims are well-founded. Our paper has less rigorous guarantees. |
| fGSEWgRHNZ (Adaptive PMixED) | 4.75 | Similar quality level — interesting approach with non-standard DP analysis that has significant gaps. Our paper has similar severity of weaknesses. |
| TbOcySs6g8 (Synthetic Data Alignment) | 2.50 | Fundamentally flawed DP analysis (clustering sensitivity not accounted for). Our paper is not this bad; the approach is coherent, just insufficiently validated. |
| vxmvbzw76R (Split-and-Denoise) | 4.75 | Very similar approach (LDP for embeddings). Both papers have weak privacy budgets and lack rigorous DP validation. Comparable quality. |
| nwDRD4AMoN (Kuramoto Neurons) | 9.00 | Exceptional paper with strong theoretical and empirical contributions. Our paper is far below this standard. |

The paper proposes a genuinely novel approach (NVIB-based learned noise for DP), which is its primary strength. However, the differential privacy analysis has multiple simultaneous gaps: the training pipeline is unprotected, the central privacy bound (Equation 7) is presented without derivation, no adjacency relation is defined, and the experiments lack standard DP baselines. The empirical evaluation uses best-run selection without variance estimates, and the headline BDP values (10–22) are weak. These weaknesses collectively prevent the paper from making a convincing case for NVDP as a practical privacy mechanism. The core ideas are interesting, and the architectural choices are well-motivated, but the validation is insufficient.

**Score: 4.0**

**Decision: Reject**

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>