# Contradiction Retrieval Via Sparse-Aware Sentence Embedding

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Contradiction retrieval refers to identifying and extracting documents that explicitly disagree with or refute the content of a query, which is important to many downstream applications like fact checking and data cleaning. To retrieve contradiction argument to the query from large document corpora, existing methods such as similarity search and crossencoder models exhibit significant limitations. The former struggles to capture the essence of contradiction due to its inherent nature of favoring similarity, while the latter suffers from computational inefficiency, especially when the size of corpora is large. To address these challenges, we introduce a novel approach: SparseCL that leverages specially trained sentence embeddings designed to preserve subtle, contradictory nuances between sentences. Our method utilizes a combined metric of cosine similarity and a sparsity function to efficiently identify and retrieve documents that contradict a given query. This approach dramatically enhances the speed of contradiction detection by reducing the need for exhaustive document comparisons to simple vector calculations. We validate our model using the Arguana dataset, a benchmark dataset specifically geared towards contradiction retrieval, as well as synthetic contradictions generated from the MSMARCO and HotpotQA datasets using GPT-4. Our experiments demonstrate the efficacy of our approach not only in contradiction retrieval with more than 30% accuracy improvements on MSMARCO and HotpotQA across different model architectures but also in applications such as cleaning corrupted corpora to restore high-quality QA retrieval. This paper outlines a promising direction for improving the accuracy and efficiency of contradiction retrieval in large-scale text corpora.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces a new loss for training sentence embeddings towards the task of contradiction retrieval. Unlike the conventional SentenceBert setting, two sentences should have high embedding similarity if they contradict with each other, while having low similarity if one is the other's paraphrasing. This work demonstrates that the traditional contrastive learning does not work well for the contradiction retrieval setting, and proposes a new contrastive loss based on Hoyer sparsity distance, which encourages the sparsity of the difference between two contradicting embeddings.

Experiments are conducted on two specific tasks: 1) evaluation on Arguana dataset, a counter-argument retrieval dataset in MTEB benchmark; 2) evaluation on synthetic passages paraphrased from MSMARCO and HotpotQA for contradiction retrieval. Results suggest that the new model is able to bring consistent improvement over the conventional contrastive model, especially for the second task, where finetuning with conventional contrastive is not effective.

### Strengths
- A new loss is proposed to train sentence embeddings for contradiction retrieval. The loss is based on embedding sparsity, motivated by the fact that two contradicting sentences may appear similar, thus traditional contrastive may not work as well.
  
- The proposed method is shown empirically effective in two task settings, surpassing baselines by large margins.

### Weaknesses
 - Though the motivation is mentioned in the paper, I think there needs more explanation and analysis on why sparsity-based distance works better.
  
- - The Introduction Section states that traditional cosine-similarity metric is transitive. However, it is a wrong statement, as it is not transitive in vector space, especially for high-dimensional space.
    
  - The experiments could give more quantitative analysis or qualitative examples on the role that the sparsity loss is playing.
    
- The paper needs more polishing for formal writing. There are also typos, e.g. Line225 "can can".

### Questions
For the synthetic task on MSMARCO and HotpotQA, does each train/dev/test split stem from a different set of original passages, or there can be overlap?

### Soundness
3

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
4

### Summary
This paper addresses the challenge of contradiction retrieval, which involves identifying documents that explicitly refute or disagree with a given query. Traditional approaches, such as similarity search and cross-encoder models, have significant limitations in this context: similarity-based methods struggle to capture contradictions, while cross-encoders are computationally costly, particularly for large datasets. To overcome these challenges, the authors propose a framework, SPARSECL, that combines specially trained sparse-aware sentence embeddings with a combined metric based on cosine similarity and the Hoyer measure of sparsity. This combination allows for efficient and accurate contradiction retrieval without the computational burden of traditional models. Experiments on three datasets demonstrate the effectiveness of SPARSECL when plugged into different LLM-based retrievers.

### Strengths
+ The problem of contradiction retrieval is important and has practical value (e.g., in scientific claim verification). The authors point out the limitations of existing bi-encoder and cross-encoder approaches and propose corresponding techniques to overcome the challenges.

+ The idea of sparse-aware sentence embeddings and the use of the Hoyer measure are intuitive and well-motivated. To be specific, The Hoyer measure is non-transitive, meaning it can effectively distinguish between sentences that are indirectly related but still contradictory.

+ Experiments are comprehensive. The proposed SPARSECL technique is plugged into various LLM-based retrievers (i.e., UAE-Large-V1, bge-base-en-v1.5, and gte-large-en-v1.5) to validate its generalizability. Besides performance comparison, the authors also conduct ablation studies to verify some of their design choices.

### Weaknesses
 - Statistical significance tests are not conducted. It is not clear whether the gaps between X+Zeroshot and X+Zeroshot+SPARSECL are statistically significant or not (X=UAE-Large-V1, bge-base-en-v1.5, and gte-large-en-v1.5). In fact, the improvement is subtle in some columns in Table 1.

- Only one real dataset (i.e., Arguana) is examined in the experiments. The other two used datasets are synthesized from MSMARCO and HotpotQA, respectively, using GPT-4. It would be valuable to explore other real datasets from other domains, such as scientific claims (e.g., SciFact [1]).


### Questions
- Could you conduct a statistical significance test (e.g., two-tailed t-test) to compare X+Zeroshot with X+Zeroshot+SPARSECL, and report the p-values?

