# Physics-Guided Learning of Meteorological Dynamics for Weather Forecasting and Downscaling

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
Weather forecasting is of paramount importance for a myriad of societal and scientific applications. Traditionally, numerical weather prediction (NWP) methods based on physical principles are computationally intensive and can struggle with the inherent complexity of atmospheric dynamics. Recently, deep learning techniques have shown promise in weather prediction, but the long-term generalization and physical consistency of pure data-driven approaches remain challenging. In this paper, we introduce a novel physics-guided approach for numerical weather prediction that combines the strengths of both physical mechanism and deep learning, namely PhyDL-NWP. Our method can capture the nonlinear dynamics of meteorology and align deep learning models with the underlying physical mechanism to improve generalization. Extensive experiments on real-world weather datasets show that our model can significantly improve the performance of deep learning methods in a wide range of tasks from forecasting to downscaling.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper attempts to model the meteorological dynamics with physics guided deep leaning method.  Authors propose a physics guided deep learning framework, which can be combined with existing deep learning networks. Experiments are conducted on real world datasets to validate the model.

### Strengths
1. First of all, weather forecasting is a very important problem and should get more attention from the ai community to defending the climate change.
2. Generally, I like the idea of combining physics mechanism with deep learning to improve the performance and generalization ability of ai methods. The proposed method seems reasonable. 
3. Experiments are conducted on the ERA5 dataset, which is one of the most high-quality weather data. The results show that the proposed method can obtain performance gain for both downscaling and forecasting tasks.

### Weaknesses
1. The writing of the paper could be further improved, especially the use of symbols. For example, what is (u, v, w) in figure 1, is Q the same as Q_pi? What is epsilon? The lack of clear definitions for these fundamental variables hinders the understanding of the proposed method. Furthermore, the relationship between the different Q terms needs to be explicitly stated, as it is not immediately obvious. The meaning of epsilon, and how it relates to the overall model, is also unclear.
2. One the mentioned advantage of physics guide is physical consistent. However, it is not clear how to measure physical consistent, do you mean the analysis in sec 4.3? The paper does not provide a clear metric or methodology for quantifying physical consistency. Simply aligning with existing equations does not guarantee physical consistency, and a more rigorous approach is needed. It is unclear how the analysis in Sec 4.3 demonstrates physical consistency beyond a qualitative comparison.
3. There are some important recent works and background information missed in the related work part. Section 2.1 missed some recent progress in weather forecasting such as GraphCast, ClimaX, and FengWu. The relate work part also lacks discussions about PINNs. The absence of these key references makes it difficult to place the proposed method within the broader landscape of weather forecasting and physics-informed neural networks.
4. It is also not clear to me what is the core technique contribution of this paper when aligning it to the broad PINN family. The paper does not clearly articulate how it differs from existing PINN approaches, and what novel aspects it introduces. The contribution should be made explicit in terms of both methodology and application.
5. Regarding the experiments, it is hard to compare this work with existing deep learning works since it is conducted in the special region. It would be good to present the results in the full ERA5 dataset or a smaller resolution (e.g., weatherbench) if the resource is limited. The evaluation is limited by the use of specific regions, making it difficult to generalize the results. The lack of comparison with established benchmarks makes it hard to assess the true performance of the method. The use of the full ERA5 dataset or the WeatherBench benchmark would allow for a more robust evaluation.
6. The assumption that deep learning model is accurate enough does not hold in this paper. While deep learning models show promise, their accuracy is not always guaranteed, especially in complex systems like weather forecasting. The paper needs to justify this assumption or provide evidence of the accuracy of the deep learning component.
7. It is not clear about the detailed train, validation, and test settings. There is also no code shared for reproduce ability checking. The lack of details regarding the training, validation, and testing procedures, as well as the absence of code, hinders the reproducibility of the results. This is a major concern for the scientific rigor of the work.

### Questions
please check the weakness part.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses two common challenges in weather and climate modeling (downscaling and forecasting). There are currently two separate ways of modeling these problems: numerical physics based models and statistical machine learning models. The paper attempts to get the best of both worlds, by proposes a machine learning approach that incorporates physics domain knowledge.

