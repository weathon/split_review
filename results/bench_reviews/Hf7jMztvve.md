Below is my consolidated meta-review.

---

## Summary

This paper investigates strategic deception in LLMs through two complementary testbeds: (1) **Secret Agenda**, a modified social-deduction game that elicits lying across 38 models, and (2) **Insider Trading**, a compliance scenario analyzed via Sparse Autoencoder (SAE) architectures. The authors report that auto-labeled SAE features for deception rarely activate during Secret Agenda lies and that steering over 100 deception-related features failed to prevent strategic lying; in contrast, unlabeled aggregate SAE activations in the Insider Trading scenario produce separable t-SNE clusters between engagement and refusal responses. The paper is a preliminary exploration that raises important questions about the reliability of auto-labeled SAE features for detecting and controlling strategic deception, but the experimental evidence is too preliminary and insufficiently rigorous to support its core claims.

---

## Strengths

1. **Clever, controlled testbed design (Secret Agenda).** The synthetic-transcript approach isolates a clean binary deception decision with clear incentive structures, enabling reproducible testing of whether models lie when lying is the optimal strategy. This is a genuinely useful methodological contribution for the community.

2. **Broad behavioral coverage across model families.** Demonstrating that all 38 tested models (across Anthropic, Google, Meta, OpenAI, Qwen, Perplexity, Grok) chose deception at least once establishes an existence proof that strategic dishonesty is widely elicitible under the right incentive structures.

3. **Transparent and thorough limitations section.** Section 8 candidly acknowledges small sample sizes, asymmetric analysis depth, resource constraints, and the provisional nature of the findings. This honesty is rare and valuable.

4. **The negative steering result is genuinely interesting, even if preliminary.** The claim that steering 100+ auto-labeled deception features to extreme values failed to prevent any instance of lying, if verified with proper quantitative controls, would be an important negative result for the mechanistic interpretability community.

---

## Weaknesses

### Fatal
None.

### Major

1. **Failed feature steering is reported anecdotally, not quantitatively.** Section 6.3 describes the steering experiments in a single paragraph with no quantitative data: no deception rates before vs. after steering, no breakdown of which features were tested, no validation that steering actually changed the target feature activations, no variation of steering strength, and no trial counts. The paper states "None of the features … when steered down all the way, resulted in non-lies" without specifying how many trials were run, what "all the way" means numerically, or whether the model's outputs were affected in other ways (coherence, content). In a scientific paper, this is an unreviewable claim. Compare to the "Bananas" control (Section 6.3), which successfully prevented banana mentions — this asymmetry suggests the steering mechanism *works*, making the deception-feature failure more interesting, but the lack of experimental documentation prevents any firm conclusion.

2. **The Insider Trading analysis lacks any quantitative discriminative metric.** The paper presents t-SNE plots (Figure 4) and heatmaps (Figure 5) showing qualitative separation between engagement and refusal clusters, but reports no classification accuracy, AUC, precision/recall, or F1 score for distinguishing response types using SAE features. No baseline comparison is provided (e.g., logistic regression on hidden states, bag-of-words). Without any quantitative metric, the positive claim that "unlabeled aggregate activations provide discriminative signal for risk assessment" (Contribution 4) remains speculative. Furthermore, the top discriminative features listed in Table 1 ("Quantity fields in structured data," "Trade execution code patterns") are surface-level content features that likely reflect response *format* (trades contain numbers/code; refusals do not) rather than the compliance *decision* itself — an acknowledged confound the paper does not address.

3. **The cross-testbed comparison (Contribution 2) is confounded on too many dimensions to support the claimed conclusion.** The paper contrasts "failure of auto-labeled features in Secret Agenda" with "success of unlabeled activations in Insider Trading" and attributes this to "domain-dependent interpretability effectiveness." However, the two testbeds differ on model (Gemma 2 8B vs. Llama 8B/70B), SAE implementation (GemmaScope vs. Goodfire), labeling scheme (auto-labeled vs. unlabeled), analysis method (manual feature checking + steering vs. t-SNE + discriminative ranking), task type, classification scheme, and sample size. Because these variables are not controlled, the contrast cannot be attributed to "domain" or "context." The paper acknowledges this asymmetry in Limitations (Section 8.3) but nonetheless draws the cross-domain conclusion (Section 7.3). This is an invalid inference.

