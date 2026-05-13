# Revisit and Outstrip Entity Alignment: A Perspective of Generative Models

- Decision: Accept
- Scores: 6, 6, 8

## Abstract
Recent embedding-based methods have achieved great successes in exploiting entity alignment from knowledge graph (KG) embeddings of multiple modalities. In this paper, we study embedding-based entity alignment (EEA) from a perspective of generative models. We show that EEA shares similarities with typical generative models and prove the effectiveness of the recently developed generative adversarial network (GAN)-based EEA methods theoretically. We then reveal that their incomplete objective limits the capacity on both entity alignment and entity synthesis (i.e., generating new entities). We mitigate this problem by introducing a generative EEA (GEEA) framework with the proposed mutual variational autoencoder (M-VAE) as the generative model. M-VAE enables entity conversion between KGs and generation of new entities from random noise vectors. We demonstrate the power of GEEA with theoretical analysis and empirical experiments on both entity alignment and entity synthesis tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce the entity synthesis task and propose an M-VAE model that can convert entity embeddings back to the native concrete features. They also propose prior reconstruction loss and post-reconstruction loss to control the generation process. Empirical results show that entity synthesis has a positive effect on entity alignment.

### Strengths
1. Through theoretical analysis from the perspective of generative models, the authors point out that generative objectives contribute to the optimization of EEA models.
2. A generative EEA framework is proposed. By introducing reconstruction loss and distribution matching loss, GEEA further improves the performance of previous EEA models.

### Weaknesses
The author needs to briefly introduce the metrics of alignment prediction. Is it consistent with the EEA model used in GEEA?

The proposed M-VAE model is a generative model, but there are no other generative models compared to baseline models. It's better to compare with some GAN-based models like NeoEA("Understanding and improving knowledge graph embedding for entity alignment." International Conference on Machine Learning. PMLR, 2022.)



### Questions
GEEA is a general method, but all experiments are completed in multi-modal settings. In a single-modal scenario, will GEEA still be competitive?
The time and memory overhead of GEEA should be reported. 
The number of entities in each data set is 15k. Can GEEA be run on larger datasets(such as 100k)?
Additionally, there are some other problems:
There are two "right hand" in the above line of Eq.43, one of them should be "left hand".
The weight of prediction matching loss is not included in Table 6.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the task of entity alignment. The authors introduce a generative EEA framework, leveraging the mutual variational autoencoder (M-VAE) to facilitate the encoding and decoding of entities between source and target KGs. A series of experiments have been executed to ascertain the efficacy of the GEEA, and the results affirm the prowess of the model.

### Strengths
The experiments showcased provide evidence of the efficacy of the GEEA model.

### Weaknesses
 - The paper would benefit from enhanced clarity. Several concepts are mentioned without a clear definition, leading to potential confusion for readers. See the questions listed below for specifics.
- The objective of prior reconstruction could be made more comprehensible. There's ambiguity regarding the priors of features in different sub-embeddings. Specifically, when dealing with images, how does one retrieve its original, tangible feature? The paper does not clearly articulate how a discrete representation of an image is obtained, especially since the image data itself is continuous.
- The paper could provide a more extensive set of experiments to offer insights into the rationale behind the design of individual components.

- Eq. (19)  is missing a right parenthesis.

### Questions
- Could you elaborate on what constitutes the multi-modal information within the knowledge graph (KG) area?
- What types of attribute information are being referred to in this context?
- How would you define "sub-embeddings" in the framework?
- What does $\mathcal{L}_{mf}$ represent within the paper?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a M-VAE based generative approach for embedding-based entity alignment. This paper theoretically justified the plausibility of formulating the problem as a generative task that is akin to what recent GAN-based EA approach has done. Specifically, for the problem with dangling entities, different from prvious work that has focused on detecting such dangling points, this work proposes a novel solution of entity synthesis. Experiments are done on common datasets shared by most prior works on this topic, with fair comparison ensured (by removing entity names, which has been violated by some prior works).

### Strengths
The contributions of this paper are from multiple perspectives. The plausibility of a generative formulation of the problem is theoretically justified. For the recently proposed dangling entity problem, a novel solution of entity synthesis is proposed to fulfill the missing targets in the target-side KG. Evaluation has covered the traditional setting of close-space entity alignment to show the effectiveness from that perspective, and a new, plausible setting is proposed for entity synthesis to show the effectiveness from this new angle of solution. The presented method and experiments look sound.

### Weaknesses
While the proposed entity synthesis approach leads to an essentially different solution to dangling entities from the previous dangling detection approaches, I wonder if the proposed approach can still can contribute to (and be compared with) dangling detection.  
There is one detail that I might have missed: in the close-space EA setting without considering dangling entities, is there any technique of constrained generation/decoding that ensure the generation to fall into the candidate space?

### Questions
Please see weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
