Now let me write the consolidated review.

## Summary

The paper addresses the problem that hindsight relabeling in goal-conditioned RL (GCRL) can reward non-interactive trajectories that don't advance the actual goal, hurting sample efficiency in object-centric domains. It proposes (1) Null Counterfactual Interaction Inference (NCII), which formalizes object interactions via a counterfactual test (if removing object i changes the transition dynamics of object j, then i interacts with j) and learns a masked forward model to infer these interactions, and (2) Hindsight Relabeling using Interactions (HInt), which uses inferred interaction graphs to filter hindsight replay, keeping only trajectories where the agent's actions causally affect the target object. Experiments across Random DAG, Spriteworld, Robosuite, Air Hockey, and Franka Kitchen show NCII achieves statistically significant improvements in interaction inference accuracy, and HInt yields up to 4× sample efficiency gains over vanilla hindsight and other baselines.

## Strengths

- **Principled formalization of interactions via null counterfactuals (Definition 3.1).** The paper replaces the intractable invariant-set requirement of prior actual-cause work with a tractable null-counterfactual definition: a cause object interacts with a target if nulling the cause changes the transition probability of the target. This is a clean, novel formalization that directly enables learning-based inference, and the empirical results (Table 1) show NCII achieves statistically significant reductions in misprediction rate across all five domains against baselines including JACI, gradients, attention, and NCD.

- **HInt delivers clear sample efficiency gains in GCRL.** The core idea — filter hindsight trajectories to only those where the agent's actions causally affect the target object — is well-motivated and empirically validated. Figure 4 demonstrates that HInt with either ground-truth contacts or learned NCII interactions outperforms HER, prioritized replay, f-policy gradients, and ELDEN across Spriteworld, Robosuite, Air Hockey, and Franka Kitchen, with up to 4× sample efficiency improvement. The heatmap in Figure 5 provides direct qualitative evidence that HInt removes trivial goals from the hindsight buffer.

- **Learned interactions (NCII) match ground-truth performance.** Section 5.2.2 shows that HInt with NCII-inferred interactions matches or exceeds HInt with ground-truth contact-based filtering in five domain variants. This is an important result demonstrating that the learned inference is accurate enough to deliver the same benefits without hand-coded contact detectors.

- **Diverse empirical evaluation across both dynamic and quasistatic domains.** The paper evaluates on five distinct environments covering 2D collision dynamics (Spriteworld), 3D quasistatic pushing (Robosuite), 2D dynamic striking (Air Hockey), 3D articulated manipulation (Franka Kitchen), and synthetic linear dynamics (Random DAG). This breadth supports the generality of the proposed methods.

## Weaknesses

### Fatal

None.

### Major

- **Insufficient explanation of null-state data generation for physical domains.** The NCII method's central training step (Equation 2) requires data where state factors are absent (null states). The paper explicitly states this "is only possible in settings where each trajectory can contain a different subset of the state factors" (Section 4.1). For the Random DAG domain, this is clearly explained ("each length 50 trajectory randomly samples a subset of the factors"). However, for the physical domains (Robosuite, Air Hockey, Franka Kitchen), where every trajectory contains all objects, the paper merely mentions "provided with null data or simulated nulling" (Section 5.1.1) with no explanation of what "simulated nulling" entails — e.g., whether it means setting state variables to a sentinel vector, removing objects from the simulator, or using the iterative refinement procedure (retraining f with h's outputs) to handle OOD queries. The paper also mentions reweighting/augmentation to address rare interactions (end of Section 4.1) but does not connect this to the null-state data problem. This lack of detail undermines reproducibility and would prevent a reader from applying NCII to a new domain. The authors should specify for each physical domain exactly how null-state training data was obtained and what encoding was used for the null state of continuous variables (e.g., position, velocity).

### Minor

