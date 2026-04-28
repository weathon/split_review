# GC-Mixer: A Novel Architecture for Time-varying Granger Causality Inference

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 6, 5

## Abstract
The neural network has emerged as a practical approach to evaluate the Granger causality in multivariate time series. However, most existing studies on Granger causality inference are based on time-invariance. In this paper, we propose a novel MLP architecture, Granger Causality Mixer (GC-Mixer), which extracts parameters from the weight matrix and imposes the hierarchical group lasso penalty on these parameters to infer time-invariant Granger causality and automatically select time lags. Furthermore, we extend GC-Mixer by introducing a multi-level fine-tuning algorithm to split time series automatically and infer time-varying Granger causality. We conduct experiments on the VAR and Lorenz-96 datasets, and the results show that GC-Mixer achieves outstanding performances in Granger causality inference.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the Granger Causality inference with the proposed GC-Mixer model. The research topic is interesting, but the paper seems to lack unique motivation and contribution. Also, the theoretical contribution and empirical analysis of the paper are inadequate.

### Strengths
- The research topic is interesting, using deep learning tools for effectively capturing the non-linear Granger Causality.

- The paper is somehow easy to follow.

### Weaknesses
 - The novelty and the motivation of the paper are not clear.

- Many state-of-the-art Granger Causality studies like [1,2,3] are missed or not fully discussed and compared in the paper.

- The theoretical contribution seems inadequate.

- The experiments seem weak, to some extent.

- The organization of the paper is busy and can be improved, the authors may want to split Section 2.

### Questions
What is the unique motivation and novel contribution of the paper that set it apart from previous studies?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work considers the topic of Granger causality discovery in multivariate time series and focuses on how to do so using deep learning. The main contribution is a new method called GC-Mixer that leverages an alternative network architecture, and which shows promising results in GC inference with synthetic datasets where the ground truth is known. In addition, the authors propose a method for automatically splitting a long time series to discover time-varying GC dynamics.

### Strengths
Granger causality discovery is a difficult problem which is not fully solved by current methods, including those using deep learning. Capturing nonlinear dynamics during GC inference is challenging, and neural networks can help alleviate this problem. However, current approaches can be cumbersome to train and offer performance that is far from perfect, even on these relatively simple datasets. It is therefore worthwhile to pursue alternative approaches like this one, which leverage alternative network architectures. On top of that, it's important to explore solutions for detecting time-varying Granger causal relationships.

### Weaknesses
Several questions and concerns:

- It was difficult to follow the description of the mixer architecture, which is one of the main contributions of this work. If I understand correctly, it seems like the second projection in the mixer block, shown in eq. 8, actually mixes information between all the time series. If that's true, wouldn't it mean that every prediction depends on every time series? That should make it difficult to identify which predictors are important, because every forecast automatically depends on every input time series. It's worth acknowledging that this is a strange design choice. The point of sparsity in Tank et al is to fit networks that eliminate dependence on certain inputs. Here, dependence is eliminated via sparsity in $W$, but $W$ itself still depends on all the inputs. It seems possible for a certain input to be truly Granger causal, yet receive no weight via $W$ because its role is to determine which other inputs should be used in the forecast (i.e., it acts like a gating variable).

- Again, it was hard to follow the description of the network architecture, but it seems like the predictions are ultimately based on an element-wise multiplication between the inputs and the output of the mixer block (this is then fed to a MLP). Would it be fair to interpret these as attention weights? It might be a helpful analogy, because similar notions of soft attention have been used in transparent deep learning.

- I'll temporarily assume, following my question above, that the $W^{(n)}$ values can be viewed as attention weights. When we pass the attention-weighted inputs $M$ into the MLPs $g_i$, do we use separate attention weights for each $g_i$? Otherwise, it would seem that we're forced to make one set of selections for all predictions, whereas we should instead select the relevant inputs for the prediction corresponding to each output series. Either I'm missing something in the notation, or this seems like a restrictive choice.

- It seems inconvenient that the weights $W^{(n)}$ determine the Granger causality relationships, but that they vary for every time point. Compared to the cMLP/cLSTM, it means that an input can be deemed non-causal only if it has small weights for all time points. Is that correct?

- The authors claim that they cannot make the $W^{(n)}$ weights exactly equal to zero, even with the group lasso penalty. This seems correct, because the weights are the output of the mixer block. However, it is untrue that the cMLP/cLSTM share this issue: they regularize parameters of the network, and the parameters can reach zero exactly due to optimization with proximal updates. The difference is still notable: choosing a high $\lambda$ value can ensure that the cMLP/cLSTM eliminates certain input dependencies. For this approach, because we're attempting to sparsify predictions rather than weights, I'm not sure we can guarantee sparsity regardless of the $\lambda$ value.

