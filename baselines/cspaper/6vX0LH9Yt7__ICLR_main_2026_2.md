---
job_id: f02295c1-a841-49a8-974b-c4e6867667ba
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 6vX0LH9Yt7.pdf
paper: Hybrid Neural-MPM for Interactive Fluid Simulations in Real-Time
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining graph-based neural simulation, generative modeling, and a hybrid neural-numerical system for physical dynamics and interactive control.

## Minimum Quality
Pass ✅. The paper contains the necessary scientific components, including abstract, introduction, methodology, experiments, quantitative/qualitative results, related work, and conclusion; while there are notable technical and experimental weaknesses, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes a hybrid system for interactive fluid simulation that combines a GNN-based neural simulator operating at reduced spatiotemporal resolution with a fallback to a classical MPM solver when a heuristic complexity measure indicates the neural rollout may be unreliable. The paper also introduces a diffusion-based controller that predicts external force fields from user sketches, trained using data generated via a reverse-simulation procedure.

Empirically, the paper evaluates the hybrid simulator on several 2D and 3D water/sand scenarios and reports reduced latency relative to pure MPM while maintaining lower error than a coarse neural simulator. It also presents qualitative and limited quantitative results for sketch-guided fluid control.

## Strengths
1. The paper targets a concrete and practically meaningful problem, namely interactive fluid simulation with both low latency and some degree of user control. The combination of simulation acceleration and controllability is broader than many prior neural-physics papers, which focus only on passive forward prediction.

2. The high-level system design is easy to understand. In particular, **Figure 3** gives a clear overview of the two main components, hybrid simulation and sketch-conditioned control, and how they fit together in a single pipeline. For a paper that spans GNN simulation, numerical fallback, and diffusion-based control, this figure does useful conceptual work.

3. The hybrid idea itself is sensible. Using a learned model where it is fast and a numerical solver where it is safer is an intuitively reasonable engineering direction. The empirical trends in **Figure 6(d)** and **Table 1** do show the expected monotonic trade-off: increasing the fallback threshold improves grid-mass error while increasing time per step. Even though I have concerns about how the threshold is selected and how broadly this generalizes, the basic behavior is coherent.

4. The paper does attempt to explore the latency-error frontier rather than only optimizing prediction error. The ablations in **Figure 6(a-c)** are useful because they explicitly study temporal downsampling, spatial downsampling, and their combination. This is more informative than reporting a single configuration.

5. The qualitative visualizations are reasonably compelling at a demo level. **Figure 11** and **Figure 12** suggest that the control component can induce directionally meaningful changes in the fluid trajectory, and **Figure 14** indicates that the hybrid solver often tracks the visual structure of MPM better than the original neural simulator.

6. The paper evaluates a variety of scenarios, including 2D/3D, water/sand, ramps, and mixed material settings, summarized in **Table 2**. That breadth is useful, even if the evaluation protocol itself still has limitations.

## Weaknesses
1. **The core technical novelty is limited and the paper does not sufficiently distinguish its contribution from a straightforward hybrid heuristic.**  
   At a high level, the method is: train a GNN simulator at coarser resolution for speed, monitor a simple instability proxy, and fall back to MPM when the proxy crosses a threshold. This is a reasonable system, but the paper overstates the scientific contribution. The fallback rule in **Equation (1)** is conceptually just a hand-designed switch, and the actual trigger in **Equation (2)** is a threshold on temporal cosine similarity of particle accelerations. The paper does not provide a principled derivation for why this is the right criterion, nor does it compare against several plausible alternatives beyond a brief mention of velocity divergence being more expensive. As written, the work reads more as a pragmatic pipeline than a method with a clearly articulated new learning principle.

