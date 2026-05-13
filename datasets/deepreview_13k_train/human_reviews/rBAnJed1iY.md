# A Provably Robust Algorithm for Differentially Private Clustered Federated Learning

- Decision: Reject
- Scores: 3, 8, 3, 6

## Abstract
Federated Learning (FL), which is a decentralized machine learning (ML) approach, often incorporates differential privacy (DP) to enhance data privacy guarantees. However, differentially private federated learning (DPFL) introduces performance disparities across clients, particularly affecting minority groups. Some recent works have attempted to address large data heterogeneity in vanilla FL settings through clustering clients, but these methods remain sensitive and prone to errors further exacerbated by the DP noise, making them inappropriate for DPFL settings. We propose an algorithm for differentially private clustered FL, which is robust to the DP noise in the system and identifies clients’ clusters correctly. To this end, we propose to cluster clients based on both their model updates and training loss values. Furthermore, when clustering clients’ model updates, our proposed approach addresses the server’s uncertainties by employing large batch sizes as well as Gaussian Mixture Models (GMM) to reduce the impact of DP and stochastic noise and avoid potential clustering errors. This idea is efficient especially in privacy-sensitive scenarios with more DP noise. We provide theoretical analysis justifying our approach, and evaluate it extensively across diverse data distributions and privacy budgets. Our experimental results show its effectiveness in addressing large data heterogeneity in DPFL systems with a small computational cost.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work propose a new differentially private clustered federated learning method based on training a GMM. The authors conduct convergence analysis on the proposed method and evaluated the method on multiple real world datasets.

### Strengths
- The problem of private clustered FL is important to study.
- The method comes with some theoretical guarantees.

### Weaknesses
 - The author claim the proposed method is private, but it is unclear what the level of privacy is enforced and what the threat model is in this work. It looks like the privacy notion being used here is example-level privacy since DP-SGD is used and the goal is to protect the server / other clients within the same cluster from inferring information of example? If that is the case, shouldn't the clustering process itself also be privatized? Specifically, the clustering in the first round is performed on noisy model updates, but the subsequent loss-based clustering is done locally, which raises questions about consistency in privacy guarantees across the different stages of the algorithm.
- There's no theoretical results of the DP bound for the proposed method. Further, due to lack of formal threat model, it's unclear what privacy guarantee the proposed method provides. It is not clear how the composition theorem is applied, especially with the two-stage clustering approach. The privacy analysis should explicitly state how the privacy budget is spent across the different stages of the algorithm.
- 4.3.1 seems problematic. Since the data augmentation is done by transformation of some data $x$, that means if you change $x$, all the augmented data also change. Therefore, in this scenario, there wouldn't be the case where the neighboring dataset only differs in one data point. And due to the way the averaging is done (average over all examples within the batch rather than first average over all augmented data for one example and then do a second level averaging), what I see is for every step of noisy stochastic gradient update, we are having a group privacy guarantee here rather than standard DP guarantee. Therefore, adding the same amount of noise would not give you better privacy with the presence of augmented data. Further, saying per instance DP is also misleading since the proposed method seems to only focus on standard DP notion rather than any per-instance DP guarantee.
- L433: "define client-level fairness as the equality of “privacy cost" across clients" is highly misleading. As I mentioned earlier, it is unclear what the privacy guarantee is here. However, fair prediction across clients does not equate to any privacy protection at either example level or client level. The performance drop due to DP should not be conflated with privacy cost, which is typically associated with the privacy parameter $\epsilon$.
- Empirical results only show results for $\epsilon=5$. I did not see where $\delta$ is defined. Also could the authors show the pareto frontier for privacy-utility / privacy-fairness tradeoff? The lack of exploration across different privacy parameters limits the practical insights of the proposed method. The paper should include a sensitivity analysis of the privacy parameters.
- The claim that "We propose the first DP clustered FL algorithm" should be more careful as there are several private federated clustering work, e.g. [1,2]

### Questions
- How does the author handle scenarios where some clusters consists only limited amount of clients (e.g. 1/2), in which case given same privacy, utility could be drastically compromised?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies the problem of accuracy disparities among clients in federated learning on their own local data distributions, especially with differential privacy. One approach to address this in the literature is to cluster the clients with similar model updates or training loss to share a model. The main contribution of this paper is to enable clustered federated learning with differential privacy. This is achieved by the authors' following observations: (a) in early rounds, model losses are not meaningful, (b) in early rounds, model updates depend too much on its initialization, but when initialization is fixed, the model updates are more stable if not using SGD but using full batch gradient descent (c) in late rounds, model updates are very small and hence not helpful. Guided by these observations, the paper proposes RC-DPFL, which uses fixed initialization, full batch learning in the first round, and for early rounds, GMM on model updates to cluster the clients (to give a probability distribution for each client's cluster), while clustering clients based on their training loss in later rounds. The authors prove that: (a) full batch training reduces uncertainty in the model updates/gradients such that the overlap between GMM component on the model updates is bounded (b) if the first rounds model updates are i.i.d. sampled from a mixture of Gaussian, the GMM has super-linear convergence rate. Empirical evaluation shows that RC-DPFL indeed finds the correct cluster of the clients and achieve high level of fairness in term of client's accuracy.

