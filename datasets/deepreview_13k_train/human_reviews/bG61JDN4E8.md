# LANE: Label-Aware Noise Elimination for Fine-Grained Text Classification

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
We propose Label-Aware Noise Elimination (LANE), a new approach that improves the robustness of deep learning models in fine-grained text classification when trained under increased label noise. LANE leverages the semantic relations between classes and monitors the training dynamics of the model on each training example to dynamically lower the importance of training examples that may have noisy labels. We test the effectiveness of LANE in fine-grained text classification and benchmark our approach on a wide variety of datasets with various number of classes and various amounts of label noise. LANE considerably outperforms strong baselines on all datasets, obtaining significant improvements ranging from an average improvement of 2.4% in F1 on manually annotated datasets to a considerable average improvement of 4.5% F1 on datasets with injected noisy labels. We carry out comprehensive analyses of LANE and identify the key components that lead to its success.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the issue of noisy or mislabeled data in single-label text classification. The authors propose an approach that incorporates a label margin, considering semantic similarity between the assigned and predicted labels. This margin is applied to both cross-entropy loss and supervised contrastive loss, forming the training objective. Experimental results indicate that this method outperforms traditional baselines and LLMs with noisy in-context learning on noisy datasets.

### Strengths
1. The paper presents clear motivations for the work, specifically identifying limitations of prior methods, such as making samples less challenging and applying uniform penalties, which are well explained.
2. The proposed approach shows strong performance on noisy classification tasks, demonstrating robustness to label noise. The comparisons with existing LLMs add value, though they could be further refined.

### Weaknesses
Some essential details are unclear, making it challenging to fully assess the proposed method. While the high-level concept and rationale for the design choices are understandable, additional specifics are needed. For example, in line 208, the authors mention that the weighting network is trained according to Eq. (3), but the weighting network does not appear in this equation, leaving its connection to Eq. (3) ambiguous. Specifically, the mechanism by which the weighting network learns to predict semantic similarity is not well-defined. The paper lacks a clear explanation of how the network's parameters are updated to achieve this goal, and how this relates to the overall loss function. Furthermore, the connection between the output of the weighting network and the label-aware margin is not sufficiently detailed. It is unclear how the network's output is transformed into a weight that modulates the margin, and how this transformation ensures that semantically similar labels receive appropriate margin adjustments. Please refer to the questions below for further clarification.

Minor Comment:  
The comparison between few-shot LLMs and LANE may be somewhat biased since the LLMs rely only on in-context learning without fine-tuning on the target dataset. To make the comparison fairer, it would be helpful to include LLM performance in both noisy and noiseless scenarios.

### Questions
1. How is the weight of the "regular linear layer" in the weighting network obtained, and why is this network expected to predict the semantic similarity between the assigned label and the predicted label? I am unclear on its connection to Eq. (3).  
2. Could you provide insights on how this method could be extended to address multi-label classification tasks?  
3. In line 255, why is the average label-aware margin summed over M(x,y) instead of LM(x,y)?

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
4

### Summary
This paper presents LANE (Label-Aware Noise Elimination), a method that improves text classification by reducing the impact of noisy labels during training. Using class relationships and training patterns, LANE shows F1-score improvements of 2.4-4.5% across their datasets.
The work's novelty is limited, though. The core idea of weighting noisy samples has been well-explored across NLP and computer vision - from text classification to multi-label tasks, named entity recognition [1], and image segmentation. The evaluation is also restricted to cases with few labels, leaving questions about its effectiveness for problems with hundreds or thousands of classes.
Furthermore, the experimental is limited to BERT-based models, lacking comprehensive ablation studies across different model architectures.

[1] Named Entity Recognition with Small Strongly Labeled and Large Weakly Labeled Data

### Strengths
The analysis includes benchmarking against recent generative AI models using few-shot prompting, demonstrating that targeted classification methods remain valuable alongside emerging large language models

### Weaknesses
The work's novelty is limited, though. The core idea of weighting noisy samples has been well-explored across NLP and computer vision - from text classification to multi-label tasks, named entity recognition [1], and image segmentation. The evaluation is also restricted to cases with few labels, leaving questions about its effectiveness for problems with hundreds or thousands of classes.
Furthermore, the experimental is limited to BERT-based models, lacking comprehensive ablation studies across different model architectures.

