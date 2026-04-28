# Exploiting Topology of Protein Language Model Attention Maps for Token Classification

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 6, 6, 3, 3, 5, 5

## Abstract
In this paper, we introduce a method to extract topological features from transformer-based protein language models. Our method leverages the persistent homology of attention maps to generate features for token (per amino-acid) classification tasks and demonstrate its relevance in a biological context. We implement our method on transformer-based protein language models using the family of ESM-2 models. Specifically, we demonstrate that minimum spanning trees, derived from attention matrices, encode structurally significant information about proteins. In our experiments, we combine these topological features with standard embeddings from ESM-2. Our method outperforms traditional approaches and other transformer-based methods with a similar number of parameters in several binding site identification tasks and achieves state-of-the-art performance in conservation prediction tasks. Our results highlight the potential of this hybrid approach in advancing the understanding and prediction of protein functions.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an interesting approach to extract topological features from protein language models. More specifically, they compute the minimum spanning tree (MST) from the attention weights of ESM2. To evaluate their method, they train a PyBoost classifier that takes the processed MST features as input and predict conservation and binding residues. They also ensemble their model with ESM to achieve stronger performance.

### Strengths
The authors provide an interesting take on the attention weights. By thinking about it as a fully connected graph, the authors present an interesting analysis using minimum spanning trees.

### Weaknesses
Evaluation is limited to binding and conservation.

The proposed models, RES-MST (ESM2-650M all) and RES-MST (ESM2-650M avg), perform comparably with ESM2 across the benchmarks. Specifically, ESM achieves stronger performance in 5 of the 12 benchmarks.

It remains unclear to me what the utility of such an approach is.

Since the topological features are extracted solely from ESM2, ESM2 already contains topological features, albeit in a rich latent representation. The similar performance of the proposed approach and ESM2 seems to suggest that one can implicitly decode these topological features from ESM2. Thus, what is the significance of this approach? Is there anything besides being “the first time that topological data analysis has been applied to classification on a per-token basis”? What are some cases in which the proposed topological features capture information that is not easily accessible from ESM2 embeddings alone? In other words, what are some potential advantages of topological approach over the ESM embedding?

To be clear, the tasks of residue conservation and binding are motivated in the introduction. However, the motivation for topological data analysis is not clear, as ESM seems to perform fine.

### Questions
This paper reports an interesting idea on how to convert attention matrices into topological features. The authors provide analysis and visualizations of the minimum spanning tree on different proteins. They look quite interesting. However, it remains unclear to me what the utility of such an approach is.

Since the topological features are extracted solely from ESM2, ESM2 already contains topological features, albeit in a rich latent representation. The similar performance of the proposed approach and ESM2 seems to suggest that one can implicitly decode these topological features from ESM2. Thus, what is the significance of this approach? Is there anything besides being “the first time that topological data analysis has been applied to classification on a per-token basis”? What are some cases in which the proposed topological features capture information that is not easily accessible from ESM2 embeddings alone? In other words, what are some potential advantages of topological approach over the ESM embedding?

To be clear, the tasks of residue conservation and binding are motivated in the introduction. However, the motivation for topological data analysis is not clear, as ESM seems to perform fine.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose to conduct topological analysis on the attention maps produced by protein language models. The analysis shows a relationship between attention strength and physical contact in 3D structures. The authors then propose to use this extracted tree information to augment protein language models in various tasks.

### Strengths
1. The manuscript is well-written. I specifically like the illustration in figure 4 and figure 5.
2. The idea is novel and the analysis is convincing. While it is widely accepted that protein language models can directly and indirectly encode structure information, the effort to directly convert this information into an explicit tree is novel, as far as I know.

### Weaknesses
1. The major flaw of this paper is about its experimental results. The table 1 shows minimal improvement over original esm-2. Could authors give a brief explanation? Also, the error reported in these tables is astonishingly low. How are these numbers produced? I think such low variance can only be obtained by training linear modules.



### Questions
1. Figure 6-9 should be renamed to one figure with sub figures.
2. The line space of contributions listed in introduction might need adjustment.
3. The "all" and "avg" in table1-4 are not explained in tables' captions.

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors apply techniques from topological analysis on graphs to the attention maps of protein language models, (particularly ESM-2)

They generate features that can be appended to the ESM-2 embeddings and then used to help in tasks that make classifications / predictions at the amino acid level.