2. **The mathematical exposition has multiple notation errors and inconsistencies, some of them in core definitions. This materially hurts confidence in the technical correctness.**  
   A few examples:
   - In **Section 2.2** on Page 3, the paper says the decoder predicts per-particle acceleration, “$\hat{\mathbf{p}}_i$”, which uses the same notation as position-like variables elsewhere and is inconsistent with the intended acceleration notation. The training loss then defines $\mathrm{RMSE}_{\hat{\mathbf{p}}}$ as  
     \[
     \frac{1}{N}\sum_{i=1}^N \frac{\|\hat{\mathbf{p}}_i - \hat{\mathbf{p}}_i\|_2}{\|\hat{\mathbf{p}}_i\|_2},
     \]
     which is obviously degenerate as written, since the numerator compares a quantity to itself. This is not a cosmetic typo because it appears in the definition of the main training objective.
   - In **Section 3.1.1** on Page 4, the grid-level error metric is again written with self-subtraction-like notation,  
     \[
     \mathrm{RMSE}_{\hat m} \equiv \frac{1}{N}\sum_{i=1}^N \frac{\|\hat m_i - \hat m_i\|_2}{(\hat m_i)_2},
     \]
     and the denominator notation is also malformed. It is impossible to verify the intended normalization from the main paper alone.
   - The paper alternates among $\hat m$, $\tilde m$, and $\mathrm{RMSE}_{\mathrm{vis}}$ / $\mathrm{RMSE}_{\hat m}$ / $\mathrm{RMSE}_{\tilde m}$ without a clean definition map. For instance, **Figure 10** is labeled with “grid $\mathrm{RMSE}_{\mathrm{vis}}$”, whereas earlier sections build the case around $\mathrm{RMSE}_{\hat m}$. This makes it unclear whether all reported curves use the same metric.
   - In the control section, **Equation (3)** uses $\mathbf{a}_t$ as acceleration and then **Section 3.2.3** says the diffusion model predicts “a dynamic force field ($\alpha$ in Equation 3),” but Equation 3 contains no $\alpha$. That is not a minor typo, it means the central predicted quantity is inconsistently named in the main text.

   These issues matter because the paper’s argument depends heavily on the exact training targets and evaluation metrics. If those are not precisely defined, it becomes hard to assess whether the method is doing what the paper claims.

3. **The empirical evidence for the hybrid simulator is weaker than the framing suggests, because the comparisons are narrow and the claimed gains are modest in absolute terms.**  
   The headline claim is “real-time” simulation with “11 to 29% latency reduced,” but the comparison is primarily against vanilla MPM and one original neural physics baseline. There is no convincing study of whether the hybrid switch is actually necessary relative to stronger learned simulators, alternative reduced-order methods, or even simple periodic correction schedules. In **Figure 10**, the hybrid solver often occupies an intermediate point between neural physics and MPM, which is expected, but the paper does not establish that this frontier is competitive beyond this immediate setup. Also, in several cases the absolute latency numbers are already in the low-millisecond range, so the practical significance of the relative gain needs more careful contextualization.

4. **The latency evaluation itself is not fully trustworthy because the neural inference timing uses an approximation rather than the actual graph aggregation cost.**  
   Appendix C.1 states that TensorRT does not support the GNN aggregation operation, so the authors approximate its time cost with a matrix multiplication \(A \cdot o\). This is a major systems caveat. The paper’s main selling point is runtime. If the most characteristic operation of the graph model is not actually timed as implemented, but replaced by a surrogate kernel, then the central latency claims become less solid. This especially affects conclusions drawn from **Figure 6**, **Figure 7**, **Figure 10**, and **Table 1**, since the paper repeatedly interprets small timing differences as meaningful. A method paper centered on real-time performance needs more faithful end-to-end timing.

5. **The fallback trigger is only weakly justified and the reported correlation is not strong enough to support the confidence placed in it.**  
   The main evidence is **Figure 5**, which shows a negative correlation between acceleration cosine similarity and simulation error, with reported Spearman correlation \(-0.3902\). That is not especially strong. Yet the paper uses this to motivate the entire safeguard mechanism. A noisy moderate correlation in a single scenario, Water 2D, is not enough to establish that this statistic reliably predicts imminent rollout degradation across materials, dimensions, and obstacle interactions. The paper should at minimum report trigger-quality analysis across the datasets in **Table 2**, such as ROC-style behavior, fallback frequency, false positives, and whether the same threshold \(r_c=0.8\) is robust across domains.

