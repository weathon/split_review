# BSM: Small but Powerful Biological Sequence Model for Genes and Proteins

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 1, 5

## Abstract
Modeling biological sequences such as DNA, RNA, and proteins is crucial for understanding complex processes like gene regulation and protein synthesis. However, most current models either focus on a single type or treat multiple types of data separately, limiting their ability to capture cross-modal relationships. We propose that by learning the relationships between these modalities, the model can enhance its understanding of each type. To address this, we introduce BSM, a small but powerful mixed-modal biological sequence foundation model, trained on three types of data: RefSeq, Gene Related Sequences, and interleaved biological sequences from the web. These datasets capture the genetic flow, gene-protein relationships, and the natural co-occurrence of diverse biological data, respectively. By training on mixed-modal data, BSM significantly enhances learning efficiency and cross-modal representation, outperforming models trained solely on unimodal data. With only 110M parameters, BSM achieves performance comparable to much larger models across both single-modal and mixed-modal tasks, and uniquely demonstrates in-context learning capability for mixed-modal tasks, which is absent in existing models. Further scaling to 270M parameters demonstrates even greater performance gains, highlighting the potential of BSM as a significant advancement in multimodal biological sequence modeling.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors of this work present BSM, small biological sequence models that ostensibly achieve competitive performance with existing larger models through the virtue of combining: 
1. Multiple types of data modalities (e.g DNA, RNA, and Protein sequences)
2. "Curating" the data used resulting in a smaller but higher quality dataset.

By being careful about the types and mixes of data used for pre-training, the authors are able to achieve performance competitive with much larger (e.g. 10x) larger models.

### Strengths
I like the general concept, there are myriad types of data that can be used for biological sequence modeling, and I'd like to believe that being smart about data/modality selection can lead to increased performance with fewer parameters/FLOPs by leveraging multiple types of information at once.

### Weaknesses
1. It is not clear what the exact effect of each phase (data mix) is.
    2. The BSM model is split up into three phases:
        3. Phase 1 trained on 100B single modal tokens (e.g each sequence is only nucleic acids or only protein sequences).
        4. Phase 2 is further trained on 146B tokens for 246B tokens seen in total
        5. Phase 3 is then further trained on $\sim$ 16.9B more tokens for 262.2B tokens seen in total.
    3. It is unclear to this reviewer what perfromance gains are due to the increased token budget vs from the different types of data included. For example, in Table 4, the authors attempt to show that increasing rounds (and therefore increasing token budgets) lead to a increase in downstream performance, but it's unclear if this gain is from the additional tokens or from the curration of the tokens. At the very least, a control where a BSM model is trained for the same number of tokens, but only with the tokens from phase 1 for example may help show that the performance increase is due to the incorporation of different types of data and not just due to training for longer. 
    4. The authors kind of show something like this in Figure 1, but it's unclear to me exactly what the validation set is (is it data from that phase? Some fixed set of data sampling from phase 3? I don't think I ever found a detailed description in the paper) so I'm not sure if the authors are showing that incoporating the other phase data actually makes the loss decrease faster or if they're showing some sort of domain shift (e.g. if val is from phase 3 but they keep training on phase 2, we might expect the validation loss to not decrease as fast). Figure 6 suffers from a similar issue where I'm unsure of what the validation data and so I'm unsure how to interpret the changes in loss per phase. 
    5. Taken together, all of these concerns lead me to doubt what the effect of the different data mixes actually is, which seems to be a key claim of the paper.  
2. The Authors do not compare to the smaller models (e.g. the small ESM models) where applicable. ESM has available 650M, 150M, and even smaller models. On all the protein tasks, the authors only report ESM-3B, except for zs-Protein Fitness Prediction where they use ESM-650M. Unless I'm missing something, reporting their 110M and 270M compared to ESM-150M would help showcase how ther training setup and architecture compares to a model similar in size. Note: going down to ESM-650M only for that one task is odd, was this a placeholder or something and 3B was to be shown in the final submission or was there some other reason for only showing 650M?
3. There is some details missing on the setup of all the models evalauted. What sequence lengths are used, for models that are truncated (e.g. max of 1024 tokens), how are long sequences processed? What was the fine-tuning procedure for each of the models? How much does this type of processing affect different model performance? Architectural choices like these likely have some effect on the performance of each model observed, but it's currently unclear how much these types of decisions contributed to the observed performance and so it's difficult to disambiguate what the true effect of the data selection is. 
4. More details are needed for each evaluation task. Appendix C and Table 4 are a good start, but there's details such as the number of instances of each class, the species the task was taken from, etc. Most of the tasks only report accuracy or SRCC, but it's unclear if this is an adequate summary statistic for each task given this missing information.


