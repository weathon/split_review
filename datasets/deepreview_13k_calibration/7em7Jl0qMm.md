# Fourier Ordinary Differential Equations

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 5, 6

## Abstract
Continuous models such as Neural Ordinary Differential Equations (NODEs) are powerful approaches for modeling time series data, known for their ability to capture underlying dynamics and generalization. Current continuous models focus on learning mappings within finite-dimensional Euclidean spaces, raising two critical questions for enhancing their effectiveness. First, Is Euclidean space the optimal representation for capturing the underlying patterns and features in time series data? Second, how can we maintain granularity while benefiting from the generalization capabilities of continuous models? To address the first question, we propose a novel approach for learning dynamics in the Fourier domain. In contrast to Euclidean space, each point in Fourier space summarizes the original signal at a specific frequency, enabling more comprehensive data representations. Additionally, time differentiation in the Fourier domain simplifies the modeling of dynamics as it becomes a multiplication operation. To answer the second question, we introduce element-wise filtering, a method designed to compensate for the bias of continuous models when fitting discrete data points. These techniques culminate in the introduction of a new approach—Fourier Ordinary Differential Equations (FODEs). Our experiments provide compelling evidence of FODEs' superiority in terms of accuracy, efficiency, and generalization capabilities when compared to existing methods across various time series datasets. By offering a novel method for modeling time series data capable of capturing both short-term and long-term patterns, FODEs have the potential to significantly enhance the modeling and prediction of complex dynamic systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces Fourier ordinary differential equations (FODEs), a new model that incorporates Fourier transforms and ordinary differential equations for analyzing time series data.The advantage of the FODEs model is its ability to capture the underlying patterns in the data through frequency component analysis, which in turn provides a better representation of the data and an in-depth understanding of the intrinsic dynamics of the system. The model reduces the difficulty of modeling complex systems by simplifying the differentiation operation to a multiplication operation in the Fourier domain, making it simpler to capture short-term and long-term dependencies in the data. An element-by-element filtering technique is also introduced in the article to keep the data fine-grained and to exploit the generalization capabilities of continuous models, an innovation that is crucial for the accuracy of time series analysis. Through experimental comparisons, FODEs outperform existing continuous and discrete time series models in terms of accuracy and generalization ability, and are more economical in terms of the number of parameters, demonstrating efficiency in terms of computational resources and training data requirements. These features make FODEs a promising tool in the field of analysis and prediction of complex dynamic systems.

### Strengths
The strength of the Fourier Ordinary Differential Equations (FODEs) model lies in its innovative integration of the Fourier transform with ordinary differential equations to analyze time series data. This hybrid approach allows for capturing the underlying patterns in data by analyzing frequency components, offering potentially better data representation and insight into the inherent dynamics of the systems being modeled. By converting differentiation into a multiplication operation in the Fourier domain, FODEs simplify the complexity of modeling dynamic systems, making it easier to capture both short-term and long-term dependencies in the data.

### Weaknesses
1. Problems of model generalization and applicability: Although the article proposes a new method for learning dynamics in the Fourier domain, the generalization and applicability of the method on different types and sizes of time series data are not fully discussed. In particular, the performance and applicability of the FODE model on time series data that are non-periodic or have relatively high signal noise is still a question mark. In addition, the Fourier transform is usually weak for non-smooth signals, which may limit the ability of FODE on complex or non-linear time series data.

2. Model Complexity and Computational Efficiency Issues: Despite the paper's claim that FODE improves on computational efficiency, in reality, the computational complexity of the Fourier transform and inverse transform may increase dramatically as the amount of data increases, especially on real-time or large-scale datasets. The paper lacks an assessment of the computational efficiency of a wider range of computations, such as on multidimensional datasets and the specific advantages and disadvantages compared to other existing methods.

3. Insufficient experimental validation and comparative analysis: while the paper provides some experimental results to support the superiority of the FODE model, it lacks comparative experiments, especially with the latest time series analysis methods. The article does not provide sufficient details of the experimental setup, such as the choice of hyperparameters for the model, training details, and measures to prevent overfitting. In addition, the article does not discuss the confidence intervals or statistical significance of the model in terms of forecasting performance, which reduces the persuasiveness of the experimental results.

