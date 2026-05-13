# Mitigating Time Discretization Challenges with WeatherODE: A Sandwich Physics-Driven Neural ODE for Weather Forecasting

- Decision: Reject
- Scores: 3, 1, 5, 6, 3

## Abstract
In the field of weather forecasting, traditional models often grapple with discretization errors and time-dependent source discrepancies, which limit their predictive performance. In this paper, we present WeatherODE, a novel one-stage, physics-driven ordinary differential equation (ODE) model designed to enhance weather forecasting accuracy. By leveraging wave equation theory and integrating a time-dependent source model, WeatherODE effectively addresses the challenges associated with time-discretization error and dynamic atmospheric processes. Moreover, we design a CNN-ViT-CNN sandwich structure, facilitating efficient learning dynamics tailored for distinct yet interrelated tasks with varying optimization biases in advection equation estimation. Through rigorous experiments, WeatherODE demonstrates superior performance in both global and regional weather forecasting tasks, outperforming recent state-of-the-art approaches by significant margins of over 40.0\% and 31.8\% in root mean square error (RMSE), respectively.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper is related to weather modeling on a 5.625° resolution using ERA-5 data as target. The solution is based on the NeuralODE model with several new features inside. A CNN-ViT-CNN sandwich architecture is proposed to model the right term of the ODE. The authors claim a strong improvement in simulation quality over the alternative approaches. Such an improvement is attributed to new scheme of velocity derivatives estimation based on the wave equation and to the CNN-based approximation of a source term in the advection equation

### Strengths
* An interesting wave-equation inspired model to capture time derivative of velocity
* Comparison with several baselines showing better results of a proposed model
* Ability to interpolate in time and produce a continuous dynamics
* Ablation studies for the velocity derivative approximation and model architecture

### Weaknesses
 * The CNN used in variable space scale loses part of its physical meaning
* The wave equation doesn’t describe the atmospheric dynamics really well so the derivative approximation is not governed by physics
* The model has low practical applicability
Probably an interesting experiment will be to use the model in the autoregressive mode and to assess its quality for longer forecast horizons. The same can be done for regional models to assess the borders influence.

### Questions
* How the model will perform on poles where the horizontal resolution is very different from the equator?
* Do your CNN implementation consider the discontinuity in latitudes (360=0)?
* The border influences much the model during regional forecasts. How do you handle this problem? (if wind velocity is 100 km/h, in 24 hours it will travel 2400 km)
* How your model can be used in practice? Consider that ERA-5 dataset is not available operationally.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper introduces a sandwich method whereby the atmospheric dynamics is represented by a simplified advection differentials and the components are separately learned (e.g., source, advection, initial condition) with a parameterized deep models, depending on whether they possess fast or slow convergence.

### Strengths
Building physics-informed network for chaotic systems, such as weather dynamics, is crucial and this paper offers an interesting ODE-based approach to tackle the problem.

### Weaknesses
Let me start off by saying that using an advection equation is only valid under __very simplified scenario__, and weather dynamics is definitely not the case at all. Elaborations to follow:

1. The paper assumes incompressible fluid, where fluid density remains static along the pressure level. This is a gross simplification and is unphysical as the weather dynamics is completely dependent on the fluid being compressible, to allow interesting processes to take place such as convection through buoyancy (cloud formation, precipitation, energy-water cycling), large-scale fluid motion (teleconnection), turbulence (boundary-layer interaction), etc. This very assumption, therefore, does not allow for many atmospheric phenomena, including but not limited to extreme events (ENSO, hurricanes, etc), or just the general circulation of the atmosphere. This is not including the paper's simplification of ignoring the spherical nature of the Earth that enables for a different set of dynamics enabled by e.g., coriolis force.

2. The paper also ignores many important conservation constraints found in the classical dynamical core, such as the conservation of mass, energy, and momentum. Specifically, the lack of explicit conservation of energy is particularly concerning, as it is crucial for maintaining the stability and physical realism of the simulation. The advection equation, by itself, does not guarantee energy conservation, and the neural network component could introduce further non-physical sources or sinks of energy, leading to unrealistic behavior over longer time scales.

