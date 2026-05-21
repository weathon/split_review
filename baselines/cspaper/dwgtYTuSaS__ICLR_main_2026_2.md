---
job_id: 9d8c270d-8d1c-41ed-9133-31de99c81dc6
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: dwgtYTuSaS.pdf
paper: Continuous Online Action Detection from Egocentric Videos
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining representation learning for video, online/continual learning, and a new benchmark for egocentric action detection.

## Minimum Quality
Pass ✅. The paper contains the necessary scientific components, including abstract, introduction, related work, methodology, experiments, results, and conclusion, and it presents a coherent empirical study even though there are several important concerns about novelty, evaluation design, and methodological clarity.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper introduces Continuous Online Action Detection (COAD), a task setting in which an online action detector is not only evaluated causally at inference time but is also updated continuously from a temporally ordered video stream under single-pass, no-replay constraints. The paper also constructs Ego-OAD, a new egocentric OAD benchmark derived from Ego4D MQ, and proposes a simple COAD training recipe built from three ingredients, state continuity, orthogonal gradient projection, and non-uniform loss on the last step of each training window. Experiments on Ego-OAD and EPIC-KITCHENS compare this recipe against a pretrained-only model and a variant without the proposed COAD components.

## Strengths
1. **Timely problem setting with a plausible deployment motivation.** The paper makes a reasonable case that standard OAD training, which relies on shuffled offline windows, is mismatched with wearable-device deployment where data arrive as a stream and environments are user-specific. Framing adaptation in a causal, single-pass, no-storage regime is practically relevant, especially for egocentric video.

2. **The benchmark effort is useful and likely to be of independent interest.** Ego-OAD appears to be substantially larger and more diverse than existing egocentric OAD testbeds, with 263 hours, 87 classes, and multi-label frame-wise annotations derived from Ego4D MQ. The examples in **Figure 1** make the data characteristics tangible, especially the presence of overlapping actions and long untrimmed streams, which are genuinely appropriate for an online detection setting.

3. **The method is simple and implementation-oriented.** I appreciate that the proposed training strategy is not buried under unnecessary complexity. The decomposition into state continuity, orthogonal gradients, and non-uniform loss is easy to understand from **Figure 2**, and the design choice of keeping the backbone frozen while adapting the lightweight temporal head is aligned with the stated on-device motivation.

4. **Some empirical gains are non-trivial on Ego-OAD.** In **Table 1**, the out-of-stream Top-5 recall improvements from COAD over Pretrained Only are fairly large, especially for Ego pretraining, from 69.1 to 76.0, and for Exo pretraining, from 55.5 to 62.0. This suggests that the continuous adaptation protocol may indeed help robustness to new scenarios, at least on this benchmark.

5. **The ablation table is informative, even if incomplete.** **Table 3** does at least attempt to separate the contribution of the three ingredients. The pattern that non-uniform loss helps out-of-stream performance while sometimes hurting in-stream adaptation is interesting and points to a meaningful adaptation-vs-generalization tradeoff.

6. **The paper includes useful visual diagnostics.** **Figure 3** is a good choice, because it does not just report one number but explicitly visualizes the in-stream versus out-of-stream tradeoff as stride and learning rate vary. Likewise, **Figure 4** supports the claim that out-of-stream performance tends to improve over the course of streaming adaptation.

## Weaknesses
1. **The core novelty is narrower than the framing suggests, and the paper does not convincingly establish COAD as a distinct scientific task rather than a specific training protocol.**  
   The main methodological ingredients in Section 4.5 are imported from prior directions rather than newly derived for OAD: continuous streaming training, state continuity for recurrent models, orthogonal gradient projection, and last-step loss weighting. What is new here seems to be their combination for egocentric OAD plus a benchmark. That can still be publishable, but the paper repeatedly presents COAD as a new task formulation. I am not fully convinced this is more than a constrained training and evaluation protocol layered on top of standard OAD. The distinction matters because task papers need especially crisp definitions of what is fundamentally new, what assumptions differ from prior OAD or streaming video learning, and why this warrants a new benchmark and terminology rather than a variant of online adaptation for OAD. As written, the paper overstates the conceptual separation.

2. **The empirical comparison is too weak to support the breadth of the claims. Key baselines are missing.**  
   The main comparisons in Section 5 are against only two baselines: "Pretrained Only" and "w/o COAD". That is far too narrow for a paper whose central claim is that a new continuous training setting materially advances OAD. In particular, the "w/o COAD" baseline is simply the same model trained on in-stream data without the three added strategies, which is not a strong external baseline. There is no comparison to stronger OAD architectures cited in the related work, such as LSTR, TeSTra, OADTR, or other modern causal temporal models, nor to simple online finetuning variants like smaller learning rates, truncated BPTT variants, EMA teachers, or regularized adaptation methods. This matters because the paper’s conclusion currently conflates two possibilities: either COAD is genuinely effective, or the chosen baseline is simply weak and unstable under streaming finetuning.

