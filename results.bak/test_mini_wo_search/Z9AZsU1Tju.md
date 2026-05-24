Now I have a thorough understanding of the paper and all the reviewer claims. Let me construct the consolidated review.

## Summary

This paper proposes the Information-Theoretic Hierarchical Perception (ITHP) model, which applies a two-level information bottleneck to multimodal fusion. A "prime modality" is designated as input, and two hierarchical latent states progressively distill relevant information from secondary modalities via variational IB objectives. The model is evaluated on sarcasm detection (MUStARD) and sentiment analysis (CMU-MOSI, CMU-MOSEI), reporting improvements over prior methods and claiming to surpass human-level benchmarks on CMU-MOSI.

## Strengths

1. **Novel hierarchical IB formulation for multimodal fusion.** The paper formalizes a two-level information bottleneck (Eq. 4–5) that compresses a designated prime modality while preserving task-relevant information from secondary modalities through a principled trade-off between compression and relevance. This differs from prior fusion methods that treat all modalities identically or simply concatenate them.

2. **Outperforms human-level benchmarks on CMU-MOSI across all four metrics.** Table 2 reports ITHP-DeBERTa achieving 88.7% BA, 88.6% F1, 0.643 MAE, and 0.852 Corr, surpassing the published human-level benchmarks (85.7%, 87.5%, 0.710, 0.820). This is the paper's strongest quantitative result and directly supports its headline claim.

3. **Consistent improvements on MUStARD across all modality combinations.** Table 1 shows ITHP achieving 75.2% F1 on V-T-A, outperforming the MSDM baseline (71.5%) and also beating all two-modality configurations, demonstrating that the hierarchical structure integrates information from all three modalities effectively.

4. **Systematic analysis of Lagrange multipliers (β, γ) on MUStARD.** Section 4.1 and Figure 3 investigate how varying β and γ affects performance, revealing that retaining text information (controlled by β) is more important for sarcasm detection. This provides interpretable insight into the learned information flow and helps justify the modality ordering.

5. **Generalization to a larger dataset (CMU-MOSEI).** Table 3 reports ITHP achieving 87.3% BA, 87.4% F1, outperforming MMIM_d (85.2%, 85.4%) and MAG_d (85.8%, 85.9%), confirming the method transfers beyond the smaller MOSI dataset.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation comparing hierarchical IB to simpler alternatives — the core architectural claim is untested.** The paper's central technical contribution is the *hierarchical* bottleneck structure (B0 → B1) with a designated prime modality. However, no experiment compares ITHP against:
   - A *flat* IB objective that compresses X0 while jointly preserving information about both X1 and X2 in a single latent variable.
   - A simple concatenation of modalities passed through a single bottleneck.
   
   The only ablation is on the Lagrange multipliers β and γ, which tests the trade-off *within* the hierarchy but does not test whether the hierarchy itself is necessary. Without this, the contribution of the specific hierarchical design over a standard IB-based fusion is unsubstantiated. This is the most significant gap in the paper.

2. **Uneven backbone comparison undermines fairness on MOSI/MOSEI.** ITHP is built on top of DeBERTa, but several baselines (UniMSE, MIB, BBFN) are reported without specifying their backbone, and the table only distinguishes BERT/DeBERTa for Self-MM, MMIM, and MAG. Since DeBERTa is known to substantially outperform BERT on language tasks, the large margins over UniMSE, MIB, and BBFN cannot be attributed to the ITHP architecture rather than the backbone choice. The only credible head-to-head comparisons are against MMIM_d and MAG_d (both DeBERTa-based), where ITHP's margins are modest (~2–3%). An ITHP-BERT version should have been tested to isolate the architecture's contribution from the backbone's.

3. **Self-MM_d is clearly broken and should not be included as a valid baseline.** Self-MM_d achieves 55.1 BA on MOSI and 65.3 on MOSEI — far below all other DeBERTa-based models (which are 85+). The paper acknowledges this is because Self-MM "heavily relies on the feature extraction process performed by BERT," yet includes it in the comparison table. This inflates the apparent improvement of ITHP and undermines the fair-comparison claim.

4. **No error bars, confidence intervals, or significance tests.** All results in Tables 2 and 3 are reported as point estimates without variance. Given that most credible gains over fair baselines (MMIM_d, MAG_d) are in the 2–3% range, it is impossible to assess whether these differences are statistically significant. The MUStARD results (Table 1) report 5-fold cross-validation averages but still lack per-fold variance.

### Minor

1. **MUStARD evaluation compares against only one baseline (MSDM).** The sarcasm detection experiments benchmark against only the original dataset paper's model (Castro et al., 2019). No comparisons are made to subsequent multimodal sarcasm detection methods from the literature (e.g., graph-based or attention-based models from 2020–2023). The claim of "outperforming state-of-the-art benchmarks" in the abstract is unsupported for this task.

