# Confounder-Free Continual Learning via Recursive Feature Normalization

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Confounders are extraneous variable that affect both the input and the target, resulting in spurious correlations and biased predictions. Learning feature representations that are invariant to confounders remains a significant challenge in continual learning. To remove the influence of confounding variables from intermediate feature representations, we introduce the Recursive Metadata Normalization (R-MDN) layer, which can be integrated into any stage within deep neural networks (DNNs). R-MDN performs statistical regression via the recursive least squares algorithm to maintain and continually update an internal model state with respect to changing distributions of data and confounding variables. Since R-MDN operates on the level of individual examples, it is compatible with state-of-the-art architectures like vision transformers. Our experiments demonstrate that R-MDN promotes equitable predictions across population groups, both within static learning and across different stages of continual learning, by reducing catastrophic forgetting caused by confounder effects changing over time.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies an interesting problem of removing the effect of known confounding variables from intermediate feature representations in neural networks. It modifies MDN to deal with sequentially available data by estimating the linear residual model through the recursive least squares method instead of the least squares method used in MDN which needs access to the entire data before the training. Through various experiments, the authors emprically demonstrated that the proposed method R-MDN reduces the confounder effects significantly.

### Strengths
The authors resolve the limitations of MDN to deal with sequential data and allow parallel processing of individual input examples. Replacing the least squares method in MDN with the recursive least squares method is a reasonable choice in the sequential nature of data, and it empirically demonstrated the effective removal of confounder effects on the learned features. The authors also visualized the experimental results well.

### Weaknesses
Despite the empirical effectiveness, this paper lacks a clear explanation for the intuition behind the linear residual model and why estimating the coefficient $\beta$ through (recursive) least squares is appropriate. While the authors cite prior work using linear models for confounder removal, they do not justify why a linear model is sufficient for this specific problem, especially given the non-linear nature of neural networks. The paper should include a discussion of the limitations of this assumption and when it might fail. Also, RLS provides different solutions from LS even after seeing the same number of samples if we start with $P(0)=\epsilon I$ for $\epsilon\neq0$. Thus, R-MDN and MDN produce different estimations on $\beta$ even for the full-batch data. An explanation of this difference and any (dis)advantages of the solution found by R-MDN compared to that of MDN's solution are missing in the paper. The paper should also discuss how the choice of $\epsilon$ affects the final estimate and convergence. 

In the methodology section, some notations are not defined well. ex) $r$ is used for two different residuals. For the second one, $r=z-\tilde{x}\tilde{\beta}_x$ is more natural than $r=\tilde{x}\tilde{\beta}_x-z$ (although the negative sign can be absorbed into the weight parameter of the next layer.) $X_i$ should be explained to be the $i$-th row of $X$. The current method is presented for a single 1-dimensional confounder variable. While the authors mention that it can be extended to multi-dimensional confounders, they do not provide details on how this extension would be implemented or whether there would be any challenges associated with it.

### Questions
This reviewer wonders about the comparison of computational complexity and memory cost between R-MDN and the baselines, especially MDN and P-MDN.

### Soundness
3

### Presentation
4

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
The work proposes to extend "Metadata Normalization" (Lu et al., 2021) for
continual learning by performing batch-wise updates to the general linear model
solution, specifically using the Sherman-Morrison-Woodbury formula to add newly
observed data to the inverse scatter matrix, where also a regularization term is added.
The static MDN, as well a previous continual version, are compared in two static
experiments. Two more experiments show the performance in a continual setting.

### Strengths
- The paper is clearly written.

- The paper provides a broad set of related work.

- Experiments are conducted carefully (with trials and variance in mind).

- The plots are of good quality.

- Various details on the experiments are provided in the appendix.

