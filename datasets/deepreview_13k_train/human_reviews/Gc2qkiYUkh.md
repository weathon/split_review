# Features are fate: a theory of transfer learning in high-dimensional regression

- Decision: Reject
- Scores: 6, 3, 5, 6, 6

## Abstract
With the emergence of large-scale pre-trained neural networks, methods to adapt such ``foundation'' models to data-limited downstream tasks have become a necessity.
Fine-tuning, preference optimization, and transfer learning have all been successfully employed for these purposes when the target task closely resembles the source task, but a precise theoretical understanding of ``task similarity'' is still lacking. 
While conventional wisdom suggests that simple measures of similarity between source and target distributions, such as $\phi$-divergences or integral probability metrics, can directly predict the success of transfer, we prove the surprising fact that, in general, this is not the case.
We adopt, instead, a \emph{feature-centric} viewpoint on transfer learning and establish a number of theoretical results that demonstrate that when the target task is well represented by the feature space of the pre-trained model, transfer learning outperforms training from scratch.
We study deep linear networks as a minimal model of transfer learning in which we can analytically characterize the transferability phase diagram as a function of the target dataset size and the feature space overlap.
For this model, we establish rigorously that when the feature space overlap between the source and target tasks is sufficiently strong, both linear transfer and fine-tuning improve performance, especially in the low data limit. 
These results build on an emerging understanding of feature learning dynamics in deep linear networks, and we demonstrate numerically that the rigorous results we derive for the linear case also apply to nonlinear networks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the gap in understanding how to adapt large pre-trained models to data-limited tasks by examining the theory behind task similarity in transfer learning. It challenges the conventional belief that similarity between source and target data distributions, such as through ϕ-divergences, predicts transfer success. Instead, it suggests a feature-centric approach where transfer learning is effective when the target task aligns well with the feature space of the pre-trained model. The authors demonstrate their theory using deep linear networks, providing insights into when transfer or fine-tuning outperforms training from scratch, especially with limited data.

### Strengths
1- Even thought the structure of the paper is atypical (e.g., short introduction with related work being a subsection), the paper is well-written and easy to follow.

2- Transfer learning is very important topic in DL and understanding when/why it works is crucial for the overall understanding of deep learning.

3- I did not read all the proofs in extreme details. I only checked the skeleton of the proofs and they seem correct and the results are reasonable. However, I am not update with the current advancements in transfer learning theory so i can not judge the novelty of the proofs/theoretical results. Hence so the low confidence in the score.

### Weaknesses
1- Lack of the empirical results: the authors only consider a small example of a two layer neural networks. So it is hard to see if the conclusion/insights of their theory  can really translate to deep state-of-the-art models. Furthermore, focusing solely on linear models for theoretical analysis is a significant limitation, especially when the core of transfer learning lies in learning non-linear features. The insights gained from linear models may not fully capture the complexities of feature learning in deep neural networks, where non-linearities play a crucial role in representation learning and transferability. The paper would benefit from demonstrating the applicability of the theory to more complex, non-linear architectures, even if it's through carefully designed experiments that bridge the gap between theory and practice.

2- The proposed theory does not offer any insights on the design of the representation learning approaches and why some work better than other (e.g., contrastive learning with self-supervised learning) which in my opinion is a very interesting question crucial to understand transfer learning. The theory should ideally provide guidance on how to design pre-training tasks and architectures that yield more transferable representations. For instance, it would be beneficial to see how the theory can be used to explain why certain self-supervised methods, like contrastive learning, are more effective at learning transferable features compared to other approaches. The absence of this connection limits the practical impact of the theoretical findings.

### Questions
Q1- Does the proposed theory shed some light into why some approaches (e.g., contrastive learning with self-supervised learning ) learn better and more transferable representation compared to others? 

Q2- Is it possible to use the proposed theory to improve the transfer learning capabilities of the models? For example, during the representation learning phase with the source data, we can add a regularizer that tries to maximize the the overlap in the feature space using a small amount of the target data. I would like to hear the authors thoughts on this and other ways to leverage this theory in practice.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims to provide new theoretical insights into fine-tuning and transfer learning with large-scale foundation models. In particular, they aim to improve the theoretical basis of measuring the similarity between two machine learning tasks - the baseline task for which the foundation model was trainied and the target task for which we are fine-tuning/transfering. The authors argue that one should study this problem from the standpoint of data features. The authors claim to make progress and relate their results to feature learning dynamics.

