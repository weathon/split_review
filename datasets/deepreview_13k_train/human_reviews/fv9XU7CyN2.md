# CL-MFAP: A contrastive learning-based multimodal foundation model for antibiotic property prediction

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
Due to the rise in antimicrobial resistance, identifying novel compounds with antibiotic potential is crucial for combatting this global health issue. However, traditional drug development methods are costly and inefficient. Recognizing the pressing need for more effective solutions, researchers have turned to machine learning techniques to streamline the prediction and development of novel antibiotic compounds. While foundation models have shown promise in antibiotic discovery, current mainstream efforts still fall short of fully leveraging the potential of multimodal molecular data. Recent studies suggest that contrastive learning frameworks utilizing multimodal data exhibit excellent performance in representation learning across various domains. Building upon this, we introduce CL-MFAP, an unsupervised contrastive learning (CL)-based multimodal foundation (MF) model specifically tailored for discovering small molecules with potential antibiotic properties (AP) using three types of molecular data. This model employs 1.6 million bioactive molecules with drug-like properties from the ChEMBL dataset to jointly pretrain three encoders: (1) a transformer-based encoder with rotary position embedding for processing SMILES strings; (2) another transformer-based encoder, incorporating a novel bi-level routing attention mechanism to handle molecular graph representations; and (3) a Morgan fingerprint encoder using a multilayer perceptron, to achieve the contrastive learning purpose. The CL-MFAP outperforms baseline models in antibiotic property prediction by effectively utilizing different molecular modalities and demonstrates superior domain-specific performance when fine-tuned for antibiotic-related property prediction tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The work introduces CL-MFAP, a model designed to predict the antibiotic properties of small molecules based on multimodal data and contrastive learning.  The model is trained on 1.6 million bioactive molecules from the ChEMBL database and takes three types of molecular data: SMILE strings, binary fingerprints, and graphs. To handle these three different modalities, the model uses a transformer with rotisserie positional embedding, MLP, and graph-based transformer accordingly. The optimization of the model is carried out with contrastive learning loss between the three modalities’ outputs. The models are then compared with several baselines on five downstream datasets and showed good performance on three of them.

### Strengths
The integration of RoPE and BRA enhances the model's ability to handle long-range dependencies and molecular structure in a multimodal contrastive learning setting. Furthermore, the BRA is used jointly alongside MPNN and graph transformer encoder. Ablation studies of the combinations of these sub-models are performed and these combinations are included as baselines.

### Weaknesses
1. The number of baselines is quite limited, out of 7 baselines, 4 of them are variant models from the proposed model. Only three of the baselines are models by other authors. 
2. There’s one mistake in algorithm 2, line 4, and line 6, where the two if conditions are the same. Maybe this is a typo. 
3. Some of the parameter values are not explained such as the value of window size S. The functions in algorithm 2 are not explained, I think one sentence of description can make the algorithm easier to understand.
4. A graph of the Window-to-Window Level Routing and Pixel-to-Pixel Level Attention could be helpful for this is a major novelty of the paper. A graph for layer structures which include the substructures would be helpful and would make the combination of BRA, GTE, and MPNN easier to understand.
5. The template is not the latest ICLR 2025.

### Questions
1. Is it meaningful to perform more ablations to the Window-to-Window Level Routing such as adjusting the window size?
2. Will you consider adding std to results based on several independently running?
3. Will you consider adding more published baselines?

### Soundness
3

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
4

### Summary
In this paper, a new method for molecular property prediction is proposed. The model is termed CL-MFAP, and it uses a multi-model approach and contrastive learning to train a molecular property predictor specialized in antibiotic properties. As an input, the model takes three molecular modalities: SMILES strings, fingerprints, and molecular graphs. Each modality is transformed using a different neural network, and the resulting representation vectors are contrasted to create one representation that is useful for predicting various properties, including bioavailability, blood-brain barrier penetration, and cell membrane permeability. The graph neural network that processes molecular graphs is redesigned to use new bi-level routing attention, designed initially by Zhu et al. (2023). The experiments demonstrate the performance of CL-MFAP across five datasets as well as compare different versions of the model in the ablation study.

### Strengths
Originality:
- There are two main novel contributions in this paper. The first one is the adaptation of bi-level routing attention to molecular graphs. The second one is the exploration of the architecture space within the contrastive learning framework for molecular property prediction.

Quality:
- Different architectures were tested to select the best model architecture in this study.

Clarity:
- The introduction and related work sections are written very clearly and with clear motivation.
- Figure 1 effectively explains the model proposed in this study.

Significance:
- The problem that the Authors try to solve in this study is very important. As explained in the introduction, we need more models that will help accelerate the discovery of new antibiotics. The proposed model is a step in that direction.
- The code of the model is shared publicly.

### Weaknesses
Originality:
- The model described in the paper is a combination of known techniques, including multi-modal molecular representations and contrastive learning.
- The focus on antibiotics is an interesting direction that is currently underexplored. However, the paper does not emphasize any novel contributions that are specific to this field.

