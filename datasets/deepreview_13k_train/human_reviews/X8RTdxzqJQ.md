# Revisit Non-parametric Two-sample Testing as a Semi-supervised Learning Problem

- Decision: Reject
- Scores: 6, 6, 3, 3, 6

## Abstract
Learning effective data representations is crucial in answering if two samples X and Y are from the same distribution (a.k.a. the non-parametric two-sample testing problem), which can be categorized into: i) learning \emph{discriminative representations} (DRs) that distinguish between two samples in a \emph{supervised-learning} paradigm, and ii) learning \emph{inherent representations} (IRs) focusing on data's inherent features in an \emph{unsupervised-learning} paradigm. 
However, both paradigms have issues: learning DRs reduces the data points available for the two-sample testing phase, and learning purely IRs misses discriminative cues. To mitigate both issues, we propose a novel perspective to consider non-parametric two-sample testing as a \emph{semi-supervised learning} (SSL) problem, introducing the \emph{SSL-based Classifier Two-Sample Test} (SSL-C2ST) framework. While a straightforward implementation of SSL-C2ST might directly use existing \emph{state-of-the-art} (SOTA) SSL methods to train a classifier with labeled data (with sample indexes X or Y) and unlabeled data (the remaining ones in the two samples), conventional two-sample testing data often exhibits substantial overlap between samples and violates SSL methods' assumptions, resulting in low test power. Therefore, we propose a two-step approach: first, learn IRs using all data, then fine-tune IRs with only labelled data to learn DRs, which can both utilize information from whole dataset and adapt the discriminative power to the given data. Extensive experiments and theoretical analysis demonstrate that SSL-C2ST outperforms traditional C2ST by effectively leveraging unlabeled data. We also offer a stronger empirically designed test achieving the SOTA performance in many two-sample testing datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce SSL-based classifier two-sample test framework that addresses limitations of discriminative representations (DRs) and inherent representations (IRs). DRs reduce the data points available for testing phase whereas IRs do not provide discriminative cues.
Both IRs and DRs need some supervision to learn good representation (DRs) or good candidate kernels (IRs). For this, the authors propose a semi-supervised learning (SSL) framework, which utilizes features learned in an unsupervised manner to fit additional classifier head to maximize the test power.

### Strengths
- Writing: The task of two-sample testing is clearly defined, with concise notations and a clear outline of the limitations of existing supervised and unsupervised approaches.
- Novelty: The paper is novel in applying a semi-supervised learning framework to the two-sample testing problem, a first in this area. The proposed framework is simple yet effective, as demonstrated by the experimental results.
- Proof of concept: Section 4, Figure 2, and Table 1 illustrate why a straightforward application of existing SSL methods may fail in certain cases, such as the HDGM-medium and HDGM-hard tasks. This clarifies the motivation for the proposed SSL-C2ST approach.
- Theoretical justification: The authors provides why more unlabeled data points can help improving test power.
- Empirical support: The experiment results on several datasets show the superiority of the proposed method over existing state-of-the-art two-sample testing methods.

### Weaknesses
 * Writing: The limitations of DRs and IRs, along with the motivation for the proposed method, are reiterated throughout Sections 1 and 3 without providing additional insights. Although recognizing these problems is key to the paper’s contributions, a single, well-placed explanation could make the writing more concise.
* Novelty: The proposed SSL-C2ST pipeline is straightforward and highly effective, but it closely resembles standard fine-tuning practices, where only the last few layers are updated after learning self-supervised features — a common approach in neural network training. The method's novelty is further diminished by its reliance on a basic autoencoder for feature extraction, a technique that has been extensively explored in prior work.
* Ambiguity: It is not very clear if obtaining features in an unsupervised manner is classified as SSL. Related to this, what do the authors think the underlying assumption of auto-encoder features is for SSL tasks if none of the three assumptions apply for this?

### Questions
1. Could you elaborate the equivalence between$max_\epsilon \frac{ (1/2- \epsilon) }{ \sqrt{\epsilon - \epsilon^2} }$ and $min_\epsilon \frac{\epsilon} {\sqrt{\epsilon - \epsilon^2} }$? It is not very obvious to me because of the denaminator.
2. In Theorem 5.3, I understand as $m_u$ increases, the third term in Eq.(8) decreases but how does that affect $\epsilon(P, Q; f’^*)$? I wonder 1. $\epsilon(P, Q; f’^*)$ does not depend on $m_u$, 2. If so, when $\epsilon(P, Q; f’^*)$ is large, is the upper bound effective?
3. Auto-encoder is not the only way to obtain unsupervised-learning features. In fact, contrastive learning is perhaps more popular and effective. Is there any particular reason why the authors restricted unsupervised-learning features to be auto-encoder-based features?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a new approach towards non-parametric two-sample testing, by first learning inherent representations using both labeled and unlabeled data, and then fine-tuning these representations by additionally learning discriminative representations using labeled data. The effectiveness of this methodology over traditional classifier two-sample testing is demonstrated via experiments and theory. The intuition behind additional utilization of unlabeled data seems solid, and the results are commendable.

