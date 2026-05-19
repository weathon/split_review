- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6
Now I have everything I need. Let me produce the final consolidated review.

## Summary
This paper presents FLIP, a model-based planning framework for general-purpose manipulation that uses image flows as a scalable action representation. The framework consists of three modules trained on video+language data without action labels: (1) a CVAE-based flow generation network as the action module, (2) a flow-conditioned video diffusion model as the dynamics module, and (3) a clip-level fine-tuned vision-language value module. FLIP performs hill-climbing beam search over flows and videos to synthesize long-horizon plans, and the generated plans can guide low-level control policies. Experiments across simulation (LIBERO, Language-Table) and real-world datasets (FMB, cloth folding, Bridge-V2) demonstrate strong planning success rates, high-quality long-horizon video generation, and improved downstream policy performance.

## Strengths

- **Flow-centric planning without action labels.** The paper demonstrates that image flows — extracted from pure video using Co-Tracker — can serve as a general-purpose action representation for model-based planning. The action module (CVAE) outperforms the state-of-the-art flow prediction method ATM across LIBERO-10 and Bridge-V2 (ADE 12.7 vs 19.6 on LIBERO-10, Table 4), and the relative-displacement design (scale+direction) is shown to be superior to absolute coordinate prediction. This is a genuinely useful finding: it enables the world model to be trained entirely on video+language data, without robot action labels.

- **Value-guided planning substantially improves success rates.** Table 1 shows that FLIP with the value module achieves 100% success on LIBERO-LONG, 86% on FMB-S, and 78% on FMB-M, compared to 78%/52%/40% for the ablation without value guidance (FLIP-NV) and 2%/0%/0% for UniPi. This provides direct evidence that model-based planning with a learned value function can synthesize correct long-horizon plans in flow+video space — a difficult and under-explored setting.

- **Mixed conditioning mechanism for video generation is effective.** The paper proposes combining cross-attention (for flow/observation conditions) with AdaLN-Zero (for text/timestep), and shows it consistently outperforms LVDM, IRASim, and an ablation using AdaLN-Zero for all conditions (Ours-SC) across both short-horizon (Table 5) and long-horizon (Table 2) video generation. The FVD gap on LIBERO-LONG (35.62 vs 206.28 for IRASim) is striking, demonstrating the value of dense flow conditioning combined with appropriate architectural design.

- **Plan-conditioned low-level policy beats strong baselines.** Figure 5 shows that policies conditioned on the generated flow+video plans (Ours-FV) achieve higher success rates and lower variance than diffusion policy, ATM, and OpenVLA baselines on LIBERO-LONG, validating that the synthesized plans are practically useful for downstream execution.

- **Scalability demonstrated.** Figure 8 shows that increasing model size for both the action module (50M→800M) and dynamics module (3×10⁸→3×10⁹) consistently reduces validation loss, supporting the claim that the approach can scale with compute.

## Weaknesses

### Fatal
None.

### Major

- **Overclaim on real-world policy execution.** The paper states at line 143 that FLIP can "guide the low-level policy for executing the plan for both simulation and real-world tasks," and the introduction (line 26) claims real-world policy guidance. However, the low-level policy experiments (Section 5.3, Figure 5) are evaluated only on LIBERO-LONG, which is a simulation benchmark. Real-robot policy execution — even on a single task — is absent. This gap between claim and evidence is significant; the paper should either provide real-world policy results or explicitly scope the claim to simulation.

- **Long-horizon video generation comparison (Table 2) conflates conditioning regime with architectural quality.** FLIP conditions on dense flow information (thousands of query points per frame), while LVDM uses only text and IRASim uses only sparse end-effector trajectories. The FVD gap (35.62 vs 206.28 on LIBERO-LONG) is far larger than what architectural differences alone would typically produce, suggesting the comparison is primarily measuring the value of richer conditioning rather than architectural superiority. The Ours-SC ablation in Table 5 (same flow conditioning, different architecture) partially addresses this for short-horizon video, but Table 2 lacks a fair controlled comparison where all methods receive the same conditioning information. Additionally, it is not explicitly stated whether Table 2 uses ground-truth flows or generated flows from the action module; this must be clarified.

- **No error bars, confidence intervals, or multi-seed variance reported in any table.** All quantitative results (Tables 1, 2, 4, 5, Figure 5) are reported as point estimates without variance. Planning success, FVD, ADE, and policy success rates all have inherent randomness. Without variance information, it is impossible to assess whether observed differences between methods are statistically significant. This is a standard expectation for empirical ML publications and should be addressed.

### Minor

- **Human evaluation of planning success lacks methodological detail.** The paper reports human evaluation of video plan correctness (Table 1) but does not specify whether evaluators were blinded, the number of evaluators, inter-annotator agreement, or how borderline cases (e.g., near-completion) were handled. The 100% success on LIBERO-LONG (50 test episodes) is unusually perfect and would benefit from independent verification or quantitative metrics (e.g., success detection by a learned classifier).

