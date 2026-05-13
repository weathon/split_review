# ReNovo: Retrieval-Based \emph{De Novo} Mass Spectrometry Peptide Sequencing

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Proteomics is the large-scale study of proteins. Tandem mass spectrometry, as the only high-throughput technique for protein sequence identification, plays a pivotal role in proteomics research. One of the long-standing challenges in this field is peptide identification, which entails determining the specific peptide (sequence of amino acids) that corresponds to each observed mass spectrum. The conventional approach involves database searching, wherein the observed mass spectrum is scored against a pre-constructed peptide database. However, the reliance on pre-existing databases limits applicability in scenarios where the peptide is absent from existing databases. Such circumstances necessitate \emph{de novo} peptide sequencing, which derives peptide sequence solely from input mass spectrum, independent of any peptide database. Despite ongoing advancements in \emph{de novo} peptide sequencing, its performance still has considerable room for improvement, which limits its application in large-scale experiments. In this study, we introduce a novel Retrieval-based \emph{De Novo} peptide sequencing methodology, termed ReNovo, which draws inspiration from database search methods. Specifically, by constructing a datastore from training data, ReNovo can retrieve information from the datastore during the inference stage to conduct retrieval-based inference, thereby achieving improved performance. This innovative approach enables ReNovo to effectively combine the strengths of both methods: utilizing the assistance of the datastore while also being capable of predicting novel peptides that are not present in pre-existing databases. A series of experiments have confirmed that ReNovo outperforms state-of-the-art models across multiple widely-used datasets, incurring only minor storage and time consumption, representing a significant advancement in proteomics. Supplementary materials include the code.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel approach for predicting peptide sequences from tandem mass spectra, achieving significant performance improvements with a simple retrieval-augmented generation method.

### Strengths
**Originality**. The paper proposes an original idea of connecting database search with *de novo* generation for predicting peptide sequences from mass spectra.

**Quality**. The experiments are sound and the source code is provided.

**Clarity**. The paper is well-written and easy to follow.

**Significance**. The performance improvement upon prior work is substantial.

### Weaknesses
 **Major Comments**

- Missing related work. The paper does not discuss related work on retrieval-augmented generation (RAG) in the context of large language models (LLMs). Is the proposed method novel compared to recent advances in natural language processing?
- Lack of comparison with database search methods. Although overcoming the limitations of database search is a primary motivation, the proposed method is not compared against database search approaches. At least a simple search baseline against the same training database should be implemented for comparison. Ideally, state-of-the-art database search methods should aslo be compared against.
- Potential data splitting issues. The leave-one-out data split by species, while seemingly reasonable, might lead to data leakage. Specifically, the same peptides could appear across different species (potentially even with identical or highly similar MS² spectra). Please analyze the overlap of spectra and peptides between the training and test sets, for example, by assessing vector similarity between binned spectra and sequence identity to evaluate spectral and peptide similarity, respectively.

**Minor Comments**

- Figure 1: Clarify what is meant by “identification rate”—is it the accuracy of preptide prediction?
- Table 1: Confidence intervals or standard deviations for the reported values are missing.
- Line 160: What is the charge state of the precursor ion? Why is it importnant?
- Line 163: “sets” -> “ordered sets of the same size” for mathematical soundness?
- Equation 2: Typo: the comma at the end.
- Line 196: Please clarify how the described features help to attend to differences.
- Line 201: A citation for teacher-forcing is missing.
- Equation 9: Adding one or two sentences explaining the intuition behind this equation could enhance clarity.
- Section 4.1: References for the datasets are missing.
- Section 4.4: If “ReNovo with Residual” is the best-performing method, please clarify why the residual component is not described in the methods section and not used in the final evaluation in Table 1.
- Table 5: Please explain the meaning of “+15.99.”
- Appendix A: References are missing.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
4

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
The paper introduces a new method for predicting peptide sequences from MS/MS spectra, with a key innovation in combining two complementary paradigms in computational proteomics: database search and de novo sequence generation. Specifically, the paper introduces the concept of a datastore, which can be used in conjunction with an autoregressive transformer model. After model training, the datastore stores outputs from the trained model across the entire training dataset, which are then used during test-time inference via k-NN indexing. The method empirically outperforms several state-of-the-art approaches across three datasets, requiring only minor additional storage and time complexity. The authors include ablation studies on key hyperparameters. The code is available in the Supplementary materials.

