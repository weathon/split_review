# Few-shot Species Range Estimation

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Understanding where a particular species can or cannot be found is crucial for ecological research and conservation efforts. By mapping the spatial ranges of all species on Earth, we could obtain deeper insights into how global biodiversity is affected by climate change and habitat loss. However, accurate range estimates are available for a relatively small proportion of known species. For most species, we have only have a few prior observations indicating the locations where they have been previously recorded. In this work we address the challenge of training with limited observations by developing a new approach for few-shot species range estimation. During inference, our model takes a set of spatial coordinates as input, along with optional metadata such as text, and outputs a species encoding that can be used to predict the range of a previously unseen species in feed-forward manner. We validate our method on two challenging benchmarks, where we obtain state-of-the-art performance in predicting the ranges of unseen species, in a fraction of the compute time, compared to recent alternative approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors tackle the problem of predicting the geographic range of a biological species given a small set of opportunistic observations, thus focusing on the few-shot setting. This is done via in-context learning: at training and inference time, a set of presence locations are given to the model, along with a textual description of the species range or habitat. This means that it is possible to obtain predictions for a species not seen during training, as long as a few presence locations and/or textual description are available.

### Strengths
1) The paper is well written and structured.
2) Instead of learning a species embedding per species, as done in LE-SINR, the authors propose to use a few (20) presence locations as the species embedding. This is makes FS-SINR naturally adapted to few-shot in-context learning.

### Weaknesses
1) The novelty wrt LE-SINR seems to be quite limited, and is not explicitly addressed. Section 3.2 clearly addresses the contribution wrt SINR, but I could not find the same for LE-SINR. Other than the fact that FS-SINR uses a transformer to combine the different data modalities, the main difference is that FS-SINR makes use of 20 locations per species during training. However, the ablations don’t explore which of the components contribute the most to the improved results. This could be easily verified by using a learnable species token that can be given to the transformer, rather than the context locations. It is unclear if the transformer architecture itself is the main driver of performance gains, or if the in-context learning approach is the key factor. The lack of ablation on this point makes it difficult to assess the true contribution.
2) Even though the fact of using in-context locations is the main contribution of this work, I found very little detail about this aspect. The ablation studies do show that the improvement of adding more locations slows down after 20 are added (and up to 50 are studied), but I could not understand if the authors studied using more than 50 in-context locations. In addition, I could not find information about how these locations are selected, and whether the same set is kept during the whole training procedure, or whether the in-context locations are dropped from the training set. The paper lacks a clear description of the sampling strategy for these in-context locations, and how this might affect the overall performance. The absence of this information makes it difficult to reproduce the results and understand the sensitivity of the method to different location sets.

### Questions
1) Is the improved accuracy due to the in-context locations or due to the transformer model used to get the species embedding? The ablation study suggested in the previous section could help answer this question.
2) How exactly are the in-context locations dealt with during training? How much does a different choice of test-time locations affect the results?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a method for few-shot species range estimation building on the SINR paper and the idea of adding context information in the form of textual information about range or habitat as was presented in the LE-SINR paper. Tokenized locations where a species has been observed are combined with context information in a transformer module along with a class token and register token. For a new location, the output class token of the transformer is passed though a small MLP and combined with the embedding of the query location to produce the final prediction.