3. As such, there are better approximation to the full Navier-Stokes equation, such as Shallow Water Equation or Quasi-Geostrophic flow, that attempts to capture some of the realism of the atmosphere, and is therefore a much better differentials than the advection equation. The Shallow Water Equations, for example, while still simplified, at least account for the vertical integration of the flow and allow for the representation of gravity waves, which are crucial for the propagation of weather systems. Similarly, Quasi-Geostrophic equations capture the large-scale dynamics of the atmosphere, including the effects of the Earth's rotation, which are completely absent in the advection equation.

Regardless, there are additional weaknesses that warrant a reject rating:

4. The limited number of variables used (5), coarse spatial resolution (5.625-degree vs 0.25; ~400x smaller horizontal resolution), and small forecasting lead-time (72-hour) are too unconvincing to test this Neural ODE formulation for real weather application. I suspect that given the gross oversimplification through the advection equation, the framework could not accurately evolve the full atmospheric state with significant vertical motion/interaction, and is therefore not useful in a short forecasting window, let alone over a longer rollout in the medium-weather and longer sub-seasonal scale. The coarse resolution also limits the ability to capture small-scale features and processes, such as fronts and convective systems, which are essential for accurate weather prediction. The choice of only 5 variables further restricts the model's ability to represent the complex interactions between different atmospheric components.

5.  This is echoed by the result in Appendix E Table 9 is inferior to ClimaX at 3-day lead time, with error growth much larger than the other model (also lacking IFS baseline here to see how the rate of error propagation). The ACC for for u10, for instance, deteriorates from 0.93 to 0.80 even at 36-hour difference! The fundamental error in the assumptions (which ClimODE is too, and the authors should therefore use stronger baselines such as GraphCast) might contribute to this result. The rapid degradation of the ACC score over such a short time frame is a strong indicator of the model's inability to capture the underlying dynamics accurately. The lack of an IFS baseline makes it difficult to assess the model's performance relative to a well-established numerical weather prediction system.

### Questions
Similar as the weaknesses.

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
This paper introduces WeatherODE, a novel weather forecasting model based on deep learning. Building on the recent ClimODE model, WeatherODE follows a similar methodology and models the evolution of atmospheric quantities through a learnable advection equation. In this framework, the authors propose new architectures for learning the advection equation. A CNN-based neural network is used to predict the initial velocity of the equation, leveraging insights from the wave equation, rather than relying on time discretization. Additionally, a Vision Transformer-based neural ODE is trained to model the evolution of velocity over time. Finally, a CNN-based neural network is introduced to learn the source term of the advection equation, aiming to reduce the propagation of numerical errors. The paper provides detailed information on the training process of this new architecture, along with extensive experiments comparing WeatherODE to several state-of-the-art baselines across global and regional weather forecasting tasks with varying lead times. Ablation studies on the model's architecture are also included.

### Strengths
The paper is well organized with a clear structure and informative figures and tables. The experimental work is extensive and technically well-documented.

Incorporating a strong physical bias into learning models is of great importance, especially for climate-related problems where the chaotic nature of underlying physical processes can cause the system to deviate from the training distribution. The inclusion of physical priors is essential for ensuring that the model generalizes well.

The proposed method outperforms the other models by a significant amount, in both global and regional forecasts.

The proposed method significantly outperforms the baselines, demonstrating improvements in both global and regional forecasting tasks.

Ablation studies, accompanied by illustrative explanations of the core contributions, are provided. The paper, in particular, demonstrates the effect of time discretization and how the proposed architecture mitigates this issue, offering comparisons to previous methods.

The discussion on the convergence speed of various learning models is first introduced qualitatively in Section 3.3 and then quantified in Section 5.3, which offers valuable insights into the architecture's design choices.

Although briefly mentioned, the paper also proposes a flexible inference model capable of producing forecasts for different lead times. The ability to make weather predictions at varying lead times is a significant advantage and a promising idea.

### Weaknesses
Despite the solid experimental results, I believe that the paper's explanation of the methodology lacks some clarity, context, and references. While the proposed architecture achieves strong performance, the scientific reasoning behind these improvements is somewhat incomplete.

First, the authors claim that all physical variables follow an advection equation, which is learned. This assumption, initially made in the ClimODE model, forms the foundation of the WeatherODE architecture and is said to provide a strong physical bias. It would be beneficial if the paper provided more physical context regarding the advection equation and why it serves as a good prior for learning atmospheric dynamics. From a physical perspective, what are the consequences of assuming that all variables follow this equation with a learned velocity field? Can the authors connect this to known atmospheric processes?


