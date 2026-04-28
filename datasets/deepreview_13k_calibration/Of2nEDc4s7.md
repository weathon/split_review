# Improved statistical and computational complexity of the mean-field Langevin dynamics under structured data

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Recent works have shown that neural networks optimized by gradient-based methods can adapt to sparse or low-dimensional target functions through feature learning; an often studied target is the sparse parity function on the unit hypercube. However, such isotropic data setting does not capture the anisotropy and low intrinsic dimensionality exhibited in realistic datasets. In this work, we address this shortcoming by studying how gradient-based feature learning interacts with structured (anisotropic) input data: we consider the classification of $k$-sparse parity on high-dimensional orthotope where the feature coordinates have varying magnitudes, and analyze the learning complexity of the mean-field Langevin dynamics (MFLD), which describes the noisy gradient descent update on two-layer neural network. We show that the statistical complexity (i.e. sample size) and computational complexity (i.e. network width) of MFLD can both be improved when prominent directions of the anisotropic input data align with the support of the target function. Moreover, by employing a coordinate transform determined by the gradient covariance, the width can be made independent of the target degree $k$. Lastly, we demonstrate the benefit of feature learning by establishing a kernel lower bound on the classification error, which applies to neural networks in the lazy regime.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors study the statistical and computational complexity of mean-field Langevin dynamics (MFLD) with anisotropic input data. In particular, they show that both complexities can be improved when prominent directions of the anisotropic input data align with the support of the target function.

### Strengths
This paper is technically solid and study an important problem. MFLD is a recent framework to help us understand the behavior of two-layer nonlinear NN, particularly relevant to the isotropic $k$-parity problem. Extending the isotropic setting to the anisotropic setting is definitely interesting to study, and the authors have established learning guarantees for two-layer nonlinear NN for this anisotropic setting.

### Weaknesses
It appears that the whole work assumes that the matrix $A$ is known a priori or prespecified. To me, this assumption might be too strong and make the problem of more theoretical interest than very practically relevant, although it seems to me that the motivation of studying anisotropic data arises from the case of realistic datasets as mentioned in the abstract.

If we have real data while $A$ is generally unavailable or can only be estimated from data, what can we say about this case with the results of this paper? 

I also wonder if the problem can be tackled with a preconditioned version of MFLD, instead of performing coordinate transforms on the input.

Typo:
- page 6, after Proposition 2: otherwise, we “still”
- page 6, after Proposition 3: Under this “condition”

### Questions
If we have real data while $A$ is generally unavailable or can only be estimated from data, what can we say about this case with the results of this paper? 

I also wonder if the problem can be tackled with a preconditioned version of MFLD, instead of performing coordinate transforms on the input. 

Typo:
- page 6, after Proposition 2: otherwise, we “still”
- page 6, after Proposition 3: Under this “condition”

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work investigates mean-field Langevin dynamics on structured anisotropic input data with a k-sparse parity target function. It provides results for specific 2-layer neural networks around both statistical and computational complexity. In particular, it proves discrete-time and finite-width learning guarantees thus extending on the results of previous work. These results are verified empirically on synthetic data.

### Strengths
Disclaimer: I have not checked the validity of the proofs in the appendix and, therefore, cannot comment on the correctness of the results.

* This work is generally well written.
* The related work seems to be well addressed (although I am not familiar with the literature). 
* The contributions are quite clearly laid out in the introduction. 
* Section 2 (and 3) does a reasonable job of laying out the problem setting.

### Weaknesses
 * I am not well-positioned to comment on the significance of the results within this research area. However, it is not clear to me why we should be interested in this formal setting beyond the fact that some previous works have considered it. The assumptions seem highly contrived and no attempt is made to link them to any practical task in a meaningful way. Could the authors explain why progress in this research direction is worth pursuing? I would argue that if this work is being submitted to a broad conference such as ICLR, more effort should be made to broaden its appeal by explaining why its setting is relevant.

 * Given the very niche nature of this paper, I'm not sure that ICLR is the best venue for this work. Given that (I would imagine) this work would be of interest to quite a small subcommunity, would it not be more suitable to submit to a more specific venue rather than a generalist conference like ICLR? This is not to speak negatively about this work, but it seems that this topic is less generally relevant in its nature and may not be best suited to this large-scale style of conference. 

