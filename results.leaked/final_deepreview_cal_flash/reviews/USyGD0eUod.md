Now let me write the final consolidated review.

## Summary

This paper tests whether commonly used sparse autoencoder (SAE) quality metrics—particularly auto-interpretability AUROC scores—can distinguish trained transformers from randomly initialized ones across Pythia models (70M–6.9B parameters). The central finding is that these metrics produce surprisingly similar values for trained and randomized models under many settings, challenging the common practice of relying on aggregate auto-interpretability scores as evidence that SAEs have discovered learned, computationally relevant features. The paper also introduces token distribution entropy as a diagnostic that reveals differences in feature "abstractness" that the standard metrics miss, and provides a toy-model analysis suggesting how random networks can preserve or amplify superposition.

## Strengths

1. **Systematic demonstration across model scales and randomization schemes.** The paper compares five carefully constructed variants (Trained, Step-0, Re-randomized incl./excl. embeddings, Gaussian control) across five model sizes (70M–6.9B), multiple SAE expansion factors (16–128), and two training data amounts (100M, 1B tokens). This thorough design makes the negative result substantially more trustworthy than a single comparison would be. The fact that only the Gaussian control falls to chance while trained and randomized variants produce overlapping ROC curves is a genuinely surprising and important finding.

2. **Introduction of token distribution entropy as a useful diagnostic.** The paper shows that this simple metric captures a dimension—feature "abstractness"—that the standard aggregate metrics miss. The finding that trained models show increasing entropy with layer depth while random variants maintain low, flat entropy provides a concrete example of what a better evaluation metric could look like. This gives the paper constructive value beyond its negative critique.

3. **Honest and well-bounded limitations.** The paper explicitly states that the findings do not imply SAEs are useless, that testing all architectures is impossible, and that the entropy metric is preliminary. It recommends practical mitigations (routine randomized baselines, targeted measures of abstractness). This balanced framing distinguishes the work from a purely negative report and gives it practical value.

## Weaknesses

### Major
None.

### Minor
1. **Title overreach relative to the evidence.** The title states that metrics "Do Not Distinguish" trained and random models, which is too categorical. The paper's own evidence shows that for Pythia-6.9B, the fuzzing AUROC for all three randomized variants (0.87–0.88) is systematically *higher* than for the trained model (0.79)—a gap of 0.08–0.09 AUROC. This *does* distinguish the two classes, just in the wrong direction (random > trained). The paper describes these curves as "overlapping" (Figure 1 caption), which understates this inversion. The inversion is arguably more interesting and concerning than mere similarity—it suggests the metric is not just blind but systematically biased—yet it receives no explicit discussion. Meanwhile, the token distribution entropy (which the paper itself introduces) and the CE loss score both successfully differentiate the settings. The body of the paper hedges appropriately ("in many settings... similar," "may not meaningfully distinguish"), but the title and, to a lesser extent, the abstract convey a stronger claim than the evidence fully supports. This is fixable with more careful framing.

2. **Absence of uncertainty quantification in the main results.** Figures 1 and 2 present single traces with no error bars, confidence intervals, or measures of variance across random seeds. For a paper whose central empirical contribution is a *negative* claim (that metrics *do not* meaningfully distinguish), the absence of uncertainty quantification is a notable gap. The reader cannot tell from the main figures whether the observed similarity between trained and random curves is robust across multiple runs or whether a different seed would produce a separation of 0.10 AUROC. The paper references Appendix E for multiple seeds, but the main results should carry this information visibly.

3. **Toy-model section is loosely integrated.** Section 4 demonstrates that random MLPs can preserve or amplify superposition in synthetic and GloVe data, which serves as a plausibility argument for why random transformers might yield interpretable SAE latents. However, this section does not directly test whether the *fuzzing AUROC* behaves similarly on toy data, nor does it establish a mechanistic link between the toy model and the specific transformer results reported in Section 3. The paper acknowledges this ("we defer conclusions as to the mechanism"), but the section remains somewhat disconnected from the main empirical narrative. The space could have been used for additional direct analysis of the AUROC inversion or extended validation of the entropy diagnostic.

