# Chunk-Distilled Language Modeling

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
We introduce Chunk-Distilled Language Modeling (CD-LM), an approach to text generation that addresses two challenges in current large language models (LLMs): the inefficiency of token-level generation, and the difficulty of adapting to new data and knowledge. Our method combines deep network-based LLMs with a straightforward retrieval module, which allows the generation of multi-token text chunks at a single decoding step. Our retrieval framework enables flexible construction of model- or domain-specific datastores, either leveraging the internal knowledge of existing models, or incorporating expert insights from human-annotated corpora. This adaptability allows for enhanced control over the language model's distribution without necessitating additional training. We present the CD-LM formulation along with performance metrics demonstrating its ability to improve language model performance and efficiency across a diverse set of downstream tasks. Code and data will be made publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a chunk-distilled language model (CD-LM), which uses a chunk proposal model (CPM) to retrieve fine-grained chunks and integrate them into the generation process. This approach offers two main advantages: (1) it distills knowledge from a larger model if the CPM datastore is encoded by that larger model, and (2) it saves decoding time by selecting chunks of multiple tokens as completions. The overall decoding algorithm in Section 3.2 is similar to speculative decoding.

The work is technically sound. For example, unlike previous retrieval-augmented generation (RAG) methods that directly search in a vector-based datastore, this model introduces an “entry token” and a trie-tree structure to reduce storage space. Additionally, in Section 5, they use dynamic decoding to marginalize the joint distribution $p(x, z)$, where $x$ represents the sequence and $z$ is the hidden state for accepting or rejecting the retrieved chunks.

### Strengths
The proposed CD-LM is well-designed and technically sound. The paper is well-written and easy to follow. The authors also conducted extensive experiments in the appendix, lending additional robustness to their findings.

### Weaknesses
While the algorithm in Section 3.2 appears reasonable, it cannot ensure the same properties as speculative decoding, namely that sampling $ x $ from $ p(x) $ is equivalent to sampling from $ q(x) $. In other words, sampling from the chunk proposal model may introduce a distribution shift, potentially reducing performance. The self-distillation experiments deepen this concern: as shown in Figure 6, saving about 20% of mean token time results in a significant performance drop across many LLMs, as measured by BLEURT.

In the knowledge distillation (KD) setting, building the datastore requires two full passes through the corpus, i.e., first with the larger model to select chunks and then with the base model to build the vector datastore. This time cost may be a concern.

### Questions
What happens if there are chunks with the same string but different contexts? I assume they would have different hidden representations. Are all of them stored?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new decoding technique called Chunk-Distilled Language Modeling (CD-LM). The technique could be interpreted as using a novel phrase-level retrieval mechanism to do phrase-level autocompletion, when confident, during decoding. Similar to speculative decoding, this speeds up decoding as a cheaper process has produced the next chunk of tokens, allowing for the base model to skip decoding steps. Unlike speculative decoding this can change the sampling model's output distribution: potentially for the better or to enable novel applications. Similar to retrieval augmentation, this technique improves grounding to an external datastore. Unlike, retrieval augmentation, this does not incur any cost by increasing the context window length.

To do this the authors come up with a novel mechanism to select high confidence / memorized phrases, via the observation that strong LLMs have very high probability for phrases that appear often in their pretraining. We can select these spans to insert in the chunk datastore, which is a collection of Tries. The leaves of the tries contain the chunk's contexts, presumably to update the KV cache with.  Alternatively, the authors also explore manually constructed datastores, that can open up new possibilities for grounding to external sources. 

During decoding, the decoded context so far, except for the last token, is encoded into a context vector, to be used to retrieve a relevant trie. The last token in the decoded sequence so far is used as the entry token. The first token of the trie has to match the entry token, to preserve fluency. The similarity of a context vector to a trie's context vector forms the acceptance probability for the decoding algorithm. If accepted, the decoding algorithm fills the sequence with the retrieved chunk, and skipping decoding for that chunk of tokens. The paper also introduces a novel method to compute perplexity given this phrase-level retrieval insertion mechanism.

The authors evaluate this decoding method in three settings: knowledge distillation (a bigger model is used to score and construct the chunk datastore), self distillation (the model itself is used to construct the chunk datastore -- e.g. turning into a sort of cache) , and expert distillation (hand constructed datastores from hand selected datasets, maybe representing new domains or tasks). The authors report improved decoding speeds, while maintaining quality and sometimes improving quality when appropriate, due to the new ability to ground to an external phrase-level datastore.

### Strengths
Originality:
- The authors introduce a new decoding paradigm that is quite novel, and has the ability to do fine-grained, phrase-level, grounding to an external source without incurring any extra context length like RAG does, all while potentially saving decoding time by skipping decoding steps. In essence, CD-LM introduces a phrase-level cache with fuzzy matching. This cache essentially gives the model the ability to autocomplete from the cache with some confidence threshold. The flexibility of being able to fill the cache with *anything* is a powerful paradigm, as the authors demonstrate very well in the paper.
- Even if there are short-comings in this paper, I believe this efficient, granular grounding technique will be of value to the community and will inspire future work. In the general LLM case, there are many ways to extend this work in the future to improve it or make it more practical for production. Even as-is, there are specific use cases that would likely benefit from such an approach.

