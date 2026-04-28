# FusionDTI: Fine-grained Binding Discovery with Token-level Fusion for Drug-Target Interaction

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Predicting drug-target interaction (DTI) is critical in the drug discovery process. Despite remarkable advances in recent DTI models through the integration of representations from diverse drug and target encoders, such models often struggle to capture the fine-grained interactions between drugs and protein, i.e. the binding of specific drug atoms (or substructures) and key amino acids of proteins, which is crucial for understanding the binding mechanisms and optimising drug design. To address this issue, this paper introduces a novel model, called FusionDTI, which uses a token-level \textbf{Fusion} module to effectively learn fine-grained information for \textbf{D}rug-\textbf{T}arget \textbf{I}nteraction. In particular, our FusionDTI model uses the SELFIES representation of drugs to mitigate sequence fragment invalidation and incorporates the structure-aware (SA) vocabulary of target proteins to address the limitation of amino acid sequences in structural information, additionally leveraging pre-trained language models extensively trained on large-scale biomedical datasets as encoders to capture the complex information of drugs and targets. Experiments on three well-known benchmark datasets show that our proposed FusionDTI model achieves the best performance in DTI prediction compared with eight existing state-of-the-art baselines. Furthermore, our case study indicates that FusionDTI could highlight the potential binding sites, enhancing the explainability of the DTI prediction.}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents FusionDTI, a new model designed to improve drug-target interaction (DTI) predictions. FusionDTI employs a token-level Fusion module to capture fine-grained interactions between drug atoms and protein amino acids. It utilizes the SELFIES representation for drugs and a structure-aware vocabulary for target proteins, while leveraging pre-trained language models to enhance understanding of complex relationships. Using the drug and protein embeddings, some existing embedding fusion strategies were evaluated.   Experiments demonstrate that FusionDTI outperforms eight state-of-the-art models, and its case study highlights potential binding sites, increasing the explainability of DTI predictions.

### Strengths
-Used large language models to extract both protein and drug features.
-Evaluated the performance of the model for both in-domains and out-of-domains.
-Explored potential interpretability of the model.

### Weaknesses
 -Overall, the novelty of the approach is low. It is not novel to apply large language model to extract protein and drug features in DTI prediction. Many related work have been published.
-It is also not novel to use the applied fussion strategies for DTI prediction. Both of the fusion strategies have been widely used before.

-The case example appears overly simplistic. The selection of only three DTI pairs, without a clear rationale for their choice, raises concerns about the generalizability of the findings. Furthermore, the analysis lacks a rigorous assessment of the model's performance on diverse and challenging cases.

### Questions
The case example appears overly simplistic. Is this prediction based on in-domain or out-of-domain data? I recommend conducting an analysis of out-of-domain cases. Additionally, the results would benefit from external validation. For instance, performing blind docking studies on the drug-protein pairs could confirm whether they truly interact as predicted, and visualizing the binding sites would provide further insights into the interaction.

### Soundness
2

### Presentation
3

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
This paper presents FusionDTI, a model for drug-target interaction (DTI) prediction that claims to improve interpretability through fine-grained interactions between drug components and protein residues. The authors leverage the two existing backbone models (BAN and CAN) to achieve the token-level interaction and finally search for the bind site with these tokens.

### Strengths
- The paper is well-written and easy to follow.
- The proposed token-fusion (TF) strategy is straightforward yet reasonable.
- The experimental results and case studies demonstrate excellent prediction performance and strong interpretability.

### Weaknesses
The authors leverage two existing backbone models (BAN and CAN) to achieve token-level interactions and ultimately search for binding sites using a dense linkage of all these tokens, which appears to be both simple and computationally intensive. Notably, DrugBAN has already employed BAN for a quite similar fusion objective, with the only difference being that the basic element is the substructure. Therefore, the novelty proposed by the authors is concerning. The approach seems like a straightforward extension of patch-based methods, such as those used in ViT [1], to the token level, lacking a strong justification for its design. Furthermore, the claim that DTI is determined by single atom and individual amino acid residues contradicts findings in the literature [2], which emphasize the importance of complex interactions between molecular substructures and binding sites. This undermines the core motivation of the proposed method.

The paper lacks a theoretical contribution regarding the proposed method for the DTI task. The authors do not provide a mathematical analysis of the token-level interaction strategy, instead focusing on motivation and experimental results. A deeper theoretical justification for the value of this approach is needed.

In the case study for searching for binding sites, FusionDTI-CAN is adopted for comparison with DrugBAN. It seems more reasonable to use FusionDTI-BAN for a fair comparison, which raises confusion. So why not choose BAN as backbone model? Given the close relationship to DrugBAN, a controlled comparison is essential to demonstrate the superiority of the proposed method. The authors should provide a direct comparison using FusionDTI-BAN, especially since they have already trained this model.

Although the TF module is useful, its computational complexity clearly indicates that it is quite time-consuming. My concern is the computational resources required for training, particularly with larger drug molecules or larger protein sequence datasets. The token-level interactions inherently increase the computational burden, which needs to be addressed.

It should be clear whether the improvements benefit from the pre-trained language models. The ablation results of w/o LLM pre-trained feature is needed. The authors' claim that "FusionDTI-BAN, which leverages pre-trained features, consistently outperforms DrugBAN, which does not,” only intensifies the concern that the performance gains are primarily due to the pre-trained representations rather than the proposed token-level interaction strategy. This issue needs to be addressed with a proper ablation study.

