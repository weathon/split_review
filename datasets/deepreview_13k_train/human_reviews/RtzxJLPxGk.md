# Adapprox: Memory Efficient Optimization via Adaptive Randomized Low-Rank Approximation

- Decision: Reject
- Scores: 5, 5, 8, 6, 8

## Abstract
As deep learning models expand, adaptive learning rate algorithms such as Adam face significant memory consumption challenges due to the need to store of optimizer states, including first and second moment data. Existing memory-efficient methods such as Adafactor and CAME often compromise approximation accuracy with their constant rank-1 matrix factorization techniques. In response, we introduce Adapprox, a novel optimizer that employs adaptive randomized low-rank matrix approximation to more effectively and accurately approximate the second moment. This method dynamically adjusts the rank used for approximation across iterations and weight matrices, mitigating the increase in computation burden while maintaining comparable accuracy. In experiments with GPT-2 and BERT, Adapprox achieves substantial memory savings compared to AdamW and surpasses other memory-efficient counterparts in convergence iterations and downstream task performance, with only a modest increase in the overall latency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents Adapprox, a memory-efficient optimization algorithm that reduces memory usage through factorization of the second moment matrix in the Adam algorithm. The key distinction from previous approaches, such as Adafactor and CAME, lies in its adaptive rank selection capability during training, whereas earlier methods were limited to rank-1 approximations. To enable this dynamic rank adjustment during training, the authors incorporated a fast randomized SVD decomposition algorithm. The method's performance and computational efficiency are evaluated through experiments on pre-training and fine-tuning of GPT-2 and BERT models.

### Strengths
1. Given the current trends in model scaling, the chosen problem of memory-efficient optimization is highly relevant and represents an important research direction.

2. The Streamlined Randomized Subspace Iteration algorithm demonstrates good performance in terms of both computational efficiency and approximation quality, with potential applications across various domains.

3. The observation regarding singular values of the second moment matrix is particularly insightful, making the proposed higher-rank factorization algorithm both novel and valuable.

### Weaknesses
1. The quality of experimental sections, including setup, descriptions and results presentation (both in Sections 3.2 and 4), requires improvement. See specific concerns, questions and suggestions in the section Questions below.

2. The absence of experimental code is a notable limitation, particularly since one of the paper's main contributions is the efficient implementation of the Streamlined Randomized Subspace Iteration algorithm.

3. The comparison baselines could be expanded to include other recent memory-efficient optimization algorithms, such as those presented in [1] and [2].

[1] Zhao et al., 2024. GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection. https://icml.cc/virtual/2024/poster/33390

[2] Zhang et al., 2024. Adam-mini: Use fewer learning rates to gain more. https://arxiv.org/abs/2406.16793

### Questions
Major concerns:

1. Section 3.2 requires clarification regarding the use of Adafactor in experimental comparisons. As Adafactor is basically an optimization algorithm [1] rather than a matrix decomposition method, its inclusion requires further explanation. Therefore, it's unclear what exactly is being compared in Figure 2:

* In Figure 2(a), what is meant by Adafactor "approximation"? How exactly is it computed?
* In Figure 2(b), what is Adafactor time? Is this the time of an Adafactor optimizer step? If so, comparing an optimization algorithm step with a matrix decomposition algorithm seems incorrect.
* Also, In Figure 2(b), it's impossible to discern the difference between Adafactor and S-RSI. I would advise the authors to change the presentation, for example, by providing a table instead.

2. Regarding Figure 4, several clarifications are needed:

* What sequence length was employed in the experiments? For language model training, the total batch size measured in tokens is a crucial parameter (see, for example, Table 2.1 in [2]).

* The hyperparameter selection process described in lines 393-399 requires elaboration. The term "uniform training parameters" needs clarification - does this indicate identical hyperparameters across all methods? Please also specify the methodology for "empirical testing": Were these parameters optimized for AdamW or Adapprox? Additionally, the hyperparameter search space should be detailed. This concern is particularly relevant for CAME, as the results (especially in Figure 4c) show initial superiority but deteriorating performance in later stages. This pattern often indicates a potentially sub-optimal (too large) learning rate choice.

* The simultaneous reporting of both perplexity and evaluation loss appears redundant, given that perplexity is simply the exponential of the evaluation loss.

* Figure 4's current visualization makes it challenging to distinguish between Adam, Adafactor, and Adapprox performance. I would suggest supplementing the figure with a table presenting final performance metrics for clearer comparison.

3. Regarding Table 3, the choice of zero-shot testing for non-instruct models raises concerns. Unlike instruct-tuned models that are designed for direct task completion, non-instruct models are highly sensitive to prompt engineering, making zero-shot evaluation potentially unreliable. I suggest to the authors:

* Justify why this evaluation setup is appropriate (e.g., by citing similar studies that use zero-shot accuracy for non-instruct models of comparable size)
* Provide either a detailed description of their zero-shot testing setup or reference the established protocol they followed, if any

4. Regarding Section 4.3 and Table 5:

* The experimental objective is unclear. If the purpose was to evaluate the optimizer's fine-tuning performance, why weren't all models initialized from the same starting point (e.g., the official BERT checkpoint)? The current setup, using different pre-trained results, creates uneven initial conditions and potentially biases the comparison.

* The comparison methodology appears incomplete, particularly the absence of PEFT methods. Given the paper's focus on memory efficiency, PEFT would serve as a natural and important baseline.

* The experimental details are insufficient - specifically, the hyperparameters used in these experiments should be explicitly stated.

Minor concerns:

1. Regarding Algorithm 3, line 347, where the square root of $V_t$ is computed: This operation implicitly assumes that all entries in $V_t$ are non-negative. However, since the $QU^{\top}$ decomposition used in line 344 is an approximation of truncated SVD rather than an exact representation, there's a concern about potential negative entries in this product $QU^{\top}$ (due to the approximation errors and floating-point precision errors) and hence in $V_t$. Could the authors please clarify how this edge case is handled or, preferably, provide a proof or explanation for why negative entries cannot occur in $V_t$ despite the approximate nature of the decomposition?

2. The paper would benefit from an additional ablation study on rank adaptation necessity. Given that the system already allocates memory for $k_{max}$ at the start of the training (line 377), maintaining this fixed rank throughout might potentially yield better performance, eliminating the need for dynamic adaptation.

3. Several typos and suggestions regarding writing:

* There's an inconsistency between Table 5 and Section 4.3: one mentions GPT 345M while the other refers to BERT 345M.

* The dimensions of matrix $U$ are inconsistent between line 161 and line 195. Adding explicit dimensions in Algorithm 1 also would be helpful.

* The units for Mean Computation Time in Figure 2(b) are not specified.

* In Algorithm 3's Inputs, $V_0$ is listed as an $m\times n$ matrix, suggesting this matrix $V$ is maintained in memory throughout training. It would be clearer to explicitly list matrices $Q$ and $U$ instead, as they are the only ones stored between optimization steps.

[1] Shazeer & Stern, 2018. Adafactor: Adaptive learning rates with sublinear memory cost. https://proceedings.mlr.press/v80/shazeer18a/shazeer18a.pdf

[2] Brown et al., 2020. Language Models are Few-Shot Learners. https://arxiv.org/abs/2005.14165

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes a strategy for reducing the memory consumed by the second moment buffer in Adam. Inspired by Adafactor, which computes a rank-1 approximation to the second-moment buffer matrices in Adam, this work computes a rank-r approximation using a randomized SVD, thereby achieving a desirable tradeoff between memory utilization and model performance. The decomposition rank, "r", is updated dynamically during training by simply measuring the approximation error of the low-rank factorization. Numerical results provided for GPT2 and BERT models, primarily comparing to Adafactor and CAME (an uncertainty aware variant of Adafactor).

### Strengths
1. Clarity: The paper is well written and easy to understand.
2. Clarity: The method is conceptually simple and well motivated.
3. Quality: Numerical results demonstrate promising performance, achieving strong performance with limited computational overhead due to computing a higher-rank approximation of the second moment buffers compared to Adafactor and CAME.
4. Significance: The paper is likely to be of interest to a broad audience, and tackles an important problem reducing the memory footprint of language model optimizers.

### Weaknesses
 * Computation times for higher rank decompositions are quite flat in the ablations (Figure 2b and Table 1); this is attributed to parallelization on the GPU, but, how does this time actually scale during training when the GPU supposedly has high SM occupancy?
* It seems a little odd that all the validation curves in Figure 4 (including those using different optimizers), line up perfectly, down to every minute jump or dip in the loss and perplexity.

### Questions
* Please investigate issues in the training runs used to produce Figure 4.
* Please report the ablations examining training time with higher rank decompositions and various model sizes; the idea is to understand how the rank affects the decomposition time during training (not just on an idle GPU).
* Consider adding memory utilization and training time in Table 3 for all methods; this will provide some insight into the relative memory utilization between Adafactor and the proposed method.
* Consider including experiments demonstrating the effect of the rank decomposition R on memory utilization for the various model sizes.

Provided further confidence in the numerical performance of the method, I am willing to increase my score.

### Soundness
2

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
4

### Summary
This paper introduces Adapprox, a memory-efficient optimizer designed to address memory consumption challenges in large-scale model training. It uses an adaptive randomized low-rank approximation for the second moment. 

Problem & Motivation: Large models like GPT-3 and BERT demand substantial memory due to optimizers such as Adam, which store both first and second moments. Existing memory-efficient methods (e.g., Adafactor and CAME) compromise accuracy by relying on constant rank-1 approximations. Adapprox is proposed to retain performance while minimizing memory.

