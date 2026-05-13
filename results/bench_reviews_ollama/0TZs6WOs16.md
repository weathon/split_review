Let me now carefully analyze the key claims and the reviewers' assessments.

---

Now let me summarize what I've verified from the paper:

**Key claim 1: Embedding size confound.**
The paper states (line 172): "As the hyperbolic models are expected to be more expressive, we limit the allowed embedding size values to (32, 64, 128), while the Euclidean models explore higher values from (256, 512, 728). Hence, we force the hyperbolic models to learn more compact representations."

This is actually the paper's *design choice* — they purposely constrain hyperbolic models to smaller embeddings to show they achieve better performance despite being smaller. The harsh critic's point that this "invalidates the central comparison" needs careful thought: the paper's claim is precisely that hyperbolic geometry gives *more compact* representations that still outperform larger Euclidean ones. This is a valid and stated design goal, not an oversight. However, the critic has a point that without same-embedding-size comparisons, we cannot fully attribute the improvement to geometry vs. dimensionality (since optimal dimension might differ between Euclidean and hyperbolic models). Still, the comparison direction actually *disfavors* the hyperbolic model (it uses smaller embeddings), so the asymmetry is in the baseline's favor. Per my rules, I should not remove this criticism if it's valid, but I should note that the comparison actually biases *against* the proposed method.

Wait, let me re-read the rule: "REMOVE 'weaknesses' about unfair comparison with other methods if the asymmetry favors the baseline and not the author's method." The hyperbolic models use *smaller* embeddings, so the asymmetry favors the *baselines* (which have larger model capacity). The harsh critic's claim is that we can't attribute the improvement to geometry because dimensions differ. But the paper's design intentionally gave the baselines *more* capacity. The fact that smaller hyperbolic models still outperformed is actually a point in the paper's favor (more compact representations). However, the critic's deeper point remains: we don't know if Euclidean models at d=128 would also do well or even better. The paper should have included same-dimension results to fully isolate the geometry effect. This is a valid concern but is more minor than the critic makes it — the claim about compactness is still supported, just the claim about geometry specifically being the driving factor is not fully isolated.

**Key claim 2: Circular reasoning in "good"/"bad" categorization.**
The paper defines "good" datasets as those with small variance in δ-hyperbolicity (line 194), and then shows that "good" datasets benefit from hyperbolic models. This is somewhat circular because the categorization is based on δ-hyperbolicity characteristics (which are data properties independent of the model), NOT based on whether the model worked. The δ measures are computed from SVD embeddings of the user-item matrix, not from the model's performance. So the categorization is not purely post-hoc based on success — it's based on a structural property of the data. However, the critic is right that no quantitative threshold is given, and the classification was done on the same 4 datasets used for evaluation.

**Key claim 3: No variance reporting.**
Confirmed — the paper reports no standard deviations, confidence intervals, or significance tests for any results in Table 1.

**Other verifications:**
- The "non-zero offset" claim (line 82) is indeed from "preliminary experiments" with no quantitative results.
- Figure 4 shows curvature estimation and quality as a function of ε, but the "quality" part has no quantitative numbers.
- The paper explicitly acknowledges the limitation that "bad" datasets don't benefit (lines 225, 238).

Now let me write the final consolidated review.

## Summary

The paper proposes HSASRec/HSASRecCE, which extend the SASRec sequential recommendation model by replacing its Euclidean prediction layer with a hyperbolic classifier in the Poincaré ball, using the economical (z,r) reparametrization of Shimizu et al. (2021) to avoid full Riemannian optimization. The paper identifies two key factors affecting hyperbolic model performance: (1) negative sampling in BCE loss destroys the popularity hierarchy that hyperbolic geometry exploits, and (2) data compatibility with hyperbolic geometry (measured via stability of δ-hyperbolicity estimation) determines whether hyperbolic models offer gains. On "good" datasets (stable δ), HSASRecCE with small embeddings (32–128) reportedly outperforms SASRecCE with large embeddings (256–728).

## Strengths

- **Clean, minimal architectural modification that isolates geometric effects:** The approach changes only the prediction layer (replacing the Euclidean inner product with a Poincaré ball hyperplane classifier) while keeping all self-attention weights Euclidean. This makes the method easy to adopt and enables clear attribution of performance differences to the geometric change (Section 3.1, Eq. 6). The (z,r) reparametrization avoids the parameter bloat of the full (a,p) parameterization.

