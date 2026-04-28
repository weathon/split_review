# Recite, Reconstruct, Recollect: Memorization in LMs as a Multifaceted Phenomenon

- Decision: Accept
- Scores: 5, 6, 8, 8

## Abstract
Memorization in language models is typically treated as a homogenous phenomenon, neglecting the specifics of the memorized data. We instead model memorization as the effect of a set of complex factors that describe each sample and relate it to the model and corpus. To build intuition around these factors, we break memorization down into a taxonomy: recitation of highly duplicated sequences, reconstruction of inherently predictable sequences, and recollection of sequences that are neither. We demonstrate the usefulness of our taxonomy by using it to construct a predictive model for memorization. By analyzing dependencies and inspecting the weights of the predictive model, we find that different factors influence the likelihood of memorization differently depending on the taxonomic category.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a taxonomy for model memorization and classifies model memorization into three categories, namely recitation, reconstruction and recollection. The authors identify several data-related or model-related features and test their correlation with model memorization. To verify the effectiveness of the proposed taxonomy, the authors trained three linear regression models for three categories respectively and found that group the regression models attain better performance than the predictors trained on other features.

### Strengths
+ A new taxonomy for understanding and analyzing the model memorization. 
+ Interesting findings on the dynamics of memorization during the scaling-up of data and model size.
+ An empirical evaluation of the utility of the taxonomy based on predictability.

### Weaknesses
+ A perplexing part of the taxonomy is the classification of repetitive or incremental sequences following a specific pattern. If the sequence duplicates more than five times, how do we know whether it is truly "memorized" or it is reproduced simply because the LLM learns its pattern? 
+ Why do we use more than five times duplication as the decision boundary for recitation and non-recitation. How is the hyper-parameter decided? Using a single threshold actually assumes an equality in difficulty for reciting every sequence.

### Questions
+ The taxonomy of memorization is purely established based on the property of data, i.e., the number of duplications in the pre-training corpus and the implicit template within the data. However, memorization is also a concept and phenomenon related to model behavior and model behaviour can also be included into the taxonomy as an evidence to classify different types of memorization.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel taxonomy for memorization in language models, categorizing it into three types: recitation (highly duplicated sequences), reconstruction (predictable templates), and recollection (other memorized sequences). The authors validate their taxonomy through predictive modeling and analysis across model scales and training time, demonstrating how different factors influence each category distinctly. The work provides valuable insights into understanding memorization as a multifaceted phenomenon rather than a uniform behavior.

### Strengths
The proposed memorization taxonomy is intuitive and interesting, drawing parallels with human memorization. This taxonomy is particularly valuable as it provides a structured approach to analyzing what has typically been treated as a uniform phenomenon. 

The analysis methodology is another strong point, featuring a thorough examination of dependencies between features and memorization categories, supported by effective predictive modeling to validate the taxonomy.

### Weaknesses
The main weakness of this paper boils down to two key issues. First, while the idea of categorizing memorization into three types sounds cool, the paper doesn't dig deep enough to tell us why we should care. Sure, they show that code gets memorized more than text across all categories - but why? And what does this mean for how these models actually work? How different types of memorization contribute to model capabilities. These are the kind of insights that would make the taxonomy actually useful, but they're missing.

In addition, the experimental setup is not convincing. For example, the experiments are conducted solely on Pythia models without validation of other popular models. And some of the key choices seem pretty arbitrary like picking $k=32$ for their memorization tests or saying "more than 5 duplicates" counts as recitation. Why those numbers? What happens if you change them?

Overall, I think the paper lacks insights and the experiments are not very solid.

### Questions
What insights from previous work on memorization mechanisms support or conflict with these findings?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This comprehensive paper presents a novel taxonomic analysis of memorization in LLMs, breaking it down into three distinct categories: recitation (highly duplicated sequences), reconstruction (inherently predictable sequences), and recollection (neither duplicated nor predictable). Through extensive experimentation with the Pythia models ranging from 70M to 12B parameters, the authors demonstrate that different types of memorization exhibit distinct patterns and dependencies on factors like sequence duplication, model size, and training time. They validate their taxonomy by showing its effectiveness in predicting memorization likelihood and reveal that recollection grows disproportionately with model size and training time. The work provides valuable insights into how different factors influence memorization depending on the taxonomic category.

### Strengths
The paper exhibits several notable strengths that demonstrate its potential value to the field. The proposed taxonomy of memorization provides an intuitive and practical framework for understanding different types of memorization in LLMs. The extensive experimental validation across model scales and training time points offers valuable insights into how memorization behavior evolves. The authors' approach to validating their taxonomy through predictive modeling and dependency analysis shows methodological rigor and provides empirical support for their theoretical framework.

### Weaknesses
1) The template detection approach appears oversimplified. For instance, only basic patterns of "repeating" and "incrementing" sequences are considered, potentially missing more complex templates. The duplication counting relies on exact matches without accounting for semantic similarity or near-duplicates (e.g. slightly modified code or text passages).
2) The paper insufficiently compares its taxonomy against existing memorization frameworks. For example, the relationship between these categories and counterfactual memorization, which is mentioned but not analyzed, deserves exploration. The advantages of this taxonomy over other approaches to studying memorization are not quantitatively demonstrated.
3) The exact procedure for computing KL divergence in Fig 3 is unclear, and the methodology for computing perplexity scores used throughout the analysis lacks essential details. The robustness of results to different tokenization choices is not evaluated.

