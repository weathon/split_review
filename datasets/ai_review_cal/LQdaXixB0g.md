- Decision: Reject
- Avg Score: 2.50
- Scores: 3, 1, 1, 5
Now I have a thorough understanding of the paper and all reviewer inputs. Let me produce the consolidated review.

## Summary

This paper applies sparse autoencoders (SAEs) — specifically GemmaScope on Gemma-2-2B — to identify fine-grained mental-health-related features (MHRFs) across all 25 layers, searching for terms related to suicide, sadness, mania, and paranoia. It reports 29 suicide-related features and 42 sadness-related features, finds subtypes within suicide features (e.g., methods vs. statistics), and performs a small-scale activation and steering study on one suicide feature (Layer 25, feature 15435) showing it preferentially activates on suicide vs. homicide prompts and that amplifying it causally shifts model completions toward suicide content. The paper also reports a negative finding: no features related to mania or paranoia were found.

## Strengths

1. **Granular sub-categorization of suicide features beyond prior work.** The paper shows that within the "suicide" topic, SAEs reveal distinct subtypes (e.g., "terms related to suicide, particularly methods and contexts" vs. "data related to suicide statistics and occurrences" in Layer 25, Section 3). This goes beyond the aggregate "mental health" feature reported in prior SAE work (Bricken et al., 2023) and demonstrates clinically meaningful nuance — a distinction that matters because a vulnerable user and a researcher would sought different types of suicide content.

2. **Clinician-guided prompt design for feature validation.** The four prompts (a–d) contrasting suicidal vs. homicidal ideation were designed with psychiatric expertise, and the activation patterns align with the semantic distinction (e.g., "myself" at +99.60 on suicide prompt vs. "someone" at +13.125 on homicide prompt, Section 3). This provides evidence beyond simple correlation that feature 15435 is specifically responsive to suicide-related content.

3. **Demonstration of a steering threshold effect.** Amplifying feature 15435 at strengths +5.0, +10.0, and +100.0 shifts the model's completion from neutral to suicide-related, while +1.0 and clamping do not (Table 2, Section 3). The existence of a threshold between +1.0 and +5.0 is a concrete, reproducible observation that the feature's influence is functionally relevant, not merely correlational.

4. **Exclusion of spurious features using domain knowledge.** When searching for "mania," the authors explicitly excluded unrelated matches like "Wrestlemania" and "Romania" based on clinical judgment (Section 2). This methodological care is a strength over fully automated approaches that might retain such false positives.

## Weaknesses

### Fatal
None.

### Major

1. **The "no mania/paranoia features" finding is based on an unreliable detection method.** The paper searches for features whose auto-generated labels/descriptions contain keywords ("mania", "manic", etc.). This is not a valid test of whether the model *represents* these concepts. Autointerpreter labels are known to be noisy, incomplete, and subject to the labeler's biases; a feature relevant to mania may simply not have had "mania" in its generated description due to polysemanticity or pipeline failure. The paper's central negative claim — "no features related to mania or paranoia were identified, suggesting critical gaps in the model's ability to handle complex psychiatric symptoms" (abstract, Section 3) — is therefore unsupported by the method used. A proper investigation would need activation-based probing: measuring feature activations on curated mania-related vs. control prompts across all layers. This is a structural flaw specific to this claim: the detection method cannot answer the question being asked.

2. **Experimental validation is extremely thin.** Only one feature (15435, Layer 25) is evaluated. The activation test uses only four prompts (two suicide, two homicide) with no control for other emotionally negative content (e.g., "I want to hurt myself," "I feel worthless"), no statistical testing, no baseline comparisons (e.g., average activation across many random prompts to contextualize raw values like +125.40), and no comparison to features from other layers or other search terms. The steering experiment uses a single prompt ("I'm so sad that I might commit") and a single feature. While steering does change the completion — consistent with well-documented results (Golden Gate Claude, prior SAE steering work) — the paper does not compare against random features, test whether the effect is specific to this feature, measure whether steering disrupts other capabilities, or use diverse prompts. The conclusion that steering has "causal impact" is true but demonstrated only at the level of a single anecdotal example; the paper does not establish that this feature is *diagnostic* of the model's suicide representation in any generalizable way.

3. **Gap between base-model findings and safety claims for deployed chatbots.** The paper repeatedly frames its contribution as improving safety of AI mental health chatbots, yet Gemma-2-2B is a base language model (not instruction-tuned or RLHF-aligned). The paper never discusses whether the same features exist in, or can be steered in, safety-tuned models actually used in deployment. The steering experiment shows that amplifying a feature increases suicide-related output from a model that, in its base state, does *not* produce such completions for the tested prompt — but this does not directly inform how instruction-tuned models behave or how feature steering would interact with safety training. The practical safety framing is aspirational rather than supported by the experiments.

### Minor

1. **Insufficient detail for reproducibility of steering.** The paper says steering was done via "Neuronpedia's steering tool/API" (Section 2) but does not specify the mechanism: is the feature's decoder direction added to the residual stream at every token? At the target layer only? At inference time or generation time? The scale (-100 to +100) is given but the mapping from this scale to actual activation magnitudes is not. This makes it difficult for others to replicate or build on the results.

2. **The code listing is misleading.** The methods section states "Listing 1 shows the Python code necessary to recreate this evaluation," but the listing's own caption says it shows "the creation of an IFrame for visualizing mental health-related features." The actual activation measurement and steering code is not shown, contradicting the reproducibility claim.

