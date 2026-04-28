# Investigating the Pre-Training Dynamics of In-Context Learning: Task Recognition vs. Task Learning

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
The emergence of in-context learning~(ICL) is potentially attributed to two major abilities: \textit{task recognition}~(TR) for recognizing the task from demonstrations and utilizing pre-trained priors, and \textit{task learning}~(TL) for learning from demonstrations.
However, relationships between the two abilities and how such relationships affect the emergence of ICL is unclear.
In this paper, we take the first step by examining the pre-training dynamics of the emergence of ICL.
With carefully designed metrics, we find that these two abilities are, in fact, \textit{competitive} during pre-training.
Moreover, we observe a strong negative correlation between the competition and ICL performance.
Further analysis of common pre-training factors (\ie model size, dataset size, and data curriculum) demonstrates possible ways to regulate the competition.
Based on these insights, we propose a simple yet effective method to better integrate these two abilities for ICL at inference time.
Through adaptive ensemble learning, the performance of ICL can be significantly boosted, enabling two small models to outperform a larger one with more than twice the parameters.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work explores the dynamics between two abilities of in-context learning (ICL) in large language models (LLM), i.e., task recognition (TR) and task learning (TL). This paper argues that TL and TR are indeed competitive during pre-training. To show this quantitatively, the authors proposed a metric called Competition Intensity that measures the extent to which one ability exceeds the other. The paper suggests that the Competition Intensity is negatively correlated with the ICL performance, and that regulating the Competition Intensity via specific choices of pre-training factors (model and dataset size, and data curriculum) is crucial for improving ICL performance. By using this hypothesis, the paper proposes a technique to fuse small models.

The contributions are:
1) Explore the relationship between TR and TL and their impact on ICL performance,
2) Analyze the influence of the pre-training factors on the competition between TR and TL, and
3) Propose an approach to fuse small LLMs more effectively.

### Strengths
- The paper is well-written and easy to follow
- The analysis of TR and TL behaviours and their effect on ICL performance is interesting
- The fusion of small models performs comparably to larger models, making a step toward the feasibility of training LLMs with fewer resources

### Weaknesses
- The novelty of the methodology section is limited.
- There is no significant improvement observed in Table 1 compared to other fusion models, small models, and large models in terms of Accuracy
- Limited discussion, limitations and future work. It would be interesting to explore how the fusion technique performs on each of the 16 individual datasets, and possibly identify common characteristics of datasets where the technique performs well/poorly.

### Questions
- I am not sure why the TL and TR curves appear to have identical data points in both plots of Figure 1.
- Could you discuss potential mechanisms or hypotheses on why the competition between TL and TR occurs, based on your observations or existing literature
- Apart from TL and TR, discuss any limitations in your experimental design that might not fully control for other factors that might affect ICL. Please suggest potential ways to address these in future work.
- In Figure 6a, it seems $C_i^S$ tend to increase in the second phase. Could you provide more detailed analysis of the relationship between $C_i^S$ and ICL performance in this specific case, and discuss any potential confounding factors.
- In Figure 6b, there is no clear evidence that CrystalCoder-7B experiences less competition than Amber-7B. Could you provide quantitative evidence supporting your conclusion about this figure or clarify if there are specific aspects of the figure that led to this interpretation.
- In Table 1, it would be helpful to report the standard deviation of the accuracies and TFLOPs. I would also recommend to include a statistical test to evaluate the significance of the obtained results.

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
3

### Summary
The authors examine the competition between Task Learning (TL) and Task Recognition (TR) throughout pretraining, and its effect on the in-context learning (ICL) capabilities of LLMs. They show that when there exists a competition, this usually leads to stagnation in ICL capabilities or a decrease. Motivated by this, they propose an ensembling technique to between different checkpoints of the same (or different) models that performed best in TL or TR. They show that, this combination can lead to performance improvements in ICL that can rival models with even larger model parameters than the sum of the fused smaller models.

### Strengths
- The paper is well-written and easy to follow
- The paper shows a clear sign of competition between TR and TL, and its effect on ICL improvement throughout pretraining
- The authors clearly defined each metric, and defended their relevance
- They have numerous ablation studies to show the effects of factors (such as dataset size and curriculum training) to ICL (or TR/TL competition)
- They have ablation studies on various ensembling techniques to show their performance improvement is not just due to model fusion, but something more systematic. However, this may require more studies (see weaknesses)

