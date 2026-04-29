# We Should Chart an Atlas of All the World's Models

- Decision: Accept
- Scores: 6, 7, 8

## Abstract
Public model repositories now contain millions of models, yet most remain undocumented and effectively lost: their capabilities, provenance, and constraints cannot be reliably determined. As a result, the field wastes training time and compute, propagates hidden biases, faces intellectual-property risks, and misses opportunities for model reuse and transfer. In this position paper, we advocate charting the world's model population in a unified structure we call the Model Atlas: a graph that captures models, their attributes, and the weight transformations connecting them. The Model Atlas enables applications in model forensics, meta-ML research, and model discovery, challenging tasks given today's unstructured model repositories. However, because most models lack documentation, large atlas regions remain uncharted. Addressing this gap motivates new machine learning methods that treat models themselves as data and infer properties such as functionality, performance, and lineage directly from their weights. We argue that a scalable path forward is to bypass the unique parameter symmetries that plague model weights. Charting all the world's models will require a community effort, and we hope its broad utility will rally researchers toward this goal.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors argue that we should maintain a huge graph for all ML models in which nodes are models and edges are weight transformations among models. The vision is helpful.

### Strengths
S1: The idea of building up an Atlas of all models is interesting.

S2: Leveraging graph approaches makes senses.

### Weaknesses
W1: The findings are not very novel. There is a lack of technical depth.

W2: Computing edges among models is not very clear.

W3: Insights on how to leverage the Atlas are missing.

### Questions
Q1: How to compute the edges among models exactly?
Q2: See W1
Q3: See W3.

Comments:
C1: Building up connections among small models is still valuable to understand and study the historical development of models.

### Presentation
3

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The authors argue that the ML field should work on developing an atlas of ML models. This atlas would take the form of a directed acyclic graph (DAG) where nodes would represent trained models (along with various metadata) and edges would represent weight transformation operations like fine-tuning or quantization. This would enable us to perform a holistic analysis on the space of models, such as: imputing missing information about models which could help with model validation, analysis of patterns that would help improve our understanding of this space, and improve the efficiency of training new models by leveraging information about existing models. The authors also outline several technical challenges that stem from the pursuit of building model atlases, such as the difficulty of determining model lineages due to the permutation symmetry of weight matrices.

### Strengths
**(S1)** The authors observe the extremely rapid increase in the space of available pre-trained models and correctly notice an opportunity to analyze this space in a holistic and principled way.

**(S2)** The paper presents an interesting initial analysis of this space in order to bolster the presented arguments.

**(S3)** The presentation is pretty clear and easy to follow.

### Weaknesses
**(W1)** The motivation for the proposed model atlas could be improved by providing a much stronger and clearer emphasis (especially in the introduction) on the problems we are facing as a field without such an atlas. As an example of a problem statement in the introduction, the authors write: "Platforms like Hugging Face (HF) now host over 1.5 million models, with over 100k added each month (see Fig. 2). Yet, most models remain undocumented and effectively lost." The problem of undocumented models is treated as self-explanatory, and it is unclear what it means for models to be "effectively lost". Even though I can appreciate the arguments and motivation provided in the remainder of the paper, I think that the motivation in the beginning of the paper (i.e., abstract and introduction) can be made much stronger if there were a clear emphasis on what we are missing out as a field by not having comprehensive model atlases available.

### Questions
**(Q1)** The authors write: "Neural networks are complex, opaque functions. They do not readily reveal details about their training data or predecessor models. However, this information is critical, particularly for the creators of training datasets or upstream models." How exactly is this information critical for creators of datasets and models? It would be good if the authors explained this in the paper.

**(Q2)** The authors write: "As shown in Fig. 5, quantization is rare in CV models (fewer than 0.15% of all models in this pool) compared to NLP. This suggests that vision models have not yet reached the scale where inference cost necessitates quantization." Is this the only possible conclusion? Could it be that quantization is harder to achieve effectively for CV models?

### Presentation
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Paper position: There are millions of models these days, largely many of which are poorly documented. Charting an atlas of models would enable applications in model forensics, meta-ML research and model discovery.

The paper starts with discussing substantial benefits of having a global model atlas in model forensics, meta-ML research and model discovery. Using a smaller subset of 60,000 models from Hugging Face, an exemplar model atlas is constructed and visualised, showing some interesting trends. For example, discriminative models primarily use fine-tuning, while generative models have widely adopted adapters.  Then, the paper argues for the need for ML-based approaches, using models and their weights as input data, to impute missing nodes, edges, and their attributes in the atlas, by showing the shortcomings of existing relevant solutions. Here, some alternatives to existing solutions are proposed: avoiding equivariance, graph kNN, learning on functional features and learning directly on weights within a connected component. Next, open challenges in model atlas charting are discussed. And finally, alternative views are considered and addressed.

### Strengths
This is a good, well-written, well-rounded paper targetting a recently emerging, topic. It gives a thorough assessment of existing problems with millions of models and ways to build a global atlas of models and open challenges associated with the building process. Discussed potential benefits in model forensics, meta-ML research and model discovery are substantial. Arguments are well-supported with properly cited evidence. The figures are compelling. The position is clearly one that is debatable.  Alternative views are update-to-date and practical, and are addressed with reasonable arguments.

### Weaknesses
I do not see any major weakness in the paper. It has a strong, practical, and valid view point.

### Questions
I do not have any question. This is a good paper overall. My only concern is that as I have not followed closely the development of recently emerging foundation models, I tend to strongly agree on the benefits described in the paper. Therefore my judgment may be positively biased.

### Presentation
4
