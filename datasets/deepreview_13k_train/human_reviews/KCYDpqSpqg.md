# SG-Adapter: Enhancing Text-to-Image Generation with Scene Graph Guidance

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
Recent advancements in text-to-image generation have been propelled by the development of diffusion models and multi-modality learning. However, since text is typically represented sequentially in these models, it often falls short in providing accurate contextualization and structural control. So the generated images do not consistently align with human expectations, especially in complex scenarios involving multiple objects and relationships. In this paper, we introduce the \textbf{Scene Graph Adapter} (SG-Adapter), leveraging the structured representation of scene graphs to rectify inaccuracies in the original text embeddings. The SG-Adapter's explicit and non-fully connected graph representation greatly improves the fully connected, transformer-based text representations. This enhancement is particularly notable in maintaining precise correspondence in scenarios involving multiple relationships. To address the challenges posed by low-quality annotated datasets like Visual Genome~\cite{krishna2017visual}, we have manually curated a highly clean, multi-relational scene graph-image paired dataset MultiRels. Furthermore, we design three metrics derived from GPT-4V\cite{achiam2023gpt} to effectively and thoroughly measure the correspondence between images and scene graphs. Both qualitative and quantitative results validate the efficacy of our approach in controlling the correspondence in multiple relationships.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes SGAdapter which solves the problem of using sequential representations for input text in recent text-to-image generation methods. They augment their approach with scene-graph-to-image generation due to the graph representations. SGAdapter introduces a small-scale adapter between StableDiffusion and the CLIP encoder for this task. They also identify the problem of casual attention masks for scene graphs. They curate a new dataset for scene-graph-to-image generation. The experiments show that SGAdapter can generate realistic images from more complicated input sentences than baselines.

### Strengths
1. The method is simple and straightforward in solving the identified problem.
2. The empirical improvement is significant.

### Weaknesses
1. Some figures are not clear.
2. Some confusing notations.

### Questions
1. L40 missing space between "CLIP model" and the citation.
2. The $\mathbf{M}^{\tau}$ in Eq. 3 can be named differently, e.g. triplet-triplet mask, to distinguish it apart from the token-triplet attention mask in Eq. 5.
3. For Fig. 2, I suggest putting some of the introduced notations in Fig. 2 to help the reader understand the paper, e.g. model $f$, embedding $\mathbf{e}, \mathbf{w}$, etc. Fig. 2 can also be improved by using more arrows between features or modules to make it more concise and clear. For example, the inputs and outputs on the right side of the figure should be indicated with arrows. Redundant word in L233 Eq (equation) 4. The visualization of the matrix and the given scene graph example do not match. There are 2 triplets with 6 tokens in the input scene graph. I think it is a good opportunity to show what is $\mathbf{M}^{sg}$ and $\mathbf{M}^{\tau}$ for the inputs here.
4. L267, $\mathbf{M}$ or $M$? 
5. In Eq. 5, what is the difference between $\mathbf{M}^{sg}$ or $M$?
5. I am confused about Tab. 2 and L413, is it about $\mathbf{M}^{\tau}$ or token-triplrt mask $\mathbf{M}^{sg}$. I thought $\mathbf{M}^{\tau}$ is for solving the problem of causal masks.
6. Fig. 1, I assume the add signs mean StableDiffusion + SGAdapter and Caption + Scene graphs. I think it can made clearer as initially I was not sure whether you were replacing captions with scene graphs or using both.

### Soundness
3

### Presentation
1

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
To correctly align text-image consistency for text-to-image task, especially in complex scenarios involving multiple objects and relationships, this paper proposes SG-Adapter to leverage the structured representation of scene graphs to rectify inaccuracies in the original text embeddings. A highly clean, multi-relational scene graph-image paired dataset MultiRels is constructed to address the challenges posed by low-quality annotated datasets. Qualitative and quantitative experiments validate the efficacy of the proposed method in controlling the correspondence in multiple relationships.

### Strengths
a. The proposed SG-adapter is effective in correcting the incorrect contextualization in text embeddings and enhancing the structural
semantics generation capabilities of current text-to-image models.

b. Both qualitative and quantitative experiments demonstrate SG-Adapter outperforms compared SOTA methods.

### Weaknesses
 a. The format of citations in this paper need be rectified.

