Now I have a thorough understanding of the paper and both reviews. Let me construct the final consolidated review.

---

## Summary

This paper empirically investigates the relationship between pretraining data frequency and the quality of Linear Relational Embeddings (LREs) — a specific type of linear representation — for factual recall relations in language models. The authors find a strong correlation (r=.82) between subject-object co-occurrence frequency and LRE causality scores across OLMo 1B/7B and GPT-J, identify frequency thresholds (~1-2k co-occurrences for 7B/6B models) above which LREs consistently form, and demonstrate that LRE metrics can predict object-level pretraining frequencies with ~70% within-magnitude accuracy across different models and datasets. The paper also releases a batch-level co-occurrence counting tool.

## Strengths

1. **Strong, well-measured correlation between pretraining frequency and LRE quality**: The paper establishes a Pearson correlation of r=.82 between average subject-object co-occurrence counts and LRE causality scores across relations in multiple models (Section 4.2, Figure 2). This directly quantifies a link that prior work (Hernandez et al., 2024; Chanin et al., 2024) had observed as unexplained variation. The correlation is notably higher than individual subject (r=.66) or object (r=.59) frequencies, showing the relationship is specific to co-occurrence.

2. **Identification of approximate frequency thresholds for LRE formation**: The paper finds that OLMo 7B and GPT-J consistently form high-quality LREs (causality > 0.9) when subject-object co-occurrence reaches approximately 1-2k occurrences, with OLMo 1B requiring ~4.4k (Section 4.2). This threshold finding is actionable for practitioners deciding whether to expect linear structure for a given relation in a given model scale.

3. **Cross-model generalization of frequency prediction from LRE features**: A regression model trained on OLMo 7B's LRE metrics predicts object frequencies in GPT-J's dataset (The Pile) with ~70% within-magnitude accuracy, without any supervision on GPT-J's data (Section 5.3, Table 1). This demonstrates transferable signal between models trained on different corpora, and strongly outperforms baselines using log-probabilities alone.

4. **Novel finding that LREs form early when frequency is sufficient**: The paper shows that even at early training steps (41B tokens), relations with sufficient co-occurrence frequency already exhibit robust LREs, while low-frequency relations never develop them even at the final checkpoint (Section 4, Figure 2). This decouples LRE emergence from overall model capability and ties it specifically to data exposure.

5. **Practical tool contribution**: The batch-level co-occurrence counting tool (Cython-based, Section 3.2) enables per-step frequency analysis not possible with corpus-level tools like WIMBD, and the authors release it to support future work.

## Weaknesses

### Major

None that undermine the core claims. The paper's central finding — a strong correlation between pretraining co-occurrence frequency and LRE quality — is well-supported by the evidence presented.

### Minor

1. **Title/abstract framing overclaims relative to the actual method**: The title promises a study of "linear representations" broadly, and the abstract uses this language throughout without always qualifying that the work specifically studies Linear Relational Embeddings (LREs). The paper does correctly state in Section 2.1 ("We focus on a particular class of linear representations called Linear Relational Embeddings (LREs)") and in the conclusion ("LREs (a particular class of linear representation)"), but the high-level framing could lead readers to infer the results generalize to all forms of linear structure in LMs (e.g., linear probing directions, activation steering, sparse autoencoder features). The paper does not test non-LRE measures of linearity, so the title's generality is unsupported. The claims should be scoped to LREs throughout, or a brief experiment with a complementary method should be added.

2. **The practical data-inference framing overstates what the method achieves**: The abstract and introduction frame the regression as providing "a new unsupervised method for exploring possible data sources of closed-source models." However, the paper's own results (Section 5.2, Figure 3) show that subject-object co-occurrence prediction — the quantity most directly tied to the paper's own central variable — is only marginally above the mean baseline ("within one standard deviation"). Object frequency prediction works well (~70% within-magnitude accuracy), but this is a weaker and less surprising result (models simply know more about frequent entities). The paper does transparently acknowledge this limitation in Sections 5.2 and 8, but the abstract and introduction do not reflect this nuance. The data-inference claims should be qualified to reflect that the method works primarily for object-level frequencies, not relation-level co-occurrence frequencies.

3. **Modified LRE procedure is claimed to "work as well" without supporting evidence**: The paper modifies Hernandez et al.'s LRE fitting by (a) using one β per relation instead of one per model, and (b) including incorrect-prediction examples in the Jacobian approximation (Section 3.1, line 73). The paper states "using examples that models predict incorrectly to fit Equation 1 works as well as using only correct examples" but provides no comparison against the original method. Since the modified procedure is used for all results, a brief validation (e.g., correlation between original and modified causality scores on the final checkpoint) would increase trust.

4. **Generalizability to other models and relation types is limited**: The paper studies 3 models (two from the OLMo family, one from GPT-J), 25 factual relations, and one linear representation method (LREs). The paper acknowledges this (Section 4.2: "Although we cannot draw conclusions from only three models"), but the threshold claims (~1-2k for 7B/6B, ~4.4k for 1B) are derived from only three data points. The paper does not test whether the frequency-LRE relationship holds within relation subtypes (e.g., controlling for whether the relation is animate-animate vs. location-based), which would help rule out confounds from relation semantics. Adding even one more model family (e.g., Llama or Pythia) and a confound analysis controlling for relation type would substantially strengthen the claims.

