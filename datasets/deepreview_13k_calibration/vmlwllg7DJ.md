# GrowLength: Accelerating LLMs Pretraining by Progressively Growing Training Length

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
The evolving sophistication and intricacies of Large Language Models (LLMs) yield unprecedented advancements, yet they simultaneously demand considerable computational resources and incur significant costs. To alleviate these challenges, this paper introduces a novel, simple, and effective method named ``\growlength'' to accelerate the pretraining process of LLMs. Our method progressively increases the training length throughout the pretraining phase, thereby mitigating computational costs and enhancing efficiency. For instance, it begins with a sequence length of 128 and progressively extends to 4096. This approach enables models to process a larger number of tokens within limited time frames, potentially boosting their performance. In other words, the efficiency gain is derived from training with shorter sequences optimizing the utilization of resources. Our extensive experiments with various state-of-the-art LLMs have revealed that models trained using our method not only converge more swiftly but also exhibit superior performance metrics compared to those trained with existing methods. Furthermore, our method for LLMs pretraining acceleration does not require any additional engineering efforts, making it a practical solution in the realm of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes GrowLength, a pre-training strategy to progressively increase the sequence length of the training data in stages. The authors propose to use position interpolation or extrapolation to use the trained model to unseen sequence lengths. The models use relative position embeddings (ROPE) and the authors discuss the utility of the embeddings for such progressive training. On multiple model scales, the authors show the efficacy of their method with training time compared to baseline training.

### Strengths
The main strength of the paper lies in its easy-to-understand logic to use progressive sequence length training with ROPE embeddings. The authors take insights from position interpolation and extrapolation works and ROPE embeddings to develop the GrowLength algorithm. Furthermore, the authors clearly point out the memory and training time benefits of different input sequence lengths. Furthermore, with ablations, the authors show the algorithm's limited dependence on different progressive training schedules.

### Weaknesses
There are a few details that are unclear from the paper's presentation.

(a) How do the authors transition between stages? Do the authors use position interpolation or extrapolation to provide a smooth transition when the sequence length increases? Furthermore, a comparison study to a different position embedding would highlight the importance of ROPE embeddings for a smooth transition across the stages.

(b) How many sequence batches do the authors use for each stage of training? Is it proportionally set to the sequence length at each stage? 

(c) Related to my second question, if the batch sizes have been changed at each stage, have the hyperparameters (Learning rate, batch size, etc.) of the baseline experiments been optimally tuned for fair comparisons?

(d) How does the improvement in perplexity relate to improvements in downstream performance? Any fine-tuned or zero-shot performance will show the general efficacy of the proposed method.

There are multiple works on efficient training that haven't been mentioned by the authors. It would be good to incorporate them to give the readers a complete view of the literature.

(1) Stacking and Layerdrop: This is a procedure to progressively increase or drop the size of the model across multiple dimensions during the course of training. [1, 2, 3, 4]. [4] had also proposed a GrowLength algorithm to incorporate into their Stacking framework.

(2) Optimization algorithm: This is a line of work that attempts to tweak the optimization algorithm to get faster pre-training. [5, 6]

### Questions
Please see my questions in my previous section.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to progressively increase input length to accelerate training. By utilizing the functionality of RoPE embedding, the longer sequence is able to adapt the model trained with shorter sequences.

### Strengths
- Good writing;
- The experiments show that progressively growing sequence length can accelerate the training process.

### Weaknesses
 - My largest concern lies in the validation of the experiment. The model is trained around 20000s (5.56h) at most, which is insufficient to validate the pretraining process since the model is far from convergence. A 160M parameter LLM typically requires several days to converge on 16 V100s, and the reported training time is orders of magnitude shorter than what is generally accepted for pretraining large language models. This raises serious doubts about the conclusions drawn from these experiments. The authors need to demonstrate that the model has reached a reasonable level of convergence to support their claims about training acceleration.
- A shorter sequence surely leads to a smaller computation complexity. Therefore, this insight is not really original. The core idea of reducing training time by using shorter sequences is well-established, and the paper does not adequately highlight the novelty of their approach beyond this basic principle. The paper needs to clearly articulate what unique contribution it makes beyond the obvious benefit of reduced computation with shorter sequences.
- Typos:
	- "while GrowLength-1 is trained with more tokens." -> while GrowLength-2 is trained with more tokens;
	- Lacks the conference of [1] in the paper;
	- etc.

### Questions
- In Sec 4.4, how many extra tokens are used by GrowLength-2?

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a simple but effective training strategy for LLMs, namely GrowLength, which changes the data loader, by progressively feeding longer training data during the pre-training phase. In this way, the model training process can be accelerated. GrowLength is motivated by the context windows extension methods for fine-tuning, which indicates that model trained with shorter sequence can also benefit tasks with longer inputs, and employ the direct positional extrapolation for implementation. Many experiments are presented in this paper, showing that the motivation is reasonable, and the proposed GrowLength is effective.

