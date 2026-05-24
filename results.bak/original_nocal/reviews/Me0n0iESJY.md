Now I have a thorough understanding of the paper and can write the final consolidated review.

---

## Summary

This paper introduces a benchmark for model merging in Multimodal LLMs with fine-grained categorization into five capabilities (VQA, Geometry, Chart, OCR, Grounding) and explores both capability merging and modality merging. It evaluates 10 merging algorithms across InternVL2.5 (full fine-tuning) and Qwen2-VL (LoRA) models, and proposes OptMerge — a method that denoises task vectors via low-rank approximation and stabilizes optimization with SGD and mean initialization.

## Strengths

1. **First fine-grained benchmark tailored for MLLM merging**: The benchmark separates capabilities (VQA, Geometry, Chart, OCR, Grounding) and modalities (vision, audio, video), with >100k training samples per capability and both full-fine-tuned and LoRA-tuned expert checkpoints released publicly. This goes beyond prior MLLM merging works (AdaMMS merges only two models; UQ-Merge lacks task categorization). *Evidence: Section 5.1, Tables 1–3.*

2. **Comprehensive evaluation of 10 merging methods across diverse settings**: The paper systematically compares linear interpolation, sparsification, SVD-based, and optimization-based methods on two model families, capability merging, modality merging, and real HuggingFace checkpoints. This provides a useful experimental snapshot for the community. *Evidence: Tables 2, 3, 5, 6.*

3. **Modality merging demonstrates clear complementary gains**: Merging vision, audio, and video specialist models via static merging achieves 67.00 average on MUSIC-AVQA and AVQA, outperforming individual modalities (best 64.11) and competitive with online composing methods (NaiveMC 66.88, DAMC 66.79) while using 3× less storage. *Evidence: Table 5.*

4. **Practical validation on real community checkpoints**: OptMerge achieves the highest average (66.70) when merging four independently developed Qwen2-VL-7B models from HuggingFace, demonstrating real-world applicability beyond lab-constructed experts. *Evidence: Table 6.*

5. **Emergent integrated capabilities on general benchmarks**: The merged InternVL2.5-1B model outperforms the best individual specialist on every general QA benchmark (MMMU, DocVQA, ScienceQA, A12D, InfographicVQA) by an average of 10.85%, suggesting genuine capability integration rather than mere averaging. *Evidence: Table 10.*

6. **Substantial computational efficiency**: OptMerge requires only 3.78h and 21.97GB GPU memory for Qwen2-VL-7B vs. 24.56h and 256GB for mixture training. *Evidence: Table 7.*

## Weaknesses

### Major

1. **Internal inconsistency in WUDI baselines undermines the claimed improvements**: Table 3 reports WUDI Merging on Qwen2-VL at **63.65** and OptMerge at **63.30**, implying OptMerge is *worse*. But Table 4 reports WUDI at **58.65** and OptMerge at **63.30** for the same model setting, claiming a **4.65% improvement**. The paper never explains this 5-point discrepancy in the WUDI baseline across two tables that describe the same experimental setup. This makes it impossible to determine whether OptMerge consistently improves over WUDI or not, and calls the reported "2.48% average improvement" into question. *Evidence: Table 3, row "WUDI Merging" (63.65) vs. Table 4, row "WUDI Merging" (58.65); both labeled Qwen2-VL LoRA merging.*

2. **Mixture training comparison is not fully controlled**: For Qwen2-VL, the paper uses Qwen2-VL-Instruct as the "upper bound" baseline, but this model was trained on a far larger and more diverse dataset than the five task-specific datasets used to create the experts. While the paper acknowledges this asymmetry, the conclusion that merging "surpasses mixture training" conflates the comparison — the Instruct model was trained on much more data, making it an asymmetric upper bound, not a controlled baseline. For InternVL2.5 (where mixture training is done in-house), the paper provides no details on data mixing ratios, hyperparameter tuning, or training budget, making it unclear whether the mixture baseline was reasonably optimized. *Evidence: Lines 234–234, Table 2 (mixture 57.66 vs. OptMerge 57.44 — merging does not surpass mixture training on InternVL2.5).*