- **Missing finer-grained ablation of value module variants on planning success.** The paper shows qualitatively that clip-level LIV fine-tuning yields smoother value curves (Figure 4) and shows overall that the value module helps planning (FLIP vs FLIP-NV, Table 1). However, it does not directly ablate whether the *clip-level* fine-tuning specifically (vs. frame-level LIV fine-tuning) translates into better planning success rates. A comparison of planning success with LIV original vs. LIV frame-fine-tuned vs. LIV clip-fine-tuned would cleanly isolate the benefit of the proposed clip-level modification.

- **Key hyperparameters not reported.** The paper defines clip length \(L\), number of query points \(N_q\), planning horizon \(H\), number of flow candidates \(A\), and number of beams \(B\) as hyperparameters, but their actual values are never specified. This is essential for reproducibility and for understanding the computational cost and practical feasibility of the approach (the paper acknowledges slow planning speed as a limitation but does not report wall-clock time).

- **Scalability evidence is thin.** Figure 8 shows only two model sizes per module, which is insufficient to demonstrate a reliable scaling trend. Additional data points would strengthen this claim considerably.

- **No analysis of tracking quality or training data failures.** The paper uses Co-Tracker to extract flow annotations from every frame of training videos but does not report tracking success rate, how tracking failures are handled, or statistics on data quality — especially for challenging scenes like cloth folding.

### Trivial

- The pen-spinning example (Figure 7/9) is used in the introduction to motivate flows as a representation for "sophisticated subtle movements" but no quantitative evaluation of pen-spinning or similarly fine-grained manipulation is provided.

## Nice-to-Haves

- A controlled video generation experiment where LVDM or IRASim are augmented to receive dense flow conditioning (even via a simple projection) would isolate the value of the architectural innovations from the value of richer conditioning.
- A failure analysis categorizing planning errors (flow prediction vs. video generation vs. value estimation) for the cases where FLIP fails (e.g., 14% failure on FMB-S).
- Sensitivity analysis for the clip length \(L\) used in value module fine-tuning.
- Reporting wall-clock planning time for typical tasks.

## Removed Points

- "Missing comparison to concurrent work (UniSim, Genie)" — Removed per instructions: I cannot confirm which works exist/existed at the time of writing; the paper cites relevant prior work.
- "The dynamics module is similar to ControlNet, not novel" — Removed as a misreading: the paper does not claim architectural novelty for the cross-attention mechanism itself; the contribution is the overall framework and the combination of conditioning strategies.
- "FLIP-NV and FLIP both use clip-based fine-tuning, ambiguity" — Removed: FLIP-NV is clearly described as "no value module as guidance"; it uses the same action/dynamics modules but without value-based beam selection. The value module impact IS quantified in Table 1.
- "Missing appendix" — Removed: this is a parser artifact; the original submission contains it.
- "Code release not stated" — Removed per hard rule: cited entities/models/tools are assumed to exist.
- "Problem formulation theoretical justification is sketchy" — Removed: the paper explicitly states the assumption V=V* and the deterministic simplification; this is standard practice in model-based RL.
- "Planning algorithm line 11 collapses diversity, may inflate success" — Removed: this is a speculative claim about a design choice without evidence that it harms results. The beam search with periodic replacement is a reasonable heuristic.
- "The comparison to ATM is unfair because ATM uses SAM-selected points" — Demoted and mostly removed: The paper explicitly discusses this difference in its training data annotation section (line 60), positioning dense grids as a contribution over ATM's SAM-based approach. Running ATM on dense grids would be a useful control but the comparison as-is tests the full system difference.

## Novel Insights

The harsh critic correctly identifies that the video generation comparison (Table 2) conflates conditioning richness with architecture quality — but the paper's Ours-SC ablation in Table 5 partially serves as a control for this. The more interesting insight that emerges from cross-referencing both reviews is that FLIP's empirical strength comes from a *convergence of three independent design choices*: (1) relative-displacement flow prediction (vs. absolute coordinates), which alone explains a large performance gap (Table 4: ADE 12.7 vs 20.5 for Ours-ABS), (2) the mixed cross-attention + AdaLN-Zero conditioning for video generation (Ours vs Ours-SC in Table 5), and (3) the clip-level value fine-tuning for stable planning. The strength finder correctly highlights that the planning success rates (up to 100%) are far beyond what the baselines achieve, but the harsh critic's point about the missing real-robot policy execution is the single most impactful gap — the paper's framing promises general-purpose manipulation hardware validation, which the current experiments do not deliver.

## Suggestions

1. **Provide real-world policy execution results**, even for a single task, to substantiate the claim that generated plans guide robot control in the real world. Alternatively, explicitly scope the claim to simulation.
2. **Clarify the evaluation protocol for Table 2**: state explicitly whether flows are ground-truth or generated, and consider adding a controlled experiment where baselines receive comparable flow conditioning.
3. **Add error bars** (or at least multi-seed variance) to all quantitative tables.
4. **Report hyperparameter values** (L, N_q, A, B, H) and wall-clock planning time to support reproducibility and assess practical feasibility.
5. **Add a finer-grained value module ablation** comparing planning success with LIV original, LIV frame-fine-tuned, and LIV clip-fine-tuned to isolate the benefit of the proposed clip-level modification.