### Weaknesses
 - **Missing details in method:** In a continual learning setting, it is true
  that the update of the inverse metadata scatter can be done exactly using the
  Woodbury formula without knowledge of previous data. However, as the $z_i$
  change during training, the $X^T z$ ($Q(N+1)$) in Eq. 1 must be recomputed in
  its entirety. This is in conflict with the continual learning setting, as both
  the required output $z_i$, as well as the metadata $x_i$ of previous data is
  assumed to not be available. Thus, this is not an issue in the input space,
  but only in feature space. I could not find this issue being addressed
  anywhere in the manuscript, but this seems to be the most important part of
  the updated algorithm, as it would otherwise correspond exactly to MDN.

 - **Unfocused experiments:** In continual learning, the most interesting
  objective is to quantify the error caused by the constraints of this setting.
  For this work, this means to compare directly with MDN on the full dataset,
  which is done only in Section 4.2 Figure 5b. It would be meaningful to
  directly see the error caused by the iterative updates instead of the
  performance in the static setting. The other experiments in Section 4.2 seem
  to only show this implicitly. The work should focus its empirical analysis
  more on the contribution in continual learning, which I understand as its main
  selling point.


The work proposes an approach to expands MDN to a continual learning setting,
but does so without specifying the important details necessary to do so, but
instead only argues that iterative updates to the metadata scatter inverse using
the Sherman-Morrison-Woodbury formula. The empirical experiments do not show
the error caused by the approximation used in the continual setting.
Without these two main points, I fear that this paper's contribution does not
justify an acceptance.

### Questions
- How do you solve the issue with previous data $z_i$ and $x_i$ required to be
  known to compute the residual?

- How large is the error caused by the approximation made by the continual
  setting?

- Is the black bar in Figure 4 plot b the variance? What is the height of each
  block? It would be good to explain this.

- In Figure 4, why does MDN have such a high variance (assuming the bars)? Is this related to the
  small batch size?

### Soundness
1

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
2

### Summary
The paper presents Recursive Metadata Normalization (R-MDN), a normalization layer designed to reduce the impact of confounders in deep neural networks (DNNs) in both static and continual learning contexts. R-MDN uses the recursive least squares (RLS) algorithm to maintain and update model parameters iteratively. The method demonstrates its effectiveness on both synthetic and real-world datasets.

### Strengths
1. The idea of R-MDN is novel and interesting.
2. The idea can be generalized to fields beyond medical context.

### Weaknesses
1. This paper spent most of experiment section on the synthetic data part, while experiments on the real data are limited. More experiments and discussions on the real data may make the argument stronger.
2. The experiments on the real world data are not convincing. First, it's a little difficult to read the metric number from the plot --- a table (like table 1) containing accuracy and other related metrics is appreciated. Second, it seems on all the real world experiments, the new method has an accuracy drop. How should we make trade-off here? I think we need more discussions on the benefits this new method could bring, and why the benefits can justify the accuracy drop. 
3. What's the computational overhead of the proposed method compared with baseline?

### Questions
See weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes a new method called Recursive Metadata Normalization (R-MDN) to address the problem of confounding variables in deep neural networks. As confounders influence both the input and the target, this can result in spurious correlations that subsequently distort the true underlying relationships within the data. Furthermore, this can lead to biased and inaccurate predictions, particularly in medical studies where demographic factors like age, sex, and socioeconomic background can affect the outcome. The proposed R-MDN is in the form of a normalization layer that can be inserted at any stage within a NN in order to remove the effects of confounding variables from learned feature representations. It uses the recursive least squares (which has a closed-form solution) to iteratively update its internal parameters based on previously computed values whenever new data is received, allowing the model to adapt dynamically as new data flows in. The novelty of the approach is that R-MDN does not require pre-computation of statistics or batch-level estimates, making it suitable for use with vision transformers and continual learning scenarios. The authors provide a theoretical foundation for their approach, showing how R-MDN can be used to residualize the effects of confounding variables from learned feature representations. They also empirically investigate R-MDN in different experimental setups and NN architectures. In comparison to other state-of-the-art methods, such as MDN and P-MDN, R-MDN shows competitive performance. The paper evaluates R-MDN in longitudinal studies, and continual learning, and shows that R-MDN can help make equitable predictions for population groups, minimizing catastrophic forgetting due to confounders.