P.S. My expertise in two-sample testing is limited, thus I am judging the paper mostly from the angle of how effectively the representations are learnt, thus unsure about the contributions and novelty in the given sub-field but curious to hear from other reviewers.

### Strengths
- [S1] The authors clearly highlight the issues with the current methodologies, particularly when viewed from the bucket of supervised and unsupervised methods. The proposed approach cleverly circumvents this problem for both buckets. The applicability to different scenarios seems to be the biggest plus point of using SSL based testing methods.
- [S2] The authors also negate the initial thoughts one might have on reading the setup and motivation by discussing the failure modes for SOTA SSL methods in this two-sample testing scenario.
- [S3] The proofs add a lot of value to the paper, and along with the provided code, make the submission a quite complete pitch.

### Weaknesses
 - [W1] I think some reorganization might help the paper read better, for example including the Algorithm 1 in the main paper perhaps at the cost of some preliminaries or shortening the introduction could help understand the proposed method better. Right now, while the motivation and setup comes across very clearly, the details of the approach are somehow missed, and the key points of why the method works in practice, while written in words, are not evident algorithm wise.
- [W2] On a similar note, I’m slightly unsure where the exact improvements are coming from, is it possible to look at some ablations where one of the steps was modified, say the featurizer for learning IRs was an suboptimal one, how would the learning DRs be affected? It would be helpful to understand the utility of each part of the sequential method proposed by the authors.

### Questions
- [Q1] For Table 1, I understand there is no standard deviation across one sampling of two groups, but would there not be several runs of such samplings that could be aggregated against and then the standard deviation be expressed? While the result of each trial is 0 or 1, would it not be more insightful to have several trials (say 5) and report the results across them in total?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose a semi supervised classification based method to perform two sample testing. The problem of two sample testing is as follows: given a finite set of samples from two distributions $P, Q$,  $S_p = (x_1, \dots x_n) \sim P$ and $S_q = (y_1, \dots y_m) \sim Q$, the task is to tell whether $P = Q$ or not. In classifier based two sample testing, a classifier is trained on a split of the data, and the test statistic - the average classification accuracy is estimated on the test split. The null hypothesis, i.e. $P = Q$ is rejected if the test statistic is sufficiently greater than random guessing. 

The semi supervised method proposed by the authors instead first learns common features of the samples by training an auto encoder based on reconstruction loss on all of the data in $S_p \cup S_q$. This gives us extracted features $S'_p = (\phi(x_1) , \dots \phi(x_n))$ and $S'_q = (\phi(y_1), \dots \phi(y_m))$. Then the usual classifier based two sample testing is performed on $S'_p, S'_q$. 

The authors provide a theorem characterizing a lower bound on test power based on number of unlabeled samples and VC dimension of classifier function class placed on top of featurizer $\phi$, and VC dimension of some compatibility function class that depends on the overall function class (input space to output space).

The authors finally provide some experimental evaluation on some low dimensional synthetic datasets (d = 2 - 10), and two real datasets -  MNIST vs MNIST fake, and Imagenet vs Imagenet fake. On these datasets their method performs better than C2ST.

### Strengths
A new method for two sample testing based on a two stage process of extracting features in an unsupervised manner, and then performing C2ST on extracted features instead of original data.

### Weaknesses
The paper has several weaknesses.

The overall presentation and organization of the paper is very poor. The actual details of the method appears quite late on page 6. The introduction section is unreasonably long. Figure 2 looks unnecessary. Figure 1 and Figure 3 are repeated. Experiment results are split across multiple sections (Table 1 in introduction, then Table 2, Figure 4 and Figure 5 in Experiments section), whereas they could have been clubbed under Experiments section. Inconsistency in experiments. In table 1 comparison is shown against 5 baselines, whereas in Table 2 it is shown against 4 baselines. Figure 4 looks unnecessary as the results already exist in table 1 and table 2. Proper details on the experimental evaluation are not provided. For instance the details of the model used for feature extractor $\phi$ is not provided. The experimental details of different baselines also not provided clearly. The theorem is quite unclear, notation is missing for instance $\chi(f, x)$ is not defined. No clear understanding of why and when is semi supervised learning better than supervised learning is provided. The proofs in the appendix are quite unclear, for instance proper references to equations is missing.