6. **Threshold selection appears under-validated and potentially overfit to one scenario.**  
   The paper tunes \(r_p\), \(r_t\), and \(r_c\) using the Water 2D ablation in **Figure 6** and **Table 1**, then seems to carry these settings into the broader experiments. It is not clear whether thresholds are tuned separately per domain or fixed globally, nor whether a validation set distinct from test trajectories is used for this calibration. Since the behavior of fallback is central to the method, threshold sensitivity should be reported per domain. Right now the paper risks presenting one operating point selected on a convenient scenario and then extrapolating the conclusion.

7. **The control component is under-evaluated and the baseline is weak.**  
   In **Section 4.3** and **Table 3**, the only explicit baseline is a constant spatiotemporal force field chosen to move particles from \(X_{T_{\text{in}}}\) to \(X_1\). That is a very low bar for a diffusion-based controller. The paper cites multiple prior works on fluid control and controllable generation, but the experimental comparison does not include stronger alternatives, not even simple optimization-based force fitting, a supervised non-diffusion predictor, or a ControlNet-style ablation without diffusion. The gains in **Table 3** are also fairly modest numerically. Given the complexity and training cost of the controller, stronger baselines are needed to justify the design.

8. **The reverse-simulation data generation procedure is physically questionable and insufficiently validated.**  
   **Equation (3)** derives an acceleration required to move particles from \(\mathbf{p}_t\) to \(\mathbf{p}_{t-1}\), subtracting gravity. But real fluid dynamics involve interactions, pressure effects, contact, and constraints, not just per-particle kinematics. The paper presents this as a “physically interpretable approximation,” which is fair, but then uses the resulting acceleration fields as training targets for the controller without carefully validating whether these fields correspond to realizable control forces under MPM. This is not a minor concern. If the supervision target is only a rough kinematic inversion, the generative controller may learn to imitate artifacts of the approximation rather than meaningful control policies. The paper’s evidence here is mostly qualitative.

9. **There are unresolved inconsistencies between the main-text claims and the actual experimental setup for control.**  
   The paper motivates “interactive” control, but the controller latency reported in **Table 12** is around 18.7 to 27.0 ms, and the control is unrolled over a fixed \(T_{\mathrm{ctr}}=100\) MPM steps. The main text does not clearly explain whether this control inference happens once per user command, once per simulation step, or over a receding horizon, which is crucial for understanding actual usability. **Figure 9** suggests denoising and temporal unrolling, but the runtime implications are not explained in the main paper. For a paper built around interactivity, this ambiguity is consequential.

10. **The paper’s evaluation protocol is limited to in-distribution rollouts, which weakens claims about robustness.**  
    On Page 7, the evaluation uses held-out trajectories “drawn from the same distribution of initial conditions used for training.” That is standard, but the paper repeatedly motivates the fallback as protection in complex or OOD regimes. If that is the motivation, then some genuinely shifted or harder test conditions should be included. Otherwise, the paper is using OOD language to justify the safeguard without actually testing the relevant regime.

11. **The paper sometimes overclaims what the results support.**  
    For example, **Figure 7** is used to conclude that the hybrid solver “improves both rollout RMSE and latency,” but that figure compares against the original neural physics at full resolution, not against a broader family of alternatives. Likewise, **Figure 10** says the method “outperform[s] both neural physics and MPM,” but what is really shown is an empirical trade-off point under a specific implementation and measurement setup, not universal dominance. The paper would be stronger if it used more careful language.