### Trivial
- The figure descriptions in the caption extraction (parser artifacts) are present in the manuscript text but do not affect the scientific content.

## Nice-to-Haves
- A downstream validation experiment (e.g., using SAE features from the random model for steering or intervention and showing they produce meaningless results) would substantially strengthen the paper's call for more rigorous validation.
- Reporting AUROC values as a function of model scale with error bars in the main text (not just the appendix) would make the negative claim more convincing.

## Removed Points

These points were raised by reviewers but are not included as weaknesses in the main review. They should be treated with caution.

1. *"The paper's central claim is contradicted by its own strongest evidence because Token Distribution Entropy and CE Loss Score successfully distinguish the settings."* — **Removed.** Token distribution entropy is the paper's *own proposed diagnostic*, not one of the standard "automated interpretability metrics" under critique. The paper explicitly presents it as a proof-of-concept for what the standard metrics miss. CE Loss Score is described as a metric that "only makes sense for the trained variant"—it trivially differs because random models have poor loss, which is expected and not a discovery. The paper's narrative is internally consistent on this point; it does not claim that *no* metric can distinguish, only that the *commonly used aggregate auto-interpretability metrics* fail to do so reliably.

2. *"The paper should cut or move the toy model to an appendix."* — **Removed as too strong.** The toy model serves a useful role as a plausibility argument and provides some mechanistic insight. Its connection could be tighter (noted as a minor weakness above), but removing it entirely is not necessary.

3. *"The paper demands that the abstract and title be brought into alignment with the body's hedging."* — **Partially retained** as the framing issue in point 1 of the weaknesses. The exaggerated title is a real concern, but the abstract is appropriately hedged ("in many settings," "similar").

## Novel Insights

The most striking observation that emerges from combining the two reviewer perspectives is that the paper's most surprising result—the AUROC *inversion* (random models scoring *higher* than trained at 6.9B scale)—is essentially invisible in the paper's own framing. The paper describes this as "similarity" and "overlap," but a systematic 0.09 AUROC gap in the wrong direction is a stronger indictment of the metrics than mere failure to separate. If correct, this inversion implies that the aggregate auto-interpretability score is not just an unreliable validator of learned features but could actively mislead by assigning higher scores to completely untrained models. This inversion, combined with the entropy diagnostic showing that random models learn only single-token features, paints a nuanced picture: the standard metrics capture some signal, but the signal is inversely correlated with the kind of abstract, multi-token feature that mechanistic interpretability cares about. The paper would be substantially stronger if it centered this story.

