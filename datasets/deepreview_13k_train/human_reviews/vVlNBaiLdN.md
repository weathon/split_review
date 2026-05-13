# ESMGain: Effective and Efficient Prediction of Mutation’s functional Effect via ESM2 Transfer Learning and robust Benchmarks

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Functional effect prediction of mutations, especially for properties like catalytic activity, holds greater significance for clinicians and protein engineers than traditional pathogenicity predictions. Recent approaches leveraging static ESM1 embeddings or multimodal features (e.g. embeddings, structures, and evolutionary data) either (1) fall short in accuracy or (2) involve complex preprocessing pipelines. Moreover, functional effect prediction suffers from (3) a lack of standardized datasets and metrics for robust benchmarking. We address these challenges by systematically optimizing ESM2-based functional effect prediction: Through extensive ablation studies, we demonstrate that fine-tuning significantly outperforms static embeddings, scaling laws for model size are non-transferable and LoRA matches full fine-tuning performance, deviating from trends observed in natural language processing. Our framework, ESM-Effect, fine-tunes 35M ESM2 layers with an inductive bias regression head achieving state-of-the-art performance. It slightly surpasses multimodal competitor PreMode indicating redundancy in structural and evolutionary features. We further propose a benchmarking framework featuring robst test datasets and strategies, and the relative Bin-Mean Error (rBME), as a metric designed to emphasize prediction accuracy in challenging, non-clustered, and rare gain-of-function regions. rBME better reflects model performance compared to commonly used Spearman’s rho, as evidenced by improved plot-based analyses. As ESM-Effect exhibits mixed transferability to different unseen mutational regions, we identify multiple areas for improvement such as finer-grained pretraining strategies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a method for fine-tuning protein language models, specifically ESM2, using deep mutational scanning (DMS) data. The fine-tuning process involves generating both local and global representations of the reference and mutant protein sequences by utilizing separate, mostly frozen ESM models for the two sequences. These representations are combined and passed through a two-layer linear neural network to predict quantitative measurements from a DMS assay.

Further, the authors propose two modifications to the evaluation of fine-tuned models. First, they recommend fine-tuning models on one protein and testing them on a different protein within the same family, rather than using held-out positions from the original protein. Second, they suggest calculating correlation metrics separately for LoF, neutral, and GoF mutations. These separate correlation scores are then combined using a harmonic mean to produce a single protein-level metric.

### Strengths
1. The authors introduce important ideas for better evaluating fine-tuned models: (a) evaluating models on completely held out proteins and (b) developing a metric that prioritizes performance on LoF and GoF variants over neutral variants.
2. Their fine-tuning approach demonstrates superior performance compared to existing methods, such as PreMode and augmented versions of unsupervised models.
3. Through ablation studies, the authors establish that using larger versions of ESM2 does not significantly improve performance and that employing separate models for reference and mutant sequences provides some benefits.

### Weaknesses
1. Limited dataset evaluation: The authors do not evaluate their method on the large compendium of DMS datasets that are available in ProteinGym (217 datasets covering 2.5 million mutations), instead focusing on only 5 datasets (Figure 2). To convincingly prove that their fine-tuning approach outperforms existing methods, they should expand their analysis to more datasets. The selection of only 5 datasets raises concerns about the generalizability of the findings and whether the observed performance gains are consistent across diverse protein families and experimental conditions. It is crucial to demonstrate the robustness of the method on a broader range of DMS data.

2. Insufficient comparison to existing fine-tuning approaches: PreMode and augmented unsupervised models are not the only approaches that have been proposed to fine-tune protein language models on DMS datasets. See https://www.nature.com/articles/s41467-024-51844-2 and https://arxiv.org/pdf/2405.06729. These papers explore strategies such as parameter-efficient fine-tuning and fine-tuning jointly on multiple DMS assays that this paper does not consider. In particular, the approach proposed in the second paper listed above shows improved performance on entirely held out proteins, which is in stark contrast to the poor generalization to new proteins exhibited by ESMGain in Fig. 4. The lack of comparison to these methods leaves a gap in demonstrating the novelty and superiority of the proposed approach. Specifically, the parameter-efficient fine-tuning methods could be more computationally feasible for large-scale application.

3. While the idea to compute separate correlation metrics for LoF, neutral, and GoF variants is clever, the method of dividing variants into these categories by splitting the ground-truth scores into thirds is arbitrary. A more robust method, such as a Gaussian mixture model with three components, could provide a more principled assignment of variants to these classes. The current approach may lead to inconsistent categorization of variants, especially if the distribution of DMS scores is not uniform or if the number of variants in each category is not balanced. This could bias the evaluation metric and misrepresent the true performance of the model.

### Questions
1. The poor generalization performance in Fig 4 to new proteins seems to indicate that ESMGain is overfitting. Can you more heavily regularize your model to avoid this?
2. Do you find that performance depends on what fraction of ESM2 is frozen? What happens if it is entirely frozen and you only train a 2-layer NN on top of the reference/mutant representations?
3. Does the harmonic Spearman correlation provide a more meaningful ranking than say AUROC at distinguishing the bottom third from the top third of variants?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposed a method called ESMGain to use fine-tuning ESM2 with a custom regression head incorporating inductive biases and enable the application of learned protein semantics to functional effect prediction. This method outperforms state-of-the-art competitor PreMode on deep mutational scans from three different enzymes.

