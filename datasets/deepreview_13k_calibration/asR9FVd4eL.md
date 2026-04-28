# Understanding and Enhancing the Transferability of Jailbreaking Attacks

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Jailbreaking attacks can effectively manipulate open-source large language models (LLMs) to produce harmful responses. Nevertheless, these attacks exhibit limited transferability, failing to consistently disrupt proprietary LLMs. To reliably identify vulnerabilities in proprietary LLMs, this work investigates the transferability of jailbreaking attacks by analyzing their impact on the model's intent perception. By incorporating adversarial sequences, these attacks redirect the source LLM's focus away from malicious-intent tokens in the original input, thereby obstructing the model's intent recognition and eliciting harmful responses. However, these adversarial sequences fail to mislead the target LLM's intent perception, allowing the target LLM to refocus on malicious-intent tokens and abstain from responding. Our analysis further reveals the inherent $\textit{distributional dependency}$ within the generated adversarial sequences, whose effectiveness stems from overfitting the source LLM's parameters, resulting in limited transferability to target LLMs. To this end, we propose the Perceived-importance Flatten (PiF) method, which uniformly disperses the model's focus across neutral-intent tokens in the original input, thus obscuring malicious-intent tokens without utilizing overfitted adversarial sequences. Extensive experiments demonstrate that PiF provides an effective and efficient red-teaming evaluation for identifying vulnerabilities in proprietary LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a simple but effective Perceived-importance Flatten (PiF) attack against LLMs by dispersing the model's focus across neutral-intent tokens, thereby reducing its attention on malicious-intent tokens. Experiments from various perspectives illustrate that, compared to existing baselines like GCG and PAIR, PiF shows high transferability, efficiency, and attack success rate (ASR).

### Strengths
1. The paper introduces a novel and efficient method to reduce LLMs' focus on malicious-intent tokens, thus bypassing the safety alignment.
2. The PiF method demonstrates high transferability across various target LLMs while maintaining a consistently high ASR.
3. Compared to existing baselines, PiF uses fewer tokens in the adversarial prompt and requires less optimization time.

### Weaknesses
1. The paper lacks comparisons with more recent baselines [1, 2, 3], which have been shown to be more effective and efficient than GCG and PAIR.
2. The authors should clarify the detailed implementation of the perplexity and instruction filters used in the paper, either in Section 5.2 or the appendix. For example, in Table 3, while PiF's perplexity is lower than GCG's, it is 9x higher than PAIR's, suggesting that a suitable perplexity threshold could filter out PiF's prompts. Listing the performance of normal text under these filters would help to justify PiF's stealthiness. Furthermore, the paper should specify the exact method used to calculate perplexity, including the model used and the tokenization process.
3. The hyper-parameter settings for GCG and PAIR should be listed in Section 5 or the appendix so that reviewers can assess the fairness of the comparisons. This includes details such as the number of optimization steps, learning rates, and any specific configurations used for each baseline.
4. In addition to GPT-4, the authors should include tests with more recent models such as GPT-4o, Claude-3, and the Gemini-1.5 series. The paper should also clarify whether the same set of adversarial prompts are used across different models, or if the prompts are optimized for each specific model.

### Questions
1. In the performance evaluation, did the authors generate only one adversarial prompt for each malicious request, or multiple adversarial prompts are generated for a single malicious request?
2. In real-world applications, user prompts may be paraphrased by software for better inference. Is the PiF attack robust to such paraphrasing?

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
This paper studies the transferability of the jailbreak. Existing white-box attacks overfit the surrogate model and thus fail to transfer to new models. The authors observe that the surrogate model focuses on the specific adversarial tokens/prompts while the new model doesn't. Therefore, this paper proposes to use synonyms to replace the neutral-intent tokens to increase their importance so that the model focuses less on harmful tokens. Experiments show it can outperform existing baselines.

### Strengths
1. Interesting observation about the distributional dependency.
2. Experiments show higher transferability than baselines.

### Weaknesses
1. Only one large commercial model is evaluated. It's suggested to include Gemini and Claude 3.5.
2. It lacks human study to prove that the generated results are harmful and truly provide the correct and useful answers.
3. This word substitution seems not robust against random drop [1] and grammar correction because the generated sentence contains typos such as "and the build a bomb".

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
3

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
This paper proposes a method for improving the transferability of jailbreaking attacks on large language models (LLMs). The paper observes that existing attacks work well on a certain LLM, but their generated jailbreaking prompts do not transfer to another LLM. To understand the underlying reason, this paper proposes to measure the importance of each token in the input text with respect to the subject LLM. It is achieved by removing each token in the input and checking the model’s output using a template. The paper shows that the importance of harmful tokens is similar to other common tokens in successful attacks but not in unsuccessful scenarios, such as transferable attacks. It hence proposes to modify the harmful question by replacing unimportant tokens with their synonyms such that the importance on each token is evenly distributed. The results show the proposed approach can significantly improve the transferability of jailbreaking prompts. It also reduces the time cost of attacks.