- Could you try SPARSECL on the SciFact benchmark dataset (either its original version or the BEIR version) to retrieve paper abstracts that refute a given query claim?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper works on contradiction retrieval, which is to identify and extract documents that disagree or refute the content of a query. Existing methods fail to capture the essence of contradiction due to its similarity comparison nature, or has efficiency issues. The paper proposes SparseCL to address these challenges, which leverages sentence embeddings designed to preserve subtle, contradictory nuances between sentences. This method could identify contradictory documents with simple vector calculations. The proposed method was verified on the Arguana dataset and synthetic contradictions from MSMARCO and HotPotQA. It has another application, which is cleaning corrupted corpora to restore high-quality QA retrieval.

### Strengths
- The experiments show that the proposed method (SparseCL) is able to maintain high performance on tested datasets compared with crossencoders while it has less computational requirement by utilizing a simple vector calculation.
- The idea of using sparsity metric to measure contradiction plus normal sentence embedding similarity is novel. As the paper mentions in line 347, there were no method for retrieving contradictions that only rely on sentence embeddings.

### Weaknesses
 - In line 229-232: The scalar $\alpha$ in scoring function F(p1, p2) requires tuning on target dataset, which limits the generalization of the method. It shows the proposed method can’t adapt to unseen data (domain shift) automatically.
- The scale of the Arguana dataset is small, with less than 7k argument-counterargument pairs.
- To address the generalization of embeddings obtained from model fine-tuning, the paper reports results from training on MS MARCO and testing on HotpotQA, and vice versa. HotpotQA consists of corpora sourced from Wikipedia, whereas MS MARCO is derived from Bing search logs, which likely include some Wikipedia documents. Therefore, the paper should first address potential data contamination to ensure that the model is tested on truly unseen data before claiming generalization of the embeddings.

### Questions
- Since SparseCL could do contradiction retrieval, it’s also possible for it to be used as a contradiction detection model (or a contradiction scoring model). For example, there are many datasets in NLI and Fact Checking domains. It would be interesting to see if this method works on these datasets.
- In line 237-238: Please check reference format.

### Soundness
2

### Presentation
3

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
This paper proposes a new task for text retrieval - contradiction retrieval, which aims to retrieve texts contradicting the input one. The author discusses the existing paradigm and claims the intransitive nature of contradiction to be an obstacle to previous contrastive learning scenarios. Following this observation, the authors propose the Hoyer sparse function as the metric for contradiction, which shows some improvements when being merged with semantic similarity scores.

### Strengths
1. This work points out a potential issue in learning a specific kind of embedding relationship - contradiction, which might not be well addressed by the existing contrastive learning paradigm.

2. The authors propose an interesting idea for learning sparse representations for contradiction retrieval with the Hoyer sparse function as an intransitive metric.

Overall, the issue is justified with a reasonable method being proposed. This paper includes an interesting idea to make it publish.

### Weaknesses
While this paper presents an interesting idea, several major components still exist to make readers agree with the proposed claims.

There are unaddressed potential opposed claims
1. Instead of learning the contradiction as a metric, it is more natural to reverse the semantics of the context to adapt the contradiction to the similarity. One way to do this is to append instructions to the input (Instructor [1]), such as "Contradicted to: [INPUT]". There can be a baseline (not the original Instructor) learning cosine similarity as the metric follows the traditional contrastive learning paradigm, while the inputs are with the mentioned prefix. Outperforming this baseline can further establish the necessity of learning a sparse metric, otherwise, people may favor context switching more because it can be merged with general similarity learning.

2. Is there a stable selection of \alpha? While direct semantic similarity plays an important role in contradiction retrieval in the benchmarks mentioned in the paper. The weight on the semantic similarity is quite unstable from my viewpoint - contradiction shall be not so relevant with the semantic similarity, for instance

Case1:
Text1: "Dinosaurs live on earth today." Text2: "Dinosaurs don't live on earth today."

Case2:
Text1: "Dinosaurs live on earth today." Text2: "A huge asteroid hit the earth 65 million years ago and caused the extinction of dinosaurs."

While the cases above are somehow extreme, this still indicates how contradiction is independent of the direct textual similarity. From some readers' view, the semantic similarity should be treated as a threshold (not totally irrelevant) rather than a weighted term. So,

- Why do you think semantic similarity should still play an important role in contradiction retrieval? I think showing some real-world distribution in the corpus can lead to some help.

Claim support is incomplete
1. An important claim of this paper is the advantage of the Hoyer function over cosine similarity because of its intransitive nature. However, this point is not supported in the content because there lack of baselines trained on the reversed similarity labels. Please consider adding this as a baseline to your main table.

- How would you define the contradiction level with non-statements like questions?

2. The performance improvement on synthesized datasets is much higher than Arguana. Based on the prompts and cases provided in the Appendix, I feel the generated contradictions are somehow favored by the proposed paradigm - mostly similar with some sparse differences. However, as mentioned above, contradiction can happen between texts with very different "length", "style", "format", so I feel this synthesis is oversimplifying the problem and making the dataset favor the proposed method. I would suggest the authors allow the synthesizer to generate text pairs with very different other attributes to further validate the too significant improvement.

- Why don't you include NLI datasets as a source of benchmarking, they directly include contradicted text pairs.

Not enough content
1. Lack of baselines. The main comparison only includes a contrastively learned encoder, which is even unintended for the proposed contradiction retrieval task. Even though contradiction retrieval is a new task, there should be some simple baselines as mentioned above. You can also consider adding the original Instructor as a baseline, though I feel I will not perform well.

2. Lack of task significance justification. As a newly proposed task focusing on a rather narrow scope, the paper does not fully justify the importance of further digging into this task. One way to further support the importance of contradiction retrieval is to select one of the tasks mentioned in the related works to show they can be improved with contradiction retrieval.

Overall, while this paper proposes a reasonable way to address a potential issue in text embedding learning, I feel this paper has to be significantly polished to reach publication quality. Thus, I am opposed to an immediate acceptance of this paper.

### Questions
My questions are corresponded with the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3
