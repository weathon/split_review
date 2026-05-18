Now I have thoroughly read the paper and verified the reviewer claims against the source text. Let me produce the final consolidated review.

---

## Summary

This paper proposes O³, a framework for continual machine unlearning on LLMs that operates *without access to retained data*. The framework combines (1) orthogonal-regularized LoRA adapters that disentangle parameters across sequential unlearning requests, and (2) an OOD detector (contrastive entropy representation learning + glocal-aware scoring + OCSVM) that measures input similarity to each unlearning distribution, enabling soft-weighted loading of unlearning adapters at inference. Experiments on question answering (ScienceQA), fictitious knowledge generation (TOFU), and intent classification (CLINC150) show O³ outperforms baselines that *are* given retained data, on both unlearning effectiveness and utility preservation.

## Strengths

1. **First framework for LLM continual unlearning without retained data.** The paper identifies and directly tackles a practical gap: existing LLM unlearning methods assume access to retained data (often the original training set), which is unrealistic due to privacy and copyright expiration. O³'s two-module design (orthogonal LoRA + OOD detector) uses only the unlearning data for each request. This claim is supported across three tasks (Figures 2–4, Tables 2–3) where O³ achieves the best Unlearning-Utility Ratio (U²R) while baselines that require retained data either fail in utility or unlearning.

2. **Orthogonal regularization across sequential LoRA adapters is validated by ablation.** The orthogonal loss (Eq. 6, \(\mathcal{L}_{\mathrm{Orth}}^t = \|(A^{t-1})^\top A^t\|^2\)) is a clean mechanism for reducing interference between requests. Table 5 shows that removing this loss (\(\lambda=0\)) degrades both unlearning effectiveness (S.U. degrades from 27.00 to 29.60 on ScienceQA) and utility preservation (R.D. drops from 57.80 to 55.50), confirming the design's necessity.

3. **Extensive empirical validation across diverse tasks and metrics.** The paper evaluates on three substantively different tasks (multiple-choice QA, generative QA, intent classification) using sample-level unlearning, distribution-level unlearning, retained distribution, and two utility benchmarks per task. O³ consistently achieves the highest U²R across all settings (Figure 2), often by a large margin (e.g., U²R of 4.70 vs. next best 2.86 in QA).

4. **High data and parameter efficiency.** Table 1 shows O³ uses approximately half the training data of baselines (no retained data needed) and only 20M trainable parameters (LoRA) versus 6,758M for full-parameter baselines. This is a practical strength for deployment.

5. **Systematic ablation study validates design choices.** Tables 4–6 ablate the contrastive entropy loss (vs. SimCLR/MoCo), scoring mechanism (Mahalanobis vs. cosine vs. both), layer aggregation, orthogonal loss coefficient, and soft-weighted inference. Each component is shown to contribute positively, providing clear evidence for the proposed design.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

1. **Orthogonal regularization only enforces pairwise orthogonality with the immediate previous request.** The loss \(\mathcal{L}_{\mathrm{Orth}}^t = \|(A^{t-1})^\top A^t\|^2\) does not explicitly enforce orthogonality with requests \(t-2, t-3, \dots\). While the experiments span up to 3–4 requests and show good results, the paper overclaims "disentanglement among different unlearning requests" without addressing whether performance degrades with longer request sequences (e.g., 10+ requests). This is a scope limitation that should be acknowledged and ideally tested.

2. **The "5.1% additional computation overhead" claim is unsupported.** The paper asserts "additional inference computation overhead is only 5.1%" (line 181) but provides no derivation, wall-clock time measurements, or breakdown of time spent on the LLM forward pass versus OOD detector forward passes versus OCSVM scoring. Given that each OOD detector uses a RoBERTa-large backbone, and inference requires running \(T\) such detectors per input, this number seems suspect without supporting evidence. The authors should provide a detailed latency/memory analysis.

3. **The OOD detector evaluation is narrow for the claimed role.** Table 4 only evaluates AUROC on the two unlearning tasks themselves (ScienceQA and TOFU), with ID being the unlearning distribution and OOD being the retained/utility distributions. While this is sufficient for the paper's specific use case, it leaves open the question of whether the detector would generalize to truly unrelated inputs (e.g., random web text). For a component that determines whether to apply unlearning adapters at inference, more adverse testing (what happens with out-of-domain inputs not close to any training distribution?) would strengthen confidence.

4. **Unaddressed failure modes of the OOD gating mechanism.** The paper does not discuss what happens when the OOD detector produces false positives (applies unlearning LoRA to normal inputs, degrading utility) or false negatives (fails to apply LoRA to unlearning inputs, defeating the purpose). The soft-weighted mechanism mitigates this somewhat, but quantitative bounds or analysis of detector calibration would be helpful.

5. **Several claims are asserted without evidence.** (a) The claim that token-level SSL tasks like MLM and SimCSE are "far less effective" for OOD detection (Section 3.2) is never empirically supported—this is precisely what the ablation in Table 4 should compare (the paper compares its contrastive entropy against SimCLR and MoCo, not against MLM or SimCSE directly). (b) GradAsc is omitted from Figure 3 because it "failed to generate meaningful answers" without defining what constitutes "meaningful." These are small but avoidable presentation gaps.