5. **Causal language in framing vs. correlational evidence**: The paper asks "what factors cause these representations to form (or not)?" (abstract) and uses "formation" language throughout. While the Limitations section (Section 8) correctly acknowledges "we cannot draw causal claims," the overall framing implies a causal relationship without controlling for plausible confounds (e.g., semantic regularity of the relation, diversity of contexts). A controlled dataset manipulation experiment would be needed for causal claims; absent that, the framing should consistently use correlational language.

6. **No validation of counting tool accuracy**: The batch-level counting tool (Section 3.2) is a practical contribution, but the paper does not describe its accuracy or compare it to alternatives like WIMBD. The paper does not discuss how many spurious co-occurrences are counted (e.g., two unrelated entities appearing in the same sequence without relational context). This matters because co-occurrence counts are the paper's primary independent variable.

### Trivial

- Figure 2 plots causality vs. co-occurrence frequency but does not show confidence intervals or uncertainty around the identified thresholds. The scatterplot shows many points below 0.9 causality even above the stated threshold, suggesting the relationship is graded rather than a hard cutoff. The paper would benefit from quantifying this variance (e.g., a logistic regression fit).

## Nice-to-Haves

- Testing a non-LRE linear representation method (e.g., linear probing or activation steering) on the same relations to see if the frequency relationship holds, which would broaden the paper's contribution beyond LREs.
- Analyzing what the learned W matrix encodes (e.g., verifying that it maps subjects to objects via the relational semantics) to validate that high causality genuinely reflects linear structure rather than memorization of a direction in activation space.
- Exploring why subject-object co-occurrence prediction fails — whether the signal is genuinely absent or the ground-truth counts are noisy — to inform future work on dataset inference.
- Adding uncertainty quantification around the frequency thresholds (e.g., a logistic regression relating frequency to probability of high causality).

## Removed Points

The following points from the reviews are removed or downgraded with justification:

- **"The paper should test non-LRE methods to speak about linear representations"** (Harsh Critic, Missing section, second point): The paper explicitly scopes to LREs in Section 2.1. Demanding coverage of all linear representation methods asks for a fundamentally different, broader paper. Moved to Nice-to-Haves.
- **"The paper should analyze what the LRE actually captures"** (Harsh Critic, Missing section, third point): This is partially out of scope — the paper's goal is connecting frequency to LRE existence, not mechanistic interpretation of the W matrix. Moved to Nice-to-Haves.
- **"Demand for more models as a major weakness"**: While adding models would strengthen the paper, the three-model design is standard for this type of empirical study and the paper acknowledges the limitation. Kept as Minor (point 4) rather than Major.
- **"Figure 3 caption says LRE features outperform LM features by 30%"** — The harsh critic's claim that the paper is "misleading" about this is incorrect. The paper's Figure 3 caption accurately states: "Using LRE features outperforms LM only features by about 30%." This refers to object frequency prediction where LRE achieves ~70% vs. LM-only ~40%, which is indeed a ~30% absolute improvement. The paper also transparently shows the co-occurrence prediction result.
- **Strength Finder's claim that the paper "provides a new unsupervised method for exploring possible data sources of closed-source models"** without noting the co-occurrence limitation: This strength is retained but the weakness (point 2 above) notes the caveat.
- **"The paper should add a fourth model"** as a fatal/major weakness: This is overblown for an initial empirical study. Kept as part of Minor point 4 with softened framing.

## Novel Insights

The most interesting observation not fully emphasized by either review is the decoupling of LRE emergence from model capability: the paper shows that LREs for high-frequency relations appear as early as 41B tokens into training and remain stable, while low-frequency relations never develop LREs even at the final 2T-token checkpoint. This suggests that linear structure for factual recall is primarily a function of data statistics rather than training progression or model maturity — a finding that resonates with the theoretical results of Jiang et al. (2024) on implicit bias toward linearity under frequency conditions, but now demonstrated empirically in realistic-scale models. The fact that this pattern holds across model scales (1B vs 7B) but with different thresholds also suggests a testable hypothesis about capacity-frequency interactions that future work could explore.

## Suggestions

1. **Scope the title/abstract claims to LREs explicitly.** Replace "linear representations" with "Linear Relational Embeddings (LREs)" or at minimum add a qualifying phrase ("a class of linear representation called LREs") in the title and abstract.
2. **Validate the modified LRE fitting procedure** against the original Hernandez et al. method on the final checkpoint of one model. Report the correlation between original and modified causality scores.
3. **Add a confound analysis for relation type.** Test whether the frequency–causality correlation holds when controlling for relation category (location relations vs. person-attribute relations vs. organization relations).
4. **Qualify the data-inference claims** in the abstract and introduction to reflect that the method works much better for object-level frequency prediction than for subject-object co-occurrence prediction.
5. **Quantify the uncertainty around frequency thresholds** — e.g., fit a logistic regression relating log-frequency to probability of high causality (causality > 0.9) and report the confidence interval on the threshold.

## Score and Decision

The paper presents a clean, well-executed empirical study connecting pretraining co-occurrence frequency to LRE quality in language models. Its core finding (r=.82 correlation, frequency thresholds) is novel, well-supported, and replicable with the released code. The secondary contribution (frequency prediction from LREs) is weaker for the co-occurrence case but the paper is transparent about this. The main weaknesses are framing overclaims that can be corrected with textual revisions, and some missing validations that would strengthen but not invalidate the results. The paper represents solid empirical interpretability work that adds meaningful understanding of when and why linear structure emerges in LMs.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>