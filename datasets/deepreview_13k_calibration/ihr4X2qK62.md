# Choosing Public Datasets for Private Machine Learning via Gradient Subspace Distance

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
Differentially private stochastic gradient descent privatizes model training by injecting noise into each iteration, where the noise magnitude increases with the number of model parameters.
  Recent works suggest that we can reduce the noise by leveraging public data for private machine learning, by projecting gradients onto a subspace prescribed by the public data. 
  However, given a choice of public datasets, it is not a priori clear which one may be most appropriate for the private task. 
  We give an algorithm for selecting a public dataset by measuring a low-dimensional subspace distance between gradients of the public and private examples. We provide theoretical analysis demonstrating that the excess risk scales with this subspace distance.
  This distance is easy to compute and robust to modifications in the setting.  
  Empirical evaluation shows that trained model accuracy is monotone in this distance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper extends on the recent line of work that gradients during private optimization lie in a low-dimensional subspace and hence we can reduce the curse of dimensionality by leveraging this fact. Unfortunately, since estimating the subspace privately also incurs an error that scales with the dimension, these works estimate the subspace using "publicly" available dataset and use it as a proxy to project the gradient computation on private data to the low-dimensional subspace. This paper provides a metric that measures the distance between private and public subspace.

### Strengths
The definition of the metric.

### Weaknesses
The metric studied in the paper, which uses cosine similarity to measure the closeness of two subspaces, is not novel. This concept has been extensively explored in low-rank approximation and non-private subspace estimation problems. The core idea of using the angle between subspaces, as captured by metrics like cosine similarity, is fundamental to the Davis-Kahan theorem and related results. The paper does not adequately acknowledge or differentiate its approach from this existing body of work. Furthermore, while the paper aims to provide a bound on the reconstruction error, it does so using a mix of spectral and Frobenius norms, which is problematic. Specifically, bounding the spectral norm of the error using the Frobenius norm of a related object is not standard practice in matrix approximation theory. The spectral norm is a much stronger measure of error, focusing on the largest singular value, while the Frobenius norm considers the sum of squares of all singular values. This makes the bound less meaningful, as it compares two fundamentally different error metrics. The proof techniques employed also lack novelty, as similar ideas have been used in numerous other contexts, including the analysis of singular value computations and related problems in privacy.

### Questions
No question. I believe I understand the paper well.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers finding good representative subspaces for the gradients of loss functions when training ML models using sensitive data. In particular, these gradient subspaces are obtained by evaluating the gradients using public data. The background for this: DP-SGD introduces lot of noise and degrades the model performance as the parameter dimension grows. To this end, certain projection method have been introduced (e.g., Yu et al., 2021) where an orthogonal projector is used such that the DP-noise is added only in the projected space, reducing the total expected 2-norm of the injected DP-noise from $O(\sqrt{d})$ to $O(\sqrt{k})$, where $d$ is the parameter space dimension and $k$ the dimension of the projection subspace. Then, the problem is, how to obtain a good basis for the projector. Doing this privately is challenging, and a natural choice is to use public data for this. Then the question is, which public data set to use, so that the basis would well represent the subspace where the sensitive gradients live. This paper proposes a certain metric, "Projection Metric", to evaluate the goodness of the projector obtained with the public data. This metric is studied both theoretically and experimentally. Another related contribution is to consider "second phase pre-training", where a public data pre-trained large model is fine-tuned with another public data by having a small number of trainable parameters, and then the "Projection Metric" can be used to select best possible public dataset for this second phase pre-training, in case we use some projection method in the final fine-tuning with the sensitive data.

### Strengths
- Very well written paper, everything is explained clearly and comprehensively.

- Nice contributions with introducing the projection metric and studying its properties and also with the second-phase pre-training (as the authors point our, it has not been considered before).

- Extensive and clearly explained experiments.

### Weaknesses
 - The biggest questions in my mind after reading the paper are related to the computational efficiency of the method. I think these questions are related to these projection methods in general, but of course are directly related to using this projection metric also. I don't really see it discussed anywhere, in the appendix either. Suppose I use that second phase pre-training such that I DP fine-tune LoRa parameters using some public dataset. There would be some $O(10^4)$ parameters, let's say there are 40k of them. And the public dataset size would be, let's say $O(10^5)$. Wouldn't computing the $V_{public}$ using SVD be quite expensive in this case? Or should I somehow limit the number of trainable parameters, the public dataset size, or use stochastic approximations to obtain $V_{public}$, or some other approximative numerical methods? As far as I see, one should update $V_{public}$ quite frequently? How frequently? I am just trying to think of a practical scenario, and what would one need to take into account when using these projection methods and this projection metric. E.g., when I compare public datasets, which one to use for construction the projector, should I just take some random subsets of them as candidates and would that be sufficient?

