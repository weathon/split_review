# KBLaM: Knowledge Base augmented Language Model

- Decision: Accept
- Scores: 8, 5, 5, 8, 3

## Abstract
In this paper, we propose\KBLaMFull (\KBLaM), a new method for augmenting Large Language Models (LLMs) with external knowledge. \KBLaM works with a knowledge base (\KB) constructed from a corpus of documents, transforming each piece of knowledge in the \KB into continuous key-value vector pairs via pre-trained sentence encoders with linear adapters and integrating them into pre-trained LLMs via a specialized rectangular attention mechanism.
Unlike Retrieval-Augmented Generation, \KBLaM eliminates external retrieval modules, and unlike in-context learning, its computational overhead scales linearly with \KB size rather than quadratically. Our approach enables integrating a large \KB of more than 10K triples into an 8B pre-trained LLM of only 8K context window on one single A100 80GB GPU and allows for dynamic updates without model fine-tuning or retraining. 
Experiments demonstrate \KBLaM's effectiveness in various tasks, including question-answering and open-ended reasoning, while providing interpretable insights into its use of the augmented knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper focuses on the open-domain question-answering task and proposes the Knowledge Base Augmented Language Model (KBLaM) framework. Specifically, KBLaM augments a large language model (LLM) with an external knowledge base (KB) at inference time by first transforming the knowledge in the KB into continuous key-value vectors using pre-trained encoders, then integrating them into the LLM through a specifically designed rectangular attention mechanism. Unlike Retrieval-Augmented Generation (RAG), the proposed KBLaM does not require costly retrieval, and, unlike in-context learning (ICL), KBLaM achieves comparable performance with significantly lower computational overhead. Experiments on both a synthesized KB and a real KB dataset demonstrate the effectiveness of the proposed method.

### Strengths
1. The motivation of the paper is strong. It addresses scenarios where external knowledge is required for LLMs to solve tasks and explores how to integrate that information into LLMs efficiently and effectively. This paper identifies the limitations of current methods, including long in-context learning (ICL) and retrieval-augmented generation (RAG), and proposes a new solution that mitigates these limitations.
2. The proposed KBLaM, to my knowledge, is novel and offers the following advantages:
- It transforms external unstructured knowledge into a structured KB with knowledge triplets, which compresses lengthy context information and facilitates convenient integration of knowledge into LLMs.
- It encodes knowledge triplets as key-value vectors of uniform size, enabling straightforward incorporation into LLMs. The structured nature of the triplets also allows efficient retrieval of relevant knowledge within the KB.
- Each knowledge triplet can be encoded and incorporated into LLMs independently, providing greater scalability and lower complexity than ICL. This approach also offers flexibility for updating the knowledge within the KB.
- It also allows high interpretability via viewing the attention matrix.
3. Overall, this paper provides solid evidence through extensive experiments and ablation studies to demonstrate the effectiveness of the proposed method. The writing is also clear and easy to follow.

### Weaknesses
1. While this paper includes experiments with both synthetic and real-world KB datasets, the baselines are limited to only ICL and zero-shot approaches. Recent state-of-the-art methods, such as RAG-based and long-context models, are not included as baselines, making it difficult to assess the effectiveness of the proposed method relative to these approaches. Including results from these comparisons would strengthen the evaluation. Specifically, the paper lacks a direct comparison with RAG in terms of generation accuracy, latency, and memory usage, which are critical for understanding the practical trade-offs of KBLaM. Without these comparisons, it's hard to gauge the true advantage of KBLaM over existing methods.
2. The generalization of KBLaM is less well-known. While it has been tested on an OOD dataset, other commonly used QA datasets have not been explored, such as [1][2][3][4]. Please see the questions below. Furthermore, the paper does not address the practical challenges of adapting KBLaM to datasets that do not inherently provide knowledge in the form of triples. The process of converting existing QA datasets into a suitable KB format for KBLaM is non-trivial and requires further investigation, especially given that the performance of KBLaM is highly dependent on the quality and structure of the KB.

