# Enhancing Neural Network Interpretability with Feature-Aligned Sparse Autoencoders

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
Sparse Autoencoders (SAEs) have shown promise in improving the interpretability of neural network activations, but can learn features that are not features of the input, limiting their effectiveness. We propose \textsc{Mutual Feature Regularization} \textbf{(MFR)}, a regularization technique for improving feature learning by encouraging SAEs trained in parallel to learn similar features. 
We motivate \textsc{MFR} by showing that features learned by multiple SAEs are more likely to correlate with features of the input. By training on synthetic data with known features of the input, we show that \textsc{MFR} can help SAEs learn those features, as we can directly compare the features learned by the SAE with the input features for the synthetic data.
We then scale \textsc{MFR} to SAEs that are trained to denoise electroencephalography (EEG) data and SAEs that are trained to reconstruct GPT-2 Small activations. We show that \textsc{MFR} can improve the reconstruction loss of SAEs by up to 21.21\% on GPT-2 Small, and 6.67\% on EEG data. Our results suggest that the similarity between features learned by different SAEs can be leveraged to improve SAE training, thereby enhancing performance and the usefulness of SAEs for model interpretability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The manuscript introduces Mutual Feature Regularization (MFR), a technique to improve Sparse Autoencoder training by encouraging multiple SAEs trained in parallel to learn similar features. Using synthetic data with known features, the authors validated that MFR helps SAEs learn actual input features more effectively than SAE. Furthermore, the technique improves reconstruction loss by up to 21.21% on GPT-2 Small activations and 6.67% on EEG data.

### Strengths
- Authors performed experiments with synthetic, EEG, and GPT2 weights datasets.

### Weaknesses
 - Tables 1, 2, and 3 do not report variability across folds or multiple runs.
- The regularization has to be compared with baselines. For example, DCCAE (Wang et al., 2015) is an autoencoder with CCA that maximizes the correlation between different views. DCCAE also uses different encoders and decoders for each view.
- It needs to be made clear how the splits have been performed. The validation set should be used only for hyperparameter search or checkpoint selection. The final performance must be reported on the hold-out test set.
- It needs to be shown how improvements in reconstruction with regularization improved interpretability. Consider performing analysis with qualitative examples of latents.
- It remains unclear how improved reconstruction necessarily leads to better interpretability, as reconstruction loss can saturate without corresponding gains in feature understanding.
- The justification for the inductive bias of similar features across SAEs needs further clarification. The potential trade-off between feature diversity and similarity should be addressed.

### Questions
- Have you ensured that splits do not have overlapping subjects for EEG data?
- Looking at Figure 5, the model performs as Multi-View models would perform (e.g., SimSiam, SimCLR). The difference is you have a separate Encoder and Decoder, like in DCCAE, instead of multi-view input. Looking at Figure 4, you have a much more diverse representation, or it is because the SAE learned different subspaces. Do you think your regularization will reduce the diversity of the features learned from the data?

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
The authors propose a regularization framework that both determines whether sparse auto-encoders need to be re-trained and enforces sparse autoencoders trained with different random initializations are learning the same features. The authors validate their results on a simulated dataset, and then apply their model on GPT-2 and EEG data.

### Strengths
This work is of high quality and largely original. Moreover, reading the paper is easy, and the authors do a great job building up their intuitions, related work, and simulation results to verify their model. Results are explained incredibly well, examples of this are Figures 2-6, and I think their method can be significant. I think everything up to the real world results are done incredibly well, and I think the authors have a good base for a strong paper.

### Weaknesses
Major weakness(es): 
As good as the paper is up to its real world results, I believe the real world results are not as convincing. One of the main issues with the real world results is that the authors do not provide any deeper insights about what their improvements tell us about the data they are analyzing. One main feature of their method in the title is to improve interpretability, but when they apply the model on real world data, they do not actually verify new interpretations, i.e. what does the author’s model tell us about EEG data that the baseline did not? How do the improvements in reconstruction accuracy translate into actionable or interesting results for both the GPT-2 and EEG results? In fact, in their introduction (Section 2.2) the authors mention in Lines 128-130 that “… the reconstruction loss itself is not sufficient to evaluate SAEs, …” which I tend to agree with, but Tables 1-3 and Figure 9&10 only evaluate exactly that (and cross-entropy for GPT-2, but in some sense this is a different measure of reconstruction accuracy: prediction preservation accuracy). I think the authors can make this paper very impactful and significant if they explain to the reader what the added improvements in reconstruction accuracy/cross entropy loss translate to in terms of interpretability, but at this moment the paper seems unfinished. I think the idea the authors propose is important, and I think that with substantial improvements in the regard that I have just described, I am open to significantly increasing my score.

