# Physics-Informed Neural Predictor

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
Accurately predicting fluid dynamics and evolution has been a long-standing challenge in physical sciences. Conventional deep learning methods often rely on the nonlinear modeling capabilities of neural networks to establish mappings between past and future states, overlooking the fluid dynamics, or only modeling the velocity field, neglecting the coupling of multiple physical quantities. In this paper, we propose a new physics-informed learning approach that incorporates coupled physical quantities into the prediction process to assist with forecasting. Central to our method lies in the discretization of physical equations, which are directly integrated into the model architecture and loss function. This integration enables the model to provide robust, long-term future predictions. By incorporating physical equations, our model demonstrates temporal extrapolation and spatial generalization capabilities. Experimental results show that our approach achieves the state-of-the-art performance in spatiotemporal prediction across both numerical simulations and real-world extreme-precipitation nowcasting benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposed the PINP method for fluid prediction. The method predicts future fluid fields by learning velocity and pressure simultaneously from partial observations. The authors employ a physical inference neural network to predict several physical quantities of the flow field at a particular moment. For the next timestep, they utilizes discrete PDEs predictor and correction network to generate the flow field. The training of the model is refined through the application of MSE loss, equation loss, and a temporal constraint loss. The proposed method shows advantages compared to several baselines on both synthetic and real-world data.

### Strengths
This paper combines equation loss with operator learning through the Navier-Stokes equation, integrating physics-driven and data-driven approaches by learning unobserved physical quantities.
- An innovative point of the proposed method is incorporating the equation loss commonly used in PINN, including incompressible Navier-Stokes equations, into predicting potential physical quantities of the future flow field.
- The figures provided in the paper can accurately reflect the characteristics of the model.
- The ablation of the paper accurately explains the role played by each module.

### Weaknesses
This paper has some weaknesses, including:
- Some datasets are too simple or may theoretically not match the methods to some extent.
  - The fluid motion in the Flow 2D dataset is relatively slow, and the dynamics are not as complex as those encountered in more advanced fluid dynamics scenarios. Specifically, the Reynolds numbers explored appear to be in a laminar flow regime, lacking the complex vortex shedding and turbulent structures that would be expected in more challenging scenarios. This limits the assessment of the model's ability to handle complex fluid dynamics.
  - The fluids in real datasets may not strictly adhere to the incompressible Navier-Stokes equations. Consequently, the physical constraints proposed in this paper might encounter limitations when applied to more diverse or complex fluid systems. The SEVIR dataset, for instance, involves atmospheric phenomena where phase transitions and non-ideal fluid behaviors could significantly impact the validity of the incompressible Navier-Stokes equations as a strict constraint.
- The improvements observed in specific datasets, such as Smoke3D, are modest. For example, the MAE and MSE metrics of Smoke 3D only demonstrate a marginal enhancement. This raises questions about the practical significance of the proposed method's improvements over existing techniques, especially given the added complexity of the model.
- The paper's grammar and expression could be improved. In some instances, the clarity of the writing detracts from the overall quality of the paper, potentially hindering the reader's understanding of the research.

Specific issues and possible improvements will be discussed in the next section.

### Questions
- For the sole real dataset, SEVIR, raises several concerns:
  - It is unclear why the MSE metric for the proposed method underperforms compared to most other baselines. A detailed analysis and discussion of this discrepancy would be beneficial.
  - Given the potential phase transition of water in the SEVIR dataset, it is questionable whether the fluid satisfies the incompressible property. The authors are encouraged to discuss the applicability of the equation loss function to real datasets with such characteristics.
  - I highly recommend the authors compare with the traditional numerical method pySTEPS[1], which predicts future fluid fields by estimating potential velocity fields and extrapolating optical flow. This method has the ability to accurately estimate extreme values.
- The paper does not specify the fluid's Reynolds number, which is crucial for understanding the flow characteristics. The fluid in the Fluid 2D dataset appears to represent simple laminar flows. The authors are recommended to provide experiments with more turbulent datasets to enhance the paper's practical value.
- The paper lacks information on how the baselines were trained, and some baselines exhibit abnormal flickering. The authors should recheck the training process for all baselines or explain these anomalies.
- The visualization of velocity in the paper is not as intuitive as it could be. Utilizing tools such as *pyplot.quiver* in *matplotlib* to depict the velocity field based on flow field observations as supplementary material is suggested.
- The grammar and expression throughout the paper should be improved. A thorough review and enhancement are advised.


