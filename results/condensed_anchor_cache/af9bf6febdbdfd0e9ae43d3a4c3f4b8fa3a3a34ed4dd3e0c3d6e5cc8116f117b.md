- Decision: Reject
- Scores: 8, 6, 3, 6

## Merged Review

### Summary
The paper explores decoding reading goals (information seeking vs. ordinary reading) from eye movements using existing models and a new ensemble, evaluated on a large-scale dataset with systematic generalization splits and error analysis. Several reviewers see it as an interesting extension of prior work on reading task classification, particularly from the ZuCo dataset and related studies on deep vs. skim reading. The analysis using linear mixed-effects models highlights features like critical span reading time and paragraph position. The dataset and code are released.

### Strengths
- Well-written, clearly structured, and easy to follow; provides exhaustive background on eye movements in reading and a logical narrative (R1, R2, R4).
- Related work is comprehensive, covering both machine learning models for reading and general eye-tracking-while-reading literature (R1).
- Evaluates a diverse set of state-of-the-art models (eye-movement-only, multimodal, ensemble) with a comprehensive evaluation protocol including three generalization levels (new item, new participant, both) (R2, R4).
- The ensemble model shows improved performance, indicating complementary information captured by different models (R3).
- Error analysis is valuable, leveraging rich textual annotations and using linear mixed-effects models to identify key features (critical span length, reading time before/after critical span, paragraph position) that influence classification difficulty (R2, R3).
- The dataset and code are made publicly available, aiding reproducibility and further research (R3, R4).
- Introduces a novel research question—decoding reading goals from eye movements—which could encourage further work in cognitive science and multimodal analysis; has potential to aid educational tools and personalized learning (R2). (Note: Some reviewers find the novelty limited—see Weaknesses.)
- Methods are appropriate, analysis sound, and implementation details are exhaustively reported (R3, R4).

### Weaknesses
- **Limited novelty in methods and task**: Several reviewers note that the methodologies are all adapted from previous work and that the conceptual framework is almost identical to earlier studies on distinguishing deep vs. skim reading (e.g., Xiuge et al. 2023), informational vs. navigational intent (Sharma et al. 2023), and document type classification (Kunze et al. 2013). The task is an extension of [1] (Hollenstein et al.) with broader ecological validity, but not starkly original (R3, R4). Reviewer 2 acknowledges novelty but also notes limited scope.
- **No new model introduced**: The paper does not propose a novel model that specifically exploits the reading-goal setting, instead applying and ensembling existing ones (R1).
- **Missing statistical rigor**: Standard errors and statistical significance tests between trainable models (e.g., best model vs. rest) are not reported. AUROC is not reported despite being a natural metric for binary classification (R1).
- **Unclear multimodal integration**: The description of how eye-movement features are combined with text embeddings is vague—e.g., whether text embeddings are static or dynamically updated, which fusion technique is used (concatenation, attention), and what the input/output dimensions and activation functions are (R2).
- **Limited scope of goals**: Only two reading goals (information seeking and ordinary reading) are considered. Extending to other common strategies like skimming, proofreading, or scanning for keywords is not addressed; the binary classification restricts practical utility. The paper does not discuss how the model could be adapted to additional goals (R2).
- **Missing discussion of real-world applicability**: No analysis of performance under variable eye-tracking calibration (e.g., web-based eye tracking) or in less controlled environments (R2). The paper lacks explanation of why reading goal prediction is important and which specific applications would benefit (R3).
- **Incomplete discussion of limitations**: The limitations of the current methods and dataset are not systematically discussed. For example, all paragraphs are short (newspaper excerpts, expository texts); generalization to longer, narrative, or entertainment-focused texts is not considered. Differences between reading comprehension tasks (e.g., exam vs. casual understanding) are not addressed (R3).
- **Interpretability constraints**: The critical-span analysis for interpretability only works for known texts (R1).
- **Accessibility issues**: The anonymous repository and data are not accessible at review time (R1).
- **Scientific implications underdeveloped**: The paper does not explain how the findings could improve current methods or fully exploit eye movements for this task (R3). Some reviewers suggest the topic fits a psycholinguistics or computational linguistics venue better than ICLR (R3).