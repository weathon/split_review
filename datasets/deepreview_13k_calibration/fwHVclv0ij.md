# Online Detection for Black-Box Large Language Models with Adaptive Prompt Selection

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 3, 6, 6

## Abstract
The widespread success of large language models (LLMs) has made them integral to various applications, yet security and reliability concerns are growing. It now becomes critical to safeguard LLMs from unintended changes caused by tampering, malicious prompt injection, or unauthorized parameter updates, etc. Early detection of these changes is essential to maintain the performance, fairness, and trustworthiness of LLM-powered applications. However, in black-box settings, where access to model parameters and output probabilities is unavailable, few detection methods exist. In this paper, we propose a novel online change-point detection method for quickly detecting changes in black-box LLMs. Our method features several key innovations: 1) we derive a CUSUM-type detection statistic based on the entropy and the Gini coefficient of the response distribution, and 2) we utilize a UCB-based adaptive prompt selection strategy for identifying change-sensitive prompts to enhance detection. We evaluate the effectiveness of the proposed method using synthetic data, where changes are simulated through watermarking and model version updates. Our proposed method is able to detect changes quickly while well controlling the false alarm rate. Moreover, for real-world data, our method also accurately detects announced changes in LLM APIs via daily online interactions with APIs. We also demonstrate strong evidence of unreported changes in APIs, which may be of independent interest.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel online change detection method for black-box Large Language Models (LLMs), combining a CUSUM-type detection statistic based on entropy and Gini coefficient with a UCB-based adaptive prompt selection strategy to effectively detect changes in LLMs. The experimental results demonstrate the method's effectiveness on both synthetic and real-world APIs, covering various change scenarios.

### Strengths
Innovation: The paper proposes an online change detection approach tailored for black-box LLMs, which is a relatively new research direction and shows high innovation.
Methodology: The combination of CUSUM-type detection statistics and UCB strategy enhances the accuracy and efficiency of change detection.
Experimental Design: The validation of the method on both synthetic and real-world data, including different change scenarios, strengthens the paper's credibility.
Practical Application: The method is significant for ensuring the stability and reliability of LLMs in commercial and safety-critical applications.

### Weaknesses
Generalizability: The paper could benefit from additional experiments to demonstrate the generalizability of the method across more datasets and application scenarios.
Computational Resources: While the paper mentions considerations for computational resources, a deeper discussion on optimizing the algorithm for resource-constrained environments would be beneficial.
Adversarial Attacks: The paper does not address the robustness of the detection system against adversarial attacks designed to evade detection.

### Questions
Generalizability: Could the authors provide more experimental results on the generalizability of the algorithm across different types and scales of LLMs?
Adversarial Attacks: Have the authors considered the impact of adversarial attacks on the detection algorithm, and how could the robustness against such attacks be improved?
Real-time Performance: Could the authors provide data on the performance of the algorithm in real-time or near-real-time environments?
Computational Efficiency: Could the authors further discuss possible methods for optimizing the computational efficiency of the algorithm in resource-constrained settings?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper proposes an online changepoint detection method aimed at identifying changes in black-box LLM APIs. The method is evaluated on synthetic data through simulated watermarking and version updates

### Strengths
+ The paper is easy to follow
+ The author tries to propose a new topic related to LLM security

### Weaknesses
First of all, I found the study itself a little bit weird. The author claims that the detection is for "tampering, malicious prompt injection, or unauthorized parameter updates" at the very beginning of the paper. However, as the user of the API(since it is the black-box setting, I can only assume that the user wants to detect the API change since it makes no sense that the LLM developer wants to detect LLM change in the black-box setting), I don't find it very convincing to claim the ''unauthorized'' parameter updates as a concern that we even need a detector for that. The LLM provider has the right to update their model, and those trusted providers like OpenAI and Anthropic often inform users of the updates and have checkpoints for older versions. Also, the watermark or fingerprint is a method to protect the model or response property [1] , leaking them would make it easier for intellectual leakage. And the decoding changes should not be necessary connected with the watermark. For example, having a more efficient decoding method like [3], or decoding-phase alignment[4] could also lead to that. There is not necessary proof that it is harmful and I don't understand why it is a concern that the user must have the detection against it. For those untrusted LLM API/interface providers, then it could be a risk by prompt injection. For example, custom GPT store or Coze have lots of uncensored bots that the system prompt can be changed into malicious and leading to security or privacy risks[2]. From my side, I can only agree that this could be a risk that we should take care of. However, even though the author mentions the prompt injection in the introduction and abstract, there's no further study on that. Please clarify and provide specific scenarios where detecting such changes is necessary.

