# Scene Flow as a Partial Differential Equation

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
We reframe scene flow as the task of estimating a continuous space-time ordinary differential equation (ODE) that describes motion for an entire observation sequence, represented with a neural prior. Our method, _EulerFlow_, optimizes this neural prior estimate against several multi-observation reconstruction objectives, enabling high quality scene flow estimation via self-supervision on real-world data. EulerFlow works out-of-the-box without tuning across multiple domains, including large-scale autonomous driving scenes and dynamic tabletop settings. Remarkably, EulerFlow produces high quality flow estimates on small, fast moving objects like birds and tennis balls, and exhibits emergent 3D point tracking behavior by solving its estimated ODE over long-time horizons. On the Argoverse 2 2024 Scene Flow Challenge, EulerFlow outperforms _all_ prior art, surpassing the next-best _unsupervised_ method by more than $2.5\times$, and even exceeding the next-best _supervised_ method by over 10\%. See http://eulerflow.github.io for interactive visuals.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes to represent scene flow as a velocity field using a neural prior. Instead of prior art that directly represents per-pair scene flow as neural prior, the authors alternatively propose to use neural prior to model the partial differential equation (PDE) of the position of the point versus the time interval. This novel velocity representation is interesting and could offer flexibility in dealing with long-term sequences of flow estimations as the authors described in the paper. The authors have also done extensive analysis of the proposed method on Argoverse 2 (and Waymo) datasets, comparing the performance with recent scene flow works, and validating the good performance of the proposed method.

### Strengths
- The paper proposes an interesting idea to represent the scene flow as a velocity field using a neural network, making it very easy to combine the temporal information (time) and the spatial information (position of points).
- The authors have done extensive analysis of the proposed method, and have shown different ablation studies to validate the effectiveness of the method.
- The proposed method also shows the potential to deal with small objects and emergent flows in robotics scenarios, which could be interesting when applied to highly dynamic environments.
- Overall, the writing of the paper is clear, and the visualization is easy to understand.

### Weaknesses
 - When using the time interval between [-1, 1] for the time encoding, will the proposed method not be able to handle time step outside the range? Given that the representation is a continuous neural network, how does it extrapolate to a longer sequence with the current representation? It's unclear how the method would perform if queried at times significantly outside this range, and whether the learned velocity field remains valid for such extrapolations. The lack of explicit discussion on the limitations of this temporal encoding is a concern.
- When comparing with a method like NSFP, I wondered if the authors could show the results of pure Euler integration of the method and highlight the benefits of wrapping a PDE with a neural network. It's not clear if the performance gain is solely due to the neural network parameterization or the PDE formulation itself. A baseline using Euler integration on top of the NSFP output would help to isolate the contribution of the PDE modeling.
- The authors mentioned that they only do sequences of length 20, I wondered if the method failed rapidly with the increase of the sequence length. It would be interesting to show an even longer sequence to highlight the arbitrary time query property of the proposed method. The current experiments do not fully demonstrate the method's capability to handle long-term dependencies and the benefits of its continuous-time representation. The lack of experiments on very long sequences limits the impact of the arbitrary time query argument.
- I feel like the authors want to talk about too many things in this paper, so they may overlook the most important part of the method. This method is good at dealing with long-term flow trajectory and has the potential to better capture the small, highly dynamic objects in the scene. The authors could reorganize the motivations and experiments to highlight the advantages of the proposed method.

### Questions
- The discussion of the different activation functions (appendix) is indeed interesting. And this could be one of the interesting parts of the ablation study. However, it is strange to see that using the Gaussian non-linear function is yielding very bad performance. Perhaps the spectral width needs to be fine-tuned, especially when the distribution of the lidar scene flow is very unique.

