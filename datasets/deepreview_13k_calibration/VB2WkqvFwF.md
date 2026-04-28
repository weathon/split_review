# The Underlying Scaling Laws and Universal Statistical Structure of Complex Datasets

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
We study universal traits which emerge both in real-world complex datasets, as well as in artificially generated ones. Our approach is to analogize data to a physical system and employ tools from statistical physics and Random Matrix Theory (RMT) to reveal their underlying structure. We focus on the feature-feature covariance matrix, analyzing both its local and global eigenvalue statistics. Our main observations are: {\it(i)} The power-law scalings that the bulk of its eigenvalues exhibit are vastly different for uncorrelated normally distributed data compared to real-world data, {\it(ii)} this scaling behavior can be completely modeled by generating Gaussian data with long range correlations, {\it(iii)} both generated and real-world datasets lie in the same universality class from the RMT perspective, as chaotic rather than integrable systems, {\it(iv)} the expected RMT statistical behavior already manifests for empirical covariance matrices at dataset sizes significantly smaller than those conventionally used for real-world training, and can be related to the number of samples required to approximate the population power-law scaling behavior, {\it(v)} the Shannon entropy is correlated with local RMT structure and eigenvalues scaling, is substantially smaller in strongly correlated datasets compared to uncorrelated ones, and requires fewer samples to reach the distribution entropy. These findings show that with sufficient sample size, the Gram matrix of natural image datasets can be well approximated by a Wishart random matrix with a simple covariance structure, opening the door to rigorous studies of neural network dynamics and generalization which rely on the data Gram matrix.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission studies the bulk eigenvalues of the Gram matrix for real-world data. The main contribution is an empirical verification that certain macroscopic (global law) and microscopic (eigenvalue spacing) spectral properties of the Gram matrix can be described by a Wishart matrix with certain correlation structures. This opens up new possibilities to use random matrix theory to understand the learning curve for realistic datasets.

### Strengths
The authors consider an important research problem: most existing random matrix theory analyses on machine learning models require strong assumptions on the data distribution, such as Gaussian with identity covariance, and one may wonder if these theoretical results have any implications in practical settings. The universality perspective in the current submission provides some justification of the Gaussianity assumption.

### Weaknesses
I have the following concerns.

1. The implications of the studied universality phenomenon on the learning behavior of machine learning models need to be elaborated. The authors motivated the study of Gram matrix using the neural scaling law, but how do the macroscopic and microscopic properties of the eigenvalues (especially the microscopic properties) relate to the power law scaling of learning performance? I cannot find such discussion in the main text. For example. although we know that the universality of eigenvalue spacing distribution can be very robust, it is unclear what insight a machine learning researcher may acquire from such statistics. It would appear that the more important quantity is the Gram matrix of the neural network representation, which has been explored in many recent works including (Seddik et al. 2020) [1] (Wei et al. 2022) [2].
* (Wei et al. 2022) More than a toy: random matrix models predict how real-world neural representations generalize.   
* (Seddik et al. 2020) Random matrix theory proves that deep learning representations of GAN-data behave as Gaussian mixtures. 

2. Related to the previous point, it should also be noted that the eigenvalue statistics alone do not decide the learning curve. For trained neural network, the aligned eigenvectors due to representation learning play a major role in the improved generalization performance, as shown in (Ba et al. 2022) (Wang et al. 2023). The authors should comment on whether such eigenvector statistics also fit into the universality perspective in this submission.    
* (Ba et al. 2022) High-dimensional asymptotics of feature learning: how one gradient step improves the representation.  
* (Wang et al. 2023) Spectral evolution and invariance in linear-width neural networks. 

3. Related works are not adequately discussed. Various forms of universality law for neural network have appeared in (Seddik et al. 2020) [1] (Wei et al. 2022) [2], and in the context of empirical risk minimization, the "Gaussian equivalence property" has been studied in many prior works, see (Goldt et al. 2020). How do these results relate to the findings in this submission? 
Also, the Marchenko-Pastur law for general covariance is a classical result that existed way before (Couillet and Liao 2022).   
* (Goldt et al. 2020) The Gaussian equivalence of generative models for learning with shallow neural networks.