#### Section 3.1

There is some lack of clarity in the discussion of discretization between lines 192 and 204, particularly around Equation (3). It is unclear at which stage the ODE is being discretized. The problem of learning an ODE's flow using neural ODEs should, in theory, be independent of the discretization, as neural ODEs are designed to differentiate through the ODE in a solver-agnostic way.  Second, indices $t_0$ and $t_n$ seem to play the same role.  It would be clearer if a single notation were used for the initial condition, even if this involves only one discretization step, with the methodology then being extended to subsequent steps.

####  Section 3.2

This section focuses on predicting the initial velocity $v(t_0)$. The authors provide physical insight on the computation of the state derivative $\partial u/ \partial t$. However, the link between the two quantities $v(t_0)$ and $\partial u / \partial t$ is not explicitly stated. Yet it is one of the paper's main objectives to improve the computation of the $v$ as a function of the state $u$, without resorting to time discretization. Indeed, it is stated that $v$ is estimated from $u$ in the ClimODE paper using time discretization, but the estimation is never mentioned. As a result, the section presents a new method based on the wave equation to estimate state derivatives, but the connection with the ultimate problem of estimating the velocity is missing. This omission impairs the clarity of the paper, as this step is one of the core contribution.
I understand that the estimation method is framed as a variational inverse problem in the ClimODE paper, and that WeatherODE improves it by casting it as a learning problem instead. I believe that it should be stated in this paper as well for Section 3.2 to be relevant.

Additionally, the link between the wave equation and the advection equation is not clearly explained. The authors mention that the wave equation is commonly used in atmospheric dynamics, but they do not provide any references or detailed physical context. While the wave equation is indeed important in describing physical processes related to propagation, further clarification is needed regarding its purpose in this model.

If I understood correctly, the integrated wave equation (5) seems to show that the first-order derivative of the state $\partial u / \partial t (t_0)$ is linked to the state gradients $\nabla u(t_0)$, which motivates predicting the velocity field should as a function of the state gradients rather than the state itself. However, assuming that the wave equation holds, the involved spatial derivatives are of second order rather than first order, and are integrated over a past time interval rather than evaluated only at the current time $t_0$. In my opinion, and if I understood correctly, equation (5) may not be entirely appropriate for predicting $v(t_0)$ as described.

This concern is compounded by the results of Figure 3, where the performance gap between the proposed method using the wave equation and other approximators is quite small. Couldn't it be that the performance gap comes from learning the initial velocity from a neural network conditioned on non-discretized state values instead of solving an inverse problem with discretized state derivatives, rather than from the wave equation-informed predictive structure of the neural network? 

Finally, the qualitative argument about spatial resolution at the end of this section is not particularly convincing, as it compares spatial resolution to time resolution in a way that seems dimensionally inconsistent. The statement on line 243,
``
the spatial domain is nearly 100 times denser than the temporal domain.
``

needs further clarification, as its implications are unclear.

### Questions
Neural ODEs are known to be computationally demanding, yet the paper does not address computational resources or the back-propagation method used to train the neural ODE. Since computational power can often be a limiting factor, it would be valuable to compare the computational times across the different architectures, particularly for the neural ODE versus other feedforward models.

The WeatherODE* model appears to be an interesting research direction, offering flexibility in generating forecasts at different lead times. However, there is limited explanation as to why WeatherODE is capable of such flexibility. Could the authors clarify the connection between the following sentence:

``
by modeling the atmosphere as a physics-driven continuous process anddesigning a time-dependent source network to account for errors at each time step, WeatherODE can capture information across all intermediate time points
``

 and the success of the 24-hour model WeatherODE*?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The study proposes a neural ODE approach to data-driven NWP by using three different neural nets with three different rates of convergence to solve for three different terms in the system of ODEs obtained by applying the method of lines to the advection continuity equation. The three models correspond to (a) solving for the initial velocity estimate using the wave equation, (b) an advection model to compute the tendency of the velocity, and (c) to estimate the source term in the momentum equation. Respectively, a 2D CNN, a vision transformer and a 3D CNN is used to estimate the three terms which are then used to march the variables in time.

