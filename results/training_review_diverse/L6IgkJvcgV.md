Now I have a thorough understanding of the paper's content (and crucially, what was stripped by the parser). Let me produce the consolidated review.

---

## Summary

This paper proposes OASIS, a four-component evaluation framework for measuring stereotypes in text-to-image (T2I) generated images and diagnosing their origins within the model. OASIS introduces (M1) a Stereotype Score that operationalizes stereotypes as *directional violations of real-world distributions* (contrasting with prior work's reliance on statistical parity), (M2) WALS measuring spectral variety along stereotypical attributes, (U1) StOP for discovering internal model associations, and (U2) SPI for tracing when stereotypical attributes emerge during generation. Applied to SDv2, SDv3, and FLUX.1 across nationalities, the paper finds that stereotypes persist (and sometimes worsen) in newer high-fidelity models, and that stereotype severity correlates with Internet footprint of nationalities.

## Strengths

- **Principled definition of stereotypes that distinguishes them from general bias.** The paper formalizes stereotypes as directional violations of real-world attribute distributions (exceeding P*(A|C) in one direction only), rather than deviations from uniform distributions used in prior work. The turban example (Section 4.1) makes the distinction concrete: requiring 50% turban for Iranian (statistical parity) is absurd when only 0.2% of Iranians wear turbans in reality. This is a genuine conceptual improvement.

- **Complementary metric pair (Stereotype Score + WALS).** The paper pairs a distributional measure with a spectral variety measure, preventing the conflation of "low stereotypes" with "low diversity." Figure 5 provides direct evidence that SDv3 sometimes achieves lower stereotype scores partly by reducing attribute variance — a trade-off invisible to either metric alone.

- **Empirical demonstration that stereotypes persist across model generations.** OASIS shows that despite dramatic fidelity improvements from SDv2 to FLUX.1, stereotypes remain prevalent. The finding that FLUX.1 depicts 84.7% of Mexican faces with mustache (vs. 34.1% for SDv3, Table 1) contradicts any assumption that better image quality reduces harmful representations.

- **Open-set stereotype generation via LLMs.** Using ChatGPT o1-preview/4o to generate candidate stereotypes per concept (Eq. 2) avoids the limitations of closed, predefined attribute sets used in prior work, enabling broader coverage including intersectional stereotypes.

- **StOP's ability to recover internal model associations.** The optimized prompts from StOP (Table 3) contain culturally specific terms like "Imam" and "brero" absent from the original neutral prompts, providing direct evidence that the model internally encodes stereotypical attributes.

## Weaknesses

### Major

- **No validation of the attribute classifiers used to compute stereotype scores.** The Stereotype Score (M1) requires estimating P(A|D,C) — the proportion of generated images exhibiting each attribute. The paper uses "CLIP ViT-G-14 from OpenCLIP trained on LAION2B" for this purpose but provides zero evidence that CLIP can reliably classify nuanced attributes such as "turban," "traditional cloths," "mustache," or "skin tone" at the accuracy needed to support precise percentage claims (e.g., 0.2% vs. 56.4%). Measurement error in attribute classification directly biases all stereotype scores in Tables 1-2 and the comparisons drawn from them. Without any validation — not even a small human evaluation on a sample of generated images — the quantitative backbone of the paper's empirical claims cannot be trusted at face value. This is the single most consequential gap in the paper.

- **The Internet footprint claim rests on thin evidence.** Section 4.2's conclusion that "stereotypes are higher for underrepresented nationalities" is based on three nationalities (Indian, Mexican, Iranian), a single proxy (number of Internet users), no correlation coefficient or significance test, and no control for confounds (e.g., cultural proximity to Western training data, economic factors). The paper's wording is appropriately tentative ("suggest"), but this finding is highlighted in the abstract and conclusion as a core result. Three data points do not support a generalizable quantitative claim, and the causal narrative (training data composition → stereotype severity) is asserted without access to the actual training data.

### Minor

- **SPI emergence analysis lacks a control condition.** Section 4.5 observes that stereotypical attributes (beard, traditional cloths) form at early time steps for 4 images across 2 nationalities, but does not compare against non-stereotypical attributes. Without showing that *all* attributes — including neutral ones — form at similar rates, the finding may reflect general properties of diffusion trajectories (early steps determine coarse structure) rather than anything specific to stereotypes. This limits the novelty of the observation.

- **Predisposition analysis (Section 4.6) is illustrative, not conclusive.** The linear extrapolation from t=0 velocities to estimate final images is acknowledged as a heuristic (the paper notes it "enables us to identify the stereotypical predispositions qualitatively"), but the conclusion that "T2I models associate stereotypical attributes with seemingly innocuous prompts" is stated strongly despite being supported by only 3 qualitative samples. The visual results are suggestive but not statistically compelling.

- **StOP analysis has qualitative subjectivity.** Table 3's discovery of M-attributes relies on manual identification of shared stereotypes from image cluster averages. The paper does not quantify overlap with human-annotated stereotype dictionaries, nor compare StOP outputs against a random-prompt baseline. While StOP is an interesting tool, the evidence that it reveals "internal model associations" (rather than reconstructing cluster centroids) remains circumstantial.

- **No discussion of normative assumptions about real-world statistics P*(A|C).** The paper's definition takes real-world attribute distributions as the reference point, but does not discuss the possibility that these distributions themselves reflect societal discrimination. If P*(A|C) is shaped by historical stereotypes, then matching it would preserve those stereotypes. This does not invalidate the metric, but it is an important nuance that deserves acknowledgment — especially since the paper motivates itself as an "important step toward ... mitigating stereotypical content."

- **No systematic comparison to existing bias metrics.** The paper motivates the new Stereotype Score by arguing that prior work (Jha et al. 2024, D'Incà et al. 2024) conflates bias with stereotype, but never applies those existing metrics to the same generated data to show where conclusions diverge and why the OASIS interpretation is preferable. The turban example (Section 4.1) makes the conceptual point clearly, but a systematic comparison would strengthen the contribution.

### Trivial

None. The paper is overall well-written; what appears as missing content or formatting issues in the extracted text are parser artifacts.

## Nice-to-Haves

- A small human evaluation (e.g., 200 images per attribute) reporting precision/recall of the CLIP-based attribute classifiers would directly address the largest threat to the quantitative results.
- A systematic comparison of OASIS Stereotype Scores against existing bias metrics (e.g., Jha et al. 2024's "stereotype tendency") on the same generated dataset would demonstrate that the new definition changes conclusions in practice.
- A brief discussion of the normative limitations of using real-world statistics as ground truth would strengthen the paper's framing.
- Quantitative evaluation of StOP (overlap with human-annotated stereotype dictionaries) would move it from illustrative to evidential.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

1. **"Core metrics not defined in main paper"** — Sections 3.1–3.4 containing formal definitions, Eq. (2), Eq. (8), and Eq. (11) were stripped by the text extraction parser. The paper references these sections and equations throughout (including the concluding remarks), confirming they existed in the original submission. This is a parsing artifact, not an author omission.
2. **"Table 1-2 numerical values not visible" / "Figure 6 y-axis not readable"** — Parser artifacts (embedded images).
3. **"Section 3 is shortest and most incomplete"** — Parser truncation. The text cuts off mid-sentence at the end of Section 3's introduction.
4. **"Reproducibility details missing"** — The paper explicitly states "Implementation details are mentioned in §A.1" (appendix stripped by parser).
5. **Strength: "Quantitative link between Internet footprint and stereotype severity"** — Conflicts with the verified weakness that this evidence (N=3, no statistical measures) is too thin to support the claimed "clear" inverse correlation. Removed per the rule that when a strength and verified weakness disagree, the weakness wins.
6. **"Missing related works"** — Cannot be confirmed without external sources; per instructions, do not mention missing related works.

## Novel Insights

The reviews surface one genuinely insightful observation beyond the paper's own contributions: the tension between using real-world statistics P*(A|C) as the normative reference point for stereotypes and the possibility that those real-world distributions are themselves shaped by historical discrimination. The paper treats "matching the real world" as the gold standard, but if the real-world distribution of, say, doctors by gender is itself the product of structural discrimination, then matching it perpetuates the problem. This is not a fatal flaw — one could argue the metric measures *faithful representation* rather than *fairness* — but the paper would benefit from explicitly addressing this framing choice. The reviews also collectively highlight that the paper's ambition (four components spanning measurement and understanding) outstrips the empirical rigor applied to each component individually.

## Suggestions

1. **Validate the attribute classifiers.** Report precision/recall of CLIP ViT-G-14 on each attribute used in Tables 1-2, either through a human evaluation on a sample of generated images or through comparison against an established attribute-classification benchmark. Without this, the quantitative results remain unverifiable.

2. **Expand the Internet footprint analysis.** Either gather data for more nationalities, report correlation coefficients with confidence intervals, or explicitly frame this as an exploratory observation rather than a main finding. Acknowledge confounds (training data composition is unknown; Internet user count is a coarse proxy).

3. **Include control attributes in the SPI analysis.** Show that non-stereotypical attributes (e.g., "facing left vs. right," "indoor vs. outdoor") do *not* exhibit the same early-step emergence pattern. This would strengthen the claim that the phenomenon is stereotype-specific.

4. **For the predisposition analysis, report results over many samples with summary statistics** rather than 3 handpicked examples. This would move the finding from suggestive to evidential.

5. **Acknowledge the normative dimension** of choosing real-world distributions as the stereotyping reference point, even briefly, to preempt the obvious philosophical objection.

## Score and Decision

The paper tackles an important and timely problem with a conceptually well-motivated framework. The directional stereotype definition is a genuine improvement over statistical parity, and the multi-component design (distributional + spectral + internal + temporal) is ambitious and offers a richer view of stereotypes than existing tools. However, in its current form, the empirical execution does not match the conceptual ambition. The lack of attribute classifier validation undermines the quantitative results that form the backbone of the paper's empirical claims, and key additional findings (Internet footprint correlation, SPI emergence, predisposition) are supported by evidence that is thin relative to the strength of the conclusions drawn. The paper needs substantial empirical strengthening before its contributions can be fully trusted. With those revisions, the paper could be a solid contribution; in its current form, it falls short.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>