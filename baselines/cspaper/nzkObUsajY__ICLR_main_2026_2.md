---
job_id: 3a8610db-c92c-48ab-8206-b163b8c02f83
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: nzkObUsajY.pdf
paper: How to Get Spiking LLMs? A Dual ANN-to-SNN Conversion with Layer-Wise Calibration
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies ANN-to-SNN conversion, efficient deployment of large language models, and representation/inference efficiency for language models.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodology, experiments with quantitative results, and conclusion; although there are important clarity and rigor issues, they do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I do not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes a dual ANN-to-SNN conversion framework for large language models, where the starting point is a statically quantized LLM rather than a specially retrained conversion-friendly ANN. The method introduces an integer spiking neuron with multi-hierarchical thresholds to emulate symmetric quantization, and then applies a parameter-efficient layer-wise calibration of thresholds and initial membrane potentials to reduce conversion error, especially unevenness error. Experiments on LLaMA-2-7B and LLaMA-3-8B under W6A6 quantization show that the calibrated spiking models recover much of the performance lost by naive conversion.

## Strengths
1. The paper tackles a timely and nontrivial problem, namely how to obtain spiking versions of modern LLMs without retraining a dedicated conversion-friendly ANN. That problem setup is interesting and practically motivated, particularly because conventional ANN-to-SNN conversion pipelines do not scale gracefully to LLMs.

2. The proposed framing is conceptually clean. The shift from “train an ANN for conversion” to “convert a quantized LLM, then calibrate the SNN” is easy to understand, and **Figure 1** communicates this difference well. In particular, **Figure 1(a)** vs **Figure 1(b)** makes the paper’s central claim concrete: the proposed pipeline removes the tailored-ANN retraining stage and inserts calibration after conversion. This figure is one of the clearer parts of the paper.

3. The neuron design in Section 3.2.2 is at least a meaningful engineering contribution. Using an integer spiking neuron with multi-level thresholds to mimic the symmetric quantization rule in **Equation (7)** is a sensible design choice for quantized LLMs, and the construction in **Equations (8)-(10)** is reasonably aligned with that goal.

4. The paper does make an effort to reason about where conversion error comes from, rather than presenting the method as a black box. The decomposition into clipping, quantization, and unevenness error in Section 3.3 is useful, and **Figure 3** provides some empirical support for the claim that unevenness error is the main source of degradation after conversion. The figure is not merely decorative, it helps motivate why calibration is needed.

5. The main empirical result, shown in **Table 2**, is genuinely encouraging. For both LLaMA-2-7B and LLaMA-3-8B, the gap between the naive “Conversion” rows and the calibrated “Ours” rows is large for \(T>1\). For example, on LLaMA-2-7B at \(T=4\), average accuracy improves from 50.26 to 67.04, and perplexity improves from 97.76 to 9.71. That is a substantial recovery. Whatever one thinks of the broader claims, the calibration stage appears to matter materially.

6. The parameter-efficiency angle is also supported by the results. **Table 4** suggests that calibrating only thresholds and initial membrane potentials can outperform or match much heavier layer-wise weight calibration while using dramatically fewer learned parameters. This is one of the stronger empirical messages in the paper.

## Weaknesses
1. The paper repeatedly leans on edge deployment and energy-efficiency motivation, but the actual evaluation does not substantiate those claims. The introduction and conclusion emphasize low power, edge devices, and reduced energy consumption, yet Section 4 reports only accuracy and perplexity on GPUs. There is no measurement of energy, latency in wall-clock terms, spike sparsity, memory traffic, or hardware-level cost. This matters because SNN papers often justify themselves precisely through efficiency claims, and here that part is mostly asserted rather than demonstrated. The issue is particularly visible in **Table 1**, where latency is summarized simply as “High” for conventional methods and “Low” for the proposed one. That is too coarse to be scientifically useful, and it sets expectations that the experiments do not later satisfy.

