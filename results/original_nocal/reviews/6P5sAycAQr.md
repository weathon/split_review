Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

The paper introduces DefNTaxS, a fully automated, training-free framework that uses LLMs to discover semantic subcategories among a dataset's classes and integrates this taxonomic context into CLIP prompts for zero-shot image classification. The method operates in four steps: LLM-based subcategory generation, class-to-subcategory assignment, granularity optimization (~20 classes per subcategory), and prompt construction combining class descriptors with contextual phrases. Across seven standard benchmarks, DefNTaxS achieves average gains of +5.5% over vanilla CLIP and +2.44% over D-CLIP, with total LLM API cost of $0.38.

## Strengths

- **Consistent accuracy gains across diverse benchmarks.** Table 1 shows DefNTaxS achieving the highest accuracy on 5 of 7 standard benchmarks (IN, CUB, Pets, DTD, ESAT) with an average +5.5% over CLIP and +2.44% over D-CLIP. The gains are not confined to one domain, spanning fine-grained bird classification (CUB), texture recognition (DTD), satellite imagery (EuroSAT), and general object classification (ImageNet). The paper also reports ImageNetV2 results (+0.66% over D-CLIP), providing some evidence that gains generalize beyond the original test distribution.

- **Fully automated, training-free pipeline with trivial cost.** Section 3 describes a completely automated four-step procedure requiring no manual prompt engineering, model retraining, or additional optimization data. Section 4.2 reports total LLM API cost of only $0.38 for all datasets — a genuine practical advantage over methods requiring hand-crafted templates (E-CLIP) or multiple inference passes (CHiLS, CGPT-P).

- **Ablation analysis exploring components of the method.** Tables 3 and 4 systematically vary elements of the DefNTaxS pipeline (adding taxonomic descriptors, removing descriptors, replacing subcategory labels with random characters, replacing descriptors with random characters). The paper honestly reports mixed results (e.g., WaffleTaxS matching DefNTaxS on ImageNet) and discusses possible causes (token position effects). This transparency is to the paper's credit, even though it undercuts the strongest version of the central claim.

- **LLM-based clustering validated against k-means.** Table 5 shows DefNTaxS's LLM-driven subcategory generation consistently outperforms a k-means alternative across all seven benchmarks (average +0.92%, largest gain +3.19% on EuroSAT), confirming that the LLM's semantic grouping provides a meaningful advantage over naive embedding-based clustering.

## Weaknesses

### Fatal

None. The paper's core contribution — an automated method for integrating taxonomic context into CLIP prompts that yields consistent empirical improvements — is real and supported by the data. The weaknesses below are substantive but addressable.

### Major

- **Overclaimed central thesis: the claim that taxonomic context is "essential" is not supported by the paper's own ablation results.** The paper repeatedly states that taxonomic context is "essential" (Abstract), "not just helpful but *essential*" (Section 1, Section 5), and that the work "establishes taxonomic context as a fundamental requirement for robust zero-shot classification" (Section 7). However, Table 4 shows that WaffleTaxS — which replaces the taxonomic subcategory label with *random characters* — matches or exceeds DefNTaxS on ImageNet (63.24 vs. 62.96), Places (40.05 vs. 39.34), CUB (53.65 vs. 53.59), and Food (80.90 vs. 81.10). On these datasets, random noise provides as much benefit as the semantic subcategory. This directly undercuts the "essential" framing. The paper acknowledges "mixed results" (line 273) but the rhetorical framing throughout (abstract, introduction, conclusion) does not reflect this nuance. A more measured claim — e.g., "taxonomic context provides meaningful gains on datasets where fine-grained semantics are the primary driver, while differentiation alone accounts for gains on others" — would better match the evidence.

- **EuroSAT result is confounded and cannot be cleanly attributed to taxonomic context.** EuroSAT has only 10 classes, so per Section 3.3 the method falls back to using the dataset name as the single subcategory context: "EuroSAT dataset." The reported gain is +13.0% over CLIP and +9.86% over D-CLIP — by far the largest improvement across all benchmarks. However, (1) this context is trivial (just the dataset name, not a meaningful taxonomy), (2) Table 3 shows that even without any descriptors ("no desc." at 55.90%), most of the gain over D-CLIP (47.36%) remains, and (3) D-CLIP's EuroSAT baseline of 47.36% is notably low relative to CLIP's 44.26%, partly because D-CLIP's descriptor format may be less suited to satellite imagery. Without a controlled comparison — e.g., D-CLIP + "a satellite image of" appended to the prompt — we cannot determine whether the EuroSAT gain stems from taxonomic context, prompt format/length changes, or simply having more tokens. The paper's framing of EuroSAT as the "most compelling" example of taxonomic disambiguation is misleading.

### Minor

- **Main results (Table 1) are reported without variance estimates.** The core comparison table reports single-run numbers for all methods. Only the ablation in Table 4 includes standard errors (over 5 iterations). Given that several reported gains over D-CLIP are sub-1% (IN: +0.48%, Places: +0.16%, Food: +1.05%, INV2: +0.66%), the absence of confidence intervals makes it impossible to assess whether these differences are meaningful or within noise. While single-run evaluation is common practice in zero-shot CLIP papers, claims of "state-of-the-art" at sub-1% margins demand more statistical rigor.

