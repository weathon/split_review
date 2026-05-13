# Physics-Assisted and Topology-Informed Deep Learning for Weather Prediction

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
Weather prediction is crucial for decision-making in various social and economic sectors. The classical numerical weather prediction methods cannot incorporate the historical observations to enhance the underlying physical models, whereas the existing data-driven, deep learning-based weather prediction methods disregard either the $\textbf{physics}$ of the weather evolution or the $\textbf{topology}$ of the Earth's surface. In light of these disadvantages, we develop PASSAT, a novel Physics-ASSisted And Topology-informed deep learning model for weather prediction. PASSAT attributes the weather evolution to two key factors: (i) the advection process that can be characterized by the advection equation and the Navier-Stokes equation; (ii) the Earth-atmosphere interaction that is difficult to both model and calculate. PASSAT also takes the topology of the Earth's surface into consideration, other than simply treating it as a plane. Therefore, PASSAT numerically solves the advection equation and the Navier-Stokes equation on the spherical manifold, utilizes a spherical graph neural network to capture the Earth-atmosphere interaction, and generates the initial velocity fields that are critical to solving the advection equation from the same spherical graph neural network. These building blocks constitute a deep learning-based, $\textbf{physics-assisted}$ and $\textbf{topology-informed}$ weather prediction model. In the $5.625^\circ$-resolution ERA5 data set, PASSAT outperforms both the state-of-the-art deep learning-based weather prediction models and the operational numerical weather prediction model IFS T42.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces PASSAT (Physics-ASSisted And Topology-informed), a deep learning model designed to improve weather prediction by integrating physical and topological information. PASSAT combines physics-driven PDEs (such as the advection and Navier-Stokes equations) with a spherical graph neural network (Spherical GNN) that leverages Earth’s topology. Experiments on the ERA5 dataset demonstrate that PASSAT outperforms several state-of-the-art weather forecasting models, including FourCastNet, Pangu, and GraphCast.

### Strengths
The model demonstrates superior performance on the ERA5 dataset compared to leading weather forecasting models.

### Weaknesses
1. The architecture of PASSAT, particularly the internal workings of the spherical GNN and the interaction between the “interaction branch” and “velocity branch,” is not sufficiently detailed. A more detailed architectural diagram and step-by-step explanation would make the model’s structure and operation easier to understand and potentially reproduce. Specifically, the paper lacks clarity on how the spherical GNN processes input data, what specific operations are performed within each layer, and how the outputs of the backbone model are utilized by the two branch models. The description should include the dimensionality of tensors at each stage and the specific mathematical operations involved in the message passing and aggregation steps of the GNN.

2. The combination of a spherical GNN and Navier-Stokes equations implies high computational demands. The paper does not provide benchmarks for computational efficiency, which is crucial for real-world applications. This includes not only training time but also inference time, memory usage, and the number of parameters in the model. A detailed analysis of the computational cost, including a breakdown of the time spent in different parts of the model (e.g., GNN computations vs. PDE solving), is necessary to assess the practical viability of the approach.

3. The benchmarks should include the SOTA Numerical Weather Prediction (NWP) models, which are the industry standard for accuracy and robustness in weather forecasting. The absence of a comparison against operational NWP models like the Integrated Forecasting System (IFS) limits the ability to evaluate the practical relevance of PASSAT. It is crucial to demonstrate that the proposed method can compete with or outperform these established models, which have been rigorously tested and refined over many years.

4. While Navier-Stokes equations are employed to capture fluid dynamics on a global scale, the work does not clarify how it manages varying boundary conditions across different geographical or atmospheric regions. The paper should address how the model handles the complex interplay of land-sea boundaries, orographic features, and varying atmospheric conditions, which can significantly impact fluid dynamics. The treatment of boundary conditions, particularly at the edges of the computational domain and at different pressure levels, needs to be explicitly described.

