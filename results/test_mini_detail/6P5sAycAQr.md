Now I have a strong understanding of the calibration landscape. Let me write my consolidated review.

## Summary

The paper proposes DefNTaxS, a fully automated method that uses LLMs to discover taxonomic subcategories for zero-shot CLIP classification. The approach works by: (1) querying an LLM to partition classes into semantic subcategories, (2) assigning each class to a subcategory, (3) ensuring subcategories have ~20 classes each via refinement, and (4) generating prompts that combine class descriptors with taxonomic context phrases. The method requires no model retraining or manual prompt engineering and costs $0.38 in LLM API fees across all datasets. The paper reports +5.5% average improvement over vanilla CLIP and +2.44% over D-CLIP across 7 benchmarks, with a notable +13% gain on EuroSAT.

## Strengths

1. **Thorough ablation study that engages honestly with uncomfortable results**: Tables 2–4 systematically probe what drives performance — reduced refinement, modified descriptors, and replacing components with random characters. The paper openly reports (and attempts to explain) cases where variants are competitive with the full method. This level of diagnostic analysis is more informative than the typical "our method always wins" ablation.

2. **LLM-based clustering demonstrably outperforms unsupervised alternatives**: Table 5 shows DefNTaxS (LLM clustering) beats k-means clustering on all 7 benchmarks (+0.92% average), with a notable +3.19% gap on EuroSAT. This provides concrete evidence that the LLM's semantic understanding adds value beyond what a simple embedding-space clustering can achieve.

3. **Practical advantages are real and well-documented**: The method is fully automated (no manual prompt engineering), requires no training or additional data, and costs only $0.38 in LLM API fees for the entire experimental suite. These properties make the approach immediately deployable.

4. **Clear framing of the motivation and method**: The paper articulates a genuine limitation of prior work — that isolated descriptors and hierarchical structures miss lateral semantic relationships — and describes a four-step pipeline that operationalizes this insight in a straightforward way.

## Weaknesses

### Fatal
None.

### Major

1. **EuroSAT baseline numbers are suspicious, undermining the headline result**: E-CLIP scores 33.44% on EuroSAT and W-CLIP scores 31.49%, while the bare CLIP baseline ("{class}") achieves 44.26%. It is extremely unusual for a prompt ensemble (E-CLIP uses 80 hand-crafted templates) to perform *worse* than a single bare class name by ~11%. On every other dataset in Table 1, E-CLIP improves over or matches CLIP (e.g., +3.01% on IN, +4.22% on Pets). The EuroSAT anomaly — which happens to be the dataset where DefNTaxS shows the largest gains (+13%) — calls into question whether the reported improvements reflect genuine taxonomic disambiguation or a degraded comparison baseline. The paper acknowledges "a modified version of D-CLIP's generation pipeline" was used due to API deprecation, but does not discuss why E-CLIP and W-CLIP collapse on this particular dataset.

2. **The paper's own ablation contradicts the claim that taxonomic semantics are "essential"**: Table 4 shows that WaffleTaxS (replacing taxonomic subcategory labels with *random characters*) *outperforms* the full DefNTaxS on ImageNet (63.24 vs. 62.96) and Places365 (40.05 vs. 39.34), and ties on Food101 (81.10 vs. 80.90 within error bars). If random characters replacing the core taxonomic content can match or beat the full method, the paper's central thesis — that "taxonomic context is not just helpful but **essential**" — is not supported by the evidence. The authors acknowledge this result but the framing of the paper's contribution (abstract line: "the inevitable need for context in classification"; contribution line: "taxonomic context is not just helpful but *essential*") is in tension with this finding.

3. **Main results lack statistical significance reporting despite very small margins**: The improvements over D-CLIP on ImageNet (+0.48%), CUB (+0.79%), and Places365 (+0.16%) are well within typical run-to-run variation of CLIP-based zero-shot classification (±0.3–0.5%). Table 1 reports a single point estimate with no confidence intervals or error bars. The ablation study (Table 4) does include standard errors, which makes their absence in the primary results table conspicuous. Readers cannot determine whether these small gains are meaningful or noise.

4. **State-of-the-art claims are overstated**: The abstract and conclusion claim "state-of-the-art across seven benchmarks" and "highest accuracy across six of seven benchmarks." Table 1 contradicts this: CHiLS achieves higher accuracy on Food101 (83.53 vs. 81.48) and Places365 (40.45 vs. 40.00). DefNTaxS wins on 5 of 7 benchmarks, not 6. The "six of seven" claim only holds if ImageNetV2 is counted as an 8th benchmark. This overcounting, combined with the absolute "SOTA" language, misrepresents the results.

### Minor

1. **Only a single CLIP backbone (ViT-B/32) is evaluated**: The LLM-based subcategory discovery is independent of the vision encoder, but the benefit of taxonomic context may vary with model capacity (e.g., ViT-L/14, ViT-H/14). Generalization claims are limited without this evidence.

2. **Motivating examples are not validated in the evaluation**: The introduction vividly describes cross-domain ambiguity cases ("boxer" as dog vs. sport, "crane" as bird vs. equipment, "mouse" as animal vs. peripheral), yet none of the seven evaluated benchmarks actually contain such cross-domain homonyms. The paper does not include a targeted experiment showing where taxonomic context resolves genuine ambiguity versus where it simply adds more tokens.

3. **The 20-class-per-subcategory heuristic is empirically motivated but appears in the appendix**: The paper states that "approximately 20 classes per subcategory yields optimal results" based on "empirical analysis (Section Appendix D)" (line 94), but the appendix is stripped by the parser. No sensitivity analysis for this hyperparameter appears in the main text.

