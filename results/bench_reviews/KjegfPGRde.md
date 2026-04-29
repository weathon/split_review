## Summary
The paper proposes DePT, a parameter-efficient prompt-tuning method that replaces part of a length-100 soft prompt with a shorter soft prompt plus low-rank additive updates to the input embeddings, preserving the nominal trainable-parameter count while reducing input sequence length. The paper evaluates DePT across many NLP and VL tasks and reports both accuracy improvements over vanilla prompt tuning and measured training/inference time and memory savings.

## Strengths
- **Clear and simple efficiency-oriented mechanism.** Section 2.2 defines DePT as replacing a vanilla prompt matrix \(P \in \mathbb{R}^{l \times d}\) with a shorter prompt \(P_s \in \mathbb{R}^{m \times d}\) plus low-rank matrices \(A \in \mathbb{R}^{s \times r}\), \(B \in \mathbb{R}^{r \times d}\), while enforcing equal parameter count via \(l d = m d + (s+d)r\). This directly targets the sequence-length overhead of prompt tuning rather than merely reducing trainable parameters.
- **The paper measures real runtime and memory effects rather than relying only on complexity arguments.** Section 3.3 reports training time, memory, and inference throughput comparisons against vanilla prompt tuning, including claims such as roughly 25% training/memory savings for T5 settings and inference throughput gains from 6.5% on T5-small to 18.1% on T5-large for \(m=20\).
- **Broad empirical coverage.** The paper evaluates on 21 NLP tasks and 2 vision-language tasks, and considers T5-small/base/large, GPT-2 small/medium/large, and CLIP-T5. This breadth makes the empirical case more convincing than a single-benchmark PEFT paper.
- **Useful ablations over prompt length and optimization.** Section 3.3 varies the remaining prompt length \(m \in \{0,20,40,60,80\}\), showing that fully removing the prompt can hurt, while Section 3.4 studies the importance of separate learning rates for the short prompt and low-rank matrices.
- **The paper is transparent about some limitations.** The limitations section explicitly acknowledges extra hyperparameter tuning and that the parameter count depends on maximum sequence length \(s\), both of which are important caveats for DePT.

## Weaknesses

### Fatal
None.

### Major
- **The central efficiency claim lacks the decisive shorter-prompt baseline.** Section 3.3 compares DePT mainly against vanilla prompt tuning with \(l=100\) while DePT uses a shorter actual prefix \(m<100\). Since the claimed time/memory benefit comes largely from reducing sequence length, the crucial comparison is vanilla prompt tuning with the same actual prompt length \(m\), or a full accuracy–latency–parameter Pareto curve over prompt lengths. Matching trainable parameter count is informative, but it does not prove that the low-rank embedding update is a better efficiency/performance tradeoff than simply using fewer soft tokens.
- **The strongest SOTA/full-finetuning claims are over-supported by heterogeneous baseline protocol.** Section 3.1 says many baseline numbers are directly quoted from published papers, while DePT is trained with careful learning-rate search and up to 300k steps, as acknowledged in the limitations. Quoted baselines can provide useful context, but they are not a fully controlled comparison for claims such as “outperforms state-of-the-art PEFT approaches” or “outperforms full fine-tuning” in some scenarios, especially when some reported margins are very small, e.g. +0.1 over MPT on GLUE and +0.4 on SuperGLUE.
- **The LLM-deployment claim is stronger than the evidence.** The paper repeatedly motivates DePT by LLM-scale inference and heavy daily querying, and concludes that efficiency “amplifies with increasing model sizes.” However, the main efficiency evaluation is GLUE-style evaluation throughput using HuggingFace Trainer on a single RTX 3090, mostly on T5/GPT-2-scale models, with only a limited T5-3B mention. This supports the narrower claim that shorter prompt-tuned inputs can improve throughput/memory in these classification-style settings, but it does not establish realistic LLM serving benefits involving long-context prefill, autoregressive decoding, KV caching, batching, output-length variation, or memory pressure.
- **The few-shot transfer setting is under-specified and may mix source and target tasks.** The paper states that PETL source tasks include MNLI, QQP, SST-2, SQuAD, and ReCoRD, and then evaluates few-shot performance across GLUE/SuperGLUE-style tasks. If GLUE targets include MNLI, QQP, or SST-2, then those results are not clean few-shot transfer from disjoint source tasks. The paper should explicitly separate overlap-free transfer from same-task prompt transfer and clarify checkpoint/source selection.