### Questions
1. Definition of $\chi$ in Definition 5.2 is not clear. How is $\chi(f, x)$ defined ? Proof of Theorem 5.3 is also very unclear. What is $\mathcal{C}[2m_1, \mathcal{S}]$, the notation is not defined. $m_1$ is also not defined (although it could be inferred that $m_1$ is number of labeled data).

2. Not clear from the theorem how this gives more power than C2ST ?

3. “Although the differences between two methods are little when N is small, the test power of SSL-C2ST has a huge gap over C2ST when N is large enough” This only seems to be the case for the right most figure ?

### Soundness
2

### Presentation
1

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
This paper revisits non-parametric two-sample testing as a semi-supervised learning problem. Specifically, AE-based representation learning is used with labeled data by removing labels, and then the standard C2ST procedure is used with the labeled data. The superior test power was demonstrated on two image datasets, i.e., MNIST and ImageNet.

### Strengths
- The paper demonstrated that using unsupervised learning, i.e., AE-based representation learning, improved the test power of C2ST.

### Weaknesses
 - The datasets used in experiments were from the computer vision domain only. It is not clear that the proposed method will be effective in other domains. At least, the datasets used in the existing study need to be used to demonstrate the usefulness of the proposed method.
- Although interesting insights into improving C2ST with unlabeled data exist, the current presentation is not easy to follow. For example, the theoretical analyses have some unclear points, particularly regarding the definition of \(err_\mathrm{unl}(\phi_f)\) and its relation to the compatibility function \(\chi(f, \mathcal{S})\). The connection between the feature extractor \(\phi_f\) and the overall classifier \(f\) is not clearly established, making it difficult to assess the validity of the analysis. The role of \(\psi\) in the method is also unclear, as it is learned but not included in the theoretical analysis, raising questions about the analysis's completeness.


### Questions
- In Step 1, AE-based representation learning is adopted. Another possible method is recent self-supervised learning. Is AE the best choice?
- Since Theorem 5.1 cites Lopez-Paz & Oquab (2018) and Theorem D.3 (the proof of Theorem 5.3) cites Boucheron et al. (2000) at the beginning, it is not easy to distinguish which parts are the contribution of this paper. Could you clarify it?
- $N = n$?, $N = m$?, or $N = n+m$?
- It is unclear how many unlabeled samples help improve the test power.
- What are $\delta$ and $\delta_{m_u,m_l}$ in Theorem 5.3?
- Semi-supervised learning often assumes labeled data and (a large amount of) unlabeled data, and both labeled and unlabeled data are simultaneously involved in training. However, this paper assumes labeled data only. In this sense, the paper sounds like it claims that an unsupervised pre-training step (by removing labels of labeled data) helps improve C2ST performance.
- From the SSL setting viewpoint, the proposed method can be compared with SSL methods using, e.g., 1,000 labeled and 10,000 unlabeled samples.
- In Sec 5.2, the setting in this paper implies m_l=m_u and labeled samples are identical to unlabeled samples. Applying the existing analysis to SSL may not be valid since the assumptions of the existing analysis and this paper are probably different. This paper should carefully discuss such a difference in the assumption.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel perspective to consider non-parametric two-sample testing as a semi-supervised learning (SSL) problem, introducing the SSL-based Classifier Two-Sample Test (SSL-C2ST) framework. The authors propose a two-step approach: first, learn IRs using all data, then fine-tune IRs with only labelled data to learn DRs, which can both utilize information from whole dataset and adapt the discriminative power to the given data.

### Strengths
1.The paper is written well and is easy to understand.

2. The studied problem is very important.

3. The results seem to outperform state-of-the-art.

### Weaknesses
1. My concern of the learning setting that is proposed in this paper is its difference and benefits compared to positive-unlabeled learning [1] and semi-supervised out-of-distribution detection [2]. Could the authors clarify or include some empirical justifications on the benefits of the proposed learning algorithm?

2. What are the key assumptions of the theoretical analysis made in the paper? Are there any empirical justification on their validity on large datasets?

### Questions
see above

### Soundness
3

### Presentation
3

### Contribution
3
