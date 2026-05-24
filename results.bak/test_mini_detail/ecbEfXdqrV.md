Now I have enough information to produce the consolidated review. Let me finalize my analysis.

**Round 1 Bracketing:** The paper sits between weak anchors (avg 2.5-3.4, clearly rejected) and strong anchors (avg 8.0, accept spotlight/oral). Middle bracket is 5.75-6.75.

**Round 2 Narrowing:** 
- NCSN paper (5.75, withdrawn): Our paper is stronger — clearer contribution, no novelty concerns
- AVOID (6.0, reject): Comparable theoretical ambition, but our paper has more extensive empirical eval and no novelty overlap concerns
- Swift Hydra (6.5, accept poster): Our paper has weaker method novelty but much stronger experimental rigor (47 datasets, 12 baselines vs 3 baselines)
- AnoLLM (6.75, accept poster): Our paper has a different contribution type (phenomenon investigation vs new method); less immediately impactful but more thorough

**Final Score:** 6.0 — solid paper, above acceptance threshold, but notable weaknesses prevent higher score.

Now let me write the review, carefully filtering the reviewer claims.

Let me verify key claims:

1. **Definition not quantitatively applied** — Verified. The paper defines Definition 3.3 with β and γ but never sets specific values or checks condition formally. The paper uses heuristics (fail ratio, top2 ratio, qualitative discussion of yeast/imdb). ✓ Valid weakness.

2. **Theory assumption gap** — Verified. Theorem 5.4 assumes independent features and perfect model. §5.2 correlation analysis is separate. The paper acknowledges this but doesn't bridge the gap. ✓ Valid weakness but moderate, not severe.

3. **Bilinear interpolation experiment** — Verified. Table 3 resizes images with bilinear interpolation, uses Glow (CNN-based). The paper says "independence between pixels is not guaranteed, so the theorem... cannot be applied." The paper acknowledges limitations but the experiment is exploratory. ✓ Valid minor weakness.

4. **Single flow architecture** — The paper says "Additionally, the results of applying other flows to NF-SLT are included in Appendix G." So the appendix addresses this. The main results focus on NICE. ✓ Valid but mitigated by appendix.

5. **Relatively Low Performance assumption critique** — The definition uses relative AUROC performance, not direct likelihood ordering. This is a reasonable operationalization but conflates model being bad vs exhibiting the specific failure mode. ✓ Valid moderate weakness.

6. **No error bars** — The paper says "10 repeated experiments" but doesn't report std devs in Table 1. ✓ Valid minor weakness.

7. **Failure cases not analyzed** — The 'yeast' dataset is mentioned briefly. ✓ Valid minor weakness.

Let me now consider what to remove:

1. The reviewer says "the evidence that the phenomenon is 'rare' rests on a single flow architecture in the main evaluation" — but the appendix has other flows (Appendix G). The paper clearly states this. I'll keep it as minor since the main text focuses on NICE but the appendix addresses it.

2. The reviewer says "The definition should be linked more directly to likelihood ordering, not just to comparative AUROC" — This is a valid conceptual criticism, not noise.

3. The "missing appendix" / "proofs in Appendix D (stripped)" — I should REMOVE this concern since appendices are stripped by the parser.

4. "The paper would benefit from a single theoretical framework that jointly handles dimension and correlation" — This is a scope creep request, I should WEAKEN this.

5. "Confidence intervals or variance of ID estimates are not reported" — Valid minor point.

6. The critique about "entropy condition verification" — The paper doesn't attempt to estimate entropy. Valid minor point.

Let me also filter the Strength Finder's output — remove generic/superficial strengths.

The Strengths Finder says things like "avoids selection bias" — this is specific and valid. Let me keep the concrete ones.

Actually, looking again at the Strength Finder, most of the strengths are specific and evidence-backed. Good.

