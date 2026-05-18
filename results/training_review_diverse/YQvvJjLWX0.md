Now I have all the information I need to carefully verify each reviewer claim against the paper. Let me produce the consolidated review.

## Summary

The paper proposes Semantic Entropy Probes (SEPs), linear logistic regression models trained on LLM hidden states to predict semantic entropy (SE). SEPs offer a middle ground: they are cheaper than sampling-based SE (requiring only a single forward pass at test time) while generalizing better out-of-distribution than probes trained directly on accuracy labels. The paper provides extensive experiments across 5 models, 4 datasets, and both short- and long-form generation settings, showing that SEPs achieve AUROC values of 0.7–0.95 for predicting SE and consistently outperform accuracy probes in OOD generalization (+2.2 to +10.5 AUROC).

## Strengths

1. **Well-motivated and cleanly designed method.** Using SE (a model-internal uncertainty measure) as a supervision signal for probes rather than accuracy labels (an external, noisy signal) is intuitively appealing and is supported by the results (§§4, 7). SEPs require no ground-truth accuracy labels for training, solving a practical bottleneck of prior probing approaches.

2. **Strong empirical support for SEP efficacy across configurations.** SEPs achieve AUROC values of 0.7–0.95 for predicting binarized SE across models (Llama-2-7B/70B, Mistral-7B, Phi-3, Llama-3-70B) and tasks (TriviaQA, SQuAD, BioASQ, NQ Open) in both short- and long-form generation settings (§6, Figs. 2–3, Table of long results). The results hold across mid-to-late layers and for both SLT and TBG token positions.

3. **Consistent OOD generalization advantage over accuracy probes.** The leave-one-dataset-out evaluation shows SEPs outperform accuracy probes by margins of +7.7 (Llama-2-7B), +10.5 (Mistral-7B), +9.9 (Phi-3), +7.9 (Llama-2-70B) in short-form, and +6.2 (Llama-3-70B) in long-form (§7, Table 2, Figs. 4, 6). Per-layer plots confirm this advantage holds across almost all layers, not just cherry-picked ones.

4. **TBG results are a notable finding.** The demonstration that SE can be predicted from hidden states *before generation begins* (Fig. 3) is a clean result with practical implications — uncertainty quantification in a single forward pass with no generation needed (§6).

5. **Counterfactual context-addition experiment provides causal evidence.** Adding context to TriviaQA questions shifts the SEP's predicted high-SE probability from ~0.9 to ~0.5, consistent with the drop in ground-truth SE from 1.84 to 0.50 (Fig. 5). This confirms SEPs capture genuine uncertainty rather than spurious correlations.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **OOD evaluation is limited to QA datasets with similar structure.** All four tasks (TriviaQA, SQuAD, BioASQ, NQ Open) are extractive or short-answer QA datasets with similar question formats. The "leave-one-dataset-out" setup tests generalization across knowledge domains but not across fundamentally different task types (e.g., summarization faithfulness, dialogue, biography generation with FactScore). The paper's claim that SEPs are "the best choice for cost-effective uncertainty quantification in LLMs, especially if the distribution of the query data is unknown" (§7) is partially overclaimed — the evidence supports this claim for QA-like distributions but does not demonstrate it for genuinely different task formats. The paper would be strengthened by acknowledging this limitation more explicitly or adding at least one non-QA OOD evaluation.

2. **Limited comparison to other probing methods despite SOTA claims.** The paper claims "a new state-of-the-art for cost-efficient hallucination detection" (§1) but the probe baselines consist only of accuracy-supervised probes. Other probing-based approaches — such as Burns et al.'s unsupervised CCAP direction or Marks/Azaria truthfulness directions — are cited in related work (§2) but not included as experimental baselines. While the paper's core comparison (SE supervision vs. accuracy supervision) is clean and internally consistent, the SOTA claim would carry more weight with a broader comparison to other probe designs. This is a gap the authors could address without changing the paper's structure.

3. **Layer selection for aggregated results is deferred to the appendix.** The main text reports aggregated results using "a representative set of high-performing layers for both probe types" with a reference to the appendix (§7). While the per-layer plots (e.g., Fig. 4) convincingly show that the OOD advantage is robust across layers, the exact procedure for selecting layers deserves a brief description in the main text for reproducibility. (Note: this is a minor presentation issue since the appendix exists in the original submission.)