Significance:
- For up to a strong 7B model, the authors demonstrate the ability of the method to save decoding time (10-20%, assuming the cached contexts cover the eval data), while maintaining the overall quality of the model.
- A novel way to ground to external source at the phrase level without training -- especially useful for private information retrieval. On private information retrieval, it outperforms RAG-based few-shot alternative. 
- A novel way to distill some performance from a larger model during only decoding, without any online decoding cost. Gets perplexity results similar to the base LM finetuned on the domain, without having to do training. 

Quality:
- This is a high quality paper, with many experimental results and detailed descriptions. The results give the reader confidence that within the constraints of their experimental setup, that the method works well. In 6.1, it is demonstrated that a sort of large-to-small model distillation does indeed happen when using a larger model to identify phrases for the cache. In 6.2 it is demonstrated that in self-distillation, the model does maintain a similar output distribution while improving decoding time by 10-20% and reducing forward passes by 20-40%. In 6.3 it is shown that the cache can be manually filled via various methods to inject new information into the model. 
- I do not have any issues with the claims made in this paper.

Clarity:
- The writing in this paper is excellent. It is easy to follow and introduces an appropriate amount of notation to make the understanding very clear. I did not find any grammatical or writing errors.
- The paper is well structured to explore various facets of the approach under different use cases.
- Methodology is very well documented, increasing reproducibility.

### Weaknesses
 1. The limitations of the experiments in this paper should be stated more clearly. Namely:

-  The contexts that are used to construct the chunk datastore / cache aligns well with the evaluation setting in every experiment in the paper. It is not possible to tell what the pitfalls of the retrieval mechanism might be when its pushed to its limit with very large collections of tries. For example in real applications, if CD-LM was used to cache the top 20% of queries with traffic (covering most topics essentially), would there be any quality interference for a tail query? How about as more items are cached and the retrieval space gets denser?
- Regarding this, unlike speculative decoding, CD-LM is essentially building a cache. The decoding time savings then is tied to how well the cache covers real evaluation traffic. In this paper it is always matching and so it represents only good-scenario results for a well built / updated cache.
- The chunk datastores considered in the experiments of this paper are quite small. It's unclear if the speed gains would hold if they were to grow in size, and at what extent the method would break down. Presumably when it stops fitting in host memory.
- There is a hidden cost in having to run LLM scoring to construct the datastore. To get sufficient chunk coverage on real traffic this may be very expensive. However, this mechanism could be used as a straightforward cache of phrases from previous live responses also, avoiding this offline cost.

2. Evaluations in this paper could represent the end model quality more directly. While authors use a variety of metrics that are fine: perplexity, ROUGE, Bleurt, and even human evaluated fluency, the results would be stronger with a more rigorous human evaluation of the overall quality of the text. This could perhaps be represented as a preference based SxS for Section 3.2 experiments.
- Similarly, for "injecting factual knowledge", this grounding capability would much benefit from an evaluation of factuality or response quality itself, rather than just relying on entity distributions. While fluency is important, mis-retrieved entities from context may hurt factuality, but this is not represented in the evaluations.

### Questions
Is there any analysis on how much the speed up from skipping tokens during decoding is offset by the trie lookup? How about for collections of tries?

What is the definition of f_theta that is used? How is the pooling from the context into the context vector defined? (Could not find it in the paper.)

If there is no coverage from the chunk datastore, do we expect a speed loss, due to the unnecessary NN search?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors of this paper propose a novel text generation method called CD-LM. By retrieving chunks, it addresses two challenges in the application process of large language models: low generation efficiency and difficulty in adapting to new data and knowledge. CD-LM combines a language model with a simple structured retrieval module, allowing the generation of multi-token text chunks in a single decoding time step. The retrieval framework can flexibly construct model- or domain-specific data stores and can utilize the internal knowledge of existing models (self-distill), the knowledge of stronger language models (knowledge distill), and human knowledge (Expert distill). Calibration of the generation distribution of existing language models can be achieved without additional training. Extensive experimental results show that CD-LM has advantages over baselines in terms of generation efficiency and quality.

### Strengths
1) Compared with traditional token-level generation methods, CD-LM can generate multiple consecutive chunks in a single decoding step, thereby significantly reducing the number of decoding steps required and reducing inference overhead. This is particularly important when dealing with a large number of long text generation tasks in the current large language model scenario.