Second, I don't find the detection in this setting very challenging. Since some experiment details are missing, I can only assume that the API usage is with a fixed system prompt and zero temperature. In such case, the response is expected to be deterministic. If I see the changes as shown in Fig1, I should know obviously that the API might change. I don't think there's a need for such algorithm proposed in the paper. Could you clarify the experimental setting and provide the LLM response between different LLM versions? Also, have you considered some simple methods, such as similarity in the text level? The lack of baseline methods also makes the contribution less significant.

For the false positive measurement,  I believe a more accurate method is to evaluate the same model with different temperatures or different system prompts since this is more practical in the real-world. For example, the ChaGPT web interface's system prompt and temperature are unknown to the user(let' put aside why this is a risk). Using generating a different answer can sometimes have a huge difference in the response. It is a more practical case and the false positives should be take care with if we really need a detector here. How would your detector perform in this scenario?

Minor weakness: no board impact nor limitation discussed in the paper, also, how the author generated those prompts in the table are unknown

### Questions
See the weakness section above

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper offers a CUSUM statistical method to detect if there is any change in underlying language models based on prompts. Towards this, it introduces a statistic based on entropy and Gini coefficient. The different methods introduced in the paper are effective in black-box settings and adaptive. The paper also discusses the detection of watermarking being enabled by model providers.

### Strengths
- The method is running aggregation of simple statistical metrics and is easy to compute.
- Strong empirical results for such simple metrics in detecting a change in a given model with little delay.
- The experiment covers both white-box and black-box API models.

### Weaknesses
 - The prerequisites of the detector are unclear. The assumptions and level of access/information are missing and therefore the precise motivation/utility behind detection is unclear. The change in model is well advertised in "real-world APIs" and is publicly available information.
- If the detector has access to log probabilities from the model API, then it can easily hash them for each prompt and observe changes in them. The tok-K log probabilities are generally available for frontier SOTA models like GPT4, Gemini, and Claude. This simple baseline (for the detection of change in the model, not watermarking explicitly) is missing. 
- The experiments only cover single instances of changes in the model. It would be great to see the True Positive Rate @ low False Positive/Alarm Rate aggregated over multiple different changes in API models. This can be difficult in black-box API case but can be easily done in a simulated case. 
- For experiments, there are no baselines identified/used making it hard to evaluate effectiveness of method and the task. The related work section is poor.

### Questions
1. What is the threat model or detector's operation surface here? Does the detector have access to API and thus to log probabilities produced by it?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work proposes a detection algorithm for online black-box LLM changes. The detection leverages a CUSUM-type statistic that incorporates entropy and the Gini coefficient. To enable effective detection, it adopts a UCB-based adaptive prompt selection strategy to identify the most change-sensitive prompts. In evaluations, the algorithm demonstrates effectiveness in identifying various backbone changes and model watermarking.

### Strengths
- The paper addresses the important issue of detecting online changes in black-box LLMs.
- The proposed approach is practical and applicable across different type of models, as it comes with minimal assumptions of model itself.
- The UCB-based adaptive prompt selection enables cost-effective detection by focusing on the most sensitive prompts.
- The method is robust, maintaining good ADD with a low false positive rate (high ARL).

### Weaknesses
 - While the authors discuss hyper-parameter selection, further ablation studies on individual hyper-parameters (e.g., C and N) would help clarify their specific effects, rather than assessing them as a whole. Specifically, the impact of varying C, the number of responses per prompt, and N, the length of each response, on both detection latency (ADD) and false positive rate (ARL) needs to be isolated. For example, how does increasing C while holding N constant affect the sensitivity of the CUSUM statistic? Similarly, how does varying N impact the stability of the entropy and Gini coefficient calculations, and consequently, the ARL?
- Due to computational limitations, most experiments are conducted on relatively small models. An analysis of larger models (e.g., Vicuna-7B) would provide more insights into real practice. For example, how ARL and ADD will change with larger model sizes? Will this method still be robust with larger models? The paper lacks a systematic exploration of how model scale affects the detection performance. It is unclear whether the observed detection performance on smaller models will generalize to larger, more complex models with different architectural nuances. The computational cost of applying this method to larger models also needs to be addressed.
- There are limited experiments on real-world APIs with LLM updates. Additional results on version changes will be helpful. For example, the author can test different versions of gpt-4o or gpt-4 with different dates from OpenAI API. The paper needs to demonstrate the method's ability to detect real-world model updates, not just synthetic changes. The current experiments do not adequately address the practical challenges of detecting subtle changes in production LLM APIs, where updates are often gradual and not explicitly announced.

### Questions
- Could you clarify the calculation methods for NTE and NTG? Specifically, how are the tokens merged to estimate the distribution?
- Will different decoding strategies affect the robustness of the detection? For instance, is the model change less likely to be detected with nucleus sampling than with greedy decoding?

### Soundness
3

### Presentation
2

### Contribution
3
