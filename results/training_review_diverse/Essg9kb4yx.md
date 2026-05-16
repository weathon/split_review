Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper tackles the important and underexplored problem of continual LLM unlearning without retained data. It proposes the O³ framework combining (1) orthogonal LoRA adapters that regularize successive unlearning requests to have orthogonal parameter spaces, and (2) an OOD detector (trained via contrastive entropy + MLM losses with a glocal-aware scoring mechanism) that measures whether an input resembles previously unlearned data. During inference, the OOD similarity score governs a soft weight that determines how strongly the unlearning LoRA is applied. Experiments across ScienceQA, TOFU, and CLINC150 show O³ consistently achieves the best balance between unlearning effectiveness and utility preservation compared to baselines that all use retained data.

## Strengths

- **Novel problem framing and practical motivation.** The paper identifies a genuine gap in existing unlearning work — continual streams of requests and no retained data — and proposes a coherent framework that addresses both challenges. This is a meaningful contribution to the LLM safety literature.

- **Orthogonal LoRA design is effective.** The orthogonal regularization loss (Eq. 5–6) provides a principled way to reduce interference between successive unlearning tasks in LoRA parameter space. The ablation (Table 5) confirms that adding the orthogonal loss (\(\lambda>0\)) improves both unlearning effectiveness and retained-distribution utility. The argument that regularizing A suffices (since outputs of AB lie in col(A)) is mathematically sound.

- **Strong and consistent empirical results.** The U²R metric (Figure 2) shows O³ achieves the highest balance across all three tasks, often by a wide margin, despite using zero retained data while all baselines use retained data. This is the most important evidence that the framework works.

- **OOD detector works without labels or retained data.** The detection system (contrastive entropy + Mahalanobis/cosine scoring + OCSVM) achieves AUROC of 0.84–0.99 (Table 4), substantially outperforming prior OOD methods (MDF, Agg). Each component contributes meaningfully, as shown by ablation.

- **Thorough ablation studies.** Tables 4, 5, and 6 systematically isolate contributions of individual components (contrastive entropy loss, scoring terms, orthogonal loss, soft-weighting factor), confirming that each piece is necessary.

## Weaknesses

### Fatal
None.

### Major

1. **Orthogonal regularization only enforces pairwise consecutive disentanglement, not cumulative separation across all requests.**  
   The loss in Eq. 6 (\(\mathcal{L}_{\text{Orth}}^t = \|(A^{t-1})^\top A^t\|^2\)) only requires \(A^t\) to be orthogonal to the immediately preceding \(A^{t-1}\). Because orthogonality is not transitive, a later task (e.g., \(t=3\)) could overlap with an earlier one (\(t=1\)) even if it is orthogonal to \(t=2\). The paper claims "disentanglement of parameter space across different unlearning requests" and "unlearning effectiveness of different requests does not interfere with each other" (Section 1, line 14), which implies all-pairs non-interference. No argument or experiment is provided to justify that pairwise consecutive orthogonality suffices for cumulative separation. This is a structural gap between the claimed guarantee and what the loss actually enforces. **(This weakness is reflected in the paper at lines 70–82 — the orthogonal loss definition only references \(A^{t-1}\) and \(A^t\), with no mechanism for earlier requests.)**

2. **Parameter-efficiency claim is overstated.**  
   Table 1 reports 20 M trainable parameters for O³ vs. 6,758 M for baselines. However, this 20 M figure counts only the LoRA parameters and excludes the OOD detector backbone (RoBERTa-large, ~355 M parameters), which is also trained at each request using \(\mathcal{L}_{\text{CEL}} + \mathcal{L}_{\text{MLM}}\) (Section 3.2, lines 103–104). While the detector is a separate module and its total is still far smaller than full-model fine-tuning, omitting it from the headline number creates a misleading comparison. The paper should either report total trainable parameters across both modules or clearly state what is included in the count. **(This is evident from line 170 — "The used OOD detector backbone is Roberta-large" — and lines 103–104 where the backbone is trained per request.)**

### Minor

1. **No variance or statistical significance reported for main results.**  
   The paper states "All experiments are run repeatedly with three random seeds" (line 170), yet Tables 2 and 3 report single numbers without standard deviations or confidence intervals, and Figures 2–4 show no error bars. Several comparisons are close (e.g., Table 2, S.U. for request 3: O³ 2.95 vs. PO 3.45), making it impossible to assess whether differences are reliable. This is the most readily fixable weakness and would substantially strengthen the paper's evidentiary weight.

2. **Missing baselines that address continual learning in the unlearning context.**  
   The compared baselines (GradAsc, GradDif, EUL, PO, NPO, SOGD, SOPO) are all single-request unlearning methods applied sequentially. They are not designed to handle task interference or catastrophic forgetting of prior unlearning. Including approaches that explicitly address continual learning — e.g., elastic weight consolidation (EWC), memory-aware synapses, or replay of previous unlearning data — would make the comparison fairer and better isolate the source of O³'s advantage.

