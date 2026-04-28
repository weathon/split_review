# Leveraging Knowledge Graphs to harvest a high-quality dataset for efficient CLIP model training

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Vision-language contrastive learning based on the CLIP method has been instrumental in driving recent advancements in computer vision. However, high quality CLIP models are based on very large datasets. This makes them expensive to train and hampers the scientific analysis of these models. We show how to train a CLIP base-size model efficiently for a broad domain on a much smaller amount of data. We demonstrate this specifically with the automated creation of a dataset named LivingThings with 8.9M images of animals and plants and 12.2M texts. The dataset is obtained via focused image-search queries of three kinds: entity queries (e.g., "eagle"), entity-attribute queries (e.g., "bushy tail of a fox"), and type-attribute queries (e.g., "insect on a leaf"). The entities and types, as well as some of the texts, are derived from the WordNet and Wikidata knowledge graphs, the attributes are obtained via LLMs. We train a CLIP model from scratch on LivingThings and evaluate it on ImageNet, iNaturalist, and CUB for object classification and OVAD and CUB for attribute classification. On the broad target domain of animals and plants, our model achieves comparable, and sometimes even much better performance than models that have orders of magnitude more parameters or training data. For instance, our ViT-B-32 model improves over much larger state-of-the-art CLIP models on the iNaturalist 21 object classification task. We will publicly release our code and dataset.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tries to propose a controlled-generated image-pair dataset, where the query entity is from the Wikidata knowledge graph, and the attribute and search query are generated using LLMs. Then, search engines are used to collect the images. Later, it proves that the 8.9M dataset can train the model with comparable performance of larger dataset on living things categories.

### Strengths
1.	The goal is to investigate whether a high-quality small-scale dataset can achieve comparable performance to the CLIP model trained on large data.
2.	Create the datasets that are based on the Wikidata knowledge graph, ensuring wide data coverage over different categories.
3.	The query creation + searching is a good way to construct high-quality dataset.

### Weaknesses
1.	This paper collected the LivingThings dataset covering animals and plants, but it is still small scale and the model trained from it cannot compare with SOTA CLIP model. I wonder if anything this paper can do to further improve the SOTA CLIP model by using this datasets? 
2.	This dataset only has a local coverage of animals and plants. But I wonder how can this data collection pipeline be further scaled up to the next DataComp or LAION sized dataset. If the author keeps increasing the entity number from wikidata, it might be piled up by including other categories, and finally still result in a very large dataset in billion scale, then you will have to prove it is better than LAION or DataComp
3.	I would expect more detailed experiment analysis and ablation study about the effect of attribute number, number of entities, scaling law, etc.
4.	The quality control of data collection seems to be loose. Seems it cannot guarantee the alignment of text and image is high. Why not use a CLIP to filter out the unaligned image-text pair?

### Questions
I think the main concern is that the dataset itself is less in data analysis and experimental ablation. Also, it cannot surpass the SOTA CLIP, and didn't show clearly how it can help boost SOTA CLIP.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes to harvest small-scale but high-quality data for CLIP training leveraging existing knowledge graphs. For a proof of concept, the paper focuses on visible living things including animals and plants. By extracting entities from knowledge graph, generating attributes and building queries using LLM, and collecting images using Google API, the authors created a dataset named LivingThings with 8.9M images and 12.2M texts. With the collected dataset, the authors trained a CLIP ViT-Base model from scratch and achieve comparable or better performance over large-scale trained CLIP variants.

### Strengths
1. The paper is well organised with clear motivation. The overall flow is easy to follow.

2. The work contributes a high-quality dataset named LivingThings covering animal and plant entities, which I believe would benefit the community.

3. This work is quite resource-efficient, training a CLIP-style model for visual recognition using only 8 RTX 2080 Ti GPUs. And each round of training only costs ~30 hours.

