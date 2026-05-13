# Correlation and Navigation in the Vocabulary Key Representation Space of Language Models

- Decision: Accept
- Scores: 5, 5, 8, 8

## Abstract
Language model (LM) decoding is based on the next-token prediction (NTP) probability distribution.
For neural LMs (e.g., Transformer-based), NTP distribution is essentially a softmax-regularized dot product between an encoded input context (\emph{query}) and fixed vocabulary representations (\emph{keys}).
In this paper, we study the effect of the key distribution on the NTP distribution, with a focus on whether the similarity between keys will trigger spurious correlations in NTP. 
Through knowledge-probing tasks, we show that in the NTP distribution, the few top-ranked tokens are typically accurate.
However, the middle-ranked prediction is highly biased towards the tokens that are distributionally (not necessarily semantically) similar to these top ones.
For instance, if ``P'' is predicted as the top-$1$ token, ``A''-``Z'' will all be ranked high in NTP, no matter whether they can lead to correct decoding results. 
This hurts the sampling diversity and makes the sampling of correct, long-tail results hopeless and noisy.
We attempt to alleviate this issue via a novel in-context method that iteratively pushes the query representation away from explored regions.
Specifically, we include the explored decoding results in the context and prompt the LM to generate something else, which encourages the LM to produce a query representation that has small dot products with explored keys.
Experiments on knowledge-probing tasks show that our method leads to efficient navigation away from explored keys to correct new keys.
We further extend our method to open-ended and chain-of-thought (for reasoning) generation.
Experiment results show that ICN contributes to better generation diversity and improved self-consistency voting performance. 
Finally, we discuss potential training issues caused by the fixed key space together with the challenges and possible ways to address them in future research.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the impact of word-embeddings parameters in the last layer (also referred to as un-embedding parameters, referred to as "keys" in this work) on spurious correlations during decoding via language models. Specifically, this paper finds that top-k items in response to a prompt tend to be close together (low cosine distance) and hence a lot of plausible and correct responses which might have a higher cosine distance from the top-k items are ranked lower in LM predictions. This impact is shown on knowledge probing tasks which shows that a significant number of correct answers lie outside of the cluster formed by top few items. To ameliorate this issue, the paper proposes a simple prompt-based fix called ICN, which appends the top-few items to the query in a listed form to encourage the language model to suggest "under-explored" items. This approach is shown to improve accuracy on knowledge probing. This approach is also used for open-ended generation to stimulate diversity among the responses. When this approach is used for CoT consistency decoding, it tends to improve upon standard CoT sampling baseline slightly. Finally, this paper also provides evidence that fine-tuning doesn't change the unembedding layer much and is still susceptible to the same spurious correlations as pre-fintuned models.

### Strengths
-- This paper is well-motivated and identifies a focused problem in natural language generation. However, as I note in the weaknesses section, it misses out on discussion about other work investigating the inadequacy of softmax for similar reasons this paper explores.

-- The effects shown are significant. The knowledge probing experiments show concerning effects of the spurious correlations introduced due to the unembedding parameters.

-- The proposed fix, while simple seems to be effective at ameliorating the issue.

-- The proposed approach also seems to improve diversity of generated text.

### Weaknesses
 --  The paper should improve the presentation. I am unsure about the exact prompt behind ICN while I understand it at a high level. Moreover, I it is also difficult to understand how this prompting scheme was explicitly adapted for open-ended generation and CoT. Clear examples would help. Also, the baselines should be clearly explained in greater detail.

-- The proposed ICN scheme also seems expensive to implement as a general method. The results indicate that one needs a large number of queries and a large number of keys to work.

-- My biggest concern is that this work ignores a lot of prior work that precisely characterizes the problem of spurious correlations due to the unembedding parameters. [1] introduces the popular concept of softmax bottleneck which shows rank-deficient behavior of the softmax function during decoding which is directly linked to the unembedding parameters. [2] investigates exactly the problem this paper studies. [3] relatedly shows that some words might never be chosen as argmax even if correct because of the manifold of the unembedding parameters.

