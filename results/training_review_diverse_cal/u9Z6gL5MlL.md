Now I have a thorough understanding of the paper and all review claims. Let me produce the consolidated review.

---

## Summary

This paper re-examines two widely held beliefs about memorization in deep learning — that over-parameterization and increased training time increase memorization — which were derived from experiments using *artificial* memorization (noisy labels/inputs). Using the computationally expensive leave-fraction-out method (Feldman & Zhang, 2020) on CIFAR-10/100 and Tiny ImageNet with VGG, ResNet, and ViT models, the authors find the opposite: deeper models memorize *fewer* natural points, and memorization exhibits a transient rise-and-fall pattern within standard training (100 epochs). The paper also reports a Pearson correlation of 0.99 between memorization count and train-test gap, and concludes that memorization is not necessary for generalization.

## Strengths

1. **Demonstrates that over-parameterization reduces natural memorization, directly contradicting the artificial-memorization prediction.** Figure 1 and Tables 1–2 show a consistent negative relationship: SmallVGG memorizes more points than VGG19, ResNet18 more than ResNet50, and ViT-Tiny more than ViT-Small. This pattern holds across three datasets and three architecture families, providing a clear empirical rebuttal of a belief derived from artificial proxies.

2. **Reveals a non-monotonic (transient) relationship between training iterations and natural memorization.** Figure 2 shows three stages — no memorization (early epochs), rising memorization (e.g., LargeVGG on CIFAR-100 peaks at ~8,300 points at epoch 77), then declining memorization (falling to ~6,400 by epoch 99). This contrasts with the artificial-memorization pattern where memorization increases monotonically with training.

3. **Identifies and characterizes transient memorization as a phenomenon.** Section 4.3 quantifies model-wise and temporal-wise transient points, showing they consist of samples from smaller sub-populations (average memorization score 44.99% ± 15.02% vs. dataset average 11.17% ± 19.13%). This provides a more nuanced understanding of how memorization evolves with model capacity and training time.

4. **Provides a principled critique of the artificial-memorization proxy.** Section 1 lists four concrete, documented reasons why artificial memorization (noisy labels/inputs) diverges from natural memorization: extreme outliers, focus on mislabeled points, overlooking small sub-populations, and altered training procedures (excessive iterations). This clearly motivates the paper's re-examination.

5. **Employs a large-scale experimental setup following Feldman & Zhang's methodology.** Training 2,000 models per architecture, using proper data augmentation and weight decay (avoiding undertraining), and replicating across three datasets and three architecture families provides a reasonably solid empirical foundation.

## Weaknesses

### Fatal
None.

### Major

1. **The claim that "memorization is not necessary for generalization" overreaches the evidence.** The paper states this as a broad finding (abstract, Section 5), but the evidence shows only that in *these specific settings* (standard vision datasets, architectures trained for 100 epochs), reducing memorization is compatible with improving generalization — indeed the two move together. This is a correlational finding. The paper does not address the long-tail subpopulation scenario central to Feldman & Zhang's argument, where subpopulations of size 1–3 may genuinely require memorization. The transient points studied have average memorization scores of 35–45%, meaning they belong to *moderately* small subpopulations — not the extreme tail where the "necessity" question is most contested. The conclusion therefore conflates "not necessary in the settings tested" with "not necessary" simpliciter.

2. **The Pearson correlation of 0.99 is reported without essential context.** The paper presents this extraordinary value (abstract, Figure 3, Sections 4.4 and 5) without stating the number of data points it is computed from, whether it is pooled or per-dataset, or any confidence interval. If it is computed from 8–9 model configurations, this is a very small sample and the value is fragile. A scatter plot showing the actual data points would help readers assess the relationship directly. Without this context, the statistic is opaque and carries less weight than the paper assigns it.

### Minor

3. **Within each architecture family, parameter count is varied through depth, not isolated as an independent variable.** While the paper states it "keeps the architecture family constant" (line 75), varying depth in VGG (SmallVGG → VGG19) changes not just parameter count but also the model's inductive bias, feature hierarchy, and learning dynamics. A cleaner test of "parameter count *per se*" would vary width at fixed depth. This does not invalidate the main empirical finding — which still shows that larger models memorize fewer natural points — but it weakens the causal attribution to "over-parameterization" specifically.

4. **The training-horizon evidence is limited.** The claim that memorization declines with further training is based on a single 22-epoch window (epochs 77–99). The paper asserts "if the model is trained for long enough, the memorization rate will eventually fall" (line 98), but does not show training beyond 100 epochs. The decline could be a temporary dip before a later rise (epoch-wise double descent is explicitly invoked, yet the paper stops before a second potential rise). Running to convergence or at least 200+ epochs would substantiate the claim of a sustained decline.

5. **The paper attributes reduced memorization to "improved feature learning" without mechanistic evidence.** Sections 4.3 and 5 repeatedly assert that larger/longer-trained models "learn better features" or "learn rare patterns," but provide no representation analysis, probing, nearest-neighbor inspection, or activation visualization to support this explanation. The claim is plausible but untested; the "transient memorization" phenomenon remains a descriptive observation rather than a mechanistically explained one.

6. **The natural vs. artificial distinction is potentially confounded by real-world label noise.** CIFAR-10/100 and Tiny ImageNet are known to contain mislabeled examples. Points memorized because of erroneous labels would, by the paper's own framing, be closer to "artificial" (noisy-label) memorization than to memorization of genuinely informative outliers or small sub-populations. The paper assumes all naturally memorized points are "correctly labeled" samples from small sub-populations, but does not check this. A non-trivial fraction of memorized points could reflect dataset errors, muddying the claimed distinction.