Methodology: The method leverages low-rank characteristics in second-moment matrices, reducing memory usage without excessive computation costs. Instead of fixed-rank approximations, Adapprox uses an adaptive rank that adjusts dynamically based on iteration needs. The rank is adjusted according to an error threshold, and an exponential averaging mechanism stabilizes updates. Adapprox balances memory savings with approximation accuracy by computing approximations using the Streamlined Randomized Subspace Iteration (S-RSI) method.

Experiments & Results: Adapprox was tested with models like GPT-2 and BERT, showing significant memory reductions and superior performance (in terms of convergence and validation loss) over AdamW, Adafactor, and CAME. Fine-tuned models trained with Adapprox achieved high accuracy across NLP tasks, outperforming other memory-efficient optimizers. Adapprox incurred a modest increase in latency (~6%) but maintained significant memory savings.

Conclusions: 
Adapprox is presented as a balanced solution that provides substantial memory efficiency and high performance in model training. The paper suggests future work on reducing the frequency of rank adjustments to optimize computational efficiency further. This optimizer is positioned as a promising approach to training large models with less memory and minimal performance trade-offs compared to state-of-the-art optimizers.

### Strengths
Originality:
The paper presents Adapprox, an optimizer that utilizes adaptive low-rank approximation for the second moment in large-scale model training. This method flexibly modifies the rank throughout the training process, achieving a balance between memory efficiency and accuracy. This flexibility sets Adapprox apart from static methods such as Adafactor and CAME. The combination of Streamlined Randomized Subspace Iteration (S-RSI) and Adaptive Rank Selection (AS-RSI) algorithms improves both computational efficiency and precision in low-rank approximations, showcasing the approach's novelty.

Quality:
Thorough experiments on models like GPT-2 and BERT validate this approach, showing notable memory savings and better convergence rates against optimizers such as AdamW, Adafactor, and CAME. The paper includes in-depth assessments of memory utilization, convergence patterns, and performance on downstream tasks, providing strong proof of Adapprox’s efficacy. The technical descriptions of S-RSI and AS-RSI are clearly articulated, accompanied by understandable pseudocode, which enhances reproducibility and comprehension.

Clarity:
The paper features a clear structure, progressing logically from problem motivation through methodology and experiments to conclusions. Technical concepts are articulated effectively and supported by equations and pseudocode that facilitate understanding. The experimental setup is thoroughly detailed, while the results are illustrated with informative figures and tables that help clarify the findings.

Significance:
Adapprox tackles a significant issue in training large-scale models by lowering memory usage while maintaining performance, greatly enhancing its relevance in the field. The optimizer's adaptive characteristics enable it to respond to different training conditions, which could result in more efficient training methods. This strategy has real-world implications for implementing large models in resource-limited settings, expanding the reach of advanced AI technologies.

### Weaknesses
 Limited Comparison with Adaptive Rank Techniques:
Although Adapprox presents a method for adaptive low-rank approximation, the paper lacks a comprehensive comparison with other adaptive rank optimization techniques. A detailed examination against recent studies on adaptive low-rank or memory-efficient methods that utilize varying ranks would enhance the originality and rigor of this work.
An in-depth examination of the latest developments in adaptive approximation methods and low-rank optimization would offer readers clearer insights into how Adapprox compares to existing techniques beyond just Adafactor and CAME.

Complexity in Explanation of Adaptive Mechanism:
The explanation of the Adaptive Rank Selection (AS-RSI) mechanism would benefit from condensing and providing extra context, particularly for those not familiar with randomized SVD or subspace iteration. While it's organized well, the technical specifics about rank adjustment thresholds and error ratios could be clarified with a more intuitive or overarching summary before presenting the equations and pseudocode. Making this section more approachable could involve adding a flowchart or offering a simplified, step-by-step outline of AS-RSI’s rank adaptation process.

Analysis of Latency and Efficiency Trade-offs:
Adapprox shows remarkable memory efficiency, accompanied by only a slight rise in latency; however, this latency-memory trade-off warrants a more detailed analysis. Investigating how latency increases with larger ranks or deeper architectures would shed light on the optimizer’s capabilities in practical scenarios. Additionally, given the results indicate a slight increase in latency with Adapprox, breaking down the computational costs associated with S-RSI and AS-RSI components could help identify which factors have the greatest impact on the additional time cost.

Impact of Rank Adaptation on Convergence:
Further investigation into how rank adaptation affects convergence rates, especially in relation to different error thresholds and AS-RSI parameters, is warranted. Although the experiments show advantages in convergence, examining the impact of rank selection on convergence stability would provide additional insights. Conducting an ablation study that alters error thresholds and monitors convergence speed alongside final model performance would also be beneficial. This type of analysis could provide clear guidance for practitioners seeking to optimize Adapprox’s configurations according to their memory and accuracy requirements.

