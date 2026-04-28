# SemCLIP: Aligning vision-language encoder models to semantic spaces for stability in retrieval

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Vision-language models (VLM) bring image and textual representations close together in a joint embedding space to tackle many tasks ranging from image captioning to text-to-image retrieval. For such models to be reliably used in cloud vector stores, it is important to have a stable association between images and text such that synonymous queries bring up the same images or have a high degree of overlap. Current textual representations based on transformer models used to build the VLMs cannot adequately capture linguistic similarities to ensure such stability. In this paper we develop a database of linguists-curated similarity list of words derived from Wordnet, and train a semantics preserving textual embedding. We then train an alignment transformation to map existing VLM (CLIP) embeddings to bring synonymous embeddings closer while also preserving image-text similarities. The alignment transform is learned from textual embeddings alone thus avoiding large-scale retraining of VLMs from image-text pairs.   This simple method outperforms other methods of creating image-joint text embeddings including even those by fine-tuning the encoders using the same synonyms lists. Results of analysis and comparison  on multiple benchmark datasets  is indicating both stable and improved quality of retrieval. The dataset of similarity lists and the semantics-preserve textual embedding itself can be employed in a variety of ways for other downstream tasks and will be made available for other researchers.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors developed A database of 114,000 linguists-curated similarity lists of words from a constrained traversal of Wordnet thesaurus to cover all English language nouns and use a representation to capture their sense context explicitly. And then a semantics-preserving textual embedding was trained to discover expanded synonymous relations between terms.  A method was developed to align a VLM embedding.

### Strengths
1. This paper identify and address the issue of instability in VLMs when dealing with synonymous queries.

2. The authors develop a dataset of linguist-curated similarity lists , followed by an alignment transformation to map existing VLM embeddings to the semantics-preserving textual embedding. 

3. Abound experiments provides extensive empirical evidence to support the effectiveness of SemCLIP model, including comparisons with multiple benchmark datasets and other CLIP variants.

### Weaknesses
1. The SemCLIP model is developed only for nouns in the English language. This limitation narrows the applicability of the model, as many queries involve verbs, adjectives, and adverbs, which are not addressed by the current approach. The restriction to nouns limits the model's ability to handle complex sentence structures and nuanced semantic relationships expressed through other parts of speech.

2. The database of similarity lists, while valuable, may introduce bias based on the linguists' perspectives and may not capture the diversity of language use across different domains. The manual curation process, while ensuring high quality, could inadvertently reflect the annotators' understanding of semantic similarity, potentially overlooking less common but valid interpretations. This could lead to a skewed representation of semantic space, particularly for specialized or technical domains.

3.  The WSD tool's accuracy rate of around 80% could introduce errors in the alignment process. While this level of accuracy is reasonable, the 20% error rate could propagate through the model, affecting the quality of the learned embeddings, especially for polysemous words where incorrect sense disambiguation could lead to inaccurate semantic representations.

### Questions
1. The alignment transform of image embeddings from VLM to SEM space is confusing. Image embedding and text embedding are directly equated, which may overlook the semantic differences between images and text.

2. How to determine the distance of semantic similarity, gamma_j ?

3. The Transformation Mapping stage in Fig. 3 lacks arrows connecting to other stages, making it difficult for the reader to intuitively understand how the output vector is utilized in the subsequent stages.

4. Why STE perform worse in antonyms dataset?

5. Long-tail or rare synonyms that may not be well-represented in WordNet could affect semantic text embedding.

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
This paper addresses the problem of image retrieval with synonymous text. It develops a dataset of linguists-curated similarity lists of
words and trains a semantics-preserving textual embedding (STE) to which the VLM embedding is aligned. Experiments on 13 benchmark datasets demonstrated the effectiveness of the proposed method.

### Strengths
1. This paper is well presented, with clear figures and organizations.
2. This paper develops a dataset for synonymous text understanding.

### Weaknesses
1. The description of how to construct the similarity list dataset is not clear enough.
 - It would be better to give out a figure for a more intuitive illustration.
 - Is the synonymousness defined for both nouns and phrases? Is the similarity defined with binary values (0/1) or continuous values between 0-1? Any difference?
 - It is concerned that are there any cases in two worlds with the same meaning on single nouns but different meanings in sentences?
 - How to ensure that the items in the dataset are diverse enough, reasonable, and frequently used?
