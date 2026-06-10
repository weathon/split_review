Now I have verified all claims against the paper. Let me produce the final consolidated review.

---

## Summary

METRA proposes a new unsupervised RL objective replacing the metric-agnostic KL divergence in mutual-information skill discovery with the Wasserstein dependency measure (WDM), using **temporal distance** as the underlying metric. Through a tractable simplification, the method learns a compact latent space where moving in different latent directions maximizes temporal coverage of the state space. The paper demonstrates that METRA discovers diverse locomotion behaviors in pixel-based Quadruped and Humanoid — a result no prior unsupervised RL method achieves — and outperforms 11 baselines across five environments in coverage, downstream task performance, and zero-shot goal-reaching.

## Strengths

1. **Temporal-distance metric enables pixel-based scalability.** Prior metric-based methods (LSD, CSD) use Euclidean distance, which is meaningless for pixels. By using temporal distance (minimum steps between states), METRA works directly from $64\times64\times3$ images. The empirical payoff is clear: METRA is the *only* method among 11 baselines that discovers locomotion in pixel-based Quadruped and Humanoid (Fig. 3, lines 534–536). This is a genuinely striking qualitative result that no prior work achieves.

2. **Principled replacement of MI with WDM is clearly motivated and derived.** The paper explains why MI is "metric-agnostic" (§3, lines 144–149), why this causes limited coverage, and how replacing KL divergence with Wasserstein distance fixes it. The derivation from the full WDM dual (Eq. 3) through the decomposition $\phi(s)^\top\psi(z)$, telescoping sum, and simplification to the tractable reward $(\phi(s')-\phi(s))^\top z$ (Eq. 8) is logically sound, clearly presented, and connections to prior work (LSD, CSD, DIAYN) are honestly discussed (lines 358–370).

3. **Comprehensive evaluation with consistent advantages.** METRA is compared against 11 prior methods across 5 environments (both state-based and pixel-based). The skill discovery comparison uses the **same SAC backbone** (line 562), controlling for the RL algorithm. Results show best or near-best performance in nearly every setting. The zero-shot goal-reaching (Fig. 6) outperforms LEXA, a dedicated goal-reaching method, on all five tasks. The use of 8 seeds with 95% CIs is appropriate.

4. **Honest limitations discussion.** The paper acknowledges the asymmetry issue in temporal distance being collapsed into symmetric Euclidean distances (lines 391–396), the simplification from setting $\psi(z)=z$ (lines 399–404), and the low UTD ratio (lines 650–653). This transparency is a strength, not a weakness.

## Weaknesses

### Fatal
None.

### Major

1. **No ablation studies.** The paper derives a multi-step objective: (i) replacing MI with WDM, (ii) decomposing the critic as $\phi(s)^\top\psi(z)$, (iii) restricting to last-state WDM with telescoping sum, (iv) setting $\psi(z)=z$, (v) using temporal distance with the corresponding Lipschitz constraint. Each step involves a nontrivial design choice, yet **the word "ablation" does not appear in the paper** (confirmed via grep). We do not know whether temporal distance is the key driver, or whether Euclidean distance on learned state features (the LSD/CSD approach, which the paper notes is equivalent to the same WDM objective but with Euclidean metric) would perform similarly given the same SAC backbone and pixel encoder. We do not know how sensitive results are to the Lagrange multiplier $\lambda$, relaxation $\varepsilon$, or latent dimensionality. The paper's central claim — that the temporal-distance-aware WDM objective drives performance — would be substantially strengthened by controlled ablations. As it stands, the reader cannot attribute performance to any specific component of the derivation versus the overall system.

### Minor

2. **The state-coverage metric is a 2D proxy for a high-dimensional claim.** The quantitative coverage metric for locomotion environments is x-y position of the robot's root (x-only for HalfCheetah, line 565). In the 29-dimensional Ant environment, this is a 2D projection. The paper is transparent about this (Fig. 1 caption: "not necessarily covering every possible leg pose"; lines 97–98: "approximately cover the state space"), and the metric is applied uniformly to all methods. However, the broader language of "state coverage" in headings and claims (§1, §5, figure captions) sometimes elides this qualification. A method that genuinely explores diverse joint-angle configurations in a small x-y area would be penalized by this metric. The downstream task results (Figs. 4, 6) partially address this concern, but the paper would benefit from an additional proxy for joint-space diversity or more precise language about what is being measured.

3. **Exploration comparison uses different RL backbones.** METRA uses model-free SAC while the pixel-based exploration baselines (LBS, Plan2Explore) use Dreamer (model-based). The paper acknowledges this (lines 604–605) and compares on wall-clock time, but wall-clock time does not fully control for differences in sample efficiency and representation learning. This concern is partially mitigated by the skill discovery comparison (same SAC backbone), where METRA also excels, but the exploration comparison specifically is less clean than it could be.

### Trivial
None.

## Nice-to-Haves

- A sensitivity analysis of latent dimension size, Lagrange multiplier $\lambda$, and relaxation $\varepsilon$.
- Empirical verification of how well the Lipschitz constraint $\|\phi(s)-\phi(s')\|_2 \leq 1$ is satisfied during training.
- An ablation comparing METRA's temporal-distance constraint against a Euclidean constraint on learned features using the same SAC backbone and pixel encoder, directly testing whether temporal distance is the key driver.

## Removed Points

- *Harsh critic: "The evaluation metric does not match the central claim of state-space coverage... This is a structural problem."* — Retained as **minor** but downgraded from "structural/fatal" because (a) the paper repeatedly qualifies the claim as "approximate coverage" (lines 18, 72, 97, 159, 211), (b) the metric is applied uniformly across all baselines, and (c) the downstream task results provide complementary validation.

- *Harsh critic: "The paper's characterization of pure exploration methods as trying to 'completely' cover the state space (lines 50–55) is slightly rhetorical."* — Removed as a framing critique with no concrete evidential problem.

- *Harsh critic: "The conversion of the Lipschitz constraint... relies on Theorem 1 (relegated to the appendix), which the parser stripped. This is a nontrivial claim."* — Removed per instructions: the appendix exists in the original submission and was stripped by the parser.

- *Harsh critic: "Different latent dimensionalities across environments with no justification."* — Removed. The paper reports the dimensions (lines 482–484); different capacities for different environments are standard practice.

- *Strength Finder: Several generic/superficial strengths (e.g., "this paper addressed an important problem") removed as they lack specific evidence anchored in the paper's content.*

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel interpretation of the paper's results that goes beyond what the authors already state.

## Suggestions

1. **Add ablations isolating the metric choice.** Compare METRA (temporal-distance Lipschitz constraint) against a version using Euclidean-distance Lipschitz constraint on learned features (the LSD/CSD approach) with identical SAC backbone and pixel encoder for at least one pixel-based environment. This directly tests the paper's central claim about temporal distance being the key enabler.
2. **Add ablations isolating the WDM simplification.** Compare the simplified objective (Eq. 8, $\psi(z)=z$) against a version using the full decomposed WDM objective (Eq. 6) to assess what is lost by the simplification.
3. **Supplement the x-y coverage metric** with a diversity proxy using average pairwise distance in joint-angle space or state embedding space across skills.
4. **Calibrate language** around "state coverage" to match what is actually measured (x-y position), or add more comprehensive metrics.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>