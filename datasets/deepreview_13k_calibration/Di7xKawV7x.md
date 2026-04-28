# End-to-End Neural Network Compression via $\frac{\ell_1}{\ell_2}$  Regularized Latency Surrogates

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Neural network (NN) compression via techniques such as pruning, quantization requires setting compression hyperparameters (\emph{e.g.,} number of channels to be pruned, bitwidths for quantization) for each layer either manually or via neural architecture search (NAS) which can be computationally expensive. We address this problem by providing an end-to-end  technique that optimizes for model's Floating Point Operations (FLOPs) via a novel $\frac{\ell_1}{\ell_2}$ latency surrogate. Our algorithm is versatile and can be used with many popular compression methods  including pruning, low-rank factorization, and quantization. Crucially, it is fast and runs in almost the same amount of time as a {\em single model training run}; which is a significant training speed-up over standard NAS methods. For BERT compression on GLUE fine-tuning tasks, we achieve $50\%$ reduction in FLOPs with only $1\%$ drop in performance. For compressing MobileNetV3 on ImageNet-1K, we achieve $15\%$ reduction in FLOPs {\em without drop in accuracy}, while still requiring $3\times$ less  training compute than SOTA NAS techniques.  Finally, for transfer learning on smaller datasets, our technique identifies $1.2\times$-$1.4\times$ cheaper architectures than standard MobileNetV3, EfficientNet suite of architectures at almost the same training cost and accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an end-to-end compression technique to compress deep models using a $l_1/l_2$ regularizer. The algorithm is versatile and fast and can be applied to different compression techniques, including pruning, low-rand factorization, and quantization. The authors build extensive experiments on various tasks, including BERT compression on GLUE fine-tuning tasks and MobileNetV3 compression on ImageNet-1K.

### Strengths
- The writing is clear and easy to understand.
- The proposed technique can be used with popular compression methods such as pruning, low-rank factorization, and quantization.
- The authors built experiments on various domains, including the pre-training and transfer learning tasks on CV and NLP benchmarks, like BERT compression on GLUE fine-tuning tasks and MobileNetV3 compression on ImageNet-1K.

### Weaknesses
 - The main concern is the limited novelty of the work. The idea of making the FLOPs constraint differentiable is commonly used in many pruning works, such as using auxiliary masks. The positivity constraints are crucial for pruning models. However, as mentioned in the work, similar ideas have been studied in existing works.
- It is recommended to evaluate the performance of the proposed method multiple times, as it is claimed to be more stable than other methods. 
- Direct comparison with advanced compression methods is also encouraged, and it would be better to show the training cost comparison since the proposed method is claimed to be fast.

### Questions
Please refer to the weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose an end-to-end framework for model compression. Specifically, the FLOPs is regarded as the target of optimization via l1/l2 latency surrogate. The experiments on MobileNetV3 and BERT show that the proposed method can achieve a cheaper architecture with almost the same amount of time as a single model training run.

### Strengths
1. This paper propose an end-to-end model compression method via optimizing the FLOPs.

2. The l1/l2 regularized surrogate is employed to optimize for the latency of the compact neural networks.

3. Experimental results on language and vision tasks demonstrate that the proposed method can find a more compact architecture.

### Weaknesses
1. The authors claim that the proposed method can be used with pruning, low-rank factorization, quantization etc. However, the quantization is not verified on the experiments.

2. The performance on different devices can be various, so I wonder is the proposed method still effective on other device?

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces on model compression method, which is with low complexity, compared to the typical NAS. 
The experiment shows that the 50% reduction is only with 1% performance loss. Besides, the author introduces its procedure of the math derivation. 

But, such method is not novel enough, and similar idea (optimize the mask) has been widely discussed. 
Secondly, model compression and quantization should be widely experimented in diverse models and modules.

### Strengths
The experiment shows that the 50% reduction is only with 1% performance loss. Besides, the author introduces its procedure of the math derivation. 
The paper is with a well-written, and clearly present the contents.

### Weaknesses
But, such method is not novel enough, and similar idea (optimize the mask) has been widely discussed. 
Secondly, model compression and quantization should be widely experimented in diverse models and modules, e.g., conv, transformer, linear.

### Questions
One question that arises is: what is the relationship between model compression and transfer learning? Do they occur in the same pipeline? For instance, is model compression done within the transfer learning process? Or is model compression performed first, followed by transfer learning to enhance performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