### Strengths
- This paper targets a little-explored aspect for LLMs, which is adjusting training data to accelerate training process. Since the training costs for LLMs are huge, I think this paper targets a very important research question.
- The presentation in this paper is clear. This paper is well-written, and results are clearly demonstrated with figures or tables.
- Plenty of experiments in this paper make the proposed idea convincing. The motivation of the paper comes from some experimental observations, regarding the computational complexity of LLMs with varying lengths of sequences. And the proposed GrowLength is evaluated and analyzed from multiple aspects, including training time, training loss, model size, and so on.

### Weaknesses
 - Some work related with general language processing but not LLMs is not discussed/compared, such as Curriculum Learning for Natural Language Understanding (https://aclanthology.org/2020.acl-main.542.pdf ). The proposed method is quite related to curriculum learning, where an easy-to-difficult curriculum is arranged for model training. This paper also has a baseline, which uses question length/paragraph length as difficulty metrics.
- How to determine the growing context window size during training (like 128, 256, 512, …) is not rigorously studies. Will this exponential growth be too fast, especially for the latter stage, or even longer sequence (e.g., 1B tokens)? And maybe direct positional extrapolation will not work well when growing too fast. The paper lacks a detailed analysis of the impact of different growth schedules on the final model performance. Specifically, it does not explore the trade-offs between faster growth (potentially leading to instability) and slower growth (potentially leading to longer training times). The choice of an exponential growth schedule is not justified with empirical evidence or theoretical analysis, and the potential for diminishing returns or negative transfer at later stages is not addressed.
- The unique challenge when applying content window extension to pretraining stage is not very clear. It seems that simply using the technique proposed for fine-tuning also works well. The paper does not clearly articulate why extending the context window during pre-training presents different challenges or opportunities compared to fine-tuning. The method seems to directly apply techniques from fine-tuning without considering the specific characteristics of pre-training, such as the scale of the dataset and the computational cost. It would be beneficial to discuss the differences in data distribution, optimization landscape, and resource constraints between pre-training and fine-tuning, and how these differences might impact the effectiveness of the proposed method.
- No final testing results are presented. Although this paper is working on optimization but not generalization. But final performance on testing set of various tasks is the thing that matters a lot. Besides loss, these results should also be included and analyzed.

### Questions
- Will this method be sensitive to the length distribution of the training data? If the pre-training dataset has few samples with short sequences, will GrowLength still be effective?
- The first observation presented before section 3 is not very rigor. Context window extension methods are proposed because LLMs are pre-trained with a fixed context window, but we would like to apply them to tasks with longer sequences. So, these methods just tell us that context length can be extended, but not say “trained with shorter sequence lengths has proven to be more effective than training with long sequences”. Not sure what the author is trying to say here.
- What LLM is used in all experiments? I am curious about how this method works in experiments when applied to LLMs which already have some techniques for accelerating and handling long context, such as GQA in llama2 and FastAttention, given that the authors have explained that they are orthogonal, but experiments are more convincing here.
- Table 1 2 3 might be better presented with figures.
- Typos: At the end of the 3rd line in Sec. 4.4, the full stop should be removed. Also the final sentence in this paragraph, the latter one should be GrowLength-2.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
> **TL;DR:** The proposed GrowLength method progressively increases the LLM training length throughout the pre-training phase, thereby mitigating computational costs and enhancing efficiency. However, I find the paper lacking comparison to the common BERT two phase pre-training approach which increases the context window in the second phase. Addressing my concerns and questions would improve my score, specifically W.1 and W.2.

The paper proposes the GrowLength method to reduce the computational cost of training LLMs. The high computational cost of LLMs is an ongoing challenge with plenty of recent research discoveries. Contrary to the fixed sequence length in the pretraining, the proposed GrowLength method utilizes a dynamic, progressively growing training sentence length. The superiority of this method lies in its adaptability and its capacity to significantly optimize the utilization of computational resources, enabling models to process more tokens in a constrained time frame.

### Strengths
* **S.1.** The proposed GrowLength algorithm tackles an important problem in the computational costs of training LLMs.
* **S.2.** The experiments show that the GrowLength method outperforms the common constant context length approach.
* **S.3.** The paper provides results on models of different sizes.

### Weaknesses
 * **W.1.** The paper lacks comparison to the BERT [1] pre-training, which used a two-step pre-trianing approach with a growing context window length.
* **W.2.** The figures are confusing with different arrows pointing at the lines with same colors (Figure 3 & 5).
* **W.3.** The experiments are conducted on a single neural architecture and the provided architecture sizes are considerably small compared to existing LLMs. Specifically, the paper does not address how the proposed method would scale to models with billions of parameters, which is a critical consideration for practical applications of large language models.

### Questions
* **Q.1.** Where are GrowLength-1 and GrowLength-2 defined?
* **Q.2.** How would the GrowLength method work with substantially larger model 7B+?
* **Q.3.** How would the GrowLength method work with substantially context windows?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
