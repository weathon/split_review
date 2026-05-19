- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3
Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper presents the first systematic investigation of how label noise affects Concept Bottleneck Models (CBMs). It demonstrates that label noise — especially concept noise — severely degrades both target prediction accuracy and interpretability across multiple training strategies, datasets, and CBM variants. The authors identify concept noise as the primary cause of failure, analyze the breakdown mechanisms via t-SNE visualization, concept weight analysis, and per-concept accuracy, and propose Sharpness-Aware Minimization (SAM) as a mitigation strategy. The diagnostic analysis (Sections 3–4) is thorough and contributes useful insights; the mitigation evaluation (Section 5) is preliminary and limited in scope.

## Strengths

1. **First systematic study of label noise in CBMs.** The paper provides broad coverage across three noise types (concept, target, combined), five noise rates (0%–40%), two datasets (CUB, AwA2), and all three CBM training strategies (Ind, Seq, Joi) (Section 3, Figures 2–3, Table 1). This breadth makes a convincing case that CBMs are severely vulnerable to label noise — a finding not previously documented in the literature.

2. **Identification of concept noise as the primary cause of degradation.** By isolating concept noise, target noise, and their combination, the paper shows that concept noise alone reproduces the degradation of combined noise (Figure 3). This attribution is evidence-based and actionable: it tells the community that concept annotation quality is the critical bottleneck, not target label noise.

3. **In-depth analysis of breakdown mechanisms.** The paper uses t-SNE projections to show that concept noise destroys representation clustering while target noise does not (Figure 4); weight analysis of the target predictor to reveal that concept noise distorts concept-target importance rankings (Figure 5); and per-concept accuracy plots to document uneven deterioration that directly harms target predictions (Figure 6). These visualizations go beyond aggregate metrics and provide mechanistic understanding of *how* noise disrupts CBMs.

4. **Generality demonstrated across CBM variants, noise structures, and architectures.** The paper tests Concept Embedding Models and Energy-based CBMs under label noise (Figure 8), pairwise structured noise (Figure 9), and multiple backbone architectures (ResNet-18, ViT-B/16, Table 3), showing that the vulnerabilities are not idiosyncratic to one setup. SAM consistently improves results across these settings.

5. **Honest self-assessment of limitations.** The Limitations section (line 191) explicitly acknowledges that "the exploration of mitigation techniques being less extensive" — which contextualizes the paper's main contribution as diagnostic rather than prescriptive.

## Weaknesses

### Fatal

None. The paper's core diagnostic claims are supported by the evidence presented.

### Major

1. **Mitigation evaluation is limited to SAM vs. SGD, with no comparison to established noisy-label methods.** The paper frames itself (line 16) as evaluating "the effectiveness of existing label noise mitigation techniques" but only compares SAM to standard SGD. There are no comparisons to robust loss functions (e.g., generalized cross-entropy, symmetric cross-entropy), sample selection/self-training methods, noise transition matrix approaches, or other robust optimizers — all of which are cited in the related work (line 182) and are standard in the noisy-label literature. The paper's own limitations section acknowledges this gap, but the framing of the contribution overstates what is actually demonstrated. Without baselines, the claim that SAM "effectively mitigates" noise effects cannot be assessed relative to alternatives. The observed gains (0.6%–0.9% concept accuracy, 2.4%–3.2% target accuracy) are modest, and it is unclear whether they are competitive with existing approaches.

2. **The detailed breakdown analysis (Section 4) is confined to a single class and a single model.** The t-SNE analysis (Section 4.1) uses three classes but a single Ind model. The weight-shift analysis (Section 4.2) examines only one class (LE CONTE SPARROW) and one model (Ind) trained on CUB. The per-concept accuracy analysis (Section 4.2) similarly focuses on one class. These analyses are compelling as illustrative case studies but do not constitute statistically robust evidence of general patterns. Aggregate statistics over all classes or multiple models would substantially strengthen the conclusions.

### Minor

