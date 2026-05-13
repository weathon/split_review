# Groundwater Seepage Modeling in a River-Canal System based on Physics-Informed Neural Networks

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
Neural networks, especially deep learning, have achieved revolutionary advances in several domains, including image and speech recognition, with excellent results. However, their reliance on labeled data, lack of interpretability, and inconsistency with physical principles limit their applicability in groundwater seepage prediction and other scientific disciplines. Physics-Informed Neural Networks (PINNs) significantly improve these issues by integrating physical knowledge with neural networks. This study focuses on modeling the groundwater flow field and proposes a physics-informed river-canal groundwater seepage model (PI-RGSM). This model enables self-supervised learning by incorporating hard constraints of boundary and initial conditions, utilizing hydrogeological parameters and boundary conditions as direct inputs, thus diminishing dependence on observable data. Compared to the baseline PINNs, the PI-RGSM adapts to and accurately predicts diverse seepage situations with just one training session, achieving a mean coefficient of determination of 0.978. To further enhance applicability in complex dynamic groundwater seepage situations, we propose PI-RGSM-K, which builds upon PI-RGSM. This model simulates heterogeneous groundwater seepage fields and improves performance in complex seepage environments through parameterized hydraulic conductivity field $K(x,y)$ and fine-adjusted model architecture, attaining a mean coefficient of determination of 0.982. The physics-informed neural network models proposed in this study demonstrate exceptional efficacy in precisely forecasting groundwater seepage behavior.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents an extension of physics-informed neural networks (PINNs) for groundwater seepage modeling, termed PI-RGSM. The proposed method enforces hard constraints on the initial and boundary conditions in the outputs of the neural network. A variant of PI-RGSM is also proposed to handle heterogeneity in hydraulic conductivity field. Experiments are performed on groundwater simulations to compare PI-RGSM with the PINN baseline.

### Strengths
1. Applies PINNs and its variants on a new real-world problem.
2. Provides details of the model architecture and the loss functions used in proposed PI-RGSM framework.

### Weaknesses
1. The overall evaluation of the paper is weak. The paper mentions (in lines 167-169) that the main challenges in PINNs are the gradient pathologies with multiple loss terms, and the tedious nature of adjusting the trade-off hyper-parameters between these different terms. There is a rich body of work that addresses these challenges in PINNs, and should be used as baselines for comparison. Here are some of them: [1, 2, 3, 4] 
2. Lack of comparison with methods that can enforce hard boundary constraints [5] in PINNs.
3. The “Input feature fusion” concept introduced in the paper is similar to the Neural Operators [6, 7, 8], where the ML model learns a family of PDEs instead of one single instantiation of a PDE. Therefore, the proposed PG-RGSM architecture seems like a simpler variant of the DeepONet [7] architecture, where both the coefficients and the spatio-temporal inputs are combined into one model instead of having a separate branch and trunk networks. Comparing against neural operators like DeepONets would further improve the paper.

### Questions
See weaknesses above.

### Soundness
2

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
The paper introduced a physics-informed river-canal groundwater seepage model (PG-RGSM) and its variant PG-RGSM-K to model the groundwater seepage described using a PDE. Specifically, the paper proposes a way to incorporate boundary and initial conditions as hard-constraints in PINNs using a boundary constraint function. Further, the paper introduces an input-feature fusion that enables PINNs to learn solutions with different PDE coefficients.

### Strengths
1. The problem of predicting river-canal groundwater seepage is interesting and is very important for a number of scientific applications.
2. The proposed method of enforcing hard-constraints is interesting.

### Weaknesses
1. The paper is poorly organized and lacks clarity, with essential content relegated to the appendix, leaving the main text insufficiently self-contained. See questions below for specific issues.
2. Although applying PINNs to groundwater seepage is relatively novel within the specific application area, the paper contributes little in terms of new machine learning techniques.
3. The model relies on manual tuning of hyperparameters (e.g., loss weights, threshold $H_{EC}$), but the paper lacks experiments analyzing the impact of these parameters.
4. The paper fails to compare the proposed method with existing machine learning models for groundwater seepage.

