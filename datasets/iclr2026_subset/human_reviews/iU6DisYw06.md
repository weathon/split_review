## Human Reviewer 1

### Summary
The paper tests whether LLMs “trust” their own explanations by intervening on tokens the model itself highlights as important, using three metrics—sufficiency (keep tokens), comprehensiveness (remove tokens), and counterfactuality (invert tokens). Experiments on IMDB and Steam with GPT-4o-mini, Gemma3-4B, Granite-8B, and DeepSeek-1.5B/14B show an “expected progression” for GPT-4o-mini/Gemma3/Granite, while DeepSeek models diverge (instability at 1.5B; over-sensitivity at 14B).

### Strengths
* Clear, testable notion of auto-consistency. The work operationalizes faithfulness via sufficiency, comprehensiveness, and counterfactual edits with simple, reproducible definitions. 

* Cross-model analysis. Compares closed- and open-source families across scales and reports coherent behavioral differences. 

* Transparent scope and limitations. The paper clearly states constraints and motivates output-based evaluation to avoid probability circularity.

### Weaknesses
* The paper’s core premise is circular: the same model flags “influential” tokens and then evaluates influence by measuring its own response after removing or altering those tokens. With no external ground truth, the model’s claims act as both hypothesis and test, creating a closed loop. Equations (3–5) bake in the assumption that the selected set (T) is meaningful; if the model is inconsistent, as the results suggest, then (T) is unstable, and the evaluation largely validates the model’s self-reports rather than true influence.

* The counterfactuality metric (Eq. 5) hinges on a weakly defined inversion (T \rightarrow \lnot T). WordNet antonyms don’t cover many domain terms, and the fallback, simply prepending “not”, often yields ungrammatical or unnatural text (just for a short e.g., “not pay to win” instead of “free to play”). The paper also provides no check that the edited sentences remain semantically valid, so measured effects may reflect broken language rather than true counterfactual meaning.

* Lacks ablation studies, small amount of testing data.

### Questions
Same as Weakness

### Soundness
1

### Presentation
2

### Contribution
1

### Rating
0

### Confidence
5

---

## Human Reviewer 2

### Summary
Tests whether LLMs’ own highlighted tokens actually drive their decisions by editing texts (keep/remove/invert those tokens) and measuring score shifts on review datasets; larger models look more self-consistent than smaller ones.

### Strengths
* Clear, behavior-level test of explanation faithfulness.

* Simple, reproducible edits with multiple aggregate metrics (Δ, variance, flip/reduction rates).

* Cross-model/scale comparison, not a single-model case study.

* Avoids probability calibration issues by using 1–10 scores.

### Weaknesses
* The 1–10 score isn’t calibrated across models; equal Δ may mean different things, and flip rates depend on arbitrary thresholds.

* Deleting/inverting tokens can break grammar or context, so effects may reflect text damage/distribution shift rather than causal importance.

* Models pick the “influential” tokens being tested, this self-selection risks tautology and lacks ground-truth attribution.

* Lacks a generalised view as the method has been tested on very short amount of data.

* I would suggest the authors to perform ablation studies to increase the faithfulness of the method

### Questions
Please regard the weakness as questions.

### Soundness
1

### Presentation
2

### Contribution
1

### Rating
0

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces a method aimed at faithful attribution of model decisions to input tokens, in a text classification setting.
Specifically, the proposed method is to
1. Prompt an LLM to perform text classification, i.e., to predict a label for a provided text
2. In addition, the prompt also asks the LLM to output a list of "influential terms" in the provided text, which "were important for the prediction".
3. Based on this list of terms, the original text is modified in three ways:
- giving only these terms as input, which is intended to evaluate if these terms are sufficient for the model prediction
- removing these terms from the original text, which is intended to evaluate if these terms are necessary for the model prediction
- replacing each of the terms with an antonym or a negation, which is intended to evaluate if these terms can "flip" the model prediction

The paper then formulates evaluation metrics for each of the three modifications and argues that together, these metrics quantify what the authors call "auto-consistency", i.e., whether the "influential terms" identified by LLMs actually influence model output in a consistent manner.
Experiments are conducted with five LLMs  on two sentiment analysis datasets (movie reviews and video game reviews).
The main conclusion of the experiments is that "auto-consistency in LLM explanations is not guaranteed by either model scale or openness".

### Strengths
The proposed method works with API access only, i.e., no model weights, activations, or output probabilities required.

### Weaknesses
The method lacks novelty and the paper is not substantive enough.

