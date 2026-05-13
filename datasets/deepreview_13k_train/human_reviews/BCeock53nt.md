# Kolmogorov-Arnold Transformer

- Decision: Accept
- Scores: 6, 8, 8, 6, 6

## Abstract
Transformers stand as the cornerstone of mordern deep learning. Traditionally, these models rely on multi-layer
perceptron (MLP) layers to mix the information between channels. In this paper, we introduce the Kolmogorov–Arnold
Transformer (KAT), a novel architecture that replaces MLP layers with Kolmogorov-Arnold Network (KAN) layers to
enhance the expressiveness and performance of the model. Integrating KANs into transformers, however, is no easy
feat, especially when scaled up. Specifically, we identify three key challenges: (C1) Base function. The standard B-spline
function used in KANs is not optimized for parallel computing on modern hardware, resulting in slower inference speeds.
(C2) Parameter and Computation Inefficiency. KAN requires a unique function for each input-output pair, making the
computation extremely large. (C3) Weight initialization. The initialization of weights in KANs is particularly challenging
due to their learnable activation functions, which are critical for achieving convergence in deep neural networks. To
overcome the aforementioned challenges, we propose three key solutions: (S1) Rational basis. We replace B-spline functions
with rational functions to improve compatibility with modern GPUs. By implementing this in CUDA, we achieve faster
computations. (S2) Group KAN. We share the activation weights through a group of neurons, to reduce the computational
load without sacrificing performance. (S3) Variance-preserving initialization. We carefully initialize the activation weights
to make sure that the activation variance is maintained across layers. With these designs, KAT scales effectively and readily
outperforms traditional MLP-based transformers. We demonstrate the advantages of KAT across various tasks, including
image recognition, object detection, and semantic segmentation. It consistently enhances performance over the standard
transformer architectures of different model sizes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
There has been a resurgence in Kolmogorov Arnold Networks (KANs) recently as an effective alternative to MLPs. This work carefully studies the major issues with scaling of the standard KAN architecture and proposes suitable modifications to create what they define as Group-Rational KAN (GR-KAN). The GR-KAN is then used as a replacement for the MLP layer in the transformer architecture in this work, which is then called the Kolmogoorv Arnold Transformer (KAT). The utility of the KAT architecture is demonstrated through experiments on various vision tasks such as Image Recognition, Object Detection, Instance Segmentation and Semantic Segmentation.

### Strengths
S1) Existing works using KANs in-place of MLP modules in various models (such as feedforward NNs, CNNs, Transformers etc) have had limited success due to various issues. This work goes a step further and proposes an alternative to the original KAN architecture called Group Rational (GR-KAN) solving the issues for inefficiencies in base functions, parametrizations and base initializations reducing the parameters and FLOPs from the original KAN architecture.

S2) The GR-KAN employs rational activations as the base function which are efficient and suitable for GPU computation replacing the B-Splines which are not optimized for GPU or parallel processing. (which is one of the core strengths of this work amongst related KAN literature)

S3) The KAT architecture improves the performance over standard transformer architectures such as ViT within the same computational budget.

### Weaknesses
W1) This work doesn’t include results on using KANs in solving PDEs (as the original work did, albeit the architecture won’t be transformers for this task) and KATs for language processing (mentioned in future work). The experiments are majorly limited to vision tasks. (Table and Graph Classification results have also been included.) It is unclear how the proposed GR-KAN would perform in tasks beyond vision, especially given that the original KAN paper demonstrated strong results on PDE solving. The lack of results in these areas limits the generalizability of the claims made about the superiority of GR-KAN over the original KAN architecture.

W2) Ablations on the function which parametrizes the learnable activation are not included. Ablations are mainly with respect to alternative MLPs and fixed activation functions. Ablations could have included alternatives to rational functions, B-splines etc. The choice of rational functions as the base activation is a key contribution, yet the paper does not sufficiently explore the impact of this choice. Without ablations on different base functions, it's difficult to ascertain whether the performance gains are solely due to the rational activation or other architectural changes. Furthermore, the paper does not investigate the impact of the degree of the rational function, which could significantly affect the model's capacity and performance.

**Presentation/Typos/Corrections**

I believe that the *Experiments* section can be shortened or moved to appendix and the *Appendix F Discussion and Future Work* be moved to the main paper as it packs a lot of relevant quality content.

*Appendix D Section D.1*
This is a minor correction, the number of multiplications in exponent will be $\frac{m(m-1)}{2}$ and correspondingly $\frac{n(n-1)}{2}$ instead of $\frac{m(m+1)}{2}$ and $\frac{n(n+1)}{2}$ respectively. 
As an example case for $m=1$, the numerator becomes $a_0 + a_1x$ which involves 0 multiplications in the exponent computation and a single multiplication from the multiplication for the coefficients.
The total multiplications will be in fact $\frac{m(m+1)}{2}$ which is $\frac{m(m-1)}{2}+m$
Note that with this change the values in the Table 1 and the appendix D will change accordingly.