### Strengths
Originality

The work’s originality mainly lies in the combination of two primary paradigms commonly applied to peptide MS/MS spectra annotation: database retrieval and de novo sequence generation.

Quality

The paper is overal of a good quality, particularly in terms of dataset preparation, benchmarking the proposed method against prior approaches, and the analysis of results.

Clarity

The paper is well-structured, clearly defines the motivation for the proposed methods, and provides a thorough analysis of the results.

Significance

The work offers a new perspective on the problem of de novo peptide sequencing, which could have a strong impact on future research in this area.

### Weaknesses
 - The main concern with the proposed approach is whether the state-of-the-art results are not a consequence of the model’s higher capacity rather than its design. To address this, it would be relevant to see, for example, results from the following experiment: evaluate the ReNovo without Retrieval model of larger size (e.g., by increasing the transformer’s number of layers and hidden dimensionality) and compare it to ReNovo, as illustrated, for instance, in Figure 3.

- Another related concern is the train-test splitting strategy. The text states that “peptides appearing in the testing set are completely distinct from those in the training set.” It would be valuable to assess the method’s performance under a stricter splitting criterion, such as one based on a sequence similarity threshold rather than sequence identity. Such an experiment would demonstrate whether the improved performance is due to generalization rather than overfitting to the training dataset through the “datastore” approach. This could be also tested by measuring the model’s improvement on test sequences that lack similar sequences in the training set.

- Certain essential parts of the text lack clarity.
    - The term “context features” is central to the work but is not clearly defined. Does this refer to an embedding from the last transformer decoder layer? What does $f$ in line 213 signify?
    - The “ReNovo with Residual” model is not fully defined. How exactly are “ReNovo without Retrieval” and “ReNovo” configured?

### Questions
- How was the case study example in Table 5 selected? Is it possible to quantify the number of similar improvements across the entire test set?
- What were the hyperparameters used for training, specifically the number of epochs and learning rate?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper Introduces a novel approach for peptide identification in proteomics, where conventional methods rely heavily on pre-constructed peptide databases, limiting their scope when dealing with novel peptides. ReNovo, leveraging a retrieval-based framework, bypasses this limitation by building a datastore from training data and retrieving relevant information during inference. This approach combines the strengths of both database search and de novo sequencing, enabling it to predict peptides absent from existing databases.

### Strengths
The paper presents strong motivation for combining database search with de novo sequencing, marking the first integration of the Retrieval-Augmented Generation (RAG) method into protein sequence prediction, which adds a novel dimension to the field. The authors effectively demonstrate the proposed method's success, showcasing the potential of integrating RAG into bioinformatics, particularly in areas with extensive databases.

### Weaknesses
1. The paper primarily employs a token-level RAG method from NLP but does not thoroughly discuss its origins or previous related work. Specifically, there is no comprehensive section on RAG methods, with most background instead focused on de novo methods. The approach closely resembles the KNN-LM paper, which originally proposed storing context and next tokens in a datastore; however, this foundational work is not referenced.

Additionally, the paper omits discussion on recent advancements in de novo methods, such as GraphNovo, PepNet, PrimeNovo, and InstaNovo, all of which are documented in Bittremieux et al.'s survey on de novo peptide sequencing methods, if author needs to refer to a good source.

2. Missing Performance Comparisons: The model performance comparisons in the main table do not adequately reflect recent advancements in the field, with several relevant methods from the past year omitted. Including a broader range of models would provide a clearer view of the current state of the art.

3. Clarification is needed on the training and testing datasets: whether a single model was trained on a single dataset and used for all number reporting or if separate models were trained for each dataset? Additionally, it would be helpful to confirm if the reported performance numbers for baseliens are replications or directly quoted from original papers. For instance, discrepancies are noted between some results here and those reported for CasaNovo paper i read from their published journal.

4. For the case study, a direct alignment between the predicted and retrieved spectra would make the comparison clearer. The current presentation lacks an easily interpretable visual comparison of their similarities.

5. If the first stage of training essentially reproduces the Casanovo model, the authors could consider using available open-source models for this step. Testing stronger baseline models could indicate whether enhanced context representations lead to better context features in the datastore. No need to re-train casanovo as first stage IMO.