Quality:
- The experimental results do not include standard deviations or confidence intervals. The proposed method is compared only against three models for molecular property prediction, none of which are multimodal.
- The data splitting method is not described in the paper.
- The data collection method is not explained.

Clarity:
- The "Proposed Approach" section is difficult to follow. It is impossible to understand the model without reading the original cited works that introduce the methods used in this study. For example, the notation used in any of the equations is not explained, like $m$ and $n$ in Equation 1, $k_n$ in Equation 2, $R_{\Theta,i}^d$ in Equation 3. Some symbols are introduced but not used, like $\varphi$ before Equation 2. If these symbols and formulas are not explained in the text, they should be removed, and there should be references to the original works instead.
- For the BRA mechanism, the equations were also copied from the work of Dong et al. (2023) (or Zhu et al. (2023)) and not properly explained or defined. There are a few typos that make the text difficult to read, e.g. "feature map $x$, $X\in\mathbb{R}^{H\times W\times C}$" (is it $x$ or $X$?).
- The algorithms included in the text use functions that were not defined. At least parts of these algorithms could be explained more clearly in the text using mathematical formulas. For example, the computeLoss function is unnecessary as it can be explained by the equations in the text. Also, it seems that the definition in Algorithm 2 is different from what Equation 9 represents.
- The font size in Figures 2 and 3 is too small. Figure 2 would be more readable if it was a 2D barplot.

Significance:
- The code repository does not contain any instructions on how to run the code or how to install the code dependencies. The repository should also include a license file that describes the allowed use of the code.
- The experiments are insufficient to support the claim that CL-MFAP "combines and compares molecular information [...] to efficiently learn representations of drug molecules **with potential antibiotic properties**."

Minor comments:
- The positive pairs on page 6 should probably include [x1, y1] instead of [x1, y2].

### Questions
1. What is special about this approach that makes this model specifically designed for antibiotic property prediction? The architecture seems to be rather general, and most of the datasets (besides MIC) used in this study are not specific to antibiotics. 
2. What does it mean that you "collected bacterial-related compounds targeting the specific domain of antibiotics from the ChEMBL database"?
3. Why should the bi-level routing attention mechanism perform well in the context of molecular graphs? If I understand correctly, this layer was designed to help the model focus on the relevant parts of images. Molecular graphs of typical antibiotics (or generally therapeutic small molecules) are rather small and do not share the problems that were identified in the case of large images. Why should this approach work better for capturing long-range dependencies than graph transformers?
4. What is $l$ in Equation 9? How is $l_i$ from Equation 8 used?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces CL-MFAP, an unsupervised contrastive learning-based multimodal foundation model for predicting antibiotic properties of small molecules, addressing the urgent need for novel antibiotics due to rising antimicrobial resistance. This model employs 1.6 million bioactive molecules with drug-like properties from the ChEMBL dataset to jointly pretrain three encoders:SMILES, graph and fingerprint encoder. The experimental results seem encouraging.

### Strengths
The authors conducted multiple down-stream tasks to verify the efficacy of their method.

Overall, the paper is clearly represented.

### Weaknesses
1. The technical novelty is limited.
1.1.  While the paper mentions contrastive learning as a foundational concept, it lacks a clear explanation of how this framework uniquely applies to antibiotic property prediction compared to existing methodologies. A more detailed discussion would help contextualize its application. The contrastive loss is the vanilla form of classical contrastive learning?
1.2.  Although the bi-level routing attention mechanism is a critical innovation in the model, the explanation provided is somewhat vague.

2. There are several statements that lack specificity and can be interpreted in multiple ways. For instance, the authors make sweeping claims about model performance without providing adequate context or evidence, which decreases the credibility of the discussion.

3. The use of jargon without sufficient definitions makes it difficult for readers who may not be well-versed in the specifics of deep learning or molecular biology to fully grasp the content. A glossary of terms or more contextual explanations could remedy this.

4. Experiments: 
4.1 It would be better to add some biological justification or visualization of the results.
4.2 Providing specific case studies or examples would not only enrich the findings but also guide future improvements in the model.
4.3 Some results lack proper contextualization, particularly in the representation of RePRA scores, which could lead to misunderstandings.
4.4 Another concern is about label leakage. Is there any overlap between the datasets?

5. While the paper includes anonymous code available on GitHub, it may not be very intuitive for users. ​It is advisable to include straightforward and easy-to-test data alongside the code, or to provide a Jupyter Notebook.​ This would enable readers to quickly and clearly grasp the operational process of the method.

### Questions
1. Could you clarify the interpretation of the RePRA scores presented in the results?
2. Are you considering including specific case studies where the model performed well or poorly to better illustrate these points?

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
This study presents a novel pre-training strategy for a multimodal representation model for the aiding in the discovery/design of antibiotic drugs. This method learns to map three different modalities describing molecular systems (1. SMILES string, 2. Molecular graph, 3. Molecular hash-based circular fingerprints) into a shared embedding space through contrastive learning.