2. Lack of important experiments.
 - Does the learning of synonymous text degenerate the retrieval of general words? Tables 2 and 3 only show the results of querying using synonyms of nouns but no general words.

### Questions
1. From methodologies, it seems that only the text encoder is updated for better alignment between synonymous pairs, while in Figure 2, image embeddings of J1 and J2 are pulled, how? Is the original VLM also fine-tuned?

### Soundness
2

### Presentation
2

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
The paper focuses on establishing stable association between images and texts, to make synonymous queries bring up the same images or have a high degree of overlap, and propose a SemCLIP framework, which consists of two main step, semantic text embedding and alignment transform. Besides, the paper develops a database of linguists-curated similarity lists of words. Performance comparison on multiple benchmark datasets show the effectiveness of the proposed framework.

### Strengths
The paper proposes a framework to transform the VLM embeddings of semantically close terms and their associated images to place close together to ensure retrieval stability, which is practical for vector-database-based data managing.

### Weaknesses
1. The novelty is limited. The proposed SemCLIP framework is mainly composed of semantic text embedding and alignment transform. However, they are all implemented through existing simple algorithmic ideas, without introducing in-depth perspectives on semantic alignment. The semantic text embedding, while utilizing a curated similarity list, essentially trains a contrastive model which is a common practice. The alignment transform, relying on nearest neighbor distances in the VLM space, also lacks a novel theoretical contribution. The paper does not delve into the underlying complexities of semantic relationships or explore more sophisticated methods for capturing these nuances beyond simple distance metrics.

2. In Modeling SemCLIP transformations (page 4), in the computation of alignment transform of images (i.e., equation 4), the determination of image representations replies on the distance between the image and its nearest text in VLM space. This implies that SemCLIP acknowledges the validity of relative distance between images and texts in VLM space, which conflicts the main claim about the loss of sensitivity to linguistic similarity in VLM space, in paper. The method uses the VLM space to find the nearest text embedding to an image, and then uses this distance to transform the image embedding. This seems to assume that the VLM space is reliable for image-text distance, which contradicts the paper's argument that VLM embeddings are not semantically consistent.

3. The writing should be improved. First, the notation in this paper needs further refinement and standardization. Secondly, some of the statements in paper are confusing and need more in-depth explanation. For example, lines 192-193 “Note that the distance is a function of the word itself, since some words have more synonyms than others.”, lines 290-291 “We developed a contrastive embedding model that captures the essence of the similarity in the curated similarity lists in a numerical formulation”, and so on. Thirdly, The implementation of semantic text embedding and alignment transform in section 4, 5 and the previous section 3 seem to be conceptually separate, and need further re-organization.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates the semantic matching of vision and language embedding vectors. Specifically, textual synonyms should match with similar images, but current vision-language models like CLIP often fail to retrieve similar images for synonymous terms. To address this issue, the paper proposes SemCLIP, which includes a new database of linguist-curated similarity lists of words. Additionally, it trains semantic-preserving textual embeddings (STE) to capture synonym relationships and aligns vision-language embeddings with STE to produce semantic-preserving embeddings for improved retrieval.

### Strengths
1. This paper addresses an important challenge in current vision-language embedding models, where synonyms with the same semantics are not well-mapped within vision or language embeddings.

2. Releasing the synonym-focused dataset as an open-source resource would be a valuable contribution to the community.

3. The evaluation on retrieval using images and labels (measured by mAP and NDCG) is also meaningful, providing a more nuanced comparison than traditional image-to-text matching, which may involve overlapping "same" semantic text.

### Weaknesses
1. Figure 2 is somewhat difficult to understand; it would be helpful to include explanations of each component (A, B, C, D, and J1, J2) in the caption.

2. It would be beneficial to report standard image-to-text or text-to-image retrieval metrics, such as Recall scores on MS COCO and Flickr, for comparison with existing CLIP methods.

3. The notations in the methods section are complex; it is unclear at times whether they refer to data samples or embedding vectors. Clarifying these distinctions would improve readability.

### Questions
I wonder if general CLIP models with larger backbones and training on large-scale datasets (in the billions), such as CLIP ViT-bigG, might not suffer from the synonym problem, as they are more likely to include diverse examples with synonyms in training and may be sufficiently generalized to handle synonym issues. Do you have any experimental results with these stronger VLM models?

### Soundness
3

### Presentation
3

### Contribution
3
