- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Now I have all the evidence needed. Let me produce the final consolidated review.

## Summary

DriveE2E introduces the first closed-loop end-to-end autonomous driving benchmark grounded in real-world traffic scenarios. The authors construct digital twins of 15 real intersections in Beijing, capture 800 real traffic scenarios from 100 hours of roadside camera footage, and integrate these into the CARLA simulator for closed-loop evaluation. Four baseline E2EAD methods (UniAD, VAD, TCP, AD-MLP) are evaluated, demonstrating the benchmark's ability to differentiate methods by planning capability. The core contribution — using recorded real-world traffic trajectories rather than hand-crafted simulated scenarios in a closed-loop simulator — is clearly novel and fills a gap in the existing benchmark landscape.

## Strengths

- **First closed-loop E2EAD benchmark using real-world traffic scenarios.** Table 1 directly shows that DriveE2E is the only entry where the "Traffic Scenario" column is "Real" while also supporting closed-loop E2E evaluation, in contrast to CARLA Leaderboard V2 and Bench2Drive which use simulated/manually configured scenarios. This is the paper's primary and well-supported contribution.

- **Detailed digital twin construction pipeline.** Section 3.2 and Figure 3 document a clear methodology: HD maps → RoadRunner refinement → OpenStreetMap augmentation → Blender merging → CARLA integration. The 15 intersections span diverse road topologies in urban Beijing, which provides a more realistic static environment than generic simulated maps.

- **Substantial real-world data foundation.** The 800 scenarios are selected from 100 hours of roadside camera footage, covering 8 driving behaviors, 6 weather conditions, and times spanning the full day (Figure 2). The elevated roadside camera setup reduces occlusion and enables comprehensive traffic flow capture — a practical advantage over vehicle-mounted sensors.

- **Empirical demonstration that closed-loop evaluation matters.** Table 3 shows that perception-based methods (VAD: 45.14% SR) dramatically outperform methods relying only on past ego states (AD-MLP: 6.85% SR, TCP: 7.42% SR). Section 4.2 further notes that open-loop L2 errors do not consistently correlate with closed-loop success, validating the benchmark's core design rationale.

## Weaknesses

### Fatal  
None.

### Major

- **Non-reactive traffic participants undermine the "closed-loop interaction" claim.** The ego vehicle is the only active agent; all other traffic participants follow pre-recorded trajectories and do not react to the ego's actions. The paper acknowledges this in the Limitations ("interactions with other traffic participants … are very weak"), but the abstract and introduction make stronger claims: "CARLA enables realistic simulations where autonomous agents can dynamically interact with their surroundings" and "effectively bridging the gap between simulated environments and real-world driving conditions." This gap between claim and reality is significant — the benchmark tests navigation through a recorded scene, not interactive decision-making in a dynamic environment where other agents respond. The paper would be considerably stronger if the framing were adjusted to match the actual capability.

- **The benchmark may not be sufficiently challenging for state-of-the-art methods.** Section 4.4 states that "VAD performs better on DriveE2E, suggesting that the scenarios in DriveE2E are generally simpler than those in Bench2Drive." With VAD achieving only 45.14% SR, the benchmark is not trivial, but the self-reported simplicity relative to a peer benchmark is a concern for long-term utility as SOTA methods improve. The authors acknowledge this and plan to add harder scenarios, but as presented, the discriminative power at the top end is unclear.

### Minor

- **No variance or confidence intervals reported.** Table 3 reports single-point results (e.g., VAD SR 45.14, DS 55.15) without standard deviations or per-scenario breakdowns. Given the diversity of 800 scenarios across 8 behavior types, performance variation is likely high. Confidence intervals would substantially increase statistical credibility.

- **No fidelity metrics for the digital twins.** The paper claims that twins "accurately replicate the physical and environmental characteristics" of real intersections, but provides no quantitative comparison (e.g., lane geometry deviation, building placement error, traffic light timing accuracy). This makes it difficult to assess how faithfully the simulation matches the real locations.

- **No annotation accuracy statistics for dynamic scenarios.** The auto-annotation pipeline (3D detection + tracking) is described, but no detection mAP or tracking MOTA figures are reported. Errors in the trajectory annotations propagate directly into the benchmark's scenarios.

- **Bench2Drive comparison is too thin.** Section 4.4 consists of a single sentence saying scenarios are "simpler" and a brief Table 5. No distributional analysis, per-difficulty breakdown, or task-level comparison is provided that would help users understand how DriveE2E relates to existing benchmarks beyond a single aggregate SR comparison.

- **Only four baselines evaluated.** AD-MLP and TCP are deliberately simple methods included specifically to show they fail. Including only one competitive perception-based method (VAD) with a fully converged model limits what can be concluded about the benchmark's ability to discriminate among strong methods.

### Trivial  

None.

## Nice-to-Haves

- Adding even a simple reactive behavior model (e.g., IDM for vehicles) would transform the benchmark from a replay test into a genuinely interactive evaluation and directly address the most significant limitation.
- Quantifying digital twin fidelity (lane centerline deviation, perceptual similarity scores) would build trust in the simulation-to-real transfer.
- A scenario difficulty rating or per-scenario breakdown would help users understand what kinds of scenarios drive failures.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **UniAD unconverged results (3a):** REMOVED — The critic claimed that including non-converged UniAD results is misleading. In fact, the paper is fully transparent: Table 3's caption states "Considering that UniAD has not yet converged, we have not reported its closed-loop results yet." Only open-loop L2 errors are reported, with explicit caveats. The reviewer misread the table.
- **No real-world validation of correlation (Point 2):** REMOVED — Asking a benchmark paper to prove that its evaluation scores correlate with on-road driving performance sets a bar that no existing benchmark in this field meets (including CARLA Leaderboard, Bench2Drive, etc.). The claim "more accurately reflects real-world driving" is supported by the use of real-world trajectory data; demanding real-vehicle validation experiments is outside the scope of a benchmark paper and impractical at this scale.
- **Dataset availability / release plan:** REMOVED per policy (the paper states "we release observation data" in Section 3.3; release links would appear in the supplementary or camera-ready version).
- **Ethical/privacy concerns about Beijing intersections:** REMOVED — Speculative and not anchored in any concrete issue with the paper's data handling. Roadside infrastructure camera data of public traffic is standard practice.
- **Missing related works:** REMOVED per policy (cannot verify completeness without external sources).
- **Computational cost / training times:** REMOVED — Not a standard requirement for benchmark papers; not a substantive weakness.
- **Formatting / typography concerns:** REMOVED per policy (parser artifacts, not author errors).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Adjust the claims to match the benchmark's actual capability.** Replace "bridging the gap between simulation and real-world" with language acknowledging that the benchmark provides more realistic initial scene configurations (real trajectories, real intersection geometry) but does not yet support interactive multi-agent behavior.
2. **Add confidence intervals or per-scenario breakdowns** to all evaluation tables to improve statistical rigor.
3. **Expand the Bench2Drive comparison** with per-behavior-category SR comparisons and a distributional analysis of scenario difficulty.
4. **Report annotation accuracy** (detection mAP, tracking MOTA) for the auto-annotation pipeline to allow users to gauge data quality.
