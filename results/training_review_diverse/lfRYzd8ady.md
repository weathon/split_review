Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper proposes DCWM (Discrete Codebook World Model), a model-based RL method that uses finite scalar quantization (FSQ) to create a discrete codebook latent space with stochastic transition dynamics trained via cross-entropy (classification) loss. The method avoids observation reconstruction (instead using latent-state consistency) and achieves strong performance on high-dimensional continuous control tasks from DMControl (Dog, Humanoid) and Meta-World. The paper includes extensive ablations to isolate the contributions of discretization, stochasticity, and the classification objective.

## Strengths

- **Strong performance on high-dimensional locomotion tasks**: DCWM substantially outperforms both TD-MPC2 and DreamerV3 on the challenging Dog (223-dim observation, 38-dim action) and Humanoid (67-dim observation, 24-dim action) tasks from DMControl (Figure 4). The margins on these tasks are large and visually unambiguous, providing credible evidence that the discrete codebook approach is particularly beneficial for high-dimensional continuous control (supporting claim C3).

- **Systematic ablations isolate key design decisions**: Section 5.2 and Figure 5 compare six variants crossing latent type (discrete vs. continuous), loss (cross-entropy vs. MSE), and dynamics (deterministic vs. stochastic). The full DCWM (discrete + CE + stochastic) consistently outperforms Continuous+MSE, SimNorm+MSE, Discrete+MSE, and Discrete+CE+det variants. This directly supports claim C1 that the combination of discrete latents with classification-trained stochastic dynamics is what drives the improvement.

- **Principled motivation for codebook over one-hot/label encodings**: Section 3 provides a clear theoretical comparison of encoding types along three axes (ordinal relationships, sparsity, dimensionality), grounded in the properties of FSQ. The ablation in Section 5.3 (Figure 6) experimentally validates that codebook encodings for reward/critic/policy networks yield better sample efficiency than label encodings, and better computational efficiency than one-hot encodings (supporting C2).

- **Broad evaluation across multiple benchmarks**: The method is evaluated on 29 DMControl tasks, 45 Meta-World tasks, and 5 MyoSuite tasks against TD-MPC2, DreamerV3, TD-MPC, and SAC, demonstrating that the approach generalizes beyond a single benchmark.

- **Transparent limitations and honest reporting**: The paper explicitly states where DCWM "generally matches" rather than beats TD-MPC2 (Meta-World), acknowledges that one-hot dynamics failed entirely, discusses limitations to deterministic environments, and provides clear pseudocode (Algorithms 1 and 2).

## Weaknesses

### Fatal
None.

### Major

- **Insufficient statistical evidence from 3 seeds for the strongest claims**: The paper uses only 3 seeds per task (line 149). While this is a common minimum in RL, it is insufficient to robustly support the strong claim in the abstract that DCWM "surpasses recent state-of-the-art algorithms, including TD-MPC2 and DreamerV3, on continuous control benchmarks." The aggregate IQM in Figure 3 shows overlapping 95% bootstrap confidence intervals between DCWM and TD-MPC2. On Meta-World, the paper itself states DCWM "generally matches TD-MPC2." The character of the evidence changes the claim: DCWM demonstrably excels on high-dimensional locomotion tasks (Dog, Humanoid) but the broader superiority claim across all continuous control benchmarks is not uniformly supported by the data presented. More seeds (at least 10) on the key DMControl tasks would substantially strengthen the credibility of the central claim.

### Minor

- **Codebook advantage over one-hot is primarily computational, not sample-efficient, on most tasks**: The paper acknowledges (line 238) that "the one-hot encoding (red) matches the codebook encoding in terms of sample efficiency in all tasks except Humanoid Walk." The superiority of codebook over one-hot is thus driven by computational efficiency (lower dimensionality, faster training) rather than better learning per environment step. This is a real benefit, but the paper's contribution statements and abstract should more precisely distinguish where the advantage is sample-efficiency versus computational. The current phrasing conflates these.

- **Encoder learning signal is underexplored**: The encoder only receives gradients from the first-step dynamics cross-entropy loss and from the reward loss on all steps (subsequent dynamics steps use stop-gradient on target codes; lines 86-91). The paper provides no analysis of encoder representation quality (e.g., codebook entropy, active percentage trajectory, representation similarity across states). Given that TD-MPC2 uses a contrastive-style consistency loss for its encoder, understanding whether the different encoder training signal matters for performance is important. The codebook usage analysis in Figure 10 partially addresses this, but more systematic analysis would strengthen the paper's explanatory power.

- **Disconnect between ablation baselines and main comparison**: The continuous latent space baselines in Figure 5 (Continuous+MSE, SimNorm+MSE) approximate but are not identical to the actual TD-MPC2 algorithm (which has a specific encoder architecture and planning procedure). The main results in Figure 3 compare against actual TD-MPC2, but the ablation conclusions (e.g., "discrete latent spaces significantly outperform continuous ones") are drawn from proxy baselines. While the paper labels these correctly, the subtle gap between the ablation and the main comparison could be acknowledged more explicitly.

