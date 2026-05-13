# Adaptive Graduated Non-Convexity for Point Cloud Registration

- Decision: Reject
- Scores: 8, 6, 6

## Abstract
Point cloud registration is a critical and challenging task in computer vision. It is difficult to avoid poor local minima since the cost function is significantly non-convex. Correspondences tainted by significant or unknown outliers may cause the probability of finding a close-to-true transformation to drop rapidly, leading to point cloud registration failure. Many registration methods avoid local minima by updating the scale parameter of the cost function using graduated non-convexity (GNC). However, the update is usually performed in a fixed manner, resulting in limited accuracy and robustness of registration, and failure to reliably converge to the global minimum. Therefore, we present a novel method to robust point cloud registration based on Adaptive Graduated Non-Convexity (AGNC). By monitoring the positive definiteness of the Hessian of the cost function, the scale in graduated non-convexity is adaptively reduced without the need for a fixed optimization schedule. In addition, a multi-task knowledge sharing mechanism is used to achieve collaborative optimization of non-convex cost functions at different levels to further improve the success rate of point cloud registration under challenging high outlier conditions. Experimental results on simulated and real point cloud registration datasets show that AGNC far outperforms state-of-the-art methods in terms of robustness and accuracy, and can obtain promising registration results even in the case of extreme 99\% outlier rates. To the best of our knowledge, this is the first study that explores point cloud registration considering adaptive graduated non-convexity.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposed a robust point cloud registration method based on Adaptive Gradient non-convexity (AGNC). By monitoring the correct definiteness of the Hessian of the cost function, the scale of gradient non-convexity is adaptively reduced without the need for a fixed optimization schedule. AGNC is far superior to existing methods in terms of both robustness and accuracy, achieving accurate registration results even at extreme 99% outlier rates.

### Strengths
1. Although the idea of this paper is simple, and it is very important for the field of point cloud registration, and I think this paper is very meaningful. Simple is best.

2. For the inherent problem of point cloud registration: high outlier rate, it provides a feasible idea: MULTI-TASK KNOWLEDGE SHARING, which can also perform well in high outlier rate.

### Weaknesses
1.The experimental setup needs to be improved.
 I have my doubts about the experimental setup. A major contribution of this paper is that high outlier rates can also perform well. As for the evaluation of high outlier rate, only on the simulation data set, however, as shown in FIG. 4, the current methods can achieve good registration. This does not speak to the strengths of your approach. On the contrary, on 3DMatch dataset, with high outlier rate, it is difficult for existing methods to achieve robust registration. It is suggested to add the experimental results of Outlier rate=99% in 3DMatch dataset, which can make this paper more convincing. "Accurate registration results are obtained even at the extreme 99% outlier rate." "Is a bit of an exaggeration.

2.Some  typos.
What do we mean by ER and Et in Tables 3 and 4 and 5? Should it be RE and TE?

### Questions
1.For the experiments on 3DMatch/3DLoMatch dataset to be registered with only one feature, I think it is not enough, please refer to the experimental setup of SC2-PCR and MAC. In addition, 3DMatch uses FCGF and 3DLoMatch uses Predator for feature extraction, which is kind of intentional to show the reader better results.

2. It is suggested that ablation experiments should also be done on the 3DMatch data set. Only the contribution to accuracy can be seen for the simulation data set, but not for the robustness, such as the index RR.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the Adaptive Graduated Non-Convexity (AGNC) method for point cloud registration, addressing challenges related to convergence to local minima caused by incorrect correspondences. By utilizing the Hessian of the cost function, AGNC adaptively adjusts the scale of the optimization landscape, enhancing  robustness without relying on a fixed optimization schedule, which can be costly or less effective. Experimental results demonstrate that AGNC significantly outperforms existing techniques on both simulated and real datasets, achieving reliable registration even with up to 99% outlier rates.

### Strengths
Overall, the paper is clearly written, excluding the equations, which could benefit from additional clarification. The algorithm is easy to follow, and the idea is original, effectively addressing the challenges of fixed scaling of cost function posed by graduated non-convexity methods.

### Weaknesses
This paper introduces an adaptive method for adjusting the scale of the cost function in graduated non-convexity (GNC) to address challenges related to convergence steps. However, there are several areas for improvement:

1-While the paper presents experimental validation using a toy example to illustrate the effects of the adaptive scheme on convergence iterations, it lacks critical information on runtime and the computational overhead required for Hessian. Including runtime data in Table 1 would be beneficial, as it would provide a complete picture of performance by accounting for the overhead of Hessian computation and binary search. The analysis should also include a breakdown of the time spent on Hessian computation versus other parts of the algorithm to better understand the computational bottleneck.

2-The paper contains many acronyms, such as FGCF and LSQ, without definitions. It is important to clarify these terms early on to enhance reader understanding. Additionally, several notations, like "r" in Equation 1, are introduced without explanation. These should be defined as soon as they are presented. Equations 6 through 11 also contain unexplained notations, such as \( g_{\text{LSQ},i} \), \( l_i \), and \( m_i \), which are important for understanding their roles in the registration process, and notations like \( z_r \) and \( z_s \) which require further clarification. Are these partial derivatives with respect to rotation and translation, or something else? The meaning of the square brackets with operators outside of them in Equation 7 is also unclear and requires explanation.