### Questions
See weaknesses above.

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
This paper observes that many real-world datasets have a power law scaling for the bulk eigenvalues of their sample covariance matrices. Hence, the authors construct a correlated Gaussian dataset by designing its population covariance from a Toeplitz matrix. In this case, the power law tail is related to the strength of the correlations between different features of each sample. By comparing some global and local statistics of sample covariance matrices, such as global distribution, level spacing distribution, $r$-statistics, and spectral form factor, the authors empirically show that the sample covariance model from real-world datasets falls into the same universal class as this Gaussian model.

### Strengths
The motivation of this paper is clear and convincing for me. This work may bring attention to random matrix theory (RMT) and statistical physics communities. The local and global eigenvalue statistics used in this paper are standard and can effectively represent the spectral behaviors of the dataset. Potentially this indicates we can use classical random matrix ensembles like GOE ensemble and Poisson ensemble to analyze the spectral properties of deterministic real-world datasets, understand the representation in datasets, and construct certain metrics to measure the quality of datasets. There is another potential motivation for analyzing the eigenstructure of the datasets. In certain cases, we can use synthetic data generation like GANs to create new datasets for training. So understanding the spectral distributions of real-world datasets via correlated Gaussian datasets helps us to further investigate if the synthetic data we generate really captures the useful representation of the data. Meanwhile,

### Weaknesses
1. This paper analyzes the bulk spectra of real-world datasets by a Gaussian sample covariance matrix whose population covariance is generated by a Toeplitz matrix and power parameter $\alpha$. The construction of this Toeplitz matrix and $\alpha$ indicates the correlation among the features of each sample. However, there is no algorithm to find the suitable $\alpha$ for different datasets. The paper should explicitly describe the fitting procedure used to determine $\alpha$ from the empirical data. Furthermore, it would be more informative to have an additional discussion on power law scaling, encoding information in the Gaussian dataset, and the representation learning of the dataset. Specifically, how does the choice of $\alpha$ impact the information content and what are the limitations of using a single power-law exponent to capture the complexity of real-world data?

2. This paper focuses on bulk eigenvalues but, in machine learning, the outlier eigenvalues and eigenvector statistics are more important for learning. For instance, [1] shows that representations of GAN-data behave as Gaussian mixtures, where spikes in spectra are beneficial for linear classification. As also studied in [2], power-law tails in the spectra may not represent useful features in neural networks but the principal components contain some useful features for learning. There should be some discussion on this here to indicate this power-law scaling is useful for real-world datasets. The authors should clarify the relationship between the observed power-law scaling in the bulk and the information encoded in the outlier eigenvalues, and why focusing on the bulk is relevant for understanding real-world data representation.

3. The authors may need to present additional references in RMT or more detailed proofs for the formula they presented to help readers in the machine learning community better understand the math here. For instance, the claim in (4), formula (11) and (28). Especially, (28) seems to provide the limiting Stieljes transform of correlated Gaussian sample covariance matrix. I am not sure if this can be used to predict the bulk spectra of CGDs in Figure 2 (Bottom). The paper needs a more rigorous derivation of the spectral density for the correlated Gaussian model, and a clearer explanation of how the theoretical results connect to the empirical observations, including a discussion of the assumptions and limitations of the theoretical model.

### Questions
1. There is another random matrix model that possesses power-law scaling, heavy-tail Wigner matrices (Levy matrices), see [3-5], which may have Poisson laws in the spectra. In this ensemble, we still have i.i.d. structure but the distribution of each entry may have heavier tails. How do you exclude the case that the real-world datasets are not in this universal class?

2. This paper empirically shows that the bulk eigenvalue distribution of the Gram matrix of the real-world dataset can be mimicked by a correlated Gaussian sample covariance matrix. Does that really mean the synthetic dataset captures useful features in the real dataset? Is it possible to train a neural network separately on both real and synthetic datasets and see if they have similar generalization behaviors? This may provide a better understanding of whether this power law scaling in datasets is useful or not.

3. In the introduction, you claimed that $O(10)$ large eigenvalues are separated from bulk and the rest of bulk eigenvalues have power law. Is this order $O(10)$, in Eq. (3), a constant order or is it related to the number of classes in the dataset? Further quantified analysis may be needed to provide here by increasing the number of samples.

4. If we consider the spectra of different classes in one dataset, like CIFAR10, do they have the power law scaling with the same $\alpha$ or not in Figure 1? So far, I have not seen a relation between $\alpha$ and classes in the dataset. Concretely, does the bulk spectrum of the full dataset have the same power-law scaling as the spectrum of the data points in a certain class of this dataset?

