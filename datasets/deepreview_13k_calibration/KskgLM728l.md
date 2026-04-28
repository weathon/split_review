# Bio-RFX: Refining Biomedical Extraction via Advanced Relation Classification and Structural Constraints

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
The ever-growing biomedical publications magnify the challenge of extracting structured data from unstructured texts. This task involves two components: biomedical entity identification (Named Entity Recognition) and their interrelation determination (Relation Extraction). However, pre-existing methods often neglect unique features of the biomedical literature, such as ambiguous entities, nested proper nouns, and overlapping relation triplets, and underutilize prior knowledge, leading to an intolerable performance decline in the biomedical domain, especially with limited annotated training data. In this paper, we propose the **Bio**medical **R**elation-**F**irst E**X**traction (Bio-RFX) model by leveraging sentence-level relation classification before entity extraction to tackle entity ambiguity. Moreover, we exploit structural constraints between entities and relations to guide the model's hypothesis space, enhancing extraction performance across different training scenarios. Comprehensive experiments on multiple biomedical datasets show that Bio-RFX achieves significant improvements on both named entity recognition and relation extraction tasks, especially under low-resource training scenarios, achieving a remarkable **5.13%** absolute improvement on average in NER, and **7.20%** absolute improvement on average in RE compared to baselines. The source code and pertinent documentation are readily accessible on established open-source repositories.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tackles the issue of Named Entity Recognition and Biomedical Relation Extraction. In particular, it proposes a framework that starts with identifying relations first, and using that information to constrain the space for entity extraction. The paper shows that the method surpasses SOA for NER and RE tasks on multiple biomedical datasets, on a variety of scenarios, including low-resource.

### Strengths
- **Quality**: Approach is grounded in biological knowledge of constraining the space for entity extractions to types of relationship
- **Originality**: The paper combines various ML concepts in an interesting and creative way
- **Results**: Results show improvement over other SOA models

### Weaknesses
The concepts introduced in the paper are not novel. However, the paper does a nice job at putting them in a creative way to obtain improvements over SOA.

### Questions
- Looking at the results in Table 1: What is the hypothesis for KECI performing better on RE task in DrugProt?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduced a novel biomedical entity and relation extraction method that deploys structural constraints for relation triplets to constrain the hypothesis space. It reported on extensive evaluations on three datasets and in a case study to provide convincing evidence of performance gains obtained using the introduced method. It supplemented these performance evaluations by conduction an ablation study as well.

### Strengths
The paper introduced a novel biomedical entity and relation extraction method that deploys structural constraints for relation triplets to constrain the hypothesis space. Biomedical applications of this kind are of substantial societal importance.

It reported on extensive evaluations on three datasets and in a case study to provide convincing evidence of performance gains obtained using the introduced method. It supplemented these performance evaluations by conduction an ablation study as well.

The paper was very carefully written. It was clear and convincing.

### Weaknesses
I was unable to find information about statistical analysis (e.g., statistical significance tests or confidence intervals).

Automatic entity and relation extraction is a trending topic in research on natural language processing, knowledge graphs, and machine/deep learning. Hence, a more convincing case for novel contributions made in this paper could be made. For example, I could not find a single paper on contrastive representation learning included in the paper, although, e.g., triplet loss and contrastive representation learning are very closely related (see, e.g., Le-Khac, P. H., Healy, G., & Smeaton, A. F. (2020). Contrastive representation learning: A framework and review. IEEE Access, 8, 193907-193934).

Reference list of the paper could be perfected and math should be punctuated.

### Questions
How were the performance gained evaluated as significant? Were they both statistically and practically significant?

What made the contributions made new/novel compared to prior work?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of information extraction (named entity recognition and relation extraction) in the biomedical domain.
The authors propose to predict the relation type in the sentence and then extract the relevant entities in a question-answering manner. Finally, the pruning algorithm is used with an entity number predictor to filter the final predicted entities.
The proposed method is evaluated on three biomedical datasets: Bacteria Biotope, DrugProt, and DrugVar, and results show that the proposed method outperforms several baselines, especially under the low-resource scenario.

### Strengths
* The authors propose an interesting paradigm for relation extraction: predict relation first and then extract entities; extract entities in a QA manner.
* The authors report strong results of the proposed method on several biomedical datasets.

### Weaknesses
 * The choice of baselines seems arbitrary; I suggest linking Section 2.1 and Section 4.2.1 to make the reason for ‘why cannot use relation-first baseline’ more explicit.
* It isn't easy to gain insights into the main strengths of the proposed method. See question A

### Questions
Question A: it is unclear what the ablated variant ‘- structure’ is. Suggest linking Section 4.5 and the four components in Section 3. For example, the ‘- Number’ variant contains only component 1, 2, 4? and, it would be nice to see a variant containing only the first two components

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel method for entity relation extraction from text, where relation types are detected first, and then entities (or arguments) are detected later. For entities, the entity candidates and their number for each relation type are detected using two types of question-answering framework, and the entities are extracted by filtering the entity candidates considering the number of entities. The approach shows the best performance among compared methods for the named entity recognition and relation extraction tasks on three biomedical data sets in the full data and low resource settings, except for relation extraction on one data set in the full data set setting. Ablation studies show the usefulness of the structure constraints and number prediction.

### Strengths
- The approach to first detect relation types and then entities is novel
- The paper is well-written and easy to follow. Figure 2 is helpful to grasp the overall framework.
- The results on three datasets show high performance in both full data and low resource settings, and the ablation study shows the usefulness of the proposed enhancements.

### Weaknesses
 - The approach could be generally applied to other domains, but the approach is presented as a model for the biomedical domain, and the scope is limited. 
- The comparison with existing state-of-the-art entity relation models is limited. The authors presented several approaches like OneRel and SPN in the related work section, and there are several SOTA models for entity relation tasks as follows, but the comparison is not performed.
  - Pere-Lluís Huguet Cabot and Roberto Navigli. 2021. REBEL: Relation Extraction By End-to-end Language generation. In Findings of the Association for Computational Linguistics: EMNLP 2021, pages 2370–2381, Punta Cana, Dominican Republic. Association for Computational Linguistics.
  - Chenguang Wang, Xiao Liu, Zui Chen, Haoyun Hong, Jie Tang, and Dawn Song. 2022. DeepStruct: Pretraining of Language Models for Structure Prediction. In Findings of the Association for Computational Linguistics: ACL 2022, pages 803–823, Dublin, Ireland. Association for Computational Linguistics.
  - Deming Ye, Yankai Lin, Peng Li, and Maosong Sun. 2022. Packed Levitated Marker for Entity and Relation Extraction. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 4904–4917, Dublin, Ireland. Association for Computational Linguistics.

### Questions
- Please see the weaknesses above. 
- How is the model specific to the biomedical domain? 
- Appendix A shows several comparisons of prompting using domain resources, but the prompts used in practice are not clear. For the activator relation type, the authors use the prompt including activate (not activator), so is question generation done manually? They also say, "Note that it is a relatively simple approach" in explaining questions, but do they use any other complicated approach in practice? Or is this simple approach the best?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
