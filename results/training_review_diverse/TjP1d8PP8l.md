Now I have enough information. Let me compose the final consolidated review.

## Summary

This paper proposes DGAP (Discriminator-Guided Action Optimization), a framework that combines a small number of expert demonstrations with LLM planning. A discriminator (RoBERTa regressor) is trained on augmented demonstration data to assign step-level scores (0–10) measuring alignment between LLM-generated actions and optimal choices. LLMs are then prompted with historical action-score pairs to generate actions maximizing these scores, with a threshold-based resampling fallback. The paper provides a theoretical connection to critic-regularized RL and evaluates on ScienceWorld (30 tasks, GPT-4 and Llama3-70B) and VirtualHome, showing consistent improvements over strong baselines including SwiftSage, Reflexion, and ProgPrompt.

## Strengths

- **Novel combination of LLM commonsense reasoning with step-wise discriminator guidance from few demonstrations.** The paper identifies a genuine limitation — pure LLM planners lack domain grounding, while pure demonstration methods fail OOD — and proposes a concrete synthesis: train a regressor on augmented expert data to produce step-level scores, then prompt the LLM to maximize those scores. This is a clean and practical idea (Sec. 1, Fig. 1, Sec. 3.1–3.2).

- **Consistent empirical superiority across two challenging benchmarks and two LLMs.** In ScienceWorld, DGAP outperforms SwiftSage (prior SOTA), Reflexion, TDT, and SFT on most of 30 task types, using both GPT-4 and Llama3-70B. In VirtualHome, DGAP achieves higher success rates (SR) and execution rates (EXEC) than ProgPrompt, Inner Monologue, and Tree Planner across In-Distribution, NovelTasks, and NovelScenes settings, with lower standard deviation indicating greater robustness. (Sec. 5.1, Table 1; Sec. 5.2, Table 2)

- **Careful data augmentation strategy for discriminator training from limited demonstrations.** The three-component dataset construction (expert actions scored 10, random negatives scored 0, offline LM-generated actions scored via cosine similarity) is thoughtful and addresses the fundamental challenge of training a regressor from very few expert trajectories (10–30 per task). (Sec. 3.1, Fig. 3, Eq. 2)

- **Practical compatibility with API-based LLMs without parameter tuning.** DGAP operates entirely through prompting with action-score pairs, requiring no gradient updates or open-weight models. This is a genuine practical advantage over RLHF-style methods and is explicitly discussed (Sec. 3.3, RLHF connection paragraph).

## Weaknesses

### Fatal
None.

### Major

- **Theory–practice mismatch undermines claimed provable guarantees.** Lemma 3.1 and Corollary 3.2 derive a policy improvement guarantee for optimizing *cumulative* return \(R_\phi(s,a) = \sum_{i=t}^{T-1} r_\phi(s_i,a_i)\) under a KL constraint. The actual DGAP algorithm uses *single-step* discriminator scores with a threshold-based resampling mechanism — not cumulative returns. The paper acknowledges this gap ("slightly different") but dismisses it with an unsubstantiated claim: "a successful multi-step plan requires single-step optimality in each planning step" (line 115). This is not generally true; many embodied tasks require coordination across steps (e.g., heating tin before measuring its temperature). Moreover, the practical resampling loop (reject actions below threshold τ) produces a censored distribution, not the exponential tilting \(\pi^{\text{llm}}(a|s)\exp(R_\phi/\beta)\) derived in the theory. There is no explicit KL control in the implemented algorithm. The paper's claim that DGAP is "provable to achieve a stronger policy than the LLM planner" (line 19, 21) is therefore overstated for the actual algorithm. The theoretical connection is a useful qualitative framing, not a formal guarantee for the deployed method. This does **not** invalidate the empirical results, but the paper should either (a) adjust the algorithm to match the theory (e.g., prompt with cumulative scores), (b) reframe the theory as an intuitive connection rather than a provable guarantee, or (c) provide an honest analysis of the rejection-sampling properties of the actual algorithm.

- **The discriminator — the central component — is never validated on its own.** The discriminator \(\mathcal{D}_\phi\) is the sole source of step-level guidance, yet the paper reports no accuracy, correlation with actual action quality, or robustness to out-of-distribution state-action pairs. Key assumptions in its training data remain untested: (a) treating the LM's first candidate as score 10 in unseen scenarios (line 65) could introduce systematic bias, (b) the sentence embedding model used for cosine similarity scoring is not named, and (c) the mapping from cosine similarity to scores relies on an unverified premise about the first candidate's quality. Without this validation, the overall task success could arise from the resampling mechanism alone (the LLM will eventually generate a decent action if forced to re-sample enough times) rather than from the discriminator providing meaningful signal. The paper also does not report how often the threshold is triggered, which would give insight into whether the discriminator provides useful signal or merely rejects obviously bad actions. **This is the most consequential weakness** because the core claim is that learned step-level scores guide planning — if the scores are unreliable, the contribution narrative weakens substantially.

### Minor

- **Imprecise reporting of demonstration counts.** The paper states "around half number of demonstrations as ToT, SFT, and SwiftSage, with 10 to 30 trajectories per task" (line 169). "Around half" is vague, and the 10–30 range is wide. Moreover, DGAP's *total* data footprint includes far more than expert trajectories due to augmentation (offline LM-generated pairs), so the claim of using fewer demonstrations is nuanced. Exact counts and a clear apples-to-apples comparison of data volume are needed for reproducibility.

