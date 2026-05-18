Now I have all the information needed to construct the final review. Let me produce the consolidated assessment.

## Summary

This paper introduces Conditional Activation Steering (CAST), a method that extends activation steering by adding "condition vectors" — directions in activation space that detect whether an input belongs to a particular category (e.g., hate speech, legal advice). During inference, CAST computes the similarity between a hidden state and its projection onto the condition vector, and uses a threshold to decide whether to apply a behavior vector (e.g., a refusal vector). This enables rules like "if input is about hate speech, then refuse." The method is evaluated on nine models ranging from 1.8B to 32B parameters, demonstrating selective refusal, logical composition of conditions, domain constraining, and several properties (duality, modulation, saturation).

## Strengths

1. **Context-dependent control via condition vectors is a genuine extension of activation steering.** CAST introduces a new type of steering vector—the condition vector—that selectively gates behavior vectors based on input content. This directly addresses the key limitation of prior activation steering (indiscriminate application) and is clearly demonstrated in Figures 1-3 with qualitative examples across multiple models.

2. **Logical composition and duality enable programmatic refusal rules.** The paper shows OR composition of multiple condition vectors (Figure 2a) and negation via the duality property (flipping the comparison direction, Section 4). This allows implementing complex rules such as "if not about legal advice, then refuse" (Figure 3a), a capability absent from prior steering methods.

3. **Selective refusal results are quantitatively strong.** CAST increases harmful refusal rates substantially (e.g., from 19.3% to 83.3% on Hermes 2 Pro, Table 2) while keeping harmless refusal rates low (e.g., 1.0% to 2.4%), yielding high discrepancy scores (88.5 for Qwen 1.5 Chat) that match or exceed reference safety-aligned models.

4. **Generalization to unseen categories during domain constraining.** When constraining to a target domain, CAST's effectiveness extends to unseen harm categories not included in training (Figure 3b), with a principled explanation relating effectiveness to semantic distinctiveness (Figure 3c).

5. **Efficiency properties are demonstrated.** Saturation (performance plateaus quickly with data volume) and linear time scaling (Figure 4) are shown, supporting the method's practicality.

6. **Broad model validation.** CAST is evaluated on nine models (1.8B–32B) with diverse post-training approaches (SFT, DPO, RLHF, merged models), supporting generality.

## Weaknesses

### Fatal
None.

### Major

1. **Refusal rate metric is not operationalized.** The paper's central quantitative results (Figures 1, 2, Table 1, all pie charts) report "refusal rate" without ever specifying how refusal is detected in model outputs. Is it a string match for refusal prefixes? A classifier? Human annotation? The paper mentions using Sorry-Bench and Alpaca test sets (Section 4) but never describes the refusal detection mechanism. This is not a minor omission — it makes every refusal-rate number uninterpretable and the experiments non-reproducible. The authors must (a) specify the exact detection method, (b) report its accuracy if learned, and (c) verify it works on the specific models evaluated.

2. **Missing comparison against the obvious baseline: classifier-gated activation steering.** The central claim is that CAST enables *context-dependent* control. A straightforward alternative is: train a binary classifier (e.g., logistic regression on hidden states from the same contrastive data) to detect the condition, then gate a standard refusal vector with its output. This achieves the same gating behavior with comparable overhead, and the gating signal is learned from the same data. CAST's condition detection *is* effectively a binary classifier living in activation space. The paper must either (a) empirically compare against this baseline to show CAST is competitive or superior, or (b) provide a principled argument for why the unified vector representation matters beyond implementation convenience. Currently the framing risks being read as "we reimplemented a classifier in activation space," which undercuts the novelty claim. The prompting baseline in Figure 3c is a much weaker comparison than a learned classifier.

### Minor

1. **The use of $\tanh$ is introduced without justification or ablation.** Equation (Section 3) defines the condition check as $f(\text{sim}(\mathbf{h}, \text{proj}_{\mathbf{c}} \mathbf{h}))$, but line 159 states "In practice, we apply a non-linear transformation $\text{sim}(\mathbf{h}, \tanh(\text{proj}_{\mathbf{c}} \mathbf{h}))$ for more predictable behavior" with no further explanation, ablation, or analysis of what the $\tanh$ changes. Since this is part of the core method, it needs justification.