3. **Privacy implications of the OOD detector are not discussed.**  
   The OOD detector is trained directly on the data to be unlearned and stores score vectors from that data (line 130–131: "store all these vectors as we cannot access the unlearning data after the unlearning"). This means the detector retains information about the unlearning distribution, potentially creating a new privacy channel. The paper highlights "without using any retained data" as an advantage but never addresses whether the detector itself leaks information about the forgotten data. This should be acknowledged and argued away.

4. **Some design choices lack rigorous justification.**  
   - The contrastive entropy loss (Eq. 7) is an unusual formulation; the paper claims it "converges much faster" (line 92) but provides no evidence.  
   - The soft-weighting formula (Eq. 13) is a complex function of two cumulative probabilities from a mixed Gaussian; the rationale for this specific form (vs. using OCSVM distance directly) is not given.  
   - The OOD scoring pipeline combines Mahalanobis distance, cosine similarity, and OCSVM with a scaling factor \(\gamma=1000\) whose sensitivity is not analyzed.  

   These do not invalidate the results (the ablation shows they work), but they make the framework feel over-engineered and harder to reproduce or build upon.

### Trivial

- The mutual-information formulation in the problem definition (Eq. 1–2) is not used by the method (which uses cross-entropy loss). This is standard practice (CE is a surrogate for MI minimization) but the connection is not explained, and the formal notation is garbled by parser artifacts.

## Nice-to-Haves

- **Scalability to more requests.** The experiments use at most 4 requests. A simple experiment with more requests (e.g., 10 on CLINC150) would demonstrate that the method does not degrade catastrophically as the number of requests grows.
- **Evaluation on paraphrased/adversarial queries.** The OOD detector is tested on data from the same distribution as the unlearning data. Testing on paraphrased or adversarial variants would probe robustness in realistic deployment.
- **Simplification of the OOD pipeline.** The current detector stacks contrastive entropy + MLM + Mahalanobis + cosine + OCSVM + Gaussian mixture + sigmoid weighting. Showing that a simpler variant (e.g., just OCSVM on fine-tuned representations) performs significantly worse would justify the complexity.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The product AB can still cause interference because B is not regularized"** (Section 3.1 note in harsh critic): Factually wrong. The column space of \(AB\) is a subset of the column space of \(A\); regularizing \(A\) to be orthogonal to previous \(A\) ensures the output space of \(AB\) is orthogonal to the previous output space regardless of \(B\). The paper's argument is mathematically sound. **(Hard Rule 2)**
- **"5.1 claim for inference overhead has no units or context"**: The "5.1" missing a "%" sign is a parser artifact stripping formatting from the original submission. **(Hard Rule 6)**
- **"The paper repeatedly cites Appendix sections — cannot evaluate those claims"**: The appendix is stripped by the submission system, not missing from the original paper. **(Hard Rule 9)**
- **"Parameter efficiency: only 20M trainable params vs 6.7B"** (Strength Finder Supporting Strength 2): Conflicts with verified Weakness #2 (parameter-efficiency claim is overstated). **(Strength/Weakness conflict rule)**
- **Criticisms about equation formatting issues, garbled text, broken symbols**: These are parser artifacts, not author errors. **(Hard Rule 6)**
- **Missing related works / should cite X**: I do not have external sources to confirm their existence. **(Hard Rule 4)**

## Novel Insights

None beyond the paper's own contributions. The reviews surface genuine methodological gaps (non-consecutive interference, overstated efficiency claim) but do not produce a new synthesis or insight beyond what the paper already presents.

## Suggestions

1. **Address the non-consecutive interference gap explicitly.** Either (a) prove that pairwise consecutive orthogonality yields cumulative orthogonality under the sequential initialization scheme (if true), or (b) extend the orthogonal loss to penalize overlap with all previous requests (\( \sum_{i=1}^{t-1} \| (A^i)^\top A^t \|^2 \)) at negligible additional cost, or (c) add an experiment that explicitly measures interference between request 1 and request 4 (e.g., test unlearning effectiveness on request 1 after processing requests 2–4).
2. **Report the total trainable parameters of the full O³ system** (LoRA + OOD detector backbone) and clarify what the 20 M figure covers. This corrects the misleading framing without changing any experimental result.
3. **Add standard deviations or confidence intervals to Tables 2 and 3 and Figures 2–4.** With three seeds, this is straightforward and would significantly strengthen the reliability of the empirical claims.
4. **Add at least one continual-learning-aware baseline** (e.g., EWC applied to the unlearning objective) to isolate whether O³'s advantage is due to its continual-learning design or its individual components.
5. **Acknowledge the privacy implications of the OOD detector** and discuss whether the stored score vectors could leak information about the unlearning data.

## Score and Decision

The paper addresses an important and timely problem with a thoughtful framework and strong empirical results. The two major weaknesses — the gap between claimed cumulative disentanglement and what the pairwise loss guarantees, and the overstated parameter-efficiency claim — are real but fixable. They do not invalidate the core contribution (the method works well empirically even if the theoretical guarantee is weaker than claimed). With revisions addressing these points, the paper would be a solid contribution. I recommend acceptance with the expectation that the authors address the major and minor concerns.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>