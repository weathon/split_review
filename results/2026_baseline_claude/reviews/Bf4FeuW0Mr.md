## Summary

DemoGrasp proposes a framework for universal dexterous grasping by formulating the problem as a **single-step MDP over demonstration editing**: given a single demonstration trajectory, an RL policy learns to output an SE(3) wrist transformation and delta hand joint angles that adapt the demonstration to novel objects and poses. This reformulation drastically simplifies exploration compared to full multi-step RL over raw actions. A flow-matching vision policy is then trained via imitation on successful rollouts with rendered images for sim-to-real transfer. The method achieves 95% success on DexGraspNet (Shadow Hand), 84.6% average generalization across six unseen datasets and multiple embodiments, and 86.5% real-world success on 110 objects including thin and small items.

---

## Strengths

- **Elegant and principled reformulation.** Converting the multi-step grasping MDP into a single-step editing problem over a structured demonstration is a genuine conceptual advance. By restricting the search space to (SE(3) transformation, Δq), the exploration challenge collapses from thousands of timesteps of high-dimensional control to a single low-dimensional decision. The translation-invariance property of replay (same grasp outcome regardless of object position) is a direct and useful consequence that enables spatial generalization for free.

- **Strong quantitative results with clean ablations.** On DexGraspNet, DemoGrasp surpasses UniGraspTransformer by +5% state-based and +4% vision-based (Table 1). Training on only 175 objects yields within 2.4% of training on the full test sets (Table 7), indicating the method is data-efficient. Ablations cleanly decompose the contributions of each component of the action space (Table 8), demonstrate robustness to demonstration quality (Table 9), and show that RL over sampling+BC is essential (Table 5, +18.7%).

- **Cross-embodiment universality without hyperparameter tuning.** The same method—same single demonstration, same reward—transfers to six embodiments (five-fingered, four-fingered, three-fingered, parallel gripper), achieving >90% on training objects and 84.6% average on unseen datasets. This is a practically significant finding given how much prior work is tied to specific hand morphologies.

- **Real-world impact including previously unsolved scenarios.** The claim that this is the first tabletop grasping policy to reliably handle small (<3.5 cm) and thin (<1.5 cm) objects without severe arm-table collisions is well supported by the 76.7% and 68.3% success rates on those categories, and is explained mechanistically by the reward's ability to selectively permit finger-table contact only when needed.

- **Simplicity of reward design.** Using only binary success × no-collision (Eq. 3) eliminates the elaborate distance shaping, curriculum schemes, and privileged contact observations relied on by prior methods, which is a significant practical advantage for adoption and extension.

---

## Weaknesses

### Fatal
None.

### Major

- **Table 2 cross-method comparison is not fully controlled.** The comparison with RobustDexGrasp uses different training sets. While the authors acknowledge this and argue both methods aim at universal grasping, the performance difference could stem from training distribution rather than method design. A controlled experiment on the same training objects, or at least a baseline run of DemoGrasp's closest ablation in RobustDexGrasp's setting, would strengthen this comparison.

- **Assumption of a single global demonstration structure.** The editing formulation (Eqs. 1–2) assumes a fixed approach→grasp→lift structure parameterized by T_lift. This structure covers tabletop pick-and-place well, but the generality of the formulation to other grasping configurations (e.g., lateral retrieval, drawer pulls) is not analyzed. The paper frames DemoGrasp as a "foundation for future manipulation research," but the extent to which the formulation generalizes beyond top/side tabletop grasping is unclear.

### Minor

- **The open-loop RL policy combined with a separately trained vision policy introduces potential distribution shift.** The RL policy is state-based and the flow-matching policy imitates it from rendered images. While this works well empirically, the paper does not discuss what happens when the vision policy's action distribution diverges during execution (e.g., in recovery from failure). The regrasp behaviors mentioned are shown qualitatively but not quantified.

- **Radar chart data (Figure 3) is reported identically across all six embodiments in the table** (all rows show 49.4, 30.7, 91.1, 83.5, 61.2, 66.6), which is clearly a PDF parsing artifact. The radar chart itself displays distinct values.

### Trivial
None worth noting.

---

## Nice-to-Haves

- An analysis of failure modes in the real world (e.g., what fraction are approach failures vs. slip failures vs. visual mislocalization) would help practitioners understand deployment risks.
- A controlled comparison where DemoGrasp and a strongest baseline (e.g., RobustDexGrasp) are both trained on the same 175 YCB+DexGraspNet objects would more cleanly isolate the method's advantage.

---

## Novel Insights

The key insight—that universal grasping can be reduced from a high-dimensional, long-horizon multi-task RL problem to a single-step MDP in a low-dimensional demonstration-editing space—is both simple and surprisingly powerful. The demonstration provides a structured inductive bias (the motion envelope) that makes exploration tractable, while the RL learns the residual degrees of freedom (where and how to grasp per object). A further underappreciated observation is that translation invariance from demo-replay eliminates spatial generalization as a learning problem entirely: the policy never has to learn to handle different object positions since this is absorbed by the replay mechanism. This suggests a broader principle: embedding known symmetries of a task directly into the policy's action parameterization, rather than expecting RL to discover them, may be a high-leverage design choice in other manipulation domains.

---

## Suggestions

- Include a failure mode breakdown (at least for real-world experiments) categorized by object type and failure cause.
- Provide a controlled baseline where both DemoGrasp and RobustDexGrasp use the same training object set, to isolate the algorithmic contribution from dataset effects in Table 2.
- Discuss the scope and limitations of the approach→grasp→lift temporal structure for generalizing the method to other grasping scenarios (e.g., bin picking, grasping from shelves).

---

## Score and Decision

DemoGrasp presents a clean, well-motivated reformulation that substantially simplifies the hard exploration problem in universal dexterous grasping. The empirical results are comprehensive, the real-world deployment is convincing, and the method's simplicity makes it likely to be adopted and extended by the community. The main comparison (Table 2) could be more controlled, but this does not undermine the overall contribution. This is a strong accept.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>