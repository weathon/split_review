## Human Reviewer 1

### Summary
The paper revisits direct prompting of off-the-shelf LLMs to detect and remove prompt injections, arguing that past negative results no longer hold for modern models. With a carefully designed system prompt, PromptArmor using GPT-4o reports very low error rates on different benchmarks. They conclude that prompting a strong off-the-shelf LLM should be considered a standard baseline for prompt-injection defense.

### Strengths
- The proposed method achieves good performance compared with SOTA baselines.

- The writing is clean and relatively easy to follow.

### Weaknesses
- In the abstract and introduction, the paper emphasizes that the reasoning ability of the guardrail LLM is essential for defense performance (e.g., Line 74: “prompting an off-the-shelf LLM with strong reasoning capabilities should be reconsidered as an important and strong baseline for evaluating future defenses against prompt injection attacks”). However, Figure 3 shows that enabling reasoning does not consistently improve detection or task utility, and in many cases even worsens performance. The support for this claim needs further clarification.

- Line 189 claims “strong generalization capabilities,” but no experimental evidence is provided.

- Line 198 highlights computational efficiency as a design advantage, yet no experiments compare computational cost with baselines.

- Table 2 contains many N/A entries for baseline methods regarding FPR and FNR; the reason for this omission should be elaborated.

- Line 362 states that GPT-3.5’s performance improves when adding a definition, but the reported FPR and UA are actually worse. Please clarify what conclusion this experiment is intended to support.

- In Table 4 (adaptive attack setting), including the same baselines as in Table 2 would strengthen the comparison.

- It is unclear how PromptArmor impacts performance on benign inputs.

- No statistical uncertainty is reported across results.

- Minor: The specific version of the GPT models used (API version) is missing.

### Questions
Please see **Weaknesses** for my questions.

### Soundness
1

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper proposes PromptArmor, a simple but effective defense against prompt injection attacks. PromptArmor works by getting an LLM to (1) identify if input data contains a prompt injection attack, and (2) output the text corresponding to the prompt injection so that it can be removed. 

The authors test PromptArmor on a number of commonly used benchmarks in this area (AgentDojo, Open Prompt Injection, and TensorTrust) and get favorable results. Overall, they find that the more performant the model used for PromptArmor, the better the performance. Using Qwen models, they also demonstrate that reasoning models are better than non-reasoning models when used in PromptArmor, which intuitively makes sense.

### Strengths
### Originality

The idea of using an LLM as judge to defend against prompt injection attacks is non surprising, however this is the first work I know of to propose it as a reasonable baseline, and more importantly to provide good empirical evidence that it is a good baseline for prompt injection defenses.

### Quality 

The quality of the experiments is good. The authors use the standard benchmarks, and test across agentic and non-agentic scenarios, as well as adaptive attack vectors (although I think more work can be done here).

### Clarity

The paper is well written and easy to follow.

### Significance

The core idea of using an LLM as judge prompt injection defense is reasonable and the results are strong. While the idea is not complex, and method is simple, as the authors point at I think this should be viewed as a strength to the method. As we see more and more agentic systems being deployed, research on easy to implement defenses this PromptArmor is significant.

### Weaknesses
There are two main weaknesses that would be good to address:

1. Adaptive attacks are now the most important way to test defenses against adversarial attacks (like prompt injection attacks). For example [1] states that "adaptive attacks cannot be automated and always require careful and appropriate tuning to a given defense." Now for prompt injection attacks, I actually expect attackers to often not have the ability to adapt their attack (instead leaving prompt injections static on websites or untrusted data sources). With that being said, there is still value in testing PromptArmor against thorough adaptive attacks to better understand the failure modes of the defense. Section 4.6 contains some adaptive attack experiments, but it seems they are automated in nature. I expect there to be examples of fairly simple attacks that defeat PromptArmor. It would be beneficial to the paper to in fact find such attacks.
2. The paper could be improved by some cost analysis. Using any defense like PromptArmor is predicated on the fact that the defense is cheap enough to run for every input. Now I expect the defense to be fairly cheap (although using reasoning models for the defense can increase costs significantly due to larger token counts). A more in depth analysis of the cost tradeoff would be desirable. As I said, I expect PromptArmor to actually fair quite well under such analysis.


[1] Tramer, Florian, et al. "On adaptive attacks to adversarial example defenses." _Advances in neural information processing systems_ 33 (2020): 1633-1645.

### Questions
1. Do you agree with weakness 1? If so, do you have any extra results regarding this? If you do not agree with the weakness, please explain why.
2. Do you agree with weakness 2? If so, do you have any extra results regarding this? If you do not agree with the weakness, please explain why.

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper investigates defenses for prompt injection attacks, and specifically, whether simply prompting models can induce them to detect and remove prompt injections. The authors' proposed PromptArmor framework consists of a simple pipeline that asks an LLM to inspect and clean the input before completing the actually specified user task. Across three agentic and non-agentic prompt injection baselines, the authors find that PromptArmor can decrease false positive and false negative rates, with improvements scaling with general model capabilities and size. The authors also perform a comparison with current state-of-the-art prompt injection defenses. Finally, the paper investigates the effectiveness of their defense against adaptive attacks that generate new attacks while interacting with a model armed with the PromptArmor defense.