Minor weakness(es):
1. Figure 8 does not show standard deviations, and the authors do not report significance tests for the numbers in their tables (1-3).
2. The authors show many training curves, I believe these should not be added in the main text unless they add something, moving them to the Appendix would provide the authors enough space to dig into interpretability results from their model.
3. The performance of the authors’ model is not better for 24 and 30, 48 and 60 for the GPT-2 and EEG results, respectively. The authors should explain better why this is the case, and potentially research why this phenomenon happens. Since just from a reconstruction error perspective, out of the models the authors have tested their baseline performs the best for both the GPT-2 and EEG data for k=30 and k=60, respectively. If the authors can show that smaller ks help with interpretability, then this is not perse an issue, but since most of the results currently do not actually dive into interpreting the results and mostly focus on reconstruction accuracy, it hurts the impact of the paper.
4. The authors cite two papers on Lines 466-467 that perform EEG denoising, but do not add these papers as baselines.
5. Some of the hyperparameters are not explained, e.g. a hidden size of 4096 and learning rate of 0.001 when training on the EEG data. To improve the confidence in their paper, I would suggest running atleast a small hyperparameter study using the validation set, and selecting the best model for the test set (this applies to all of the authors’ results, including the simulation results).

### Questions
Why did the authors decide to use EEG data, and specifically the TUH dataset? \
Line 427: Why is the author’s model only better in terms of reconstruction error for small k values? See table 1 and 3 \
Line 320/321: Do the authors return the mean of the max cosine similarity pairs based on the Hungarian algorithm output? \
Line 244: Why do the authors use cosine similarity maximization and not another distance metric? Since cosine similarity does not take the magnitude of the two matrices into account.

### Soundness
4

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
4

### Summary
The paper investigates a mutual alignment regularization to train a set of sparse auto-encoders (SAE) in the context enhancing efficiency and interpretability. It does so by penalizing the elements in one dictionary (decoder basis) from not being matched with at least one  element in another dictionary. The method is validated on synthetic data created with a sparse, group-structured model. Only one group is active and $K$ elements in the group are active, based on underlying rates. The method is also tested on a small trained transformer GPT2 small and finally on EEG data. The results show that with fewer active components the regularized networks outperform the unregularized network in terms of reconstruction cost, and for the GPT2 corpus in terms of the cross-entropy loss.

### Strengths
Directly ensuring robustness of SAE through an alignment loss appears original and seems to provide some gains. It addresses a problem in the use of SAE-based interpretation of networks.

### Weaknesses
Based on the premise I was expecting more resulting showing improved interpretation. While quantitative results are given, the significance of them is questionable.

The paper's organization could be improved by stating initially the formulation. Figure 1 does not convey much information.  It says on line 81 that "auxiliary penalty calculated using the similarity of the SAE weights" is used, but it is not introduced until Section 3.3 titled "Analysis" there is finally a formulation (in numbered equations) at the bottom of page 6.  Jumping directly to the description of the synthetic data seems out of place.

The formulation of the auxiliary penalty/regularization itself is cryptic. It appears to involve asymmetries (perhaps due to the choice of cardinalities) that are not motivated.  If this is used to regularize all networks, due to the asymmetry, it seems that the index of the network adjusts how it is applied.

The choice of number of SAEs in the regularization isn't precisely given. I take it that the SAEs trained at different levels cardinality (TopK) are co-learned, but this isn't stated explicitly. 

Some of the statements early on are not clear (noted in question/comment set 1 below).

The use of EEG data is not well motivated nor are the details of the data well explained. If there was a downstream task like in GPT2 case that would be more interesting.

