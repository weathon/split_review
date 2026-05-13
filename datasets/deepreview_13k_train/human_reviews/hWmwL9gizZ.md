# Immunogenicity Prediction with Dual Attention Enables Vaccine Target Selection

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
Immunogenicity prediction is a central topic in reverse vaccinology for finding candidate vaccines that can trigger protective immune responses. Existing approaches typically rely on highly compressed features and simple model architectures, leading to limited prediction accuracy and poor generalizability. To address these challenges, we introduce \immu, a novel deep learning solution with a dual attention mechanism that integrates pre-trained latent vector representations of protein sequences and structures. We also compile the most comprehensive immunogenicity dataset to date, encompassing over $9,500$ antigen sequences, structures, and immunogenicity labels from bacteria, viruses, and tumors. Extensive experiments demonstrate that \immu~outperforms existing methods across a wide range of evaluation metrics. Furthermore, we establish a post-hoc validation protocol to assess the practical significance of deep learning models in tackling vaccine design challenges. Our work provides an effective tool for vaccine design and sets valuable benchmarks for future research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present the ProVaccine model for immunogenicity prediction, as well as the Immuno datasets of antigens from bacteria, viruses and tumors, which is balanced across protective and nonprotective antigens. They show that ProVaccine is more accurate compared with both baseline ML and hosted models.

### Strengths
- novel model architecture
- contribution of the Immuno datasets
- ProVaccine achieves mostly top performance as reported in Table 1

### Weaknesses
 - It's not obvious what the contribution of any of the representations (sequence, fine, coarse, and descriptors) is to model performance. What if only the sequence representation is used as input? Doing ablation studies is essential for understanding these contributions, and should be included in this work.
- Figure 4 is hard to interpret, it would be easier to understand if instead the likelihood stats of the 11 determined immunogens under each model were reported.
- The appendix is missing:
  - page 7 in section 5.2.1 refers to Tables 4-6 in the appendix
  - page 8 in section 5.3.1 refers to recall and fold-enrichment metrics that do not appear in any table. Also reference is made to Table 10, which does not appear to exist.
  - page 9 in section 5.3.2 refers to Table 11 in the appendix, which does not exist

### Questions
- I don't understand the approach to measuring accuracy described in the first paragraph of section 5.2.1. Are you doing hyperparameter optimization on the validation set for each split? Why randomly select "50% of the test data to calculate the scores for each metric" since you already have a validation set in your split?
- It's not clear what the generalizability of section 5.2.2 is measuring. Should a immunogenicity predictor generalize across bacteria, viruses and humans?
- For the three conclusions about ProVaccine in the final paragraph of subsection 5.3.1, I don't understand how the authors concluded the second and third - could you please explain these in greater detail?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents PROVACCINE, a deep learning model designed to predict the immunogenicity of proteins, which is a crucial task in vaccine development. The authors introduce a dual-attention mechanism within the model, enabling it to process multimodal representations of protein sequences, structures, and physicochemical properties. They also curate Immuno, an extensive dataset of over 9,500 antigen sequences and structures from various sources, to facilitate robust training and validation. The experimental results show that PROVACCINE outperforms traditional methods across multiple evaluation metrics, with specific validation studies on Helicobacter pylori and SARS-CoV-2. The post-hoc analyses further confirm PROVACCINE’s efficacy in identifying potential vaccine targets.

### Strengths
- In my knowledge, the ProVaccine tool is the first method to utilize all three modalities of sequence, structure, and amino-acid descriptors to predict immunogenicity with deep-learning.
- The authors have tried multiple PLMs to encode the sequences (ESM2, ANKH, and ProtBert) and structural embedding methods (ESM3, FoldSeek) to encode the structures.
- They have compiled a new dataset called IMMUNO (stratified by antigen type- viral, bacterial, and tumour), which should serve as a valuable resource for training and benchmarking new methods for researchers in the field.
- They have carried out a very comprehensive benchmarking and compared their method to appropriate baselines and also previous methods in literature. They also carried-out a cross-testing benchmarking of viral, bacterial, and tumour-specific models across datasets to assess the generalizability of the method.
- The post-hoc analyses on specific pathogens (Helicobacterpylori and SARS-CoV-2) provide additional evidence of the model's usability in applied research. The method clearly improves upon immunogenicity prediction accuracy (against previous SOTA) and thus provides a reliable framework for future research in computational vaccinology.

### Weaknesses
 -  Availability of negative dataset is a known problem in this field. The authors have used VAXIJEN to classify sequences as non-antigens and then subsequently filtered the sequences based on sequence-homology to compile the negative dataset. This will bias the negative dataset for certain features which might coincide with the features used in other tools (not just VAXIJEN, AA descriptors used for immunogenicity predictions are generally common across various methods). This might overinflate the recall for the negative class. An alternative approach could be to randomize the order of the amino-acids in the sequence while making sure that the sequence-identity of the randomized sequence isn't similar to any sequence in the positive class. The authors can also look at the IEDB database for compiling the negative dataset as it has sequences of non-antigens from experimental assays (one can chose sequences which were negative in atleast two independent studies)

- For the structural embeddings, the authors have relied on ESMFold for the structure of the antigenic proteins. ESMFold, while much faster than AlphaFold, lags behind in accuracy (in the backbone atoms as well) to AlphaFold/RosettaFold. There isn't any justification provided for choosing these models. There needs to be more analysis done to show how does the structural model quality affect the performance of ProVaccine. The comparison can be done against experimental structures (from PDB), AlphaFold2/3 structures, and other structure prediction methods.

### Questions
- Was there any homology cut-off applied between the training and testing datasets for each class of the antigens? High sequence similarity b/w training and testing might over-inflate performance.

