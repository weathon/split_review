---
job_id: 12dd9d2b-68db-4bb3-9048-044a1610382d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Me0n0iESJY.pdf
paper: OptMerge: Unifying Multimodal LLM Capabilities and Modalities via Model Merging
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, focusing on model merging, multimodal representation learning, optimization, and benchmarks for MLLMs.

## Minimum Quality
Pass ✅ The paper contains all core components expected for a research submission, including abstract, introduction, related work, methodology, experiments/results, and conclusion. While I have notable concerns about some theoretical claims, evaluation choices, and overstatements, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find evidence in the provided paper content of hidden prompts, manipulative instructions to reviewers, or other attempts to interfere with the review process.

# Expected Review Outcome:
## Summary
This paper studies data-free model merging for multimodal large language models. It introduces a benchmark covering capability merging across five categories, VQA, geometry, chart understanding, OCR, and grounding, as well as a modality-merging setting across vision, audio, and video. The paper also proposes OptMerge, an optimization-based merging method that denoises task vectors via low-rank approximation and modifies the optimization procedure for full fine-tuning and LoRA settings, and reports broad empirical comparisons against ten merging baselines.

## Strengths
The benchmark contribution is useful and timely. A recurring problem in this area is that papers mix together arbitrary datasets, heterogeneous fine-tuning procedures, and unclear evaluation protocols. Here, the benchmark is more structured, with explicit task categorization and both full fine-tuning and LoRA settings. Table 1 on Page 7 gives a reasonably broad view of the training data composition, and the capability evaluation suite is more fine-grained than simply reporting one aggregate MLLM score.

The experimental scope is broad. The paper evaluates many baselines across two backbone families and two adaptation regimes, then extends to cross-modality merging and also to real checkpoints collected from Hugging Face. Even when I am not fully convinced by every claim, this is a stronger experimental package than many model-merging papers that only test one architecture or one toy benchmark.

The paper includes informative visual diagnostics. In Figure 2 on Page 5, the task-vector magnitude histograms and layer-wise normalized Frobenius norms make the central motivation more concrete, namely that the benchmark is built around relatively small task drifts and that full fine-tuning and LoRA produce very different spectral/statistical patterns. This figure does useful work beyond decoration, because it explains why the authors later split their methodology between Sections 4.1 and 4.2. Likewise, Figures 3 and 4 on Page 6 provide an intuitive explanation for the optimization pathology in LoRA merging, where the merged vector norm grows during optimization under Eq. (1), and they support the claim that the proposed initialization and optimizer choice stabilize the norm.

Some results are genuinely strong. In Table 3 on Page 8, OptMerge reaches the best average score on Qwen2-VL among the compared static merging methods, and improves particularly on MATH-Vision, ChartQA, and RefCOCO/RefCOCO+. Table 5 on Page 9 is also interesting because it shows that static merging of language-side parameters across vision, audio, and video models can compete with or slightly exceed online composition baselines, which is a nontrivial finding for multimodal reuse.

The paper is fairly clear overall. The method is not mathematically deep, but the practical recipe is understandable: low-rank denoising, mean initialization, and optimizer changes depending on whether the expert models are fully fine-tuned or LoRA-adapted.

## Weaknesses
1. **The theoretical claims are much stronger than what the main paper actually justifies, and the theory is only loosely connected to the practical MLLM setting.**  
   On Pages 4-5, Theorem 3.1 is presented as an explanation of how learning rate and iteration count affect mergeability. The statement depends on PL-type convergence, bounded gradients, directional similarity, and approximate orthogonality assumptions, all of which are introduced only in the appendix and are very strong for modern multimodal fine-tuning. In particular, Assumptions A.2-A.4 in the appendix are doing most of the work: PL for each task loss, task vector alignment with the initial negative gradient, and near-orthogonality between task vectors. Those assumptions are not empirically validated in the main paper. This matters because the theorem is used in Section 3.2 to motivate benchmark construction and to interpret mergeability of fine-tuned MLLMs, yet the actual fine-tuning pipelines involve Adam/LoRA/full SFT, instruction tuning, multilingual data, and nonconvex transformers, which are quite far from the deterministic fixed-step GD setup in Appendix A. As written, the theorem is more of a stylized motivation than a serious explanatory account of the empirical system.