The authors describe how to generate barcode of different persistent homology features by varying a threshold for edge weights, filtering the edges in the graph and recording when various topological features come and go as the threshold is raised. There are simple edge features (H_0), and cyclical features (H_1), and presumably higher level feature s that can be extracted from the barcode.

Next, the authors state that the topological features for H_0 are equivalent to features derived from the Minimum Spanning Tree (MST). 

The experiments show that concatenating these features to the pLM embeddings can improve performance on downstream tasks.

### Strengths
The discussion about barcodes and topological features is nice.
The motivation seems clear; An output feature that says 'dense clique around here' or 'cycles present' will be useful for some tasks.

The method is non-parametric which is good, the MST does not need a threshold, and there is no need to fine tune ESM-2.

New features are generated from the attention maps of the transformer network. 
Since the transformer was trained on language model tasks, the embedding features at the output do not necessarily encode the graph structure contained in the attention maps, only the information necessary for the output token, so it makes sense to try and include more of the information held in the network of attention weights remaining in the transformer.

The new features do improve the results on downstream tasks.

### Weaknesses
The main results only use H_0 features, which can be derived from an MST. The method for H0 boils down to generating the MST and taking basic statistics over the edges to the neighbors for each node.  There is no description about why these statistics are equivalent to H_0 except [212]: "Each interval in a barcode corresponds to an edge in MST". Perhaps a more thorough description in the appendix could be provided?

When some edge weights are the same, MST can give different resulting graphs, since the order of edges is ambiguous. 
And since small changes in attention weights could cause radically different MST doesn't this make the resulting features very noisy? In your experience, how widely spread are transformer attention weights? And how is your method robust to this?

For results using both H_0 and H_1 , one has to look to the appendix for the RES-LT results. While they are not better than MST the main body would be clearer if they were included - there is discussion in section 2 about persistent homology and Betti numbers for H_k, and there is talk of cycles and topological features, but cycles only appear in H_1 and only H_0 is used in all the results (in the main text).

RES-MST takes some statistics over edges are taken per node in the MST. [194] In the description for the features derived from the MST (for each node - min,max,sum,mean weights and count incident edges). 
Here it is also mentioned that: "We add: self-attention + sum abs values in ith row jth col.".
There should be an ablation study for the effect these (non-MST) features have.
How much performance do the MST features add over these extra features?

Typos::

*** 159: is
*** a: 201 - LxH should be resulting in L accroding to 187
*** 450 -(2020) - paper title missing.

### Questions
What is actual size of resulting feature vector (to be added to ESM-2 Embedding) - 8? or 8 x L (when all heads in layer are averaged).

Perhaps this model has advantages over ESM-2 embeddings because it uses features from other layers in the pLM.
The pretraining task for the pLM is for token reconstruction, which might throw away information about connectivity in the last layer.
What about simply taking ESM-2 features from other the layers (eg. middle + last layers) and concatenating them?

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
This paper performs a topological data analysis (TDA) of the attention maps produced by 
ESM2 protein language models. Inspired by TDA of natural language model attention maps 
and TDA of protein structures, this work leverages the apparent relationship between 
attention and 3D structure in ESM models. The authors demonstrate that some topological 
features are correlated with structural features of proteins and show that adding 
topological features improves per-residue performance on a variety of downstream tasks. 
I would recommend to accept this paper. It is difficult to understand the precise 
contribution of the TDA methods, but the approach is interesting, and the experiments are 
thorough.

### Strengths
• The method is an interesting way to probe what ESM models are attending to and 
how this relates to its knowledge of 3D structure. 
• The figures (both diagrams and renderings) are very clear and helpful. 
• The analysis of the relationship between TDA features and 3D structure sheds some 
light on the utility of the method. 
• The results show a consistent benefit from the method and generally provide a fair 
comparison to other state of the art sequence methods.

### Weaknesses
The analysis of the TDA in section 3.3 feels somewhat incomplete. Is this just based 
on the one example from figure 5? Can some of these descriptions such as 
“chaotic” vs “star” or “linear” be quantified? What is the significance of each of 
these stages? 
• (small) Figure 7 would be clearer if the ymin was set to 0 
• LMetalSite, another (strong) sequence-based method from Yuan et al (2024) is 
missing from the metal-binding table. Also, it may be appropriate to include 
ESMFold-derived structural methods, since this is another sequence 
“preprocessing” step. 
• The provided source code is incomplete. There was substantial use of a package 
called bio_tda which was not provided.

