Now I have all the information I need. Let me write the final consolidated review.

---

## Summary

This paper tests whether common sparse autoencoder (SAE) evaluation metrics—particularly auto-interpretability AUROC—can distinguish features from trained transformers vs. randomly initialized ones. Across Pythia models from 70M to 6.9B parameters and multiple randomization schemes (Gaussian re-randomization with/without trained embeddings, Step-0 initialization), the central finding is that aggregate auto-interpretability scores and reconstruction metrics are often similar between trained and random models, especially at larger scales. The paper identifies token distribution entropy as a proof-of-concept measure that does reveal differences, and uses toy models to explore why random networks might preserve or amplify superposition in their activations.

## Strengths

- **Systematic demonstration across model scales**: The paper evaluates five Pythia sizes (70M–6.9B) with five well-motivated variants (Trained, Re-randomized incl./excl. embeddings, Step-0, Control). Figure 1 cleanly shows that for Pythia-6.9b, the trained model and all randomized variants produce overlapping ROC curves (AUC ~0.79–0.88) while only the control (random embeddings) performs at chance (~0.50). This scaling analysis—showing the gap narrows systematically from 70M to 6.9B—goes beyond smaller-scale prior results (Bricken et al., 2023) and is the paper's strongest empirical contribution.

- **Token distribution entropy as a differentiating measure**: The last row of Figure 2 shows that this simple metric cleanly separates trained from random models: trained models show increasing entropy across layers (from ~0.25 to ~0.5 for 6.9b) while randomized variants remain low and flat (~0.2). The paper is appropriately cautious, presenting this as a "proof-of-concept" rather than a fully validated solution, but it concretely demonstrates that not all SAE evaluation is hopeless—targeted measures can capture the "abstractness" that aggregate AUROC misses.

- **Honest and well-scoped claims**: The paper consistently qualifies its findings ("in many settings," "under certain conditions"), explicitly discusses the Bricken et al. (2023) result for small models, and clearly states what it does *not* claim ("SAEs fail to capture information from trained transformers above and beyond randomly initialized transformers"). Section 5 (Limitations) is thorough and appropriately modest.

- **Robustness checks**: The paper confirms the main results hold under different SAE expansion factors (16–128), sparsities (16, 32), training token budgets (Appendix C), and multiple random seeds (Appendix E), suggesting the findings are not artifacts of a single configuration.

## Weaknesses

### Major
None.

### Minor
- **Missing error bars / variance information on primary AUROC results**: The paper samples 100 latents per SAE and reports single curves in Figures 1–2 without any confidence intervals or variance shading. With only 100 samples from thousands of latents, the reader cannot assess whether the observed similarities between trained and random variants are within measurement noise. Appendix E apparently addresses multiple random seeds, but this information should be visualized alongside the main curves. This is the paper's most significant evidential gap—it weakens the central claim proportionally to how noisy 100-sample estimates might be.

- **Token distribution entropy is presented as a solution but not validated**: The paper shows that entropy differentiates trained from random models, but does not validate that entropy correlates with anything we actually care about (e.g., human judgments of feature quality, success in steering/intervention experiments). It is presented as a "proof of concept" which is fair, but the paper's practical recommendation ("develop more targeted measures of feature abstractness") would be significantly stronger if entropy were shown to predict something about downstream feature utility beyond what aggregate AUROC captures.

- **The toy model section (Section 4) is suggestive rather than explanatory**: The paper uses toy MLPs and GloVe vectors to hypothesize why random networks might preserve or amplify superposition, but explicitly defers to future work the question of which mechanism predominates in the language model setting. This is honest but means Section 4 functions primarily as plausibility motivation rather than mechanistic evidence for the main results. The GloVe experiment is a useful bridge but GloVe vectors lack the contextual structure of transformer residual stream activations.

- **Title slightly overstates the finding for small models**: The title "Automated Interpretability Metrics Do Not Distinguish Trained and Random Transformers" is a categorical claim, but the paper's own results show visible AUROC differences for Pythia-70m and 160m between trained (~0.63) and Step-0 (~0.60) or randomized-incl (~0.68). The body appropriately qualifies ("in many settings," "the gap narrows with scale"), making the title a reasonable rhetorical choice but technically imprecise for smaller models.

### Trivial
- The figure descriptions are dense (especially Figure 2's 35 subplots in a 7×5 grid); the text would benefit from more explicit quantitative comparisons (e.g., "the max AUROC difference between trained and Step-0 is <0.02 across all layers for 6.9b") rather than relying on qualitative "overlap" language.

## Nice-to-Haves
- The "Re-randomized incl. embeddings" variant uses Gaussian noise sampled with mean/variance matching each trained weight matrix. A permutation/shuffling baseline would preserve the exact marginal distribution of weights rather than matching only first two moments. The results are consistent across randomization schemes so this is unlikely to matter, but it would tighten the methodology.
- A downstream utility check (e.g., do SAE features from random models produce meaningful steering effects?) would directly assess whether the similar AUROC scores represent a practical failure or just a theoretical concern.
- Reporting per-layer maximum absolute difference in AUROC between trained and each random variant would be more rigorous than visual inspection.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **Harsh Critic's claim that the "randomized excl embeddings" variant "partially undermines the claim"**: This criticism is factually backwards — the randomized excl embeddings variant actually shows **higher** AUROC than the trained model (0.87 vs. 0.79 in Figure 1), which *strengthens* the paper's claim that these metrics fail to distinguish trained from random computation. The paper already acknowledges this variant's properties clearly (Section 2's discussion of Zhong and Andreas). The critic's framing suggests this weakens the paper when in fact it makes the case more striking.

