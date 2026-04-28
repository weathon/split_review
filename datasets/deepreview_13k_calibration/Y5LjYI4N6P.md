# Efficient stagewise pretraining via progressive subnetworks

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 6, 8, 5

## Abstract
Recent developments in large language models have sparked interest in efficient pretraining methods. Stagewise training approaches to improve efficiency, like gradual stacking and layer dropping \citep{reddi2023efficient, zhang2020accelerating}, have recently garnered attention. 
The prevailing view suggests that stagewise \emph{dropping} strategies, such as layer dropping, are ineffective, especially when compared to stacking-based approaches. This paper challenges this notion by demonstrating that, with proper design, dropping strategies can be competitive, if not better, than stacking methods. 
Specifically, we develop a principled stagewise training framework, \emph{progressive {\layerdrop} training}, which only trains subnetworks within the model and progressively increases the size of subnetworks during training, until it trains the full network. We propose an instantiation of this framework --- \textbf{Ra}ndom \textbf{P}art \textbf{Tr}aining ({\method}) --- that selects and trains only a random subnetwork (e.g. depth-wise, width-wise) of the network at each step, progressively {\em increasing} the size in stages. We show that this approach not only generalizes prior works like layer dropping but also fixes their key issues. Furthermore, we establish a theoretical basis for such approaches and provide justification for (a) {\em increasing} complexity of subnetworks in stages, conceptually diverging from prior works on layer dropping, and (b) {\em stability} in loss across stage transitions in presence of key modern architecture components like residual connections and layer norms. Through comprehensive experiments, we demonstrate that {\method} can significantly speed up training of standard benchmarks like BERT and UL2, up to 33\% compared to standard training and, surprisingly, also shows better downstream performance on UL2, improving QA tasks and SuperGLUE by 1.5\%; thereby, providing evidence of better inductive bias.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper leverages the idea of stochastic depth for the training of language models. The paper proposed a particular training schedule (RAPTR) suitable for training with stochastic depth, where the depth of the network increases over the course of model training, ultimately training the full model. As a significant number of layers are skipped, this translates to direct gains in wall-clock time. The proposed RAPTR training scheme was evaluated on two encoder-decoder language models including BERT and UL2. Results on a small set of benchmarks indicate competitive performance w.r.t. the full model training and even outperforms it in some cases due to this acting as a regularization scheme.

### Strengths
- The paper is well written
- The approach is well motivated by the literature on stochastic depth
- The obtained results on a small set of benchmarks indicate either competitive or superior performance than the control (i.e., full model training) and directly translate to savings in wall-clock time

### Weaknesses
 - The paper only focused on encoder-decoder models. I would like to see similar results on simple decoder-only language models, which are much more prevalent.
- Evaluation on only a limited number of tasks. I would expect evaluations on a very large number of tasks from eval-harness as evaluation costs are relatively modest in comparison to the training cost.
- Important implementation details are scattered throughout the paper. I would expect all of the details such as sequence length, and batch sizes to be specified at a single location to make it easier to understand.
- Simple implementation details buried in the appendix such as how to provide gradients to all the layers, which I expect to be a part of the main paper. It can be significantly shorter though by just stating that we need a way to compute gradients for all the layers even if that layer didn't participate in that round. Perhaps just include another trivial implementation that works even in distribution reduction i.e., to multiply block $i$ output with $\alpha_i$. This ensures that gradient is computed for all parameters, however, without any gain in wall-clock time.

### Questions
- Unclear how the authors decided to take specific mixtures of specific datasets. Was there no off-the-shelf dataset suitable for this analysis (such as FineWeb / FineWeb-edu)?

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
This paper proposes a stagewise pretraining method, progressive subnetwork training. This method randomly selects subnetworks to train in each stage and gradually increases the size of the selected subnetworks in stages. They also discussed why layer dropping can hurt the models’ ability to capture complex correlations in the data. The authors verify the effectiveness of the proposed progressive subnetwork training method by pretraining BERT and UL2.

### Strengths
The proposed progressive subnetwork training method is straightforward and easy to understand.
The experiments show that the proposed method is simple but effective.
The paper is well-structured and written.

### Weaknesses
It is good that try to theoretically explain why layer dropping methods cannot achieve good performance. However, the illustration setting that using Polynomial learning and 2-layer residual network is too naïve, which makes the conclusion less convincing. The analysis lacks depth and does not consider the complex interactions within deep networks. The chosen example is overly simplistic and does not translate well to the complexities of models like BERT or UL2. The theoretical justification needs to be more robust and consider more realistic scenarios, such as the impact of different activation functions and the depth of the network. The current analysis is insufficient to support the claims made about layer dropping's limitations in capturing complex correlations.

