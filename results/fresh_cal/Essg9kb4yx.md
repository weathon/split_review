Now I have all the information needed. Let me compose the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions
## Score and Decision

Let me write the review now.

---

**Important check on the critic's claim about random split timing:**

The critic says: "This random split is done *after* the OOD training, which means the test samples in D_rest are seen by the OOD detector during training?"

But the paper says (line 104): "When dealing with the continually arriving unlearning requests, we **first** randomly divide the unlearning dataset DU,t into two subsets ... Then D_used is used to compute L_OOD and train the OOD detector backbone."

So the critic misread - the split happens first, then training. This is a factually wrong criticism. **REMOVE.**

**Check on MI formulation:**

The critic says: "The formulation using mutual information is decorative — it is never used or computed." This is accurate - Section 2 introduces MI-based objectives but the rest of the paper uses cross-entropy loss. This is a minor weakness/disconnection between formalization and implementation.

**Check on "ignoring orthogonality on B matrix":**

The paper says (line 70-71): "Note that the matrix B can be regarded as the linear weights of matrix A. Thus, we don't consider its interference among different requests."

This is hand-wavy. B can mix the orthogonal components of A, producing overlapping effective updates. This is a valid but minor concern.

OK, now I'm ready to write the final review.Here is my consolidated final review:

---

## Summary

This paper addresses the underexplored problem of continual unlearning for large language models (LLMs) without access to retained data. It proposes the O³ framework with two main components: (1) an orthogonal LoRA module that uses a regularization loss to disentangle parameter updates across sequential unlearning requests, and (2) an OOD detector (trained with a contrastive entropy loss and a glocal-aware scoring mechanism) that determines during inference whether and how much to activate the unlearning LoRA. Experiments on ScienceQA, TOFU, and CLINC150 show that O³ achieves a better balance between unlearning effectiveness and utility preservation than existing baselines, many of which rely on retained data that O³ does not use.

## Strengths

1. **Highest Unlearning-Utility Ratio (U²R) across three diverse tasks.** Figure 2 shows O³ achieving the highest U²R on ScienceQA, TOFU, and CLINC150, substantially surpassing all baselines. This directly supports the paper's core claim that O³ balances unlearning and utility preservation better than prior methods in a continual setting.

2. **Competitive unlearning without any retained data.** Tables 2 and 3 show that O³ obtains strong unlearning effectiveness (low S.U. and D.U. accuracy) while using zero retained data, whereas all baselines rely on retained data yet often suffer catastrophic utility loss or degraded unlearning. This supports the claim that the method can operate under realistic privacy constraints where retained data may be inaccessible.

3. **Orthogonal regularization is empirically shown to be necessary.** Table 5 ablates the orthogonal loss weight λ: setting λ=0 (no orthogonality) reduces retained distribution accuracy from 47.27 to 32.36 and increases S.U. accuracy (worse unlearning) on ScienceQA. This ablation validates that the orthogonal design contributes to maintaining both utility and unlearning effectiveness.

4. **Extreme parameter efficiency.** Table 1 reports O³ uses only 20M trainable parameters via LoRA (<3% of the 6,758M parameters required by full-model fine-tuning baselines) while also eliminating the need for retained data, making the approach substantially more practical for large models.

5. **OOD detector design is validated through systematic ablation.** Table 4 shows the full OOD detector (contrastive entropy loss + Mahalanobis distance + cosine similarity) achieves the highest AUROC (0.95+ on both tested tasks) compared to ablations using SimCLR, MoCo, or single distance measures, confirming that each component contributes to reliable unlearning knowledge detection.

6. **Soft-weighted inference demonstrably outperforms hard thresholding.** Table 6 shows the soft-weighted mechanism (Eq. 13) achieves better unlearning (lower S.U. and D.U.) than a hard-weighted baseline, and the scaling factor ζ provides a tunable trade-off.

## Weaknesses

### Fatal
None.

### Major

1. **Orthogonal regularization only constrains consecutive request pairs, which weakens the "continual" guarantee for longer sequences.**  
   The orthogonal loss in Eq. (6) is ℒ_Orth^t = ‖(A^{t-1})^⊤A^t‖², penalizing only non-orthogonality between the current LoRA's A-matrix columns and those from the *immediately preceding* request. After three requests, there is no direct loss term enforcing orthogonality between request 1 and request 3. The paper provides no argument or analysis that pairwise consecutive orthogonality suffices to prevent interference over 3+ requests. While the experiments test only 3–4 requests (where rank-8 subspaces in a 4096-dim space may not overlap much even without regularization), this gap undermines confidence that the method scales to longer sequences of unlearning requests, which is the central claim of "continual" unlearning. The paper should either (a) extend the loss to constrain all-pair orthogonality (e.g., via a Gram matrix penalty over all previous A matrices), or (b) provide a theoretical or empirical argument that consecutive orthogonality is sufficient.

