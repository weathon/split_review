# NV-Embed: Improved Techniques for Training LLMs as Generalist Embedding Models

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Decoder-only large language model (LLM)-based embedding models are beginning to outperform BERT or T5-based embedding models in general-purpose text embedding tasks, including dense vector-based retrieval. 
In this work, we introduce the \ours{} model with a variety of architectural designs and training procedures to significantly enhance the performance of LLM as a versatile embedding model, while maintaining its \emph{simplicity} and \emph{reproducibility}.
For model architecture, we propose a \emph{latent attention layer} to obtain pooled embeddings, which consistently improves retrieval and downstream task accuracy compared to mean pooling or using the last \texttt{<EOS>} token embedding from LLMs. 
To enhance representation learning, we remove the causal attention mask of LLMs during contrastive training.
For model training, we introduce a two-stage contrastive instruction-tuning method. It first applies contrastive training with instructions on retrieval datasets, utilizing in-batch negatives and curated hard negative examples. At stage-2, it blends various non-retrieval datasets into instruction tuning, which not only enhances non-retrieval task accuracy but also improves retrieval performance.
Combining these techniques, our \ours{} model, using only publicly available data, has achieved a record-high score of 69.32, ranking No. 1 on the Massive Text Embedding Benchmark (MTEB)~(as of May 24, 2024), with 56 tasks, encompassing retrieval, reranking, classification, clustering, and semantic textual similarity tasks. Notably, our model also attains the highest score of 59.36 on 15 retrieval tasks in the MTEB benchmark (also known as BEIR).
We will open-source the model at: \url{https://huggingface.co/nvidia/NV-Embed-v1}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper gives a summary of the NV-Embed model that achieved the top performance in the MTEB benchmark. 
The techniques used are
1. latent attention layer that achieves better pooling/combination of the last layer embeddings. Causal attention mask is removed during contrastive learning. 
2. a two-stage contrastive instruction tuning method. First step tuning with in-batch negative and hard negative on retrieval datasets, and the second step tuning on non-retrieval datasets.
3. large amount of efforts on training data curation.

### Strengths
1. This work gives a good summary of the STOA NV-Embed model that leads the MTEB benchmark. I think the community will very much appreciate this paper.
2. Impressive experimental results with good ablations to justify the design choices.
3. Clear presentation.

### Weaknesses
The NV-Embed model is a result of a combination of methods/tricks/datasets etc. 
There does not seem to be single innovative algorithm piece. This by itself is not a weakness of the work. However, as a result, the technical depth of the work is limited.

### Questions
The v2 model largely outperformed v1: 
"We then further improve the model through the curation
of training dataset, including adding more retrieval datasets, applying positive-aware hard-negative
mining technique, using synthetic data generation process and constructing example-based multi-class
labels." 
It would be nice to have more discussions and ablations specifically regarding the v2 vs. v1.

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
This paper presents techniques for leveraging pretrained decoder-only large transformers in retrieval tasks, achieving state-of-the-art results on the standard retrieval benchmark (MTEB). The core methods include:
* A latent attention layer for creating pooled embeddings, which surpasses traditional mean pooling and last-token embedding approaches.
* A two-stage training process: the first stage focuses on retrieval datasets, while the second integrates non-retrieval tasks for broader versatility.
* The use of curated datasets (e.g. hard-negative mining) to further refine embedding quality.

### Strengths
* Provides very strong empirical results. This work achieves state-of-the-art results, securing the #1 position on the MTEB benchmark. This demonstrates the effectiveness of the proposed approach.
* Provides nice ablation studies (e.g., Table 4) to analyze the effects of various design choices, including single-stage vs. two-stage, hard negative mining (HN), public retrieval set (AD), and synthetic data generation (SD).
* Provides detailed descriptions of the data curation process, including specific techniques like hard negative mining and synthetic data generation. This transparency allows for better understanding and potential reproducibility of the work.

### Weaknesses
 * Using decoder-only pretrained models for retrieval is not entirely novel (e.g., as seen in GritLM [1] and discussed in Section 2.2). While the authors note differences in their specific training approach, this limits the novelty of this aspect.
* Given this, the main contributions center on the latent attention layer and two-stage instruction tuning. However, the performance improvement from latent attention over mean pooling appears modest (see Table 2, bidirectional columns), raising questions about the added complexity for minimal gains. Specifically, the gains are less than 0.5 points on the MTEB benchmark, which is a small improvement given the added complexity of the latent attention mechanism.
* Although the authors provide empirical support for the benefits of two-stage training, there is limited explanation or intuition behind why this approach works effectively. The paper would benefit from a more in-depth discussion of the underlying mechanisms that contribute to the success of the two-stage training process. For example, how does the initial retrieval-focused stage impact the subsequent generalization to other tasks?

### Questions
* What would happen if the order of the two-stage training were reversed?
* Could you expand on the points raised in the weaknesses section, offering more discussion on these limitations?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new embedding model: NV-embedder. The model uses a latent attention layer to obtain pooled embeddings instead of the common EOS token. The authors also propose a two-stage training method and employ hard example mining and data synthesis.

### Strengths
- The authors tested the model on a leaderboard outside of MTEB. Since the training data is related to MTEB, out-of-domain testing is necessary. 
- The authors conducted extensive ablation studies to verify the effectiveness of each module.

### Weaknesses
The biggest drawback is the complexity of the entire training process, which includes multi-stage training, hard example mining, and data synthesis. This involves too many operations, making it difficult to reproduce. The specific implementation details of the hard example mining and data synthesis are not clearly defined, raising concerns about the robustness and generalizability of the approach. The reliance on multiple training stages also introduces additional hyperparameters that require careful tuning, further complicating the reproduction process.

### Questions
no

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents the NV-Embed-v1 and v2 systems for general purpose text embeddings. The paper presents the learning algorithm along with architecture variations (latent attention), ywhich describes how the system achieves #1 on the MTEB leaderboard at the time of submission. This paper documents the high performing system, which is likely to have gathered much attention given its position in the leaderboard.

### Strengths
This paper severs a very clear and important purpose -- documenting the current top performing system on the extremely competitive text embedding benchmark, MTEB. The paper presents an approach, which like other approaches on the MTEB leaderboard, takes a pretrained transformer model and trains using a mixture of datasets/tasks, including a hard negative mining pipeline. The authors also introduce a simple architectural change, latent attention layer.

The key strength of the paper, is its empirical gains and empirical analysis. The authors provide benchmark performance on a wide range of settings with highly performing models. This shows the capabilities of models on a wide variety of tasks, including important ablations regarding attention type, stages of training, etc.

### Weaknesses
As this paper is primarily the documentation of a very highly performing empirical system, main weakness I would point out is about innovation. On one level the paper is ground breaking because of its empirical gains, on another, the core methodological techniques are well known, only that they are more effectively performed and analyzed here.

The latent attention mechanism, while a nice architectural change, only has a small effect on the average performance (Table 2). The hard negative mining pipeline, a more established technique, on the other hand makes much more of a difference (Table 4).

### Questions
For each stage of training, do you use the same optimizer? Restarting it for each stage?

### Soundness
3

### Presentation
3

### Contribution
3
