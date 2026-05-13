# CURVALID: A Geometrically-guided Adversarial Prompt Detection

- Decision: Reject
- Scores: 6, 3, 6, 3

## Abstract
Adversarial prompts that can jailbreak large language models (LLMs) and lead to undesirable behaviours pose a significant challenge to the safe deployment of LLMs. Existing defenses, such as input perturbation and adversarial training, depend on activating LLMs' defense mechanisms or fine-tuning LLMs individually, resulting in inconsistent performance across different prompts and LLMs. To address this, we propose CurvaLID, an algorithm that classifies benign and adversarial prompts by leveraging two complementary geometric measures: Local Intrinsic Dimensionality (LID) and curvature. LID provides an analysis of geometric differences at the prompt level, while curvature captures the degree of curvature in the manifolds and the semantic shifts at the word level. Together, these tools capture both prompt-level and word-level geometric properties, enhancing adversarial prompt detection. We demonstrate the limitations of using token-level LID, as applied in previous work, for capturing the geometric properties of text prompts. To address this, we propose PromptLID to calculate LID in prompt-level representations to explore the adversarial local subspace for detection. Additionally, we propose TextCurv to further analyze the local geometric structure of prompt manifolds by calculating the curvature in text prompts. CurvaLID achieves over 0.99 detection accuracy, effectively reducing the attack success rate of advanced adversarial prompts to zero or nearly zero. Importantly, CurvaLID provides a unified detection framework across different adversarial prompts and LLMs, as it achieves consistent performance regardless of the specific LLM targeted.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies adversarial prompt detection. It revitalizes metrics of LID from anomaly detection to this task, by estimating the score on a learned prompt-level representation instead of a suboptimal word-level one. The paper further proposes TextCurve score, and merges these two metrics into a single score for the final decision. The final binary classifier needs to be trained on a collect. Extensive empirical results and ablation study demonstrate the generation and robustness of the proposed metrics despite the need for training.

### Strengths
1. Novelty: The author revitalized LID score in detecting adversarial prompts by estimating it on the learned aggregated output of word level embeddings. It further proposes TextCurve to capture the extra curvature information around the prompt. The final decision takes account for both metrics via a learned linear combination.
2. Extensive experimental evaluations. The paper includes a detailed amount of empirical evaluations and analysis to support the effectiveness of the proposed method, as well as providing insights into how different components affect its performance.

### Weaknesses
1. How is curveLID’s defenses against jailbreaking algorithms rather than static harmful prompt? It Whitebox methods are not applicable in this setting, but the author can potentially try some blackbox methods, such as DrAttack or Multijail? It seems that the authors include several defense methods in the Appendix, but the experiment seems not directly related to the proposed metrics (I could be wrong).
2. Minor: the appendix is very rich in useful information so it cannot be ignored. Tut currently the organization is quite flattened so a bit difficult to track everything. Organizing it into sections/subsections (e.g. all ablations are grouped together, all analysis are grouped together) might improve its readability.

### Questions
1. Several parts of the CurveLID metric requires fitting on training data of adversarial v.s. benign prompts. I’d expect that the performance will depend heavily on the coverage of training data distribution, but judging from the experimental results it seems the generalization is pretty descent, have the authors had any insights on why this is the case?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Summary:
This paper presents CurvaLID, a framework that claims to detect adversarial prompts in LLMs using geometric measures combining Local Intrinsic Dimensionality (LID) and curvature. While achieving reported empirical results of 99% detection accuracy, the paper suffers from fundamental theoretical flaws, questionable design choices, and significant limitations that are either unexplored or unacknowledged.

Major issues identified:

1. The paper presents three classical curvature definitions (osculating circle, Whewell equation, differential geometric) but implements a formula (dθ/(1/||u|| + 1/||v||)) that has no clear mathematical connection to any of them. The reference to Whewell's equation (dφ/ds) lacks proper theoretical grounding. The authors don't define arc length, don't justify how embedding angles relate to tangential angles, and provide no proof of geometric equivalence to Whewell’s equation. The denominator term using inverse vector norms appears ad hoc and unfortunately comes with no geometric justification.Claims about semantic shifts relating to curvature are made without mathematical rigor or proof. The relationship between their geometric measures and adversarial behavior is assumed (lines 265-266) rather than proven. Therefore, there is a massive disconnect between the theory shown in Section 3 and what is finally implemented. 

