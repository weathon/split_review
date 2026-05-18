Now I have a thorough understanding of the paper. Let me compose the consolidated review.

## Summary

This paper investigates why intrinsic self-correction (LLMs improving their responses using only abstract task-level instructions, without external feedback) is effective. The authors empirically demonstrate that multi-round self-correction performance converges across six tasks (Figure 3), that model uncertainty and calibration error decrease and stabilize (Figure 4), and that latent concepts measured via probing converge to stable positive states (Figure 5). The paper proposes a mechanism: self-correction instructions activate positive latent concepts (e.g., non-toxicity), which reduce model uncertainty, leading to lower calibration error and ultimately converged performance. A mathematical formulation (Section 6.2) and a simulation task (Section 6.1) are provided to support this account.

## Strengths

1. **Comprehensive convergence demonstration across diverse tasks.** Section 3 reports multi-round self-correction experiments on six tasks spanning QA, generation, and vision-language modalities (social bias mitigation, jailbreak defense, VQA, commonsense generation, text detoxification, visual grounding). Figure 3 consistently shows performance improving and eventually stabilizing, establishing convergence as an empirically reproducible phenomenon.

2. **Convergent evidence linking uncertainty, calibration, and performance.** Section 4 measures semantic uncertainty and calibration error (ECE/RCE) across rounds. Figure 4 shows that both decrease and converge, and the round at which calibration error converges (e.g., round 6 for text detoxification) matches the round at which task performance plateaus (Figure 3). This temporal alignment supports the proposed link between uncertainty reduction and performance stabilization.

3. **Simulation task quantifying concept–uncertainty dependence.** Section 6.1 uses concept vector differences between round pairs to predict whether uncertainty increases or decreases, achieving 83.18% accuracy. This provides quantitative evidence that the measured concept representations carry information about uncertainty direction, consistent with Equation 1's formal relationship.

4. **Multi-modality validation.** The inclusion of vision-language tasks (visual grounding, VQA) using GPT-4 demonstrates that the convergence trend generalizes beyond pure text, broadening the scope of the findings.

## Weaknesses

### Major

1. **The theoretical derivation contradicts the empirical observations it is meant to explain.** Section 6.2 derives that `p(C_p|q_k) = (c_i c_y)^{t-1} p(C_p|q_0)` and explicitly states that "the effect of the positive concept activated by self-correction instructions **degrades** as the interaction round progresses," approaching `p(C_p|q_k) ≈ 0`. However, the empirical measurements in Figure 5 show the opposite: concept similarity either **increases** (QA tasks) or **stabilizes at a high level** (generation tasks). There is no regime in which the measured concept decays toward zero. The paper does not acknowledge, let alone resolve, this conflict. Because the theory is offered as the central explanatory mechanism for convergence ("This formulation explains why model uncertainty evolves towards convergence"), this contradiction undermines the claimed understanding of *why* convergence occurs. The derivation also relies on independence assumptions (`p(x,i,y)=p(x)p(i)p(y)`) that are implausible for language generation, where the output `y` depends heavily on the input `x` and instructions `i`.

2. **Causal claims outpace the correlational evidence.** Section 6.1 states its goal is to "empirically validate the strong causal relationship between concept and uncertainty" and concludes that the concept is "a strong driving force" for uncertainty change. Yet the simulation task only shows correlation: concept change between two randomly sampled rounds predicts uncertainty change. Because both concept similarity and uncertainty follow smooth temporal trends (Figures 4 and 5), any two rounds sampled without controlling for round index will produce correlated changes simply because both variables move in consistent temporal directions. The paper does not control for this confound (e.g., by conditioning on round-pair distance, or by showing that concept change adds predictive power beyond what round indices alone provide). Causal claims should be replaced with appropriately hedged language (dependence, association) unless stronger evidence (e.g., intervention experiments directly manipulating concepts) is provided.

### Minor

3. **"Irreversibility" is mischaracterized by the evidence.** The paper defines irreversibility as concepts "consistently maintain[ing] their positive nature" and cites the intervention experiment (injecting immoral instructions at rounds 2, 5, 8) as validation. However, this experiment shows the concept **immediately reverses** from positive to toxic when the instruction changes—the opposite of irreversibility. The intended meaning appears to be that the concept converges to a stable state aligned with the most recent instruction and does not spontaneously oscillate, but this is not what "irreversibility" standardly conveys. The term is misleading, and the experiment that should demonstrate irreversibility actually demonstrates reversibility in response to new instructions. The paper would benefit from a more precise term (e.g., "stability" or "instruction-responsiveness") and a clearer operational definition.