For downscaling, the method starts from a physics-informed neural network (PINN) that takes as input spatiotemporal coordinates and outputs weather variables (e.g. temperature). PINN models use a set of known physical constraints (in the form of PDEs) to penalize models for violating physical laws. However, this model does not assume that physical constraints are given --- instead, they must be discovered from the data. The method entails fitting a PINN neural network in a supervised manner without physics constraints, then identifying relationships in the form of a sparse set of PDEs that relate the variables of interest. These physical relationships contain parameters learned from the data, so they are able to capture subgrid effects that are not captured by traditional physics constraints. Since these relationships are assumed to remain constant throughout space and time, it is reasonable to assume that they can be learned efficiently.

For forecasting, the method starts from a typical machine learning forecasting model and then uses the same strategy to learn physical relationships and penalize the forecasts for violating them.

The method is tested on three different weather datasets and compared to other deep learning methods.

### Strengths
- The paper addresses an interesting problem, provides a reasonable solution, and demonstrates its value through experiments. 
- Figures 1 and 2 are helpful in explaining and comparing the steps of the methods. 
- It was exciting to see the section discussing the physical relationships that were discovered by the model. The discovery of sparse, interpretable models like this is of high interest.

### Weaknesses
 - Overall, I found the writing to be unclear and difficult to follow. This includes details of the method and its relationship to previous work.
- The experiments comparing on multiple datasets and multiple benchmark architectures are nice, but there is no discussion of hyperparameter optimization, early stopping, and how the competitor models were implemented. A few details were in the appendix but not enough details are provided to be confident in these results.
- While I agree that this is an interesting method, I disagreed with many of the ways the authors motivated the work.
- In section 1, I don't agree with the motivations. (1) "While deep learning models can excel at fitting complex patterns in training data, they lack the ability to generalize well to unseen scenarios by capturing noise or specificities of the training data. Moreover, the models often do not consider the physical mechanisms that govern weather systems, leading to predictions that may be statistically accurate for the training dataset but physically inconsistent." Yes, overfitting is a problem in ML, but models can still generalize. In the second sentence, it's unclear what "physically inconsistent" means in this context. I believe the authors are referring to the idea that incorporating physics knowledge is a useful source of inductive bias that will help the model generalize better.
- In section 3.3 the authors say PINNs won't work for forecasting because a dense neural network lacks the advantages of more complicated "state-of-the-art" architectures. It's not the architecture that is important here, it is how the problem is being modeled, i.e. the inputs and outputs.
- In section 4.1, "Unlike computer vision, the weather data has multiple variables and the spatio-temporal dependencies are not completely local". I disagree. Natural images have RGB channels (plus the time dimension). I would argue that they have more non-local spatio temporal dependencies.

### Questions
- I would like to see a more clear description of how this relates to previous work.
- I would like to see a better description of how the hyperparameters were tuned.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new method that blends deep learning and traditional numerical methods for weather downscaling and forecasting. The main idea is to train neural networks to represent different components in a partial differential equation (PDE). These networks can then either be used independently to perform weather downscaling or used to guide the training of a weather forecasting model. The experiments on different datasets show that the proposed method outperforms other baselines on weather downscaling, and boosts the performance of existing weather forecasting models.

### Strengths
- Relevance: The paper aims to combine the strengths of deep learning and numerical methods for weather prediction tasks, which I think is a very important and interesting direction to pursue. 
- Originality: To the best of my knowledge, the idea of the paper is original. 
- The authors conduct a large number of experiments, and the empirical results support their claim.

### Weaknesses
### Paper presentation
- Overall, I think the paper writing and presentation can be improved a lot. I had to spend quite a long time reading Section 3, as different sections were not connected very well. It would be much easier for readers if the authors first presented an overview of the method, i.e., learn a PDE using neural networks that can later be used for weather downscaling or guiding weather forecasting models. While the authors did mention this in the introduction, I think it's good to also repeat this at the beginning of Section 3 as it's important to understand the method.
- Many details of the method and experiments are missing: what partial derivative candidate terms are used and why, the weights of different loss terms, the network architectures, training details (e.g., learning rate, scheduling, etc.), and implementation of the finite difference method, etc. These details are needed to understand how to train the model in practice, and to improve the reproducibility of the paper.

