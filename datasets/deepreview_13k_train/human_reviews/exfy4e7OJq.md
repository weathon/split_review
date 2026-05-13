# Learning Towards Emergence: Paving the Way to Induce Emergence by Inhibiting Monosemantic Neurons on Pre-trained Models

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Emergence, the phenomenon of a rapid performance increase once the model scale reaches a threshold, has achieved widespread attention recently. The literature has observed that monosemantic neurons in neural networks gradually diminish as the model scale increases. Subsequently, *Learning From Emergence* is proposed to actively inhibit monosemantic neurons in relatively small neural networks (e.g., BERT and Swin-Transformer) for promoting model performance with fine-tuning. However, to ultimately achieve emergence, it is demanding to support the monosemantic neuron inhibition in the pretraining phase of large-scale models. Thus, this work further pushes the boundary of this research direction to be *Learning Towards Emergence (L2E)* and enables the training and validating of the impact of inhibiting monosemantic neurons on larger pre-trained neural networks (e.g., Pythia-70M, 410M, and 2.8B). More specifically, to bridge the gap in current research, we first conduct experiments on models of various scales (up to 6.9B) to validate the monosemantic ideas. Then, we present a novel method L2E to address the inefficient monosemantic neuron retrieval and ineffective monosemantic neuron inhibition when existing methods are applied in the pretraining phase of large-scale models. It employs an adjustable thresholding technique for efficient neuron retrieval, incorporates a False Killing Rate metric to assess inhibition effects, and proposes a regularization-style inhibition approach, which addresses the limitations of previous approaches in both efficiency and effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This authors conduct extensive analysis on monosemanticity. They further upgrade previous methods with more carefully determined number of inhibited neurons based on False Killing Rate, a moving threshold for global inhibition with better efficiency, and a regularization term for models in the early pre-training stage. The proposed method surpasses MEmeL and the backbone model in both efficiency and effectiveness.

### Strengths
1. The paper is well organized and is easy to follow.
2. The paper includes a thorough overview of the background and development of prior arts.
3. The authors provide interesting analysis on monosemantic neurons, and extend the experiments to relatively larger models. The insights can be useful to works in this direction.

### Weaknesses
1.The paper's experimental scope falls significantly short of the scale where emergence typically occurs. Current observations suggest that dramatic emergence phenomena primarily manifest in models around 70B parameters or larger, where there's a clear performance gap compared to smaller models. By limiting their analysis to models up to 6.9B parameters, the study misses the most critical scale range where emergence actually happens. This substantially weakens their conclusions about emergence and raises questions about the practical applicability of their findings to truly large-scale models. The absence of experiments at the scale where emergent behavior is most pronounced makes it difficult to ascertain whether the observed effects of inhibiting monosemantic neurons are truly linked to the emergence of advanced capabilities, or simply a consequence of improved training dynamics within smaller models.

2.The research is exclusively conducted on the Pythia model family, and the results are heavily dependent on the quality of feature datasets. For a study claiming to understand fundamental properties of large language models, this narrow focus is concerning. A more comprehensive analysis should include widely-used open-source models like Llama, BLOOM, or Falcon, which have different architectures and training approaches. This would help validate whether their findings about monosemantic neurons are truly general properties or just specific to Pythia models. The reliance on a single model family introduces a significant risk of overfitting to the specific characteristics of Pythia, potentially limiting the generalizability of the findings to other model architectures and training paradigms. Furthermore, the feature datasets used to identify monosemantic neurons might be biased or incomplete, which could lead to inaccurate conclusions about the role of these neurons in model behavior.

3.Without analyzing mainstream models, the paper's conclusions remain largely theoretical and potentially disconnected from practical reality. While acknowledging the challenges of training large-scale models, the authors could have conducted analysis and interpretation on existing pre-trained models. This would have provided valuable validation of their hypotheses and strengthened their arguments about the relationship between monosemantic neurons and emergence. The lack of such analysis leaves a significant gap between their theoretical framework and real-world applications. The absence of empirical validation on established models makes it difficult to assess the practical utility of the proposed method and its potential impact on real-world applications. The study's conclusions, therefore, remain largely speculative, without concrete evidence of their relevance to the broader landscape of large language models.

### Questions
1. Can this method be generalized to other domains and other benchmarks?
2. From Figure 6, the optimal percentage seems to be 1%. From Table 4, neither 1% nor 2% achieves consistently better performance (not to mention significance). Is there a more robust way for this percentage selection? 
3. Will the authors add more analysis on the relationship between the proposed method and "emergence"?

### Soundness
2

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
This paper investigates the relationship between model scaling and monosemantic neurons, introducing a novel method called Learning Towards Emergence (L2E). The key observation driving this research is that larger language models tend to exhibit fewer monosemantic neurons - neurons that form one-to-one mappings with interpretable features. Building on this insight, the authors develop L2E to actively inhibit monosemantic neurons during the pre-training phase of large models. The method's effectiveness was validated on Pythia models ranging from 70M to 2.8B parameters. Through comprehensive experiments, they demonstrate that inhibiting monosemantic neurons can enhance model performance across multiple downstream tasks. A particularly significant contribution is their efficient implementation using adjustable thresholds, which addresses the computational challenges in scaling to larger models. The authors also introduce the False Killing Rate metric to quantify inhibition effects. While the study is currently limited to the Pythia model family, it provides valuable insights into neural network organization at scale and suggests a potential mechanism for understanding emergence phenomena in large language models. The findings open new avenues for improving pre-training strategies, though further research is needed to fully validate the connection to emergence.