### Strengths
1. The proposed method performs the best for functional effect prediction in the dataset.
2. The methodology of ESMGain can predict functional effects without the limitation of feature redundancy and task specificity.

### Weaknesses
1. The organization needs improvement. Some terms like "PTEN" didn't have full names. The size of font in those figures is too small to read and is not consistent. The section 7 should be in the section of the experiential setup.
2. In Fig4, "LoF, Neutral and GoF" in captions should be the same as the text in x axis of figure. How about the performance in all other baselines like competitor PreMode in Fig4?
3. Have you conducted multiple train-test split seeds in ablation study of ESMGain? Why the result of the original ESMGain in the ablation study is different from the one in Fig2? Do they use different datasets or strategies to train and test?

### Questions
see above. The questions are about the description of the result and additional result in other baselines.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a novel model method  ESMGain for predicting the functional impact of protein mutations, expanding addressing limitations in existing binary pathogenicity predictors. By fine-tuning ESM2 embeddings with a custom regression head, ESMGain aims to accurately classify mutations as loss-of-function, neutral, or gain-of-function. Through evaluations  in catalytic activity prediction tasks, ESMGain outperforms the state-of-the-art baselines by leveraging only ESM2 embeddings. Besides, the authors propose a new benchmarking framework for functional effect prediction, emphasizing cross-protein generalization tests within the same protein family. A Harmonic Spearman metric is also introduced to balance performance evaluation across mutation effect categories.

### Strengths
1) The paper is well-structured and clearly written.

2) The proposed method achieves state-of-the-art performance on selected datasets in functional effect prediction.

3) By employing two independent ESM2 models to embed wildtype and mutant sequences separately, the paper addresses potential information loss in mutation representation, enhancing the model’s ability to capture subtle differences. Ablation studies demonstrate that only using ESM2 embeddings effectively captures most of the relevant information on DMS datasets,  effectively reducing the reliance on additional data modalities.

4) The paper proposes a novel benchmarking framework for functional effect prediction incorporates a cross-protein generalization test within the same protein family.

### Weaknesses
1) The novelty of this paper is limited. The use of dual ESM2 embeddings to separately represent wildtype and mutant sequences, along with the introduction of the Harmonic Spearman metric to address label imbalance, appears more incremental than groundbreaking. The core idea of using separate embeddings for wildtype and mutant sequences, while potentially beneficial, is not a fundamentally new concept in sequence modeling. Furthermore, while the Harmonic Spearman metric is useful for imbalanced datasets, it is not a novel statistical method, and its application here feels like a minor methodological adjustment rather than a significant contribution.

2) It seems that the motivation of the proposed benchmarking framework is underdeveloped. While focusing on cross-protein generalization within the same family is technically interesting, it lacks a clear connection to real-world situations where this type of evaluation would be essential. The paper does not adequately justify why cross-protein generalization within a family is a crucial benchmark for practical applications. It is not clear if this type of generalization is more relevant than, for example, generalization to different experimental conditions or different types of mutations. The lack of a clear rationale diminishes the impact of this proposed benchmark.

3) While ESMGain performs well on the tested DMS data, its generalization to other samples within the same protein family is weak (cross-family tests). The model may be overfitting in the specific training proteins. The reported weak cross-family generalization suggests that the model may be learning protein-specific features rather than generalizable principles of mutation effects. This raises concerns about the model's practical utility beyond the specific proteins used in training. The lack of robustness across different proteins within the same family is a significant limitation.

### Questions
1) The paper includes relatively few citations and offers limited analysis of related work. Could the authors clarify if this indicates that the approach is less informed by recent research developments?

2) Additional questions are noted in the "Weaknesses" section.

### Soundness
2

### Presentation
2

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
The paper introduces a method for mutation effect prediction. The method relies on two ESM2 heads for generating protein sequence embeddings, one used with wildtype sequences and the other one for the mutated sequences. On top of the embeddings a custom regression head is trained. The technical novelty of the method is their design of the regression head and the fact that the two ESM2 models have different weights one fine-tuned for wildtype sequences and the other for the mutated sequences. Other contributions claimed by the paper are towards better bencharking (i) testing generalization of the models fine-tuned on one protein by testing them on a different protein from the same family and (ii) introduction of “Harmonic Spearman” as a new metric.

### Strengths
1. The generalization test is of interest. In Figure 3, authors show the different distribution of labels for two different proteins from the same family and convincingly show why generalization between proteins (even in the same family) is not easy.