4. **Concept probe validity is not established.** The empirical measure — cosine similarity between hidden states and a probing vector trained for non-toxicity — is treated as a direct proxy for "the activated concept" (the probability `p(C_p|q_t)` used in the theory). However, the paper provides no validation that this representation-level similarity correlates with actual behavioral indicators of concept activation (e.g., the model's probability of producing toxic continuations, or classifier-based toxicity scores of generated text). Without this grounding, the central variable connecting instructions to uncertainty remains on uncertain footing. Additionally, the probing classifier's training procedure (dataset, label source, number of layers, training hyperparameters) is only referenced to prior work, making the measurement difficult to assess independently.

5. **Core analysis uses a single model.** All non-vision experiments use only zephyr-7b-sft-full. While the vision tasks use GPT-4, the mechanistic analysis (concept probing, uncertainty measurement, theory validation) rests entirely on one 7B model. Convergence patterns and concept dynamics could differ across model families and scales, limiting generality.

6. **Scope/title mismatch.** The paper's title and abstract imply general claims about LLM self-correction, but the experiments focus exclusively on morality-related tasks (bias, toxicity), and Section 7 explicitly excludes reasoning tasks. The conclusions should be tempered in the abstract and title to accurately reflect the moral-domain focus.

### Trivial

7. **Notational inconsistency in the derivation.** The expression for `t=1` in the derivation (Section 6.2) introduces `c_y` before any output has been generated in the first round, and the indexing scheme between the `t=0`, `t=1`, and general `t>1` cases is inconsistent in how `c_i` and `c_y` appear.

## Nice-to-Haves

- An ablation controlling for temporal trends in the simulation task (e.g., comparing concept-change prediction to a baseline that uses only round indices) would strengthen the dependence claim.
- An experiment directly manipulating the concept representation (e.g., activation steering) and observing downstream uncertainty effects would substantiate the causal direction.
- Adding a second model (e.g., Llama-3-8B) to the core analysis would improve generality.

## Removed Points

These points from the reviewer are removed or downgraded per the filtering rules:

- **"Convergence is not novel; prior work already shows this"** — The reviewer's claim that Madaan et al. (2023) and Huang et al. (2023a) already show convergence is overstated. Those works focus on self-refine in general and do not systematically demonstrate multi-round convergence across six diverse tasks or connect it to uncertainty/calibration dynamics. The reviewer's characterization undervalues the breadth of the empirical contribution. Removed as an unfair minimization.

- **"Exact prompts not given in main text" / "Probing classifier training procedure must be specified"** — These implementation details would be in the appendix (stripped by the parser). The paper cites Liu et al. (2024) for the probing approach, which is standard practice. Removed per the rule about missing appendix content.

- **"Number of rounds seems arbitrary"** — The paper follows Huang et al. (2023a) and the choice is clearly stated. This is a standard practice, not a weakness. Removed.

- **"Variance 0.00024 is suspiciously small"** — Low variance across 5 runs of the same logistic regression pipeline with fixed train/test split is normal, not suspicious. This is a misunderstanding of expected experimental variance. Removed.

- **Strength: "Theoretical derivation explaining convergence via concept activation"** — This strength conflicts with verified Weakness #1 (theory contradicts empirics) and is therefore dropped. The derivation as presented does not explain the observed data.

- **Strength: "Irreversibility and intervention experiments"** — This strength conflicts with verified Weakness #3 (irreversibility is mischaracterized) and is therefore dropped. The experiment does not support the property as claimed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation that the paper itself misses.

## Suggestions

1. **Resolve the theory–empirics contradiction.** Either reformulate the derivation to predict increasing or stable concept activation (matching Figure 5), or clearly scope the theory as modeling a different quantity (e.g., the *marginal contribution* of each round, not the absolute level of concept activation) and explicitly reconcile it with the probing measurements.

2. **Replace causal language with associational language** unless stronger causal evidence (e.g., concept interventions, temporal confound controls) is provided. The simulation task is correlational; the paper should say "dependence" or "association" rather than "driving force."

3. **Replace "irreversibility" with a more precise term** (e.g., "stability" or "convergence persistence") and clarify the property being demonstrated: the concept converges to a stable state consistent with the instruction's moral direction and does not spontaneously oscillate.

4. **Validate the concept probe** by showing that the probing similarity correlates with external behavioral measures (e.g., classifier-based toxicity scores of generated text) across rounds.

5. **Clarify in the title and abstract** that the analysis focuses on morality-related tasks, not all forms of self-correction.

## Score and Decision

The paper makes a useful empirical contribution by documenting the convergence of intrinsic self-correction across multiple tasks and linking it to uncertainty and calibration dynamics. However, the core explanatory mechanism — that concept activation drives uncertainty reduction — is undermined by a direct contradiction between the theoretical derivation and the empirical measurements, and by causal claims that outpace the correlational evidence. These issues prevent acceptance in the current form; a revision that removes or reformulates the theory, tempers the causal language, and strengthens the evidence could produce a worthwhile empirical characterization.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>