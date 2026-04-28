# Towards Reliability of Parameter-free Optimization

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Hyperparameter tuning, particularly the selection of an appropriate learning rate in adaptive gradient training methods, remains a challenge.
To tackle this challenge, in this paper, we propose a novel parameter-free optimizer, \textsc{AdamG} (Adam with the golden step size), designed to automatically adapt to diverse optimization problems without manual tuning.
The core technique underlying \textsc{AdamG} is our golden step size derived for the AdaGrad-Norm algorithm, which is expected to help AdaGrad-Norm preserve the tuning-free convergence and approximate the optimal step size in expectation w.r.t. various optimization scenarios.
To better evaluate tuning-free performance, we propose a novel evaluation criterion, \textit{reliability}, to comprehensively assess the efficacy of parameter-free optimizers in addition to classical performance criteria. 
Empirical results demonstrate that compared with other parameter-free baselines, \textsc{AdamG} achieves superior performance, which is consistently on par with Adam using a manually tuned learning rate across various optimization tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The script proposed a new parameter-free method called AdamG. The design principle are derived from the analysis of Adagrad-norm.

### Strengths
The topic is important and interesting.

### Weaknesses
 The topic is important and interesting.

 The motivation of the stepsize design is rather weak. The writing is sub-optimal. The efficacy of the proposed algorithm is not convincing. See below.

 **Weakness and questions:**

1.  **The design principle is rather weak.** stepsize design is to optimize the constant terms in the convergence upper bound of AdaGrad-Norm. To me, this motivation is rather weak. Here are my reasons. 

   1-1. the bound is derived based on worst case assumptions,which does not utilize much properties of neural nets. 

   1-2. The upper bound itself is likely to be loose, similar as most existing convergence upper bound for adaptive methods. I don't think we can reach much insightful result by optimizing a loose upper bound of this kind.  

   1-3. The derived upper bound is tailored for AdaGrad-Norm, which is significantly different from Adam. Such theory will miss many important properties of Adam. For instance, the update direction of AdaGrad-Norm is the same as SGD direction, but Adam is not.


2.  **The algorithm description is not clear.**  In Algorithm 2, is the operation $r_{k+1}g_{k}$  operated coordinate-wisely? Also, how is eta_k changes with k? I did not find the update rule on eta_k.

4.  **Extra memory overhead.** According to Algorithm2, do we need to store an additional momentum building block $r$? If yes, it would introduce significant  extra memory overhead. Please discuss.

5.  **Extra hyper-parameter.** AdamG introduces a new hyperparameter beta3. Is AdamG sensitive to beta3? We need more ablation studies, otherwise, the proposed method is far from "parameter-free".

6.  **The experiments are not convincing enough.** Currently, the results are only shown for small & middle-scaled experiments such as TinyImageNet and BLUE. It is much more convincing if the authors can provide evidence on LLM (>1B) pretraining.

### Questions
**Weakness and questions:**

1. **The design principle is rather weak.** stepsize design is to optimize the constant terms in the convergence upper bound of AdaGrad-Norm. To me, this motivation is rather weak. Here are my reasons. 

   1-1. the bound is derived based on worst case assumptions,which does not utilize much properties of neural nets. 

   1-2. The upper bound itself is likely to be loose, similar as most existing convergence upper bound for adaptive methods. I don't think we can reach much insightful result by optimizing a loose upper bound of this kind.  

   1-3. The derived upper bound is tailored for AdaGrad-Norm, which is significantly different from Adam. Such theory will miss many important properties of Adam. For instance, the update direction of AdaGrad-Norm is the same as SGD direction, but Adam is not.


2. **The algorithm description is not clear.**  In Algorithm 2, is the operation $r_{k+1}g_{k}$  operated coordinate-wisely? Also, how is eta_k changes with k? I did not find the update rule on eta_k.

4. **Extra memory overhead.** According to Algorithm2, do we need to store an additional momentum building block $r$? If yes, it would introduce significant  extra memory overhead. Please discuss.

5. **Extra hyper-parameter.** AdamG introduces a new hyperparameter beta3. Is AdamG sensitive to beta3? We need more ablation studies, otherwise, the proposed method is far from "parameter-free".

6. **The experiments are not convincing enough.** Currently, the results are only shown for small & middle-scaled experiments such as TinyImageNet and BLUE. It is much more convincing if the authors can provide evidence on LLM (>1B) pretraining.

### Soundness
2

### Presentation
2

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
This paper proposes a novel parameter-free optimization algorithm named AdamG. At the core of the proposed algorithm is the definition of “golden step size” derived aiming to approximate the optimal step size in expectation. Extensive experiment results are presented to demonstrate the effectiveness of the proposed optimization algorithm.

