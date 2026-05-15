Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper systematically investigates whether video generation models can learn fundamental physical laws from visual data, using a 2D physics simulation testbed covering uniform motion, elastic collision, and parabolic motion. It categorizes generalization into three types — in-distribution (ID), out-of-distribution (OOD), and combinatorial — and conducts scaling experiments (30K–3M videos, 22M–310M parameters) for each. The key finding is that scaling consistently improves ID and combinatorial generalization but fails to improve OOD extrapolation of out-of-range physical parameters. Further analysis reveals case-based (rather than rule-based) generalization behavior and an attribute prioritization hierarchy (color > size > velocity > shape), providing mechanistic insight into model limitations.

## Strengths

- **Systematic three-way generalization taxonomy with dedicated experiments.** The paper cleanly separates ID, OOD, and combinatorial generalization (Fig. 1) and designs purpose-built experiments for each type, going well beyond standard visual quality evaluation. This framework is reusable by future work.

- **Well-supported demonstration that OOD generalization does not improve with scaling.** Across three physical scenarios (uniform motion, elastic collision, parabolic motion), OOD velocity errors remain an order of magnitude higher than ID errors and show no decreasing trend as data scales from 30K to 3M or model size from 22M to 310M (Fig. 2, Sec. 3.2). This directly challenges the assumption that scaling alone can yield world models, and is the paper's strongest result.

- **Novel 2D simulation testbed enabling quantitative physics evaluation.** The Box2D-based simulator with pixel-parsing velocity extraction (Sec. 3.1) provides unlimited data, ground-truth state access, and a quantitative error metric with a known GT baseline (error ~0.01). This design cleanly isolates what models learn about physics rather than about texture or appearance.

- **Discovery of the attribute prioritization hierarchy (color > size > velocity > shape).** The pairwise attribute competition experiments (Sec. 5.3) are elegant and produce a clear, interpretable ranking supported by 1,400 test cases for the color-vs-shape comparison. This finding has practical implications for model design (e.g., explains why shape preservation is difficult).

- **Case-based generalization evidence (Sec. 5.2).** The flipped-data experiment showing directional bias in low-speed balls is a clean demonstration that the model mimics training patterns rather than abstracting the law of inertia. This complements concurrent findings in LLMs.

- **Convex-hull generalization analysis (Sec. 5.1).** The experiment showing good generalization inside the convex hull of training data but failure outside provides geometric insight into interpolation vs. extrapolation boundaries.

## Weaknesses

### Fatal
None.

### Major

- **Confounded combinatorial generalization experiment (Sec. 4, Table 1).** The number of templates (6, 30, 60) and total data volume (0.6M, 3M, 6M) co-vary because each template contributes 100K videos. This makes it impossible to attribute the out-of-template improvement (e.g., abnormal ratio falling from 67% to 10%) to broader combinatorial coverage versus simply having more total data. The claim that "scaling laws should focus on increasing combination diversity, rather than merely scaling up data volume" (line 264) is not supported by the present evidence — a controlled experiment holding total data fixed while varying template count is required. This is the most consequential unaddressed confound in the paper.

- **Human evaluation for the abnormal ratio is underspecified (Table 1).** The headline 67% → 10% reduction in "abnormal" videos is critical evidence for combinatorial generalization, yet the paper provides no information about the number of raters, inter-rater reliability, evaluation instructions, or whether raters were blind to condition (line 239: "assessed by humans" is the only detail). While the pixel-level metrics (FVD, SSIM, PSNR, LPIPS) also improve with more templates — corroborating the trend — the dramatic claim about physical plausibility depends heavily on this unvalidated human score and cannot be properly assessed without methodological details.

- **Absence of variance or confidence intervals for the central OOD scaling result (Sec. 3.2).** Figure 2 and the accompanying text report single velocity-error values per data/model combination with no error bars or statistical significance. For a negative finding ("scaling does not improve OOD"), variance estimates are essential — without them, it is impossible to tell whether the variation across conditions (e.g., DiT-B errors of 0.433, 0.328, 0.358 across 30K, 300K, 3M) is meaningful noise or if small but real improvements are being masked.

### Minor

- **OOD evaluation covers only one narrow type (out-of-range continuous parameters).** The paper tests OOD by extrapolating velocity and radius values beyond the training range. The conclusion that "scaling alone is insufficient for video generation models to uncover fundamental physical laws" (lines 14–15, 425) is broader than the evidence supports. Qualitatively new regimes — different object types, interaction types, or boundary conditions — are not tested. The paper should more carefully scope its claims about "physical law discovery" to the specific OOD settings evaluated.

