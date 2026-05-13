# Towards Robust and Cost-Efficient Knowledge Unlearning for Large Language Models

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large Language Models (LLMs) have demonstrated strong reasoning and memorization capabilities via pretraining on massive textual corpora. However, this poses risk of privacy and copyright violations, highlighting the need for efficient machine unlearning methods that remove sensitive data without retraining from scratch. While Gradient Ascent (GA) is commonly used to unlearn by reducing the likelihood of generating unwanted content, it leads to unstable optimization and catastrophic forgetting of retrained knowledge. We also find that combining GA with low-rank adaptation results in poor trade-offs between computational cost and generative performance. To address these challenges, we propose two novel techniques for robust and efficient unlearning for LLMs. First, we introduce Inverted Hinge loss, which suppresses unwanted tokens while maintaining fluency by boosting the probability of the next most likely token. Second, we develop a data-adaptive initialization for LoRA adapters via low-rank approximation weighted with relative Fisher information, thereby focusing updates on parameters critical for removing targeted knowledge. Experiments on the Training Data Extraction Challenge dataset using GPT-Neo models as well as on the TOFU benchmark with Phi-1.5B and Llama2-7B models demonstrate that our approach effectively removes sensitive information while maintaining reasoning and generative capabilities with minimal impact.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a framework to remove sensitive information from LLMs without retraining them from scratch. Recognizing the limitations of common unlearning methods like Gradient Ascent (GA), which risks instability and unintended forgetting, the authors introduce two new techniques. The Inverted Hinge Loss (IHL) method enhances stability by suppressing unwanted tokens with the next most likely alternative, while the Fisher-weighted Initialization of Low-rank Adapters (FILA) uses Fisher information to initialize LoRA adapters, selectively targeting parameters associated with unwanted information to optimize unlearning. This dual approach was evaluated on the Training Data Extraction Challenge and TOFU benchmark with models such as GPT-Neo, Phi-1.5B, and Llama2-7B, achieving efficient unlearning with minimal loss to the model’s reasoning and generative capabilities, and demonstrating improved performance over existing methods.

### Strengths
1. The motivation is clearly explained. 
2. Extensive experiments have been conducted to prove the effectiveness of the proposed methods. 
3. The theoretical analysis strengthens the rationale of the proposed methods.

### Weaknesses
1. One of the most significant contributions of this paper is the proposal of Inverse Hard Loss (IHL), which claims to increase the probability of the second-best token only. However, it is not clear why IHL does not affect the probability of other tokens. Based on the definition of IHL in Lines 233, the probability of all other tokens is impacted. As such, IHL can only address problem 1 (Line 224) but cannot address problems 2 and 3 of GA (Lines 224 ~ 226).
2. In Figures 3 and 5, the unlearning performance of employing only IHL (represented in green) does not outperform the GD baseline (depicted in blue), which undermines the effectiveness of IHL. Furthermore, the GD+FILA results in Figures 3 and 5 show lower accuracy and higher perplexity compared to GD, suggesting that FILA may not be effective when combined with a gradient descent based unlearning approach.
3. The main results only use GPT-neo models, which are old models. It is better to use more recent models like Llama and Mistral models to make it more practically useful. It is also inconsistent to use different models for main results and analysis.
4. There are no ablations studies for the following settings: 1) full parameter fine-tuning with IHL; 2) LoRA + FILA only; 3) GD + LoRA + FILA.

### Questions
1. In Figure 3, why are some data points missing? 
2. It is better to add legends in Figures 3 and 4 to improve the clarity.
3. It is better to define “Model Utility” within the paper instead of referring readers to other papers.
4. For the Hinge loss equation in Line 233, since the probability p(.) is in the range of (0,1), the second item within max() function is always larger than 0, right? If so, IHL is to reduce the probability of true tokens but to increase the probability of other tokens, right?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper works on machine unlearning in LLMs, particularly focusing on the challenges of removing specific data instances from a model's memory without retraining from scratch. The authors propose two strategies: Inverted Hinge Loss (IHL) and Fisher-Initialization of Low-rank Adapters (FILA). IHL is designed to replace the unbounded negative cross-entropy loss in gradient ascent with a more stable and efficient loss function. FILA aims to initialize low-rank adapters in a way that prioritizes the removal of unwanted information and accelerates the unlearning process. Extensive experiments validates that the proposed methods significantly outperform existing baselines in efficiency and post-unlearning performance.