2. The choice of architecture to use a CNN for text classification is unjustified by the authors. Why choose a CNN when there are more appropriate architectures (like Transformers, RNNs etc) available for sequential data?
The missing aspects are that: (i) there is no justification as to why CNNs would better capture textual properties. 
(ii) how are variable length sequences handled by a CNN? Is it via padding? 
(iii) How would a CNN capture long-range dependencies in text?
(iv) CNNs typically rely on “spatial order”, what is the equivalent in this setting?

3. In the multi-class classification definition, there is no proper specification given of the label space Q and its relationship to their task. It looks like it’s just a single label per training example. 

4. This paper provides no theoretical time and storage complexity analysis of their defense, especially for their key algorithms. While TextCurv computation is O(nd) for sequence length n and embedding dimension d, they don't discuss this in detail. The fact is that if “true differential geometry” metrics were used then the computational complexity is high and mostly polynomial time. 

The complexity analysis for critical components should be presented. Such as CNN feature extraction, k-NN computation for PormptLID, Overall pipeline complexity including the MLP classifier. How does complexity scale with longer sequences or larger embedding dimensions or increased batch sizes?

This lack of complexity analysis makes it difficult to assess: i). Practical deployability of their method, ii). scalability to longer prompts, iii). real-time defense capabilities and iv). resource requirements for implementation


5. The method relies critically on exact word order, making it vulnerable to simple paraphrasing. If there are basic linguistic variations like active/passive voice conversion, which retains the semantic meaning, this method would end up with two different representations (geometric measures) completely. This limitation isn’t mentioned or addressed. A simple text restructuring can circumvent this defense. 

6. This work presents a limited evaluation in terms of variety of attack types, even when focused on just single-step attacks. There is no analysis of the dataset diversity or potential overlaps between the 8 datasets proposed. There are no evaluations on social engineering attacks (as claimed in introduction) where they stop persuasion attacks for example. There is no testing of non-English attacks despite claims of language-agnostic performance. 

7. The CNN feature extraction process is not explained properly and leaves a lot of questions. The hyperparameter choices are arbitrary and do not come with a good justification. It would be nice to see training stability, convergence and sensitivity to initialization studies in the experiments. There must be comparisons made to move naive baseline approaches. 

8. There are some reproducibility concerns that must be highlighted too. Critical hyperparameters are left unspecified. Preprocessing details are left incomplete. There is no outline of the training environment and no discussion of potential implementation challenges that are faced.


The paper suffers from multiple fundamental flaws that significantly undermine its contribution. Currently, the paper presents a major disconnect between the presented theoretical framework (which is sophisticated and borrowed from differential geometry) and actual implementation (which is a heuristic). The sequence dependency problem reveals a fundamental limitation that makes the method vulnerable to simple linguistic variations, while the choice of CNN architecture for text processing appears arbitrary and poorly justified.

Additionally, the lack of thorough analysis, missing implementation details, and limited validation make it difficult to assess the method's true effectiveness and reproducibility. The combination of theoretical flaws, practical limitations, and methodological gaps warrants a rejection at this point.
 
I recommend the following:
1. A complete theoretical overhaul establishing proper connections between differential geometry and their implementation
2. Justification for architectural choices and comparison with alternatives
3. Analysis of and solutions for the sequence dependency problem
4. Comprehensive evaluation across a wider range of linguistic variations and attack types
5. Complete technical details enabling reproducibility

While the empirical results appear promising, they cannot overcome the fundamental theoretical and methodological issues present in the paper.

### Strengths
1. The paper introduces an innovative geometric framework (CurvaLID) that combines two complementary measures - Local Intrinsic Dimensionality (LID) and curvature - to detect adversarial prompts. Unlike existing approaches that rely on token-level analysis, the paper presents PromptLID which analyzes geometric differences at the prompt level, and TextCurv which captures semantic shifts at the word level.

2. The paper achieves exceptional performance metrics like (i) Over 0.99 detection accuracy for English prompts, 
(ii) 0.994 accuracy for non-English prompts and (iii) Successfully reduces attack success rates to near zero
It also Includes detailed ablation studies showing the importance of both PromptLID and TextCurv components.