The model is compared with multiple other AI NWP models and this approach is found to substantialy reduce prediction errors in both global and regional contexts mst likely by reducing the errors in the estimation of the time derivative of velocities which might be quite erroneous due to a large (hourly) time step.

The ultimate approach is to the create a "sandwich"  physics driven ODE which uses the three architectures together to predict the future state of the atmosphere.

### Strengths
The experimental setup is robust and it is nice to see the significant improvements in performance across all variables for the neural ODE sandwich architecture. The paper is well written and the hybrid approach in the paper could likely be valuable to the AI NWP community.

I like the paper for its skillful approach of blending classical PDE theory with AI to improve errors in atmospheric state forecasting.

### Weaknesses
1) I don't think ClimaX is a good baseline for such comparisons, as it was itself trained on a wide range of CMIP6 models which are (a) not really tuned for weather forecasting and (b) due to model design have multiple biases. Finetuning can only fix so many of them. Thus, I would not put too much weight into how the WeatherODE performs against ClimaX as it is a weak baseline to begin with. Similarly, I would recommend comparing the method with the newer version of FourCastNet based on the SFNO architecture which is more stable for short and long term rollouts and is more topology-aware.

2) A minor point but the paper tends to over-cite at places: the Evans (2022) reference, the Vaswani et al reference and the Biswas et al. (2013) reference are totally unnecessary. Vaswani et al. has not even been cited in the correct context as it has not realtion to weather forecasting. Similarly on Line 37-38.

3) The figures' text could be increased. It is tough to interpret Figures 1 and 4 in print.

4) It would have been interesting to see the time complexity of the sandwich model proposed in the study and how it compares with other models. Current AI weather forecasting models have been a bit over-glorified in a sense that they ignore baroclinic motions in the atmosphere and use data on very few vertical levels, and then claim to be as good as traditional NWP models - which are way more versatile thab AI NWPs in the problems they can be used to solve. Understandably, the only advantage then is the computational speed and the reduction in operational cost that they offer. Therefore, as more traditional numerical are embedded into pure data-driven architectures, it would be interesting to see the effect on more complicated hybrid architectures on the run speed.

5) If the refined horizontal resolution is the key here (as it allows computing spatial gradients accurately), they can simply using higher spatial resolution training data (like 25 km x 25 km ERA5 data) lead to similar improvements in performance?

6) One worry is that the achitecture is becoming too combersome to be practical: a unified model structure for past AI NWP models is one of the key cornerstones of its appeal. Traditional NWP model provide forecasts at a 9 km resolution. If the same models were to be run at 5.625 deg resolution, one can expect similar order run times between AI weather emulators and NWP models, ultimately leading one to question the central point of these models. So, having multiple ML models in sequence, such as those proposed in this study, can increase the complexity of the problem to the point that one begins to question the novelty of this approach. What would have been great could be to train one single neural net on atmospheric data sampled at a high frquency and use that for more accurate initializations.

7) If i undestand correctly, the study employs a two dimensional equation. Have the authors considered using a three dimensional equation instead which considers the vertical verlocity into account as well? This could be important especially for tropical predictability ad thermodynamical processes like dry and moist convection evolve over sub-hourly timescales and can introduce notable errors into the equation. This could also affect longer lead time rollouts of the model. Or, if I undertand it correctly, the vertical velocity is simply treated within the source term (which might not be the best approach).

8) Source term: If I understand correctly, and I could be wrong, the source model tend to learn all the other forcing terms of the advection equation. In the context of ERA5, this would not just contain other forcings, but also data assimilation errors. Since the DA errors are not bery systematics in nature, how can errors in predicting the terms influence the u_t+1 prediction obtained from the neural ODEs?

5) "While NWP provides solutions based on human-defined ODEs, we believe these models may not fully capture the complexities or imperfections of the real world."

I disagree with the authors here when they claim that NWP models can not capture the complexities of the real world but the data-driven methods can. I must remind them that the data-driven models (a) are trained on datasets created by these equations-driven traditional NWP models (along with observations) and (b) employ a simplified form of same equations for hybrid modeling. The only benefit AI-driven weather emulators have delivered on till date is speed. None of the models have systematically beaten IFS. Moreover, when integrated at a high-enough resolution, NWP models (without assimilation) can still be maintained physics-fidelity over longer periods of time than the state-of-the-art data driven models. It has become a fashion to bash traditional NWP models these days withouth appreciating the heavy amount of physics that goes into their design. Until these data-driven models show significant improvements over IFS after being trained on IFS input itself, alas, such claims about imperfections of the NWP models will remain baseless.