### Strengths
- The paper is overall clear and well-written
- The main limitations are well identified. 
- Several ablation studies are provided to anticipate different questions that could arise.
- The problem that the paper tackles (species range estimation in the few-shot setting) has not been explored much before but could have important impact in ecology. 
- The proposed method outperforms other existing methods (which haven't been designed for the context of FS learning specifically) but more importantly enables predicting range maps for previously unseen species without any retraining, which could make it appealing in a real-life application setting.

### Weaknesses
 - Limited technical novelty and limited ecological analysis: this paper builds on LE-SINR and SINR, the main difference being the stack of transformer blocks used to combine text and location data. I also understand this work builds on previous work, and thus it is common in the machine learning context to not question certain design choices (the choice of LLM for the text encoder, the evaluation metrics, the different types of analyses done), but as this is a different application context that is put forward (few-shot setting), it would make the paper really more convincing (and appealing to ecologists who might use this method) to dive deeper in an ecological analysis of the results. (see some questions in the questions section)

- One of the main limitations I see of this work is pointed out by the authors themselves, i.e. the fact that the same set of locations will always give the same range map. Proposing different possible range maps could definitely be more appealing to downstream users of such a method, especially when very few locations are provided.

### Questions
- I would like to confirm the methodology used for doing the different runs that make up the error bars in the few-shot setting.  For a given test species,  are the provided context locations of the different runs different? 

-   Have the authors looked into how /if  the performance of the model changes depending on the type of habitat /  the more or less restricted range that species have? 

- It seems in the Black and White Warbler example that predictions in South America go up as more examples in North America and Central America are added. As the authors point out, the method could be more effective in practice if a way to handle absences is added. 
I wonder if there is a way to consider adding information not only about range and habitat but also about the family/ genus of the species, and whether that could help having more precise predictions. 

- The following question is connected to the previous point. I understandable this work builds upon previous SRM estimation papers using their datasets and metrics, but I wonder if other evaluation metrics than MAP in the few-shot setting could be added.
Have the authors looked into analyzing the performance by taxonomic group / geographical distribution of the species? I suppose there is some bias in the data used for training (the majority of the data would be for species observed in North America and Europe) and it would be valuable to understand to what extent this method works for less well surveyed regions  because from a practical standpoint it seems those regions would be where few-shot learning would be the most helpful. 
To phrase it differently, this paper frames an important and relevant problem but if such a method is to be truly used in a real-life context, some more focus could be put into showcasing examples that are ecologically relevant, for example showing the performance for different groups of species depending on the number of observations available in the training set. 

- In general, it would be interesting to have a bit more ecologically relevant analysis of the results. I really appreciate the effort of the authors to show examples of concepts learned by the text encoder in the appendix, but it would perhaps resonate more in the ecology community if there was some analysis showing to what extent the language encoder learns taxonomical hierarchy. 



Minor comments about figures: 
- Unless the locations overlap, it seems the same figure is provided for Hyacinth Macaw on rows-5 of Figure 4. Perhaps it would be helpful to just zoom into the South American region (I don’t see 5 or 10 context locations)
- The FS-SINR (No Train or Eval Text) model line is quite hard to see in figure A1 
- Numeric results of Figure 3 could be reported in a table in the appendix to make it easier to read the overlapping error bars of different models as the number of samples increases. 
- In the appendix figures A7 and A8 it would be nice to show that the textual descriptions are for range and habitat. 
- I would have liked to see some error bars for the ablation studies. I understand this is appendix content, but it makes it a bit difficult to agree fully with certain statements, e.g. in figure A2: "we observe the trend that as more data is  used, performance increases" It seems that allowing for a higher maximum number of  training examples during training does not necessarily lead to better performance in the case when  textual information is provided in the form of range or habitat description. I read the figure as showing that initializing from different SINR models that have seen greater number of examples for each species does not make much of a difference when textual data is provided.

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
5

### Summary
This paper addresses the task of species range estimation, which is represented as a location-conditioned probability of observing an individual of a given species. Unlike previous approaches, this work does not explicitly model a given species (such as from a species label or an image of the species). Instead, the idea is to predict a species vector from a set of sparsely sampled observations and a textual description (which could include a range or a habitat description). A location embedding is estimated based on each location of interest. The final per-location probability is computed by passing the dot product of the species encoding and the location encoding.

### Strengths
1. This seems like a new setting for species range estimation, addressing the important long-tail problem.
1. The writing is clear and the methods are sensible.
1. It should be easy to replicate the architecture at a high level but important details about the specific modules are missing.
1. There is some nice discussion of the limitations of the work.

### Weaknesses
1. The methods are sensible, but there aren't any significant theoretical/technical contributions.

2. The paper ignores some of the most important issues related to making this a practical system for real-world use cases (dataset bias and uncertainty modeling). On the uncertainty modeling side, consider Figure 4, where the difference between range maps between 1 and 5 samples is relatively minor and each has fairly confident predictions. This could be misleading for a practitioner.

3. There has been quite a bit of work on few-shot learning (see https://arxiv.org/abs/2203.04291 for a survey), but I don't see much if any of that work cited. I was expecting to see some connections to that literature on general approaches to few-shot learning to place this approach in context. Also, some indication of why this particular approach was best for this task.

4. I would have liked to see some qualitative comparisons between maps constructed by the baselines and the proposed methods. That would help better understand the reason for the improved performance.



### Questions
1. Is MAP a meaningful error metric for this task given that it ignores geographic distance?

1. I don't fully understand how the few-shot experiments for SINR were conducted. Was the model retrained including the full dataset plus the restricted (<k) samples for the evaluation species? Or, was the model limited to at most k samples for all species and trained at that level? I see that there are experiments with random initialization and without, so perhaps the results in the main paper are from a pre-trained SINR with then separate fine-tuning for each species? Or, fine-tuning across all evaluation species?

1. What is the practical impact of the register token? Was this evaluated?

1. Will sufficient technical details be released to exactly replicate this work, either source code or architecture and training details? What exactly is the transformer block? The project head? How is training performed (optimizers, etc.)?

1. Figure 5 highlights a concern I have about several of the results. It seems like the model does not put much weight on individual observations. For example, the "desert" case shows that the observation was in a very low probability region.  Also, it would be nice to see what these figures look like across the globe. Some of the results in the appendix (A.8) indicate that the model doesn't seem well suited to modeling endemic species. I suspect if you zoomed out from the Figure 5 examples you would see that it was mostly highlighting areas that match the range description.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an architecture and a training procedure for few-shot species range estimation. The authors argue that current species observation datasets contain limited observations for majority of the species. They propose **FE-SINR**, a transformer-based architecture that can accept a few context locations and optional textual description of species and estimate ranges of unseen species. By providing a few positive locations as context, FE-SINR can estimate the range of a species more effectively than existing state-of-the-art SDMs. FE-SINR is trained on 35.5M observations in iNaturalist and evaluated against SINR and LE-SINR in both few-shot and zero-shot setting. The results reported in the paper confirm the effectiveness of the proposed method.

### Strengths
- The motivation and problem formulation is sound and interesting. There is a growing need for reliable species distribution models for rare and unseen species and the paper addresses the problem of unseen species distribution modeling in low data regime.
- The authors propose a transformer-based architecture that processes a few presence locations of unseen species, along with metadata and predicts the range of a given species.
- The experiments are framed and conducted well.

### Weaknesses
 - I believe there are a few flaws in the methodology that need to be clarified:
    1. The context location embeddings provided as input to the transformer seems to be an important piece. During training, the authors use **fixed** 20 context locations as input per example. Why do the authors use 20 context locations for every species? Mallard, for example, is found in four continents, which might need larger number of context locations to cover its range as compared to *platypus*, which is only found in Australia and Tasmania. The use of a fixed number of context locations seems arbitrary and may not be optimal for all species, potentially limiting the model's ability to capture the full range of species with broader distributions.
    2. The context location encoder used in FS-SINR is a pretrained SINR (**Line 252**), which is already trained in a fully-supervised setting. Is it fair to use this location encoder in few-shot prediction scenario? The pre-trained SINR encoder might introduce a bias towards the training data distribution, potentially hindering the model's ability to generalize to unseen species with different spatial patterns. This is a critical point that needs further investigation.
    3. Regarding inference, how do you select the optimal number of context locations to guarentee the range of a given species will be accurately mapped? Since, I see **false activations** increasing with increasing number of context locations in **Figure 4**. For example, *Black and White Warbler* getting activated in India in the bottom-most figure. The paper lacks a clear strategy for selecting the number and spatial distribution of context locations during inference, which is crucial for reliable range estimation. The observed false activations with increased context locations raise concerns about the model's robustness.
    4. Who is providing the context locations during inference? By the end user or are they retrieved? The lack of clarity on how context locations are obtained during inference makes it difficult to assess the practical applicability of the proposed method.

> **Line 188-191** For the SINR model to make predictions for a new species, it is necessary to learn a new embedding vector $w_s$ for that species. If additional location data is later observed for that species, the model must be updated again.

- This is not entirely correct. There are methods like nearest-neighbor (Wang et al. (2019)) or prototypical networks (Snell et al. (2017)), which can be used as a post-hoc method for few-shot classification using frozen models. How does SINR and LE-SINR compare to FS-SINR using such methods without training? The paper should explore and compare against these established few-shot learning techniques to provide a more comprehensive evaluation.

- The performance improvements in zero-shot setting as shown in **Table 1** seems marginal. It is surprising FS-SINR performs worse than SINR even when test species are present during training (row 2 and 3). Section 4.3 on zero-shot evaluation needs more discussion and critical evaluation of the results. The marginal improvements in zero-shot performance and the worse performance compared to SINR in the fully supervised setting raise questions about the effectiveness of the proposed approach in these scenarios. A more in-depth analysis of these results is needed.

- Have the authors considered comparing to the approach described in Lange et al. (2023) with a few pseudo absence locations? Since, **Line 276-280** mentions, SINR and LE-SINR are fine-tuned on few-shot presence observations with pseudo-absences. The lack of comparison with methods that utilize pseudo-absence data is a significant gap in the evaluation, especially given the relevance of such methods to the problem.

- Some visualizations of what the latent embedding looks like after passing through the species decoder might help. How are the learned species embeddings different than the locations embeddings?, since the species ranges are predicted using the inner product between the two. Visualizing the latent embeddings would provide valuable insights into the model's internal representations and how it distinguishes between species and locations.

- **Section 3.2** has confusing notations. Are the networks $h_\phi$ and $m_\psi$ referring to the same thing? Please refine **Figure 2** and clearly label each component according to the notations used in **Section 3.2**. The unclear notations and lack of correspondence between the text and the figure make it difficult to understand the model architecture.

### Questions
How would the model incorporate absence data as context (if made available)?

### Soundness
3

### Presentation
3

### Contribution
3