- The authors state that they applied the hierarchical penalty to all models tested here, including GC-Mixer, cMLP and cLSTM. However, the cLSTM only has an explicit dependence on one past timepoint, so it's not possible to apply the hierarchical penalty. Indeed, Tank et al discussed that penalty only in the context of the cMLP. Can the authors explain what they mean about using the hierarchical penalty with the cLSTM, because this sounds like a mistake.

- The methods for splitting the time series to discover time-varying dynamics seems reasonable. However, the experiment that tests it seems quite simplistic, and I wonder if the authors could design an experiment that is either more challenging or more realistic. Also, I'm not certain about this, but it seems like the algorithm has no specific relationship with GC-Mixer: it is perhaps unfair to only use it with GC-Mixer in Table 4 and not apply it with cMLP or cLSTM?

- The results with VAR data are encouraging, but this is not the type of data where GC-Mixer should be most valuable. Indeed, we would expect that traditional linear methods would perform far better with this data. On the Lorenz dataset that's actually nonlinear, GC-Mixer underperforms both cMLP and cLSTM. It makes this method significantly less interesting that it underperforms on nonlinear data. Also, I wonder if it's especially well matched for VAR data because $W$ can basically be a constant prediction for all timepoints, $g$ can behave linearly, and we'll recover the exact VAR model. I didn't realize this before, but now that I do I think it's important to expand the experiments before publication.

- The results in Figure 4 look like they did not involve tuning the penalty strength for cMLP. Can the authors describe what they did here and whether it's providing a fair comparison?

- The final architecture is quite complicated, and I wonder if the authors performed any ablations to understand what aspects are important for it to work. For example, could they try with different numbers of blocks? Or removing batch normalization? Currently, it is hard to understand why this type of autoregressive model should enable better GC discovery than a MLP or LSTM - it's a different parameterization, but not obviously better. (And as mentioned above, the empirical results are not convincing on their own.) I think these ablation results would be important to include before publication.

- Could the authors provide more details about how they generated AUROC curves? For example, did they keep epsilon fixed and train with different lambda values? Or did they train with one lambda value and sweep epsilon? It would be important to know whether there are any differences compared to previous methods. I'm pretty sure this differs from how Tank et al generated results: they effectively set $\epsilon = 0$ and swept $\lambda$. How do the authors set $\lambda$ before sweeping $\epsilon$? This seems like an important hyperparameter choice.

- For the title of Section 2.1.2, the "non-autoregressive" model looks like it actually is autoregressive, in that it predicts the future using the past. Perhaps what the authors meant to say is that it's nonlinear? This should be corrected.

- Typo in Section 2.2.3: GULE -> GELU

### Questions
Several questions are mentioned in the weaknesses section above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a model for time-invariant Granger causality inference which exhibits consistent performance across various time series using the same hyperparameters. The model can also be extended to infer the time-varying Granger causality within a multi-level fine-tuning framework.

### Strengths
1. The literature review is comprehensive and clear.
2. The authors conduct extensive experiments on simulated datasets with different configurations.
3. The authors proposed an algorithm that has been claimed as the first algorithm to utilize an MLP Mixer-based architecture for inferring Granger causality in time series.

### Weaknesses
1. Given that the proposed algorithm involves significantly more parameters than the baselines, it would be helpful to include a comparison of the number of parameters required in the experiment section, along with the corresponding training times. Furthermore, a discussion on the potential for overfitting due to the increased number of parameters should be included. The authors should also clarify whether the reported training times are for a single run or averaged over multiple runs.
2. Some details about the loss function are not clear. Specifically, the equation 12 loss function contains the time index $t$ and time series index $i$, yet there is no summation regarding $t$ and $i$. It is unclear if the loss function is computed for each time series $i$ at a specific time $t$, or if it is aggregated in some way. The paper needs to clarify how the loss is aggregated across time and across different time series.
3. Some details about the experiments are not clear. The value of the threshold $\epsilon$ in equation 13 needs to be specified, along with a justification for how it was determined. It is also unclear if the True Positive Rate (TPR) and False Positive Rate (FPR) are calculated based on the F-norm of the weight matrix $W_{j,k}^n$, and whether these metrics consider the accuracy of the identified lag, or only if a causal relationship exists. For instance, if the true lags are 1, 2, and 3, would lag 4 from time series $j$ to $i$ be regarded as a False Positive?  The paper also needs to clarify if the algorithm is run $p$ times for a $p$-variate time series, and if so, how the results are aggregated.
4. Table 3 shows that the cMLP algorithm outperforms the proposed algorithm. Given that no other nonlinear experiment has been provided, it is unclear if the proposed algorithm performs worse than the baselines in the nonlinear cases. More nonlinear experiments should be included to thoroughly examine the performance of the proposed algorithm in nonlinear cases. The authors should also consider the computational cost of the proposed algorithm compared to cMLP, especially in nonlinear settings.
5. Additional nonlinear experiments should be conducted in section 3.3 on automatic lag selection, given that the Lorenz-96 dataset does not involve time lag. Since the proposed method did not yield the best performance in the Lorenz-96 dataset, it is unclear if this would also be the case in the time lag selection stage. Additional results would provide valuable insights. The authors should also discuss why the Lorenz-96 dataset was chosen if it does not involve time lags.
6. More details are needed regarding the procedure for generating the time series in section 3.4 on time-varying Granger causality inference. If, in the four scenarios, two sets of time series with different configurations are merged together with equal lengths, this could potentially favor the proposed algorithm. The authors should also clarify the value of $i$ when the algorithm stops in the time-varying experiment. The paper should also explain how manual splitting is performed, and if it utilizes additional information about the true time series. The paper needs to clarify why the multi-level fine-tuning approach is used, given that it does not significantly outperform manual splitting in Table 4, despite the increased computational cost and parameter requirements. It is also unclear why the algorithms mentioned in section A.2 have not been applied as baselines, even though they require manual selection of the time lag. Finally, the visualization should be improved by incorporating axis titles and subtitles.