### Strengths
The authors are correct that a theory of fine-tuning foundation models is lacking, and so work in this space is welcome. Indeed an explanatory theory for transfer/fine-tuning of nonlinear, deep networks would be a significant advance in the field.

The feature-centric viewpoint appears novel.

### Weaknesses
I found it difficult to assess the contributions of the paper because of unclear explanations. In particular, Theorem 2.2 is crucial because it is claimed to motivate the work (“General Theoretical Setting”), but I cannot follow the argument. What I can best infer from the text is that the authors are saying the following:  If the source and target distributions are the same (or similar) but the features are different, then transferring will fail. This means that, even if the data is the same for both source and target, if a network f is the pretrained one, then we can find a "bad" network g that has worse performance. But this seems obvious, since one can pick a random network g that will with overwhelmingly high probability have worse performance than any trained network. My suspicion from this is that the authors’ results won't actually hold up in practice. But it is hard to tell because the set up is so unclear.

The claimed theory (that I could not exactly follow due to the unclarity above) is proved only for deep linear networks and shallow (e.g, 2 layer) nonlinear networks, which significantly reduces its potential explanatory potential in realistic deep learning settings.

I am also concerned about the setup of the problem itself. The authors state that x and y are jointly distributed, with y being a real number. Then, they define noisy versions of y, denoted as ys and yt, which are essentially noisy transformations of x. This is fine. However, in Assumption 2.1, they state that x is a data point and y is a function of x that derives its statistical properties from f(x) + e. This is problematic because if y is a function, it cannot have statistical properties. The authors seem to be simultaneously stating that y = f(x) + e AND that y is a function of x (i.e., y(x) = f(x) + e), which is inconsistent. Furthermore, if x is a point, then y is simply Gaussian since e is Gaussian. This raises questions about the randomness of x and whether the analysis is limited to Gaussian data, specifically univariate Gaussian, which is a very basic case. The authors also claim that they can find a function g in the same subspace as f that gives poor performance. This is not surprising, since one can always find a function in the same subspace that performs poorly by simply choosing random coefficients, or scaling the coefficients to achieve larger error. This is especially true since the authors do not impose any similarity constraint between f and g, only that they exist in the same subspace.

### Questions
If I have a misconception regarding Theorem 2.2, can you please clarify your explanation? The entire paper revolves around this result.

>> Thank you for your discussion around Theorem 2.2. While reading your rebuttal plus re-reading the paper, I have a few additional concerns that should be discussed.

1. You initially say that x and y are jointly distributed and that the labels are real numbers y in R (second sentence in Section 2). This is fine although a slight abuse of notation since random variables are not numbers. Then you define noisy versions of y and call them ys and yt. They are essentially noisy transformations of x. So far that is fine. Now in Assumption 2.1, you say that x is a data point and that y is a function on x that derives its statistical properties from f(x) + e. This is incorrect, because, if y is a function and not a random variable, then it cannot have statistical properties. Essentially, you are simultaneously saying that y=f(x)+e AND that y is a function of x (ie y(x) =f(x)+e), which doesn't make sense. Additionally, if x is a point, then y is just Gaussian since e is Gaussian. So where did the randomness in x go? Also are you only considering Gaussian data? Actually, it seems to be univariate Gaussian, and so the most basic case possible.

2. Your explanation is helpful but not complete. For example, let's say that we train the source model and get f which is essentially a wavelet transform. Then the basis functions phi's are just some wavelet basis in L^2. Then the subspace is the entire space. Then you are saying that you can find another function using the wavelet basis that gives poor performance. Obviously that is true -- just pick random wavelet coefficients. And if you want larger error you can just scale the coefficient weights.

3. Point 2 seems especially true, since you do not say that f and g are similar. You just say that you can find a g in the same subspace that f is in that is different.

4. If x has a fixed distribution for source and target tasks but fs and ft are different then the joint distributions p(x,ys) and p(x,yt) will be different. So I am not sure how you can claim in your rebuttal that "it is impossible to build two tasks with identical distribution for which transferring is poor". It must be that you are defining these functions, somehow, by learning them. But it is not clear how. Maybe you are assuming that the networks converge to a global minima?

