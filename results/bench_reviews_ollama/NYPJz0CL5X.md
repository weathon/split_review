Now I have a thorough understanding of the paper. Let me synthesize the review.

Key observations:

1. **RFF connection**: The encoding $\vec{B}_x = e^{i\vec{\theta}_x/w_x}$ with $\theta \sim \mathcal{N}(0,1)^D$ is indeed Random Fourier Features (Rahimi & Recht, 2007). The paper cites Bochner (1946) but not RFF. This is a legitimate concern — the paper presents this as a novel "universal hyperdimensional encoding method" but it is essentially RFF applied to HDC. However, the paper *does* apply this in the specific context of HDC and analyzes how the bandwidth affects learning vs. cognition differently. So the RFF connection is real but the paper's contribution may be more about the analysis framework than the encoding itself.

2. **Separation metric contradiction**: The paper defines $s = (\mu_2 - \mu_1)/(\sigma_1 + \sigma_2)$ in Section 4 (Eq. 3). The text says $s$ decreases as $w$ increases (Section 4, line 96). For decoding, small $w$ gives high accuracy and high $s$ (low $w$ → high $s$ → high accuracy). Then in Section 7.3 (line 156): "When the separation metric is low, the accuracy is high." This seems to contradict the framework: the framework says high $s$ = less overlap = better decoding, but Section 7.3 says low separation = high accuracy. Wait, let me re-read this more carefully.

Actually, looking at the context — in Section 7.3, the "separation metric" being discussed is specifically about *decoding* separation. The separation $s(w)$ for decoding decreases as $w$ increases (Fig 5a). Decoding accuracy also increases as $w$ decreases. So both $s$ and accuracy are high for small $w$. But Section 7.3 says "When the separation metric is low, the accuracy is high." That IS contradictory. When $w$ is small, both $s$ is high AND accuracy is high. When $w$ is large, both $s$ is low AND accuracy is low. So saying "low separation, high accuracy" contradicts the framework.

Wait, let me re-read the exact quote again: "When the separation metric is low, the accuracy is high. The correlation, however, loses meaning when the separation is large and the accuracy is high because at these levels the overlap will vary randomly for different data sets."

Hmm, this is confusing. Let me think about what they might mean. Perhaps they mean something about the *correlation* relationship being the reverse? Or maybe there's a specific context where they're referring to a different kind of separation?

Actually, re-reading more carefully: they might be talking about the fact that in the decoding context, when $w$ is very small (high exclusivity), the separation $s$ is high and accuracy is high. But the way they wrote it says "When the separation metric is low, the accuracy is high" — this is clearly contradictory to their own framework. Looking at Fig 5(a), they say separation $s$ decreases as $w$ increases. In Fig 7(a), accuracy decreases as $w$ increases. So both decrease with $w$ — they are positively correlated, not inversely. The statement in Section 7.3 seems to be an error.

3. **$N(p\mu_{12}, \sqrt{p}\mu_{12})$ typo**: Line 107 states the cross-class distribution as $N(p\mu_{12}, \sqrt{p}\mu_{12})$. But the standard deviation should use $\sigma_{12}$ (as used in the separation formula on line 113), not $\mu_{12}$. This appears to be a typo in a key equation.

4. **Experiments only on MNIST**: True, but this is an exploratory/analysis paper, not a benchmarking paper. The MNIST experiments serve to demonstrate the theoretical concepts. More datasets would be better but this isn't fatal.

5. **Comparison with HDC baselines**: The paper doesn't compare against other HDC encoders. This is a legitimate concern but the paper's focus is on understanding encoding properties, not beating baselines.

6. **65% baseline on MNIST**: The 65% is not a comparison against other methods — it's the accuracy with poorly-chosen encoding parameters ($w$ too small), which then improves to 95% with better-chosen parameters. The comparison is within the same framework showing that encoding choice matters.

