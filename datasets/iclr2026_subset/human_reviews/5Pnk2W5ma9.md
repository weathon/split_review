## Human Reviewer 1

### Summary
Traditional NAS surrogate models predict architecture performance within a fixed search space, which ties them to a specific architecture representation with constrained topologies. To enable research that spans multiple NAS search spaces and to improve generalization across them, the authors unify architectures from different NAS benchmarks in ONNX format and build ONNX-Bench. To learn from these representations, the authors design ONNX-Net, an LLM-based predictor that treats ONNX files as text. The experiments demonstrate the generalization ability of ONNX-Net, and the ablation studies further support the effectiveness of the surrogate’s design.

### Strengths
1. The paper unifies search spaces from different NAS works using ONNX. This allows surrogate models to predict performance across search spaces and provides the community with a valuable dataset.

2. The paper is well structured and easy to follow.  
   - It explains how ONNX-Bench is built, shows the similarities and differences between the search spaces, and displays the text form of the ONNX files for easy understanding.  
   - It provides ablation experiments for the text encoding and shows how each component contributes to training and prediction.

3. Generalization is a key problem for surrogate models. The authors validate ONNX-Net in three ways:  
   - Cross search space in subsection 5.1.  
   - Zero-shot transfer in subsection 5.2.  
   - Cross dataset in subsection 5.3.  
   These experiments collectively demonstrate that ONNX-Net achieves well-generalized performance across different search spaces and datasets.

### Weaknesses
1. Subsection 5.1 does not compare with other baselines. It is hard to judge how well the proposed surrogate model is in that setting.

2. Table 3 compares zero-shot results only for models trained on 50k samples from NAS-Bench-101 and evaluated on NAS-Bench-201. Readers may want to see zero-shot comparisons for more search spaces ( such as hNAS-Bench-201, NAS-Bench-301 ), since ONNX-Bench collects many spaces from NAS Benchmarks.

3. While the paper demonstrates strong cross-space and zero-shot results, several potential causes behind the OOD behaviors remain under-analyzed:
   - In the all-but-one search space setting, why do some target spaces show weaker OOD performance? Could this be caused by differences in operator op_type across spaces?
  
   - The ablation shows that Input information and Parameter information clearly contribute to performance. Does this imply that the model relies mainly on information that is independent of operator names in unseen spaces, such as input shapes or operator parameters?
  
   - Since different NAS benchmarks have different node number distributions, could OOD prediction performance also be affected by such node scales?

### Questions
1. ONNX-Net is evaluated with an ONNX-based representation, while other baselines are evaluated with their own representations. Since both the input representation and the surrogate model architecture differ, can this comparison be regarded as fair and meaningful?

2. In subsection 5.2, the correlation after leaving out NATS-Bench is 0.390, while training on all is 0.788. Does this large gap indicate poor generalization?

3. Are the issues listed in Weaknesses 3 reasonable and important? If they are indeed important, could the authors provide more explanations or discussions on these points?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper is about designing a generalizable predictor for Neural Architecture Search (NAS) using the Open Neural Network eXchange (ONNX) representation standard, and then using a Large Language Model (LLM) to perform the predictions. The name for this framework is ONNX-Net - consisting of ONNX-Bench, the neural networks in (representation, accuracy) pairs, on CIFAR-10, and ONNX-Net, the LLM-based predictor. ONNX-Net is evaluated on some unseen NAS tasks.

### Strengths
The strongest contribution of this paper is representing neural network architectures using the ONNX standard. 
This is probably the best method to do so as ONNX is a platform for saving a neural architecture on one device, then deploying on another, e.g., for mobile deployment applications.

Further, the reviewer appreciates the operation distribution calculations shown in section 3, e.g., the JSD calculation and Fig. 3. This provides some necessary insights on the distributions of different search spaces. 

Extensive experiments are performed measuring the Kendall's Tau and Spearman Rho across different benchmarks, in the transfer context, and on unseen tasks.

### Weaknesses
The first weakness of this work is that it is primarily on CIFAR-10 which is an incredibly worn-out benchmark at this stage and unlikely to be a good representative of how an architecture would perform on a higher-resolution task. For instance, NAS-Bench-201 [1] also consider CIFAR-100 and downsampled ImageNet; TransNAS-Bench [2] consider other tasks besides image classification and also provide macro search space architectures; AIO-P [3] only consider macro search space architectures for high-resolution tasks as well. While this work considers hierarchical search spaces as well as cell-based, it fails to substantially reach beyond CIFAR-10 and low-resolution tasks.

Second, the characterization of GENNAPE [4] is not accurate, since GENNAPE is not limited to cell-based architectures, but uses the same representation as [3] which covers macro-search space architectures for cross-task prediction. The description the authors use in the paper is better suited to CDP [5], which is one of the earliest iterations of a generalizable predictor but also confined to cell-based architectures.