3. **Raw activation values are unnormalized and lack baselines.** The activation values reported in Figure 2 (+125.40, +99.60, etc.) are given without any baseline or normalization. It is impossible for a reader to assess whether +125 is high, moderate, or typical for this feature across diverse inputs. Reporting raw values without context limits the interpretability of the key quantitative result.

4. **No statistical rigor.** Results are presented as single examples with no error bars, repeated trials, or confidence intervals. LLM outputs are stochastic; single completions at a single seed do not constitute deterministic evidence. While single-run evaluation is common in some SAE exploratory work, the paper's claims about feature relevance and causal impact would benefit from at minimum reporting of multiple runs.

5. **Ethical discussion, while present, is too brief given the demonstration.** The paper demonstrates that amplifying a suicide feature *increases* suicidal completions. While the paper does acknowledge dual-use risk (Section 4), this is addressed in a single paragraph that quickly pivots to justifying the research. Given the direct demonstration of a technique to increase harmful content, a more thorough discussion of safeguards, disclosure, and responsible-use guidelines would be warranted.

### Trivial
None.

## Nice-to-Haves
- Replace the auto-label-based search for mania/paranoia with activation-based probing using curated mania-related, psychosis-related, and neutral text datasets. This would make the negative finding meaningful.
- Validate the suicide feature systematically across ~100 prompts spanning suicide ideation, self-harm, homicide, and neutral content, reporting precision/recall or AUC for distinguishing suicidal from non-suicidal content.
- Conduct a controlled steering study with multiple features (suicide, random, unrelated) at matched strengths, a diverse prompt set, and quantitative metrics (e.g., proportion of suicide-related tokens).
- Discuss the base-model vs. instruction-tuned gap explicitly as a limitation, or replicate a key experiment on a tuned variant.
- Provide a deeper analysis of the layer distribution pattern (e.g., why layers 4 and 24 have no MHRFs; whether this is an artifact or a structural property).

## Removed Points
These points were flagged for removal; treat them with caution if cited elsewhere.

- **Harsh Critic: "Introduction overstates the gap; Bricken et al. (2023) already used SAEs to find a 'mental health' feature."** — The paper correctly distinguishes its contribution: prior work found a single aggregate "mental health" feature, while this paper takes a *more granular* approach identifying distinct subtypes. The paper explicitly cites Bricken et al. and situates its work as an extension, not a claim of priority. The criticism misreads the claim.
- **Harsh Critic: "Layers 4 and 24 had no features — this is not discussed."** — The paper does mention this observation both in Results (Section 3) and Discussion (Section 4: "It is also interesting that there is not a feature in any layer..."). It is not deeply analyzed, but it is not ignored.
- **Harsh Critic: "Only six search terms; depression notably absent."** — The paper explains the psychiatric rationale for choosing sadness as a proxy for depression. This is a reasonable scoping choice for an exploratory study.
- **Harsh Critic: "Figure 1 axes not labeled, not interpretable."** — This is a PDF extraction artifact; the original figure is present in the submission.
- **Harsh Critic: "Speculation without evidence about SOTA model performance on depression vs. psychosis."** — The paper clearly marks this as speculation ("If this pattern holds... this might partially explain..."). Speculation is appropriate in a Discussion section.
- **Strength Finder: Strength 3 "Systematic negative finding for mania and paranoia across all layers."** — This conflicts with the verified Major weakness (Weakness 1) that the detection method for this negative finding is methodologically invalid. Per the filtering rules, the weakness wins, so this strength is removed.
- **Strength Finder: "Clinician-guided verification with contrasting prompts"** — While this has some merit, the validation is of only four prompts on one feature, which is too thin to count as a strong supporting strength. Moved here for context but not treated as a core strength.
- **Harsh Critic: "Duplication across layers not analyzed; autointerpretation may be conflating them."** — This is a minor speculation about a peripheral observation, not a verifiable weakness that harms the paper's claims.

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface any observation about the work that the paper itself does not already state or clearly imply. The harsh critic's methodological critique of the auto-label-based search is the one point that goes beyond what the paper acknowledges, but it is a standard limitation of this paradigm rather than a novel insight.

## Suggestions

1. **Re-do the mania/paranoia investigation using activation-based probing.** Take a set of mania-related prompts (e.g., describing grandiosity, racing thoughts, decreased need for sleep) and measure feature activations across all layers, identifying features that differentially activate regardless of their auto-labels. This would either confirm the negative finding rigorously or reveal features the autointerpreter missed.

2. **Expand the activation and steering validation.** Test at least 3-5 features from different layers and search terms. Use a larger prompt set (20-50 prompts) spanning suicide, self-harm, homicide, general negativity, and neutral content. Report quantitative metrics (precision/recall, AUC, or effect sizes) with multiple runs.

3. **Add ablation controls for steering.** Show that amplifying a random feature or a top-activating but conceptually unrelated feature (e.g., a punctuation feature) at similar strengths does not produce the same behavioral shift. This would demonstrate specificity of the suicide feature's causal role.

4. **Explicitly discuss the base-model limitation and its implications for the safety claims.** Acknowledge that findings on a 2B base model may not directly transfer to instruction-tuned, safety-aligned chatbots, and outline what further work would be needed to bridge this gap.

5. **Specify the steering mechanism in sufficient detail for reproduction.** Describe whether the feature direction is added to the residual stream, at what layer, at every token position, and how the -100 to +100 scale maps to actual activation magnitudes.
