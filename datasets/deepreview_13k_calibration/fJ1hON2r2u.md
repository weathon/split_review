# A Single Swallow Does Not Make a Summer: Understanding Semantic Structures in Embedding Spaces

- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 3, 5, 3

## Abstract
Embedding spaces encapsulate rich information from deep learning models, with vector distances reflecting the semantic similarity between textual elements. However, their abstract nature and the computational complexity of analyzing them remain significant challenges. To address these, we introduce the concept of Semantic Field Subspace, a novel mapping that links embedding spaces with the underlying semantics. We propose \textsf{SAFARI}, a novel algorithm for \textsf{S}em\textsf{A}ntic \textsf{F}ield subsp\textsf{A}ce dete\textsf{R}m\textsf{I}nation, which leverages hierarchical clustering to discover hierarchical semantic structures, using Semantic Shifts to capture semantic changes as clusters merge, allowing for the identification of meaningful subspaces. To improve scalability, we extend Weyl's Theorem, enabling an efficient approximation of Semantic Shifts that significantly reduces computational costs. Extensive evaluations on five real-world datasets demonstrate the effectiveness of \textsf{SAFARI} in uncovering interpretable and hierarchical semantic structures. Additionally, our approximation method achieves a 15$\sim$30$\times$ speedup while maintaining minimal errors (less than 0.01), making it practical for large-scale applications. The source code is available at \url{https://anonymous.4open.science/r/Safari-C803/}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method named SAFARI which constructs a cluster of semantic embeddings (I interpret as some meaningful word/phrase embeddings) from a set of such embeddings. The clustering algorithm is bottom-up hierarchical in nature, but employees a custom merge criteria based on their proposed semantic shift computation (Fig 4). The semantic shift between two clusters (hence two lists of embeddings) is calculated by first treating the list of embeddings as a matrix, and then finding their eigen-value and vectors, and finally taking the difference (eq 7). The authors noted that this process can be a bottleneck for the runtime because of the need of performing SVD, and proposed a approximation to this computation that seems to work well in the following experiments. Experimentally, the authors tested how strong their algorithm can separate embeddings from datasets coming from different domain, and compared with some baselines on classifying the embeddings of different textual classes.

### Strengths
The paper proposes an interesting angle to semantic embedding spaces by quantifying it as the semantic shift when as new embedding is introduced.  An efficient workaround to their semantic shift metric that requires SVD is introduced, and might be useful in other scenarios where a similar calculation is needed.

### Weaknesses
1. The experiment section needs some more details, It is missing details on how the baselines are adapted in the work, the hyperparameters chosen, and how the dataset for the experiment is constructed. Specifically, the description of the baseline models lacks sufficient detail to allow for reproducibility. For example, it is unclear whether the baseline models were trained from scratch or if pre-trained models were used, and if so, which ones. Furthermore, the specific hyperparameter settings for each baseline, such as learning rate, batch size, and number of training epochs, are not provided. The dataset construction process is also vague, lacking information on how the different domain datasets were created, the size of each dataset, and the specific criteria used to assign embeddings to different classes. This lack of detail makes it difficult to assess the validity and significance of the experimental results.
2. The intuition behind the semantic shift in eq (7) is lacking. It seems quite a big jump from an abstract definition of semantic fields to a concrete definition based on the differences of their eigen-values and eigen-vectors. The connection between the proposed semantic shift metric, which is based on the difference of eigenvalues and eigenvectors, and the actual semantic change in the embedding space is not clearly established. While the authors propose that changes in singular values and vectors reflect semantic shifts, a more detailed explanation of why this is the case is needed. The paper would benefit from a more intuitive explanation of how changes in the basis of the subspace, represented by the eigenvectors, and the importance of these bases, represented by the eigenvalues, directly correspond to semantic changes in the underlying text.

### Questions
1. The two weaknesses might be addressable via detailed experimental configurations and better intuition.
2. There are many equations in the paper, the ones that are not referenced later probably does not need a label.

### Soundness
3

### Presentation
3

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
The paper presents a new approach SAFARI, which is a novel algorithm for Semantic Field subspace determInation. It uses hierarchical clustering to uncover semantic structures present in a set of data representations. The paper claims to improve efficiency of the clustering process by efficiently quantifying the semantic drift during clustering. The paper presents several results on text classification datasets and analysis experiments to evaluate their method.

### Strengths
1. The paper tackles an important problem of automatically uncovering latent semantic concepts within a set of data representations. 
2. The paper uses several visual illustrations (Fig. 1-3) that help the reader understand better.