12. **Presentation quality is uneven despite the appealing high-level story.**  
    Several sections contain grammar issues, notation drift, and imprecise wording. There are also contradictions, such as “fluid complex is high” in Section 4.4, or referring to the target in control as both force field and acceleration field without a clean unit convention. This may sound superficial, but in a paper with several moving parts, presentation errors compound into real interpretability problems.

## Questions
1. The main paper has multiple inconsistent definitions for the core losses and metrics. Please provide corrected forms of:
   \[
   \mathrm{RMSE}_{\ddot{\mathbf p}},\quad \mathrm{RMSE}_{m},
   \]
   including exact numerator, denominator, and whether the normalization is per-particle, per-grid-cell, or global. I would like to understand precisely what is optimized during training and what is reported in each table/figure. A clean notation table in the rebuttal would help substantially.

2. How exactly is the fallback threshold \(r_c\) selected for the experiments in **Figure 10**? Is \(r_c=0.8\) fixed across all scenarios in **Table 2**, or tuned per domain? If fixed, please report fallback frequency and error/latency sensitivity per scenario. If tuned, please clarify the validation protocol and whether test trajectories were used at any point in threshold selection.

3. Can you provide stronger evidence that the acceleration-cosine trigger is a reliable proxy for failure? The current evidence in **Figure 5** is one Water 2D plot with Spearman \(-0.3902\), which is not particularly compelling. I would like to see the same analysis across multiple domains, plus quantitative trigger diagnostics such as how often fallback activates before large rollout error spikes.

4. The runtime story is central, but Appendix C.1 says the GNN aggregation cost is approximated via matrix multiplication rather than timed directly. Can you report end-to-end measured latency of the actual deployed implementation, including graph construction and true aggregation, for both the neural and hybrid solvers? This would significantly increase confidence in the “real-time” claim.

5. For the control component, why is the only baseline in **Table 3** a constant force field? Please discuss whether you evaluated, or could evaluate, simpler learned baselines such as a direct regression model without diffusion, or optimization-based force fitting. A stronger baseline suite could materially change my assessment of the control contribution.

6. In **Equation (3)**, the target acceleration used for reverse simulation seems to ignore many coupled fluid effects beyond gravity and observed displacement/velocity. What evidence do you have that these solved accelerations correspond to realizable external controls under MPM, rather than merely kinematic reverse-engineering artifacts? Some validation of the generated supervision targets would help.

7. In **Figure 10**, the method appears to sit between MPM and neural physics on an error-latency frontier, which is plausible. But the paper claims “outperforming both neural physics and MPM.” Could you make this more precise? For example, is the claim Pareto dominance under some scenarios, or simply a better trade-off than two selected baselines at chosen operating points?

8. The paper trains separate models per scenario. How much of the reported performance depends on this specialization? If a single model were trained across multiple related domains, would the hybrid system still offer the same advantage? This matters for judging how general the contribution is to the ICLR audience rather than to narrowly scoped scene-specific simulators.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper itself. The work focuses on simulation and interactive control for fluids in graphics-style environments, and the datasets are generated procedurally.

## Soundness Rating
2: fair. The overall idea is plausible and some empirical trends are coherent, but the paper has too many unresolved issues in metric definitions, trigger justification, latency measurement methodology, and control evaluation for me to rate the technical support more highly.

## Presentation Rating
2: fair. The paper has a clear high-level narrative and several helpful figures, but the mathematical notation and several key definitions are inconsistent enough to impede careful verification.

## Contribution Rating
2: fair. The integrated system is interesting and potentially useful, but the scientific contribution feels incremental relative to the amount of engineering, and the empirical support is not yet strong enough for a stronger rating.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper has a practical idea and some promising experiments, but in its current form it falls short of ICLR standards due to underdeveloped methodological justification, notation/mathematical inconsistencies, limited baselines, and a runtime evaluation that is less solid than the framing suggests.

## Reviewer Confidence
4: confident. I am confident in the main concerns, especially regarding the equations, experimental framing, and the interpretation of the latency/error trade-offs, though some implementation details remain ambiguous because of the paper’s notation issues.