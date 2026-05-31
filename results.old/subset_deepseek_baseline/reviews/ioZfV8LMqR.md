## Summary
This paper introduces a new setting for few-shot design optimization where evaluating a design yields both a scalar reward f(x) and high-dimensional auxiliary information h(x), and a history of related tasks is available. The authors propose a transformer-based neural model that learns to leverage auxiliary information from a small context of observations to predict performance of unseen designs. They create a novel benchmark task involving designing customized robotic grippers using tactile feedback, and demonstrate that their method significantly outperforms baselines that only use reward information in both prediction accuracy and optimization efficiency.

## Strengths
- **Novel and well-motivated problem setting**: The paper identifies a realistic gap in Bayesian optimization—that real-world experiments generate rich auxiliary information beyond scalar rewards—and formalizes this as a new learning problem. The setting is practically relevant to robotics, drug discovery, and scientific experimentation.
- **Strong empirical results on a challenging benchmark**: The gripper design task is non-trivial (21-dimensional design space, high-dimensional tactile feedback), and the method shows consistent and substantial improvements over baselines. The 34.4% vs 26.7% task completion rate and the qualitative examples demonstrating genuinely creative solutions (e.g., rotating the airplane to stabilize it) are compelling.
- **Careful ablation controlling for model capacity**: The authors include an f-only(+p) baseline with more parameters than their model, which performs identically to the smaller f-only model. This convincingly shows that the improvement comes from utilizing auxiliary information, not from increased model capacity.

## Weaknesses
### Fatal
None.

### Major
- **Limited comparison to relevant baselines**: The paper only compares against an f-only baseline and a nearest-neighbor baseline. Given the setting involves multi-task optimization with auxiliary information, comparisons to composite Bayesian optimization methods (Astudillo & Frazier, 2019) adapted to the multi-task setting, or to multi-task GP methods that could potentially incorporate h(x) through custom kernels, would strengthen the evaluation. The paper claims these methods are limited by GP assumptions, but an empirical comparison would substantiate this claim.
- **No analysis of what the model learns from h(x)**: The paper does not provide any analysis or visualization of how the model utilizes the tactile information. For example, which parts of the tactile sequence are most informative? Does the model attend to specific taxels or time steps? This would provide insight into the method's inner workings and validate that it is genuinely learning useful representations rather than exploiting spurious correlations.

### Minor
- **The acquisition function choice is not justified**: The paper uses Probability of Improvement without discussion. Expected Improvement or Upper Confidence Bound might yield different results, and the sensitivity to this choice is not explored.
- **The optimization setup uses a discrete set of pre-evaluated designs**: While this is a practical choice, it limits the generality of the method. The paper mentions continuous optimization is possible but does not demonstrate it, which would be valuable for broader applicability.

### Trivial
- The paper states "Our model with a context size of 10 observations has a lower error than the f-only model with a context of 30 observations" but the actual numbers (155 vs 155) show they are essentially equal at these specific points.

## Nice-to-Haves
- An analysis of how the model's predictions degrade when h(x) is corrupted or partially observed would test robustness.
- A comparison to a method that uses h(x) only through simple summary statistics (e.g., mean tactile force) would help isolate the value of the full high-dimensional representation.
- A study of how the number of training tasks affects performance would be informative for practitioners.

## Novel Insights
The paper's key insight is that auxiliary information in design optimization can be leveraged not just within a single task (as in composite BO) but across tasks through meta-learning. The finding that tactile feedback from failed grasps can be used to infer successful gripper geometries is genuinely interesting and suggests that the model learns a form of "physical intuition" about how shape relates to stability. The qualitative example where the model learns to exploit dynamics (rotating the airplane) indicates the method captures causal structure beyond simple pattern matching.

## Suggestions
- Add comparisons to at least one multi-task BO method and one composite BO method adapted to the multi-task setting. Even if these baselines perform worse, the empirical evidence would strengthen the paper's claims about the limitations of GP-based approaches for high-dimensional h(x).
- Include an attention analysis or feature visualization showing which aspects of the tactile sequence the model finds most predictive. This would significantly increase the paper's impact by providing interpretability.

## Score and Decision
The paper presents a well-motivated new problem setting, a sound method, and strong empirical results on a challenging benchmark. The main weakness is the limited baseline comparison, but this does not invalidate the core contribution. The work is likely to be of significant interest to the ICLR community working on Bayesian optimization, meta-learning, and robotics.

MY FINAL SCORE: <score>8</score>
MY FINAL DECISION: <decision>Accept</decision>