### Minor
- **The conceptual framing as “decomposition of a prompt” obscures that the method is a position-specific embedding offset.** Operationally, DePT learns a low-rank matrix indexed by absolute sequence position and adds it to every input embedding. This is a valid PEFT mechanism, but it raises questions about sensitivity to padding/truncation, variable-length inputs, and whether the learned component behaves more like a positional bias than decomposed prompt information.
- **The low-rank multiplication notation is inconsistent.** The text defines \(A \in \mathbb{R}^{s \times r}\) and \(B \in \mathbb{R}^{r \times d}\), so the product should be \(AB \in \mathbb{R}^{s \times d}\), but Eq. (2) writes \(BA \in \mathbb{R}^{s \times d}\). This is likely a notation error, but it is central enough to the method that it should be corrected.
- **Small average improvements should be interpreted more cautiously.** The paper reports mean/std for few-shot experiments, but the main full-data comparisons rely on averages over heterogeneous tasks and sometimes very small margins over strong PEFT baselines. This does not invalidate the results, but the text should avoid treating +0.1 or +0.4 average gains as strong evidence without seed variance or controlled reruns.
- **The learning-rate ablation is suggestive but not fully fair.** Section 3.4 compares two fixed single-learning-rate choices against a grid-searched mixed-learning-rate setting. This supports that the chosen single rates are bad, but a stronger conclusion would require comparing the best single-rate run under a comparable search budget against the best two-rate run.
- **Practical training efficiency is incomplete without accounting for hyperparameter search.** The paper fairly notes that DePT introduces extra hyperparameters and trains up to 300k steps with careful learning-rate search. The runtime/memory savings per training step and inference run are useful, but the total cost picture is less favorable if extensive search is needed.

### Trivial
None.

## Nice-to-Haves
- Add accuracy–latency–parameter Pareto curves comparing vanilla PT at multiple prompt lengths, DePT at multiple \(m/r\) allocations, and perhaps LoRA/adapter-style PEFT methods.
- Report learned update norms by position to clarify whether DePT primarily modifies early positions, late/padding positions, or distributes signal across the full sequence.
- Break inference timing into prefill and decoding for autoregressive generation, ideally with batching and KV caching, to support LLM-serving claims.
- Clarify the maximum sequence length \(s\) used for each benchmark/model setting, since it directly affects the allowed rank \(r\) and the parameter allocation.
- For VL experiments, explicitly state whether the trainable visual projection layer is included in the trainable-parameter budget and whether it is treated identically across baselines.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Pure formatting/style complaints.** Any criticism about awkward phrasing, capitalization, or formatting artifacts should not count against the paper; the provided text is PDF-extracted and formatting issues may be parser artifacts.
- **Claims that cited models, tools, datasets, or references are unavailable or unverifiable.** No such criticism should be retained; all cited entities are treated as real and available.
- **Missing related work complaints.** I do not include missing-related-work criticisms because external completeness cannot be verified from the paper alone.
- **Generic “needs more datasets/models” criticism.** The paper already evaluates many tasks and several model families/sizes. More LLM-scale generation experiments would specifically support the LLM claim, but a generic request for broader evaluation would be too weak.
- **Overly strong dismissal of the efficiency results.** The efficiency experiments are not meaningless: they do show measured time/memory and throughput benefits relative to length-100 PT. The valid criticism is narrower: the paper has not shown that DePT dominates shorter vanilla prompts or realistic LLM-serving baselines.
- **Generic strength that the problem is important.** The fact that prompt-tuning efficiency is an important topic is not a paper-specific strength unless tied to DePT’s concrete method and evidence.
- **Overstated strength that the inference evaluation is fully deployment-relevant.** The paper measures inference speed across model sizes, which is useful, but the experiments do not model realistic LLM serving conditions; therefore that claim is weakened rather than retained as a full strength.

## Novel Insights
The main novel observation from synthesizing the reviews is that DePT’s contribution sits between two interpretations: as a prompt-decomposition method and as a low-rank, absolute-position embedding adaptation method. The empirical results suggest this can be a practical way to reclaim some prompt-token overhead, but the paper’s strongest claims depend on whether this position-specific offset provides a better Pareto frontier than simply shortening prompts. That missing comparison is the key distinction between “useful PEFT variant” and “established solution to prompt-tuning sequence-length overhead.”

## Suggestions
- Add vanilla PT baselines at the same actual prompt lengths \(m\) used by DePT, and plot performance versus inference/training cost.
- Rerun the closest competing baselines under matched training steps, validation selection, prompt lengths, learning-rate search budgets, and random seeds, at least for GLUE/SuperGLUE and the headline PEFT comparisons.
- Rephrase SOTA and full-finetuning claims to reflect the mixed and partially quoted baseline protocol.
- Evaluate DePT under realistic decoder-only generation workloads, separating prefill, decoding, batching, and KV-cache behavior.
- Explicitly exclude source-task overlaps from few-shot transfer averages, or label those cases as same-task transfer rather than few-shot transfer.
- Correct the matrix multiplication notation and describe how padding/truncation and variable sequence lengths interact with the position-indexed low-rank update.

