# Amortized SHAP values via sparse Fourier function approximation

- Decision: Reject
- Scores: 6, 3, 5, 8, 6

## Abstract
SHAP values -- a.k.a.~SHapley Additive exPlanations -- are a popular local feature-attribution method widely used in interpretable and explainable AI. We tackle the problem of efficiently computing these values. We cover both the model-agnostic (black-box) setting, where one only has query access to the model and also the case of (ensembles of) trees where one has access to the structure of the tree.  For both the black-box and the tree setting we propose a two-stage approach for estimating SHAP values. 

Our algorithm's first step harnesses recent results showing that many real-world predictors have a spectral bias that allows us to either {\em exactly represent} (in the case of ensembles of decision trees), or {\em efficiently approximate} them (in the case of neural networks) using a compact Fourier representation. 
For the case of trees, given access to the tree structure, one can extract the Fourier representation using a simple recursive algorithm.
For the black-box setting, given query access to the black-box function, we utilize a sparse Fourier approximation algorithm to efficiently extract its compact Fourier approximation. 

In the second step of the algorithm, we use the Fourier representation to {\em exactly} compute SHAP values. The second step is computationally very cheap because firstly, the representation is compact and secondly, we prove that there exists a closed-form expression for SHAP values for the Fourier basis functions. Furthermore, the expression we derive effectively ``linearizes'' the computation into a simple summation and is amenable to parallelization on multiple cores or a GPU. Since the function approximation (first step) is only done once, it allows us to produce Shapley values in an {\em amortized} way. We show speedups compared to relevant baseline methods equal levels of accuracy for both the tree and black-box settings. Moreover, this approach introduces a reliable and fine-grained continuous trade-off between computation and accuracy through the sparsity of the Fourier approximation, a feature previously unavailable in all black-box methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper provides a principled approach for estimating Shapley (SHAP) values in the context of explainable machine learning. A closed-form expression for exact computation of the SHAP values in terms of the Fourier representation of the predictor function is obtained, which is used to obtain a tractable algorithm (polynomial asymptotic computational complexity) for estimating the SHAP values. Extensive experiments show that the proposed methods beats several recently proposed approaches for SHAP estimation in terms of the accuracy-efficiency trade-off.

### Strengths
- The paper is well-organized and easy to read with sufficient background on techniques used and prior methods.
- A new principled approach for estimating SHAP values is proposed based on a sparse Fourier representation of the prediction function
- The closed form expression in terms of the Fourier representation allows the approach to perform well with better Fourier approximation or when the sparsity assumption holds.
- Extensive experiments show benefit of using the proposed approach over previous methods in the literature.
- The approach can be parallelized making it potentially even faster in practice.

### Weaknesses
- It is not clear how the SHAP estimate degrades with the approximation error in sparse Fourier approximation. 
- The initial step for Fourier approximation can be computationally expensive.

### Questions
- Past work has shown several optimizations are possible for Kernel SHAP making it faster. Are they applicable to your approach?

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
4

### Summary
The paper proposes FourierSHAP as a novel way to amortize Shapley value (SV) computation for XAI use cases. Therein, the work sits between traditional approximation methods such as KernelSHAP or Permutation Sampling and model-based amortized methods such as FastSHAP. In a way, FourierSHAP can be compared to model-specific methods like TreeSHAP or RKHS-SHAP. FourierSHAP transforms the black-box model to be explained into a fourier representation. Then, based on interesting and novel theoretical results, FourierSHAP computes SVs for the transformed model efficient. 

## References for this Review
- [1] RKHS-SHAP: https://openreview.net/pdf?id=gnc2VJHXmsG
- [2] GP-SHAP: https://openreview.net/forum?id=LAGxc2ybuH
- [3] Linear TreeSHAP: https://openreview.net/forum?id=OzbkiUo24g
- [4] Interventional TreeSHAP: https://ojs.aaai.org/index.php/AAAI/article/view/26322
- [5] TreeSHAP: https://www.nature.com/articles/s42256-019-0138-9

### Strengths
- **Novel Theoretical Results:** Theorem 2 and Lemma 1 are (to the best of my knowledge, though I did not check [1,2] in detail) novel and very interesting results. This result can be useful for different kernel-based model classes and like the authors demonstrate even to create high-fidelity surrogate representations of black box function. This is a good contribution.

- **Potentially Good Surrogate**: From Figure 1 and the theory of the paper, it seems like the Fourier representation of the tree models seems to be a good surrogate model for approximating tree structures (high $R^2$ in Figure 1). I think this is a nice experiment and insight whcih begs the question if this holds for even more complicated black box models and functions.

### Weaknesses
While the paper proposes interesting theoretical results strengthening the body of research concerned with efficient computation of Shapley value based explanations, it ultimately falls short to present a convincing picture of their method FourierSHAP. This problem arises from the fact that the work evaluates FourierSHAP in a very limited way missing key baseline comparisons, which would help researches better understand the strengths and weaknesses of FourierSHAP. The method itself has inherent restrictions that are not well explored or discussed: 

