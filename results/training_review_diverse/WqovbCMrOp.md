Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper studies whether causal relations can be recovered from temporally aggregated i.i.d. data when the true underlying process involves time delays. It formalizes two notions of consistency — **functional consistency** (for FCM-based methods) and **conditional independence consistency** (for constraint-based methods) — and provides conditions under which each holds. The key contributions are: (1) showing that the collider structure is robust to aggregation even in nonlinear cases, while chain and fork structures are not; (2) proving that partial linearity in either the X-Y or Y-Z relation suffices for chain/fork consistency; and (3) demonstrating through theory and experiments that fully nonlinear systems distort causal discovery, but recoverability is possible under partial linearity or with appropriate priors.

## Strengths

- **Novel conditional independence consistency analysis.** The paper formalizes what it means for conditional independence structure to survive temporal aggregation (Definition 7, Remark 3, Theorem 4) and delivers a clean, nontrivial result: collider structure is robust, while chain and fork are not, and partial linearity in the causal mechanism suffices for chain/fork consistency (Corollaries 4–5). This directly supports the paper's central claim that recoverability is possible under certain conditions but fails in fully nonlinear settings.

- **Experimental validation of the core theoretical predictions.** Figure 2 shows Direct LiNGAM accuracy dropping from near 100% to random chance as the aggregation factor k increases, confirming that even linear non-Gaussian cases suffer from aggregation. Table 1 shows that the key conditional independence (VI) for fork structure is rejected 58% of the time in fully nonlinear systems (far from the expected 5%) but drops to 5% under partial linearity — directly validating the sufficient conditions in Corollary 5.

- **Clear bridging argument between time-delay and aligned models.** Section 2.2 provides a precise asymptotic argument showing that temporal aggregation of a time-delay VAR converges to aggregation of an instantaneous aligned model as k → ∞, and the paper transparently states that its theoretical results apply to aligned models with any finite k, with the extension to time-delay models requiring large k (lines 100–102).

- **Identifies and addresses limitations of prior work.** The paper explicitly critiques Fisher (1970) for assuming fixed noise and Gong et al. (2017) for considering only linear cases, then extends the analysis to general nonlinear settings with random noise, justifying the novelty of its contributions.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **The functional consistency section (Section 3) is weakly developed relative to the claims made for it.** Theorem 2 gives a necessary and sufficient condition for the additive noise model to hold on aggregated data, but the condition (independence of the residual from $\overline{X}$) is essentially a restatement of the definition in terms of the theorem's own construction. The paper's own analysis observes that this reduces to a constant conditional variance requirement — a non-trivial condition, but no further sufficient conditions beyond the already-known linear case are provided. Theorem 3 (general case for different regions) shows both directions are representable, which follows from standard arguments about the existence of arbitrary conditional distributions and yields an unsurprising negative result. The paper's contribution list claims this section as a main pillar, but the delivered insight is largely "functional consistency is hard in nonlinear cases" without substantive new sufficient conditions. The paper would be stronger by either providing nontrivial sufficient conditions or explicitly acknowledging this as a formalization of negative results rather than a discovery of comparable weight to the CI consistency analysis.

- **Theorem 4 (CI main theorem) is presented as an integral condition that is essentially a restatement of the conditional independence condition.** The theorem involves integrals over $y_{1:k}$ of products of conditional densities, which is a direct translation of the definition into integral form. While the paper does use the decomposition of this integral to motivate the sufficient conditions (lines 265–269: "This inspires us to consider different parts of the model individually"), the connection from the integral equations to the corollaries is not derived explicitly — the corollaries are instead introduced via an intuitive separate argument ($\overline{X} \perp Y_{1:k} \mid \overline{Y}$). Making the derivation from the integral condition to the partial linearity result explicit would strengthen the theoretical chain.