b. This method requires the construction of a high-quality dataset, and it is mainly effective for the relationships within the constructed dataset, which will limit its generalization ability.

c. The quantitative results are insufficient and the author should provide more results to prove the its effectiveness.

### Questions
Can SG-Adapter solves the color bind problems?

### Soundness
3

### Presentation
4

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
This paper hopes to optimize the generation of entity interaction in text-to-image generation by introducing the scene graph structure into the adapter. The method is simple and clear and has achieved significant improvement compared to the baseline.

### Strengths
- The motivation is straightforward. The description of the problem and method is simple, clear and understandable.
 - Entity interaction information is introduced through scene graph to optimize the generation of entity interaction, which is relatively direct.
 - Judging from the demo and numerical comparison results, there are good results.

### Weaknesses
 - The novelty in method design is limited. It only performs an attention on the text embedding based on the scene graph relationship. It can even be considered as a replacement of the key and value values in the cross attention structure. Simplicity is not a disadvantage. If it is simple, direct and works, the author can provide some discussions to analyze the most important factors behind it.
Is the adapter structure important or is the scene graph information the most important? For example, in addition to the adapter, can simply injecting scene graph information through cross attention also obtain similar results?
And whether there are some situations where scene graph information is not applicable.
 - The experimental evaluation of entity interaction generation is not comprehensive enough. The scene graph detection method itself will also have a very obvious long-tail phenomenon for entity relationships. For entity interaction image generation, this should also be considered. Distinguishing and explaining according to the detection frequency in the training dataset will make the evaluation of the model more comprehensive and convincing. The author can try to divide buckets according to the frequency of scene graph detection, and finally give the results of each bucket and the average result.

### Questions
-  The currently shown results (Figure 3) seem to have at most two main bodies interacting with their accessories. 1) In the case of more main bodies, such as a crowd surrounding or three people facing away from each other; 2) For some pairs that may not be common in the training set, such as pandas riding on horsebacks, what is the generation effect like? This helps evaluate whether the sg-adapter has learned to generate general interaction relationships or just high-frequency combinations in the training set.
 - The effect of scene graph detection may not be 100% accurate. What will be the effect when the detection result conflicts with the meaning of the text itself? Will it be more serious for some freely input long texts? For example, when users use the text-to-image function, they often add a long string of magic prompts, such as 4K, realistic, specific lenses, etc. These may all have an impact on scene graph detection.
 - How many parameters need to be fine-tuned in the current adapter part? Will the size of the number of parameters affect the final effect? The analysis of this part may make the article more complete.

In general, I think the problem solved by this paper is quite important. However, I feel that the current method is not general enough and may be a temporary technique. When there is a specific need for interaction generation in a specific scene, fine-tuning based on the SG Adapter will have some improvement. But it does not fundamentally solve the problem of entity interaction. Because I think the introduction of the SG adapter will lead to the problem that entity interaction adds the long-tail problem of scene graph detection on top of the long-tail problem of interaction relationships in the training set itself. The impact on the community may be limited. If the author has more thoughts and ideas on this aspect, we can discuss them.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a Scene Graph Adapter for text-to-image generation that leverages scene graph to refine CLIP text embeddings. Additionally, a dataset of 309 images with relational annotations is proposed for evaluation.

### Strengths
1. The paper contributes a scene graph dataset with relational annotations, which adds value to the community.
2. The authors include their code in the supplemental materials.
3. Human evaluations are conducted to assess the effectiveness of the proposed method.

### Weaknesses
1. Experiments are conducted only on the proposed dataset, which is relatively small and may not provide a robust evaluation.
2. The method uses a Scene Graph to refine CLIP text embeddings, which may be overly simplistic. I think the adapter should also change the parameters of the Stable Diffusion.
3. The latest method compared in Table 1 is from 2023. Including more recent methods would strengthen the comparative analysis.
4. The authors note that fine-tuning Stable Diffusion on a small dataset can degrade FID (shown in Table 1). Fine-tuning on a larger dataset, such as Flickr30k Scene Graph, is recommended.
5. Human evaluation is conducted on only 20 cases (from the proposed test set). Expanding the test set could improve the reliability of these results.

### Questions
See the detail in the weaknesses

### Soundness
3

### Presentation
2

### Contribution
2