### Weaknesses
1. Paper is poorly structured, making it very hard to read:

	- Introduction contains contents which would better fit to related work or background (“Notably, PreMode was pre-trained to predict the binary measurement of “pathogenicity” for 4.7 million mutations and uses AlphaFold2 predicted protein structure, Multiple Sequence Alignments (MSAs) and pre-trained ESM2 650M embeddings as features (John Jumper, 2021).”) And it also presents some results and their discussion (“That leads us to hypothesize that the signal provided by protein structure, MSAs, and embeddings is largely redundant for the task of effect prediction. PreMode’s ablation studies show minimal performance drop when any of these modalities is ex- cluded, suggesting that they capture overlapping information for functional effect prediction. This explains ESMGain’s superior performance in turn: its fine-tuned embeddings are task-specific and the single modality avoids the redundancy.”). I suggest honoring the usual structure of the paper and using introduction just for motivation and a very brief (not so detailed) teaser for the contributions of the paper.

    - Chapter 4, which should be describing the technical novelty and the method does not provide that many details, for example Figure 1 illustrating the method is never referenced in the text. I suggest to use a figure and equations to better describe the regression head, instead of the textual description at the end of section 4.2.

    - No table summarizing results. The reported numbers are scattered across text and some figures, making it very hard to get a glimpse of the results. I suggest a more transparent summarization of the results, such as by using a table.

2. Poor formatting of the paper.

    - Authors are not economical with the space by being sometimes too verbose, repetitive in repeating their contributions or for example by wasting the whole first page just on abstract. Being more economical would enable the authors to make bigger figures which have too small fonts and are hard to read. I suggest making figure large enough so the fonts can be legible.

    - References are poorly formated. Some references starting with “…” . AlphaFold referenced as “(John Jumper, 2021)” - note that AlphaFold was a collective effort. I suggest proper citing and formatting of references.

3. Insufficient literature survey. Authors only have 13 references. I suspect authors were trying to fit into the page limit of 10 pages including references - this is not necessary references dont count in the page limit. I suggest making proper literature survey and crediting relevant work. For example, I miss the reference to ProteinGym, arguably one of the most influential benchmarks in this area.

4. Insufficient benchmarking. Authors only focus on the comparison to PreMode (which was still not peer reviewed) and only compare on 5 proteins. I suggest to compare for example to AlphaMissense as well.

5. The key contribution of having separate ESM2 heads for wildtype and for the mutated sequence is questionable. Authors claim this to give them the key improvement by the underlying inductive bias. To me it is not clear how to decide what is wildtype and what is mutation. What if the mutation is adopted by evolution and becomes the “new wildtype” and then gets mutated again? There is no fundamental reason to distinguish between the sequences. So I believe that using the distinction between the sequences based on the dataset definition and then adapting the two heads to this definition only leads to overfitting to the dataset, potentially explaining any benefit gained from these separate heads. I dont have a concrete suggestion how to prove authors point, because I think the point is wrong. If authors stand by their point they should present convincing evidence supporting that their “inductive bias” is not just overfitting to the dataset definition of what is wildtype and what is mutation.

6. The model seems to improve over PreMod on just 2-3 out of 5 proteins (Figure 2), this does not seem very convincing. My suggestion would be to get other datasets (maybe something relevant could be found in ProteinGym) and show improvement on other dataset as well.

7. The Harmonic Spearman is just introduced at the end of the paper and not motivated well enough. Could authors explain the choice of using harmonic average? Could authors clearly compare harmonic spearman to normal spearman? How does it change the evaluation of all the benchmarked models? A table summarizing the results (as suggested in Weak point 1) would help.


I suggest to reject this paper for the following reasons. (i) The paper is not is well placed in literature, comparison to AlphaMissense is missing and the survey of the related work is not sufficient. (ii) The key contribution of using two separate ESM2 models for the wildtype and the mutated sequence is questionable and the claim of bringing a useful inductive bias is not supported by strong evidence, the improvement coming from this choice might be due to overfitting to the dataset definition of what is mutant and what is original sequence. (iii) The results dont seem as strong, only showing improvement for 2-3 out of 5 proteins. More convincing evaluation using other dataset would be necessary. (iv) The technical novelty of separate fine-tuning of two ESM models with a custom regression head is limited. (v) The writing is poor, making it hard for the reader to asses the contributions, the results of the method and its placement in the literature.

### Questions
Most of my questions and suggestions for the authors are listed alongside the weaknesses in the above section. 

To sum up: 

- I suggest to find more datasets of other proteins from ProteinGym and use them to compare ESMGain at least with PreMode and AlphaMissense.

- Present clearly the results in a table using both the Spearman correlation and the proposed Harmonic Spearman at one place.

- Authors should provide evidence for bringing a new useful inductive bias by taking the two separately fine-tuned ESM2 heads. Other evidence than the improved performance (for some proteins), which might just hint at overfitting to the dataset definition.

- The paper should be rewritten focusing on clear presentation of the method and results, clear structure of the paper and proper formatting of figures and references. The method (in particular the new regression head) is not clearly presented, the structure is chaotic with discussion of results and related work appearing already in introduction. The figures have tiny fonts making them hard to read and the references are wrongly formatted.

### Soundness
2

### Presentation
1

### Contribution
2
