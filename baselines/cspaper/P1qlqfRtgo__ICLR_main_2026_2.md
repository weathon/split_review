---
job_id: 99dec318-4a7f-4f20-a0c6-0aa1b1c0dd82
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: P1qlqfRtgo.pdf
paper: Comparison of Neural Network Architectures in the Thermal Explosion Approximation Problem
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is an ML-for-physical-sciences submission comparing neural architectures for surrogate modeling of stiff chemical kinetics, which fits ICLR’s scope on applications to physical sciences and general machine learning.

## Minimum Quality
Pass ✅. The paper contains the core ingredients of a scientific submission, including abstract, introduction, methodological description, training/evaluation setup, quantitative results, figures, and conclusions. While the novelty and empirical depth are limited, the submission is complete enough to warrant full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, suspicious reviewer-targeting instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies surrogate modeling of thermal explosion dynamics in a hydrogen-oxygen-air mixture using three neural architectures: a plain MLP, a DeepONet-style model, and a U-Net-like residual network. The authors generate a dataset from a stiff ODE solver over a range of temperatures, pressures, and timesteps, train all models with a multi-step rollout loss, and report that the U-Net-style residual network achieves substantially lower test MSE and lower variance than the MLP and DeepONet-style alternatives.

## Strengths
The paper addresses a practically relevant problem, namely learning surrogates for stiff chemical kinetics where direct ODE integration is expensive. This application is legitimate and potentially useful for ML in the physical sciences.

The experimental setup is at least superficially controlled in one important sense: the three models are trained on the same input/output representation, on the same train/validation/test split, and with the same optimizer settings. That makes the central comparison easier to interpret than many applied papers where each baseline gets a different tuning budget.

The paper does make an effort to preserve some simple physical invariants in the architecture and outputs. In Section 4.1 to 4.3, the authors explicitly copy \(dt\), \(N_2\), and Ar from input to output, rather than asking the network to relearn obvious constants. This is a sensible engineering choice for this particular task.

Table 1 is clear and does communicate a nontrivial empirical gap: the U-Net model has a much lower mean MSE (\(1.374\times 10^{-3}\)) than both the MLP (\(2.029\times 10^{-2}\)) and DeepONet-style model (\(1.808\times 10^{-2}\)). The confidence intervals reported in the same table also suggest that this is not just noise from a tiny test set. Even though the analysis around the table is overinterpreted in places, the raw performance difference itself is visible.

Figure 2 is useful for giving the reader a quick visual impression of the three compared architectures. In particular, the residual and skip-connection structure in Figure 2B helps explain what the authors mean by a “U-Net-like” fully connected model, and it makes clear that the strongest model differs from the MLP by more than just width.

Figures 3 and 4 provide qualitative trajectory-level comparisons rather than only scalar error summaries. In both figures, the U-Net prediction appears visually closer to the reference trajectory than the two alternatives, especially around rapid transients. This is helpful because for stiff kinetics, a single averaged MSE can hide timing errors and phase drift.

## Weaknesses
1. **The contribution is quite limited from an ICLR perspective, and the paper does not really move beyond an architecture bake-off.**  
   The main claim is that a residual U-Net-like MLP works better than a plain MLP and a DeepONet-style design on this dataset. That may be true empirically, but the paper does not extract deeper scientific insight about *why* this happens, nor does it formulate a new learning problem, a new algorithm, a new training principle, or even a careful analysis of stiffness-related inductive bias. Section 5 mostly restates that architecture matters and that the U-Net has lower MSE. For ICLR main track, that is a thin contribution unless accompanied by a more incisive analysis.

2. **The DeepONet baseline is not convincingly implemented or justified as a meaningful operator-learning comparator.**  
   In Section 4.3, the model takes a scalar \(dt\) in one branch and the remaining 12 state variables in the other, then combines them via a matrix product. This is described as “following the operator-learning principle of DeepONet,” but the paper does not show that the task is actually posed in a way where operator learning is the right abstraction. Standard DeepONet usually learns mappings between functions and evaluations at coordinates; here the input is just a 13-dimensional state vector with a timestep, and the output is another 13-dimensional state vector. That is closer to one-step state transition regression than to a genuine infinite-dimensional operator setting. As a result, the comparison risks becoming a straw-man version of DeepONet rather than a fair test of operator-learning methods on chemical kinetics.

3. **The comparison is not fair enough to support strong architectural conclusions, because the models are not matched in capacity, tuning budget, or design effort.**  
   The U-Net-style model is not merely a different topology, it also has residual connections and a global skip that are known to ease optimization. The MLP baseline in Section 4.1 is a straightforward feed-forward stack without residuals, and the DeepONet-style model is given a fairly constrained factorized output structure. The paper claims “identical training conditions” in Section 5, but identical hyperparameters are not the same as fair optimization across different architectures. Some models often need different learning rates, widths, depth, normalization, or schedule tuning. Without a modest hyperparameter search per baseline, the paper cannot cleanly attribute the observed gap to architecture alone.

