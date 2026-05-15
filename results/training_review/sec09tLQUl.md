Now I have all the information needed to produce a rigorous, evidence-based review. Let me finalize.

---

## Summary

This paper connects minority-group poor generalization in spurious-correlation settings to memorization, and proposes FairDropout — an example-tied dropout method that pre-allocates "memorizing" neurons during training and drops them at inference. The authors first demonstrate (via the neuron-flipping procedure of Maini et al., 2023) that minority-group examples on CelebA rely on fewer critical neurons, and that dropping those neurons improves worst-group accuracy in ~75% of cases. They then scale example-tied dropout to ResNet-50 and BERT, reporting competitive worst-group accuracy on a five-dataset benchmark spanning vision, language, and medical domains.

## Strengths

- **Novel diagnostic linking minority-group poor generalization to memorization in spurious-correlation settings.** The analysis in §3.2 (Figures 2–3) shows that minority-group examples require fewer neurons to flip, and that dropping those neurons systematically improves test worst-group accuracy. This extends the Maini et al. (2023) memorization-localization framework from label noise to spurious correlations for the first time, providing a useful mechanistic perspective.

- **Scaling of example-tied dropout to large architectures.** Previously demonstrated only on small networks (ResNet-9), the paper shows that example-tied dropout can be applied to ResNet-50 and BERT, demonstrating practical feasibility on modern architectures (§3.3, §4.2).

- **Broad evaluation across diverse modalities.** The benchmark covers image (CelebA, Waterbirds, MetaShift), text (MultiNLI), and medical X-ray (MIMIC-CXR) datasets, using the standardized subpopulation-shift library (Yang et al., 2023). FairDropout achieves strong gains over ERM on MultiNLI (+7.8 points) and MIMIC-CXR (+7.2 points), and is competitive with methods that require group annotations.

- **Practical advantage of not requiring group annotations.** FairDropout improves over ERM on 4 of 5 datasets without needing training or validation group labels, making it more scalable than methods like GroupDRO or DFR.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison to standard dropout (the most critical missing baseline).** FairDropout is a dropout variant, yet the paper includes no comparison to vanilla dropout at comparable rates and layer placement. The warm-up experiment on CelebA (§4.1) shows a 45%→80% jump when switching from training-mode (neurons kept) to test-mode (neurons dropped) — an interesting within-method control — but this does not isolate whether the improvement comes from the *example-tied allocation mechanism* or simply from the regularization effect of having any dropout at test time. Without this baseline, the paper cannot substantiate the claim that FairDropout's design ("redirecting memorization") is responsible for the gains.

2. **Gap between diagnostic analysis and the method's mechanism.** The analysis in §3.2 identifies *critical neurons* via an expensive sequential procedure, and shows that dropping *those specific neurons* improves worst-group accuracy. However, FairDropout (§3.3) does **not** identify or target those neurons — it randomly allocates a fixed number of "memorizing" neurons per example *before training*. The paper provides no evidence that (a) the randomly allocated neurons actually capture spurious features, or (b) the model learns to redirect memorization to them as claimed. The warm-up experiment shows that memorizing neurons matter *after* training with FairDropout, but does not verify they capture the same phenomenon as the neurons identified in §3.2. The paper acknowledges this indirectly in its limitations (L. 197–199: "we hypothesize... this assumption requires further exploration"), but the central causal narrative is not supported by direct evidence.

3. **Mixed benchmark results relative to the paper's claims.** The paper states that FairDropout "outperforms spurious correlation methods," but the results are more nuanced:
   - On **Waterbirds**, FairDropout (85.4) substantially underperforms DFR (90.6), ReWeightCRT (90.0), and several other methods.
   - On **CelebA**, FairDropout (75.6) is comparable to simple Resample (74.1) and ReWeight (73.6).
   - On **MetaShift**, FairDropout (85.9) is tied with ReWeightCRT (85.1±0.4 vs 85.9±1.1).
   - The strongest results are on **MultiNLI** and **MIMIC-CXR**, where gains over ERM and baselines are substantial and clear.
   
   The paper's claims should be calibrated to reflect where the method genuinely excels versus where it is merely competitive.

### Minor

1. **Ambiguous description of the allocation mechanism (§3.3).** The method description states "each sample is allocated a memorizing neuron uniformly with probability p_mem" while also stating "every example allocates the same fixed number of memorizing neurons" and "each image allocates only one memorizing neuron." It is unclear how p_mem interacts with the allocation — is it a per-example Bernoulli draw governing whether a memorizing neuron is assigned, or does every example always get one? If the latter, what does p_mem control? This needs clarification.

