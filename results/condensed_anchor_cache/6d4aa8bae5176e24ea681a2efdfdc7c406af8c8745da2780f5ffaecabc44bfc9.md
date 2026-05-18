- Decision: Reject
- Scores: 5, 5, 6

## Merged Review

### Summary
The authors address two limitations of existing knowledge tracing (KT): (1) heavy reliance on expert-defined knowledge concepts (KCs) and (2) neglect of semantic information in questions and KCs. They propose KCQRL, a framework that (a) uses a SotA LLM (GPT-4o) to generate chain-of-thought (CoT) solutions and automatically annotate KCs per solution step, and (b) applies contrastive learning with false negative elimination to produce semantically rich question and step embeddings aligned with KCs. These embeddings can replace randomly initialized embeddings in any existing KT model. On two large math learning datasets, KCQRL yields consistent improvements across 15 KT models. Secondary experiments show benefits in low-sample settings, better-than-default KC annotation quality (evaluated by an LLM), and superiority over alternative embedding methods. The idea of leveraging LLMs for automatic annotation and learning better question embeddings is recognized, but the design of both components has notable limitations.

### Strengths
- The paper makes a convincing case that the proposed LLM-based improvements advance the state of the art for knowledge tracing; the framework is flexible and can enhance many existing and future KT models.
- Methodologically, the approach is novel within the KT domain (automated KC annotation, contrastive learning for question embedding) but follows standard ML/NLP recipes. The applied contribution is strong.
- The formulation is well-motivated, conceptually sensible, and performs well; consistent performance gains are demonstrated across a wide range of KT models.
- The figures are clear and well-drawn, and the experimental discussion highlights key findings with specific table references.
- Extensive experiments support the importance of question embedding, including secondary experiments on training data size, KC annotation quality, and embedding alternatives.
- The framework shows potential for low-sample settings, which could benefit platforms with limited student data.

### Weaknesses
- **Limited domain generalization:** Experiments focus solely on two math-learning datasets (line 168–169). It is unclear whether the CoT and KC annotation approach works for other domains (e.g., physics, history) or for more complex question types (e.g., open-ended responses). [All reviewers]
- **Dependence on LLM quality and stability:** The quality of KC annotations is heavily influenced by the chosen LLM. The paper does not report results with different LLMs (e.g., domain-specific models, lower-power models), which limits understanding of adaptability. [Reviewers 1, 3]
- **Evaluation of KC annotations is weak:** Automatically generated KCs are evaluated only by another LLM, which is not standard. Human-in-the-loop evaluation would strengthen this part. [Reviewer 1; also implied by Reviewer 3 on quality dependence]
- **Noise from LLM annotation undermines contrastive learning:** The auto-annotation inevitably introduces noise and inconsistent KC labeling (similar concepts annotated differently). The paper’s false-negative elimination may not sufficiently mitigate this, and clustering similar KCs still mixes distinct concepts at the data level. A bootstrapping/seed bank approach to standardize KC candidates is suggested. [Reviewer 2]
- **Question embedding design ignores student history:** The learned embeddings have no connection to student interaction sequences, which are crucial for personalized prediction in KT. The paper treats student history merely as labels, abandoning semantic or sequence guidance from past performance. This is a fundamental problem for the KT task. [Reviewer 2 – a significant minority/negative point not raised by other reviewers]
- **Notation confusion:** Both “student” and “solution steps” are represented by the symbol ‘s’. [Reviewer 2]
- **Title mis-claims LLM:** The paper uses BERT for some components (e.g., the first-version annotation? The auto-annotation pipeline description mentions GPT-4o, but BERT is not an LLM; the title is misleading. [Reviewer 2]
- **Interpretability concerns:** Heavy reliance on contrastive learning for false negatives may reduce model interpretability, especially when KCs are similar or overlapping. [Reviewer 3]
- **Limited baseline comparisons:** No experiments with simpler embedding baselines (e.g., bag-of-words, tf-idf) or with a variety of LLM qualities; such experiments would broaden the paper’s interest. [Reviewer 1]
- **Unaddressed practical issues:** It is unclear how KCQRL handles ambiguous or multi-topic questions that do not map clearly to a single KC, and what steps are planned to adapt if the LLM used for annotation becomes outdated or unavailable. [Reviewer 3]