-  Overall, I think the presented ideas are intuitive and I believe useful but on theoretical level the contribution is not big, the value is on the experimental side. All in all this is a nice contribution and I appreciate also the "second phase fine-tuning" part of the paper and the careful experiments. I think this paper would fit well to this venue.

### Questions
- I have mostly questions related to the computational efficiency (see above). In the experiments of this paper, how big was the computational burden of choosing and using the projectors? I mean if you compare, e.g., to DP-SGD?

Comment: I think the form of the "projection metric" with those cosine principal angles as given in Definition 2 is quite intuitive, but I think the form where it is written with the Frobenius norm (used e.g. in the proof of Lemma 4.1) makes it even clearer, perhaps you could consider moving that to the main text? Just to quickly mention it.

Minor comments:

- Dot missing after Eq. 4
- There are some dots left to the tables all over, e.g. on page 8 and in the appendix.
- Page 20, paragraph "Experiment Setting", third line: bracket missing
- Page 21, before D.3 title: dot in the middle of the page

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the Gradient Subspace Distance (GSD), a metric to quantify the difference between two data sets: First, finding the gradient subspace of two data sets and then computing the distance between two subspaces.
The GSD was used in selecting public datasets in both pre-conditioning and transfer learning settings in this paper, and some experiments were done to support this.

### Strengths
1. The combination of public data and private is something interesting in differential privacy, and this paper follows that flow.
2 The. introduces the Gradient Subspace Distance (GSD) is something new in the measure of similarity of data sets.
3. The quality of presentation this paper is Good.

### Weaknesses
1. GSD-based public data set selection may leak sensitive information.



### Questions
1. What is running time (time complexity) of Algorithm 1 Gradient Subspace Distance (GSD) ?
2. It is unclear why Gradient Subspace Distance is a good measure of the similarity of data sets in nature.
3. In Lemma 4.1 what is the relationship between singular values and gradient subspace distance, which one is larger?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Considering training a network privately via differential privacy, this work adopts a two-phase pre-training followed by a low-dimensional adaptation as the training pipeline to achieve better performance. Specially, both the second phase pre-training and low-dimensional adaptation are executed suing a public dataset selected from plenty of candidates via the proposed gradient subspace distance measure. The authors have conducted experiments on various architectures and datasets demonstrate the effectiveness of the proposed method.

### Strengths
i) A high-quality basis would be crucial for the performance of low-dimensionally projected DP-SGD. This work manages to achieve this goal by identifying the most suitable public dataset from a group of candidate for computing the basis.

ii) The paper provides analysis to justify why choosing a basis with a smaller gradient subspace distance is beneficial in the context of low-dimensionally projected optimization.

### Weaknesses
i) Computing the basis using private dataset compromises privacy, as the basis is directly depending on the private data. Although the authors argue that this can be considered as tuning hyperparameters, such an argument is unconvincing. In particular, this work does not conserve privacy for basic hyperparameter-tuning such as learning rate. Compared to related works or baselines, the proposed method definitely loses more privacy .

ii) The authors claim to focus on smaller public datasets due to computational resource limitations. For instance, instead of pre-training a network in CIFAR100, a batch of CIFAR100 data is selected for the projected DP-SGD. However, this argument seems weak. In my experience, projected DP-SGD is resource -intensive due to the basis calculation and gradient matrix storage. I suspect that conducting PEFT on the entire CIFAR100 dataset followed by vanilla PEFT DP-SGD could be faster and yield better results. This raises questions about the motivation and necessity of devising such a multi-stage training pipeline. The authors could conduct some additional experiments and provide details on running time, memory usage and configurations to justify the merits of their framework.

iii) The best utility gains reported in the experiments are primarily achieved when the private dataset is used as the public dataset. This result is trivial and does not demonstrate the necessity of employing GSD. Additionally, only a limited number of candidates are reported in each experiment, making it is unclear whether the GSD order is aligned well with the actual utility gain.

iv) Most of the utility gains are marginal. I also note the reported results are poor given that the networks are pre-trained. Specifically, the best results of CIFAR10 and FMNIST are worse than or only comparable to some basic baselines, e.g. [1].  Although the original paper of this baseline does not report the results of $\epsilon=2$, the authors can run its code to verify this.

### Questions
In addition to my questions in the weaknesses section, I have the following questions:

i) Is it consistently the case that CIFAR100 is a better public dataset for CIFAR10 than CIFAR10 itself, regardless of variations in batch size and the data points selected for basis calculation?

ii) Based on the experimental results, it seems that visually similar datasets usually make the best choices. Could Frechlet inception distance, which is widely used in generative models, serve as a replacement for GSD?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