### Questions
See Weaknesses

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, authors present a Fourier-based framework to learn the dynamics of systems following ODEs. Essentially, time-series systems are learned by first applying an FFT followed by an inverse FFT. Then an element-wise product with a filter is applied to obtain the updated field variable. The resulting framework is termed as FODE. The empirical studies on six different datasets including three datasets on ECG show superior results over the baselines.

### Strengths
The following strengths of the work. 

S1. Learning dynamical time-series system is an important problem and the work makes a contribution towards this direction.

S2. The idea of combining Fourier transform with an ODE is interesting. 

S3. Empirical results show superior performance of FODE over the chosen baselines.

### Weaknesses
There are several weaknesses for the work as follows.

W1. The idea of using Fourier transform for learning dynamical systems is not new. There are a large family works following Fourier Neural Operators, Deep Operator Networks, and Koopman operators in this direction. Authors have not discussed or compared the results with any of these works in the manuscript.

W2. The experimental systems taken in the work are not very complex. In NODE-based works and in FNOs, much more complex time-series systems such as fluid flow, weather forecasting, complex dynamical equations etc. are considered. However, the first three examples considered in this work are fairly simple equations resulting in 1D dynamics. The ECG dataset is a realistic dataset that is reasonably complex. However, this is again 1D. It is not clear how well the system will scale to larger and more complex problems.

W3. The baselines considered are fairly simple ones that are not truly SOTA. Authors should compare the results with FNO, DeepONet, or such frameworks which are considered to be SOTA.

W4. NODE is essentially a physics-informed approach which requires the integration of the equation of motion to obtain the time-series modeling. FNO is a purely data-driven approach which allows to predict $x_{t+1}$ directly from $x_{t}$ without any integration. By combining Fourier approach with ODE, it seems that the disadvantages of the NODE are still retained. That is, the time integration is still limited by the time-step and hence rollout over a large time window might be challenging.

W5. There is no discussion on the limitations of the present work. This should be included.

### Questions
Q1. What is the loss function? This should be clearly articulated.

Q2. More baselines should be compared. How well does the model perform in comparison to FNO, DeepONet and other SOTA time series models. RNNs and LSTMs are some of the earliest models to be considered as baselines.

Q3. How well does the model scale to more complex data? It is not clear.

Q4. What are the advantages of the FODE over NODE? Is it data-efficient? How robust is it to noisy data?

Q5. Although FODE seems to have a reduced parameter footprint over NODE, what about the training and inference time? 

Q6. Why is a sliding window approach required? Can't the model predict the $x_{t+1}$ directly from $x_t$? Please clarify? If this is a hyperparameter, how does the model work when the only data point is used to predict the future? In the original NODE and FNO, only one data point is used for the future prediction.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proses a model dynamics in the frequency domain for an ODE. This builds along the line of NODE and many other works. The two main components as mentioned in the paper are the use of Fourier transform and hence the modelling of the dynamics in the frequency space and finally the use of an element-wise filter prior to predicting the output. Empirical evaluation is provided on several time-series modelling tasks as an evidence for the model performance.

### Strengths
The paper studies the utility of modelling dynamics in the frequency space, specifically using Fourier transform for ODEs while enabling learning via neural networks. 

It is well articulated, making it easy to understand and follow through.

The element-wise learnable filter seems to be improving performance and I believe can be a good add-on to other models belonging to the same family.

### Weaknesses
The use of Fourier transform and modelling the dynamics in the frequency space have been demonstrated for PDEs [1] and has been widely used, given that the extension to ODE and hence performing reasonably well enough is expected. What I don't find is authors clearly pointing out the value in their work and operator learning framework and/or even the frequency space modelling used for ODE in [2]. Note that [2] uses Laplace transform, but I think this in principle achieving the same modelling paradigm as FODE. Comparing and contrasting to these is critical I think.