### Strengths
* Interesting and important problem: performance disparities among clients in FL
* Detailed and complete literature review on FL, FL personalization and fairness, clustered FL and DP
* Novel algorithm that combines different approaches and is theoretically guided
* Comprehensive experimental results on different types of data heterogeneity
* The paper is structured nicely and I enjoyed reading the paper

### Weaknesses
 * It seems that Theorem 4.3 has a very strong assumption that in the first round, the model updates from all clients are i.i.d. and sampled from a Gaussian mixture, and the theorem argues that under such assumption, the GMM can converge faster with larger batch size. May I know if this assumption on model updates are well justified? Is it a standard assumption or is it in fact likely true in practical settings? The assumption of i.i.d. model updates, even if drawn from a mixture of Gaussians, seems questionable given that the data distributions across clients are explicitly non-i.i.d. This discrepancy between the data and update distributions needs further justification. Specifically, how can we be sure that the model updates, which are functions of non-i.i.d. data, will behave as if they are i.i.d. samples from a Gaussian mixture? The theorem's reliance on this assumption weakens its practical relevance.
* Some settings of the experiments are not clearly described. For example, how to choose the time to switch from update-based GMM soft clustering to loss-based hard clustering? How does the server know and set the hyperparameters of the Gaussian mixture model, such as the number of clusters? I would like to see that how different choices of these parameters (i.e., switching round and number of clusters) will affect the results. The lack of clarity on how to determine the switch from update-based to loss-based clustering is a significant concern. The paper mentions a 'confidence' measure, but it is not clear how this is quantified and used in practice. Furthermore, the GMM's performance is highly sensitive to the choice of hyperparameters, especially the number of clusters. The paper needs to provide a more detailed explanation of how these parameters are set and how the algorithm's performance varies with these choices. Without this, the practical applicability of the method is limited.
* Some minor typos and grammatical errors. For example, in line 187--188, should it be "the larger the batch size, the smaller the variance"?

### Questions
I raised a few questions in the weakness section when I list my concerns. I will appreciate it if the authors could address those questions.

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
The paper looks at the problem of differentially private (DP) federated learning (FL) when the clients have heterogeneous data sets. The authors propose to use a Gaussian mixture model (GMM) on the server side to cluster similar clients to mitigate the issues when updating the global model. The authors note that the uncertainty in the clustering is highest during the first update and the client updates get smaller during training, and therefore propose a multi-stage method that i) uses full batches and soft clustering on client model updates on the 1st epoch, ii) then does smaller batches with hard-clustering still on client model updates for some epochs, iii) and finally switches to using hard clustering on client losses towards the end of the training. The authors present some theoretical motivation for the different stages, and empirically show that their method outperforms their own baselines on several image recognition tasks.

### Strengths
i) Increasing the robustness of FL w.r.t. client heterogeneity is an important topic.

ii) Including DP to the clustered FL approach, while not completely novel, seems like a potentially sound direction.

iii) The paper is mostly clear-enough to read, although it could be improved still.

### Weaknesses
i) Some of the claimed novel results are very close to published results (Lemma 4.1, see Questions below for details).

ii) I doubt that some of the claims about DP hold (see Questions below for details).

iii) All the experiments are run assuming that the true number of clusters is known. There are also no experiments using data with inherent splits, only with simulations.

iv) It is not clear what effect different design choices have on the results, as there is no ablation study (e.g., changing batch size after initial update, switching from soft to hard clustering later, using data augmentations or not, etc.).

v) There are no baselines using other approach beyond clustering aimed at addressing heterogeneity in DPFL (see, e.g., Shen et al. 2023, Silva et al. 2022,  Yang et al. 2023).

vi) Most results do not report any deviation measure besides, e.g., the mean.

### questions:
 ### Update after the discussion

I still recommend rejecting the paper: as detailed in the discussion, the main issue is that while the proposed method is claimed to be DP, I think there is a clear violation of formal DP guarantees in the proposed method (the privacy leakage from clustering based directly on the (non-DP) local loss is not accounted for in the privacy budget, as acknowledged by the authors). This is not acceptable.

