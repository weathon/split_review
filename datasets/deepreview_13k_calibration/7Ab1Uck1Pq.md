# Profiler: Black-box AI-generated Text Origin Detection via Context-aware Inference Pattern Analysis

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
With the increasing capabilities of Large Language Models (LLMs), the proliferation of AI-generated texts has become a serious concern. Given the diverse range of organizations providing LLMs, it is crucial for governments and third-party entities to identify the origin LLM of a given text to enable accurate infringement and mitigation of potential misuse. However, existing detection methods, primarily designed to distinguish between human-generated and LLM-generated texts, often fail to accurately identify the origin LLM due to the high similarity of AI-generated texts from different sources. In this paper, we propose a novel black-box AI-generated text origin detection method, dubbed Profiler, which accurately predicts the origin of an input text by extracting distinct context inference patterns through calculating and analyzing novel context losses between the surrogate model's output logits and the adjacent input context. Extensive experimental results show that Profiler outperforms 10 state-of-the-art baselines, achieving more than a 25\% increase in AUC score on average across both natural language and code datasets when evaluated against five of the latest commercial LLMs under both in-distribution and out-of-distribution settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors present an AI-generated text origin detection method (aka Profiler) by extracting distinct context inference patterns through calculating and analyzing novel context losses between the surrogate model’s output logits and the adjacent input context. They demonstrate the effectiveness of Profiler by comparison against multiple baselines on natural language and code datasets.

### Strengths
The experiments are thoroughly performed and the comparison with multiple state-of-the-art baselines bring out the novelty and the advancement clearly. They further present the ablation study to demonstrate the effectiveness of the different components in the proposed architecture such as context window size and surrogate model selection.

### Weaknesses
It would really help the readers if the authors can provide the intuition behind the design of Profiler (Section 4). The section, though presents the working of the different components, fails to provide the different design choices behind each component. In the current form, it is difficult to intuitively understand why the proposed approach is working effectively. Specifically, the rationale behind using cross-entropy loss between the surrogate model's output logits and the one-hot encodings of the context is not clear. Why is this loss a good indicator of AI-generated text? Furthermore, the motivation for subtracting neighboring cross-entropy losses to enhance distinguishability needs more explanation. What specific properties of AI-generated text does this operation exploit?

### Questions
Check my comments in Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work focused on different AI-generated text origen detection. Compared to other baselines, this work proposed to capture the context-aware patterns between the generated output logits and its adjacent input contexts. By collecting such contextual information across different close-source commercial LLMs, such as GPT-4-Turbo, Claude3 Sonnet and Gemini-1.0 Pro. The proposed method Profiler outperforms several baselines across 6 different datasets.

### Strengths
- This work designed a contextual loss between the output logits and its adjacent input tokens, and then use this pattern to further capture the independent and correlated patterns to train a classifier.
- This work evaluated their methods across different baselines and datasets.

### Weaknesses
 - This work lacks lots of details about how to construct the AI-generated texts from GPT-3.5-Turbo, GPT-4-Turbo, Claude-3-Sonnet, Claude-3-Opus, and Gemini-1.0-Pro, for example, how many data samples are generated for each dataset, how different is each generated sample compared to original dataset samples, and what kinds of prompts are used to instruct those five close-source LLMs?
- It lacks reasonable explanations as to why the cross-entropy loss between the output logits with its adjacent input tokens can capture the difference between different LLMs' generated texts. In addition, there is no more analysis regarding this contextual loss in the experimental results section, and how to make the correlation between the entropy loss and different identified LLMs' generated texts.

