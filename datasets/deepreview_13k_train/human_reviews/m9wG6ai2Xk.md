# MQuAKE-Remastered: Multi-Hop Knowledge Editing Can Only Be Advanced with Reliable Evaluations

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Large language models (LLMs) can give out erroneous answers to factually rooted questions either as a result of undesired training outcomes or simply because the world has moved on after a certain knowledge cutoff date. Under such scenarios, knowledge editing often comes to the rescue by delivering efficient patches for such erroneous answers without significantly altering the rests, where many editing methods have seen reasonable success when the editing targets are simple and direct (e.g., "what club does Lionel Messi currently play for?").

However, knowledge fragments like this are often deeply intertwined in the real world, making effectively propagating the editing effect to non-directly related questions a practical challenge (e.g., "who is the offspring of the owner of the club that Messi currently plays for?"). Prior arts have coined this task as multi-hop knowledge editing with the most popular dataset being MQuAKE, serving as the sole evaluation benchmark for many later proposed editing methods due to the expensive nature of making knowledge editing datasets at scale.

In this work, we reveal that **up to 33% or 76% of MQuAKE's questions and ground truth labels are, in fact, corrupted in various fashions due to some unintentional clerical or procedural oversights.** Our work provides a detailed audit of MQuAKE's error pattern and a comprehensive fix without sacrificing its dataset capacity. Additionally, we benchmarked almost all proposed \mquake{}-evaluated editing methods on our post-fix dataset, \mquaker{}. It is our observation that many methods try to overfit the original \mquake{} by exploiting some data-specific properties of \mquake{}. We provide a guideline on how to faithfully approach such datasets and show that a simple, minimally invasive approach can bring excellent editing performance without such exploitation. Please refer to the supplemental material for assets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MQuAKE-Remastered, an enhanced version of the MQuAKE dataset designed to improve the evaluation of multi-hop knowledge editing methods for large language models (LLMs). The authors identify significant flaws in the original MQuAKE dataset, including data contamination, conflicting edits, missing information in multi-hop question instructions, and duplicated cases. These issues, which affect lots of the data including 33% or 76% of MQUAKE’s questions and ground truth labels, undermine the accuracy of previous evaluations conducted with MQuAKE. The revised dataset, MQuAKE-Remastered, provides a cleaner, more reliable benchmark without sacrificing dataset capacity. Additionally, the authors propose a novel, minimally invasive method for knowledge editing, achieving state-of-the-art performance without exploiting dataset-specific biases. The paper provides re-benchmarks of existing methods on MQuAKE-Remastered, offering a clearer view of each method's true effectiveness and guiding future approaches to knowledge editing evaluation.

### Strengths
1.	The proposed fixed benchmark and new baseline are clear and easy to follow.
2.	The analysis for the prior benchmark and re-benchmarking the prior works are extremely valuable, which prevents the community from going in the wrong direction of research.
3.	The proposed fixing method is useful for building reliable fixed benchmark.
4.	The proposed method is an effective brand new baseline for this task.

### Weaknesses
1.	The process of identifying the error cases is unclear. The paper introduces the types of error cases, but not show the process of extracting them.

### Questions
1.	How to identify the problematic cases of the original MQuAKE Benchmark?
2.	Do you have a more detailed analysis and case study of your GWalk methods? Could you show some correct cases in your fixed benchmark where GWalk performs well while the baselines fail? What’s the critical part of the GWalk method?

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
2

### Summary
This paper argues that the original MQuAKE dataset contains data contamination, potentially leading to inaccurate evaluation results. The authors audit several contamination categories and remaster the dataset through rewriting and masking.

### Strengths
The paper identifies potential issues within the original MQuAKE dataset and provides an effective remedy. It re-benchmarks several existing knowledge-editing methods and proposes a data-specialty-free approach (GWalk) to address this issue.

### Weaknesses
However, the heuristic approach using dynamic masking may not be adaptable to all types of knowledge editing methods, particularly those without memory-based editing.

