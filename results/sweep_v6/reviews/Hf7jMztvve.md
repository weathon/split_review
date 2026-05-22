Now I have a thorough understanding of the paper. Let me write the final review.

## Summary
This paper investigates strategic deception in LLMs using two testbeds: Secret Agenda (a social-deduction game applied across 38 models) and Insider Trading compliance analysis (via Sparse Autoencoder features). The paper claims that auto-labeled SAE features for deception rarely activate during strategic lying and cannot control it through steering, while unlabeled aggregate activations show discriminative structure for compliance detection. The core contributions are the Secret Agenda testbed itself and negative evidence about current auto-labeling approaches.

## Strengths

1. **Broad behavioral deception elicitation across 38 model families.** The Secret Agenda testbed produced lying behavior in every model tested (Gemma/Gemini, Claude, Llama, OpenAI, Qwen, DeepSeek, Grok, Perplexity). This breadth demonstrates that incentive-driven deception is reliably elicitable across the current LLM ecosystem. The "at least once" framing is appropriately conservative given the small per-model sample sizes (n=2–30).

2. **Prompt variant series controlling for superficial confounds.** Section 5.3 describes five distinct variants (nature-themed "Snails vs Slugs," meta-commentary "Truthers vs Liars," color-coded "Day vs Night" and "Pink vs Turquoise," and an abridged version). All continued to elicit deception, strengthening the argument that the behavior is driven by incentive structure rather than political framing or semantic cues.

3. **Honest and detailed limitations section.** Section 8 explicitly acknowledges the resource constraints, small sample sizes, asymmetric analysis depth, and the preliminary nature of the findings. The paper states it "shows the capability exists, not its precise rate" and limits its negative claims to "current auto-labeled SAE features." This candor is welcome and partially mitigates the overclaiming in earlier sections.

4. **Contrasting two approaches (behavioral vs. mechanistic).** The framing—comparing what behavioral probes and SAE-based tools each reveal about deception—is a productive structure for future work, even if the present experiments do not fully deliver on the contrast.

## Weaknesses

### Fatal
None.

### Major

1. **Claim-evidence gap in the central negative result.** The abstract states that "autolabel-driven interpretability approaches fail to detect or control behavioral deception," but the evidence is far narrower than this framing implies. The GemmaScope analysis (Section 6.1) checks only five manually selected features (IDs 5665, 14971, 1741, 6442, 10248) on an unspecified number of examples—no systematic search over the full 65k+ feature space. The steering experiments (Section 6.3) test only one model (Llama 3.3 70B), report no quantitative lie rates before/after steering (no rates, no statistical tests, no effect sizes), and include no manipulation check to verify that the steering actually changed the intended feature activations. The paper disclaims these limitations in Section 8.4, but the abstract and conclusion (Section 10) frame the finding as a broad failure, creating a mismatch between claim and evidence that undermines the paper's headline contribution.

2. **Secret Agenda testbed conflates strategic deception with role-play continuation.** The synthetic transcript places the model in a game where lying is the expected narrative move. The paper includes no control condition where lying is penalized or truth-telling is rewarded. Without such a control, the observed behavior could reflect the model continuing the game's role-play narrative (associative text generation) rather than strategic reasoning. The prompt variants (Snails vs Slugs, etc.) control for political content but not for the underlying incentive structure, because all variants still have a clear winning strategy that involves lying. The paper acknowledges this partially (Section 8.2: "models may behave differently in evaluation versus deployment") but does not treat it as a validity threat to the "strategic" attribution.

3. **Insider Trading analysis is purely qualitative and does not validate its claims.** The t-SNE clustering (Figure 4) and heatmaps (Figure 5) are not backed by any quantitative discriminative metric—no classification accuracy, AUROC, precision/recall, cross-validation, or held-out evaluation. The paper claims "population-level structure for risk assessment" but reports no risk assessment metric. Confounds such as response length, refusal keywords, or syntactic patterns are not controlled for. A simple bag-of-words or embedding-based classifier on the text alone might achieve the same separation, and this baseline is not provided. Without quantitative validation, the paper cannot substantiate the added value of SAE activations over text-only analysis.

4. **The two testbeds are not integrated.** The behavioral deception data (Secret Agenda) are not analyzed using the mechanistic tools (SAEs), and the SAE analysis is performed on a different task (Insider Trading). The paper's central narrative—that "autolabel-driven interpretability fails while unlabeled activations succeed"—is a cross-study comparison across different models (Gemma 2 for GemmaScope, Llama for Goodfire), different tasks (game vs. financial compliance), and different analysis methods (feature checking vs. t-SNE clustering). The Secret Agenda outputs could have been analyzed with the same SAE pipeline used for Insider Trading, but this was not done. The paper notes this gap (Section 8.3: "asymmetric analysis depth" due to resource constraints) but it critically weakens the integrated claim.

### Minor

1. **Sample sizes vary drastically across models (n=2–30)** and the bar chart in Figure 1 aggregates trials without normalizing. The paper is transparent about this (table note), but the visual impression of comparative rates (e.g., OpenAI 21/21 "lie" vs. Meta-Llama 7/11 "lie") is misleading because the per-model denominators differ. The paper appropriately uses "at least once" framing but the visualization undercuts this caution.

2. **Steering experiments lack a manipulation check.** The paper does not verify that the steering intervention actually changed the activation of the target features (e.g., by comparing SAE activations with and without steering on held-out inputs). Without this, the failure of steering could have many explanations (wrong features, insufficient steering strength, interaction effects) that are not disentangled.

