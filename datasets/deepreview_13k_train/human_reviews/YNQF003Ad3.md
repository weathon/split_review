# Factorized Implicit Global Convolution for Automotive Computational Fluid Dynamics Prediction

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Computational Fluid Dynamics (CFD) is crucial for automotive design, requiring the analysis of large 3D point clouds to study how vehicle geometry affects pressure fields and drag forces. However, existing deep learning approaches for CFD struggle with the computational complexity of processing high-resolution 3D data.
    We propose Factorized Implicit Global Convolution (FIGConv), a novel architecture that efficiently solves CFD problems for very large 3D meshes with arbitrary input and output geometries. FIGConv achieves quadratic complexity $O(N^2)$, a significant improvement over existing 3D neural CFD models that require cubic complexity $O(N^3)$. Our approach combines Factorized Implicit Grids to approximate high-resolution domains, efficient global convolutions through 2D reparameterization, and a U-shaped architecture for effective information gathering and integration.
    We validate our approach on the industry-standard Ahmed body dataset and the large-scale DrivAerNet dataset. On DrivAerNet, our model achieves an $R^2$ value of 0.95 for drag prediction, outperforming the previous state-of-the-art by a significant margin. This represents a 40\% improvement in relative mean squared error and a 70\% improvement in absolute mean squared error over prior methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This manuscript describes a method for regressing drag coefficient and pressure field for automotive fluid dynamics simulation data. The proposed method achieves higher accuracy with lower computational complexity by representing the data by a set of different projections and fusing the corresponding set of predictions. The resulting models are evaluated on the DrivAerNet and Ahmed body Datasets.

### Strengths
- the algorithm shows good performance on the chosen application
- the manuscript makes an attempt to generalize prior work that used plane projections or separable convolutions
- in most parts, the manuscript is easy to read

### Weaknesses
 - the mathematical description is in several cases unclear or wrong, see questions below 
- the manuscript is partly rushed an contains errors, see detailed issues
- the proposed method is designed for a very specific application, which limits the contribution, see final question below.
- detailed issues
    - Pfaff et al. 2020 a and b is the same
	- L055 girding
	- L301-305 after reading this part three times, it still does not reveal its meaning, needs reformulation.
	- table 2, caption a symbol is missing after the kernel size definition
	- figure 5 lost its number, says just a and b
	- L514: table 6 is in the appendix, not the main paper

### Questions
- L043: when it says "most of these works", it implies at least one doesn't. So which approach is that and what is different with that approach compared to the others?
- 2.1/3.1 why is the approach called "factorization"? There is no product in (1)/(2), just a linear combination of non-linear projections. What is the relation to the mathematical concept of factorization?
- for one position v, the complexity is reduced, but doesn't the regression task for the pressure fields require prediction at the full grid resolution, i.e. $O(N^3)$? Please elaborate more on the computational complexity, also in the case of computing the pressure field prediction as done in the experiments.
- is the function f() in (3) the same as in (1) and if so, what argument is replaced with the 3d convolution? If it is a different function, how is it defined?
- what is the difference between global convolution as used in 3.3/figure 2c and a simple scalar product / contraction alternatively a point-wise operation along the chosen dimension? What are the advantages of the identified differences?
- looking at the identity (4)=(5), a contradiction is obtained for e.g. incrementing $s$ from 1 to 2 vs $c_{in}$ from 1 to 2 (if we assume C>2). The kernel $W$ might have different values in (4) but the same value is used in (5). Or is there anything wrong with this example? Please provide a proof if possible.
- L252: 3D convolution is a linear operator, why wouldn't it be possible to rewrite in matrix multiplication with the flattened vector in all cases? What are the differences between the standard matrix formulation of convolution and the proposed formulation?
- (6) vs (7): it is well known that convolution is commutative. Correlation requires additional reflection. To which extent differs (7) from correlating with the swapped (and reflected) arguments?
- L301 how is a continuous convolution realized in the voxel-based grid? Which signal model and approximation is used?
- (8) is a function over $m$, obviously missing on the RHS, but where? Please provide a corrected/complemented formulation.
- L423 what is meant by DFCNN not incorporating both? Both are occurring table 1? Please revise the formulation or explain.
- L655 this reference is quite important for the submitted manuscript. Has this reference been published or is it still just a preprint?
- to which other application domains can the proposed method be applied to? Please discuss potential applications of the proposed method beyond automotive CFD and highlight any modifications that might be necessary for other domains.