2. **Equation (3) is insufficiently justified and contains a notation/derivation gap that makes the core objective feel more heuristic than principled.**  
   In Section 4.1 on Page 6, the paper performs SVD on the centered task vector,  
   \[
   \mathrm{SVD}(\tau_{i,l}-\bar{\tau}_l)=U\Sigma V^\top,
   \]
   then proposes optimizing
   \[
   \left\|(\tau_{m,l}-U_{1:k}\Sigma_{1:k}V_{1:k}^\top-\bar{\tau}_l)(\Sigma_{1:k}V_{1:k}^\top)^\top\right\|_F^2.
   \]
   The paper says this substitutes \(\Sigma_{1:k}V_{1:k}^\top\) for the input subspace \(x_{i,l}\), but the justification is thin. In Eq. (1), the WUDI objective uses \((\tau_{i,l})^\top\) as a proxy for data. In Eq. (3), the proxy changes to a truncated factor of the centered matrix, but the paper does not derive why this is the correct surrogate for hidden activations, nor why discarding the left singular vectors from the “input subspace” is valid beyond intuition. Since this is the main technical novelty, the lack of a cleaner derivation weakens confidence in the method. At minimum, the paper should explicitly define the tensor/matrix shapes involved layer by layer and explain why \((\Sigma_{1:k}V_{1:k}^\top)^\top\) is the right substitute rather than, for example, \(V_{1:k}\), \(U_{1:k}\Sigma_{1:k}\), or the reconstructed truncated task vector itself.

3. **The comparison to the strongest baseline is mixed, and the paper sometimes overstates the superiority of OptMerge.**  
   For InternVL2.5 in Table 2 on Page 8, WUDI Merging has a higher average than OptMerge, \(74.48\) vs \(73.94\). Yet the text around Section 5.2 repeatedly frames OptMerge as achieving the best results and “superior average results across various scenarios.” That is too broad. The paper later softens this by saying OptMerge improves full fine-tuned models by \(0.44\%\) and \(1.9\%\) in Tables 2 and 6, but that sentence is itself confusing, because Table 2 does not show OptMerge beating WUDI on average. This inconsistency should be cleaned up. If the main claim is robustness across settings rather than universal dominance, the narrative should say that plainly instead of implying consistent best-in-class performance.

4. **The evidence for “surpassing mixture training” is not yet convincing, because the comparison is not apples-to-apples.**  
   This is one of the paper’s more eye-catching claims, stated in the abstract, introduction, and Section 5.2. But the support is uneven. For InternVL2.5 in Table 2, the Mixture Training baseline underperforms several merging methods on the reported average, which is interesting. However, for Qwen2-VL in Table 3, the paper uses Qwen2-VL-Instruct as an “upper bound for mixture training” rather than an actual jointly trained multitask baseline. That is not the same experimental condition. A pretrained instruct version may differ in data volume, task mixture, training recipe, and alignment objectives. This matters because the headline claim is not merely that merging is competitive with other strong models, but that it can outperform data mixing or multitask training. The paper does not yet establish that cleanly across both backbones.

5. **Hyperparameter sensitivity is underexplored, especially for a method positioned as practical and data-free.**  
   The method still depends on several design choices: the scaling coefficient \(\lambda\), the SVD truncation rank \(k\), optimizer choice, initialization, 300 optimization steps, and the decision to apply the method “exclusively to the linear layer” on Page 7. Table 8 on Page 10 gives some ablation for the rank ratio, which is helpful, and Table 4 on Page 8 provides component ablations. But several important aspects remain underspecified. For example, the main text says \(\lambda\) is selected by searching over \([0.1,0.3,0.5,0.7,1.0,1.5]\), but it is not clear whether this is done per method, per backbone, or per evaluation suite, and on what validation signal. Since the paper emphasizes “no hyperparameter search” relative to some prior work, the role of this search should be described more carefully. Also, the choice \(k = \mathrm{rank}(\tau)/5\) is simple but looks arbitrary; the fact that performance degrades sharply in grounding metrics at larger \(k\) in Table 8 suggests that rank truncation is not a benign detail.

6. **Some tables raise questions about metric aggregation and interpretation.**  
   Table 2 and Table 3 report an “Avg.” score, but the averaging convention is not fully transparent in the main text, especially since some individual models have “-” for tasks that they cannot evaluate, and Table 8 includes an extra RefCOCOg column not present in Tables 2 and 3. Similarly, Table 6 on Page 9 appears to contain several typos in dataset names, for example “Vis/Wic,” “truit,” and “TestVQA,” which makes me less confident in the care taken with reporting. More importantly, in Table 6 many merging methods are nearly tied, and OptMerge is not clearly ahead, \(86.42\) vs \(86.77\) for TIES w/ DARE. That weakens the practical significance of the claimed method advance on real community checkpoints.

