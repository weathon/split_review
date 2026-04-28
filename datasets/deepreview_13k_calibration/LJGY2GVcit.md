# Foldable SuperNets: Scalable Merging of Transformers with Different Initializations and Tasks

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 5, 6

## Abstract
Many recent methods aim to merge neural networks (NNs) with identical architectures trained on different tasks to obtain a single multi-task model. Most existing works tackle the simpler setup of merging NNs initialized from a common pre-trained network, where simple heuristics like weight averaging work well. This work targets a more challenging goal: merging large transformers trained on different tasks from distinct initializations.
First, we demonstrate that traditional merging methods fail catastrophically in this setup.
To overcome this challenge, we propose Foldable SuperNet Merge (FS-Merge), a method that optimizes a SuperNet to fuse the original models using a feature reconstruction loss.
FS-Merge is simple, data-efficient, and capable of merging models of varying widths. We test FS-Merge against existing methods, including knowledge distillation, on MLPs and transformers across various settings, sizes, tasks, and modalities.%\footnote{Code and models will be published upon acceptance.} %% change for ICLR

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenging problem of merging large transformers trained on different tasks from distinct initializations, where prior works typically rely on models that share a common pretrained initialization. The proposed method, FS-Merge, utilizes a feature reconstruction loss to merge the original models effectively.

### Strengths
- The method is data-efficient, requiring only an unlabeled subset of the training data for optimization, which is advantageous when full access to data is limited.
- The paper presents comprehensive experimental results across various model architectures and data scenarios, demonstrating the scalability and effectiveness of FS-Merge in merging models of different scales and tasks.

### Weaknesses
 - While the method is designed for models trained from scratch, it would be insightful to investigate its performance when applied to pretrained models that are fine-tuned on different sources. Specifically, it would be beneficial to explore potential challenges or advantages this application might present compared to merging models trained from scratch. This analysis could provide a broader understanding of the method's applicability and limitations.
- The paper could benefit from a discussion on robustness to distribution shifts, similar to what is explored in the WiSE-FT paper, "Robust fine-tuning of zero-shot models".
- It would be helpful to compare this method to Mixture of Experts (MoE) approaches, such as "Branch-Train-MiX: Mixing Expert LLMs into a Mixture-of-Experts LLM", to provide context on how FS-Merge differs or could complement these strategies. I encourage the authors to provide a comparison between FS-Merge and MoE approaches, with a focus on key differences such as computational efficiency, model size, and how FS-Merge could potentially complement MoE methods. This comparison would contextualize the distinct contributions of FS-Merge and highlight its unique strengths.
- Why does distillation perform poorly in the last task (C, M, C100, E) as shown in Table 4, while it performs well in the earlier tasks? An analysis or hypothesis explaining this discrepancy would strengthen the paper's results section. Discussing potential contributing factors such as task similarity, dataset characteristics, or interactions between specific models being merged would add depth to the findings and clarify this discrepancy.
- Given the use of the “first” initialization, how sensitive is the method to changes in the order of models? Would changing the order significantly affect the merged model’s performance, and if so, why? The authors should consider conducting an ablation study on the impact of model ordering during initialization. Reporting performance metrics for different orderings and discussing any observed patterns or practical implications would provide valuable insights into the method's robustness and guide its real-world application. Furthermore, the lack of consistency in the choice of datasets and ordering across different experiments, such as the newly added Table 24 which uses a unique order and datasets, makes it challenging to compare the method across different scenarios.