Lack of novelty: Attribution to specific tokens by modifying the input has been studied in prior work, e.g.: the "input reduction" proposed by Feng et al., 2018 (Pathologies of Neural Models Make Interpretations Difficult); or the erasure of tokens by DeYoung et al., 2020 (ERASER: A Benchmark to Evaluate Rationalized NLP Models). There is potential novelty in using LLMs to suggest input modifications, e.g., by identifying possible influential tokens, as proposed, but this idea is not explored in any meaningful depth. For example, how consistent are LLMs in predicting "influential tokens", e.g. under different prompts, with varying number of in-context examples, etc? How similar are the list of "influential tokens" across models? Can models predict "influential tokens" for other models or only for themselfves? etc)

Lack of substance: The paper only contributes a very small amount of experiments, whose results do not offer any insightful conclusions. There is a one-page discussion of the results, but the findings are vague. For example, what is the reader supposed to learn from the finding that on the one hand "the highlighted tokens are not enough to preserve the original prediction", but on the other hand that "the same tokens are indispensable" and that "This contradiction is compounded in counterfactuality"? Or that predictions are "collapsing under perturbations that other models absorb with greater stability."?  (quotes from lines 388-394).

Furthermore, the paper does not compare the proposed method to any existing attribution methods or other meaningful baselines.

### Questions
- The comprehensiveness and sufficiency metric were proposed by DeYoung et al., 2020. The paper defines these metrics in section 3.3 but fails to cite the source.

- line 275: "minimally plausible counterfactual intervention" should probably be "minimal, plausible counterfactual intervention", since "minimally plausible" means something like "smallest degree of plausibility"

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
3

---

## Human Reviewer 4

### Summary
This paper presents a study aimed at measuring the consistency of explanations produced by large language models (LLMs) when they highlight tokens deemed most influential for their decisions. The authors evaluate this consistency using three metrics: sufficiency, comprehensiveness, and counterfactuality, each defined in terms of a review score that is itself generated by the LLM.

The authors introduce an experimental framework grounded in the principle of auto-consistency: if a model identifies certain tokens as decisive, then isolating, removing, or semantically inverting these tokens should lead to systematic and interpretable changes in its predictions.

Experiments are conducted on two datasets, IMDB and Steam reviews, using five different LLMs. Results show that GPT-4o follows the expected progression across all metrics, Gemma3 and Granite8B maintain coherence under sufficiency but lose consistency under more demanding interventions, while DeepSeek variants exhibit structural deviations, either failing to preserve sufficiency or overreacting under comprehensiveness and counterfactuality. These findings indicate that the reliability of explanations varies significantly across LLM families and scales.

### Strengths
- The paper clearly demonstrates the substantial variability in the consistency of explanations produced by different LLMs when justifying their decisions, according to the authors’ proposed method for computing the evaluation metrics.

### Weaknesses
- The entire study relies on the authors’ specific definitions of sufficiency, comprehensiveness, and counterfactuality, yet this choice is not discussed or justified.
- The decision to have the LLM generate the review score via a prompt, alongside its explanations, raises concerns about the reliability of that score.
- The proposed framework appears highly tailored to binary classification tasks such as sentiment analysis; it is not clear whether it would generalize effectively to other types of tasks.
- The robustness of the method with respect to prompt formulation is not investigated.

### Questions
Discussion

Line 62: How do your proposed definitions of sufficiency, comprehensiveness, and counterfactuality serve as good proxies for those introduced by DeYoung et al. (2019)? A discussion clarifying this connection would strengthen the methodological grounding of your work.

Line 64: You state that the review score "reflects how favorably the text evaluates the target item." This definition is somewhat unclear. Is this concept limited to binary classification tasks such as sentiment analysis, as used in your experiments?

Line 233: Why did you choose the scalar range [1, 10] for the review score? Is it an integer value, it appears it is generated through the prompt. Since all your metrics depend on this score, can we genuinely trust its reliability?

Line 265: For counterfactuality, you appear to replace all selected tokens with their antonyms. However, counterfactual transformations can be defined at different levels of granularity. Why did you choose to apply the inversion to all tokens simultaneously?

You study the coherence of LLMs under token-level interventions, yet the mention of possible alternative approaches involving internal representations appears only late in the paper (line 289). Expanding this discussion earlier could provide valuable context and situate your framework within the broader landscape of explanation consistency analysis.

Minor Comments (do not affect the score)
Line 330: The logical symbol used for the indicator function seems uncommon. If it refers to a different function, it should be explicitly defined.

--------------------------

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
4