Question/comment Set 1:
-"features that are not features of the input"  Rather directly correlate with known features of the input.
- The expression  "features that correlate with features of the input" should be clarified with the fact that the latter corresponds to human interpretability.
-I assume reconstruction loss in the abstract is at the same sparsity level.
-Are polytopes "fundamental units of neural networks" like unit activations?
-The premise of "studying an SAE would not be guaranteed to reveal information about the neural network that SAE was trained on activations from" is strange. Just because the SAE activations aren't as interpretable they are still a function of the activations of the neuron network. Of course by the information processing inequality they can contain less information (or possibly zero if they don't pass anything). However, I do agree with the premise that "studying SAEs would [not always] be more fruitful than studying the raw activations directly".
- It should be made clear that the 'model loss' in the definition of 'loss recovered' refers to a task loss, perhaps the training loss, but could also be a loss function used in validation. References for this definition should be given.


Comment 2:
While not studied formally the significance of the problem reminds me of work studying whether LASSO is a consistent estimator of the true support. The authors considered whether random initialization of the weights is necessary if bootstrap sampling could be used to create different training samples for the same data. This is explored in Francis Bach's work on bootstrap LASSO, which uses the intersection of the support of sparse linear models to find a reliable support. It would be interesting if the proposed regularization works from simply different sampling of the same data without random initialization of the weights. In this case the weights may correspond without the quadratic cost. 

Comment 3:
The Hungarian algorithm is used to assign pairs to maximize correspondence with results in Figures 2, 3, 4 and 5; however, the linear assignment problem assumes one-to-one so if there is duplication of a neuron/dictionary element it will lead other pairs to be improperly matched.  So it is not clear to me that when the result shows low similarity, which is interpreted there wasn't a correspondence, it is in fact the case that the assignment didn't correspond.  Partial optimal transport methods that don't require the marginals to be matched exactly can be used to give a more robust matching.

Comment 4:
The synthetic data has some arbitrary choices of simulation (groups all being the same size). Furthermore, after $p_j$ is chosen as active, wouldn't it make sense to bound that sparse features coefficients away from 0? Choosing uniform over [a,1] with a>0 or some other distribution.

Comment 5:
It is not clear to me why a cluster of features that are similar between SAEs but are to the input feature matter if they are not active in the TopK activation? While I agree that reinitializing those features (which to my understanding is common for SAEs) can make the network more efficient.

Comment 6: Asymmetry in penalty across models. See comment in Weaknesses. 

Comment 7:
In Figure 6, the definition of the average of the absolute value is not clear. Why would the activation be k/N in the top-K. The top-K doesn't ensure sums to 1, but rather that it is above the threshold. Otherwise the metric is not meaningful. Its not clear if the reset threshold in caption Figure 8 makes sense.

Question set 8:
Line 363, it is not clear what the initial reconstruction loss was? Is it the first batch, the first epoch? What does the "100 training step cosine warmup for the penalty" mean?

Comment 9:
The lower loss on the task loss in Table 2 is interesting. Especially since the lowest loss is achieved at at k=18 which isn't the lowest reconstruction loss. However, it is hard to tell if this difference is meaningful as the loss is much higher than the no modification loss, while much lower than the zeroing out ablation.

Question 10:
For the EEG data it is not clear what is meant by vectorized. Is it multichannel windows that is vectorized? If so what is the size of the windows, sampling rate, and number of channels?

Minor points:
-Lines 97–100, need parenthetical references.  Also on lines 126-127, lines 132-133, 138–139 and elsewhere.
-Line 129 "to optimizing"
-Lines 140–141 is not a complete sentence.
-Figure 10 doesn't convey any information to the reader (especially without log y-axis).

### Questions
Question/comment Set 1:
-"features that are not features of the input"  Rather directly correlate with known features of the input.
- The expression  "features that correlate with features of the input" should be clarified with the fact that the latter corresponds to human interpretability.
-I assume reconstruction loss in the abstract is at the same sparsity level.
-Are polytopes "fundamental units of neural networks" like unit activations?
-The premise of "studying an SAE would not be guaranteed to reveal information about the neural network that SAE was trained on activations from" is strange. Just because the SAE activations aren't as interpretable they are still a function of the activations of the neuron network. Of course by the information processing inequality they can contain less information (or possibly zero if they don't pass anything). However, I do agree with the premise that "studying SAEs would [not always] be more fruitful than studying the raw activations directly".
- It should be made clear that the 'model loss' in the definition of 'loss recovered' refers to a task loss, perhaps the training loss, but could also be a loss function used in validation. References for this definition should be given.