### Questions
• Figures 6-9 are interesting, but it is not immediately clear what the takeaway is. It 
seems to me that figure 6, 8, and 9 can be explained by: “ESM2 attends more to 
linear positional encoding in the early and late layers”. 
• What are the specific features included in the RES-MST (*) methods? The 
performance of these methods is suspiciously good for just the features listed in 
section 3.1 - in particular, the models don’t seem to need residue types? 
• How expensive is the MST preprocessing compared to structure prediction with 
ESMFold or AlphaFold2?

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
4

### Summary
This paper investigates the topological features of protein language model attention maps using the lens of persistent homology. The study computes minimum spanning trees (MSTs) from these attention maps to derive per-residue features. The incorporation of topological features enhances the performance of PLMs in prediction tasks such as residue conservation prediction and binding site prediction. Furthermore, the study analyzes variations in the topological features of the MSTs derived from attention maps across different layers of the language model.

### Strengths
- The analysis of attention maps using persistent homology offers a commendable theoretical perspective.
- The relationship between protein attention maps, residue conservation, and amino acid distances has been analyzed extensively.

### Weaknesses
 - While the paper suggests that the MST method could enhance model performance by extracting topological information from attention maps, it lacks empirical evidence to substantiate this claim. Drawing on prior experience, the potential for performance enhancement with attention map integration appears plausible.
- The benchmarks assessed are less widely used (especially for the conservation prediction task), which challenges the demonstration of the new method's practical applicability.
- The baseline comparisons for the binding experiment are limited in diversity and omit the latest methods (e.g., [1,2]), thereby reducing the persuasiveness of the findings. Specifically, the exclusion of methods that utilize structural information is not well-justified, given the current accessibility of accurate protein structure prediction.
- There are many typos in the manuscript. e.g., wrong citation format (e.g., "Several unique properties of proteins can be derived from their 3D structure Wang et al. (2022a); Zhang et al. (2022); Kucera et al. (2024); Sun et al. (2024)." -- the references should be included in a parentheses.) and repetitive figures (e.g., Figure 4 and Figure 10).

### Questions
- What's the empirical advantage of the MST-based method in comparison to other deep learning-based methods for topological feature extraction in downstream tasks?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work introduces a method to extract topological features from protein language model attention maps for improved per-amino-acid classification tasks. The authors present RES-MST, which uses minimum spanning trees derived from attention matrices to capture structurally significant protein information. By combining these topological features with standard embeddings from the PLMs, the method outperforms existing sequence-based approaches on binding site identification and conservation prediction tasks.

### Strengths
Novel application of topological data analysis to protein language models: This work bridges two important areas (TDA and protein LMs) in an innovative way, potentially opening up new avenues for analyzing and improving protein language models.

### Weaknesses
- Limited theoretical foundation: The paper lacks a robust theoretical explanation for why this topological approach should outperform alternative methods that leverage attention maps. A stronger motivation for the use of topological data analysis in this context would strengthen the paper's argument. Specifically, the authors should elaborate on how topological features capture information about protein structure and function that is not accessible through other methods that utilize attention maps.

- Insufficient ablation studies: The paper would benefit from more comprehensive ablation studies to elucidate the contribution of different components of the method, such as various types of topological features and the impact of different layers. For instance, the authors could compare the performance of models using only minimum spanning tree (MST) features, only attention map features, and combinations thereof. They should also investigate the contribution of each layer to the overall performance.

- Unclear methodology description: The explanation of the method in Section 3.1 lacks clarity. Specifically: a) The exact features extracted from the MST for each amino acid are not clearly defined. It is mentioned that topological features are extracted, but the specific features are not listed. b) The features extracted directly from the attention map are ambiguously described. Are these raw attention weights, or are they further processed? c) The process of combining the MST-derived and attention map-derived features is not explained. Are they simply concatenated, or is a more sophisticated fusion method used? d) The final prediction process using this non-parametric method is not adequately detailed. What kind of classifier is used, and how are the predictions aggregated?

- Ambiguous interpretation of results: The interpretation of Figures 6, 8, and 9 in relation to the described patterns (chaotic, star, linear) in Section 3.3 is not sufficiently clear, making it difficult to follow the authors' reasoning. The authors should provide a more detailed explanation of how these figures support their characterizations of the patterns observed in the MSTs across different layers.

- Choice of evaluation metric for conservation prediction: The authors' decision to treat the conservation prediction task as a classification problem, rather than using regression metrics like Pearson correlation or Spearman's rank correlation, is not well justified. Conservation scores are typically continuous, and regression metrics are better suited for evaluating the accuracy of predicted conservation scores.