2. **Modality ordering is determined by a heuristic, not validated.** The prime modality is chosen based on feature dimension size (e.g., V for MUStARD because d_v=2048 is largest; T for MOSI because d_t=768). No experiment tests alternative orderings to verify this choice is optimal or robust. The Limitations section acknowledges this is a preset order but does not validate it empirically.

3. **On CMU-MOSEI, ITHP does not uniformly outperform all baselines on all metrics.** ITHP's MAE (0.564) is worse than MMIM_b (0.526). While ITHP wins on BA, F1, and Corr, this partial trade-off should be discussed more transparently rather than claiming to "consistently surpass the SOTA" without qualification.

4. **Neuroscience framing overclaims biological fidelity.** The introduction emphasizes *reciprocal* connections and feedback mechanisms in the brain (lines 19–23), but the ITHP architecture is strictly feed-forward (X0 → B0 → B1) with no feedback path. The "reciprocal information exchange" referenced in the Figure 4 caption describes the IB loss terms (mutual information is symmetric) rather than architectural feedback. The model is a chain of variational bottlenecks — a plausible technical contribution — but the neuro-inspiration framing is more dramatic than the architectural realization warrants.

### Trivial

- The paper states "our ITHP model outperforms all the SOTA models in both BERT and DeBERTa incorporation settings" (line 271). ITHP is only evaluated with DeBERTa; the phrasing is ambiguous and could be read as claiming an ITHP-BERT variant was also tested.

## Nice-to-Haves

- A flat-IB ablation (single bottleneck compressing X0 to preserve I(B;X1)+I(B;X2) jointly) would directly validate the hierarchical contribution.
- Reporting bootstrapped 95% confidence intervals on MOSI/MOSEI metrics would address variance concerns.
- Adding 2–3 contemporary sarcasm detection baselines on MUStARD would strengthen the SOTA claim.
- Testing multiple modality orderings and reporting whether the best order aligns with information-theoretic criteria (rather than feature dimension) would improve the method's credibility.

## Removed Points

These points were flagged by reviewers but are excluded from the main weaknesses for the reasons stated:

- **"Human-level benchmarks are inter-annotator agreement, not a controlled human baseline"** — The paper is transparent that these benchmarks are from the original dataset paper (Zadeh et al., 2016). This is standard practice in the field; the criticism is about framing preference, not factual inaccuracy.
- **"First work to outperform humans claim is not verified by literature search"** — Speculation by the reviewer about work the authors may have missed. The paper uses "based on our knowledge" (line 301). No concrete missing work is identified.
- **"Missing related work / appendix / proofs"** — Per hard rules, these are parser-stripped content or require external knowledge the reviewer does not have.
- **"Typography and formatting nitpicks"** — Parser artifacts, not author errors.
- **"The model doesn't discuss training cost" (as a major weakness)** — This is a secondary concern; demoted to minor/optional.

## Novel Insights

The reviews surface a tension that is not explicitly discussed in the paper: the ITHP architecture's information-theoretic framing (hierarchical bottlenecks) is separable from its choice of backbone (DeBERTa), but the experimental design conflates the two. The strongest result — outperforming human benchmarks on MOSI — could be driven primarily by the DeBERTa backbone rather than the hierarchical IB structure. Without an ITHP-BERT baseline or a flat-IB+DeBERTa ablation, this confound is unresolved. Additionally, the sarcasm detection results on MUStARD, while consistent, are pitched against only a single 2019 baseline, making the "SOTA" claim fragile. The paper's genuine contribution (hierarchical IB for modality-ordered fusion) is promising but needs tighter experimental isolation to be convincing.

## Suggestions

1. **Add a flat-IB ablation**: Compare ITHP (hierarchical) against a single bottleneck that jointly preserves I(B;X1)+I(B;X2) using the same DeBERTa backbone. This directly tests whether the hierarchy matters.
2. **Test ITHP with a BERT backbone** (or remove the "both BERT and DeBERTa" claim). This would isolate the architecture's contribution from the backbone's.
3. **Remove Self-MM_d or clearly flag it as incompatible with DeBERTa** rather than including it as a fair baseline. Its anomalously low scores distort the comparison.
4. **Report variances (standard deviations or bootstrapped intervals)** for all main results, especially given the modest margins over fair baselines.
5. **Add contemporary baselines to MUStARD** to substantiate the SOTA claim for sarcasm detection.
6. **Test at least one alternative modality ordering** on each dataset to validate the heuristic (feature dimension → prime modality) or acknowledge this as a limitation more prominently.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Weak Accept</decision>