### Soundness
1

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
The authors introduce FIGConv, an efficient spatial representation learning method designed to address large-scale 3D simulation modeling challenges. Their experimental results are remarkable, showing significant improvements across two large datasets. Notably, on the Ahmed Body dataset, FIGConv achieves an order-of-magnitude improvement over GINO, a result that is indeed impressive. However, the manuscript does not provide sufficient insight into the specific aspects of the FIGConv architecture that contribute to such substantial performance gains compared to previous state-of-the-art models like GINO. Understanding what aspects of the proposed model structure enable these advancements would be beneficial.

### Strengths
1. The experimental results are impressive.
2. The authors introduce Factorized Implicit Grids and Factorized Implicit Convolution methods to the neural operator field as an efficient representation learning modeling method.

### Weaknesses
1. As far as I know, many attention-based methods deal with this problem, and representation learning for large-scale 3D data. Why did the author not discuss it in the related work section and conduct comparative experiments as the baseline in the methods section? Oformer, GNOT, Transolver. 

2. The method part of the paper is poorly stated. First, what is the problem definition? What are the inputs and outputs of the model? Second, what are the core innovations of your model? How to apply the method of 3d decomposed representations in the cv domain to the operator domain? So what's the innovation of your model? 

3. The experimental part, at present, seems to only have the main result part, which shows the effect of the proposed method on the two data sets. As I initially questioned, the model achieved impressive results, so why? Why such a big improvement? Which modules play an important role? 

4. The authors did not open source or provide pseudocode for the algorithm, leaving us unclear on exactly how the method works.

### Questions
The experimental results of this paper are impressive, but the manuscript is unable to provide a strong explanation, and if the authors provide some convincing feedback, I will consider improving the score further.

1. In the related work section, can the author join the discussion of attention-based methods? Many attention-based methods show quasi-linear computational complexity, which is in sharp contrast to the quadratic complexity of the proposed method. Please refer to the author for further elaboration.

2. As suggested in the previous section, can the authors go into further detail in the methods section? What is the problem definition? What are the inputs and outputs of the model? After input mesh, how is learned factorization obtained, and in the final fusion, how is the corresponding pressure obtained? What is data streaming?

3. What are the core innovations of your model? How to apply the method of 3d decomposed representations in the cv domain to the operator domain? So what's the innovation of your model?

4. Can we add comparison experiments of attention-based methods in the experimental part? GNOT, Transolver, etc., have linear complexity.

5. Then 4, in the experimental section, can more ablation experiments be provided? As I initially questioned, the model achieved impressive results, so why? Why such a big improvement? Which modules play an important role?

6. The authors did not open source or pseudocode the algorithm, leaving us unclear on exactly how the method works.

### Soundness
3

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
The author used factorized implicit global convolution as a supervised learning algorithm for CFD problems for the prediction of pressure quantities. They claimed that the complexity of their algorithm is O(N^2), compared to other methods, which have the same complexity of O(N^3). They tested their work over 3D benchmark problems. More specifically, they integrated factorized implicit global convolution with U-Nets. They used point convolution to convert grid vertices of unstructured meshes to the space of the factorized implicit global convolution networks. They also compared their model to others, such as PointNet++, PointNext, etc. Comparisons were made using different metrics such as the R2 score, root mean squared errors, and visual comparisons.

### Strengths
--> Well written, high-quality figures, 3D benchmark problems (rather than 2D), comprehensive error analysis,

### Weaknesses
-->The following statement from the manuscript is inaccurate and based on a false assumption. The literature was not thoroughly reviewed:

**Prior works in the deep learning literature, focusing on large-scale point clouds, ranges from the use of graph neural networks and point-nets to the u-shaped architectures along with advanced neighborhood search (Qi et al., 2017a; Hamilton et al., 2017; Wang et al., 2019; Choy et al., 2019; Shi et al., 2020). However, these methods make assumptions that may not be valid when applied to CFD problems.**

This is not true, PointNet and PointNet++ have been successfully applied to 2D and 3D problems in CFD.  