5. **(Major concern)** Although the paper employs the Navier-Stokes (NS) equations for physical realism, it does not provide a theoretical justification for their selection over other possible fluid dynamics models. Moreover, it is unclear how PASSAT addresses the variability and abrupt changes often observed in real-world data, which may not always align with the idealized assumptions of the NS framework. For instance, sudden atmospheric shifts and noise present in observational data could challenge the applicability and robustness of the NS-based approach in capturing highly dynamic or turbulent weather events. The paper should discuss the limitations of using incompressible NS equations, especially when dealing with compressible atmospheric flows, and justify why this simplification is appropriate for the intended application.

### Questions
See weakness.

### Soundness
3

### Presentation
2

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
This paper introduces PASSAT, a physics-assisted and topology-informed deep learning model designed for weather forecasting. PASSAT employs a graph neural network to anticipate the velocity field associated with interaction and advection processes, followed by the application of numerical methods forecast the velocity field and other variables using the advection equation and the Navier-Stokes equation, respectively.

### Strengths
PASSAT incorporates the physical processes inherent in weather forecasting. It also addresses the discrepancies between the differences between equiangular observations from ERA5 data and planer expansion typically assumed in the existing models, offering a more accurate representation for the real world.

### Weaknesses
1. The experiment only utilized T2m, 10u, 10v, Z500, T850 from ERA5 as input and target variables, leading to two major problems:
   - These variables are not at the same altitude, which impedes the accurate application of the Navier-Stokes equation to velocity and temperature observations at varying heights. Specifically, the Navier-Stokes equations, in their typical form, require co-located velocity and temperature fields to accurately model the momentum and energy transport. Applying these equations to variables at different pressure levels introduces significant approximation errors, potentially explaining the lack of improvement observed in the ablation study. The model's attempt to reconcile these disparate vertical levels through a graph neural network may not fully capture the complex inter-level dynamics, leading to inaccurate physical modeling. The ablation experiment further indicated that introducing the Navier-Stokes equation did not significantly improve the prediction.
   - Regarding the incorporation of temperature, existing methods of embedding physical equations such as NeuralGCM[1] consider the thermal dynamics introduced by temperature variations and employ the more commonly accepted primitive equations for physical modeling. The current approach appears to only use temperature as an input feature, without explicitly modeling its evolution through thermodynamic equations, which is a significant limitation compared to more comprehensive physics-informed models.
2. The author only used 13 years of ERA5 data with a spatial resolution of 5.625° for their experiment, which is a relatively simple prediction task. This resolution is quite coarse, and the limited temporal span might not adequately capture the full range of weather phenomena. It is recommended that the authors use the highest resolution data of 1.40625° available in WeatherBench to enrich their dataset. Furthermore, the use of a longer time series would allow for more robust training and evaluation, potentially revealing the model's limitations under more extreme or less frequent weather conditions.
3. When compared to GraphCast, the proposed method hdemonstrated a marginal improvement of approximately 1%. In the ablation experiment, the inclusion of Navier-Stokes equations and advection equations resulted in only a modest  performance promotion, which does not validate the effectiveness of the author's design. The lack of substantial improvement suggests that the model's architecture or training process may not be effectively leveraging the incorporated physical constraints. The marginal gains, especially given the increased complexity of the model, raise questions about the practical utility of the proposed approach.

### Questions
See weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new deep learning model PASSAT (Physics-ASSisted And Topology-informed) for weather prediction tasks. It first attributes the weather evolution to two major factors which are the advection process (characterized by the advection equation and the Navier-Stokes equation) and the Earth-atmosphere interaction. PASSAT works by training a spherical graph neural network to estimate interactions between the Earth and atmosphere and use it to create initial velocity fields. It also solves the advection equation on the sphere and update velocity fields by solving the Navier-Stokes equation on the sphere. With this certain methods, PASSAT reduces the uncertainty brought by cumulative errors to mid-term forecasts and increase forecast accuracy. Experiments show that PASSAT outperforms existing deep learning and traditional numerical weather prediction models on the ERA5 dataset, especially in terms of stability and accuracy of medium-term forecasts.

### Strengths
1. Combining physical and data-driven methods at the same time: PASSAT model uses both physical equations (convection equations and Navier-Stokes equations) and deep learning method (spherical graph neural network) to make the prediction results more accurate, robust and more interpretable, and reduces the cost as well as the model uncertainty compared to purely data-driven methods.

