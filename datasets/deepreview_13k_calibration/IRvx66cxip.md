# Enhancing Integrated Gradients Using Emphasis Factors and Attention for Effective Explainability of Large Language Models

- Decision: Reject
- Avg Score: 2.75
- Scores: 1, 1, 8, 1

## Abstract
Understanding the decision-making processes of large language models (LLMs) is critical for ensuring transparency and trustworthiness. While Integrated Gradients (IG) is a popular method for model explainability, it faces limitations when applied to autoregressive models due to issues like exploding gradients and the neglect of the attention mechanisms. In this paper, we propose an enhanced explainability framework that augments IG with emphasis factors and attention mechanisms. By incorporating attention, we capture contextual dependencies between words, and the introduction of emphasis factors mitigates gradient issues encountered during attribution calculations. Our method provides more precise and interpretable explanations for autoregressive LLMs, effectively highlighting word-level contributions in text generation tasks. Experimental results demonstrate that our approach outperforms standard IG and baseline models in explaining word-level attributions, advancing the interpretability of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper highlights limitations of integrated gradients (IG), an importance attribution method for input tokens and proposes multiple solutions to address the downsides of not accounting for the attention computation and the exploding gradients problem. The authors compare their method to other feature attribution methods when performing language modeling on the SST-2 and IMDB datasets and show that their proposed method outperforms the considered alternatives, albeit being close to IG.

### Strengths
- The proposed method outperforms integrated gradients in the given experiments

### Weaknesses
There is a number of issues within the paper - lack of clear purpose and coherence, mathematical precision and various arbitrary choices.

- Section 2, limitations of gradients: The counterexample works for the simple RNN formulation, however the work of the paper focuses on Transformer networks. It is not clear how this relates to the rest of the paper.
- Section 3.1, Theorem: The theorem essentially spells out the chain rule for RNNs. Furthermore, the output of a RNN is not an embedding vector but a probability distribution over the output space, or in the case of language modeling, the vocabulary.
- Section 4, attention axiom: Higher attention value should intuitively imply greater importance, but this is not often the case. See works on Attention is not explanation & subsequent. If the attention value is high, but the norm of the value vector low, its relative contribution in the attention output is low.
- Section 4, Eqs 11—13: AIEG and PosNorm have a mutually recursive definition and it is not clear when it terminates.
- Section 4, Theorem 1: You use the emphasis factor to dampen exploding gradients, however what about vanishing gradients? 
- Section 4, Theorem 2: “Consider an input token with an attention value greater than 0 with respect to the output token” — which, of the many, attention values?
- Section 4, Theorem 2: “Regions where the model is making decisions” — which are these regions, and how do we know with certainty that the model is making decisions there?
- Section 4, Theorem 2: “areas where the output has already been predicted” — how do we know the output has already been predicted?

Section 5: 
- Choice of k: removing top 20% of words is a pretty drastically lage amount. What happens with values of k < 20%?
- “We randomly selected 5000 reviews from each dataset and fine-tuned the models as masked language models” — you fine tuned autoregressive language models as masked language models? How is this done, what are the hyperparameters and why did you not perform tuning in the same manner the models were trained? Furthermore, it is not clear why this step is even required, as the models are already trained for language modeling (which is the task you evaluate token attributions on).
- “Similarly for testing, we randomly selected around 2100 movie reviews from each dataset and used a portion of the review to construct a paragraph of 50, 200, and 400 tokens, with each category having an equal amount of movie reviews (700)” — you need to be precise here.

Typos etc
- Citations in introduction: L31 Lipton citep, space before Shrikumar L34, L36 Enguehard citep
- Figure 1 does not display well when zoomed in
- Theorem much greater than = \gg
- L208: The attention mechanism was not introduced by Vaswani

### Questions
See weaknesses

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The paper critiques the limitations of the Integrated Gradients (IG) method when applied to autoregressive models, particularly concerning exploding gradients and the neglect of attention mechanisms. To resolve these issues, the authors propose an enhanced explainability framework that augments IG with emphasis factors and incorporates attention mechanisms. This approach aims to provide more precise and interpretable explanations for autoregressive LLMs, especially in text generation tasks. The experimental results suggest that this method outperforms standard IG and baseline models in explaining word-level attributions.

### Strengths
The paper presents an improvement over the traditional IG method by addressing its limitations in the context of autoregressive LLMs. The introduction of emphasis factors and attention mechanisms enhances interpretability and precision in explaining model behavior.

### Weaknesses
1. Poor Writing and Formatting: The paper suffers from several unprofessional formatting issues that detract from its presentation and readability. For example: (1) Citation formats are incorrect, specifically noted in lines 30, 35, and 39. (2) Figures are not in vector graphics, resulting in blurry images that compromise their clarity and utility. (3) There is a lack of proper spacing before the start of new sentences, such as the issue in line 75. (4) Incorrect use of quotation marks in the caption of Figure 2. 

2. Unclear Motivation and Relation to Recent Work: The introduction does not clearly establish the motivation of the paper or its relation to recent works beyond 2017-2018. The enhancement based on a 2023 work is mentioned, but the connection to current research trends and its necessity is not well articulated.

