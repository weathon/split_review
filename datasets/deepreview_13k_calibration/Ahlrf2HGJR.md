# Repetition Improves Language Model Embeddings

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Recent approaches to improving the extraction of text embeddings from autoregressive large language models (LLMs) have largely focused on improvements to data, backbone pretrained language models, or improving task-differentiation via instructions. In this work, we address an architectural limitation of autoregressive models: token embeddings cannot contain information from tokens that appear later in the input. To address this limitation, we propose a simple approach, ``echo embeddings,'' in which we repeat the input twice in context and extract embeddings from the second occurrence. We show that echo embeddings of early tokens can encode information about later tokens, allowing us to maximally leverage high-quality LLMs for embeddings. On the MTEB leaderboard, echo embeddings improve over classical embeddings by over $9\%$ zero-shot and by around $0.7\%$ when fine-tuned. Echo embeddings with a Mistral-7B model achieve state-of-the-art compared to prior open source models that do not leverage synthetic fine-tuning data.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a very easy method to improve the language model embedding. They introduce echo embedding by repeating the input and extracting embedding from the repeated tokens. The experiment show that the echo embedding improve over classical LM embeddings by over 5% in zero-shot settings. Echo embeddings are also compatible with supervised fine-tuning, even with an identical compute during training and inference.

### Strengths
1. The echo embedding method is both easy and effective. While previous studies have demonstrated that repetition is beneficial for reasoning tasks and recurrent language models, this paper shows that it is also effective for causal language model embedding.
2. The paper is clearly written and easy to understand.
3. The use of a simple synthetic dataset to analyze why causal attention might inhibit embeddings from reliably capturing information across the entire context is interesting.

### Weaknesses
The echo embedding method will inevitably double the input length. Although experiments show that reducing the input length and training steps by half still yields good results, this approach may not be suitable in cases where important information is located in the latter half of the input context. For example, the S2 (Early redundant; late discriminatory) cases described in Section 3.1 of the paper. Additionally, because self-attention has a computational complexity of O(n^2) with respect to input length, training for only half as many steps may not necessarily equate to the training cost of the original baseline. The paper does not fully explore the trade-offs between training steps, input length, and the resulting embedding quality. Specifically, the paper only considers halving the training steps when doubling the input length, but does not explore the impact of keeping the number of training steps constant when doubling the input length, which would result in a significantly higher training cost. This is a crucial point that needs further investigation to fully understand the practical implications of the proposed method.

### Questions
Have you tried tripling or increasing the input length even further? I'm curious to know if this would result in any additional improvements.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a simple strategy to extract high-quality sentence representation from causal LMs, i.e., repeating the input and extracting embeddings from the repeated tokens. They argue that their method requires neither bi-directional attention nor supervised fine-tuning. They first conduct experiments on a toy dataset, where they can control the information type of part of the inputs. Then, they clearly show the limitation of classical embeddings (mean pooling or last token) and the advantage of their method. Experiments on the MTEB dataset show that their method has advantages over classical approaches and recent alternatives. However, I hold some concerns with the experiment setting, see weakness parts. Overall, I find the paper's idea interesting, but the practical aspects need further discussion.

### Strengths
1. I appreciate the toy experiment, which clearly supports their claim about the limitation of classical embeddings and the advantages of echo embeddings.

2. The results on the MTEB dataset show clear improvements over classical embedding extraction settings, achieving comparable results with LLM2Vec, which needs backbone changes and unsupervised finetuning.

3. The method itself is very simple and insightful, requiring no changes to the backbone.

### Weaknesses
1. The setting of the most relevant baseline, promptEOL, does not seem to exactly align with that in the original paper. The results of PromptEOL appear significantly different from those reported in the original paper. In the original study, PromptEOL achieved an average score of 72.10 across seven STS tasks using the OPT-6.7B model. However, in your paper, PromptEOL only obtains an average of 67.14 on ten STS tasks. I didn't expect such a big performance discrepancy. Is this because of the three additional STS tasks in the evaluation?

