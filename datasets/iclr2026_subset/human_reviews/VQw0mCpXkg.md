## Human Reviewer 1

### Summary
The paper proposes a two-stage voting architecture for suicide risk detection. Stage 1 uses a BERT classifier to handle explicit cases, while Stage 2 routes ambiguous posts to either (a) an LLM voting ensemble or (b) an ML ensemble using psychologically grounded features extracted via LLMs. The authors claim state-of-the-art performance on both explicit (Reddit) and implicit (DeepSuiMind) datasets, with F1 scores of 98.0% and 99.7%, respectively, and a reduced cross-domain performance gap.

### Strengths
The two-stage design is conceptually appealing for balancing efficiency and robustness.
The use of psychologically inspired features is a step toward interpretability.
The problem is timely and socially impactful.

### Weaknesses
The DeepSuiMind dataset contains only suicidal posts (1,605 samples, all positive class). This violates basic principles of binary classification evaluation and artificially inflates performance metrics. The reported 99.7% F1 is misleading and not comparable to standard benchmarks.

The authors compare against BERT and LLM variants but fail to include strong baselines such as RoBERTa, DeBERTa, or other suicide-specific models (e.g., PsyGuard, Evidence-Driven Marker Extraction). This undermines the claim of novelty and superiority. The weight optimization for the ML ensemble is described only at a high level. No formulation, constraints, or optimization objective is provided, making replication impossible.

The authors claim a cross-domain gap below 2%, but this is based on two highly dissimilar datasets (one explicit, one synthetic and implicit-only). No true cross-domain or out-of-distribution evaluation is performed.

While the authors promise to release code, key details—such as routing thresholds, LLM versions, prompt templates, and hyperparameters—are omitted or only superficially described.

The DeepSuiMind dataset is LLM-generated, which raises serious concerns about ecological validity and real-world applicability. The authors do not validate their model on real-world implicit suicidal content or clinician-annotated data.

The “fundamental features” (e.g., suicide intent, distress level) are reduced to binary or categorical outputs from an LLM, with no validation against clinical gold standards. This risks misrepresenting complex psychological states.

The idea of cascaded models and LLM-based feature extraction is not new. The paper does not sufficiently differentiate its contributions from prior work in cascaded NLP systems or interpretable mental health AI.

The prompt examples in the appendix are overly verbose and lack clarity.

### Questions
None

### Soundness
2

### Presentation
3

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper proposes a two stage pipeline mainly focused on finding implicit suicidal intent in text. Stage one uses BERT, stage 2 uses a combination of proprietary LLMs (GPT-5/GPT-4o) and heuristic ML methods. The method is evaluated on two datasets, Reddit (mainly explicit) and DeepSuiMind (mainly implicit).

### Strengths
1. The paper studies an important and socially impactful problem identifying implicit suicidal intent, which is considerably more challenging than explicit detection.

### Weaknesses
1. The Stage 2 ML subsystem still depends on an LLM to extract features at inference time, so the ML based system is not necessarily fast.
2. Since DeepSuiMind (entirely implicit) is routed directly to Stage 2 (and the Reddit dataset being mainly explicit), this setup is somewhat artificial and does not reflect real world mixed distributions.
In many cases, BERT-base-uncased already performs well; a more recent, better encoder model with fine tuning might close the gap significantly.
3. The choice of baselines is somewhat unconventional, and the evaluation lacks clarity on how they were selected or tuned.
4. The results report extremely high scores (often >99%), but no error bars or statistical significance analysis are provided, making it difficult to assess whether these differences are meaningful.
5. The length-based confidence filtering of posts appears arbitrary. Using entropy or uncertainty of classification logits could be a more principled approach. This also connects to the potential use of modern BERT variants with longer context windows.

While the topic is highly relevant and the two-stage design is interesting, the paper can benefit from a better experimental setup and analysis.