- **Identifying loss function compatibility as critical for hyperbolic models:** The analysis that uniform negative sampling creates an anti-popularity bias (Figure 2), which undermines the very structure hyperbolic geometry is meant to capture, is a meaningful and actionable insight. Table 1 confirms that HSASRec (BCE loss) performs poorly across all datasets while HSASRecCE (full cross-entropy) succeeds on compatible datasets, cleanly demonstrating this effect.

- **Machine precision analysis for curvature estimation:** Section 3.3 identifies that the default ε=10⁻⁵ used in prior work yields substantially different curvature estimates than ε=10⁻¹², and Figure 4 shows this directly affects recommendation quality. This is a concrete methodological contribution for practitioners of hyperbolic models.

- **Principled evaluation methodology:** The paper uses global time-point splits and full-item ranking (no subsampling), explicitly citing the problems these practices address (Krichene & Rendle, 2020; Meng et al., 2020), which aligns with best practices for sequential recommendation evaluation.

## Weaknesses

### Fatal
None.

### Major

- **Embedding dimension confound limits causal attribution to geometry:** The paper restricts hyperbolic models to embedding sizes {32, 64, 128} while allowing Euclidean models {256, 512, 728} (Section 4.1). This design purposefully demonstrates compactness — the headline "8–18% improvement" and "~3% improvement over SASRecCE" are achieved with smaller models. While this actually makes the comparison *harder* for the proposed method (the baselines have more capacity), it does not fully isolate the effect of geometry from the effect of dimensionality. Without same-embedding-size comparisons (e.g., SASRec/SASRecCE at d=128), it is impossible to determine whether the gains stem from hyperbolic geometry or from the fact that smaller Euclidean models might also perform well on these datasets (possibly due to overfitting at high dimensions). The paper's claim that hyperbolic geometry itself drives improvements — rather than the match between optimal dimension and model type — requires this control. This affects the core claim in Section 6.2 and the Conclusion.

- **The "good"/"bad" dataset categorization lacks quantitative thresholds and is evaluated on the same datasets used to derive it:** Section 6.1 categorizes datasets as "good" (stable δ-hyperbolicity) or "bad" (unstable δ), and Section 6.2 shows that "good" datasets benefit from hyperbolic models while "bad" ones do not. While the δ-hyperbolicity is computed independently of model performance (from SVD embeddings), the categorization itself — with no quantitative threshold, only visual inspection of convergence patterns (Figures 5–6) — is derived and validated on the same four datasets. This provides no out-of-sample prediction. The paper would be substantially strengthened by pre-specifying a threshold on δ variance and ideally demonstrating it on held-out datasets.

### Minor

- **No variance or significance reporting for evaluation metrics:** Table 1 reports single numbers for all metrics across all models and datasets. Differences of ~3% over SASRecCE on "good" datasets could plausibly fall within run-to-run variance. Standard deviations from multiple seeds would substantially increase confidence in the claimed improvements (Section 6.2).

- **Preliminary claims about non-zero offset lack quantitative support:** The assertion that "the non-zero offset indeed slightly improved the results for the hyperbolic models" (Section 3.1, line 82) is based on unspecified preliminary experiments with no quantitative results. Given that the offset parameter r is an important design choice specific to this paper's implementation, this should be supported with evidence.

- **Disentangling loss function from sampling is incomplete:** Section 3.2 argues that negative sampling hurts hyperbolic models because it destroys hierarchical structure, but the experiment in Table 1 simultaneously changes both the loss function (BCE→CE) and the sampling strategy (sampled→full). While the conceptual argument is compelling, the paper cannot distinguish whether the improvement comes from avoiding sampling bias or from the softmax normalization properties of full CE. A clean ablation (HSASRec with CE but sampled negatives) would resolve this.

## Trivial
None worth noting.

## Nice-to-Haves

- Same-embedding-size experiments (SASRec/SASRecCE at d=128) to fully isolate geometric effects from dimensional effects.
- Ablation on curvature estimation: a table comparing HSASRecCE performance under ε=10⁻⁵ vs. ε=10⁻¹² to quantify the practical impact of the precision finding.
- t-SNE or Poincaré disk visualizations of learned item embeddings for "good" vs. "bad" datasets.
- A quantitative threshold for δ-hyperbolicity stability that could be used as a pre-training criterion.

## Removed Points

- **"The paper explicitly constrains hyperbolic models to embedding sizes {32, 64, 128} while allowing Euclidean models {256, 512, 728}. The claimed 8–18% improvement over the 'original Euclidean baseline' and 3% improvement over SASRecCE are comparisons across fundamentally different model capacities."** — While the dimension mismatch is real, the harsh critic overstates the severity. The asymmetry *favors the baselines* (they have more capacity), so this is not an unfair advantage for the proposed method. The comparison actually makes the paper's point stronger (smaller hyperbolic models beat larger Euclidean ones). The valid concern remains that same-dimension comparisons are needed to isolate geometry, but it is a major weakness, not a fatal one. Kept in reduced form as Major.

