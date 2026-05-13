# DiscQuant: A Quantization Method for Neural Networks Inspired by Discrepancy Theory

- Decision: Reject
- Scores: 3, 6, 3, 6

## Abstract
Quantizing the weights of a neural network has two steps: (1) Finding a good low bit-complexity representation for weights (which we call the quantization grid) and (2) Rounding the original weights to values in the quantization grid. In this paper, we study the problem of rounding optimally given any quantization grid. The simplest and most commonly used way to round is Round-to-Nearest (RTN). By rounding in a data-dependent way instead, one can improve the quality of the quantized model significantly.

We study the rounding problem from the lens of \emph{discrepancy theory}, which studies how well we can round a continuous solution to a discrete solution without affecting solution quality too much. We prove that given $m=poly(1/\epsilon)$ samples from the data distribution, we can round all but $O(m)$ model weights such that the expected approximation error of the quantized model on the true data distribution is $\le \epsilon$ as long as the space of gradients of the original model is approximately low rank (which we empirically validate).

Our proof, which is algorithmic, inspired a  simple and practical rounding algorithm called \emph{DiscQuant}. In our experiments, we demonstrate that DiscQuant significantly improves over the prior state-of-the-art rounding method called GPTQ and the baseline RTN over a range of benchmarks on Phi3mini-3.8B and Llama3.1-8B. For example, rounding Phi3mini-3.8B to a fixed quantization grid with 3.25 bits per parameter using DiscQuant gets 64\% accuracy on the GSM8k dataset, whereas GPTQ achieves 54\% and RTN achieves 31\% (the original model achieves 84\%).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new method of quantizing neural networks with inspiration from theory of discrepancies. Traditionally, quantization in neural networks is composed of two processes, namely defining a grid of quantization and rounding model weights to match that particular grid. Standard rounding procedures are typically RTN, alongside data-dependent methods, some of which include GPTQ; however, in this paper, the round the weights using the theory of discrepancies approach without resulting in an increase in the loss on unseen data.

DiscQuant relies on a mathematical framework to guarantee low error through rounding of nearly all model weights based on a low-rank assumption of gradient covariance. The authors establish theoretical bounds that their method can be guaranteed to achieve the expected generalization error to be at most epsilon on the data distribution, conditioned on certain low-rank conditions being met in the gradient space. They use such theoretical results to design a practical rounding algorithm that rounds the model weights from such an optimizer in a way that minimizes a regularized objective function combining KL divergence and linear constraints; it thus preserves overall model performance.

Extensive experiments on Phi-3-mini-3.8B and Meta-Llama-3.1-8B models across tasks and quantization levels indicate the superior performance of DiscQuant against RTN and GPTQ specifically at low bits. The authors are able to show that DiscQuant has gained in performance over benchmarks GSM8k, ARC Challenge, and PIQA, which then comes to expose its generalizability and robustness over any possible format of quantizations such as block scaling and incoherence processing.

### Strengths
This paper contributes a new input to the field of neural network quantization by pursuing a novel angle inspired by discrepancy theory in tackling the rounding problem. Traditional methods of quantization lie on two strands: Either the quantization grid must be designed efficiently, or the standard rounding technique, Round-to-Nearest, must be used. In its work, this paper introduces discrepancy theory for optimizing the rounding step and shows it can get high performance with all weights rounded to almost all possible bits but with a rather small approximation error. This result is established in a theoretical framework that automatically ensures low error, such as in the low-rank covariance matrices of the gradients, and so on. Therefore, this problem formulates a relatively little-investigated area of quantization in a new way.

The quality of this paper is very good in terms of methodology, with sound theoretical underpinnings for the proposed DiscQuant method to work. The authors systematically derive bounds on generalization error, effectively coupling their method with gradient covariance properties empirically validated. This is further complemented by a robust experimental setup in which DiscQuant is tested in several neural architectures (Phi-3-mini-3.8B and Meta-Llama-3.1-8B) along with quantization formats (block scaling, incoherence processing) with clear evidence that it surpasses the state-of-the-art techniques already in place like GPTQ and RTN. The results are very diversified regarding the extended coverage of benchmarks and quantization levels and therefore effectively demonstrate the applicability of DiscQuant over a wide scope and strength.

The paper is very clear in both its structured presentation of the theoretical framework and the algorithmic details. The authors do an excellent job in delineating the motivation behind DiscQuant as well as the central ideas of discrepancy theory. Figures and tables are well incorporated to help understanding in clear ways of how DiscQuant differs from other methods. While portions of the math development are tough slogging, the authors offer explanations that make intuitive sense, such as in the interpretation of results within the context of quantization grids and convex polytopes, which makes the theoretical contributions accessible to those readers with a strong technical background.

