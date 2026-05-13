# Benchmarking DNA Sequence Models for Causal Variant Prediction in Human Genetics

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
Machine learning holds immense promise in biology, particularly for the challenging task of identifying causal variants for Mendelian and complex traits.  Two primary approaches have emerged for this task: supervised sequence-to-function models trained on functional genomics experimental data and self-supervised DNA language models that learn evolutionary constraints on sequences.  However, the field currently lacks consistently curated datasets with accurate labels, especially for non-coding variants, that are necessary to comprehensively benchmark these models and advance the field.  In this work, we present TraitGym, a curated dataset of genetic variants that are either known to be causal or are strong candidates across 113 Mendelian and 83 complex traits, along with carefully constructed control variants.  We frame the causal variant prediction task as a binary classification problem and benchmark various models, including functional-genomics-supervised models, self-supervised models, models that combine machine learning predictions with curated annotation features, and ensembles of these.  Our results provide insights into the capabilities and limitations of different approaches for predicting the functional consequences of genetic variants.  We find that alignment-based models CADD and GPN-MSA compare favorably for Mendelian traits and complex disease traits, while functional-genomics-supervised models Enformer and Borzoi perform better for complex non-disease traits.  All curated benchmark data, together with training and benchmarking scripts, will be made publicly available upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This manuscript presents a comprehensive benchmarking analysis for a wide range of DNA models in the task of predicting causal non-coding variants. The benchmark spans multiple model types, including supervised sequence-to-expression models, self-supervised DNA models, and baselines leveraging genome annotation-based summary statistics. The authors evaluate models on both Mendelian and complex traits, with a further distinction between disease and non-disease traits.

### Strengths
- This paper offers rigorous benchmarking for DNA models on causal variant prediction, ensuring a balanced comparison by controlling for factors such as distance to the transcription start site (TSS) and minor allele frequency (MAF) in the positive-negative matching.
- It evaluates an extensive array of model types, from supervised and self-supervised DNA models to non-ML baselines using CADD features, which adds robustness to the benchmark.

### Weaknesses
 - The benchmark could be better positioned within the landscape of existing DNA benchmarks. While the authors have added a paragraph since my last review they haven't answered the question of what this particular benchmark brings in terms of insights on top of other existing ones. The discussion is just focused on the source of the variants. I appreciate that the CADD models provide a good baseline, and other benchmarks may not have this.


### Questions
- Please highlight any distinct model insights provided by this benchmark on top of other similar benchmark which is not based on the source of variants

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
This paper describes the curation of two benchmark datasets for evaluating approaches to predicting causal genetic variants. A study was performed to compare several such existing methods (including one trained by themselves) from three categories using the proposed benchmarks.

### Strengths
-  After made available, the two curated benchmark datasets can help to advance the field of developing computational approaches to identifying genetic variants with major functional consequences. 

- It is interesting to see that considering alignment is important in self-supervised training for causal variants prediction. (By comparing gLM-Promoter and GPN-MSA if I understand correctly.) 

- Analyzed model predictions from varying prospectives and the obtained results are interesting

- It is interesting to see the ensembling of outputs of different models leads to the best predictions.

### Weaknesses
 - The technical contribution may be considered low with minimal innovation.

- More discussion about gLM promoter and its difference from GPN-MSA and other self-supervised trained models would be helpful. Specifically, the architectural differences and training data between gLM-Promoter and GPN-MSA should be elaborated on, as well as how these differences might lead to the observed performance variations. It would also be beneficial to discuss how gLM-Promoter compares to other existing self-supervised models in terms of architecture, training data, and performance.

- A cross comparison between the curated genetic variants with those from ClinVar would strengthen this study. The analysis should not only focus on the distribution of variant types (e.g., coding vs. non-coding) but also assess the overlap in specific variants and their predicted functional impact. This would provide a more comprehensive view of the datasets' utility and limitations.

- Why choosing to use common variants as controls in the study of Mendelian traits? The causal variants of Mendelian traits are typically rare (i.e., low MAF). It is important to acknowledge the limitations of using common variants as controls, as they may not accurately represent the characteristics of truly benign variants in the context of Mendelian disorders. The study should discuss the potential biases introduced by this choice and explore alternative control sets, such as variants with strong evidence of being benign.

### Questions
- Why choosing to use common variants as controls in the study of Mendelian traits? The causal variants of Mendelian traits are typically rare (i.e., low MAF).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
TraitGym introduces a benchmarking framework designed to evaluate DNA sequence models in their ability to distinguish causal from control variants across a wide range of traits, covering 113 Mendelian and 83 complex traits. The benchmark relies heavily on established datasets, particularly those curated and described in Finucane et al. (2019, 2024) and databases like gnomAD and OMIM. TraitGym’s primary contributions focus on developing matched negative control sets for variants labeled as pathogenic in previous studies, as well as introducing a new genomic language model, gLM-Promoter. This model claims to specifically train on promoter regions to capture regulatory features that may play a role in causal variant prediction, addressing a gap in current modeling approaches.