Scope of Downstream Tasks:
The downstream tasks tested are well-chosen for NLP, but expanding to other domains (e.g., vision tasks or different LLM architectures) could strengthen claims about Adapprox’s generalizability. Given the optimizer’s potential for a wide range of models, testing on a broader selection of model types could emphasize its applicability beyond the NLP-focused experiments.

### Questions
Comparison with Adaptive Rank Methods:
Can you elaborate on how Adapprox contrasts with modern adaptive-rank or low-rank approximation techniques regarding memory-efficient optimization? For example, approaches like GaLORE and CAME utilize low-rank strategies but depend on a fixed rank. Are there other adaptive-rank methods besides these that you’ve considered or think are pertinent to your methodology? Additionally, a more in-depth comparison with GaLORE, which emphasizes memory-efficient optimization via low-rank gradient projections, would clarify Adapprox's distinctive contributions.

Clarification on Adaptive Rank Selection (AS-RSI):
The adaptive rank selection mechanism within AS-RSI is crucial for Adapprox’s adaptability. Can you elaborate on how the error threshold and rank modifications are established? For instance, is there an empirical method for selecting threshold values, or are they adjusted specifically for each model? 

Exploration of Latency and Memory Trade-off:
Considering the minor increase in latency with Adapprox, could you share more detailed insights on how various algorithm components, such as S-RSI and AS-RSI, add to this overhead? Analyzing the added computational time could help us pinpoint potential optimization areas. Would you be willing to run experiments with different model sizes or ranks to investigate how latency varies and better understand the algorithm’s effectiveness for diverse large models?

Convergence Analysis and Ablation Studies:
Can you elaborate on how rank adaptation influences convergence? Specifically, how responsive are the outcomes to changes in the error threshold applied in AS-RSI? Conducting an ablation study that varies error thresholds and demonstrates their effects on memory efficiency and convergence stability would bolster your assertions regarding the effectiveness of the adaptive rank. Would you like to include this to substantiate AS-RSI’s adaptive mechanism further?

Availability of Code for Reproducibility:
Will you provide code to support reproducibility? If yes, can you suggest specific guidelines or configuration settings for those looking to replicate your results, especially concerning rank selection and error thresholds?

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
This paper introduces Adapprox, a novel approach that leverages randomized low-rank matrix approximation to achieve a more effective and precise approximation of Adam’s second moment. The proposed method is more memory-efficient than Adam/AdamW and achieves greater accuracy than Adafactor/CAME due to its refined second-moment estimation. Additionally, the authors integrate a power iteration technique and an adaptive rank selection mechanism to further enhance the optimization process. Empirical studies on Transformer optimization are conducted, showcasing the effectiveness of the proposed method.

### Strengths
1. The integration of randomized low-rank matrix factorization into Adam optimization is an interesting idea, though its novelty remains uncertain.
2. Adapprox offers a flexible trade-off between memory usage and performance, which I consider to be an important contribution.
3. The paper is generally well-written, with a clear and easy-to-follow presentation.

### Weaknesses
1. Several design choices in this paper appear empirical and lack theoretical justification, such as the selection of $k_0$, $k_{min}$, $k_{max}$, $l$, and $p$. Additionally, these choices have neither been validated on larger-scale cases, such as optimizations for models with over 1 billion parameters, nor supported by any theory.
2. Certain techniques that are orthogonal to low-rank matrix factorization, such as CAME or quantization, are not explored in combination with the proposed method.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a new optimizer ADAPPROX that can lead to a reduction of memory requirement needed to train a neural network.  The optimizer is tested on BERT and GPT2 pretraining tasks and achieved comparable performance with AdamW.

### Strengths
The paper presents an interesting approach to overcome the memory limitation of Adam and AdamW optimizer, especially related to training large language models. 

The paper presents sufficient details related to the algorithm itself, making the paper easy to follow and comprehensive.

The paper's approach, to me, is novel and the impacts are valuable.

### Weaknesses
The paper presents an interesting approach to overcome the memory limitation of Adam and AdamW optimizer, especially related to training large language models.

The paper presents sufficient details related to the algorithm itself, making the paper easy to follow and comprehensive.

The paper's approach, to me, is novel and the impacts are valuable.

The experiment setting could be more comprehensive to illustrate the benefits, for example,  It would be great to have SGD baseline in the experiment section, to show how impactful the memory reduction is, as well as the training speed comparison.

### Questions
How will the proposed optimizer work in multi-node large scale training? Can author comment on whether there will be additional limitations or benefits of the approach in multi-node training scenario?

### Soundness
3

### Presentation
4

### Contribution
3