- Limited comparison with relevant baselines: The paper lacks comparison with other approaches that use both protein sequence embeddings and their attention maps. This makes it unclear whether the performance improvement stems from the proposed Topological Data Analysis approach or simply from leveraging attention patterns. Additional baselines utilizing both embeddings and attention maps with different methods such as (Rao et al, 2020) is necessary to substantiate the effectiveness of the proposed method. For example, the authors could adapt the method of Rao et al. (2020) to per-residue prediction tasks and compare its performance to RES-MST.

### Questions
- Can you provide more theoretical justification or intuition for why this topological approach should work better than alternative methods that leverage attention maps? How does it capture information that other approaches might miss?
- Could you clarify the feature extraction process in more detail? Specifically: a) What exact features are extracted from the MST for each amino acid? b) What features are extracted directly from the attention map? c) How are these two sets of features combined? d) How is the final prediction made using this non-parametric method?
- The paper describes patterns in the MSTs as "chaotic," "star," and "linear" across different layers. Could you provide a more detailed explanation of how Figures 6, 8, and 9 support these characterizations?
- How does your method compare to other approaches that use both protein sequence embeddings and attention maps? Can you provide additional baselines or comparisons to isolate the contribution of the topological data analysis approach versus simply leveraging attention patterns?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 7

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose RES-MST, a method that leverages attention maps from protein language models to generate minimum spanning trees (MSTs) and extract various features for per-residue conservation and binding predictions. By evaluating their approach on datasets such as ConSurf10k for conservation and diverse binding site prediction benchmarks, they demonstrate that RES-MST outperforms baseline models, achieving superior accuracy and AUC scores.

### Strengths
The paper introduces a non-parametric framework aimed at transforming attention matrices from transformer models into topological features that are customized for token-wise classification. The results presented in the paper demonstrate impressive performance in per-residue conservation and binding predictions. The competitive accuracy and AUC values highlight the effectiveness of the proposed method, particularly in leveraging attention maps from pLMs for generating MSTs.

### Weaknesses
Methodology:
- Suitability of attention maps for topology: Attention maps represent learned relationships between sequence tokens (amino acids) based on the model's training objective, which is primarily language-based. These relationships are not necessarily grounded in spatial or physical proximity, which are crucial for understanding protein structure and function. Attention matrices are often dense and noisy, with attention spread across many tokens, which might make topological methods like persistent homology less informative or even misleading when applied naively. The paper would need to convincingly demonstrate that the topology derived from attention maps has a meaningful connection to physical or functional protein properties. While the authors cite work showing attention maps can highlight residue contacts, this does not guarantee that the *specific* topological features extracted here are meaningful, especially given the inherent noise in attention maps. The authors need to provide stronger evidence that the chosen topological features are robust and not simply capturing noise.
- While the authors analyze MST structures across layers, they don’t provide a clear theoretical or empirical justification for why these specific patterns (chaotic, star, linear) are meaningful in terms of protein functionality or how these differences are expected to relate to biological significance. It is not clear if these patterns are directly related to actual protein structure or function, or if they are simply artifacts of the attention mechanism. A more rigorous analysis is needed to establish a clear link between these observed patterns and the underlying biology.
- The transformation of attention scores into a quasi-distances matrix is a key step, but the reasoning behind this particular transformation is under-explained. Why the maximum of the bidirectional attention scores is chosen, or how this approach compares with others, isn’t detailed. The authors need to justify this choice with a more thorough analysis, including a comparison with alternative methods such as averaging or using the attention scores directly without symmetrization. The lack of ablation studies here is a significant weakness.
- The choice to focus on topological features derived from MSTs lacks sufficient motivation regarding why these features, specifically from MSTs rather than other graph representations. The authors should provide a clear rationale for choosing MSTs over other graph representations, such as k-nearest neighbor graphs or fully connected graphs, and explain why MSTs are particularly well-suited for capturing the relevant information in attention maps. The connection between MST properties and the desired protein features needs to be more clearly established.
- The authors do not specify the model used for downstream tasks, nor do they clarify the form and structure of the input to this model. While they detail the process of extracting topological features from attention maps and MSTs, they omit critical information on how these features are subsequently utilized in downstream tasks. Without specifying the model type or its architecture, it’s challenging to assess how effectively the extracted features are integrated or if they are even suited to the task's requirements.