### Questions
- The authors leverage two existing backbone models (BAN and CAN) to achieve token-level interactions and ultimately search for binding sites using a dense linkage of all these tokens, which appears to be both simple and computationally intensive. Notably, DrugBAN has already employed BAN for a quite similar fusion objective, with the only difference being that the basic element is the substructure. Therefore, the novelty proposed by the authors is concerning.
- The paper lacks a theoretical contribution regarding the proposed method for the DTI task.
- In the case study for searching for binding sites, FusionDTI-CAN is adopted for comparison with DrugBAN. It seems more reasonable to use FusionDTI-BAN for a fair comparison, which raises confusion. So why not choose BAN as backbone model?
- Although the TF module is useful, its computational complexity clearly indicates that it is quite time-consuming. What will happen if the model is faced with larger drug molecules or larger protein sequence datasets?
- It should be clear whether the improvements benefit from the pre-trained language models.  The ablation results of w/o LLM pre-trained feature is needed.

### Soundness
2

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
5

### Summary
The authors present FusionDTI, a drug-protein interaction prediction model developed to enhance fine-grained interaction learning. The model introduces a token-level (atoms for drugs, residues for proteins) fusion module based on bilinear attention (BAN) or cross-attention (CAN) mechanisms. It leverages pretrained encoders, Saprot for ligands and SELFormer for proteins, to capture comprehensive molecular features. Experimental results on three benchmark datasets demonstrate robust improvements over competitive baselines. The authors also include extensive ablation studies to validate the uniqueness and effectiveness of each component in FusionDTI. Furthermore, a case study illustrates how the fine-grained interaction learning enhances model interpretability.

### Strengths
- The fine-grained interaction learning is the performance bottleneck of DTI prediction models, which is valuable for designing new strategies.
- The fusion module is clearly defined.
- A comprehensive ablation study is conducted to examine each part of the model, including different pretrained models, fusion modules, and hyperparameters.

### Weaknesses
 - While the study is technically sound, many of the components used in FusionDTI, such as the cross attention and bilinear attention mechanisms, have been well studied in previous DTI research as acknowledged and cited by the authors. FusionDTI appears to be more of **an integration of known pretrained encoders and existing interaction modules**. We may not gain new insights from this study into improving the computational simulation of drug-protein binding, as using attention mechanisms for atom-residue interactions is already a widely adopted strategy. This raises questions about the study’s methodological novelty.

- The model interpretation aspect of the study has several limitations:

    - The selected cases for demonstrating FusionDTI's interpretability are **not representative**. Readers would be interested not only in the very top predictions but also in moderate and poor predictions (like some bad case analysis) because there is no clear threshold or metric provided to assess whether a prediction is good enough for practical interpretative use.

     - Some inconsistencies in the case study results need to be addressed. For instance, GLN92 is highlighted in Table 5 but does not appear in Figure 9. Please double check that.

    - Incorporating a **binding structure visualization analysis** would greatly enhance the comparison between the predicted interactions and the experimentally validated interactions. It would be also helpful for determining which one (FusionDTI or DrugBAN) aligns best with the known interactions.

    - A better solution could involve **quantifying the attention visualization results**. For example, calculating how much of key residues or interactions are highlighted by attention weights on a larger scale dataset, such as PoseBusters or CASF, would help to verify the tool’s effectiveness in elucidating drug-protein binding modes.

### Questions
- What specific **selection criteria or threshold for attention weights** were used to determine the predicted interactions between ligand atoms and protein residues?
- The accuracy results for the Human dataset are missing.

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
5

### Summary
The paper presents FusionDTI, a deep learning architecture for drug-target interaction (DTI) prediction that aims to capture fine-grained binding patterns between drug atoms and protein residues. The model's architecture integrates two specialized pre-trained language models: SELFormer for drug molecule encoding (using SELFIES representation) and Saport for protein sequence processing (using structure-aware vocabulary). The core contribution lies in the token-level fusion module, implemented through two variants: Bilinear Attention Network (BAN) and Cross Attention Network (CAN), designed to model detailed interaction patterns between molecular components.

The authors evaluate the model on three established DTI benchmark datasets using both in-domain and cross-domain validation protocols. Comparative analysis against eight baseline methods demonstrates competitive performance, with the CAN fusion module showing superior capability in capturing fine-grained interactions compared to BAN. The authors provide interpretability analysis through case studies that align with known binding site information from crystallographic structures. 

While the implementation is technically sound and shows incremental improvements over existing methods, the primary innovation lies in the integration of established techniques rather than fundamental methodological advances in DTI prediction.

### Strengths
Well-engineered integration of state-of-the-art components

### Weaknesses
1. **Architectural Considerations**
        - The fusion module's novelty could be better justified beyond combining existing approaches
        - There is a contradiction in the description of model flexibility: it claims that the encoder can be replaced but relies on specific SELFIES and SA representations
2. **Methodological Aspects**
        - The dataset selection and splitting strategy, while valid, follows previous work (DrugBAN) without significant adaptation
        - The evaluation metrics suite could be expanded to include F1-score and Matthews Correlation Coefficient
3. **Experimental Validation**
        - Case studies could be more innovative and differentiated from DrugBAN
        - The same evaluation metrics in DrugBAN should be shown

### Questions
1. **Methodology**
        - What motivated the selection of unpublished work (SiamDTI) as a baseline?
        - How does protein sequence length impact prediction accuracy?
        - Please specify the dataset context for results in Figures 5-7
2. **Theoretical Foundation**
        - What evidence supports the correlation between token-level interactions and actual molecular binding sites?
        - How was the choice between BAN and CAN architectures motivated?
3. **Practical Applications**
        - Has the model been validated in real-world drug discovery scenarios like virtual screening?
        - How can this approach be extended to other types of molecular interactions beyond DTI?

### Soundness
2

### Presentation
3

### Contribution
2
