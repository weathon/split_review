# MAGNET: Augmenting Generative Decoders with Representation Learning and Infilling Capabilities

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
While originally designed for unidirectional generative modeling, decoder-only large language models (LLMs) are increasingly being adapted for bidirectional modeling. However, these unidirectional and bidirectional models are typically trained independently with distinct objectives (generation or representation learning) thereby missing the potential opportunity for one objective to enhance the other. In this work, we introduce MAGNET, an adaptation of decoder-only LLMs that enhances their capabilities in generating robust representations and infilling missing text spans, while retaining their original text generation capabilities. MAGNET employs three self-supervised training objectives and introduces an attention mechanism that combines bidirectional and causal attention, enabling unified training across all objectives. We show that LLMs adapted using MAGNET can outperform state-of-the-art text encoders on token-level and sentence-level representation learning tasks. We also demonstrate that MAGNET enhances the base LLM's ability to generate contextually appropriate text infillings by enabling it to take future context into consideration. Lastly, we show that, unlike other bidirectional language models for representation learning, the LLMs adapted using MAGNET can still perform open-ended text generation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces MAGNET, a decoder-only LLM enhanced in its ability to generate robust representations and infilling missing text spans while preserving its original text generation capabilities. The model's training integrates both unidirectional and bidirectional attention mechanisms. It is also trained with three objectives: masked next token prediction, self-supervised contrastive learning, and missing span generation.

### Strengths
* The paper is very well written.
* The concept of a single model that combines the strengths of both masked language models and causal language models is interesting.

### Weaknesses
 * **Claims with Insufficient Experimental Results** My main concern is that the authors claim the model retains its original text generation capabilities, but they provide insufficient experimental results to support this. Maybe the authors can demonstrate some results on commonly used text generation tasks, e.g. natural language understanding (MMLU, BigBench), summarization.

* **Lack of Motivation** It's unclear whether the results reported in Section 4 reflect zero-shot performance or task-specific fine-tuning. I believe zero-shot performance would be more meaningful, as it would more convincingly demonstrate the effectiveness of a unified model in both semantic representation and text generation tasks. Otherwise, selecting the optimal attention mechanism and training objective for each specific task would be more practical.

### Questions
In the "Overall Loss" section of Appendix A, it's unclear why a two-stage training approach is necessary and why only two objectives are used in the first stage.

### Soundness
2

### Presentation
3

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
This paper introduces MAGNET, a model adaptation framework aimed at enhancing decoder-only large language models (LLMs) with representation learning and infilling capabilities, without compromising their generative performance. MAGNET employs a modified attention mechanism that integrates bidirectional and causal attention, supporting unified training across three self-supervised objectives: masked next token prediction, contrastive learning, and missing-span generation. Experimental results show that MAGNET surpasses state-of-the-art models in token-level and sentence-level representation tasks and excels in text infilling, making it a versatile approach for various natural language processing (NLP) tasks.

### Strengths
1. Proposes an innovative modification to the attention mechanism of LLMs, balancing bidirectional and causal attentions for improved versatility.
2. Demonstrates strong empirical results, showing MAGNET's effectiveness in multiple tasks, including representation learning and text infilling.
3. Provides a comprehensive analysis of MAGNET’s performance compared to state-of-the-art models, highlighting improvements in both quality and efficiency.

### Weaknesses
The main problem is the lack of experiments on text generation task. Text generation is the most important task since any NLP tasks can be transformed into the format of text generation, so it might be undesirable if the method sacrifices the text generation ability for text understanding ability. The paper only studied the text repetition problem of the method, but did not test it on widely-used benchmarks for LLMs evaluation. Furthermore, the evaluation of text infilling, while showing promising results, lacks a detailed analysis of the types of infilling the model excels at and where it struggles. For instance, does it perform better with short, localized infilling or longer, more contextually dependent spans? This granularity is crucial for understanding the practical applicability of the proposed method. The paper also does not explore the computational cost associated with the modified attention mechanism, which could be a significant factor in real-world deployment.