Writing:
- There is no explanation for the choice of the name 'RES-MST.'
- The citation format used in the paper does not adhere to standard conventions. For example, in line 172, the citation 'ESM-2 Lin et al. (2022)' should be formatted as 'ESM-2 (Lin et al., 2022)'. I recommend reviewing and revising the citation style throughout the manuscript.
- There is no interpretation provided for Figures 6, 7, 8, and 9.
- Line 136: there is an incorrect use of the open quotation mark.
- Line 147: "the vertices set" is not grammatically correct. 
- Line 150: "The natural issue is a necessity to pick some α." is not grammatically correct. A grammatically correct version would be: "A natural issue is the necessity of choosing a value for α."
- In the tables, some numbers are in different fonts.

### Questions
- There is no explanation for the choice of the name 'RES-MST.' What does 'RES' stand for in 'RES-MST'?
- Could the authors elaborate on the theoretical or empirical rationale behind analyzing MST structures in terms of chaotic, star, and linear patterns? How do these specific patterns relate to protein functionality and biological significance?
- In the paper paper, the author discuss the extraction of topological features from attention maps, but do not specify the model used for downstream tasks. Could you provide more detail about the model type and architecture?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 8

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method that applies the topological information embedded in the attention maps of protein language models (PLMs) to downstream tasks. Specifically, the paper treats the information in the attention maps as a fully connected undirected graph, where each node represents an amino acid. It then extracts a minimum spanning tree (MST) from this graph and further derives effective topological information from the MST to be used in downstream property prediction tasks. In summary, this work represents an effective attempt to mine structure-related topological information from the attention layers in PLMs, offering a new perspective for further analysis and understanding of PLM behavior.

### Strengths
1. The research question addressed in this paper is both interesting and significant. Understanding and interpreting the behavior and knowledge learned by PLMs is an essential research direction.
2. The idea of treating the attention map as a fully connected graph and modeling structure-related knowledge by capturing its topological information is innovative and worth investigating.

### Weaknesses
1. The paper lacks a more comprehensive discussion of approaches for utilizing the graph topological information in the attention map. While the MST approach is one option, the authors need to provide stronger motivation for choosing this method to capture topological information. For example, why was the MST method chosen? What are its advantages in comparison to other graph-based methods? These questions require further clarification. On this basis, the paper should also offer more comparative and reference experiments, such as evaluating the impact of using different methods to model topological information on performance. The MST inherently tends to capture high-weight edges between each node and its neighbors, akin to capturing information about nodes strongly associated with each node. But what if alternative modeling methods with similar properties were used? For example, one could identify the top k nearest nodes for each node by distance and index, then construct features for downstream tasks. How would this approach differ, particularly in terms of computational cost and information captured? A more detailed analysis of the trade-offs is needed.

2. The paper’s organization needs improvement. The second section introduces substantial background knowledge on topological information, yet this part has little relevance to the content in the following third section. Even if removed, this background section would not impact the understanding of the paper's main content. Furthermore, while defining RES-LT in the appendix, this paper references topological background knowledge from the second section; however, as RES-LT is only used in the appendix, the background knowledge could be moved there as well. In other words, I find the paper's structure to be flawed, with insufficient logical cohesion between different parts.

3. More details regarding the experiments should be provided. For instance, what is the difference between RES-MST (ESM-2 650M all) + ESM-2 (650M) and the RES-MST (ESM-2 650M all) model? I couldn’t find any explanation of this in the paper. The description of the experimental setup and the specific configurations used for each model variant are not sufficiently detailed, making it difficult to reproduce or fully understand the results.

4. The chosen downstream tasks primarily focus on per-residue scale tasks. However, it would be valuable to discuss structure-related tasks on a larger scale (e.g., protein function annotation), as this could reveal whether this MST-based topological modeling approach can capture more global protein property information. The current focus limits the scope of the conclusions that can be drawn about the method's ability to capture higher-level structural features.

5. A more detailed comparison of the method’s runtime is needed. Compared to traditional full-parameter fine-tuning approaches, your method requires first calculating the MST, then extracting features and training a Pyboost classifier, which incurs significant time costs and may reduce algorithmic efficiency. Therefore, a discussion of the time costs of this approach compared to traditional full-parameter fine-tuning is necessary. However, in Appendix A.5, you did not provide runtime comparisons with baseline models. The lack of a thorough runtime analysis makes it difficult to assess the practical applicability of the method.

### Questions
Please refer to the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2