2) The authors effectively extend the chunk-based generation method to three very important application scenarios: (1) By recalling and utilizing chunks constructed by stronger models, the generation distribution of weaker language models can be naturally corrected to improve their generation effects; (2) By recalling and utilizing chunks constructed by the model itself, inference acceleration can be achieved; (3) By recalling and utilizing chunk information in high-quality manually written data or even inaccessible private data, the ability of human experts can be utilized to improve the generation quality of language models.

3) The method in this paper is highly versatile. Without additional training, only by building a database and completing retrieval, plug-and-play implementation can improve generation quality and efficiency.

### Weaknesses
1) Novelty: CD-LM completely follows the Copy Generator framework proposed in the paper "Copy is all you need", and its novelty is slightly insufficient. However, as I mentioned in the Strengths part, they successfully extend the application scenarios of CoG. Therefore, I think the contribution of this paper is still good.

2) Lack of important reference: Nearest Neighbor Speculative Decoding for LLM Generation and Attribution: This paper also proposes applying chunk-level generation mechanisms to the speculative decoding process to improve decoding efficiency. The authors need to carefully clarify the main differences between the proposed method and this method in terms of inference speed and generation quality.

3) In experiments 6.1 and 6.2, the quality of generated text is mainly evaluated using automated evaluation metrics such as ppl and MAUVE. However, a large number of works have already verified that there is a large difference between such automated evaluation metrics and real human evaluations and cannot accurately reflect the quality of real text. It is noted that the author also introduced human evaluation in experiment 6.3. It is strange that human evaluation is not introduced in experiments 6.1 and 6.2. A feasible suggestion is to refer to existing works and use the LLM-as-a-judge method to achieve highly reliable automated evaluation. [1,2,3]

4) Including more QA and closed-set tasks in the experiments:  The evaluation of open-domain text generation is still too difficult. Perhaps it is easier to demonstrate the effectiveness of the proposed methods on more QA and closed-set tasks. I strongly suggest that the authors follow the experimental setting of the paper 'Nearest Neighbor Speculative Decoding for LLM Generation and Attribution'.

### Questions
1) A question corresponded to weakness 3): Why don't you include human evaluation in experiments 6.1 and 6.2?

2) There is a problem with the data highlighting in Table 1. The ppl index of KCD-LM in applications in medical and law scenarios is not better than that of the Base model. Does this indicate that using a chunk-based generation method may reduce the quality of generation? Would you please discuss possible reasons for this discrepancy and its implications for the effectiveness of CD-LM in different domains?

3) Regarding the metric PPL: Can you provide the detailed calculation method of PPL? In my understanding, since there is no fixed vocabulary for this kind of method, PPL cannot be calculated.

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
3

### Summary
The paper proposes an extension of chunk-level $k$NN-LM. In $k$NN-LM, context representations and the next token are stored as key-value pairs. This work uses context representations and the next phrase as key-value pairs, where the next phrase consists of an unspecified number of consecutive tokens. Chunks are primarily constructed using an off-the-shelf language model to evaluate token probabilities in an input sequence. A chunk is extracted when each token's probability exceeds a certain threshold. During generation, similar to $k$NN-LM, before generating the next token, the current step's hidden states are used to query the vector database to retrieve candidate chunks.  A small model is tuned to convert the similarity scores to acceptance probabilities for different LMs.
Overall, experimental results demonstrate better domain transfer capabilities compared to $k$NN-LM, but no significant improvement over domain fine-tuned LMs. It also brings inference speed up compared to base LMs.

### Strengths
The $k$NN-LM has notable limitations, such as retrieving only one token at each step, which results in low information density and slower inference speeds. This method extends kNN LM to chunk retrieval, mitigates these issues, and even accelerates inference speed.

### Weaknesses
1. Scalability Issues: A major issue with $k$NN-LM is storing huge amounts of key-value pairs, making scaling up difficult. This work is also evaluated on a small dataset, raising questions about the scalability of such methods.
2. Baseline Issue: The chosen baselines are not strong. Comparing with other models using chunk retrieval, such as https://arxiv.org/abs/2402.17532, would make the results more convincing. Meanwhile, $k$NN-LM achieves improvements by building key-value pairs using the pre-trained model itself, while KCD-LM relies on distillation from large models to improve small models, which may be unfair to other small models. There is also no comparison of performance based on self-distillation.
3. Practicality Issue: Distilling large models and storing key-value pairs come with costs, which may not be cheaper than fine-tuning a small model. However, according to Table 1, KCD-LM doesn't perform better than fine-tuned models, raising questions about cost-effectiveness.
4. Insufficient Machine Learning: The method primarily uses statistical approaches to mine chunks, with machine learning applied only in tuning chunk acceptance probability. As a machine learning conference, this work lacks insights in machine learning or representation learning.

### Questions
1. Section 5 is difficult to follow, are there any more simple words to describe the intuition behind it?
2. For the self-distillation part, why is there a comparison of inference speed but not of perplexity (PPL)?

### Soundness
3

### Presentation
2

### Contribution
2
