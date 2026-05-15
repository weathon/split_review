Now let me write the final consolidated review.

## Final Consolidated Review

Let me carefully verify each point against the paper text before including it.

## Summary
The paper proposes CONTROL, a contrastive learning framework for Open World Semi-Supervised Learning (OWSSL). CONTROL integrates three contrastive objectives—supervised contrastive loss (\(\mathcal{L}_{\mathrm{SupSeen}}\)), nearest-neighbor contrastive loss (\(\mathcal{L}_{\mathrm{SupNN}}\)), and unsupervised contrastive loss (\(\mathcal{L}_{\mathrm{SimAll}}\))—as add-on modules to BCE-based OWSSL methods. The paper claims theoretical justification that contrastive learning at the feature level is less affected by misaligned nearest-neighbor pairs than BCE loss, and that uniformity in contrastive loss prevents unseen-class collapse. Experiments on CIFAR-10, CIFAR-100, and ImageNet-100 show improvements over ORCA and NACH baselines.

## Strengths
1. **Well-motivated problem framing and practical contribution**: Open-world semi-supervised learning is a realistic and timely problem. The paper correctly identifies that misaligned seen-unseen nearest-neighbor pairs degrade BCE-based methods, and proposes a simple, modular solution (adding three contrastive losses) that can be plugged into existing BCE-based methods. The framework architecture (Fig. 4) is clean and the design rationale is clearly explained.

2. **Consistent empirical improvements on unseen-class accuracy**: CONTROL+NACH improves unseen-class accuracy by 6.4% on CIFAR-100 and 2.2% over the prior contrastive method OpenCon (Table 1). Similar gains are reported on ImageNet-100 (Table 2). These gains are non-trivial for a field where improvements of a few percentage points are meaningful.

3. **Ablation studies confirm individual contributions of each loss component**: Table 3 shows that \(\mathcal{L}_{\mathrm{SupSeen}}+\mathcal{L}_{\mathrm{SimAll}}\) yields +2.7% unseen accuracy and +1.1% all-class accuracy, and adding \(\mathcal{L}_{\mathrm{SupNN}}\) yields further gains. This validates the design rationale that each contrastive objective plays a distinct role.

4. **Diagnostic evidence supports the claimed mechanism**: Table 4 directly measures the ratio of unseen-class predictions and unseen-unseen nearest-neighbor pairs, showing that CONTROL reduces seen-unseen confusion. This is more concrete than accuracy numbers alone and connects the framework design to observable behavior.

## Weaknesses

### Fatal
None.

### Major
1. **The theoretical derivation in Section 4.1 does not withstand scrutiny and undermines the paper's claim of a principled foundation.** The paper lists theoretical justification as a core contribution (line 40: "theoretically demonstrate that the proposed CONTROL can not only enhance the classification of BCE loss but also avoid unseen classes collapse"). However, the derivation has two serious gaps:

   - **Unjustified collapse to \(\log(|\mathcal{N}(x)|)\)**: The derivation in lines 132-135 transitions from expectations over \(\phi(x)^\top\cdot\phi(v^-)/\tau\) to the constant \(\log(|\mathcal{N}(x)|)\) with the single statement "the last equation holds because \(\phi(x)\), \(\phi(v^+)\), and \(\phi(v^-)\) are independent." Even granting independence, the step from \(\mathbb{E}_{x,v^-}\log\sum\exp(\phi(x)^\top\phi(v^-)/\tau)\) to \(\log(|\mathcal{N}(x)|)\) requires assuming that all dot products are zero in expectation—i.e., that features are uniformly distributed on the hypersphere and centered at the origin. This assumption is neither stated nor defended, and it is unlikely to hold during training.

   - **Problematic BCE loss derivation**: The claim on line 127 that independent logits imply \(g(\phi(x))^\top g(\phi(v)) = 0\) (and thus \(M \to -\infty\)) is also unsupported. Independent random vectors can have non-zero dot products; the expectation would be zero only under an additional zero-mean assumption that is not established.

   **Why this matters**: The theoretical argument is presented as a key differentiator of the paper (line 40: third contribution). If the derivation is not valid, this claimed contribution is unsupported. The empirical results still have value, but the paper significantly overstates its theoretical contribution.

2. **The claim of being a "unified framework compatible with a broad range" of OWSSL algorithms is not supported by the evidence.** The abstract (line 4) and contribution list (line 39) claim broad compatibility. However, experiments only combine CONTROL with two BCE-based methods (ORCA and NACH). Non-BCE methods (OpenLDN, TRSSL) are discussed in related work (lines 22, 50) but never tested with CONTROL. The paper also compares against OpenCON as a baseline (Table 1) but does not demonstrate CONTROL as a plug-in to OpenCON. **If CONTROL is designed specifically for BCE-based methods, that should be stated as a scope condition rather than claiming broad generality.**

3. **The large performance gap between ORCA* and NACH* improvements is unexplained.** On CIFAR-100 unseen classes, CONTROL+ORCA* improves by 11.8% (per line 221), roughly double the 6.4% gain over NACH*. While different baselines can have different headroom, the paper provides no analysis or discussion of this discrepancy. This matters because it raises questions about whether the claimed mechanism (enhancing BCE via feature-level alignment) accounts for the gains uniformly, or whether other factors (e.g., baseline stability, hyperparameter tuning) are responsible.

### Minor
1. **No error bars or variance reported.** All results are described as "average of three runs" (lines 213, 221, 245), but no standard deviations, confidence intervals, or per-run ranges are provided. Without measures of variance, it is impossible to assess whether the reported improvements are statistically significant or within the noise of the experimental setup.

