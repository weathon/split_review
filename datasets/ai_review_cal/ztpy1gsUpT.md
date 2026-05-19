- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have a thorough understanding of the paper and can verify the claims. Let me write the final consolidated review.

## Summary

This paper proposes FTC (Fine-Tuning with Context), a pipeline that extracts medical keywords from clinical text via NER, uses them (with few-shot clinician demonstrations) to prompt GPT-3.5 to generate medical context, and then feeds that context as additional input when fine-tuning a small language model (SLM) on multiple-choice medical QA. The method yields substantial gains over standard fine-tuning across MedQA, HEADQA, and MedMCQA in both full-training and few-shot settings, demonstrates out-of-domain generalization, and extends to general-domain QA tasks. The core idea—using keyword-based LLM prompting to improve a locally-trainable SLM under a data-sharing constraint—is practically motivated and produces clean results.

## Strengths

1. **Large and consistent empirical gains across multiple settings.** FTC with BioMedLM achieves 55.90% on MedQA and 63.17% on HEADQA test sets—outperforming prior methods including VOD+BioLinkBERT (55.0%) and DRAGON (47.5%) (Table 1). The improvements over standard fine-tuning (SFT) are large and consistent across full training, few-shot, and OOD settings.

2. **Ablation studies convincingly isolate the source of improvement.** The No Relation ablation (Figure 2b) shows that removing relationship information from contexts still yields substantial gains over SFT (~15% absolute), demonstrating that the SLM learns substantive medical knowledge rather than simply pattern-matching relationships. This is a well-designed ablation.

3. **Robust few-shot results with a dramatic headline finding.** With only 100 training samples, FTC improves over SFT by 14.12% on MedQA and 22.57% on HEADQA (Table 2), and even exceeds SFT trained on the full dataset. These numbers are noteworthy even if the evidence base is limited to 3 splits.

4. **Controlled privacy-budget comparison.** The paper compares keywords against random spans and random words at the same compression ratio (Table 6), showing keywords produce the best downstream accuracy. This provides evidence that using *meaningful* extracted tokens (not just any compressed representation) is responsible for the gain.

## Weaknesses

### Major

1. **Privacy framing is overstated relative to what the method provides.** The title uses "Privacy-preserving Contextual Prompting," and the paper repeatedly presents keyword extraction as a privacy mechanism. However, the method does not provide any formal privacy guarantee—it reduces the *amount* of data sent to the LLM, but a single keyword (e.g., a rare disease name or a specific medication) can carry high sensitivity. The "privacy budget" defined in Section 4.5 is explicitly a ratio of word counts (keywords/question words ≈42%), i.e., a measure of input compression, not privacy protection. The paper positions itself against differential privacy and de-identification work in the related work section (lines 65–66) but neither compares against nor rules out the need for such methods. The core contribution—keyword-based LLM prompting to improve SLMs—is useful regardless. But the "privacy-preserving" framing risks misleading readers about the level of protection offered. The paper should replace "privacy-preserving" with a more precise descriptor such as "reduced-data prompting" and explicitly state the limitations of keyword-based protection in a limitations section (which is currently absent).

2. **Few-shot evidence for the strongest claim is thin.** The paper claims that FTC with 100 examples beats SFT trained on the full dataset—a dramatic finding (e.g., HEADQA: 55.03 vs. 41.00). But this rests on only 3 random data splits with a single run per split (line 163: "we randomly generate three data splits... performing a single run for each split"). No statistical significance testing is reported. Given the magnitude of the claim, the evidence should be stronger: at minimum 5–10 splits and bootstrapped confidence intervals. The standard deviations are moderate (e.g., ±1.03 on MedQA 100-shot), but the core comparison (100-shot FTC vs. full-data SFT) does not share the same experimental conditions, so a formal test would be valuable.

3. **No limitations section acknowledging keyword-based privacy risks.** The paper does not discuss that (a) keywords may still contain identifiable information (names, rare conditions, dates), (b) the LLM could potentially reconstruct sensitive information from keyword patterns, or (c) the method should be combined with formal de-identification or differential privacy for actual deployment. The abstract and conclusion present the method as a solution to privacy concerns without hedging. This is a framing gap rather than a technical one, but it needs to be addressed for the paper's claims to match its evidence.

### Minor

1. **The SOTA claim mixes privacy-restricted and unrestricted baselines without clear demarcation.** Table 1 compares FTC against VOD, DRAGON, QA-GNN, etc.—most of which operate without any privacy constraint (e.g., VOD retrieves full-text passages). The paper hedges with "within privacy-restricted scenarios" (abstract, line 5), but the table caption and main text (line 159: "FTC with BioMedLM achieves SOTA performance on both MedQA and HEADQA datasets") do not consistently mark which comparisons are apples-to-apples on the constraint. Against the methods that clearly operate under the same constraint (SFT, LLM prompting), FTC wins decisively—which is a real result. The comparison to non-restricted methods is informative contextually, but the paper should mark this distinction in the table and temper the SOTA claim accordingly.