3. The solution is highly efficient, requiring only 15 minutes of training on a single Nvidia H100 GPU, compared to competing methods that need up to 16 hours on more extensive hardware setups. The approach is model-agnostic, meaning it doesn't require access to or modification of the underlying LLM. The method also scales well to different languages without requiring retraining.

### Weaknesses
1. The paper presents three classical curvature definitions (osculating circle, Whewell equation, differential geometric) but implements a formula (dθ/(1/||u|| + 1/||v||)) that has no clear mathematical connection to any of them. The reference to Whewell's equation (dφ/ds) lacks proper theoretical grounding. The authors don't define arc length, don't justify how embedding angles relate to tangential angles, and provide no proof of geometric equivalence to Whewell’s equation. The denominator term using inverse vector norms appears ad hoc and unfortunately comes with no geometric justification. Claims about semantic shifts relating to curvature are made without mathematical rigor or proof. The relationship between their geometric measures and adversarial behavior is assumed (lines 265-266) rather than proven. Therefore, there is a massive disconnect between the theory shown in Section 3 and what is finally implemented.

2. The choice of architecture to use a CNN for text classification is unjustified by the authors. Why choose a CNN when there are more appropriate architectures (like Transformers, RNNs etc) available for sequential data?
The missing aspects are that: (i) there is no justification as to why CNNs would better capture textual properties. 
(ii) how are variable length sequences handled by a CNN? Is it via padding? 
(iii) How would a CNN capture long-range dependencies in text?
(iv) CNNs typically rely on “spatial order”, what is the equivalent in this setting?

3. In the multi-class classification definition, there is no proper specification given of the label space Q and its relationship to their task. It looks like it’s just a single label per training example.

4. This paper provides no theoretical time and storage complexity analysis of their defense, especially for their key algorithms. While TextCurv computation is O(nd) for sequence length n and embedding dimension d, they don't discuss this in detail. The fact is that if “true differential geometry” metrics were used then the computational complexity is high and mostly polynomial time. 

The complexity analysis for critical components should be presented. Such as CNN feature extraction, k-NN computation for PormptLID, Overall pipeline complexity including the MLP classifier. How does complexity scale with longer sequences or larger embedding dimensions or increased batch sizes?

This lack of complexity analysis makes it difficult to assess: i). Practical deployability of their method, ii). scalability to longer prompts, iii). real-time defense capabilities and iv). resource requirements for implementation


5. The method relies critically on exact word order, making it vulnerable to simple paraphrasing. If there are basic linguistic variations like active/passive voice conversion, which retains the semantic meaning, this method would end up with two different representations (geometric measures) completely. This limitation isn’t mentioned or addressed. A simple text restructuring can circumvent this defense. 

6. This work presents a limited evaluation in terms of variety of attack types, even when focused on just single-step attacks. There is no analysis of the dataset diversity or potential overlaps between the 8 datasets proposed. There are no evaluations on social engineering attacks (as claimed in introduction) where they stop persuasion attacks for example. There is no testing of non-English attacks despite claims of language-agnostic performance. 

7. The CNN feature extraction process is not explained properly and leaves a lot of questions. The hyperparameter choices are arbitrary and do not come with a good justification. It would be nice to see training stability, convergence and sensitivity to initialization studies in the experiments. There must be comparisons made to move naive baseline approaches. 

8. There are some reproducibility concerns that must be highlighted too. Critical hyperparameters are left unspecified. Preprocessing details are left incomplete. There is no outline of the training environment and no discussion of potential implementation challenges that are faced.

The paper suffers from multiple fundamental flaws that significantly undermine its contribution. Currently, the paper presents a major disconnect between the presented theoretical framework (which is sophisticated and borrowed from differential geometry) and actual implementation (which is a heuristic). The sequence dependency problem reveals a fundamental limitation that makes the method vulnerable to simple linguistic variations, while the choice of CNN architecture for text processing appears arbitrary and poorly justified.

Additionally, the lack of thorough analysis, missing implementation details, and limited validation make it difficult to assess the method's true effectiveness and reproducibility. The combination of theoretical flaws, practical limitations, and methodological gaps warrants a rejection at this point.

### Questions
I recommend the following:
1. A complete theoretical overhaul establishing proper connections between differential geometry and their implementation
2. Justification for architectural choices and comparison with alternatives
3. Analysis of and solutions for the sequence dependency problem
4. Comprehensive evaluation across a wider range of linguistic variations and attack types
5. Complete technical details enabling reproducibility