Comment 2:
While not studied formally the significance of the problem reminds me of work studying whether LASSO is a consistent estimator of the true support. The authors considered whether random initialization of the weights is necessary if bootstrap sampling could be used to create different training samples for the same data. This is explored in Francis Bach's work on bootstrap LASSO, which uses the intersection of the support of sparse linear models to find a reliable support. It would be interesting if the proposed regularization works from simply different sampling of the same data without random initialization of the weights. In this case the weights may correspond without the quadratic cost. 
 

Comment 3:
The Hungarian algorithm is used to assign pairs to maximize correspondence with results in Figures 2, 3, 4 and 5; however, the linear assignment problem assumes one-to-one so if there is duplication of a neuron/dictionary element it will lead other pairs to be improperly matched.  So it is not clear to me that when the result shows low similarity, which is interpreted there wasn't a correspondence, it is in fact the case that the assignment didn't correspond.  Partial optimal transport methods that don't require the marginals to be matched exactly can be used to give a more robust matching.

Comment 4:
The synthetic data has some arbitrary choices of simulation (groups all being the same size). Furthermore, after $p_j$ is chosen as active, wouldn't it make sense to bound that sparse features coefficients away from 0? Choosing uniform over [a,1] with a>0 or some other distribution.

Comment 5:
It is not clear to me why a cluster of features that are similar between SAEs but are to the input feature matter if they are not active in the TopK activation? While I agree that reinitializing those features (which to my understanding is common for SAEs) can make the network more efficient.

Comment 6: Asymmetry in penalty across models. See comment in Weaknesses. 

Comment 7:
In Figure 6, the definition of the average of the absolute value is not clear. Why would the activation be k/N in the top-K. The top-K doesn't ensure sums to 1, but rather that it is above the threshold. Otherwise the metric is not meaningful. Its not clear if the reset threshold in caption Figure 8 makes sense.

Question set 8:
Line 363, it is not clear what the initial reconstruction loss was? Is it the first batch, the first epoch? What does the "100 training step cosine warmup for the penalty" mean?

Comment 9:
The lower loss on the task loss in Table 2 is interesting. Especially since the lowest loss is achieved at at k=18 which isn't the lowest reconstruction loss. However, it is hard to tell if this difference is meaningful as the loss is much higher than the no modification loss, while much lower than the zeroing out ablation.

Question 10: 
For the EEG data it is not clear what is meant by vectorized. Is it multichannel windows that is vectorized? If so what is the size of the windows, sampling rate, and number of channels?

Minor points:
-Lines 97–100, need parenthetical references.  Also on lines 126-127, lines 132-133, 138–139 and elsewhere.
-Line 129 "to optimizing"
-Lines 140–141 is not a complete sentence.
-Figure 10 doesn't convey any information to the reader (especially without log y-axis).

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
This paper introduces a method of enhancing the feature interpretability of a learned neural network via sparse auto-encoders. Specifically, a mutual feature regularization technique has been proposed by correlating multiple SAEs. The experiments were conducted on a simulated dataset and two real-world datasets.

### Strengths
The paper addresses the important issue of interpreting an internal representation of a trained network.

Three datasets, one simulated and two real, were used to support the validity of the proposed method.

### Weaknesses
The paper needs to reorganize its structure to describe its ideas and contributions better. In its current form, it isn't easy to understand.
The technical contribution is marginal and is not well supported by the experiments.

This paper is about enhancing the interpretability of an internal representation of a neural network. However, there are quantitative values compared with baseline models, but there are no interpretation-related results or explanations in the experiments. 

When training SAEs, the hidden size plays an important role, which may cause the feature superposition or feature distribution to occur.
In this respect, there should be a comparison among varying hidden sizes in SAEs.  

The current experimental results do not support many hypothetical statements well in Section 3.3. The validity of their arguments needs rigorous efforts.

Page 6, line 307: A statistical significance test is needed to justify the increase in correlation with reinitialization better.

### Questions
Page 5, lines 225-226: “We see the exact value of total active features, 36, ~~.” What do the authors mean by the exact value, and where does the value 36 come from?

How exactly does the proposed MFR is defined? It is not explicitly entailed.

### Soundness
2

### Presentation
1

### Contribution
2
