# Identifying Sub-networks in Neural Networks via Functionally Similar Representations

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 5, 6, 3, 3

## Abstract
Mechanistic interpretability aims to provide human-understandable insights into the inner workings of neural network models by examining their internals. Existing approaches typically require significant manual effort and prior knowledge, with strategies tailored to specific tasks. In this work, we take a step toward automating the understanding of the network by investigating the existence of distinct  sub-networks. Specifically, we explore a novel automated and task-agnostic approach based on the notion of functionally similar representations within neural networks, reducing the need for human intervention. 
Our method identifies similar and dissimilar layers in the network, revealing potential sub-components. We achieve this by proposing, for the first time to our knowledge, the use of Gromov-Wasserstein distance, which overcomes challenges posed by varying distributions and dimensionalities across intermediate representations—issues that complicate direct layer-to-layer comparisons.
Through experiments on algebraic and language tasks, we observe the emergence of sub-groups within neural network layers corresponding to functional abstractions. Additionally, we find that different training strategies influence the positioning of these sub-groups. Our approach offers meaningful insights into the behavior of neural networks with minimal human and computational cost. %\footnote{Code will be made publicly available.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new metric based on the Gromov-Wasserstein distance to measure the similarity between layers in neural networks, which can be used for mechanistic interpretability and understanding of the inner workings of neural networks. Experiments are conducted on algebraic and language tasks and a number of interesting patterns and observations are reported.

### Strengths
- A new metric for measuring the functional similarity of layers which has a number of desirable properties.
- The metric behaves experimentally as expected which may aid in improving our understanding of the inner workings of neural networks.
- Experiments on algebraic and language tasks under a number of settings, e.g., fine-tuning, sparsity, etc., reveal some sensible patterns.

### Weaknesses
 - The metric relies on qualitative assessment of the numerical results, which may be complicated for large neural networks, or may be subjective or ambiguous.
- Missing comparison with state-of-the-art metrics, e.g., Yu et al., 2024, Klabunde et al., 2023, Lohit & Jones, 2022 (listed in Sec 2)
- The mathematical notation is inconsistent and in some minor instances incorrect, e.g., "Let f0 be a function that produces a set of output Y0 given a set of input X, where Y0 ∈ Rn×dy", i.e., so is Y0 a set or a matrix?
- Overall, the paper was hard to follow, and I had to read it multiple times to appreciate the details.

### Questions
- Can we use this metric in a quantitive manner?
- Can observations reported in Sec 5.2 and 5.3 be shown experimentally? For example, the paper states, "The first major differences occur at block 9 and then the last three layers (10, 11, 12) seem to form a distinct block. This seems to indicate that most of the function/task fitting occurs at these later layers. This may be explained by the fact that gradient values are potentially larger at these later layers so they change faster from the pretrained models." This can be shown experimentally.
- The algebraic task is simple which is suitable for a controlled study, can a computer vision task be included to compare with the observations reported for the NLP task?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the functional similarity of sub-modules by applying Gromov-Wasserstein distance (GW) to their outputs. The core idea is that sub-modules (e.g., attention head/layer outputs at different depths along a transformer) can be seen as individual functions over their input, and these functions can be studied through the similarity of their outputs. However, existing methods in the literature involve either indirectly comparing the information content with respect to another function's output (a downstream task applied independently on each sub-module output) or directly with some (dis)similarity measure that assumes their pre-existing compatibility/comparability between representations. The approach proposed in this paper falls in the second category of methods, and by using GW models, a more generic measure (i.e., that takes into account more invariants) than the considered baselines. The approach is tested on a controlled environment (synthetic dataset and controlled training dynamic of an ad-hoc model) and on an NLP task (sentiment analysis) on a pre-trained model (BERT).

### Strengths
- The research question is extremely fitting for the venue, as it directly studies neural representations and is not one of the many deep learning topics that only indirectly involve them.
- The approach is well-founded and investigated even for training dynamics, with an insightful analysis in Figure 8.
- The high-level structure of the paper is robust: overall idea -> synthetic investigation -> real-world case -> in-depth analysis for the real-world one. I particularly appreciated the experiment structuring with their modularity in "setup" and "results".

### Weaknesses
 - I had a hard time understanding the **scope and goals** of the work: the paper is claimed to be aiming at mechanistic interpretability, but the methods, to my understanding, do not provide any human-understandable finding. Studying whether different layers provide similar or dissimilar representations is definitely interesting (and in fact, many existing works already do this), but I find the relation to mechanistic interpretability to be far-fetched.
- The **novelty** of the approach is also not entirely clear — in particular, in what aspect is the approach novel? Prior work has already investigated the (dis)similarity of different layers, both intra- and inter-networks [1, 2], and has also studied the block structure hinted at in this paper [2]. The similarity measure, by itself, reminds me of a topology-based measure in [3]. Some discussion on the novelty of the measure would help to understand. If it is novel, then how does it compare to widely established measures such as CKA [4] or CCA-based measures? The former is cited in the work, but I don’t see it in any experiments. CCA and CKA take into account (in different ways) the “sample-to-sample” relationships, so they are more suited as baseline methods to see the advantages of GW. In general, [1, 2] are too relevant to not be discussed in the work.
- **Clarity of the method.** While it is clear from the text why GW could be a strong measure to apply in this context, the method part is a bit confusing. From my understanding, GW in this paper is just “evaluated” on the representation pairs since the correspondence ($\pi$) is known (i.e., the representation for sample X at layer i corresponds to the representation of sample X at layer j). Is it correct? If this is the case, I would suggest specifying that $\pi$ is not optimized in this setting because equation 2 suggests the opposite. If this is not the case, it’s unclear to me why we would want to optimize a correspondence that is already known at the risk of matching different samples across layers. Can the authors kindly expand on this?
- I found the writing to be a bit confusing, often mixing low-level details with high-level takeaways. I suggest moving any detail not immediately necessary to understand the experiments to an appendix to allow the reader to focus on the core message.
- **Experiment inconsistencies.** There are a few mismatches between the tables/figures content and the text. For example:
    - Table 1 introduces "All representations considered in experiments". However, all the other experiments have only one of them considered. Table 2 is the only exception, where apparently, all of them were used to find the most similar ones across all possible representations. I would suggest to introduce all the variations in this experiment (the one related to Table 2) since they are applied only there, otherwise it comes up as confusing, especially since it's the first table in the paper.
    - Figure 2 (related to the experiment for section 4.1), contains the “Pretrained” (a) and “Fine-Tuned” (b) sub-figures, but I didn’t find in the text any description of what they are. The associated paragraph “Distance Distributions” just refers to the generic Figure 2 without describing its content or commenting on the different results according to the model.
    - The paragraph “Neighborhood Change” refers to a T-SNE plot showing the results that are commented on, but the figure is in the appendix (Figure 9e, Appendix D). Since the message of this paragraph is to study neighborhood consistency, I would use a quantitative metric for measuring neighborhood overlap (even a Jaccard similarity between the top-k neighbors, I think, could suffice), adding it to the main text rather than (only) a qualitative plot in the appendix.
    - Table 2 for experiment 5.1 shows results that I think are not well-commented in the text. What's missing is the message from them: what's the meaning of the top similar layers being the ones of those specific kinds and not others?
    - In the synthetic data experiment (section 5.1), 3 models are used: Model 0, Model E, and Model L. According to the *Training procedure/setup* paragraphs, Model E and L have three layers each. However, in the Results paragraph of the same section and in the related figures (3 and 4), they appear to have more than 90 layers each.

### Questions
- *Unconnected Related works*. I think that the related work section could benefit from some restructuring. For example, it is not clear to me why the "Algorithm discovery in algebraic problems" and "Real applications" (e.g., here "vision and language components" are mentioned, why?) paragraphs are connected to this work. On the contrary, I found the last one (Similarity Measure between Neural Network Layers) to be clear and well-connected to the rest of the paper. I think a couple of sentences for each paragraph explaining the connection with the rest of the work could help.
- *Section 5.2, Setup paragraph*: when the three sparse models are introduced, I would suggest explaining why they are used/useful in this experiment. Even a single sentence like "The sparse models are used to force their respective models to condense more the information in the few weights they have remaining, so we can analyze any link between this constraint and their structural similarity".
- *Section 5.1, Training procedure paragraph, line 356:* "In all these models, we are able to achieve 100% prediction accuracy". Is it on a validation set hinting at perfect modeling of the target function or on a training one useful to understand if the models could overfit or not?
- There's a typo in line 146/147 (intro to Section 3). A full stop is missing after "as a similarity search problem".
- *Experiment 5.2, Results paragraph*: on line 439, it is written: "from layer 8 and only fine-tuning the later layers". As a minor comment, I would suggest changing this sentence to “freezing the model up to layer 8 and only fine-tuning the layers after that” to make the sentence clearer.
- The figures are dense and have really small ticks/labels. For example, Figure 6 and Figure 2 require a lot of zooming in. My suggestion to improve the readability would be to start by sharing the x and y axes labels and avoid adding details in the titles (i.e., the KL divergence, especially because it appears only there and is not commented on in the text).
- Section 4, start of the “Unknown Targets” paragraph (line 230/231): I think there are missing words, the opening sentence is not grammatically correct. A rewrite could be “When the search target is unknown, functionally similar parts cannot be identified by comparison to a predefined set of target functions.”

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to compute functional similarity between layers of neural networks using Gromov-Wasserstein distance in order to identify subcomponents in the architecture of trained models. In particular, the goal is compare different neural networks layers in order to identify subcomponents of the networks, which may be specific to solve particular tasks. Experiments are conducted on synthetic modular arithmetic tasks and on BERT text models fine-tuned on sentiment analysis tasks.

### Strengths
- The direction proposed by the paper is interesting and relevant: extracting subcomponents of neural networks based on similarity measures is a core direction for fields such as representation alignment, interpretability and model selection potentially leading to new strategies for transfer learning and neural network pruning and merging, among others.


- The paper writing is clear and the proposed method is simple.

### Weaknesses
While the direction of the paper is interesting the realization seems not to be as broad as it stated in the introductory section and title. In particular: 

- As stated in the paper one core objective is "to detect how many distinct (complex) functions exist in a learned network, and which layers correspond to each such function". While the question is very relevant, I don't see direct evidence of the fact that blocks of layers with identify with a given complex function, except for the synthetic modular experiment. In particular on real data there is no analysis on correlation on accuracy on downstream tasks and GW similarity of layers, which to the bet of my understanding seems necessary in order to assess if a subcomponent learned a specialized function of the input. In order to understand this one way could be just to train leaner readout on the downstream from representations of the two blocks separately and see how the performance changes and correlates with the GW distance.  Related to this: 
      
    - In Figure 8 shows just the mean GW distances across all layers which doesn't allow to validate any task specialization of the block of layers with similar GW distance


- Experiments and method section are focused on transformer networks, not general neural network architectures as discussed in th intro/title. However measuring GW distances in representation space should be agnostic of the architecture. Why the focus just on this architecture? 


- The paper focuses on the synthetic task of modular arithmetic and the one of sentiment analysis on text. In order to make the statements more general more tasks, datasets and /or modalities should be taken into account. For example, it might be interested to see in Vision models based on ResNet or convolutional architectures, early layers subcomponents would be able to solve more task which depends on local statistics of the input, while layers closer to the inputs are more expect to solve task which rely on global information, such as image classification.

- The synthetic task on modular arithmetic is trained from scratch but it doesn't seem to take into account possible effects given by different random initializations. See questions section for more details on this. 

- The following papers should be included for discussion and/or comparison:

    - Tsitsulin, Anton, et al. "The shape of data: Intrinsic distance for data distributions." ICLR 2020 

    - Kornblith, Simon, et al. "Similarity of neural network representations revisited." International conference on machine learning. PMLR, 2019.

In the former, it is proposed a similarity measures based on heat kernels of graph on latent representations which gives a lower bound on the GW distances between embeddings. 
In the latter is proposed the CKA measure to compute similarity across data representations. This shares most of the favorable properties highlighted for the GW distance and is computationally efficient. Also it shows how comparing different layers of networks reflects the functional structure of each component (e.g. see the Figure 4 in the paper). 

More broadly there are many contributions from the field of model merging which might be useful to take into account and discuss, for example: 

- Singh, Sidak Pal, and Martin Jaggi. "Model fusion via optimal transport." Advances in Neural Information Processing Systems 33 (2020)

- Stoica, George, et al. "Zipit! merging models from different tasks without training." ICLR
  

- More details on the method to compute GW distance could be provided in the paper in order to make it self-contained. Specifically, why the choice of the Fused Gromov Wasserstein method in particular?

### Questions
- Modular arithmetic experiment: could the authors justify why the choice of the GW distance represent a good choice for extracting compared to measures as CKA [b], canonical correlations analysis and other kernel distance measures mentioned in (Klabunde,2023)  

- Networks initialized with different feed converge to different representations (see e.g. [a,b,c]), although they might perform similarly. In the modular arithmetic experiment how is this taken into account? It would be interesting to measure the GW distance between networks trained on the same data and task but with different initializations.  Alternatively the experiments could be repeated averaging results for multiple seeds.  


    - [a] Moschella, L. "Relative representations enable zero-shot latent space communication (2023)." ICLR 2023

    - [b] Li, Yixuan, et al. "Convergent learning: Do different neural networks learn the same representations?." PMLR

    - [c] Kornblith, Simon, et al. "Similarity of neural network representations revisited." International conference on machine learning. PMLR, 2019.



- What is the exact difference between the implemented version of Wasserstein and GW distance in the paper?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a novel method for identifying sub-components within neural networks, addressing challenges arising from varying distributions and dimensionalities in intermediate representations.

### Strengths
- The proposed method discerns similar and dissimilar layers within the network, revealing potential sub-components, and addresses challenges from varying distributions and dimensionalities in intermediate representations.
- The presentation of the experimental results is precise and well-organized.

### Weaknesses
 - The experiments are limited due to insufficient validation across diverse tasks, datasets, and learning methods. This includes gaps in testing with image (classification) datasets, self-supervised learning methods, etc.
- The contribution of the proposed method is unclear. Can the identified sub-network effectively serve as a proxy, replacing the entire original network to accelerate inference for specific downstream tasks?
- The motivation for identifying subnetworks requires clarification. Specifically, the phrase "understanding the network by investigating the existence of distinct subnetworks" needs a more explicit explanation. It is unclear why identifying these subnetworks contributes to a deeper comprehension of the neural network as a whole.
- The proposed technical solution appears straightforward. To address challenges associated with varying distributions and dimensionalities in intermediate representations, the primary approach involves identifying subnetworks using the Gromov-Wasserstein (GW) distance. However, since GW distance has been previously proposed, it could potentially reduce the novelty of this work [1].

### Questions
- Could you elaborate on the necessity and benefits of understanding neural networks through the identification of sub-networks?
- Could you detail the technical innovations presented in this paper that extend beyond the Gromov-Wasserstein method?
- Could you present additional experimental results across diverse tasks, datasets, and learning methodologies?
- Could you discuss a real-world application of sub-network identification, such as improving the inference speed of neural networks?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a novel perspective on model interpretation by utilizing the Gromov-Wasserstein (GW) distance to compute similarities between model layers and identify sub-networks. For algebraic and real-world NLP tasks, the proposed methods effectively identify sub-components.

### Strengths
1. This paper proposes a novel perspective for model interpretation that minimizes both human and computational expenses.
2. The proposed methodology can effectively identify subnetworks.

### Weaknesses
1. The motivation for identifying subnetworks is unclear. Once identified, I'm curious about how they can enhance our understanding of networks in real-world applications.
2. The key idea to identify subnetworks is the use of Gromov-Wasserstein (GW) distance, which has been proposed before and might diminish the novelty of the work.
3. There are some typos, such as a missing comma on line 146.

### Questions
1. The motivation for why it is necessary to identify subnetworks is unclear. Could the authors provide more explanation about the relationship between model interpretation and subnetwork?
2. Additionally, the field of model pruning involves identifying and retaining stronger subnetworks. What are the differences and connections between this approach and model pruning?
3. Could the author provide more explanation about Figure 3, particularly the relationship between the three identified groups and the model architecture?

I am happy to engage further during the discussion phase.

### Soundness
2

### Presentation
2

### Contribution
2