The framework evaluates several model types, including functional-genomics-supervised, self-supervised, and integrative models, on a binary classification task aimed at identifying causal versus non-causal variants. To improve predictive performance, TraitGym further explores ensemble approaches, combining features from different models to leverage distinct predictive signals. This work include s an stratification of variant-type and traits to further understand model performance. Additionally, it incorporates a feature interpretation analysis to reveal insights into trait-specific effects across tissues, aiding in the understanding of trait relevance and tissue-specific regulatory mechanisms associated with the variants under study.

### Strengths
TraitGym provides a diverse evaluation framework by assessing a range of models, including supervised, self-supervised, and integrative types, enabling a comprehensive comparison across different model architectures. The benchmark’s use of publicly available data sources and well-established resources like gnomAD and OMIM enhances accessibility and reproducibility, contributing to transparency and ease of use for the broader community. The inclusion of the gLM-Promoter model offers a unique approach focused on promoter regions, which may uncover regulatory insights specifically related to these key genomic areas. Additionally, TraitGym’s exploration of ensemble methods, trait specific stratification, and feature interpretation for both CADD and Borzoi is interesting.

### Weaknesses
Data Curation and Benchmark Design

The threshold for minor allele frequency (MAF) in pathogenic OMIM variants, set at 0.1%, appears arbitrary, particularly since a 1% threshold is typically standard for rare variants. The lack of ablation studies to justify this choice is a significant concern, as it's unclear how this threshold impacts the balance between positive and negative samples and the overall performance of the benchmark. The control matching process, while using TSS distance, MAF, and LD score, would also benefit from a more rigorous approach, such as closest gene-specific stratification. Matching controls solely based on Euclidean distance across these features assumes they are equally relevant, which may not hold true. Given that MAF and LD score are more population-dependent, while TSS distance is more functionally related, this approach risks introducing biases in the control set, potentially leading to spurious correlations and inflated performance metrics. Furthermore, the choice of nine negative controls per causal variant, without a clear justification, raises concerns about the robustness of the benchmark and the potential for biased results due to an insufficient number of negative samples.

Model Evaluation Framework:

The leave-one-chromosome-out (LOCO) validation approach in the linear probing evaluations has notable limitations. Chromosomes differ significantly in size, gene density, and variant distribution, leading to inconsistencies in split sizes and class balance for variant groups. Smaller chromosomes, such as chromosome 21, have fewer variants, which can skew model performance and impact the validity of linear probing, potentially leading to unreliable generalization estimates. Additionally, the evaluation of the CADD model introduces a significant risk of data leakage. CADD is a meta-predictor that integrates conservation scores and population data, among other annotations, and if any benchmark variants overlap with those in CADD’s training data, the evaluation may be inadvertently biased in CADD's favor. Without a thorough check of these overlaps, the comparison with CADD is potentially flawed and could lead to misleading conclusions about the relative performance of other models.

gLM-Promoter Model Clarity

The gLM-Promoter model’s design and training process lack sufficient detail, which weakens its clarity and potential impact. Missing information includes the model's approach to defining promoter regions, the rationale behind choosing a 512bp window size, and how TSS coordinates are determined across different genomes. The current evaluation appears limited and does not specify if the model was exclusively tested on promoter variants, nor does it present a comparison across different variant types. Furthermore, it is unclear whether the evaluated variants are distinct from those seen in the model’s training, particularly when using the human reference genome. The lack of clarity on training data and evaluation methodology makes it difficult to assess the true contribution of gLM-Promoter to the benchmark.

Organization and Clarity Issues

Several presentation issues detract from the paper's readability and clarity. Figure 1, for instance, is overly complex and could benefit from simplification to improve interpretability. Additionally, the writing style is often verbose, and adopting a more concise approach would enhance clarity. For example, the parenthetical explanation of Mendelian versus complex traits in the introduction disrupts the flow unnecessarily and could be integrated more smoothly into the text.

### Questions
Could the authors clarify whether variants used in the evaluation overlap with those in CADD’s training data? This would help ensure unbiased results by addressing potential data leakage.

Why was a threshold of nine negative controls chosen per causal variant? An explanation of how this number impacts benchmark robustness would provide greater clarity on the control selection process.

Were ablation studies conducted to assess the impact of the 0.1% MAF threshold for OMIM variants on model performance? A comparison with a 1% threshold would align with conventional standards and strengthen the study’s design choices.