### Questions
Q1) As per my understanding, Kolmogorov Arnold Representation Theorem and the setup mentioned here involves learning a multivariate function, why do *lines 146-147* in the *section 2.2* mention *learn a univariate functions on the edge*. The dimension of $f(x)$ would be 
$d_{out}$ making it multivariate?

Q2) Do we have a theoretical understanding of the behaviour outlined in lines *316-317*? How are the parameters adjusted in case of B-splines or any other type of functions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper introduces the Kolmogorov–Arnold Transformer (KAT), where they replaces MLP layers in transformer with Kolmogorov-Arnold Network (KAN) layers. B-spline functions in KANs were replaced with rational functions to improve compatibility with modern GPUs. Group KAN was used to reduce computations and variance preserving initialization was employed. Introduces Group-rational KANs for intergation into ViT. Extensive experiments on image classsification has shown improved performance of GR-KAN.

### Strengths
Indentified issues with integrating KANs with ViT.
Overcame the recursive computation requirement for using B spline curves in KANs and replaced them with faster rational functions.
Introduced variance preserving initialisation to stabilize training.
Created an efficient an fast CUDA implementation of rational function for faster running in GPU
Improved performance gains by grouping and sharing parameters
Extensive experimetation is provided

### Weaknesses
Replacing MLP in transformers with KAN is an obvious choice and does not warrant any novelty.
phi_in matrix in eq. 2  Top row right element should show phi_1,d instead of phi_1,n
In line 46, the paper says KANs require fewer parameters than MLPs, then goes on to show in Line 176-189 than KAN requires more paramters.
The violation of variance-preserving nature in higher order B-splines is not clear.
The basic novelty is the use of rational function instead of B-splines

### Questions
How do you explain the contradiction of saying KANs require less paramters and then saying KAN requires more parameters?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents the Komlogorov-Arnold Transformer, a transformer architecture that replaces the typical transformer layer's concluding 2-layer MLP with (modified) Kolmorogov-Arnold layers. The authors explain why a simple substitution of KAN layers will fail to both perform well and to scale with the hidden dimension of the network, and provide fixes (via different base functions, weight sharing across grouped edges, and improved initialization) that improve performance and speed. Improvements are shown in experiments across a variety of machine learning tasks in vision domains and beyond.

### Strengths
1) The paper is generally well written: it has a clear narrative, each new section is well-motivated, and for the most part, technical discussions are nicely balanced with takeaways and intuition.
2) The technical analysis and contributions of the paper directly lead to practical improvements. The entire chain of derivations/modifications creatively connect different lines of research (KAN networks + rational neural networks, for example) and add some new techniques as well. In particular, I found the re-expression of the grouped parameters in Section 4.3 into a specialized MLP to be quite elegant.
3) The experiments are comprehensive, all of the important training details are made available, and the results show that using these layers does lead to improvement in accuracy with relatively little increase in training time.

### Weaknesses
1) I felt some details about the method and novelty were missing. In my opinion this is mostly clearly true in the initialization section (which seems to be where a lot of the improvements/convergence come from). A lot of Section 4.4 is spent showing that choosing these initialization values is difficult and non-obvious - which I agree with! - but then there is no space left to actually show how you pick values for a and b (I know you say that you "determine a and b such that F fits established activations", but a small algorithm or set of equations would do a lot to disambiguate this). The description lacks the necessary detail for reproducibility; specifically, how the parameters of the rational functions are fit to approximate the target activation functions is not sufficiently explained. It is unclear what optimization algorithm is used, what the loss function is, or how the sample points are chosen to fit the rational functions to the activation functions. This makes it difficult to understand and replicate the initialization procedure.

2) The suite of experimental results is impressive, but there are comparatively few ablations studies. I am left wondering which parts of your method are responsible for the improvement over standard ViTs. This is particularly disappointing because you clearly break down your improvements step-by-step, so it is easy to imagine what such an ablation would look like. I realize that some of your modifications are meant to address scalability, so a large set of experiments might be infeasible. But something like accuracy & total training time of a ViT-T with different parts of your method (i.e., with/without your initialization scheme, with/without grouping, etc) seems like it should be possible. Without these ablations, the reader is left to guess which components are most critical, and it is hard to assess the true value of each contribution.

3) Similarly to the above: after switching the base functions to rationals, the GR-KAN layer in practice resembles the rational layers from Boulle et al much more than it resembles the original KAN layers. But there are no direct comparisons to those; I would also find this experiment useful. The paper should include a direct comparison to the rational activation units used in Boulle et al., as the proposed method shares significant similarities with their approach, especially after the base function change. Without this comparison, it is difficult to assess the true novelty and performance advantages of the proposed method over existing rational activation techniques.