This tradeoff between model complexity and performance and how it contributes towards interpretability is argued in more detail in [1] which provides a comprehensive discussion of the different approaches - purely data-driven to hybrid to pure-physics based, and, simple models to intermediate complexity models to comprehensive weather forecasting and climate prediction model. I highly recommend the authors to atleast acknowledge such tradeoffs between model complexity, realism, and accuracy in the final manuscript as limitations of their approach and connect it to [1] (and other studies).

Also, a complete data-driven approach also leads to reduced interpretability of the model, as is again argued in [1] and multiple other studies. How do you think your approach embeds increased interpretability?

6) Regarding ensemble averaging: no offense but a 0.01 or a 0.02 decrease in RMSE does not equate to much and should not be read much into. A better test would be around case-specific events. If you can show that ensemble methods lead to better predictability around, say, a cyclogenesis events, that would be something. Sorry if this sounds a bit rough, but, I think the AI weather prediction community needs to be reminded every now and then that this is not merely an engineering problem where comparing RMSEs will suffice. What is needed is a set of physically more rigrous tests that demonstrate that these models are physically robust and are capable of being used for meaningful physical analysis.

1) ClimaX operating at 5.625 degree and 1.4 degree resolution is akin to a toy model for weather prediction at best. I reemphasize that predicting the large-scale features at 5.625 degrees with reasonable accuracy is a much easier problem than learning the actual multi-scale dyanamics from data - simplified models like Quasi-geostrophic equations can be used at these resolutions to get reasonbale forecasts as well over 12-24 hr timescales, while taking a fraction of the compute cost at NWP. 

2) Sure, the neural scaling laws can be invoked to surmise that the model will continue to scale with increased resolution, but I still do not see it being independent of the underlying reanalysis. The model will continue to be (a) more computationally intensive, (b) require newer and newer reanalysis datasets, and (c) based on current equations, still not have limited value for long term forecasts. Moreover, increasingly complex equations will be needed to ensure stable rollouts over longer periods - which connects to my next point.

3) Coriolis term? What about other physics on longer time scales? A heavy limitation of your approach is that you will eventually have to embed more complex equations into the hybrid architecture - at which point the architecture might converge to existing models like NeuralGCMs.


4) I am not convinced by the authors' response on the computational complexity. Of course, auto regressive rollouts will be more expensive than single-shot predictions, but if all one is getting from the (arguably more-complex) hybrid approach is marginal improvements over 6-24 hour timescales, that barely has any significant utility because pure-data driven models are relatively easier to train, and the auto-regressive rollout issue can be circumvented for medium-range timescales, as has recently been done with the weather and climate foundation model Prithvi wxc (if i understand correctly).

### Questions
Questions are combined with weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper extends a recent neural weather ODE model (ClimODE 2024) by using wave-equations for initial state estimation, adopting a more transformer based dynamics, and adding a CNN source field. The contributions range from incremental (transformers) to substantial (source field). The results are outstanding.

------

Post-response update. I'm decreasing the score to reject, which I understand is exceptional given my initial positive review. The authors have not been able to clarify or address my concerns regarding the role of the source term, and the role of wave term in the advective system. I believe using the wave term is unfounded in an advective system, while the source term seems not to be part of the PDE afterall (given that source gets as input future states), which violates eq 1. The paper is not ready for publication.

### Strengths
- The paper extends weather ODEs in sensible ways, and the overall model is sensible. Adding the source field is a major contribution, while the initial estimation and network searches seem useful (but more incremental).
- The results are outstanding: they even beat IFS at times, which is an outstanding achievement!

### Weaknesses
 - The motivations behind the model choices seem a bit weak
