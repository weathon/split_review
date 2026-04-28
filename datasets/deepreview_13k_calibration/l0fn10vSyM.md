# Semi-Parametric Retrieval via Binary Bag-of-Tokens Index

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 8, 6

## Abstract
The landscape of information retrieval has broadened from search services to a critical component in various advanced applications, where indexing efficiency, cost-effectiveness, and freshness are increasingly important yet remain less explored.
To address these demands, we introduce \textbf{S}emi-parametric \textbf{V}ocabulary \textbf{D}isentangled \textbf{R}etrieval (\ours). 
\ours is a novel semi-parametric retrieval framework that supports two types of indexes: an embedding-based index for high effectiveness, akin to existing neural retrieval methods; and a binary token index that allows for quick and cost-effective setup, resembling traditional term-based retrieval.
In our evaluation on three open-domain question answering benchmarks with the entire Wikipedia as the retrieval corpus, \ours~consistently demonstrates superiority.
It achieves a 3\% higher top-1 retrieval accuracy compared to the dense retriever DPR when using an embedding-based index and an 9\% higher top-1 accuracy compared to BM25 when using a binary token index.
Specifically, the adoption of a binary token index reduces index preparation time from 30 GPU hours to just 2 CPU hours and storage size from 31 GB to 2 GB, achieving a 90\% reduction compared to an embedding-based index

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper main contribution is a retrieval model where documents are represented by the presence (boolean) of tokens (i.e. a binary bag of tokens). The advantage of such an approach is that the index has to be computed just once (it does not depend on parameters). However, the precision of such a model being low, the authors show that it can be successfully trained with a dense model (used as a second-stage ranker) - and combined with it at inference time. Experiments are conducted on the Wiki21m and BEIR benchmarks and retrieval latency is evaluated - showing that this approach offers a good compromise between effectiveness and efficiency.

### Strengths
The main strength of the paper lies in the static representation of documents. As far as I know, this is the first model that relies on a simple index structure, that of representing the documents as a binary bag-of-token. This allows for potentially fast retrieval (although this can be debated, see weaknesses) of potential candidates that have then to be re-ranked.

### Weaknesses
One of the main weaknesses is related to the number of collisions (i.e. number of documents for one token) increases with the size of the collection. It is unclear how this approach performs when the number of documents, their length, or both, increase. It would be important thus to investigate using the model on a larger collection (e.g. MS-Marco).

Another point is that the authors state (l. 329) that SOA training "techniques are orthogonal to the retrieval model and have not been applied in our works.". It is not clear if this is truly the case here, and no experiments have been conducted to check the potential of e.g. simple techniques like knowledge distillation. 

Other things:
- The authors propose to use the elu1p (p. 4) - it is not clear why softplus has not been used, the function is quite close to this and more "standard".
- The negative mining proposed for the Wikipedia collection is very specific to this collection (l. 292-293). In my opinion, this invalidates the results reported on the Wikipedia collection (table 1 p. 7) and would justify the use of the dismissed SOA training techniques.

### Questions
- what is the purpose of section 3.1? I guess the argument is around the relationship between MLM and vocabulary expansion - see e.g. https://dl.acm.org/doi/10.1145/3634912

- Unless I miss something, there is no justification of the second par of $L_{semi-para}$, i.e. $L(V_{BoT}(q), V_\theta(p))$ since it is never used. And no ablation shows the importance of this factor

- What is $VDR_{\beta}$ in table 1? I could not find this model in the VDR paper.

- I do not agree on the difference in efficiency (lines 499-506) between your model and BM25. While it is true that leveraging GPU is useful in your case, BM25 could actually be implemented on GPU, so the reported speedup does not mean much.

### Soundness
3

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
This paper extends the VDR encoder (which also seems to be under review), aligning masked term prediction and bag of tokens representations. The paper shows that hybrid retrieval outperforms either vector based or token based retrieval alone, and the same parametric representation used in vector based retrieval can be "aligned" with bag of tokens to perform non-parametric retrieval.

### Strengths
The paper is well motivated. The problems identified with constructing and refreshing vector based document indices are consistent with prevalent challenges in the industry. While most SOTA retrieval systems, especially those used in the industry, are hybrid, re-using representations across the two forms of retrieval seems novel. There is a good set of baselines, though the most relevant baselines are those that perform hybrid retrieval with vector based and token based approaches. The paper will also benefit from inclusion of more qualitative analysis, especially on how the aligned BoT query representations tackle classical IR problems like polysemy and synonymy.

### Weaknesses
One of the strengths of bag-of-token based retrieval is that it is easily interpretable. The paper misses an opportunity to demonstrate how going from a parametric representation (which is considered semantic retrieval) allows us to tackle the standard problems in IR such as polysemy and synonymy. How do the lack of weights (a la BM25) on the document side affect retrieval?

A nit: since the paper uses a hybrid retrieval system, comparison against either vector retrieval alone is not an apples to apples comparison. For example, in Table 1, this system seems to handily outperform BM25. But BM25 doesn't have the benefit of query side synonyms. While the index is non-parametric, the query is not (it's an "aligned version" of the parametric embedding). This doesn't invalidate the results. Rather it provides a channel for further investigation into the kinds of representations that are produced.  

Comparison against other hybrid retrieval systems (Gao et al 2021, Kuzi et Al 2020) would make the paper a lot stronger. (These are ones that come to mind, but there may be more).