While the empirical results appear promising, they cannot overcome the fundamental theoretical and methodological issues present in the paper.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an adversarial prompt detection method using the geometric information within the latent representation of an input prompt. Specifically, prompt-level local intrinsic dimensionality using a CNN is proposed as a feature to distinguish the difference between adversarial and benign prompts. TextCurv is also proposed to account for semantic change at the word level, which is another feature to classify adversarial prompts. The proposed method is validated across several adversarial attacks in different LLMs.

### Strengths
The paper is clearly written and the proposed method is described clearly.

### Weaknesses
1. The size of the data (2500 prompts) is quite limited.

2. Persuasive adversarial prompts [1] will also lead to harmful content but not considered and tested in this work.

3. The proposed detection looks similar to perplexity-based filter. It would be more convincing to include attacks that can bypass perplexity-based filter like AutoDAN [2].

### Questions
Could the authors address the three weaknesses above?

### Soundness
2

### Presentation
3

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
This paper introduces CurvaLID, a model that detects adversarial prompts targeting LLMs. CurvaLID can capture the structural characteristics of entire prompts through "Prompt-Level Local Intrinsic Dimensionality" (PromptLID) and detects semantic shifts within the text using "Text Curvature" (TextCurv) to identify whether a prompt is adversarial. Since this method relies entirely on analyzing textual structure rather than LLM-specific architectures or parameters, it requires no fine-tuning for each LLM. This design significantly accelerates training speed, taking only 15 minutes on a single Nvidia H100 GPU.

### Strengths
The method has good advantages. Currently, most adversarial sample detection methods rely on large models, which makes the training process quite time-consuming. CurvaLID bypasses large language models entirely, directly analyzing text embeddings to identify adversarial inputs, and saving computational resources.

Additionally, the method is zero-shot, meaning it doesn't require fine-tuning for each LLM, making it even more versatile and efficient.

### Weaknesses
1 I think that the innovation and contributions of your method are somewhat limited. The proposed approach resembles a CNN-based text filter, primarily detecting anomalies in embeddings, which isn't a novel concept.

2 The connection between this work and LLMs is relatively weak. As mentioned, CurvaLID functions more like an independent text filter, focusing only on text structure and density features. It's more of a generic text filter than a targeted tool for detecting adversarial samples specific to LLMs. I don't mean to suggest that the detection method has no value, but most LLM-focused adversarial attacks today generate adversarial samples that closely resemble benign samples in terms of structure, density, and even embedding similarity. This would likely limit CurvaLID's effectiveness against subtle adversarial prompts.

3 There are also issues in the experimental design. CurvaLID was trained and evaluated on the same datasets—Orca, MMLU, AlpacaEval, and TQA—which could inevitably lead to overly optimistic results.

4 I noticed that the manuscript mixes American and British spellings in some places (such as "defence" and "defense"). To maintain a professional and consistent tone throughout, I recommend choosing one spelling style—American or British—and using it uniformly across the article.

5 The formatting of tables is inconsistent. Some tables use a three-line format, while others do not. A unified table style would improve clarity and presentation quality.

### Questions
1 Have the authors tried different CNN configurations to assess their impact on the performance of PromptLID and TextCurv?

2. Why did the authors choose to use CNN? If the goal is to capture relationships between textual features, wouldn’t Transformers perform better? Have you considered trying Transformers for this purpose?

3. The method relies only on structural and semantic changes to identify adversarial samples. Have the authors tested against adversarial examples with structural and semantic characteristics similar to benign samples? Specifically, have the authors tried generating adversarial examples with density and curvature that closely resemble benign samples to evaluate CurvaLID’s performance?

4. Have the authors analyzed the impact of text length on PromptLID? Given that longer texts have higher complexity and density, could they lead to benign texts being misclassified as adversarial?

5. Have the authors tested whether non-standard benign samples, such as those containing spelling errors or slang, might be misclassified as adversarial examples?

6. Can the method detect adversarial prompts that rely on contextual association across multiple prompts?

7. The authors trained the model on Orca, MMLU, AlpacaEval, and TQA datasets and then used the same datasets to evaluate whether the samples were benign or adversarial. Given this setup, does the model’s high accuracy have practical significance?

### Soundness
3

### Presentation
2

### Contribution
2