### Soundness
2

### Presentation
2

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
The paper theoretically studies transfer learning for deep linear networks in the feature-learning "rich" regime, in the joint scaling of large number of fine-tuning samples $n$ and dimension (including width) $d$. The pertaining is performed on the population loss to simulate the fact that the source task has to be larger than the fine-tuning one.

The authors first argue that the model-agnostic task-similarity metrics (based solely on the source and target distributions) are insufficient to capture how good the transfer is and find counter examples where it can be the case. Then, they propose a new metric based on the discrepancy between the performances of the fine-tuned model and the trained-from-scratch model.

Given this metric, they compute the network performances in the asymptotic limit described above, both in the case of linear fine-tuning and "full" fine-tuning of all the parameters.

### Strengths
1. The results presented, especially Theorem 3.7, 3.8, and 3.9 are, to my knowledge, novel and relevant to the development of the theory of transfer learning in neural networks. Although in the linear setting, these results are non-trivial to obtain since the authors operate in the rich regime, which corresponds to a non-convex optimization problem from an optimization perspective (all the weight matrices move from initialization in the limit).

2. The paper is overall very well-written. The results are nicely presented, and the storyline is logically flawless. I especially appreciated how results from existing work are adequately presented, such that the novel theorems feel tied into the existing literature. Finally, the results are adequately discussed and put into context (e.g. Theorem 3.6).

### Weaknesses
The main fundamental weaknesses of this paper in my opinion lie in how certain results are portrayed, which can be quite misleading. More concretely:

1. First of all, I think studying linear networks in the specific context of transfer learning is an inherent limitation that should be more clearly discussed. This is because the function class is linear no matter how many hidden layers. In fact, one could consider a simple linear regression model (for which the asymptotic analysis is known, as the authors correctly cite), and then perform linear evaluation on fresh new weights. This is how I interpret Theorem 3.5 and 3.6, where there is no dependence on the depth. A more thorough discussion on the role of depth, or lack thereof, in the presented results would strengthen the paper's claims. Specifically, the authors should clarify whether the insights gained from analyzing deep linear networks are fundamentally different from those obtained from a simpler linear regression model in the context of transfer learning.

2. I find it a bit misleading to consider as misleading the dataset-based discrepancy metrics based on the “anomalous positive transfer”. In this case, as the authors state, the positive transferability comes purely from the double descent phenomenon and not from anything inherent positive feature of fine-tuning. In a sense, the benefits of pretraining come purely from the additional datapoints that the model is pre-trained on and that makes you avoid double descent. In this sense, I feel that the message stated in the abstract that model-agnostic similarity metrics are insufficient, while the proposed feature-centric metric is portrayed as the solution, is misleading: the proposed metric has precisely this flaw that does not take into account the double descent phenomenon. To give an example, when the source and target distributions are exactly the same, the metric would still present this anomaly. Thus, comparing with the trained-from-scratch model is not enough to evaluate transferability. A more detailed discussion on the limitations of the proposed metric in light of the double descent phenomenon is needed.

3. The results in Section 3.8 are also incomplete. How does the measure of transferability $\mathcal{T}$ change? I appreciate the result that in general, the transfer is worse (and this is a nice result per se), but it would be nice to tie it to the previous section, i.e. comparing it to the trained-from-scratch model. I would imagine that the picture in Figure 1 (b) would be different, as regularization makes training from scratch in general a bit better by avoiding double descent. Again, in this case, I would imagine that the dataset-based discrepancy metrics correlate with transferability. More generally, I wonder how much of these conclusions would hold excluding the double descent phenomenon, or if what we are observing is entirely due to it. If this is the case, then advocating for a feature-centric view of transfer learning is misleading. The authors should elaborate on how their proposed measure of transferability changes when regularization is introduced and discuss the implications for the broader conclusions of the paper.

4. Figure C requires better formatting.

Minor issues/questions:

1. What is M, line 161?

2. Dudley Metric not introduced

3. Assumption (22) should be explained in the main text, or at least referenced because initialization is not really discussed there.