-- It is not discussed/analyzed in detail what makes ICN work. The prompt as designed could have worked against the desires as well in which it explores the nearest items more eagerly. I don't come away with a good understanding of why this method of prompting is effective over other potential prompts.

### Questions
Please address the concerns above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper present an interesting fact that the vocabulary representations (keys) has spurious correlations with the generation process. More specifically, when some token gets a higher generation probability, the tokens that are closer to this token will also have higher generation probability, even though they may not lead to correct generation results.

The paper also present a simple solution, which includes the explored decoding results in the context and prompt the LLM to generate differently. Experiments on knowledge-probing tasks show that the method leads to exploration away from the explored keys.

### Strengths
The paper use clustering and visualization to show that the similarities in keys did resulting in generation bias.

The proposed method, ICN, could increase the generation probability for tokens that are different from previous explored keys.

### Weaknesses
I dont think it is reasonable to ask the LLM to be correct for the top 100 candidate. At least it has already shown strong performance on the top 10 or maybe to the top 20 candidate.

I think ask the LLMs to generate different tokens is an practical approach, but it will also decreases the generation probability for correct answers that shows the same tokens with those explored ones.

### Questions
Since the key representations are learned during large scale pretraining, it is also possible that the generation probability behind these keys still matches the knowledge in the world. As shown in Figure 2, there are quite a lot of correct key around the query. It is not possible, in this case, to have all the correct answer appears around the query anyway.

I am wondering what prompt is used for rephrasing and reranking, respectively. I am wondering why rephrasing does not bring to much difference.

I am also curious about how the method related to the contrastive decoding approach.

[Contrastive Decoding: Open-ended Text Generation as Optimization. ACL 2023]

### Soundness
2

### Presentation
3

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
The paper discover a fundamental issue that the next-token prediction is affected by correlations within the vocabulary key space. By analyzing key representations in transformer LMs, the authors observe that context-agnostic similarities between certain keys can lead to spurious correlations, such as the capital alphabets are predicted with high probabilities together without regarding their real relevance. These correlations cause certain “middle-ranked” tokens, often unrelated semantically to the top-ranked token, to be underestimated in ranking. This issue introduces bias and reduces sampling diversity in open-ended or exploratory text generation. The author further proposed In-Context Navigation (ICN) to incorporate the previous generated outputs into the input context to iteratively guide the LM away from explored key regions.

### Strengths
- Novel discovery on the the issue of very fundamental design of transformer LMs. It's valuable to facilitate the understanding of LM decoding biases
- Novelty in proposed approach ICN to mitigate such bias.
- The paper shows strong empirical evidence through diverse tasks, including knowledge probing and chain-of-thought generation, to validate ICN’s effectiveness.
- The author proposed some potential direction to solve this issue in the LM pretraining stage, which can be positive contributing to the community.

### Weaknesses
 - Lack of exploration on larger models: the paper only discuss LLaMA-3-8B in the experiments. However, I expect that a larger model with higher-dimensional embedding space can more or less mitigate such issue. When the dimension is large enough, the query embedding can be similar to different key embeddings in many different sub-spaces, so as to reduce the problem of similar key vectors always get activated together. It will be good to show more results in the larger models like LLaMA-3-70B.
- ICN increase the context length. When making the model generating longer responses (e.g. CoT) while considering previous generated outputs, ICN can largely increase the context length and inference cost.

### Questions
- I wonder why a regular decoding process cannot achieve the same effects of ICN did? In regular decoding, the previous generated outputs are natively placed in the input context. If we put always put the generated outputs in the context, we should be able to achieve the same thing as ICN did, right?
- Is there any analysis of how ICN can increase the context length and inference cost?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Following the terminology in the paper, let us denote the encoded input hidden sate representation at some position (the one that is multiplied with the vocabulary matrix to get the probability distribution at that position) as "query", and let us denote the vectors in the vocabulary matrix (each correspondent to some token in the vocabulary) as "keys". 