### Original comments

Questions and comments In decreasing order of importance:

1) Alg 1, line 21: when switching to loss-based clustering, how is DP guaranteed (or if this is required)? I do not seem to find any details on how exactly this part works.
   
2) Lemma 4.1: the actual content as well as the proofs seem to be very close to the results stated in Sec 3 and the corresponding proofs in Malekmohammadi et al. 2024 (compare e.g. their Appendix C, eqs 12 & 13 to your Appendix D eqs 8 & 9). Are you aware of this work? The general result is also closely related to Räisä et al. 2024.

3) Sec 4.3.1: I do not understand why using data augmentations would *improve* per-instance (=per sample) DP guarantees. Looking at releasing the sum of gradients at client $i$ for a single iteration, say we use clipping constant $C$, and add $|	au|$ augmentations for each sample. Then I would claim that the sensitivity for the sum is $C |\tau|$ (as the worst-case effect of changing a single sample in the data results in all the corresponding augmentations to also change), not $C$ as you state (as we are not interested in protecting a single augmentation but the actual sample). Do I misread this somehow?

4) How are all the hyperparameters tuned for the proposed method and for the baselines? Please include a proper description of this at least to the Appendix. Also mention other relevant details, like if and when exactly you use data augmentations, etc.
 
5) Sec 5.1, on the baselines: please state somewhere how exactly do you implement DP version of loss based clustering methods (as the loss values as such are sensitive, you need to add DP somewhere, i.e., you need extra DP mechanism to release also the loss besides the local weights; this is related to issue 1)).

6) All experiments: please also clearly report $\delta$ besides $\epsilon$ for all DP runs.

7) Def 3.1: Please also state explicitly which neighbourhood definition you use with DP (e.g. add/remove).

8) Lines 136-140: Do you actually use the classical Gaussian mechanism for something, if all accounting is done using RDP?

### Minor issues (no need to acknowledge or comment on these)
* Please fix typos on lines: 117, 144-45 (differing datasets are the same?), 187-88 (should be larger batch size or variance?)
* Lines 51-53: On the disparate impact of DP: there is also contrary evidence that DP has in some sense only a limited impact on fairness (e.g. Berrada et al. 2023, Mangold et al. 2023)

### Questions
### Update after the discussion

I still recommend rejecting the paper: as detailed in the discussion, the main issue is that while the proposed method is claimed to be DP, I think there is a clear violation of formal DP guarantees in the proposed method (the privacy leakage from clustering based directly on the (non-DP) local loss is not accounted for in the privacy budget, as acknowledged by the authors). This is not acceptable.

### Original comments

Questions and comments In decreasing order of importance:

1) Alg 1, line 21: when switching to loss-based clustering, how is DP guaranteed (or if this is required)? I do not seem to find any details on how exactly this part works.
   
2) Lemma 4.1: the actual content as well as the proofs seem to be very close to the results stated in Sec 3 and the corresponding proofs in Malekmohammadi et al. 2024 (compare e.g. their Appendix C, eqs 12 & 13 to your Appendix D eqs 8 & 9). Are you aware of this work? The general result is also closely related to Räisä et al. 2024.

3) Sec 4.3.1: I do not understand why using data augmentations would *improve* per-instance (=per sample) DP guarantees. Looking at releasing the sum of gradients at client $i$ for a single iteration, say we use clipping constant $C$, and add $|\tau|$ augmentations for each sample. Then I would claim that the sensitivity for the sum is $C |\tau|$ (as the worst-case effect of changing a single sample in the data results in all the corresponding augmentations to also change), not $C$ as you state (as we are not interested in protecting a single augmentation but the actual sample). Do I misread this somehow?

4) How are all the hyperparameters tuned for the proposed method and for the baselines? Please include a proper description of this at least to the Appendix. Also mention other relevant details, like if and when exactly you use data augmentations, etc.
 
5) Sec 5.1, on the baselines: please state somewhere how exactly do you implement DP version of loss based clustering methods (as the loss values as such are sensitive, you need to add DP somewhere, i.e., you need extra DP mechanism to release also the loss besides the local weights; this is related to issue 1)).

6) All experiments: please also clearly report $\delta$ besides $\epsilon$ for all DP runs.

7) Def 3.1: Please also state explicitly which neighbourhood definition you use with DP (e.g. add/remove).

8) Lines 136-140: Do you actually use the classical Gaussian mechanism for something, if all accounting is done using RDP?

### Minor issues (no need to acknowledge or comment on these)
* Please fix typos on lines: 117, 144-45 (differing datasets are the same?), 187-88 (should be larger batch size or variance?)
* Lines 51-53: On the disparate impact of DP: there is also contrary evidence that DP has in some sense only a limited impact on fairness (e.g. Berrada et al. 2023, Mangold et al. 2023)