4. **The insider-trading response labeling is heuristic-based and not validated.** The paper classifies responses as Engagement/Helpful/Refusal using unspecified heuristics (presumably regex matching) but provides no inter-annotator agreement, no human validation, and no description of the exact rules. Additionally, the use of a 4-bit quantized Llama 70B (Section 7.1) for SAE analysis is a potential concern not discussed: SAEs are typically trained on full-precision activations, and quantization may distort the activation space.

### Minor

1. **Steering strength is not validated.** Even for the successful "Bananas" control, the paper does not show that steering actually changed target feature activations (e.g., by measuring activations before/after intervention). For the deception features that "failed," this makes it impossible to distinguish between "the feature is not causally involved" and "the steering was too weak."

2. **Secret Agenda behavioral results lack statistical rigor.** The paper's own Figure 1 note states: "Sample sizes vary (n=2–30) making statistical inference limited. Error bars omitted due to insufficient trials for meaningful confidence intervals." While the existence proof (38/38 models lied at least once) is robust even with small n, the paper uses language like "reliably induced lying" (Abstract) that implies more statistical signal than the data support. No inter-annotator agreement is reported for the human/LLM judgment used to classify responses as truth/partial/lie.

3. **Several prompt variants are mentioned but no results are reported.** The paper mentions "Day vs Night," "Pink vs Turquoise," and "Shortened" variants (Section 5.3) but provides no results, making these references unverifiable.

4. **No robustness checks for t-SNE.** t-SNE is sensitive to hyperparameters (perplexity, learning rate, random seed). The paper specifies settings but does not report whether the cluster separation is robust across different settings or random seeds. Silhouette scores or permutation tests would strengthen the claim.

5. **The "expected deception features" selection criteria are unclear.** Section 6.1 states that "most expected deception-related features did not activate" but does not specify how these features were selected from GemmaScope's library. If they were chosen by keyword search on auto-labels, the failure is partly predictable — keyword-based labels are known to be noisy.

### Trivial
- The paper's title and framing use strong language ("strategically lie," "scheming") that implies agency, which is at odds with the paper's own framing of the behavior as incentive-driven (Section 4). This rhetorical inconsistency could confuse readers.
- Several references are not clearly integrated into the text flow (e.g., the "How Israel Used AI" citation).
- The "Reproducibility Statement" (Section 9) references a Google Drive folder for feature-steering screenshots rather than providing the actual data and code.

---

## Nice-to-Haves
- Applying the same SAE methodology (Goodfire) to both testbeds to enable a clean comparison.
- Using probe-based methods (e.g., logistic regression on SAE features) to predict deception in Secret Agenda, rather than relying only on auto-labeled features.
- Reporting classification accuracy for distinguishing engagement/refusal in Insider Trading using the top discriminative SAE features, compared against a simple baseline (e.g., bag-of-words or logistic regression on last-layer hidden states).
- Validating the steering intervention by measuring target activation values before and after steering.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that reference padding exists because some references "appear irrelevant."** The paper's full reference list includes citations that may have been used in appendix sections stripped by the parser. This is not a substantive scientific criticism.
- **Complaint about news-article citation (Economic Times) and author name formatting.** Formatting and source-type nitpicks; irrelevant to scientific evaluation.
- **Complaint about auto-labeling failure being "not a demonstrated finding."** The paper appropriately scopes its claim to "current auto-labeled features" in the Limitations section (8.4) and presents the finding as preliminary evidence, not a definitive proof. The reviewer's stronger interpretation of this claim is not what the paper asserts.

---