## Suggestions
1. **Re-frame the title and narrative.** Replace the categorical "Do Not Distinguish" with something like "Can Misleadingly Resemble" or "Do Not Reliably Identify." Use the AUROC inversion as a motivating puzzle—the metric not only fails to identify trained models but systematically favors random ones at large scale—and position the entropy analysis as the resolution.
2. **Add error bars** to the main figures (bootstrapped confidence intervals over latents or standard deviations across seeds). The negative claim requires the reader to be confident that the trained/random similarity is robust.
3. **Discuss the AUROC inversion explicitly.** Include a paragraph analyzing why random models might score *higher* than trained ones on auto-interpretability, tying it to the observation that random models yield more token-specific, single-ID features (which are easier for the explanation pipeline to describe accurately).
4. **Tighten or shorten the toy model section.** Either connect it directly to the AUROC phenomenon (e.g., by testing whether the toy model's Pareto frontiers correlate with the inversion) or move it to the appendix and keep only a one-paragraph summary in the main text.

## Score and Decision

**Calibration protocol.** Round 1 (bracketing) retrieved 18 anchors across three bands. The weak band (avg < 3.5, n=6) contained papers on SAE-adjacent topics scoring 1.67–3.40. The middle band (3.5 < avg < 7.5, n=6) contained papers on SAE evaluation and limitations scoring 4.00–7.00. The strong band (avg > 7.5, n=6) contained papers on broader interpretability topics scoring 7.60–8.20. This placed the paper plausibly between 4.5 and 7.0.

Round 2 (narrowing, 4.5 < avg < 6.5 and 5.5 < avg < 7.5, total n=12) pulled anchors including: "Automatically Interpreting Millions of Features in LLMs" (5.50, Reject) — comparable in quality but less conceptually important; "Applying SAEs to Unlearn Knowledge" (5.25, Reject) — less well-executed; "Interpreting and Steering LLM Representations" (5.00, Reject) — more applied; "Benchmarking Deletion Metrics" (6.00, Reject) — similar critique-of-evaluation contribution but with stronger empirical framing; "PRIME" (6.25, Accept) — cleaner methodology; "One slice is not enough" (7.33, Accept) — stronger experimental design.

Comparing directly: this paper's experimental scope (5 model sizes, 5 randomization schemes, multiple SAE hyperparameters) is more thorough than the 5.00–5.50 rejected anchors. Its conceptual contribution (questioning standard SAE evaluation practice) is important and timely. However, its framing overreach and lack of uncertainty quantification are more severe weaknesses than the accepted papers at 6.25–7.33, which have cleaner narratives and tighter evidence. The closest comparable anchor is "Benchmarking Deletion Metrics" (6.00, Reject), a critique-of-evaluation paper with similar ambition but better specificity in its claims. This paper is slightly weaker due to the framing/title issue, placing it at 5.5.

**Full anchor list:**

| Path | Avg | Round | Comparison to this paper |
|------|-----|-------|------------------------|
| 89wVrywsIy | 3.40 | R1 | Weaker — less systematic |
| Wxl0JMgDoU | 2.50 | R1 | Weaker — narrower scope |
| 9L9j5bQPIY | 2.50 | R1 | Weaker — less relevant |
| UbLvSPMvMA | 1.67 | R1 | Much weaker |
| zgHamUBuuO | 3.00 | R1 | Weaker |
| K9xuqsaP0R | 3.00 | R1 | Weaker |
| ghH6YYDs15 | 4.67 | R2 | Similar quality, different topic |
| 1Njl73JKjB | 7.00 | R1 | Stronger — cleaner methodology |
| 9ca9eHNrdH | 7.00 | R1 | Stronger — more novel techniques |
| sknUS8X9q0 | 4.00 | R1 | Weaker — more narrow |
| F76bwRSLeK | 4.80 | R1 | Slightly weaker |
| NB8qn8iIW9 | 4.00 | R1 | Weaker |
| PBjCTeDL6o | 8.00 | R1 | Much stronger |
| STUGfUz8ob | 7.60 | R1 | Stronger |
| d8w0pmvXbZ | 8.00 | R1 | Much stronger |
| PdaPky8MUn | 8.00 | R1 | Much stronger |
| I4e82CIDxv | 8.00 | R1 | Much stronger |
| tcsZt9ZNKD | 8.20 | R1 | Much stronger |
| 5lIXRf8Lnw | 5.50 | R2 | Similar quality, slightly less important topic |
| yR5QbFv4Xb | 5.33 | R2 | Slightly weaker |
| ZtvRqm6oBu | 5.25 | R2 | Slightly weaker |
| vc1i3a4O99 | 5.00 | R2 | Weaker |
| 9ngFxN83j2 | 5.75 | R2 | Similar quality, different topic |
| ZLAQ6Pjf9y | 5.60 | R2 | Similar quality |
| bXeSwrVgjN | 6.00 | R2 | Slightly stronger — better framing |
| QrEHs9w5UF | 6.25 | R2 | Stronger — cleaner methodology |
| upALuXjdxc | 6.00 | R2 | Slightly stronger |
| Im2neAMlre | 7.33 | R2 | Stronger |
| irorVob9Eq | 5.67 | R2 | Similar quality |
| bwZ9xh178a | 6.00 | R2 | Slightly stronger |

**Round-1 bracket:** 4.5–7.0. **Round-2 narrowing:** centered the paper between the 5.0–5.75 anchors (weaker due to framing issues) and the 6.0–6.25 anchors (which are better executed). Final score: 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>