### Strengths
1.The study of emergence in large language models is a compelling and significant research direction. Understanding why and how models suddenly exhibit enhanced capabilities beyond simple scaling laws provides crucial insights into the nature of large language models. This kind of research is fundamental for both advancing our theoretical understanding and guiding practical model development.

2.This paper provides fresh perspectives and introduces novel tools for understanding emergence, including the False Killing Rate metric and adjustable thresholding techniques. By linking monosemantic neurons to model performance, it offers a new angle for analyzing how neural networks organize and process information as they scale up, while also providing practical methods to enhance model capabilities.

3.The experimental results are comprehensive and convincing, demonstrating consistent performance improvements across various model scales (70M to 2.8B) and downstream tasks. The proposed L2E method not only shows effectiveness in improving model performance but also addresses efficiency challenges in large-scale implementation, making it practically viable for real-world applications.

### Weaknesses
1.The paper's experimental scope falls significantly short of the scale where emergence typically occurs. Current observations suggest that dramatic emergence phenomena primarily manifest in models around 70B parameters or larger, where there's a clear performance gap compared to smaller models. By limiting their analysis to models up to 6.9B parameters, the study misses the most critical scale range where emergence actually happens. This substantially weakens their conclusions about emergence and raises questions about the practical applicability of their findings to truly large-scale models.

2.The research is exclusively conducted on the Pythia model family, and the results are heavily dependent on the quality of feature datasets. For a study claiming to understand fundamental properties of large language models, this narrow focus is concerning. A more comprehensive analysis should include widely-used open-source models like Llama, BLOOM, or Falcon, which have different architectures and training approaches. This would help validate whether their findings about monosemantic neurons are truly general properties or just specific to Pythia models.

3.Without analyzing mainstream models, the paper's conclusions remain largely theoretical and potentially disconnected from practical reality. While acknowledging the challenges of training large-scale models, the authors could have conducted analysis and interpretation on existing pre-trained models. This would have provided valuable validation of their hypotheses and strengthened their arguments about the relationship between monosemantic neurons and emergence. The lack of such analysis leaves a significant gap between their theoretical framework and real-world applications.

### Questions
1. How do you define and measure emergence more precisely? The paper suggests a connection between monosemantic neurons and emergence, but is this correlation or causation?

2. What is the theoretical justification for why reducing monosemantic neurons would lead to better model performance?

3. Why choose 2% as the optimal threshold for neuron inhibition? Could this vary with model size or architecture?

4. How robust is the False Killing Rate metric across different types of models and tasks?

5. Could the efficiency improvements in L2E potentially sacrifice some accuracy in identifying monosemantic neurons?

6. Given that emergence typically occurs in models around 70B parameters, how relevant are the findings from much smaller models (up to 6.9B)?

7. Why focus exclusively on the Pythia model family? How would the results generalize to other architectures?

8. What specific characteristics of the feature datasets might affect the reliability of the results?

9. Could this method be applied to existing pre-trained models without retraining?

10. How would this approach scale to truly large models where emergence is actually observed?

11. What are the computational costs and practical challenges of implementing L2E in production environments?

12. How might this work extend to understanding other emergent properties in large language models?

13. Could this approach be adapted for other types of neural networks beyond language models?

14. What additional metrics or methods could help validate the connection between monosemantic neurons and model performance?

### Soundness
2

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
3

### Summary
The manuscript presents an approach termed Learning Towards Emergence (L2E), which aims to enhance the performance of large pre-trained neural networks by inhibiting monosemantic neurons. The authors argue that as model scale increases, the presence of monosemantic neurons diminishes, potentially contributing to the phenomenon of emergence. L2E employs the FKR, an efficient retrieval method, and proposes a regularization-style inhibition approach. The experiments demonstrate the effectiveness of L2E in improving model performance during pre-training.

### Strengths
* The introduction and the related works are clear.
* The motivation is straightforward that previous methods for inhibiting monosemantic neurons lack efficiency and experimental evidence.

### Weaknesses
* The study is limited to Pythia models, and it is unclear how well L2E would perform on other architectures or datasets.
* Table 1 lacks the comparison results of related works, such as MEmeL.
* While the introduction highlights the potential of suppressing monosemantic neurons to promote emergence, the experiments presented in this paper fall short of validating this hypothesis.

### Questions
1. The y-axes in Table 1(a) and 1(b) are inconsistent. It is unclear why the minimum value in Table 1(a) is 2 rather than -2.
2. The authors claim that the neurons in Table 1(b) are polysemantic, yet the data suggests that they are inactive to all inputs.

### Soundness
2

### Presentation
2

### Contribution
2