Now let me write the final review.Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper investigates whether the well-known "counterintuitive phenomenon" (deep generative models assigning higher likelihoods to anomalous data) occurs in tabular anomaly detection. It provides a domain-agnostic formal definition of this phenomenon (Definition 3.3), conducts extensive experiments on all 47 ADBench tabular datasets and 10 CV/NLP embedding datasets against 12 baselines, and shows that likelihood-based detection with a normalizing flow (NICE) rarely exhibits the phenomenon and actually outperforms existing methods. The paper also offers theoretical analysis (linking dimensionality to likelihood-gap degradation under independence assumptions) and empirical analysis (using intrinsic dimension as a proxy for feature correlation) to explain why tabular data avoids the counterintuitive behavior.

## Strengths

1. **Domain-agnostic formal definition of the counterintuitive phenomenon**: Definition 3.3 (with conditions on β and γ for proportion of outperforming baselines and minimum performance gap) provides a precise, transferable formulation that goes beyond the vague qualitative descriptions in prior work. This is a clear intellectual contribution that enables consistent detection across domains.

2. **Comprehensive empirical evaluation on all 47 ADBench tabular datasets**: Table 1 shows NF-SLT achieves the highest average AUROC (0.8575), highest AUPRC (0.6398), best average rank (3.43), highest Top2 Ratio (0.45), and critically the lowest Fail Ratio (0.02) among 13 models. The paper uses all ADBench datasets without selection bias (citing Shwartz-Ziv & Armon, 2022), compares against 12 baselines (6 shallow + 6 deep), and reports 10-run averages.

3. **Theoretical analysis connecting dimensionality to likelihood gap**: Theorem 5.4 proves that under independence assumptions and entropy conditions, the lower bound of the likelihood gap between normal and abnormal data decreases linearly with dimension d. Corollary 5.6 derives an inverse relationship between AUROC upper bound and dimensionality. The ICA dimensionality-reduction experiment (Table 2) provides clean empirical support — reducing image dimension systematically improves AUROC when ℍ(P) > ℍ(Q).

4. **Feature correlation analysis via intrinsic dimension**: The paper quantifies overall feature correlation using the d Ratio (intrinsic dimension / ambient dimension), showing that image datasets (d Ratio ≈ 0.001-0.019) have far smaller ratios than tabular datasets (d Ratio ≈ 0.389-0.810). Figure 1 and Table 4 convincingly demonstrate that tabular data has weaker global correlation, providing an intuitive explanation for why likelihood-based detection works better in this domain.

5. **Consistency on CV/NLP embeddings**: The paper extends results to 10 CV/NLP embedding datasets from ADBench, showing NF-SLT outperforms deep models on all but one (imdb), where the performance gap is small. This demonstrates the findings generalize beyond raw tabular features.

## Weaknesses

### Fatal
None.

### Major

1. **The formal definition (Definition 3.3) is not applied quantitatively anywhere in the evaluation**. The definition uses thresholds β (proportion of outperforming baselines) and γ (minimum performance gap), but the paper never specifies any values for these thresholds or checks how many datasets satisfy the conditions. Instead, the claim that "the phenomenon is rare" is supported by high average AUROC, low Fail Ratio, and qualitative discussion of the 'yeast' and 'imdb' cases. This creates a disconnect between the formalization and the empirical evidence. The paper should either (a) choose defensible β,γ values and report the fraction of datasets that trigger Definition 3.3, or (b) clarify that the definition is a conceptual framing and the actual test is the overall pattern. Without this, the central claim is not directly verified against the paper's own criterion.

2. **The theoretical analysis (Theorem 5.4, Corollary 5.6) relies on strong assumptions (independent features, perfect model) that do not hold for real tabular data**. The paper acknowledges this but the causal chain is indirect: the theory shows that *if* features were independent and the entropy condition held, high dimensions cause trouble, and then the empirical argument is that tabular data have lower dimension and weaker correlation. The correlation analysis in §5.2 is entirely separate and uses intrinsic dimension as a proxy. The theory and empirics are never formally unified. The paper should explicitly state the gap between the theoretical assumptions and the empirical setting, and clarify that the theory's role is to suggest a mechanism rather than to directly prove the phenomenon's absence in tabular data.