--> The main issue of this work is grid projection, a challenge faced by all convolution-based neural networks. The authors use PointNetConv to map 3D finite volume vertices to a convolutional representation, but this mapping introduces errors when converting from unstructured grids to Cartesian grids. As a result, the advantages of PointNet and graph neural networks, which excel in handling unstructured data, have been overlooked, and not discussed by the authors.

--> Another wrong assumption by the authors. Please note that PointNet and PointNet++ have been used to predict the velocity and pressure of whole space in CFD problems not only the surface of objects. In this work, the authors only predict the pressure on the surface. 

--> The literature review overlooks several researchers who have done significant work in applying PointNet and graph neural networks to CFD problems. 

--> The paper seems a bit misleading, as the authors initially propose that their work addresses CFD problems, but they ultimately reduce the problem to predicting the pressure distribution on the surface. The introduction needs to be rewritten to reflect this more accurately.

--> In the end, I would say that the authors have done a lot of work; however, the proposed framework is very complicated and not scalable, and the results are not impressive.

### Questions
--> On page 15, line 808, the figure number is missed and we see ??. Please fix it.

--> I suggest writing the Navier-Stokes Equations, at least, in Appendix.

--> I suggest adding the visual results of the Ahmed Body benchmark in the Appendix.

--> The authors claim to have compared their model with others, such as PointNet++. In the appendix, they provided the code. On line 845, we see that the radius is set to 0.05. This is a very sensitive hyperparameter and plays a significant role in the performance of PointNet++. Did the authors fine-tune this parameter or not? When comparing our model to previous models, we should be fair and aim to achieve the best performance for all models involved.

--> I have also listed some issues in the Weaknesses section. Please address them.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces FIGConv, a U-shaped architecture to solve large-scale 3D CFD problems for the automotive industry, specifically to perform regression of the drag coefficient and the pressure field of a CFD simulation. FIGConv main contribution is the reduced computational complexity, of O(N^2), as opposed to most other pipelines with complexity O(N^3 logN^3). The authors correctly stress the main limitation of deep learning models employed in CFD, i.e. their scalability when processing large meshes. 

 The reduced computational complexity of FIGConv is achieved through an approximation of high-resolution meshes via Factorised Implicit Grids, which significantly reduces the number of input elements by a factor of 10. This is done by creating M implicit grids via an MLP (learnt representation), each implicit grid having one low resolution axis. Such grids are then processed by Factorised Implicit Convolutions, which simplify 3D convolutions. FIC works by projecting 3D convolutions onto 2D ones by flattening the low resolution dimension of the FIGs. 

Such choice of representation is based on recent advancements that use multiple orthogonal 2D planes to represent 3D quantities and on the technique of weights factorisation, which is however applied at domain level rather than at kernel level. 

FIGConv is validated on two datasets, DrivAerNet and Ahmed body dataset and authors present results on estimated pressure field and drag coefficients. These two quantities are estimated at decoder and encoder stage, respectively, of the proposed architecture.

### Strengths
The paper introduces a representation for large 3D meshes and an approximation of 3D convolutions for the estimation of physical quantities in CFD simulations.

It tackles an important issue common to all learning-based PDE solvers, i.e. the handling of large meshes.

Good contextualisation with respect to previous work.

Results are promising and a comparison with multiple models is offered, especially in terms of speed. 

The paper is fairly clear and easy to read.

### Weaknesses
Major points:

My main issue in the paper is Table 5, which shows some shortcomings in the overall approach:

1)  Reporting normalised error at test stage is formally incorrect, since at inference time we wish to have an estimate of actual pressure values, not normalised ones.

2) An error of 0.89% seems optimistic, especially considering that FIGConv is a convolutional neural network, while Neural Operators have been already demonstrated to be superior to most architectures when it comes to PDE modelling. The lack of figures and discussion on this result is also an important limitation. Li et al. use 0 mean, unit standard deviation normalisation, which yields a relative L2 norm error a bit higher compared to the denormalised version (you can do the math yourself and compare the normalised and denormalised relative L2 norm), which would mean a denormalised error similar or even lower compared to 0.89%. In the appendix you mention the same type of normalisation procedure, but, without further elements to assess the results and based on personal experience, an error of 0.89% is more likely to be deriving from a min max normalisation instead, since it squeezes the range of pressure values and significantly underestimates the error. The fact that the authors claim to use the same evaluation code as Li et al. does not justify the discrepancy in the results, as the reported error is an order of magnitude lower, which is a substantial claim that requires more thorough justification.