7. **The standard deviations of memorization scores suggest substantial overlap between transient and average points.** The paper reports transient points at 44.99% ± 15.02% vs. dataset average 11.17% ± 19.13%. The large standard deviations mean many individual transient points have scores within the range of the overall distribution. The paper does not perform a statistical test (e.g., a t-test or Kolmogorov–Smirnov) to confirm these distributions are significantly different, which weakens the characterization of transient points as a distinct category.

### Trivial

- The text does not always specify which dataset a given figure panel (e.g., Figures 1–3) corresponds to, sometimes relying on reader inference from surrounding text.
- The paper switches between "over-parameterization" and "model complexity" without consistent operationalization of what is being varied.

## Nice-to-Haves

- **Isolate parameter count from depth** by varying width within a single architecture (e.g., a ResNet block with differing channel multipliers at fixed depth).
- **Train significantly beyond 100 epochs** (300–500 or until convergence) to verify whether the Stage 3 decline in memorization is stable or merely a temporary dip.
- **Quantify label noise contribution** by cross-referencing memorized points against known CIFAR/ImageNet mislabels, and report results separately for clean and noisy points.
- **Add mechanistic evidence** for the "improved feature learning" claim, such as probing classifier accuracy on representations, nearest-neighbor analysis in feature space, or visualizing activation patterns for transient points before and after the transition.
- **Provide a scatter plot** for the correlation analysis with model-level data points labeled, along with per-dataset correlation values and confidence intervals.

## Removed Points

These points were raised by reviewers but removed or downgraded after verification against the paper. They are listed here for completeness but do not affect the assessment.

- **"Over-parameterization claim confounds parameter count with architectural depth"** (critic's major weakness) — Downgraded to minor (see Weakness #3 above). The paper *does* keep architecture family constant within each comparison. The critic overstates this as a structural flaw when it is a standard methodological limitation.
- **"Transient memorization is less novel than claimed"** — Removed. This is a subjective opinion on novelty. The paper explicitly acknowledges the connection to epoch-wise double descent (line 98) and differentiates itself by showing the correction occurs within standard (100-epoch) training rather than requiring thousands of extra epochs. The critic provides no specific argument for why the overlap is inadequately addressed beyond asserting it.
- **"The paper would benefit from a controlled comparison with and without artificial memorization points"** — Removed. This is a suggestion for a different paper design (testing interference between artificial and natural memorization) rather than a weakness in the paper as written. The paper's thesis is about divergence, not interaction.
- **"Figures 1–3 appear to show specific datasets per panel and the text does not always specify"** — Moved to Trivial. The paper does specify datasets in the surrounding text for most panels; the issue affects at most one or two references and does not impede comprehension.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Temper the central conceptual claim.** Replace "memorization is not necessary for generalization" with a more precise statement: "In the standard-vision-dataset settings studied, reducing natural memorization is compatible with — and indeed accompanied by — improved generalization. The long-tail subpopulations where Feldman & Zhang argued memorization is necessary exhibit transient memorization that resolves with larger models or longer training." This would align the claim with the actual evidence and avoid overreach.

2. **Report the correlation with full statistical context.** State N per correlation, provide 95% confidence intervals, show a labeled scatter plot, and report the correlation separately for each dataset (not just pooled). This would allow readers to assess how robust the 0.99 value is.

3. **Run a control experiment varying model width (not depth)** within a single architecture family to isolate the effect of parameter count from depth-induced inductive bias changes. This would directly answer the critic's concern while the finding would either strengthen or qualify the existing claim.

4. **Acknowledge and discuss the label-noise confound explicitly** as a limitation, and ideally quantify it by checking whether memorized points overlap with known CIFAR/ImageNet mislabels.

## Score and Decision

**Originality:** The paper identifies a real gap — the divergence between artificial and natural memorization — and presents counterintuitive findings (larger models memorize *fewer* natural points). The transient memorization phenomenon is a useful descriptive contribution, though it builds on known ideas (epoch-wise double descent).

**Importance of the research question:** Important. The artificial-memorization proxy is widely used, and demonstrating that it yields qualitatively different conclusions is a meaningful contribution that should influence experimental practice.

**Soundness of experiments:** The experimental design (following Feldman & Zhang's leave-fraction-out method, 2,000 models per architecture, three datasets, three architecture families) is solid in scale and methodology. However, two central interpretation claims go beyond what the evidence supports (the "not necessary" claim and the 0.99 correlation without context). The mechanistic explanation for transient memorization ("improved feature learning") is asserted without evidence.

**Clarity of writing:** The paper is clearly organized and generally readable, though it could benefit from more consistent dataset labeling in figures.

**Value to the community:** High. The finding that commonly held beliefs about memorization reverse when studied on natural rather than artificial points should encourage researchers to re-examine conclusions drawn from the proxy. However, the overclaimed "memorization not necessary" conclusion may mislead if taken at face value.

The paper's core empirical contribution — that over-parameterization and longer training *reduce* natural memorization, contrary to artificial-memorization findings — is valuable and reasonably well-supported. However, two major weaknesses (the overreaching "not necessary" claim and the poorly contextualized correlation statistic) undermine the paper's strongest interpretive claims. These are addressable: tempering the claims to match the evidence and reporting the correlation with proper context would largely resolve them. The remaining issues are standard methodological limitations. The paper makes a real contribution and should be accepted contingent on revising these overclaims.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>