The paper explores the confounding factor that is brought about by the input-context-insensitive similarity of keys in their vector space in next token predictions (NTPs). Particularly, in the context where there are multiple good answers for an input prompt, many of the good answers are not as highly ranked, because input-irrelevant vocabulary keys can get highly ranked because they are close (in the non-contextual vocabulary embedding space) to some of the top ranked keys that are actually relevant to the input. Essentially, even if the top ranked keys are appropriate, they being scored high leads to a side effect of inappropriate (unrelated to input) keys to be also ranked moderately high only because they are close to the top keys in the vocabulary embedding space (which is insensitive to input context by design).

1. The paper provides empirical analysis of this phenomenon by probing LLMs. 
2. The paper explores several ways to mitigate this issue - example by reranking/rephrasing and the main proposed method ICN (in-context navigation). ICN - employees iterative prompting to sequentially generate multiple good answer candidates (instead of just multi-sampling), where the model is prompted explicitly to generate something other than prior generated answers -- thus allowing to focus on different vocabulary key clusters unrelated to the prior answer-clusters. 
3. The paper presents the utility of ICN as a strategy in different contexts - like incorporating it with self-consistency for mathematical reasoning or investigating open-ended generation.

### Strengths
1. Provides a reasonable analysis of an interesting phenomenon in the context of LLMs. Devises reasonable ways to quantify it. 
1. Proposes a simple method (ICN) to mitigate the identified issue, and shows its utility empirically in a wide set of experimental contexts. 
1. In the end, suggestions some interesting ideas to potentially solve this issue in a more principled manner (contextual layer for vocabulary or re-ranking). 
1. The paper is well written (lower presentation score because of weakness in literature review)

### Weaknesses
1. Similar analyses have been already done. If I understand correctly, this issue is related to the well-known softmax-bottleneck phenomenon. And there are a bunch of related works on that - especially see [1]. While I think the current paper has some virtues over some of those prior works (like investigation in terms of LLMs, exploration of a tuning-free method ICN to mitigate it, and potentially better empirical measure by cluster divisions and such of this issue) - the past related works should be still acknowledged and used for contextualization.  

2. If I am not missing anything, most of the analyses and investigation is based on a single LLM (Llama 3 8B instruct). While olmo results seem to be presented in the appendix, but ICN-related experiments seem to be missing for olmo. So the universality of the utility of ICN is still a question.

3. There could be more discussion about how much does this issue have anything to do with NTP in particular. Seems like a general issue -- that can apply to other language modeling settings (like Masked language modeling).

4. The technical details hyperparameters and the prompt settings are not crystal clear to me.

### Questions
1. Line 256-257 is phrased in a confusing manner (and probably wrongly). Instead of "specifically, from
top-N (N = 100) to top-(K + 1) (K = 10)", you should probably say something like "specifically, from
all tokens in top-N (N = 100) but not in top-K (K = 10)".

1. I think the equation in 261 defining InTop is wrong. It should have $j \leq K$ not $K \leq j$. j is supposed to be one of the top-k tokens (thus $\leq K$) based on the text description.  

1. Related to the last weakness: I think it would be good to more explicitly show what prompt template is used for ICN in different contexts and maybe some concrete examples about how iteratively the input prompt is being changed for different cases (mathematical reasoning, open ended generation, knowledge probing). I saw the case studies in the appendix but they seem to focus only on the output, or just the original input and output (rather than the processed prompt input with all the templates and such). And Table 16 doesn't seem to show anything related to ICN.

1. Still somewhat related to the last weakness: I am a bit confused by your definition of COT prompt in Table 16. Normally, COT prompt is supposed to be add something like  "Let's think step by step" to the beginning of the assistant response. Your COT prompt seems to be just about generating multiple answers. Moreover, self-consistency normally used distinct samples, whereas this COT prompt seems to be designed to generate multiple answer procedures in a single sample.

1. What exactly is Top in Table 6 or 5? Do you mean greedy decoding? If so I am not sure how that can be used to generate different sequences for diversity measures or self-consistency voting.

### Soundness
3

### Presentation
3

### Contribution
3