- **Key implementation details not specified.** The pre-trained sentence embedding model used for semantic similarity scoring in data augmentation (line 65) is not named. The fine-tuned LM used to generate "offline data" is not specified. These details are important for others to replicate the data construction pipeline.

- **Missing statistical reporting for ScienceWorld results.** VirtualHome results include standard deviations (mentioned as "minimal standard deviation" in line 186), but ScienceWorld results (Table 1) are reported without confidence intervals, error bars, or significance tests. Given the per-task nature of the evaluation and potentially small differences on some tasks, this makes it difficult to assess which gains are robust.

- **Threshold selection not justified.** The thresholds (5 for ScienceWorld, 6 for VirtualHome) are said to be "based on their respective training data distributions" (line 99), but no analysis or sensitivity study is provided. Performance may depend significantly on this parameter, and its selection process is opaque.

- **VLM experiments in VirtualHome are presented superficially.** The VLM variant (InternVL2-8B) changes the observation pipeline and action step length, making it a different method. It is compared only descriptively without a full baseline comparison (Sec. 5.2, paragraph starting line 184). While not central to the paper's contribution, this section feels incomplete and could mislead readers about the role of perception in the framework.

### Trivial

- Typographical issues: "around around" (line 169), "scenerios" → "scenarios" (line 195), "diffculty" → "difficulty" (line 99), "emboied" → "embodied" (line 92).
- "exact" → "extract" (line 61).

## Nice-to-Haves

- Ablation of the threshold τ (sensitivity analysis showing how performance changes with different thresholds).
- Ablation of the discriminator components (expert data only; expert + random; full augmentation) to quantify each component's contribution.
- Analysis of resampling frequency (average number of replanning calls per step) to quantify efficiency and discriminator behavior.
- Analysis of discriminator failure modes (false positives/negatives — high score on a bad action or low score on a good action).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength: "Theoretical connection to critic-regularized RL with provable policy improvement"** — This strength is in direct tension with a verified weakness (theory-practice mismatch). The theoretical derivation applies to cumulative-return optimization, not the single-step thresholding algorithm actually used. The claimed "provable" guarantee does not hold for the deployed method, so this cannot be listed as a strength without qualification.

- **Criticism about missing discriminator training hyperparameters (learning rate, batch size, epochs, optimizer)** — Per the instructions, nitpicks about undisclosed hyperparameters for standard model training (RoBERTa with a linear head) are removed as they are typically provided in supplementary materials or code, and requesting them is a trivially fixable detail.

- **Criticism about prompt templates being incomplete** — Partial prompt snippets are standard in papers with page limits; the full prompt is a detail typically provided in supplementary materials or the appendix (which the parser strips).

- **Criticism about missing appendix, proofs, or references** — The parser removes these sections; they exist in the original submission.

- **Criticism that VLM experiments "detract from the core narrative"** — While the VLM experiments are supplementary and somewhat disconnected, they do not harm the paper's main contribution; they are an extension the authors chose to include.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an important meta-point: there is a recurring pattern in LLM-agent papers where a theoretical RL-style derivation (KL-constrained optimization, exponential tilting) is presented alongside a prompting-based algorithm that does not actually implement the derived objective. This mismatch is worth highlighting because it points to a broader question: when an LLM is prompted with scores and asked to "maximize high-score actions," what optimization problem is it actually solving? The paper's empirical success suggests the approach works, but the disconnect between theory and practice means the *why* remains unclear. A more grounded analysis — treating the LLM's score-guided resampling as a form of rejection sampling with learned acceptance probabilities, and analyzing its bias-variance properties — would be a genuinely useful contribution that goes beyond what this paper or the reviews individually provide.

## Suggestions

1. **Validate the discriminator.** Report its predictive accuracy, correlation with ground-truth action quality (on a held-out set), and robustness to OOD inputs. This is the single most impactful improvement the paper could make.

2. **Align theory with practice or reframe honestly.** Either modify the algorithm to use cumulative scores (making the proof directly applicable) or drop the "provable" language and reframe the theoretical section as a qualitative connection/analogy. If the rejection-sampling nature of the algorithm is analyzed explicitly (e.g., bound on the probability of accepting a low-quality action), that would be a more honest and still useful theoretical contribution.

3. **Provide exact demonstration counts** and clarify the total data footprint (expert + augmented) to allow fair comparison with baselines.

4. **Name the sentence embedding model** and the fine-tuned LM used for offline data generation.

5. **Add error bars or confidence intervals** to the ScienceWorld results, even if based on multiple seeds of the LLM calls or bootstrapping.

6. **Report resampling frequency** (average number of replanning calls per step) to help readers understand the discriminator's behavior and the method's efficiency.

## Score and Decision

The paper addresses a genuine problem (grounding LLM planners with minimal demonstrations), proposes a clean and practical method (step-level scores from a learned discriminator), and demonstrates consistent empirical gains on two challenging benchmarks with two different LLMs. These are real contributions. However, two major weaknesses — the overclaimed theoretical guarantees that do not match the actual algorithm, and the complete lack of validation of the discriminator itself — mean that the paper's core claims are not fully supported by the evidence presented. The experiments show that *something* in the pipeline works, but it is unclear whether the discriminator's scores are the reason, or whether the resampling mechanism alone drives the gains. These issues are addressable in revision but are too significant to ignore.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>