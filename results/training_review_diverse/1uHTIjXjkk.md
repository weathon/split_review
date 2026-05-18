Here is my consolidated final review, written after verifying each claim directly against the paper.

---

## Summary

This paper introduces a potential-based motion planning approach using diffusion models. The key idea is to learn energy-based potential functions over trajectories via the denoising diffusion objective, such that the gradient of the learned energy can be followed during sampling to produce collision-free motion plans. The approach is evaluated in 2D, 7D, and 14D configuration spaces, showing competitive performance against both classical (RRT*, BIT*) and learned (MPNet, MπNet, AMP-LS) baselines. A central claimed advantage is **compositionality**: separately trained diffusion potentials can be summed at test time to handle new combinations of constraints without retraining.

## Strengths

1. **Strong empirical results across multiple environments and dimensions.** The method achieves the highest success rates while requiring the fewest collision checks and competitive planning times across Maze2D (2D), KUKA (7D), and Dual KUKA (14D) (Figure 3). In Dual KUKA, it surpasses MπNet by ~35% in success rate with less than 40% of its planning time and 7× fewer collision checks.

2. **Compositionality enables generalization to unseen obstacle counts.** By summing potentials from a model trained on 6 obstacles, the method maintains near-100% success on environments with up to 11 obstacles, while all baselines degrade sharply beyond their training distribution (Figure 5). This is the paper's most distinctive result and directly supports the compositionality claim.

3. **Effective mitigation of local minima, a classic limitation of potential-based planning.** On environments with concave obstacles, where traditional RMP achieves only 28% success, the proposed method achieves 100% success while requiring 3× less planning time than BIT* (Table 2, Figure 6). This concretely demonstrates that the diffusion-based annealing avoids the local minima trap that plagues gradient-based potential methods.

4. **Motion refining scheme boosts success in high dimensions.** The local-perturbation-and-denoise strategy increases success on Dual KUKA from ~47% to 80.8% after 10 refining attempts (Table 1), providing a practical mechanism to improve plan quality without full resampling.

## Weaknesses

### Major

1. **Compositionality evaluation lacks comparison to a jointly trained model.** The paper claims that composition enables handling novel constraint combinations that "a single model cannot handle" (lines 31–33, 181). Yet the composition experiments compare only against the *uncomposed* base model (trained on 6 obstacles, tested on 7–11) or against methods designed for different settings (SIPP). A baseline trained directly on the test distribution (e.g., 11 obstacles, or static+dynamic jointly) is never included. Without this comparison, the reader cannot assess whether composition actually provides benefits over standard training, or whether the advantage is simply that composition avoids retraining — a meaningful but different claim. The test environments for static+dynamic composition (Table 4) involve combining obstacle types seen separately during training, making a jointly trained model a natural and feasible baseline. This is the single most impactful missing experiment.

2. **Real-world evaluation is qualitative only.** Section 6.5 (lines 558–565) presents results on the ETH/UCY dataset with only anecdotal visual comparisons (Figures 10, 11). No quantitative metrics — success rate, collision rate, or comparison to any trajectory prediction/motion planning baseline — are reported. Given that the simulated experiments are thorough, the omission is conspicuous and substantially weakens the real-world claims.

### Minor

3. **Planning time comparisons do not clarify handling of failed trials.** The paper reports average planning time (e.g., "less than 11% of BIT*'s planning time" at line 365, and Table values) but does not specify whether this includes failed trials that terminated due to timeout or only successful plans. For sampling-based methods with a 5s timeout, including failed trials would inflate their averages relative to the diffusion method (which always runs all denoising steps). A fair comparison would report median time on successful plans, or success-rate-vs-time tradeoff curves.

4. **Motion refining procedure is under-specified.** Algorithm 2 uses a noise scale \( k \) that is listed as a hyperparameter but never assigned a concrete value. The denoiser \( f_\theta \) is described as "an iterative diffusion potential denoiser that outputs a clean trajectory" (line 259) — suggesting it runs the full reverse process from step \( k \) to 0 — but this is not explicitly stated, nor is the computational cost of refining compared to full resampling from pure noise.