This work can be the first to provide significant influence for further work in quantization research, especially for large language models, where post-training quantization has to be very efficient for deployment on memory-constrained devices. At the same time, it frames quantization as a discrepancy problem and finds a practical rounding algorithm that achieves high compression with low loss in accuracy; thus, we contribute to new approach affecting far beyond LLMs and ranging from model deployment over mobile and embedded environments. This work further opens a route of further research into discrepancy theory in neural network quantization, inviting work that itself may eventually lead to very efficient quantization techniques. For value along the dimension of presentation, the paper is a highly significant and valuable addition to the field, advancing our understanding of effective quantization for modern, large-scale models.

### Weaknesses
 While this paper has meaningful contribution, there are areas where it can improve with theoretical explanations of the methods, experimental validations, and practical applicability.

One area for improvement concerns the theoretical justification of why the proposed method is better than other data-dependent rounding methods, like GPTQ, in settings where the gradient covariance is not strongly low-rank. The authors assume low-rank covariance to support the theoretical bounds for DiscQuant, though it remains unclear how the method would perform when such an assumption fails to hold. Discussing some cases where the low-rank assumption is violated and offering either theoretical insights into potential limitations or proposing ways to adapt DiscQuant for such cases would strengthen the contribution. This would be an opportunity to refer to alternate bounding techniques that would account for the high-rank scenarios, or comparisons with approaches based on other assumptions.

The experimental evaluation was exhaustively done for standard models, but some additional comparisons of alternative data-dependent rounding techniques that are also effective in PTQ contexts may be very helpful. For example, newer approaches like CDQuant or AdaQuant-all seek to minimize quantization error in a data-dependent optimization manner-would make good baselines. Including the experiments that were run in those methods would actually give more background about how the comparative performance of DiscQuant goes along with an outline of relative advantages. Experiments on further tasks beyond text generation and multiple-choice questions - such as real-time inference on mobile devices or edge computing environments - should further enable these results to generalize. Extensions in this direction will unveil the flexibility and possible trade-offs of DiscQuant across different practical applications.

While clear on the whole, some aspects of the presentation of discrepancy theory in the paper could have been clearer for readers not familiar with discrepancy theory, such as explaining quantization in terms of how discrepancy theory lends itself to being quantized. As it stands now, it is not very intuitive especially to readers not familiar with convex polytope to connect the random walk the Lovett-Meka algorithm used and the rounding process in DiscQuant. The connection is necessary to be explained further in order to make the text more readable and understandable.

In conclusion, though DiscQuant strongly performs well on all benchmarks, it may extend its discussion regarding the practical impact of the deployment of DiscQuant in real-world applications. For example, since the approach is iterative, even the computational efficiency along with memory usage in comparison to lesser approaches such as RTN may be much beneficial. Examined in greater detail, the amount of increased computational expense in terms of overhead in the form of time or memory could shed light on the trade-offs between using DiscQuant and alternative approaches. Second, some comments on ease of implementation, especially in comparison to such widely used approaches as GPTQ, might be useful for practitioners testing its practical utility.

In summary, what the paper contributes is a good contribution, but it requires theoretical discussion on the possible limitations of the low-rank assumption, more experiments on a variety of baselines and tasks, clearer depiction of the role of discrepancy theory, and more practical insights into trading off deploying DiscQuant in a variety of real-world settings, thereby making the results of this paper more comprehensive, accessible, and applicable across a wider range of contexts.

### Questions
1. How does DiscQuant do if the gradient covariance does not have strong low rank structures? In other words, if the low rank structure of the gradient covariance does not hold, are there alternative strategies by which we could adapt or extend DiscQuant so that the discrepancies may continue to be effective? Perhaps by modulating the discrepancy-based constraints? I'd appreciate any insight into whether or not DiscQuant is extensible to other model architectures and distributions.

2. Of relevance to GPTQ and RTN, it would be interesting to see other baselines of recent data-dependent rounding techniques, such as CDQuant and AdaQuant, which optimize the quantization error. This would give a more thorough view of the possibilities and compromises with DiscQuant. Could the authors include these new baselines in future work or some ideas on how DiscQuant would theoretically compare with them?