### Questions
- This work chose the surrogate model to detect different AI-generated texts. In line 55, the authors also mentioned that a surrogate model is an LLM with comparable capabilities. This work uses LLaMA2-7B, LLaMA2-13B, LLaMA3-8B, Mistral-7B, Gemma-2B, Gemma-7B as surrogate models to detect close-source LLMs, such as GPT-3.5-Turbo, GPT-4-Turbo, Claude3-Sonnet, Claude-3-Opus and Gemini-1-Pro. It is interesting whether those surrogate models have comparable capabilities to detect those larger close-source LLMs.
- In line 247, the argument about the potential overlapping training data needs further explanation as we actually do not know what kinds of training data are used for those closed-source LLMs.
- As mentioned in the weakness section, it is unclear why the cross-entropy loss works to detect different LLMs' generated texts. What does the cross-entropy loss represent if the loss is high or low?
- The AI-generated texts lack lots of collection and construction details as mentioned in the weakness section. It is the same for the paraphrased versions of the six datasets. If we do not know how those datasets are constructed, we won't understand why the proposed Profiler method can even achieve close 100% AUC on some datasets for some LLMs, such as Essay dataset for GPT-4 Turbo.
- In line 429, Profiler and other baselines are trained on the original datasets and test them on the paraphrased version of the same datasets. As the used surrogate models are LLaMA2-7B, LLaMA2-13B, LLaMA3-8B, Mistral-7B, Gemma-2B, Gemma-7B, how do authors make sure that those surrogate models never see those datasets before during their pretraining. In addition, do authors train profiler using fine-tuning or other methods? It lacks many details.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
PROFILER proposes a novel method for detecting the origin of AI-generated text using a black-box approach that involves calculating novel context losses between the output logits of a surrogate model and the adjacent input context. PROFILER can differentiate texts generated by various LLMs with higher precision by broadening the analysis beyond simple next-token prediction patterns to include contextual information around each output token.

### Strengths
Overall, the proposed PROFILER has the following advantages:
1. PROFILER consistently outperforms state-of-the-art baselines, showing over 25% average increase in AUC score across evaluations, indicating a robust capability to detect the origin of AI-generated texts.
2. Effective across both natural language and code datasets, demonstrating the method’s adaptability to different content types.
3. The use of context-level inference patterns provides a deeper insight into the generation patterns of different LLMs, improving discrimination between sources.

### Weaknesses
1. Some terms, concepts, and figure captions need definitions and explanations for readers to better understand.
2. Mathematical notations and derivation need improvement.
3. The experimental setup requires enhancement, and further validation is necessary to evaluate its generalizability.

1. In lines 69-70, references are needed for independent and correlated features. 'output logits for each token' needs further explanation. Are they feature vectors learned from something? Why are they independent?
2. In lines 184-186, do the PROFILER features only have 2 dimensions? If not, how are these two dimensions selected?
3. In Figure 2, most of the features have an oval shape. This makes sense since projecting them onto the PROFILER feature axis 1/2 gives you Gaussian distributions. Is there an explanation for why do the GPT-3.5 Turbo features (green) not follow a 2D Gaussian distribution and why does it look very different from GPT-4 Turbo (I do not expect the shapes to be very different from GPTs)?
4. It seems PROFILER feature 1 provides most of the separable information, and the feature 2 ranges of different data samples are highly overlapped. Is it possible to separate the texts with only one feature?
5. In Equation 1, what does the black dot represent? Functions with black dots represent a family of functions and are usually used for caption explanations, but not used for formally defining a variable.
6. Lines 235-240, what is the definition of the input token sequence X? X=x_{1:n} or X=x_{1:i}? 
If X=x_{1:i}, X needs a subscript index i (e.g., X_i), since X depends on i.
7. Line 256, what is the definition of C? Is C a set or a vector?
8. Lines 259-260, why does an even W guarantee the context matrix L^C to be symmetric? It seems that the dimension of L^C also depends on n.
9. Equation 2 looks confusing. Considering that tilde P_k is a ||V||x1 vector, the dot in Equation 2 is an element-wise product (if o^v_{i-1+W/2} is a scalar) or a vector inner product (if o^v_{i-1+W/2} is a vector)?
10. Line 279, standard deviation and variance are highly dependent (providing repeated information), is there any specified reason for including both in the key property feature s^i?
11. Lines 291-293, why do the vectors s^j, d^j, and g^j in IP vector have the same dimension and how do these vectors construct a matrix? It seems that s^j is a 6x1 vector, d^j is a (n-W-1)x1 vector, and g^j is (n-W-2)x1.
12. Line 340, what is zero-shot pattern? Further explanation or reference is needed here.
13. Line 356, please explain what are 'in-distribution' and 'out-of-distribution' settings. Further explanations are required to demonstrate the difference between these two experiment settings.
14. Line 465, the authors consider the samples from Arxiv and Yelp as natural language datasets. Is it possible the samples from Yelp consist of some of the GPT-generated texts or Arxiv consists of some of the human-written and GPT-moderated samples?
15. The experiments show that the proposed model can perform well in distinguishing two situations -- human-written and LLM-generated cases. I am curious about the generalization on the marginal cases, such as the text is firstly human-written but later modified (rewritten) or translated by LLM. Will these be considered as human-written or LLM-generated?

