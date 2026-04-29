## Summary
The paper proposes **GreenTrainer**, an adaptive backpropagation method for LLM fine-tuning that selects trainable tensors under a user-specified FLOPs budget. Its main technical components are a tensor-level backpropagation FLOPs model, a first-order tensor-importance metric based on estimated loss reduction from weight updates, and a dynamic-programming tensor selector. The experiments report substantial PFLOPs and wall-clock reductions on OPT, BLOOMZ, and FLAN-T5 summarization fine-tuning, but several central methodological and evidential gaps weaken the strongest claims.

## Strengths
- **Addresses a real inefficiency not fully handled by many PEFT methods.** The paper explicitly decomposes training cost into forward propagation, activation-gradient propagation, and weight-gradient/update computation, and correctly observes that methods such as LoRA and Prefix Tuning can still require backpropagating activation gradients through much of the model. This is clearly motivated in Section 2.3 and Eq. (2), where even frozen layers may need `dy` computation to propagate gradients to selected tensors.
- **The tensor-level cost formulation is a useful and concrete direction.** Section 3.1 separates each tensor’s activation-gradient cost `t_dy` and weight-gradient cost `t_dw`, and Eq. (2) / Eq. (3) model the fact that selecting a tensor can induce additional backward propagation through intervening tensors. This is more nuanced than simply counting selected parameters or selected layers.
- **The paper reports both PFLOPs and wall-clock time.** Table 2 reports end-to-end PFLOPs and time, and line 195 states that the measured cost includes forward/backward passes, tensor importance evaluation, and DP selection. This is stronger than relying only on theoretical parameter-count reductions.
- **Empirical results show promising cost–accuracy tradeoffs in several settings.** For example, on FLAN-T5-3B/DialogSum, GT-0.4 reduces PFLOPs from 135.7 to 62.5 while reaching 46.0/20.7/38.1 ROUGE versus full fine-tuning’s 46.5/20.8/38.5. On OPT-2.7B/SciTLDR, GT-0.5 uses 20.8 PFLOPs versus 41.8 for full fine-tuning and still obtains 30.5/13.1/25.2 ROUGE.
- **Includes some useful ablations and scaling evidence.** Table 4 compares the proposed importance metric against update-magnitude-only and gradient-only metrics, and Table 5 evaluates OPT models from 350M to 6.7B parameters, which helps show that the approach is not demonstrated on only one model size.

## Weaknesses

### Fatal
None.

### Major
- **The tensor-importance computation is under-specified and appears potentially circular.** The importance metric in Section 3.2 is defined as  
  \[
  I_k = -\sum_i \Delta w_i^{(k)} \partial L/\partial w_i^{(k)}.
  \]  
  To rank all tensors before selecting them, GreenTrainer seems to need candidate updates and gradients for all tensors, including tensors that are currently frozen or not selected. The paper does not explain when these quantities are computed, on which batches, whether unselected tensors receive fresh gradient estimates, or how this is done without incurring the full backward cost that the method aims to avoid. The authors state that measured costs include importance evaluation and DP selection, but the algorithmic description does not resolve the circularity: either full gradients are computed, threatening the FLOPs-saving claim, or unselected tensors lack meaningful current importance estimates, risking self-locking selection. This is the most serious gap because adaptive selection is the core contribution.