More minor pieces of feedback:

4) On L248: I don't think it's quite right to say that this gradient computation is "Similar to Monila et al"; it is identical to their calculation. I also don't think the details of this calculation are used anywhere later in the paper, unless I am mistaken, so they could also be relegated to the appendix.
5) Table 1: This caption could use more detail - is this just the forward pass, or forward and backward passes? Also, a comparison to an analogously-sized MLP layer would be additionally useful.
6) L433: "ViT-L + KAN fails to converge" - I think this should be ViT-B?
7) Figure 3: I think I understand what this figure is trying to communicate (i.e., that the choice of values for $a$ and $b$ do a good job of fitting the activation functions), but in practice it just ends up looking like... graphs of activation functions. Something quantitative would probably be more effective is communicating how well the rationals approximate the activation functions, and it would take up less space as well.

### Questions
1) Can you explain very specifically the novelty of your method? You break your contribution into three pieces, can you say which portions of these are novel and which are not?
2) Much of the presentation about scalability is presented through FLOPs computation. Is there a reason that you chose this representation, rather than actual training/inference time?
3) A major part of this work is the CUDA implementation of the layer. How do you plan to make this available? Will the layer also be eventually made available through frameworks like pytorch or jax? I appreciate the work that goes into a direct CUDA implementation, but I think it is crucial that there are plans for wide availability in popular frameworks in order to have this work translate to impact in the community.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, authors propose Kolgomorov-Arnold Transformer (KAT) as an improvement to standard transformer architecture, which uses MLP networks, by replacing MLPs with KAN networks. Authors propose a number of improvement over vanilla KAN architectures to make them scalable in practical settings and achieve better results: 1.) they swap b-spline functions with rational function for speed 2.) they make use of parameters sharing (grouping) 3.) they employ a variance preserving initialization.
Results show that KAT achieves better results than ViT on certain benchmarks.

### Strengths
- The topic is highly relevant, as literature has not focused much on improving the MLP aspect of transformers
- KANs have emerged as an interesting alternative to MLPs, however, they present issues (e.g. scaling) which make them unfavorable w.r.t. MLPs
- The proposed approach is scalable, faster, and requires less parameters than KANs, making it usable in practical settings and on large-scale datasets such as ImageNet-1k or MSCOCO
- The experimental evaluation comprises different tasks such as classification, object detection and segmentation.

### Weaknesses
Here are my doubts about this work: 
- While the results for ImageNet are convincing, the proposed KAT still lags behind traditional architectures such as ConvNext or even transformers such as SwinB in segmentation. 
- A proper ablation study is missing (e.g. combinations of KAN + rational function + grouping + initialization). It is difficult to evaluate the contribution of each proposed change quantitatively. Also I wonder how simple KAN perform with parameter grouping in terms of MACS/FLOPS and results? 
- It is not clear how you choose the hyperparameters for KAT such as number of groups and maximum order of rational function (m)
- (More of a philosophical doubt) KAN are based on the Kolmogorov-Arnold representation theorem, which states that a multivariate function can be approximated by a composition of univariate functions, while your proposed method only uses one irrational function. Can you still say it's based on the Kolmogorov-Arnold theorem? 
- (minor) some typos and missing notation are present in the paper (see questions below)

### Questions
- In Eq. 5, 6, and 7 what are MSA and LN? 
- Missing text in paragraph name in line 485 
- In Tab. 4 KATDet-S is reported as best (41.5) but ConvNext and SwinT are higher (41.7 and 41.6)
- I feel like the change you propose can be applied to KANs also outside of the transformer architecture. Perhaps it could be useful to add a comparison between KANs and GR-KANs on toy problems

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The author proposes and implements Kolmogorov-Arnold Transformer (KAN) architecture. Especially, they propose rational activation functions, group KAN, and variance-preserving initialization, demonstrating improved performance over conventional vision transformers across various tasks.

### Strengths
* Comparative experiments are conducted on image classification, object detection, instance segmentation, and semantic segmentation.
* Challenges and solutions are clearly explained, supported by experimental results.
* The proposed method is sufficiently general to be applicable across different transformer architectures.

### Weaknesses
 * In Tab 1, given the efficient CUDA implementation, experimental results of GPU computation are needed. Specifically, the inference time on a specified GPU should be provided.
* The choice of the number of groups in group-rational KAN is not discussed. What is the reason for the current choice of group number? An experiment analyzing the effect of different group numbers would be beneficial for better understanding.
* For consistency, it would be helpful to include the GPU information used for image classification task as well.
* Could you specify where in the report it states that KAN is "10x slower than MLPs, given the same number of parameters"?

### Questions
* Could you specify where in the report it states that KAN is "10x slower than MLPs, given the same number of parameters"?

### Soundness
4

### Presentation
3

### Contribution
4