3. **The EPIC-KITCHENS results are mixed to the point that they undercut the generality claim.**  
   In **Table 2**, the adaptation story is not consistently positive. For in-stream performance, COAD does not clearly improve over Pretrained Only, and in several cases it is worse, for example Action Top-5 recall is 20.5 versus 22.9, and Action mAP is 7.9 versus 9.6. The paper acknowledges this in Section 5.3, but the discussion is too quick and too convenient. If the method is supposed to be a general training paradigm for continuous OAD, then a second dataset where adaptation largely fails should trigger a more serious analysis of when the method works, why it fails, and whether Ego-OAD is unusually favorable. Right now the paper presents positive headline numbers from Ego-OAD while the cross-dataset evidence is substantially weaker.

4. **The benchmark curation process raises validity concerns that are not fully quantified.**  
   Section 3 states that all annotation passes are merged and each frame is assigned the union of all overlapping labels, after which semantically similar free-form labels are manually grouped into 87 classes. This is a strong intervention in the label space. It may be necessary, but the paper does not quantify its consequences rigorously. For example, how much disagreement exists before merging, how often do multiple labels per frame arise from genuine simultaneity versus annotator disagreement, how sensitive are results to the manual grouping, and what is the inter-annotator consistency after mapping? The class distribution and duration histograms in **Figures 7 and 8** help characterize imbalance and temporal extent, but they do not address annotation reliability. Since the benchmark is one of the key claimed contributions, this missing analysis matters a lot.

5. **There is a potentially serious evaluation-design issue around hyperparameter selection and split usage.**  
   In Section 5.1, the out-of-stream set is described as "held-out data reserved for evaluation only", yet Section 5.4 analyzes learning rate and stride tradeoffs using out-stream performance in **Figure 3**, and **Figure 4** tracks out-of-stream performance over training. This by itself is fine for reporting, but the paper never states what data were used for hyperparameter tuning or model selection. There is no explicit validation split. If the reported stride and learning rate were selected based on out-of-stream performance, then the "held-out" nature of that split is compromised. This is not a minor procedural detail, because the whole paper hinges on out-of-stream generalization gains. The authors need to state clearly whether all hyperparameters were fixed a priori, chosen on a separate validation subset, or tuned on the reported out-of-stream test set.

6. **The mathematical formulation is under-specified in several places, and the optimization story is much less complete than it should be for a method paper.**  
   A few examples:
   - In Section 4.3, the paper first says the backbone is pre-trained on trimmed clips $\tilde{x} \subset V$, but then writes $z_t = \Phi(x_t)$, where $x_t \in \mathbb{R}^{H\times W\times 3}$ is a single frame. This is inconsistent with the implementation in Section 5.2, where TimeSformer uses 8-frame clips and TSN uses 6-frame chunks. So the notation in Equations around Sections 4.2 to 4.4 blurs frame-level and clip-level inputs. The model should define whether $t$ indexes frames, clips, or stride positions, because this affects causality and temporal resolution.
   - The orthogonal-gradient update in Section 4.5 defines
     $$
     g_t^\perp = g_t - \frac{\langle g_t, g_{t-1}\rangle}{\|g_{t-1}\|^2} g_{t-1}.
     $$
     But the paper does not state what happens when $\|g_{t-1}\|^2 = 0$ or is numerically tiny, whether projection is done over the full parameter vector or only the GRU head, and whether gradients are computed before or after truncation through the recurrent state. These details materially affect stability.
   - The "non-uniform loss" is described only verbally as computing loss on the final step of each window. That is not enough. The paper should write the actual objective, for example something like
     $$
     \mathcal{L} = \sum_{t \in \mathcal{T}} \ell(\hat{y}_t, y_t),
     $$
     where $\mathcal{T}$ are only window-end indices, and specify the exact multi-label loss, presumably binary cross-entropy, class weighting, thresholding, and handling of background. Given the severe class imbalance shown in **Figure 7**, omitting these details is not acceptable.
   These issues are not just cosmetic. They make it harder to assess what was actually optimized and whether the method is reproducible.

7. **Some of the claimed component effects are overstated relative to the ablation evidence.**  
   In Section 5.4 the text says "Table 3 presents an ablation of COAD's components, each contributing to performance." That is not really what **Table 3** shows. State continuity appears to have almost no effect: the full model gives 26.0 / 36.8 mAP out/in, while removing state continuity gives 25.9 / 36.7. That difference is negligible. Orthogonal gradients help out-of-stream recall more clearly, but again the effect is moderate relative to the total gain over Pretrained Only. The strongest signal seems to be from non-uniform loss. The paper should be more honest here: not all components contribute equally, and one of them may barely matter for this setup.

8. **The headline claims rely heavily on Top-5 recall, while mAP improvements are less consistently compelling.**  
   The abstract emphasizes "up to 20% in top-5 accuracy" and "up to 7%" generalization improvement, but the more standard detection metric here is per-frame mAP. In **Table 1**, for in-stream Ego pretraining, COAD actually lowers mAP relative to w/o COAD, 36.8 versus 39.0, despite improving Top-5 recall. Likewise for Exo in-stream, mAP is unchanged at 31.0 while Top-5 recall improves. This pattern suggests the method may be improving candidate ranking breadth more than calibrated detection quality. That distinction is important in online action detection, and the paper does not analyze it. The claims should be phrased more carefully.

