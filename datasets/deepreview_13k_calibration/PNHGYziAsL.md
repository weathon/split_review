# SPIN: Self-Supervised Prompt INjection

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Large Language Models (LLMs) are increasingly used in a variety of important applications, yet their safety and reliability remain major concerns. Various adversarial and jailbreak attacks have been proposed to bypass the safety alignment and cause the model to produce harmful responses. We introduce Self-supervised Prompt INjection (\name) which can detect and reverse these various attacks on LLMs. Just by injecting an adaptive defense prompt at inference-time, our method is simple, effective, and compatible with existing safety-aligned models. Our benchmarks demonstrate that our system can reduce the attack success rate by up to 87.9\%, while maintaining the performance on benign user requests. In addition, we discuss the situation of an adaptive attacker and show that our method is still resilient against attackers who are aware of our defense.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method to automatically detect and repair attacker prompts, gaining insights from the relationship between malicious cues and model capabilities. It leverages self-supervision techniques to identify adversarial attacks and implements a inference-time multi-layered defense mechanism against adversarial trigger attacks. The method also aims to complicate the adaptive attacker by considering more constraints.

### Strengths
1. The paper presents a novel self-supervised detection scheme, "repeat" and "interjection," based on the impact of jailbreak attacks on LLM capabilities.
2. Building on this detection method and generating prefixes based on perplexity, this work proposes a multi-layer defense mechanism with multiple components. Combining "repeat" or "interjection" with "reversal" to fix malicious prompts appears feasible, achieving a balance between overhead and effectiveness. Additionally, it considers the challenges of adaptive attacks under the defense mechanisms and predicts an increase in the difficulty of future attacks.
3. The paper evaluates a comprehensive range of attack methods and defense mechanisms, providing comparisons with various existing works.

### Weaknesses
1. The figures and captions in the paper are inconsistent. For example, in Figure 1, the caption mentions "The blue example," which does not exist in the figure.
2. The overall insight is not prominent enough, the reasons for selecting the "repeat" and "interrupt" tasks are unclear, and there is no other ablation about the prompts of these two tasks.
3. The related work section does not provide a comprehensive introduction to the existing defense mechanisms against jailbreak
4. The number of evaluation models is limited, focusing on only two 7B models.

### Questions
1. Why is the defense suffix appended at the beginning? Is there any ablation study to support this choice?
2.The "best thresholds" mentioned in the title (0.89 and 6.55) do not match the values shown in the figure (0.90 and 5.73). Can this inconsistency be clarified?
3. Since the thresholds appear to be fixed, when the dataset is updated, will these thresholds change across different datasets? 
4. In real-world scenarios, the "repeat" and "interjection" tasks may affect the outputs required for benign prompts. Is this jailbreak detection mechanism limited in practical use cases?
5. In Figure 5, it seems that the paper by Jain et al. (2023) is not cited. I could not find this reference in the bibliography.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper detects jailbreakings by task redirection. It introduces an additional inference by prompting the model to do something else (repeat the input, output the capital of France, etc). The detection works because (1) the model tends to do the new task if there are no jailbreakings (2) the model tends to reject to respond when there is a jailbreak. Experiments show an improved security against jailbreakings, and a flexible choice of the three proposed filters. The repeat filter asks the model to repeat the instruction, and the detection loss is the Levenshtein Distance between the original user request (ground truth) and the newly generated sentence. The interjection filter redirects the model to answer “What is the capital of France?” with the loss as the logits for ‘Paris’ as the next token. The reversal layer optimizes a prefix to minimize perplexity, which is much larger when there is a jailbreaking.

### Strengths
1. It is novel to detect jailbreakings by prompt injections. The method is well motivated to construct a task where we know the ground truth, and judge using a loss function whether the redirected input leads to the expected response. This seems to be an initial paper that uses prompt injections for good.

2. The authors design three filters and demonstrate their individual defense performance with the computational cost, and show that we could choose different combinations according to the defense case. 

3. The experiments are very comprehensive, highlighting the detection advantage. Most notably, it shows good defense performance against adaptive attacks. The authors carefully design adaptive attacks that optimize with the defense, and show that this optimization becomes much harder.

### Weaknesses
1. The title is misleading, and it seems to be proposing a new prompt injection attack. However, the paper aims to detect jailbreakings using the idea of prompt injection. Also, I think only the interjection is doing prompt injection as there are two conflicting instructions. Repeat is adding a higher level instruction that treats the original instruction as the data. Reversal is not for detection - it is a prevention defense by optimizing prefixes to have less perplexity. A clearer way to present is necessary.

2. For Table 1, can you explain why repeat and interjection costs less than standard inference? I thought it requires an additional inference, so the overall computation should be more than doubled.

3. The defense assumes the model is vulnerable to prompt injections. What if the model is secure against them? Does it invalidate some proposed defense filters? GPT-4o mini implemented with the instruction hierarchy defense against prompt injections could be a good model to test.

