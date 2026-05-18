Good. I now have a clear calibration picture. Let me compile the final review.

My bracketing assessment: The paper sits between scores 4 and 6. It is clearly stronger than the score-3 papers (which have fundamental execution issues or data leakage problems) and clearly weaker than the score-7+ papers (which are rigorous, well-controlled contributions). Within the 4-6 bracket, the most comparable anchors are IntentGPT (4.40), ICConv (4.00), ReSpect (5.00), Segmenting Text (5.25), and Bayesian WeakS-to-Strong (5.50). The ConvINT paper has a clearer conceptual contribution than IntentGPT, a more novel framework than ICConv, and comparable empirical scope to ReSpect. However, the reward mechanism ambiguity is a more significant methodological issue than what Bayesian WeakS-to-Strong (5.50) faces, placing it slightly below that.

Final score: **5.0**.

Now writing the review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
None

### Major
- weakness 1 — why it matters
- weakness 2 — why it matters

### Minor
- weakness 1 — why it matters

### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points

## Novel Insights

## Suggestions

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

Wait, decision... This is borderline. Let me think about whether this is an Accept or Reject at 5.0.

At 5.0, the paper has real contributions but significant issues that prevent acceptance in its current form. The reward mechanism ambiguity is a real issue that undermines the claimed contribution of WeRG. The weak baselines mean we can't attribute gains to the right mechanism. However, the ConvINT framework itself is interesting and the dataset contributions are valuable.

I think at 5.0, this is a borderline reject/revise-and-resubmit. Let me check the calibration anchors - IntentGPT (4.40) was Reject, ICConv (4.00) was Reject, ReSpect (5.00) was Reject, Segmenting Text (5.25) was Reject, Bayesian WeakS-to-Strong (5.50) was Accept. So the threshold seems to be around 5.5.

Given the issues with the reward mechanism and baselines, I'll recommend Reject with encouragement to revise (major revision needed to clarify WeRG and add proper baselines).

Actually, wait - the scoring says the final decision should be in the XML. Let me check what the instructions say... It says "MY FINAL DECISION: <decision>Accept/Reject</decision>". So it's binary. At 5.0, I think Reject is appropriate given the issues, but it's borderline.

Let me finalize.Now I'll compose the final consolidated review.

**Round 1 bracket:** I identified the paper sits between scores 4 and 6, anchored by low-band papers at 3.00 (weak execution, data leakage, or poor evaluation) and high-band papers at 8.00 (rigorous, well-controlled). The most relevant middle-band anchors were IntentGPT (4.40), ICConv (4.00), ReSpect (5.00), Segmenting Text (5.25), and Bayesian WeakS-to-Strong (5.50).

**Round 2 narrowing:** Reading these in full confirmed the ConvINT paper is stronger than ICConv (4.00, a dataset paper with limited methodology) and IntentGPT (4.40, data leakage concerns). It is comparable to ReSpect (5.00) and Segmenting Text (5.25) in terms of having a genuine contribution tempered by methodological concerns. It is weaker than Bayesian WeakS-to-Strong (5.50), which has a cleaner method. The reward mechanism ambiguity is a more significant issue than the gaps in those comparable papers.

---

## Summary

This paper proposes ConvINT, a semi-structured intention framework that organizes user utterances into four aspects (situation, emotion, action, knowledge), and WeRG, a weakly-supervised generation method that combines coarse (hard-mapped from existing annotations), mid (LLM-generated), and fine (human-annotated) data with tiered scalar rewards to train an LLM to generate ConvINT annotations. Experiments on DuRecDial and ESConv show that WeRG-generated annotations outperform prompting-only baselines on automatic metrics and improve downstream response generation.

## Strengths

1. **Well-motivated framework grounded in cognitive theory.** The four-aspect ConvINT formalism (situation, emotion, action, knowledge) is explicitly derived from semantic pointer theory (Eliasmith, 2013; Schröder et al., 2014), providing a principled alternative to rigid slot-value structures. The paper articulates a clear problem — that existing CU representations are too shallow for the open-ended intentions LLMs need to handle.

2. **Ablation studies validate the multi-source design.** Table 3 systematically removes each supervision source (D_coarse, D_mid, D_fine) and the quadruple reward. The consistent degradation across conditions supports the claim that all three annotation tiers and the tiered reward contribute to generation quality. The ablation of D_mid causing the largest drop is a meaningful finding.