- **Section 5.1 (interpolation/extrapolation) lacks quantitative error values.** The convex-hull finding is interesting but supported only by color maps and qualitative descriptions (line 286: "the OOD generalization error remains relatively small and comparable to the ID error" — with no numbers). Reporting actual velocity errors for internal vs. external OOD points would substantially strengthen this section.

- **Section 5.2 (memorization) provides only a single qualitative example (Fig. 12).** The directional-reversal behavior in the flipped-data model is compelling but anecdotal. No aggregate statistics are reported (e.g., proportion of test cases exhibiting reversal, broken down by velocity range). The claim that "the model appears to rely on memorization, and case-based imitation" (line 323) requires quantitative support.

- **Section 5.4 (complex combinatorial patterns) is purely anecdotal.** Three patterns (attribute, spatial, temporal composition) are illustrated with one example each, with no quantification, no negative examples, and no frequency measures. While suggestive, this section reads as preliminary observation rather than rigorous analysis.

### Trivial
None.

## Nice-to-Haves

- A controlled combinatorial scaling experiment holding total data volume fixed (e.g., 3M videos) while varying the number of templates (6, 30, 60) would cleanly resolve the central confound.
- Reporting confidence intervals or standard deviations for the velocity error measurements (Fig. 2) would strengthen the negative OOD result.
- Extending the attribute hierarchy analysis (Sec. 5.3) to at least one additional physical scenario (e.g., collision) would test whether the ranking is task-dependent or universal.
- Testing whether behavioral cloning of the simulator (rather than diffusion generation) shows the same OOD failure pattern would help determine whether the limitation is architectural or fundamental to data-driven approaches.

## Removed Points

These points were flagged for removal; treat them with caution.

- **Sora quote as straw man.** The critic claimed the paper uses the Sora quote as a straw man. The paper fairly engages with Sora's stated goal of "general purpose simulators of the physical world" — the question of whether scaling alone suffices for physical law discovery is a legitimate research question directly motivated by that claim. Removed: not a valid weakness.

- **Missing related works on physical reasoning networks.** The critic suggested discussing interaction networks and neural physics engines. Per the hard rule, missing related works are not flagged as weaknesses since I cannot confirm which works exist or are relevant from context alone. Removed: violates hard rule.

- **"Visual Ambiguity (Sec. 5.5) should be elevated to discussion."** This is an organizational suggestion, not a weakness in the paper's methodology or claims. The paper already identifies this limitation. Removed: organizational preference, not a substantive flaw.

- **"OOD experiments test only one narrow type of OOD — the conclusion about physical law discovery is substantially broader than evidence."** This was moved to Minor (kept but downgraded). The paper's OOD setting is indeed narrow, but the experiments are valid within their stated scope. The paper does acknowledge it studies classical mechanics with specific scenarios. The critic's stronger framing ("substantially broader") overstates the gap.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run a controlled combinatorial experiment** — fix total data volume (e.g., 3M) while varying templates from 6 to 60 by adjusting videos per template. This is critical to substantiate the "diversity vs. volume" claim.
2. **Document the human evaluation** — report number of raters, inter-rater agreement (e.g., Cohen's κ or Fleiss' κ), evaluation instructions, and whether raters were blind to condition.
3. **Add error bars** — provide confidence intervals or standard deviations for all velocity error measurements in Fig. 2 to support the negative OOD result.
4. **Quantify the memorization analysis** — report the proportion of test cases exhibiting reversal behavior in Sec. 5.2, broken down by velocity range.
5. **Report quantitative error values for the convex-hull experiment** — give numerical velocity errors for internal vs. external OOD points in Sec. 5.1.
6. **Scope the OOD claims** — explicitly acknowledge in the conclusion that the tested OOD is limited to out-of-range continuous parameters, and that conclusions about "physical law discovery" are relative to this setting.

## Score and Decision

The paper tackles an important and timely question with a carefully constructed synthetic testbed and a principled evaluation taxonomy. Its core finding — that scaling improves ID and combinatorial generalization but fails at OOD extrapolation — is well-supported and has clear implications for the field. The attribute prioritization hierarchy and case-based generalization evidence are valuable secondary contributions. However, two major weaknesses prevent the paper from being fully convincing: the confounded combinatorial experiment (which undermines the "diversity vs. volume" claim) and the underspecified human evaluation (on which a headline result depends). The lack of confidence intervals for the OOD scaling result is a further concern. These are addressable in revision but limit the strength of the paper in its current form.

The paper's contributions are solid but its strongest claims are partially overreaching relative to the evidence. It warrants acceptance contingent on addressing the combinatorial confound and human evaluation documentation.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>