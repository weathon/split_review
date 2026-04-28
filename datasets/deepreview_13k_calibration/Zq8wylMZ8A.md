# Interpretable Language Modeling via Induction-head Ngram Models

- Decision: Reject
- Avg Score: 6.75
- Scores: 8, 6, 5, 8

## Abstract
Recent large language models (LLMs) have excelled across a wide range of tasks, but their use in high-stakes and compute-limited settings has intensified the demand for interpretability and efficiency. We address this need by proposing \methodlong{} (\method{}), a method that builds an efficient, interpretable LM by bolstering modern ngram models with a hand-engineered ``induction head''. This induction head uses a custom neural similarity metric to efficiently search the model's input context for potential next-word completions. This process enables \method{} to provide ngram-level grounding for each generated token. Moreover, experiments show that this simple method significantly improves next-word prediction over baseline interpretable models (up to $26\%p$) and can be used to speed up LLM inference for large models through speculative decoding. We further study \method{} in a natural-language neuroscience setting, where the goal is to predict the next fMRI response in a sequence. It again provides a significant improvement over interpretable models ($20\%$ relative increase in the correlation of predicted fMRI responses), potentially enabling deeper scientific investigation of language selectivity in the brain.
\blfootnote{$^\ast$ Equal contribution. ~ $^\dag$ Corresponding authors.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper improves on LLM interpretability by integrating a specially designed 'induction head' with state-of-the-art n-gram models. Beyond interpretability, authors present overall improvement in next-word prediction over baseline interpretable models.

### Strengths
* Completeness in presentation and experimentation
* Effective interpretable model with improvements in next word prediction and efficiency

### Weaknesses
 * Not effective in all settings (e.g. short sentences or reasoning tasks)

### Questions
How will your conclusions be affected with larger models?

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
This paper proposed a new language model formulation that integrates three distinct components: infini-gram constructed by a corpus, an induction-only model that searches for the input context and constructs a distribution over obtained subsequence, and induction-only model with fuzzy matching. These models are exclusively selected by the effective n (max length of matched sequence) so only one component is responsible to yield the distribution of the next token at each time.
Experiments show its accurate behavior especially when the effective n is large, as well as its compute efficiency when the proposed model is applied to speculative decoding. The paper also involves a downsteram evaluation on fMRI, showing the effectiveness in correlation against response fo brain voxels, and its qualitative summarization with LLMs.

### Strengths
As all the components in the proposed model rely on some sequences in the corpus and/or input context, the proposed model also maintains a certain transparency to calculate the word probability, though it doesn't guarantee the full interpretability on the result of fuzzy matching model.

### Weaknesses
The actual accuracy is far below the baseline LLM (gpt-2 and llama). In addition in Figure 4, any components of the proposed model don't surpass the baseline LLM (llama) when the effective n is small. This is one of the limitations of the proposed model that heavily relies on symbolic history. The performance gap is particularly concerning given the computational resources required for the proposed method, which involves maintaining and searching through a large corpus and input context. The reliance on symbolic history, while offering transparency, seems to limit the model's ability to generalize beyond the seen sequences, especially when the effective n is small, indicating a potential lack of robustness in novel or less frequent contexts.

Experiments in the Table 2 looks unfair. Only a bare Transformer is introduced as a baseline and any other compute-efficient models are not considered. The table also doesn't contain information about the statistics of proposed samples and their acceptance. The absence of more relevant baselines, such as other efficient language models, makes it difficult to assess the true practical value of the proposed method. Furthermore, the lack of details on the acceptance rate of the proposed samples during speculative decoding raises concerns about the practical efficiency gains. Without this information, it's hard to determine if the speed improvements are significant enough to justify the performance gap compared to the baseline LLMs.

### Questions
It is still unclear about the actual relation between the proposed method and "induction head". I think the authors adopted this term for just an analogy, but I would expect some quantitative comparison between the existing analysis of "induction heads" and the result of this study.

More ablation study, especially investigating with one omission of the component is recommended. I got this curiosity because it looks the fuzzy model is generally better than the exact model except its compute efficiency.

It looks the fMRI experiment is interesting, but jsut superfluous and should be investigated in the another study. In contrast, there are few discussion about the behavior of the method itself in-depth in the paper. Because the paper targeted on the interpretability of the method, the authors should focus on reinforcing such information instead of spreading the interest of the paper.

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
4

### Summary
The paper presents a method called the Induction-head ngram model (Induction-Gram), aimed at addressing the issues of interpretability and efficiency in large language models (LLMs). By combining modern ngram models with a hand-designed "induction head," Induction-Gram improves interpretability while significantly enhancing the accuracy of next-word prediction, demonstrating good performance in the natural language fMRI context. Overall, the paper has a high level of innovation and research value, but there are also several areas that require improvement.

### Strengths
The paper demonstrates significant methodological and application innovations with the Induction-Gram model. By introducing the induction head into the ngram framework, the model effectively addresses the limitations of traditional ngram models in adapting to new contexts and handling ambiguous matches. This approach offers a fresh perspective for building interpretable and efficient language models, showcasing notable originality compared to existing research. Furthermore, applying the Induction-Gram model in natural language fMRI contexts is a pioneering effort that broadens the application scope of language models and provides new tools and insights for neuroscience research. The study contributes to a deeper understanding of the mechanisms underlying language models, particularly the role of the induction head in contextual learning. It provides a theoretical basis for advancing the research on the interpretability of language models. Practically, the model enhances prediction accuracy while maintaining interpretability, which is crucial for high-stakes applications requiring explainable model decisions, such as in science, medicine, and policy-making.

### Weaknesses
The limitations in comparison with other models: The paper only compares the Induction-Gram model with a few baseline models, making it difficult to comprehensively assess its relative strengths and weaknesses in the broader modeling field. The lack of comparisons with more diverse types of models, particularly those with unique advantages in interpretability and efficiency, fails to clearly demonstrate the model's true competitiveness in different modeling environments and hinders the identification of its optimal applicability across various scenarios. Insufficient explanation of experimental parameter settings: For some key experimental parameters, such as the hyperparameters in the Fuzzy Matching Model, the paper does not provide sufficient detail regarding their selection criteria and analysis of their impact on model performance. This makes it challenging for other researchers to understand the rationale behind these parameter settings, hindering their ability to effectively adjust and optimize parameters according to their research needs, which ultimately affects the model's reproducibility and scalability.

### Questions
1.Regarding the potential improvements of the induction head: The authors mention that under suboptimal input contexts, techniques such as retrieval-augmented generation can be combined to enhance the performance of the induction head. Can they elaborate on the specific mechanisms of this combination and the expected outcomes? 
2.Details of comparison with other models: The paper only compares the Induction-Gram model with a limited number of baseline models. To provide a more comprehensive assessment of the model's performance, it would be helpful to understand its specific advantages and disadvantages compared to other models that excel in interpretability and efficiency. Particularly, how does the Induction-Gram model's performance differ from these models when handling complex linguistic structures, domain-specific texts, and large-scale data?
3.Impact of training data on the Fuzzy Matching Model: The paper states that the Fuzzy Matching Model was trained using the OpenWebText and Pile-train datasets but does not elaborate on how the selection of these datasets specifically impacts model performance. Different datasets may exhibit varying language styles, topic distributions, and data quality, which could affect the similarity metrics learned by the Fuzzy Matching Model. How do these factors influence the performance of the Induction-Gram model across different tasks?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new interpretable-by-design approach for language modeling and similar prediction tasks named Induction-Gram, in which the existing Infini-gram approach by [Liu et al. (2024)](https://openreview.net/forum?id=u2vAyMeLMm#discussion) for n-gram language modeling is combined with an handcrafted induction mechanism inspired by the induction heads observed to emerge in large language models during early training stages. The proposed approach is shown to improve next word prediction performance for shorter n-gram sequences where the Infini-gram approach underperforms by using local context. Moreover, authors experiment with using their proposed fuzzy induction approach as a draft model for speculative decoding, accelerating LLM generation in a similar or better way than current approaches. Finally, the proposed induction methodology is adapted to predict brain responses to natural language stimuli recorded via fMRI. Again, the induction method outperforms simpler matching baselines, obtaining performances short of state-of-the-art black-box LLM embeddings. Finally, authors employ LLMs to identify common properties of texts for which various prediction strategies perform well, finding induction matching to perform well on narratively critical phrases relying on preceding context.

### Strengths
The idea of complementing n-gram modeling with interpretable context-based mechanisms proposed in this work is very appealing since an interpretable-by-design model mirroring the in-weights vs. in-context learning of modern LLMs can be used to further our understanding of how these mechanisms operate and when they fail. The proposed combination of fuzzy induction matching and Infini-gram is simple yet elegant and seems to address the shortcomings of n-gram-based approaches in an effective way. The fMRI analysis provides an interesting perspective on extending such a technique to other sequence prediction tasks, showcasing promising results. Finally, the qualitative evaluation of Induction-gram improvements further supports the relevance of the proposed approach in context-rich settings.

### Weaknesses
According to Table 1, Induction (fuzzy) would be a strong contender for the best method across all tested settings when using the GPT-2 tokenizer, but falls significantly behind Induction-gram for the LLaMA-2 tokenizer. While this was not discussed in depth in the paper, I believe this results could indicate ta lack of robustness of the reported findings across various tokenization systems.

**Minor corrections:**

Line 238: Typo "are is low"

Mentions to BabyLM should cite the work [Findings of the BabyLM Challenge: Sample-Efficient Pretraining on Developmentally Plausible Corpora
](https://aclanthology.org/2023.conll-babylm.1/) corresponding to the first edition of the shared task.

### Questions
Is the choice of a Fuzzy Matching Model constrained to models using the same tokenizer as the Infini-gram when combining them for Induction-gram? Otherwise, the choice of retraining a similarity model rather than using pretrained sentence embeddings for fuzzy retrieval is unclear to me.

In Figures 2b and 4, it is shown that the large majority of ngram predictions on BabyLM use an effective n below ~8, even when using in-distribution data from another BabyLM split to create the ngram model. In light of this, the choice of the $\tau = 8$ or $9$ in Equation 5 seems to suggest that most cases will recur to fuzzy matching. In light of this, is it even meaningful to maintain the n-gram component in Induction-gram, or are trends shown in these Figure not representative of other tested datasets?

### Soundness
4

### Presentation
3

### Contribution
3