### Weaknesses
1. The soundness and novelty of the paper are not substantial. Specifically, the paper builds on a simple agglomerative clustering algorithm and modifies the cluster merging logic using semantic drift.
2. The initial part of the paper is quite difficult to understand. This is mainly due to the inconsistent use of mathematical notations. Some of the claims in the Theorem proofs are incorrect. Please find my concerns below:

Definition 5 is confusing. What is matrix $\mathbf{A}$? It wasn’t defined before. What does it mean that $\mathbf{A}$ can be approximated by $\mathbb{S}$?

What does the notation $F_{sem}(\mathbb{S}) ≈ \Sigma, V^\top$ mean? How can a matrix be approximated using two matrices?

I’m unable to follow the intuition behind Eq. 7. What does the difference signify? Earlier $F_{sem}(\mathbb{S})$ was defined as a tuple of two matrices $\Sigma, V^\top$.

Line 265: In the example, it is unclear to me how Fig. 4 is formed after just 3 iterations. In Algorithm 1, Line 5, the merging happens in a cluster-wise fashion, there are 8 merges in Fig. 4.

$\sigma_i([A_x|O]) = \sigma_i(A_x)$: this isn’t true as there are additional 0 eigenvalues for the matrix on the left.

How is Equation 8 proved after Theorem 2? The approximation is an upper bound on the original value.

$r, r_1, r_2$ are not defined in Eq. 13.

3. The presentation of the experimental section needs to be improved. The section should start by stating the overall goal of the empirical results and analysis experiments. Currently, the reader is confused about several setup issues. Please find my concerns below:

The experimental setup in Section 5.2 isn’t clear to me. Are you using labels during training? If yes, then doesn’t the reported results significantly underperform simple neural network classification baselines on top of BERT?

If the paper is posed as a new hierarchical clustering method, it should present results of dendogram accuracy on clustering datasets.

### Questions
Please respond to the questions in the Weaknesses section.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a method to understand embedding spaces through hierarachical clustering. The authors define semantic fields, semantic field subspaces, and semantic shifts. In the quest of quantifying semantic shifts, the paper introduces a method based on singular values. Then, one of the paper's key contributions is a method to approximate the semantic shift without the need for SVD, getting speed-ups of 15-30x.

### Strengths
- an interesting method to understand embeddings
- the paper is very clear on the methodology part, building on a solid mathematical foundation

### Weaknesses
 - although the paper starts off with a generic motivation, it remains unclear how the proposed approach would tackle, e.g., mentioned problem of polysemiotic words. The paper introduces semantic fields and semantic shifts, but it does not clearly articulate how these concepts help in disambiguating polysemous words. For example, a word like 'bank' can refer to a financial institution or the side of a river. The paper does not explain how the hierarchical clustering and semantic shift analysis would differentiate these meanings, especially given that the clustering assigns each word to a single cluster.
- some assumptions seem to be made without justification. Unless I'm missing something, hierarchical clustering only ever assigns a point to a single cluster. This does not play well with the key motivation that words are polysemous and meaning determined by their use in context. The method seems to assume that each word has a single dominant meaning, which contradicts the initial motivation of analyzing polysemy. The hierarchical clustering, by its nature, forces a single assignment, which is a significant limitation when dealing with words that have multiple distinct meanings.
- the experiment section is not very clear about what embeddings are used. The paper mentions using embeddings but does not specify the type of embeddings used, which makes it difficult to reproduce the results and assess the validity of the approach. Are these simple word embeddings like word2vec or more complex contextualized embeddings from models like BERT? The lack of clarity on this crucial detail undermines the credibility of the experimental results.
- the evaluation seems weak (details below).
- limited to text embeddings

### Questions
Q1: How do you disambiugate polysemous words in the clustering? It seems that the method only assigns a word to a single cluster?

Q2: What embeddings are used for the experiments? Are they just tf-idf vectors? word2vec? contextualized embeddings from a language model?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper is well-structured and introduces a novel approach to understanding the semantic structure of embedding spaces. It presents the SAFARI algorithm, which aims to uncover hierarchical semantic structures within high-dimensional embedding spaces using a method based on hierarchical clustering and Semantic Shift analysis. The concept and motivation are both relevant and timely, given the increasing need to interpret embeddings in NLP. The technical aspects are adequately explained, though a few areas could benefit from additional clarification to enhance accessibility for a broader audience. Also, the authors evaluate the proposed model from diverse aspects, including token classification accuracy, computational complexity and visualization. This diverse experimental validation is interesting and throughout.