2. The “training-free” presentation is overstated. In Section 3.2, the first stage is described as training-free because it starts from a PTQ model, but Section 3.4 then introduces a calibration objective
\[
\min_{\theta^k, v^k(0)} \left\| \sum_t \hat{y}^k(t) - y^k \right\|,
\]
which is clearly an optimization problem over learnable parameters. Even if the number of optimized variables is tiny, this is still a post-conversion learning stage. The paper should be much more precise here and distinguish “no retraining of LLM weights” from “fully training-free.” This matters because the practical appeal of the method depends strongly on how expensive calibration is for 7B/8B models, and the paper does not quantify calibration compute, data, optimization schedule, or runtime in the main text.

3. The theoretical presentation is weaker than the paper claims, and some statements are underspecified or inconsistent. A central issue appears around **Theorem 1**, **Theorem 2**, and their assumptions on the per-step current \(\mathbf{I}^k(t)\). Theorems 1 and 2 require that for every time step, the current lies in one of three intervals, but these intervals are mutually exclusive and exhaustive by construction, so the condition as stated is tautological and does not seem to impose a meaningful restriction. If the intended condition is something stronger, it is not clearly written. Moreover, the main text states \( \mathbf{v}^k(0)=\theta^k/2 \) in Theorem 1 and Theorem 2, while the appendix proof around Page 14 briefly says “if \( \mathbf{v}^k(0)=\theta^k/T \)” before later returning to \( \mathbf{v}^k(0)/\theta^k=0.5 \). That inconsistency is not cosmetic, it directly affects the derivation of equivalence to rounding. For a theory-backed paper, these details need to be watertight.

4. The calibration objective in Section 3.4 is not well matched to the upper bound in **Theorem 3**. The theorem bounds final output error by accumulated layer-wise unevenness and QANN-vs-ANN errors propagated by products of \(\rho^\tau\). But the proposed calibration simply minimizes a local discrepancy \(\left\|\sum_t \hat y^k(t)-y^k\right\|\) layer by layer, with no explicit handling of the propagation factors \(\prod_{\tau=k+1}^K \rho^\tau\), no discussion of ordering effects, and no justification that this greedy procedure approximately minimizes the global bound. In other words, the theorem is used as motivational rhetoric for calibration, but the optimization that follows is only loosely connected to it. This matters because the theory is presented as a key support for the method.

5. The paper’s treatment of nonlinear operations is too dependent on external work, and the main-paper description is incomplete. Section 3.2.3 says that replacing quantization with IS neurons applies only to linear operations, and for LayerNorm, SiLU, Softmax, and activation-activation multiplication the method adopts spiking-compatible operations from prior work. But these nonlinearities are not a side detail in LLaMA, they are central. Since the contribution is a spiking LLM conversion framework, the main paper should explain much more explicitly how much of the end-to-end system is actually new versus inherited. **Figure 2** is visually dense and gives a high-level architecture, but it also reveals the dependence on several imported blocks, especially for attention and MLP nonlinearities. Right now, the reader is left with the impression that the truly novel part may be narrower than the framing suggests.

6. The empirical comparison is not strong enough to establish state-of-the-art spiking LLM conversion. The baselines in Section 4 are PrefixQuant and DuQuant, which are quantization baselines, plus uncalibrated conversion and weight calibration. That is useful, but it leaves a gap: the paper does not compare against other recent spiking-LLM-specific conversion or spike-based LLM approaches. Even if implementation is difficult, the absence of stronger task-matched spiking baselines makes it hard to judge relative progress within the actual target area. As written, **Table 2** mainly shows that calibration recovers performance relative to the authors’ own naive conversion, not that the overall framework is the strongest available route to spiking LLMs.

7. Some of the main empirical claims are weaker than the prose suggests. The abstract says the method achieves performance “comparable to state-of-the-art quantization techniques,” but **Table 2** shows this is only partially true. On LLaMA-2-7B, PrefixQuant average accuracy is 68.70 and the proposed method drops to 67.65, 67.04, and 66.03 for \(T=2,4,8\), with perplexity worsening substantially as \(T\) increases. On LLaMA-3-8B, the gap at \(T=8\) is larger, 63.76 average accuracy vs 70.24 for PrefixQuant, with PPL 18.93 vs 6.90. So the method is competitive at low \(T\), but not uniformly “comparable” across the tested spiking regimes. The paper should state this more honestly.

