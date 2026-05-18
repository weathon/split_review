I have thoroughly read the paper and verified each reviewer claim against the actual text. Now I'll produce the consolidated review.

---

## Summary

This paper proposes OASIS, a toolbox for measuring and understanding stereotypes in text-to-image (T2I) models. The key innovations are: (1) a directional stereotype definition grounded in real-world distributions (rather than statistical parity), (2) two metrics — Stereotype Score (distributional) and WALS (spectral variance), and (3) two understanding methods — StOP (discovers what attributes the model internally associates with a concept) and SPI (quantifies when stereotypical attributes emerge during generation). The paper evaluates SDv2, SDv3, and FLUX.1 on three nationalities and finds that despite fidelity improvements, strong stereotypical predispositions persist.

## Strengths

1. **Sociologically grounded directional definition of stereotypes**: The paper correctly identifies that prior work conflates bias (any deviation from uniform) with stereotype (directional over-representation relative to reality). The turban example (Tab. 1 Remark) concretely demonstrates why uniform parity is wrong: requiring 50% turban for Iranian images when only 0.2% of Iranians wear turbans would itself be a misrepresentation. This is a meaningful conceptual advance over prior work.

2. **Complementary dual metrics (Stereotype Score + WALS)**: Fig. 5 shows that SDv3 achieves lower stereotype scores at the cost of lower WALS (spectral variance), proving that a single metric gives an incomplete picture. This is a principled design choice that other evaluation frameworks should adopt.

3. **Open-set stereotype discovery via StOP**: Rather than relying on a predefined closed set of attributes, StOP uses an LLM to generate candidate stereotypes and optimizes prompts to surface model-internal associations. Tab. 3's discovery of culturally specific terms like "Imam" and "brero" demonstrates that the method surfaces stereotypes no predefined classifier would capture.

4. **SPI reveals early emergence of stereotypes**: Fig. 6 shows that stereotypical attributes like beard and traditional clothing form within the first 3–20 generation steps, demonstrating that stereotypes are not late-stage artifacts but core predispositions built into the model's initial trajectory. This is the paper's most novel empirical insight.

5. **Cross-model comparison across generations**: Tab. 1 systematically compares SDv2, SDv3, and FLUX.1 on the same pipeline, isolating stereotype persistence from fidelity improvements. Even FLUX.1 maintains a 92.1% stereotype score for beard in Iranian images (98.4% generated vs. 6.3% real).

6. **Intersectional analysis reveals limitation of single-concept debiasing**: Tab. 2 shows that SDv3 reduces gender imbalance for "doctor" alone, but adding a nationality (e.g., "Iranian doctor") worsens the imbalance — a practical finding with real implications for mitigation strategies.

## Weaknesses

### Major

1. **The Internet-footprint finding rests on only three data points, far too few to support the claim.** Section 4.2 and Fig. 3 compare stereotype scores across Indian, Mexican, and Iranian nationalities against their Internet user counts. Three points cannot sustain a general conclusion about the relationship between Internet footprint and stereotype severity. Many confounds exist (cultural distance from training data, language representation, geopolitical prominence) that are not controlled for. The paper hedges somewhat ("suggest," "may be exacerbated"), but Fig. 3's caption ("shows that stereotypes are higher for underrepresented nationalities") overstates what three points can show. This weakness is substantive because the paper's narrative uses this observation to motivate calls for increased participation of under-represented communities.

2. **The open-set attribute pipeline (LLM generation + CLIP detection) is used without any validation.** The paper generates candidate stereotypes via ChatGPT (Eq. 2) without evaluating whether the generated attribute set is complete, relevant, or introduces LLM-specific biases. Similarly, CLIP ViT-G-14 is used to estimate P(A|D,C) without assessing its accuracy for fine-grained attributes like "wearing a turban" or "mustache." The quantitative scores in Tables 1 and 2 may reflect artifacts of this unvalidated pipeline rather than genuine model stereotypes. At minimum, a human evaluation of a subset of attributes and CLIP classifications would be needed to establish that the measurement pipeline is trustworthy.

### Minor

3. **Using the real-world distribution as the stereotype-free baseline is not defended or discussed as a limitation.** The paper defines stereotypes as P(A|D,C) > P*(A|C), where P*(A|C) comes from real-world statistics. But real-world distributions of attributes like gender ratios in professions are themselves shaped by historical inequalities, cultural norms, and social stereotypes. The paper does not discuss when and whether this baseline is appropriate, or acknowledge that it may embed the very stereotypes one wishes to detect. This does not invalidate the metric (measuring *amplification* of real patterns is valuable), but the paper's claim of "aligning with the sociological definition of stereotypes" requires a more nuanced treatment of what the baseline represents.

4. **"Understand the origins" overstates what the methods actually do.** StOP discovers *what* attributes the model associates with a concept, and SPI shows *when* they emerge during generation. This is about where and when stereotypes manifest, not *why* the model has those associations (e.g., from training data distribution, architecture, or objective). The paper's framing conflates description with causal explanation. The methods are still useful — they reveal internal model structure — but the language in the title and conclusion ("understand their origins") should be calibrated to "identify where stereotypes reside and when they appear."