### Questions
Could the species you used for training also have an effect on downstream performance. Existing models usually train on human+mammal data, occasionally also incorporating data from invertebrates, bacteria, fungi, etc. I think the BSM models were trained on a mix of mammal and fungal DNA from RefSeq, was there any logic to the species selected? Is it possible that any differences in performance are (at least partly) due to the species selected? This may be a useful thing to point out for curation (i.e. we get better perf because we picked better species), but currently I can't actually tell what the affect of adding in each specie is nor how much each specie is represetned in the training data.  NOTE:  the assembly accession information for each specie accessed is missing from the paper, please make sure this is available somewhere since these assemblies tend to be updated periodically by NCBI. 

How exactly were data leaks prevented? I understand that data from the downstream tasks was removed from pre-training but how exactly was this done and how are you sure that no leakage occurred by e.g. a very similar sequence, or having a gene whose transcribed protein is in the test set?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper presents BSM, a compact mixed-modal biological sequence foundation model, trained using three types of data: RefSeq, Gene Related Sequences, and interleaved biological sequences from the web. The model's performance is assessed by comparing it to other existing larger models (e.g., LucaOne, ESM2, Evo, etc.) across various downstream tasks.

### Strengths
A compact mixed-modal biological sequence foundation model is introduced and assessed across various downstream tasks.

### Weaknesses
The clarity and precision of the paper could be greatly enhanced by making it more concise. For example:

•	The paper contains numerous repetitive phrases, sentences, and references that could be removed to improve readability.

•	Data and experimental details would be better summarized in tables for clarity and ease of comparison.

•	Section 4 is largely redundant.

•	Many figures are of poor quality, with barely readable legends.

Drawing conclusions from the experiments presented in the paper is challenging due to the lack of important details, including:

•	There are no details about the head used in the experiments in conjunction with the foundation models (FMs). These details are crucial and need to be carefully set for a head-to-head comparison with other FMs.

•	Additionally, for other FMs, there could be inverse scaling, where larger models do not consistently outperform smaller ones on all tasks (see McKenzie, et al. (2023). Inverse scaling: When bigger isn’t better. arXiv preprint arXiv:2306.09479). Therefore, it is difficult to conclude that the proposed BSM model performs the best, despite being the smallest, solely due to the introduction of additional data for training.

•	The differences in performance across models are mostly subtle in many experiments. Statistical analysis would be helpful here.

### Questions
See Weakness

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to model the multiple biological sequences (DNA, RNA, and Protein) into a single model for cross-modal and uni-modal biological sequence tasks.
Authors propose to utilize small language model for the task, which outperforming larger models in various tasks.

### Strengths
- Modeling biological sequence and integrating heterogeneous types of sequences are important in building foundational model for biological sequences.
- Extensive experiments are conducted to demonstrate the superiority of BSM

### Weaknesses
 - The main motivation of this paper is to use the small language model (SLM) for biological sequences. But why do we need SLM for biological sequence analysis? SLM is usually practical in real-life for implementing language model for on device or resource limited settings. However, in biological sequence analysis, scientists may already have intensive computational resources. It would be great if the authors can justify why we need SLM for biological sequence analysis.
- It may be convincing, if the SLM performs better than larger model due to the limited availability of data. However, as shown in various experiments, larger models perform better than smaller models. For example, Figure 3 (b) LucaOne performs better than BSM models, and BSM-270M model performs better than BSM-110M model.
- Experimental results
    - I think we need more ablation studies on multi modal data to further demonstrate the necessity of multi-modal pre-training approach.

### Questions
- How do you choose the data mixing ratio? Is it heuristically decided? How the model performance varies as mixing ratio changes?

### Soundness
2

### Presentation
3

### Contribution
2