### Trivial
None.

## Nice-to-Haves

- **Quantitative analysis of where taxonomic context helps**: The paper would benefit from a per-class or per-subcategory breakdown showing whether gains concentrate in semantically similar class groups, which would directly support the disambiguation narrative.
- **Comparison with WaffleCLIP+concept under identical conditions**: This baseline is closest in spirit to DefNTaxS (high-level semantic concept + descriptors). The paper reports W-CLIP+conc. but uses the original GPT-3-generated concepts rather than matching the LLM and backbone setup.
- **Discussion of failure cases**: Are there datasets or class groups where the LLM-generated subcategories are misleading or unhelpful?

## Removed Points

- *Criticism about "CLIP backbone not explicitly stated"*: The abstract explicitly says "vanilla ViT-B/32 CLIP" (line 13), which is sufficient. The harsh critic's claim that this "should be in Section 4.1" is a formatting preference, not a substantive weakness.
- *Criticism about the prompt template not being compared to alternatives*: The paper presents a single reasonable template. An ablation on template ordering would be nice-to-have but is not a core requirement. This is scope creep.
- *Criticism about "$0.38 cost only covers LLM API"*: The paper states this is the cost for "generating all text across all datasets" (line 211), which is clearly about the LLM query cost. The inference cost is identical to D-CLIP, which is standard practice. This criticism is a misreading.
- *Criticism about "missing backbone evaluation"*: Kept as minor weakness. It is a genuine but not fatal limitation.
- *Criticism about the paper "does not demonstrate that existing methods actually fail" on the chosen benchmarks*: The paper shows that D-CLIP, E-CLIP, etc. achieve lower accuracy than DefNTaxS, which is the standard way to demonstrate that prior methods are less effective. This is a strawman.
- *Strength about "large accuracy gains"* from Strength Finder: The +5.5% average gain is over the bare CLIP baseline ("{class}"), not over a strong baseline. The more relevant comparison is over D-CLIP (+2.44%), which is more modest. This strength is ambiguous and is removed.
- *Strength about "ablation isolates unique contribution of taxonomic semantics"*: Conflicts with verified weakness #2 (WaffleTaxS matching/beating DefNTaxS). Removed per the rule that weakness wins when strength and weakness disagree.

## Novel Insights

An interesting observation emerges from the interaction of Tables 4 and 5. WaffleTaxS (random subcategory labels + real descriptors) beats DefNTaxS (real subcategory labels + real descriptors) on ImageNet and Places365, suggesting that for large/general datasets, the random strings may serve as a *differentiation mechanism* without the semantic narrowing that comes from real category labels. Meanwhile, TaxCLIP (real subcategory labels + random descriptors) performs poorly across the board. This asymmetry — that the *function* of differentiation matters more for some datasets than the *content* of the semantics — echoes the WaffleCLIP finding but extends it to the subcategory level. The paper identifies this tension but does not fully resolve it, leaving an open question: is taxonomic context actually helping via semantics, or is it mainly providing a token-level differentiation signal that could be achieved with random strings? This is a genuinely interesting question for the community.

## Suggestions

1. **Verify and report correct EuroSAT baselines**: Investigate why E-CLIP and W-CLIP perform anomalously low on EuroSAT. Report the corrected numbers and recalibrate the claimed gains. If the baselines cannot be reproduced faithfully, acknowledge this and frame the comparison as internally controlled.
2. **Add error bars to Table 1**: Run each method 3–5 times (or use bootstrap estimates) and report mean ± standard error. This is essential given the small margins on several datasets.
3. **Temper the "essential" language**: The WaffleTaxS result shows that differentiation without semantic content works well on several datasets. Rewrite the central claim to reflect that taxonomic context *often helps* rather than is *essential*, and discuss the conditions under which semantic content vs. mere differentiation drives gains.
4. **Correct the SOTA claim**: Acknowledge that CHiLS achieves higher accuracy on Food101 and Places365. The paper's strongest results are on ambiguity-prone satellite imagery (EuroSAT) and fine-grained domains (Pets, DTD), and the framing should reflect this.

## Score and Decision

**Bracket determination (Round 1):** Initial calibration placed the paper between weak anchors at ~2.5–3.4 (low-quality rejected papers) and strong anchors at ~8.0 (oral acceptances). The topic is most similar to papers in the 4–6 range, so the plausible bracket is [4.0, 6.0].

**Narrowing (Round 2):** Direct comparison with highly similar papers:
- **FuDD** (avg 6.00, Accept poster): Same task (LLM-augmented CLIP prompts), cleaner baselines, more consistent gains, no baseline-anomaly problems. DefNTaxS has more ablations but also more unresolved contradictions → DefNTaxS is weaker than FuDD.
- **SLR-AVD** (avg 4.75, Reject): Similar issues with baseline concerns and marginal improvements. SLR-AVD had fewer ablations. → DefNTaxS is comparable to SLR-AVD.
- **CARPRT** (avg 5.75, Reject): Clean method, small gains, rejected due to marginal contribution. DefNTaxS has bigger gains on some datasets but more methodological concerns. → DefNTaxS is weaker than CARPRT.

The paper falls in the 4–5 range. It has a reasonable idea and thorough ablations, but the suspicious EuroSAT baselines, the WaffleTaxS contradiction of the core thesis, the lack of error bars for small-margin results, and the overstated SOTA claims collectively prevent it from reaching acceptance quality.

**Final score: 4.5 — Reject.** The core idea has merit, but the evaluation has significant unresolved issues that undermine the main claims. A major revision addressing the baseline verification, adding error bars, tempering claims, and resolving the WaffleTaxS tension could raise the paper to acceptance level.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>