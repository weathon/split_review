# GlycoNMR: A Carbohydrate-Specific NMR Chemical Shift Dataset for Machine Learning Research

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Molecular representation learning (MRL) is a powerful contribution by machine learning to chemistry as it converts molecules into numerical representations, which serves as fundamental for diverse biochemical applications, such as property prediction and drug design. While MRL has had great success with proteins and general biomolecules, it has yet to be explored for carbohydrates in the growing fields of glycoscience and glycomaterials (the study and design of carbohydrates). This under-exploration can be primarily attributed to the limited availability of comprehensive and well-curated carbohydrate-specific datasets and a lack of machine learning (ML) techniques tailored to meet the unique problems presented by carbohydrate data. Interpreting and annotating carbohydrate data is generally more complicated than protein data, and requires substantial domain knowledge. In addition, existing MRL methods were predominately optimized for proteins and small biomolecules, and may not be effective for carbohydrate applications without special modifications. To address this challenge, accelerate progress in glycoscience and glycomaterials, and enrich the data resources of the ML community, we introduce GlycoNMR. GlycoNMR contains two laboriously curated datasets with 2,609 carbohydrate structures and 211,543 annotated nuclear magnetic resonance (NMR) atomic-level chemical shifts that can be used to train ML models for precise atomic-level prediction. NMR data is one of the most appealing starting points for developing ML techniques to facilitate glycoscience and glycomaterials research, as NMR is the preeminent technique in carbohydrate structure research, and biomolecule structure is among the foremost predictors of functions and properties. We tailored a set of carbohydrate-specific features and adapted existing MRL models to effectively tackle the problem of predicting NMR shifts. For illustration, we benchmark these modified MRL models on the GlycoNMR.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The Manuscript presents a benchmark data set for NMR shift prediction in carbohydrates. It then also introduces some features based on domain knowledge that can be used to build classifiers based on the benchmark data.

### Strengths
The data set seems to be a valuable contribution to the presented domain (NMR shift prediction in carbohydrates).

The engineered features might enhance future prediction models.

### Weaknesses
I have a problem with reproducibility. The introduction is very extensive (the own contributions basically start at page 5), but in section 3 at page 5 it is only mentioned that substantial domain expertise is required to annotate and process the data from Glyco-sciences.DB. This makes it hard to reproduce the methods and also to evaluate the contribution (Glyco-sciences.DB -> GlycoNMR.Exp). Also the sentence in the middle of page 6 "we had to utilize domain knowledge to reduce such ambiguities as much as possible when handling..." is not really describing a procedure in a reproducible manner. It is clear that not all domain knowledge can be described, but one could spend more space on the own contributions and less on the general introduction (currently 4 pages).

This is apparently addressed better after the revision, but still I think this contribution should be part of the manuscript and one could cut some of the content of the 4 pages introduction.

Furthermore, the simulated part of the data base is a little bit more problematic, since one model (GODESS) is used directly. It is questionable if ML models trained on the simulated data can learn important parameters that are not already known from GODESS. For a performance comparison of different models the data set might still be valuable, with the remark that GODESS might produce a biased view of the real world in which some methods perform worse than they would perform on real data (and we cannot judge, because we do not know the biases of the individual methods).

The authors addressed some points in the revision, but the problem is still that the potential biases of GODESS make it hard to decide how useful such a data set based on this one simulation software is.

### Questions
It would be good to concisely define the NMR shift prediction problem in the main manuscript.

SHAP values should be included into the manuscript for comparison.

I am not sure, if the Glycoscience.DB data could be used directly under a CC license, because it is not accessible and therefore, I cannot check the license. There should be a statemtent regarding making this data available in the manuscript.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper explores the application of Machine Learning to carbohydrate studies using NMR by offering data sources and providing a benchmark. The main contribution of the paper is the "GlycoNMR" dataset which contains two laboriously curated datasets.
The authors made predictions on specific chemical properties using their proposed dataset using tailored a set of carbohydrate-specific features. The authors hope that this research helps ML researchers in carbohydrate research. The authors acknowledged some limitations in their dataset and highlighted the need for more comprehensive data in upcoming research.

### Strengths
The paper introduces a dataset to expand the NMR studies on carbohydrates, an area that presents substantial challenges.
The authors also presented a set of features for carbohydrates.
The quality is acceptable; the methods used for data annotation and feature engineering are described, though there's room for refining the approach in places. 
The paper sets a dataset for more in-depth studies and it adds incremental value to the ongoing research in the domain.

### Weaknesses
The paper provides statistics on the dataset but omits details for certain features like ring size, ring position, and atom type. Adding those statistics would add to the clarity of the features extracted. Additionally, a deeper validation of the introduced features would enhance the paper's value and credibility. Specifically, the paper lacks a rigorous analysis of feature importance and how each feature contributes to the model's predictive power. Without this, it's difficult to assess the true utility of the proposed carbohydrate-specific features. Furthermore, the relationship between ring position and chemical shift is not thoroughly explored. While the authors mention that ring position influences the chemical shift, they do not provide a detailed analysis of this relationship, including any observed trends or patterns. This limits the understanding of how the dataset can be used to study the underlying chemistry.

### Questions
**Feature Statistics:** There seems to be a bit of missing statistics on some specific features. Could you share some more detailed stats about the ring size, ring position, and atom type? It'd be really helpful to get a fuller picture of the datasets!

**Ring Position vs. Shift Relationship:** Could you provide further elaboration on the relationship between the ring position and the shift? 
Specifically:

* How does the ring position influence the chemical shift value?

* Are there any trends or patterns observed based on different ring positions that affect the shift?

* Including some analysis, possibly graphs or charts that showcase this relationship, could enhance our understanding of the dataset.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is about two databases of NMR of carbohydrate structrures, one extracted from a hand-curated database, another is from a simulation.

### Strengths
A database readily available for ML deployment is usually useful for ML research.

### Weaknesses
Since it is a database paper, I'm looking for its significance to the field. While it can be used, it is very difficult for me to judge its importance and the paper doesn't really help that much. The processing carbohydrate data is "more complicated than protein data, and requires substantial domain knowledge". The comparison with protein data, making protein data "much easier" to work with is not concrete enough. These claims require some evidence to back it up, otherwise, rather hollow.

The first database is extracted from Glycosciences.DB with "domain expertise and efforts". I think this is true for any database extraction, and not any extraction can be that significant. The second database of simulation also needs to show its significance. Does it requires a massive computing power that costs millions of dollar or can be finished in a PC in a couple of hours? In the end, I am still not sure these databases how much effort, is that absolute necessary to generate once and just once for all, or it can be done by most people in the field? How does this work help the field? Is it irreplaceable?

Another thing is to show an example of how useful the database is in some problem. The paper keeps talking about chemical shifts problem without a background that is useful for those who do not work on this problem.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