In conclusion, this paper presents a relatively new contribution to embedding space interpretability. Its main strengths lie in the innovation of the SAFARI algorithm and the diverse experimental validation. With further clarifications and added discussions on the limitations, this paper could fairly impact interpretability research in embedding models.

### Strengths
The introduction of Semantic Field Subspaces and the SAFARI algorithm is an interesting new approach. The approach is innovative and offers a structured way to interpret embedding spaces, potentially broadening the scope for further research in embedding interpretability.

The paper provides a comprehensive evaluation of SAFARI on multiple datasets, showcasing its performance in terms of accuracy, computational efficiency, and interpretability. This diverse evaluation adds credibility to the proposed method and its applicability across various real-world tasks.

The paper is well-written and well-organized. No English grammar errors are detected. The graphs and figures are presented with enough details. The proposed methods is well described.

### Weaknesses
Given all the merits mentioned in above, there is one relatively major defects: There is a lack of comparison, which is a common defects shared by many many papers. To this work, especially:

1. There is a lack of baseline models: The authors compared the classification accuracy and training time of the proposed model against SVM, KNN, Random Forest and BERT on the AG-News dataset. The only notable baseline models is the BERT model. All others, SVM, KNN and random forest, cannot be regarded as formal baselines. You need to find more published models to serve as baselines. Now that you adapt BERT, why not further include RoBERTa, Electra and XLNet? More published baseline models are required to make the comparison more convincing.

2. There is a lack of comparison scenario: The authors only conducted classification accuracy and training time comparison on the AG-News dataset. I think that is not enough. I am not familiar with this dataset, so I think the authors may provide a better background introduction to benchmark dataset used. Also, the authors may consider using more than one dataset for accuracy and training time comparison. In addition, beyond accuracy, how about F-1 score, precision, and recall comparison. Accuracy is sometimes not enough to fully evaluate the performance of a model.

### Questions
The authors need to find more published models to serve as baselines. Now that you adapt BERT, why not further include RoBERTa, Electra and XLNet?
 Why not conduct more comparisons on datasets other than AG-News? 
 Why not use F-1 score, precision and recall other than classification accuracy?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
**Title**: A Single Swallow Does Not Make a Summer: Understanding Semantic Structures in Embedding Spaces

**Summary**: The authors present a novel algorithm titled SAFARI, which is claimed to discover hierarchical semantic structures in embedding spaces.

### Strengths
The authors introduce a novel algorithm inspired by classical hierarchical clustering. Throughout their work, they attempt to provide deep motivations for their design choices, although these justifications often appear somewhat forced or artificial.

The study aims to address the interpretability of embedding spaces generated by models such as BERT and Word2Vec. This is one of the most crucial yet poorly understood components of deep learning architectures in Natural Language Processing (NLP).

The proposed algorithm and accompanying theory could prove valuable in various scenarios where practitioners seek to interpret a model's embeddings. This potential for practical application is a noteworthy aspect of the work.

### Weaknesses
### Major Comments

1. On line 160, the authors define the "interpretable semantics" of an embedding vector, $f_{int}(v)$. Their definition is based on the previously defined "close neighborhood" of said embedding vector, $\mathcal{N}(v)$. In particular, they define $f_{int}(v)$ as any subset of $\mathcal{N}(v)$. This implies that there are several "interpretable semantics" for each embedding vector. Furthermore, their notion of "interpretable semantics" is simply the intersection between the semantics of close neighborhood embeddings. It's unclear how this is "interpretable."

2. In lines 180-200:
   - The authors rightfully claim that $f_{sem}$ is not computable and introduce the concept of "semantic field subspace" to address this issue.
   - They motivate the choice to substitute a set of embedding vectors with a subspace of $\mathbb{R}^d$, presumably to make the "semantic field" computable.
   - However, their definition of "semantic field subspace" is still based on the non-computable $f_{sem}$, which seems to achieve very little.
   - In definition 5, they approximate the "subspace" with a finite set of vectors, which raises the question of why the "semantic field subspace" was introduced in the first place. This section feels like a convoluted and unconvincing justification for substituting $f_{sem}(v)$ with $v$. The argument would be more compelling without this section.

3. In line 197 (definition 5), the authors state that the subspace $\mathbb{S}$ can be approximated by a matrix $A$. This is unclear, as I am interpreting $\mathbb{S}$ as a simple subset of $\mathbb{R}^d$. Furthermore, the approximation $F_{sem}(\mathbb{S})\approx \Sigma,V^T$ is not well-explained. The authors should detail this approximation more clearly. It is not clear why the singular values and vectors of an SFS should approximate distances in the semantic space.