5. Eq. (1) looks incorrect. Are $X_{ia} $ entries of the data matrix or a full matrix? You need to make the notions consistent.

6. In Eq. (2), is $\mathbf{I}_{ij}$ the $(i,j)$ entry of the identity matrix?

7. In (4), you claimed the power law of the eigenvalues of the correlated Gaussian matrix, but you showed the power law for the Toeplitz-type population covariance matrix in (24). Is this enough to conclude (4)?

8. What is $\Sigma(\rho_\Sigma)$ in exponent below Eq. (8)?

9. Can you explain the last sentence in Section 4.1?

10. How do you ensure that the population covariance $\Sigma^{\text{Toe}}$ is p.s.d from Eq. (18)?

11. The caption in Figure 8 is not in the right order.

=================================================================================================

[1] Seddik, et al. "Random matrix theory proves that deep learning representations of gan-data behave as gaussian mixtures." 

[2] Wang, et al. "Spectral evolution and invariance in linear-width neural networks."  

[3] Burda and Jurkiewicz. "Heavy-tailed random matrices." 

[4] Arous and Guionnet. "The spectrum of heavy tailed random matrices."  

[5] Guionnet. "Heavy tailed random matrices: How they differ from the GOE, and open problems."

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies the spectral statistics of the bulk of sample covariance matrices from different image datasets (MNIST, fMNIST, CIFAR10, tiny-IMAGENET). Its main result is to show that different spectral statistics of the bulk, such as the spectral density tails, level spacing, r-statistics, spectral form factor and Shannon entropy closely follows the one of correlated Wishart matrices with matching population covariance.

### Strengths
The paper is well written and relatively smooth to read. Concepts from RMT are introduced from scratch and intuition is given, making it accessible for a wider audience. The result suggesting a universality of the Gaussian ensemble for the bulk of the sample covariance matrix is interesting, and motivates the classical assumption of Gaussian data used in many theoretical works in high-dimensional statistics.

### Weaknesses
The paper has a few limitations which should be better discussed by the authors:

1. First, it only considers natural image data. The statistical properties of images have been intensively in the context of signal processing, and the observation that natural images tend to display a power-law behaviour is much older than neural scaling laws, see e.g. [Ruderman 1997]. The assumption of power-law features is also classical in the study of kernel regression, where it is known as "*capacity conditions*" [Caponnetto 2007]. The authors should acknowledge that the observed spectral properties might be a consequence of the specific data distribution and not a universal phenomenon. It is crucial to investigate whether these findings extend to other types of data, such as time series or audio signals, which may not exhibit the same power-law characteristics. The lack of such analysis limits the scope of the conclusions.

2. Second, the paper focus on the bulk of the sample covariance spectrum. While one does not expect universality beyond the bulk, they play a central role in learning. For instance, consider a $k$-Gaussian mixture data $X = y\mu^{\top}+Z$ with means $\mu\in\mathbb{R}^{d\times k}$ and labels $y\in\mathbb{R}^{N\times d}$. In this case, the information about the $k$ modes is on the outliers, and the performance of a classifier trained in this data set will crucially depend on the correlation between the labels and the means. Moreover, the outliers is crucial in feature learning: it has been recently show that for two-layer neural networks a single gradient step away from random initialisation takes precisely the form of a rank one spike that correlate with the labels [Ba et al. 2023]. The neural collapse phenomenon provides a similar observation for deep neural networks [Papyan et al. 2020]. The authors should discuss the implications of focusing solely on the bulk and acknowledge that the most relevant information for learning might be contained in the outliers, which are not covered by their analysis. This limitation significantly impacts the conclusions about the relevance of their findings to neural network dynamics and generalization.

### Questions
- **[Q1]**: In the abstract, the authors say that:
> "*These findings show that with sufficient sample size, the Gram matrix of natural image datasets can be well approximated by a Wishart random matrix with a simple covariance structure, opening the door to rigorous studies of neural network dynamics and generalization which rely on the data Gram matrix.*"

However, how these results open the door to the study of "*neural networks dynamics and generalization*" is actually never discussed. In light of my second commend in *Weaknesses* on the relationship between feature learning and generalisation with the outliers, why the authors believe the observation of spectral universality of the bulk is relevant to the study of generalisation?