### Questions
1. It might be interesting to investigate why PINNs fail for this particular PDE (lines 167-169).
2. In the Introduction section, there are a couple of references to the Appendix. Adding appropriate citations (along with ref. to the appendix) would improve the readability.
3. The Related Works section provided in the Appendix was really helpful. I would suggest shrinking it and adding it to the main paper to help readers familiarize with the current state-of-the-art.
4. The paper claims that PG-RGSM improves convergence rates (line 179). It will strengthen the proposed method if it is demonstrated empirically.
5. Eqn 11: The $t$ present in both the numerator and denominator of $C(x, y, t)$. Shouldn’t the denominator be $T$ (which is the final time)?
6. How are the Dritchlet boundary conditions obtained for this problem?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes two models, PI-RGSM and PI-RGSM-K, for groundwater seepage prediction using physics-informed neural networks (PINNs). These models integrate physical constraints into neural networks to enhance prediction accuracy in groundwater flow, reducing dependency on observational data and adapting well to complex seepage conditions. PI-RGSM-K extends the base model by incorporating heterogeneous hydraulic conductivity fields, showing improved adaptability in complex conditions.

### Strengths
1. The paper effectively applies physics-informed neural networks to model groundwater seepage, enhancing model interpretability and physical consistency.
2. By integrating hard constraints, the models reduce reliance on labeled data, making them suitable for scenarios with limited observational data.
3. The models achieve promising predictive performance.

### Weaknesses
### weaknesses:
 - (clarity/novelty) The authors claim they introduce self-supervised PINNs, but I fail to comprehend how these models are more self-supervised than the original PINNs.
   The proposed models seem to use have an additional scaling and shift on top of the additional inputs compared to the baseline PINN, but I do not see how this makes these models self-supervised. Specifically, the training objective still relies on minimizing the residual of the governing PDE, similar to standard PINNs. The addition of scaling and shifting parameters does not fundamentally change the reliance on the PDE for supervision. A more detailed explanation of how the proposed modifications enhance the self-supervised nature of the model is needed.
 - (novelty) This model fails to cite any relevant related work in the main paper.
   I noticed there is a related work section in the appendix, but that does not suffice.
   During reading I had the impression this is the only paper applying deep learning in the field of hydrogeology, which is obviously not the case.
   Furthermore, the main paper should discuss how the proposed method compares to existing methods. A thorough comparison with prior work, especially in the context of incorporating physical constraints into neural networks, is crucial for establishing the novelty of the proposed approach.
 - (quality/clarity) I could not find information on how the baseline PINN was trained.
   E.g. section 2.2 mentions the different hyper-parameters in the loss function, but I could not find any information on what hyper-parameters were used or how they were found. Without details on the hyperparameter tuning process, such as the range of values explored and the criteria used for selection, the results cannot be properly evaluated or reproduced. The lack of a systematic approach to hyperparameter optimization raises concerns about the robustness and generalizability of the baseline model.
 - (quality) Each model is compared to a single baseline PINN.
   I strongly doubt that there are no stronger baselines to compare against (e.g. regular networks, non-ML methods, ...).
   Furthermore, the performance of the baseline PINN is so poor that it seems as if something went wrong during training (assuming a random model would achieve an R^2 of 0).
   Also, there are no error bars to indicate the consistency of the compared model(s). The absence of stronger baselines and error bars undermines the validity of the experimental results. A comparison with established numerical methods or other machine learning approaches would provide a more comprehensive evaluation of the proposed models.
 - (significance/novelty) I fail to find a technical contribution that would be of interest to the machine learning community.
   The PINN modifications are ad-hoc solutions for the equations at hand, and I can't imagine that this general idea has not been applied before.
   For an example of how physical constraints have been embedded in the architecture in the context of hydrology, I can refer to [1], but there are probably many more. The lack of a clear and novel technical contribution limits the impact of the work on the broader machine learning research landscape. The authors should clearly articulate the unique aspects of their approach and highlight its potential advantages over existing methods.

###### References
 - Hoedt et al. (2021). MC-LSTM: Mass-Conserving LSTM. Proceedings of the 38th International Conference on Machine Learning, 139, 4275–4286. http://proceedings.mlr.press/v139/hoedt21a.html