### Questions
BM25 as a token retrieval baseline has stood the test of time, being competitive for three decades. Why do the authors think SiDR_beta handily outperform BM25? What can we learn from this? Could this be because it's not an apples to apples comparison? Are there other underlying factors? 

Why did the authors not consider hybrid retrieval systems a more natural baseline?

### Soundness
3

### Presentation
4

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
The paper focuses on sparse neural retrieval using a SPLADE-like model. It proposes to train a neural sparse bi-encoder V for both queries Q and documents D in such a way that it works well when computing similarity in the standard bi-encoder fashion, i.e., as the inner product of V(Q) and V(D) as well as through the inner product of V(Q) and the binary bag-of-tokens representation of a document.

This can be quite useful since it permits using a neural encoder together with non-parametric document representations (that do not required encoding) for effective and efficient retrieval.

Initially I had several concerns regarding the fairness of comparison to BM25 (multi vs single-thread and running BM25 on GPU) as well as to a possibility of re-ranking using a stronger model. However, additional experiments and clarifications resolved the issues. 

There are also some clarity issues (see the weaknesses section), which I think could be resolved or mitigated in the final version. The paper is somewhat hard to read, but it's understandable with some effort.

I would like to emphasize that the final version of authors need to compare against the fast implementation of BM25 (i.e., using PISA or similar) and make sure they make it clear that the comparison is vs single-thread BM25 (this is only for efficiency evaluation, no need to re-run all experiments).

Last, but not least, that BM25 with re-ranking is a strong baseline is definitely worth highlighting and connecting it to prior work, e.g.:
Leonhardt, Jurek, et al. "Efficient neural ranking using forward indexes." Proceedings of the ACM Web Conference 2022. 2022.

### Strengths
See the summary for more details.
* An interesting approach
* A semi-parameteric index retrieval is easy to carry out on a GPU
* A substantial evaluation using the BEIR datasets (plus additional QA datasets)
* Promising results

### Weaknesses
After discussion with authors, I have come to a conviction that the paper is generally solid, but presentation can be improved.

There are several examples of where the paper is hard to read:
1. No explanation for the need of VDR (I still didn't quite get your explanations in the rebuttal).
2. The whole section of revisiting MLM is very confusing. You say "We provide insights into the consistencies between semi-parametric alignment and masked language
model pre-training", but this is already a pretty confusing phrase. To begin with you probably meant to say "connections". This is a small things, but a lot of such small things here and there complicate reading. Compare, e.g., how this was introduced in the SPLADE paper: We describe in Section 3.1 how the Masked Language Modeling (MLM) head of Pre-trained Language Models can be used to represent tokens in a sequence as vectors in the vocabulary space.
3. Then the whole section "PARAMETRIC AND NON-PARAMETRIC REPRESENTATION" is a bit of a slog to read. You need to explain what you mean by "parametric" vs "non-parameteric" vs "semi-parametric" representations. Moreover, when you talk about parametric representations it's IMHO better talk about **learned* token weights vs token computed using a hand-crafted rule (as in BM25). Don't get me wrong parametric vs non-parametric isn't wrong per se, but the distinction between parametric and non-parametric ML is a bit blurry. Plus, in the context of learned representations it is not frequently used IMHO.

BoT appears almost out of the blue. I think it was only mentioned in the MLM-section. IMHO, it's better to start by explaining that a document/query can be represented by a bag of words or tokens. In some cases these tokens are actual document/query tokens and in some cases they are "predicted" by the encoder model. Moreover, tokens can be weighted and non-weighted. Weights can come either from a model or from token-counting (as in BM25). This would have been a much less confusing explanation IMHO. Then, you can explain how weights are coming from an MLM head of a BERT model. This would have been much more logical, IMHO.

Last, but not least, that BM25 with re-ranking is a strong baseline is definitely worth highlighting and connecting it to prior work, e.g.:
Leonhardt, Jurek, et al. "Efficient neural ranking using forward indexes." Proceedings of the ACM Web Conference 2022. 2022.

I am still confused about the updated Table 3. It says BM25 takes 40 seconds but 2 minutes overall? This only convinces me that the paper needs a thorough revision. These last-minute updates are not reliable.

A single-thread CPU is a HUGE no-no. So, basically all BM25 latencies should have been divided by 32 or even more (if one used PISA instead of Pyserini/Lucene)?

### Questions
N/A

### Soundness
3

### Presentation
2

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
This paper introduces a Semi-parametric Disentangled Retrieval (SiDR) strategy that integrates the advantages of non-parametric and parametric retrieval, achieving competitive performance through the late parametric mechanism while maintaining high efficiency.

### Strengths
1. The proposed SiDR integrates the advantages of non-parametric and parametric retrieval, achieving competitive performance while maintaining high efficiency.
2. The paper provides clear explanations of the SiDR method, experiments, and analysis, making it easy to understand.

### Weaknesses
1. In Table 1, the performance of SiDR in parametric retrieval scenario does not surpass ANCE, even with the late parametric mechanism, yet the authors still report it as the best result with the bolded values.
2. In Table 2, under the non-parametric retrieval scenario, SiDR fails to surpass BM25 in most of datasets.
3. The late parametric mechanism is not novel, and the experiments should include more comparisons to various methods in this category.
4. Because of the comparison results with SiDR and ANCE/BM25, the experimental analysis should include an examination of the reasons for SiDR's better performance in the late parametric scenario.

### Questions
1. How does SiDR compare with other late parametric methods, and what are the reasons for its success in the late parametric scenario?

### Soundness
3

### Presentation
3

### Contribution
2