### Strengths
1. Jailbreaking attacks are an important research direction for understanding the vulnerability of LLMs. This paper studies the transferability of existing attacks, which is critical for evaluating the robustness of LLMs when no access to their weight parameters.

2. The study on the importance of each token with respect to the model under investigation is very interesting. It seems that using the template can exact attention-like information from LLMs. This is an interesting method and may be generally applicable to other tasks as well.

3. The design of evenly distributing the importance of each token makes sense. From empirical results, the proposed simple synonym-replacement is sufficient to improve the transferability of jailbreaking attacks.

### Weaknesses
1. The paper focuses on the transferability of jailbreaking attacks. The original paper of GCG has also conducted such an evaluation, where it crafts an adversarial suffix on multiple LLMs and then tests the attack on other models. However, such an experiment is not conducted in the paper. GCG has shown reasonable transferability across various LLMs. It is critical to conduct the comparison with these attacks on top of the base attack methods. The paper also only uses Llama-2-7B-Chat as the source model for GCG and PAIR. Why are other models not used as the source model for the evaluation?
2. According to Table3, it seems Instruction Filter is quite effective defending against the proposed attack approach. It is unclear why the proposed attack is needed if it can be easily defended. The paper does not provide sufficient justification to support the usefulness of this approach.
3. There is no comparison with state-of-the-art attacks [1]. The evaluated attacks in the paper are from 2023. There are many new attack methods. The paper needs to provide explanation and justification why only GCG and PAIR are used as the baselines.

### Questions
Please see the weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the transferability of jailbreaking attacks. By quantitatively studying the model's intent perception based on Llama-2-7B/13B, this paper concludes that the inconsistent effectiveness of the adversarial prompts across source and target LLMs is due to the inherent distributional dependency. This paper also proposes a novel attack method named PiF.

### Strengths
1. This paper provides a plausible explanation for the transferability of jailbreaking attacks, backed up with a demonstrative example shown in Figure 2. I believe this is the right direction for transferable jailbreaking attack research. To better support the claims in Section 3, I suggest providing more quantitative results in future revisions.

It is also notable that the presentation of this paper is very good. The color scheme is carefully chosen. The tables and the LaTeX boxes are well-made. It is a pleasure to read this paper.

### Weaknesses
1. Some results in this paper are merely demonstrative, e.g., those shown in Figures 1 and 2. As its title suggests, this paper works on both understanding and enhancing the transferability of jailbreaking attacks. The effort put into "understanding" is much less than those on "enhancing". More quantitative results would greatly help support the claims in Section 3.

2. Perspective III, i.e., the distribution dependency, is trivial. It is not surprising that the high-importance regions are dependent on the model's parameters. As the term distribution dependency is emphasized many times (even in the abstract!), the readers would expect a more significant result than those in Section 3.3. The analysis lacks depth; for instance, it does not explore how specific architectural differences in LLMs might affect the distribution dependency, or how this dependency manifests across different layers of the models.

3. Evaluation.
    + In Table 2, only GCG and PAIR are compared. I suggest comparing some other popular jailbreaking attacks, e.g., AutoDAN [1] and ReNeLLM [2].
    + In Line 395, it is claimed that only the outputs are accessible. However, GCG is a white-box attack method that requires the access to model's parameters, leading to a contradiction. It is also very confusing how it is possible to attack GPT-4 using GCG. I suppose GPT-4 is a close-sourced model which does not meet the requirement of GCG. 
    + I cannot find the results about "enhancing" the transferability of the jailbreaking attacks.

There are also some minor issues.
1. It seems that Figure 1 does not illustrate the main idea of this paper, which is slightly misleading.
2. In Table 1, the existing jailbreaking attacks are categorized into model/token/prompt-level and hand-crafted. It seems that the "model-level attacks" refers to the white-box attacks in the literature. Could the authors please provide some references for this kind of taxonomy?

### Questions
See the weakness part, especially the evaluation.

### Soundness
3

### Presentation
3

### Contribution
3
