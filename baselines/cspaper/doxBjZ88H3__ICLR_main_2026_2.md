---
job_id: d6fcd53d-51c3-478a-bb77-cddda0dbf861
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: doxBjZ88H3.pdf
paper: An Information-Theoretic Framework For Optimizing Experimental Design To Distinguish Probabilistic Neural Codes
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, at the intersection of probabilistic methods, uncertainty quantification, neural decoding, and applications to neuroscience and cognitive science.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, presents a coherent method with derivations and experiments, and provides nontrivial empirical validation, although there are several limitations in clarity, scope, and experimental realism.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes an information-theoretic framework for designing experiments that distinguish two competing probabilistic neural coding hypotheses, likelihood coding and posterior coding. The core quantity is the information gap, defined as the expected decoder performance difference between likelihood and posterior decoders under an idealized decoding limit, with analytic expressions derived for both coding hypotheses. The paper validates the framework on simulated neural populations, explores optimized task designs under different prior families, and uses an existing single-context neurophysiology dataset to illustrate why conventional designs are insufficient for adjudicating the two hypotheses.

## Strengths
1. The paper addresses an interesting and well-motivated scientific question, namely how to design experiments that can actually differentiate between likelihood-coding and posterior-coding accounts, rather than merely fitting one or the other post hoc. That problem formulation is valuable on its own and is broader than just the specific decoder architecture used here.

2. The central idea is conceptually clean. The information gap links distinguishability of coding hypotheses to a cross-entropy/KL-based quantity, which gives the paper a principled objective instead of a heuristic design rule. In the main text, **Eq. 1**, **Eq. 2**, **Eq. 3**, and **Eq. 5** make the proposed framework reasonably concrete, and the asymmetry between likelihood-coding and posterior-coding cases is an interesting takeaway.

3. The simulations are fairly systematic. **Figure 3** is especially useful because it does not just show one favorable example, it explicitly studies convergence as a function of trial count and neuron count across high-, medium-, and low-contrast settings. The dashed theoretical values and empirical curves aligning over increasing data size support the claim that the derived information gap is predictive of asymptotic decoder performance differences in the idealized simulation setting.

4. **Figure 4** is a strong validation figure. It tests many task parameter settings and two response models, Poisson and gain-modulated Poisson, and shows close agreement between theoretical information gap and empirical decoder difference across conditions. That is the most convincing empirical evidence in the paper that the theory is not merely tailored to one simulation point.

5. The task-design perspective is practically relevant. **Figure 5** provides an interpretable landscape over prior separation \(d\) and prior width \(\sigma\), making clear that “make the priors as different as possible” is not actually the right answer because overlap also matters. This is a nice example of where the theory provides nontrivial guidance.

6. I also appreciated that the paper does not overclaim on existing data. The real-data analysis in **Figure 7** is modest in scope, but the conclusion drawn from it is appropriately narrow, namely that a single-context dataset should not be expected to discriminate the hypotheses.

7. Reproducibility is reasonably supported by the code release statement and by the inclusion of implementation details for the decoders and simulation setup.

## Weaknesses
1. The main limitation is that the paper remains almost entirely a simulation-and-theory exercise, while the stated goal is to guide experimental design for neuroscience. The only real-data result, **Figure 7** on Pages 9 to 10, verifies a near-trivial prediction under a single-context design, namely \(\Delta^{\mathrm{info}} \approx 0\). This is fine as a sanity check, but it falls well short of demonstrating that the proposed framework yields experimentally actionable gains in a realistic recording regime. What matters scientifically is not only that the idealized information gap exists, but that the optimized design remains distinguishable under finite trials, finite neurons, nonstationarity, tuning heterogeneity, and imperfectly learned subject priors. The paper acknowledges some of this in the discussion, but the main empirical case still stops one step too early.

2. The framework depends heavily on idealized assumptions that are stronger than the paper sometimes lets on. On Page 4, the derivation assumes contexts are explicitly cued and that subjects adopt the intended context-specific prior. On Pages 4 to 5, the information gap is derived under optimal decoders and a known generative model \(p(x\mid \theta)\). On Page 6, the simulated posterior code is implemented by directly modulating mean firing rates with the prior. These assumptions are not just technical conveniences, they are doing a lot of the work. If the subject’s internal prior differs from the experimental prior, if the context cue is incompletely learned, or if the decoder class is mis-specified, the optimized design may no longer be optimal, and possibly not even robust. Since the entire selling point is experimental design, robustness to such mismatch matters substantially.