2. **The OOD claim is slightly overstated.** The paper states "FTC consistently outperforms both SFT in OOD settings and LLM prompting baselines" (line 221). In Table 3, for MedQA→HEADQA, FTC achieves 47.26±0.96 while the LLM achieves 47.50—FTC is slightly lower (within 1σ). The overall OOD pattern strongly favors FTC (8 of 9 comparisons beat LLM), but the "consistently" qualifier is technically inaccurate for this one cell. A small wording fix.

3. **No ablation of the number of clinician demonstrations (M=5).** The method uses M=5 clinician-written examples for few-shot prompting. The paper provides no sensitivity analysis (e.g., M=1, 3, 5, 10) to justify this choice or show how dependent the results are on the quality/quantity of these examples. This is a non-trivial component of the pipeline.

4. **General-domain experiments use a different architecture (T5-base + FiD) than the medical experiments (BioLinkBERT/BioMedLM with concatenation).** This change makes it difficult to attribute the gains specifically to the prompting pipeline versus the architectural shift. The general-domain result is a secondary contribution, so this is minor, but a consistent setup would strengthen the generalization claim.

### Trivial

- None beyond what is addressed above.

## Nice-to-Haves

- A manual audit of ~100 extracted keyword sets to quantify how often they contain obvious identifiers (names, dates, locations) would substantially ground the privacy discussion.
- An analysis of LLM-generated context quality (e.g., manually categorizing contexts as "correct reasoning," "incorrect but informative," or "misleading") would enrich the FTCR ablation.
- Releasing the five clinician demonstrations used for each dataset would aid reproducibility.

## Removed Points

These points surfaced in the reviews but are removed for the reasons stated:

1. **"No evaluation of what keywords actually look like"** — The paper includes a case study (Figure 7 / `fig:contextanalysis`) with examples of keywords, contexts, and predictions. While a systematic audit would be stronger, the claim that there is *no* evaluation is inaccurate.

2. **"Privacy analysis measures input compression, not privacy" (as a fatal flaw)** — The paper transparently defines its metric as a word-count ratio ("estimating information usage," line 354). The issue is the *framing* of this as a privacy analysis, not that the metric itself is wrong or hidden. This is captured in the Major weakness 1 above at the appropriate severity.

3. **"Inconsistent comparison set invalidates the method's contribution"** — The paper explicitly qualifies its SOTA claim with "within privacy-restricted scenarios." Against the methods that clearly operate under this constraint (SFT, LLM prompting), FTC wins handily. The comparison to VOD/DRAGON is informative context. This is a presentation clarity issue, not an evidential one.

4. **"The FTC vs LLM OOD claim is contradicted"** — In 8 of 9 OOD settings FTC beats LLM; the one exception (MedQA→HEADQA: 47.26 vs 47.50) is within standard deviation. This is a wording precision issue captured in Minor weakness 2.

5. **"Should compare against differential privacy methods"** — The paper's contribution is a prompting pipeline for improving SLMs under a data-sharing constraint, not a privacy mechanism per se. Requiring DP comparisons would be scope creep. The framing should be toned down, but DP comparison is not needed.

6. **Strength about "important problem"** — Generic; all papers claim to address an important problem. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally new interpretation of the method or results that the paper itself does not provide.

## Suggestions

1. **Rename the method and tone down the privacy language.** Replace "privacy-preserving contextual prompting" with "keyword-based contextual prompting" or "reduced-data prompting." Change the title accordingly. The method's genuine contribution—improving SLMs via keyword-based LLM context generation—stands on its own merits without overclaiming privacy.

2. **Add a limitations section.** Explicitly state that keyword extraction does not guarantee privacy, that keywords may contain sensitive information, and that the method should be combined with formal de-identification or differential privacy for real-world deployment.

3. **Strengthen the few-shot evidence.** Increase the number of random splits (5–10) and report bootstrapped confidence intervals or significance tests for the headline claim (100-shot FTC vs. full-data SFT).

4. **Clarify the SOTA claim.** Mark which baselines in Table 1 operate under the same privacy constraint (e.g., with a footnote) and which do not. Restrict direct SOTA claims to the privacy-restricted subset, and present comparisons to unrestricted methods as contextual performance reference.

5. **Ablate M** (number of clinician demonstrations). Run M ∈ {1, 3, 5, 10} on one dataset to show sensitivity.