### Questions
- Why does distillation perform poorly in the last task (C, M, C100, E) as shown in Table 4, while it performs well in the earlier tasks? An analysis or hypothesis explaining this discrepancy would strengthen the paper's results section. Discussing potential contributing factors such as task similarity, dataset characteristics, or interactions between specific models being merged would add depth to the findings and clarify this discrepancy.
- Given the use of the “first” initialization, how sensitive is the method to changes in the order of models? Would changing the order significantly affect the merged model’s performance, and if so, why? The authors should consider conducting an ablation study on the impact of model ordering during initialization. Reporting performance metrics for different orderings and discussing any observed patterns or practical implications would provide valuable insights into the method's robustness and guide its real-world application.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work addresses the challenging task of merging large transformers trained on different tasks from distinct initializations. The authors first demonstrate that traditional merging methods fail catastrophically in this scenario. To tackle this, they propose Foldable SuperNet Merge (FS-Merge), a method that optimizes a SuperNet to fuse the original models using a feature reconstruction loss. FS-Merge is straightforward, data-efficient, and capable of merging models with varying widths. The method is evaluated against existing approaches, including knowledge distillation, on MLPs and transformers across diverse settings, sizes, tasks, and modalities. FS-Merge consistently achieves state-of-the-art (SOTA) results, particularly in data-limited scenarios.

### Strengths
1.	The paper tackles an intriguing problem: merging large transformers trained on different tasks from distinct initializations into a single model.
2.	The proposed method is simple and easy to follow.

### Weaknesses
1.	FS-Merge is a training-based merging method, which can be costly compared to other model merging techniques. Furthermore, the comparison to knowledge distillation (KD) as a baseline is not clearly justified, as KD is also a training-based method, making the comparison potentially unfair. The computational overhead of FS-Merge, especially in terms of FLOPs and memory usage, needs more rigorous analysis and comparison against other merging methods.
2.	The figures, such as Figure 3, are low resolution, and the overall writing quality of the paper is not very professional, requiring significant improvement and refinement. The lack of clarity in the writing makes it difficult to fully grasp the nuances of the proposed method and its advantages over existing techniques.
3.	The datasets used, such as MNIST and SVHN, are relatively small, and the performance improvements appear marginal. Also, the experimental setup seems unique to this paper and not aligned with standard practices in prior literature. The choice of datasets and experimental setup makes it difficult to generalize the findings to more complex scenarios and compare them with other model merging approaches. The lack of alignment with standard practices raises concerns about the validity and generalizability of the results.
4.	The paper is largely empirical, lacking an in-depth discussion on why the proposed method effectively combines models trained on different domains. The method's effectiveness is not well explained, and it is unclear why it outperforms other methods, especially given its similarity to adapter-based approaches. The absence of a theoretical framework or a deeper analysis of the underlying mechanisms limits the understanding of the method's strengths and weaknesses.

### Questions
1.	What is the training cost associated with different datasets, such as FLOPs?
2.	The proposed approach is similar to adapter-based methods. Could the authors discuss this similarity?
3.	It would be beneficial to include results on larger-scale datasets, such as the VTAB-1K benchmark and even ImageNet-1K, which are widely used in model merging or domain adaptation research.

### Soundness
2

### Presentation
2

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
The paper tackles the problem of merging two Transformers with different initializations and target tasks. To this problem, the paper proposes an extension of the previous idea of folding two weight matrices to the Transformer architecture, and proposes to optimize the merging/unmerging layers for folding by knowledge distillation on unlabeled data.

### Strengths
1. The paper is well-structured and easy to follow.
2. The paper polishes the idea of merging by folding from [1], i.e., merging two weights by inserting merging/unmerging layers, and extends it to the specific architecture of Transformer. Also the paper shows it works well when combined with knowledge distillation on unlabeled data.