2. **Choice of $\text{sim}(\mathbf{h}, \text{proj}_{\mathbf{c}} \mathbf{h})$ vs. a more direct similarity is unexplained.** As the reviewer correctly notes, $\text{sim}(\mathbf{h}, \text{proj}_{\mathbf{c}} \mathbf{h}) = |\cos(\mathbf{h}, \mathbf{c})|$, which discards the sign of $\cos(\mathbf{h}, \mathbf{c})$. Using $\text{sim}(\mathbf{h}, \mathbf{c})$ directly would preserve sign information. The paper should explain why the projection formulation is preferable, or at minimum note that using $\text{sim}(\mathbf{h}, \mathbf{c})$ is a natural alternative. (Note: the duality property still works with non-negative values — the reviewer's claim that this "seems at odds" with direction flipping is incorrect, as partitioning $[0,1]$ by a threshold still yields complements.)

3. **Hyperparameter sensitivity is not discussed.** The grid search for optimal threshold $\theta$ and layer is described as the most time-intensive step, but the paper reports no analysis of how sensitive results are to these choices, nor whether the selected settings generalize across test splits. For a method whose deployment depends on hyperparameter tuning, this omission limits practical guidance.

4. **Vanilla AST refusal rates are not reported in Table 1.** The bar chart in Figure 1 shows vanilla AST indiscriminately increasing refusal, but Table 1 only reports CAST and reference models. Including vanilla AST numbers for the same models in Table 1 would make the selective refusal claim more concretely verifiable at a glance.

### Trivial
None.

## Nice-to-Haves

- The saturation property (Figure 4a) is demonstrated on only three models; additional data points would strengthen the claim.
- An ablation comparing $\text{sim}(\mathbf{h}, \text{proj}_{\mathbf{c}} \mathbf{h})$ vs. $\text{sim}(\mathbf{h}, \mathbf{c})$ vs. $\text{sim}(\mathbf{h}, \tanh(\text{proj}_{\mathbf{c}} \mathbf{h}))$ would resolve the methodological ambiguity.
- The paper could discuss whether the condition vectors from different layers capture semantically redundant or complementary information.

## Removed Points

These points from the reviewer were evaluated against the paper and are flagged for removal with brief justification:

- **"$\text{sim}(\mathbf{h}, \text{proj}_{\mathbf{c}} \mathbf{h})$ = $|\cos(\mathbf{h},\mathbf{c})|$ — this loses directional information, which seems at odds with later discussion of flipping the comparison direction."** Removed because this misunderstands the duality property. Flipping $> \theta$ to $< \theta$ on a $[0,1]$-valued similarity still partitions the complement set. The duality claim is mathematically valid regardless of the absolute value. The underlying concern about *why* the projection formulation is used instead of a direct similarity is retained as Minor Weakness #2.

- **"The comparison of CAST models against LLaMA 3.1 Inst and LLaMA 2 Chat as 'references' in Table 1 is not informative because the base models differ."** Removed because the table caption explicitly labels these as "References show how the top safety-aligned models would behave on the same test set" — they are not presented as matched comparisons but as external reference points. The table also includes arrows showing change from each model's own base, which is the relevant within-model comparison. The separate request for vanilla AST numbers in Table 1 is retained as Minor Weakness #4.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Define the refusal detection metric explicitly.** For every result reporting refusal rate, specify the detection method (exact string match? regex? classifier?), its accuracy on held-out data, and whether the same method works across all evaluated models (which have different refusal phrasing styles).

2. **Add a classifier-based gating baseline.** Using the same contrastive data, train a logistic regression classifier on the hidden states at the same layers used for condition detection. Gate the refusal vector using this classifier's output with an analogous threshold. Report the harmful/harmless refusal rates and discrepancy scores alongside CAST's. This directly addresses whether CAST's unified representation has advantages over a modular approach.

3. **Clarify the condition detection mathematics.** Either justify why $\text{sim}(\mathbf{h}, \text{proj}_{\mathbf{c}} \mathbf{h})$ is preferable to $\text{sim}(\mathbf{h}, \mathbf{c})$, or switch to the more direct formulation. Provide an ablation for the $\tanh$ transformation.

4. **Add vanilla AST numbers to Table 1** for the same models, enabling a direct comparison of CAST vs. unconditional activation steering in the same table.

## Score and Decision

The paper presents a well-motivated extension to activation steering with a clear idea and broad experimental coverage across nine models. The qualitative demonstrations and quantitative results suggest the method is effective. However, two issues prevent acceptance in the current form: (1) the refusal rate metric — the paper's primary quantitative evaluation criterion — is never operationalized, making the core results uninterpretable and non-reproducible; (2) the absence of a comparison against classifier-gated activation steering, the most natural alternative baseline, undercuts the novelty claim. These are significant but addressable. I recommend rejection with strong encouragement to resubmit after resolving these issues.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>