### Strengths
The paper is very well written and easy to follow. The introduction does a comprehensive analysis of the literature, outlining many previous approaches, highlighting their strengths and weaknesses, as well as motivating the problem at hand. The plots are well formatted (maybe Figure 1 could have a bit larger formula font for readability). Furthermore, the methodology section is clearly written and easy to follow. While going through the formulas I did not find typos. The experimental section is thorough, the experiments are thorough and plots are easily readable.

### Weaknesses
I struggle to convince myself about the contribution of the paper and the experimental results. Although the paper is well written and experiments are thorough, when comparing to the original MDN paper, I did not find much novelty in the paper. The proposed usage of working with mini-batches through and using the Sherman-Morrison-Woodbury formula does indeed allow MDN to extend to vision transformers, but I did not find a convincing experiment in the paper that solidifies this claim (also, P-MDN seems to be able to work with vision transformers, although its performance is subpar to that of R-MDN). The theoretical part in Section 3. is clear and easy to follow and does provide a simple idea but I remain unconvinced whether this idea is sufficient for a conference paper.

For example, in the synthetic dataset example, the network which is used is a 2D convolutional neural network, and possibly here is not the right playground where R-MDN would truly shine. From Table 1, we can see that R-MDN has inherited good performance from MDN and that it enjoys favorable performance, however for extremely small batch sizes (2, 16 and 64). The results for batch sizes 256 and 1024 are on parr or worse to MDN. The t-SNE visualisations of learned feature representations do not really tell much - the distribution overlap seems to have just delocalised rather than focused on one region, like in MDN, but that did not really affect my score. For example, does R-MDN perform better or comparatively for batch size 2048 (in the original paper authors use batches 200, 1000 and 2000 so I am curious).

In the ABCD sex classification example, you mention that PDS confounder is significantly larger in girls than in boys but it seems to me that the difference is not significant as the two intervals overlap (please correct me if I am wrong here): 2.175+-0.9 in girls and 1.367+0.6 in boys. The plots in Figure 4 are nice but it is really hard to tell how big is the improvement gain here. Again, the architecture used is a CNN, which I find a bit disappointing considering one of the main motivation for your work is that it can be applied with transformer architectures.

For the continuum of synthetic datasets, although all methods are very good at backward transfer, R-MDN performs better at forward transfer. I find that the plot in 5b (similar to Fig. 4a and 4b) is visually appealing, however it is hard to read how big the improvement is and what the difference is. Why did the authors choose this rather than reporting the results in a Table, akin to Table 1? Figure 5c also very confusingly conveys whether the dist. changes are significant or not, and I am not sure whether it adds much to the paper. I believe here would be beneficial to summarize the benefits of using R-MDN with a transformer architecture to using MDN with non-transformer architecture, and having baselines both for CNNs and vision transformers. The same comment as in previous paragraph goes for the Figure 6. - although the figure is very clean and visually appealing, the accuracy, dcor^2, Backward Transfer and forward transfer are portrayed as a bar chart, and we do not see whether the differences are significant, what is the actual value. It does not really give a convincing argument. Finally, I would say that although the datasets are nicely introduced, the introductions take quite a lot of space and would maybe be more beneficial in the appendix, while the authors could post further experiments, with exact numbers and more comparisons to really highlight whether R-MDN does improve performance and why in the future scientists should resort to using R-MDN rather than P-MDN (which might potentially be hard to tune) or just MDN.

### Questions
In line 48 you mention that there is a multitude of situations where some of the previous methods cannot be applied, such as MDN, but you do not mention why is this the case. The question, although it motivates R-MDN well, hangs in the air until the next section. Could you please provide a short explanation of why MDN (and other methods) cannot be applied in this part of the paper?

In line 259, you mention that you apply residualization modules after every convolution and pre-logits layer. Could you briefly explain why did you make this choice? It would be nice to motivate this choice a bit and comment whether other choices might be beneficial for certain applications.

### Soundness
2

### Presentation
4

### Contribution
2