7. **Independence assumption in $\sqrt{p}$ result**: The CLT derivation assumes independence of the bundled vectors, but correlated encodings (large $w$) create correlations between bundled vectors. This is a legitimate theoretical concern.

8. **The paper cites Rahimi et al. 2018** but that's for an HDC application paper, not for the RFF paper (Rahimi & Recht, 2007). The RFF connection is not acknowledged.

Let me now write the final review.</think>Now I have a thorough understanding of the paper. Let me write the final consolidated review.

## Summary

This paper proposes a tunable kernel-based encoding method for Hyperdimensional Computing (HDC) that interpolates between "correlative" encoding (suitable for learning) and "exclusive" encoding (suitable for cognition/decoding) by adjusting Gaussian kernel length-scale parameters $w_x, w_y$. The encoding maps pixel positions to hypervectors via $\vec{B}_x = e^{i\vec{\theta}_x/w_x}$, $\vec{B}_y = e^{i\vec{\theta}_y/w_y}$, and the paper analyzes a separation metric to study how these parameters affect decoding accuracy, classification performance, and factorization in resonator networks. Experiments on binarized MNIST demonstrate that decoding favors small $w$ while learning benefits from moderate-to-large $w$.

## Strengths

- **Tunable continuum between correlative and exclusive encoding**: The paper provides a clean, continuous mechanism to interpolate between correlative and exclusive HDC encodings via a small number of kernel parameters, which is more principled and flexible than switching between qualitatively different encoders. The formulation $B_x^X = e^{i\theta_x \cdot X / w_x}$ with tunable $w_x$ is straightforward and well-motivated for the HDC context.

- **Theoretical framework with separation metric**: The derivation of the separation metric $s = (\mu_2 - \mu_1)/(\sigma_1 + \sigma_2)$ and its dependence on $w$ for decoding (Section 4, Eq. 3) and the $\sqrt{p}$ scaling for memorization (Section 5, Eq. 4) provide useful analytical tools for HDC practitioners to reason about encoding parameter choices.

- **Qualitative demonstration of opposing encoding requirements**: Figures 7 and 8 provide empirical evidence that decoding accuracy drops for $w > 0.75$ while learning accuracy peaks at intermediate $w \approx 0.5$, confirming the theoretical prediction that the two tasks require different encoding regimes.

- **Factorization ablation (Section 7.5)**: The experiment systematically varying $w$ for individual factors in the resonator network provides a clear causal demonstration that correlation in individual factors directly destroys factorization ability.

## Weaknesses

### Fatal
None.

### Major

- **The proposed encoding is Random Fourier Features without acknowledgment**: The encoding $\vec{B}_x = e^{i\vec{\theta}_x/w_x}$ with $\theta \sim \mathcal{N}(0,1)^D$ is precisely the Random Fourier Feature mapping of Rahimi & Recht (2007), which constructs explicit feature maps for shift-invariant kernels via Bochner's theorem. The resulting similarity $\delta(B_x^{X_1}, B_x^{X_2}) \approx k((X_1-X_2)/w_x)$ is the Gaussian RBF kernel. The paper cites Bochner (1946) but not the RFF paper, and presents the encoding as a novel "universal hyperdimensional encoding method" (abstract and contributions list). The "tunable knobs" $w_x, w_y$ are Gaussian kernel bandwidth parameters well-known in kernel methods. While the paper applies this encoding to HDC-specific analysis (separation metric for learning vs. decoding), the encoding itself is not new. This misattribution undermines the paper's first claimed contribution.

- **The central claimed theoretical insight is a restatement of well-known kernel bandwidth principles without acknowledgment**: The paper's main discovery—that learning benefits from correlated/wide-bandwidth encodings while decoding requires exclusive/narrow-bandwidth encodings—is equivalent to the established principle in kernel methods that classification benefits from larger kernel bandwidths (smoothing local variation) while density estimation/reconstruction requires small bandwidths. The paper presents this as "the first rigorous theoretic analysis" of fundamental HDC requirements (line 23), but the underlying principle is a direct consequence of the encoding being a kernel method. The $\sqrt{p}$ scaling result (Eq. 4) depends on an independence assumption for bundled vectors that is violated precisely in the correlated encoding regime being analyzed (see below), further weakening the theoretical novelty.

