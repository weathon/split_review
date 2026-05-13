# Understanding Reasoning with Looped Models

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Large language models have shown promising abilities in reasoning problems and scaling laws suggest that parameter count is a key driver. Recent works (Chen & Zou, 2024; Ye et al., 2024) argue that for reasoning, depth plays a very important role in addition to parameter count. In this work, we make a more fine-grained claim — many reasoning problems require large depth but not necessarily many parameters, in the sense that they can be solved via looped models. This unlocks a novel application of looped models for reasoning. We empirically study various synthetic reasoning problems like addition, variable assignment and math problems. For each of these, we find that $k$-layer transformer model looped $L$ times nearly matches the quality of a $kL$-layer non-looped model and is much better than a k-layer model. Thus, using a small model and providing depth via looping can suffice for such reasoning problems. We then show theoretical results proving that many such reasoning problems can be solved via iterative algorithms, and thus, can be solved with looped models. Motivated by these findings, we train autoregressive models on general language modeling datasets with looping and compare a $k$-layer model looped $L$ times to a $kL$-layer model. While the looped model is understandably worse on perplexity and memorization tasks, it surprisingly does very well on tasks that require reasoning, like open book QA, math word problems and reasoning primitives. Despite having significantly fewer parameters, it can even match or outperform the non-looped $kL$-layer model on some of these tasks. These results suggest a novel inductive bias of looped models towards enhanced reasoning. We provide further evidence for this inductive bias by visualizing perplexity vs downstream isoplots, and design a looping-inspired regularization that solidifies this hypothesis.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies performance of looped transformers on reasoning tasks. They show that looped models result in worse memorization of facts reflected by lower perplexity but can outperform non-looped models on some tasks that require compositional generalization. They highlight that perplexity may be unsuitable metric because looped and non-looped models with same perplexity can result in substantially different performance on downstream tasks requiring reasoning. Lastly, they introduce regularization of non-looped models which forces the weights to be closer to each other in terms of cosine similarity. This leads to a same perplexity but better downstream performance on reasoning tasks.

### Strengths
In terms of originality and contribution, the paper demonstrates that a simple regularization can improve reasoning abilities of transformers and provides a basic theoretical analysis of looped models. The writing is clear and the experiments seem sound.

### Weaknesses
Personally, I do not find the results very surprising. The fact that looped models can improve performance on algorithmic tasks is known and the extension to the tasks tested in the paper does not seem substantial. It seems to me that that the authors are not aware of the work done in the group of Tom Goldstein related to reasoning abilities of recurrent models (different term for looped models):
https://arxiv.org/abs/2202.05826
https://arxiv.org/abs/2106.04537
And also Daniel Selsam's paper which also showed the importance of recurrence: https://openreview.net/forum?id=HJMC_iA5tm&referrer=%5Bthe%20profile%20of%20Daniel%20Selsam%5D(%2Fprofile%3Fid%3D~Daniel_Selsam1)

Minor:
The first sentence in related work contains a typo: intelligent and robustly model

### Questions
1. An obvious goal for the looped models would be to figure out how to make the looping adaptive, i.e. that the model would be able to decide when to stop the looping. Did you considered experiments which would test this ability? This could provide clear benefits over the non-looped baseline and I believe it would be substantial contribution. From Table 3, it is visible that different tasks require different number of loops.
2. Why do the plots in Figure 1 contain datapoints for different perplexities for the two compared models?

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
4

### Summary
This paper investigates using looped language models for reasoning tasks. The authors demonstrate that reasoning tasks can benefit from deeper models achieved through looping without significantly increasing the parameter count. They show that on synthetic reasoning tasks like multi-digit addition and p-hop induction, looped models can match or even surpass the performance of deeper models with more parameters. Additionally, they identify an inductive bias in looped models toward reasoning tasks and propose a looping-inspired regularization technique to capture these advantages without substantially compromising language modeling efficiency.

### Strengths
1. The experiments on synthetic tasks like multi-digit addition and p-hop induction provide a valuable starting point for understanding the strengths of looped models, particularly in recursive reasoning scenarios.

2. Proposing a looping-inspired regularization technique is a noteworthy contribution. It offers a practical method to capture the inductive bias of looped models while maintaining competitive performance in perplexity metrics.

### Weaknesses
1. Some explanations, particularly regarding the looping mechanism and training setup, are not as clear as they could be. The paper lacks detailed explanations of how the transformer architecture implements the looping mechanism. For instance, it’s unclear how the KV cache is managed when layers are looped multiple times. Specifically, when a layer is looped, is the KV cache reinitialized or is the previous state maintained? If the state is maintained, how does this impact the attention mechanism and the model's ability to attend to relevant parts of the input sequence across multiple loop iterations? Additionally, how does looping interact with the residual connections and layer normalization typically present in transformers? Does the looped layer receive the output of the previous loop iteration before or after the residual connection and layer normalization? More detailed descriptions and possibly visual aids would enhance understanding.