### Questions
- As extensive masking is applied in MQuAKE-Remastered, did the authors evaluate its effectiveness on methods that do not have memory retrieval?

- What instruction was used to prompt Llama-3.1 for rewriting? Was this rewriting model the original version, or was it specifically fine-tuned?

- (Minor) There are a few typos that need correction, such as the duplicate “only” in line 71 and the misspelled “audix” in line 488.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
MQUAKE has been a primary benchmark for multi-hop knowledge editing, but the authors reveal that up to 33% of MQUAKE’s ground truth labels and 76% of its questions are compromised by clerical or procedural errors. This paper provides a comprehensive audit and correction of these issues, resulting in MQUAKE-REMASTERED, which preserves the dataset’s capacity while enhancing accuracy. Additionally, the authors benchmark various MQUAKE-evaluated editing methods on the revised dataset and note that many approaches overfit the original MQUAKE dataset by exploiting dataset-specific properties. The paper concludes by recommending a minimally invasive approach for faithfully addressing such datasets, demonstrating that it achieves excellent editing results without exploiting dataset idiosyncrasies.

### Strengths
1.  Knowledge editing is an important topic, and addressing multi-hop knowledge editing is a challenging yet meaningful direction.
2.  The authors identified and addressed key issues within the MQUAKE dataset, which significantly enhances the benchmark’s credibility.
3.   The proposed GWalk method achieves substantial performance improvement over some baseline methods.

### Weaknesses
1.  I believe that methods like fine-tune-based, meta-learning-based, and locate-and-edit would not be significantly affected by the issues raised by the authors in Section 3.1, Section 3.2 and Section 3.3, since they typically perform editing and evaluation on individual samples independently.
2.  GWalk, as a knowledge graph-based search method, is quite common in the Retrieval-Augmented Generation (RAG) domain, which limits its contribution in terms of novelty for knowledge editing.
3.  Although the GWalk method achieves impressive results, there is insufficient analysis on why it performs well. Specifically, the paper lacks a detailed explanation of the benefits introduced by different components, and the construction and search within the knowledge graph could be computationally expensive.
 4.  While the dataset proposed by the authors is helpful for research in the editing domain, especially for multi-hop knowledge editing, its benefits seem to be primarily demonstrated through parameter-preserving methods, such as in-context learning and external knowledge integration. The authors are encouraged to explore more parameter-modifying methods, such as fine-tuning, meta-learning-based, and locate-and-edit approaches, to evaluate the overall effectiveness and versatility of the dataset.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper identifies significant flaws in the widely used MQuAKE dataset for evaluating multi-hop knowledge editing methods. The authors present MQuAKE-REMASTERED, a corrected and enhanced version of the original dataset. They audit and rectify several errors, including intra-contamination, inner-contamination, and conflicts in the multi-hop question instructions. Furthermore, the authors propose a minimally invasive knowledge editing method called GWalk, which achieves state-of-the-art results without exploiting dataset-specific properties.

### Strengths
1. The authors thoroughly analyze the errors in the MQuAKE dataset, bringing awareness to issues that could distort performance evaluations. The audit's depth and transparency add value to the field.
2. MQuAKE-REMASTERED fixes the original dataset's flaws without sacrificing data capacity. This improvement will be a valuable resource for future research on knowledge editing.
3. The proposed GWalk approach is a well-designed and simple method that effectively handles multi-hop knowledge editing without relying on dataset-specific heuristics. Its performance is impressive and highlights the potential for broader applicability.
4. The paper provides extensive re-benchmarking of existing methods, showcasing the significance of the dataset corrections and the robustness of GWalk.

### Weaknesses
1. Some methods encounter out-of-memorOOM issues, which restricts broader adoption and testing. The authors could explore efficient data handling or suggest guidelines for reducing memory usage.
2. The experiments cover a few models. Expanding this to a broader range of LLMs (like 5 LLMs) would provide a more generalized understanding of the benchmark's utility.
3. The authors may run controlled experiments to quantify the impact of each type of contamination on model performance. This would provide more insights into which errors had the most significant effect and how much improvement is due to each fix.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