- **The comparison to LoRA and Prefix Tuning is not sufficiently specified or convincingly tuned.** Section 4 states that all methods use batch size 4, 5 epochs, AdamW with learning rate \(2\times10^{-5}\), linear schedule, and weight decay \(10^{-2}\). However, LoRA rank, scaling/alpha, dropout, prefix length, initialization, and tuning procedure are not specified in the main text. Applying one full-fine-tuning-style hyperparameter configuration to all baselines makes the headline claim of superiority over PEFT methods less reliable, especially given very poor Prefix-Tuning results in some rows, e.g. OPT-2.7B/SciTLDR Prefix-T at 7.6/0.4/6.1 versus Full FT at 32.9/14.9/27.1.
- **The “up to 64% FLOPs reduction without noticeable accuracy loss” claim is overstated relative to the reported results.** Table 3 shows that OPT-2.7B GT-0.36, with 64–65% FLOPs reduction, collapses badly: SciTLDR R1 drops from 32.9 to 4.1 and DialogSum R1 drops from 23.6 to 15.7. The paper later characterizes low \(\rho \leq 0.4\) as causing only “moderate model accuracy loss,” but this is not accurate for GT-0.36 on SciTLDR. There are settings where high FLOPs reduction has little loss, particularly FLAN-T5/SciTLDR, but the paper itself says that dataset is trivial for FLAN-T5 because FT-Top2 already matches full fine-tuning. The abstract and conclusion should qualify the claim as task/model-dependent rather than presenting it as a general property.
- **The DP/FLOPs model is not validated in enough detail to support the claimed rigor.** Section 3.1 gives qualitative rules for embeddings, MHA, LayerNorm, and FFN, but does not demonstrate that the ordered one-dimensional recurrence in Section 3.3 exactly captures arbitrary transformer computation graphs with residual paths, attention branches, tied embeddings, and encoder–decoder cross-attention. The reported PFLOPs and times show that some savings are realized, but there is no direct validation comparing the predicted tensor-selection FLOPs against profiler measurements across sampled tensor masks. Since the selector depends directly on these costs, this is a substantive methodological gap.

### Minor
- **Small claims of improvement over full fine-tuning are not supported by variance estimates.** Some reported gains are very small, e.g. OPT-2.7B/SciTLDR GT-0.7 at 33.1/15.2/27.6 versus Full FT at 32.9/14.9/27.1, and BLOOMZ-3B/SciTLDR GT-0.7 at 28.0/12.2/22.4 versus Full FT at 28.3/12.1/22.5. Without multiple seeds or confidence intervals, these should be described as comparable performance rather than evidence that GreenTrainer reliably improves accuracy or reduces overfitting.
- **The experimental scope is narrower than the broad LLM fine-tuning claims.** The evaluation covers two summarization datasets and ROUGE metrics, with useful variation across model families, but the claims are framed broadly around downstream LLM fine-tuning. Additional task types would be needed to support broad generalization beyond summarization.
- **The paper would benefit from stronger controls isolating the value of adaptive tensor selection.** The importance-metric ablation is useful, but the experiments do not include random tensor selection, static cost-matched tensor masks, uniform-per-block selection, or cost-aware but importance-free selection. Such controls would help show that the gains come from the proposed importance metric and DP selection rather than simply from selecting any sufficiently deep/large subset of tensors.
- **The DP complexity and budget discretization are unclear.** The paper states an \(O(N^2 T_{\text{full}})\) DP complexity, but \(T_{\text{full}}\) is a FLOPs budget and may be a very large continuous/integer quantity. The implementation presumably discretizes or rescales costs, but the discretization granularity and approximation error are not explained.
- **The environmental framing is stronger than the measurements.** FLOPs and wall-clock time are useful proxies, but the paper repeatedly links FLOPs reduction directly to carbon-footprint reduction without measuring energy, power, GPU utilization, or carbon intensity. This does not invalidate the compute-efficiency contribution, but the “Green AI” claims should be stated more carefully.

### Trivial
None.

