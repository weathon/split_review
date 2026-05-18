- Decision: Reject
- Scores: 6, 6, 5

## Merged Review

### Summary
Reviewers agree that the paper introduces representation engineering (RepE), a top-down approach to understanding and controlling large language models via population-level representations. They find the neuroscience motivation sensible, the approach novel, and the experiments extensive, especially regarding honesty and safety. However, all reviewers note severe omissions in the main text: core methodology (reading/control vectors) is left to appendices, mathematical formulation is missing, and implementation details are unclear. Two reviewers (R1, R3) specifically flag the manuscript as poorly structured for ICLR. All reviewers point to the absence of a limitations discussion. The third reviewer (R3, score 5) is notably more critical, stating the paper is "not informative enough" as an ICLR proceeding and questioning the clarity and terminology of Figure 1. Despite strong contributions, presentation and soundness are rated only fair.

### Strengths
- Well-motivated top-down approach to transparency, drawing a fresh analogy from cognitive neuroscience and neuroimaging (R1, R2, R3).
- Clear contrast between RepE (top-down/normative) and mechanistic interpretability (bottom-up/descriptive) in the main text (R2).
- Conceptually straightforward and intuitively appealing method (R1).
- Extensive set of experiments on multiple safety-relevant problems (truthfulness, memorization, power-seeking, etc.) with clear boosts in accuracy on benchmarks (R1, R2).
- Practical benefits are evident: RepE improves LLM transparency and prevents untruthful responses (R1).
- The Contrast Vector baseline and lie-detector monitoring tool are interesting, simple, and practical (R2).
- Novel lower-dimension representation analysis and development of suitable control techniques (R3).

### Weaknesses
- **Severe lack of methodological detail in the main text.** The process of creating reading/contrast/control vectors is not sufficiently described: what data are used, how positive/negative examples are selected, and which algorithms or mathematical formulations derive the final vectors are all unclear. The exact mechanism for merging low-rank matrices into model weights and the rationale for targeting specific layers are absent (R1, R2, R3).
- **Inappropriate manuscript style for ICLR.** Core methodology (representational analysis, control mechanisms) and most results are relegated to the appendix, accessible only through multiple links. The paper reads like a journal narrative rather than a conference paper, making it difficult to assess novelty and validity without the supplement (R1, R3). Reviewers note that the 9-page main body is not informative enough (R3).
- **No discussion of limitations.** The paper overlooks fundamental drawbacks such as the need for full white-box access to LLMs, the cost of collecting stimulus sets and generating contrastive examples, sensitivity to architecture and choice of stimulus set, and potential for introducing biases (R1, R2). Reviewer 2 asks specifically about current limitations and future directions.
- **Unclear differentiation from prior work.** The Related Works section lacks a comprehensive technical comparison, making it hard to distinguish RepE’s contributions from existing approaches (e.g., ROME, Knowledge Editing). The relative effectiveness of LAT compared to prior internal representation extraction methods (not just the Heuristic baseline) is not validated (R1, Q2).
- **Figures poorly integrated and unclear.** Figure 1 is not referenced in the main text; reviewers disagree on its clarity. One reviewer (R3) finds it unclear and argues that the classification of “top-down as normative vs. bottom-up as mechanistic” contradicts terminology in computational neuroscience. Figure 2 takes up excessive space with repetitive examples and is also unreferenced (R1, R2, R3).
- **Missing summary of results from the numerous other applications.** The paper focuses on honesty but leaves navigators to the appendix to appreciate the breadth and performance across all safety-relevant tasks. A concise table or summary in the main text is needed (R2).
- **Questions raised about comparisons and applicability.** Reviewers ask: (1) Why were methods like ROME or knowledge-editing approaches not considered? (R1, Q3). (2) Is the performance gain over in-context learning (few-shot) in Figure 3 significant, especially given the extra assumptions of white-box access and cost? (R1, Q4). (3) Will the code for analyzing pretrained models be publicly released? (R3, Q). These reflect missing experimental comparisons or justification.