## Calibration and Score Rationale
I calibrated this paper against retrieved human-review anchors:

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fswihJIYbd.md`, avg 7.00, Accept — very close topic anchor on decomposed/adaptive prompt tuning; accepted despite questions about generality and efficiency evaluation, suggesting this family of simple PEFT contributions can score around 7 when empirical coverage is broad.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6PmJoRfdaK.md`, avg 7.00, Accept — efficient long-context LLM fine-tuning anchor; stronger LLM-scale relevance than this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pCEgna6Qco.md`, avg 6.75, Accept — LLM fine-tuning behavior paper; comparable empirical usefulness but less directly about prompt-token overhead.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vmlwllg7DJ.md`, avg 4.25, Reject — efficiency paper with weaker evidence; DePT is stronger and more concrete.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/KJLqgaixgn.md`, avg 3.50, Reject — efficient sequence-length training anchor with much more severe weaknesses; DePT is clearly above this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fL8Zp8o6RL.md`, avg 5.50, Reject — efficient long-context inference paper; DePT has broader task evaluation but weaker realistic serving evidence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/am5Z8dXoaV.md`, avg 5.00, Reject — long-context inference efficiency anchor; DePT is methodologically cleaner but similarly overclaims deployment relevance.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/t8KLjiFNwn.md`, avg 7.00, Accept — strong efficiency paper with some baseline concerns; DePT is somewhat weaker because the missing same-length PT baseline is central.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/v9Sfo2hMJl.md`, avg 5.67, Reject — strong results but uncontrolled/unfair baseline tuning; DePT shares this issue but has a clearer efficiency mechanism and broader experiments.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Qyp3Rni2g1.md`, avg 5.25, Reject — efficiency benchmark with generalization concerns; DePT is above this due to a concrete method and measured savings.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LDu822E45Q.md`, avg 4.25, Reject — useful empirical motivation but weak baselines; DePT has a stronger contribution and much broader evaluation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bJx4iOIOxn.md`, avg 7.50, Accept — high-quality prompt-tuning analysis across many datasets; stronger analytical depth than DePT.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gTwRMU3lJ5.md`, avg 7.33, Accept — LoRA/PEFT optimization anchor; likely more controlled conceptually than DePT.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/26XphugOcS.md`, avg 7.00, Accept — prompt-transfer anchor; comparable PEFT relevance.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/iynRvVVAmH.md`, avg 7.00, Accept — PEFT/model fusion anchor; comparable contribution level.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5HCnKDeTws.md`, avg 6.75, Accept — LLM fine-tuning scaling study; stronger on large-model scaling than this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/SYnIf4LxAG.md`, avg 6.50, Accept — prompt transfer under scarcity; comparable but less directly efficiency-focused.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/v6NNopExN4.md`, avg 5.00, Reject — soft-prompt transfer paper with setting/evaluation gaps; DePT’s empirical breadth is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NeVbEYW4tp.md`, avg 5.00, Reject — efficient test-time prompt tuning anchor; DePT is stronger due to clearer mechanism and broader experiments.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/J6Xgra2bE5.md`, avg 4.75, Reject — context-aware prompt tuning; DePT is above this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/27n0kvWgqT.md`, avg 5.50, Reject — PEFT comparison anchor; DePT is somewhat above due to concrete measured efficiency.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PPjpGTPG5K.md`, avg 5.33, Reject — routed PEFT anchor; DePT is above but shares some claim/evaluation concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/BeT8QvxCk2.md`, avg 4.80, Reject — soft prompt framework with weaker evaluation; DePT is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/RP0NPepy1m.md`, avg 4.40, Reject — lower-borderline LoRA-style PEFT anchor; DePT is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/pdzHpQbGrn.md`, avg 2.50, Reject — low-quality prompt-learning anchor with weak novelty/runtime evidence; DePT is far above this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/49ti6LOUw5.md`, avg 3.00, Reject — PEFT paper with outdated/insufficient experiments; DePT is much stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/kYUpFKqtNe.md`, avg 3.50, Reject — VLM PEFT paper with constrained novelty and missing ablations; DePT is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bYsieh8LE2.md`, avg 3.67, Reject — Universal LoRA paper with shaky experiments and generality issues; DePT is above this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9KatbAXLAq.md`, avg 3.75, Reject — PEFT-related paper with setup/presentation concerns; DePT is above this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nb9DiBUt7c.md`, avg 4.00, Reject — PEFT efficiency paper with unclear end-to-end efficiency and limited experiments; DePT is stronger.

Relative to these anchors, DePT is well above the low-scoring PEFT papers because it has a simple concrete method, broad experiments, and measured efficiency gains. However, it is below the stronger accepted PEFT/efficiency anchors because the most important efficiency comparison—shorter vanilla prompts at the same actual input length—is missing, and the SOTA/LLM claims are overstated relative to the protocol. I would place it in the upper borderline-to-weak-accept range.

## Score and Decision
Score: 6.5  
Decision: Accept

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>