### Weaknesses
- I believe the results on Table 2 can be better represented. Especially choosing a "random" checkpoint can be very misleading, and frankly I don't think it's necessary to look at such data point. I'm interested in the {TR or TL}_best + ICL_best checkpoints for the same models. And, ICL_best_model_1 + ICL_best_model_2 when ensembling different models.
- I also believe p-adaptive should be better motivated. I don't see the performance improvements big enough, and also Pythia-1B models, p-fixed performs significantly better.

### Questions
- Are there a few benchmarks that skew the average to Pythia-1B p-fixed instead of Pythia-1B p-adaptive? We do not observe p-fixed performing better than p-adaptive in other scenarios
- Could you compare your proposed ensembling method to other ensembling methods? (You can choose Pythia-1B + Pythia-2B final checkpoints for baselines to compare to your selection of checkpoints for ensembling)

### Soundness
3

### Presentation
4

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
This paper investigates how task recognition (TR) and task learning (TL) abilities influence in-context learning (ICL) performance in large language models (LLMs). Building on prior work by Pan et al. (2023) and Lin & Lee (2024), the authors assess TR and TL by constructing Gold, Random, and Abstract input-label pairs to isolate these abilities. They introduce several new metrics based on ICL performance across a sequence of LLM checkpoints:  (1) **competition indicator** $C_i^H$; (2) **competition intensity** $C_i^S$; (3) **cumulative intensity**, which is used to infer the dynamic interplay between TR and TL. Through a series of empirical evaluations, the authors demonstrate key insights into how these abilities interact. Additionally, they propose an adaptive ensemble method that fuses two smaller models to improve ICL performance, suggesting a promising direction for enhancing context-based learning in LLMs.

### Strengths
- The paper brings a fresh perspective to ICL by examining the roles of task recognition (TR) and task learning (TL), shedding light on how these two abilities interact and shape ICL performance.

- The authors introduce some new metrics, including the competition indicator and cumulative intensity score, which add depth to our understanding of TR and TL dynamics over time. 

- Through a comprehensive experimental setup, the paper examines model behavior across multiple checkpoints, allowing for a nuanced view of how TR and TL evolve during training. 

- The adaptive ensemble method presented is somewhat novel, selecting models based on their TR and TL strengths. By leveraging each model’s unique abilities, this approach suggests a practical way to optimize ICL performance through complementary ensemble strategies.

### Weaknesses
- The clarity of the paper could be improved to make key concepts more accessible. For instance, terms like "dynamics of pre-training" are introduced without clear definitions and make it challenging for readers to grasp the intended meaning. Also, it's encouraged to clearly highlight what are the key assumptions and intuitions more clearly in the paper.

- The paper also  lacks substantial technical novelty and depth of insight into the ICL problem. The new metrics proposed in for measuring competition indicator, intensity and dynamics heavily rely on an assumption that these metrics could be derived from the change of TL and TR scores from consequent checkpoints.  I'm not convinced that the  change of performance on checkpoints could reflect the capability of TL or TRs. It is hard to figure out what kind of training the model has gone through for each new release and version of checkpoints could be arbitrary too. Especially for large-scale models where checkpoints are not saved at every step.  How could the $\triangle$TL and $\triangle$TR evaluated on consequent checkpoints robustly tell the true capability of TL and TR, which is of interest to the audience? This reliance could limit the broader applicability and scalability of the proposed method.

- The cumulative intensity score $R_i$  used to track the dynamics of competition intensity over time, raises some concerns. Since it simply aggregates $C_i^S$  values, which are strictly positive, this score inevitably increases, potentially making it less informative as a dynamic metric.

- Key figures, such as Figure 1 and Figure 6, lack error bars and the tables do not come with standard deviations, making it difficult to evaluate the robustness of the observed trends. In the paper, the authors discuss a lot about the  "fluctuations" of the checkpoints, which in fact often can be somewhat random, and without error bars, it’s not able to tell whether these patterns are consistent or potentially artifacts.

- One fundamental assumption in this work is that the relationship between TR and TL can be inferred directly from changes in ICL ability across checkpoints. However, training conditions and checkpoint improvements are not always straightforward, and observed changes in ICL ability may not consistently reflect meaningful performance shifts. A more detailed discussion validating this assumption would strengthen the technical foundation of the method.


 - Sections 3 and 4 lack a cohesive connection, and the title of Section 4 may be somewhat misleading, as it suggests that TL and TR no longer compete. Although Section 4 introduces an ensemble model by selecting the best-performing models for TR and TL, it remains unclear whether this ensemble approach results in the highest combined TR and TL scores compared to individual checkpoints. The two chosen models are combined using simple weights inferred from their respective accuracy, but further clarity is needed on the effectiveness of this weighting approach. The experiments would be more robust if the authors included comparisons with other ensemble methods and conducted an ablation study on using fixed, non-adaptive weights (e.g., 0.5, 0.5).