- **Slightly overstated SOTA claims in presentation.** The paper states "DefNTaxS achieving the highest accuracy across six of seven benchmarks" (line 201) and "consistent state-of-the-art performance across seven benchmarks" (line 299). However, on Food, CHiLS achieves 83.53% vs. DefNTaxS's 81.48%; on Places, CHiLS achieves 40.45% vs. DefNTaxS's 40.00%. DefNTaxS achieves SOTA on 5 of 7 benchmarks, not 6 or 7. Additionally, the DefNTaxS row in Table 1 is bolded across all columns including Food and Places where it is not the best, creating a misleading visual impression.

- **No controlled comparison separating taxonomic context from prompt template changes.** The DefNTaxS prompt template (Section 3.5) differs from D-CLIP in both structure ("[class] which [has/is] [descriptor], [contextual phrase] [subcategory]") and length (the subcategory phrase adds tokens). The paper never evaluates the simplest possible control: D-CLIP prompt + subcategory name appended as an additional phrase. Without this baseline, we cannot attribute gains to the *semantic content* of the taxonomic context versus the mechanical effects of longer prompts or token-position changes (which the paper itself acknowledges as a potential confound at line 252).

### Trivial

- The paper should clarify at line 179 that all baselines were recreated using the same GPT-4o-mini API (the text at line 161 and line 155 already implies this, so it's clear to a careful reader but could be more explicit).

## Nice-to-Haves

- Evaluate on a dataset where classes genuinely exhibit cross-domain ambiguity (e.g., "boxer" appearing as both dog breed and sport) — none of the current benchmarks primarily test this type of ambiguity that motivates the paper's framing.
- Show qualitative examples (misclassifications corrected by DefNTaxS with the taxonomic context as the plausible cause) to make the mechanism more transparent.
- Test whether a simple baseline of adding "a type of [dataset name]" to D-CLIP prompts recovers part of the EuroSAT gain.

## Removed Points

- **LLM model choice unclear**: The harsh critic claimed the paper does not state whether D-CLIP was re-run with GPT-4o-mini. Lines 155 and 179 explicitly state that all experiments use the same modified pipeline due to GPT-3 API deprecation, with GPT-4o-mini for all methods. This criticism is factually wrong.
- **Edge case handling is ad hoc/underspecified**: The critic faults the method's handling of conflicting class assignments (§3.2). While the description is brief, this is an edge case with no evidence it significantly impacts results on these benchmarks. A minor procedural detail of this nature does not constitute a substantive weakness.
- **"The paper never quantifies how many classes in these benchmarks are truly ambiguous"**: This demands a form of analysis that is useful but not required to validate the method's contribution, which is about improving classification accuracy, not diagnosing ambiguity prevalence.
- **Criticism about ~20 classes per subcategory being arbitrary with missing justification**: The paper explicitly references Appendix D for the empirical analysis supporting this choice. Since appendix content is stripped by the parser, this criticism cannot be verified and is removed per instructions.
- **Reproducibility nitpicks** (undisclosed token counts, number of LLM calls per dataset): These are trivial implementation details not expected to be in a 9-page submission.
- **Generic speculation** (e.g., "could the metric be measuring a proxy?", "are confounders controlled?" phrased as concerns rather than identified problems): These lack specific anchors in the paper content.
- Several formatting and stylistic nitpicks that reflect parser artifacts, not author errors.
- **Strength Finder claim about "ablation isolating the necessity"**: This is weakened because the ablations actually show mixed results. The strength is retained as the paper conducting thorough ablations, but the "necessity" framing is dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the method or results that the authors themselves do not discuss.

## Suggestions

1. **Temper the central claim.** Replace "essential" (which appears 5+ times with strong emphasis) with language like "consistently beneficial" or "provides meaningful improvements." The ablation showing WaffleTaxS matching DefNTaxS on several datasets is honest data, and the framing should match it.

2. **Add standard errors to Table 1** (or at minimum, 3-run averages for the main comparison). Several gains are sub-1%; without variance estimates these are uninterpretable for SOTA claims.

3. **Run a controlled comparison:** D-CLIP + subcategory name appended to the prompt (e.g., "fork, which has tines, a type of kitchen utensil" vs. D-CLIP's "fork, which has tines"). This directly tests whether the taxonomic *content* matters beyond just having more tokens.

4. **Acknowledge the EuroSAT confound explicitly** and either (a) add a control experiment adding "a satellite image of" to D-CLIP prompts, or (b) present the EuroSAT result with appropriate caveats rather than as the headline "most compelling" example.

5. **Correct the bolding in Table 1 and the "six of seven" claim.** CHiLS objectively achieves higher accuracy on Food and Places; this should be reflected in the table formatting and text.

6. **Expand the WaffleTaxS discussion** to more clearly address why random subcategory labels work on some datasets — is the mechanism purely about differentiation (adding distinguishable tokens), or is something else happening? The current speculation about token position effects (Section 6.1.3, Appendix C) needs stronger evidence.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>