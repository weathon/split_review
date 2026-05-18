Now I have all the information needed. Let me construct the consolidated review.

---

## Summary

The paper introduces iReVa, a model editing method that inserts explicit key-value adaptors into the MLP blocks of GPT-like Transformer models. Each edit corresponds to an inserted key-value neuron, enabling traceable storage and retrieval (each neuron can be located, inhibited, or removed). The method initializes knowledge neurons from cached hidden states and fine-tunes them with a multi-objective loss (edit success, reconstruction regularity, and irrelevance loss). During inference, a max-pooling mechanism activates only the best-matching neuron. Experiments on GPT2-XL, GPT2-Large, GPT-NEO-2.7B, and GPT-J-6B show strong edit success (ES), paraphrase generalization (PS), and specificity (NS), with margins of ~9% and ~6% average score improvement over baselines on zsRE-10K and PARAREL-10K respectively. The paper also demonstrates a knowledge withdrawal test where individual edits can be removed by inhibiting their corresponding neurons, achieving near-perfect retrieval success and consistency.

## Strengths

- **Traceable knowledge withdrawal demonstrated empirically**: iReVa achieves Retrieve Success of 98.76 and Consistency of 99.13 on zsRE-10K (Table 2) by inhibiting specific inserted neurons. This capability is genuinely novel — most batch-editing methods cannot trace which parameters correspond to which edit, making withdrawal impossible or unreliable. The paper validates this with quantitative metrics rather than just claiming the ability.

- **Substantial and consistent performance gains across datasets and model scales**: On zsRE-10K, iReVa achieves average Score 96.95 vs. best baseline (FT) at 88.33; on PARAREL-10K, 93.95 vs. FT at 88.49 (Table 1). These margins derive from simultaneously achieving near-perfect Edit Success (~100%) and high Specificity (~99%), a combination no baseline matches. The advantage holds across GPT2-Large, GPT-NEO-2.7B, and GPT-J-6B (Table 4), and across edit quantities from 500 to 10,000 (Figure 3), where ROME degrades sharply and MEMIT underperforms throughout.

- **Well-designed architectural components validated by ablation**: The activation function with margin θ (GeLU(x−θ)) and inference-time max-pooling are shown to be critical: removing the activation drops NS from 98.95 to 60.02, and removing max-pooling collapses all three metrics (Table 3). The ablations cleanly separate the contribution of each design choice and confirm that specificity is not coincidental.

- **Parameter-efficient design with clear practical costs**: For 10K edits on GPT2-XL (1.5B parameters), the adaptor adds only 0.08B parameters (~5% overhead). Training completes in 7.5 hours (fine-tuning) or 1.6 hours (without fine-tuning) on a single A800 GPU, compared to 9.16 hours for ROME. These numbers are reported transparently and support the method's practicality.

## Weaknesses

### Fatal

None.

### Major

- **Unclear fairness of baseline comparison due to different data preprocessing.** The paper states (Section 5.4) that it "pre-process the edit input-output pairs differently from previous studies": multi-token targets are decomposed into multiple data pairs by greedily appending previous tokens. This fundamentally changes the task structure — what was one edit with a multi-token target becomes multiple consecutive sub-edits, each getting its own key-value neuron. The paper then says baselines are re-implemented "using the same configuration reported in existing studies," but does **not** state whether those baselines received the same preprocessed data or the original format. If baselines were evaluated in their standard single-update-per-example setting while iReVa effectively receives more neuron allocations per original edit, the comparison is asymmetric and the reported 9%/6% margins cannot be trusted. This is the single most important issue to resolve. The authors must clarify whether all methods received the same input data and, if not, re-run experiments under fair conditions.

### Minor

- **Training-inference discrepancy in neuron activation is acknowledged but not analyzed.** During training, all inserted key-value neurons are active (subject to the activation margin), and gradients flow through all of them. During inference, a hard max-pooling/argmax selects only the single best-matching key. The paper acknowledges this mismatch (Section 4.3) and the ablation (Table 3) shows max-pooling is essential, but provides no analysis of how often the correct key is selected, how similarity scores are distributed, or what happens when two edits share similar hidden states (e.g., paraphrases). While the method works empirically, this design choice limits understanding of its robustness on noisier or more densely edited datasets. The ablation shows NS drops from ~99.96 to ~62.54 without max-pooling — a 37-point collapse — which suggests the training objective does not enforce that keys remain discriminative when operating simultaneously.

- **Withdrawal evaluation does not test cross-edit interference.** The withdrawal test (Section 6.2) checks whether removing a neuron reverts the edited input (Consistency) and whether outputs change (Retrieve Success). However, it does not test whether *other edits* remain intact after removal of one neuron. Because inference uses max-pooling over all inserted keys, removing one neuron changes the pool of candidates — potentially altering which key is selected for other inputs. The paper's claim of "almost perfect" withdrawal is only validated on the narrowest possible metrics and does not verify that the remaining edits are unaffected.

- **Contradiction between claimed scope and stated limitation.** The introduction (Contribution 1) claims iReVa is "compatible with most LMs," but the Limitation section (Section 7.b) states "iReVa can be only applied on GPT-like models and generation task." These statements are contradictory and the paper should correct the overclaim in the introduction.

