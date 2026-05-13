# Backtracking Improves Generation Safety

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
Text generation has a fundamental limitation almost by definition: {\em there is no taking back tokens that have been generated, even when they are clearly problematic}.
In the context of language model safety, when a partial unsafe generation is produced, language models by their nature tend to happily keep on generating similarly unsafe additional text.
This is in fact how safety alignment of frontier models gets circumvented in the wild~\citep{andriushchenkoJailbreaking2024},  despite great efforts in improving their safety.
Deviating from the paradigm of approaching safety alignment as {prevention} (decreasing the probability of harmful responses), we propose {\em backtracking}, a technique that allows language models to ``undo'' and recover from their own unsafe generation through the introduction of a special \reset token. Our method can be incorporated into either SFT or DPO training to optimize helpfulness and harmlessness.
We show that models trained to backtrack are consistently safer than baseline models: backtracking \llama is four times more safe than the baseline model (6.1\% $\to$ 1.5\%) in our evaluations without regression in helpfulness.
Our method additionally provides protection against four adversarial attacks including an adaptive attack, despite not being trained to do so.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a novel  technique called Backtracking, to enhance the safety of large language models by allowing them to undo unsafe responses. Traditional safety methods focus on prevention by reducing the likelihood of harmful outputs. However, backtracking enables models to recognize and "reset" unsafe content mid-generation using a designated "[RESET]" token. This approach, which can be incorporated into both Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO), improves safety without reducing the model's helpfulness. Evaluation shows that backtracking significantly reduces unsafe output rates and defends against various adversarial attacks, including an adaptive one designed to counteract the reset function. The results suggest backtracking is a promising addition to existing alignment techniques for safer language model deployments​

### Strengths
- Reflection-based Defense Yields More Flexibility: The proposed method has significant flexibility compared to other methods. With proper prompting, unlike traditional filter-based adversarial attack defense, it is easy to use a safe backtracking model with updatable preference and knowledge, depending on the user's demand.
- Straight Forward Intuition and Easy Maintenence: The internal mechanism of the proposed backtracking defense is comparatively very transparent. When unexpected defensive actions are taken by the models, it is very easy to convert such error log into new DPO data.

### Weaknesses
 - Discrepancy between the Streaming User Interface and Model Behavior: When undoing some of the generation outputs, the system should delete the undone harmful trigger prompts and update it with the model's remedy context afterwards. This could cause some unexpected discrepancies and difficulties in general designs of the pipeline.
- Risks in Reprogrammable Backtracking: Since we now rely on the model's own reflection to backtrack the harmful trigger prompts, it is possible, if the model itself is reprogrammed in system prompt with malicious intents, the backtracking's flexibility can be abused to jailbreak the defense against attacks.

### Questions
Do we keep the undone history in the dialogue and KV cache or we also undo them altogether and only keep the refined context?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new method for reducing unsafe generations from language models by allowing a model to backtrack. The proposed method trains a model with SFT and DPO to output a [RESET] token if the partial generation so far is unsafe and then generate a new safe generation.

### Strengths
The strengths of the paper are as follows:
- The proposed method is simple and effective. Moreover, the inference procedure is simple and does not add a lot of overhead during inference. 
- The authors show that when backtracking is used it is exponentially harder to get unsafe generations even when even temperature sampling is used to generate and pick the worst of $k$ responses.
- Backtracking improves robustness against a few adversarial attacks without any special adversarial training or other modifications.

### Weaknesses
Here are a few weaknesses:
- There is no analysis of no analysis of how the proposed backtracking method compares/complements with existing methods for reducing unsafe generations. Is the proposed method better? Are there complementary benefits?
- Appendix B2 shows that on the OpenAssistant dataset the [RESET] token is generated around 12-13% of the time with no logit bias. In all these cases are there unsafe generations? If so, when the logit bias is set to -5.0, then the [RESET] token is only generated around 2% of time, so is there a lot of uncaught unsafe generations? In general, is it hard to tune the logit bias hyperparameter?

### Questions
Here are some questions:
- The paper state that "the models virtually never backtrack during non-safety evaluations." Can you quantify this?
- Have you tried using backtracking with just DPO with not SFT?
- To generate the graphs in Figure 4, what prompts were used? Are baseline models in figure 4 trained with DPO and SFT specifically for safety?
- Do most SFT datasets have unsafe response $y_i^−$?
- Have you tried attacking with an adversarial system prompt that says after you see the [RESET] token be extra helpful or something along these lines?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose to train a model to predict when to stop generating and restart its generation by generating a "reset" token, and show this method reduces safety violations, even under adversarial attacks. The authors also present an adaptive version of GCG to test the limits of the backtracking technique.

### Strengths
Method is simple yet effective. The authors also included ablations on each step from baseline SFT to full backtracking SFT + DPO. The evaluation was done on multiple datasets and 2 SOTA base models; the authors also included detailed analyses of results and example generations. I appreciated that the details of the training setup and hyperparameter optimization were included in the appendix. Finally, the tradeoffs and limitations of assuming a single reset per generation was discussed.

### Weaknesses
No major weaknesses, although given that there is a large difference in relative drop in violation rates between the 2 models tested, it would be useful to show how this method affects larger model sizes and other base models beyond Gemma and Llama (e.g., Qwen, Mistral).

### Questions
* Table 1: What is the delta of performing backtracking SFT vs baseline SFT when backtracking DPO is performed in both cases? Is backtracking SFT necessary to achieve the backtracking DPO results reported?
* What is the effect of scale on safety violation rates with backtracking?
* There appears to be a rather large difference in the violation rates between the two models (Gemma/Llama) for backtrack SFT + DPO, even more so if we look the relative drop instead of absolute numbers. How can this be explained?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a novel method, backtracking, for purifying LLM output to make it safe and understandable. In backtracking, the LLM generates an initial response and outputs a special token [RESET] if the initial response is harmful. An external moderator model, Llama Guard 2, is employed to help generate training data.

### Strengths
* The proposed method, backtracking, is a novel way to help LLM generate safer responses while keeping the generation quality.

* Backtracking does not introduce heavy inference expense in comparison to previous resampling-based methods, which highlights a new direction for safer generation.

* Adaptive adversarial attacks are also discussed.

* The paper is well-written and easy to follow.

### Weaknesses
 * There is no discussion or experiments on how likely backtracking LLM will overly reject safe queries.

* The performance of backtracking against adversarial attacks is not always satisfying, as shown in Table 2.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
