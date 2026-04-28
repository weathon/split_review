# EmbedLLM: Learning Compact Representations of Large Language Models

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
With hundreds of thousands of language models available on Huggingface today, efficiently evaluating and utilizing these models across various downstream tasks has become increasingly critical. Many existing methods repeatedly learn task-specific representations of Large Language Models (LLMs), which leads to inefficiencies in both time and computational resources. To address this, we propose \algname{}, a framework designed to learn compact vector representations of LLMs that facilitate downstream applications involving many models, such as model routing. 
We introduce an encoder-decoder approach for learning such embeddings, along with a systematic framework to evaluate their effectiveness.
Empirical results show that \algname{} outperforms prior methods in model routing both in accuracy and latency. Additionally, we demonstrate that our method can forecast a model's performance on multiple benchmarks, without incurring additional inference cost. Extensive probing experiments validate that the learned embeddings capture key model characteristics, \textit{e.g.} whether the model is specialized for coding tasks, even without being explicitly trained on them.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel framework for generating compact vector representations of LLMs to enhance model routing, task efficiency, and performance forecasting. The EmbedLLM framework creates embeddings that capture important characteristics of different LLMs, such as suitability for specific tasks like coding or conversational response generation. Experiments results indicate that the embeddings effectively capture key characteristics of LLMs, enabling efficient and accurate task allocation and performance prediction across a variety of benchmarks.

### Strengths
Embedding LLMs to handle downstream tasks is indeed a fascinating approach! This method allows you to create compact representations of each model that capture its unique strengths and weaknesses, enabling efficient task-specific decisions without running each model on every input. This approach streamlines the workflow significantly, as it allows for general-purpose embeddings that can adapt to a variety of downstream tasks without retraining the models themselves. It's especially beneficial in settings where computational resources are a concern or when the model pool is large.

### Weaknesses
The term "decoder" in this paper is a bit misleading. In typical encoder-decoder architectures, the "decoder" reconstructs or generates the output in its full or intended form, such as reconstructing text in sequence-to-sequence tasks. Here, however, the so-called "decoder" is merely a binary classifier that outputs a label indicating whether the LLM correctly answered a question.
We have to re-train the embedder if we want to represent new models, this makes the whole framework non-scalable. I'd like to see details cost metrics for re-train embedder for new model vs traditional benchmarking approaches.

### Questions
Please address the weakness I mentioned above.

### Soundness
2

### Presentation
2

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
The paper presents EmbedLLM, a framework for creating compact vector embeddings of large language models (LLMs) to improve efficiency in tasks like model routing and benchmark performance prediction. EmbedLLM uses an encoder-decoder architecture to map LLMs into a unified embedding space that captures important model characteristics. This representation allows accurate model selection and performance forecasting across multiple tasks without repetitive re-evaluation, reducing both time and computational costs. Experiments show that EmbedLLM enhances accuracy and latency in model routing and can predict benchmark scores reliably. The embeddings also reflect intrinsic model attributes, useful for identifying task-specific strengths, even in models not explicitly trained for certain tasks.

### Strengths
- The paper innovatively proposes the embedding of LLMs to facilitate managing and comparing them.    
- The experiments in the paper are comprehensive, tested on 112 large models

### Weaknesses
 - The paper proposes a method for encoding LLMs. However, in the implementation, this encoding is merely based on model IDs, treating each model entirely as a black box. With only 30,000 data for training, can the resulting encoding truly capture all the characteristics of the models? Large models differ significantly in their strengths across various domains and capabilities. Can such an approach, based solely on one round question-answer pairs, truly distinguish the models’ abilities when facing complex reasoning problems? Another issue is whether the scale of the proposed embedding network is sufficient to represent the characteristics of numerous models effectively.

- A little confused about line 256-257. Why are two values (p(m,q)_0 and p(m,q)_1) output here? Is it simply to add a nonlinear operation?

- The experiments do not appear to categorize models by scale. Intuitively, the larger the model, the smaller the performance differences between models. What is the authors' view on this issue?

- The paper does not seem to provide a clear and intuitive illustration of the overall architecture, including training, input, and output processes. Figures 1-3 are quite similar and take up too much space, and it wasn’t until section 4.1 that I understood how the whole system works. Of course, I do not deny the paper's contributions, but I suggest the authors improve the visual presentation.

### Questions
See the weaknesses

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The goal of this paper is to represent LLMs using an embedding that can predict performance on new inputs and benchmarks. Such an embedding can be learned from matrix factorization methods applied to a matrix that contain the behavior of the LLM on several data points as well as behavior of other LLMs on these datapoints, i.e., a matrix with rows as LLMs and columns as data points, and each cell indicate an LLM's performance on a specific data point. The factorization aims to reconstruct this matrix by learning an embedding for each LLM and an embedding for each data point (built from its static embedding which is further projected into the same embedding space of LLM). 

The resulting embeddings are evaluated to predict performance of new data points and benchmarks and to improve model routing.

### Strengths
1. A simple and intuitive method.
2. Once the embedding of an LLM is built, the performance of the LLM can be accessed without access to the model.

### Weaknesses
1. The paper can be motivated better and clarify why the current formulation is intuitive, i.e., a model's behavior on new data points can be predicted based on its behavior on already existing data points. The core assumption that a model's performance on unseen data can be inferred from its performance on existing data needs more justification. It's not immediately clear why a matrix factorization approach would be the most suitable method for this task, especially given the high dimensionality and potential non-linearity of LLM behaviors.
2. Details are hard to follow or underspecified, e.g., kNN classifier, random routing. The description of the kNN classifier lacks specifics on the distance metric used and the method for handling ties in majority voting. The random routing baseline is also vaguely described, making it difficult to assess its effectiveness as a comparison point. The paper should provide more details on the implementation and hyperparameter tuning for these baselines.
3. There are no references to highly similar work that predicts performance on a new task based on the performance of existing tasks. For example, Xia et al. Predicting Performance for Natural Language Processing Tasks, 2020
4. Calling the method as encoder-decoder in Sec 4.3 is confusing. The decoder is nothing but a classifier, and calling it straightforwardly that will make it easier to follow instead of calling it a decoder. The use of the term 'decoder' is misleading, as it implies a generative process, while the model is simply performing classification. This terminology obscures the simplicity of the approach and makes it harder to understand the core mechanism. A more accurate description would be a linear classifier applied to the Hadamard product of the question and model embeddings.
5. There is no analysis/visualations of the embeddings. Current histogram plot in Figure 6 is not that informative. Could you provide TSNE plots of the resulting embeddings.

### Questions
1. Why does the method assume that answer have to be a binary label? Is this a limitation of this method?
2. The explanation of kNN-classifer baseline is unclear. How is final label chosen? -- based on the majority voting of k-nearest neighbours?
3. Lines 264--267 are unclear. What is mxp and nxp represent?
4. Some qualitative discussion with examples on what happens when the resulting data points are widely different from already seen data points will be useful. 
5. Does the prompt embedding have an impact on the results, i.e., using better recent LLM-based embeddings. 
6. I would also like to see the TSNE plots of the embeddings.

Minor:
1. Vaswani et al. should be 2017. The paper opens up with a wrong citation. This paper is also wrongly attributed to LLMs. You could be more careful with your citations.
2. The method should perhaps be named EmbedLLM rather than Matrix Factorization.

I am willing to increase the score based on better presentation and qualitative analysis. The paper is quite weak in this aspect.

### Soundness
3

### Presentation
3

### Contribution
3