- The ablations are very interesting, but have some issues. In the v0 ablation there is no ClimODE baseline, so it’s difficult to say if any improvement was actually gained here. The Fig4 is superficial and difficult to interpret. The stability analysis seems interesting, but I don’t think it provides much insights into why things sometimes fail. One would not really expect such a simple ODE system to fail in the first place.
- The experiments make an unfair comparison to the ClimODE baseline, where ClimODE uses 5 data variables and weatherODE 48. Results lack standard deviations. Some results show that weatherODE beats IFS, and this is not elaborated further. This is a major achievement, and is now provided a bit too casually. There should be some discussion on how the results relate to the larger model (panguweather, gencast, graphcast, etc).
- The clarity and text needs improvements.

- I have hard time understanding the v0 estimation. First, a wave equation is introduced in general terms, and then a CNN appears. These two are not connected together, so I’m left wondering what do we do with the waves, and how do they relate to the CNN. Furthermore, the wave equation is poorly motivated, and it seems disconnected from the advection equation 3. To me this looks like a discrepancy: the system follows advection, but initial state assumes different kind of physics (ie. laplacians appear out of nowhere). Surely the initial state estimation needs to respect the chosen ODE model, and not introduce some physics effects that are not part of the ODE.
- The arguments about spatial vs temporal resolution are not convincing. Low temporal sampling rate does not necessarily mean that the temporal resolution is low: this depends on how quickly the process varies. It also feels misguided to say that spatial resolution is 100x higher than temporal resolution: this is only true if you take 32*64, and I don’t think you should do this. Since the (t,x,y) axes have similar ranges (24,32,64), I would argue that there is no resolution gap in the sampling rate between space and time.
- I couldn’t follow the CNN/ViT convergence arguments. I’m not sure what convergence even means here (of training..?, of rollouts..?). I think the paper is arguing that training CNNs is somehow instable, and thus ViT’s have to be used. This sounds implausible, and a poor motivation for choosing how the dynamics should evolve. Surely the networks need to be chosen such that they respect some physical system properties (eg. feature locality/globality).
- I don’t understand the source model. It takes as input all 1…N simulated states u(t_n), but one needs the source states s(t_n) to do this simulation. This has to be a mistake: I assume that we instead take as inputs u(t_1 : t_n), so that the history grows along the ODE rollouts. How do you handle set inputs and set outputs? I don’t think a 3D CNN supports sets as inputs or outputs [maybe these are not sets, but just tensors of fixed size..].
- At sec 3.5. I’m again confused what do you mean by “convergence”.
- Sec 3.5. claims that advection dynamics involves long-range dependencies. I’m not sure I agree, and would even argue the opposite. PDE’s are by nature local models: why would the weather in new york affect the infinitesimal change of weather in london? There is no connection between them. Can you elaborate?
- Sec 3.6. claims that earlier methods only train against final state, and ignore intermediate terms. I’m surprised by this statement. ClimODE trains with all intermediate points, as does the original neural ODE, and every other neural ODE/PDE model I’ve seen. Can you provide examples of models where this happens? Calling this “multi-task” learning is also wrong: intermediate points in an ODE are not different “tasks” (they are not even a single repeated task, since it’s not a “task” in the first place).
- The benchmarks use 48 weather variables, but only evaluate 5 of them. The benchmarks also take ClimODE results as-is from the paper at least in Table 2. The results are then unfair to ClimODE: the ClimODE is using only 5 variables worth of information, while weatherODE is using 48 variables. The paper needs compare apple to apples by either running weatherODE results using only 5 variables, or running ClimODE with 48 variables.

I don't think I can follow the v0 estimation motivation. The PDE model is following advection equation assumption, while the v0 is estimated using wave equation assumptions. As far as I can see, these are incompatible with each other. You can't use wave equation to estimate v0 if the underlying PDE system does not follow wave equation. The wave equation might help the v0 estimation, but in that one needs to show why it helps (preferably with a theoretical argument). Can you still try clarify the situation?

Furthermore, I find the way the CNN and PDE and wave equations all play together confusing. I would like to see a mathematical presentation of how all of these come together.

I also couldn't follow the source estimation explanation in the response. The equations 1-3 all imply that the source is part of the time derivative, and is incrementally added to the state change. However, sec 3.3. and sec 3.4. say that the source is estimated as a set output of a set-input neural network, where apparently the source terms are estimated based on future states. 