### Questions
1) Can you provide empirical justification for this specific cutoff? How sensitive are your results to this choice?
2) Could you include statistical significance tests for the reported trends across model sizes?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a taxonomy of memorization in language models, breaking it down into three categories: recitation of highly duplicated sequences, reconstruction of inherently predictable patterns, and recollection of rare sequences. The authors validate their taxonomy through statistical analysis and predictive modeling, showing that different factors influence memorization differently across categories. 

They analyze how memorization patterns evolve with model scale and training time, finding that recollection grows disproportionately with model size. The paper illustrates the practical value of this taxonomy by showing how different categories matter for different applications (privacy, copyright, scientific understanding) and by achieving better predictive performance compared to both a baseline without taxonomy and an optimally partitioned model.

### Strengths
- **The paper provides a methodologically sound approach to developing and validating taxonomies in ML research (and beyond).** By grounding qualitative distinctions in statistical analysis (e.g., following the example of Simpson's paradox), it offers a template for studying complex phenomena in ML beyond memorization that could be of interest for the ICLR community. 
- **The taxonomy enables discoveries about memorization dynamics.** For instance, the finding that duplicate count beyond 5 barely affects recitation likelihood challenges simple assumptions about exposure and memorization. The categorical distinctions also help align research directions with specific applications (e.g., privacy vs. copyright concerns). 
- **Analysis of the semantic properties of the sequence.** This type of statistics provides valuable insights into how models can perfectly reproduce sequences through pattern completion rather than pure memorization for the reconstruction category. This distinction, while simple in hindsight, is important for understanding the relationship between memorization and generalization, and the limit of the k-extractability definition of memorization.

### Weaknesses
- **The predictive model's performance is relatively poor** (precision ~0.5, PR AUC ~0.5), despite including continuation perplexity as an input feature. This raises questions about the practical utility of the identified factors in predicting memorization. The heavy reliance on continuation perplexity for every category (see Figure 5.), which is closely related to the definition of k-extractability, makes it difficult to assess the independent predictive power of other factors. 
- **No clear progress in understanding the memorisation of rare sequence.** While the paper identifies recollection of rare sequences as an important phenomenon, particularly as models scale, it provides limited insight into the underlying mechanisms. This gap is particularly notable given the paper's emphasis on understanding different types of memorization.
- **The presentation lacks clarity at times.** 
	- When introducing the taxonomy, early concrete examples of each category would significantly improve understanding. 
	- The paper should also better highlight the distinction between intuitive notions of memorization and the technical definition of k-extractability used in the study. This could help the reader understand why the reconstruction phenomenon (where sequence outside of the training set could be predicted perfectly) fall in the scope of the study of memorization. 
	- The study could benefit of including reference to a broader set of references such as the study of mechanistic interpretability and training providing more insights on how and when models become able to predict simple sequences. See for instance "In-context Learning and Induction Heads", by Olsson et al.
- **Methodological limitation in the computation of the corpus statistics.** 
	- The corpus statistics are not broken down into prompt/continuation/full sequence. This could enable the isolation of sequences with a frequent prompt but infrequent continuation, or the opposite for instance. The paper doesn't clearly state which one of the three is used for the corpus statistics.
	- If I understood correctly, the semantic similarity measurements are made between sequences of length 64 (or 32) tokens (the memorized/non-memorized samples), and the 2049-token sequences from the Pile. This length mismatch could introduce heavy distortion as even if the small sequence is included in the large sequence, it is not clear that the cosine similarity of their embedding would be similar.

### Questions
1. How would the predictive model perform without continuation perplexity as a feature? This would help assess how much signal the other identified factors provide to predict memorization.
2. How novel is the introduction of statistically validated taxonomy? Do similar case studies exist in other fields? Beyond the reference to the Simpson paradox, the paper doesn't include references in this area.
3. Are corpus statistics computed on the prompt, continuation or the full sequence? 
4. What are the characteristics of sequences with high duplicate counts (>100) that don't get memorized? Understanding these cases might provide insight into factors that inhibit memorization despite repeated exposure.
5. How sensitive are the semantic similarity measurements to the length mismatch between the 64 (or 32)-token samples and the 2049-token sequences they're compared against? 
6. (Less important) Could the sudden increase in reconstruction at 86% of training be related to the "induction bump" phenomenon described in the mechanistic interpretability literature? Again, see "In-context Learning and Induction Heads", by Olsson et al. for the introduction of the concept.


Minor points:

The Figure 6 would benefit from being vertically compressed without deforming the text.

Likely typo lines 140-142: "we generate document embeddings for each full sequence using SBERT and count the number of sequences with cosine similarity ≤ 0.8. These sequences are semantically similar but may not be exact token-level duplicates." -> I guess it should be "cosine similarity ≥ 0.8" instead.

### Soundness
3

### Presentation
2

### Contribution
3