### Questions
1. In Figure 6(a), why are the in-context learning results (orange line) missing from the Enron dataset?
2. I’m interested in the generalization of the proposed method. For other QA datasets and benchmarks commonly used by the community, such as [1][2][3][4], is it possible to extend KBLaM to address these problems? How can a KB be constructed for them? Do you need to build a KB for each dataset? What is the size (number of knowledge triplets) of the KB that is sufficient or suitable to solve these problems?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents KBLAM, a novel approach to augment Large Language Models (LLMs) with external knowledge from a structured knowledge base (KB). The method utilizes pre-trained sentence encoders with linear adapters to transform knowledge into continuous key-value vector pairs, which are then integrated into the LLM via a specialized rectangular attention mechanism. This approach brings the following benefits: improvements in computational efficiency, dynamic knowledge updates, and interpretability compared to existing methods such as Retrieval-Augmented Generation (RAG) and in-context learning.

### Strengths
1. The KBLAM method offers a significant advantage in memory efficiency by compressing the kv cache, which enables the model to scale to longer contexts.

2. KBLAM eliminates the need for separate retrieval steps, simplifying the architecture and making the model more efficient compared to RAG.

3. KBLAM allows for runtime KB updates without the need to re-pretrain the model, providing a level of flexibility in deploying LLMs. Additionally, the ability to refuse to answer when the required information is not present in the KB adds a layer of reliability, an essential trait for LLMs used in real-world applications.

4. The paper exhibits a robust methodology with meticulous experimentation. It particularly emphasizes KBLAM’s scalability, efficiency, and interpretability. The use of a rectangular attention mechanism enables the model to scale linearly with the size of the KB. Furthermore, the authors provide comprehensive ablation studies to substantiate their design choices.

### Weaknesses
1. I think that the most relevant baseline for comparison with the proposed method should be prompt caching (e.g., as described in the following link). This approach converts the knowledge base into a key-value cache for subsequent use. Compared to this method, I think the advantages of the KBLAM method maybe diminished. For instance: a) it requires instruction tuning; b) the accuracy of retrieval might be substantially lower compared to prompt caching; c) the key-value cache generated by a pretrained encoder is inherently inferior to that obtained from LLMs.
the prompt caching method:
a) https://platform.openai.com/docs/guides/prompt-caching
b) https://ai.google.dev/gemini-api/docs/caching
c) https://proceedings.mlsys.org/paper_files/paper/2024/file/a66caa1703fe34705a4368c3014c1966-Paper-Conference.pdf