## Novel Insights

A genuinely interesting observation emerges from the contrast between the two testbeds, even if the confounds prevent a clean conclusion: **auto-labeled deception features are strikingly absent during Secret Agenda's strategic lying, yet the same label source successfully identifies topical features (e.g., "bananas").** This asymmetry — where superficial topical concepts are captured but strategic behavioral concepts are not — suggests a systematic gap in how current auto-labeling pipelines map behavioral-level concepts to SAE features. If this gap is real (rather than an artifact of feature selection), it implies that auto-labeling methods relying on LLM-generated feature descriptions from corpus co-occurrence may systematically miss incentive-driven, context-dependent behaviors. The community's focus on improving label quality (rather than simply scaling SAE size) may need to prioritize *behavioral* grounding of label concepts.

---

## Suggestions

1. **Provide quantitative steering data.** Report deception rates before and after steering for each feature tested, at multiple steering strengths, with trial counts. Validate that steering changed the actual activations.
2. **Add quantitative discriminative metrics for Insider Trading.** Report classification accuracy/AUC using top SAE features, with a baseline comparison (e.g., logistic regression on hidden states).
3. **Temper the cross-testbed comparison claims.** Either present the two testbeds as independent case studies without claiming domain-dependent effectiveness, or run a controlled comparison using the same model and SAE on both tasks.
4. **Add statistical validation for t-SNE.** Provide silhouette scores, permutation tests, and hyperparameter robustness checks.
5. **Validate the response-type classification** with inter-annotator agreement or a held-out human-judged set.

---

## Score and Decision

### Calibration Anchors

| Path | Avg Human Score | Comparison to this paper |
|---|---|---|
| `/home/wg25r/review_agent/human_reviews_2026/PDBBYwd1LY.md` (Beyond Prompt-Induced Lies) | 6.67 | Stronger: well-designed experiments with quantitative metrics, solid methodology. This paper is notably weaker. |
| `/home/wg25r/review_agent/human_reviews_2026/IbDr8xgUMW.md` (Strategic Dishonesty Can Undermine AI Safety) | 5.50 | Stronger: extensive 80+ model evaluation, quantitative probe validation. This paper is less rigorous. |
| `/home/wg25r/review_agent/human_reviews_2026/x8WlNCQL4s.md` (Deception in LLMs: Audit Game–Theoretic Analysis) | 4.00 | Comparable: both have interesting frameworks undermined by weak experimental validation. This paper is roughly similar in quality. |
| `/home/wg25r/review_agent/human_reviews_2026/Y6PLaCHqoc.md` (Deceive, Detect, Disclose: Mini-Mafia) | 3.00 | This paper has a broader model-coverage and more honest limitations, placing it somewhat above Mini-Mafia. |
| `/home/wg25r/review_agent/human_reviews_2026/VKGTGGcwl6.md` (LLMs Get Lost In Multi-Turn Conversation) | 8.00 | Much stronger: large-scale, well-controlled experiments, clear results. This paper is far below this standard. |
| `/home/wg25r/review_agent/human_reviews_2026/xpvQ8vUtwW.md` (Why Language Models Lie) | 2.00 | Weakest anchor; the current paper has a better testbed design and more honest limitations. |
| `/home/wg25r/review_agent/human_reviews_2026/qtUw7Wwu0t.md` (The EEG activation maps...) | 1.50 | Not comparable (different domain); included to anchor the low end of the scale. |

**Score rationale:** The paper has a genuinely interesting testbed and raises important questions, but the SAE analysis is critically underdocumented (steering experiments lack quantitative data) and the core comparative claim is unsupported due to confounded experimental design. The Insider Trading analysis provides only qualitative visualization without any quantitative validation. These weaknesses are substantial enough that the paper cannot be accepted in its current form. However, the transparency about limitations, the clever testbed design, and the breadth of behavioral testing place it above the weakest rejected papers. Positioned relative to the anchors, the paper sits around 4.0.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>