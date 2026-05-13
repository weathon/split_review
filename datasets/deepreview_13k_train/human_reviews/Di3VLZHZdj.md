# Efficient Fatigue Modeling: Applying Operator Networks for Stress Intensity Factor Prediction and Analysis

- Decision: Reject
- Scores: 3, 3, 5, 5

## Abstract
Fatigue modeling is essential for material-related applications, including design, engineering, manufacturing, and maintenance. Central to fatigue modeling is the computation and analysis of stress intensity factors (SIFs), which model the crack-driving force and are influenced by factors such as geometry, load, crack shape, and crack size. Traditional methods are based on finite element analysis, which is computationally expensive. A common engineering practice is manually constructing handbook (surrogate) solutions, though these are limited when dealing with complex scenarios, such as intricate geometries. In this work, we reformulate SIF computation as an operator learning problem, leveraging recent advancements in data-driven operator networks to enable efficient and accurate predictions. Our results show that, when trained on a relatively small finite element dataset, operator networks --- such as Deep Operator Networks (DeepONet) and Fourier Neural Operators (FNO) --- achieve less than 5\% relative error, significantly outperforming popular handbook solutions. We further demonstrate how these predictions can be integrated into crack growth simulations and used to calculate the probability of failure in small aircraft applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper evaluates the effectiveness of neural operators for the problem of fatigue modeling. Three neural operator learning methods are used, namely FNO, DeepONet, and POD-DeepONet for predicting crack growth on simulated datasets. Results show comparison of neural operator methods with a numerical method considered as ground-truth.

### Strengths
1. Studies an interesting real-world problem with application to a new area of engineering
2. Provides citations to relevant literature in machine learning for fatigue modeling

### Weaknesses
1. Weak comparison with baselines. While the paper mentions several previous works in using machine learning methods such as ANNs in fatigue modeling, none of them have been compared. This makes it hard to evaluate the importance of operator learning methods compared to previous works.
2. It is not clear where the novelty of this paper lies, since they explore applications of known neural operator methods on a new dataset. It will be useful to explicitly state the contributions of this work.
3. Limited complexity of the dataset. The visualizations suggest that the problem involves predicting a single 1D variable that is smoothly varying. More details can be provided on the complexity of tasks considered, and a possible categorization of data samples based on the level of complexity.

### Questions
See weaknesses above.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The work compares the performance of three operator networks in predicting the stress intensity factors in model structures. Based on two sets of finite element datasets on representative plate and holed-specimen geometries, the operator neural network approach outperforms approximate textbook solutions solved from the Newman equations, with very high computational efficiency (0.1 M loading cycles within 0.5 s). The workflow to integrate the calculated stress intensity factors into fatigue crack growth is discussed.

### Strengths
Finite element simulation datasets are created, which allow the assessment of operator neural networks in predicting the stress intensity factor solutions from the finite-geometry linear elastic problems under specific loading conditions. The data-driven computation of stress intensity factors is orders of magnitudes faster than the finite element solvers, which very good accuracy for the different geometries and crack shapes (for plates and holed specimens). The work shows the potential of applying these methods into fatigue performance assessment.

### Weaknesses
The loading conditions is limited to uniform tension. The authors are suggested to explore the performance of predictions under more complex loading conditions such as non-uniform tension and a combination of tension and shear. Similar, it is not clear how the model trained using the datasets constructed in the current work generalizes to specimens and cracks with very different geometries and shapes such as a plate with varying thickness, and a solid with irregular or 3D crack geometries, which are essential if one considers practical applications of these ideas. The detailed parameters and settings of the operator neural network models should be given in the appendix.

### Questions
How does the model trained for the plates apply to the holed specimens, and vice versa? The authors are suggested to introduce quantitative performance metrics when applying the model trained on one geometry to the other, compared to when it's trained on the specific geometry. How do the three operator neural networks compare in terms of computational costs and speeds?

### Soundness
2

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
3

