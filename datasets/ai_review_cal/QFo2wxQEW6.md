- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5
Now I have verified all the claims against the actual paper. Let me construct the final consolidated review.

## Summary

This paper presents CathSim, an open-source, real-time endovascular simulator built on MuJoCo, designed to support machine learning research for autonomous catheterization. It includes four anatomically diverse aortic models, a guidewire model with capsule-based collision, a simulated robotic follower, and validation against a real robotic system (CathBot). The paper also introduces an Expert Navigation Network (ENN) trained with SAC that uses multimodal inputs (image, segmentation mask, joint positions/velocities) and demonstrates its utility in downstream imitation learning and force prediction tasks.

---

## Strengths

1. **First open-source endovascular simulator purpose-built for ML**: The paper releases a simulator that is (a) open-source, (b) real-time (40–80 FPS, Section 5.2), (c) Gymnasium-compatible for RL workflows, and (d) validated in part against real-world force data from the same phantom model used by Kundrat et al. This fills a genuine gap — existing simulators are predominantly closed-source or too slow for training iterative ML pipelines (Table 1 comparison).

2. **Real-time training speed is convincingly demonstrated**: The paper reports training a SAC policy for 600K time steps in 2–5 hours on an RTX 2060 (Section 4.1, Training Details), and the simulator runs at 40–80 FPS (Section 5.2). This is a concrete, verifiable advantage over computationally heavy closed-source simulators and is directly relevant to the stated goal of enabling rapid ML development.

3. **Multiplicity of anatomically realistic aortic models**: Four distinct models are included (Type-I, Type-II, Type-I with aneurysm, patient-specific low-tortuosity CT model) sourced from real silicone phantoms (Elastrat), providing anatomical diversity beyond a single phantom (Section 3, Aorta paragraph). The V-HACD convex decomposition approach for collision modeling is clearly described.

4. **Honest and thorough limitations section**: The Discussion (Section 6) explicitly acknowledges the rigid-body/deformability gap, the simulator-specific bias of ENN trajectories, the absence of real-robot transfer, and the fact that ENN uses privileged information unavailable in real procedures. This transparency is commendable and lets readers calibrate the claims appropriately.

5. **Modular, well-documented architecture**: The simulator is decomposed into four clearly described components (follower robot, aorta, guidewire, blood simulation) with explicit modeling choices (e.g., serpentine guidewire model with revolute joints, frictional actuation simplified to perfect slip prevention for speed). The design choices are justified in terms of the computational-efficiency goal.

---

## Weaknesses

### Fatal
None.

### Major

1. **Force validation compares to a Gaussian fit of real data, not the raw real data itself**: Section 5.1 states: "We compare the observed empirical distribution and a normal distribution derived from the real experiments… We derive a cumulative distribution by sampling data from a Gaussian distribution given the experiments by Kundrat et al." The Mann-Whitney test (p≈0.445) therefore tests whether CathSim's forces are statistically indistinguishable from a **Gaussian noise fit** of the real data, not from the raw real-world force measurements. This conflates two questions: (a) whether CathSim matches the real distribution, and (b) whether the real distribution is Gaussian. A direct comparison (e.g., Kolmogorov–Smirnov test on the raw real samples, had they been available) would be the proper methodology. As presented, the evidence for "CathSim successfully mimics the behavior of the real-world robotic system" is weaker than the text suggests. The authors should either obtain the raw data from Kundrat et al. for a direct comparison, or explicitly reframe this as a preliminary validation using a parametric approximation.

2. **Validation is limited to force magnitude on one aorta type with no trajectory or position validation**: The only quantitative validation is force-distribution matching on the Type-I aorta model. No comparison is made for trajectory shape, guidewire tip position accuracy, contact locations, or any other metric relevant to endovascular navigation. The user study (10 novices, not expert interventionists) provides subjective feedback but does not benchmark quantitatively against real procedure data. For a simulator that purports to "significantly accelerate research in the autonomous catheterization field," the validation scope is narrow.

### Minor

3. **ENN vs. human comparison is acknowledged as unfair but the framing still overstates it**: The paper notes (Discussion, Section 6) that ENN uses multiple privileged modalities (segmentation masks, joint positions/velocities) while the human surgeon operates with only a camera image via a keyboard (discretized actions). This is correctly disclosed. However, the paper still states "ENN outperforms human surgeons in some metrics" (abstract and Section 6) and "half of them exhibited superior performance compared to the human operator" (Section 5.2) without sufficiently emphasizing in the results section itself that the comparison is apples-to-oranges. Given the asymmetric information and control interface, the human comparison does not demonstrate that ENN is a clinically meaningful expert — it demonstrates that more information + continuous control beats less information + discrete control in simulation.