### Strengths
1. The authors find that a simple defense technique, namely prompting an LLM to determine whether its input has a prompt injection, can be a successful defense method, beating many more sophisticated defenses. The paper demonstrates that these perform better than many other defense baselines. The authors also note how this defense is computationally efficient, as it does not require additional training and can be used with the same model as answering the user query.

2. The paper also evaluates three prominent prompt injection benchmarks in both the agentic and non-agentic settings. The agentic setting is particularly relevant with the recent release of AI browsers, which have access to sensitive data and have been shown to be able to be prompt-injected.

### Weaknesses
1. The biggest issue with this work is novelty. Prior works have experimented with having LLMs examine their inputs to determine when they might be malicious. For instance, [1] has LLMs examine inputs in a pipeline (see Figure 1 of this paper) that is very similar to the proposed pipeline (see Figure 1 of the submission). The only difference seems to be the use of the model to actually remove the prompt injection, which allows the user's intent to be carried out. However, this does not seem to be a major difference. The authors also do not cite [1] nor discuss differences.

2. Table 2 does not seem to be a fair comparison since two variables are being experimented: (1) the base model used and (2) the method used. For a fair comparison, the openai models should be fine-tuned / used as initializations to each of the methods e.g., fine-tuning on the protectai prompt injection dataset.

3. I am confused by Figure 3. This figure seems to be showing that ASR goes up when reasoning is used. This result seems counterintuitive, as more inference time usually leads to better performance. The result also seems to contradict the findings of [2]. Could you explain why this might be?

4. Tensor Trust was designed such that humans found natural prompt injections *against specific models* and are therefore, not highly transferable, but instead reflect the common use case, where individual users find injections that work well against specific models. Therefore, it is not a fair comparison to use much stronger models like GPT-4o and GPT-4 as defenses without a comparison to the ASR on these new stronger models, which is not provided in Table 1 or in the paper (these are only provided for AgentDojo) 

I am generally open to raising my score, especially if weakness 1 is adequately addressed.

[1] Phute, Mansi, Alec Helbling, Matthew Hull, ShengYun Peng, Sebastian Szyller, Cory Cornelius, and Duen Horng Chau. "Llm self defense: By self examination, llms know they are being tricked." arXiv preprint arXiv:2308.07308 (2023).

[2] Zaremba, Wojciech, Evgenia Nitishinskaya, Boaz Barak, Stephanie Lin, Sam Toyer, Yaodong Yu, Rachel Dias et al. "Trading inference-time compute for adversarial robustness." arXiv preprint arXiv:2501.18841 (2025).

### Questions
1. It would be interesting to see an analysis of the number of reasoning tokens used by the defense with ASR (similar to [2] from above).

2. You mention that PromptArmor is less computationally expensive, but this only refers to its lack of training-time compute. However, presumably, if a smaller model could be trained for this purpose, it could then be used much more cheaply at inference time. Did you analyze inference vs. training time efficiency?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper proposes a simple (yet effective) baseline for the defense of prompt injection attacks. The core intuition is that recent large reasoning models are good enough to spot the linguistic components within a prompt that don’t belong to the user’s task. Evaluation on ASR and several perspectives of the detection rate show that the method is performant.

### Strengths
1. The paper is well-written with a reasonable intuition. The storyline is well-justified.
2. The research topic of effective and efficient defense against injection attacks is timely and important.

### Weaknesses
1. It is not fully justified whether the general-purpose utility of the prompt is still preserved after the fuzzy-removal sanitization. **That is, what if the original task already contains some string that looks like an injection (e.g., "Please remove the digits and sort the rest characters in the following string in alphabetical order: qwax6a1sda3cm3sdr5bm.")?** I understand that the authors have reported that the FPR on AgentDojo is very low, so that the guardrail LLM won't strip benign stuff in the existing queries. But this is relatively a vague evaluation, and authors shall consider **curating a collection of seemingly harmful (but actually benign) queries** to stress-test the counterfactual robustness of the guardrail. To make an analogy, it should be like the data in XSTest (NAACL 2024) or MOSSBench (ICLR 2025), which is used to test the over-refusal.
2. Although I do appreciate the straightforward idea of training-free prompting, I would find it more convincing if the injection is used to instruction-tune a model for detection. Please note that, the current symbolic process (fuzzy-match) already enables sufficient input-output data. As authors aim to make the approach "regarded as a standard baseline", releasing such an instruction-tuned judge will be more helpful.

### Questions
The weakness of the paper is listed above, and my initial rating of this paper is marginal rejection. However, I look forward to the authors' response, and my final rating is conditioned on the soundness of our further interactions.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4