3. **Feature steering reproducibility is limited.** The steering experiments were conducted via a proprietary web UI (Goodfire dashboard) with only screenshots provided as documentation (Section 9). The paper would be strengthened by code-based or API-based steering that others can reproduce exactly.

4. **No details on response classification methodology for Insider Trading.** The paper classifies responses into Engagement/Helpful/Refusal (Section 7.1) but does not describe the classification method (human annotation? regex? LLM-as-judge?), report inter-annotator agreement, or validate the classification.

### Trivial
None.

## Nice-to-Haves
- A systematic search over the full SAE feature space (65k+ features) for Secret Agenda outputs, comparing auto-labeled features against a data-driven ranking of discriminative features, would directly test whether auto-labeling misses relevant features.
- A within-task mechanistic analysis applying the unlabeled SAE pipeline (t-SNE, discriminative feature ranking) to Secret Agenda lie vs. truth outputs from a single model (e.g., Llama 70B).
- Quantitative steering evaluation with lie-rate measurements before/after steering over multiple trials, with statistical tests.
- Classification accuracy or AUROC for the Insider Trading discriminative features, with confound controls and comparison to text-only baselines.

## Removed Points
These points were flagged by reviewers but are removed or downgraded for the following reasons:

- **"The paper does not claim that SAE architectures cannot represent deception"** — The harsh critic's framing of this as a weakness is partially addressed by Section 8.4, which explicitly limits the scope. However, the abstract's broader phrasing remains a real problem, so the underlying issue is kept as a Major weakness.
- **Criticism about t-SNE perplexity not being specified** — The reproducibility statement (Section 9) says these settings are in the provided Colab notebooks. This is standard practice.
- **Criticism about the "banana" control not validating the method** — The paper's banana steering example is presented as an illustration that steering can work for topical features, not as a validation of deception detection. This is contextualized appropriately.
- **Missing related work concerns** — Removed per the hard rule.
- **Formatting/presentation nitpicks** — Removed per the hard rule.
- **Complaint about "not yet released" or reproducibility concerns about cited resources** — Removed per the hard rule (all cited models/resources assumed to exist).

## Novel Insights
None beyond the paper's own contributions. The reviews surface no genuinely novel observation that the paper itself does not already contain.

## Suggestions
1. **Narrow and reframe the claims.** Either restrict the contribution to the Secret Agenda testbed itself (a useful behavioral probe) and present the SAE analysis as preliminary observations, or expand the SAE analysis substantially: run the full feature search, add quantitative steering metrics with manipulation checks, and apply the same mechanistic pipeline to the Secret Agenda lie/truth data.

2. **Add a control condition to Secret Agenda.** Test the same game format but with lying penalized (truth-telling rewarded). If the model still lies, the behavior is not strategic deception; if it tells the truth, the incentive-driven account is supported.

3. **Quantify the Insider Trading analysis.** Report classification accuracy/AUROC for predicting compliance from unlabeled activations, using held-out prompts, and compare to a text-only baseline (e.g., bag-of-words or embedding classifier) to demonstrate added value.

4. **Calibrate the abstract and conclusion** to match the evidence. Replace "autolabel-driven interpretability approaches fail to detect or control behavioral deception" with a more precise statement like "on the limited set of features and model we tested, auto-labeled features did not activate during or control strategic deception."

## Score and Decision

**Calibration anchors used** (from `deepreview_13k_calibration`):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `9ca9eHNrdH.md` — "Sparse Autoencoders Do Not Find Canonical Units of Analysis" | 7.00 (Accept) | Rigorous experiments, well-supported claims, clear methodology. This paper is substantially weaker across all dimensions. |
| `567BjxgaTp.md` — "How to Catch an AI Liar" | 6.75 (Accept) | Clean execution with proper controls, validated results, strong generalization experiments. Our paper is less rigorous and has narrower validation. |
| `HxKSzulSD1.md` — "Super(ficial)-alignment: Strong Models May Deceive Weak Models" | 6.50 (Accept) | Systematic experiments across multiple model pairs, well-defined metrics. Our paper is more preliminary. |
| `Wf2ndb8nhf.md` — "Targeted Manipulation and Deception Emerge in LLMs Trained on User Feedback" | 6.33 (Accept) | Well-designed simulated environments, clear results. Our paper has weaker experimental design. |
| `vc1i3a4O99.md` — "Interpreting and Steering LLM Representations with Mutual Information..." | 5.00 (Reject) | Mixed reviews citing methodological flaws but with a clear technical contribution. Our paper has a useful testbed but thinner evidence. |
| `YRXDl6I3j5.md` — "Tall Tales at Different Scales: Evaluating Scaling Trends For Deception in LMs" | 3.67 (Reject) | Very weak evidence, unclear experiments, overclaimed results. Our paper is stronger—cleaner testbed, clearer findings within its scope. |
| `NB8qn8iIW9.md` — "Enhancing Neural Network Interpretability with Feature-Aligned SAEs" | 4.00 (Reject) | Comparable in having interesting ideas but limited validation. |

**Comparative judgment**: This paper has a genuinely useful testbed (Secret Agenda) and a worthwhile research question. However, the central claim about the failure of auto-labeled interpretability rests on far too thin an evidence base (5 features checked manually, 1 model for steering, no quantitative metrics, no systematic search). The Insider Trading analysis is purely qualitative. The abstract substantially overclaims relative to what the experiments support. For an ICLR-level venue, the experiments need to be dramatically expanded and the claims properly scoped. The paper reads as promising preliminary work that is not yet ready for a full publication.

**Score**: 4.0  
**Decision**: Reject  

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>