### Summary
The authors use operator networks to predict SIFs with high efficiency and accuracy and can be generalizable to a wide range of geometries and crack shapes. The combination of the FE model and M-integral acts as an operator. The capabilities of models are demonstrated by integrating the learned operator into crack growth simulations and calculating the probability of failure in small aircraft applications.

### Strengths
1. They reformulate the SIF computation as an operator learning problem.

2. The SIFs are predicted with high efficiency and accuracy, which are validated on datasets of surface and corner cracks in plates.

3. The framework can be integrated into crack growth simulations and used to calculate the probability of failure in small aircraft applications.

### Weaknesses
1. The methodological innovation is not prominently highlighted. It seems to be a combination of existing approaches such as FE modeling, operator networks.

2. The details of the method may require further elaboration, such as the process of neural network training and the setting of hyperparameters. Additionally, information on how the training and test datasets were divided, and which crack geometries were used for training versus testing, should be specified.

3. The framework lacks more demonstrative experimental data to verify its feasibility. The dataset, trained through FE models, may have deviations in experimental scenarios compared to the FE models (such as in material constitutive models, geometry, loading conditions, etc.).

### Questions
1. Please further elucidate the methodological innovation. It should not merely be a concatenation of existing methods. 

2. Please add the details of the method, such as the process of neural network training and the setting of hyperparameters. Additionally, information on how the training and test datasets were divided, and which crack geometries were used for training versus testing, should be specified to better evaluate the generalizability of models.

3. Provide examples of the best, worst, and median performance of the proposed machine learning model. Show the prediction of the closest point in the dataset of each of those examples, so that readers understand the quality of the machine learning model.

4. The operator implicitly encapsulates material constitutive relations, loading conditions, etc., within the finite element model. When the method is applied to real-world engineering scenarios with uncertainties compared to the training environment, a discussion on the model’s applicability should be expanded.

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
The paper presents the application of neural operators to enhance fatigue Modeling while maintaining a high level of accuracy. A dataset featuring diverse geometries and crack types is created through finite element (FE) simulations. This data is utilized to develop operators capable of predicting the Stress Intensity Factor (SIF) in near real-time. The effectiveness of these operators is demonstrated in crack growth simulations, achieving significant acceleration compared to traditional FE methods. Additionally, the approach is shown to be more accurate than the handbook solutions commonly employed in the industry.

### Strengths
The paper is well written. Accelerating FE simulations is an important problem in the field of numerical simulations. The need for faster inference is clearly articulated. Neural operators naturally lend themselves to the problem. However, their application is not straightforward. 
The paper presents a very interesting application of neural operators for a practical problem in the industry. The idea of using neural operators for mitigating the repetitive bottlenecks in fatigue modelling looks novel. The methodology is reasonably clear barring few details which seem to be skipped. Claims in the paper are well supported by the results identifying the benefits over conventional methods.

### Weaknesses
A thorough exploration of prior work on fatigue modeling using PINNs, neural networks and machine learning approaches, pointing out their limitations would strengthen the case of this work.  

While this is an interesting engineering application of neural operators, it seems to use only vanilla neural operator frameworks. The details of the modeling effort - architecture used, learning strategies tweaked for this problem, challenges faced during training, hyperparameters selection, loss curves are all missing from the paper. It is very difficult to evaluate the contribution without these details. 

The results look good against conventional handbook methods, but they should also be compared against other ML approaches - PINNs, neural networks, ML methods. 

Is there any validation for probability of failure with real life data? If yes, that should be added as well. 

The ground truth in Figures 4,5,6 is very hard to see. Suggest changing the symbol/colour/font size to make it easy to comprehend.

### Questions
Is it possible to use neural operators for capturing entire transient fatigue modeling? Instead of switching between crack growth calculation and SFI prediction. What would be the challenges in this?  

What challenges do you envisage for operator learning when loading conditions and material properties change?

What about performance on new out-of-distribution scenarios? How about using physics equations as a constraint while building these operators? As an example, can something similar be done within neural operator framework - https://www.sciencedirect.com/science/article/abs/pii/S0167844224004671?via%3Dihub

### Soundness
2

### Presentation
3

### Contribution
3