2. **No hyperparameter sensitivity analysis.** The final loss (Eq. 11) has three weighting parameters \(\lambda_1, \lambda_2, \lambda_3\) and a temperature \(\tau\). The paper reports ablation of which losses matter (Table 3) but never examines sensitivity to specific hyperparameter values. It is unclear whether the same settings work across datasets and baselines, or how they were selected. Given that some gains are modest (e.g., 2.1% all-class on NACH CIFAR-100), robustness to hyperparameter choices matters.

3. **The uniformity-to-collapse-prevention argument (Section 4.2) is asserted rather than rigorously supported.** The paper invokes Wang & Isola's decomposition of contrastive loss into alignment + uniformity (line 164-170) and then claims "by avoiding feature-level collapse, the contrastive losses also avoid logit-level collapse of the unseen classes" (line 172). The step from feature uniformity to logit-level collapse avoidance relies on the unspecified mapping \(g(\cdot)\) "maintain[ing] the spatial structure" — a relationship that is never formalized or empirically tested. The intuition is plausible, but the paper does not directly measure feature collapse or uniformity in its experiments (e.g., average pairwise cosine similarity of unseen-class features).

### Trivial
None.

## Nice-to-Haves
- Combining CONTROL with a non-BCE method (OpenLDN or TRSSL) would substantially strengthen the generality claim, even if only as a small-scale experiment.
- Adding a hyperparameter sensitivity plot (e.g., accuracy vs. \(\lambda_3\) or \(\tau\)) would improve reproducibility confidence.
- Directly measuring feature uniformity (e.g., using the metric from Wang & Isola 2020) on unseen-class features for baselines vs. CONTROL would substantiate the uniformity argument in Section 4.2.

## Removed Points
- **The claim that the 2.35-2.77% improvements in Table 4 are "inconsistent" with the 6.4% unseen-class accuracy improvement**: This criticism reflects a misunderstanding. Table 4 measures *different quantities* (ratio of unseen samples predicted as any unseen class, and ratio of unseen-unseen nearest-neighbor pairs) than the accuracy metric in Table 1. There is no inconsistency.
- **The claim that the paper should combine CONTROL with OpenCON**: The paper presents OpenCON as a baseline competitor, not a method to be combined. CONTROL is designed to plug into BCE-based methods that already have \(\mathcal{L}_{\mathrm{CE}} + \mathcal{L}_{\mathrm{BCE}} + \mathcal{L}_{\mathrm{Entropy}} + \mathcal{L}_{\mathrm{Balance}}\); OpenCON uses only contrastive loss and operates differently. The paper never claims CONTROL can be combined with OpenCON.
- **The claim that the independence assumption in the theory is fundamentally wrong**: The \(\eta\)-component of the mixture model \(\mathrm{P}_{XV}^\eta\) treats \(x\) and \(v\) as independently sampled from marginals — this is the model's representation of a *misaligned* pair. Under this model, \(\phi(x)\) and \(\phi(v)\) are indeed independent (deterministic functions of independent random variables). The deeper issue (which is kept in the main weaknesses) is the unjustified collapse to \(\log(|\mathcal{N}(x)|)\), not the independence claim per se.
- **Several minor formatting nitpicks** from the harsh critic (not reproduced here) — these are parser artifacts, not author errors.
- **Strength Finder's claim that the theoretical proof is a core strength**: This conflicts with the verified weakness that the derivation is flawed, so it is removed per instructions.

## Novel Insights
The reviews collectively reveal that the paper's most valuable contribution is its *empirical demonstration* that combining feature-level contrastive objectives with logit-level BCE objectives yields meaningful improvements in OWSSL. The theoretical framing, while intuitively appealing, is presented as a formal proof that does not hold up under scrutiny — the key step collapsing expectations to \(\log(|\mathcal{N}(x)|)\) is simply asserted without justification, and the BCE-side derivation also relies on unstated zero-mean assumptions. Rather than pursuing a formal proof that may not be salvageable, the paper would benefit from being reframed around its empirical findings with the theoretical section repositioned as intuitive motivation (which is what it actually provides). The ablation study (Table 3) and diagnostic analysis (Table 4) are the paper's strongest evidence, and expanding this line of analysis — directly measuring feature uniformity and the impact of each loss on the feature space — would be more valuable than patching the current theory.

## Suggestions
1. **Reframe or substantially rewrite the theoretical section (Section 4.1).** The current derivation claims mathematical rigor but relies on unjustified simplifications (collapsing expectations to \(\log(|\mathcal{N}(x)|)\), zero-dot-product assumptions). Either: (a) provide a rigorous derivation with stated assumptions and verified steps, or (b) reposition the section as intuitive motivation/analysis rather than formal proof, and remove "theoretically demonstrate" from the contribution list.
2. **Tone down the generality claims.** Change "compatible with a broad range of existing open-world semi-supervised learning algorithms" to "compatible with BCE-based open-world SSL algorithms" (matching what is actually tested). If the authors wish to retain the broader claim, add at least one experiment with a non-BCE method (e.g., OpenLDN).
3. **Report standard deviations or per-run ranges** for all main results (Tables 1, 2). Three runs is sufficient to estimate variance, but the variance itself must be reported for readers to assess reliability.
4. **Add a hyperparameter sensitivity analysis** — at minimum, a brief table or plot showing accuracy over a range of \(\lambda_3\) and \(\tau\) values on one dataset.
5. **Directly measure feature collapse/uniformity** on unseen-class features (e.g., average pairwise cosine similarity, or the uniformity metric from Wang & Isola 2020) for baselines vs. CONTROL. This would directly substantiate the claim in Section 4.2.
6. **Discuss the ORCA* vs. NACH* improvement gap** — even a brief analysis of why ORCA benefits more (weaker baseline? more headroom? different hyperparameter sensitivity?) would improve transparency.

## Score and Decision
MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>