### Strengths
The idea of the proposed algorithm is very interesting.

The experimental results are fairly comprehensive.

### Weaknesses
I feel that there may be some important weaknesses in the current version of the paper.

First of all, unless I missed something very important, it seems that this paper does not provide any rigorous theory. The derivation in Section 3.3 relies on many 'approximately hold' equations, and Corollary 3.3 and Theorem 3.4 are not theoretical guarantees for the proposed AdamG, but known bounds for AdaGrad-Norm and NGD, respectively. In comparison, I find that the existing line of work on parameter-free optimization algorithms is highly theory-oriented. For example, the parameter-free algorithms in Table 1, such as DoG, DoWG, D-adaptation, and Prodigy, are all proposed with (and motivated by) rigorous theoretical guarantees. Therefore, not having rigorous theory for the proposed algorithm is a significant weakness and makes this paper diverge from the line of parameter-free optimization methods.

Second, the authors pointed out the first contribution of this paper is to propose the novel evaluation criterion named reliability. However, I am not convinced that reliability defined in Definition 4.1 is innovative. I believe it is a simple summary of what people do all the time – when proposing a new algorithm, it should be compared with existing algorithms with the optimally tuned hyperparameters. Moreover, the definition of reliability is not rigorous or general enough: why should the definition require specific comparison with Adam(1e-2), Adam(1e-3), Adam(1e-4), and Adam(1e-5)? Clearly, this definition hides assumptions on the (possible range of) scale of the optimal learning rate, is not mathematically reasonable, and is against the spirit of parameter-free optimization.

### Questions
Can you establish theroetical guarantees for the proposed algorithms?

How is the reliability evaluation criterion novel?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces ADAMG, a new parameter-free optimizer that leverages a novel golden step size derived from the AdaGrad-Norm algorithm. Additionally, the authors propose a new evaluation criterion, "reliability", to assess how consistently parameter-free optimizers perform compared to manually tuned ones like Adam across various tasks. The empirical results suggest that ADAMG performs competitively with manually tuned Adam while retaining the benefits of being parameter-free.

### Strengths
1. **Novel Contribution**: The introduction of the golden step size for AdaGrad-Norm and its adaptation into ADAMG is an interesting and original theoretical advancement in parameter-free optimization.
2. **Comprehensive Evaluation**: The "reliability" criterion offers a new and effective way to assess parameter-free optimizers, going beyond traditional metrics like convergence speed and accuracy.
3. **Theoretical Foundation**: The paper is built on a solid mathematical framework, with a well-justified derivation of the golden step size and its properties.
4. **Practical Applications**: Empirical results show that ADAMG performs close to manually tuned Adam, which is beneficial for practitioners looking to avoid the time-consuming process of hyperparameter tuning.

### Weaknesses
See Questions.

Here are a few points:

1. Your experimental validation must be as strong as your claims: If you’re asserting that your method outperforms Adam (I suggest using AdamW, as it’s standard for LLMs), you must ensure you’ve thoroughly optimized its hyperparameters, schedulers, and other settings. This is because being better than a non-perfectly-optimized Adam(W) defeats the purpose of your effort. **I doubt this has been done properly**. To do this, I suggest taking two different LLM architectures (GPT and Llama) in three increasingly larger sizes (do not have to be hube but maybe 124, 248, 496M param) on three datasets of different quality (e.g. FineWeb,  Common Crawl...). Then, fine-tune AdamW to the best of your abilities: 5 learning rates, 5 batchsizes, 5 beta1, 5 beta2, 5 lambdas, and 3 different schedulers. I know this is very expensive and a huge burden, but once you do this, and you see that you performed consistently better (or even marginally less than AdamW, practitioners will pay attention to this paper).

2. The measure you propose is a beginning, but not maybe the best measure. A way to improve this is to devise measures that consider the "saved compute". For example, you can weight each experiment by how much compute they saved w.r.t. "best-tuned AdamW", or a normalized version of this. This way, there is no risk that some Param-Free optimizer receives a high score on tasks where fine-tuning Adam(W) is cheap, and thus "less valuable". Measuring success where it counts is important: The more compute you save, the higher the score.

3. After confirming that Adam(W) has been optimally tuned, you need to show that your optimizer consistently outperforms or at least matches Adam(W) in performance. You’ve already made some efforts in this direction and compared it against other parameter-free optimizers, which is good. **This has to be enhanced based on 1. and re-evaluated based on a measure in line with 2.**

4. I recommend shifting more of the empirical evaluation to LLMs, as they are a hot topic and where most fine-tuning resources are being spent.