### Questions
See weaknesses.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a defense mechanism designed to detect and counteract jailbreak prompts. The proposed approach, Self-supervised Prompt Injection (SPIN), employs adaptive prompt injection at inference time, allowing it to detect and mitigate adversarial prompts by leveraging self-supervised tasks. By injecting defense prompts, SPIN effectively reduces the success rate of attacks while preserving performance on benign inputs. The paper demonstrates that SPIN achieves a significant reduction in attack success rates, even against adaptive attackers aware of the defense mechanism. Extensive evaluations on benchmarks, including Advbench, indicate the robustness of SPIN, as it shows a notable reduction in attack success rates for both Vicuna and Llama-2 models.

### Strengths
The proposed method leverages adaptive prompts, which dynamically align with attacks, rather than requiring training-time adjustments or extensive resources for defense, offering an innovative defense mechanism against unforeseen and adaptive attacks.

### Weaknesses
1. The proposed method is built on an argument that "We find jailbreak inputs often leave a trace, such as degrading other capabilities of the LLM in order to achieve a successful attack." However, this claim is not strictly verified. The paper conducts experiments on Llama-2-chat and Vicuna-7b, which, from today's perspective, do not have strong performance compared to models like the Llama 3 series. Thus, if the evaluations and the claim are based on Llama-2-chat and Vicuna-7b, it may hold true that injecting anything—not specifically jailbreaks—will influence the models' capabilities, but not true for other advanced models. The authors should demonstrate the generalization of their argument. This is critical as the proposed method is built on this argument.
2. Another fatal weakness is that the paper mentions predefined thresholds for the repeat and interjection tasks to distinguish between benign and malicious inputs. However, it is unclear how well these thresholds generalize across different models or contexts, and it seems the paper does not discuss how it decides the thresholds either. In practice, the choice of threshold can have a severe impact on the defense performance, as we can infer based on Figure 4.
3. Based on the computational overhead discussed in Section 4.6, the proposed method introduces additional (multiple) LLM inference rounds. Therefore, it should also be compared with other baselines that have similar computational overhead. For example, guardrail methods like the LlamaGuard [1] series have shown strong performance on jailbreak attacks. Thus, the paper should include a comparison with these guardrail defenses.

### Questions
1. Could the authors elaborate on the process of threshold calibration for the repeat and interjection tasks? Specifically, how robust are these thresholds across different LLMs and configurations?
2. How does SPIN generalize across more LLMs, as mentioned in the weaknesses?
3. How does SPIN perform with prompts or adversarial inputs from specialized domains (e.g., medical, legal)? Are additional defenses required for domain-specific attacks, or does SPIN generalize effectively across diverse content areas?

Update: I have reviewed the authors' feedback and revised my score accordingly.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces SPIN, a new defense against various LLM attacks. SPIN detects these various attacks by constructing self-supervised tasks and reverses them by adding an optimized prefix to the inputs. Experimental results demonstrate that SPIN effectively defends against different types of LLM attacks.

### Strengths
1. The proposed algorithm is straightforward and easy to implement, and the paper provides a clear description of the algorithm.

2. The experiments tested various attacks and evaluated results on different datasets.

3. An adaptive attack is introduced, along with evaluation and analysis.

### Weaknesses
1. The paper needs to clarify which specific type of attack it defends against, such as jailbreak, prompt injection, or both.

2. The paper should include additional experiments to show FPR and TPR, especially FPR on benign data. Furthermore, it should evaluate on more recent models.

3. The computational cost of the proposed method may be impractical.

### Questions
1. I believe the paper should clarify the specific type of attacks it defends against. Generally, prompt injection and jailbreak attacks are distinct. If SPIN is designed specifically for jailbreak attacks, it should state this clearly rather than introducing things like "detect and reverse these attacks (various adversarial and jailbreaks)" in Abstract or “Figure 1 shows our prompt injection defending an adversarial prompt injection.” If SPIN can also defend against prompt injection, it should be compared with more defenses, such as Known Answer Detection [1] and StruQ [2].

[1] Formalizing and Benchmarking Prompt Injection Attacks and Defenses

[2] StruQ: Defending Against Prompt Injection with Structured Queries


2. I recommend including FPR and TPR (ROC curves) in the evaluation. Current evaluation results only contain ASR. Based on the results in Figure 4, the interject task shows a relatively high FPR (over 0.2 at the best threshold). Therefore, metrics like FPR should also be presented in the evaluation to assess whether SPIN results in significant utility loss.

3. The computational cost of the proposed method may be impractical. First, both the repeat and interjection techniques require an additional query, which can be a substantial cost for high-traffic LLM applications (e.g., ChatGPT). Additionally, while the paper states that "detection will remove a large portion of attacks," Figure 7 shows a noticeable gap in ASR with and without reversal, especially on less robust models (e.g., Vicuna). In such cases, the computational overhead of reversal becomes excessive.

4. The evaluation is somewhat lacking. The experiments were conducted only on Vicuna and LLaMA2. I suggest including more models, such as LLaMA3, Mistral, etc., for broader evaluation. Additionally, since the reversal modifies the prompt structure, I would like to see tests on more datasets to assess the extent of utility loss caused by the reversal rather than just using TriviaQA.

Typo: Figure 4 shows "Best Threshold = 5.73" for interject tasks, but the caption states it as 6.55.

### Soundness
2

### Presentation
3

### Contribution
2