### Trivial
None.

## Nice-to-Haves

- Direct comparison with a "continuous + stochastic" variant (e.g., Gaussian dynamics trained with log-likelihood) as a full system. Figure 12 in the appendix provides some of this, but highlighting it in the main text would strengthen the argument about discreteness vs. stochasticity.
- Full-system comparison where all components (including dynamics) use one-hot encoding, even if it fails — showing the failure mode would strengthen the paper's argument for codebook encodings.
- Wall-clock runtime comparison with TD-MPC2 (the paper mentions DCWM has "similar runtime" but does not provide the data).
- Per-task results in a main-text table or heatmap to complement the aggregate metrics.

## Removed Points

These points are flagged to be removed — treat them with caution:

1. **"Unfair comparison between codebook and one-hot encodings"** — The paper is fully transparent that dynamics uses codebook in all conditions because one-hot/label dynamics failed to learn (lines 229-234). This asymmetry (all conditions share the best dynamics) favors the alternative encodings, not the author's method. Per hard rule: remove criticisms about unfair comparison when the asymmetry favors the baseline.

2. **"Label encoding ordinal relationships oversimplification"** — The reviewer claims ordinal relationship discussion is "oversimplified." The paper correctly states that if A<B<C<D, assigning integers 1,2,3,4 preserves |e(A)-e(B)|<|e(A)-e(C)|. This is mathematically correct for ordered categories with labels assigned in the correct order. Nitpick removed.

3. **"No per-task results in main text"** — The parser strips the appendix where these tables likely exist. Per hard rule: remove weaknesses about missing appendix content.

4. **"No discussion of computational cost"** — The paper states "DCWM has similar runtime to TD-MPC2 when using our default hyperparameters" (line 248) and discusses computational efficiency of codebook over one-hot in Section 5.3. Addressed.

5. **"No comparison to discrete latent space with reconstruction"** — This is an additional experiment suggestion, not a weakness of what's presented. Moved to Nice-to-Haves.

6. **"Limitations should also note stochastic environments"** — The paper already has a Limitations section (line 257) stating "we have only evaluated DCWM in deterministic environments."

7. **"Missing related works"** — Per hard rule, do not mention missing related works.

## Novel Insights

The reviews surface a tension not fully resolved in the paper itself: the observed advantage of DCWM on high-dimensional tasks may stem from the combination of (1) the discrete codebook's ability to create an efficient Voronoi partition of the latent space, effectively serving as a learned quantization that simplifies high-dimensional dynamics, and (2) the categorical transition dynamics that can express multimodal next-state distributions where a unimodal Gaussian would struggle. The reviewer's observation that the encoder's gradient signal is limited (only first-step dynamics + reward) raises an interesting question: does the FSQ discretization itself provide sufficient regularization so that the encoder learns useful representations with less supervision than continuous methods require? This is a potential interpretive avenue the paper could explore.

## Suggestions

1. **Run more seeds (at least 10) on the key DMControl tasks** (Dog, Humanoid, Walker, Quadruped) and report per-task statistical significance. This is the single most impactful change for strengthening credibility.

2. **Reframe the abstract and contribution claims** to match the evidence precisely. The current abstract says "surpasses recent state-of-the-art algorithms, including TD-MPC2 and DreamerV3, on continuous control benchmarks." The paper's own evidence shows DCWM "generally matches" TD-MPC2 on Meta-World, and the codebook advantage over one-hot is primarily computational on most tasks. A more precise claim: "excels on high-dimensional DMControl tasks, matches TD-MPC2 on Meta-World, and is more sample-efficient than DreamerV3 across both benchmarks, with computational advantages over one-hot discrete representations."

3. **Add encoder representation analysis**: Report codebook entropy over training, percentage of active codes, and perhaps representation similarity (CKA) across seeds to demonstrate that the encoder learns meaningful structure without reconstruction or contrastive losses.

4. **Clarify the ablation-to-main-comparison bridge**: Explicitly note that the continuous ablations in Figure 5 are simplified versions that isolate the latent-space design choice, while the main results compare against the full TD-MPC2 system.

## Score and Decision

This paper presents a well-motivated method with strong results on challenging high-dimensional continuous control tasks and thorough ablations. The core idea — discrete codebook latent spaces with classification-trained stochastic dynamics — is novel and practically useful. However, the paper's strongest claims of general superiority over TD-MPC2 are undercut by (a) only 3 seeds per task, and (b) the evidence itself showing that on Meta-World DCWM matches rather than surpasses TD-MPC2, and that the codebook advantage over one-hot is primarily computational on most tasks. These are not fatal flaws — the method clearly advances the state of the art on high-dimensional locomotion — but they warrant more measured claims and stronger statistical evidence. The paper would benefit from additional seeds and a more precise framing, but the contributions are solid and well-executed.

**Score**: 7.0 / 10

**Decision**: Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>