- **Independence assumption in the $\sqrt{p}$ scaling result is violated in the correlated regime**: The derivation in Section 5 uses the Central Limit Theorem to obtain $N(p\mu_1, \sqrt{p}\sigma_1)$, assuming the $p$ bundled hypervectors contribute independently. However, under correlated encoding (large $w$), the bundled vectors share significant pairwise correlation, violating the independence requirement of the CLT. This is exactly the regime the paper claims is beneficial for learning. The theoretical result $s \propto \sqrt{p}$ therefore does not hold under the conditions where it is most needed.

- **Experimental evaluation is limited**: All experiments use only binarized MNIST. The 65%→95% classification improvement is achieved by tuning $w$ within the same framework, not by comparing against other HDC encoders or standard baselines. The 65% baseline is quite poor for MNIST (even simple HDC methods typically achieve higher), making the improvement claim uninformative about competitiveness. No results on continuous-valued decoding, more complex datasets, or real cognitive tasks are provided, limiting the generalizability of the findings.

### Minor

- **Contradictory statement about separation metric in Section 7.3**: The text states "When the separation metric is low, the accuracy is high," but the framework defines separation $s = (\mu_2 - \mu_1)/(\sigma_1 + \sigma_2)$ such that higher $s$ means less overlap (better discrimination). Section 4 confirms $s$ decreases with $w$ while decoding accuracy also decreases with $w$ (both are positively correlated). The quoted statement from Section 7.3 thus directly contradicts the paper's own framework and figures. This appears to be a careless error rather than an intentional claim, but it creates confusion about the relationship between the metric and accuracy.

- **Typo in key equation**: In Section 5 (line 107), the cross-class distribution is written as $N(p\mu_{12}, \sqrt{p}\mu_{12})$, using the mean $\mu_{12}$ as the standard deviation. The separation formula (Eq. 4) uses $\sigma_{12}$ in the denominator, suggesting this should be $N(p\mu_{12}, \sqrt{p}\sigma_{12})$.

- **Data-driven heuristic for $w$ selection is validated only on one dataset**: The proposal to set $w_x = l_x, w_y = l_y$ based on average pixel correlation lengths (Section 7.2) is the paper's most concrete practical guidance, but it is tested only on MNIST without any cross-dataset validation.

### Trivial
None.

## Nice-to-Haves

- Comparison against other HDC encoders (e.g., random projection, level encoding, thermometer encoding) on at least one non-trivial dataset beyond MNIST to assess competitiveness.
- Experiments on continuous-valued decoding to support the "easily extended" claim for non-binary features.
- Acknowledgment of the RFF connection and discussion of how the separation metric analysis relates to established kernel bandwidth selection theory.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **RFF not cited**: While the encoding being RFF without acknowledgment is a major issue (kept above), the specific claim that the paper "cannot be independently verified" regarding RFF is removed under the hard rule against questioning cited entities' existence. The concern is about attribution, not existence.

- **65% baseline is "suspiciously poor"**: The 65% figure is the result of using suboptimal encoding parameters within the proposed framework, not a comparison against other methods. Whether other HDC encoders perform better is a valid experimental limitation (kept above), but calling 65% "suspicious" mischaracterizes the experimental setup—it is intentionally a baseline showing what happens with poor encoding choices.

- **"The kernel's exact form is unimportant" claim is too casual**: This is a minor stylistic disagreement. The paper does acknowledge that different $p(\theta)$ distributions yield different kernels via Bochner's theorem (line 59), so the claim is contextually about the general framework being kernel-agnostic, not dismissive of kernel choice.