2. Considering the spherical topology: The model innovatively designs a spherical graph neural network to perform calculations on the sphere, avoiding the errors caused by using plane projection, which improves the accuracy of global weather forecasts.

3.The experimental verification effect is significant: Experimental results on the ERA5 data set show that the PASSAT model surpasses many current advanced models in medium-term weather prediction under similar parameter quantities, demonstrating its potential in practical applications.

### Weaknesses
1. The author's choice of the number of variables is not good enough. Although the author mentioned this shortcoming, it cannot be ignored. For example, FourCastNet predicts 20 climate variables at the same time. Predicting multiple variables at the same time will inevitably have a certain impact on the performance of the model. How does the author view this impact?

2. Due to the timeliness of climate prediction, the training time and inference time of the model are also very important evaluation indicators. The author mentioned that PASSAT has the characteristic of less computational complexity. Can you give a specific comparison of training time and inference time?

3. The author mentioned "To be specific, we no longer trust the velocity field v estimated by the velocity branch of the spherical graph neural network, except for the initial time t. Instead, we solve the Navier-Stokes equation that governs the evolution of the velocity field, to calculate v." So how exactly does the author "no longer trust the velocity field v"?

4. An extra ablation experiment can be designed to further demonstrate the difference between using a spherical graph neural network and a normal planar graph neural network.

5. Appendix E mentions how the authors compressed the baseline model, but the authors need to provide more detailed evidence to prove that such compression is reasonable and fair, especially for baselines such as GraphCast and Pangu whose original model parameters are relatively large.

### Questions
For the questions, please see the weakness section. If you can answer my question, I will improve my rating.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper describes a hybrid deep-learning and physics-based weather forecasting model. The authors combine the numerical solving of the advection and Navier-stokes equations with tendencies predicted by a neural network. Both components are tailored to respect the spherical geometry of earth, by adapting the physical equations accordingly and by using a spherical graph neural network for the deep learning component. Experiments are conducted on 5.625 degree ERA5 data. The proposed model shows RMSE values lower than baseline deep learning and hybrid models that do not respect the spherical geometry, and comparable values to the graph-based GraphCast* model.

### Strengths
1. Building hybrid deep-learning and physics-based models for the atmosphere is a highly interesting area of research, and if such models show new capabilities they can have a big impact.
2. The idea of using both the advection equation and Navier-stokes in a hybrid model like this is novel, and shows a way to take one step further in the physics direction than e.g. the ClimODE model.
3. The authors have accurately identified that many deep learning weather models do not properly handle the spherical geometry of earth. In the proposed model this is remedied in a satisfying way both in the physics equations and in the deep learning component of the model.
4. The authors experimentally compare against a relevant set of baseline models in a fair setup. The proposed PASSAT model shows strong performance over models not considering the spherical geometry.

### Weaknesses
 **Major**:
1. My biggest doubt about this work is about the role of the physics part in the hybrid model. Looking at table 2, the version of the model w/o Navier-Stokes achieves similar or even better results. Going even further, the version of the model without the physics-component (last column, pure GNN) shows only slightly worse RMSE values than the full PASSAT model. Crucially, this pure GNN version still substantially outperforms all baselines except GraphCast*. The conclusion to draw from this is that the most important part of the model seems to be the GNN, and the authors have mainly developed a very good GNN model, rather than a model that crucially relies on the physics equations. This could of course be a contribution in itself, but is not the focus of the paper as is. There is furthermore very little description of how this GNN component of the model works, which is a shame given how important it seems to be experimentally. The framing of the paper could be changed to highlight more this contribution, but that would change the shape of the paper enough that it would warrant a resubmission.
2. The authors write in the list of contributions that "PASSAT ... remarkably improves the stability of medium-term prediction". There are no experiments to back this up. Stability is mentioned also in section 3.5, but there is no investigation of the stability of the model. The existing experiments are conducted up to 5 days, while most deep learning weather models are stable to roll out up to 10 days or beyond, so there is no support for this being an improvement in stability. Explicit experiments on how stable the different models are for long rollouts could shed some light on this. 
3. I am missing important related work, that should be discussed:
  * ML Weather models handling the spherical geometry: (Bonev et al., 2023), (Esteves et al., 2023)
  * Graph-based models: (Keisler, 2022), (Lam er al., 2023), (Oskarsson et al., 2024), (Lang et al., 2024). Given that the deep learning component of the model is a GNN, I would expect some mention of existing graph-based approaches and discussion about how the model relates. Lam et al. (2023) is mentioned heavily throughout the paper, but I miss a proper discussion about how the GNN used in PASSAT relates to GraphCast. 
