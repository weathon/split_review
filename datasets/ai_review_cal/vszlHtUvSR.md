- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 5
Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary
This paper proposes RDHNet, a rotation-invariant network architecture for continuous-action multi-agent reinforcement learning. The core idea is to replace absolute Cartesian coordinates with relative polar coordinates (distance and angle relative to a chosen reference entity), encode these using entity-type-specific hypernetworks with symmetric aggregation, and integrate the result into value-decomposition frameworks like COMIX. The paper provides formal definitions of permutation and rotational symmetry in MARL, and reports experiments on two continuous-control task families (Cooperative Prey Predator and Cooperative Navigation) showing improved performance over baselines.

## Strengths
1. **Clear formalization of rotational symmetry in MARL (Section 3).** The paper provides explicit definitions of permutation-invariant and rotation-invariant functions (e.g., \(h(P\cdot u, Z) = h(P, Z)\)), which is more rigorous than informal descriptions of symmetry in prior MARL work. This frames the problem in a way that future work can build on.

2. **Relative Direction Layer (RDL) for continuous rotation invariance (Section 4.1).** The conversion of absolute Cartesian coordinates to relative polar coordinates \((d_{ijk}, \theta_{ijk})\) with respect to a selected reference entity is a principled architectural choice for achieving continuous rotation invariance. This directly addresses a limitation of prior work (van der Pol et al., Yu et al.) that only handled discrete rotations at multiples of 90°.

3. **Strong empirical performance trend across 4 of 5 tasks (Table 1, Figure 4).** RDHNet achieves the best mean returns in the majority of tested scenarios, and its advantage over baselines tends to grow with the number of entities (e.g., the 6-predator scenario). This is consistent with the paper's claim that exploiting rotational symmetry compresses redundant representation space.

4. **Entity-type-specific hypernetworks (Section 4.2).** Using separate hypernetworks for different entity categories (predator vs. prey, etc.) allows the model to maintain expressiveness while enforcing symmetry constraints, addressing a known tension between invariance and representational capacity.

## Weaknesses

### Fatal
None.

### Major
1. **Rotation invariance is claimed but never empirically verified.** The paper asserts that RDHNet produces rotation-invariant representations, but provides no direct verification. A simple sanity check — feeding a rotated observation (rotating all agent positions by an arbitrary angle) and confirming that the predicted Q-value or action does not change — is absent. For a paper whose central contribution is a rotation-invariant architecture, this is a significant evidential gap.

2. **Unresolved arctan ambiguity in the angle computation (Section 4.1).** The paper computes \(\theta_{ijk} = \arctan\frac{y_k-y_i}{x_k-x_i} - \arctan\frac{y_j-y_i}{x_j-x_i}\) and notes that \(\arctan\) is \(\pi\)-periodic, creating ambiguity over a \(2\pi\) range, "requiring discarding one of the values based on the specific context, complicating efficient algorithm execution." The paper then states that angles are encoded with \(\sin\) and \(\cos\) (Section 4.2), but this encoding does not resolve the underlying quadrant ambiguity if standard \(\arctan\) (rather than \(\operatorname{atan2}\)) is used. If the sign of the angle is ambiguous, the \(\sin/\cos\) encoding would not produce consistent outputs for rotated inputs, undermining the claimed invariance. The paper must clarify whether \(\operatorname{atan2}\) is used or how the quadrant is disambiguated.

3. **No comparison with prior rotation-invariant MARL methods that the paper critiques.** The related work (Section 2.2) discusses van der Pol et al. (2021) and Yu et al. (2023, 2024), stating they "can only handle rotational symmetry at multiples of 90 degrees" and "cannot be applied to continuous random rotational symmetry." Despite this critique, the experiments include none of these methods as baselines. Without showing either (a) that these prior methods fail on the same tasks (validating the claimed limitation) or (b) that RDHNet outperforms them on tasks where their discrete capability suffices, the paper's novelty claim rests on an untested assertion rather than empirical evidence.

4. **The ablation study does not isolate the effect of rotation invariance cleanly.** The ablation (Figure 5) compares (i) COMIX, (ii) COMIX with HPN (PI-only), and (iii) RDHNet (PI+RI). The gap between (ii) and (iii) involves multiple changes beyond adding rotation invariance: the RDL coordinate transformation, polar encoding schemes, entity-specific hypernetworks, and the full aggregation pipeline. Any of these differences could contribute to the performance improvement. A cleaner comparison would benchmark COMIX with relative coordinates alone (without HPN) and COMIX+HPN+RI to isolate the marginal benefit of each component. This does not invalidate the overall trend, but the claim that the improvement is attributable specifically to rotation invariance is not fully supported.

