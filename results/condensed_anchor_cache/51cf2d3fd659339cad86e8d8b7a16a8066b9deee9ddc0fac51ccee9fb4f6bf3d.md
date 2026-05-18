- Decision: Reject
- Scores: 3, 5, 5, 5

## Merged Review

### Summary

The paper introduces Retrieval-based Parameter Ensemble (RPE), which stores LoRA parameters in a vector database (LoRA-VecDB) and retrieves/ensembles them based on task similarity for zero-shot adaptation of foundation models. Reviewers generally find the idea simple and intuitive, with potential for privacy-preserving and efficient adaptation, especially on medical tasks. However, there is a clear minority view (Reviewer 1, score 3/confidence 5) raising stronger concerns about novelty, privacy claims, experimental scope, and practical feasibility. The other three reviewers (scores 5, confidence 3 each) see promise but agree that significant gaps—particularly in evaluation, scalability, and comparison to prior work—prevent a stronger acceptance. All reviewers request additional experiments, clearer exposition, and validation of claimed advantages.

### Strengths

- **Simplicity and intuitiveness**: The proposed RPE framework (retrieve LoRA modules, ensemble via weighted combination) is straightforward and easy to implement. [R2, R3]
- **Zero-shot capability**: Avoids expensive fine-tuning on new datasets; only requires a database of pre-computed LoRA weights and dataset representations. [R1, R2, R3]
- **Privacy consideration**: The design keeps raw data local (only parameter ensembles are shared), which is motivated by privacy-sensitive domains like healthcare. [R1, R2, R3]
- **Empirical results on medical data**: Experiments on medical report generation and image segmentation tasks show the method can be competitive with or even outperform supervised fine-tuning in certain cases, demonstrating practical potential. [R2, R3, R4]
- **Multiple weighting strategies**: The paper explores several ways to compute ensemble weights (e.g., cosine similarity, kNN). [R4]

### Weaknesses

1. **Novelty and differentiation from prior work**: The approach strongly resembles existing model‑zoo zero‑shot learning techniques (Task2Vec, Zoo‑Tuning, HyperSTAR, Ada‑Mix); the main difference is using LoRA parameters instead of full models. The paper does not clearly articulate unique algorithmic contributions beyond storage efficiency. [R1, R2]  
   - Specific methods cited: Halbheer et al. (2024, LoRA-Ensemble), Zhai et al. (2023, uncertainty-penalized RLHF with LoRA ensembles). The relation to these LoRA ensemble works is not discussed. [R2]  
   - Reviewer 4 notes that improvement is mostly due to LoRA itself, with RPE providing only marginal gains. [R4]

2. **Privacy claim inaccuracy**: The paper incorrectly states that RAG requires access to raw data, whereas RAG typically retrieves from embedding databases. Privacy‑preserving RAG variants (federated learning, differential privacy) already exist; the paper should compare against them. The claim that RPE improves privacy by not accessing raw data is not novel and needs proper contextualization. [R1]

3. **Insufficient experimental scope**: Evaluations are limited to two medical tasks (report generation and image segmentation) with only 4–6 LoRA adaptations. This narrow domain makes it impossible to assess generalizability to diverse tasks or standard zero‑shot learning benchmarks. [R1, R2, R3]  
   - No evidence that the method works for non‑medical tasks or truly novel (out‑of‑distribution) tasks. [R1, R2, R3]

4. **Lack of scalability analysis**: For realistic deployments with many tasks, storing both LoRA weights and dataset representations creates large storage overhead, and retrieval / weighting of all LoRA modules may become computationally expensive. The paper provides no analysis of retrieval efficiency or storage growth. [R3]  
   - The experiments only handle 4–6 LoRA parameters; no stress tests or scaling experiments are provided. [R3]

5. **Task representation and retrieval process unclear**: The paper does not explain how dataset representations are generated (e.g., mean of embeddings from a pretrained encoder) or how representation quality affects retrieval. The method in Eq. 1 (mean embedding) is ad‑hoc and may not generalize; theoretical justification or broader empirical validation is missing. [R1, R3]  
   - The assumption that similarity of dataset representations correlates with similarity of optimal LoRA weight space is not validated. [R3]

6. **Missing details hindering reproducibility**:  
   - The meaning of δθ_i and δθ_i^{ref} is not explained, nor is the process for obtaining them. [R4]  
   - Regularization details are omitted: how to set the regularization parameter is not specified, preventing replication. [R2]  
   - Experimental setup is vague; e.g., for segmentation, the datasets and evaluation metrics are only briefly described. [R2, R4]  
   - Minor typos (e.g., "from" on p.3 line 159, "reports" → "report" on line 344). [R3]

7. **Performance advantage not convincingly demonstrated**:  
   - Table 3 lacks discussion on why the ensemble method outperforms other methods. [R2]  
   - No runtime / efficiency experiments to back the claim of computational efficiency. [R2]  
   - The improvement over simple LoRA fine‑tuning is marginal; ablation studies isolating the effect of RPE are missing. [R4]

8. **Practical feasibility concerns**: The method assumes a large pool of downstream LoRA models with well‑defined task representations already exist, which is costly and challenging to obtain. Privacy concerns also apply to storing task representations derived from sensitive data. [R1]  
   - For completely new tasks far from existing ones, the approach is unlikely to work; no experiments on domain shift or truly novel tasks. [R3]

9. **Questions overlapping with weaknesses** (explicitly requested by reviewers):  
   - What is the dataset handling / pre‑processing pipeline? [R4]  
   - How are the four LoRA models obtained? What is the pre‑training process? [R4]  
   - What are the time/memory performance measurements? [R2]  
   - Is the ensemble method designed specifically for medical tasks, or does it generalize? [R2]  
   - How does RPE compare to existing LoRA ensemble methods (Halbheer et al., Zhai et al.)? [R2]