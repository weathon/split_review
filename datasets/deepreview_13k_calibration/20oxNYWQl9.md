# Sensitivity Sampling for Coreset-Based Data Selection

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Given the sustained growth in both training data and model 
parameters, the problem of finding the most useful training data 
has become of primary importance for training state-of-the-art and
next generation models. 

We work in the context of active learning and consider the problem 
of finding the best representative subset of a dataset to 
train a machine learning model. Assuming embedding representation of
the data (coming for example from either a pre-trained model or a 
generic all-purpose embedding) and that the model loss is Lipshitz
with respect to these embedding, we provide a new active learning
approach based on k-means clustering and sensitivity sampling.

We prove that our new approach allows to select a set of ``typical'' 
$k$ 
elements whose average loss corresponds to the average loss of the 
whole dataset, up to a multiplicative $(1\pm\epsilon)$ factor and an additive $\epsilon \lambda \Phi_k$, where $\Phi_k$ represents the $k$-means cost for the input data and $\lambda$ is the Lipshitz constant. 
Our approach is particularly efficient since it only
requires very few inferences from the model ($O(k + 1/\epsilon^2)$).
We furthermore demonstrate the performance of our approach on classic
datasets and show that it outperforms state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a data selection algorithm for ML models with a holder continuous loss, based on the idea of first doing a $(k,z)$ clustering of the points and then using the clustering to define sampling probabilities for the points. Sampling and reweighing the sampled points appropriately, gives you a subset which can approximate the loss over the full data with an additive error proportional to the clustering cost. The authors specifically show the theoretical guarantees of the algorithm for the case of linear regression. Finally, they perform experiments to validate their claims comparing their sampling technique with uniform sampling and $k$- center based technique for the case of neural networks and leverage scores for regression problem.

### Strengths
1. Data selection is an important problem and as such the paper will be of interest to the community.
2. The paper, for the most part, is well written and is easy to follow. 
3. Experiments for the Neural network seem good.

### Weaknesses
1. I do not feel the paper has enough novelty at all for a venue like ICLR. The idea seems a combination of the one by Sener (2018) and results from coreset literature with only minor or incremental modifications.
2. The paper title has sensitivity; however, the paper does not really use sensitivity as defined in literature. It appears to use a very crude approximation to sensitivity which is why there is an additive error. This idea also is very similar to the one of "light weight coresets".
3. The additive error can be pretty large I believe.
4. The proofs are pretty straight forward (not a bad thing in itself); however, it means even proof technique wise there is not much contribution. For e.g., the proof of theorem 6 is direct application of Bernstein and is well known. The proof for the 1-round algorithm is also very similar to existing proofs.
4. For regression, theoretical guarantees are much weaker than ones obtained using leverage scores. Empirically the authors claim they can match leverage score sampling in much less time. However, I could not find if they report the time for regression experiments.
5. There are small writing errors as well. For e.g.: what is $X$ in theorem 1,7? In Algorithm 2 $x_0$ is mentioned in step 2 and computed in step 3.
Overall, I think the authors need to clarify and highlight the contributions of the paper more and contrast them with existing results, especially in terms of novelty.

### Questions
Please try and address the points given as weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an application of sensitivity sampling to obtain coresets for clusterable data. Their method involves computing approximate k-means or k-median clusters over a dataset, and selecting data points based on a modified sensitivity sampling method, where each point is chosen with probability proportional to its distance from the centers and the loss associated with the center. Their results differ from previous methods because they study a class of losses more general than Lipschitz functions, but a subset of Holder continuous functions. 

Their main theoretical contribution lies in showing that with constant probability, the weighted loss on their proposed coreset closely approximates the loss on the entire dataset, with an additive error dependent on the cost of clustering the data.

They provide experiments where they compare their method to existing sampling techniques like uniform sampling, leverage score sampling, other clustering based methods for tasks like linear regression and training neural networks on datasets, including gas sensors and CIFAR.

### Strengths
Their contribution of applying the preprocessing step to obtain $(k,z)$ clustering is interesting since the samples are diverse and not sensitive to outliers. Moreover, their results extend to tasks beyond classification because of the loss being Holder continuous. Empirically, their method seems to perform similar to existing methods for linear regression and neural network based tasks in the low sample regime.

### Weaknesses
 * For the case of linear regression, it is not clear how the proposed method is theoretically better (in terms of number of samples or runtime) than existing works using sensitivity sampling including Chen and Price, Chen and Derezinski, etc. Moreover there are additional assumptions on the data as opposed to distributional assumptions which is not stated clearly. It would be good to have a detailed explanation for the assumption 10 that requires for any $i,j$ $| b_i - b_j | \le ||a_i - a_j||_2$. Specifically, how does this assumption compare to those made in prior work, and what are its implications for the applicability of the method? A quantitative comparison of the sample complexity and runtime with these methods, under comparable assumptions, would strengthen the paper.