I interpret the response such that the source is actually added after the PDE rollout as a correcting term, and it's not actually part of the time derivative function. That is, I think you run the PDE solver using only the advection term and without source term, and add the sources as kind of external corrections afterwards. Can you clarify if this is indeed the case? If this is the case, then eqs 1-3 are wrong. The paper needs to be mathematically precise and unambiguous to avoid this type of concerns.

On wave. I'm not sure I understand. I don't see how the advection is related to the triple-equality equation given, or what this new equation even is. Advection has velocity field, while this new equation here doesn't seem to have. I really can't connect these two together. And even if we can connect these, it seems that one needs to make some drastic assumption of u_t = u_x, which I'm not sure if we are doing. I would recommend the authors to give a wider mathematical exposition to the model assumptions. Even if this is trivial for the authors, one needs to make all the the underlying physics assumptions precise, and make their connection to ML precise as well.

I also don't really understand the source term still. I think now that the source term is a CNN over the (3K,H,W) tensor of (u,v) at one single timepoint. This however clashes with the sec 3.4. where the source is instead given as input the entire (N,3K,H,W) tensor of states at all timepoints. This is obviously impossible, since in the ODE/PDE forward unrolling only knows the state at the current (single) timepoint. I can't make sense of the system, and would appreciate a mathematically rigorous and complete description of the model at this stage.

In the case the above concerns are not resolved, the paper is suffering from either substantial modelling or presentation issues. These would warrant changing my score to negative.

### Questions
- I have hard time understanding the v0 estimation. First, a wave equation is introduced in general terms, and then a CNN appears. These two are not connected together, so I’m left wondering what do we do with the waves, and how do they relate to the CNN. Furthermore, the wave equation is poorly motivated, and it seems disconnected from the advection equation 3. To me this looks like a discrepancy: the system follows advection, but initial state assumes different kind of physics (ie. laplacians appear out of nowhere). Surely the initial state estimation needs to respect the chosen ODE model, and not introduce some physics effects that are not part of the ODE.
- The arguments about spatial vs temporal resolution are not convincing. Low temporal sampling rate does not necessarily mean that the temporal resolution is low: this depends on how quickly the process varies. It also feels misguided to say that spatial resolution is 100x higher than temporal resolution: this is only true if you take 32*64, and I don’t think you should do this. Since the (t,x,y) axes have similar ranges (24,32,64), I would argue that there is no resolution gap in the sampling rate between space and time.
- I couldn’t follow the CNN/ViT convergence arguments. I’m not sure what convergence even means here (of training..?, of rollouts..?). I think the paper is arguing that training CNNs is somehow instable, and thus ViT’s have to be used. This sounds implausible, and a poor motivation for choosing how the dynamics should evolve. Surely the networks need to be chosen such that they respect some physical system properties (eg. feature locality/globality).
- I don’t understand the source model. It takes as input all 1…N simulated states u(t_n), but one needs the source states s(t_n) to do this simulation. This has to be a mistake: I assume that we instead take as inputs u(t_1 : t_n), so that the history grows along the ODE rollouts. How do you handle set inputs and set outputs? I don’t think a 3D CNN supports sets as inputs or outputs [maybe these are not sets, but just tensors of fixed size..].
- At sec 3.5. I’m again confused what do you mean by “convergence”.
- Sec 3.5. claims that advection dynamics involves long-range dependencies. I’m not sure I agree, and would even argue the opposite. PDE’s are by nature local models: why would the weather in new york affect the infinitesimal change of weather in london? There is no connection between them. Can you elaborate?
- Sec 3.6. claims that earlier methods only train against final state, and ignore intermediate terms. I’m surprised by this statement. ClimODE trains with all intermediate points, as does the original neural ODE, and every other neural ODE/PDE model I’ve seen. Can you provide examples of models where this happens? Calling this “multi-task” learning is also wrong: intermediate points in an ODE are not different “tasks” (they are not even a single repeated task, since it’s not a “task” in the first place).
- The benchmarks use 48 weather variables, but only evaluate 5 of them. The benchmarks also take ClimODE results as-is from the paper at least in Table 2. The results are then unfair to ClimODE: the ClimODE is using only 5 variables worth of information, while weatherODE is using 48 variables. The paper needs compare apple to apples by either running weatherODE results using only 5 variables, or running ClimODE with 48 variables.

I'm looking forward to the responses.

### Soundness
3

### Presentation
2

### Contribution
3
