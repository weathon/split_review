## Human Reviewer 1

### Summary
The paper proposes a technique for forecasting the early stages of pandemics. The approach is based on residual CNNs. The paper claim that the proposed approach outperforms both traditional compartmental models and CNNs in the accuracy of predictions with limited data.

### Strengths
* Improving the prediction of pandemics is a worthy goal.

### Weaknesses
* The literature review section of the paper is very limited. The scale and impact of the COVID pandemic was so large that many thousands of papers were published, effectively trying every single technology available. Resnet being a very popular model, it was used in many papers. The combination of deep learning with compartmental models was also one of the most popular (and natural) techniques for prediction.
* As a result of the previous weakness, the paper does not clarify what is the novel contribution in this extensively explored subject.
* The paper does not explain the choice of the residual CNNs, versus other CNN techniques, or newer techniques such as attention models, diffusion models, LLMs etc.

### Questions
* Please see weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1

### Rating
0

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper presents a framework where the neural network predicts parameters of a compartmental epidemiological model. The neural network learns from historical data on epidemics, and the authors test the trained neural network during the early stages of the COVID-19 pandemic.

### Strengths
Early-stage pandemic forecasting is a critical and under-explored challenge where data scarcity is the norm.

The method is sound, and the results show it is promising.

### Weaknesses
The central idea of using neural networks to predict the parameters of a compartmental model is promising, but it is not novel. The authors appear to be unaware of a substantial body of prior work in this area, as the main methodological contribution of the paper has already been proposed in earlier studies, particularly in [1] and [2], and in a slightly different form in [3]. Related extensions have even been explored in the context of agent-based modeling (e.g., [4]). The paper’s contribution largely centers on this existing technical idea, with the additional element that the neural network learns from data across multiple diseases. While this cross-disease transfer concept is interesting, it does not constitute a technical innovation. I would recommend that the authors consider submitting this work to an epidemiological or applied modeling venue, where the empirical findings and early-pandemic insights would be more appreciated. To strengthen the experimental analysis, the paper should also compare its approach with alternative methods for calibrating compartmental models, such as approximate Bayesian calibration. Additionally, I suggest exploring other compartmental models to showcase the generalizability of the approach. Overall, I do not find the current level of technical contribution sufficient for publication at a leading AI/ML venue such as ICLR.

[1] Arik, S., Li, C.L., Yoon, J., Sinha, R., Epshteyn, A., Le, L., Menon, V., Singh, S., Zhang, L., Nikoltchev, M. and Sonthalia, Y., 2020. Interpretable sequence learning for COVID-19 forecasting. Advances in neural information processing systems, 33, pp.18807-18818.

[2] Arık, S.Ö., Shor, J., Sinha, R., Yoon, J., Ledsam, J.R., Le, L.T., Dusenberry, M.W., Yoder, N.C., Popendorf, K., Epshteyn, A. and Euphrosine, J., 2021. A prospective evaluation of AI-augmented epidemiology to forecast COVID-19 in the USA and Japan. NPJ digital medicine, 4(1), p.146.

[3] Qian, Z., Alaa, A.M. and van der Schaar, M., 2020. When and how to lift the lockdown? global covid-19 scenario analysis and policy assessment using compartmental gaussian processes. Advances in neural information processing systems, 33, pp.10729-10740.

[4] Chopra, A., Rodríguez, A., Subramanian, J., Quera-Bofarull, A., Krishnamurthy, B., Prakash, B.A. and Raskar, R., 2023, May. Differentiable Agent-based Epidemiology. In Proceedings of the 2023 International Conference on Autonomous Agents and Multiagent Systems (pp. 1848-1857).

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
0

### Confidence
4

---

## Human Reviewer 3

### Summary
The authors propose a model that combines a CNN with a deep compartmental model for early-stage pandemic forecasting. The CNN outputs interpretable parameters (e.g., transmission rates) that drive the compartmental ODEs. They use historical pandemic data with metadata to guide parameter inference and claim superior early-stage forecasting.

### Strengths
· The T-DCM ablation (HG-DCM without historical data/metadata) clearly shows performance degradation, providing strong empirical evidence that integrating historical pandemic signals improves early-stage forecasting stability and accuracy.

· The authors compiled a novel dataset spanning six major outbreaks since 1990 (COVID-19, Ebola, SARS, Dengue, Monkeypox, seasonal influenza) across 258 global locations, including country-level development indicators and epidemiological metadata (e.g., transmission pathways). This is a valuable community resource.

### Weaknesses
· This work lacks any rigorous theory or mathematical notations for the explanation of the overall model and simply seems to be an incremental work that simply fuses a CNN with DELPHI. The authors need to distinguish between the contributions they make here. Table 1 seems to just be an ablation study.

· The authors claim that the COVID-19 Forecasting hub models “lack publicly available, reproducible codebase, and the shared forecasting outputs do not include early-stage results”. This is false as all the forecasting has been made publicly available since the early stage of the pandemic. Please see https://github.com/epiforecasts/covid-us-forecasts . Unfortunately the authors use none of these models as baselines. Talking about early stage forecasting, there are also works[1,2,3] that are deep-learning based and also incorporate physics. 


· The motivation that prior pandemics are equally important to make predictions in a new pandemic is a bizarre assumption by any means. I am not sure why the Dengue Fever outbreak dynamics will be useful for predicting the COVID pandemic.

· Coming to the details of the methods, there are some critical issues that drew my concern:

o You define "Last Day of Augmentation (LDoA)" using the peak of the first wave → future knowledge, which seems to be data leakage.

o ResNet-50 on 1D time series ignores temporal dynamics and risks over-fitting.

· There are no SOTA comparisons like EpiFNP [4], DeepGLEAM [5], or NeuralODE [6].

· Predictions do not have uncertainty estimates. Are multiple runs not done for Table 1?

· No code provided, so I have reproducibility concerns. 

[1] Rodriguez, Alexander, et al. "Deepcovid: An operational deep learning-driven framework for explainable real-time covid-19 forecasting." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 35. No. 17. 2021.

[2] Rodríguez, Alexander, et al. "Einns: epidemiologically-informed neural networks." Proceedings of the AAAI conference on artificial intelligence. Vol. 37. No. 12. 2023.

[3] Motavali, Amirhossein, et al. "DSA-BEATS: dual self-attention N-BEATS Model for forecasting COVID-19 hospitalization." IEEE Access 11 (2023): 137352-137365.

[4] Kamarthi, Harshavardhan, et al. "When in doubt: Neural non-parametric uncertainty quantification for epidemic forecasting." Advances in Neural Information Processing Systems 34 (2021): 19796-19807.

[5] Wu, Dongxia, et al. "DeepGLEAM: a hybrid mechanistic and deep learning model for COVID-19 forecasting." arXiv preprint arXiv:2102.06684 (2021).

[6] Kosma, Chrysoula, et al. "Neural ordinary differential equations for modeling epidemic spreading." Transactions on Machine Learning Research (2023).

### Questions
Please address the weaknesses listed above.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
0

### Confidence
1