5. Is your optimizer 4x more computationally expensive than SGD? If so, that makes it more expensive than AdamW, which is a significant drawback for LLMs. In this case, you might have to consider that your optimizer prevents the training of larger models, which will be a limitation.

### Questions
I am not an expert in parameter-free optimization, so my feedback might not be fully exhaustive. I won’t elaborate much on the theory—it looks sound at a glance. From my perspective, the aspect I want to highlight is that if you claim to outperform the best-tuned Adam, you need to be absolutely certain as this might have massive consequences.

Here are a few points:

1. Your experimental validation must be as strong as your claims: If you’re asserting that your method outperforms Adam (I suggest using AdamW, as it’s standard for LLMs), you must ensure you’ve thoroughly optimized its hyperparameters, schedulers, and other settings. This is because being better than a non-perfectly-optimized Adam(W) defeats the purpose of your effort. **I doubt this has been done properly**. To do this, I suggest taking two different LLM architectures (GPT and Llama) in three increasingly larger sizes (do not have to be hube but maybe 124, 248, 496M param) on three datasets of different quality (e.g. FineWeb,  Common Crawl...). Then, fine-tune AdamW to the best of your abilities: 5 learning rates, 5 batchsizes, 5 beta1, 5 beta2, 5 lambdas, and 3 different schedulers. I know this is very expensive and a huge burden, but once you do this, and you see that you performed consistently better (or even marginally less than AdamW, practitioners will pay attention to this paper).

2. The measure you propose is a beginning, but not maybe the best measure. A way to improve this is to devise measures that consider the "saved compute". For example, you can weight each experiment by how much compute they saved w.r.t. "best-tuned AdamW", or a normalized version of this. This way, there is no risk that some Param-Free optimizer receives a high score on tasks where fine-tuning Adam(W) is cheap, and thus "less valuable". Measuring success where it counts is important: The more compute you save, the higher the score.

3. After confirming that Adam(W) has been optimally tuned, you need to show that your optimizer consistently outperforms or at least matches Adam(W) in performance. You’ve already made some efforts in this direction and compared it against other parameter-free optimizers, which is good. **This has to be enhanced based on 1. and re-evaluated based on a measure in line with 2.**

4. I recommend shifting more of the empirical evaluation to LLMs, as they are a hot topic and where most fine-tuning resources are being spent. 

5. Is your optimizer 4x more computationally expensive than SGD? If so, that makes it more expensive than AdamW, which is a significant drawback for LLMs. In this case, you might have to consider that your optimizer prevents the training of larger models, which will be a limitation.

I understand that addressing the points above might be too much to ask during rebuttal.

I will follow the discussion and reserve the right to modify my score based on further developments.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new parameter-free version of Adam, using an automatic adaptation of the step size which they call golden step size. They also propose a "reliability" criterion to measure how good parameter-free optimizers are compared to the best performing Adam baseline.

### Strengths
The paper is clear and relatively well written. The idea of a reliability measure for optimizers is interesting and a decent contribution.

### Weaknesses
 -    Very little analysis of the results or explanations of why AdamG seems to underperform on some of the more challenging training datasets like tiny imagenet, which leaves wondering how it would perform on even more challenging tasks such as full imagenet. Particularly surprising are its lack of performance with the ResNets.

-    While the method is parameter-free, they add additional parameters (like q=0.24) which are not properly analyzed or explained. The impact of this parameter on the optimization process and its sensitivity to different tasks is not clear.

-    In many of the experiments, it would have been appropriate to run image classification for longer (200 or even 300 epochs is standard, especially when dealing with ViTs). The lack of convergence analysis makes it difficult to assess the true potential of the proposed optimizer.

-    The paper leaves many of its results in the appendix, some of the main results are left at the bottom and not discussed or analyzed in depths. This makes it hard to follow the main findings and their implications.

-    Weight decay is completely left out and never mentioned in the paper. How does it compare when using Adam with weight decay? How does it compare with AdamW? The lack of comparison with AdamW, a widely used variant, is a significant omission.

-    The figures in the appendix use full range on the Y axis, and make it close to impossible to see smaller differences. A zoom-in at the end or a smaller range on the Y axis would make it easier to compare them. Test accuracy plots are missing, which are crucial for evaluating the generalization performance of the optimizer.

### Questions
-    How does AdamG compare when using Adam with weight decay, or with AdamW? 
-    How does AdamG compare when running the image classification tasks until full convergence (~200/300 epochs for CIFAR-10/100)
-    How does the optimizer compare in wall-clock time to Adam?
-    How does AdamG perform on pretraining with small language modeling tasks, rather than finetuning only? 50-100K steps on GPT2 tiny would be enough.

### Soundness
2

### Presentation
2

### Contribution
2