3. The mathematical setup for the posterior-coding case is not fully satisfying in the main paper. In **Eq. 3** on Page 5, the sum is written over pairs \((x_j,x_k)\), but the exact set of admissible pairs is only described informally as those satisfying **Eq. 4**. That leaves several unresolved issues: whether pairs are unique or can be double-counted, how approximate equality is handled in practice when posteriors are only approximately equal, how the pairing is constructed numerically for continuous or finely discretized \(x\), and what happens when multiple \(x_k\) satisfy the condition for a given \(x_j\). Since \(\Delta_{\mathrm P}^{\mathrm{info}}\) depends entirely on this pair set, this is not a cosmetic notation issue, it affects the meaning and computability of the objective.

4. Relatedly, the paper’s notation blurs the distinction between neural responses and encoded distributions in a way that occasionally muddies the formal claims. On Page 4, the likelihood-coding population is written as \(\mathbf r_{\mathrm L}\sim p(x\mid \theta)\), and on Page 5 the posterior-coding population is written as \(\mathbf r_{\mathrm P}\sim p(\theta\mid x)\). Strictly speaking, a neural population response is not distributed as a likelihood function or posterior distribution; it is some stochastic code carrying information about one of these objects. The appendix later introduces an encoding function \(f(\cdot)\), which is the right way to say it, but the main text glosses over this. That matters because the claims about decoder optimality and one-to-many versus many-to-one mappings are really claims about equivalence classes under the encoding map \(f\), not directly about \(p(x\mid \theta)\) or \(p(\theta\mid x)\).

5. The paper would be stronger with clearer comparisons to more standard experimental design criteria. The proposed objective is specialized and interpretable, which is good, but the paper never seriously asks whether one would get similar designs from maximizing mutual information, Bayes factor discrimination, or expected log-likelihood ratio between the competing hypotheses. Right now the reader is asked to accept that the information gap is the right objective because it matches the downstream decoder comparison the authors want to make. That is defensible, but the paper is weaker for not situating this objective against established information-theoretic design principles. This is partly a positioning issue, but also a scientific one: without such a comparison it is harder to know whether the contribution is a genuinely better criterion or a task-specific reparameterization of familiar ones.

6. The optimization story is less developed than the title suggests. Section 4 presents heatmaps over a low-dimensional Gaussian-prior parameterization and then chooses “sweet spots” visually from **Figure 5**. This is useful, but it is not yet a general optimization framework in the algorithmic sense. There is no optimization algorithm, no complexity discussion, no treatment of higher-dimensional design spaces, and no demonstration that the method scales beyond hand-sweeping a two-parameter grid. For Gaussian priors this is acceptable, but the broader framing of “optimizing experimental design” feels a bit ahead of what is actually implemented in the main paper.

7. Some of the key empirical design conclusions are conveyed only visually, without precise quantitative reporting in the main paper. For example, **Figure 5** identifies starred “sweet spots,” but the actual maxima, near-maxima, sensitivity to neighboring parameters, and uncertainty around those selections are not reported systematically in a results table or even in concise numeric summaries. That weakens the practical usefulness of the method for experimentalists. The same issue appears in **Figure 6**, where the conclusion that heavy-tailed priors are poor choices is visually plausible, but the paper does not quantify how close to zero \(\Delta_{\mathrm P}^{\mathrm{info}}\) is across parameter space, nor how sensitive that statement is to discretization and finite-sample decoder error.

8. Presentation has several rough edges, including some that touch the technical content. On Page 3 the text refers to **Fig. 2D**, but **Figure 2** has panels A, B, and C. On Page 8, the notation appears to switch to \(\Delta_{\mathrm P}^{\mathrm{ndo}}\) and \(\Delta_{\mathrm L}^{\mathrm{ndo}}\), which looks like a typo for \(\Delta^{\mathrm{info}}\). There are also recurring notation inconsistencies and awkward phrasing, and the appendix contains at least one clearly spurious equation on Page 18 labeled as **Eq. 10**, which is unrelated to the surrounding derivation. Even if that appendix artifact does not affect the main claim, it does lower confidence that the mathematical exposition was polished carefully enough.