### Trivial

- None beyond the procedural clarification above.

## Nice-to-Haves

- A regression-based variant of SEPs (predicting continuous SE rather than binarized SE) could be compared on the same AUROC metric by thresholding post-hoc, avoiding any concern about the binarization threshold (§4). The authors' current choice is defensible, but this would be a clean ablation.
- A breakdown of SEP failure modes (e.g., by question type or SE level) would help users understand when the method is safe to deploy.
- A fixed decision rule for the SE threshold (e.g., 80th percentile of training SE) would test sensitivity to the optimized threshold in Eq. 5.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Layer-selection procedure underspecified (Harsh Critic, Issue 1):** The paper references `\cref{app:exp_details}` for the layer selection procedure. The appendix was stripped by the parser but exists in the original submission. Moreover, the per-layer plots (Fig. 4 for Llama-2-7B, and referenced Fig. for Mistral-7B) already demonstrate that the OOD advantage of SEPs holds across most layers, not just a selected subset, making the robustness concern empirically addressed.
  
- **Binarization as a limiting choice (Harsh Critic, Other Observations):** The paper explicitly motivates binarization (§4): the ultimate goal is binary hallucination detection, and binarization enables a direct comparison to binary accuracy probes. The authors also note that logistic regression outputs probabilities, preserving fine-grained signal. This is a reasoned design choice, not a flaw.
  
- **Context-addition experiment is qualitative (Harsh Critic, Other Observations):** The paper reports specific quantitative values: p(high SE) shifts from ~0.9 to ~0.5, ground-truth SE from 1.84 to 0.50, accuracy from 26% to 78% (§6). This goes beyond a purely qualitative description.

- **Demand for non-QA OOD task (Harsh Critic, Strengthening section):** While useful, adding a summarization or biography-generation evaluation would substantially expand the paper's scope beyond what is standard for a conference submission. The paper already evaluates across 4 datasets × 2 generation settings × 5 models. The existing OOD setting — leave-one-dataset-out among diverse knowledge domains — is a meaningful and widely used protocol.

- **Demand for feature attribution of accuracy probes (Harsh Critic, Strengthening section):** This is a nice research direction but well beyond what is needed for a paper presenting a new method.

## Novel Insights

Beyond the paper's own contributions: The reviews collectively surface an interesting tension — SEPs are presented as an *unsupervised* method (no accuracy labels needed), yet their training requires access to SE computed from multiple generations (N=10). This hybrid character (unsupervised with respect to ground-truth labels, but requiring supervised training on model-derived SE labels) is worth explicit discussion. It means SEPs are "unsupervised" in a different sense than Burns et al. — they don't need human labels, but they do need a multi-sample SE computation for training data creation. This distinction is blurry in the paper's terminology and could be sharpened.

## Suggestions

1. Temper the claim "best choice for cost-effective uncertainty quantification... especially if the distribution of the query data is unknown" to reflect that the OOD evaluation covers QA datasets. Something like "best choice for cost-effective hallucination detection on question-answering tasks, especially when generalizing across knowledge domains" would be more precise.

2. Add at least one comparison to another probing baseline (e.g., a probe trained on the CCAP direction or a truthfulness direction) to support the SOTA claim, or qualify the claim to reference only accuracy-supervised probes.

3. Include a brief description of the layer selection procedure in the main text (e.g., "we selected layers that achieved peak AUROC on in-distribution validation data for each probe type independently").

4. Consider a fixed-threshold variant of the binarization (e.g., always using median or 80th percentile of training SE) to test sensitivity to the optimized split in Eq. 5.

## Score and Decision

The paper makes a genuine contribution: it identifies a useful supervision signal (SE) for probing, demonstrates that this choice yields better OOD generalization than accuracy supervision, and provides thorough experimental validation across models and settings. The weaknesses are limited in scope — the OOD evaluation is confined to QA datasets, and the probe baseline comparison could be broader — but neither undermines the core results. The paper is well-written, the method is practical and deployable, and the main findings are clearly supported.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>