- **Time complexity formula appears incorrect.** The paper claims inference complexity O(l·d₁²·n) (Section 6.3), but the adaptor computation (key lookup \hat{K}^T i, activation, value lookup \hat{V}^T · result) is O(l·d₁·n) per the stated dimensions (i ∈ ℝ^{1×d₁}, \hat{K} ∈ ℝ^{\dot{d}_1×n}, \hat{V} ∈ ℝ^{n×d₁}). The extra factor of d₁ appears to conflate the key-value lookup with a full matrix multiplication. This should be corrected.

- **Key notation ambiguities hinder reproducibility.** Several dimension variables (d₁, d₂, \dot{d}_1, \bar{d}_1, \bar{n}, n) are introduced without clear relationships (Section 4, Section 4.3). The matrices appear as \bar{K}∈ℝ^{d₁×\bar{n}} and \bar{V}∈ℝ^{n×\bar{d}_1} in Section 4, then as \hat{K}∈ℝ^{\bar{d}_1×n} in Section 4.3 — these notational shifts make it difficult to verify parameter counts. In Equation 10, x_i (previously used for the edit input sequence) is used for a hidden state in \mathcal{L}_{irr}, which is inconsistent.

- **"Gradient-free method" for GPT-NEO-2.7B is unexplained.** The paper says it "applies gradient-free method on GPT-NEO-2.7B" (Section 5.4) but never specifies what this method is, how it differs from the training procedure used for other models, or whether the results on that model (Table 4) are comparable to those from the full training procedure.

- **Hyperparameters for non-GPT2-XL models are not reported.** Hyperparameters a, b, α, θ are given only for GPT2-XL. For GPT2-Large, GPT-NEO-2.7B, and GPT-J-6B, the paper does not state whether these were tuned separately or reused. The learning rate for GPT-J-6B is given, but not the other hyperparameters.

### Trivial

- No standard deviations or confidence intervals are reported for main results (Table 1). Given that model editing methods can be sensitive to initialization and data ordering, single-run results are the norm in this field but variance reporting would strengthen the paper.
- The PARAREL-10K construction selects only sentences ending with "[MASK]" — the paper should report what fraction of PARAREL was retained and discuss potential selection bias.

## Nice-to-Haves

- A histogram or analysis of key-matching scores for in-scope vs. out-of-scope inputs would strengthen the traceability claim and help understand the max-pooling behavior.
- Testing withdrawal with verification that all other edits remain intact (not just the withdrawn one) would make the withdrawal evaluation complete.
- Reporting results on the full zsRE dataset (19,086 examples) rather than a 10K subset would improve comparability with prior work.

## Removed Points

The following points from the reviewers were removed or downgraded per the filtering rules:

- **Harsh Critic Point 3 ("first attempt" claim overstated)**: The paper qualifies its claim ("Most existing methods can't perform the withdrawal test... stream-fashion methods like GRACE may encounter the forgetting challenge") and is not asserting absolute novelty against all possible modular-editing methods — it is stating that no existing method *demonstrates* withdrawal quantitatively. This is defensible. The substantive part (missing cross-edit interference test) is kept in Minor.
- **Criticism that T-Patcher was excluded**: The paper provides a valid architectural reason (T-Patcher is encoder-only, inapplicable to decoder-only GPT models). This is not a missing-baseline issue.
- **Request for larger human studies or multi-seed runs at industrial scale**: These are impractically expensive for an academic submission. The single-run reporting at this scale is standard for the field.
- **Generic formatting/style nitpicks and "typos"**: These are parser artifacts, not author errors.
- **Missing related works / missing appendix content**: The parser strips supplementary material; the original submission likely contains it.

## Novel Insights

The most striking finding is how the interaction between the activation margin (θ) and inference-time max-pooling creates a functional "key routing" mechanism despite the training-inference mismatch. During training, all neurons receive gradient signal, enabling convergence; during inference, argmax selects the single best match, effectively implementing a sparse retrieval scheme. The ablation shows this design is not optional — both components are essential — which suggests the method's success relies on a carefully balanced tension between training all neurons jointly and picking only one at test time. This is an interesting architectural lesson for traceable editing beyond the specific results.

## Suggestions

1. **Clarify the data preprocessing fairness issue immediately.** State explicitly whether baselines received the same preprocessed (multi-token decomposed) data or the original format. If they did not, re-run experiments with matched preprocessing and update Table 1, or provide a controlled experiment where all methods use the same format.

2. **Add cross-edit interference analysis after withdrawal.** Test whether removing one edit's neuron changes the model's predictions on other edited inputs (beyond simply verifying the removed edit is gone).

3. **Correct the time complexity formula** from O(l·d₁²·n) to O(l·d₁·n) and clean up the notation to use consistent dimension variables throughout.

4. **Reconcile the abstract/intro's "compatible with most LMs" with the limitation section's "only applied on GPT-like models."**

5. **Describe the "gradient-free method" used for GPT-NEO-2.7B** and report whether all hyperparameters (a, b, α, θ) were reused from GPT2-XL or tuned separately for each model.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>