Third, the use of an LLM in this paper to predict performance seems like a large leap but doesn't provide sufficient pay-off, given the results, which while not lackluster, are mostly incremental. The reviewer would note that there have been several advances in low-cost predictor design to take advantage of the graph structure [6, 7] that this paper either does not seem to be aware of or simply discards.

### Questions
Two questions:
- Can the authors provide further comparison with flow-based [6] predictor models as well as causal predictor models [7]? This would help to better justify the use of an LLM.
- L038: "Recently, researchers have begun to focus on more expressive search spaces that enable the discovery of more diverse and innovative architectures". There is more work in this field than the authors lead on. Are you able to provide some revised/further commentary/dialogue/work on these efforts?

References:

[1] Dong, Xuanyi, and Yi Yang. "Nas-bench-201: Extending the scope of reproducible neural architecture search." arXiv preprint arXiv:2001.00326 (2020).

[2] Duan, Yawen, et al. "Transnas-bench-101: Improving transferability and generalizability of cross-task neural architecture search." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2021.

[3] Mills, Keith G., et al. "Aio-p: Expanding neural performance predictors beyond image classification." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 8. 2023.

[4] Mills, Keith G., et al. "Gennape: Towards generalized neural architecture performance estimators." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 8. 2023.

[5] Liu, Yuqiao, et al. "Bridge the gap between architecture spaces via a cross-domain predictor." Advances in Neural Information Processing Systems 35 (2022): 13355-13366.

[6] Hwang, Dongyeong, et al. "Flowerformer: Empowering neural architecture encoding using a flow-aware graph transformer." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

[7] Ji, Han, et al. "CARL: Causality-guided Architecture Representation Learning for an Interpretable Performance Predictor." arXiv preprint arXiv:2506.04001 (2025).

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 3

### Summary
This paper proposes ONNX-Net, a universal surrogate model for neural architecture performance prediction that operates across diverse NAS search spaces. It builds ONNX-Bench, a unified benchmark of 600k architectures in ONNX format, and converts each network into text for LLM-based prediction.

### Strengths
The paper introduces ONNX-Bench, which collects architectures from multiple search spaces into a unified ONNX format. The dataset may benefit further research.
The paper explored the ONNX-to-text encoding method that applies to arbitrary architectures.

### Weaknesses
The motivation for using the text encoding method is unclear. The authors should further clarify the differences and advantages of introducing text encoding compared to other possible approaches.
The authors argue that using Python code as an architectural representation could produce nonsensical or syntactically incorrect results. I believe the proposed ONNX approach in this paper faces a similar issue, and the authors may need to provide further clarification on the key difference.
I noticed that the authors report Kendall’s τ for some results (Table 2) but Spearman’s ρ for others (Table 3). They should either include both metrics for completeness or explain why different correlation measures are used.
The zero-shot transfer experiments are only conducted on NAS-Bench-101 and NAS-Bench-201, both of which are cell-based search spaces. The authors should also demonstrate the model’s generalization ability across different types of search spaces.

### Questions
In addition to the above, I also have a question: how do the authors view the relationship between the ONNX format and the encoded text? It seems that the ONNX-to-text process is essentially a simplification of the ONNX representation to fit the model’s input length. Therefore, can we consider ONNX merely as an intermediate format, and in fact, directly establish a search-space-to-text representation?

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 4

### Summary
This work mainly accomplished the representation of mainstream neural network architectures using the ONNX file format, which can be used for NAS research. It has more engineering value and lacks research innovation. In this standardisation process, the technical work also lacks sufficient validation. I suggest the authors to focus just one point, ONNX format or LLM refining on ONNX, with more in-depth research.

### Strengths
This work explores the possibility of using ONNX for the unified conversion of network architectures, which provides some inspiration for subsequent research.

### Weaknesses
1. The focus of this work is not clear enough. Specifically, is the theme of this paper the unified handling of network representations in the ONNX file format, or is it verifying LLM performance based on this? In either case, the research content is insufficient. 

2. For work involving the design and release of a unified representation format, the key point should be that the unified format does not alter the performance of existing models. This is essential to verify the effectiveness and reliability of a compromise unified representation format. However, this paper indicates that the performance of the proxy model changes at this point, which seems abnormal. It is recommended that the authors consider comparing the performance of the same proxy model prediction method under the proposed ONNX format and the original format, and then further demonstrate it.

### Questions
I have one big concern. The author claims that 'a surrogate model using the novel text-based encoding trained on ONNX-Bench achieves competitive performance, especially for zero-shot transferability with minimal pretraining.' The question here is, compared with existing work, ONNX-NET only differs in file format or network representation, so why does it lead to model performance improvement? If asked further, is it a general performance improvement or mainly targeted at zero-shot? In fact, I doubt this conclusion.

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
0

### Confidence
3