### Questions
1. In lines 69-70, references are needed for independent and correlated features. 'output logits for each token' needs further explanation. Are they feature vectors learned from something? Why are they independent?
2. In lines 184-186, do the PROFILER features only have 2 dimensions? If not, how are these two dimensions selected?
3. In Figure 2, most of the features have an oval shape. This makes sense since projecting them onto the PROFILER feature axis 1/2 gives you Gaussian distributions. Is there an explanation for why do the GPT-3.5 Turbo features (green) not follow a 2D Gaussian distribution and why does it look very different from GPT-4 Turbo (I do not expect the shapes to be very different from GPTs)?
4. It seems PROFILER feature 1 provides most of the separable information, and the feature 2 ranges of different data samples are highly overlapped. Is it possible to separate the texts with only one feature?
5. In Equation 1, what does the black dot represent? Functions with black dots represent a family of functions and are usually used for caption explanations, but not used for formally defining a variable.
6. Lines 235-240, what is the definition of the input token sequence X? X=x_{1:n} or X=x_{1:i}? 
If X=x_{1:i}, X needs a subscript index i (e.g., X_i), since X depends on i.
7. Line 256, what is the definition of C? Is C a set or a vector?
8. Lines 259-260, why does an even W guarantee the context matrix L^C to be symmetric? It seems that the dimension of L^C also depends on n.
9. Equation 2 looks confusing. Considering that tilde P_k is a ||V||x1 vector, the dot in Equation 2 is an element-wise product (if o^v_{i-1+W/2} is a scalar) or a vector inner product (if o^v_{i-1+W/2} is a vector)?
10. Line 279, standard deviation and variance are highly dependent (providing repeated information), is there any specified reason for including both in the key property feature s^i?
11. Lines 291-293, why do the vectors s^j, d^j, and g^j in IP vector have the same dimension and how do these vectors construct a matrix? It seems that s^j is a 6x1 vector, d^j is a (n-W-1)x1 vector, and g^j is (n-W-2)x1.
12. Line 340, what is zero-shot pattern? Further explanation or reference is needed here.
13. Line 356, please explain what are 'in-distribution' and 'out-of-distribution' settings. Further explanations are required to demonstrate the difference between these two experiment settings.
14. Line 465, the authors consider the samples from Arxiv and Yelp as natural language datasets. Is it possible the samples from Yelp consist of some of the GPT-generated texts or Arxiv consists of some of the human-written and GPT-moderated samples?
15. The experiments show that the proposed model can perform well in distinguishing two situations -- human-written and LLM-generated cases. I am curious about the generalization on the marginal cases, such as the text is firstly human-written but later modified (rewritten) or translated by LLM. Will these be considered as human-written or LLM-generated?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper addresses the challenge of detecting the origin of AI-generated texts, given the increasing capabilities of large language models (LLMs) and the similarity of texts produced by different models. Current detection methods struggle to accurately identify the specific source model. To tackle this, the authors propose PROFILER, a novel black-box detection method that predicts the origin of a text by analyzing distinct context inference patterns, specifically by calculating context losses between the surrogate model’s output logits and adjacent input contexts.

### Strengths
1. The paper is well-written and presents its ideas clearly, making it accessible to readers from both technical and non-technical backgrounds. 
2. The detection method is effective and rigorously tested. The authors designed comprehensive experiments, evaluating the model against ten state-of-the-art baselines and providing performance comparisons under both in-distribution and out-of-distribution scenarios.
3. Unlike prior methods that primarily focus on distinguishing human-generated from AI-generated texts, this work addresses the more nuanced task of identifying the specific source model.

### Weaknesses
The paper does not have any major shortcomings, but please refer to the Questions session to add additional analysis of experimental observations.

### Questions
1. In Table 1, I was surprised by the significant performance variation of the baseline methods implemented by the authors across different models, **ranging from 0.01 to 0.8**. In contrast, PROFILER appears to perform more robustly. Could the authors provide further analysis of this performance variation and discuss potential reasons why PROFILER appears more robust across models

2. Similarly, in Table 2, I noticed that the scores of the two models from the Claude family are relatively lower compared to other models in the Normal Dataset. Could the authors provide more discussion on this observation? Additionally, it would be helpful to explain why the performance of your method is better on paraphrased datasets than on the Normal Dataset.

### Soundness
3

### Presentation
4

### Contribution
3