### Questions
1. "However, the ”black box” nature of DNN exhibiting a lack of transparency in their decision-making processes and the significant dependence on extensive training data, limit their use in groundwater research." These are general drawbacks of DNN, are there any unique challenges to groundwater modeling?
2. "Although significant progress has been made in improving groundwater seepage models using PINNs, current models still heavily depend on the adequacy and quality of observed data and remain sensitive to outliers." Are there references supporting this? If these methods have known limitations, why not compare them experimentally?
3. It's better to define $\mu$ and $t$ explicitly in Section 2.1 for clarity. 
4. The study uses randomly generated hydraulic conductivities and source/sink terms to enrich the training data. Is random generation commonly accepted in groundwater modeling, and does it effectively capture real-world scenarios?
5. Do $\phi$ and $\varphi$ represent the same meaning in this paper? Their mixed usage leads to confusion.
6. $H_{EC}$ is not clearly defined, nor is its role in the model explained.
7. Why use $RES$ in section 2 while use $LOSS$ in section 3?
8. Section 4.1 states, "The experiment did not use observations," which conflicts with Section 2.2(4), which introduces observed data constraints. In addition, Section 2.2 is confusing since it introduces multiple terms while it looks like most of them ($RES_{BC}, RES_{IC}, RES_{OC}$) are not used in the experiments.
9. Is there a specific reason for choosing $K=-0.01x+0.8$?

Some minor suggestions:
1. Use proper LaTeX notation for quotes: \`\`example text'' for left and right quotes.
2. Figures 2 and 3 appear nearly identical. Consider combining them into a single figure that highlights the distinctions between PI-RGSM and PI-RGSM-K for conciseness.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This manuscript introduces two PINN-like models for predicting groundwater seepage, a task in hydrogeology.

### Strengths
(significance) automating the analysis of groundwater dynamics seems to be a useful application for machine learning.

### Weaknesses
- (clarity/novelty) The authors claim they introduce self-supervised PINNs, but I fail to comprehend how these models are more self-supervised than the original PINNs.
   The proposed models seem to use have an additional scaling and shift on top of the additional inputs compared to the baseline PINN, but I do not see how this makes these models self-supervised.
 - (novelty) This model fails to cite any relevant related work in the main paper.
   I noticed there is a related work section in the appendix, but that does not suffice.
   During reading I had the impression this is the only paper applying deep learning in the field of hydrogeology, which is obviously not the case.
   Furthermore, the main paper should discuss how the proposed method compares to existing methods.
 - (quality/clarity) I could not find information on how the baseline PINN was trained.
   E.g. section 2.2 mentions the different hyper-parameters in the loss function, but I could not find any information on what hyper-parameters were used or how they were found.
 - (quality) Each model is compared to a single baseline PINN.
   I strongly doubt that there are no stronger baselines to compare against (e.g. regular networks, non-ML methods, ...).
   Furthermore, the performance of the baseline PINN is so poor that it seems as if something went wrong during training (assuming a random model would achieve an R^2 of 0).
   Also, there are no error bars to indicate the consistency of the compared model(s).
 - (significance/novelty) I fail to find a technical contribution that would be of interest to the machine learning community.
   The PINN modifications are ad-hoc solutions for the equations at hand, and I can't imagine that this general idea has not been applied before.
   For an example of how physical constraints have been embedded in the architecture in the context of hydrology, I can refer to (Hoedt et al., 2021), but there are probably many more.

###### References
 - Hoedt et al. (2021). MC-LSTM: Mass-Conserving LSTM. Proceedings of the 38th International Conference on Machine Learning, 139, 4275–4286. http://proceedings.mlr.press/v139/hoedt21a.html

### Questions
1. Why are the proposed models considered self-supervised variants of PINNs?
2. Are there no other possible baselines or models to compare against?
3. How were the hyper-parameters for the baseline PINN tuned?
4. Wouldn't this paper be more interesting to hydrogeologists than to the ML community?

### Soundness
1

### Presentation
1

### Contribution
1
