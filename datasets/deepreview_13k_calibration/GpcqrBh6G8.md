# Data-driven plasma equilibrium forecasting in magnetic fusion tokamak

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
The most promising approach to achieving nuclear fusion is through tokamaks, which confine plasma using magnetic fields.
Understanding the current plasma equilibrium state in tokamaks is critical for effective plasma control.
Unlike previous studies, which reconstruct equilibrium from magnetic field information, our work forecasts future equilibrium based on past equilibrium states.
Specifically, we formulate the plasma equilibrium prediction task as a video prediction task, a well-explored problem in the machine learning community.
This formulation allows us to capture the spatio-temporal dynamics of plasma states and provides a foundation for multimodal modeling of data streams from tokamak operations.
Our methodology, incorporating a physics-inspired learning technique for physically reliable predictions, achieved plausible results in forecasting future plasma equilibrium up to 200 ms ahead compared to baselines.
This approach holds promise for predicting plasma instabilities and preventing disruptions, marking a significant step towards developing stable fusion reactors.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this work, the author considers an application for predicting plasma equilibrium, formulated as a video prediction task. The author proposes a physics-informed learning technique built upon an existing CNN-based model. This model can forecast future plasma equilibrium up to 200 ms ahead, outperforming baseline methods.

### Strengths
- The author demonstrates an important application on plasma equilibrium forecasting.
- The author generates a new dataset, which can be a contribution if published.

### Weaknesses
### Method
- The paper utilizes an existing method, simVP, which should be introduced in more detail. Specifically, the paper lacks a description of the architecture, loss function, and training procedure of simVP. The reader is left to guess how this model is adapted to the plasma equilibrium prediction task.
- The physics-informed loss using finite differences is fairly standard [1]. The paper does not discuss the specific finite difference scheme used, nor does it justify why this particular scheme was chosen over other alternatives. Furthermore, the paper does not analyze the impact of the finite difference discretization on the accuracy of the physics-informed loss.

### Scope
- Overall, I am concerned that the paper may lack sufficient contributions from the ML perspective, making it potentially more suitable for a journal in nuclear fusion. The paper does not clearly articulate the novelty of applying video prediction to this problem. The use of a standard video prediction model and a standard physics-informed loss function does not represent a significant advancement in machine learning methodology.
- Alternatively, if the dataset can be published, it might be more effective to present this work as a benchmark paper comparing existing methods. However, even as a benchmark, the paper would need to provide a more thorough analysis of the dataset's characteristics and the challenges it presents for video prediction models.

### Questions
It seems quite standard to define the task as video prediction. What was the challenge preventing previous works from doing so? It could be helpful to discuss more the contribution from formulating the problem this way.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a machine learning forecasting technique for applications in tokamak plasma predictions.  The data are spatio-temporal fields characterizing the plasma dynamics.  The method proposed makes use of equilibrium solutions from the past to predict the future states.

### Strengths
As for applications, they do propose to apply this to an important problem in physics which is difficult to do forecasting on.  Certainly the characterization of plasmas is an important and challenging data set.

### Weaknesses
While I do agree that they are proposing a new method, the comparatives to other methods just aren't up to the level required for ICLR.  Only convLSTM is really compared with for forecasting.  But I would argue there should have been a much richer set of comparatives.  For instance, there is the very simply DMD method for forecasting plasma dynamics:

https://pubs.aip.org/aip/pop/article/27/3/032108/929066

The dynamics they are looking have been shown to be pretty well characterized by a linear model in many application areas.  Using all this technology without comparison to a baseline linear model does not warrant the paper to move forward.  I work in spatio-temporal dynamic systems and just don't find their results compelling enough in terms of advancing the field, nor the results so compelling in terms of the application itself.

And there are other methods that should have been applied beside convLSTM:  

ResNet (He et al 2016)
PredRNN (Wang et al 2017)

Also, completely missed for the video prediction task idea is https://www.nature.com/articles/s43588-022-00281-6

Ultimately, I just don't think either the results or their method represent an innovative enough leap (either in the ML/AI architecture proposed or in the advancement of the application) for ICLR.

I cannot recommend the paper moving forward at this point.

### Questions
The baselines and comparatives are simply not good enough in my view (see above).  There are other plasma reduced order models for forecasting that are completely ignored.  In addition, the method, while clever, does not signify an significant innovation for ICLR.

### Soundness
2

### Presentation
3

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
This paper addresses the crucial issue of predicting plasma equilibrium in tokamaks, which are essential for advancing nuclear fusion technology. The authors propose a novel method that formulates this prediction task as a video prediction problem, enabling the capture of spatio-temporal dynamics of plasma states. By applying well-established video prediction algorithms, the authors aim to forecast future plasma equilibria based on past states and achieve promising results that contribute to the understanding of plasma instabilities and control.

### Strengths
The approach of framing plasma equilibrium prediction as a video prediction task is new in this area, introducing a fresh perspective to the fusion community, which has been largely focused on magnetic field data. This formulation may inspire future research in related fields. The methodology demonstrates a solid understanding of both machine learning techniques and plasma physics, with the integration of a physics-inspired loss function showing potential for improving model predictions. The paper is generally well-organized, providing a clear explanation of the background and motivations behind the research, as well as a structured presentation of methods and results.

### Weaknesses
The application of existing video prediction algorithms to the specific context of plasma equilibrium is straightforward and thus may not present sufficient novelty. Further differentiation from previous works is needed to establish the unique contribution of this study.
The selection of the loss function has not been illustrated and validated sufficiently. Equation (2), which should be crucial in this paper, looks strange without an essential explanation.

### Questions
1. About the loss function: Why do the authors choose the ell-1 norm, rather than the more frequently used ell-2 norm? In eq. (2), what's the difference between $\Delta^* \psi_{pred}$ and $\Delta^*(\psi_{pred})$?
2. How does the resolution of discretization affect the accuracy of the prediction?
3. Could the authors elaborate on the choice of video prediction algorithms? What specific adaptations were made to ensure compatibility with the plasma equilibrium data?
4. Are there plans to extend this method to include a wider variety of tokamak data, such as temperature profiles or density distributions?

### Soundness
3

### Presentation
3

### Contribution
2