9. **The visual evidence is selective and only partially convincing.**  
   **Figure 5** and **Figure 6** show only the top predicted class over time, despite the task being multi-label and overlapping by construction. This visualization choice hides failure modes, especially because Section 3 states that 36% of action instances overlap. For a multi-label benchmark, showing only argmax predictions is a weak diagnostic. A more faithful figure would visualize multiple active labels or at least confidence traces for the relevant classes. As it stands, the qualitative section supports the narrative but not the actual complexity of the task.

10. **The on-device and resource-constrained motivation is not matched by concrete efficiency measurements.**  
    The paper repeatedly motivates COAD via wearable devices and on-device training, yet there are no measurements of memory use, update latency, FLOPs, energy, or even wall-clock throughput. **Figure 2** presents the method as suitable for streaming deployment, but this is asserted rather than demonstrated. Since the approach uses recurrent updates plus online backpropagation over 128-step windows, the practicality claim should be backed by actual runtime or memory numbers, at least for the GRU head.

11. **The writing is understandable overall, but there are enough inconsistencies and small errors to reduce confidence.**  
    There are naming inconsistencies, for example COAD is introduced in the title and abstract, but Section 4 says "CODA" once, and the contribution bullet says "Countinuous" instead of "Continuous". Section 4.5 begins "enabling the model to continuous video streams", which is incomplete. The results text also says "Table 1 confirm the trends observed for Ego-OAD" when it clearly means **Table 2** for EPIC-KITCHENS. These are fixable, but they add to the impression that the paper is not fully polished.

## Questions
1. **How were hyperparameters selected?**  
   Please state explicitly whether learning rate, stride, window size, and any other training choices were tuned using a separate validation set. If not, and if out-of-stream performance informed these choices, then the reported generalization numbers are optimistic. A precise answer here would significantly affect my confidence.

2. **Can the authors provide a stronger baseline suite?**  
   At minimum, I would like to see comparisons against a stronger causal OAD model or a stronger online adaptation baseline, not just "w/o COAD". Even a rebuttal discussion clarifying why such baselines were infeasible, plus evidence that the current baseline is competitive under the same backbone/features, would help.

3. **Please clarify the exact training objective mathematically.**  
   What is the precise multi-label loss, how is background handled, are there class weights, what thresholds are used at evaluation, and how exactly is non-uniform loss instantiated? Writing the full objective would resolve a lot of ambiguity in Section 4.5.

4. **What is the exact temporal indexing unit in the model equations?**  
   Are $x_t$ and $z_t$ frames, clips, or stride-aligned chunks? How do the equations map onto the TimeSformer setting with 8-frame clips and stride 2 versus the training window stride 16? This is important for understanding causality and effective context size.

5. **How robust are results to the manual label grouping used in Ego-OAD?**  
   It would strengthen the dataset contribution to report statistics on annotator disagreement before and after grouping, or some sensitivity analysis showing that the main conclusions do not depend heavily on the chosen label mapping.

6. **Can the authors explain the metric discrepancy between mAP and Top-5 recall?**  
   In **Table 1**, COAD often improves Top-5 recall more than mAP, and sometimes reduces in-stream mAP relative to w/o COAD. Why does the method help one metric more than the other? Is it improving recall at the expense of calibration or precision?

7. **Do the authors have any measurements supporting the on-device motivation?**  
   Even simple numbers for update time, memory footprint, and trainable parameter count of the temporal head would help justify the repeated deployment claims.

8. **Why does adaptation fail or plateau on EPIC-KITCHENS?**  
   The current explanation in Section 5.3 is speculative. Can the authors provide evidence, for example recurrence statistics, class repetition frequency, or qualitative failure modes, to explain why the method transfers poorly there?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the main paper. The work uses existing egocentric datasets and proposes a benchmark/method for action understanding. I do note that wearable egocentric systems can raise privacy and surveillance concerns in deployment, but the paper itself does not introduce a new data collection protocol or release sensitive personal information in the provided text.

## Soundness Rating
2: fair. The empirical study is reasonably extensive for the proposed setting, but the evidence does not fully support the stronger claims, the baseline suite is limited, and important methodological details around the objective and evaluation protocol remain under-specified.

## Presentation Rating
2: fair. The paper is readable and the figures/tables are generally helpful, but there are multiple notation inconsistencies, some textual errors, and several places where crucial details are described only informally.

## Contribution Rating
2: fair. The benchmark effort is useful and the problem motivation is relevant, but the methodological contribution is incremental, the task framing is not fully differentiated from existing streaming adaptation setups, and the empirical validation is not strong enough to establish a clear ICLR-level advance.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is promising and practically motivated, with a potentially useful benchmark and some encouraging Ego-OAD results, but the current version does not yet make a sufficiently strong case on novelty, baseline strength, protocol rigor, and methodological clarity for ICLR main track.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with online action understanding and streaming/continual learning settings, and I checked the technical details and experimental evidence carefully.