### Questions
See weaknesses.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies an analytical model for transfer learning in deep linear networks. To begin, the authors prove that general wisdom surrounding feature learning, namely that being close in distribution between the source and the target domains, is not a necessary condition for transfer learning. The authors study deep linear networks trained using gradient flow and establish a measure of transfer, namely the transferability, which is the difference between the generalization error of the model trained from scratch and the one that has undergone transfer learning. The authors study the transferability phase plots as a function of source-target alignment and the data to parameter ratio for linear transfer, meaning just the readout layer is trained on the target task, and fine-tuning, where all the layers are trained on the target. Finally, the authors show empirically that their predictions hold in the case of a 2 layer relu network.

### Strengths
The paper is very well written in general and the result is novel and interesting. The model is able to capture transfer learning both just by fine tuning on the last layer, and over the whole parameters. The authors validate empirically their results on regression tasks.

### Weaknesses
The paper is generally well written and understandable, and there aren’t really any major flaws that I could find. While one may consider the very simplified setting as a weakness, especially since in deep non-linear networks and Transformers the transfer learning behaviour might be different, I believe that such models would currently be too complicated to study. While I do not find any technical flaw with the paper, I do have several questions that I detailed below.

Specifically, the core argument against dataset-based metrics for transfer learning, while mathematically sound, lacks a clear connection to practical transfer learning scenarios. The paper demonstrates that source and target distributions can be arbitrarily far apart according to metrics like KL divergence or Wasserstein distance, yet still reside within the same feature space, leading to successful transfer. However, the practical implications of this are not fully explored. It's unclear how often such scenarios occur in real-world datasets, where source and target distributions are often assumed to have some degree of overlap for effective transfer. The paper's focus on linear networks, while analytically tractable, might not fully capture the complexities of feature learning in non-linear networks, where the learned feature representations are not always a simple linear combination of the input features. This raises questions about the generalizability of the findings to more complex architectures.

### Questions
Can this framework also explain what happens in the case of gradient descent (rather than gradient flow)? As a follow up, what would be the effect of noise in stochastic gradient descent?

While I do understand and agree with Theorem 2.2, it seems to go against prior literature showing that these metrics correlate well with transfer. Would it be possible to empirically test the claim? More concretely, would it be possible to show an experiment where the source and target distributions are “far apart” with respect to the stated metrics, yet the transfer achieved is still positive?

Can these results also be extended to logistic regression in a classification setting?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper develops a theoretical framework to analyze transferability in high-dimensional regression tasks within the context of transfer learning. The authors adopt a feature-based approach, proposing that the similarity between source and target tasks is best understood through feature space overlap rather than distributional similarity. The paper establishes phase diagrams that quantify the conditions under which transfer learning outperforms training from scratch, particularly when feature space alignment is high and target data is limited. The analysis primarily focuses on deep linear networks but extends some insights to nonlinear networks.

### Strengths
This paper addresses the essential and meaningful topic of understanding transferability in transfer learning. The problem setup, including assumptions, is clearly and concisely presented.

### Weaknesses
The main theoretical results depend on assumptions like normally distributed inputs and linear source and target functions, which limit applicability. Specifically, the assumption of normally distributed inputs with a shared covariance structure across source and target domains is a strong simplification that may not hold in real-world scenarios. This assumption restricts the analysis to cases where the input feature distributions are highly similar, potentially overlooking the complexities arising from domain shifts. Furthermore, the linearity assumption for both source and target functions significantly constrains the model's ability to capture non-linear relationships present in many practical applications. While these simplifications are useful for initial analysis, the theoretical conclusions may not generalize to more complex, realistic scenarios. The paper also does not adequately address the potential impact of the dimensionality of the feature space on the transferability results. It is unclear how the phase diagrams would change with varying feature dimensions, and whether the observed trends would remain consistent.

### Questions
1. Equations (1) and (2) use the same $\epsilon$. Does this imply that the source and target outputs for a given input $x$ share the same noise component?

2. In Equation (6), could the authors clarify the interpretation of $\Theta_i$?

3. In line 174, what is the meaning of the symbol $\leq_L$?

4. Theorems 3.4 and 3.5 are referenced from Yun et al. What is the motivation for re-proving these theorems, and why are they prominently highlighted in the main text?

### Soundness
2

### Presentation
2

### Contribution
3
