# Scalable Multi-phase Word Embedding Using Conjunctive Propositional Clauses

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
The Tsetlin Machine (TM) architecture has recently demonstrated effectiveness in Machine Learning (ML), particularly within Natural Language Processing (NLP). It has been utilized to construct word embedding using conjunctive propositional clauses, thereby significantly enhancing our understanding and interpretation of machine-derived decisions. The previous approach performed the word embedding over a sequence of input words to consolidate the information into a cohesive and unified representation. However, that approach encounters scalability challenges as the input size increases. In this study, we introduce a novel approach incorporating two-phase training to discover contextual embeddings of input sequences. Specifically, this method encapsulates the knowledge for each input word within the dataset’s vocabulary, subsequently constructing embeddings for a sequence of input words utilizing the extracted knowledge. This technique not only facilitates the design of a scalable model but also preserves interpretability. Our experimental findings revealed that the proposed method yields competitive performance compared to the previous approaches, demonstrating promising results in contrast to human-generated benchmarks. Furthermore, we applied the proposed approach to sentiment analysis on the IMDB dataset, where the TM embedding and the TM classifier, along with other interpretable classifiers, offered a transparent end-to-end solution with competitive performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a novel two-phase method for generating word embeddings using the Tsetlin Machine (TM) and Coalesced Tsetlin Machine (CoTM) structures. The authors describe how the CoTM automaton process and the TM autoencoder (TM-AE) operate, introducing a two-phase training mechanism for the TM-AE. The proposed approach's effectiveness is evaluated on semantic similarity and sentiment classification tasks, comparing the performance of the two-phase TM-AE embeddings with other word embedding frameworks, including GloVe, Word2Vec, FastText, BERT, and ELMo. Results indicate that the two-phase TM-AE embeddings outperform GloVe, Word2Vec, and FastText on specific tasks and metrics. Additionally, the authors highlight that this approach represents the first scalable, transparent, end-to-end framework for generating word embeddings based on propositional logic through a TM-based method.

### Strengths
This paper has several notable strengths:
1. It introduces a relatively novel approach by employing the Tsetlin Machine automaton to generate word embeddings, distinguishing it from more conventional methods.
2. The paper provides a thorough explanation of the CoTM architecture, TM automaton, TM-AE training process, and the unique two-phase TM-AE training schema.
3. The authors highlight a computational efficiency feature: by skipping the first phase of TM-AE when updating a single word, one can reduce the computational load.
4. Multiple human-annotated datasets, including RG65, MTURK287, MTURK717, and WS-353, are used to rigorously evaluate the quality of the generated word embeddings.
5. The proposed two-phase TM-AE embeddings are comprehensively compared to established models such as GloVe, Word2Vec, FastText, BERT, and ELMo, offering insight into its relative strengths and weaknesses.

### Weaknesses
The paper has several areas where it could be improved:
1. Although the model reportedly required 6 months of training on a DGX H100 machine, the paper lacks a rigorous analysis of the computational time and space complexity of the proposed method. Specifically, it does not provide a breakdown of the time spent in each phase of the training process, nor does it compare the memory footprint of the proposed method with other approaches like GloVe, Word2Vec, and FastText. This makes it difficult to assess the practical scalability of the approach, especially for larger datasets and vocabularies.
2. While the paper emphasizes the scalability and transparency of the two-phase TM-AE approach, further explanation and analysis of these properties would strengthen the argument for its advantages. For example, the paper could include empirical scalability results by showing how the training time and memory usage scale with increasing vocabulary sizes and dataset sizes. Additionally, the authors could provide concrete examples of how the logical structure of embeddings can be interpreted, perhaps by visualizing the logical clauses associated with specific words.
3. The quality of the two-phase TM-AE embeddings could be better demonstrated by including additional evaluation tasks beyond semantic similarity, such as analogy, categorization, and outlier detection. These tasks would provide a more comprehensive assessment of the semantic and syntactic properties captured by the embeddings. For instance, analogy tasks could test the ability of the embeddings to capture relationships between words (e.g., "king is to man as queen is to woman"), while outlier detection could assess their ability to identify semantically dissimilar words within a set.
4. The hyper-parameters used in the sentiment classification MLP model and TM classifier are not documented, and there is no discussion of the hyper-parameter fine-tuning process for the TM classifier. This lack of transparency makes it difficult to reproduce the results and assess the robustness of the findings. Specifically, the paper should detail the range of hyper-parameter values explored, the optimization strategy used (e.g., grid search, random search), and the criteria used to select the optimal hyper-parameter settings.
5. In Section 4.1, the comparison of TM-AE and two-phase TM-AE on similarity tasks shows that TM-AE performs better on two out of three metrics. This result raises questions about the benefit of the two-phase approach for this task. To address this, a more in-depth analysis is needed to explain why the two-phase approach underperforms on these metrics. The authors should discuss potential trade-offs or benefits that the two-phase approach might offer despite these results, such as improved performance on other tasks or better interpretability.
6. In Section 4.2, the paper omits the performance of the TM-AE model, which would provide valuable context for assessing the gains offered by the two-phase TM-AE. Including the TM-AE results would allow for a direct comparison and a more thorough understanding of the benefits of the two-phase approach in the sentiment classification task.

