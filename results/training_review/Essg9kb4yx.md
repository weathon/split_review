Now I have thoroughly verified the reviewer claims against the paper. Let me produce the final consolidated review.

## Summary

This paper tackles the practical and underexplored problem of **continual unlearning for LLMs without access to retained data**. The authors propose **O³**, a framework combining (1) an orthogonal regularization loss on sequential LoRA updates to prevent interference across unlearning requests, and (2) an OOD detector (RoBERTa-large, trained with a novel contrastive entropy loss and glocal-aware scoring) to determine whether and how strongly to apply the unlearning LoRA at inference. Experiments across three tasks (ScienceQA, TOFU, CLINC150) and seven datasets show O³ achieves the best Unlearning-Utility Ratio (U²R) compared to seven baselines, while using only half the training data and <3% of the trainable parameters.

## Strengths

1. **Tackles a genuinely important and under-explored problem.** Continual unlearning without retained data is a realistic constraint (privacy, expired access, copyright), yet nearly all prior work assumes retained data is available. The paper formalizes this setting clearly in Section 2 and motivates why it matters. *(Evidence: Problem definition in Section 2; discussion of data access limitations in Section 1.)*

2. **Novel and well-motivated framework architecture.** The core idea — using an OOD detector trained purely on unlearning data to gate a single unlearning LoRA — is creative and principled. The contrastive entropy loss (Eq. 7) and glocal-aware scoring (combining Mahalanobis distance and cosine similarity per layer) are non-trivial technical contributions that collectively enable unsupervised OOD detection for text. *(Evidence: Ablation in Table 4 shows the full OOD detector achieves best AUROC; removing either distance or the contrastive loss degrades performance.)*

3. **Comprehensive evaluation across diverse tasks and strong empirical results.** The paper tests on three qualitatively different tasks (multiple-choice QA, generative QA, intent classification) with multiple utility datasets per task. O³ achieves the highest U²R across all settings and outperforms baselines on nearly every individual metric, despite using no retained data while baselines are given retained data. *(Evidence: Figure 2, Tables 2–3.)*

4. **Impressive data and parameter efficiency.** O³ uses roughly half the training data of baselines (no retained data) and only 20M trainable parameters via LoRA, compared to 6,758M for full fine-tuning baselines. Additional inference overhead is stated as 5.1%. *(Evidence: Table 1, line 181.)*

## Weaknesses

### Fatal
None.

### Major

1. **Max-weight inference conflates all unlearning requests.** At inference, the method computes a single scalar weight `w(x) = max{w(x)^1, ..., w(x)^T}` and applies it to the *entire accumulated* LoRA update: `h' = Wh + w(x)·ABh`. This means that an input similar to *any one* unlearning distribution triggers the contributions from *all* requests. Even with orthogonal A column spaces, the combined `ΔW = Σ A_t B_t` modifies the hidden state in ways that are not request-specific. The paper's claim that "the unlearning effectiveness of different requests does not interfere with each other" is not supported by this design, because the inference mechanism does not select which request's unlearning to apply — it loads everything or nothing. The method could still work in practice (the empirical results suggest it does), but the stated disentanglement claim is overstated given the inference design. *(Verified: Eq. 3 modification, line 149.)*

2. **Per-request unlearning persistence is not evaluated.** The paper reports S.U. and D.U. "at every unlearning request" but it is ambiguous whether these are cumulative over all seen unlearning data or per-request. Even if cumulative, this does not separately verify that request 1's unlearning persists after request 2, 3, etc. Without showing, e.g., accuracy on request 1's unlearning test set immediately after request 1, then again after request 2, the core claim of "continual unlearning without interference" is empirically incompletely supported. This is a structural gap because it is the central claim of the paper. *(Verified: The paper defines metrics globally in Section 4.1 and never states a per-request breakdown; the text and figures are ambiguous.)*

3. **The orthogonal regularization only constrains matrix A, ignoring the full `AB` effect.** The paper justifies ignoring B by calling it "linear weights of matrix A" (line 70–71), but this is not further analyzed or ablated. The effective update is `ABh`, and orthogonality of A's columns does not guarantee that the outputs `A_1 B_1 h` and `A_2 B_2 h` are disentangled in their effect on the hidden representation. An ablation using separate LoRAs per request (as suggested by the reviewer) would clarify whether the orthogonal loss is compensating for an artifact of the single-LoRA design or genuinely disentangling tasks. *(Verified: Eq. 4–6; line 70–71.)*

### Minor

1. **Ambiguous definition of "Retained Distribution" (R.D.) across tasks.** The paper defines R.D. as "the distribution most susceptible to unlearning requests" but does not concretely specify which data constitutes R.D. for each task. For ScienceQA (biology → physics → chemistry → economics), it is unclear whether R.D. is other ScienceQA domains or something else. For TOFU, the paper mentions "another dataset containing 400 samples" — it is not explicit whether this *is* the retained distribution. For CLINC150, R.D. is not defined at all. The baselines are said to be given "sufficient retained data" without quantity or source details. This ambiguity weakens interpretability of the R.D. metric reported in tables and figures. *(Verified: Section 4.1, line 166; ScienceQA/TOFU/CLINC150 descriptions in lines 160–162.)*