3. The proposed method, DiscQuant, basically comprises an optimization loop. How do the computational and memory costs of DiscQuant compare to the alternatives, like RTN and GPTQ? Is the latency or memory overhead for quantization drastic? How would these effects lead to deployment challenges for applications that have specific real-time requirements or are large-scale models? A careful study of those practical tradeoffs would be useful for understanding how this approach is actually feasible in the production setting.

4. This paper relies upon the discrepancy theory as a basis for its rounding strategy, but not all readers will be as familiar with discrepancy theory as the authors. Could the authors provide additional explanation for why discrepancy theory is especially well-suited to this problem? Moreover, explanations of the concepts random walk and convex polytope would be more transparent and therefore better for readers who are unaware of these topics if they were illustrated with an example, perhaps also simplified, to bridge the gulf between such a theoretical approach and practical application.

5. In DiscQuant, the random walk approach by inspiration of the Lovett-Meka algorithm finds some feasible vertex in the polytope. Could the authors provide more intuition behind why this method is useful for quantization? For instance, does one actually need the random walk to get low generalization error, or might possibly much simpler methods for finding a vertex of the polytope work comparably? Such intuition would help clarify the design choices and could perhaps lead to avenues for simplifications.

6. The paper employs KL divergence as a metric to be minimized to reduce the gap between the original and a quantized model. Would the authors consider alternative metrics, such as MSE or other activation-based losses, for further generalizing the properties of DiscQuant? The better understanding of loss formula interactions would allow practitioners to fine-tune this method for specific applications.

7. Although DiscQuant is only tested on text-based tasks with Phi-3-mini and Meta-Llama models, the authors might highlight the scope of potential application of this work with CNNs or transformers for vision. Are there any architectural or task-specific restrictions such that the approach of DiscQuant needs to be adjusted? Further research in that would demonstrate the extensibility of DiscQuant and what needs to be changed to allow the approach for other applications.

8. The authors assume in practice that the gradient space is low rank, an assumption they verify empirically with certain architectures. Do they have additional insight or data on how DiscQuant behaves with higher-rank gradient spaces over datasets or models? Elucidation of any limits or change in performance within such settings would help one understand whether the assumptions for the method are generalizable.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes "DiscQuant", a method to quantize weights of a large language model, which aims to improve the quantization-accuracy trade-off. The authors argue that quantization can be roughly thought of as two steps: 1) coming up with a good quantization grid,  2) a good rounding scheme that maps the exact parameters to a point in the discrete grid. Authors argue that while there ha been much effort on step 1, there is less focus on step 2, which is the rounding procedure. The key theoretical ingredient of the paper is to formulate the problem of rounding in the framework of discrepancy theory. In particular, they aim to bound the errors introduced due to rounding for all seen and unseen samples

After formulating the problem in an exact manner, which is roughly the KL divergence between unrounded and rounded model predictions, they go on to make several assumptions: 1) they assume that a simple rounding up/down suffices, and there is no needs for "jumps" in the rounding, which becomes more reasonable if the grid is fine enough. 2) they assuming a particular low-rank structure about the weight gradients, and that gradients are well behaved (defined as $\beta$-reasonable). This is key to achieve an unseen or generalization error bound. 3) They assume that  the first order approximation to the error is sufficient for calculating the errors. Here, they stress the fact that while loss gradients averaged over samples may be small, the per sample gradients are not small and in fact dominate the errors due to rounding. 

After making thee assumptions, the paper goes on to state the main theorem of the paper, Theorem 3.3, which gives the guarantee for generalization error, and subsequently introduce the algorithm that finds such a rounding efficiently in section 4. Finally, the paper presents, what seems like very compelling evidence that their proposed quantization scheme outperforms two baselines (RTN and GPTQ, see Figure 2). They also empirically test two key assumptions, the first order error approximation in Figure 3, and the low-rank structure of gradients in Figure 4,  which substantiates why their theoretical results are applicable.

### Strengths
In general, I find this work to be very strong, as it works on an important practical problem, and presents an innovative appraoch that is both theoretically grounded and is practically impactful. Let me enumerate these strengths one by one:
- The recognition of the problem with exiting quantization methods, in that they ignore the importance of the rounding step and only focus on the quantization grid, seems to be a highly relevant and important message of this paper
- After recognizing this problem, authors propose a very nice and innovative approach by formulating the problem in terms of discrepancy theory, which in hindsight, seems like an excellent choice for this problem
- The assumptions necessary for the theory, seems to be well substantiated and reasonable, and authors go to reasonable length to explain and justify them, rather than hiding them. 
- The empirical results of the paper are equally strong as the theoretical results.