- **"As presented, the claim that δ-hyperbolicity predicts success is supported only by the observation that the method works where it works."** — This overstates the circularity. The δ-hyperbolicity is computed from data structure (SVD of user-item matrix), not from model performance. The categorization is based on a structural data property, not directly on results. However, the lack of quantitative thresholds and out-of-sample validation is a real concern. Kept in reduced form as Major.

- **"The paper needs, at minimum, SASRec and SASRecCE results at d=128 (and ideally d=32, 64) to isolate the effect of geometry from the effect of dimension."** — Kept as nice-to-have rather than a required change, since the paper's explicit design goal is to show compact representations.

- **"Missing experiments / appendix"** — The parser strips appendices; removed complaints about missing appendix content (Section C on δ computation).

- **"The introduction implies broader applicability than the experiments ultimately support (2 out of 4 datasets show improvements; 2 show degradation)."** — The abstract explicitly states "under certain conditions" and the paper transparently shows when hyperbolic models hurt. The paper itself identifies the conditions. This is honest scoping, not overclaiming. Removed.

- **"Excluding all newer architectures (BERT4Rec, DuoRec, etc.) to 'isolate the effects of the geometry'" then making "broad claims about 'improving recommendation quality'"** — The paper explicitly acknowledges this scope limitation (Section 4.1, Section 5). The claims are specifically about improvements within the SASRec family, not broadly about all recommendation. Removed as scope creep.

- **Strength finder claims about "achieving competitive or superior quality with significantly smaller embeddings" and "8–18% improvements on 'good' datasets"** — These are accurate but largely recapitulate the paper's own claims. The more substantive version (compactness as a design goal) is kept. The framing as "genuine representational efficiency" is premature without same-dimension comparisons, so the stronger version is removed.

## Novel Insights

The most distinctive insight of this paper is the identification that negative sampling — the standard efficiency technique in BCE-based recommenders — is structurally incompatible with hyperbolic geometry because the sampling-induced anti-popularity bias destroys the hierarchical structure that hyperbolic models are designed to exploit. This creates a previously unarticulated constraint: any model using hyperbolic representations likely needs to operate over the full item catalog in the loss, which limits scalability. The machine precision finding for curvature estimation (ε=10⁻¹² vs. the community default ε=10⁻⁵) is a practical methodological contribution that any practitioner working with Poincaré ball models should be aware of.

## Suggestions

- Run SASRec and SASRecCE at embedding sizes d ∈ {32, 64, 128} to create a same-capacity comparison and isolate the geometric contribution. This is the single experiment that would most strengthen the paper.
- Add standard deviations from 3–5 random seeds to Table 1. Given the reported improvements are in the 3–8% range, variance estimates are essential.
- Define a quantitative criterion for δ-hyperbolicity stability (e.g., coefficient of variation across sample sizes below a threshold) and ideally validate on additional held-out datasets.
- Run HSASRec with full cross-entropy but sampled negatives to disentangle the effect of the loss function from the sampling strategy.

## Score and Decision

The paper makes a clean, well-motivated architectural contribution (hyperbolic prediction layer only, keeping Euclidean self-attention) and provides useful practical insights (machine precision for curvature, sampling incompatibility). However, two major weaknesses — the embedding dimension confound that prevents clean attribution of improvements to geometry, and the lack of quantitative thresholds or out-of-sample validation for the good/bad dataset classification — significantly weaken the core empirical claims. These are addressable in principle (same-dimension experiments, quantitative thresholds), which suggests the work could be strong with revisions rather than being fundamentally flawed. The paper also honestly acknowledges its limitations (transparent about "bad" datasets, honest about scope). On balance, the contribution is promising but not yet sufficiently validated.

Originality: Moderate — applies existing hyperbolic classification machinery to SASRec, with useful engineering insights.
Importance: The question of when hyperbolic geometry helps sequential recommendation is relevant, but the answer is not yet conclusive.
Claim support: Partially supported; the compactness benefit is demonstrated but the geometric attribution is confounded.
Experiments: Methodologically sound evaluation protocol but missing critical same-dimension controls and variance reporting.
Clarity: Well-written, clear presentation of mathematical details.
Community value: Useful practical guidance on curvature estimation and loss compatibility for hyperbolic models.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>