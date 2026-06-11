Now I have enough data to calibrate. Let me finalize.

**Round 1 Bracket Analysis:**

Retrieved anchors across all queries (listing path, avg score, round):

| Path | Avg Score | Topic Relevance |
|------|-----------|----------------|
| 5kMwiMnUip.md | 1.40 | Weak — jailbreaking, generic |
| 8QTpYC4smR.md | 1.00 | Weak — LLM survey |
| gwZ90hFSL2.md | 1.00 | None — humanoid robots |
| nSDOkm0SKo.md | 1.00 | None — financial NN |
| DXaUC7lBq1.md | 3.00 | Moderate — LLM personality, SAE steering |
| 89wVrywsIy.md | 3.40 | Moderate — SAE circuit tracing |
| tcsZt9ZNKD.md | 1.75 (actual 8.20) | High — SAE scaling (miscategorized) |
| Wxl0JMgDoU.md | 2.50 | Moderate — SAE skill adaptation |
| vc1i3a4O99.md | 5.00 | High — SAE steering LLM behavior |
| sknUS8X9q0.md | 4.00 | High — SAE evaluation framework |
| ZtvRqm6oBu.md | 5.25 | High — SAE unlearning application |
| F76bwRSLeK.md | 4.80 | High — SAE interpretability (seminal) |
| MDvecs7EvO.md | 6.50 | High — SAE feature matching |
| 9ca9eHNrdH.md | 7.00 | High — SAE limitations |
| 1Njl73JKjB.md | 7.00 | High — SAE evaluation |
| XAjfjizaKs.md | 6.50 | High — multi-layer SAE |
| I4e82CIDxv.md | 8.00 | Moderate — sparse feature circuits |
| EytBpUGB1Z.md | 8.00 | Low — retrieval heads |
| 5Ca9sSzuDp.md | 8.00 | Low — CLIP interpretation |
| z8sxoCYgmd.md | 8.00 | Low — synthetic detection |
| YRXDl6I3j5.md | 3.67 | Very high — deception scaling in LMs |
| q9g13IoWmk.md | 4.75 | High — honest AI, deception reduction |
| HxKSzulSD1.md | 6.50 | High — weak-to-strong deception |
| o6eUNPBAEc.md | 5.00 | Moderate — LM self-explanation |
| q9g13IoWmk.md | 4.75 | High — deception reduction |
| wwO8qS9tQl.md | 3.00 | Moderate — LM explainability |
| Eyv12jjyMN.md | 4.00 | Moderate — attack for interpretability |
| VvAiCXwPvD.md | 5.67 | Moderate — counterfactual explanations |
| Wd1R0oxe5j.md | 3.50 | Moderate — LLMs for XAI |

**Initial bracket: 3.5–5.0**

Key comparisons:
- vs. "Tall Tales at Different Scales" (3.67, rejected): Similar topic (deception in LMs), similar conceptual weaknesses (is role-playing really deception?), similar lack of quantitative rigor. The paper under review has broader scope but weaker execution per component.
- vs. "Towards Safe and Honest AI Agents" (4.75, rejected): Similar AI safety ambition, similar gap between ambition and execution. The paper under review has the SAE angle which adds novelty.
- vs. "Applying SAEs to Unlearn" (5.25, rejected): Similar SAE application to safety task, similar methodological rigor level, but that paper had more quantitative metrics.
- vs. "Interpreting and Steering with SAEs" (5.00, rejected): Very similar methodological approach (SAE feature steering), but that paper had better quantitative evaluation.
- vs. "Super(ficial)-alignment" (6.50, accepted): Same deception theme but significantly more rigorous methodology with quantitative metrics, controlled experiments, and clear definitions.

The paper under review sits between the 3.5 "Tall Tales" anchor (similar conceptual issues, similar lack of rigor) and the 5.0-5.25 SAE application papers (which have better quantitative evaluation). The genuine novelty of the deception+SAE intersection and the differential steering finding push it above 3.5, but the methodological shortcomings (no quantitative t-SNE metrics, confounded comparison, informal steering reporting, inflated claims) keep it below the 5.0 rejected SAE papers.

**Final score: 4.0**

The paper identifies an important research direction and presents some genuinely novel preliminary findings, but the execution falls significantly short of the quantitative rigor expected for a conference paper: the headline claim is inflated relative to evidence, the central comparison is confounded, the most distinctive contribution (feature steering) is reported qualitatively, and the insider trading analysis relies on unvalidated visualizations. The honest limitations section partially redeems these issues but the conclusions don't adequately scale to match the evidence.