8. The parameter-size ablation in **Table 3** is interesting but under-analyzed, and arguably contradicts an intuitive monotonicity story. The default setting labeled “-1 (Ours)” uses the smallest parameter size, 0.107K, yet obtains the best average accuracy among the listed settings. Larger parameter budgets do not help and sometimes hurt. This could be an important finding, but the paper gives no serious explanation. Is the calibration landscape unstable with too fine a grouping? Is there overfitting to the calibration set? Is the grouping interacting with activation statistics? Without analysis, the table reads more like an unexplained curiosity than an insightful ablation.

9. There are several clarity and notation issues throughout the paper that make careful checking harder than it should be. A few examples: in **Equation (7)** the denominator appears as \(\lambda\) rather than \(\lambda^k\); Section 3.3 switches between \(a\), \(a_{\max}\), and \(\beta\) in a way that is not fully coherent; **Theorem 3** refers to \(h,g,f\) and layer outputs \(x^k,y^k,\bar y^k,\hat y^k\) without a sufficiently clean notation table in the main paper; and parts of the appendix contain duplicated equations and typographical mistakes. None of these alone is fatal, but together they reduce confidence in the formal presentation.

10. The paper does not report enough calibration details for reproducibility from the main text. Section 4 omits key ingredients such as the amount and source of calibration data, number of optimization steps, optimizer settings, whether calibration is sequential per layer or jointly staged, and how validation/model selection was performed. Since the central empirical gain comes from calibration, these are not minor implementation details.

## Questions
1. Please clarify the computational cost of calibration in the main paper. How many samples/tokens are used, how many optimization steps are run per layer, what optimizer is used, and what is the total wall-clock cost relative to PTQ and to ordinary LLM fine-tuning? A concise table would substantially improve my confidence.

2. Can the authors sharpen the “training-free” claim? If the intended message is “no weight retraining of the source LLM,” please say that explicitly and avoid implying that the whole pipeline is optimization-free.

3. The assumptions and proof path around **Theorem 1** and **Theorem 2** need clarification. In particular, why is the interval condition nontrivial, and which initialization is actually required, \(v^k(0)=\theta^k/2\) or \(v^k(0)=\theta^k/T\)? Please provide a corrected statement if there is a typo.

4. Please explain how the layer-wise objective in Section 3.4 relates operationally to the upper bound in **Theorem 3**. Is calibration performed greedily from shallow to deep layers, and if so, why is that a good surrogate for minimizing the global output discrepancy?

5. Stronger evidence on efficiency would help materially. Even a simple analysis of spike rate, number of additions versus multiplications, estimated activation sparsity, or measured end-to-end energy/latency on suitable hardware would make the deployment motivation much more convincing.

6. Can the authors compare against a stronger spiking-LLM-specific baseline, or at least discuss more concretely how the proposed method differs from and improves upon prior spiking LLM conversion pipelines? This would help calibrate the contribution more fairly.

7. **Table 3** deserves interpretation. Why does the smallest parameterization perform best? If this is due to regularization or optimization stability, that would be a useful insight and should be discussed.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are raised based on the content of the paper. The work focuses on model conversion and efficient inference, and I did not identify dataset, privacy, human subjects, or misuse issues requiring separate ethics review from the main paper text.

## Soundness Rating
2: fair. The core empirical trend is plausible and supported by the tables/figures, but the theoretical presentation and several methodological details are not sufficiently solid for a higher rating.

## Presentation Rating
2: fair. The high-level story is understandable, and some figures are useful, but the notation, theorem statements, and experimental detail in the main paper need substantial cleanup.

## Contribution Rating
3: good. Converting quantized LLMs into spiking counterparts with lightweight calibration is a relevant and interesting direction, and the empirical recovery over naive conversion is meaningful even though the paper does not fully close the case.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem and shows a real empirical gain from calibration, especially in **Table 2** and **Table 4**, but it overstates some claims, under-supports the edge-efficiency motivation, and needs tighter theory and stronger positioning.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and checked the main technical claims and experiments with care, though some implementation details are not fully specified in the main paper.