5. **The StOP output is shown only qualitatively.** Tab. 3 presents optimized prompts and visually similar images, but there is no quantitative evaluation — e.g., do human raters confirm that the optimized prompts capture genuine stereotypes? How much do the optimized prompts diverge from neutral prompts? A quantitative grounding would strengthen the claim that StOP discovers meaningful internal associations.

6. **No ethical discussion of using LLMs to generate stereotype lists.** The paper uses ChatGPT to generate candidate stereotypical attributes for nationalities, which could produce offensive terms or mischaracterizations. There is no description of how the prompts were constructed to avoid harmful outputs, what filtering (if any) was applied, or how this risk was managed. This is a standard expectation for work that systematically surfaces stereotypes.

### Trivial

7. The paper uses "stereotype" and "bias" in close proximity (e.g., "stereotypical biases" in the introduction, "gender imbalance" discussed alongside "intersectional stereotypes" in Section 4.1). While the distinction is conceptually clear, some phrasings could confuse readers about which construct is being measured in a given analysis.

## Nice-to-Haves

- A broader set of nationalities for the quantitative analysis (even 5–7 would substantially strengthen the Internet-footprint observation).
- Human validation of a random subset of LLM-generated attributes for completeness and relevance.
- CLIP accuracy verification against manual annotation for a small set of attribute detections (e.g., turban, mustache, beard).
- A brief summary of the P* source methodology in the main text rather than only in the appendix reference.
- Quantitative evaluation of the StOP-optimized prompts (e.g., attribute overlap metrics, human ratings of stereotypical content).

## Removed Points

These points were raised by reviewers but are removed or downgraded for the following reasons:

- **"WALS is insufficiently described in the main text"**: The paper says "as mentioned in §3.2" — Section 3.2 is a parser artifact (stripped from extraction). In the original submission, this definition exists. Removed.
- **"Real-world statistics source not reported in main text"**: The P* values are given in Tab. 1; the source methodology is cited to §A.1.3. This is standard practice and not a weakness. Removed.
- **"Missing appendix/proofs content"**: Parser artifact — these sections exist in the original submission. Removed.

## Novel Insights

The most insightful observation emerging from the review process is that the paper's four components (Stereotype Score, WALS, StOP, SPI) form a genuinely complementary toolkit where each addresses a distinct gap left by the others — Stereotype Score catches directional over-representation that uniform metrics miss, WALS catches homogenization that distributional metrics miss, StOP surfaces attributes that no predefined checklist would capture, and SPI reveals that these stereotypes are not surface artifacts but are baked into the earliest generation trajectory. This architecture is the paper's strongest contribution and is resilient to many of the empirical concerns raised. However, the validation gap between the ambitious framework and the thin empirical execution (3 nationalities, no pipeline validation) creates a mismatch — the framework is ready for broad adoption, but the paper's own demonstration of it is narrower than it should be. The Internet-footprint finding is an interesting hypothesis generator, not a verified result.

## Suggestions

1. **Acknowledge and discuss the real-world baseline limitation.** Reframe the metric as measuring *amplification* of real-world patterns and discuss conditions under which the baseline is appropriate. This would strengthen rather than weaken the contribution.

2. **Add at least 2–3 more nationalities to the quantitative analysis** (ideally spanning a wider range of Internet footprints and geographic/cultural regions) or, if this is infeasible, reframe the Internet-footprint section as a speculative observation rather than a finding.

3. **Validate a subset of the LLM-generated attributes** with a small human evaluation (e.g., 50 attributes × 3 raters, measuring relevance and stereotypicality) to establish that the open-set generation is not introducing noise.

4. **Report CLIP's accuracy** on a small manually annotated sample for the specific attributes used (beard, mustache, turban, traditional clothing), or discuss known limitations of CLIP for these detections.

5. **Tone down the "origins" language** in the title and abstract. Replacing "understand their origins" with "localize their emergence" or "trace their appearance" would be more accurate.

6. **Include an ethics statement** describing how the LLM was prompted to avoid offensive stereotype generation and what safeguards were applied.

7. **Provide a quantitative summary** of StOP's output (e.g., attribute token frequency, semantic distance from neutral prompts) to complement the qualitative examples.

## Score and Decision

**Originality**: High — the directional definition, WALS, and SPI are novel contributions. Prior work used uniform parity and didn't probe emergence timing.

**Quality**: Moderate — the framework is well-designed but the empirical evaluation is thin (3 nationalities, unvalidated pipeline).

**Clarity**: Good — the paper is generally well-written despite parser artifacts in the review copy.

**Significance**: High — if validated, OASIS would be a useful auditing tool. The finding that stereotypes are encoded in early generation steps has practical implications for mitigation.

The core framework is genuine and useful, but the paper's empirical support for the Internet-footprint claim is substantially weaker than the paper's framing suggests, and the measurement pipeline needs validation before the quantitative results can be taken at face value.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>