- **[Q2]**: I miss a discussion on the relationship between these results and error universality, which has been intensively investigated starting from [Mei & Montanari 2022; Gerace et al. 2020; Goldt et al. 2022; Hu, Lu 2023]. Here, one looks directly at the universality of the training and generalisation error instead of the features, taking into account the labels and the task. Although more restrictive, it has been observed to hold for data close to the one studied here [Loureiro et al. 2021]. For a simple regression task, a parallel with the type of universality discussed here can be drawn, since the computation of the error boils down to a RMT problem [Wei et al. 2022]. In particular, it has been noted that in some cases the structure of the bulk fully characterises the error, even for multi-modal distributions, see [Gerace et al. 2023; Pesce et al. 2023]  



**Minor comments**:

- Although that's ultimately up to the authors, the notation $X_{ia}\in\mathbb{R}^{d\times N}$ is unconventional in machine learning.

**References**

- **[Ruderman 1997]** Daniel L. Ruderman. *Origins of scaling in natural images*. Vision Research, Volume 37, Issue 23, 1997, Pages 3385-3398, ISSN 0042-6989, https://doi.org/10.1016/S0042-6989(97)00008-4.

- **[Caponnetto 2007]** Caponnetto, A., De Vito, E. *Optimal Rates for the Regularized Least-Squares Algorithm*. Found Comput Math 7, 331–368 (2007). https://doi.org/10.1007/s10208-006-0196-8

- **[Ba et al. 2023]** Jimmy Ba, Murat A. Erdogdu, Taiji Suzuki, Zhichao Wang, Denny Wu, Greg Yang. *High-dimensional Asymptotics of Feature Learning: How One Gradient Step Improves the Representation*.  Part of Advances in Neural Information Processing Systems 35 (NeurIPS 2022).

- **[Papyan et al. 2020]** Vardan Papyan, X. Y. Han, and David L. Donoho. *Prevalence of neural collapse during the terminal phase of deep learning training*. PNAS, September 21, 2020, 117 (40) 24652-24663, https://doi.org/10.1073/pnas.2015509117.

- **[Mei & Montanari 2022]** Song Mei and Andrea Montanari. *The generalization error of random features regression: Precise asymptotics and the double descent curve*. Communications on Pure and Applied Mathematics, 75(4):667–766, 2022.

- **[Gerace et al. 2020]** Federica Gerace, Bruno Loureiro, Florent Krzakala, Marc Mezard, Lenka Zdeborova. *Generalisation error in learning with random features and the hidden manifold model*. Proceedings of the 37th International Conference on Machine Learning, PMLR 119:3452-3462, 2020.

- **[Goldt et al. 2022]** Sebastian Goldt, Bruno Loureiro, Galen Reeves, Florent Krzakala, Marc Mezard, Lenka Zdeborova. *The Gaussian equivalence of generative models for learning with shallow neural networks*. Proceedings of the 2nd Mathematical and Scientific Machine Learning Conference, PMLR 145:426-471, 2022.

- **[Hu, Lu 2023]** H. Hu and Y. M. Lu, *Universality Laws for High-Dimensional Learning With Random Features*, in IEEE Transactions on Information Theory, vol. 69, no. 3, pp. 1932-1964, March 2023, doi: 10.1109/TIT.2022.3217698.

- **[Loureiro et al. 2021]** Bruno Loureiro, Cedric Gerbelot, Hugo Cui, Sebastian Goldt, Florent Krzakala, Marc Mezard, Lenka Zdeborová.
*Learning curves of generic features maps for realistic datasets with a teacher-student model*. Part of Advances in Neural Information Processing Systems 34 (NeurIPS 2021).

- **[Wei et al. 2022]** Alexander Wei, Wei Hu, Jacob Steinhardt. *More Than a Toy: Random Matrix Models Predict How Real-World Neural Representations Generalize*. Proceedings of the 39th International Conference on Machine Learning, PMLR 162:23549-23588, 2022.

- **[Gerace et al. 2023]** Federica Gerace, Florent Krzakala, Bruno Loureiro, Ludovic Stephan, Lenka Zdeborová. *Gaussian Universality of Perceptrons with Random Labels*. arXiv:2205.13303 [stat.ML]

- **[Pesce et al. 2023]** Luca Pesce, Florent Krzakala, Bruno Loureiro, Ludovic Stephan. *Are Gaussian data all you need? Extents and limits of universality in high-dimensional generalized linear estimation*. Proceedings of the 40 th International Conference on Machine Learning, Honolulu, Hawaii, USA. PMLR 202, 2023

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