- In Figure 3, the authors plot ICL performance and $R_i$  curves together, showing increasing trends. However, the increase and decrease patterns do not always align, raising questions about the strength of the correlation between ICL performance and $R_i$. More statistical analysis or validation would help clarify the relationship and strengthen the visual interpretations.

### Questions
- The paper offers very little discussion regarding the choice of the number of checkpoints. Does the method’s performance remain robust when applied with varying numbers of checkpoints? An ablation study would be beneficial to address this.

- It would be helpful if the authors could elaborate more on the intuition behind the dynamics of pre-training and clarify how studying this aspect could directly benefit in-context learning (ICL).

- A key aspect of evaluating the method is the reliability of its modeling of competition intensity dynamics $R_i$. How can we systematically assess the quality of the proposed $R_i$ score, and in what ways does this score contribute to improving ICL capability in practice?

- In the ablation study, it would be beneficial to include results for a non-adaptive ensemble baseline, as well as standard ensemble models incorporating more than two LLMs.

- The proposed metrics rely on checkpoint fluctuations to measure task learning (TL) and task robustness (TR). Would the method remain consistent and valid if checkpoints were sparse? It would be helpful to include discussion or experiments around this. 

-  It would be helpful if standard deviations could be added to the tables and figures from the paper. Could the authors provide statistical test results to determine whether the observed fluctuations are significantly different from random noise? 

- For Fig 3, the relationship between ICL performance and $R_i$ sometimes misalign in certain intervals. Is it possible to quantify the correlations between them and confirm that the positive relationship statistically hold? Additionally, a detailed discussion on potential reasons for those observed misalignments could provide valuable insights.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper studies how two mechanisms related to in-context learning (ICL), task recognition (TR) and task learning (TL), develops over the course of LLM pre-training. Through the experiments, the authors find that there is competition between the TR ability and the TL ability through the pre-training process. The authors further propose a measure to quantify such competition, and fine a negative correlation between the magnitude of such competition to the final ICL performance. The paper also studies how different factors, including parameter count, dataset size, and data curriculum affects the magnitude of the competition and ICL performance. Finally the paper proposes a method to ensemble checkpoints with best TR performance and best TL performance to get better ICL performance, outperforming the ICL performance of a larger model with more than twice the parameters.

### Strengths
- The main insight of this paper that there exists competition between TR and TL and such competition is correlated with worse ICL performance is very novel and interesting to me. Discovering this insight and investigating how different pre-training factors affect TR/TL competition already makes it a good paper, and the fact that the authors propose a well motivated method to improve ICL performance makes the paper a great one.
- The presentation of the paper is good. The authors provide a clear outline in the beginning and smoothly dives into each part of the story.
- The authors provides anonymous code which allows easy reproduction of the experiment results.

### Weaknesses
- The related work section is a little bit limited. If constrained by space in the main text, it can be elaborated in the appendix. 
- Many experiments in section 3 involves comparisons between only 2-3 models (many of them are trained with datasets and architectures). While I understand that it is very challenging to run carefully controlled experiments due to the lack of pre-trained models in many settings, this still limits the significance of the conclusions.
- See more potential concerns in the "questions" section.

### Questions
- In lines 371-373 where the authors discusses the results shown in figure 6(a), the author attributes higher ICL performance of the mini-CPM model to reduced competition. However, from the figure we can clearly see that the competition intensity of mini-CPM 2B is higher than that of Pythia-2.8B on the right side of the dashed line, which seems to contradict with the author's reasoning. I would like to hear about more explanation on this.
- I would like to hear about more reasoning on how the value of the adaptive weights $w_r$ and $w_l$ is determined, and more experiments with other possible value of $w_r$ and $w_l$.
- Regarding the results in figure 4b, does the authors have any possible explanation on why the Pythia-1B model does not follow the general trend? 
- Related to the point above, I want to note that different Pythia models have different width-depth ratios. If possible, it might be helpful to further investigate the effect of the width and depth of the model separately. The fact that the width-depth ratio of the model might have a big effect on the TR/TL competition also raises a small concern about whether the comparison in table 1 is actually the most fair, if the 1B+1B model has a different width-depth ratio from the other bigger models. I would hope to get more info about this.
- Other than the method proposed in section 4 of the paper, are there other potential implications of the TR/TL competition phenomenon?
- Does the TR/TL competition phenomenon only occur in pre-training, or it also occurs in fine-tuning?

### Soundness
3

### Presentation
3

### Contribution
3