2. I found the prompt used in this paper differs from that in the original paper. How about the performance of promptEOL that uses exactly the same prompt?  


3. I found the "halve input" setting weird to me. For a prompt like "rewrite S, rewritten S'", does it mean halving both S and S' to extract embedding? If so, I will read the results as the "nature"/"issue" of the problem itself, rather than an advantage of echo embedding. E.g., how about also halving the input for PromptEOL?

### Questions
See weaknesses

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
Causal attention in autoregressive models limits the use of LLMs in text embedding tasks because tokens in a sequence cannot reference subsequent tokens. This paper introduces an "echo embedding" method to transform autoregressive language models into high-quality text embedding models without altering the causal attention architecture or requiring fine-tuning. By repeating the input sequence twice and extracting embeddings from the second occurrence, the tokens can attend to the full input from the first occurrence. Experimental results demonstrate that the proposed method can nearly match the performance of bi-directional and fine-tuned models using zero-shot embeddings.

### Strengths
1. The proposed method is simple by repeating the input sentence twice to get the text embeddings.

2. The toy example design is interesting.

3. The results of zero-shot settings is impressive.

### Weaknesses
1. The motivation regarding causal attention seems questionable. Although LLM2Vec utilizes causal attention, it still performs exceptionally well in extracting text embeddings.

2. After fine-tuning the model, the performance gap between "echo embedding" and other models is minor. However, "echo embedding" requires the input sentence to be repeated twice, increasing computational costs. This limitation confines the proposed method to zero-shot settings only.

3. At least one illustrative example should be included in the main article, rather than relegating all examples to the appendix.

4. Typo: line 122, "encode can" -> "can encode"
line 283: "embedding 4" -> "embedding in Table 4"

### Questions
1. I am curious about the influence of number of repetition times, which is not important though.

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
The paper presents a simple and effective method called "echo embeddings" that enhances text embeddings generated by autoregressive language models without finetuning. This technique involves prompting the model with the input twice and extracting embeddings from the repeated tokens. The authors demonstrate that echo embeddings significantly improve the quality of embeddings in zero-shot settings, achieving nearly the same performance as bidirectionally-converted LMs that undergo additional masked-language modeling training. Echo embeddings are also shown to be compatible with supervised fine-tuning, matching or outperforming the bidirectionally-converted LMs in direct comparisons.

### Strengths
- The paper introduces a novel and straightforward method to enhance autoregressive embeddings without the need for architectural changes or additional fine-tuning. This simplicity is a significant advantage, making the approach easily applicable to existing models. The results indicate that echo embeddings provide a substantial performance boost in zero-shot settings compared to classical embeddings. 

- Echo embeddings can be applied in both zero-shot and fine-tuned settings, demonstrating flexibility and robustness across different tasks and benchmarks. The technique also shows consistent results across multiple models and scales. While repetition doubles the compute cost, the paper provides compute-matched results showing that echo embeddings still outperform classical embeddings even when adjusting for compute. This suggests that the method is efficient and scalable.

- The paper presents extensive experiments on a variety of datasets and tasks such as classification, clustering, reranking, retrieval, and sentence similarity. This comprehensive evaluation supports the validity and generalizability of the proposed method.

### Weaknesses
While the method shows strong performance across various benchmarks, it is possible that the specific tasks and datasets used in the evaluation may favor the proposed approach. Further validation on different types of data and tasks would strengthen the claim of general applicability. And also, does this technique helps some generation tasks? For example, if echoes some important information in the prompt, will it boost the performance on downstream generation tasks?

### Questions
- See above, performance on generation tasks.

- Can you provide more details on the impact of different prompts on the performance of echo embeddings? Have you explored variations in the prompt structure, and how sensitive are the results to these variations?

- Have you tested the echo embeddings method on a wider range of autoregressive models beyond those reported in the paper? How does the method perform on models with different architectures and training paradigms? For example, non-gpt models.

### Soundness
3

### Presentation
3

### Contribution
3