Please also see the above section for detailed comments.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel approach to scene flow estimation by reframing it as the task of estimating a continuous space-time partial differential equation (PDE) that describes motion across an entire observation sequence. The proposed method, called EulerFlow, utilizes a neural prior to represent this PDE and optimizes it against multi-observation reconstruction objectives. This approach allows for high-quality, unsupervised scene flow estimation on real-world data, outperforming existing supervised and unsupervised methods, particularly on small and fast-moving objects like birds and tennis balls. The authors demonstrate the effectiveness of EulerFlow on datasets such as Argoverse 2 and Waymo Open Dataset, and show its applicability across different domains without domain-specific tuning. Additionally, they highlight emergent 3D point tracking behavior as a result of solving the estimated PDE over long time horizons.

### Strengths
- I'm not up-to-date to the latest scene flow models, but from the results in the paper it surpass the prior art by a large margin, which is very significant
- Introducing the concept of modeling scene flow as a PDE is innovative and offers a new direction for research in motion estimation.
- The method is rigorously developed, with comprehensive experiments and ablation studies that validate the approach.
- The paper is well-written, with clear explanations and effective use of figures to illustrate key points.

### Weaknesses
 - As stated in the paper, the speed of the proposed method is a big concern, preventing it from deploying on real world application.
- Some hyperparameters, such as the depth of the neural prior, seem to require dataset-specific tuning (e.g., increasing depth to 18 for the Argoverse 2 challenge), which may affect the method's out-of-the-box applicability. The need to adjust the neural prior's depth for different datasets suggests a potential sensitivity to the complexity of the motion patterns or scene characteristics, which could limit its generalizability without careful hyperparameter optimization.
- It would be great if the author could show more failure cases to help readers better understand its limitations. Specifically, it would be beneficial to see failure modes related to occlusions, rapid changes in depth, or complex object interactions, as these are common challenges in scene flow estimation.

### Questions
Overall I believe this paper is in a good shape, the authors discuss the properties and limitations of the proposed method thoroughly in the paper. I have a few more questions:

- How does the method handle scenes with deformable objects?
- What is the impact of temporal sampling rate on performance?
- How does the point cloud density affect the performance?

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
4

### Summary
The paper proposes a neural representation to optimize scene flow as a discrete partial differential equation of scene geometry over time. Compared to previous method, Neural Scene Flow Prior (NSFP), a method is most related to this work in the neural representation, the proposed method introduces a multi-frame formulation and learns bi-directional three-step Euler integration of the geometry consistency using decoded per-frame scene flow. Compared to previous work, the proposed representation can achieve better performance in Autonomous driving datasets and the authors demonstrate qualitative performance on depth camera input as well.

### Strengths
1. The proposed scene flow representation is simple and technical sound. Compared to prior work NSFP, extending it to multi-frame and learns a bi-directional consistency scene flow is a very intuitive step forward. 
2. The performance of this method (both qualitative and quantitative) is impressive. The method can learn very consistent scene flow in trajectory despite not explicitly considering common issues such as occlusion artifacts. As the paper demonstrated, it can tackle well on small objects (with potentially large motions as well).

### Weaknesses
1. The paper title and introduction is very general and does not provide a precise position of this paper's main contribution. "Scene flow a partial differential equation" has been historically formulated long time ago in many prior paper, e.g. [1] as one examplar reference, and it has been proposed as a continuous representation in one early seminal work [2]. Many related work studied this optimization problem using images input and solved it using differential optimization approaches before. In this paper seems only consider related work in the point cloud space, and beneficially solved in using a neural representation. I will suggests to more precise position their scope and contributions  in paper title, introduction and contributions.

2. The evaluation dataset in this paper is mostly on autonomous driving datasets though as the method demonstrated, it should also work on other data domain when depth is available. Though real world depth and flow ground  truth is hard to get, it won't be too hard if evaluated using a more general synthetic dataset that provide different motion patterns, compared to the type of motion and accuracy that autonomous driving dataset can provide. 

3. The paper has already discussed the main limitations it section 6.1. Particularly for the last point "EulerFlow does not understand ray casting geometry", it was clear how this has been demonstrated in the current results. It will be good if the authors can provide examples and metrics that reflect the challenge in this aspect.

### Questions
Among all the three points I illustrated in the weakness, 

For point 1, I hope the authors can provide concise update on their paper title and contributions in particular for the first bullet time (line 99-100).