4. The proposed model shows similar performance to the GraphCast* model. GraphCast has been reimplemented for this study, which is completely fair, but I wonder how close GraphCast* follows the original GraphCast model? In Table. 5 the number of nodes in GraphCast* is listed as 4096, which is 2 * 2048 (the number of grid points in the data). I don't see how you would arrive at this by summing the 2048 grid nodes with nodes in a multi-scale mesh graph constructed as described by Lam et al. (2023). If the graph used by GraphCast* in the paper is not such a icosahedral multi-scale graph this does not seem like a fair representation of the GraphCast model. This becomes important as GraphCast is the closest baseline competitor to the proposed method. I would appreciate if the authors could clarify this. 
5. The motivation for introducing the Navier-stokes equations is unclear. This is motivated by the GNN predictions leading to error accumulation, but would not heavy error accumulation be remedied by the rollout training scheme being used?

**Minor** (not important for my final rating):
1. When discussing the importance of considering the spherical geometry, it would be a stronger argument to point to explicit problems in existing models that do not, rather than only conceptual issues. An argument can be made that flexible deep learning models can learn to correct for the problems caused by disregarding the geometry. See for example how Pangu still provides physical predictions close to the poles. An example of this not working out can be found in Bonev et al. (2023), and the discussion there is an example of a more concrete motivation for considering the geometry.
2. While I agree that existing models do not respect earth's *topology*, the fact that the earth is a sphere is even an aspect of *geometry*. I think this would be a better terminology to use.
3. The paper discusses the role of the deep learning component as modeling the earth-atmosphere interactions. I interpret earth-atmosphere interactions as interaction between the earth's surface and the atmosphere just above it. In reality, this second component of the model seems to take the role of parametrizations of all kinds of unresolved processes happening on sub-grid scales. The terminology and exact meaning of earth-atmosphere interactions should be clarified.
4. The authors write (about pure deep learning models): "Thus, their predictions are often unreliable due to the lack of the physical constraints or suffer from the distortions caused by the topological structure". I would argue that this is not an accurate statement for modern deep learning weather models, that tend to be reliably quite accurate and stable. The citation given to back this statement up is (Schultz et al., 2021), which is an earlier work than almost every single deep learning model discussed in the rest of this paper.
5. Sections 1.1 and 1.2 read as related work subsections, and would feel more at home as part of that section. 
6. As opposed to what is written in the paper, GraphCast, Pangu and NeuralGCM have provided open code. Now there might be other good reasons to reimplement these for this study, but this should be clarified.

### Questions
1. Comparing the continuity equation used in ClimODE with the advection equation used here, the difference seems to be that you exclude the compression part. This should correspond to an assumption that the flow is incompressible. What is the motivation for this choice? Is this well-motivated for the earth's atmosphere?
2. Is my understanding correct that all equations (advection and Navier Stokes) are applied to each weather variable $u$ independently, and all interactions between them happen in the deep learning component? How can one then think of the u and v wind components? Is it reasonable to assume that these independently follow the advection equation? Not being an expert on these physical equations, my intuition would rather be that the wind components would have a close connection to the actual transport of at least the geopotential field. Could you comment on this? 
3. In algorithm 1 you introduce a $\lambda$ that controls the update of the velocity field. With the value given, only $\frac{1}{60}$ weight is given to the updated value from Navier Stokes. The motivation given for this is to ensure stability. Could you expand on this choice? Is there a physical motivation for this? It seems like this could be one reason why the introduction of Navier Stokes has very little impact in the ablation study.

### Soundness
2

### Presentation
2

### Contribution
3