- **Strength Finder's generic strength "Systematic evidence that the discriminability problem scales with model size"**: This is actually a valid and specific concrete strength, so I will keep it in Strengths.

- **Strength Finder's "Robustness checks across multiple hyperparameter settings"**: The core claim about hyperparameter robustness references Appendix C and Figure 18, which are appendix-stripped. The paper's main text does state these checks were performed, so I will keep this as a supporting strength but note it's dependent on appendices for verification.

- **Harsh Critic's "The control condition... is a useful sanity check but..."**: This is a clarification, not a weakness. The paper already positions the control as a lower-bound sanity check, which is entirely appropriate. The critic acknowledges this.

## Novel Insights

The most novel insight from the reviews is the observation that the randomized-excluding-embeddings variant (which retains trained embeddings but randomizes all other weights) can produce **higher** AUROC scores than the fully trained model. This is a stronger result than the paper's headline: it suggests that auto-interpretability metrics may not merely fail to distinguish trained computation, but can actually be *misled* by structured embeddings combined with random computation into producing *inflated* scores. This inversion—where more "interpretable" latents come from a less capable model—is a sharper critique of aggregate auto-interpretability than the paper's own framing emphasizes. None beyond the paper's own contributions.

## Suggestions
- Add confidence intervals or variance shading to the main AUROC figures (bootstrap across sampled latents or show multiple random seeds as separate curves) so readers can assess whether the observed similarities are within noise.
- Either validate token distribution entropy against a ground-truth task (e.g., does low entropy predict weaker steering effects?) or reframe it more clearly as purely exploratory rather than a recommended alternative metric.
- Add a short quantitative summary (e.g., per-layer max absolute AUROC difference between trained and each random variant) to complement the visual comparisons in Figures 1–2.
- Consider a slightly more nuanced title that reflects the scaling trend (e.g., "Aggregate Auto-Interpretability Metrics Often Fail to Distinguish Trained from Random Transformers at Scale").

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak anchor: `/home/wg25r/split_review/datasets/deepreview_13k_calibration/89wVrywsIy.md` (avg 3.40) — "Automatically Identifying and Interpreting Sparse Circuits." Weak paper with unclear contributions and missing baselines. The paper under review is substantially stronger.
- Weak anchor: `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Wxl0JMgDoU.md` (avg 2.50) — SAE on chess model. Very weak.
- Middle anchor: `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9ca9eHNrdH.md` (avg 7.00) — "Sparse Autoencoders Do Not Find Canonical Units of Analysis." Methodologically novel paper introducing SAE stitching, meta-SAEs, and BatchTopK. Strong experiments and clear contribution. The paper under review is less methodologically novel but also well-executed; slightly weaker overall.
- Middle anchor: `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1Njl73JKjB.md` (avg 7.00) — "Towards Principled Evaluations of Sparse Autoencoders." Introduced supervised dictionaries for SAE evaluation. Limited to one task but well-executed. Comparable quality to the paper under review.
- Strong anchor: `/home/wg25r/split_review/datasets/deepreview_13k_calibration/tcsZt9ZNKD.md` (avg 8.20) — "Scaling and evaluating sparse autoencoders." Landmark paper with new architecture, scaling laws, training on GPT-4. The paper under review is not at this level of ambition or impact.

**Round 2 (Narrowing):**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MDvecs7EvO.md` (avg 6.50) — "Mechanistic Permutability." Introduced SAE Match. Solid execution but some methodological concerns about generalization. The paper under review is comparable in quality.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/XAjfjizaKs.md` (avg 6.50) — "Residual Stream Analysis with Multi-Layer SAEs." New SAE variant, clean experiments. The paper under review is of similar quality.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5lIXRf8Lnw.md` (avg 5.50) — "Automatically Interpreting Millions of Features." Rejected; had issues with correlation between scoring methods. The paper under review is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/sknUS8X9q0.md` (avg 4.00) — "SAGE." Rejected for confusing presentation. The paper under review is much clearer and better structured.

The paper is clearly above the 4.0–5.5 rejected papers in terms of experimental design, clarity, and validity of contribution. It is slightly below the 7.0 papers in terms of methodological novelty (those papers introduced new techniques; this paper runs a well-designed sanity check). It is comparable to the 6.5 papers in execution quality. The main weaknesses (no error bars, preliminary entropy measure) are addressable and do not threaten the core claim. Final score: 6.0 — a solid paper that makes a clear, important point and should be accepted.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>