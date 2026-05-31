## Summary

CoRAL is a modular neuro-symbolic framework for zero-shot, contact-rich robotic manipulation that integrates (1) FoundationPose for 6-DoF pose tracking, (2) a VLM (GPT-4o) for physical parameter estimation, (3) an LLM that generates MPPI cost functions and contact strategies, (4) a RAG-based memory unit for experience retrieval, and (5) a reactive MPPI controller operating within nested feedback loops. The core design thesis is that explicitly separating VLM perception from LLM strategic reasoning—rather than using a unified multimodal model—substantially improves both task performance and explainability. Experiments on six contact-rich manipulation tasks in simulation compare the system against OpenVLA-OFT, π₀.₅, and expert-designed cost function baselines.

---

## Strengths

- **Principled role separation with strong ablation evidence.** The *Unified VLM* ablation (single prompt for both perception and planning) collapses to near-zero success across almost all tasks, providing decisive evidence for the paper's core architectural claim that separating VLM and LLM roles is non-negotiable. The contrast is stark and well-measured.

- **LLM as cost-function designer is a creative and well-instantiated idea.** Grounding the LLM's symbolic output directly in the MPPI cost function (Eq. 2–6) creates a clean, principled bridge between commonsense reasoning and physics-based optimal control. The quantitative support—83.9% faster and 63.9% shorter paths when guided contact strategy is used vs. random MPPI sampling on T6—is compelling evidence that this design is productive.

- **Clear superiority over end-to-end VLAs on contact-rich tasks.** OpenVLA-OFT and π₀.₅ score 0/10 on T1, T4, and T6. CoRAL scoring 4/10, 9/10, and 7/10 on these tasks in a zero-shot setting, without any task-specific demonstrations, is a meaningful and significant result that speaks to a genuine capability gap.

- **Comprehensive ablation covering each component.** The study cleanly ablates pose tracking, memory, online refinement, and role separation—each with dramatically different outcomes—giving the reader a high-confidence view of which components matter and why.

---

## Weaknesses

### Fatal
None that fully invalidate the core claims.

### Major

1. **Figure 4 is inconsistent with its accompanying text.** The paper states (§4.1.4) that the experiment involves a mass "severely overestimated" at **2.0 kg** vs. a ground truth of **0.1 kg**, and that the system "converged remarkably close to their true values." However, Figure 4's y-axis spans only 0.75–1.00 kg, and the depicted correction goes from ~1.00 kg to ~0.85 kg—nowhere near the claimed 0.1 kg ground truth. This is a major inconsistency: either the figure depicts a different, much easier experiment than described in the text, or the correction mechanism does not actually achieve convergence to ground truth. This undermines the robustness claim and erodes confidence in the evaluation.

2. **Simulation-only evaluation with N=10 trials.** All six tasks are evaluated entirely in ROBOSUITE/MuJoCo with only 10 trials per task. For a paper making strong claims about contact-rich manipulation, the absence of any physical robot experiment is a serious gap—contact dynamics, compliance, and sensor noise differ substantially between simulation and reality. Moreover, with N=10 the success rates (4/10 on T1, for instance) carry enormous uncertainty; one cannot distinguish 40% ± ~16% from 20%–60% without much more data. Statistical tests are never applied.

3. **Modest absolute performance on the flagship task.** T1 ("Push and Pick Cutting Board"), presented as the key demonstration of long-horizon, contact-rich reasoning, achieves only **4/10** with the full system. Even the human FSM expert reaches 8/10. A 40% success rate on the paper's central contribution, evaluated in simulation with randomized but otherwise fairly clean physical parameters, is unconvincing as evidence of a robust system.

4. **No analysis of LLM reliability or prompt sensitivity.** The LLM generates the MPPI cost function and contact strategy from scratch. If the LLM produces an inconsistent or physically nonsensical cost function, the entire system fails silently. The paper provides no quantification of how often the LLM produces usable outputs, how sensitive performance is to prompt design, or what percentage of outer-loop calls lead to successful world model corrections. This is a critical gap for a system that relies on LLM outputs as a hard dependency.

### Minor

1. **Computational latency is not characterized.** The paper states K=200 MPPI rollouts over H=50 steps are run on a CPU, but never reports the actual control frequency achieved. This matters because the reactive control loop's effectiveness is frequency-dependent.

2. **Broken cross-reference.** Section 4.1.4 refers readers to "Appendix ??" for the natural language diagnosis example, indicating an unresolved reference that makes this qualitative claim unverifiable.

3. **Memory module scaling is not discussed.** The RAG-based memory stores successful episodes, but with 10 trials per task the memory pool is tiny. There is no discussion of how retrieval quality degrades or scales with pool size, or how the system handles ambiguous matches.

### Trivial
None worth listing.

---

## Nice-to-Haves

- A real-robot evaluation on even one or two tasks would substantially strengthen the paper's practical claims.
- A failure mode analysis—how often does the LLM propose an infeasible or degenerate cost function, and how is this detected/recovered—would significantly improve the trustworthiness of the framework.
- Reporting confidence intervals or using bootstrap resampling across the 10 trials would make the performance comparisons more statistically interpretable.

---

## Novel Insights

The most genuinely novel conceptual contribution is treating the LLM as a *cost-function architect* for a physics-based optimal controller rather than as a high-level goal generator feeding a learned policy. This decoupling—LLM designs the optimization objective, MPPI solves it online with reactive feedback—creates a clean interface between commonsense world knowledge and rigorous trajectory optimization. The nested two-loop structure (fast MPPI inner loop, slow LLM-driven outer loop for world model correction) is a principled and elegant way to handle the different timescales of physical execution and symbolic reasoning. The ablation evidence that even separating VLM from LLM roles (perception vs. strategy) is decisive further crystallizes this insight into a concrete design principle with measurable consequences.

---

## Suggestions

- Replace or clearly reconcile Figure 4: either change the text to match the depicted experiment or show a figure that actually spans the claimed parameter range (2.0 kg → 0.1 kg).
- Increase N to at least 20–30 trials per task, or provide confidence intervals, to permit statistically defensible comparisons.
- Add at minimum one physical robot experiment (even a single task) to validate the sim-to-real robustness claims.
- Include a table logging the LLM output success rate (how often does it produce a syntactically and semantically valid cost function per call?) and average outer-loop invocations per task.
- Fix the broken "Appendix ??" reference and include the qualitative failure diagnosis log it was meant to point to.

---

## Score and Decision

The paper proposes a creative and principled architecture with a convincing ablation study and clear advantages over end-to-end VLAs on contact-rich tasks. However, the Figure 4 inconsistency is a significant credibility issue, the evaluation is limited to simulation with only 10 trials yielding low absolute success rates on the paper's flagship task, and the LLM reliability question is left unaddressed. These are substantive gaps that prevent confident acceptance.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>