### Minor

1. **The definition conflates two distinct failure modes**. Assumption 3.1 defines the counterintuitive phenomenon purely in terms of relative AUROC (being outperformed by most baselines). However, this does not distinguish between (a) the model being genuinely bad for structural reasons (poor density estimation) and (b) the specific failure mode where likelihoods are inverted relative to data complexity (anomalies having higher likelihood than normal data). These are different phenomena and conflating them weakens the definition's diagnostic value.

2. **Main experimental results focus on a single flow architecture (NICE)**. While Appendix G reports results for other flow variants, the headline tables and analysis use only NICE. The paper's title and abstract claim to investigate whether the counterintuitive phenomenon occurs in tabular domain with deep generative models generally, but only one generative model is deeply evaluated. A more convincing test would apply multiple density estimation models and check if any exhibit Definition 3.3 conditions.

3. **No standard deviations or error bars reported in Table 1**, despite the paper stating "10 repeated experiments." This makes it impossible to assess whether performance differences between models are statistically meaningful. The hyperparameter selection procedure (choosing the combination with the highest average AUROC across all datasets) also raises questions about potential overfitting to the benchmark.

4. **The bilinear interpolation experiment (Table 3) is difficult to interpret and does not cleanly support the core claims**. The paper acknowledges that "independence between pixels is not guaranteed, so the theorem... cannot be applied" and that the results "conflict with the theorems in Appendix D." The paper's post-hoc explanation (resizing strengthens correlation, reducing entropy) is plausible but no entropy measurements or correlation statistics are provided to verify it. This experiment would be better suited for the appendix.

5. **No direct entropy estimation is attempted for the tabular datasets**. The theoretical and empirical arguments depend on the entropy difference ℍ(P) − ℍ(Q) between normal and anomalous distributions, but the paper never attempts to estimate entropy for any tabular dataset (e.g., via a Gaussian approximation or kNN estimator). This would help validate whether the condition for likelihood inversion holds in practice.

6. **Failure case analysis is thin**. The 'yeast' dataset where NF-SLT underperforms is mentioned in one sentence but not investigated in terms of its dimensionality, feature correlation structure, or entropy characteristics. A brief case study would strengthen the correlation analysis.

### Trivial
- No trivial issues worth reporting (parser artifacts are not author errors).

## Nice-to-Haves
- Include standard deviations or confidence intervals for the main results in Table 1.
- Apply the formal definition quantitatively by choosing specific β,γ values and reporting the fraction of datasets that satisfy the conditions.
- Add a brief case study of the 'yeast' dataset (and any other failure cases) linking performance to its d Ratio and other properties.
- Provide entropy estimates for normal vs. anomalous distributions in a subset of tabular datasets to validate the theoretical condition.
- Test at least one additional flow architecture (e.g., RealNVP) in the main results table.

## Removed Points
Points flagged for removal; treat with caution as they were filtered for being speculative, scope-creep, or based on stripped appendices:

- **"Missing proofs in Appendix D"**: The appendix is stripped by the parser; this is not an author error. → Removed.
- **"The bilinear interpolation experiment should be removed entirely"**: Overstated. The experiment has acknowledged limitations but provides some useful exploratory evidence. → Downgraded to Minor.
- **"The theoretical framework should jointly handle dimension and correlation"**: This requests a fundamentally new theoretical contribution beyond the paper's scope. → Removed (scope creep).
- **Strength Finder item about "Avoidance of selection bias"**: While valid, this is a methodological good practice rather than a distinctive strength. → Removed as generic.
- **Strength Finder items about generic problem importance**: Removed as superficial/sycophancy.

