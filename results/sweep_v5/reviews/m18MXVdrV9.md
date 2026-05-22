Now I have thorough calibration data. Let me write the final consolidated review.

## Summary
This paper introduces INFO-SEDD, a method for estimating mutual information (MI) on high-dimensional discrete data using Continuous Time Markov Chains (CTMCs) and discrete diffusion models. The core idea is to derive a tractable KL divergence estimator from Dynkin's formula, then use score functions from a single diffusion model (via an absorbing-state trick) to compute joint and marginal quantities needed for MI. The method is validated on synthetic benchmarks and applied to text summarization (consistency testing and model selection) and genomics (motif discovery). The synthetic results are strong, and the genomics motif-discovery application is a genuinely compelling use case.

## Strengths

- **Novel theoretical foundation connecting CTMCs to KL estimation**: Deriving a KL divergence estimator from Dynkin's formula (Eqs. 2–5) is principled and mathematically grounded. The error bound in Eq. (7) provides a clear decomposition into score-approximation error (linear) and truncation bias (exponentially decaying with T), establishing consistency guarantees that competing black-box neural estimators lack.

- **Absorbing-state trick for single-model estimation**: Equation (6) shows that by using an absorbing-state transition matrix, a single score model trained on the joint distribution suffices to compute the marginal scores needed for MI. This is clever and practically important — it avoids training separate models for each marginal distribution.

- **Dominant performance on high-dimensional synthetic benchmarks**: Table 1 convincingly shows that INFO-SEDD-J produces accurate estimates (e.g., 9.92±0.12 for MI=10, D=10) where variational methods (MINE, NWJ, SMILE) collapse or exhibit large bias/variance. The advantage grows with MI and dimensionality, exactly where existing methods are known to fail.

- **Compelling genomics application for motif discovery**: Figure 5 demonstrates that INFO-SEDD-J localizes the TATA-box motif in *Arabidopsis thaliana* promoters, with MI peaking precisely in the known region (−39 to −26 relative to TSS). Importantly, INFO-SEDD natively supports subset-based MI estimation without retraining for each sliding window — a capability no competing estimator offers.

- **Sample efficiency**: The method remains accurate with as few as 10³ samples (Appendix C.1.5), two orders of magnitude fewer than the main benchmark, demonstrating practical utility for sample-starved domains.

## Weaknesses

### Fatal
None.

### Major
- **Model selection experiment lacks statistical rigor**: Table 2 reports Pearson/Kendall correlations based on only 15 summarization models. No confidence intervals, p-values, or significance tests are provided for the *differences between methods*. The observed advantage of INFO-SEDD-C over KL-DIME on consistency (0.740 vs. 0.214) could be non-significant or driven by a small number of outliers. While Figures 2–3 show GP regression with 95% CIs, this does not constitute a test of whether INFO-SEDD is significantly better than alternatives. The conclusion that MI is "meaningful for model selection" would be strengthened by bootstrap or permutation testing.

- **Real-world validation relies on approximate, non-ground-truth references**: The consistency test in text summarization (Figure 1) uses literature entropy rates (256–303 nats) linearly scaled by ρ as a "reference." The paper acknowledges this is an order-of-magnitude estimate (Section 4.2), but the framing ("closely matches the empirical derivation") overstates the certitude. Similarly, the genomics consistency test (Figure 4) uses a classifier-based reference that depends on the accuracy of an independent classifier. While consistency tests are standard practice in the MI estimation literature, the paper would benefit from at least one controlled experiment with known ground-truth MI embedded in realistic data structures (e.g., a synthetic genetic regulatory network).

### Minor
- **Monte Carlo variance not characterized**: The estimator in Eq. (5) requires Monte Carlo integration over time t and diffusion trajectories, but the main text does not specify how many time samples or trajectories are used, nor does it report error bars on real-data MI estimates (Figures 1, 4; Table 2). This makes it difficult to assess the reliability of individual point estimates. (Details may reside in the appendix, but the main text should include at least a brief summary.)

- **"Empirical MI estimate" in Figure 1 is not defined in the main text**: The grey curve labeled "Empirical MI estimate" appears in the figure legend but is not explained — it is unclear whether this is a plug-in estimate, a histogram-based count, or some other baseline. The reader should not have to consult the appendix for this basic information.

- **Derivation step from Dynkin's formula to Eq. (4) is compressed**: The paper states "By combining the result from Equation (3) with Equation (2)" but does not sketch the algebraic manipulation in the main text. While the appendix may contain the full derivation, a brief outline would help the reader follow the key methodological step.

- **Overclaimed "uniqueness"**: The conclusion states the method is "unique" as a "scalable, consistent, and accurate" discrete MI estimator. This overstates the claim — prior plug-in and autoregressive-based estimators for discrete data exist. The method is novel in its diffusion-based approach, but the phrasing should be more measured.

### Trivial
- The constants C₁, C₂ in the error bound (Eq. 7) are referred to as "boundedness of score functions" but are not further specified. This is typical for such bounds but limits practical interpretability.

