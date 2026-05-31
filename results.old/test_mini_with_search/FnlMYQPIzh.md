I have all the verification I need. Here is the consolidated final review.

---

## Summary

This paper proposes ConvINT, a semi-structured intention framework that decomposes user utterances in dialogue into four aspects (situation, emotion, action, knowledge), and WeRG, a weakly-supervised reinforced generation method that combines coarse-to-fine annotations (mapped intents, LLM-generated, and human-annotated) with tiered per-aspect rewards to generate ConvINT annotations at scale. Experiments on DuRecDial and ESConv evaluate the generated annotations against prompting baselines and demonstrate improvements in downstream response generation tasks.

## Strengths

- **Four-aspect semi-structured framework (ConvINT).** Section 3.2 formalizes intention understanding along situation, emotion, action, and knowledge dimensions, grounded in cognitive intention theory. This provides a principled middle ground between rigid slot-value ontologies and unstructured free-text. The downstream task experiments (Tables 4, 5) validate that each aspect contributes meaningfully — removing the emotion aspect from ESConv causes the largest performance drop, which aligns with the domain's nature and supports the aspect-level design choices.

- **Downstream task validation is the paper's strongest evidence.** Tables 4 and 5 show that incorporating ConvINT annotations into response generation improves dialogue-level Success Rate on both DuRecDial and ESConv. These experiments establish that the ConvINT framework itself is useful for downstream conversational AI tasks, independent of how one evaluates the generation method.

- **Ablation studies confirm the internal design choices matter.** Table 3 shows that removing any data source ($\mathcal{D}_{\text{coarse}}$, $\mathcal{D}_{\text{mid}}$, $\mathcal{D}_{\text{fine}}$) degrades performance, and removing the reward hierarchy causes a notable drop. These ablations support the claim that the coarse-to-fine weak supervision design and the tiered rewards are both necessary within the WeRG pipeline.

- **Human evaluation with inter-annotator agreement.** Table 2 reports Fleiss' Kappa (0.2–0.6) for three annotators across 50 samples per dataset, providing evidence of reliability for the human-rated quality comparisons.

## Weaknesses

### Major

- **Missing supervised fine-tuning (SFT) baselines for WeRG evaluation.** The paper's core claim is that WeRG generates high-quality ConvINT annotations. Yet the comparison in Table 1 is only against prompting methods (Direct Prompt, CoT Prompt, zero-shot and few-shot). WeRG is a multi-stage fine-tuning method (SFT + RL with weak supervision). The appropriate baselines should include at minimum: (1) SFT on $\mathcal{D}_{\text{fine}}$ alone, and (2) SFT on the full $\mathcal{D}_{\text{WeRG}}$ dataset (same training data) without the RL reward component. Without these, it is impossible to determine whether WeRG's gains come from (a) simply having more training data, (b) the RL objective, or (c) the specific reward design. The ablation study in Table 3 only compares *within-WeRG* variants — it does not situate WeRG against simpler supervised alternatives. As a result, the paper's claim that "WeRG markedly improves LLMs' ability" (abstract) is not supported by the evidence presented. (Section 4.3, Table 1)

- **Ground-truth annotation process for the test set is not documented.** The automatic evaluation metrics (F1, BLEU, BERTScore, BARTScore) in Table 1 depend entirely on "human-annotated ConvINT labels for the test set" (Section 4.2). The paper provides no details about: how many annotators created these ground-truth labels, what instructions or guidelines were used, whether there was a pilot phase, and crucially, what the inter-annotator agreement was for the ground truth itself. The Fleiss' Kappa reported in Table 2 is for the *rating* task (evaluating generated outputs), not for the ground truth creation. If the ground-truth labels are not reliable, all automatic metrics measure alignment with an unstable target. This gap weakens the validity of the automatic evaluation chain. (Section 4.2)

### Minor

