## Summary
This paper introduces the Text-Guided Decision Transformer (TG-DT), an offline meta-reinforcement learning framework that enables zero-shot task generalization by replacing task demonstrations or IDs with natural language descriptions. The core of the approach is a dual-alignment mechanism involving Text-Behavior Contrastive (TBC) learning for cross-task distinction and Text-Behavior Matching (TBM) with hard negative mining to distinguish behavioral quality within tasks. Experimental results on MuJoCo and Meta-World benchmarks show that TG-DT achieves performance comparable to or better than state-of-the-art meta-RL baselines, such as Prompt-DT and Meta-DT, even though it does not require test-time environment interaction or demonstrations.

## Strengths
- **Strong Zero-Shot Generalization:** The model matches or exceeds the performance of state-of-the-art methods like Prompt-DT and Meta-DT in zero-shot settings across benchmarks including Cheetah-dir, Cheetah-vel, and ML10 (Table 1), notably without needing the task-specific demonstrations required by many baselines.
- **Novel Alignment Mechanism for Sequential Decision-Making:** The combination of TBC and TBM objectives effectively bridges the semantic gap between language and temporally extended trajectory data. The use of hard negative mining in TBM specifically addresses the unique offline RL challenge of distinguishing quality variations within the same task (Section 3.2).
- **Effective Representation Grounding:** t-SNE visualizations (Figure 4) demonstrate that the model learns a structured latent space where continuous task parameters (like target velocity) are mapped to smooth manifolds, suggesting genuine semantic grounding rather than simple categorical memorization.
- **Robustness to Offline Data Quality:** TG-DT maintains competitive performance across Medium, Mixed, and Expert datasets (Table 4), showing resilience to noisy or suboptimal demonstrations in the training set.

## Weaknesses

### Major
- **Reliance on Oracle-like Metadata in Prompts:** The "zero-shot" prompt template includes fields for "expected return" and "expected episode length" (Section 3.1). Since Decision Transformers are highly sensitive to Return-to-Go (RTG) conditioning, providing "approximate statistics inferred from the training distribution" at test time may grant the model a significant information advantage akin to an oracle signal. There is no sensitivity analysis showing how performance degrades when these estimated values are inaccurate. Without this, it is unclear if the results stem from semantic task understanding or simply from the precise numerical priors embedded in the prompt.
- **Ambiguity in Fairness of Zero-Shot Comparisons:** TG-DT is compared against baselines that must *infer* task parameters (like target returns) from data or interaction. By manually providing these parameters in the text prompt, the comparison may be asymmetric in TG-DT's favor. The paper lacks a baseline showing performance when these prompt values are set to a non-informative flat average across all unseen tasks.

### Minor
- **Lack of Linguistic Robustness Evaluation:** The reliance on a fixed prompt template ("This is the [task_name]...") suggests the model might be overfitting to specific keywords. While the authors use BLIP initialization, they do not evaluate whether the model is robust to natural language variations such as paraphrasing or the use of synonyms (e.g., using "move quickly" instead of "target velocity 3.0").
- **Missing "Naive" DT-Text Baseline:** While the paper ablates TBC and TBM, it does not compare against a simpler "Naive" DT baseline where text embeddings are concatenated to the state-action sequence without the specialized dual-alignment losses. This comparison would better isolate the specific value added by the TBC/TBM architecture.

### Trivial
- **Complexity-Related Slower Convergence:** The paper notes slower convergence on Meta-World tasks compared to simpler benchmarks (Section 5.2/Figure 3), which is a minor trade-off for the learned robustness.

## Nice-to-Haves
- A sensitivity analysis plotting performance as the "expected return" citing in the test prompt is varied (e.g., from 50% to 150% of the true target).
- Evaluation of cross-task compositionality (e.g., assessing "lift hammer" performance if "lift" and "hammer" were only encountered separately during training).

## Removed Points
- Reproducibility concerns about the "approximate statistics" calculation logic being in the appendix were removed as per instructions regarding the presence of appendix materials.
- Discussion about the availability of external BLIP weights was removed as per hard rules.
- Suggestions requesting more models or different benchmarks were removed because the current evaluation on standard MuJoCo and Meta-World task suites is sufficient for the field.

## Novel Insights
TG-DT successfully demonstrates that dual-objective alignment (contrastive + matching), traditionally used in vision-language tasks, can be adapted to sequential decision-making. A key insight is the necessity of the matching objective with hard negative mining to handle the quality variance inherent in RL trajectories, which contrasts with standard contrastive learning that often only distinguishes task identity.

## Suggestions
- Conduct a sensitivity study on the "expected return" value in the test prompt to confirm the model's robustness to inaccurate priors.
- Evaluate performance on paraphrased text instructions to verify that the model has acquired true semantic grounding rather than keyword matching.
- Include a baseline that uses simple text concatenation without specialized alignment losses to quantify the architectural contribution more clearly.

## Calibration and Scoring
### Round 1 — Bracketing
Initial anchors were identified via `calibration_search`:
- **Strong (Score 8.0):** `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/9pW2J49flQ.md` (DeepLTL: Learning to Efficiently Satisfy Complex LTL Instructions). This paper has highly rigorous proof-of-concept and complex logic grounding.
- **Middle (Score 6.25):** `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/AY6aM13gGF.md` (LaMo: Unleashing the Power of Pre-trained Language Models for Offline RL). This is a topically similar paper using LLMs for DT initialization.
- **Middle-Low (Score 5.0):** `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/g6iiIUvhko.md` (Zero-Shot Task-Level Adaptation via Coarse-to-Fine...). This paper also addresses zero-shot task adaptation but was rejected for poor representation learning.

**Initial Bracket:** Between 5.5 and 7.0. The paper is stronger than the rejected representation paper (5.0) due to its dual-alignment mechanism and strong Meta-World results, but the oracle-leakage concern in the prompts is a significant major weakness compared to top-tier papers.

### Round 2 — Narrowing
- **Anchor 1 (Score 6.25):** `AY6aM13gGF.md`. TG-DT is comparable in its use of pre-trained knowledge but offers a more novel dual-alignment mechanism specifically for trajectory-text grounding. However, TG-DT's prompt sensitivity is more pronounced.
- **Anchor 2 (Score 6.5):** `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/phAlw3JPms.md` (Robust Sequence Modeling for Offline RL). This paper shows strong empirical robustness across shifts.
- **Anchor 3 (Score 5.75):** `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/FhbZ1PQCaG.md` (Decision Transformers with Internal Memory).

**Narrowed Score:** The paper's contribution to text-behavior alignment for DT is technically sound and empirically strong on Meta-World, placing it slightly above the 6.0 threshold. The reliance on templated "expected return" metadata in the prompt is the main factor preventing a score of 7.0 or higher. The current work is a solid contribution to the community.

**Final Score Calculation:** Better than 5.75 (more novel alignment), comparable to 6.25 (LaMo), but held back from 7.0 by prompt sensitivity.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>