6. Including a recall-coverage curve could offer valuable insights into performance across varying confidence levels, which is especially useful for biologists relying on model certainty for predictions on unlabeled data. This would provide more depth than single averaged metrics, which may not fully capture the model's reliability.

### Questions
The authors use training data to construct the datastore, but I believe this approach could benefit from further discussion and refinement. In mainstream RAG-based methods, the datastore is generally maintained as an independent entity, distinct from the training data for language models. This separation allows the datastore to act as an “additional” resource that complements a model’s learned knowledge. When the same dataset is used for both training the language model and constructing the datastore, much of the useful information may already be encoded in the model weights through the training phase, reducing the unique value of “retrieval.” Specifically, the language model’s objective—next-token prediction—already captures “context-target” relationships by predicting the next token based on the previous context. Token-level retrieval, in this context, could become redundant, as the model effectively performs this retrieval autonomously. I strongly recommend the authors separate training data from datastore data to better evaluate the impact of retrieval on de novo sequencing. It would also be useful to see how a larger datastore, too complex to incorporate into training, might act as an external resource that enhances model performance.



During inference, could you clarify how the top K “next target” retrievals assist the model? Formulas 9-10 lack clarity in this respect. Simplifying the formulas and using clearer explanations would improve comprehension, as sophisticated formulas are only effective if they are accompanied by a clear rationale. Specifically, does the probability for each amino acid derive directly from the retrieved targets in the output layer, or is it calculated after embedding these K tokens into the input layers?

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
The authors present a method called Renovo for identifying peptide sequences from mass spectrometry data. The challenge of peptide identification is undeniably complex and significant, and this paper offers a solution that integrates prior sequence knowledge into de novo sequencing. This is achieved by revisiting learned co-occurrences of amino acids. The authors evaluate their method against widely used de novo techniques using standard community benchmarking datasets, demonstrating superior performance.

### Strengths
•	The authors advance beyond existing de novo methods by allowing the integration of prior knowledge.

•	They showcase better performance compared to established approaches.

*       The manuscript is well written and easy to follow.

### Weaknesses
•	Mixture methods combining de novo and database searches have been well documented (notably Spider 10.1109/CSB.2004.1332434 and BICEPS 10.1074/mcp.M111.014167). This is not a novel contribution of this paper, as such approaches have been recognized for two decades and should be acknowledged as related work.

•	Error-tolerant and open database searches are prevalent in the field but are not discussed here, despite their potential relevance (as noted in the following point).

•	The authors claim that comparing against database searches is not valid, yet they incorporate prior database information into Renovo that is unavailable to other de novo methods, creating an unfair comparison. Specifically, the method uses a datastore built from training data, which is effectively a form of prior knowledge not available to standard de novo methods. This datastore, while not an external database, still biases the method towards sequences seen during training, which is a form of data leakage if not properly addressed. The authors do not clarify the extent to which related sequences are filtered, raising concerns about the independence of the training and test sets. For instance, if a peptide with a common modification is present in both sets, the method may be learning to identify the modification rather than performing true de novo sequencing. The redundancy of b- and y-ion series in mass spectra further exacerbates this issue, potentially leading to the same spectral information being present in both training and testing, even for peptides that are not identical.



### Questions
•	The specific database information provided to Renovo during the benchmarks is unclear. What is the size of the database, and to what extent are related sequences excluded (are only identical sequences filtered out, or do filters also apply to those with PTMs, chemical modifications, or single amino acid substitutions)?

•	Can the authors compare their results to an error-tolerant/open database search method, such as MSFragger, which is currently considered the gold standard in the field? It may be beneficial to replicate a typical scenario, such as in a 7/9 species setup, where I could supply a complete database of closely related organisms. For instance, while humans and chickens diverged around 300 million years ago, it has been shown that error-tolerant approaches can effectively bridge that gap. Unless going for very obscure organisms, there are related species available and that should be the starting point.

•	In practical proteomics applications, reliability is crucial, yet the benchmark setup appears limited in this context. Most mass spectra tend to be low quality, and redundancy in measurements is high. Standard practice (and often a requirement for publications in the field) necessitates that peptide identifications exceed a 1% false discovery rate (FDR) threshold. Currently, the authors only provide precision and recall metrics, which do not indicate how many peptides the search algorithm considers reliable. It is not essential for every spectrum to be identified. Can the authors also present the number of peptides identified above the 1% FDR threshold?

### Soundness
3

### Presentation
2

### Contribution
3