### Weaknesses
1. The model studied in this work is ViT-Base, a small variant of the CLIP family. Therefore, the scalability of model size using the LivingThings dataset might need further verification. It is unclear how the performance would scale with larger models such as ViT-Large or even larger variants, which are commonly used in state-of-the-art CLIP models. The current results only demonstrate the effectiveness of the dataset on a relatively small model, and it remains to be seen if the dataset can support the training of more complex models with significantly more parameters.

2. The method relies on the prior knowledge of the root entity (e.g., plant and animal) when collecting the dataset. Therefore, the proposed paradigm seems only suitable for visual recognition in a single or limited number of domains. The manual definition of root entities limits the generalizability of the approach. Expanding to new domains would require identifying and manually defining new root entities, which could be a time-consuming and potentially subjective process. This contrasts with methods that aim to learn representations across a wide range of domains without such manual intervention.

### Questions
1. LivingThings has a total of 8M images. I am curious about the model performance of using even fewer images, e.g., 100K, or 1M.

2. How would the proposed paradigm be extended to build a CLIP-level model that covers unlimited domains? And how many images might be needed to match the performance of standard CLIP models? Just some analyses would suffice.

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
3

### Summary
This paper proposes a new dataset, named LiveThings, with 8.9M images and 12.2M text scale, leveraging the knowledge graph, Large Language Model, and image search engines. Specifically, the knowledge graphs (e.g., WordNet, Wikidata) output the entity classes and natural types, following the generation of attributes via LLMs. Following the image searching and filtering process, the author proposes a high-quality datasets for animal and plant, which is for biological domain.

### Strengths
1. The author proposes a new dataset, LiveThings, to efficiently train the CLIP-based model, which could be leveraged for future works involving foundation model construction.
2. Through extensive experiments, the paper demonstrates the superiority of utilizing automatically generated datasets, especially in efficiency.
3. The paper is well-written, allowing readers to understand easily.

### Weaknesses
1. It seems necessary to consider the additional baseline [1]. The proposed dataset, which focuses on biological information containing animal and plant entities, shares similarities in size with another dataset called TreeOfLife [1] that also contains biological data and spans 10M sizes. Therefore, to better demonstrate the advantage of using a knowledge graph in developing their dataset, the authors should perform a comparative analysis with a model that has been trained on the TreeOfLife dataset.

Since it was trained in the biological domain, such as animals and plants, with attribute information, it is natural that it performs well in attribute classification and species classification while showing low performance on other domains (e.g., other in ImageNet). Therefore, it seems necessary to compare it with models trained in the biology domain using a dataset of a similar scale (i.e., TreeOfLife) to validate the effectiveness of leveraging knowledge graphs.

2. There is no experiment for other domains to support the claim that this approach can be used for any domain covered by the given knowledge graph. In the whole paper, only the biological domain is covered, but it is crucial that this approach indeed can cover other domains, such as urban and molecular. The reason for this doubt is that the entities in the knowledge graph may not be diverse in other domains, or it might not be effective in extracting natural types. Therefore, it seems necessary to conduct experiments to prove this.

3. The quality of the image search results is a concern. The paper mentions using both Google and Bing image search engines, but it's unclear how the results from these two sources are combined or filtered. Given the known variability in search engine results, especially for more specific or niche entities, it's crucial to understand the impact of using both search engines on the overall dataset quality. It is possible that the Google search results may introduce noise or unaligned images, which could negatively impact the performance of models trained on this dataset. A more detailed analysis of the search results and their impact on the dataset quality is needed.

### Questions
The goal of this paper is to create high-quality data using the knowledge graph, but it seems to be utilized only for extracting entity classes or natural types. To fully leverage the knowledge graph, it appears necessary to use the structural information about the entities within it. Extracting entity-related attributes from the knowledge graph is more natural than using an LLM. 
Regarding it, what if the attributes are extracted based on the structural information within the knowledge graph instead of using LLMs? I think it is more natural to fully utilize the knowledge graph's information.

### Soundness
3

### Presentation
3

### Contribution
2