### Strengths
1. Authors analyze the derivatives of GA and highlight its shortcomings, the motivation is clear and the theoretical foundation strengthens the rationale for the proposed methods.
2. The introduction of IHL addresses the instability issues of GA by focusing gradient updates on a minimal number of viable replacements for the ground-truth token. This results in a more controlled and stable unlearning process.
3. The proposed strategies are effective. The authors evaluate the methods on multiple datasets and multiple model sizes. This comprehensive evaluation demonstrates the robustness and generalizability of the proposed methods.

### Weaknesses
The intuition and connection between the proposed methods, IHL and Fisher-Initialization of FILA, appear somewhat weak. This makes the paper feel like it is stacking two separate tricks rather than offering a unified and coherent approach. A more systematic linkage between these methods would enhance the overall coherence and impact of the paper. The paper lacks a clear explanation of how IHL and FILA interact to achieve the reported unlearning performance. Specifically, it is unclear whether FILA is simply accelerating the convergence of IHL, or if it is also contributing to the unlearning process in a more fundamental way. Furthermore, the experimental results are primarily on models smaller than 3B parameters, and it is unclear how these methods would scale to larger models such as 7B or larger. The paper does not provide a clear trend of performance as the model size scales up, which limits the generalizability of the findings.

### Questions
How robust are the proposed methods to changes in the data distribution of the forget set? For instance, if the forget set contains highly diverse or outlier data, would the unlearning process still be effective?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors identify the limitations of current unlearning methods (e.g., Gradient Ascent (GA)), which can lead to unstable optimization and catastrophic forgetting of retrained knowledge. To overcome these challenges, the paper introduces two novel techniques for robust and efficient unlearning:

1. **Inverted Hinge loss (HIL):** This new loss function suppresses unwanted tokens while maintaining fluency by boosting the probability of the next most likely token.

2. **Fisher-Initialization of Low-rank Adapters (FILA):** Developed through low-rank approximation weighted with relative Fisher information, this method focuses updates on parameters critical for removing targeted knowledge.

The paper demonstrates the effectiveness of these techniques through experiments on the Training Data Extraction Challenge dataset using GPT-Neo models and on the TOFU benchmark with Phi-1.5B and Llama2-7B models. The proposed approach successfully removes sensitive information while maintaining the reasoning and generative capabilities of the models with minimal impact on performance.

In summary, this paper provides innovative solutions to the drawback of GA and demonstrates the effectiveness of the solutions.

### Strengths
### Originality
- This paper points out the shortcomings of Gradient Ascent (GA) by analyzing its inverse. 
- This paper proposes two strategies to improve these shortcomings. 
- This paper demonstrates the effectiveness of their improvements on two datasets.

### Clarity
- The structure of this paper is clear, and most of the content is explained clearly.

### Significance
- This paper provides insights into knowledge unlearning through the analysis of Gradient Ascent (GA).

### Weaknesses
 - This paper lacks the state-of-the-art knowledge unlearning baselines (such as [1][2]). Although the main goal of the paper is to address the shortcomings of GA, incorporating the state-of-the-art knowledge unlearning for comparison would make it more convincing.

- Some descriptions are not clear enough. For example, lines 221-223 should include more explanation for the reasons. The authors should explain in detail why GA increases the prediction score for all other tokens $v \neq x_t$ in the vocabulary.

- From the experimental results, when only IHL is used, the performance is worse than the original GA. Does this contradict the paper's claim that IHL is designed to address the shortcomings of GA and the analysis of derivatives of GA?

- The paper devotes too much content to the background of knowledge unlearning in the Abstract and in the first paragraph of the Introduction. Since knowledge unlearning is a common problem, I believe it is unnecessary to describe it in such detail. The main content should focus on describing the research conducted in this paper. Specifically, Figure 1 should illustrate the proposed approach rather than the knowledge unlearning problem.

