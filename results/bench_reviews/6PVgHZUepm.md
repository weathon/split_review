## Summary
The paper proposes Rep-Adapter, a two-branch adaptation module for pretrained ConvNets/visual encoders: one branch keeps pretrained weights frozen, the other is trainable, and learned per-filter/channel scaling combines the two. The key practical contribution is that the two branches can be merged after training into a single convolution/linear layer, giving no additional inference-time parameters or compute, and the paper evaluates this approach across classification transfer, CLIP few-shot transfer, semi-supervised ImageNet, detection, and segmentation.

## Strengths
- **Practical zero-extra-inference adaptation mechanism.** Section 3.2 derives an explicit merge rule, e.g. \(\widetilde{w}=\mathrm{diag}(\delta)w_0+\mathrm{diag}(\zeta)w^\mathcal{R}\), after Conv-BN folding. This is a concrete deployment advantage: the method uses extra training-time structure but produces a standard single-branch model at inference.
- **Simple and plausible adaptation design.** The frozen pretrained branch plus trainable branch is an effective way to retain pretrained information while allowing task-specific movement; the ablation in Section 4.8(f) supports the importance of keeping the frozen branch fixed, since making it learnable drops performance toward fine-tuning.
- **Broad empirical coverage.** The paper evaluates many-shot and 1000-example transfer on VISSL/VTAB-style datasets, 16-shot CLIP transfer, semi-supervised ImageNet with 1%/10% labels, and downstream detection/segmentation. This breadth is unusually strong for an adaptation-method paper.
- **Empirical gains over standard transfer baselines.** In Section 4.2, the authors report Rep-Adapter outperforming linear probing and fine-tuning in 37/42 many-shot scenarios, with average PIRL gains of 16.1% over linear probing and 1.4% over fine-tuning. Section 4.3 similarly reports low-shot gains.
- **The paper does include some stronger adaptation-method comparisons.** Section 4.4/Table 4 compares against LoRA, VPT, \(L^2\)-SP, DELTA, AutoLR, and SpotTune, not only linear probing and vanilla fine-tuning. This partially addresses the concern that the method is evaluated only against weak baselines.
- **Ablations are meaningful.** Table 8 probes learnable frozen-branch scaling, joint vs. iterative optimization, BN statistics, BN placement, pretrained initialization, and freezing of the frozen branch. These ablations help identify which parts of the design matter, even if they do not fully validate the paper’s learning-rate interpretation.

## Weaknesses

### Fatal
None.

### Major
- **The central “automatic per-filter learning-rate optimization” interpretation is not established for the actual algorithm.** The paper claims that Rep-Adapter “simulates a model fine-tuning with adaptive learning rate for each filter” and that “the optimization of lr can be relaxed to the optimization of \(\zeta\)” (Sections 3.3–3.4). Proposition 3.1 only shows a one-step equivalence for a linear layer when \(\zeta_i=\sqrt{\eta_i/\eta_m}\) is chosen to match a desired per-filter learning rate. The actual method jointly optimizes \(\zeta,\delta,\omega^\mathcal{R}\) by ordinary backpropagation, where \(\zeta\) is a model parameter affecting the forward function, not a bilevel hyperparameter governing update rules. The proof also does not cover nonlinear networks, BN with batch statistics, momentum/Adam/weight decay, heads, or interactions across layers. This does not invalidate the engineering method, but it substantially weakens the paper’s main explanatory and “automatic learning-rate” claim.
- **The experiments do not fully isolate the claimed automatic protocol-selection advantage.** The paper is empirically broad and includes comparisons to several adaptation methods, but the central claim is stronger than “a good transfer recipe”: it claims to avoid tedious learning-rate/protocol search and automatically balance fine-tuning and linear probing. To establish that, the relevant comparison would be a validation-selected or well-tuned family of transfer protocols under matched search/compute: linear probing, full fine-tuning, partial freezing, layer-wise learning-rate decay, tuned weight decay/regularization, early stopping, and perhaps simple frozen-residual/two-branch controls. Table 4 helps, but the main text is too compressed to show comparable tuning budgets and fair search accounting for all methods.
- **The breadth of low-shot/few-shot/semi-supervised claims is stronger than the reported uncertainty supports.** The main low-shot, CLIP few-shot, and semi-supervised tables appear to report single numbers, while only the ablation table reports mean/std over multiple trials. Since 1000-example transfer and 16-shot CLIP adaptation can be sensitive to sampled examples, seed, validation split, augmentation, and early stopping, variance matters—especially where gains are modest. This does not erase the empirical signal, but it weakens claims of consistent superiority across data-scarce regimes.

