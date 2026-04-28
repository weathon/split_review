# GEPCode: A Context-Aware 1M-Parameters Graph-Based Language Model for Source Code

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
The pursuit of optimal conditions for software execution poses a complex challenge. This task can be automated by harnessing the structured nature of programming languages, especially from compiler intermediate representations of code (IR). The manipulation of source code using Large Language Models (LLMs) is a thriving area of study in Natural Language Processing (NLP) literature. However, in this study we illustrate how we can circumvent the need for exceedingly large models by employing domain-specific language models. These models have a reduced number of parameters but retain the ability to capture the relationships within source code elements. We introduce GEPCode, a graph neural network designed to model IR with the flexibility to adapt to new tasks. This flexibility is obtained through special "meta" nodes, that allow for the representation of additional task-dependent contextual information. Pre-training is performed by solving node and graph-level tasks, resulting in a general language model. After a fine-tuning phase on two downstream tasks, Device Mapping and Algorithm Classification, we achieve average accuracy results of 88.9% (NVIDIA) and 92.3% (AMD) for the former and 97.2% for the latter. Comparing our methodology with state-of-the-art models trained from scratch, our results are similar or better, yet providing a more flexible model. Moreover, we achieve similar accuracy results in downstream tasks compared to state-of-the-art pre-trained language models based on Transformers, while utilizing 100 times fewer parameters.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces GEPCode, a graph-based, efficient, pre-trained, context-aware LM of graph representations of source code. The proposed approach expands upon ProGraML and Perfograph. GEPCode expresses LLMV-IR code samples as graphs, where nodes are token within a vocabulary of LLVM-IR elements, and edges are directed and represent dependencies between the elements of code. GEPCode is pretrained using synth-compilable subset of the Exebench dataset, using three tasks - attribute masking, meta prediction, and contrastive learning. For downstrem tasks, GEPCode is evaluated on device mapping and algorithm classification. Experimental results demonstrate that GEPCode is able to bridge the gap between the efficiency of task specific architectures and the generality of larger LMs, while using a limited number of parameters.

### Strengths
- Overall the paper is written well. The motivation behind the model choice is sound.
- The pretraining objectives that include three tasks are effective.
- Experiment results show the value of the proposed method.

### Weaknesses
 - The biggest weakness of the work is the novelty. In a nutshell, it is a paper that is using GNN for some specific code tasks. GNN was previously explored for coding tasks, however, with the emergence of LLMs, the focus has shifted. In this paper, authors emphasized on compact LMs, but why GNN is the solution, it is not clear.
- The paper could use more software engineering tasks for evaluation. In the analysis part of the work, there is not much critical thinking paid by the authors. Straight-forward main results and a piece of ablation study - that's it. Moreover, I didn't understand the baselines used in comparison.

### Questions
- Why GNN is used as a solution to build compact LMs in this work? What is the motivation.
- The paper uses LLMV-IR representation of code; in that case, is the proposed method scalable?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces GEPCode, a novel approach using a Graph Neural Network to model compiler intermediate representations of code with the adaptability to accommodate new tasks. The model is first pre-trained as a general-purpose language model, then fine-tuned on downstream tasks, achieving results comparable to state-of-the-art models trained from scratch. Additionally, GEPCode performs similarly to leading pre-trained Transformer-based language models while requiring fewer parameters, offering a more flexible and efficient solution.

### Strengths
The problem statement addressed in this paper is worth solving as there is demand for smaller, efficient and flexible models in this domain.

### Weaknesses
(1) Typically, fine-tuning is performed for 1 to 10 epochs. Here, fine-tuning for both downstream tasks was run for 100 epochs, which could have led to overfitting. The risk of overfitting is particularly high given the relatively small size of some datasets used for fine-tuning. Furthermore, the paper does not include any analysis of the training and validation loss curves to demonstrate that the model is not overfitting. Without this analysis, it is difficult to assess the generalization capability of the model.

(2) The accuracy of fine-tuned GEPCode on downstream tasks is compared against pre-trained transformer-based language models. A comparison with fine-tuned transformer-based language models for our downstream tasks would have been ideal. This comparison is crucial to understand the true potential of GEPCode. Comparing against pre-trained models only shows that GEPCode is competitive with a baseline, but not necessarily with the state-of-the-art after fine-tuning.

### Questions
Please clarify if IRGen is a non-transformer-based pre-trained language model that performs better than GEPCode.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes GEPCode, a Graph Neural Network (GNN) to embed compiler intermediate representation of source code. GEPCode is pre-trained on 1.3M graphs constructed from source code for three objectives: (1) Attribute Masking, (2) Meta Prediction, and (3) Contrastive Learning. The resulting model is then fine-tuned for two downstream tasks respectively: (1) Device Mapping and (2) Algorithm Classification. Evaluation shows that GEPCode, which has only 1M parameters, achieves comparable performance with respect to much larger pre-trained transformer models, highlighting its efficiency.

### Strengths
* While previous works have approached the same problem with graph representations, GEPCode is the first to *pre-train* an GNN for intermediate representation, and proposed the three new objectives for pre-training.
* The proposed method is compared against a comprehensive list of baseline methods. All experiments are repeated 5 times for reliability.
* The paper is written clearly.

### Weaknesses
 * The proposed method does not show a clear advantage over Perfograph which performs better on DevMap with an even smaller model size, and does not require pre-training.
* It is highlighted that GEPCode is more parameter-efficient than pre-trained transformers. I do not think this is a well-established advantage of the proposed method unless it can be demonstrated that GEPCode outperforms the SOTA pre-trained transformer of the same model size. The comparison should be made against a transformer model with a similar number of parameters, not just a general statement about parameter efficiency.
* Regarding efficiency, I'm not sure about the practical benefit of reducing the inference time from around 100ms (with CodeT5 or other transformers) to 23ms (with GEPCode), at the cost of accuracy degradation. Those transformers are already pretty small and fast, whose inference latency should be acceptable for DevMap and algorithm classification that are considered in evaluation. The paper needs to justify the trade-off between accuracy and inference speed more clearly, especially since the tasks are not latency-critical.
* The baseline transformer models are mostly trained on multilingual programming language data, while GEPCode is trained on IR which is a single language. Is it possible that a monolingual transformer model trained only on the target language for the evaluation task would perform better, and thus the baseline numbers are underestimated? This is a significant concern, as it's not an apples-to-apples comparison. The authors should include a monolingual transformer baseline trained on the same IR data to ensure a fair evaluation.

### Questions
* A transformer model over flattened source code is naturally a GNN over fully connected graphs. It would be interesting to study how it performs to directly pre-train a transformer model over the same data with the same objectives.
* L292 is confusing to me. Is the "normalized property value" in META edges the same as $m$ in eq.6? If that's the case, isn't the training objective already known from the input?

### Soundness
2

### Presentation
3

### Contribution
2
