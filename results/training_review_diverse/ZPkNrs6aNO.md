Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper proposes CONFST, a method for steering LLM outputs during inference by selecting "confident" activations (those most predictive of a target user's identity according to a logistic regression classifier) and averaging them into a steering vector. The paper also presents a Bayesian theoretical framework, adapted from Xie et al. (2021), intended to characterize when a steering direction is effective. Experiments on topic shift (AgNews, Emotion) and style shift (conciseness, helpfulness, safety) with GPT-2 XL, Mistral-7B, and Gemma-9B show that CONFST outperforms mean steering (its β=0 ablation) and some additional baselines.

## Strengths

- **Multi-preference steering demonstrated empirically**: CONFST is shown to steer output toward one of four topic classes on AgNews (Fig. 4), going beyond the two-direction (bidirectional) setting that dominates prior work. This is a genuine and nontrivial extension of existing model steering capabilities.

- **Systematic ablation of confidence threshold β**: The paper studies multiple β values (Figs. 4–5) and discusses the trade-off between precision and coverage (Remark 4), providing practical insight into when higher confidence hurts because too few activations remain.

- **Composability of steering directions**: The paper demonstrates additive combination of steering vectors (e.g., helpfulness + conciseness in Fig. 7, topic + conciseness in Fig. 8), showing that multiple attributes can be controlled simultaneously with predictable effects.

## Weaknesses

### Fatal
None.

### Major

- **The experimental evaluation does not compare against the methods the paper claims to improve upon.** The paper states advantages over Li et al. (2024b), Rimsky et al. (2023), and Adila et al. (2024a) — claiming CONFST is "more powerful," simpler (no layer/head search), and requires no explicit instructions — yet never empirically compares against any of these methods. Without controlled comparisons, these claimed advantages are unsupported. The baselines that ARE included (Massive Mean Shift, Act Addition, ICL) appear only in topic shift (Figs. 4–5) and are not described (e.g., "Massive Mean Shift" has no definition or citation; the paper simply names it in figure captions). For style shift, the only comparator is "mean steering" (the β=0 version of CONFST itself) or "no steering."

- **The method does not generalize to unseen users, a core limitation that is not discussed.** The logistic regression classifier is trained on activations from a fixed set of N users, and the confidence scores correspond to predicting user identity. A new user with a new preference cannot be handled without retraining. The paper never acknowledges this limitation, nor does it discuss the implicit assumption that user identities are known at training time and that each user maps to a single, separable preference.

- **The theory does not validate the specific algorithmic choices in a way that rules out alternatives.** The Bayesian framework in Section 3 shows that a good steering direction is one where P(θ*|v) is close to 1. The paper then observes that this posterior is proportional to P(v|θ*) and proposes using logistic regression classifier confidence as a proxy. The connection is conceptually plausible but loose: the classifier is trained to discriminate user identities (not preferences), the theoretical quantities (ε, c, δ) are never operationalized or estimated on real data, and the framework provides no formal justification for the specific choice of logistic regression over any other classifier, or for thresholding by confidence over other selection strategies. The theory and method coexist rather than flowing from one to the other.

### Minor

- **The "no need to determine which layer" claim in the abstract is inconsistent with the method's use of a target layer ℓ.** Algorithm 1 takes ℓ as input, and the experiments explicitly set ℓ per model/task (ℓ=1 for Mistral on topic shift, ℓ=0 for Gemma). The conclusion more honestly states "without selecting among all the layers to choose the most separable features," which correctly contrasts with prior methods that iterate over layers/heads. But the abstract's stronger phrasing is misleading, and the paper provides no ablation or analysis showing that results are robust to the choice of ℓ.

- **No variance or uncertainty estimates are reported.** Despite generating 200 outputs per condition for topic shift (and using stochastic LLM decoding throughout), all results are reported as point estimates without confidence intervals, error bars, or significance tests. This makes it impossible to assess whether observed differences (e.g., between CONFST and mean steering in Fig. 10) are reliable.

- **Key hyperparameters (subsequence length s, starting token position t) are not reported in the experiments.** Step 1 of the method requires setting t and s, but no values are given for any experiment. This undermines reproducibility.

- **The theory's Assumption 1 requires that as n → ∞, P(θ*|v) → 1, which is an asymptotic idealization.** Claims 1–2 then derive conditions involving unmeasurable quantities (ε, c, δ, min_y P(y|θ̂;X)). The theory provides qualitative insight (a good steering direction should be highly predictive of the target preference) but is not operationalized or empirically validated; it serves as motivation rather than a verifiable foundation.

### Trivial
- Figure references in the text are occasionally garbled due to parser artifacts (e.g., "Fig. 11" is referenced but not present in the extracted text).
- The notation in Eq. (4) uses both ε and δ without connection to empirically measurable quantities, leaving the reader unable to assess whether the conditions could ever hold on real data.

## Nice-to-Haves

- An ablation showing sensitivity to the layer choice ℓ would help resolve the ambiguity about whether the method truly avoids layer selection.
- A comparison of computational cost (training the logistic regression + forward passes for activation extraction vs. prior methods' layer/head iteration) would contextualize the claimed simplicity advantage.
- Discussion of how the method could be extended to unseen users (e.g., via few-shot adaptation or a different classifier architecture) would strengthen the paper's practical relevance.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"Missing related works (Zou et al., 2023; Arditi et al., 2024)"** — Removed per Hard Rule: missing related works cannot be confirmed without external sources.
2. **"Table 1 cannot be evaluated (probably stripped by parser)"** — Removed per Hard Rule: parser artifacts are not author errors.
3. **Criticisms framed as "the paper should also cover Y / domain Z" when they amount to scope creep** — Removed per instructions about depth vs. breadth.
4. **Strength from Strength Finder: "Formal theoretical framework... addressing a previously unstudied fundamental question"** — While the framework is novel in the context of model steering, it closely follows Xie et al. (2021)'s Bayesian framework. The strength is kept in spirit but downgraded in the review text to match its actual novelty.

## Novel Insights

Beyond the paper's own contributions, the reviews surface the observation that the gap between theory and practice in model steering papers is often structural: theoretical frameworks (here, Bayesian analysis) provide high-level characterizations of what a "good" direction is, but the specific algorithmic choices (classifier type, thresholding scheme, subsequence construction) are guided by engineering intuition rather than derived from theory. This suggests that the field would benefit from work that designs algorithms by directly optimizing theoretically motivated objectives, rather than using theory as post-hoc justification.

## Suggestions

1. **Run controlled comparisons against the specific methods you claim to improve upon** (Li et al. 2024b's truthful steering adapted to topic/style tasks; Adila et al. 2024a). Without these, the core contribution is unsubstantiated relative to the state of the art.
2. **Acknowledge and discuss the fixed-user limitation** — either propose a variant that handles new users, or clearly scope the method to settings where the user set is known at training time.
3. **Report error bars or confidence intervals** for all stochastic experiments (200 generations per condition provides ample data for bootstrap estimates).
4. **Clarify the "no layer selection" claim** — either show robustness across layers with an ablation, or rephrase to accurately reflect that a fixed layer must still be chosen (even if not searched).
5. **Report the values of hyperparameters t (starting token position) and s (subsequence length)** that were used in experiments.

## Score and Decision

**Originality**: Moderate — the confident-direction selection idea is novel, but the theoretical framework is largely adapted from existing work (Xie et al., 2021).

**Importance of research question**: High — efficient, optimization-free LLM steering for multiple preferences is practically important.

**Claims support**: Weak — the paper's central comparative claims (advantages over Li et al., Rimsky et al., Adila et al.) are not supported by experiments.

**Soundness of experiments**: Below the acceptance threshold — missing baselines, no variance estimates, undefined "Massive Mean Shift" baseline, unreported hyperparameters.

**Clarity**: Adequate — the method description is mostly clear, but the framing of the "no layer selection" advantage is inconsistent between abstract and implementation.

**Value to the community**: The core idea (selecting high-confidence activations via a classifier) is interesting and could inspire follow-up work, but the paper as presented lacks the experimental rigor needed to establish its effectiveness relative to existing approaches.

The paper has a reasonable core idea and takes a step toward multi-preference steering, a genuine gap in the literature. However, the experimental evaluation is fundamentally incomplete: it does not compare against the very methods it claims to surpass, key baselines are undefined, and no uncertainty estimates are provided. These are not minor presentation issues — they affect whether the central claims are believable. The paper needs major revisions before it can be accepted.

**MY FINAL SCORE: <pineapple>5.0</pineapple>**
**MY FINAL DECISION: <orange>Reject</orange>**