### Questions
In addition to addressing the items raised in the Weaknesses section, the authors could consider the following suggestions to further enhance the paper:
1. Include a more detailed comparison between TM-AE and two-phase TM-AE embeddings to clarify the specific benefits and limitations of each approach.
2. Evaluate the quality of two-phase TM-AE embeddings on additional word embedding tasks such as analogy, categorization, and outlier detection.
3. Provide a few examples of two-phase TM-AE embeddings to illustrate their characteristics more concretely.
4. Demonstrate the potential of two-phase TM-AE embeddings in more complex NLP tasks by incorporating them into Transformers or other state-of-the-art NLP or large language models, showcasing applications beyond classification tasks.
5. Include a discussion of possible future research directions to give readers insight into how this work could be further developed.
6. Provide the code for two-phase TM-AE training and evaluation to facilitate reproducibility and further research.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a scalable two-phase word embedding method using the Tsetlin Machine (TM) framework for NLP tasks. Phase 1 generates interpretable word embeddings by learning contextual knowledge for each target word, capturing it in logical clauses. In Phase 2, these embeddings are used to create representations for word sequences, supporting applications like sentiment analysis. Evaluations show competitive performance, particularly in sentiment analysis and similarity assessments on human-annotated datasets. The approach provides a transparent, reusable alternative to traditional embeddings.

### Strengths
A novel tsetlin machine based incorporating two-phase training to discover contextual embeddings of input sequences.

### Weaknesses
 - The main motivation is not clearly expressed; the introduction does not outline the differences and advantages over previous methods, only presenting an overview of prior work. The CoTM method is also not original, thus the interpretability mentioned at the beginning is also not a contribution of this paper.

- The introduction mentions the issue of long training time, but the experiments section does not seem to analyze the efficiency issue.

- The experiments are conducted only on a sentiment analysis dataset for a text classification task, which is of limited persuasiveness.

### Questions
I have a question regarding the Tsetlin machine-based word embedding approach. This method does not seem to account for word order, relying more on co-occurrence features to represent semantics. As a result, it may be less effective at capturing dependency, structure, and other linguistic characteristics. This could be why it performs reasonably well only on tasks like sentiment classification that do not require deep structural semantics. What is the authors' view on this issue?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper introduces a scalable two-phase word embedding approach using TM and conjunctive propositional clauses. Phase 1 captures knowledge for individual words, while Phase 2 constructs embeddings for word sequences. Experiments show that the model achieves competitive cosine similarity on benchmark datasets but lags in Spearman correlation. Additionally, the model performs moderately well in sentiment analysis compared to BERT and ELMo. This approach demonstrates TM’s potential for interpretable NLP applications, though further refinement is needed.

### Strengths
- The two-phase approach to word embedding with TM is novel, especially using conjunctive propositional clauses, which adds interpretability.
- The use of Tsetlin Machines enables a more transparent and interpretable embedding process compared to deep learning models.
- Practical Application in Sentiment Analysis: The embeddings show utility in real-world tasks, as demonstrated through sentiment analysis with data augmentation.

### Weaknesses
 - The results don’t look good; the model performs poorly on Spearman and Kendall correlations, which suggests it struggles to capture the ranking of word pairs.
- I guess Algorithm 1 doesn’t seem to be a direct contribution of this paper, so it might be better left out of the main text or put into Appendix.
- The paper could use more polish. For example, Tables 1 and 2 are missing top and bottom lines, which affects readability.
- The evaluation is pretty narrow, focusing mostly on basic similarity metrics and sentiment analysis, without exploring a broader range of NLP tasks that would really show the model’s robustness.
- For Table 2, why the socres for all models looks quite similiar? Also, I didn't see the TM outperform the other models. It even lag behind a lot for some embeddings. It may happens very randomly but it becomes hard to convince the advantages of TM.

### Questions
See the Weaknesses

### Soundness
2

### Presentation
1

### Contribution
2