2. **Baseline comparison lacks a controlled ablation isolating the effect of O³'s specific mechanisms from the advantage of using LoRA.**  
   All baselines (GradAsc, GradDif, PO, NPO, etc.) are applied by sequentially fine-tuning the *full* 7B LLM on each unlearning request, while O³ uses a tiny LoRA (20M parameters) with inference-time switching. The paper states "We only conduct reasonable modifications to customize them in our continual unlearning settings" but provides no details on what modifications were made. Since full-model fine-tuning is known to suffer from catastrophic forgetting under sequential updates, the baseline comparison asymmetrically favors O³. The paper is missing an essential ablation: separate LoRAs per request without orthogonal loss or OOD switching (or an oracle version that picks the correct LoRA). Without this, it is unclear how much of O³'s superior U²R comes from using a parameter-efficient adapter versus the specific orthogonal regularization and OOD detection innovations. The paper's central claims would be significantly strengthened by isolating these factors.

### Minor

3. **Contrastive entropy loss (Eq. 7) lacks a theoretical guarantee that it aligns positive pairs.**  
   The loss ℒ_CEL = −Σ_i Σ_l Σ_j Δ(i,l,j) log Δ(i,l,j) minimizes the entropy of the softmax distribution over batch samples. Minimizing entropy makes the distribution peaked, but nothing in the loss *explicitly* favors the peak aligning with the positive pair (j = i, the same unmasked instance) over any negative pair. The paper states the "convergence condition... is that one dimension holds the probability of 1" and assumes this corresponds to the positive pair, but provides no justification. The supplementary MLM loss (ℒ_MLM) provides some structure, but the claim that the loss "shares similar intuition with standard contrastive learning" is imprecise — standard InfoNCE explicitly maximizes the numerator for the positive pair, whereas this loss does not. The strong empirical AUROC in Table 4 suggests the overall pipeline works, but the loss design would benefit from a theoretical or empirical analysis showing why it learns useful representations.

4. **Missing error bars / standard deviations in main results.**  
   The paper states "All experiments are run repeatedly with three random seeds" (line 170), yet Figures 2–4 and Tables 2–3 do not report standard deviations or confidence intervals. Without these, it is impossible to assess the statistical significance of the observed improvements, especially when some baseline comparisons show close values.

5. **The OOD scoring mechanism contains several ad-hoc components that are not justified.**  
   (a) The scaling factor γ = 1000 in Eq. (11) is hardcoded without any sensitivity analysis. (b) The OCSVM hyperparameter ν (controlling the expected fraction of outliers) is not reported. (c) The weight formula in Eq. (13) — involving a mixture of two Gaussians, symmetric CDF values, a sigmoid, and ζ = 10 — is complex and its derivation is not clearly motivated. The ablation in Table 6 shows soft weighting beats hard thresholding, but it is unclear whether this specific functional form is necessary or whether a simpler continuous weighting would work as well.

6. **The 5.1% inference overhead claim lacks supporting calculation.**  
   Line 181 states that "Our additional inference computation overhead is only 5.1" (presumably 5.1%). Given that O³ requires running a 355M-parameter RoBERTa-large OOD detector for each inference *for each unlearning request* (T times), and the score computation involves layer-aggregated processing, this figure needs a breakdown. How is the 5.1% computed relative to the base LLM inference?

7. **The mutual information formulation in Section 2 is decorative.**  
   Equations (1)–(3) frame the unlearning objective in terms of mutual information, but this formalism is never used or referenced in the method or experiments. The actual training loss is cross-entropy on random labels (Eq. 4). This disconnection between the formalization and the implemented method is misleading.

### Trivial

8. **The dismissal of B-matrix orthogonality is hand-waved.**  
   The paper states (line 70) "the matrix B can be regarded as the linear weights of matrix A. Thus, we don't consider its interference." Even if A's columns are orthogonal, B can mix them, causing the effective update ΔW = AB to overlap across requests. At minimum, this should be acknowledged as a limitation or empirically tested.

9. **Storage requirements for OOD score vectors are not discussed.**  
   The method stores score vectors for all D_used and D_rest samples across all unlearning requests (line 130–131: "store all these vectors as we cannot access the unlearning data after the unlearning"). For T requests with N samples each and L layers, this storage can be large. The paper does not discuss this practical concern.