3. **The decomposition analysis identifying concept noise as the primary cause (Figure 3) is shown for the Ind model only.** While Ind is the most instructive setting, showing comparable decomposition for Seq and Joi would verify that the conclusion holds across training strategies.

4. **No variance/uncertainty reporting in tables.** The paper reports results averaged over three seeds but does not include standard deviations or confidence intervals (e.g., in Tables 1, 2, 3). With only three runs, the reader cannot assess whether observed improvements (e.g., the SAM gains) are within the noise range of the measurements.

5. **Overstated motivation regarding "real-world" noise modeling.** Section 2 (line 38) claims the dataset "can mimic the real-world noisy dataset," but the primary experiments use symmetric random label flipping — a standard academic noise model that does not closely simulate real annotation errors. The pairwise noise experiments (Section 6.2) partially address this, but most core results rely on symmetric noise. This mismatch should be acknowledged more frankly.

### Trivial

None.

## Nice-to-Haves

- The paper would benefit from a multi-class aggregate version of the Section 4 analyses (e.g., average concept weight shift or average concept accuracy drop across all classes) to move from illustration to robust empirical finding.
- Statistical significance testing for key comparisons (e.g., SAM vs. SGD differences) would strengthen the quantitative claims.

## Removed Points

These points are flagged for removal; treat them with caution:

1. **Hyperparameter/optimizer configuration underspecified** (Harsh Critic, Issue 2). The critic argues that lack of detail about tuning for SGD vs. SAM risks an unfair comparison. This is a valid methodological concern, but per the filtering rules, it is categorized as a reproducibility nitpick and removed from the main weaknesses. However, the authors are encouraged to include these details in a revision to strengthen the comparison.

2. **"?Baek et al." citation concern** (Harsh Critic, Missing Parts #4). The "?" before the citation is a PDF-to-text parser artifact; the original submission contains the proper citation. Per the filtering rules, parser artifacts are not author errors.

3. **"SAM reducing overfitting is a known behavior"** (Harsh Critic, Section 5 note). The paper cites prior work establishing SAM's effectiveness in noisy settings; the contribution is applying and verifying this in the new domain of CBMs. This is not a paper weakness but an observation that the mechanism is not novel — which the paper does not claim.

4. **Comparison asymmetry favoring baseline** — Not applicable; no such claim was made.

5. **Missing related works** — Per the filtering rules, this cannot be evaluated without external references and is not included.

## Novel Insights

The two reviews largely converge on the same assessment: the paper makes a genuine contribution in documenting and diagnosing CBM vulnerability to label noise, but the mitigation evaluation is underdeveloped relative to the paper's framing. The most interesting tension between the reviews is the harsh critic's assertion that the Section 4 analysis is merely "illustrative" versus the strength finder's characterization of it as "in-depth." The truth lies between: the analysis is genuinely informative and uses multiple lenses (t-SNE, weight analysis, per-concept accuracy), but its restriction to a single class and single model does limit generalizability. The paper would be markedly stronger if this analysis were extended to aggregate statistics across classes and training strategies.

## Suggestions

1. **Add at least one non-trivial baseline** to the mitigation experiments — e.g., a robust loss function (generalized cross-entropy) or a sample-selection method. This is the single most impactful addition the paper could make. Alternatively, reframe the paper's title and abstract to focus on the diagnostic contribution and present SAM as a preliminary observation rather than a validated mitigation.

2. **Extend the Section 4 analysis to multiple classes** and provide aggregate summary statistics (mean/median weight change, average concept accuracy drop across classes) alongside the illustrative single-class plots.

3. **Include standard deviations** in all tables reporting averaged results over multiple seeds.

4. **Add decomposition plots (Figure 3 equivalent) for Seq and Joi** training strategies, even in supplementary material.

5. **Tone down the "mimic the real-world" claim** in Section 2 and explicitly acknowledge that symmetric random flipping is a synthetic noise model, while noting that pairwise noise experiments partially address realism.