2. There’s limited discussion on the computational efficiency and scalability of looped models, including potential overhead during training and inference. Specifically, it’s important to know how the training time and inference speed of looped models compare to standard models. Does looping result in longer training times due to repeated computations, or does it impact memory consumption during training and inference? For example, if a layer is looped 3 times, does this triple the memory footprint for storing intermediate activations during backpropagation? Furthermore, how does the looping affect the parallelizability of the model during training and inference? Can the looped layers be processed in parallel, or does the sequential nature of looping impose a bottleneck?

### Questions
1. Given that looped models may have higher perplexity but better reasoning performance, how do you suggest balancing these aspects in practical applications where both are important?

2. Can the looping approach be extended to other domains, such as computer vision models like vision transformers, or models employing different attention mechanisms?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work explores the looped models in reasoning tasks, demonstrating that they can achieve deeper reasoning depth with fewer parameters compared to the traditional models. The authors also conducted comprehensive experiments on reasoning tasks like addition and math word problems, and looped models showed improved performance in reasoning, despite having worse performance on memorization tasks. The findings may offer a potential new direction for language model development to improve its reasoning capacity.

### Strengths
1. This work provides extensive empirical studies showing that looped models perform well on reasoning tasks, even outperforming traditional models in some cases.
2. This work offers theoretical results that support the expressiveness and efficiency of looped models in solving reasoning problems.
3. The paper is well-presented, making it easy for readers to follow, despite some complex theoretical analysis.

### Weaknesses
1. There is limited evidence on the performance of looped models in real-world applications or datasets.
2. It would be much better if the authors could scale up the experiments, and validate the effectiveness of the looped model in real-world tasks.

### Questions
please see the weakness.

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
3

### Summary
The paper investigates the performance of looped Transformers on arithmetic and reasoning tasks and compares it with feedforward models with the same amount of flops. The authors show that looped models can equal and sometimes outperform models with a comparably larger amount of parameters by simply looping over the network, although they demonstrate a worse perplexity. The authors also propose a regularization method to induce feedforward models to behave as looped models and show that it yields better performance on reasoning without reducing perplexity.

### Strengths
The experimental setup is sound and the findings are interesting. Although the good performance of looped models is not novel, the paper provide clear insights into the reasons, and makes a disctinction between reasoning and memorization performance. The claims are properly backed-up by the experiments.

The looping-inspired regularization is a particularly interesting and original idea to improve reasoning in Transformers.

The paper is also well-written and easy to follow.

### Weaknesses
Experiments lack a comparison with other categories of models that use looping in the computation (e.g. recurrent Transformers [1,2] or Transformers autoregressively returning an output via chain-of-thought or other prompting strategies). Adding comparisons on the arithmetic and reasoning tasks could help to further discriminate what makes looping efficient. Specifically, a comparison with recurrent models, which also maintain state across iterations, could illuminate whether the performance gains are due to the looping mechanism itself or simply the increased effective depth. Furthermore, the lack of comparison with chain-of-thought methods, which also involve iterative processing, makes it difficult to assess the novelty and specific advantages of the proposed looping approach.

The results in Figure 1 and Table 4 are not thoroughly explained and are hard to interpret. In Figure 1, it is not exactly clear what the y-axis represents and therefore what each data point represents. The description of the figure lacks detail on how the downstream metrics are calculated and averaged. In Table 4, the choices for the values of $k$ and $\lambda_{\text{reg}}$ are not well justified and a deeper analysis of the results could be helpful. Specifically, the paper does not provide a clear rationale for selecting the specific values of $k$ (divisors of 24) and the range of $\lambda_{\text{reg}}$ values, making it difficult to understand the sensitivity of the results to these hyperparameters. The lack of a systematic hyperparameter search also raises questions about the optimality of the reported results.

### Questions
1. In Figure 1, can you explain how each of the data points are generated?

2. In Table 4, do you have an explanation as of why performance increases when setting $k=4$ but then is reduced when $k$ increases?

3. I am curious to know how looping compares with chain-of-thought as the latter effectively performs looping via autoregression but introduces a bottleneck between each loop with the next-token selection. Have you investigated the similarities and differences between the two approaches in your experments?

4. Have you further studied the connection between the number of loops and performance in your experiments, particularly with a high number of loops? Does accuracy keep increasing as the model loops or where is the upper bound? Does it differ depending on the model size?

### Soundness
3

### Presentation
2

### Contribution
3
