# Efficient Bayesian DNN Compression through Sparse Quantized Sub-distributions

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
This paper presents a novel method that simultaneously achieves model pruning and low-bit quantization through Bayesian variational inference to effectively compress deep neural networks (DNNs) while suffering minimal performance degradation. 
Unlike previous approaches that treat pruning and quantization as separate, sequential tasks, our method explores a unified optimization space, enabling more efficient compression. 
By leveraging a spike-and-slab prior combined with Gaussian Mixture Models (GMM), we can achieve both network sparsity and low-bit representation. Experiments on CIFAR-10, CIFAR-100, and SQuAD datasets demonstrate that our approach achieves compression rates of up to 32x with less than a $1.3\\%$ accuracy loss on the CIFAR datasets and a 1.66 point decrease in F1 score on SQuAD. Additionally, we show that the Bayesian model average of neural networks can further mitigate the impact of quantization noise, leading to more robust compressed models. Our method outperforms existing techniques in both compression efficiency and accuracy retention, offering a promising solution for compressing DNNs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors proposed a variational inference-based method for pruning and quantizing DNNs.

### Strengths
+ Well-motivated idea. 
+ Novel ELBO approximation enabling the method in practice.
+ Experiments on both vision and natural language networks.

### Weaknesses
 - Computational expenses and data requirement not well discussed.  
- The existence of extra hyperparameters requires further tuning, and the nontrivial balance between the aggressiveness of pruning and of quantization is not well addressed.

### Questions
* It is not really clear to a practitioner, after reading the paper, how to tune the knobs of this new method, at what cost, and how to factor in the specific information of the target hardware the model is to be deployed on.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel method called Sparse Quantized Sub-distribution (SQS) that unifies neural networks pruning and quantization through Bayesian variational inference. The key innovation is treating both compression techniques as part of a single optimization problem rather than sequential steps. The method leverages spike-and-slab priors combined with Gaussian Mixture Models (GMMs) to achieve both network sparsity and low-bit representation, while using Bayesian model averaging to improve robustness to quantization noise.

### Strengths
- The unified treatment of pruning and quantization as a single single optimization problem is novel and well-motivated. 
- The mathematical framework combining spike-and-slab priors with GMMs is theoretically sound. 
- The preliminaries are rigorously explained. 
- Mathematical notation is consistent and well explained. 
- The methodology is presented in a reproducible manner.
- Strong results for ResNet/BERT on CIFAR/SQuAD. Upto 32x compression rates with minimal performance degradation. The baselines are well defined and diverse for a fair comparison.

### Weaknesses
 - Some hyperparameter choices could be better justified.
- The results presented are technically on just 2 different architectures : ResNet and BeRT, which are very limited.

### Questions
1. I would like to see similar results across other computer vision models, on other datasets than just CIFAR. Maybe include results on ImageNet1k with a wider variety of models. 
2. Similarly for the NLP task, I would like to see performance on other tasks like GLUE/SuperGLUE/MMLU etc with a wider variety of models and not just BERT. 
3. Consider adding an ablation study on the impact of different prior choices other than spike-and-slab. It might not work and that is fine, but having a better understanding on why only this prior works would be helpful. 
4. An analysis on scalability to larger models would also be helpful.
5. For Table 1 and Table 2, consider adding in the captions the type of test/dataset on which you evaluate the model on. Otherwise the captions and the results are a bit ambiguous if one does not go over the experiment section in detail.

### Soundness
4

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
3

### Summary
This paper introduces a novel method that simultaneously achieves model pruning and low-bit quantization through Bayesian variational inference, effectively compressing deep neural networks with minimal performance degradation. This method explores a unified optimization space using a spike-and-slab prior combined with Gaussian Mixture Models, achieving significant (up to 32x) compression rates with negligible accuracy loss on CIFAR-10, CIFAR-100, and SQuAD datasets. The proposed approach outperforms existing techniques and demonstrates that Bayesian model averaging can further mitigate quantization noise for more robust compressed models.

### Strengths
Pros:
1.	The proposed method unified the pruning and quantization, further shrinking the model size with less model accuracy drop.
2.	Approximating the sub-distribution problem and leveraging the variational learning to solve the problem reduces the complexity of optimizing the quantization and sparsity in all weight data.
3.	Bayesian average training is introduced to enhance the performance.

### Weaknesses
Cons:
1.	The experiments are not sufficient to demonstrate the effectiveness of the LLM model. The Bert model and GPT-2 model are not widely used LLM models.  The choice of BERT and GPT-2, while common, does not fully represent the current landscape of large language models. More recent and larger models, such as those based on the Transformer architecture with billions of parameters, should be included to assess the scalability and effectiveness of the proposed pruning and quantization method. The experiments should also explore a wider range of tasks beyond those used in the current evaluation to demonstrate the generalizability of the method.
2.	The baselines are not the SOTA work. Some SOTA works, e.g. AWQ, are expected to be compared in evaluation. The absence of comparisons with state-of-the-art methods, such as AWQ, significantly weakens the evaluation. It is crucial to demonstrate that the proposed method offers a competitive advantage over existing techniques. The evaluation should include a more comprehensive set of baselines, including both pruning and quantization methods, to provide a thorough comparison.
3.	Can you provide the evaluation in Table 5 with some baselines to show the proposed framework outperforms the existing works?

### Questions
See weeknesses

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
4

### Summary
This paper proposes a framework that integrates quantization and pruning into a unified process, rather than applying them sequentially. This study reformulates the weight quantization issue as the selection of a sub-distribution within the Gaussian Mixture Model, while the pruning problem is approached as a probability sampling problem from a Bernoulli Distribution. The authors established an approximate ELBO objective that consolidates the optimization processes for pruning and quantization into a unified optimization framework. Results for the ResNet and BERT models in image classification and question answering tasks demonstrate a significant compression rate with low performance degradation.

### Strengths
1. The idea of combining the optimization processes of quantization and pruning into a unified optimization space is interesting, and the optimization objectives have been thoroughly theoretically derived.
2. The paper is easy to read.

### Weaknesses
1. While the authors perform experiments on ResNet and BERT models, they restrict their testing to small-sized datasets (CIFAR10/100, SQUAD V1.1). Furthermore, the evaluated tasks are standard (image classification), in contrast to the previous work DGMS compared in this paper, which conducted experiments on a large dataset (ImageNet) and an object detection task. I think the proposed method may have certain inherent limitations.
2. The idea is not novel.
3. The main limitation of this paper is that proposed method lacks more experimental results on larger datasets (i.e., Imangenet, COCO2017, VOC), larger networks (i.e., VIT, EfficientNet, LLMs, etc), and compared with more competitors (i.e., OMPQ [1], EMQ [2], etc).
4. The statement "HAQ is suboptimal" is not accurate in Section I. You should provide empirical results to prove your statement.
5. The format of references is not correct, i.e.,  "Deep learning with limited numerical precision"
6. There exist some typos/grammatical errors in the paper and should be revised.
7. The presentation of the paper is bad.
8. The paper claims that the method outperforms state-of-the-art methods, but a more comprehensive comparative analysis is needed. Detailed comparisons with other existing approaches, along with discussions about the reasons behind the performance differences, would strengthen the argument for the superiority.
9. Exploring the reasons behind the success of these techniques and providing intuitive explanations would contribute to the overall scientific contribution of the work.
10. Provide a more thorough discussion of the generalization ability, robustness, and potential applications of the proposed approach.

### Questions
1. In line 176, is $T$ used before definition?

### Soundness
3

### Presentation
3

### Contribution
3