3. **Downstream task improvements are demonstrated.** Tables 4–5 show that incorporating ConvINT annotations improves Success Rate and reduces turns for DuRecDial response generation (using ChatGPT backbone), and that each of the four aspects independently contributes to ESConv response quality (Table 5). This provides some evidence that the framework has practical utility beyond generation quality metrics.

4. **Human evaluation complements automatic metrics.** Table 2 reports human judgments (Informativeness, Understanding, Conciseness) with Fleiss' kappa, showing WeRG outperforms prompting baselines across all three criteria on both datasets. While the sample is small (50 per dataset), the multi-faceted human assessment strengthens the paper.

## Weaknesses

### Fatal
None.

### Major

1. **The WeRG reward mechanism is underspecified and the RL framing is misleading.** Equation (2) defines the reward as `r_c(h_i, x_i, o_i) = <r_s^{c_i}, r_e^{c_i}, r_a^{c_i}, r_k^{c_i}>` where `c_i ∈ {coarse, mid, fine}`. The paper states these are "simple scalar rewards" with a hierarchy `r_coarse < r_mid < r_fine`, but never clarifies whether the reward depends on the *quality of the generated output* or is a fixed scalar determined solely by the source level. If the latter — as the description suggests — then the RL objective in Equation (3) assigns the same reward to any output from a given source type, regardless of how well it matches the gold annotation. This means the "RL" term in the objective does not incentivize better generations and collapses into a weighted supervised fine-tuning scheme where weights are predetermined by source. The paper invokes the closed-form optimal policy derivation (Eq. 4–5) following Wang et al. (2024), but without a reward function that differentiates output quality, this derivation is not properly grounded. The claimed advantage of RL over simple weighted SFT cannot be evaluated from the presented description. The method may still work in practice as a weighted imitation learning approach, but the paper presents it as principled RL without the necessary specification.

2. **Inadequate baselines for the fine-tuning comparison.** WeRG is a fine-tuning method (SFT data + reward-weighted objective), yet the only comparison methods are zero-shot and few-shot prompting (Direct Prompt, CoT Prompt). The paper lacks SFT-only baselines that would isolate whether gains come from (a) fine-tuning itself, (b) the multi-source data mixture, or (c) the reward hierarchy. Specifically missing: SFT on D_fine alone, SFT on full D_WeRG without reward weighting, and a weighted SFT baseline that assigns loss weights matching the reward hierarchy. The ablation study (Table 3) removes data sources and the reward module (`w/o r_c`), which partially addresses this — `w/o r_c` is effectively a flat SFT on D_WeRG — but the paper would need a proper D_fine-only SFT to demonstrate the value of the multi-source design. Without these baselines, the reported gains over prompting could be largely attributable to fine-tuning rather than to the WeRG mechanism specifically.

3. **Evaluation does not directly measure the quality of intention understanding.** The automatic metrics (F1, BLEU, BERTScore, BARTScore) measure lexical/semantic overlap between generated and gold ConvINT text. These are generation-level proxies and do not directly assess whether specific aspects (emotion labels, action verbs, knowledge entities) are factually correct. The paper would be significantly stronger with aspect-level accuracy metrics — e.g., emotion classification accuracy, action recall, knowledge entity F1 — that test whether ConvINT actually improves *understanding* of user intentions. The human evaluation (50 samples per dataset) covers informativeness and understanding but is too small and coarse-grained to substitute for aspect-level diagnostics.

### Minor

1. **Downstream evaluation on ESConv does not specify the response generation backbone.** Table 4 (DuRecDial) clearly states "utilizing ChatGPT as the backbone generation model," but Table 5 (ESConv) omits this information entirely. This makes it impossible to assess whether the reported gains are specific to a particular backbone or would generalize.

2. **No comparison to alternative intention representations for the downstream task.** The downstream experiments (Tables 4–5) compare ConvINT-augmented generation to generation without ConvINT. They do not compare against alternative structured representations (e.g., traditional slot-value interpretations or free-text summaries), so the unique benefit of the *semistructured four-aspect* format over simpler alternatives is not established.