5. **Probabilistic completeness argument (Section 3.5) is trivial.** The argument relies only on the property that the model assigns positive density to all trajectories (line 269: \( \forall q, f_\theta(q) > 0 \)) combined with the existence of an \( \epsilon \)-ball around any valid trajectory. This reasoning holds for *any* distribution with full support on configuration space — including uniform random sampling. It says nothing specific about the diffusion model or the learned potentials. The paper does not claim this as a core contribution, but presenting it as a formal result is misleading; it should be removed or explicitly reframed as a trivial observation.

6. **MPD (Carvalho et al., 2023) — a related diffusion-based motion planner — appears only in the concave-obstacle comparison (Table 2) but not in the main multi-environment evaluation (Figure 3).** Since MPD is the most directly comparable diffusion-based method, its omission from the primary evaluation weakens the claim of advancing the state of the art. Including it in the main comparison would strengthen the evidence.

### Trivial

7. **No sensitivity analysis for the classifier-free guidance scale** (set to 2.0, line 129). This parameter controls how strongly the model conditions on obstacles; its effect on success rate vs. diversity is not examined.

8. **Dynamic obstacles are simulated with linear trajectories only** (line 331). This is a very simple motion model; real-world dynamic obstacles exhibit complex interaction patterns. The paper acknowledges this implicitly but does not discuss how the method would scale to non-linear obstacle motion.

## Nice-to-Haves

- A comparison between composed potentials and a single model jointly trained on the union of the same data (both obstacle-count scaling and static+dynamic) would directly test whether composition provides advantages beyond simply training on more data.
- Quantitative metrics (success rate, collision rate) on the ETH/UCY real-world dataset, even against simple baselines, would substantially strengthen the real-world claims.
- Reporting median planning time for successful plans only, rather than (or in addition to) average times that may include failed/timeout trials.
- An ablation of the guidance scale to show the sensitivity of success rate to this parameter.

## Removed Points

- **"The paper does not compare to MPD in the main multi-env evaluation" (as a fatal omission):** The reviewer presents this as a major gap, but MPD *is* compared in Table 2 (concave obstacles), and the paper's main evaluation uses a different set of baselines. This belongs at Minor severity, not Major.
- **"The composition experiments do not rule out that joint training would perform equally well" (as a structural flaw):** The reviewer frames this as fatal to the composition claim, but the paper's claim is specifically about generalization to combinations not seen together during training. A jointly trained model on 11 obstacles would *have* seen 11 obstacles during training, making it a test of different capability. The missing comparison would be informative but does not invalidate the existing results. Downgraded from Fatal/Major to Major.
- **"The noise schedule mismatch between independently trained models" (Other Observations):** Both models use the identical diffusion process (same S=100, same schedule), so there is no schedule mismatch. The concern about the composed score deviating from the true product distribution is a known theoretical property of energy-based composition, not a flaw specific to this paper. The paper shows empirical success; a theoretical analysis of when composition would fail is a reasonable suggestion but not a weakness. Moved to Nice-to-Haves.
- **Strength from Strength Finder about probabilistic completeness:** Conflicting with verified weakness #5, this strength is removed per instructions.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an interesting tension: the diffusion-based composition approach provides a practical way to handle *emergent combinations* of constraints at test time without retraining, but the paper does not adequately disentangle whether the performance gain comes from composition *per se* versus simply having more total model capacity or from the repeated application of the same model to different obstacle subsets. The distinction between "composition of distinct specialized models" (static + dynamic) and "composition via repeated application of one model to different subsets" (more obstacles via overlapping subsets) is a design choice with different implications for generalization that the paper does not analyze.

## Suggestions

1. **Add a joint training baseline to the composition experiments.** Train a single model on the full set of 11 obstacles (for the scaling experiment) and on the union of static+dynamic data (for the composition experiment), and compare its performance to the composed model on the same test sets. This is the single highest-leverage experiment to substantiate the compositionality claim.

2. **Report quantitative metrics on the ETH/UCY dataset.** Even basic numbers — success rate, collision rate, average deviation from ground-truth trajectories — would turn the real-world section from an illustration into evidence.

3. **Clarify the planning time reporting.** Specify whether averages include failed trials, and ideally report median time on successful plans.

4. **Specify the value of \( k \)** in Algorithm 2 and explicitly state whether \( f_\theta \) runs the full reverse process from step \( k \) to 0, with a cost comparison to full resampling.

5. **Remove or reframe the probabilistic completeness argument** (Section 3.5) as a trivial observation rather than a formal result.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>