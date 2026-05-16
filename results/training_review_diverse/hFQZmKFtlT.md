Now I have all the information I need. Here is my final consolidated review:

---

## Summary

This paper introduces a controlled experimental framework using formal grammars (random and hierarchical) to cleanly separate rote memorization from genuine generalization in LLMs. By training models (Pythia-1B, Llama3-8B, Mistral-Nemo-12B) on small synthetic datasets with known distributions and independent test sets, the authors make three core observations: (1) models pass through an overlapping generalization phase followed by a memorization phase; (2) memorization harms generalization and, symmetrically, learning new data erases previously memorized data; (3) lower-entropy distributions are easier to generalize to but harder to memorize, and vice versa. The paper also demonstrates that training loss alone cannot distinguish memorization from generalization, since two models can achieve identical training loss while one is in the memorization phase and the other is still generalizing.

## Strengths

1. **Clean, well-motivated experimental framework.** Using formal grammars gives full control over the data distribution, guarantees no prior model exposure, and provides ground-truth test sets from the same distribution. This is a genuine methodological contribution that enables precise measurement of the memorization–generalization distinction, which would be impossible with natural language. Figure 1 confirms the manipulation succeeds: grammar-trained models distinguish grammatical strings from random strings.

2. **Demonstration that memorization and generalization are at odds, with two-way causality.** The sequential training experiment (Figure 4) shows that after fully memorizing a first dataset, training on a second dataset from the same distribution causes the loss on the first dataset to rise from near zero to match the test loss. This empirically establishes that (a) memorization harms generalization *and* (b) learning new data actively erases prior memorized content — a specific, non-obvious finding with implications for unlearning and privacy.

3. **Entropy as a systematic modulator of learning dynamics.** The paper provides convergent evidence across three orthogonal manipulations of entropy (alphabet size, token oversampling, production rule skew) and three model families, all showing the same qualitative trend: lower entropy → better generalization, slower memorization; higher entropy → faster memorization, worse generalization (Figure 5). The consistency across manipulations rules out artifact-driven explanations.

4. **Practical impossibility result for prior memorization measures.** Figure 3 directly demonstrates that two models with identical training loss can be in fundamentally different learning phases — one memorizing, one generalizing. This cleanly exposes the failure of recollection-based memorization measures (both the conservative 50-token and liberal 1-token variants) and supports the paper's central methodological critique: any useful memorization measure must contrast training and test performance.

## Weaknesses

### Fatal

None.

### Major

None. The paper's core claims are well-supported within its stated scope.

### Minor

1. **The 5% divergence threshold for memorization onset is arbitrary and untested.** The paper defines memorization start as the epoch where test loss exceeds training loss by >5% (Section 3.1, line 83), but provides no justification for this specific value and no robustness analysis. While the paper's qualitative observations (existence of two phases, overlap, entropy trends) are unlikely to be sensitive to the exact threshold, the precise epoch-level comparisons across models (e.g., "Pythia starts memorization at epoch 9 vs. Llama at epoch 6") rely on this threshold. A simple supplementary analysis showing robustness across 2%, 5%, and 10% thresholds would address this cleanly.

2. **The sequential forgetting experiment does not distinguish between competing mechanisms.** The paper interprets the rise in D1 loss during D2 training as "generalization harming memorization," but does not discuss the alternative explanation of standard catastrophic forgetting (McCloskey & Cohen, 1989). The observation that D1 loss rises to match test loss (rather than to a random level) is *more specific* than simple catastrophic forgetting and does suggest a reversion to generalization, but the paper would benefit from either a control experiment (training on a different-distribution dataset after D1) or a more explicit discussion of why the observed pattern goes beyond catastrophic forgetting.

3. **Random-string baseline is shown only in Figure 1, not in the main experiments.** The paper uses random strings in Figure 1 to demonstrate that the model learns the grammar, but does not include this baseline in Figures 2, 4, and 5. Including the random-string loss would help confirm that models never simply memorize all strings, and would strengthen the interpretability of the main results.

4. **Statistical variance of the epoch-level markers is not reported.** The paper aggregates results over 5 runs (with standard deviation shown for loss curves), but does not report variance for the specific epoch numbers where memorization starts or generalization ends. Given that these markers are used for cross-model comparisons, reporting their stability would improve reliability assessment.