### Minor
- **“Parameter-free” is overstated unless consistently qualified as inference-time only.** The title/abstract call the method “parameter-free automatic adaptation,” but during adaptation the method uses an additional trainable branch plus learnable scaling/BN parameters and produces task-specific merged weights. The paper often correctly says “without introducing additional parameters during inference,” but the broader “parameter-free” phrasing should be tightened to avoid conflating inference efficiency with training/adaptation cost.
- **The CLIP comparisons mix different adaptation mechanisms and deployment assumptions.** Rep-Adapter modifies/fine-tunes the visual encoder during training, while CoOp and Tip-Adapter adapt prompt/cache-style components. Reporting the comparison is useful, but the conclusion should be framed as empirical transfer performance rather than a clean like-for-like comparison of adaptation mechanisms.
- **The detection/segmentation batch-size conclusion is too broad.** Table 7 is a useful stress test beyond classification, but the statement that these experiments show the method is “not limited by the batch size” is stronger than what is demonstrated. The results show that it works in the reported small-batch detection/segmentation settings, not general batch-size robustness.
- **The ablations do not directly test the claimed learned-learning-rate mechanism.** Table 8 supports the importance of the frozen branch, BN design, and pretrained initialization, but it does not show that learned \(\zeta\) behaves like an explicit per-filter or per-layer learning-rate schedule. The gains may instead arise from regularization, preserved pretrained features, BN effects, or overparameterized training dynamics.

### Trivial
None.

## Nice-to-Haves
- Add a validation-selected transfer-protocol baseline that chooses among linear probing, full fine-tuning, partial freezing, layer-wise LR decay, and regularized fine-tuning under the same validation/search budget.
- Report seed/split means and standard deviations for the main low-shot, few-shot, and semi-supervised results, not only for ablations.
- Visualize learned \(\zeta,\delta\), effective layer-wise weight movement \(\|\widetilde{\omega}-\omega_0\|\), and adaptation strength on datasets where linear probing vs. fine-tuning behaves differently.
- Compare against explicit per-layer/per-filter LR schedules or post-hoc schedules matched to learned scaling values to test whether the learning-rate interpretation predicts behavior.
- Provide clearer training-time memory/compute and hyperparameter-search accounting relative to fine-tuning, adapters, AutoLR, and dynamic routing methods.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **“The paper only compares to linear probing and fine-tuning.”** Removed as stated because it is factually incomplete. Section 4.4/Table 4 compares against LoRA, VPT, \(L^2\)-SP, DELTA, AutoLR, and SpotTune. A weaker version remains: the paper still needs better search-budget and tuned-protocol comparisons for its automatic-adaptation claim.
- **Strength claim: “The paper provides a theoretical link that directly supports the main automatic learning-rate claim.”** Removed/strongly weakened. Proposition 3.1 gives a limited one-step linear equivalence under chosen fixed scaling, but it does not justify the actual joint optimization of \(\zeta,\delta,\omega^\mathcal{R}\) as bilevel learning-rate optimization.
- **Strength claim: “Joint optimization approximates adaptive learning-rate behavior.”** Removed as an unsupported interpretation. Table 8(b) shows joint and iterative optimization have comparable performance, but not that either is learning optimal learning rates.
- **Generic strength that the paper addresses an important problem.** Removed as too generic. The retained strengths focus on concrete method design, merge equations, empirical coverage, and ablations.
- **Formatting/wording artifacts from the extracted PDF.** Removed under the parser-artifact rule; no typos or PDF extraction issues are considered part of the evaluation.

## Novel Insights
The most important synthesis is that the paper is much stronger as a practical reparameterizable frozen-plus-trainable adaptation method than as a theory of automatic learning-rate optimization. The empirical and ablation evidence supports the idea that preserving a frozen pretrained branch during training and merging it afterward is useful, but the evidence does not establish that the learned scalings are equivalent to learned per-filter learning rates or that the method solves automatic transfer-protocol selection. Reframing the contribution around mergeable adaptation and pretrained-feature preservation would make the paper substantially more defensible.

## Suggestions
- Rephrase the main theoretical claim: “fixed scaling can mimic one step of filter-wise LR scaling in an idealized linear layer” rather than “Rep-Adapter jointly optimizes learning rates and model parameters.”
- Add a direct mechanistic analysis of learned scaling factors and effective weight movement across layers/datasets.
- Include a matched search-budget comparison against a validation-selected suite of common transfer protocols.
- Add uncertainty estimates for low-shot/few-shot/semi-supervised tables.
- Separate claims about **training-time adaptation cost**, **task-specific storage**, and **inference-time cost**. The strongest claim is “no extra inference parameters/compute after merging.”
- For CLIP experiments, state clearly that Rep-Adapter adapts the visual encoder, while prompt/cache methods adapt different components; avoid implying all methods solve identical deployment constraints.
- Replace the broad batch-size robustness claim with the narrower supported statement that Rep-Adapter works in the reported small-batch detection/segmentation settings.