3. **No statistical significance tests.** Results in Tables 1–5 are reported without error bars, confidence intervals, or significance tests. The reported BERTScore values are very high (>90) across conditions, raising questions about metric discriminability.

### Trivial
- The paper mentions "fine-annotated data comprising 10% of the total dataset" in Section 4.5.2 but never reports the absolute sizes of D_coarse, D_mid, and D_fine.
- The LLM used for mid-level annotations is not specified ("cost-effective LLMs" — which model?).
- Table 2 reports Fleiss' kappa as 0.2–0.6, described as "fair to moderate," which is accurate, but the paper does not discuss how low agreement on some criteria affects the reliability of those scores.

## Nice-to-Haves
- Aspect-level accuracy metrics (emotion F1, action recall, entity F1) would substantially strengthen the claim that ConvINT improves intention understanding.
- An SFT-on-D_fine-only baseline would clarify whether the coarse and mid data sources provide additive value beyond human annotations.
- A comparison against traditional structured output (slots) and free-text summaries would isolate the value of ConvINT's semi-structured format.

## Removed Points

The following points from the harsh critic are removed with justification:

- **"The reward is fundamentally underspecified and likely invalid" — the "fatal" characterization.** Demoted from Fatal to Major. The reward mechanism is indeed underspecified, but this does not invalidate the whole paper. The ConvINT framework and empirical demonstrations have independent value, and the method can be reinterpreted as weighted SFT. The issue is presentation/overclaiming, not that the method cannot work.
- **"Coarse annotation construction is not described" (Section 3.3 note).** The paper states "hard mapping to transform existing structured interpretations into ConvINT labels" — this is minimal but not absent. Moving to Minor/trivial territory.
- **"The model used for mid annotations is not specified."** Retained as Trivial.
- **"Reward values are never disclosed."** Part of Major weakness 1 — merged.
- **"The base policy π_w is poorly defined."** The paper states π_w is "the policy model augmented by the weak supervision signals in D_WeRG." While not fully detailed, this follows a standard formulation from Wang et al. (2024), which is cited. Keeping this as part of Major weakness 1.
- **"No discussion of the size of D_coarse, D_mid, D_fine."** Retained as Trivial.
- **"No analysis of failure cases."** Fair but not a standard requirement for this type of paper. Removed.
- **"No comparison to concurrent weakly-supervised annotation approaches."** Missing related work should not be mentioned per instructions. Removed.
- **"Reproducibility: the LLM used for mid annotations, the specific prompts, the reward values, and the RL algorithm are not provided."** Partially covered by other weaknesses. The LLM specification is a Trivial concern. The reward values and algorithm are part of Major weakness 1.
- **Strength Finder Strength #3 ("Grounded in psychological intention theory").** This is valid — the paper does cite psychological theories to motivate the four aspects. Kept.
- **Strength Finder Strength #5 ("All four aspects contribute independently").** Valid — Table 5 shows this. Kept.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the WeRG reward function, as described, is source-level only (not output-quality-dependent) and that the RL framing is therefore misleading is a genuinely insightful critique. However, this is a meta-observation about the paper's presentation rather than a new research insight. If the paper were to clarify that WeRG is properly understood as a weighted imitation learning / weighted SFT approach (rather than RL), this would resolve the conceptual tension without changing the empirical results.

## Suggestions

1. **Clarify the reward mechanism.** State explicitly whether the reward for a generated output is (a) a fixed scalar per source, (b) a function of similarity between generated and gold output, or (c) both. If (a), rename the method to "weighted supervised fine-tuning" and remove the RL framing. If (b) or (c), provide the exact reward computation, how the quadruple is aggregated into a scalar, and the specific reward values used.
2. **Add the SFT baselines** listed in Major weakness 2 — SFT on D_fine alone, SFT on full D_WeRG without reward, and a weighted SFT. This would allow attribution of gains to the specific WeRG design rather than to fine-tuning in general.
3. **Add aspect-level accuracy metrics** (emotion detection F1, action recall, knowledge entity F1) on a held-out set using the gold ConvINT test annotations to directly measure whether the framework improves *understanding*, not just text generation overlap.
4. **Specify the ESConv response generation backbone** and add a comparison against alternative intention representations (structured slots, free-text summaries) for the downstream task.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>