### Weaknesses
My main criticism of the current draft is its lack of clarity on some of the technical/theoretical parts of the paper. 
For example, the paper would benefit a lot from an expanded explanation of the basics, ie, the basic discrepancy theory setup that they are casting their problem to, explaining the e Lovett-Meka algorithm that they are invoking so many times in detail, and then explaining what problems (complexity perhaps) it has, and what they do to fix it. Currently, it seems like the paper assumes the reader is already familiar with all thee topics and they only present bits that are novel. For reference, I spent nearly 1 hour trying to catch up with thee basics, namely the  Lovett-Meka algorithm,  but still only partially understood the technical details of the paper.  

Even after an expanded explanation on the theory basics, I think the paper needs to give more intuitive high level view of the algorithm. In particular, in section 4, there could be more explanations on what is the idea behind this formulation/heuristic of minimizing along arbitrary direction $c$? Perhaps a geometric intuition, similar to the one given in Fig 1, could be given here? 

Another point is the lack of clarity on the complexity of the proposed approach. From my limited understanding, the Lovett-Meka algorithm involves iteratively solving a SDP, which could be highly expensive in some cases. It sounds like this paper addresses some of these complexity issues via the heuristics (eg, lines 371-272). But it's hard to fully understand the solution, if the reader hasn't fully understood the problem. So an expanded section on background methods and their complexity, and then the complexity of the heuristics-based approach, would help the reader quite a bit.

One of my biggest questions that remained unresolved while reading the paper was, when discussing gradient covariance matrix, are we talking about the covariance within a fully connected layer, or could it be between different layers? In general,  there is some ambiguity as to what “n” in the parameter space really entails here. Is it the full parameter space (all parameters together), or is this procedure applied per each fully connected layer? If it is the latter, the next question is, in which order are these soundings applied? And would the authors re-calculated the gradients after each step? 

On a related note, if this procedure is done iteratively for different fully connected layers, can authors expand on this? For example, do they quantize every layer as if other layers are in the original form, or do they have an iterative approach where the the quantization of first layer impacts the quantization of the subsequent layers. 

If this is done in one shot, is that a complex operation? In general, I would also highly welcome some notes on complexity of running this algorithm.

### Questions
One of my biggest questions that remained unresolved while reading the paper was, when discussing gradient covariance matrix, are we talking about the covariance within a fully connected layer, or could it be between different layers? In general,  there is some ambiguity as to what “n” in the parameter space really entails here. Is it the full parameter space (all parameters together), or is this procedure applied per each fully connected layer? If it is the latter, the next question is, in which order are these soundings applied? And would the authors re-calculated the gradients after each step? 

On a related note, if this procedure is done iteratively for different fully connected layers, can authors expand on this? For example, do they quantize every layer as if other layers are in the original form, or do they have an iterative approach where the the quantization of first layer impacts the quantization of the subsequent layers. 

If this is done in one shot, is that a complex operation? In general, I would also highly welcome some notes on complexity of running this algorithm.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper studied the generalization gap of quantization using techniques from discrepancy theory under the assumption that the gradient is approximately low-rank. Based on theoretical analysis, the authors proposed a new quantization algorithm, named DiscQuant. Experiments are conducted to compare the proposed algorithm with existing quantization algorithm, like RTN and GPTQ.

### Strengths
1. Theoretical analysis is solid. The paper provides a solid theoretical analysis to study the generalization error of quantization. 
2. Connection with discrepancy theory. It is novel to apply techniques of discrepancy theory to neural network quantization.

### Weaknesses
The weaknesses of the paper mainly come from the numerical algorithm and experiments. 

1. The proposed algorithm solves the optimization problem (3). It seems like full-model training is required to solve the problem (3), which can be too expensive for state-of-the-art large language models. 
2. The authors only compare the proposed approach with RTN and GPTQ, which are relatively old PTQ algorithms in the area. The results seem to show a big gap between the SOTA PTQ methods. The performance gains of DiscQuant may not be solely attributed to the algorithm itself, but also to the increased computational resources used during optimization. It is unclear if the performance improvement comes from the proposed algorithm or from the increased computation. If similar resources were used for other methods, such as QAT or distillation with a small calibration dataset, it is possible that their performance would also improve. Therefore, the comparison with PTQ methods alone is not sufficient to demonstrate the superiority of DiscQuant, given its higher computational cost. 