4. From what I can gather, each "Semantic Field Subspace" is simply a set of embeddings that the SAFARI algorithm found to be particularly semantically coherent. If this is the case, the name "Semantic Field Subspace" is somewhat confusing as it suggests a relation with fields and vector spaces that is not evident in the paper. I suggest the authors consider different nomenclature. I have similar concerns about the "Semantic Field" name.

5. On line 247, the authors use the threshold $\mu + 2\tau$ to detect new clusters. They should better motivate this choice. It might be more natural to use a hyperparameter to control how much semantic shift should be allowed in each cluster.

6. In section 5.2, it's unclear whether SAFARI accounts for the initial embedding training step (e.g., Word2Vec or BERT) in Figure 7. If not, the authors should mention this in the paper.

7. The authors use clusters generated by SAFARI for text classification and compare it to alternatives such as SVM, BERT, and KNN. However, from what I can gather from their code, it appears these algorithms are trained on the top-n entities rather than directly on the textual data (which would be natural for BERT). The authors should clarify the training procedure for the baselines, at least in the appendix.

8. The evaluation of SAFARI seems weak overall:
   - Section 5.2 tests for text classification, but SAFARI's purpose is not text classification.
   - Section 5.1 tests semantic field subspace alignment with BLINK entities at the dataset level, which seems less natural than using a single text classification dataset.
   - Section 5.4 presents only an anecdotal example showcasing SAFARI's ability to uncover hierarchical structures.
   - The absence of baselines makes it difficult to assess SAFARI's improvement over the state of the art.

   I suggest the authors consider a more comprehensive evaluation.

9. If SAFARI is indeed a clustering algorithm, shouldn't it be compared with other clustering algorithms rather than BERT or SVM?

### Minor Comments

1. On line 118, the authors mention the "deep learning" model $h:\mathcal{X}\rightarrow \mathcal{E}$, but don't use it meaningfully in the rest of the paper. It would be clearer to simply describe $\mathcal{E}$ as a set of embedding vectors, each representing a word in the vocabulary, possibly trained using a deep learning method.

2. On line 128, I believe the authors meant the power set of $\mathcal{M}$ (excluding the empty set) when writing $2^{|\mathcal{M}|}\setminus\emptyset$. It would be clearer to write $2^{\mathcal{M}}\setminus\emptyset$.

3. In lines 125-135, the authors' argument about words not being fully interpretable in isolation seems flawed. Their example of "Apple" as both a fruit and a tech company doesn't support their point, as $f_{sem}(\text{"apple"})$ could simply return $\{\text{"fruit"}, \text{"tech company"}\}$. The John Rupert Firth quote also seems irrelevant to their argument.

4. On line 154, the authors' method for characterizing the "close neighborhood" of an embedding seems arbitrary. Using k-NN with $k=3$ to exclude strict synonyms may exclude relevant embeddings if a word has fewer than 3 synonyms. A distance-based test might be more appropriate.

5. On line 167, the authors use the term "field" in a non-mathematical sense, which could be confusing. Consider changing the name to avoid this confusion.

6. In Algorithm 1, line 5 (line 224), the authors write $d_{sem}(\mathcal{C}_i,\mathcal{C}_j)$, but $\mathcal{C}_i$ and $\mathcal{C}_j$ are sets of vectors while $d_{sem}$ is a distance function on vectors. The distance function should be specified more clearly.

7. The authors use $\tau$ to denote standard deviation. It would be more conventional to use $\sigma$ instead.

8. On line 389, the BERT reference points to the wrong paper.

### Questions
My primary concerns center on the paper's narrative and experimental validation. I am open to reconsidering my assessment of the paper in a future revision, particularly if the following points are addressed:

1. Experimental Comparison:
   - Provide experiments that demonstrate superior clustering capabilities compared to other clustering approaches.
   - Note: Algorithmically generated datasets would be acceptable to keep the scale of experiments manageable.

2. Narrative Refinement:
   - Consider shifting the focus from "an interpretability tool" to a "clustering algorithm for interpreting embeddings."
   - Improve the nomenclature, or at least provide a clear rationale for the current terminology.

I hope the authors find this review constructive. Despite my current reservations about the paper, I believe there is potential in this work and look forward to seeing how it evolves in the review process.

### Soundness
1

### Presentation
1

### Contribution
2