4. **The mathematical specification of the training objective in Equation (4) is incomplete enough to matter.**  
   The loss is defined as
   \[
   \mathrm{Loss}=\sum_{k=1}^{n_{\mathrm{steps}}}\frac{1}{k}\operatorname{MSE}\big(X_{t+k\Delta t},\hat{X}_{t+k\Delta t}\big),
   \]
   with \(n_{\mathrm{steps}}=30\), and the text says models are trained by “recursively forecasting the state vector up to thirty steps ahead.” But the recursion is underspecified. Is the same \(dt\) used repeatedly during rollout? Is the predicted state \(\hat X_{t+k\Delta t}\) fed back autoregressively as input at step \(k+1\)? If so, how are the components that are copied from input to output, especially \(dt\), handled across rollout? Is teacher forcing used at any stage? Since the central training strategy relies on multi-step prediction, these details are not cosmetic. They determine the effective objective and can materially affect stability and performance.

5. **The output-space constraints look physically questionable and are poorly justified.**  
   In Section 4.2, the U-Net output is “clamped to the range \([-10,10]\).” It is unclear what space this is in, because the paper later says Figures 3 and 4 are shown in a normalized space, but the preprocessing itself is never properly defined. If concentrations and temperature are normalized, what normalization is used, per-variable standardization or min-max scaling? If species concentrations are physically nonnegative, why is a symmetric clamp to negative values acceptable? More importantly, clamping can artificially improve numerical stability while distorting gradients and hiding physically invalid predictions. This needs explicit explanation because it could be one reason the U-Net appears more robust.

6. **The data generation and evaluation protocol is too vaguely described to assess generalization.**  
   Section 3 states that \(T\in[250,5000]\) K, \(p\in[10^4,2\times10^7]\) Pa, and \(\Delta t\in[10^{-10},10^{-5}]\) s are sampled over a “wide variety of randomized thermodynamic conditions,” but the sampling distribution is not specified. Uniform in linear scale or log scale? Independent across variables or conditioned on physically meaningful states? How are initial species concentrations sampled, and how is mass conservation enforced in the sampled initial conditions? These details are essential because a random i.i.d. split of states from the same generated trajectories can substantially overestimate generalization if nearby states from one trajectory appear in both train and test.

7. **The paper never clarifies whether the split is trajectory-level or state-level, which raises a serious leakage concern.**  
   On Page 4, the paper says the dataset is split into 50,000 training, 15,000 validation, and 5,000 test samples, but it does not say whether a “sample” is an individual state transition or an entire trajectory. Given that Figure 1 shows kinetic trajectories and the task is next-state prediction, this distinction matters a lot. If temporally adjacent states from the same ODE rollout are distributed across train and test, the reported error would not reflect extrapolation to unseen conditions. This is one of the most important missing experimental details in the paper.

8. **The empirical evaluation is too narrow for the paper’s claims about robustness and practical value.**  
   The authors report only MSE statistics in Table 1. For chemically reactive systems, this is not enough. The paper makes claims about preserving “physical consistency,” “correct qualitative dynamics,” and handling “rapid transients and slower reaction dynamics,” but it does not evaluate physically meaningful metrics such as ignition delay error, peak temperature timing, species peak timing, conservation-law violations, negativity rates, or stability over long rollouts. Figures 3 and 4 are suggestive, but two cherry-picked trajectories do not substitute for systematic diagnostics.

9. **The statistical analysis around Table 1 is overstated and somewhat superficial.**  
   The paper uses non-overlapping 95% confidence intervals to claim “statistically significant improvement.” That heuristic is not always a proper significance test, and more importantly, it is not clear what random variable the CI is over. Is it over test-sample MSEs, over repeated training runs, or over something else? The paper reports one mean, one standard deviation, and one CI per model, but does not explain whether model stochasticity from random initialization was measured. If these are sample-level CIs over one fixed trained model, they say little about reproducibility of the training outcome. This is especially relevant because the paper’s main thesis is architectural superiority.

10. **Figure-level evidence is under-analyzed and may be selectively presented.**  
   Figure 3 is explicitly described as a trajectory from the lowest 10% of test-sample MSE values, which is effectively a best-case example. Figure 4 is from the upper quartile, but again only one example is shown. The figures do visually suggest that the U-Net tracks transients better, especially around ignition-like rapid changes, but the paper never quantifies how representative these examples are. If the goal is to support claims about robustness, the paper should aggregate trajectory-level quantities across the full test set rather than leaning on two handpicked plots.

11. **The architecture description is not fully consistent with the terminology used.**  
   Calling the strongest model a “U-Net-like residual network” is somewhat misleading. According to Section 4.2 and Figure 2B, this is essentially a fully connected residual MLP with local and global skip connections, not a U-Net in the usual encoder-decoder sense with multi-resolution contraction and expansion paths. The naming is not fatal, but it inflates the architectural story. If the key ingredient is residual learning on tabular state vectors, the paper should just say so.