- **Missing comparison to a simple movement-heuristic baseline.** The paper acknowledges in Section 4.2 that "compared to domain-specific heuristics, such as checking if the target object has moved, interactions can apply to any relationship between primitive agent actions, and effects," and argues for the principled approach on generality grounds. However, no experiment compares HInt against this obvious heuristic baseline (e.g., filtering trajectories by whether the target object's position/velocity changes beyond a threshold). Such a baseline would directly test whether the expensive interaction inference machinery is necessary or whether a cheap proxy suffices in the evaluated domains. Given that HInt is proposed as a general solution, this comparison is needed.

- **No ablation of the chain length limit in HInt's filtering criterion.** The paper states "we limit the length of a chain in the graph to two state factors, and actions" (Section 4.2) but provides no ablation or justification for this specific choice. Varying the maximum path length (1, 2, 3, unlimited) would show whether this design choice is critical or robust.

- **No sensitivity analysis of the ε_null threshold.** The interaction detection in Equation 3 relies on a hard threshold ε_null. The paper does not study how this choice affects inference accuracy or downstream RL performance across domains. As a key hyperparameter, its sensitivity should be analyzed.

- **Quantitative metric missing for the goal distribution analysis.** Figure 5 provides a qualitative heatmap showing that HInt filtering better matches the desired goal distribution, but no quantitative divergence measure (e.g., KL divergence, Wasserstein distance) is reported. This would strengthen the claim that HInt meaningfully shifts the hindsight distribution.

- **Limitations discussion does not address the null-state data requirement.** The conclusion's limitations paragraph mentions only "limited utility in domains where interactions are less critical" and does not discuss the practical limitation that NCII requires null-state training data, which may be unavailable in many real-world settings. This is a notable omission given the centrality of this assumption.

### Trivial

- The text has a few minor typos (e.g., "flitering" instead of "filtering," "asses" instead of "assesses") and some incomplete sentences in the reproducibility statement, though these are parser artifacts.

## Nice-to-Haves

- Investigating whether NCII can be trained without explicit null-state data (e.g., via density estimation or modeling null states as OOD inputs) would broaden its applicability.
- Reporting statistical significance (e.g., paired bootstrap) and confidence intervals for the 4× sample efficiency claim across more seeds (10–20) would strengthen the headline result.
- Concrete failure case analysis showing trajectories that HInt correctly keeps vs. incorrectly filters would help readers understand the method's limitations.

## Removed Points

*"Only 5 random seeds are used, which is insufficient to establish statistical significance"* — 5 seeds is standard practice in RL papers for these types of environments and is aligned with community norms. The paper also shows standard error shading.

*"The table is presented as an image; the actual numeric values are not given in the text"* — This is a formatting observation, not a substantive weakness. Table 1 as rendered is the standard way numerical results are presented.

*"no standard deviations or confidence intervals are reported for the 4× factor"* — The 4× claim describes the relative sample efficiency observed in the learning curves (one method reaches a given success rate at ~0.5M steps where another takes ~2M steps). Standard error is shown on the curves. This is standard reporting for such claims.

*"the paper overstates the problem... is asserted without a concrete demonstration that HER fails in the evaluated domains"* — HER is included as a baseline and its performance is shown in Figure 4, providing concrete evidence.

*"f-policy gradients is cited... but not clearly described"* — The paper provides a one-sentence description of each baseline, which is standard for the experimental setup section.

*"Prioritized replay with hindsight uses TD error to prioritize high error states"* — This is a description, not a weakness; the paper accurately describes this baseline.

## Novel Insights

The reviews surface a useful tension: the null-counterfactual definition is elegant and principled, but its empirical instantiation (NCII) requires training data that simulates object absence. The paper's iterative procedure — where the inference model h is trained on the forward model f's null-outputs, and f is retrained on h's predictions — is an interesting bootstrapping approach that could potentially reduce the dependence on explicit null-state data. However, the paper does not isolate whether this iterative refinement alone suffices for physical domains or whether explicit null-state data (or "simulated nulling") was necessary. An ablation separating these two sources of null-state information would be valuable. The reviews also highlight that the HInt algorithm's contribution is somewhat decoupled from NCII's — HInt can work with ground-truth interactions, and the paper's strongest RL results do not depend on perfect inference. This suggests that the paper's main practical contribution (HInt for GCRL) is more robust than the inference contribution (NCII), even though NCII is presented first.

## Suggestions

1. **Clarify null-state data generation.** Explicitly describe for each physical domain how null-state training data was created for NCII. If "simulated nulling" was used (e.g., setting state variables to a zero vector or other sentinel), specify the exact encoding. If the iterative refinement (training f then h then f again) was used to bootstrap from limited null data, explain the process and its duration (how many iterations, convergence criteria).
2. **Add the movement-heuristic baseline.** Compare HInt against a simple filter that checks whether the target object's position or velocity changes between trajectory start and end. If HInt matches or beats this baseline, the result strengthens the paper; if the simple baseline is competitive, the paper should discuss when the extra complexity of NCII is warranted.
3. **Ablate the chain length limit.** Vary the maximum path length in the temporal interaction graph (1, 2, 3, unlimited) and report downstream RL performance.
4. **Add sensitivity analysis for ε_null.** Show how interaction inference accuracy and/or RL performance vary with this threshold, and describe how it was set across domains.
5. **Report a quantitative divergence metric for Figure 5.** Compute KL divergence or Wasserstein distance between the goal distribution and the (HInt-filtered vs. vanilla) hindsight distributions.

## Score and Decision

**Originality:** 7/10 — The null-counterfactual formalization of interactions and its application to hindsight filtering are novel.  
**Importance of research question:** 8/10 — The problem of spurious hindsight goals in object-centric GCRL is well-recognized and practically important.  
**Claims supported:** 6/10 — The main claims are supported by diverse experiments, but the null-state data generation is inadequately explained, and a key baseline is missing.  
**Soundness of experiments:** 6/10 — Reasonable breadth but missing ablation, sensitivity analysis, and the movement-heuristic baseline.  
**Clarity of writing:** 7/10 — The core ideas are communicated clearly; the main clarity gap is the null-state data handling for physical domains.  
**Value to community:** 7/10 — HInt is a practical, well-motivated method that could be adopted by practitioners, and the null-counterfactual formalization may stimulate further work.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>