3-The assertion that “…. H in Eq. 2 obtained at µ_{k+1} is ensured to remain positive definite, then the new estimate z_{k+1} is guaranteed to be in the same convergence domain as the previous iteration” requires citation or proof. Providing a reference would strengthen the validity of this claim.

4-An insightful addition would be to include experiments assessing the impact of a multi-task knowledge-sharing mechanism with fixed scaling in Table 6, alongside the number of iterations and runtime required for convergence. Currently, the errors without knowledge sharing are worse than those of the fixed scaling scheme, raising questions about whether the adaptive scale adjustment primarily enhances convergence speed rather than accuracy. Adding columns to compare knowledge sharing in fixed scaling settings and the number of convergence stages would clarify the contributions of each component. The runtime is also missing in Table 6. The results with knowledge sharing for the fixed scheme are much better than those without knowledge sharing, but the convergence steps remain the same, which raises a concern. Why did the convergence steps not decrease for the fixed scheme with knowledge sharing despite achieving relatively high accuracy? Could you please clarify the criteria for convergence in this case?

5-I recommend visualizing the outputs from competitive methods in Figure 4 and using bright colours to enhance clarity in the visualizations (minor)

6-In Tables 3 and 4, it is unclear if "ER" and "Et" refer to rotation error and translation error, respectively. If so, for consistency with the previous definitions, they should be labelled as "RE" and "TE" as mentioned in line 344.

7-I am not convinced of the accurate performance of this method, as the criteria for successful registration (line 431) in Tables 3 and 4 seem too lenient for both indoor and object-level settings. Similar concerns also arise for Table 5.

Please correct the spelling of "black-Rangarajan" duality. It would also be beneficial to include a brief sentence explaining what this duality is about for the reader’s clarity.
In line 305, please change the reference from "(line 4)" to "(line 5)"

### Questions
1-Given that computing the Hessian is typically expensive, could the authors please discuss whether alternative routines, such as Adam or RMSprop, could serve as equivalent methods for scaling? How would these compare in terms of performance and convergence speed?
2-The paper states that "little attention has been paid to how the scaling factor is determined." Please provide references to existing techniques that address this issue. Including comparisons to these methods would enhance the context of this work.
3- Once the Hessian is computed, how valuable is its inclusion in the cost function? I would expect this to lead to faster convergence with minimal overhead. Can authors provide insights on this aspect?
4-How valid is it to consider different optimization stages as different tasks? Could authors elaborate on this concept and its implications for the proposed method?
5-How is the final value of \mu_{final}determined? 
6-Could authors add extra columns in Tables 3 and 4 to indicate the range of initial total translation and rotation offsets? The translation errors of greater than 6 cm and 9 cm for even the best performances seem unacceptable for practical applications in small indoor settings.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on the task of registration, specifically on estimating the rotation and translation given correspondences that may exist outliers. To this end, it presents a method to register point clouds rubostly by leveraging Adaptive Graduated Non-Convexity (AGNC). First, the scale in graduated non-convexity is reduced by monitoring the positive definiteness of the Hessian of the cost function. Then knowledge sharing mechanism across different tasks is used to achieve collaborative optimiazation. Experiments are conducted on both synthetic and real datasets, and the results demonstrate the significance of the proposed method for robust point cloud registration.

### Strengths
1. The idea is novel, and from the experimental results, it helps boost the registration performance without additional traning procedure. It can be widely adopted as an alternative to RANSAC;

2.The overall writing is OK

3. Experiments are conducted on both synthetic and real data, and the results are convincing

### Weaknesses
1. In the experimental results, it seems there is no time analysis. It is better to compare the proposed method to existing ones in terms of time cost;

2. The experiments on Indoor Scenes may be insufficient, as this is the main field that registration methods focus on. I would suggest adding different descriptors on both 3DMatch and 3DLoMatch, those descriptors should cover a wide range of outlier rates. (as on synthetic data, the test covering different outlier rates is included, but on real data, there is no such setting) Moreover, using FCGF descriptors on 3DMatch but Predator on 3DLoMatch is weird. It looks like that FCGF doesn't perform well on 3DLoMatch, which leads to bad results for the proposed method. The authors have to choose another descriptors for 3DLoMatch.

3. More  visualization results on indoor and outdoor scenes are encouraged. And it is also better to directly visualize the correspondences before and after using the proposed method.

4. Some closely related works may be missing:

  [1]. Yu et al. CoFiNet: Reliable Coarse-to-fine Correspondences for Robust Point Cloud Registration, NeurIPS 2021;

  [2]. Ao et al. SpinNet: Learning a General Surface Descriptor for 3D Point Cloud Registration, CVPR 2021

   [3]. Qin et al. Geometric Transformer for Fast and Robust Point Cloud Registration, CVPR 2022;

   [4]. Want et al. You Only Hypothesize Once':' Point Cloud Registration with Rotation-equivariant Descriptors, ACM MM, 2022;

   [5]. Yu et al. RIGA: Rotation-Invariant and Globally-Aware Descriptors for Point Cloud Registration, TPAMI 2024
   [6]. Yu et al. Rotation-Invariant Transformer for Point Cloud Matching, CVPR 2023;

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