The comparison with generative AI models lacks rigor in prompt optimization - the baseline performance could potentially be improved significantly through systematic prompt engineering or automated tuning frameworks like DSPy. This limitation undermines the fairness of the comparison.

### Questions
1. What are the key conceptual differences between LANE and previous noise-weighting methods in text classification and NER? The paper would benefit from a clearer positioning of its technical novelty.
2. The current evaluation focuses on tasks with limited label sets. How would LANE handle extreme classification scenarios with hundreds/thousands of labels, and what adaptations might be needed?
3. The experiments are currently BERT-centric. Could you discuss LANE's potential performance and compatibility with other architectures (T5, RoBERTa)? Is the semantic relationship modeling architecture-independent?
4. The GenAI baselines seem to use basic few-shot prompting. Have you considered using prompt optimization tools like DSPy to establish a more rigorous comparison? How might LANE's advantages compare against such optimized baselines?
5. Have you considered LLM instruction tuning, like tune the LLaMA-2/4 model?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, the authors pointed out the current limitation of area under margin (AUM)-based methods for mitigating label noise. Especially, they suggested the importance of inter-class semantic similarity (e.g., 'joy' is closer to 'happy' than 'fear'). To incorporate this characteristic, they proposed Label-Aware Noise Elimination (LANE) framework. LANE proposes the concept of label-aware margin and methods to mitigate the harmful effect of noisy label data. Their experiment on ten different fine-grained text classification datasets shows the effectiveness of LANE.

### Strengths
- The consideration of similarity between labels is interesting and can be meaningful for future studies for fine-grained classification.
- The empirical gain of LANE is considerable compared to other baselines. Furthermore, such gain is consistent, whereas other baselines sometimes have performance degradation.
- It should also be noted that the experiments also include datasets on news and scientific articles, implying that the proposed LANE is not limited to sentiment classification

### Weaknesses
I don't think there are any critical weaknesses in this paper. However, I believe that the paper should incorporate more discussion regarding the re-weighting scheme for mitigating noisy labels. For instance, Gao et al. suggested leveraging the concept of bi-level optimization for mitigating noisy labels from synthetic data. Building upon this, Zou et al. proposed a weighting function that does not require computationally expensive bi-level optimization.

### Questions
- Can you present any examples of similar labels in RCV1 and SciHTC datasets?
- Missing reference: Wang et al., Symmetric Cross Entropy for Robust Learning With Noisy Labels, ICCV 2019.
- Please ensure to cite the published version instead of preprints. For instance, "Understanding deep learning requires rethinking generalization" by Zhang et al. was published at ICLR 2017.
- Please use \citet and \citep in correct context.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new approach, Label-Aware Noise Elimination (LANE), aimed at improving the robustness of deep learning models under label noise in fine-grained text classification. LANE uses semantic relationships between classes and monitors training dynamics to lower the importance of noisy training examples. It is evaluated on various datasets and outperforms baseline methods.

### Strengths
The authors address a well-defined problem: the impact of label noise on fine-grained text classification tasks and demonstrates a clear improvement in performance across various datasets with different levels of noise. The idea of leveraging inter-class semantic relationships in noise reduction is an interesting contribution.

### Weaknesses
-The overall novelty of this paper is relatively modest, with the main focus being on weighting noisy labeled data. 

-Regarding the comparison with LLMs, the study used a 20% noise labeled data setup. However, the correctness of labels in few-shot learning isn't necessarily the key factor in making in-context learning effective. Therefore, introducing noisy labeled data into LLMs' few-shot examples may not hold significant value (refer to the paper Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?).

Overall, I don't believe this is a particularly strong paper, though I may reconsider my score after the rebuttal stage.

### Questions
1. Have there been any previous studies on weighting noisy labeled data? Besides using a weighting network for dynamic weighting, were any other weighting approaches explored?
2. How was the hyperparameter α in Equation (9) determined?
3. Why were ChatGPT and Llama2 chosen as the LLM baselines, rather than a more advanced model like GPT-4?

### Soundness
3

### Presentation
2

### Contribution
3