### Soundness
- The main claim of the paper is the physical mechanism in Equation (1) provides guidance to optimizing neural networks that better obey physics. However, I wonder if this is true, because all components of the PDE are parameterized as a neural network and are learned from data. Therefore, all the Equation (1), or correspondingly, the L_physics loss does is to make sure these different networks "agree" in a certain way, and it's not guaranteed that they'll agree with physics laws after training.

###  Significance
- My biggest concern I have about the paper is its significance. While the experiments support the authors' claim, they are quite small-scale compared to existing works, and seem to use non-sota baselines for comparison.
- The paper uses 3 regional datasets that specifically target China. These datasets are not standard and I've not seen them used in previous works in deep learning for the weather domain. Can the authors justify their choice of data? What stops the authors from using more standard datasets such as ERA5 for weather forecasting, which have been a standard in the literature, and have also been used in different benchmarks [1, 2, 3]?
- The baselines used for comparison are not strong enough. For downscaling, why don't the authors compare with models that were specifically proposed for downscaling such as YNet [4] and DeepSD [5], or more recent super-resolution models? For weather forecasting, there have been significant advancements in recent years, including FourCastNet [6], ClimaX [7], GNN [8], PanguWeather [9], Graphcast [10], etc. The paper only compares with FourCastNet, which is the least-performing method among these baselines. Can the authors include more recent baselines for weather forecasting? It would be more convincing if the proposed framework also improves sota methods.
- Scalability: I suspect the proposed method will scale well to more data and bigger/better base models. As the training loss is computed for each grid point (x, y, t), the number of training samples will increase significantly with higher spatial and temporal resolutions. Is this the reason why the experiments are limited to small-sized datasets?
- Ablation studies are lacking. It's important to understand the importance of different components in the framework, such as the physics loss, regularization loss, etc. 

### Minor comments
- Equation (7) is strange because the PDE parameters are already learned and fixed. They should not appear here.
- The papers I cited here are relevant and should be discussed in the paper.

### Questions
- In Equation (4), can we use n' and m' (coordinates of the high-resolution data) too?
- For the downscaling task, how do you make predictions after training given the coarse resolution data?
- The PDE is learned but only used to provide guidance to training other neural networks. Can we solve this learned PDE to solve weather tasks?

### Soundness
2 fair

### Presentation
2 fair

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
In this paper, the author proposes a new physics-informed framework to solve PDEs, with the aim to achieve enhanced downscaling reconstruction and temporal forecasting in weather forecasting problems. This is an important and challenging problem. The author conducts a series of experiments to justify the effectiveness of the proposed model in both downscaling and forecasting cases. Additionally, it is demonstrated that the proposed model can be easily incorporated with other deep learning models as a plug-in module.

### Strengths
1. The paper provides a clear and effective explanation of the background and justifies the proposed method through a comprehensive series of experiments.
2. The paper studies an important and challenging problem. 
3. It demonstrates how the proposed method can be seamlessly integrated as a plug-in module into additional deep learning models.

### Weaknesses
1.	The presentation in the method section remains unclear in some parts, particularly in explaining the model's approach to downscaling. A detailed explanation of the model's design rationale for addressing the downscaling problem, including its advantages over existing methods, would be beneficial. The description lacks specific details on how the model leverages the physics-informed component to achieve higher resolution outputs. For instance, it's not clear how the latent force term is parameterized and how it interacts with the spatial and temporal components of the model to generate downscaled results. The explanation should include a more explicit description of the mathematical operations and transformations that occur during the downscaling process.
2.	The authors may want to discuss the difference/superiority between the proposed method with existing works on similar topics (e.g., decomposing PDEs into components using neural networks and capturing temporal dynamics). The paper needs to more clearly articulate the unique advantages or improvements of the proposed method over these existing approaches. Specifically, the paper does not address how the model handles the inherent ill-posedness of downscaling, and how the physics-informed component helps in stabilizing the solution compared to purely data-driven methods. Furthermore, the paper should discuss the computational complexity of the proposed method and how it scales with the size of the input and output grids, especially when compared to more traditional PDE solvers.

### Questions
See weakness points above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