## Summary
This paper investigates whether auto-labeled SAE features can detect or control strategic deception in LLMs, using two testbeds: a "Secret Agenda" social deduction game across 38 models and an Insider Trading compliance scenario analyzed with dual SAE implementations. The authors find that auto-labeled deception features are dormant during strategic lying and fail to control it via steering, while unlabeled aggregate activations discriminate compliance from engagement in the insider trading domain — suggesting current auto-labeling rather than SAE architectures is the bottleneck.

## Strengths
- **Differential feature steering result**: Steering topical features (e.g., "Bananas") successfully suppressed their mention, while 100+ deception-related features could not prevent strategic lying (Section 6.3), demonstrating the failure is specific to deception features rather than a general steering inability.
- **Specific, named evidence of dormant features**: Section 6.1 identifies concrete GemmaScope features by ID (14971: "deception and betrayal", 1741: "falsehoods in political speech", 6442, 10248) documenting their dormancy during actual deception, making the negative finding directly verifiable.
- **Breadth of model coverage**: 38 models across 7 families (Anthropic, Google, Grok, Meta, OpenAI, Perplexity, Qwen) with multiple prompt variants to control for political bias (Section 5.3).
- **Thorough limitations disclosure**: Section 8 explicitly acknowledges sample size constraints, asymmetric analysis depth, and appropriately scopes findings to auto-labeled features rather than SAE architectures generally (Section 8.4).
- **Cross-architecture consistency**: Both 8B and 70B SAE implementations showed directionally consistent separation patterns in t-SNE for the insider trading domain (Figure 4).

## Weaknesses

### Fatal
None.

### Major
- **Inflated claims relative to evidence**: The headline "38/38 models lied at least once" uses an existence criterion with n=2–30 per model (acknowledged in Section 8.1), yet the abstract and conclusions use "systematic," "reliably," and "universal elicitability." With n=2 for some models, one lie in two trials is an existence proof at best. The conclusions (Section 10) read as if limitations are minor qualifications rather than central constraints.

- **Central narrative confounded by methodological differences**: The core story — auto-labeled features fail in Secret Agenda but unlabeled activations succeed in Insider Trading — is confounded because the analyses differ in nearly every dimension: individual feature activation checking vs. PCA + t-SNE on aggregate activations; qualitative manual analysis (~160 examples) vs. visual t-SNE on 149 generated examples; no quantitative metrics in either case but different kinds of no metrics. The paper acknowledges asymmetry in Section 8.3 but treats the contrast as domain-dependent when it equally supports method-dependent effectiveness.

- **SAE feature steering experiments lack systematic reporting**: Section 6.3 claims "100+ deception-related features" were tested but provides no table of features tested, no trial counts per feature, no control conditions, and no success/failure rates. Evidence points to a Google Drive folder of screenshots (DeLeeuw, 2024). For the paper's most distinctive contribution, this qualitative reporting is inadequate.

- **Insider Trading t-SNE analysis is purely visual**: Section 7.2 presents t-SNE plots showing "clear separation" but reports no quantitative clustering metrics (silhouette scores, classification accuracy), no comparison to random baselines, and no statistical significance tests. t-SNE is known to produce spurious separation depending on perplexity settings; "clear separation" in 2D projections does not establish meaningful discrimination in the original high-dimensional space.

### Minor
- **Role-playing vs. genuine deception unaddressed**: In Secret Agenda (Section 5.1), the LLM is given a synthetic transcript placing it in the "Fascist Leader" role. Lying could reflect strategic deception or coherent role-playing within the game scenario. The paper never addresses this distinction; testing without game framing would help disambiguate.
- **Quantized model activations through non-quantized SAEs**: Insider Trading responses use Unsloth's 4-bit quantized Llama 70B (Section 7.1), but SAEs were trained on standard Llama 3.3 70B. The paper doesn't discuss or validate this distribution mismatch.
- **No quantitative results for prompt variation tests**: Section 5.3 mentions testing Snails vs Slugs, Truthers vs Liars, Day vs Night, and Pink vs Turquoise variants, reporting "continued deception" but providing no actual counts or rates.

### Trivial
None.

## Nice-to-Haves
- Running the same aggregate PCA + t-SNE analysis on Secret Agenda responses would make the domain comparison methodologically consistent.
- Adding silhouette scores or classifier accuracy to the insider trading analysis would strengthen the visual evidence.
- Testing deception without game framing would help address the role-playing ambiguity.

## Removed Points
These points are flagged to be removed, treat them with caution:
- No points were removed as all identified weaknesses were verified against the paper text.