### Questions
1. In the equation 12 loss function, the right-hand side of the equation contains the time index $t$ and time series index $i$, and there is no summation regarding $t$ and $i$. Does this mean the loss function is computed for each time series $i$ at a specific time $t$? Personally, I do not think the loss function is linked to each $t$, but equation 12 seems to suggest otherwise.
2. What is the value of the threshold $\epsilon$ in equation 13 in the experiment, and how to determine it? Could you help me locate the place if you have stated it already in the paper?
3. It is advisable to cite the related work in the first paragraph in section 2.3 regarding the existing approach?
4. Can you clarify how you compute the True Positive Rate (TPR) and False Positive Rate (FPR)? Do these metrics calculate from the F-norm of $W_{j,k}^n$? In other words, do they not only assess whether time series $j$ Granger-causes time series $i$ but also consider whether the lag is accurate? For instance, if the true lags are $1,2,3$, would lag $4$ from time series $j$ to $i$ be regarded as a False Positive?
5. Given that the loss function is computed for each time series $i$, does this mean the whole algorithm will run $p$ times for $p$-variate time series?
6. Table 3 shows that the cMLP algorithm outperforms the proposed algorithm. Since no other nonlinear experiment has been provided, does this imply that the proposed algorithm performs worse than the baselines in the nonlinear cases? Personally, I recommend conducting further nonlinear experiments to thoroughly examine the performance of the proposed algorithm in nonlinear cases.
7. Can additional nonlinear experiments be conducted in section 3.3 on automatic lag selection, given that the Lorenz-96 dataset does not involve time lag? Since the proposed method did not yield the best performance in the Lorenz-96 dataset, might this also be the case in the time lag selection stage? Additional results would provide valuable insights.
8. Can you offer more details regarding the procedure for generating the time series in section 3.4 on time-varying Granger causality inference? If, in the four scenarios, two sets of time series with different configurations are merged together with equal lengths, would this potentially favor the proposed algorithm? Considering that the multilevel fine-tuning algorithm separates input time series into $2^{i-1}$ segments, such a configuration might be advantageous. Furthermore, could you provide the information about the value of $i$ when the algorithm stops in the time-varying experiment?
9. Still in section 3.4, how to do manual splitting? Does it utilize additional information about the true time series?
10. Could you briefly explain why the algorithms mentioned in section A.2 have not been applied as baselines, though they ask to select the time lag manually?
11. It is advisable to enhance the visualization by incorporating axis titles and subtitles.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors investigate the problem of the Granger causal structure discovery. Considering that the existing method can hardly address the time-varying Granger-Causality inference, the authors proposed the GC-Mixer, which contains a mixer Block and a causality inference block. The authors further devise the multi-level fine-tuning method. The authors evaluate the proposed method on the VAR and Lorenz-96 datasets.

### Strengths
The authors address the problem of the time-varying Granger Causality inference.

### Weaknesses
1.  There are several methods that are proposed to solve the Granger Causality, for example [1],[2],[3][4][5]. Moreover, [2] is similar to the proposed method. Hence, it is suggested that the authors should discuss the difference between the proposed method and these methods and consider them as baseline.  
2.  The authors propose multi-level fine-tuning to address the time-varying causal structure, but the motivation and intuition are not clear. Moreover, it is suggested that the authors should provide the complexity analysis for the multi-level fine-tuning method.   
3.  I am also curious if the proposed method can address the causal structures that do not exist in the training set (OOD causal structure).

### Questions
N.A.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