2. **No hyperparameter sensitivity analysis.** Only a single warm-up setting (p_mem = p_gen = 0.2) is shown on CelebA, and the paper does not report how results vary across a grid of these hyperparameters or across different layer placements, despite noting that placement is tuned per dataset.

3. **Small-scale memorization analysis without confidence intervals.** The neuron-flipping experiment (§3.2) uses 100 examples per group, and no confidence intervals are reported for the proportion (~75%) of cases where dropout improves accuracy. While this is an exploratory analysis, stronger statistical grounding would support the paper's mechanistic claims.

### Trivial
- The paper states "the fair prefix comes from the fact that every example allocates the same fixed number of memorizing neurons" — but the hyperparameter p_mem notation suggests probabilistic allocation. This tension should be resolved in the description.

## Nice-to-Haves

- **Standard dropout baseline:** Adding a comparison to standard dropout at matched rates and placement would cleanly separate the effect of the example-tied design from pure regularization.
- **Mechanism verification:** Apply the neuron-flipping procedure (from §3.2) post-hoc to a FairDropout-trained model to check whether the allocated memorizing neurons disproportionately correspond to critical neurons for minority examples. This would validate (or refute) the claimed mechanism.
- **Combination experiments:** The paper claims FairDropout "can be combined with any baseline method" but does not test this. A simple combination with, e.g., JTT or DFR would demonstrate additive value.
- **Analysis of Waterbirds underperformance:** The paper attributes Waterbirds underperformance to pre-trained features being easily transferable, but this explanation is not tested directly.

## Removed Points

- **"Conflation of memorization and spurious feature reliance" (Critic Point 3):** The paper defines memorization (after Maini et al., 2023) as "the ability to correctly predict atypical examples with potentially wrong patterns." In spurious-correlation settings, minority-group examples are precisely the atypical cases where the shortcut does not hold, so the model must fit them individually. The paper's framing of this as memorization is coherent and not a conflation — the neuron-flipping evidence (fewer neurons needed to flip, dropping them helps) directly supports this framing. **Removed** because it mischaracterizes the paper's argument.

- **"Critic's §2.3 note that Maini et al. did not apply a dropout scheme":** The paper correctly states "Drawing inspiration from the example-tied dropout introduced in the context of label noise by Maini et al. (2023)." Maini et al. *did* propose example-tied dropout alongside the detection method. The criticism is factually incorrect. **Removed.**

- **Strength Finder's warm-up claim as "single most important piece of evidence":** The warm-up experiment is indeed informative, but it does not by itself validate the claimed mechanism — see Major Weakness #2. This strength is retained in spirit (the warm-up is mentioned in the Summary) but downgraded from "single most important" since it does not fully close the mechanism gap.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the diagnostic analysis and the method: the paper convincingly shows that *if you can identify critical neurons for minority examples, dropping them helps* (Figure 3), but FairDropout allocates neurons randomly rather than identifying them. This raises a non-trivial question: does the method work because allocating ANY fixed neurons per example induces the model to use them for memorization (as claimed), or could a much simpler explanation suffice — namely, that having a per-example dropout mask at a fixed location during training, combined with dropping those neurons at test time, simply regularizes the model in a way that happens to benefit worst-group accuracy? The paper's internal control (training mode vs. test mode) is a step toward answering this, but without comparing to standard dropout or verifying the neuron correspondence, the question remains open. If FairDropout's gains are empirically robust but mechanistically unvalidated, the paper's contribution shifts from "a new principle for debiasing" to "an interesting but underspecified heuristic."

## Suggestions

1. **Add standard dropout as a baseline** — this is non-negotiable for a paper about a dropout variant. Compare FairDropout to vanilla dropout at matched rates, placement, and total dropped-neuron count.
2. **Run a post-hoc verification experiment**: train with FairDropout, then run the neuron-flipping procedure from §3.2 on the trained model. Check whether the allocated memorizing neurons are disproportionately among the critical neurons for minority examples. This would directly substantiate the claimed mechanism.
3. **Clarify the allocation rule**: resolve the ambiguity between p_mem as a probability and the "fixed number" claim. Provide a precise algorithmic description.
4. **Add a hyperparameter ablation** showing worst-group accuracy across a grid of p_mem and p_gen values on at least one dataset.
5. **Calibrate the paper's claims** to acknowledge that FairDropout is competitive (rather than consistently superior) on several benchmarks, and excels primarily on MultiNLI and MIMIC-CXR.

## Score and Decision

The paper presents a novel diagnostic analysis and a creative method, but the contribution is undermined by the absence of a standard dropout baseline and the gap between the mechanistic narrative and the validation evidence. The empirical results are promising but mixed. Major revisions — most critically the dropout baseline and mechanism validation — are needed before the paper's contribution can be properly assessed.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>