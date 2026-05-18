Now I have all the information needed. Let me craft the final consolidated review.

## Summary

This paper uses formal grammars (random and hierarchical) to create a controlled experimental framework for studying the dynamics of memorization (learning by rote) vs. generalization (learning with understanding) in LLMs. By training models from three families (Pythia-1B, Llama3-8B, Mistral-NeMo-12B) on tiny datasets (n=8 or 64) of grammar-generated strings over many epochs, the paper tracks train/test loss dynamics and makes three main claims: (1) rote learning and learning with understanding are inversely related during training, (2) entropy of the training distribution governs which type of learning dominates, and (3) one cannot determine memorization from training-set recollection alone—a test-set comparison is needed. The framework is clean and the experiments are well-executed, but the paper's framing significantly oversells the novelty of its empirical findings.

## Strengths

- **Controlled experimental framework using formal grammars.** Unlike natural-language settings where disentangling memorization from generalization is inherently difficult, the grammar-based data generation provides precise control over syntax, entropy, and distribution, guarantees the model has had no prior exposure, and enables clean measurement of train-vs-test loss divergence. This is a genuine methodological contribution that the field can build on (Section 2, Section 3.1).

- **Clear demonstration that identical training loss can correspond to different learning phases.** Figure 3 shows two Pythia models (trained with n=8 vs. n=64) achieving the same training loss of ~0.6, yet the n=8 model is in the memorization phase (test loss diverged to ~0.8) while the n=64 model is still generalizing (test loss ~0.6). This concretely illustrates why recollection-only measures of memorization (e.g., Carlini et al. 2022's 50-token criterion, Tirumala et al. 2022's single-token criterion) are insufficient—they fail to account for the contribution of generalization.

- **Systematic characterization of how entropy affects learnability.** Section 5 varies entropy through three independent manipulations (alphabet size, token oversampling, production-rule skew) across all three model families, consistently showing that lower-entropy distributions yield lower test loss (better generalization) while higher-entropy distributions exhibit a larger train-test gap (more memorization by their measure). This provides a principled basis for thinking about which types of strings may be more or less susceptible to rote memorization.

- **Consistency across diverse model architectures and scales.** All main results (Figures 2, 4, 5) are replicated across Pythia-1B, Llama3-8B, and Mistral-NeMo-12B, spanning more than an order of magnitude in parameters. This rules out architecture-specific artifacts and suggests the findings reflect fundamental learning dynamics shared across autoregressive LLMs.

## Weaknesses

### Fatal
None.

### Major

- **The paper systematically oversells the novelty of its empirical observations, presenting standard properties of neural network overfitting as surprising discoveries.** The two core dynamical findings—(a) that models initially generalize before overfitting to specific training examples, and (b) that training on a new small dataset overwrites previously overfit examples (catastrophic interference)—are textbook behaviors of neural networks trained to convergence on tiny datasets. The paper repeatedly characterizes these as "surprising and unexpected" (Section 1, Section 4, Section 6) and claims they "cannot be easily explained" (Section 6), when in fact they are exactly what one would expect from models with vastly more capacity than needed to memorize a handful of strings. The controlled grammar setup is a valuable way to *measure* these dynamics cleanly in LLMs, but presenting textbook overfitting and catastrophic interference as surprising findings misrepresents what is known. The paper would be substantially stronger if it acknowledged these connections and focused on what the grammar framework uniquely adds (e.g., measuring the *relative timing* of phases across models, manipulating entropy independently of other factors, the regeneralization phenomenon in Section 4) rather than claiming the phenomena themselves are novel.

- **The operational definition of memorization conflates rote learning with relative overfitting, and this conflation weakens the entropy analysis.** The paper defines memorization (learning by rote) as the train-test loss gap and proposes the measure `1 – loss_train/loss_test`. This is a measure of *relative overfitting*, not of rote recall in any absolute sense. The problem is most visible in the entropy experiments (Section 5): on a low-entropy grammar, both train and test losses are low, so the gap is small by construction—making the memorization measure low even if the model has perfectly memorized every training string. The paper's conclusion that "lower-entropy strings are harder to memorize" is therefore partly a mathematical consequence of the measure rather than an empirical discovery about the cognitive difficulty of rote recall. The paper acknowledges that the measure captures relative overfitting but then interprets it in terms of "rote learning" as if it measured absolute recall. This distinction matters for the practical implications (e.g., privacy risks: a model that has perfectly memorized low-entropy strings may still have a low memorization score by this measure).

### Minor

- **The 5% divergence threshold for memorization start is arbitrary and no sensitivity analysis is provided.** The paper defines memorization as starting when test loss exceeds training loss by more than 5% (loss_train/loss_test > 1.05). Different thresholds would shift the reported epoch of memorization onset, and it is unclear whether the cross-model comparisons (e.g., "Pythia-1B starts memorization later than Llama3-8B") are robust to this choice. A sensitivity analysis (e.g., testing 1%, 10% thresholds) would strengthen the claims.

