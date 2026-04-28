# LiFT: Learning to Fine-Tune via Bayesian Parameter Efficient Meta Fine-Tuning

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
We tackle the problem of parameter-efficient fine-tuning (PEFT) of a pre-trained large deep model on many different but related tasks. Instead of the simple but strong baseline strategy of task-wise independent fine-tuning, we aim to meta-learn the core shared information that can be used for unseen test tasks to improve the prediction performance further. That is, we propose a method for {\em learning-to-fine-tune} (LiFT). LiFT introduces a novel hierarchical Bayesian model that can be superior to both existing general meta learning algorithms like MAML and recent LoRA zoo mixing approaches such as LoRA-Retriever and model-based clustering. In our Bayesian model, the parameters of the task-specific LoRA modules are regarded as random variables where these task-wise LoRA modules are governed/regularized by higher-level latent random variables, which represents the prior of the LoRA modules that capture the shared information across all training tasks. To make the posterior inference feasible, we propose a novel SGLD-Gibbs sampling algorithm that is computationally efficient. To represent the posterior samples from the SGLD-Gibbs, we propose an online EM algorithm that maintains a Gaussian mixture representation for the posterior in an online manner in the course of iterative posterior sampling. We demonstrate the effectiveness of LiFT on NLP and vision multi-task meta learning benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper develops a general fine-tuning strategy for foundational models that is based on the meta-learning principle. This way not only the foundational models become shareable, but also the layers responsible for task-specific fine-tuning can be accumulated and shared to be used on unseen tasks with not enough fine-tuning data. The core contribution of the paper is the Bayesian methodology that casts meta-learning (and hence task-specific fine-tuning) as Bayesian sampling exercise. Technically, this is implemented via a modification of SGLD and the online EM algorithm. Empirical results are obtained from NLP and Vision tasks.

### Strengths
- Overall, the idea seems sufficiently novel and interesting
- The empirical evaluation is extensive and convincing
- Results are state of the art

### Weaknesses
 - The justification of SGLD-Gibbs Sampling is only empirical through a toy example in Appendix A. A theoretical justification showing the required convergence would have significantly strengthened the contribution. Specifically, while the individual components (SGLD and Gibbs) have known convergence properties, the convergence of their composition, especially under the proposed asynchronous update scheme, is not rigorously established. The paper lacks a proof that the proposed asynchronous updates maintain the desired stationary distribution, which is a critical gap in the theoretical foundation.
- Ablation studies are not comprehensive enough, failing to support major decisions made in the algorithm design step: the $J$-term update and the Online-EM Mixture for Posterior Approximation. The paper does not adequately explore the necessity of the $J$-term update, a core component of the algorithm. Furthermore, the ablation study for the Online-EM Mixture for Posterior Approximation is insufficient, as it only compares GMM with different numbers of components, without comparing to a single Gaussian, which is the most natural baseline.
- It looks like literature review could be updated with the online EM literature. I am not sure if the online EM algorithm is genuinely novel given the lack of analysis of the related work on this topic in the paper. The paper does not sufficiently discuss the novelty of the proposed online EM algorithm in the context of existing literature. The provided references highlight the existence of similar methods, and the paper needs to clearly articulate the specific differences and advantages of its approach.
- It is unclear if code is being open sourced.

### Questions
- $J$ appears in (11) out of nowhere. Could you please motivate the need in this term more clearly in the text transition between (7) and (9)? It seems to be the core algorithmic contribution that does not follow trivially from the original SGLD formulation in (7-8). It feels like by not discussing it in sufficient detail authors basically undersell their contribution.
- Can you say at least something theoretical about your approximations, to strengthen the theory? I understand that convergence rate analysis might be to much of an ask, but if we talk about means and if you take the expectations of (9-11) will they match the expectations of equations (7-8) in the limit?
- On a related note, can you run an ablation study by comparing against a more naive version of the algorithm that does not rely on $J$ updates? For example, you could use the sample approximation of the sum in (7) by the log-probability of $\theta_{i}^a$ in a given update round. In my view, this could further strengthen the algorithmic contribution of the paper, or simplify the algorithm if sample approximation has same or better accuracy.
- "However, we aim to enrich it by a mixture of Gaussians to better approximate the true posterior that is inherently a multi-modal distribution". Can you provide the results of ablation study comparing against Gaussian confirming that such enrichment is actually useful? This is especially important given that the Online-EM Mixture for Posterior Approximation is necessary only to support the GMM. If the GMM is not provably necessary, the value of the Online-EM Mixture contribution is questionable.
- Since you are claiming online EM as a technical contribution, could you please update the related work section with the online EM literature? For example: https://arxiv.org/abs/2207.14019, https://www.diva-portal.org/smash/get/diva2:857377/FULLTEXT01.pdf, https://www.sciencedirect.com/science/article/abs/pii/S0167947304003263. Please discuss the novelty of your work w.r.t. existing contributions and motivate why you need a new version of online EM.
- "Hence we stick to the simple average of the metrics over all test tasks regardless of the metric types." I understand that the relative lift could be tricky, because of division by small numbers. Could you please consider reporting the mean of the absolute deltas between the baseline and the candidate algorithm? I believe this could be a more robust and more statistically significant measure of accuracy improvement than reporting the sum of raw metric values.
- Will code be open-sourced?

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
3