- **Restrictive Application Settings:** _First_, FourierSHAP can only applied when input spaces are binary. This means numerical features cannot be represented. This is a big limitation of the method, which obvious competitors like [1-4] do not have, which reduces the applicability of FourierSHAP in settings with numerical data. I am sure workarounds and fixes exist (binning and binarization), however this is left unexplored by the paper. _Second_, FourierSHAP seems to work only with very shallow neural networks (i.e. 3 layers with 300 neurons), which definitely is not realistic given modern architecture sizes. Usually, for XAI use cases testing with smaller networks is ok for model-agnostic methods, as the focus lies in showing that such methods can work with all sorts of models. However, given that FourierSHAP relies on finding a sparse Fourier representation of the underlying model, the aforementioned argument is invalid. This Fourier representation will most definitely be drastically different from smaller sized networks. This needs to be theoretically or at least empirically explored. Otherwise, I am doubtful the results generalize to large scale networks.

- **Lacking Empirical Evaluation**: While FourierSHAP can be seen as a model-agnostic method for computing SVs, the experimental section and focus of the paper lies with **tree ensembles** and **very small neural networks**. Also strong focus of the paper is to show how SV computation can be amortized, i.e. made more efficient. Therein, the paper **needs to compare itself with better baselines**. These baselines include _TreeSHAP_ [5] which was made even more efficient with _Linear TreeSHAP_ [3] and extended to also account for _interventional SVs_ in [4]. As the core concept of the method is a kernel representation of the underlying model to be explained, a comparison to kernel based SV computation methods is important as well. This would include works like _GP-SHAP_ [2] or _RKHS-SHAP_ [1]. I really don't think DeepLIFT or potentially even FastSHAP is the right baseline to compare against here. Lastly, computing ground-truth SVs with an approximation based method like KernelSHAP is an okay proxy, but in smaller feature settings like the _Entacmea_ (13 features) dataset used in this paper or potentially synthetic settings, real ground truth values can be obtained through brute force or clever tricks with knowledge about the underlying data generating process / black box function.

- **Missing Limitations Section**: The paper does not contain a limitation section discussing FourierSHAP's drawbacks and avenues for interesting future work.

- **Poor Related Work**: While the paper does include a related work section in the appendix, key works [1-4] are missing and not delineated from. Given the above mentioned critique with the evaluation, this is problematic.

- **Presentation can be Refined**: The papers could be presented better. The work is more verbose than it needs to be. This starts in the abstract which is overly detailed and too long. The paper looses itself in discussing aspects that are in my opinion secondary and can be postponed to the appendix, like the parallelization and GPU acceleration. The paper contains multiple typos.

### Questions
- How does the Figure 1 look if the underlying model is a large neural network that potentially operates on text (text is also binary)?
- How is FourierSHAP different from [1] and [2]?

### Soundness
2

### Presentation
1

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
The paper presents a novel method, FourierSHAP, that amortizes the computations of SHAP values. FourierSHAP can be employed to explain tree-based models or black-box neural network models. The proposed method is composed of two phases. The first phase, which is the most computationally expensive, extracts a compact Fourier representation approximation using a sparse Fourier approximation
algorithm. In the second phase, the SHAP values are computed using a closed-form expression that avoids the exponential summation operation over all possible coalitions of features. The proposed method showed an order of magnitude improvement in running time over the baseline method, KernelSHAP.

### Strengths
1- The approach presented in the paper to compute the SHAP values is novel and theoretically grounded. 

2- The paper is mostly clear and understandable, although the description of Fourier representations can be further clarified.

3- The discussed problem, i.e., reducing the computational cost of SHAP values to explain black-box models, is important.

4- The presented solution provides a new perspective to compute the SHAP values, which can benefit the explainable machine learning community.

### Weaknesses
1- The proposed method is limited to binary features or categorical data that can be presented using one-hot encoding.

2- FourierSHAP is not a model-agnostic explanation method, e.g., KernelSHAP, i.e., does not explain any black-box model but is limited to either tree-based models or neural networks (or any sparse and low-degree functions).

3- The experiments are limited, including only four datasets.

4- The metric used to evaluate the accuracy of the SHAP approximations does not adequately capture how closely the approximated values align with the ground truth, nor does it assess the agreement in feature ranking based on their relative importance.

### Questions
1- Line 105 says, ``This was not formerly possible with these two black box methods." 
which two black-box methods is the line referring to?

2- In the experiments, why were not all the algorithms trained and explained on all the datasets for evaluation?

3- In the evaluation of the SHAP value accuracy, why just 4 query points were selected to be explained?

4- As I understand it, all the evaluation datasets are for regression problems. Is FourierSHAP applicable to classification problems as well?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper considers the problem of computing the SHAP values of machine learning models, which is essentially the significance of each feature.

This problem is well-motivated, has a significant amount of work, and even has a legal interest.

The direction is rather interesting and seems novel as well.

### Strengths
Extensive experimental results, that include various models.

The problem is very well-motivated, as stated in the introduction Section.

The paper is fully contained since I have understood the main parts of the paper without significant prior knowledge on the subject.

The direction seems rather novel and interesting.
That is, provide an exact bound on the SHAP value of *Fourier representation*, which can approximate (or even give exact representation) many models, and in turn yields an approximation to the SHAP value or an exact value.

