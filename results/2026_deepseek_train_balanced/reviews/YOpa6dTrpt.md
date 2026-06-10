## Summary

This paper introduces the PMR dataset, a large-scale pedestrian motion reconstruction dataset built from a mixed-reality platform combining VR headsets, optical motion capture, and the CARLA simulator. It provides synchronized multi-modal data (third-person RGB, egocentric video, LiDAR) with accurate global ground-truth annotations across 12,138 sequences from 54 subjects in 13 traffic scenarios, including rare and safety-critical events. Benchmark evaluations across third-person, egocentric, and LiDAR modalities, plus a domain gap study showing PMR data improves nuScenes 3D pedestrian detection, demonstrate aspects of the dataset's practical utility.

## Strengths

- **First large-scale dataset to simultaneously provide egocentric perspective, third-person multi-view RGB, and LiDAR data with global ground-truth poses (SMPL-X) from a unified mixed-reality pipeline.** This combination is infeasible in real-world collection (Section 3.1–3.2). The paper correctly identifies that existing pedestrian datasets lack this multi-perspective alignment (Section 2).

- **Domain gap experiment provides concrete downstream evidence (Section 4.4):** Replacing 40% of real nuScenes training data with PMR data improves BEVStereo 3D pedestrian detection across *all* four metrics (AP, ATE, ASE, AOE). This is a tangible demonstration that the synthetic data has practical value beyond mere label accuracy.

- **Multi-view SLAHMR experiment (Section 4.1, Table 4) surfaces a non-trivial finding:** Adding a second camera can degrade global pose estimation when the primary camera is moving, due to cascading coordinate-alignment errors. This identifies a concrete open problem that the PMR dataset's controlled multi-view configuration uniquely enables studying.

- **Inclusion of simulated rare/collision scenarios (Section 3.2)** not safely collectable in real-world settings, with quantified behavioral data covering pedestrian reactions during vehicle approach (Fig. 6–7).

- **Technically clear and replicable collection pipeline** (MoCap + VR HMD + UE4 + CARLA, Fig. 2–3) that generates accurate ground-truth labels without manual annotation.

## Weaknesses

### Major

- **Behavioral realism of VR-induced behavior is not validated against real-world data, yet the paper's strongest framing claims depend on it.** The abstract states PMR "integrates real-world behaviors" and "naturally exhibit[s] pedestrian intent," and Section 3.2 draws conclusions like "pedestrians tend to move fast when the vehicle is moving at low velocities" as if these are generalizable traffic behaviors rather than VR-induced responses. No experiment compares PMR behavioral patterns (reaction times, pose distributions, trajectories) against real-world pedestrian data (e.g., from nuScenes, PIE, or Waymo). The domain gap experiment (Section 4.4) tests *visual* domain transfer for 3D detection, not behavioral realism. Without such validation, the paper's core framing claim — that PMR captures realistic pedestrian behaviors with genuine intentions — is unsupported. This does not invalidate the dataset (it remains valuable as a source of synthetic labeled multi-modal data), but the paper must either provide behavioral validation or honestly narrow its claims.

- **"Pedestrian intention" framing oversells what the dataset provides.** The abstract, introduction, and conclusion repeatedly foreground "pedestrian intention" as the dataset's focus and contribution, but the actual annotations are raw motion data — SMPL-X meshes, 3D keypoints, head poses, RGB video, LiDAR — without structured intention labels. GPT-4 intention descriptions get one sentence in Section 3.2 and are relegated to supplementary without any accuracy/reliability evaluation. The dataset enables *research toward* intention-aware modeling, but the current framing implies a level of annotation the data does not contain.

### Minor

- **Dataset release details (URL, license, planned date) are absent.** For a paper whose primary contribution is a dataset, this is a conspicuous omission that must be rectified before or at publication.
- **No human subjects ethics documentation.** The paper involves 54 volunteers wearing MoCap suits and VR headsets in scenarios including simulated collisions, but mentions no IRB approval, informed consent procedures, or data privacy protections. This should be addressed before public release.
- **Domain gap experiment confounds multiple factors.** The "replace 40% of nuScenes with PMR" design changes scene content, annotation quality, image statistics, and behavioral patterns simultaneously. The improvement could stem from higher annotation quality or rarer scenarios rather than behavioral/photorealisic fidelity. A cleaner design (e.g., training on PMR alone, or ablating data proportions) would strengthen the claim. The result is a positive signal but less cleanly interpretable than claimed.

### Trivial

- **No limitations section.** The conclusion summarizes contributions but does not discuss dataset limitations (e.g., synthetic appearance diversity, potential behavioral artifacts of VR, domain gaps), which is especially valuable for dataset papers.

## Nice-to-Haves

- Report variance/confidence intervals for benchmark results (Tables 3–5), particularly the 40-sequence-per-group random selections in the multi-view analysis, which introduce sampling variability not captured by single-run results.
- Compare behavioral distributions (pedestrian-vehicle distances, reaction times, body pose patterns) between PMR and real-world datasets to directly validate or characterize behavioral realism.
- A limitations paragraph acknowledging the synthetic nature of the behavior and what the dataset is and is not suitable for.

## Removed Points

- *"The supplementary materials likely contain important details about hardware and calibration"* — Removed per policy: concerns about missing appendix content are inadmissible (the parser strips appendices from all papers).
- *"The paper cannot be evaluated for its contribution if the contribution cannot be accessed"* (re: dataset availability) — Removed the fatal framing of this point. The valid concern about missing release details is kept in Minor.
- *Strength Finder's claim that "VR-induced reactions are ecologically valid and directly tied to pedestrian intention"* — Removed as overclaiming because it conflicts with the verified weakness about unvalidated behavioral realism. The quantitative analysis in Section 3.2 exists but does not constitute ecological validation; the strength is reframed above as a more measured observation about data diversity and diversity of scenarios.
- *Various formatting/style observations* — Removed per policy (parser artifacts, not author errors).
- *Generalized concern that "the current analysis stops at domain gap exists without characterizing it" for the egocentric task* — The paper does give specific reasons for the gap (virtual environment, VR glasses vs. head-mounted camera) in Section 4.2; this critique lacked a concrete anchor in the paper.

## Novel Insights

The multi-view SLAHMR experiment (Section 4.1, Table 4) surfaces a genuinely non-obvious finding: additional camera views can degrade global pose reconstruction when the primary camera is moving, due to cascading errors in coordinate alignment during the initial optimization stage. This is a specific open problem — how to leverage multi-view information without introducing interference — that the PMR dataset's controlled multi-view configurations enable studying. The paper identifies this problem but does not analyze it further; it remains as a useful observation for the community.

## Suggestions

1. **Either validate behavioral realism** via cross-dataset comparison of behavioral distributions (PMR vs. PIE/nuScenes/Waymo pedestrian data), **or reframe the paper's contribution** as "a large-scale synthetic multi-modal dataset with accurate labels for rare traffic scenarios" rather than claiming realistic intention-driven behaviors. This is the single most impactful revision.
2. Add dataset release URL, license, and a brief ethical oversight statement (IRB/consent/privacy) before publication.
3. Provide variance estimates for benchmark results, especially the multi-view analysis where 40-sequence-per-group random selection introduces sampling variability.
4. Add a limitations paragraph to the conclusion.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>