### Summary
The authors propose a parameter efficient finetuning scheme called learning-to-finetune (LiFT) that can adapt a model not only to a single, but to a set of related tasks. 

At the heart of LiFT sits a Bayesian meta training method that is executed on a set of related finetuing tasks. It uses hierarchical priors for the PEFT parameters to split task specific from task agnostic knowledge and runs stochastic gradient Langevin dynamics (SGLD) for posterior inference. The transferable task agnostic knowledge is later used as a prior for test-time adaptation. 

While they explain their method, using LoRA, the method is general and can be adapted easily to any other PEFT scheme.

### Strengths
The paper is in general well written and I enjoyed reading it. Ideas are explained in detail. For most of the math intuitive explanations are provided. Hence, it is easy to understand the proposed meta-learning method and all the tricks that are needed to make it work. 

The paper contains two creative ideas: 1) Their particular hierarchical Bayesian model for the PEFT parameters. 2) The combination of Gibbs sampling and SGLD for memory efficient posterior inference.

### Weaknesses
There are several weaknesses to this paper:
* The main claim of the paper is, that it is beneficial to use their Bayesian formulation for PEFT of models to a set of related tasks. They give an intuitive explanation that one of their latent variables learns task agnostic and the other task specific adaptations. While this sounds reasonable, there is no analysis if this claim is actually true and, hence, if their hierarchical model actually makes sense. However, experimental sanity checks could be easily made e.g. by comparing to a non-hierarchical model. In the end I am completely puzzled what part causes the demonstrated increase in performance: 1) The formulation of the problem or 2) favorable training dynamics of this quite large training algorithm. 

* Important ablation studies are not provided: Their hierarchical model requires the choice of two variances $\sigma^2$ and $\beta^2$. Only one set of values is provided. However, to judge how brittle the model is, some ablations would be helpful.

* The paper does not give any idea how the proposed algorithm scales with #adapted parameters (can it only be used with PEFT methods or even with FFT?). Training requires to run the SGLD sampling. From the appendix I got, that it requires quite some steps, i.e., 2000 burn-in and 1000 warmup steps. It is not obvious how this translates to training time.

* The paper proposes an online EM algorithm to fit a GMM to posterior samples in an iterative way, making it unnecessary to store the full set of posterior samples. While stating that this is a novel contribution, there exists lots of work about this problem already. Keywords are: 1) incremental EM or 2) streaming GMMs [1], [2]. Related works are not referenced and a comparison is missing.

### Questions
After thoroughly reading the paper, some questions remain:
* Is there any experimental evidence that $\phi$ really learns meaningful task-agnostic adaptations?

* How brittle is the training if we change the parameters $\sigma^2$ and $\beta^2$ of the hierarchical model? Did you do any experiments there?

* Why do you choose a GMM to model $\phi|\{D_i\}_{i=1}^N$. 

I think, having a multi-modal distribution goes against your idea that $\phi$ learns task-agnostic adaptations, because each mode can represent a specialization. More specifically, if the number of modes $M$ is equal to the number of tasks $N$, each mode of $\phi|\{D_i\}_{i=1}^N$ can specialize to one task. In this case you would have something very similar to a stochastic version of the mixtures of LoRA idea. How do you prevent this from happening?

* After test-time adaptation, is the model output stochastic or deterministic? I.e. do you continue to run the SGLD sampling for $\theta|\phi$ or do you use some statistics and perform just a deterministic forward pass?

* In the stochastic case: Why don't you provide confidence intervals for the LiFT results?

* How does the LiFT scale with the #trainable parameters?

* What is the difference between warm-up samples and burn-in samples for the SGLD Gibbs sampling?

I am looking forward to your explanations.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The author proposed a modulated meta-learning scheme where the modulation is the LoRA parameter of the large model. Specifically, each task-specific parameter is represented with LoRA, and the base model is shared across all tasks. To learn such a model, the author proposed a hierarchical Bayesian meta-learning method called LiFT. Here, the task specifical LoRA is modeled to be sampled from a prior distribution, where the author have suggested an efficient sampling method.

### Strengths
The overall writing is clear, and the method itself is sensible.

The proposed sampling method is efficient. I think it would be great to show the experiment that shows the efficient gain.

### Weaknesses
Missing critical related works and comparison. Currently, there are many works that consider meta-learning with modulation (i.e., a few parameter updates from the base model, such as LoRA). For instance, CAVIA [1] is the first paper that suggested meta-learning with modulation. Furthermore, a more recent method, CNAPs [2], combines amortization-based meta-learning with modulation. Several works consider modulated meta-learning as follows: FiLM modulation with MAML [3,4], LoRA modulation with MAML [5], Scaling CNAPs to large-scale meta-learning [6,7], and LoRA modulation with amortization-based meta-learning [8].