### Questions
Have you tried other method of using Llama features? For example, using pooled embeddings? The reason I ask is because decoder model is not explicitly trained for text understanding, it is unclear what is the best way to utilize them for text understanding task.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces MAGNET, a novel adaptation of decoder-only large language models (LLMs) designed to enhance both representation learning and text infilling capabilities while maintaining their original generative functions. Traditionally, unidirectional and bidirectional models are trained separately with distinct objectives—either generation or representation learning—thus missing the potential benefits of integrating these objectives. MAGNET addresses this gap by employing three self-supervised training objectives and introducing an attention mechanism that combines bidirectional and causal attention. This unified approach allows for simultaneous training across all objectives. The results demonstrate that LLMs adapted with MAGNET outperform state-of-the-art text encoders in token-level and sentence-level representation learning tasks. Additionally, MAGNET enhances the base LLM's ability to generate contextually appropriate text infillings by considering future context. Unlike other bidirectional models focused solely on representation learning, MAGNET-adapted LLMs retain the ability to perform open-ended text generation.

### Strengths
1. The proposed method enhances both representation learning and text infilling capabilities while preserving the original generation ability through a multi-level training objective.

2. Experimental results demonstrate that the proposed MAGNET outperforms traditional text encoders and decoders. Specifically, LLMs adapted with MAGNET surpass state-of-the-art text encoders in token-level and sentence-level representation learning tasks.

### Weaknesses
1. Several works have aimed to optimize pre-trained models for both generation and understanding tasks, such as XLNet, ERNIE, and GLM. The authors should provide a comparison with these approaches.

2. Contrastive loss has been widely employed in representation learning, as demonstrated by Gunel et al. (2022) and Wei et al. (2021). The authors should present a comprehensive related work section and compare relevant studies to highlight the effectiveness of their proposed approach.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduced MAGNET ((Modified Attention for Generation and Encoding of Text), a method to transform causal LLMs into text encoders and infilling language models with bidirectional context capturing ability. 
Three training objectives are introduced including: masked next token prediction, sentence level contrastive learning, and missing span generation,  to adapt the LLM to different tasks.
Experimental results shows a significant improvement in sequence labeling and text-filling tasks over the baseline
and a fair performance in open-ended text generation.

### Strengths
1. I think the idea to combine both unidirectional and bidirectional attention is new. This enhanced the representation learning and infilling capabilities of LLMs, while retaining their core generative functions.
2. I like the identification of token repetition problem in open-text generation, and the proposed method does have a positive impact in this direction.

### Weaknesses
1.  I am a little confused of the motivation. The author try to design a unified framework for text generation and text encoding,
by introducing some training objectives in bidirectional models (BERT, ERNIE) to LLMs.    The resulting model could do both tasks with a fair performance. But what is the purpose of the unified framework ? Could each task benefit from each other? I don't see much evidence in this paper.

2. The proposed three training objectives are not new: mask next token prediction is a variant task of LLMs, and I think MNTP is not a proper name, since the token predicted is actually not the "next" one, with the bidirectional setting. 
SSCL is widely studied in representation learning, such as <On learning universal representations across languages> ICLR21. 
And the MSG is a similar version of ERNIE (Enhanced Language Representation with Informative Entities).
And I suggest the author to explore more sophisticated loss function, rather than a simple linear combination of these three.
So in general I think the innovation of this paper is limited.

3. For the experiment part, I suggest the author to compare with stronger baseline on word-level and STS tasks like XLNet and StructBERT, since BERT and RoBERT(2019) is a little out-dated.

### Questions
1. How much does the adaptation of MAGNET hurt the text generation ability of LLMs ?  I think if the author claims to potentially unify text generation and text encoding within a single framework. This question should be carefully studied.

2. How does the proposed model compare with the SOTA performance in STS and word-level tasks?

### Soundness
3

### Presentation
3

### Contribution
2