- **Reward values for the tiered quadruple reward are unspecified.** Section 3.3 defines $r_{\text{coarse}} < r_{\text{mid}} < r_{\text{fine}}$ but gives no actual numerical values (e.g., $r_{\text{coarse}}=0.1, r_{\text{mid}}=0.5, r_{\text{fine}}=1.0$ or similar). This is essential for reproducibility. The ablation study (Table 3) shows the hierarchy helps, but without the values, another researcher cannot reproduce or fairly compare against the method. (Section 3.3, Eq. 2)

- **Coarse supervision data source is underspecified.** Section 3.3 describes $\mathcal{D}_{\text{coarse}}$ as "hard mapping to transform existing structured interpretations into ConvINT labels." The paper does not disclose what these "existing structured interpretations" are for DuRecDial and ESConv, nor whether the same information was made available to the prompting baselines. If $\mathcal{D}_{\text{coarse}}$ uses dataset-specific labels (e.g., DuRecDial's goals/topics or ESConv's emotion types) that the prompting baselines were not given, this creates an asymmetric comparison. The paper should either clarify that this information was equally available to all methods or control for it. (Section 3.3)

- **No statistical significance reported.** Tables 1, 3, 4, 5 report point estimates without confidence intervals or significance tests. Given the modest number of test examples for some metrics, it is unclear whether the observed differences are reliable.

- **No qualitative examples of ConvINT outputs.** The paper shows no concrete example of what a generated ConvINT label looks like for any method. Including a few examples with analysis (good WeRG output vs. a prompt baseline output) would substantially strengthen the qualitative argument for the framework's value.

- **Missing hyperparameters for RL fine-tuning.** The KL coefficient $\beta$, learning rate, number of RL training steps, and model backbone details are not reported, making the method difficult to reproduce.

### Trivial
- The computational cost of the multi-stage WeRG pipeline vs. prompting baselines is not discussed, which would be helpful for practitioners evaluating the trade-off.

## Nice-to-Haves
- A comparison against a simpler alternative representation (e.g., a complete free-text summary of user intent) in the downstream task experiments would strengthen the claim that ConvINT's semi-structured format specifically helps (as opposed to any additional information).
- The "semantic pointers" concept is mentioned as inspiration (Section 3.2) but never operationalized — this reference could be made more concrete or removed for clarity.

## Removed Points
- **Claim that the quadruple reward is "actually a single scalar per source" (from harsh critic):** The paper states the quadruple "allows for the allocation of distinct reward components to each aspect," implying they could differ per aspect. The critic's assertion that they are all equal is speculative and not verifiable from the paper text. Removed.
- **Claim that baselines comparison is "designed in a way that guarantees WeRG looks favorable":** This overstates the intent. The missing baselines are a real gap, but characterizing it as rigged is unwarranted. The claim about structural unfairness has been softened to a Minor weakness.
- **Semantic pointers being a "throwaway reference":** While accurate, this is a presentation nitpick that does not affect the paper's core claims.
- **Strength Finder's generic praise of "importance of the problem":** Removed as generic — it does not constitute a concrete, evidence-based strength specific to this paper's execution.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the core tension in the paper: the ConvINT framework is well-motivated and the downstream validation is meaningful, but the main evaluation that WeRG generates high-quality annotations is missing critical baselines (SFT-only) and documentation (ground-truth annotation process, reward values). Neither reviewer identified an insight that goes beyond what the paper itself states or that reframes the contribution in a new light.

