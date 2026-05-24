Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

This paper proposes CONFST, a method for steering LLM outputs during inference by constructing a "confident direction" from user history. The core idea is: (1) train a logistic regression classifier on token-level activations from user history data, (2) select only those activations whose classifier confidence exceeds a threshold β, (3) average the selected activations to form a steering vector, and (4) add this vector to the model's residual stream at a chosen layer. The paper also presents a Bayesian theoretical framework (Section 3) that characterizes effective steering directions as those that concentrate posterior probability on the ground-truth latent preference. Experiments on GPT-2 XL, Mistral, and Gemma-it cover topic steering (4-class AgNews, multi-class Emotion) and style steering (conciseness, helpfulness, detoxification, indirect emotion expression).

## Strengths

- **Empirical demonstration of multi-class (beyond binary) steering (Figures 4, 5).** The paper shows that CONFST can steer model output toward one specific class among 4 (AgNews) or multiple (Emotion) candidates. This directly addresses the limitation the paper identifies in prior steering work, which is largely limited to binary directions (truthful/untruthful, harmless/harmful). The experiments span two model families (GPT-2 XL, Mistral) and show that the method improves over naive mean steering across multiple β thresholds.

- **The confidence-thresholding idea is simple and principled.** The use of logistic regression confidence to filter noisy activations before averaging into a steering vector is a clean heuristic. The paper openly reports (Remark 4) that higher β does not always improve performance — an honest observation that reveals an interesting trade-off between activation selectivity and sample size. This nuance goes beyond cherry-picking best results.

- **Evaluation across multiple model sizes and diverse style tasks.** Experiments cover GPT-2 XL (1.5B), Mistral (7B), and Gemma-it (9B) on conciseness, helpfulness, detoxification, and emotion expression. The combined topic+style experiment (Fig. 8) demonstrates that steering vectors can be additively combined for multi-attribute control.

- **Complete, reproducible algorithm specification (Algorithm 1, Steps 1–5).** The method is described with enough detail that the core procedure (train classifier → threshold on confidence → average → add to activations) can be reimplemented.

## Weaknesses

### Fatal

None.

### Major

- **No comparison against state-of-the-art steering methods.** The paper's Table 1 and Related Work section (lines 34–38) cite several recent steering methods (Li et al., 2024b; Rimsky et al., 2023; Wang et al., 2024a; Adila et al., 2024a; Lee et al., 2024) and explicitly positions CONFST against them (e.g., claiming no need to iterate over all layers/heads). However, **none of these methods are evaluated as baselines.** The paper only compares against Massive Mean Shift, Act Addition, and In-context learning — and the first two are barely described beyond being named in figure captions (lines 300, 304). Without a direct comparison to at least one method that does iterate over layers/heads (a key claimed disadvantage of prior work), the reader cannot assess whether CONFST's simplicity comes at a performance cost or offers a genuine advantage. This is the most consequential gap in the evaluation.