## Nice-to-Haves

- **Fluency/perplexity metrics on unlearned outputs.** The paper measures unlearning by accuracy (S.U./D.U.), but low accuracy could reflect incoherent output rather than successful unlearning. Reporting perplexity or fluency of generated text (e.g., checking that outputs are grammatical but wrong) would strengthen the unlearning evaluation.
- **An ablation removing the OOD detector entirely** (always loading the LoRA with weight 1) would clarify how much utility preservation comes from the soft weighting vs. the LoRA adapter itself.
- **Results for longer sequences (e.g., 8–10 requests)** on a synthetic or semi-synthetic task would help address scalability concerns about the pairwise orthogonal regularization.

## Removed Points

These points from the reviews are flagged for removal; treat them with caution if referenced:

1. **Criticism about the random split timing** (harsh critic): "This random split is done *after* the OOD training, which means the test samples in D_rest are seen by the OOD detector during training?" — **Factually incorrect.** The paper explicitly states (line 104): "When dealing with the continually arriving unlearning requests, we **first** randomly divide the unlearning dataset... Then D_used is used to compute L_OOD and train the OOD detector." The split precedes training.
2. **Speculation about AUROC inflation from "easy negatives"** — This is unsupported speculation; no evidence is provided that the tasks have easy/hard negative structure that would inflate AUROC. AUROC is reported consistently across multiple tasks, which mitigates this concern.
3. **Generic formatting/style nitpicks** (typos, garbled characters, missing appendix content) — These are parser artifacts from PDF extraction, not author errors, and per instruction are removed.
4. **Questioning whether baselines' missing values (dashes) are explained** — While the paper could be more explicit, the text does state "we omit the results of GradAsc as it failed to generate meaningful answers" and the metric details are referenced to the appendix.
5. **Strength Finder's generic/superficial strengths** — None found; all six listed strengths are concrete and evidence-backed.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely interesting observation: the pairwise orthogonal regularization approach (adjacent-only constraints) as a design choice for continual learning with LoRA raises the question of whether gradient-based sequential fine-tuning plus a simple orthogonality penalty can implicitly maintain non-interference through the sequential training dynamics, even without explicit all-pair constraints. This is an empirical question worth exploring in future work. The contrast between the method's strong empirical performance and its theoretically loose regularization hints that the high dimensionality of LoRA parameter spaces may make exact subspace disentanglement unnecessary for practical sequence lengths — a finding that could simplify future continual unlearning designs.

## Suggestions

1. **Extend the orthogonal regularization** to constrain A^t against *all* previous A matrices (e.g., via a cumulative Gram matrix ℒ_Orth^t = Σ_{k=1}^{t-1} ‖(A^k)⊤A^t‖²) and show this scales to 8–10 requests, or provide an analysis of why pairwise adjacent constraints are sufficient.
2. **Add a controlled ablation** with separate LoRAs per request (no orthogonal loss, no OOD switching, oracle LoRA selection) to isolate the contribution of the core O³ mechanisms from the baseline advantage of using LoRA at all.
3. **Provide standard deviations** for all main results (Figures 2–4, Tables 2–3). If error bars are small, this bolsters confidence; if large, it reveals important variance that needs discussion.
4. **Justify the contrastive entropy loss** either theoretically (e.g., show that under the MLM loss, minimizing entropy of the softmax distribution implicitly aligns positive pairs) or empirically (e.g., visualize the learned similarity matrix to confirm the diagonal dominates).
5. **Simplify or justify the OOD weight function** (Eq. 13). Provide a sensitivity analysis for γ and report the OCSVM ν value. Consider whether a simpler function (e.g., directly using the OCSVM probability or normalized distance) would suffice.
6. **Add a break-down of the 5.1% inference overhead** to explain how it is computed given the per-request OOD detector costs.
7. **Acknowledge and discuss** the storage requirements for the OOD score vectors and orthogonal regularization scalability.

## Score and Decision

The paper addresses an important and underexplored problem (continual LLM unlearning without retained data) with a creative, technically coherent solution. The empirical results are strong across three diverse tasks and the ablations confirm the importance of the main design choices. The weaknesses are real but addressable: the orthogonal regularization gap weakens but does not invalidate the "continual" claim for the tested 3–4 request scenarios, the baseline comparison could be tightened with a controlled LoRA ablation, and some methodological details need better justification. With reasonable revisions (particularly suggestions 1, 2, and 4 above), the paper would be a solid contribution.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>