[1] https://pysteps.github.io/

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work presents a new physics-informed learning approach that enables the prediction of coupled physical states, under a partially observed data environment. It applies the discretization of physical equations, integrating into the model architecture and loss function. The superior performance is shown in four benchmarks including a real-world data.

### Strengths
1. The proposed method enhances the simulation capacity of PDEs, especially on the long-term prediction.
2. The proposed method is tested on multiple benchmarks across different scenarios, especially on the real-world measured dataset.
3. The authors vividly demonstrated the simulation process through videos.

### Weaknesses
 1. The reviewer believes that there are significant issues with the introduction of the method. The method is complex and lacks an overview of the proposed method. The reviewer understands that the proposed method first outputs $p(t')$, $u(t')$, and $c(t')$ through a physical inference network, where these three outputs are constrained by physical and temporal conditions. Then $\hat{c}'(t+1)$ is computed through discretized PDEs, after which $\hat{c}'(t+1)$ and $c(t)$ are fed into another network for prediction, while simultaneously incorporating a data loss with the label. If this understanding is correct, the reviewer questions the novelty of this work, as it merely sandwiches numerical FDM calculations between neural networks. Moreover, the motivation for this approach remains unclear.
 2. In line 039, the statement is inaccurate and needs to be referenced to the literature. The reviewer points out that velocity fields can be observed through techniques such as PIV and PTV.
 3. In line 069, what does the past observable data mean. Authors should introduce more about the settings.
 4. In line 102, "often difficult to obtain in practical applications". The reviewer considers the statement is inappropriate, as initial conditions are typically obtainable when solving PDEs.
 5. In Table 1, the reviewer appears to have misinterpreted the meaning of the three categories in this table. If 'velocity' refers to velocity fields, then this table is not appropriate, as FNO (Fourier Neural Operator) is equally capable of predicting both velocity and pressure fields.
 6. In Eqn. 3, why does this equation still integrate from t to t+1? A more detailed derivation process is needed to help readers understand. This is crucial for comprehending the motivation behind the problem. What is the meaning of $\Delta t$?
 7. In Sec. 3.4, the introduction is oversimplified, merely stating which networks are used. This raises two concerns for the reviewer: first, why was U-Net chosen over more advanced transformer architectures, and second, too many network structural details are omitted, forcing readers to consult the appendix for understanding.
 8. In Sec. 3.5, author should carfully introduce the training process as there are many networks and parameters. Are they trained in an end-to-end manner? This raises a question about how the physials inference network can simultaneously learn Pe and output flow fields. These two components might interfere with each other, potentially making the network untrainable. Has the use of stop-gradient operations like VQVAE been considered?
 9. What is the PDE for the real-world data? Is it explicitly known? Real data often comes with noise - has this method considered noise effects, or are there any approaches proposed to address the influence of noise?
 10.  In Sec. 5, especially in Fig. 9(a), the authors need to specify the number of experimental trials conducted and report the confidence levels, as it appears that the two constraints overlap for an extended period of time.
 11. What is the detail setting of the fluid 2D data, including $\nu$, $dx$, $dt$, and boundary conditions?
 12. The reviewer does not find the link of code and dataset from the paper. Code and data are important criteria for verifying the rationality of results. Will the author make them opensource？

### Questions
Please check the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper's core idea is to combine a data-centric deep learning approach with physics by incorporating the discretised Navier-Stokes equations into the neural network architecture and constraining the loss function. By explicitly incorporating the governing equations and the associated physical quantities, the authors try to model the system and help with consistency, interpretability, and extrapolation capabilities. The extensive proposed experiments show good performances and generalisation to unseen domains.

### Strengths
- The paper is very well written and explains complex problems clearly.
- While the idea of incorporating PDE-based constraints in the network architecture and loss function is not new, the author presents a set of methods, tricks, and ideas that make the technique work better than previous literature.

### Weaknesses
 - Interpretability depends on the other physical quantities' models. While there are theoretical reasons to believe the quantities are interpretable, there is little experimental evidence.
- The pertinence of benchmarking nowcasting and the advantage of this method over other neural operator-based methods for this task is unclear.

### Questions
- The gradient discretisation used here is a second-order central difference approximation. Could you elaborate on whether there were specific architectural reasons for choosing this method over other discretisation schemes? Additionally, it would be helpful to understand if you considered alternative discretisation approaches
You compare two different sets of baseline: one for now-casting and one for Navier-Stoke simulation. Why is your model capable of doing both, as other neural operator-based models are not? That seems like a significant advantage that has yet to be developed.

### Soundness
4

### Presentation
3

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
This paper proposes a new physics-informed fluid predictor, named PINP. PINP firstly estimates the underlying pressure and velocity filed from observed fluid, which is constrained by a discretized physics loss. Then it employs an interpolation formalization of integral for future prediction, where an additional correction network is presented to reduce the error of discretized PDE predictor. Experimentally, PINP performs well in 2D and 3D flows and weather prediction tasks.

### Strengths
This paper is overall well-written.

The idea of incorporating physics loss into fluid prediction is reasonable.

The authors have provided comprehensive experiments to verify the effectiveness of the proposed method.

### Weaknesses
1.	The title is kind of overclaimed.


Since this paper is tailored to fluid prediction, I think “physics-informed fluid predictor” is more suitable. Otherwise, it is a little bit overclaimed, where there are extensive prediction tasks that PINP cannot solve, such as rigid body movement (controlled by classical physics) or magnetic field (governed by electromagnetism).

2.	A series of technical designs are underexplored or not well supported.

(1)	PINP adopts the discretized PDE loss for physics constraint, which may bring serious approximation error. The current design is based on the assumption that the differential operator can be approximated by spatial or temporal difference, which cannot be satisfied, especially in low-resolution data. Note that I am not saying that being physics-informed is a bad idea. The canonical physics-informed neural works employ the auto differential in neural works for approximation, which is much more precise than the discretization in PINP.

(2)	I cannot figure out that why additionally predicting the pressure field can boost the performance. As shown in Figure 2 (b), the predicted pressure field is only used in physical constraint loss, which cannot affect the future prediction process. This means that predicting the pressure field is just to fit the physical loss, which brings a new meaningless task. According to my experience, I think this design can only bring extra load to the model instead of benefiting the prediction. Besides, as shown in Figure 9(a), removing physical constraints will not bring a serious decrease. Further, How about keeping the second equation in Eq.(12) but removing the pressure-related one? I believe that the benefit of physics loss is mainly brought by the incompressible term loss.

(3)	The design of the correction network is also weird. As formalized in Eq.(10), the inputs and outputs of the correction network are both expected to be close to the ground truth. Under this constraint, why correction network is necessary? (Minor: Eq.(10) may have a typo, where the comma should be “-”).

(4)	About the temporal loss. I am curious about how likely is this loss function to work. Some statistical results on how many times this loss is non-zero are expected.

Going further from (2), I doubt that the prediction of pressure field is useless in the current design, which is listed as one of the main contributions w.r.t. other papers. I think compared with Helmfluid, the advantage of PNIP lies in the physical loss, which can provide a more direct and explicit constraint to the velocity field.

In summary, I think there are many unsupported designs in the proposed method, which may affect the claim of the main contribution of this paper.

3.	About the efficiency. 

I am curious about the training overload. Since the calculation of loss in Eq.(16) may also cause extra computation costs than other baselines.

### Questions
1.	About implementation of baselines.

In NowCastNet, ensuring eidetic prediction results is one significant contribution of this paper. However, as shown in Figure 8, its prediction is quite blurry. I am wondering how the authors experimented with this baseline.

Besides, in the supplementary materials, the prediction results of LSM and FNO appear strange periodic shakes. Actually, I think a well-trained deep model will not make such weird predictions. Did the authors carefully tune these two baselines?

2.	About spatial generalization.

Why PINP can achieve spatial generalization? Can the authors provide some intuitive explanations?

### Soundness
2

### Presentation
3

### Contribution
2
