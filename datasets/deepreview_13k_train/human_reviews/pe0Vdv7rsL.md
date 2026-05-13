# Graph Transformers on EHRs: Better Representation Improves Downstream Performance

- Decision: Accept
- Scores: 6, 5, 8, 5

## Abstract
Following the success of transformer-based methods across various machine learning applications, their adoption for healthcare predictive tasks using electronic health records (EHRs)  has also expanded extensively. Similarly, graph-based methods have been shown to be very effective in capturing inherent graph-type relationships in EHRs, leading to improved downstream performance. Although integrating these two families of approaches seems like a natural next step, in practice, creating such a design is challenging and has not been done. This is partly due to known EHR problems, such as high sparsity, making extracting meaningful temporal representations of medical visits challenging. In this study, we propose GT-BEHRT, a new approach that leverages temporal visit embeddings extracted from a graph transformer and uses a BERT-based model to obtain more robust patient representations, especially on longer EHR sequences. The graph-based approach allows GT-BEHRT to implicitly capture the intrinsic graphical relationships between medical observations, while the BERT model extracts the temporal relationships between visits, loosely mimicking the clinicians' decision-making process. As part of our method, we also present a two-step pre-training strategy for learning better graphical and temporal representations. Our proposed method achieves state-of-the-art performance in a variety of standard medical predictive tasks, demonstrating the versatility of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents GT-BEHRT, an innovative approach that integrates graph-based and transformer-based methodologies to enhance the analysis and predictive accuracy of electronic health records (EHRs). The technique specifically addresses the sparsity in EHR data and the need for capturing complex, graph-type relationships. GT-BEHRT combines graph transformer-derived embeddings for individual visits with a BERT-based framework, facilitating richer patient representations over extended EHR sequences. This method also features a novel two-step pre-training process that further refines the model’s capacity to decode both graphical and temporal patterns in the data. As a result, GT-BEHRT achieves leading performance across diverse medical predictive tasks, indicating its robustness and versatility.

Main Contributions:

GT-BEHRT Design: A new hybrid model that integrates graph transformer and BERT-based architectures to better handle the temporal and graphical nature of EHR data.

Two-Step Pre-training Strategy: A unique pre-training process that enhances the model's ability to understand complex relationships in EHRs, improving performance on predictive tasks.

Superior Predictive Performance: Through its innovative approach, GT-BEHRT sets a new benchmark for state-of-the-art results in various standard medical predictive tasks, demonstrating its potential to significantly impact healthcare analytics.

### Strengths
The authors present a commendable effort in intertwining GNN and Transformer methodologies, showcasing an innovative approach to a topic gaining traction in the field. Their literature review is generally thorough, but it's surprising to note the omission of recent contributions from Jure Leskovec's lab, which bear resemblance to this work. While the essence of the paper is intriguing, a deeper exploration of their model's specifics would have provided more comprehensive insights. Overall, the strength of this paper lies in its novel perspective on a burgeoning issue, even if there are areas left to be further elaborated.

### Weaknesses
The paper, while advancing an intriguing new architecture, does not fully address the breadth of state-of-the-art works within the Graph Neural Network (GNN) sphere. A more exhaustive acknowledgment and discussion of leading GNN research would have provided a richer context for the authors' contributions. Additionally, while the authors assert that their proposed architecture outperforms existing models, the paper falls short in offering visual depictions of the architecture. Such illustrations are crucial for readers to fully grasp the design and the innovations it purports to bring. Furthermore, the rationale behind the selection of certain models as baselines is not sufficiently elucidated. This lack of detailed justification and visual support may leave the reader questioning the thoroughness of the comparative analysis and the foundation of the authors' claims. The paper would benefit from more comprehensive visual materials and a deeper discussion on model selection to solidify its standing within the current scientific discourse.

### Questions
Why did you only used one dataset to test you model?
Have you looked at Michele Moore works?
Why you didn't compare your results with some of the state of the art works such as GMAI?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focused on patient representations and developed a tailor transformer architecture leveraging both graph transformer and BERT-like encoder only transformer. Evaluation on MIMIC-III and eICU showed improved performance on two tasks, mortality and length of stay.

### Strengths
The paper is well written and the developed method is easy to follow.

The architecture sounds reasonable to me.

### Weaknesses
Baselines are quite old. The most recent baseline is 2021. More literature research is necessary. For example,  [1,2,3] have dome similar things. Consequently, I am not convinced by the advantage of bringing GNN into BERT,



### Questions
What do authors would like to convey in the title "BETTER REPRESENTATION IMPROVES DOWNSTREAM PERFORMANCE"
What's the definition of better and how to obtain it?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors presented an approach towards extending graphical neural networks to temporal domain using transformers for modeling EHRs. Past research has shown the importance of modeling EHR modalities as GNN that can better capture the inherent correlation better than a flat data structure. However, nuance of EHR data, especially around longitudinal aspects, makes it important to also capture the temporal dynamics. The authors compared their proposed method with several baselines and reported strong results.

### Strengths
Some of the key strengths of the paper are as below
- the authors have proposed a hybrid architecture combing GNN and transformer architectures to capture both the spatial and temporal dynamics of EHR data. Key contributions around this proposed architecture are around identifying some of the issues for extending GNN to temporal domain and propose a multi stage pre-training method to capture the dynamics accurately
- The authors compared their methods against strong baselines and reported significant performance improvements
- they key insights around the model being able to capture longer medical histories is very interesting and adds makes the model more applicable
- The authors have also added ablation studies to capture the importance of their training strategy

### Weaknesses
The paper can be improved upon by addressing the following aspects
 - The method description can be improved upon. Consider adding an illustration of the training strategy and describing the methods using the illustrations
- the authors can also consider adding sub-group analysis to further strengthen the claims around model performance
- While being cognizant of the page limits, it would have been interesting to analyze some of the inferred graphical networks at individual example level

### Questions
See above

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a BERT-based model to represent EHR with a graph-based time-aware visit embedding to better capture the implicit graphical structure of EHR data and the temporal relationships between visits. The paper shows better performances in multiple tasks on the MIMIC-IV dataset.

### Strengths
- The paper demonstrates the importance of temporal effects in the EHR. This is insightful for research on EHR.

- Comprehensive studies are conducted including various tasks and ablation settings. The confidence intervals are provided.

### Weaknesses
 - The proposed method is a combination of building blocks originated from several previous papers, e.g. graph transformer, BEHRT. It is a good application paper that utilizes all these aspects, but the methodological impact is limited.

- In the ablation study section, the author claims that "both pre-training strategies seem to have a great impact on the overall results, as showcased by the second, fourth, and fifth rows.". However, in fact, Table 3 shows the performance differences between experiments with and without NAM, MNP, and GT are marginal. The confidence interval of the last row and the first row (the simplest version) even overlap. The simple linear model seems to already perform very well compared to GT. A better way of justifying the impact of pretraining can be directly using linear probing on the frozen pre-trained representation.

- The power of pretraining seems to be limited by the size of the dataset (around 20K patients). Under this condition, pretraining a large model may not significantly outperform a simple linear model. It will be more exciting to apply the proposed method to a larger dataset.

### Questions
- How is the F1 score calculated? Which threshold is picked? Some experiments with similar AUPRC result in substantially different F1 scores.

- What is the difference between NAM and MNP? It seems they can be merged into one loss.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