For point 2, the current evaluation is sound and maybe sufficient for this paper. I do believe it is nice to more evaluation on non-AV dataset quantitatively that very likely will benefit this method as a baseline for future work in different domain. 

For point 3, it will be good if the author can provide specific example (as a figure)

### Soundness
3

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
The paper proposes SFvPDE, a framework to cast scene flow estimation as a PDE with a neural prior, and EulerFlow, an example demonstrating how SFvPDE can be trained using the Euler method to locally integrate the PDE during training. A space-time-dependent vector-field is trained to match subsequent point clouds at different timestamps via solving the underlying PDE. The method significantly outperformes both supervised and unsupervised baselines and is especially effective on small objects compared to prior work.

### Strengths
The method is simple and intuitive yet effective. Extensive experiments section shows clearly that the proposed method surpasses prior work.

### Weaknesses
The main weakness of EulerFlow, as also noted by the authors (lines 524-528), is the time it takes to converge on a single scene. But given the performance of the method, this should not be considered critical. However, the presentation of the paper can be improved, the paper lacks some implementation details, as from time to time the reader has to guess what is actually happening (see questions section).

1) In lines 189 and 195 $\frac{\partial L^*}{\partial t}$ is referred to as the partial differential equation, or a PDE. However, $\frac{\partial L^*}{\partial t}$ alone is not a PDE yet, unless it is set equal to something (as in equation 2).
2) I guess that in equation 2 SFvPDE should also depend on $x$. Could the authors clarify this?
3) In general, it would be nice to have more formal definitions. E.g. in EulerFlow, an exact formula for solving the PDE, $\text{Euler}_\theta(P_t, d, k)$, would improve understanding and reproducibility of the method.
4) In principle, the PDE can be integrated in both directions by simply reverting the time. The usage of the direction as an extra argument in the model makes the connection between sections 3 and 4 slightly weaker and seems to be a legacy design choice from NSFP. Thus, a question to the authors is whether they have tried training without the direction argument?
5) Given the high computational complexity of the method, it would be better to see some implementation details on how exactly equation 3 is calculated during training. Are any optimizations already incorporated? E.g. in the current form separate terms in the loss are independent. However, I believe that subsequent Euler steps can use previous estimates instead of recalculating them.
6) More ablation studies would better highlight the contributions of the paper. E.g. how general and how sensitive is the method to different numerical solvers and sizes of discretization steps? Have the authors tried higher-order PDE solvers or using $\Delta t$ smaller than the time between observations?

### Questions
Here are some questions and concerns regarding the presentation and the method:

1) In lines 189 and 195 $\frac{\partial L^*}{\partial t}$ is referred to as the partial differential equation, or a PDE. However, $\frac{\partial L^*}{\partial t}$ alone is not a PDE yet, unless it is set equal to something (as in equation 2).
2) I guess that in equation 2 SFvPDE should also depend on $x$. Could the authors clarify this?
3) In general, it would be nice to have more formal definitions. E.g. in EulerFlow, an exact formula for solving the PDE, $\text{Euler}_\theta(P_t, d, k)$, would improve understanding and reproducibility of the method.
4) In principle, the PDE can be integrated in both directions by simply reverting the time. The usage of the direction as an extra argument in the model makes the connection between sections 3 and 4 slightly weaker and seems to be a legacy design choice from NSFP. Thus, a question to the authors is whether they have tried training without the direction argument?
5) Given the high computational complexity of the method, it would be better to see some implementation details on how exactly equation 3 is calculated during training. Are any optimizations already incorporated? E.g. in the current form separate terms in the loss are independent. However, I believe that subsequent Euler steps can use previous estimates instead of recalculating them.
6) More ablation studies would better highlight the contributions of the paper. E.g. how general and how sensitive is the method to different numerical solvers and sizes of discretization steps? Have the authors tried higher-order PDE solvers or using $\Delta t$ smaller than the time between observations?

I will adjust my score based on the other reviews and the rebuttal by the authors.

### Soundness
3

### Presentation
2

### Contribution
3