## Novel Insights
The harsh critic's observation that the formal definition (Definition 3.3) is not applied quantitatively — i.e., the paper never sets β,γ thresholds and checks which datasets satisfy the conditions — is a genuinely insightful criticism that directly undermines the paper's claim to have "detected" the phenomenon by its own standard. This is not a minor presentation issue but a structural gap between the formalization and the evaluation. The paper's evidence remains compelling heuristically (high average rank, low Fail Ratio), but the formal definition plays no operational role in the empirical section beyond providing conceptual framing. The harsh critic's point about the definition conflating "model is bad generally" with "likelihood inversion specifically" is also a substantive conceptual concern that deserves attention. On the strength side, the combination of a formal definition + comprehensive benchmark (all 47 ADBench datasets) + theoretical + empirical analysis of why the phenomenon is rare is a genuinely useful contribution that goes beyond prior work's narrow demonstrations on 1-2 datasets.

## Suggestions
1. **Apply Definition 3.3 quantitatively**: Choose reasonable β and γ thresholds (e.g., β = 0.5, γ = 0.05) and report the fraction of datasets that trigger the counterintuitive phenomenon. This directly connects the formal contribution to the empirical evidence and would cleanly resolve the paper's central claim.
2. **Explicitly state the theory-empirics gap**: Add a paragraph clarifying that Theorem 5.4 assumes independence and perfect models, and that its role is to identify a mechanism by which dimensionality can amplify likelihood inversion. The actual empirical case rests on the combination of lower dimension + weaker correlation in tabular data.
3. **Include error bars**: Add standard deviations or confidence intervals to Table 1 for the 10-run averages.
4. **Add at least one more flow architecture to the main results**: Even a single additional flow (e.g., RealNVP with MLP) in the headline table would significantly broaden the claim.
5. **Move Table 3 to the appendix** or add entropy/correlation measurements to make it interpretable.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak anchors (avg 2.5-3.4): e.g., 6Z8rZlKpNT (NFs for OOD, 3.40), oDGkq0AleM (AnoRand, 3.00), i28ZjVxl81 (Dealing with OOD, 2.50), ifGvDAcJK4 (AnoRand, 3.00) — All clearly rejected/withdrawn. Our paper is substantially stronger in both contribution and experimental rigor.
- Middle anchors (avg 4.25-6.75): hWF4KWeNgb (HGAD, 4.25, reject) — Less rigorous experiments; Vi6p2TeujL (PTAD, 4.25, withdrawn); 7QDIFrtAsB (NCSN for tabular AD, 5.75, withdrawn) — Limited novelty concerns; 7VkHffT5X2 (AnoLLM, 6.75, accept poster) — Novel method with good results but weaker experimental scope.
- Strong anchors (avg 8.0): cJs4oE4m9Q (Deep Orthogonal Hypersphere, 8.0, spotlight), G32oY4Vnm8 (PTaRL, 8.0, spotlight) — These are method papers with clear novel contributions and thorough evaluation; our paper is not at this level.

**Round 1 bracket**: 5.0 – 7.0.

**Round 2 (Narrowing):**
- 3a505tMjGE (AVOID, avg 6.0, reject): Theoretical analysis of VAE overestimation in OOD detection, with a proposed fix. Similar in genre (analysis + theory), but our paper has more extensive empirical evaluation (47 datasets vs mostly image pairs) and a different (arguably more useful) contribution type. Our paper is slightly stronger.
- LjygLD0AkT (LPath, avg 5.0, reject): Theory-heavy OOD detection paper with strong assumptions and limited empirical scope. Our paper is substantially stronger empirically and clearer in presentation.
- P7t2niLbvw (Swift Hydra, avg 6.5, accept poster): Novel RL+generative AD method but only 3 baselines. Our paper has much stronger experimental rigor (12 baselines, 47 datasets) but less direct methodological novelty. Comparable quality.
- 7VkHffT5X2 (AnoLLM, avg 6.75, accept poster): Novel LLM-based tabular AD method. Slightly higher impact but less thorough evaluation. Our paper is comparable.

**Final position**: Between 6.0 (AVOID) and 6.5 (Swift Hydra). The weaknesses in the paper (definition not applied quantitatively, theory-assumption gap, single architecture) are real and prevent it from reaching the 6.5+ level, but the paper is clearly stronger than the 5.0-5.75 range papers.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>