### Questions
1. Typo at line 206 (“Stage”).
2. How does the BERT baseline perform when fine-tuned on synthetically generated implicit cases?
3. Have the authors considered fine-tuning a mid-sized decoder LLM (1B–3B parameters) on a synthetic dataset mixing explicit and implicit examples? This could bridge the performance gap between BERT and the proprietary LLMs.
4. Why not employ ModernBERT [1], which supports longer contexts and has shown substantial gains in both efficiency and performance over standard BERT?
5. How about providing few-shot in-context demonstrations to GPT?

[1] Warner, Benjamin, et al. "Smarter, better, faster, longer: A modern bidirectional encoder for fast, memory efficient, and long context finetuning and inference." arXiv preprint arXiv:2412.13663 (2024).

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
The paper presents a two-stage binary suicide risk classification framework. The idea is the use lightweight BERT to directly classify input if the confidence level is high; otherwise, use LLM agents or efficient feature-engineered ML models (prepared with the help of LLMs). In this way, the authors aim to achieve a balance between efficiency and robustness. The authors also claim the work to be "among the first works to operationalize LLM-extracted psychological features as structured vectors for suicide risk detection".

### Strengths
- Metaphor, sarcasm, or subtle emotional cues are real challenges in NLP research, and it is meaningful to study classification tasks that could address them.

- The overall approach is simple and easy to follow. Motivation is clear as well.

- Authors provided full prompts to the LLM, which could be referred to by relevant researchers.

### Weaknesses
- The novelty is marginal, considering research on query extension or retrieval-augmented generation already exists and leverages various techniques to help with natural language processing (NLP) tasks.

- The claimed contributions (page 2) do not appear substantial: simple voting, leveraging LLM-generated features appear to be commonplace in NLP tasks, even recommendation tasks.

- The empirical studies only cover GPT-5 agents, BERT as baselines. More recent, competitive baseline methods should be included to make the results convincing.

### Questions
na

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
2

---

## Human Reviewer 4

### Summary
This paper introduces a two-stage ensemble learning framework for predicting suicidal risk in posts from online social networks such as Reddit. The framework's core innovation lies in its division of labor: the first stage efficiently predicts risk for short posts with high confidence, while the second stage employs a large language model to infer psychological features, such as suicide intent. For experimental validation, the authors construct a dataset from Reddit and adapt an existing implicit suicidal ideation dataset, DeepSuiMind. The results demonstrate that the proposed framework outperforms baseline approaches that utilize only components of the full system. Additionally, the authors provide evidence that their psychological features contribute meaningfully to risk identification.

### Strengths
The primary strength of this work is the demonstrated effectiveness of the two-stage ensemble approach. While conceptually straightforward, the framework achieves superior performance compared to its individual components, and the authors present comprehensive experimental results that illuminate the contribution of each design choice.

### Weaknesses
Several significant concerns warrant attention. First, the experimental design lacks sufficient baselines and thorough analysis. The authors cite Hasan & Saquer (2024) to support their claim that BERT represents the state-of-the-art, yet that paper actually reports RoBERTa as the best-performing model (see Table 2 of the paper). Since BERT is merely one component of the proposed framework, it would be valuable to compare it against other strong baselines, particularly RoBERTa. Furthermore, for fair comparison, the authors should consider evaluating their framework on the same dataset used by Hasan & Saquer (2024); the rationale for constructing a new dataset rather than using this existing benchmark is unclear.

Second, the analysis of psychological features requires deeper exploration. While the authors claim these features enhance interpretability, they provide limited investigation into which specific features contribute most to prediction accuracy and why. A feature-level ablation study or importance analysis would substantially strengthen the interpretability claims. 

Third, the manuscript requires careful revision for clarity and completeness. For instance, the reference "Komati et al." appears incomplete. Additionally, the six risk-relevant dimensions lack proper attribution. The authors should cite the established suicide risk assessment frameworks from which these dimensions are derived.

### Questions
- There is a discrepancy in the DeepSuiMind test set size: the original paper reports 1,308 cases, while Table 3 shows 1,605. This inconsistency needs clarification. 
- (Minor comment) Performance metrics would be more accessible in tabular format rather than bar graphs, as the current visualization makes it difficult to discern precise values and compare model performance accurately.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3