## Nice-to-Haves
- A controlled experiment with known ground-truth MI in a realistic data domain (e.g., synthetic regulatory network where true MI between regulator and target is computable).
- Variance/sensitivity analysis: report MI estimates over multiple random seeds (including time sampling and trajectory Monte Carlo) with standard errors.
- Ablation on time horizon T and number of integration steps to validate that truncation bias is minimal.
- Comparison to a simple discrete plug-in baseline (e.g., tokenized bag-of-words with binning) to calibrate the magnitude of reported MI values.
- Qualitative examples from the summarization experiment showing high- vs. low-MI summary pairs alongside human consistency judgments.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Criticism that MDLM is "not a trivial embedding"**: The paper uses the same MDLM backbone for all methods (including competitors). INFO-SEDD simply avoids an additional embedding lookup table that competitors require. This is correctly presented as an advantage. Removed as factually incorrect — a misreading of the text.
- **Speculation about synthetic data matching the independent-component assumption**: The paper cites evidence (Sahoo et al., 2024; Lou et al., 2024) that single-token-change decomposition works for complex distributions with non-local interactions. The critic's concern is speculative and unsupported by the paper's content. Removed as a strawman.
- **Criticism that the absorbing-state trick is only valid for absorbing forward processes**: This is a deliberate design choice that the paper clearly describes. It is a feature, not a weakness. Alternative processes (uniform transitions) are not in scope.
- **Missing appendix/content complaints**: The parser strips appendix content from all papers. Criticisms about missing proofs, experimental details, or figures that reside in the appendix are automatically removed per policy.
- **Formatting, typo, and style nitpicks**: Removed per policy — parser artifacts, not author errors.
- **Strength Finder items that conflict with verified weaknesses or are generic**: Claims that the consistency test is a "strength" are retained but caveated; generic/superficial strengths (e.g., "the paper addresses an important problem") dropped.

## Novel Insights
Beyond the paper's own contributions, the reviews surface an interesting observation: the tension between the rigorous synthetic validation (Table 1) and the approximate-reference-based real-world validation highlights a structural challenge faced by essentially all neural MI estimators — there is no established benchmark with known ground-truth MI on natural discrete data at scale. The paper's genomics motif-discovery application partially addresses this by providing a concrete downstream task where the ground-truth *location* (not MI value) is known, serving as an indirect but verifiable validation signal. This suggests that the field may benefit from shifting toward task-based evaluation (where correctness is measured by downstream utility on problems with known structure) rather than only consistency tests with approximate references.

## Suggestions
1. **Add statistical testing for the model selection experiment**: Report bootstrapped confidence intervals for the correlation differences between methods in Table 2, or perform a permutation test to establish whether INFO-SEDD's advantage over KL-DIME on consistency is significant.
2. **Include a controlled experiment with known MI**: Even a simple setup — e.g., a Markov chain of similar complexity to the genomics data where ground-truth MI is analytically computable — would substantially strengthen the empirical case.
3. **Report Monte Carlo variance for real-data estimates**: Provide standard errors or confidence intervals for the MI estimates in Figures 1, 4, and Table 2, and specify the number of time samples and trajectories used.
4. **Define the "Empirical MI estimate" in Figure 1** in the main text caption or body.
5. **Tone down the "unique" claim** in the conclusion to something like "to the best of our knowledge, the first diffusion-based MI estimator for discrete data."

## Score and Decision

**Calibration anchors** (from the human-review corpus):

| Paper | Avg Score | Comparison |
|-------|-----------|------------|
| MINDE (0kWd8SJq8d) | 6.50 | Very similar: diffusion-based MI estimation, strong synthetic results, real-world validation with approximate references. The current paper extends to discrete data — a genuine gap — and has a clever single-model trick. Comparable quality. |
| Convergence of Score-Based Discrete Diffusion (pq1WUegkza) | 7.00 | Pure theory paper on discrete diffusion. Different contribution type — no experiments but rigorous theory. Current paper has stronger empirical validation. |
| Flow-based Variational MI (spDUv05cEq) | 6.00 | Normalizing flows for MI estimation. Weaker theory, no real-world applications. Current paper is stronger on both theory and applications. |
| f-DIME (KC2MViQASx) | 5.60 | Rejected. f-divergence MI estimation with claims that didn't fully match evidence. Current paper has stronger theory, better synthetic results, and real-world applications. |
| Normalizing Flows DoE (vgQmK5HHfz) | 4.83 | Rejected. Limited novelty, weak experiments. Current paper is substantially stronger. |
| A Discrete Actor and Critic (EWKPEtwjTy) | 2.50 | Very weak paper, not comparable in scope or quality. |
| sCM (LyJi5ugyJx) | 9.20 | Exceptional paper; different league. Current paper is not at this level. |

The paper makes a genuine contribution — it is the first principled diffusion-based MI estimator for high-dimensional discrete data, with solid theory, strong synthetic results, and interesting applications. The main weaknesses (lack of ground-truth real-world validation and limited statistical rigor in the model selection experiment) are meaningful but not fatal, and are comparable to those in accepted papers of similar scope (e.g., MINDE at 6.50).

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>