2. **OOD detector is only evaluated as binary (ID vs. OOD), not multi-request discrimination.** Table 4 reports AUROC for binary detection (unlearning data vs. other data). However, the method requires distinguishing which unlearning distribution a sample belongs to, since different requests may overlap semantically. Without per-request AUROC or a confusion matrix, it is unclear whether the detector can discriminate request 1's distribution from request 2's — the max-weight inference design relies on the detector's ability to flag *any* relevant distribution, but understanding false positive patterns across requests would inform the design. *(Verified: Table 4; no multi-request analysis present.)*

3. **Inference overhead of the OOD detector is unclearly reported.** The paper states "additional inference computation overhead is only 5.1" (line 181) without specifying whether this is a percentage, a factor multiplier, or an absolute value. Since the OOD detector uses a 355M-parameter RoBERTa-large model and one detector backbone is run per request (with LoRA adapters), the actual overhead is nontrivial and should be clearly specified and compared to baselines. *(Verified: line 181 — incomplete specification.)*

4. **Variance is not reported despite running three random seeds.** The paper states "All experiments are run repeatedly with three random seeds" (line 170) but no standard deviations or confidence intervals are shown in any table or figure. This makes it impossible to assess whether reported differences are statistically significant. *(Verified: line 170; no variance in Tables 2–6 or Figures 2–4.)*

### Trivial

- The paper contains several garbled passages from PDF extraction (e.g., line 29, 269) which are parser artifacts, not author errors.
- The scaling factor γ=1000 (Eq. 11) is used without justification for its specific value; the ablation only studies λ and ζ.

## Nice-to-Haves

- A baseline using **separate LoRAs per request** (one per unlearning task, selected by the OOD detector) would isolate the effect of the orthogonal regularization and clarify whether a single shared LoRA is beneficial or merely convenient.
- Sensitivity analysis of the Gaussian distribution assumption used in soft-weighting (Eq. 12–13) — e.g., comparing against a non-parametric alternative.
- Qualitative examples showing model outputs on unlearning data before/after O³ and on utility data, to illustrate the behavioral effect of the method.

## Removed Points

*These points were flagged for removal from the harsh critic's review; they are listed here for completeness but should not be weighed in the evaluation.*

- **Claim that contrastive entropy loss is not compared against standard contrastive losses (InfoNCE, SimCLR):** The paper *does* compare against SimCLR and MoCo in Table 4 ("Ours w/ SimCLR", "Ours w/ MoCo"). This criticism is factually incorrect. *(Removal reason: factually wrong.)*
- **Criticism about missing appendix content (proofs, extended experiments, dataset details):** The parser strips these sections. The original submission contains them. *(Removal reason: parser artifact.)*
- **Formatting/style nitpicks about specific notation or presentation choices:** Parser artifacts from PDF extraction, not author errors. *(Removal reason: formatting nitpick / parser artifact.)*

## Novel Insights

The most interesting unresolved question this paper surfaces is whether **gating a single shared adapter via OOD scores** is actually better than selecting among multiple specialized adapters. The orthogonal regularization on A matrices is an elegant idea, but the max-weight inference design means all accumulated knowledge is loaded simultaneously — the method does not selectively retrieve the right request's unlearning. This tension between the training-time disentanglement claim and the inference-time conflation is the paper's most significant open issue. The empirical success (strong U²R across three tasks) suggests the combined LoRA does not catastrophically degrade utility when applied to non-matching inputs, but the *mechanism* behind this robustness is unclear and warrants deeper investigation.

## Suggestions

1. Add per-request unlearning persistence curves: after each request, report S.U./D.U. on each prior request's data individually (not just cumulatively). This is the single most important missing experiment.
2. Add a baseline with separate LoRAs per request, selected by the OOD detector, to ablate the orthogonal regularization and single-LoRA design.
3. Clarify the retained distribution definition for all three tasks, state the quantity and source of retained data given to baselines, and report standard deviations across seeds.
4. Report multi-request OOD detection performance (per-request AUROC or confusion matrix) and analyze whether false positives are concentrated on semantically related distributions.
5. Clarify the inference overhead (is "5.1" a percentage or multiplier?) and discuss latency/memory trade-offs of running multiple RoBERTa-large detectors.

## Score and Decision

The paper tackles an important problem with a well-motivated and novel framework, backed by strong empirical results across diverse tasks. However, three structural issues prevent full acceptance: (a) the inference design (max-weight over all requests) does not support the claimed per-request disentanglement, (b) the central claim of continual unlearning without interference is not backed by per-request persistence measurements, and (c) the orthogonal regularization's justification ignores the B matrix without analysis. These issues require new experiments (not just text revisions) to resolve. The ideas are promising enough that a substantially revised version could be strong, but in its current form the contribution is partially overstated relative to the evidence.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>