## Score and Decision
**Originality:** Good. The frozen-plus-trainable reparameterizable branch design is simple but practically valuable, especially with exact inference-time merging.  
**Importance:** Good. Transfer adaptation without inference overhead is useful to the vision community.  
**Support for claims:** Mixed. The empirical claim that the method performs well is reasonably supported; the theoretical/automatic-learning-rate claim is overextended.  
**Experimental soundness:** Good breadth, but missing uncertainty in data-scarce settings and insufficient search-budget accounting for the strongest “automatic protocol selection” claim.  
**Clarity:** Generally clear, but the theory-to-algorithm interpretation is misleading.  
**Community value:** Positive, especially if reframed as an effective mergeable adaptation recipe.

### Calibration anchors considered
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Fb93MfxX7T.md` — Avg 4.75, Reject: a PETL empirical study; Rep-Adapter appears more methodologically concrete and empirically stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/RxQOKupaui.md` — Avg 5.00, Reject: adapter-placement work with interesting findings but practicality/search concerns; Rep-Adapter is stronger due to exact inference merging and broader experiments.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TVg6hlfsKa.md` — Avg 7.25, Accept: strong adaptation paper with excellent task-specific results; Rep-Adapter is broader but less convincing mechanistically/theoretically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bJx4iOIOxn.md` — Avg 7.50, Accept: strong transfer-learning analysis with credible insights; Rep-Adapter has a useful method but its central explanatory claim is less well supported.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/FItPCl4uEc.md` — Avg 5.25, Reject: transfer method with concerns about evidence/contribution; Rep-Adapter is somewhat above this due to broader positive results and ablations.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/3rmpixOjPS.md` — Avg 7.20, Accept: reparameterization method with no inference overhead; Rep-Adapter shares this practical strength but has more overclaiming around theory.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hWjPRRyiqm.md` — Avg 5.33, Reject: CLIP/video adaptation with concerns; Rep-Adapter is stronger in breadth and ablations.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/rkAqvDnnmO.md` — Avg 5.25, Reject: multi-adapter/incremental-learning adaptation; Rep-Adapter is more convincing for its stated transfer setting.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/fWNHKHh0Yn.md` — Avg 4.20, Reject: optimizer paper with weak theory-practice link and marginal gains; Rep-Adapter has a similar theory-practice mismatch but much stronger empirical breadth and practical contribution.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9mX0AZVEet.md` — Avg 6.00, Reject: useful method with theory-practice mismatch; Rep-Adapter is comparable in score range, with stronger engineering value but similarly overclaimed interpretation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/55EO8gSCBT.md` — Avg 5.50, Reject: broad empirical study with unsupported conclusions and variance concerns; Rep-Adapter is slightly above due to concrete method and deployment benefit.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GqI4fTVUXC.md` — Avg 6.00, Reject: strong empirical/theoretical investigation tempered by theory-practice concerns; similar caution applies here.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/R6klub5OXr.md` — Avg 5.25, Reject: broad experiments but conclusions not fully supported; Rep-Adapter’s practical contribution is more direct.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Ok7ZH2Cyd7.md` — Avg 4.20, Reject: broad but insufficiently supported methodological framing; Rep-Adapter is clearly stronger empirically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/vJkktqyU8B.md` — Avg 6.00, Accept: ViT adapter paper for dense prediction; Rep-Adapter is in a similar acceptance-borderline range.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/YNbLUGDAX5.md` — Avg 6.00, Accept: progressive adaptation for segmentation; Rep-Adapter is comparable in practical adaptation value.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/5btFIv2PNb.md` — Avg 6.33, Accept: low-rank visual prompting adaptation; Rep-Adapter is similar but penalized for overclaimed theory.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/29sul3tAEa.md` — Avg 4.80, Reject: HyperAdapter with practicality/evidence concerns; Rep-Adapter is stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bC50ZOyPQm.md` — Avg 5.00, Reject: recurrent adaptation of large transformers; Rep-Adapter’s inference merge and broad experiments place it above this.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/u6vC7KaFel.md` — Avg 4.75, Reject: HyperLoRA-style adaptation with limited support; Rep-Adapter is stronger empirically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/TxIrMD6lAN.md` — Avg 3.00, Reject: adapter method with severe novelty/baseline issues; Rep-Adapter is far above this low anchor.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jqx5XI4Yr3.md` — Avg 3.40, Reject: adapter method with weak support; Rep-Adapter is much stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ebnyMCM63m.md` — Avg 4.00, Reject: adapter reverse-engineering method with substantial weaknesses; Rep-Adapter is above this due to clearer method and experiments.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zvoM1Wastw.md` — Avg 3.50, Reject: transfer adapter for quantile regression with weak support; Rep-Adapter is much stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bYsieh8LE2.md` — Avg 3.67, Reject: universal LoRA-style adapter with weak evidence/generalization; Rep-Adapter is much better supported.

Relative to these anchors, this paper is clearly stronger than the low and medium-low adapter papers because it has a concrete deployable mechanism, broad experiments, and meaningful ablations. It is below the stronger 7+ anchors because its core theoretical framing is overclaimed and the experiments do not fully validate automatic protocol selection. I therefore place it in the borderline-to-positive range.

**Score: 6.0**  
**Decision: Accept**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>