### Weaknesses
The theoretical results are on the simpler side, specifically the proofs span around 2.5 pages and seem to be on the simpler side.
While there is absolutely no need to overcomplicate the proofs and short proofs have merit, I believe that it should be noted.

The writing seems to require some improvement.
Specifically, I felt that the abstract, introduction, and background were on the cumbersome side and should be shortened.
As a consequence, the introduction only "moved me over the fence" on the significance of the problem and did not truly excite me.
It also seemed to me that the abstract is rather long and is somewhat repeated in the introduction.

Additional writing suggestions are included in the questions section.

### Questions
The paper answered the suggested problem and I have no significant questions.
Nonetheless, regarding the approximation of neural networks, I am intrigued by the exact values (as a function of the approximation) of the representation for common networks (say AlexNet).
It seems that this is an active research area in itself, thus perhaps there are yet exact values for such networks.
If there are such results consider including them since it could give a good picture of the complexity of approximating (with theoretical guarantees) the SHAP value via the proposed method.

Regarding the writing, I suggest the following changes:

* Consider rewriting the abstract, introduction, and background to be more concise since I found it to be on the cumbersome side.

* When mentioning the "exponential sum" in the second paragraph of page two consider giving a reference to the full expression on page 3.
I am unsure if this is due to me being unfamiliar with the matter, but noting the sum over the exponential number of combinations simply as "exponential sum" rather confused me initially.

* The first line of Section 2.2 seems to require rewriting.

* I would prefer the machine properties in the experimental section, and for you to include more details such as CPU and RAM.

## In the proof of Lemma 1:

* Consider Changing "One can see by checking for different values" to something along the lines of "By checking all the possible 8 values" since it is needed to check for all the values, and the current writing seems to unnecessarily suggest corner cutting to the reader.

* I believe that both Equations i and ii should be proven before use in Equation 8.
This would make the proof more organized.

* Fully prove Equation i and not leave it to the reader, especially since the cancelations can be demonstrated rather effectively.

* While Equation ii is correct, and I liked that it was a combinatorial proof, the writing is rather confusing, consider rewriting it.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a fast approximation for SHAP values using sparse fourier analysis for pseudoboolean functions. It leverages the evidence that neural networks have a spectral bias that can allow the blackbox function learned by NNs to be represented by a sparse fourier approximation to derive a formula for calculating exact SHAP values that does not have a exponential sum term. For datasets considered they show orders of magnitude improvement in calculating shap values relevant to baseline methods while achieving the same accuracy (where accuracy is measured by how close the SHAP values are to values predicted by kernelSHAP).

### Strengths
Overall the paper is well written and covers the relevant literature well. The problem being tackled is a significant problem and speedups in calculating accurate SHAP values can be an extremely useful tool. The empirical results are convincing for the subset of problems being considered and there seems to be no problems with the theoretical underpinnings either.

### Weaknesses
My biggest concern with this submission is that the fact that it's only applicable to pseudoboolean functions is far too restrictive. I don't think that limitation can be overcome simply by "discretizing continuous features into quantiles" to transform them into categorical features. Post-hoc explanations like SHAP values are largely a useful area of research because they enable interpretation of real-world deployments of machine learning methods. I have trouble thinking of how many real-world problems out there can be easily tackled with boolean inputs. What are the main challenges towards extending this work to continuous valued problems? is it possible at all? at the very least a discussion is warranted. I'm afraid without that this paper, while theoretically neat would just end up without a significant impact.

In summary, the paper is lacking: a) Concrete examples of real-world problems where the boolean limitation is and isn't problematic. b) Discussion of potential challenges and ways of extending this method to continuous-valued cases. c) impact of discretization on model and SHAP performance when applied to otherwise continuous-valued datasets.

### Questions
My first question is described in the Weakness section and I'd love to hear more from the authors on that limiation. 

Q2: One of the arguments for the assumption that NNs can be sufficiently approximated through a sparse fourier transform is presented in lines 242 to 247. From my reading of Yang and Salman it doesn't seem like they are saying that the *weak* spectral bias present in NNs is sufficient enough for the "this sample, roughly speaking, looks like a lienar combination of eigenvectors with the largest eigenvalues" line to hold true. As you point out in the footnote the spectral bias is separated out into even and odd frequencies, not higher degree and lower degree frequencies. How well are the sparse approximations in general can be relied upon to actually approximate the NNs beyond the simple cases discussed in the experiments? This also has a direct bearing on how exact the claimed "exact SHAP values" are. Consequently also, in my opinion, line 264 at best should say The aforementioned literature *suggests*, rather than "shows".

Q3: How accurate are the SHAP values? the results are relative to kernelSHAP but it might be worth setting up results on simulated data to see how well can you get at actual ground truth SHAP values.

Q4: This relates to the discretization of the data, I'm assuming there's discretization going on in some of these datasets that you included results for. How does that impact model performance? Just to get a sense of whether the underlying model itself was useful or not.

there are a few typos in the paper: please check lines 32, 33, 139, 177, 230, 231

### Soundness
3

### Presentation
3

### Contribution
2