### Questions
1. The result in the main Theorem 3.3 only depends on the data distribution. In practice, the PTQ performance also depends on the value distribution of weight matrices. If values in weights are evenly distributed, the performance after PTQ is usually better. The authors also mentioned incoherence processing, a popular method to reduce the ranges of weights. I am very curious why the distribution of weights is not reflected in the main theorem 3.3 for generalization error. 
2. Could authors explain more about how to solve the problem (3) in their algorithm? In my understanding, we may need to run backpropagation and optimize the problem (3). If that is the case, the cost is almost the same as training the full model which is too much for PTQ compared to other existing algorithms. By using the resources, people can directly run distillation or quantization-aware training for better compression and better performance. 
3. A follow-up question, can authors provide time and memory costs for the proposed algorithm?
4. Nowadays, there are lots of new algorithms for quantizing neural networks. It is better if authors can compare their algorithm with those works. Some new algorithms are listed in the following: 
      * Zhang, Aozhong, et al. "MagR: Weight Magnitude Reduction for Enhancing Post-Training Quantization." arXiv preprint arXiv:2406.00800 (2024).
      * Shao, Wenqi, et al. "Omniquant: Omnidirectionally calibrated quantization for large language models." arXiv preprint arXiv:2308.13137 (2023).
      * Chee, Jerry, et al. "Quip: 2-bit quantization of large language models with guarantees." Advances in Neural Information Processing Systems 36 (2024).
      * Liu, Zechun, et al. "SpinQuant--LLM quantization with learned rotations." arXiv preprint arXiv:2405.16406 (2024).
The results shown in the paper seem to be worse than the reported results in these most recent algorithms. It will be great the authors can choose some of them to make comparisons and explain the performance gap.

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
2

### Summary
This paper proposes DiscQuant, a data-driven rounding algorithm for post-training quantization (PTQ) of large neural networks. DiscQuant assumes that the gradients of the original model are low-rank. Under this assumption, the authors prove that their algorithm can arbitrarily minimize the upper bound on the error of the quantized model, given an accordingly large number of samples from the target data distribution.

The algorithm is primarily concerned with the second (rounding) step in quantization. The rounding process aims to minimize the KL divergence between the distributions of the next token predictions of the original and quantized models. The proposed algorithm significantly improves against the existing state-of-the-art when quantizing LLMs like Phi-3-mini-4k-instruct and Meta-Llama-3.1-8B-Instruct.

### Strengths
1. The paper is well-written and provides sufficient theoretical results using discrepancy theory (§3).
2. The proposed algorithm is agnostic to the quantization grid, which makes it quite generally applicable.

### Weaknesses
While I acknowledge the contributions made in this work, I hesitate to place a higher score here because of the following reasons.

1. The scope of the currently presented applications is limited to LLMs. I feel that if VLMs (e.g., Llava-v1.6-34b) were to be tested, consistent results there would greatly increase the paper's relevance. The absence of experiments on VLMs leaves a gap in understanding the method's applicability to multimodal models, which are increasingly important. The core idea of minimizing KL divergence between output distributions could be relevant for VLMs, but this remains untested.
2. Even within LLMs, the tested models seem quite small. Quantization is concerned with memory efficiency, so it makes sense to perform experiments with large models (e.g., Llama-3.1-70B-Instruct) that would pose greater storage challenges than the ones tested in the current work. Understandably, as the authors note (lines 405-406), DiscQuant requires two copies of the model to be stored in memory during the quantization process. This limits the scope for large-scale experiments in academic settings, but it also highlights a major shortcoming of the approach. The computational overhead of maintaining two model copies, especially for very large models, is a significant practical limitation that needs to be addressed.
3. The method needs access to data, which might be the bottleneck for many practitioners who, for instance, quickly need to prototype a handful of models but don't have the resources to run the full models, neither the data to quantize them using a DiscQuant-like algorithm. Besides, as the authors note in the last paragraph, the choice of data is in itself non-trivial. The requirement for task-specific data for effective quantization introduces a practical barrier, especially in scenarios where such data is scarce or expensive to acquire. This contrasts with methods that can operate with minimal or generic calibration data.

**Minor issues**

1. The authors may want to confine the abstract to one paragraph in the interest of adherence to the ICLR 2025 guidelines.
2. Line 133: let's --> lets?
3. Line 379: close *to* the polytype?

### Questions
It would be great to hear the authors' comments on the points raised above (see **Weaknesses**). In addition,

1. Lines 249-251: "We make this assumption because we don’t want to change any parameter of the original model too much during quantization, consider it an important property of algorithms we design" -- could the authors further explain this design choice, and the drawbacks of potentially relaxing this restriction?
2. do the authors plan to release their code?

### Soundness
3

### Presentation
3

### Contribution
3