Furthermore, the experimental results are okay, but not very convincing that the. proposed method has significant benefits, if any.

Please refer to the questions, below for more specific.

1) I am not sure why the authors mention "Euclidean space" as a contrast to their frequency space modelling method. I don't think this is correct, specifically is FODE using any metric space different from "Euclidean", shouldn't it be just contrasted by mentioning in the data space or something like that? If one uses to choose specifics, these need to be pointed out, mentioning terms vaguely isn't helpful

2) It is mentioned that "time differentiation in the Fourier domain simplifies the modeling of dynamics as it becomes a multiplication operation". I believe author's refer to the convolution property in this case. Is this even being used implicitly and/or explicitly if not, what is the point of mentioning some property. DFT has many properties, if they are not used, these shouldn't be presented as if they are helping the proposed method in any way.

3) What is $T$ in equation (1)? Should it be $t_1$ instead?

4) Eqn (3) is wrong, I will consider this as typo.

5) So, DFT from eqn (4) is being performed along the feature dimension, if this is the case, what do frequency even mean in this case? If authors can clarify this, it would be great.

6) In experimental result, comparison to a frequency space based method is something that I would like to see. If nothing else [2] can be a good baseline, any comment on this one?

7) I would expect time-series classification results be evaluated on accuracy and not MSE, table 3. Why is the choice for MSE justified for classification task?

8) In Table (2) what is the result for NODE with comparable parameters, can the authors discuss this briefly if possible?

9) Figure 4 is good, this is expected, but is there any further analysis that authors plan to present?

10) I am not sure about the utility of Figure 5, this needs to be explained and justified better.

### Questions
1) I am not sure why the authors mention "Euclidean space" as a contrast to their frequency space modelling method. I don't think this is correct, specifically is FODE using any metric space different from "Euclidean", shouldn't it be just contrasted by mentioning in the data space or something like that? If one uses to choose specifics, these need to be pointed out, mentioning terms vaguely isn't helpful

2) It is mentioned that "time differentiation in the Fourier domain simplifies the modeling of dynamics as it becomes a multiplication operation". I believe author's refer to the convolution property in this case. Is this even being used implicitly and/or explicitly if not, what is the point of mentioning some property. DFT has many properties, if they are not used, these shouldn't be presented as if they are helping the proposed method in any way.

3) What is $T$ in equation (1)? Should it be $t_1$ instead?

4) Eqn (3) is wrong, I will consider this as typo.

5) So, DFT from eqn (4) is being performed along the feature dimension, if this is the case, what do frequency even mean in this case? If authors can clarify this, it would be great.

6) In experimental result, comparison to a frequency space based method is something that I would like to see. If nothing else [2] can be a good baseline, any comment on this one?

7) I would expect time-series classification results be evaluated on accuracy and not MSE, table 3. Why is the choice for MSE justified for classification task?

8) In Table (2) what is the result for NODE with comparable parameters, can the authors discuss this briefly if possible?

9) Figure 4 is good, this is expected, but is there any further analysis that authors plan to present?

10) I am not sure about the utility of Figure 5, this needs to be explained and justified better.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper looks to learn a Neural ODE (NODE) system that resides in the Fourier domain, and shows promising empirical results on some time series analysis tasks. The main contribution is to learn NODEs in the Fourier domain rather than Eucledian domain.Also, with element-wise filtering, FODEs address biases in continuous models.

### Strengths
The empirical results are promising, and the presentation is clear. The novelty mainly comes from learning NODE systems in the Fourier domain, and is well investigated.

### Weaknesses
Despite the obvious performance boost compared to NODEs and RNNs, there are many SOTA benchmarks not addressed. For example, [1] has SOTA performances on many time series tasks, along with many other NODE methods. The reviewer understands that the point of the paper is to show learning in the Fourier domain is beneficial, but it would make the paper stronger if such comparisons are made. Also, compared to vanilla NODEs, what theoretical benefits do FODEs have? It would be great to understand this too.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