[1] Fast Context Adaptation via Meta-Learning, ICML 2019
[2] Fast and flexible multi-task classification using conditional neural adaptive processes, NeurIPS 2019
[3] From data to functa: Your data point is a function and you can treat it like one, ICML 2022 
[4] COIN++: Neural Compression Across Modalities, TMLR 2022
[5] Modality-Agnostic Variational Compression of Implicit Neural Representations, ICML 2023
[6] Memory Efficient Meta-Learning with Large Images, NeurIPS 2021
[7] Improved Few-Shot Visual Classification, CVPR 2020
[8] Online Adaptation of Language Models with a Memory of Amortized Contexts, arXiv 2024

----

Need to consider more recent baselines, and more effective meta-learning baselines. Currently, most of the meta-learning baselines are highly outdated. Furthermore, there are more effective and recent baselines [1,2,3]. Typically, [3] suggested the interpolation of sparse experts (i.e., only a few parameter updates), which has similarities with the current approach (i.e., LoRA modulation).

[1] Meta-learning with warped gradient descent, ICLR 2020
[2] Bootstrapped meta-learning, ICLR 2022
[3] Unleashing the Power of Meta-tuning for Few-shot Generalization Through Sparse Interpolated Experts, ICML 2024

---

I think the experiment application needs to be more motivating. The main purpose of using LoRA is to fine-tune large models to reduce the computation burden or overfitting. However, the current setup is mostly conducted in small-scale networks. I believe showing whether the proposed method scale to large-scale LLM (e.g., more than 1B param) will be an interesting and motivating example.

---

I agree that using meta-learning could be beneficial, but I don't understand the advantages of modeling with Bayesian meta-learning specifically. From an uncertainty perspective, it makes sense, but it's still possible to "jointly learn the source task" without a Bayesian approach. I'm particularly concerned about whether this proposed sophisticated sampling technique will truly scale with large models.

### Questions
See the question above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a novel hierarchical Bayesian model to tackle the cross-task PEFT knowledge transfer problem with meta-learning. The proposed LiFT approach introduces a SGLD-Gibbs sampling algorithm for efficient training and an online EM algorithm to maintain a Gaussian mixture representation of the posterior samples in an online manner. This method is evaluated on both NLP and vision tasks, and the results show improved performance over several baselines.

### Strengths
*  The paper tackles the cross-task PEFT knowledge transfer problem, which is a relevant and important topic in meta-learning and fine-tuning large models.
*  The paper is well written and well structured. The design concept is clear from the very beginning. The reader is guided through the method step-by-step and the theoretical foundations are supported by the experiments.
*  The integration of Gibbs sampling into SGLD and the assumptions made to approximate the posterior (all the variables are visited a sufficient number of times and frequently) are valuable.
*  The proposed approach can also be applied when pre-fine-tuned models are already available, which is valuable for knowledge reuse.

### Weaknesses
 *  The meta-learning baselines considered in the experiments are limited. I recommend including more recent deterministic and bayesian meta-learning approaches. Some examples, but not restriced to these, are SNAIL [2], ProtoNet [3], and MetaQDA [4]. It is important to compare against methods that are directly applicable to the same problem setting, especially those that have shown strong performance in few-shot learning scenarios. The current selection does not fully represent the breadth of available meta-learning techniques.
*  The results do not include standard deviations, making it difficult to assess whether the improvements with LiFT are statistically significant. Without measures of variance, it is impossible to determine if the observed performance gains are due to the proposed method or simply random fluctuations. This lack of statistical rigor weakens the claims of superiority.
*  While the work addresses several challenges, it also has some limitations, such as the joint training on the training tasks, which can be infeasible for large-scale datasets. The authors might consider adding a limitations section to acknowledge this constraint and any other potential challenges the method faces. The computational cost associated with joint training could be a significant barrier to adoption in practical scenarios.
*  It is unclear which architectures and hyperparameters are used for the meta-learning baselines. I assume that, for a fair comparison, ViT-B/16 was employed. However, MAML is generally inefficient when adapted to large feature extractors due to the difficulty of finding an optimal meta-initialization, which scales with the overall parameter space. This lack of clarity makes it difficult to assess the fairness of the comparison and the generalizability of the results. The specific choices for MAML, especially given its known challenges with large models, need to be explicitly stated.
*  A single inner step is used for MAML and its variant. While this reduces the computational cost, it is unclear if these results reflect the best possible performance for MAML, As noted in [1], MAML typically benefits from multiple inner loop updates. The choice of a single inner loop might be a significant factor limiting the performance of MAML, and it is crucial to explore the impact of this hyperparameter on the overall comparison.

### Questions
*  How does the choice of $\sigma$ and $\beta$ impact on the model performance? 
*  In Figure 4 and the related discussion in line 742, it does seem that SGLD converges faster than SGLD-Gibbs especially for a low number of iterations. Could the authors clarify how to interpret this figure?
*  Could the choice of parameters selected for meta-learning in the MAML-based baselines be explained in more detail?
*  Could a comparison with MAML using 5 inner loops be provided to ensure that performance is not affected by the choice of a single inner loop? If conducting this experiment is not feasible due to time constraints, could an estimate of the time and computational resources required to complete it (based on the time taken for 1 inner loop) be provided?

### Soundness
3

### Presentation
4

### Contribution
3