5. **Hyperparameter details are incomplete.** The paper mentions gradient accumulation and number of epochs but does not state the learning rate, optimizer, scheduler, or other training hyperparameters. While some of these may reside in a parser-stripped appendix, the main text should at minimum list the key settings for reproducibility.

### Trivial

- The claim that the paper "stands in contrast to many related works that solely focused on LLM memorization from the perspective of quantifying privacy risks" (line 35) slightly overstates the distinction, since cited works such as Tirumala et al. (2022) and Jagielski et al. (2022) do study memorization dynamics. The paper engages with those works appropriately elsewhere, so this is a minor framing imprecision.

## Nice-to-Haves

- **Exact string recall analysis.** In addition to loss, reporting the proportion of training strings the model can generate exactly (or next-token accuracy on training vs. test) at each epoch would directly quantify "recollection" and further strengthen the argument about why loss alone is insufficient.
- **Model size scaling.** Testing at least two sizes within one family (e.g., Pythia-70M vs. 1B) would clarify whether the phase dynamics scale with model capacity.
- **Small-scale natural-language probe.** A brief experiment fine-tuning on a small set of structured natural-language strings (e.g., poems with a fixed meter) could bridge the gap between the synthetic regime and the claimed practical implications.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"The experimental setup uses very small training sets (n=8 and n=64) and synthetic data, which limits the strength of claims about LLM behavior in naturalistic settings"** — The paper is explicitly scoped as a foundational "laboratory conditions" study (Section 6). The synthetic data is a deliberate methodological choice, not a flaw. The paper acknowledges this limitation and does not overclaim. This criticism evaluates the paper against expectations for applied NLP work, not for a controlled scientific study of learning dynamics. Removed per scope-mismatch rule.
- **"The sequential memorization experiment is interpretively underdetermined — could be catastrophic forgetting"** — As noted in Minor Weakness #2, this is a valid observation but the reviewer overstates its severity. The D1 loss rises to match *test loss* (not a random baseline), which is more specific than simple catastrophic forgetting. The paper's core observational claim stands regardless of mechanism attribution. Kept but downgraded to a minor note.
- **"The paper does not discuss potential positive roles of memorization (e.g., factual recall)"** — The paper explicitly scopes this out (line 37: "we do not engage with the question of memorization being desirable or undesirable"). Scope creep. Removed.
- **"No analysis of model size effects"** — Moved to Nice-to-Haves.
- **Various formatting/typo/style nitpicks** — Removed per instruction (parser artifacts, not author errors).

## Novel Insights

The most interesting insight emerging from the reviews is that the paper's core finding — that memorization onset and generalization offset overlap — has a natural explanation through the lens of loss landscape geometry that neither the paper nor the reviewers fully develop. Specifically, the observation that re-training on a new dataset causes the loss on an old dataset to rise to *match the test loss* (not to a random baseline) suggests the model is not simply overwriting weights but is actively driven toward the distribution-level attractor defined by the grammar. This points toward an interpretation where generalization corresponds to finding a basin in the loss landscape that captures the distribution, and memorization corresponds to descending further into data-point-specific wells within that basin. When new data from the same distribution arrives, the model returns to the distribution-level basin before carving new wells. This perspective, if correct, would unify the sequential forgetting result, the entropy trends (lower entropy means a narrower, more defined basin), and the impossibility of judging memorization from recollection alone (since being in the basin vs. a well can yield identical point-wise loss).

## Suggestions

1. Add a robustness analysis showing that the 5% threshold choice does not affect qualitative conclusions (e.g., repeat key figures with 2% and 10% thresholds).
2. Add a brief discussion of catastrophic forgetting in Section 4, explaining why the observed pattern (D1 loss rising to match *test* loss) is more specific than generic overwriting.
3. Include a random-string baseline in Figures 2, 4, and 5 for completeness.
4. Report variance for the epoch-level cross and triangle markers across the 5 runs.
5. Add a sentence with the key training hyperparameters (learning rate, optimizer) to the main text or prominently note that they are in the appendix.

## Score and Decision

This is a well-executed empirical study that makes several clean, non-obvious observations about memorization dynamics in LLMs using a deliberately simplified but well-controlled framework. The weaknesses identified are minor and addressable; none threaten the paper's core contributions. The paper is clearly written, the figures communicate effectively, and the findings have genuine value for the community's understanding of how LLMs store and retrieve information.

**Score**: 7.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>