### Minor
1. **Limited task diversity and environment detail.** The paper evaluates on only two task families (Cooperative Prey Predator and Cooperative Navigation) with simplified dynamics. Standard continuous-control MARL benchmarks (e.g., Multi-Agent MuJoCo, SMAC) are not included. The environment details (observation dimensions, reward functions, number of entities per scenario, number of random seeds) are not specified, making reproducibility difficult. The paper acknowledges limited diversity in its limitations section (Section 6), but the lack of detail remains a concern.

2. **Computational complexity of the reference-entity averaging.** Section 4.3 describes averaging over all entities in the observation as reference targets, leading to \(\mathcal{O}(n^2)\) complexity per agent per timestep (for \(n\) entities). The paper acknowledges this but does not report wall-clock time or memory comparisons against baselines, which would help readers assess the practical trade-off.

3. **Actor-critic evaluation is absent.** The paper claims RDHNet can be used for both action prediction and value evaluation, but experiments evaluate it only as a critic (utility network) within COMIX. The paper acknowledges this limitation, but an evaluation of the architecture in an actor-critic setting (e.g., MADDPG with RDHNet as actor) would strengthen the claim of generality.

### Trivial
None.

## Nice-to-Haves
- Include a direct verification experiment: feed a state and its rotated counterpart through RDHNet and show that the output (Q-value or action) is unchanged.
- Compare against prior discrete-rotation methods (van der Pol et al., Yu et al.) on at least one task to ground the claim that continuous-rotation capability provides practical benefit.
- Clarify whether \(\operatorname{atan2}\) is used in the angle computation (replacing \(\arctan\)) to resolve the quadrant ambiguity discussed in Section 4.1.
- Report the number of random seeds and provide standard deviations/confidence intervals for the results in Table 1.

## Removed Points
- **Ablation study "isolates" the effects (Strength Finder claim #4):** This conflicts with verified Major Weakness #4 (the ablation conflates multiple architectural changes). When a strength and weakness disagree, the weakness wins. The ablation shows a useful trend but does not cleanly isolate rotation invariance.
- **"Strong empirical performance" claim in Strength Finder was retained with caveat**, however the unqualified version is too strong given the unresolved reproducibility details (undisclosed seed count, no standard deviations in text).
- **Reproducibility nitpicks about undisclosed hyperparameters** (Harsh Critic's Missing Parts section): These are standard reproducibility concerns but do not rise to the level of a weakness given the paper states hyperparameter consistency was maintained; they are noted under Minor weakness #1.
- **Criticism that Table 1 is "not visible" (Harsh Critic):** This is a PDF parsing artifact, not a paper flaw. The table is present in the original submission.
- **Criticism about missing code availability:** Not a standard weakness for a conference submission; code is ideally provided at publication.
- **Criticism that the paper "should at least compare against a version of the baselines that uses relative coordinates":** This is partially addressed by the PI+RI ablation, and the suggestion is reasonable but not a necessary criterion for acceptance.
- **Criticism about state occlusion breaking invariance (Harsh Critic Section-by-Section notes):** Speculative — the paper does not discuss occlusion scenarios, and this concern is not grounded in any experiment or observation from the paper.

## Novel Insights
The Harsh Critic's observation that the arctan ambiguity (Section 4.1) is not resolved by subsequent sin/cos encoding is a genuine insight that neither the reviewer list nor the paper itself fully confronts. If the paper uses standard \(\arctan\), the angle could be off by \(\pi\), and \(\sin(\theta+\pi)=-\sin(\theta)\) would break invariance. This is a concrete technical gap that the authors must address. The Critic also correctly notes that the ablation conflates architectural changes — but reframed, this reveals a broader point: the paper's contribution is not "adding rotation invariance to COMIX+HPN" but rather building a complete architecture (RDL + polar encoding + entity-type hypernetworks) that jointly handles both symmetries. The ablation design should reflect this by testing each component's marginal contribution, not just comparing the full system against an incomplete one.

## Suggestions
1. **Add a direct invariance verification experiment** (e.g., take a held-out state, rotate all agent positions by a random angle, and show that RDHNet's Q-value output changes by \(\leq \epsilon\) across many random rotations). This single experiment would dramatically increase confidence in the core claim.
2. **Clarify the angle computation:** explicitly state whether \(\operatorname{atan2}\) is used (and if so, replace \(\arctan\) with \(\operatorname{atan2}\) in Equation (1) to avoid ambiguity), or describe the disambiguation procedure.
3. **Extend the comparison set** to include at least one prior rotation-invariant MARL method (van der Pol et al. or Yu et al.) on the same benchmarks, even if those methods are designed for discrete rotations, to empirically support the claimed limitation.
4. **Clean the ablation** by adding an intermediate condition: COMIX with relative coordinates but without HPN (RI-only), to disentangle the effect of relative coordinate encoding from the hypernetwork architecture.
5. **Report the number of seeds** and provide error bars or confidence intervals for all numerical results, along with basic environment specifications (observation dimensions, reward structure, number of entities per scenario).