### Questions
1. For models like LLaMA that are capable of performing tasks in a zero-shot manner, why is there still a need to fine-tune on specific datasets? Would it not be more insightful to analyze their zero-shot performance directly?
2. Figures 4 and 5 present results for the GPT-2-small model. What are the results for other models?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper highlights shortcomings in current Integrated Gradients (IG) methods when applied to autoregressive model explainability, specifically due to the neglect of attention mechanisms and issues with exploding or vanishing gradients. To address these challenges, the authors propose an enhanced method called "Attended Integrated and Emphasized Gradients" (AIEG), which augments IG with emphasis factors and incorporates the attention mechanism. This approach not only outperforms standard IG and baseline models in generating more accurate word-level attributions for autoregressive models, but it also presents a novel solution to the existing problems in the field. This approach will be helpful for the explanability research community as well as for researchers trying to assess the trustworthiness of autoregressive models.

### Strengths
- Well written and easy to understand paper. The research gaps are identified correctly and a mathematically sound formulation is provided to address IG when it comes to attention based autoregressive models. Well labeled diagrams help in better comprehension of the paper.
    
- The paper provides explanation, albeit in the appendix, regarding the non-usage of gradient clipping to address the exploding gradients problem of IG in autoregressive models.
    
- Clearly highlights in section 2 the limitations of gradients as attributions in autoregressive models.
    
- Comprehensive comparison against multiple competitive baselines. The method performs well on all metrics provided.

### Weaknesses
 - Human assessment for adjudicating the effect of AIEG on the importance of tokens is missing.
    
- Statistical significance test missing for the metrics in the main paper.
    
- Provide examples for importance of EF, in the formulation wrt stability of AIEG calculations.

### Questions
- Line 081: State the sensitivity axiom.  

- Line 474: Use `` instead of “ for opening brackets.  

- Section 5.2: Is there a way to quantify attribution? Which one is better than the other? Are there any comprehensive human evaluations conducted for the same?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper proposes a new feature attribution method, called Attended Integrated and Emphasized Gradients (AIEG) for language models. The authors claim two main improvements: (1). Integrated Gradients with attention mechanisms (although not the first one as we have scaled attention already and it is kind of robust), (2). an emphasis factor to address limitations in explaining autoregressive models. The authors evaluate AIEG against a few gradients-based baseline methods on sentiment analysis tasks and demonstrate improved performance on Log-odds, Comprehensiveness, and Sufficiency.

### Strengths
- **Quality**: The paper presents a sound derivation of the limitations of standard IG for autoregressive LLMs, supported by mathematical proof and visual evidence.
- **Clarity**: The exposition is generally clear, particularly in explaining the shortcomings of IG and motivating the proposed enhancements.
- **Significance**: Improving explainability for large language models is an important research direction.

### Weaknesses
1. **Baseline --> no comparison with scaled attention**:

- Scaled attention (α∇α)  should be included as it is also a feature attribution method that considers both attention and gradients simultaneously.


2. **Experimental Scope**:

- The evaluation is performed on only two datasets (SST-2 and IMDB), which limits the generalizability of the findings. Also, considering the diversity of LLM applications, the experimental results would be more compelling if additional datasets—particularly more common use cases for LLMs, like we do not use LLMs for such easy semantic analysis tasks. It makes sense previous work uses these datasets on BERT or RoBERTa, which are much smaller models used in those easy tasks. 

- The paper only considers GPT2-small, GPT-nano, and llama models for evaluation. While these are commonly used models, additional comparisons with other sizes, e.g. GPT-2 medium/large or LLaMA-7B/13B, or different model architectures, e.g. RNN-based (as you take it as an example in section 2) would provide a broader perspective on the applicability of the method, or LSTM, mamba.

3. **Ablation Studies**:

- The paper does not present sufficient ablation studies to isolate the effects of emphasis factors and attention components individually. An ablation study that shows the contributions of the emphasis factor alone, the attention mechanism alone, and their combination would clarify the value of each component. This would be especially useful given the novel combination approach used in AIEG.

4. **RNN as an example in Section 2 rather than Transformer-based**:

- The entire section 2 explains the limitations of gradients with RNN as examples. Better switch to transformer block, as GPT or Llama included in the paper, neither is RNN-based. It should be include an explanation of why the authors chose RNN examples and how the limitations generalize to transformer architectures. 

5. **Unclear Impact on Downstream Tasks**:

- The paper does not sufficiently address how the improved attributions impact practical downstream tasks like model debugging, bias detection, or other real-world applications that are more complex than SST or IMDB, e.g. GLUE, SuperGLUE, or BoolQ, Winogrande, PIQA,  Hellaswag these popular reasoning tasks.  Further, for example, for a reasoning task, we might be not only interested in one particular prediction but an overall prediction for a sequence. Including a case study demonstrating how AIEG aids in a downstream application could provide a stronger argument for its utility.

### Questions
1. Could you give an intuitive explanation for emphasis factors?

2. How sensitive is the AIEG method to different choices of emphasis factors or the range of α during gradient calculation? A hyperparameter sensitivity analysis would help understand whether these parameters need extensive tuning for different datasets.

3. Would it be possible to incorporate your emphasis factor approach into other gradient-based methods? Have you explored this potential extension?

4. Can you provide a concrete example of how your enhanced attribution method can be used in model debugging or bias detection? Demonstrating a practical use case could help bridge the gap between theoretical contribution and real-world applicability.

5. Is there a reason for choosing 20% as the value of k for masking in the log-odds, comprehensiveness, and sufficiency evaluations? Would varying this value change the relative performance of AIEG compared to the baselines? (Zhao & Aletras, ACL 2023)

Zhixue Zhao and Nikolaos Aletras. 2023. [Incorporating Attribution Importance for Improving Faithfulness Metrics](https://aclanthology.org/2023.acl-long.261). In *Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, pages 4732–4745, Toronto, Canada. Association for Computational Linguistics.

### Soundness
2

### Presentation
2

### Contribution
1