12. **Important practical claims are unsubstantiated, especially regarding computational benefit.**  
   The introduction motivates the work by saying ODE solution is the main computational bottleneck and that neural models can significantly speed up calculations. However, the paper never reports inference time, end-to-end speedup, memory cost, or cost-accuracy tradeoffs for the three surrogates relative to the stiff solver. A surrogate that is more accurate but not meaningfully faster would only partially support the stated motivation.

13. **The literature positioning is incomplete and dated relative to the exact problem setting.**  
   The paper cites some general DeepONet and combustion references, but the related discussion is sparse and mostly placed in the introduction. There is little engagement with more recent ML architectures for reactive-flow or combustion surrogate modeling beyond a couple of DeepONet-related references. This weakens the claim that the presented comparison meaningfully advances the state of knowledge rather than reproducing an expected result that residual architectures train more easily than plain MLPs.

14. **Presentation quality is uneven, and several statements are too strong relative to the evidence.**  
   There are multiple places where the prose overreaches, for example claiming that architecture is the “primary determinant of performance” or that the U-Net preserves “physical consistency,” without experiments that isolate those claims. There are also numerous language issues and imprecisions, such as “During the mechanism 9 hydrogen-oxygen compounds are formed,” “Such careful selection open the way,” and inconsistent notation between species counts and vector dimensions. The paper remains readable, but the exposition is not at the level where I can trust the stronger scientific claims without additional evidence.

## Questions
1. **What exactly is one training/test sample?**  
   Please clarify whether the split is done at the level of trajectories or individual state transitions. If trajectories are split across train and test, please report results with a strict trajectory-level split, since that would substantially increase my confidence in the generalization claims.

2. **Can you fully specify the rollout training procedure in Equation (4)?**  
   I would like a step-by-step description of how recursive prediction is performed during training: what is fed into the model at rollout step \(k+1\), whether \(dt\) is constant across the 30-step horizon, whether teacher forcing is used, and how the copied variables are handled. This is central to assessing both correctness and reproducibility.

3. **How is the data normalized, and in what space is the output clamp \([-10,10]\) applied?**  
   Please define the preprocessing transform for each variable. Also explain why clamping to a symmetric interval is physically acceptable for concentrations and temperature, and provide an ablation showing whether this clamp materially affects the U-Net advantage.

4. **Did you tune the baselines separately, or were all architectures forced to use the same hyperparameters?**  
   A modest per-model tuning budget, even a small one, would make the comparison much more credible. If such tuning was done, please report it. If not, please explain why the current setup should be interpreted as an architectural conclusion rather than an implementation-specific one.

5. **Can you report physically meaningful metrics beyond MSE?**  
   In particular, ignition delay error, peak temperature timing error, species peak timing, negativity rate for concentrations, and any conservation-law residuals would help. These would directly test the paper’s claims about capturing “key reaction regimes” and maintaining physical fidelity.

6. **What is the actual computational gain relative to the stiff ODE solver?**  
   Since the motivation is acceleration, please report inference throughput or wall-clock speedup, ideally along with accuracy-speed tradeoffs for the three models.

7. **How reproducible are the results across random seeds?**  
   Table 1 could reflect variation across test samples rather than training runs. Please report mean and variance over multiple training seeds. If the U-Net remains consistently superior, that would strengthen the paper materially.

8. **Why is the DeepONet-style model the right operator-learning baseline for this problem formulation?**  
   Please explain the operator-learning viewpoint more carefully, and ideally compare against a stronger or more standard operator-learning baseline if possible. As written, the current DeepONet-style implementation feels only loosely connected to the canonical setting.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the paper. The work uses simulated chemical-kinetics data and does not involve human subjects, personal data, or obviously sensitive datasets. While combustion modeling can in principle have dual-use aspects, the paper is a standard surrogate-modeling study and does not introduce a uniquely concerning capability.

## Soundness Rating
2: fair. The central empirical observation, that the residual U-Net-like model outperforms the two alternatives on the reported test set, is plausible and supported by the presented table and figures. However, the experimental protocol, loss specification, fairness of baseline tuning, and generalization setup are not described rigorously enough for a stronger soundness score.

## Presentation Rating
2: fair. The paper is readable and includes useful figures and a clear summary table, but important details are missing, some terminology is imprecise, and several claims are stronger than what the evidence supports.

## Contribution Rating
1: poor. The paper mainly offers a limited three-model comparison on one application setting, without sufficient methodological innovation, analytical depth, or breadth of evaluation to constitute a strong contribution for the broader ICLR community.

## Overall Rating
2: Reject, not good enough. The application is relevant and the reported U-Net advantage is plausible, but the paper remains too narrow and under-analyzed for ICLR. The core result is essentially that a residual architecture works better than a plain MLP and a weakly justified DeepONet-style baseline, and the paper does not provide enough methodological rigor or scientific insight to elevate that observation into a strong conference contribution.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the relevant ML issues around architecture comparison, rollout training, and surrogate modeling, though some domain-specific combustion details are outside my deepest area of expertise.