### Trivial

- The preliminary problem formulation (Section 2) presents the traditional continual unlearning objectives as two comma-separated expressions (min and max of mutual information terms) without explicit conjunction, making the notation slightly ambiguous.
- \(\mathcal{P}_{\mathcal{X}}^{\mathrm{O}}\) in Eq. 2 is described only as "other distributions" without formal definition; this is fine for a background section but could be clearer.

## Nice-to-Haves

- Evaluate with 5–10 sequential unlearning requests (even on a synthetic setup) to test whether the orthogonal regularization holds over longer sequences.
- Compare O₃ against baselines *without* retained data (currently baselines get retained data and O₃ doesn't), to further isolate the source of O₃'s advantage.
- Include an OOD detection baseline using the LoRA's own prediction confidence/logit difference as a lightweight alternative to the RoBERTa-based detector.
- Provide a formal derivation or measured breakdown of the claimed 5.1% inference overhead.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *Harsh Critic Issue 1 (problem definition is "garbled" and "nearly unintelligible")* — The garbled text ("continueaesnsttds...") is a PDF extraction artifact, not an author error. Per hard rules, such parser artifacts must be removed. The reviewer also misreads the retained distribution discussion: the paper clearly frames it as describing *traditional* approaches before stating that O³ departs from them. The mathematical expression, while awkwardly formatted (comma-separated min/max terms), is decipherable as two standard sub-objectives.
- *Harsh Critic statement about OOD detector novelty being lacking* — While the contrastive entropy loss shares structural similarity with existing contrastive losses, the paper's contribution is the overall *framework* (orthogonal LoRA + OOD gating + soft-weighted inference), not a claimed breakthrough in representation learning. Critiquing the loss for not being "fundamentally new" evaluates a component against an unrealistically high bar. The ablation shows it outperforms SimCLR/MoCo alternatives, which is sufficient.
- *Harsh Critic claim about unfair experimental setup ("hard to attribute O³'s success to its core ideas")* — The reviewer acknowledges this comparison "is a legitimate comparison for demonstrating that O³ works without retained data." The asymmetry favors baselines (they get retained data) and the paper still beats them, which is a valid and intentionally strong demonstration. The ablation studies (Tables 4–6) already isolate the contributions of individual components. The reviewer's suggestion to drop retained data for baselines would only make baselines perform worse, adding no new information.

## Novel Insights

The most interesting observation that emerges across the reviews is the tension between the paper's framing ("continual unlearning without retained data") and the potential failure mode where the OOD detector itself requires unlearning data for training. This creates a subtle circularity: the method claims independence from retained data, but the OOD detector's ability to discriminate unlearning distributions from other distributions depends on the diversity of the unlearning data it was trained on. If the unlearning data for a given request is highly homogeneous, the detector's Gaussian + cosine similarity scoring may not generalize well to real-world inputs that fall between distributions. The paper does not explore this failure regime, which would be an interesting direction for follow-up work. None beyond the paper's own contributions.

## Suggestions

1. Add a latency/memory breakdown table to substantiate the 5.1% overhead claim. Measure wall-clock time for: (a) LLM forward pass, (b) T OOD detector forward passes, (c) OCSVM distance computation, and (d) soft-weight calculation.
2. Add a brief discussion of when orthogonal regularization might fail (long request sequences, highly similar unlearning distributions) and how the current design mitigates or does not mitigate these cases.
3. Include an adverse evaluation of the OOD detector on truly unrelated text (e.g., news articles, general web text) to demonstrate that it does not falsely trigger on inputs far from all training distributions.
4. Define "meaningful" when omitting a baseline from a plot (e.g., GradAsc in Figure 3) and justify the exclusion with a quantitative threshold.

## Score and Decision

**Originality**: The paper addresses an underexplored problem formulation (continual unlearning without retained data) and proposes a novel combination of existing techniques (LoRA + orthogonal regularization + OOD detection). The individual components are not groundbreaking, but the synthesis into a working framework for this specific setting is original.

**Importance**: High. Real-world LLM unlearning faces exactly the constraints the paper identifies: sequential requests and no access to original training data. A solution to this problem would have practical value.

**Claims support**: The core claims are supported by experiments across three tasks. The "best U²R" claim is consistently supported. The "works without retained data" claim is supported. Some secondary claims lack full evidence (e.g., OOD detector generalization, 5.1% overhead).

**Soundness**: The experimental design is sound. The evaluation metrics are appropriate (S.U., D.U., R.D., U.1., U.2., U²R). Baselines are reasonable state-of-the-art methods. Ablations are thorough. The main limitation is the narrow evaluation of the OOD detector and the unsupported 5.1% overhead claim.

**Clarity**: The paper is generally readable but has notation issues in the preliminaries and some vague claims. The main methodology (Sections 3.1–3.3) is clearly explained.

**Value**: The paper makes a solid empirical contribution that would be useful to practitioners working on LLM safety and unlearning.

The weaknesses identified are all minor — none threaten the paper's core claims. The orthogonal regularization limitation (only pairwise) is acknowledged by the experiments covering up to 4 requests. The 5.1% overhead claim needs verification but does not invalidate the contribution. The paper makes a genuine contribution to a timely and practical problem with clean empirical validation.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>