- **Section 6 is primarily a review of Frady et al. (2020)**: The resonator network description is indeed largely from prior work, but the paper provides new analysis of how correlation affects factorization convergence (Section 7.5), which is a genuine contribution in context.

- **No error bars / statistical significance**: For exploratory analysis papers examining encoding parameter effects, single-run heatmaps showing clear trends are standard. Demanding error bars is a nice-to-have, not a substantive weakness for this type of work.

- **"Cognition" oversimplified to decoding**: While true that "cognition" in the paper reduces to information retrieval/decoding, the paper explicitly scopes cognition this way. Criticizing it for not addressing reasoning, planning, and analogy-making is scope creep.

- **Missing comparison against other HDC encoders**: Demanding this is partially scope creep—the paper's focus is on understanding encoding properties within a single framework, not on beating SOTA. However, the lack of any cross-method comparison does limit the ability to assess competitiveness, so a weakened version of this concern is kept under minor weaknesses.

## Novel Insights

The most interesting observation is the fundamental tension the paper exposes within HDC: the same encoding hyperparameters must serve opposing objectives depending on the task. Correlation between position basis vectors (large $w$) is essential for learning—because bundling correlated vectors allows the class prototype to grow a meaningful signal with $\sqrt{p}$ scaling—but is precisely what destroys orthogonality needed for decoding and factorization. This creates a genuine design dilemma for any unified HDC system that must both learn and reason: you cannot optimize for both simultaneously with a single $w$. The $\sqrt{p}$ scaling insight (that memorization capacity grows with samples only under correlated encoding) is a clean theoretical result, even though its independence assumption needs qualification. The data-driven heuristic $w_x = l_x$ (setting bandwidth to match the dataset's correlation length) provides a practical, interpretable rule that connects encoding choice to data statistics—something missing from prior HDC encoding practice.

## Suggestions

- Explicitly acknowledge the connection to Random Fourier Features (Rahimi & Recht, 2007) and frame the contribution as analyzing how RFF-based encoding serves different HDC tasks, rather than claiming the encoding itself as novel.
- Fix the contradictory statement about separation and accuracy in Section 7.3, and correct the typo $N(p\mu_{12}, \sqrt{p}\mu_{12})$ to $N(p\mu_{12}, \sqrt{p}\sigma_{12})$.
- Add at least one experiment on a non-binary, non-MNIST dataset to demonstrate generalizability.
- Discuss the independence assumption in the $\sqrt{p}$ result and its limitation in the correlated regime.

## Score and Decision

The paper identifies a genuine and important problem in HDC (principled encoding selection), but its core novelty is undermined by the fact that the encoding is RFF without acknowledgment, and the main insight (learning needs wide kernels, decoding needs narrow kernels) is a direct consequence of well-known kernel bandwidth principles. The experimental evaluation is limited to binarized MNIST with no comparison to other approaches. The theoretical analysis has a significant gap (independence assumption violated in the regime of interest) and contains a contradictory statement about the separation metric. These issues collectively weaken the contributions substantially, though the work does provide useful analysis for the HDC community.

**Originality**: Limited — the encoding is RFF unattributed, and the core insight restates kernel bandwidth principles. The separation metric analysis and $\sqrt{p}$ result have novelty but are hampered by theoretical gaps.

**Importance of research question**: Relevant for HDC practitioners; encoding selection is a real problem.

**Whether claims are well supported**: Partially — empirical results on MNIST are consistent with the framework, but the contradictory Section 7.3 statement and limited evaluation weaken support.

**Soundness of experiments**: Limited — only binarized MNIST, no baselines, no error bars.

**Clarity of writing**: Generally clear but with the contradictory passage and equation typo.

**Value to research community**: Moderate for HDC community, but the contribution would be significantly strengthened by acknowledging connections to kernel methods.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>