## Nice-to-Haves
- Report selected tensors over training, e.g. heatmaps by layer/block/epoch, to show whether GreenTrainer learns meaningful adaptive patterns or mostly selects predictable regions.
- Add a FLOPs/time breakdown into forward pass, activation-gradient propagation, weight-gradient computation, importance evaluation, DP overhead, and optimizer update.
- Include accuracy–FLOPs Pareto curves rather than only tables.
- Study sensitivity to \(\rho\), learning rate, and selection frequency, especially because Table 3 shows sharp degradation at very low \(\rho\).
- Measure actual energy consumption on matched hardware if the Green AI framing remains central.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Do not treat lack of direct carbon/energy measurements as a core flaw.** It is reasonable to ask for energy measurements as a nice-to-have, but FLOPs and wall-clock time are common efficiency proxies. The absence of power/carbon measurement should not be used to reject the compute-efficiency contribution by itself.
- **Do not criticize missing related work.** External related-work completeness cannot be reliably verified from the provided paper text and should not be part of the final evaluation.
- **Do not treat presentation/formatting artifacts as weaknesses.** Any odd line breaks, missing appendix references, or PDF extraction artifacts are not author errors.
- **The claim that fixed selections are always inadequate should be weakened rather than treated as a decisive flaw.** Table 1 does show that \((W_Q,W_V)\) on OPT-2.7B/DialogSum slightly exceeds Full FT on R1, but the authors’ broader point is partly that such fixed selections save only around 33% FLOPs in their setup. This complicates the narrative but does not invalidate the motivation.
- **Do not question the existence or availability of any cited model, dataset, benchmark, or tool.** All cited entities should be treated as real and available.

## Novel Insights
The most important synthesis is that GreenTrainer’s core idea—optimizing tensor selection under the true cost of induced backward propagation—is genuinely promising and more targeted than ordinary parameter-count PEFT. However, the current submission leaves a gap exactly where the method must be most precise: computing tensor importances for candidate tensors without paying for the full gradients it aims to avoid. This makes the paper stronger than a routine PEFT variant but weaker than a fully validated efficient-training systems paper; the reported wall-clock gains are encouraging, yet the algorithmic explanation and baseline rigor do not fully support the strongest claims.

## Suggestions
- Provide an explicit algorithm for each training epoch: when tensor importances are computed, for which tensors, using which gradients/updates, and how frozen tensors receive updated importance estimates.
- Add a cost breakdown showing whether importance evaluation requires full backward propagation or only selected backward propagation.
- Fully specify and tune LoRA and Prefix-Tuning baselines, including LoRA rank/alpha/dropout/target modules and prefix length/initialization.
- Qualify the “64% FLOPs reduction without noticeable accuracy loss” claim and distinguish best-case results from model/task-dependent failures.
- Validate the FLOPs predictor by sampling tensor masks and comparing predicted FLOPs to profiler-measured FLOPs/time.
- Add random/static/cost-aware selection baselines to isolate the contribution of the importance metric and DP solver.
- Rephrase small improvements over Full FT as “comparable” unless supported by multi-seed variance.