* It seems that their primary theoretical contribution revolves around the use of Holder-continuous loss functions; however, their experiments do not seem to leverage this property. The experiments primarily focus on standard loss functions like squared loss for linear regression and cross-entropy for neural networks. It would be beneficial to include experiments that specifically highlight the advantages of using Holder-continuous loss functions, perhaps by considering less common loss functions that satisfy this property but are not Lipschitz continuous. This would provide a more convincing demonstration of the theoretical contribution.

* This paper as a whole is not reader friendly and requires significant time commitment because of imprecise definitions, lack of explanations and inconsistent terminology. For example, Algorithms 1 and 2 are never referred. The definition of $\mathcal{A}$ from the first lines of both algorithms is not properly stated and it is also overloaded $\mathcal{A}(e)$. Is it defined as $\mathcal{A}(\mathcal{D}) := \min_{|C| = k} C' \cdot \Phi_z(\mathcal{D},C)$ for some constant $C'$? In the clustering objective $C$ is not defined correctly where $|C| = k$ and $C \subset \mathbb{R}^d$. There is also inconsistency in using norms, somewhere $||\cdot||$ or $||\cdot||_2$ is used. $\Delta$ is mentioned in section 3.1 without definition. Overall I recommend a better use of space for defining variables as opposed to other sections like stating Berstein's inequality. A thorough revision of the notation and definitions is necessary to improve the clarity and readability of the paper.

### Questions
* For the case of linear regression, it is not clear how the proposed method is theoretically better (in terms of number of samples or runtime) than existing works using sensitivity sampling including Chen and Price, Chen and Derezinski, etc. Moreover there are additional assumptions on the data as opposed to distributional assumptions which is not stated clearly. It would be good to have a detailed explanation for the assumption 10 that requires for any $i,j$ $| b_i - b_j | \le ||a_i - a_j||_2$. 

* It seems that their primary theoretical contribution revolves around the use of Holder-continuous loss functions; however, their experiments do not seem to leverage this property.

* This paper as a whole is not reader friendly and requires significant time commitment because of imprecise definitions, lack of explanations and inconsistent terminology. For example, Algorithms 1 and 2 are never referred. The definition of $\mathcal{A}$ from the first lines of both algorithms is not properly stated and it is also overloaded $\mathcal{A}(e)$. Is it defined as $\mathcal{A}(\mathcal{D}) := \min_{|C| = k} C' \cdot \Phi_z(\mathcal{D},C)$ for some constant $C'$? In the clustering objective $C$ is not defined correctly where $|C| = k$ and $C \subset \mathbb{R}^d$. There is also inconsistency in using norms, somewhere $||\cdot||$ or $||\cdot||_2$ is used. $\Delta$ is mentioned in section 3.1 without definition. Overall I recommend a better use of space for defining variables as opposed to other sections like stating Berstein's inequality. 

 Given these questions, their overall contribution appears reasonable in terms of the empirical study of their proposed algorithm, but the theoretical contribution is lacking.

### Soundness
2 fair

### Presentation
1 poor

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
This paper provides a coreset-based data selection algorithm that relies on clustering, specifically the $(k,z)$-clustering.

### Strengths
In what follows, I will present the strengths of the techniques proposed in the paper:
  * The idea of using $(k,z)$-clustering is interesting, as it is a better candidate than $k$-center for small $z$, in terms of robustness against outliers.
  * The proofs given in the paper are elegantly written, and easy to follow.
  * Connecting the use of H$\ddot{o}$lder Continuity to coresets specifically through the $(k,z)$-clustering problem is innovative. 
  * The proposed coreset is small in size which is an advantage, however, with such a small size, an additive approximation term is guaranteed by the coreset in addition to the usual multiplicative factor approximation that most coresets admit.

### Weaknesses
While the paper has quite an impressive set of strengths, the paper suffers from the following weaknesses:
   * The writing could use some polishing.
   * The experimental section lacks more information, to better understand what each experiment aims to show -- specifically in the realm of neural networks.
   * Assumption 10 in the field of linear regression seems too restricting. Specifically, the assumption that the absolute value of the difference between the regression targets of a data point and its nearest neighbor, divided by the distance between their feature vectors, is bounded by a constant seems quite strong. This implies a global Lipschitz-like condition on the target function, which may not hold in many practical scenarios, especially when the data distribution is complex or high-dimensional. The assumption also restricts the kind of noise that can be present in the data.
   * See my questions below.

### Questions
Please address each of the following questions:

* Page 3 -- It is stated that "Therefore, our upper-bound is less robust to outliers"
Should your choice of $(k,z)$-clustering make your bounds more robust against outliers as $z$ get smaller? since as $z$ increases, the behavior of the $(k,z)$-clustering tends to behave more like $k$-center problem.

* Page 4 -- Change "there exists a real-valued constant" to "there exist real-valued constants"

* Page 9 -- It is stated "We round them to the closest data point from the dataset in $\ell_2$ norm": This implies that the centers in practice at least are replaced by the data points from the original data such that their embedding are the closest to the centers in the embedding space. right?

* How do you ensure that your version of H$\ddot{o}$lder Continuity holds in the neural network regime?

* Assumption 10 seems too restricting. Can you elaborate on this?

* Can you put time graphs concerning Figure 1 to further highlight the speed gain one would enjoy when using your approach as opposed to using the leverage score sampling technique?

* In the neural network experiments:
  * How many epochs were used to train the uniformly sampled points of size $k^\prime$?
  * Can you put the runtime for uniform sampling coreset in Figure 2 (a) for better comparison?
  * In Figure 4, it was stated "independently run each data point 100 times", did you mean you ran the experiment 100 times with different sampled sets? If not, then please elaborate.
   * Also concerning Figure 4, can you put the running times to highlight the advantages of your approach better -- while margin is the best, it does require the most time (due to the inference payload it has to pay).

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new data selection approach under the Holder continuity assumption. The proposed approach can find a 1/a^2-size coreset with k query to the model, with (1+a) multiplicative error and an additive term. Compared with other approaches, the approach is query efficient because it only needs k inferences from the model. Several experiments are performed to verify the validity of the approach.

### Strengths
This paper propose a simple yet query efficient approach. The proof is clear and easy to follow. The proposed approach performs better on several datasets, compared with some previous works.

### Weaknesses
1. The Holder continuity assumption lacks empirical support. Does the dataset really satisfy the assumption? It would be better to perform experiments to verify it. Furthermore, the assumption is made on the sample space, but it should be on the embedding space. This discrepancy needs to be addressed, as the current formulation does not align with the typical use of embeddings in machine learning.
2. The paper lacks comparison with previous works, both theoretically and empirically. 
    
   Theoretically, the proposed method can find a 1/a^2-size coreset with k query to the model, with (1+a) multiplicative error and an additive term, under the Holder continuity assumption. What are the assumptions in previous works? How large is the coreset in previous works? How many are the queries of previous works? I can't find explicit comparisons. It would be better to add a table to list them. Specifically, the paper should compare the theoretical guarantees (coreset size, error bounds, query complexity) with other coreset construction methods. It's not clear how the proposed method's guarantees compare to existing state-of-the-art approaches.
    
   Empirically, there is only one compared method [1], which is published in 2018. It seems there are several methods for coreset after 2018, as listed in the related work. But there is no comparison with them. The experimental section should include a broader range of baselines, especially more recent methods, to demonstrate the advantage of the proposed method.
3. It seems there are some errors in the proof and algorithm. 
    
   a. By using Holder continuity of $l$, you obtain that $l(e)\leq \hat{l}(e)+\lambda v(e)$, where $v(e)$ is defined as $||e-A(e)||^z$. It seems $e$ and $A(e)$ belong to the sample space. But the Holder continuity needs that $e$ and $A(e)$ belong to the embedding space. To satisfy the Holder continuity, $v(e)$ should be $||v_e-v_{A(e)}||^z$, where $v_x$ stands for the embedding of $x$. There should be some modifications in proof and algorithm. The current formulation of the Holder continuity is not aligned with the use of embeddings, which are crucial for the method.
    
   b. It seems that the expectation of $X_i$ (defined in Appendix B.2) is $\sum l(e)w(e)p(e)=\sum l(e)/s$. Therefore, by using Bernstein’s inequality, $|\sum l(e)/s-\sum w(e)l(e)|$ is bounded, rather than $|\sum l(e)-\sum w(e)l(e)|$. The Bernstein inequality application needs to be carefully reviewed and corrected to ensure the proof is valid.
4. There is an extra time cost to obtain the embedding for each sample, which may take about the same amount of time as inference.  Although query efficient, the total time cost may be similar with previous works. The paper should provide a more detailed analysis of the computational cost, including the time spent on embedding computations, and compare it with the overall time cost of other methods. This is crucial for evaluating the practical efficiency of the proposed approach.

### Questions
1. Is Holder continuity a general assumption? Does Holder continuity hold in real datasets?
2. Is [1] the state-of-the-art method? Why not compare with other methods which listed in the related works?
3. How much is the time cost to obtain the embedding of the sample? Does previous work need to obtain the embeddings?

[1] Ozan Sener and Silvio Savarese. Active learning for convolutional neural networks: A core-set approach.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