- **The theoretical framework (Section 3) is disconnected from the method and empirically unvalidated.** The Bayesian analysis defines what a "good" steering direction should look like (high P(θ*|f(T(A))) — but this is essentially a formal restatement of the goal rather than a result that guides construction. The method then uses logistic regression confidence as a proxy for this posterior without any empirical bridge between the two. Notably, the paper's own finding (Remark 4) that higher confidence thresholds can *worsen* steering performance is not reconciled with the theory, which would predict the opposite. There are no experiments showing that high-confidence activations actually correspond to better steering directions, or that the KL bounds from Claim 1 hold in practice. The theory functions as motivational framing rather than a testable, falsifiable contribution.

- **Baselines are insufficiently described and may be weakly configured.** The three baselines (Massive Mean Shift, Act Addition, In-context learning) are named but not described methodologically. The paper states that after "testing several different α values for mean steering" the authors "observed similar success rates across the board" and used the same α as CONFST (line 295). This is not a proper hyperparameter search; it conflates the baseline's best possible performance with a casual sweep. In-context learning configuration (number of shots, example selection, format) is not reported at all, making the comparison uninformative.

### Minor

- **Claim about avoiding layer selection is overstated.** The abstract says "there is no need to determine which layer the steering vector should be added to," but the method takes layer ℓ as an input hyperparameter, and different layers are used for different models (ℓ=1 for Mistral, ℓ=0 for Gemma — line 297). The true advantage is that CONFST does not *iterate* over all layers/heads, not that layer choice is irrelevant. The conclusion (line 332) states this more accurately ("without selecting among all the layers"). The abstract should be corrected to match.

- **Abstract's "simultaneously" phrasing is ambiguous.** The abstract claims "multiple (i.e. more than two) users' preferences can be aligned simultaneously." The intended meaning (clarified in the conclusion: "steering towards one preference among multiple preferences") is that the method handles preference sets larger than 2 — which is demonstrated. But "simultaneously" could be read as satisfying multiple preferences in a single output, which is only tested in the combined topic+style experiment (Fig. 8) with two additively combined vectors. This framing invites misinterpretation.

- **No statistical rigor.** None of the results include confidence intervals, error bars, or significance tests. Given the modest sample sizes (200 generations per direction in topic shift), variance is non-negligible. This weakens the reliability of reported improvements.

- **LLM-as-evaluator is underspecified.** Several experiments rely on "LLM auto-evaluation" (lines 309, 315, 317) without naming which LLM was used, what prompt was provided to the evaluator, or whether any calibration or human agreement check was performed. The emotion support experiment (line 309) sets baseline helpfulness scores to 4.0 without justification.

### Trivial

- The paper contains several minor typographical issues and garbled characters typical of PDF extraction artifacts. No substantive concerns.

## Nice-to-Haves

- Ablation study on the choice of layer ℓ. Since the method uses different layers for different models, understanding sensitivity to this choice would strengthen confidence in the method's robustness.
- Reporting the weights used in the combined topic+style steering (Fig. 8).
- A sanity check that CONFST outperforms random selection of the same number of activations (to isolate the effect of classifier confidence from the effect of using fewer activations).

## Removed Points

*These points were flagged by reviewers but are removed as per the filtering rules.*

1. **"No experiment where model must distinguish among four user preferences" (Harsh Critic).** The AgNews experiment has 4 classes. The paper does demonstrate steering toward one of four topic classes. The criticism is factually incorrect. **Removed.**

2. **"The combined topic+style experiment adds steering vectors as weighted sum — this is not handling multiple preferences."** The paper's core claim about handling >2 preferences is about the preference set size (4-class steering), not about multi-objective combination. The combined experiment is presented as an additional demonstration of additivity. The criticism conflates two different claims. **Removed** as a misunderstanding of the paper's main claim.

3. **In-context learning "requires demonstrations" criticism.** The critic says ICL uses explicit demonstrations. This is true of all ICL methods and is not a weakness of the comparison — it is a known property of the baseline. The paper acknowledges this as a point of contrast. **Removed.**

4. **Criticisms asserting methods mentioned in the paper do not exist or cannot be independently verified.** The Harsh Critic says "neither Massive Mean Shift nor the specific Act Addition implementation is described with enough detail to assess fair configuration" — these are standard methods cited in the paper's references that exist in the literature. **Removed** per Hard Rules about questioning existence of cited entities.

5. **"The theory section could be shortened or removed without harming the contribution"** — This is a judgment about editorial decisions, not a verifiable weakness. The substance (theory-method disconnect) is retained in Major Weaknesses above; the opinion about removing it is dropped.

6. **"More preferences directions could be aligned at the same time" as a limitation** — The paper's conclusion section lists this as a future direction, not a weakness. The Harsh Critic calls this contradictory, but it is simply an honest statement of scope. **Removed.**

7. **Generic strength about "addressing an important problem" and "clear writing"** from Strength Finder — These are generic/superficial. **Removed.**

## Novel Insights

None beyond the paper's own contributions. The reviewer inputs do not surface any observation about the paper that the paper itself does not already articulate. The strengths and weaknesses identified are all grounded in the paper's own framing and experimental design.

## Suggestions

1. **Add at least one SOTA steering baseline** — compare CONFST to the layer-iterating method of Li et al. (2024b) or the probing-based method of Adila et al. (2024a) on a shared task (e.g., truthfulness or topic steering). Report both performance and runtime. This is essential to substantiate the claimed simplicity advantage.

2. **Validate the theory empirically.** Show that classifier confidence correlates with downstream steering success (e.g., bin activations by confidence percentile and measure resulting steering quality). This would close the gap between Section 3 and Section 4.

3. **Provide proper hyperparameter selection for baselines** — conduct a systematic sweep for each baseline and report best results, not single shared-α comparisons.

4. **Add confidence intervals or error bars** to all quantitative results using at least 3 random seeds or bootstrap resampling.

5. **Specify the LLM evaluator** — name the model, the evaluation prompt template, and report agreement with human judgments for at least one task (e.g., helpfulness scoring).

6. **Correct the abstract** to say "without iterating over all layers/heads" rather than "no need to determine which layer" to match the actual method.

## Score and Decision

**Originality:** Moderate. The confidence-thresholding idea is a new application to model steering, though the theoretical framework largely formalizes existing intuitions.

**Importance of research question:** High. Practical, multi-direction model steering without costly search is a real bottleneck in LLM personalization.

**Claims supported:** Partially. The core claim (CONFST works for >2 preference categories) is supported. The claim about simplicity is supported in terms of no layer iteration, but the "no need to determine layer" wording is overstated. The theoretical contribution is not validated.

**Soundness of experiments:** Moderate. The paper experiments across multiple models and tasks, but the baseline set is too limited, statistical rigor is absent, and the LLM evaluator is underspecified.

**Clarity of writing:** Adequate. The key algorithmic steps are clear. The theoretical section is formal but its connection to the method could be clearer.

**Value to community:** Moderate. CONFST is a simple and plausible method that practitioners could adopt. However, without validation against competitive baselines, its practical value versus alternatives is unknown.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>