### Weaknesses
1. Although the extension of the previous idea to Transformer is a technical contribution, the novelty of the proposed method is still limited since it just applies the feature-level knowledge distillation to the merging/unmerging layer which is originally proposed in [1]. The core idea of using knowledge distillation to optimize the merging layers, while effective, lacks significant novelty beyond the direct application of existing techniques. The specific parameterization of the merging matrices as diagonal plus low-rank, while potentially beneficial, does not fundamentally alter the approach's reliance on knowledge distillation for optimization.
2. While the title suggests that this paper addresses the general problem of merging Transformers with different initializations, but the experiments are performed only with the Vision Transformer with a few downstream tasks. Also, since there are various pre-trained Vision Transformers available, it should be tested with other initializations rather than just ImageNet-1K pre-trained one. The limited scope of the experiments, focusing primarily on Vision Transformers and a single pre-training initialization, raises concerns about the generalizability of the findings to other Transformer architectures and pre-training strategies. The lack of experiments with diverse initializations, such as those derived from different datasets or self-supervised methods, limits the conclusions that can be drawn about the method's robustness.
3. The proposed approach heavily relies on optimization with unlabeled data, while the previous works (SLERP, RegMean, ZipIt, Opt) are designed to be applied without any optimization (but also can be with additional finetuning). If we allow such optimization, the problem can also be reduced to multi-task learning or distillation (with unlabeled data in this case), which now has a plenty of existing approaches ([2,3,4,5] for e.g.) to solve it. Thus, the paper should discuss more on the relationship to such works. The heavy reliance on optimization with unlabeled data fundamentally alters the problem setting compared to previous merging methods that operate without any optimization. This makes direct comparisons difficult and raises questions about the method's practical applicability in scenarios where unlabeled data is scarce or unavailable. The paper needs to more thoroughly discuss the relationship to existing multi-task learning and distillation approaches, which also leverage unlabeled data for optimization.
4. There is a concern about the computational/memory inefficiency in the optimization phase particularly when the size of models to be merged increases, because the knowledge distillation part involves large matrices. Since model merging is typically used with a low-end GPU, the proposed approach may be not promising. The computational and memory demands of the knowledge distillation process, especially when dealing with large models, are a significant concern. The need to store and process large intermediate feature maps during distillation can make the method impractical for resource-constrained environments, which is a common use case for model merging.
5. The number of optimized parameters reported in Table 3,4,5 may be (possibly intentionally) too misleading. It apparently suggests that the proposed method is more than 10x efficient compared to the vanilla knowledge distillation, but the actual time for merging reported in Table 6 of Appendix shows this is not the case. Rather, the proposed method seems more than 2x inefficient, possibly due to the above weakness. The presentation of the number of optimized parameters is misleading, as it does not accurately reflect the true computational cost of the proposed method. The actual time for merging, as shown in the appendix, indicates that the method is significantly more computationally expensive than suggested by the parameter count, raising concerns about the practical efficiency of the approach.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the method of merging large transformers trained on different tasks from distinct initializations, deviating from the traditional setting where models are required to originate from the same checkpoint. The authors build upon and enhance the concept of folding from Zipit![1], successfully extending its application to transformers, thereby broadening its original scope. Furthermore, the authors employ data augmentation to address the constraints of limited data settings. This approach has achieved remarkable results on models such as MLPs and ViTs.

### Strengths
1. Expanding the scope of model merging is a highly significant direction.
2. Very detailed introduction and guidance.
3. Thorough ablation studies and large-scale experimental results and discussions.

### Weaknesses
1. Concerns about application scenarios: While the paper takes a step forward in expanding the scope of model merging, it does not significantly enhance the applicability of model merging scenarios. The target scenario (same model architecture with identical pre-training data but different initialization, followed by fine-tuning on different tasks) is not common in practice. This setup, while interesting from a research perspective, does not address the more prevalent use case of merging models fine-tuned from the same pre-trained checkpoint, limiting its immediate practical impact.
2. I noticed that data augmentation techniques are also used and discussed in Zipit. I suggest the authors address this point when discussing the connections with Zipit, highlighting similarities and differences in the methods used. Specifically, it would be beneficial to clarify whether the data augmentation strategies employed are identical, similar, or distinct from those used in Zipit, and how these choices impact the merging performance. A more detailed comparison of the augmentation techniques and their effects on the final merged model is needed.

### Questions
1. There is not much discussion about the next steps in the paper. What are the authors' thoughts on merging truly similar architectures but trained entirely from scratch on different datasets?
2. I am a little curious about the potential effects if the method were applied to the more common setting we have now (originating from the same checkpoint, fine-tuning on different tasks).

Typos:
Table 22, last row.

[1] ZIPIT! MERGING MODELS FROM DIFFERENT TASKS without Training

### Soundness
3

### Presentation
3

### Contribution
3