2. In the KBLAM method, there is no relative order among different triples, which means there are no position embeddings. In scenarios involving extremely long contexts, this could render the attention mechanism ineffective (the over-smoothing phenomenon), greatly reducing the precision of retrieval. Although the authors propose an attention score scaling method to mitigate this, it would be beneficial to conduct some analytical experiments, such as a needle-in-a-haystack experiment (https://github.com/gkamradt/LLMTest_NeedleInAHaystack), for further analysis.

3. The KBLAM method requires KB instruction tuning. Does this imply freezing the pretrained LLM and only training the adapters? According to the paper, PEFT methods were not used. Consequently, updating the KB kv cache without re-training the LLMs might result in a performance decline, potentially compromising the plug-and-play nature of the method.

4. The performance of the adapter is highly dependent on the data used for instruction tuning. A non-homogeneous kv cache encoder can lead to a significant drop in performance. Therefore, in ablation experiments comparing the pretrained encoder from other sources, it would be best to compare it with the kv cache generated by the prompt caching method, i.e. the LLM itself. This would help readers better understand the performance of the proposed method.

### Questions
1. Given that the KBLAM method inevitably leads to information loss (due to the compression of the kv cache and over-smoothing in scenarios with large kb sizes), have the authors considered incorporating a retrieval module to mitigate this issue? Additionally, it might be beneficial to use retrieval scores as a position bias (for example, the kv cache closer to the prompt corresponds to a higher relevance of the triple, which aligns with the inherent characteristics of the attention mechanism and should effectively enhance the method's performance).

2. Have the authors experimented with making the method more modular, such as by using PEFT (Parameter-Efficient Fine-Tuning) methods and training only the adapters part? If so, what were the results of this approach?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new regime called KBLaM to integrate the entire KB into LLM with a complexity that grows linearly. The paper primarily introduces Rectangular Attention to achieve this. Experimental data shows that the method can be scaled to handle data with up to 10K triples.

### Strengths
-	The paper proposes a new method for integrating KB into LLM, and theoretically, this method is one order of magnitude more efficient than the ICL method.
-	It is a neat and interesting way to map each triple into a fixed-length key-value vector pair
-	The main body of the paper is written well, and the explanations for each step of the calculation are precise

### Weaknesses
 - The experimental comparison setup is not well-designed:
		
	No comparisons in the first experiment. How is the retrieval accuracy compares to that of BM25?
	
	In the last two experiments, although the authors mentioned that ICL encountered memory constraints, it also resulted in fewer data points.
- The conclusion of the experiment is relatively ordinary. In the last two experiments, the author claims that KBLaM can reason about knowledge and KBLaM knows when it cannot answer a question. However, these two features seem to be the result of the newly proposed structure working in conjunction with the original parameters and structure in LLMs.
- The novelty of this paper is limited. As the author points out in the appendix, the overall approach is very close to structured prompting[1] and structured attention[2]. If each triple is considered as a demonstration, could the method proposed in this article be seen as transferring structured prompting from text to triples? Additionally, although the author cites work related to structured attention in the appendix, I believe the degree of relevance to these methods is much greater than that to the work on the key-value (KV) cache mechanism and multi-modal language models, and should be cited in the main body.
[1]Hao, Yaru, et al. "Structured prompting: Scaling in-context learning to 1,000 examples." arXiv preprint arXiv:2212.06713 (2022).
[2]Cai, Tianle, et al. "Scaling In-Context Demonstrations with Structured Attention." arXiv preprint arXiv:2307.02690 (2023).
- There are some repetitive words in the article:
	
	There is no need to use a large section in Chapter 3 background to introduce Self-attention layer.
	
	Image label and paper content overlap. For example, “uses the attention score at the 15th layer, averaged over all attention heads, as a classification score for each triple and measures the top-1 and top-5 accuracy” in Fig5 overlaps with the content introduced in the first experiment.
- The accuracy of ICL on the Enron dataset does not seem to be demonstrated in Fig6(a).

### Questions
-	As seen in Fig6, within the range where the ICL method can operate, i.e., less than 200 triples, the ICL method is generally not inferior to KBLaM in terms of accuracy. Can these gaps be narrowed?
-	How does this method compare to retrieval + ICL?
-	How does KBLaM perform on more popular datasets and different types of problems?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors implement a scheme that encodes Knowledge Base triplets into Key+Value pairs via a pretrained embedding encoder.  The information from the triplets can then be continually 'looked up' by a pretrained local LLM through the training of adapter matrices that (essentially) convert the local LLM representations into embedding space.  Experiments are performed to show that this is effective, including the training of the adapter matrices using synthetic data - which points to greater applicability of the method.

### Strengths
The paper presents an interesting new KB embedding lookup technique, with some small-scale experiments.  Also included was some visualisation of the attention across the KB - which was particularly striking for the multistep case (KB items 4+6).

Oeverall, it seems like the ideas in the paper are of general interest, even though they may not be fully fleshed out as presented here.  Even if "KBLaM" isn't the end-point of this line of research, this paper points towards a line of research that could be quite fruitful : Loosely, that weight matrix adapters can be trained to reverse the embedding process using synthetic data.

It also seems that the top-k choices among the Keys are all that are necessary (particularly since the facts are likely stand-alone, rather than mutually reliant), which could mean that much cheaper approximate search could be used to select out relevant entries before doing a full dot-product.

### Weaknesses
At several points, the 'linear rather than quadratic scaling' of the method is emphasised.  This seems a weak point, since the size of the tuples $M$ already exceeds the context length $N$, so $MN>N^2$ in this regime (as obliquely mentioned in L284).

The constant $C$ introduced in Eqn 11 feels like something that should have a more principled origin.

small edit: L103 "training samples is not of interests." -> "training samples is not important."

Looking at the triplet examples (in the Appendix), and the test questions, it seems that there is an extremely high character-overlap between the name-property text and the Questions being asked.  To what extent do the queries have to 'hit' the keys exactly (for instance : Asking about 'Maggie Thatcher' rather than 'Margaret Thatcher')?  Is there an identifiable effect whereby inexact matches get honed-in on subsequent layers/tokens (for instance)?

### Questions
Looking at the triplet examples (in the Appendix), and the test questions, it seems that there is an extremely high character-overlap between the name-property text and the Questions being asked.  To what extent do the queries have to 'hit' the keys exactly (for instance : Asking about 'Maggie Thatcher' rather than 'Margaret Thatcher')?  Is there an identifiable effect whereby inexact matches get honed-in on subsequent layers/tokens (for instance)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new method, KBLaM, for enhancing language models with external knowledge. The main idea can be interpreted as an information compression method of in-context learning (directly putting the entire external corpus in context). Specifically, KBLaM first transforms each piece of knowledge in the knowledge base into continuous key-value vector pairs using a pre-trained sentence encoder. These vector pairs are then mapped into the language model's hidden space via linear adapters. By employing a rectangular attention mechanism, KBLaM enables the integration of external knowledge into the model. Experimental results show that KBLaM achieves performance comparable to in-context learning while offering significantly better scalability.

### Strengths
1. Compared to in-context learning, KBLAM introduces linear attention computation scaling relative to the size of the knowledge base (KB). Additionally, it preserves the key advantage of in-context learning by enabling dynamic updates to the knowledge without requiring model fine-tuning.

2. The proposed method also enhances interpretability by potentially offering insights into how the model leverages knowledge through the attention matrix.

3. This paper is clearly-written and easy to follow.

### Weaknesses
### 1. Limitations of the method:
- The proposed method encodes each piece of knowledge in the knowledge base separately, without leveraging the graph structure or interconnections between knowledge entities. This could limit the method's ability to capture richer, contextual relationships within the knowledge base.
- The method introduces significant computational overhead by requiring fine-tuning of multiple adapters: a key adapter ($\in \mathbb{R}^{D \times P}$), a value adapter ($\in \mathbb{R}^{D \times P}$), and a query transformation ($\in \mathbb{R}^{D \times D}$) in each transformer layer. For example, using the experimental setup described in the paper, where the hidden sizes of Llama3-8B and the pre-trained OpenAI ada-002 encoder are 4096 and 1536, respectively, the total number of trainable parameters amounts to around **1 billion**—roughly 1/8 of the base model. Compared to in-context learning (training-free), this method represents a substantial increase in resource requirements.
- The performance of the method appears to be heavily dependent on the choice of pre-trained encoder. As shown in Figure 7, using a weaker encoder can lead to a significant drop in performance, in some cases falling below that of the zero-shot baseline.

###  2. Limitations of the experiments:
- The experiments are only conducted on a single base LLM (Llama3-8B). Testing on a wider range of model architectures and sizes would help assess the generalizability of the proposed method.
- The evaluation is based on a small number of datasets, specifically a synthetic knowledge base and Enron. A broader evaluation on more diverse and real-world datasets would provide stronger evidence of the method's effectiveness.
- Missing comparison with Retrieval Augmentation Generation (RAG).

### Questions
1. Could you elaborate on the design rationale behind Eq. (9)? Specifically, it seems that the output of each attention layer, $\Tilde{\bf{y}}_n^l$, could alternatively be derived by aggregating the information from both $\Tilde{\bf{v}}_m^l$ and $\bf{v}_i^l$ independently. What specific advantages does the chosen design in Eq. (9) offer over this potential alternative formulation?

2. Could you provide insights on how another competitive baseline, such as RAG, might perform under your experimental settings? Additionally, it would be interesting to know if KBLaM could offer reduced memory overhead compared to RAG.

3. How would KBLaM perform in more challenging KBQA scenarios, such as multi-hop reasoning tasks? Additionally, can KBLaM maintain its advantage over in-context learning in such complex environments?

### Soundness
2

### Presentation
3

### Contribution
2