## Suggestions
1. **Add SFT baselines.** Train the same backbone on (a) $\mathcal{D}_{\text{fine}}$ alone via SFT and (b) the full $\mathcal{D}_{\text{WeRG}}$ via SFT without RL rewards. This is the single most important addition — it isolates whether WeRG's RL objective outperforms simply using the same data with standard supervised training, which is necessary to justify the method's complexity.
2. **Document ground-truth annotation.** Report the number of annotators, annotation guidelines, and inter-annotator agreement (e.g., Fleiss' Kappa) for the test set ground-truth labels, not just for the human evaluation ratings.
3. **Report the reward values.** The specific numerical values of $r_{\text{coarse}}, r_{\text{mid}}, r_{\text{fine}}$ (whether per-aspect or uniform per source) must be disclosed.
4. **Clarify $\mathcal{D}_{\text{coarse}}$ mapping.** State what the "existing structured interpretations" are for each dataset and whether the prompting baselines had access to the same information.
5. **Include significance tests or confidence intervals** for all automatic metrics, especially where gains appear modest.
6. **Add qualitative examples** showing ConvINT outputs from WeRG and from baselines for concrete comparison.

## Score and Decision

### Calibration Anchors

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| cAPyfsUusL.md (CONSINTBENCH) | 3.00 | R1 (low) | Weaker — fundamental evaluation issues, withdrawn |
| tpkBiKShwV.md (Semi-Supervised Disease) | 2.67 | R1 (low) | Weaker — not topically relevant, more fundamental flaws |
| TG8b8LmRsY.md (Bargaining Skills) | 1.50 | R1 (low) | Much weaker — substantially lower quality |
| kjCzhKVzEJ.md (UserRL) | 4.50 | R1 (mid) | Similar — both have missing SFT baseline comparison, both present reasonable frameworks |
| 44xt30V679.md (Intent-FT) | 5.00 | R1 (mid) | Similar — clean contribution but evaluation gaps; ConvINT's framework contribution is more novel |
| ZgCCDwcGwn.md (AgentGym-RL) | 7.00 | R1 (mid) | Stronger — more comprehensive evaluation, stronger empirical results |
| K6T0o875zF.md (Practitioner's Guide) | 4.50 | R1 (mid) | Weaker — limited novelty, more of a survey |
| VKGTGGcwl6.md (LLMs Get Lost) | 8.00 | R1 (high) | Much stronger — rigorous large-scale evaluation, clean experimental design |
| fRCm5c8x0j.md (Intent-Aware LFQA) | 6.00 | R2 | Stronger — 4 unanimous 6s, multi-benchmark eval, similar "missing baseline" gap but less severe |
| afO3vnSNsS.md (ClarifyVC) | 6.00 | R2 | Stronger — clearer evaluation pipeline, more detailed experimental analysis |
| ftLqH4tgrh.md (Dialogue as Discovery) | 5.00 | R2 | Similar — principled contribution with evaluation limitations (simulated only) |
| ROioaZ45Yz.md (CW-PO) | 5.20 | R2 | Slightly stronger — cleaner empirical story |
| Pv5l6cvfno.md (Turing Test S2S) | 5.50 | R2 | Similar — good framework but limited scope |

**Round 1 bracket:** 4–7. The paper clearly exceeds the 0–3 band (those papers have fundamental, often fatal flaws). It does not reach the 8+ band (no paper in that range had evaluation gaps of this magnitude).

**Round 2 narrowing:** The paper sits near the low-to-mid 5s. Its framework contribution is genuine (comparable to Intent-Aware LFQA at 6.00 in clarity of motivation), but the evaluation gaps are larger (Intent-Aware LFQA's missing baseline was CoT prompting; this paper's missing baseline is SFT, which is more central to the method being evaluated). The paper is slightly stronger than UserRL (4.50) because ConvINT's framework is more clearly novel and the downstream task validation is more direct. It is comparable to "Dialogue as Discovery" (5.00) — both have principled contributions undermined by incomplete evaluation. It is weaker than ClarifyVC (6.00) and Intent-Aware LFQA (6.00) because those papers have more complete evaluation despite their own gaps.

**Final score: 5.0** — The paper presents a well-motivated framework (ConvINT) with promising downstream results, but the main evaluation of WeRG is missing critical baselines (SFT-only) and essential documentation (ground-truth annotation process, reward values). These are fixable in revision but the paper in its current form does not fully substantiate its central claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>