- **Experimental detail is uneven across the five claimed experiments.** The CI consistency experiment (Section 5.3) is described with reproducible detail. However, the FCM-based experiment (Section 5.2) is reported qualitatively without precise numerical results (rejection rates, confidence intervals). The "skeleton prior" experiment (experiment five) is named but receives no description of setup, results, or analysis — the paper simply states it "consistently obtained correct results" as a "preliminary solution" (line 301). For an empirical paper where experiments support theoretical claims, this unevenness makes parts of the evidence base harder to assess.

- **Column-label mapping in Table 1 requires cross-referencing.** The columns I–VI and A–B are defined in the body text (line 339) but the table caption does not restate the mapping, and the table is stated to be for "fork structure" only in the surrounding text. A self-contained table (explicitly labeling which CI statement each column tests) would improve readability and reduce the risk of misinterpretation.

### Trivial

- **Notation shifts across sections.** The paper switches from vector-valued $X_t$ (Section 2) to scalar $X,Y,Z$ (Sections 3–4) with a footnote acknowledgment, but the shift is jarring when reading consecutively. A unified notational scheme from the outset would improve flow.

- **The title is broader than the paper's actual focus.** The paper primarily studies the *limits* of recoverability and conditions under which it *fails* (or succeeds only under partial linearity). A more precise title (e.g., "On the Limits of Recovering Causal Relations from Temporally Aggregated Data") would better reflect the paper's contributions.

## Nice-to-Haves

- The paper could briefly discuss how the choice of normalization $g(k)$ (sum, average, etc.) interacts with distributional properties and CLT convergence rates, to guide practitioners in real applications.
- A brief discussion of how heavy-tailed noise distributions could slow CLT convergence and thus alleviate the identifiability problem in the linear non-Gaussian case would strengthen the interpretation of the Direct LiNGAM experiment.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- "Theorem 4 does no work in the paper" — **Removed because factually incorrect.** The paper explicitly states that the decomposition of the integral in Theorem 4 "inspires us to consider different parts of the model individually" (lines 265–269) and uses this to motivate the sufficient conditions.
- Criticism about missing appendix/stripped content — **Removed per hard rule:** parser strips appendices from all papers; they exist in the original submission.
- "The paper should not claim to be 'first'" — **Removed:** the paper already uses "To the best of our knowledge" (line 31).
- Pure formatting and labeling nitpicks (table label mismatches, missing numbers) — **Removed per hard rule:** these are parser artifacts.
- "Gap between motivating problem and aligned model is underclarified" — **Downgraded from major to removed as a weakness:** the paper explicitly acknowledges this gap and states the conditions under which the results transfer (lines 100–102). The paper is transparent about the scope; the framing is reasonable for the paper it is.
- Missing related works / demands for broader coverage — **Removed:** cannot verify existence of missing references; demanding the paper cover additional domains constitutes scope creep.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's core strengths (CI consistency analysis, partial linearity condition) and highlight that the functional consistency section is the weaker part of the paper, but these observations are consistent with the paper's own presentation.

## Suggestions

1. **Restructure Section 3** to either (a) provide nontrivial sufficient conditions for functional consistency beyond the linear case, or (b) explicitly recast it as a formalization of why functional consistency fails, downgrading its prominence relative to the CI consistency results.

2. **Connect Theorem 4 to its corollaries more explicitly** by showing how the integral equations simplify under the linearity assumptions of Corollary 5, rather than introducing the corollaries through a separate argument.

3. **Fill in experimental gaps in the main text** — at minimum, report numerical rejection rates for the Direct LiNGAM experiment and describe the skeleton prior experiment's setup and results briefly.

4. **Make Table 1 self-contained** by including the mapping of columns I–VI and A–B to the tested conditional independence statements directly in the caption or as a table footnote.

## Score and Decision

This paper addresses a genuine and understudied problem with a clean theoretical framework. The conditional independence consistency analysis — particularly the robustness of colliders, the failure of chain/fork, and the partial linearity sufficient condition — is the paper's strongest contribution and is well-supported by experiments. The functional consistency section is noticeably weaker and would benefit from reduced emphasis or strengthening. The experimental section has uneven coverage. However, the core contributions are novel, sound, and useful to the community. The paper is suitable for publication with minor revisions.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>