3. **Ablation study confounds components and lacks transparency**: Table 4 builds components cumulatively (WUDI → +SGD → +Init → +Low-rank) rather than testing each independently. This makes it impossible to isolate each component's standalone contribution. The +SGD row alone *hurts* Qwen2-VL by -9.77%, so the method's components are highly interdependent and the improvements may come primarily from the combination rather than from principled design. Furthermore, Table 4 has no column headers specifying which tasks or evaluation metrics the reported numbers average over, making it uninterpretable. *Evidence: Table 4, lines 244–247.*

4. **Theoretical result (Theorem 3.1) is not connected to the method**: The theorem bounds merging error as a function of learning rate and iterations under Lipschitz smoothness and PL conditions. However, it is never used to justify any design decision in OptMerge (SVD truncation, SGD vs. Adam, mean initialization). It functions as background motivation but does not guide or explain the proposed algorithm. The assumptions are also unverified for MLLMs. *Evidence: Section 3.2, Theorem 3.1.*

### Minor

5. **No analysis of individual expert forgetting**: The paper does not report how each fine-tuned expert performs on non-target tasks. Without this, it is impossible to tell whether the merged model's gains (e.g., Table 10) come from genuine integration of complementary skills or simply from recovering base-model capabilities that individual experts forgot during narrow specialization. *Evidence: Missing from Tables 2–3 where only target-task performance is shown for individual models.*

6. **"Data-free" claim is slightly overstated**: OptMerge requires searching the merging coefficient λ over a discrete set [0.1, 1.5] using a validation set, and the rank size k uses a heuristic (rank/n_tasks). This is a mild hyperparameter dependence, not "no hyperparameter search" as claimed in Section 2. The paper is data-free in the sense of not requiring training data for the optimization, but the λ and k choices do rely on validation performance. *Evidence: Lines 182–183, line 64.*

7. **Rank size heuristic lacks principled justification**: The paper sets k = rank of each task vector divided by number of tasks (i.e., 5) without explaining why this ratio is appropriate, and only shows robustness for k between 10–30% (Table 8). The default (20% for 5 tasks) is within this range but the reasoning for the heuristic is absent. *Evidence: Lines 182–183, Table 8.*

### Trivial

8. **"No benchmark exists" phrasing (line 18) is slightly overbroad**: The paper acknowledges AdaMMS and UQ-Merge, which do provide evaluation settings for MLLM merging, though with less task granularity. The qualifier "that clearly divides the tasks" partly addresses this.

## Nice-to-Haves

- An independent ablation (testing each component alone — initializer only, SVD only, SGD only — rather than cumulative addition) would substantially strengthen the analysis.
- Reporting each individual expert's full cross-task performance would clarify whether merging recovers lost base-model knowledge or genuinely integrates capabilities.
- A controlled mixture training baseline for Qwen2-VL (fine-tuned on exactly the same five task datasets with proper mixing) would make the "surpassing mixture training" claim more rigorous.
- Qualitative examples showing the merged model on tasks requiring combined skills (e.g., an OCR-heavy chart question) would help illustrate the claimed integration.

## Removed Points

The following points from the input reviews were removed with brief justifications.