4. **The downstream tasks are basic demonstrations with weak baselines**: The imitation learning experiment compares Behavioral Cloning with ENN trajectories against a BC baseline using only image input (Table 5, referenced). The force prediction experiment shows that more ENN-generated samples reduce MSE — a near-trivial result. There is no comparison to human-expert demonstrations, no comparison to alternative simulators (acknowledged as infeasible, but this limits the evidence for "CathSim enables something previously impossible"), and no analysis of whether the learned policies would transfer to a real robot. The experiments demonstrate that CathSim can be used for ML, which is useful, but do not constitute strong evidence that it will "significantly accelerate research."

5. **No error bars or variance reported for the main navigation metrics**: Section 4.1 states training used 5 random seeds, but the quantitative results (Table 2, main navigation table) appear to be reported without confidence intervals, standard deviations, or per-seed breakdowns. This makes it impossible to assess the statistical reliability of the reported advantages over baselines.

### Trivial

6. **The 168-dimensional joint space is unexplained**: The guidewire is described as comprising "numerous rigid segments" (Section 3, Guidewire), but the paper never states how many segments this corresponds to, nor why 168 dimensions are needed for joint positions (and another 168 for velocities). This is a small detail that should be clarified for reproducibility.

---

## Nice-to-Haves

- A direct force-distribution comparison using the raw real-world data (e.g., via KS test or Earth Mover's Distance) rather than a Gaussian proxy would substantially strengthen the core validation.
- Adding a human-expert demonstration baseline in the imitation learning experiment would make the "expert trajectory" claim more concrete.
- Reporting per-seed results or confidence intervals for the main navigation metrics (Table 2) would improve statistical rigor.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"First open-source" claim needs qualification** (Harsh Critic): The paper claims "the first open-source simulator for endovascular intervention." Per review policy, I cannot verify or challenge this claim without external sources, and the rule prohibits raising missing-related-work criticisms. **Removed.**

2. **Criticism of rigid-body assumption as inappropriate** (Harsh Critic): The paper explicitly acknowledges this limitation in the Discussion ("Second, in order to simplify the simulation and enable real-time factors, we utilize rigid body and rigid contact assumptions, which do not fully align with the real world where the aorta is deformable and soft"). The paper also notes it is "a well-known assumption in many state-of-the-art simulators to balance the computational time and fidelity." The criticism is already addressed. **Removed.**

3. **Criticism that "Table 2 was not visible"** — parser artifact; the original submission has the table. **Removed.**

4. **Criticism about missing appendix content or proofs** — known parser stripping. **Removed.**

5. **Strength Finder claim #3 (downstream quantitative gains)** — some of the cited numbers (0.123N, 0.342N, etc.) are from \input tables whose content is not fully visible in the parsed text. However, the paper text in Section 5.3 corroborates the general claim that ENN-augmented BC outperforms the image-only baseline. Kept as a qualified strength. **Retained with caveats.**

6. **Generic "evaluation lacks rigor" sweep** from the Harsh Critic's preamble — removed as it lacks specific, verifiable anchor in the paper. Specific sub-claims (Gaussian fit issue, limited validation scope, no error bars) are retained as individual points.

7. **Criticism that "not providing evidence that no open-source alternative exists"** — removed per missing-related-works rule.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surfaced no synthesis that the paper itself does not already articulate: the simulator fills a clear gap, the validation is a useful start but methodologically imperfect, and the downstream demonstrations are preliminary. The paper's own Discussion honestly captures the key limitations.

---

## Suggestions

1. **Redo the force validation against the raw real-world data directly** (obtain the raw force recordings from Kundrat et al. if possible, or partner with them). A direct distribution-comparison test (KS test, EMD, or similar) on the actual measured forces, rather than on Gaussian samples derived from them, would significantly strengthen the central validation claim.

2. **Expand validation to include at least one additional axis** (e.g., trajectory shape similarity, tip position error over time) on a second aorta model to demonstrate that the simulator captures more than aggregate force statistics.

3. **Reframe the human comparison** more carefully: put it in a dedicated "qualitative comparison" subsection with explicit caveats up front, or remove it entirely if it is not needed to support the paper's main claims (the ENN's value is in generating expert trajectories for downstream tasks, not in beating a human in an asymmetric comparison).

4. **Report per-seed results or confidence intervals** for the main navigation metrics (Table 2) to make the results statistically interpretable.

---