- **The cryptographic-key forgetting analogy in the practical implications is not supported by the experiments.** The paper suggests that memorizing new cryptographic keys of a certain format could cause an LLM to forget previously memorized keys (Section 4). However, the experiment uses 8 training strings from the same grammar; the model forgets them when trained on 8 other strings from the *same* distribution. Real-world cryptographic keys are far more numerous and structurally different from grammar-generated strings. The analogy is stretched and should be caveated as speculative.

- **The paper does not examine whether the observed patterns are specific to LLMs (transformer architecture) or would generalize to any model trained on tiny datasets with many epochs.** The paper is titled "Rethinking Memorization in LLMs," but the key dynamics (generalization then overfitting, catastrophic forgetting when switching tasks) are known to hold for simpler architectures trained on small data. Replicating even one condition with an LSTM or MLP would clarify whether the findings are about LLMs or about neural-network overfitting in general.

- **The practical utility of the proposed memorization measure is limited by the requirement for a test set from the exact same distribution.** The paper acknowledges this (Section 3.2) and leaves it as "future work," but this is a fundamental limitation: in real-world privacy/copyright audits, one does not have access to a test set drawn from the precise distribution that generated the training data. The measure is therefore primarily useful within the paper's own controlled framework, which limits its practical impact.

### Trivial

- The "generalization ends at test loss minimum" terminology is slightly imprecise: test loss can continue improving (decreasing) after memorization starts (the curves overlap). The paper's operational definition is clear, but the prose framing of "end of generalization" over-interprets what is simply the test loss minimum.

## Nice-to-Haves

- A sensitivity analysis for the 5% memorization-start threshold across a range of values (e.g., 1%, 10%, 20%) to assess robustness.
- A version of Figure 2 that shows loss curves at the *same y-axis scale* across model families to facilitate cross-model comparison of absolute loss values.
- An ablation with a non-transformer architecture (e.g., LSTM) to test whether the observed dynamics are architecture-specific or general.
- Probing experiments that move beyond input-output curves to study what the model learns internally during the generalization vs. memorization phases (e.g., does it learn grammar production rules during generalization?).

## Removed Points

These points from the reviewer are flagged as unreliable and should be treated with caution:

- **Criticism about missing citations of specific works on overfitting and catastrophic forgetting** (Neyshabur et al., Keskar et al., McCloskey & Cohen, Kirkpatrick et al.): Removed per the rule that missing-related-work complaints cannot be verified. The general point about overclaiming novelty is kept in Major weakness 1.
- **Criticism that the paper's impossibility claim ignores Carlini et al.'s use of counterfactuals**: The paper does discuss Carlini et al. 2022 (lines 97-104) and characterizes their approach accurately. The paper's point is that even counterfactuals don't solve the fundamental issue if they are not from the *same distribution*, which is a valid extension. This criticism misreads the paper's argument.
- **Request to add mechanistic probing of internal representations**: This is outside the paper's stated scope (which is to provide input-output observations and leave mechanism to future work — stated explicitly in Limitations, line 159). Added as a Nice-to-Have instead.
- **Criticism about not testing different string lengths or more grammar types**: This is a reasonable direction for future work but demanding it amounts to scope creep for a single paper that already tests two grammars, three model families, and multiple entropy manipulations.
- **Criticism about no discussion of model capacity relative to dataset size**: The paper partially addresses this by comparing n=8 vs n=64 and across three model sizes (1B, 8B, 12B). A deeper discussion would be nice but the comparison is present.

## Novel Insights

Beyond the paper's own contributions, the most interesting emergent observation is the **regeneralization phenomenon** in Section 4: when training switches to the second dataset, the loss on the *first* dataset temporarily drops and plateaus near the test loss before rising again. This suggests that the model briefly recovers a distributional understanding of the grammar (which it had lost while overfitting to the first dataset) before overfitting to the new dataset. This specific dynamic—the model's ability to "bounce back" to generalization when exposed to fresh data from the same distribution—is not a standard finding in classic overfitting and could be a genuinely novel observation worth further investigation. The paper reports it but does not analyze it.

## Suggestions

1. **Reclaim the framing.** The paper's genuine contribution is the controlled grammar framework and its use to *measure and decompose* memorization vs. generalization in LLMs, not the discovery of new training phenomena. Reframe the paper accordingly: present the observations as clean empirical demonstrations enabled by the framework, not as surprises. Remove claims like "cannot be easily explained."
2. **Add a sensitivity analysis for the 5% threshold.** Justify the threshold empirically or show that the qualitative patterns are robust across a range of thresholds.
3. **Disambiguate the entropy results.** Acknowledge that the memorization measure (train-test gap) is partly a mathematical artifact: when test loss is low, the gap is mechanically constrained. Clarify what is actually being claimed about "harder to memorize."
4. **Replace or heavily caveat the cryptographic-key example.** It is not supported by the experiments and weakens the paper's credibility.
5. **Discuss the capacity-to-data ratio explicitly.** The models have orders of magnitude more capacity than needed to memorize 8 strings. This context is essential for interpreting the observed dynamics.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>