* Could the authors provide a definition of anisotropic input data? I don't think this was clearly defined. Does it exactly refer to the setting defined mathematically at the beginning of Sec 1.1?

* Why can the existing results for the regression setting not be directly applied in the binary classification setting by converting it to a regression problem?

### Questions
* Given the very niche nature of this paper, I'm not sure that ICLR is the best venue for this work. Given that (I would imagine) this work would be of interest to quite a small subcommunity, would it not be more suitable to submit to a more specific venue rather than a generalist conference like ICLR? This is not to speak negatively about this work, but it seems that this topic is less generally relevant in its nature and may not be best suited to this large-scale style of conference. 

* Could the authors provide a definition of anisotropic input data? I don't think this was clearly defined. Does it exactly refer to the setting defined mathematically at the beginning of Sec 1.1?

* Why can the existing results for the regression setting not be directly applied in the binary classification setting by converting it to a regression problem?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors address how gradient-based feature learning interacts with anistropic input data. They do this by studying the sparse parity problem where feature coordinates have varying magnitudes. To this end, they analyze the learning complexity of the mean-field Langevin dynamics, which describes the noisy gradient descent update on two-layer neural networks. They show one can use the anisotropy of the data to improve the statistical complexity (i.e. sample size) and computational complexity (i.e. network width) of the mean-field Langevin dynamics. This improvement is found when the main directions of the anisotropic input data aligns with the support of the target function. They also provide a method using coordinate transformations determined by the gradient covariance to show that the computational complexity can be improved by exploiting the anisotropy.

### Strengths
- The results seem novel and interesting. Namely they show how one can utilize the anisotropy of the input data to improve learning for a specific setting.
- The result of coordinate transformations which leverages anisotropy could be of interest for practical neural network training.
- The implication of a tradeoff between statistical and computational complexity also seems interesting. 
- The paper is clearly written and the results clearly stated.

### Weaknesses
 - In my opinion, the claim that "anisotropy helps" seems too strong, a bit specific to the problem in the paper, and not necessarily a general statement that can be made for neural networks based on the assumptions and results of the paper. It would be great if the authors could better motivate a connection between this problem and more general neural networks with real-world datasets. The current analysis focuses on a highly specific $k$-sparse parity problem, and it's unclear how the observed benefits of anisotropy would translate to more complex, real-world scenarios where data distributions and target functions are far less structured. For example, in image classification, the relevant features are often entangled and not aligned with simple coordinate axes, making it unclear if the same coordinate transformation would be beneficial.

- The authors state on page 2, under "Feature learning under structured data", that 

  > in certain regression settings with low-dimensional target, structured data with a spiked covariance structure can improve the performance of both kernel methods and optimized NNs (Ghorbani et al., 2020; Ba et al., 2023; Mousavi-Hosseini et al., 2023; Suzuki et al., 2023b). However, these regression analyses do not directly translate to the binary classification setting which the k-parity problem belongs to.

  This implies that the intuition "anisotropy helps" is perhaps already observed in the literature, which may weaken the impact of the paper. If the authors could expand on why the $k$-parity problem is worth studying separately, that would really help motivate things. The paper needs to better articulate the specific challenges and nuances of the $k$-parity problem that make it a valuable case study, distinct from the regression settings already explored in the literature. It's not immediately obvious why the insights gained from this specific problem would generalize to other classification tasks, especially given the differences in loss functions and optimization landscapes between regression and classification.

### Questions
- One page 7, under Corollary 1, the authors state: 
  > On the other hand, if the input covariance is anisotropic so that ... then the value of $R$ becomes dimension-free: $R = O(k^2 log(k)^2 )$."
  
  Can similar results apply to real-world datasets?

- How applicable is the coordinate transformation used in the paper, to conventional neural network training for real-world datasets?

- For equation (2), we're using a smooth activation function (tanh). Can the results apply for nonsmooth activation functions, namely ReLU networks? i.e. can the intuition "anisotropy helps" also apply for ReLU networks?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