### References:

Berrada et al. 2023: Unlocking Accuracy and Fairness in Differentially Private Image Classification.

Malekmohammadi et al. 2024: Noise-Aware Algorithm for Heterogeneous Differentially Private Federated Learning.

Mangold et al. 2023: Differential Privacy has Bounded Impact on Fairness in Classification.

Räisä et al. 2024: Subsampling is not Magic.

Shen et al. 2023: Share your representation only.

Silva et al. 2022: FedEmbed: Personalized Private Federated Learning.

Yang et al. 2023: PRIVATEFL: Accurate, Differentially Private Federated Learning
via Personalized Data Transformation.

### Soundness
1

### Presentation
2

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
The authors propose RC-DPFL, a robust clustering algorithm to address performance fairness under privacy constraints. The algorithm uses client clustering based on both model updates and training loss values to mitigate the negative impacts of DP noise. The authors provide theoretical results to justify their claims and conduct extensive experiments. RC-DPFL is empirically effective in mitigating the disparate impact of DP noise.

### Strengths
1. The empirical results are promising. Namely, RC-DPFL performs close to the oracle algorithm in terms of accuracy, fairness, and clustering accuracy.
2. The authors provide interesting theoretical results on how large batch sizes can improve clustering accuracy and reduce noise.
3. The algorithm is evaluated across various data distributions and privacy budgets, demonstrating its ability to handle heterogeneous datasets while maintaining computational efficiency and fairness.

### Weaknesses
1. The article is not well organized. I cannot find the appendix authors mentioned in the main content. Namely, the theoretical proofs, details of the experiment implementation, table 1, table 10, and table 11 are missing. As a result, reviewers cannot verify theoretical claims and experimental results.

2. Assumption 3.2 is confusing. Please modify the statements if there is any typo/error. How could the gradient variance upper bound $\sigma_{i,g}^2$ decrease when we use a smaller batch size $b$?

   - Does Assumption 3.2 contradicts Lemma 4.1?

   - Which theoretical result requires Assumption 3.2? It's unclear from the paper.

   - Is there any other assumption not mentioned in the main content? The proof of FL convergence typically requires some standard assumptions. For example, some FL papers require smoothness and bounded gradients (Assumption 1, 2, 3 in Reddi et al., 2021).

     Reference: “Adaptive Federated Optimization” by Sashank Reddi et al., ICLR 2021.

3. In figure 1, the motivation of using smaller batch sizes in the third stage is unclear. Can we use a fixed batch size throughout the training process?

   - In real implementations of (centralized) DP-SGD, people usually use very large batch sizes to improve the performance. Why should the clients switch to a smaller batch size?

     Reference: "Unlocking High-Accuracy Differentially Private Image Classification through Scale" by Soham De et al.

   - The authors need to provide more details about the experiment implementations. Switching the batch size changes the sample rate of the training data. This could lead to some issues on the privacy composition. To the best of my knowledge, this functionality is unavailable in popular python DP libraries like Opacus or fastDP by awslabs.

4. The server hard clusters clients based on their loss values after $E_c$ rounds. The local loss function of a client is privacy sensitive as it is a function of the local training data. What kind of privacy mechanism is applied to ensure the privacy guarantee when sharing the local loss values? How does privacy accounting work in RC-DPFL given that different statistics (gradient updates, loss values) are shared?

5. One limitation is that the algorithm assumes the number of client clusters is known beforehand, which may not always be the case in real-world applications. This could reduce the applicability of the algorithm without prior knowledge or estimation of clusters.

### Questions
1. Could you please explain the results in figure 3(c) and 5(c)? For example, why are the success rates of f-DPFL non-monotonic as we increase $\epsilon$? Why do the success rates suddenly drop to zero in ($epsilon=5$, covariate shift, CIFAR-10), ($\epsilon=4$, MNIST), and ($\epsilon=3,5$, FMNIST)?

2. Could you please explain the intuition of Lemma 4.1? Previous theoretical results also suggest that the variance of the stochastic gradient estimator is a decreasing function of $b$. For deep neural networks with L2 loss we show that the variance of the gradient is a polynomial in $1/b$ (Qian et al., 2020). Is this different from Lemma 4.1? Does Lemma 4.1 consider different models other than deep neural networks?

      Reference: "The Impact of the Mini-batch Size on the Variance of Gradients in Stochastic Gradient Descent" by Xin Qian, Diego Klabjan.

### Soundness
2

### Presentation
2

### Contribution
2