7. **The benchmark design is useful, but there are confounds in training data and language composition that make algorithmic conclusions less clean than the paper suggests.**  
   On Page 7 and in Appendix C, InternVL uses multilingual data while Qwen2-VL excludes Chinese data because it degraded English benchmark performance. That is a reasonable engineering choice, but it means the two benchmark tracks are not directly comparable in data composition. More generally, the benchmark is not purely probing merging algorithms; it is also probing a particular set of fine-tuning recipes chosen to keep parameter drift small. Figure 2 on Page 5 is illustrative here: the benchmark is intentionally constructed in a merge-friendly regime with relatively small task vectors. That is acceptable for an initial benchmark, but then claims about general model merging behavior should be toned down. The benchmark may be measuring performance in a carefully curated “mergeable expert” regime rather than in the broader open-source reality.

8. **The method description for LoRA merging is partly empirical and lacks a more precise optimization account.**  
   Section 4.2 on Page 6 says that with LoRA, gradients are effective only in directions corresponding to non-zero singular values and that Eq. (1) “achieves orthogonality by increasing the length of the merge vector,” causing collapse in language ability. Figure 3 is a good intuition sketch, and Figure 4 shows norm growth for WUDI versus a flatter curve for the proposed method. But the argument remains informal. The geometry in Figure 3 is 2D intuition, not a derivation, and the paper does not quantify the supposed “collapsed language ability” in the main results. If large merge-vector norm is a central failure mode, I would expect explicit measurements of base-language or general instruction-following degradation, especially because Section 4.2 makes a fairly strong causal claim about why Adam fails and SGD helps.

9. **The paper misses an opportunity to evaluate retention of base/general capabilities more systematically.**  
   Table 10 on Page 10 is a nice step in this direction, since it tests the merged model on broader multimodal QA benchmarks and OptMerge does well. Still, this section is limited to the InternVL2.5-1B merged model, and there is no comparable general-capability evaluation for the Qwen2-VL and omni-modal settings. This matters because one of the standard concerns in merging is catastrophic forgetting or corruption of base-model behavior. The paper talks about “collapsed language ability” and deviation from the original distribution in Section 4.2, but does not directly evaluate that claim across settings.

10. **Presentation is generally good, but there are enough inconsistencies and overclaims that the paper needs tightening.**  
   Examples include the mixed message around whether OptMerge is universally strongest, the ambiguous wording around “upper bound for mixture training,” and several small typographical/reporting issues in Tables 6 and 8. None of these is fatal, but together they make the paper read as slightly more polished experimentally than analytically.

## Questions
1. For the key claim that model merging can outperform mixture training, can the authors provide a stricter apples-to-apples multitask baseline for the Qwen2-VL setup, instead of using Qwen2-VL-Instruct as a proxy? This would substantially increase my confidence in one of the paper’s main claims.

2. Please clarify exactly how the merge coefficient \(\lambda\) is selected. Is it tuned separately for each method and backbone? What data or criterion is used for selection, given the emphasis on data-free merging and on avoiding test-time hyperparameter search?

3. In Eq. (3), can the authors give a more rigorous derivation of why \((\Sigma_{1:k}V_{1:k}^\top)^\top\) is the right surrogate for the hidden-input subspace? A shape-aware derivation and a comparison to alternative surrogates would help.

4. Can the authors reconcile the narrative in Section 5.2 with Table 2, where WUDI has a higher average than OptMerge for InternVL2.5? I would like a more precise claim, for example robustness across regimes rather than outright superiority.

5. Figure 4 suggests norm stabilization is central to the LoRA setting. Can the authors report direct measurements of general language or instruction-following retention before and after merging, to verify that large merge-vector norms actually correlate with the claimed collapse in language ability?

6. The benchmark intentionally appears to favor small parameter drift, as suggested by Figure 2 and the discussion in Section 3.2. How does OptMerge behave when merging experts that are farther from the base model, or when the task vectors are not nearly orthogonal? Even a small controlled stress test would help assess external validity.

7. In Tables 2, 3, and 6, please define exactly how the “Avg.” column is computed when some individual experts do not have scores for all tasks, and clean up the apparent table typos. This is a small issue, but it affects interpretability.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work is primarily methodological and benchmark-oriented.

## Soundness Rating
3: good. The empirical study is broad and mostly careful, but some central claims, especially around theory and superiority over mixture training, are not fully supported as strongly as stated.

## Presentation Rating
3: good. The paper is generally readable and well organized, with useful figures and extensive tables, but there are several inconsistencies, under-justified derivations, and reporting issues that should be corrected.

## Contribution Rating
3: good. The benchmark is a meaningful contribution and the method is a useful optimization recipe, though the methodological advance itself feels more incremental than the paper’s framing suggests.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The benchmark and breadth of experiments make this a worthwhile contribution for the community, and the method appears practically useful. That said, the theoretical framing is idealized, the strongest empirical claims are occasionally overstated, and several evaluation/comparison choices need tighter justification.

## Reviewer Confidence
4: confident. I am confident in my assessment, though not absolutely certain. It is unlikely, but not impossible, that I misunderstood some parts or missed some related work.