## Novel Insights
The most genuinely novel finding is the differential steering result: topical SAE features (e.g., "bananas") can be successfully steered to suppress their concepts, but over 100 auto-labeled deception features cannot prevent strategic lying, suggesting that the failure is specific to how deception is represented or labeled in current SAE decompositions rather than a general limitation of the steering methodology. Combined with the positive insider trading result showing aggregate unlabeled activations carry discriminative signal, this points to auto-labeling — not SAE architectures — as the bottleneck for deception detection.

## Suggestions
- Quantify the feature steering results with a systematic table listing all features, steering values, trial counts, and outcomes, using the banana-feature as a formal positive control.
- Add quantitative clustering metrics (silhouette score, classifier accuracy) to the insider trading analysis and compare to a random-feature baseline.
- Run aggregate unlabeled analysis (PCA + t-SNE) on Secret Agenda responses for methodologically consistent domain comparison.
- Address the quantization-SAE mismatch by validating SAE reconstruction quality on quantized-model activations or re-running with non-quantized generation.

---

**Reporting — All anchors and comparison:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 5kMwiMnUip.md | 1.40 | R1 | Generic jailbreaking survey — much weaker than this paper |
| 8QTpYC4smR.md | 1.00 | R1 | Generic LLM survey — much weaker |
| gwZ90hFSL2.md | 1.00 | R1 | Off-topic humanoid robots — irrelevant |
| nSDOkm0SKo.md | 1.00 | R1 | Off-topic financial NN — irrelevant |
| DXaUC7lBq1.md | 3.00 | R1 | LLM personality via SAE steering — similar methodology, rejected |
| 89wVrywsIy.md | 3.40 | R1 | SAE circuit tracing — methodologically related, rejected |
| tcsZt9ZNKD.md | 1.75 | R1 | SAE scaling (miscategorized score filter) — actually score 8.20, seminal work |
| Wxl0JMgDoU.md | 2.50 | R1 | SAE skill adaptation in chess — moderate quality, rejected |
| vc1i3a4O99.md | 5.00 | R1 | SAE steering LLM behavior — better quantitative eval, rejected |
| sknUS8X9q0.md | 4.00 | R1 | SAE evaluation framework — related, rejected |
| ZtvRqm6oBu.md | 5.25 | R1 | SAE unlearning — similar application depth, rejected |
| F76bwRSLeK.md | 4.80 | R1 | SAE interpretable features — seminal, accepted with mixed scores |
| MDvecs7EvO.md | 6.50 | R1 | SAE feature matching — accepted, stronger methodology |
| 9ca9eHNrdH.md | 7.00 | R1 | SAE canonical units critique — accepted, stronger rigor |
| 1Njl73JKjB.md | 7.00 | R1 | Principled SAE evaluation — accepted, much stronger |
| XAjfjizaKs.md | 6.50 | R1 | Multi-layer SAE — accepted, cleaner methodology |
| I4e82CIDxv.md | 8.00 | R1 | Sparse feature circuits — top-tier accepted |
| EytBpUGB1Z.md | 8.00 | R1 | Retrieval heads — top-tier, different topic |
| 5Ca9sSzuDp.md | 8.00 | R1 | CLIP interpretation — top-tier, different topic |
| z8sxoCYgmd.md | 8.00 | R1 | LOKI benchmark — top-tier, different topic |
| YRXDl6I3j5.md | 3.67 | R1 | Deception scaling in LMs — very similar topic, rejected for similar issues |
| q9g13IoWmk.md | 4.75 | R1 | Honest AI via SOO — similar ambition/execution gap, rejected |
| HxKSzulSD1.md | 6.50 | R1 | Weak-to-strong deception — similar theme, accepted with stronger rigor |
| o6eUNPBAEc.md | 5.00 | R1 | LM self-explanation — moderately related, rejected |
| wwO8qS9tQl.md | 3.00 | R1 | LM explainability benchmark — moderately related, rejected |
| Eyv12jjyMN.md | 4.00 | R1 | Attack for interpretability — moderately related, rejected |
| VvAiCXwPvD.md | 5.67 | R1 | Counterfactual explanations — moderately related, rejected |
| Wd1R0oxe5j.md | 3.50 | R1 | LLMs for XAI — moderately related, rejected |

**Round 1 bracket: 3.5–5.0**

The paper sits between "Tall Tales" (3.67, rejected, similar deception-in-LMs topic with similar conceptual weaknesses) and "SAE Unlearning" / "SAE Steering" (5.00–5.25, rejected, similar SAE application but with better quantitative evaluation). The genuine novelty of the deception+SAE intersection and differential steering result push it above 3.5, but the methodological shortcomings (no quantitative t-SNE metrics, confounded comparison, informal steering reporting) keep it below the 5.0 rejected SAE application papers. Final score: **4.0**.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>