Each modality has an associated architecture to map the raw data into the shared embedding space, it is divided as follows:

1. SMILES strings are modelled with a transformer architecture with rotatory positional embeddings.
2. Molecular graphs are modelled with a graph transformer encoder (GTE). The study introduces the bi-level routing attention (BRA) from computer vision models to molecular graphs as an additional component to the graph transformer encoder.
3. Molecular fingerprints are modelled with a multi-layer perceptron.

The model is pre-trained in the subset of ChEMBL molecules with known antibiotic activity with over 1.5 M data points.

The approach is evaluated against 5 datasets relevant for antibiotic discovery and it outperforms the baselines considered (3 molecular language models: MolFormer, MolBERT, and ChemBERTa-2) in 3 of them.

### Strengths
1. **Evaluation.** The experimental results of the model demonstrate a notable improvement with regards to the baselines chosen, the datasets chosen are well studied benchmarks that could be relevant for the purposes of antibiotic discovery/design.
2. **Molecular graph encoder.** The idea of adapting the bi-level routing attention to graphs is interesting and could be beneficial for the broader domain.

### Weaknesses
Main weaknesses
----

1.  **Relevance.** Antibiotic discovery/design is a societally important problem and new approaches for accelerating or improving pharmaceutical pipelines are sorely needed. From a technical standpoint, however, antibiotic small molecules are not inherently different from any other small molecule drugs. I think that the authors should include justification regarding why this method is specifically well-suited for antibiotics and not for any other class of small molecule (e.g., is there any antibiotic-specific inductive bias embedded in the method?) Conversely, if there is no technical reason why the method could not be applied to other small molecule drugs, then I think that its evaluation should concern a more diverse evaluation including general benchmarks like MoleculeNet [1] or Therapeutic Data Commons [2].
2.  **Baselines.** The baselines considered in Table 2 and Figure 2 correspond to Molecular Language Models. The method herein proposed combines three different modalities (or molecular views), i.e., fingerprints, molecular graph, and SMILES (or molecular language). Therefore, I think that additional baselines  should be included to, at least, consider:
   - i) A model with fingerprints as input that can be an MLP or any other type of downstream model.
   - ii) A GNN for the molecular graphs.
   - iii) A contrastive learning pre-trained model like MolCLR [3].
3.  **Ablation study.** The ablation study conducted with models CL-BL1-4 only concerns the molecular graph and the different components that integrate it. There are missing elements in this ablation that should be considered:
   - i) the contribution of each modality (does the performance change when the SMILES, the graphs, or the fingerprints are not used?)
   - ii) 2. is the pre-training helpful or could the same performance be achieved with a model trained from scratch for each dataset?
   - iii) what would happen if the more general models like MolFormer or ChemBERTa-2 were finetuned to the same pre-training data as the model?
4.  **Significance of results**. The results in Table 2 and Figure 2 do not have an error associated which makes it difficult to compare among approaches as there is no sense on the variability between independent runs. The introduction of error estimations for different runs (3 or 5 would be sufficient) would provide a proxy value that would give an intuitive idea of the statistical significance of the differences between model performances.

Minor weaknesses
----
_(These weaknesses do not influence my decision-making, but I think could serve to improve the paper)_

1. There are minor typos throughout the paper.
2. Please note that the PDF corresponds to the ICLR template for 2024 and not 2025, be careful when submitting the final version.
3. The description of bi-level routing attention focuses primarily in its original use in computer vision, where context windows are described in terms of a 2D feature map or pixel-to-pixel attention, I would find it helpful if the explanations concern the generalisation of the method to graphs and how the concept of 2D feature map or pixel would apply to graph topology.
4. There is not a description of what fingerprint was used, even though, is one of the modalities used in the paper (In appendix A.2, ECFP is mentioned as a standard baseline, but no further details regarding the pre-trained model are included). Not only fingerprint type is missing, but also critical parameters as number of bits in the fingerprint (1,024; 2,048; ...) and radius (1, 2, ...).

### Questions
1. What is the reason why you think this particular approach is specifically well-suited for representing antibiotic drugs? Have you run a comparison of your method against other benchmarks for a wider class of small molecules (e.g., MoleculeNet [1] or Therapeutics Data Commons [2])
2. What criteria was used to decide on the downstream datasets? What other datasets were considered and why were they excluded?
3. Were other fingerprints types or configurations considered for the fingerprint modality? If so, which and what criteria was used to reach the final decision?


References
----
1. Wu Z, Ramsundar B, Feinberg EN, Gomes J, Geniesse C, Pappu AS, Leswing K, Pande V. MoleculeNet: a benchmark for molecular machine learning. Chemical science. 2018;9(2):513-30.
2. Huang K, Fu T, Gao W, Zhao Y, Roohani Y, Leskovec J, Coley CW, Xiao C, Sun J, Zitnik M. Therapeutics data commons: Machine learning datasets and tasks for drug discovery and development. arXiv preprint arXiv:2102.09548. 2021 Feb 18.

### Soundness
3

### Presentation
3

### Contribution
3
