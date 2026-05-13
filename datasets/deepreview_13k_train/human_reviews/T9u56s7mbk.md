# Learning Harmonized Representations for Speculative Sampling

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Speculative sampling is a promising approach to accelerate the decoding stage for Large Language Models (LLMs). Recent advancements that leverage target LLM's contextual information, such as hidden states and KV cache, have shown significant practical improvements. However, these approaches suffer from inconsistent context between training and decoding. We also observe another discrepancy between the training and decoding objectives in existing speculative sampling methods. In this work, we propose a solution named HArmonized Speculative Sampling (HASS) that learns harmonized representations to address these issues. HASS accelerates the decoding stage without adding inference overhead through harmonized objective distillation and harmonized context alignment. Experiments on four LLaMA models demonstrate that HASS achieves 2.81x-4.05x wall-clock time speedup ratio averaging across three datasets, surpassing EAGLE-2 by 8\%-20\%.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Hass method includes leveraging a hybrid autoregressive and non-autoregressive (HASS) approach to optimize decoding time. The authors present experimental results demonstrating improved performance compared to baseline SD methods.

### Strengths
The experiments are well-detailed, with clear metrics for comparison against baselines (e.g., EAGLE and multiple architectures).

The method makes sense in the perspective of typical acceptance process in SD.

### Weaknesses
1. While the paper introduces a novel approach, it does not sufficiently explore the construction and utilization of the self-distillation dataset. Isn't the quality and configuration of this dataset more crucial than the framework itself? A deeper discussion on how the dataset is designed and its influence on model performance would strengthen the claims [Referring to A].

2. The paper lacks experiments analyzing how the framework performs across different token counts and task types [Referring to A]. Adding these analyses could provide a more comprehensive understanding of the proposed method's scalability and robustness. For instance, how does performance vary when the token count significantly increases or decreases? Are there certain task types where the proposed method excels or struggles compared to baselines?

### Questions
Seek weakness.

Will update the score after looking at the results of Weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes two improvements to the speculative decoding method EAGLE. First, it regularizes training of the draft model to focus on top-K tokens. Second, it trains the draft model to use its own predictions when drafting more than one token. Both improvements are inspired by how speculative decoding is used during inference.

### Strengths
The paper carefully considers the two important aspects of speculative decoding efficiency: the ability of the draft model to predict top-K tokens and the number of tokens the draft model can successfully predict. Authors identify respective shortcomings of the recent method EAGLE and propose practical solutions.

- Empirical results are convincing and demonstrate meaningful improvements in terms of acceptance rate and speedups
- Authors present extensive ablation studies providing additional insights

### Weaknesses
A more rigorous mathematical presentation of the loss function in Section 3.2 (harmonized context alignment) would help to improve clarity. It is not easy to parse what is the input to the draft model at every step and what is it trying to predict. Writing out the objective function for training the draft model would help. I am also confused by Figure 3 - should Training Step 2 have $f^{(l)}_{t-2}$ and $f^{(l)}_{t-1}$ in the bottom row and only use superscript $(s_1)$ in the bottom right entry $f^{(s_1)}_{t}$ (analogously for steps 3 and 4)?



### Questions
- Could you please specify what data was used for training the draft model in the experiments? Does the proposed method (and EAGLE) suffer from generalization issues when speculative decoding is tested on data different from what was used to train the draft model?
- Can training on Model Generated data mitigate the context misalignment? In other words, will HASS outperform EAGLE-2 trained on Model-Generated data? It'd be interesting to see a comparison to EAGLE-2 in Table 8.

My rating for this paper is (7), which is not available as an option. If my questions and clarity concerns are addressed, I will be happy to consider raising the rating to (8).

### Soundness
4

### Presentation
2

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
This paper identifies two drawbacks—objective misalignment and context inconsistency—within the current speculative approach (EAGLE) and proposes a progressive training framework, HASS, for better adapting draft models to actual decoding scenarios. The framework incorporates a distillation loss and a progressive training paradigm to reduce error accumulation caused by misaligned input features, empowering draft models to generate longer and more reliable token sequences. Experiments across various datasets and model sizes demonstrate that HASS significantly outperforms other speculative competitors and achieves impressive inference acceleration.

### Strengths
1. The motivation to improve the current speculative decoding method is clear and well-founded.
2. The paper is well-written and easy to follow.
3. The proposed HASS significantly outperforms other baseline methods and achieves impressive speed-up performance. Without introducing extra inference costs, HASS can be nearly considered a 'free lunch' while incurring only acceptable additional training costs (3 or 4 extra alignment steps).
4. The authors conduct interesting ablation experiments to provide a better understanding of this method, such as the variations in reweight factors demonstrated in the experiments shown in Table 5.

### Weaknesses
1. The training efficiency of this method appears to have limitations. During the additional training steps (step 2, 3, 4...), each token’s corresponding KV matrix differs, making it infeasible to compute all attention scores through a single matrix multiplication. Could the authors offer a solution for this issue or provide detailed reports on the specific training time costs?
2. Section 3.2 (HARMONIZED CONTEXT ALIGNMENT) is the core of the proposed method, but the description is overly brief. To enhance readers' understanding, the authors could consider adding more technical details and method insights into the design choices. For instance, highlighting that different steps in model training focus on generating tokens for specific positions within the draft sequence would provide valuable context.

### Questions
1. What does the vertical axis of the line charts in Figures 5 and 6 represent? The ranges shown do not appear to correspond to the acceptance rate.
If the authors are willing to address our concerns, we are open to raise the scores during the rebuttal stage.

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
This paper proposes HASS, a speculative sampling algorithm. HASS makes two main improvements:

- Training objective. The loss focuses on the k most likely tokens in the target distribution, rather than fitting the complete target distribution.

- Training strategy. Methods like EAGLE have inconsistent distributions between training and inference phases - training uses hidden states from target mode, while inference involves predicted values. HASS simulates this process during training by using model predictions as training data.

The paper evaluated HASS on dialogue, code, and math tasks. On LLaMA models, HASS improved the acceptance length by 8%-16% compared to EAGLE-2, achieving 2.81-4.05x speedup.

### Strengths
- The research addresses LLM latency reduction, which is highly relevant for LLM applications.

- The experiments are comprehensive, covering various tasks and models, achieving 3-4x speedup compared to vanilla decoding.

- The ablation studies are thorough. They clearly demonstrate the impact of HASS's two improvements and how different parameter settings affect the final results.

### Weaknesses
 - HASS builds upon EAGLE but requires higher training overhead compared to EAGLE.
- The paper lacks comparisons with more related methods, such as vanilla speculative sampling and Medusa.
- The presentation could be clearer. In Figure 3, the light green text is difficult to read. In Table 1, the "-" marks for PLD and Lookahead Temperature=1 should be explained, considering readers may not be familiar with these methods.

### Questions
- The authors state "It takes $n$ times the training overhead of EAGLE", suggesting HASS training steps have the same overhead as EAGLE training steps. However, HASS training steps (except step 0) actually have larger KV caches, attention scores, etc. For the $i$-th step, how much does the HASS training step increase compared to the EAGLE training step in terms of overhead (computational FLOPs, memory access bytes, GPU memory usage, actual execution time, and actual peak GPU memory)?

- The presentation could be clearer. In Figure 3, the light green text is difficult to read. In Table 1, the "-" marks for PLD and Lookahead Temperature=1 should be explained, considering readers may not be familiar with these methods.

### Soundness
3

### Presentation
2

### Contribution
3