### Questions
What is the reason for deriving the unlearning mechanism of GA from the formulas in lines 217-220?

### Soundness
3

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
4

### Summary
The paper focus on the problem of unstable optimization, catastrophic forgetting, and computational cost from Gradient Ascent for LLM unlearning, and propose two novel techniques, including the Inverted Hinge Loss and Fisher Information weighted initialization of LoRA adapters, for robust and efficient unlearning for LLMs. Experiments on two tasks with different LLMs show that the proposed methods enable faster and more stable LoRA-based LLM unlearning.

### Strengths
1. The paper makes a good contribution to knowledge unlearning of LLMs through improving tuning stability and efficiency with Inverted Hinge Loss and Fisher-Initialization of Low-rank Adapters, respectively. The proposed method is valuable of managing unnecessary forgetting and unbounded optimization in typical Gradient Ascent strategies.
2. The paper is generally well-written, particularly in formula derivation and clear explanation about IHL and FILA solve the weaknesses of GA in Section 3.3 and Section 3.4.
3. The experiments and analysis of the paper is comprehensive, with great illustration on performance evaluation using high quality charts.

### Weaknesses
1. In Introduction Section (Line 51-53), you mention GA and its shortcomings, I think a better way of writing here would be providing a brief overview of 2-3 other key knowledge unlearning approaches beyond GA, and summarize 1-2 common shortcomings across these methods that motivate the proposed approach. GA should be only one of those existing typical methods.

2. In Introduction Section (Line 76), you mention the application of LoRA to LLM unlearning remains unexplored, however, there are some existing studies using LoRA for LLM unlearning, including Practical Unlearning for Large Language Models (https://arxiv.org/abs/2407.10223) and Machine Unlearning in Large Language Models (https://arxiv.org/abs/2405.15152v1). It would be better to briefly summarize (in 1-2 sentences each) how LoRA was used for unlearning in these two papers, and then explain how their proposed approach differs or improves upon these methods.

3. Some important content is missing. In Introduction Section, a lack of clear summarization of contributions in the paper, making readers difficult to capture the important points of the study. Besides, in Related Work Section, a brief comparison between your proposed method and other relevant studies should be presented to better emphasize the advantages of your work.

4. In Section 3.3 (Line 223-227), you should provide a more detailed explanation of how you arrived at these hypotheses. There is still a gap between GA motivation and its weaknesses. To make the illustration more convincible here, a better way would be providing a specific example or mathematical derivation showing how the GA loss function leads to one of the stated problems (e.g., unbounded optimization or inefficient gradient updates).

5. In Section 3.4 (Line 265), a basic and brief description of Fisher Information is necessary here for better understanding of the reason you employ it to address the importance quantification you mentioned before.

6. In Table 1, to make the table more readable, the data of important results should be highlighted via bolding the best result in each row or using color coding to show relative performance between methods, in order to show either your FILA LoRA performs much better than traditional LoRA, or it can approach the performance of full fine-tuning.

7. There are some writing flaws:
* Some sentences are too long to follow and comprehend, such as Line 89-93.
* In Line 419-421, there are two "Second" in these two sentences, making them difficult to be understood.
* The capitalization in the text should be more consistent. For instance, you use lowercase "l" in "Inverted Hinge loss" at Line 20 and Line 161, but uppercase "L" in "Inverted Hinge Loss" at Line 82. All uppercase would be better.

### Questions
1. In Introduction Section (Line 72-74), can you explain more about the reason that low-rankness can be beneficial in stabilizing optimization and preventing catastrophic forgetting? Clearer illustration would be better here.

2. In Table 1, why you record results from running different epochs? Does it mean the method reaches the optimal with these epochs?

3. In Experiments Section, why different LLMs are used for those two tasks? Have you evaluated more popular and larger LLMs such as Llama3.1-8B? I suggest giving explanation of the strategy and purpose of model selection.

### Soundness
3

### Presentation
3

### Contribution
3