3) Intuition on why such good results are obtained on the Ahmed Body dataset but not on the DrivAerNet dataset is also missing.
 
The paper often cites GINO, by Li et al. The computational complexity cited by Li and by the authors of this paper, however, is not consistent, and I don’t see a complexity of O(N^3) reported by Li et al. I invite the author to be clearer on the meaning of N in their work. 

The paper does not discuss the complexity added by the chosen representation: the MLP, the sampling and the radius search all play a role in the FIGConv pipeline and they have an impact on the computational complexity. Such impact, even if minor, is not mentioned.

There is no intuition behind why the proposed approach would work better - FIGConv is used to justify the reduced computational complexity (obtained by moving from a 3D to an almost-2D approach), the faster processing and the smaller model size, which I understand. The authors, however, do not provide a reason why it would actually perform better compared to neural operators, for example. 

Results are listed but they are not thoroughly discussed.

Minor points:

Notation is not clearly introduced (e.g. meaning of N, M).

Fig. 6 has no color bars, making it hard to interpret.

Some minor typos spotted: u-shaped vs U-shaped (lines 86, 109), Cardimality (line 262), ConvNet vs convnet (line 327). 

General comments:

While I find the idea of representation fairly original, since it is an important question common to most research in large-scale, 3D PDE solver, I would have liked to see authors make a better argument on why FIGCov performs so well on the regression of the proposed physical quantities. I find the explanation of FIGCov working principle and benefits in terms of computational complexity clear and satisfactory, but those don't necessarily justify the enhanced accuracy. Do I think that FIGs are an original idea and worth presenting? Yes. Is it a game-changing approach in the field or would I use it in my own works? Probably not. 
While the introduction of the work seems promising, the second half of the paper feels rushed and not that well executed, especially in the way in which results are presented, discussed and justified.

### Questions
Line 56: What does N represent in your paper? It is mentioned that GINO by Li et al. (NeurIPS 2023) has complexity O(N^3 logN^3), but from their paper, the reported complexity is O(N log N + N degree), with N, quoting, being “the number of mesh points” and “degree” stemming from the graph representation. 

Line 160: What does the number of channels $C$ represent?

Line 194: How have $r_x, r_y, r_z$ been picked?

The reported computational complexity of O(N^2 logN^2) derives from the approximated 3D convolutions and the FIG representation. However, the complexity of the MLP which learns the FIGs, of the radius search of Eq. 8 and of the fusion of the feature maps is not discussed. How do those play a role, if any?

Fig. 6: What is the range of the of the pressure field? Is It normalised or denormalised? It is hard to tell how predictions compare with ground truth, also because the colors maps are not exactly consistent. 

Table 5: The error metrics for Unit, FNO and GINO is relative L2 norm, but in the caption you mention L2 pressure error. Which one are you using, relative or absolute? I assume you meant relative?

Line 485: You report a normalized pressure error of 0.89%. Is this correct? A decrease of about 8% in error is huge, especially on a hard dataset like Ahmed body, and such improvement should be justified, which you don’t do in the text. Also, there is no figure on how the estimated pressure fields for the Ahmed body dataset look like to back up the claim. A discussion on this is especially needed since FIGConv performs only marginally better compared to other architectures on DrivAerNet, but significantly better on Ahmed body: what's the intuition behind such disparity between the two datasets?

 Moreover, a few points to be made: 
 1) errors at test stage have to be reported on denormalised data, since what we care about in the end is the value of pressure in its original unit of measurement.    2) How are you normalising the data? 

3) The fact that FIGConv is purely convolutional requires an explanation: why does GINO, which is a GNO + FNO architecture, perform poorly compared to FIGCov?

line 526: physics-based constraints can be hard to include, for example PINN are a whole different class of models. There are methods that provide an easy inductive bias, for example by embedding physical quantities within Clifford Algebra (cfr. Brandstetter et al., 2022, Ruhe et al. 2023), which could be an easier next step to boost the performance of FIGConv, especially since you are estimating two physical quantities at once. Have you considered that?

### Soundness
2

### Presentation
2

### Contribution
2