- **"Evaluation benchmarks overlap, so per-task breakdowns are not interpretable"** (Harsh Critic, Point 2): This criticism could apply to any multi-task benchmark — real-world capabilities naturally overlap (reading is involved in chart understanding, reasoning in OCR tasks). The categorization is a reasonable granularity for model merging. This is a generic concern, not a concrete flaw in this paper.
- **"No benchmark exists claim is inaccurate"** (Harsh Critic, Section-by-Section): The paper qualifies this with "clearly divides the tasks" and explicitly discusses differences with AdaMMS and UQ-Merge. The claim is appropriately scoped.
- **"Theory assumptions are strong and unverified"** (Harsh Critic, Theory section): Standard assumptions for convergence analysis; no paper is expected to verify Lipschitz constants for 7B models. Removed as a one-size-fits-all criticism.
- **"Iso-C fails on Qwen2-VL — controlled experiment needed"** (Harsh Critic, Obvious Next Steps): The paper already provides an explanation (LoRA task vectors are already low-rank, averaging singular values reduces Frobenius norm) and notes λ adjustment only marginally helps. The request for a controlled LoRA-rank experiment is a nice-to-have, not a weakness.
- **"Comparing static merging to online composing is not apples-to-apples"** (Harsh Critic, Experimental Results): The paper explicitly acknowledges the difference (3× storage) and the comparison is still informative — showing static merging can compete with online methods is a meaningful finding, not a flaw.
- **"Table 7 comparison is one-sided"** (Harsh Critic): The table compares to mixture training, which is the relevant baseline. All merging methods share similar costs; this doesn't invalidate the comparison.
- **"Table 6 — need to confirm model identity"** (Harsh Critic): All four HuggingFace models are explicitly Qwen2-VL-7B variants (URLs provided). The critic's concern is unfounded.
- **"Missing appendix / implementation details"** (Harsh Critic, multiple): These sections are present in the original submission but stripped by the PDF parser. Not author errors.
- **"Formatting nitpicks"** (Harsh Critic, various): Parser artifacts, not author issues.
- **Strength Finder generic/superficial strengths**: Removed strengths that were generic (e.g., "this paper addressed an important problem") or that conflict with verified weaknesses. Also removed the Strength Finder's claim that "OptMerge robustly improves task vector optimization" — this conflicts with the verified weakness about the inconsistent WUDI baseline.
- **"Model merging surpasses mixture training" as a strength** (Strength Finder, Point 3): This claim is the subject of a verified weakness (not fully controlled comparison, and on InternVL2.5 the merged model 57.44 does not surpass mixture training 57.66). A strength and weakness cannot contradict each other; the weakness prevails.

## Novel Insights

The most interesting finding not fully anticipated by prior work is that **static model merging of vision, audio, and video specialists can match or exceed online composing methods** (NaiveMC, DAMC) that dynamically merge activations during inference at 3× the storage cost. This suggests that weight-space integration may be sufficient for multimodal unification, challenging the assumption that per-modality parameter decoupling during training is necessary. Additionally, the observation that **Iso-C catastrophically fails on LoRA-tuned models** (26.69 on Qwen2-VL vs. 60.63 average for other methods) while performing reasonably on full fine-tuning (54.78 on InternVL2.5) is a concrete insight about the interaction between merging algorithms and fine-tuning strategies — LoRA's already-low-rank structure is disrupted by isotropic singular value flattening. The paper would benefit from a deeper analysis of why this failure occurs, as it points to a fundamental constraint in SVD-based merging.

## Suggestions

1. **Fix the WUDI baseline inconsistency**: Explain why Table 3 and Table 4 report different WUDI Merging scores for the same Qwen2-VL setting (63.65 vs. 58.65). If the ablation uses a different metric or task subset, state this explicitly and report the main-table baseline for fair comparison.
2. **Tone down the "surpassing mixture training" claim**: On InternVL2.5, the merged model (57.44) does not surpass mixture training (57.66). The claim should be qualified as "competitive with or sometimes exceeding" mixture training, with the computational advantages (Table 7) highlighted as the primary differentiator.
3. **Add independent ablations**: Show the effect of each OptMerge component in isolation (SGD-only, initializer-only, low-rank-only) to disentangle contributions.
4. **Report cross-task performance of individual experts**: Show how each expert performs on all evaluation tasks to distinguish genuine integration from base-model recovery.

## Score and Decision

**Score**: 6.0 (Weak Accept)

The paper makes a solid empirical contribution with the first fine-grained MLLM merging benchmark and a comprehensive evaluation spanning 10 methods, two model families, capability/modality merging, and real-world checkpoints. The modality merging results and the computational efficiency advantage are genuine contributions. However, the paper's central claim (surpassing mixture training) is not uniformly supported by the evidence, and a significant internal inconsistency in the reported baselines undermines confidence in OptMerge's claimed improvements. The method itself produces only modest gains where improvements are verifiable, and its components are not convincingly isolated. With the baseline inconsistency resolved and claims calibrated, this could be a solid contribution. As-is, the overclaims and internal inconsistency prevent a stronger rating.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>