### Questions
Why can RaPTr achieve better performance than the baseline full-model? The baseline full-model is well-trained and is supposed to achieve the best performance.
How about the performance when more FLOPs are reduces? For example, reduce the FLOPs of the baseline model to half or 1/3?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper argues that stagewise dropping strategies, such as layer dropping, can be effective for efficiently training large language models. The paper proposes a stagewise training framework of progressively growing a subnetwork and shows that it generalizes layer dropping. They theoretically illustrate the effectiveness of this strategy and moreover empirically demonstrate effectiveness in speeding up training on standard benchmarks.

### Strengths
The problem of efficient training is of increasing importance as we scale to larger models and data sets. The paper is well-written and comprehensive, covering theoretical justification, detailed numerical analysis, and implementation guidelines.

### Weaknesses
In the numerical evaluations, the selected settings of Rel. FLOPS seemed somewhat arbitrary (e.g., fixing to 1.33x for Table 1). It would be nice to get some intuition why these were chosen and the sensitivity to these experimental settings (e.g., how do the results hold as we sweep the Rel. FLOPS). Specifically, the paper lacks a clear explanation of how the specific Rel. FLOPS values were derived for each experimental setup. For instance, while the 1.33x reduction is mentioned, the connection to the underlying schedule (e.g., equal stage lengths) and the resulting average layer usage is not explicitly detailed in the main text. This makes it difficult to assess the generality of the findings and how they might apply to different model sizes or training regimes. Furthermore, the paper should include a more thorough exploration of the trade-off between computational savings and model performance as the Rel. FLOPS are varied. The current analysis only provides a single point of comparison, which limits the understanding of the method's behavior under different computational constraints.

### Questions
Please see Weaknesses.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a new approach to stage-wise pre-training of large models to improve the efficiency and computational cost. The main idea is to train random subnetworks within a base network for each stage of training and increase the complexity of the subnetworks as training progresses. Experimental results show some improvement in language models. Additionally, they include theoretical work to support their method, using a simple example of learning a polynomial function and demonstrate stability in stage-wise training.

### Strengths
1. The importance of improving pre-training efficiency is well justified, and it’s clear that addressing this issue is valuable. 

2. Efforts have been made to offer theoretical justifications for the method.

### Weaknesses
1. For experiments on BERT, only a base model is used and the improvements are relatively marginal compared to other stacking or dropping methods and only 3 tasks in GLUE are reported. Some improvements for UL2 are also within the variance of the baseline.

2. Although the polynomial example illustrates how RAPTR learns lower and higher degree components, it is overly specific and lacks sufficient theoretical support to convince me that RAPTR is better than PLD. The theoretical analysis is limited to a very specific polynomial form, and it's unclear how this translates to the complex, high-dimensional feature spaces encountered in real-world language models. The analysis does not address the potential for overfitting or instability when learning these hierarchical features in a deep network.

3. Theorem 5.3 shows that the loss gap $|L_2(F) - L_1(F) |$ is upper bounded by the stability of the network and that is used to show that the losses between stages can be small for linear models in RAPTR. However, it is not clear if the same may hold for other stacking or dropping methods. The theoretical analysis does not provide a comparative analysis of the loss gap bounds for other stage-wise pre-training methods, making it difficult to assess the relative advantage of RAPTR. Without such a comparison, it's hard to conclude that the stability properties are unique to RAPTR.

4. The empirical verification with BERT in section 5 does not seem to support the theory as in Fig 3, there is no linear decrease in loss gap as depth of model increases.

Formatting: Many typos, for example line 482: "layernorm is enabled or not respectively" should be the other way around, and figures with subplots are not labelled clearly.

### Questions
1. Is there a generalisation beyond the polynomial example for RAPTR capturing higher or lower degree components in each stage?

2. Can it be shown that the loss gap for other stacking or dropping methods are either unbounded or have a larger upper bound than RAPTR?

3. Can all GLUE tasks be reported together with results on BERT-large as a base model is quite small and easy to pre-train, while RAPTR is aimed at improving pre-training efficiency. More convincing experimental results using other models are also appreciated as the current results do not persuade me to use RAPTR. 

4. Are we able to use RAPTR for fine-tuning on downstream tasks instead of pre-training?

### Soundness
2

### Presentation
2

### Contribution
2