Were any ablation studies conducted to explore a range of posterior inclusion probability (PIP) thresholds for the complex trait benchmark? Examining how different PIP thresholds impact model performance could provide valuable insights into the robustness of the benchmark design for complex traits.

Could the authors provide additional information on their approach for trait- and tissue-based evaluations? Including positive and negative splits for these analyses, as well as integrating plausibly causal eQTLs (e.g., from GTEx fine-mapping), could enhance interpretability and contribute novel insights into trait- and tissue-specific variant effects.

Would the authors consider further expanding the trait analysis by integrating eQTL datasets (such as GTEx fine-mapping) that overlap with causal variants from Finucane et al. (2015) or OMIM? This approach could create a unique dataset combining eQTLs with fine-mapped UKBB GWAS variants, potentially providing additional validation and highlighting cases where expression changes may not fully capture phenotypic effects at the organism level.

### Soundness
2

### Presentation
1

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
This paper conducted a benchmarking study of DNA sequence models for predicting causal genetic variant for 113 Mendelian and 83 complex traits. They tested the performance of three different types of methods, including functional-genomics-supervised models, self-supervised genomic language models (gLMs), and integrative models that combine machine learning predictions with annotation features (from the viewpoint of ensemble learning). The benchmark results demonstrated differences in model performance across different types of trait, different model classes, and different variant types

### Strengths
1.	The consideration of both Mendelian and complex traits provides a quite comprehensive dataset of genetic variants, which is a valuable contribution to the field. Especially the performance difference across different types of traits could deepen the understanding of how a causal genetic variant may contribute to a trait or disease.
2.	The computational problem is well-defined by treating it as a binary classification of causal versus non-causal variants. The negative non-causal variants set should also be very useful in many computational models where negative controls are needed.
3.	The authors demonstrate that combining different types of computational models leads to performance improvements, especially for complex traits. This finding suggests that distinct models capture complementary information that can be leveraged for more accurate predictions.

### Weaknesses
1.	The numbers of both variants and traits are small. The way for the benchmark study to define the causal variants is too simple and might be controversial. Both OMIM pathogenic annotation and PIP>0.9 do not imply the variant is causal. The OMIM database, while useful, is not a definitive source of causal variants, as it often includes variants with varying degrees of evidence. Similarly, a PIP>0.9 from a GWAS only indicates a strong statistical association, not necessarily a direct causal relationship. The study should acknowledge the limitations of using these proxies for causality and explore alternative approaches for defining causal variants.
2.	Many baseline methods were missed. The authors may refer to a very recent variant effect prediction benchmark study (doi: 10.1186/s13059-024-03314-7). 24 methods for variant effect prediction were benchmarked. In another benchmark study in 2023 (doi: 10.15252/msb.202211474), 55 variant effect predictors were benchmarked. Many of those methods were ignored in this study. The lack of comparison with a wider range of existing methods, especially those specifically designed for non-coding variant effect prediction, limits the study's ability to contextualize the performance of the tested models. The authors should justify their choice of baseline methods and consider including more established approaches.
3.	The evaluation metric used by the benchmark study is too simple based on the binary classification problem. In most of the cases, the number of non-causal variants are far more than causal variants. The auPRC will be affected by the imbalance ratio. Other metrics, such as auROC, precision, recall, f1-score are also necessary to provide more comprehensive benchmark results. Relying solely on auPRC can be misleading due to the class imbalance. The authors should include additional metrics to provide a more robust evaluation of model performance, particularly metrics that are less sensitive to class imbalance, such as the Matthews correlation coefficient (MCC).
4.	Why only choose 9 non-causal variants as negative controls? The true causal variant proportion for different traits or diseases might be significantly different. Using a constant proportion here for different trait might not be consistent with the true biology. The arbitrary choice of 9 negative controls per positive variant is not well-justified. The authors should consider using a more biologically informed approach to select negative controls, such as matching the allele frequency distribution of the causal variants or using a larger set of negative controls to better represent the true distribution of non-causal variants.

### Questions
1.	The causal variants of Mendelian traits were collected from a single source (Smedley et al., 2016). The causal variants of complex traits were collected from also a single source (UKBiobank). It would be more meaningful if the authors could incorporate more complex traits and disorders with well-defined causal variants, such as those from FinnGen or other large BioBanks, to improve the benchmark’s generalizability.
2.	The authors need to address how biases in the single dataset curation might affect benchmarking results and suggest methods for mitigating these biases, such as incorporating data from additional cohorts or stratified sampling.
3.	Since many deep learning models were included. Any way for enhancing the interpretability of the results by analyzing the biological relevance of model predictions? For instance, interpret how causal variants affect gene regulation networks.

### Soundness
2

### Presentation
2

### Contribution
2