- Most of  the figures have a generic caption. The captions should explain the figures clearly and the results being shown in the figure (especially the figures showing the results and comparison). The results from the figures should also be discussed in the main text in detail. 

- In the post-hoc analysis, it it possible to check how well will the model perform for non-immunogenic antigens in Helicobacter pylori (Fig 4). The sequences of the 11- experimentally verified immunogens can be randomized and then it can be checked where does the prediction for the randomized-sequence lie in terms of probability. The authors also need to describe how 'the probability of identifying known protective antigens through random guessing' was calculated? It's not clear from the current description.

-  Model interpretability plays an important role for any downstream analysis and experimental work (especially in screening vaccine candidates or selecting antigens for vaccine development). Can the weights of the attention modules be used for identifying the immunogenic region in the antigen? This could possibly be leveraged to identify epitopes that can elicit protective antibodies when developing vaccines. This could be an useful addition to the manuscript.

- How would the model handle variations in immunogenicity features across less common or novel pathogens that are not represented in the current dataset?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduced PROVACCINE, a novel deep-learning solution for immunogenicity prediction in reverse vaccinology, designed to identify candidate vaccines that trigger protective immune responses. The authors also constructed a comprehensive immunogenicity dataset with over 9,500 antigen sequences from various pathogens. PROVACCINE employs a dual attention mechanism, integrating pre-trained representations of protein sequences and structures, and outperforms existing methods. The paper provided a comprehensive overview of the problem, related work, and the proposed methodology.

### Strengths
1. This paper proposed a deep learning supervised learning framework with a dual attention mechanism to address the key challenges of immunogenicity prediction in vaccine development.
2. This paper provided a valuable benchmark for future research in vaccine development and immunogenicity prediction.

### Weaknesses
1. The work is innovative to construct a new benchmark dataset, but they didn't show novelty in algorithm development. The authors need to prove their methods on existed dataset, in addition to their own dataset.
2. The dual-attention mechanism, while sophisticated, may increase the computational cost and complexity of the model significantly. The paper does not thoroughly compare this method against simpler architectures to show that the added complexity justifies the performance gains. Specifically, the paper lacks a comparison against a single attention mechanism or simpler concatenation of sequence and structure embeddings.
3. The model’s performance is similar to XGBoost on the largest dataset, Immuno-Virus (1952/1762 positive/negative instances). However, the main improvement over XGBoost is on the smallest tumor dataset (300/477 positive/negative instances). Usually, DL is strong for big dataset and weak for small dataset, in contrary to this study. This discrepancy raised questions about the reliability and robustness of the model's performance. The authors should provide a more in-depth analysis of why the model performs better on the smaller dataset, potentially exploring the feature space and data distribution differences between the two datasets.
4. A major contribution of this work is the construction of a data set for immunogenicity prediction and vaccine development. It’s insufficient to discuss data quality, noise, or variability, particularly for immunogenic labels sourced from different repositories. Moreover, authors should demonstrate that the new dataset is superior to existing datasets. The authors need to provide a more detailed analysis of the data curation process, including the specific criteria used for data inclusion and exclusion, and a quantitative comparison of the dataset's characteristics (e.g., sequence diversity, label distribution) with existing datasets.
5. The authors should include ablation comparisons of sequence and structural features? Specifically, the authors should evaluate the performance of the model using only sequence information, only structural information, and different combinations of sequence and structural features to assess the contribution of each modality.
6. This paper only compares web server methods, lacking comparisons with other deep learning frameworks. The authors should compare their model against other state-of-the-art deep learning models for protein sequence analysis, such as those based on transformers or graph neural networks, to demonstrate the superiority of their approach.

### Questions
The authors need to prove their methods on existing datasets. They also need to dig out why the model shows the largest improvement on the smallest dataset. The case study also needs to discuss about reason, instead of the performance only.

### Soundness
2

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
5

### Summary
In the paper, the authors proposed a protein-language-model-based method called PROVACCINE for predicting the antigen from the amino acid sequence. They constructed the largest and most comprehensive antigen dataset through collecting published sequences. They further conducted cross-validation and some post-hoc analysis to show the effectiveness of the proposed model.

### Strengths
The paper conducted generalization experiments, which is good.
The comprehensive datasets, especially the positive sequence may work as the foundation for other work.

### Weaknesses
1. What I am mostly concerned with is the dataset construction. It seems that the authors construct the positive dataset from the literature, which is great, but the negative data are constructed with some other computational tools. This will lead to a serious problem: if the golden standard is created using BLAST+VAXIJEN, then if we use the combination of the two will be enough, why do we bother to train a model on top of it? 

2. Continuing from 1, the authors should add the baseline method using their way to construct the training dataset, they will get a perfect score for all metrics. The logic for building negative samples is very weird and then making the model unreliable.

3. In section 5.2.1, the authors should also consider splitting the data based on the sequence similarity. If the training and testing data share very high sequence similarity, it's very likely that the model just memorizes the training and can not generalize.

4. I see XGboost and KNN are good from Figure 4 -- suggesting the novel antigens share high similarity with known ones. Actually XGBoost seems to be perfect and much better than Provaccine. The proposed model did not show superiority than the traditional similarity-based method. Moreover, as majority of these 1, 858 sequences lack immunogenicity ground truth labels, how can we ensure the enrichment is a good metric?

5. In section 5.3.2, it's unclear whether the spike protein already exist in the training dataset

6. Continuing from 6, section 5.3.2 is too rough -- it's very easy to identify the spike protein as well as the RBD as the antigen, the results can not support the effectiveness of the proposed model.

Taken together, the proposed method did not show enough novelty, and the performance is not as good as the similarity-based method.

### Questions
See weakness above

### Soundness
2

### Presentation
2

### Contribution
1