9. The empirical decoder setup is plausible but not thoroughly stress-tested for fairness between the two decoder families. On Page 24, the likelihood decoder and posterior decoder use closely related MLPs with different output interpretations. However, because the likelihood decoder receives the ground-truth prior and the posterior decoder does not, the two decoder tasks are not equally difficult in a purely architectural sense. That asymmetry is part of the scientific question, so it is not “unfair” per se, but it would still help to see stronger evidence that the measured performance differences are not sensitive to network capacity, regularization, training dynamics, or calibration issues. **Figure 3** and **Figure 4** help, but they mostly show asymptotic agreement, not robustness to decoder misspecification.

10. The literature positioning is decent within computational neuroscience, but lighter than I would expect on Bayesian experimental design more broadly. Since the paper’s main contribution is an information-theoretic objective for choosing experiments, it should be more explicit about what is gained relative to generic Bayesian design objectives and why a specialized criterion is necessary here.

## Questions
1. For the posterior-coding case, please define precisely the set of pairs summed over in **Eq. 3**. Is this a set of exact matches satisfying **Eq. 4**, approximate matches under a tolerance, or a partition into equivalence classes of responses? How do you avoid double-counting when multiple pairs correspond to the same posterior?

2. How sensitive are the optimized task parameters in **Figure 5** to mismatch between the experimenter-specified prior \(p^c(\theta)\) and the subject’s internal prior? A quantitative robustness analysis here would materially increase my confidence in practical applicability.

3. Can you compare the proposed information-gap objective to at least one more standard experimental-design objective, such as mutual information between response and hypothesis label, or expected log-likelihood ratio between the two coding hypotheses? Even a limited comparison on the same Gaussian-prior design space would help clarify whether your criterion is uniquely useful or largely aligned with existing objectives.

4. The real-data result in **Figure 7** is consistent with the theory, but it is also a low bar. Can you provide stronger evidence, even in simulation under more realistic constraints, that the optimized designs remain distinguishable with finite trial budgets closer to real experiments, for example a few hundred to a few thousand trials rather than the large-\(n\) regime emphasized in **Figure 3**?

5. In the main text, the coding hypotheses are written as \(\mathbf r_{\mathrm L}\sim p(x\mid \theta)\) and \(\mathbf r_{\mathrm P}\sim p(\theta\mid x)\). I think you really mean \(\mathbf r\sim f(\cdot)\) for some encoding family. Please clarify this in the main paper, because otherwise the derivation reads as if neural responses are literally samples from those distributions.

6. The starred operating points in **Figure 5** are selected visually as strategic compromises. Is there a formal scalarized criterion used to choose them, for example maximizing \(\min(\Delta_{\mathrm L}^{\mathrm{info}}, \Delta_{\mathrm P}^{\mathrm{info}})\) or a weighted sum? If not, I would encourage adding one, because “sweet spot” selection is currently more heuristic than the rest of the paper.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
3: good. The central technical claims are mostly supported within the paper’s idealized setting, but there are important assumptions, some underspecified aspects of the posterior-coding derivation, and limited evidence for robustness in realistic experimental regimes.

## Presentation Rating
2: fair. The paper is readable and the core intuition comes across, but notation, equation presentation, and several figure/text inconsistencies reduce clarity more than they should for a theory-heavy submission.

## Contribution Rating
3: good. The problem formulation is important and the information-gap viewpoint is a meaningful contribution, though the work is not yet as comprehensive or practically grounded as the framing suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper has a clear and interesting idea, and the simulation evidence is stronger than average for a theory-driven neuroscience application. Still, the gap between idealized theory and experimentally realistic deployment, plus some technical underspecification in the posterior-coding case, keeps this from being an easy accept for me.

## Reviewer Confidence
4: confident. I am confident in the main assessment and checked the technical setup with care, though some derivation details, especially around the posterior-coding pairing construction, would benefit from author clarification.