## Score and Decision
I calibrated this paper against the following retrieved human-review anchors:

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gEwKAZZmSw.md`, avg score 6.50, Accept — similar efficient-backpropagation topic; stronger because reviewers viewed the method as more clearly justified and broadly evaluated, though they also wanted wall-clock validation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bsFWJ0Kget.md`, avg score 6.25, Accept — PEFT/LoRA efficiency anchor with adaptive allocation; comparable topic, but the present paper has a larger unresolved cost-accounting issue.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/gTwRMU3lJ5.md`, avg score 7.33, Accept — strong LoRA optimization anchor; stronger empirical/theoretical positioning than the current submission.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/s7DkcgpRxL.md`, avg score 6.20, Accept — efficient LoRA training anchor; current paper is more novel in targeting activation-gradient cost but less fully specified.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GbgCRJedQ7.md`, avg score 6.20, Accept — sparse PEFT anchor; comparable efficiency motivation, but current paper has more serious unresolved selection-cost ambiguity.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3ylNuZXtMg.md`, avg score 4.25, Reject — LoRA efficiency critique anchor; current paper is more constructive and empirically developed, so it should score above this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5HCnKDeTws.md`, avg score 6.75, Accept — empirical LLM fine-tuning study; broader/cleaner empirical support than the current paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/aW7XcFocYr.md`, avg score 5.00, Reject — efficient sparse training with FLOPs reductions but weak practical validation; close in weakness pattern to this paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/z1nSpA2dAW.md`, avg score 5.75, Accept — efficient forward-learning anchor; less topically close but indicates that efficiency papers with some validation gaps can be borderline-positive.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zfeso8ceqr.md`, avg score 6.00, Accept — optimizer-efficiency paper with broad empirical comparisons; stronger baseline/tuning rigor than this submission.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/MLhquJb1qN.md`, avg score 5.25, Reject — tuning/scaling paper with hyperparameter/baseline issues; similar concern pattern.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TwJrTz9cRS.md`, avg score 8.00, Accept — high-quality PEFT anchor with consistent improvements and ablations; current paper is clearly below this due to unresolved methodology.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/NjNfLdxr3A.md`, avg score 7.25, Accept — strong PEFT efficiency anchor; current paper is less mature.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6PmJoRfdaK.md`, avg score 7.00, Accept — efficient long-context LoRA anchor; stronger practical validation than the current submission.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LvNROciCne.md`, avg score 7.00, Accept — memory-efficient LLM training anchor; current paper’s core cost mechanism is less convincingly specified.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9BiVepgmWW.md`, avg score 7.00, Accept — low-rank zeroth-order PEFT anchor; stronger acceptance-level positioning.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/d4UiXAHN2W.md`, avg score 6.33, Accept — lightweight instruction-tuning anchor; current paper is competitive in ambition but less polished methodologically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/EQZMx8Lc0n.md`, avg score 5.00, Reject — PEFT method with broad claims but baseline/novelty concerns; similar overall quality band.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DLJznSp6X3.md`, avg score 5.75, Accept — ReLoRA anchor; current paper is somewhat below due to the central importance-cost ambiguity.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/RbKThNNFxr.md`, avg score 5.33, Reject — memory-efficient LoRA anchor with unresolved validation issues; similar but the current paper has a more novel target.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zcx6rIMbbR.md`, avg score 5.40, Reject — efficient quantized fine-tuning anchor; comparable borderline quality.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/iEUZMISIKj.md`, avg score 4.75, Reject — SwitchLoRA anchor; current paper is slightly stronger because it reports wall-clock and tensor-level cost modeling.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/lR7rqLtsXZ.md`, avg score 5.75, Reject — efficient training anchor with unresolved concerns; comparable upper-borderline.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PPjpGTPG5K.md`, avg score 5.33, Reject — PEFT routing anchor; similar borderline rejection band.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7X65yoKl3Y.md`, avg score 3.33, Reject — low-scoring LoRA variant with weak reasoning and baseline issues; current paper is substantially better than this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6nZwOYDcQx.md`, avg score 4.00, Reject — low-scoring PEFT method; current paper is stronger due to clearer motivation and empirical cost results.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nb9DiBUt7c.md`, avg score 4.00, Reject — low-scoring PEFT complexity-reduction anchor; current paper is above this band.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/VpeAsLmcvg.md`, avg score 3.75, Reject — low-scoring theoretical LoRA-style anchor; current paper has stronger empirical evidence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/LWvgajBmNH.md`, avg score 4.00, Reject — low-scoring mixture-of-LoRA anchor; current paper is more compelling.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/igGeaxOiFM.md`, avg score 3.00, Reject — weak PEFT anchor; current paper is clearly above it.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bYsieh8LE2.md`, avg score 3.67, Reject — weak PEFT generalization anchor; current paper is stronger.

Relative to these anchors, this paper is above the clearly weak PEFT submissions in the 3–4 range because it has a real systems insight, end-to-end timing, and meaningful empirical results. However, it is below the 6–7 accepted efficient-training/PEFT anchors because the core adaptive-selection mechanism is not sufficiently specified, the PEFT baselines are not convincingly tuned, and the strongest FLOPs/no-loss claims are overgeneralized. I therefore place it in the borderline-reject range.

**Score: 5.0 / 10**  
**Decision: Reject**

MY FINAL SCORE: <pineapple>5.0</pineapple>  
MY FINAL DECISION: <orange>Reject</orange>