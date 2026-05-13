# Generalizing Dynamics Modeling Easier from Representation Perspective

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Learning system dynamics from observations is a critical problem in many applications over various real-world complex systems, e.g., climate, ecology, and fluid systems. Recently, the neural-based dynamics modeling method has become the prevalent solution, where its basic idea is to embed the original states of objects into a latent space before learning the dynamics using neural-based methods such as neural Ordinary Differential Equations (ODE). Given observations from different complex systems, the existing dynamics modeling methods offer a specific model for each observation, resulting in poor generalization. Inspired by the great success of pre-trained models, we raise a question: whether we can conduct a generalized Pre-trained Dynamic EncoDER (PDEDER), which, for various complex systems, can embed their original states into a latent space, where the dynamics can be easier captured. To conduct this generalized PDEDER, we collect 153 sets of real-world and synthetic observations from 24 complex systems. Inspired by the success of time series forecasting using Pre-trained Language Models (PLM), we can employ any PLM and further update it over these dynamic observations by tokenization techniques to achieve the generalized PDEDER. Given any future dynamic observation, we can fine-tune PDEDERwith any specific dynamics modeling method. We evaluate PDEDER on 18 dynamic systems by long/short-term forecasting under both in-domain and cross-domain settings and the empirical results indicate the effectiveness of PDEDER.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a generalized framework to learn system dynamics across different settings, by utilizing a pretrained language model from massive observational data, and jointly fine-tuning the pretrained language model and a Graph ODE-based  neural simulator. The proposed PDEDER is pre-trained on 153 sets of observations from 24 complex systems, using a pre-trained language model updated via tokenization techniques. Experiments evaluate PDEDER on 18 dynamic systems for long/short-term forecasting in both in-domain and cross-domain settings.

### Strengths
1. The proposed generalized pre-trained dynamics encoder is well-motivated and technically sound.

2. The proposed approach achieves good in-domain and cross-domain performance, highlighting its generalization ability.

### Weaknesses
 1. The writing needs further improvement. For example, the citation in the main text sometimes should be \citep (line 36-39 for example, with references within brackets) instead of \cite. Also in the problem setting section, can the authors justify if the graph structure (edges) are fixed or evolve over time?

2. I feel the experiments can be further improved: for the baselines, they are all neuralODE-based approaches. However for dynamical system modeling, there are also many discrete neural simulators [1]. The authors are suggested to justify why these approaches are not compared in this paper. As mentioned in the abstract part, the proposed framework should be easily coupled with any dynamic modeling methods (besides neural ODEs). Also, there are works [2] that learn a generalized neural simulator trained from multiple systems. It is also suggested to include them in the paper for a more comprehensive comparison.

### Questions
1. For the model implementations, I wonder if the model performance will be large affected by the dynamic modeling module during fine-tuning stage, such as changing into discrete GNNs or trained with one-step/multiple-step losses?

2. What would be the runtime of the proposed method compared to others?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a method for leveraging observations from multiple systems to create a generalized model that captures shared dynamics across these systems in a common latent space. Their method, PDEder, builds on pre-trained language models, adapted to specific dynamic observations through tokenization and fine-tuning, which enables predictions of future dynamics. The authors evaluate their model on 18 dynamical systems, covering both long- and short-term forecasts.

### Strengths
The paper is well-written and tackles a significant challenge in modeling time series obtained from multiple systems. It leverages recent advances in language models and emphasizes generalizability, which is an important quality for such models.

### Weaknesses
 # Critical:
1) I am concerned about the main assumptions the paper relies on. Are you assuming that different systems come from the same statistics or share fundamental dynamics? I would argue that systems from completely different worlds, time scales, and dynamical regimes should not necessarily be trained together when the overlap in their behaviors is minimal. There is an assumption the authors rely on that needs better quantification regarding how much the systems can differ in terms of dynamical regimes and time scales. Even within the same field and data modalities, recordings from different subjects often differ significantly, indicating that they should not always be learned together. Across fields, I am concerned this issue is more pronounced and must be addressed more carefully both mathematically and as a discussion with a clear list of assumptions. Specifically, what are the statistical properties of the observed data that the method assumes? Does it assume Gaussian noise, or are there other constraints? How does the method perform when the underlying distributions of the observations differ significantly, such as when some data is Poisson-distributed while others are Gaussian?

2) Regarding the previous point, in Line 044 you mention generalizability across domains. While models should indeed, broadly. be generalizable, they must also capture the unique characteristics of different domains. Therefore, I believe the trade-off between generalizability, expressivity, and interpretability needs to be more thoroughly addressed. The authors should clarify how the model balances learning shared dynamics with preserving the specific characteristics of each system. This is particularly important when dealing with systems that have distinct underlying mechanisms.

3) Additionally, more papers should be discussed in the related work, including works on neural dynamics that leverage multi-session information via shared dynamical priors [1] or transformers [2] for inferring dynamics. The authors should clarify why these approaches are not relevant or how their work differs from them. If the proposed method is not intended for neural dynamics, this should be explicitly stated.

4) I am also concerned about the interpretability of the model, which you barely discussed. When using deep learning for scientific purposes, we want to ensure that our model parameters and latent variables are interpretable. However, with the use of pre-trained language models and fine-tuning across observations, it seems the model lacks interpretability. How would the authors address this? While applying SINDy to the embeddings is an interesting idea, it is not clear how this provides interpretability beyond error quantification. The key advantage of SINDy is its ability to decompose a system into basic functions or components, not just considering reconstruction accuracy as the primary metric. The authors should analyze the SINDy weights and provide some interpretations of the underlying components.

5) It is not clear how you calculate the graphs (i.e., $\mathcal{G}$) for the real-world data. Is it known, or do you calculate it during pre-processing? If the graphs are required or need to be calculated from labeled data, this should be stated explicitly in the text. Many real-world dynamical datasets lack pre-defined graphs or labels for graph construction, so this need should be acknowledged clearly.

6) It is unclear how robust the system is to hyperparameter choices. Please discuss or explore this.

7) Additionally, it is unclear how you train/fit Eq. 3 in practice. Is it via EM or global optimizers? Please include an algorithm.

8) Many results are presented in the supplementary materials. While I understand that the page limit sometimes necessitates this approach, the authors did not use the full page limit in this case. Why not include more results in the main text? I suggest incorporating additional results (e.g., from Appendix B) into the main text.

9) I think an important question that needs discussion is how many observations you need for the method to succeed. I would assume that performance will improve rapidly with a low number of observations and then level off as more are added. Do you have any quantification of that? Specifically, what is the scale of the number of datasets for training needed to achieve a robust pre-trained model, and how does this scale with more or less datasets? The authors should also discuss how the similarity between the pre-training datasets and the fine-tuning dataset affects the performance of the model.



# Minor:

1) In the abstract, you used "neural Ordinary Differential…" without capitalizing "N"; however, in the introduction, it’s capitalized. Please be consistent.

2) Line 052: Change "where the dynamics can be easier captured" to "where the dynamics can be more easily captured."

3) While the paper is well-written overall, the first paragraph of the related work section reads more like a list than a motivation to identify the research gap. I suggest rephrasing it to better highlight the gap and clarify what your method aims to address.

4) Line 147: There’s a missing period after the ODE subtitle.

5) Line 192: The fourth word (`We`) should not be capitalized.

6) Lines 209-211: This content seems out of place and might fit better in the related work section.

7) Line 247: Did you mean "serve" instead of "sever"?

8) Line 370: The last word, "we", should be capitalized.

9) Table 5: Why is the "%" sign only next to some numbers? Are all values percentages, or do those with "%" represent a different scale (1/100)? This needs clarification. Why not use standard scientific notation (e.g., (e^(-3))  ) for small values?

### Questions
1. What happens if some observations are from a different distribution than the others?

2. What is the level of similarity you assume across systems? Please clarify the assumptions regarding the level of similarity required across different systems for your model to be effective. Are you suggesting that systems must share certain statistical properties or fundamental dynamics?

3. What is the model's computational complexity, and how does it scale with the number of observations?

4. How do you choose the system-specific parameters? 

5. Can you clarify the dimension of $\tilde{x}^\text{in}$? Is it equal to 1? Additionally, please specify the dimension of $W^s_{dp}$ in the `Data Projection` section.

6. Why was the architecture explained in Eq. 2 chosen? 

7. Why did you choose the $\ell_1$ rather than $\ell_2$ loss? (line 258).

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a neural system, the Pre-trained Dynamic Encoder (PDEDER), which is pre-trained on observations from various dynamic processes that unfold on graphs. They evaluate this model on a variety of long- and short-term forecasting tasks, both within domains (in-domain) and across domains (cross-domain).

Definition of benchmark:
   -153 sets of observations from different dynamical systems: 122 synthetic datasets from 14 dynamical systems and 31 real-world datasets from 10 dynamical systems.

   - Each dynamical system has Ms sets of observations with different parameters. Observations are multivariate, capturing data for each node in the system across different time steps.

    - Dynamical systems include: Springs, Mutualistic interactions, Heat diffusion, various Fluid dynamics, Biology, Climate, and Traffic, with system sizes ranging from 5 to 1024 nodes, timestamps from 100 to 28,000 steps, dimensionality from 1 to 10, sample counts from 1 to 10,000, and varying hyperparameters (from 1 to 15) for each dynamical system.

    - Each set of observations is temporally divided into in-sample and out-of-sample portions. PDEDER is trained to reconstruct in-sample data and forecast out-of-sample data.

Tokenization: to handle observations from various lengths, sub-observations are created to the fixed patch length and number of patches with specific stride length R. Additionally, Gaussian noise and instance normalization is done on each patch. 

Authors use system-specific linear projection layer. 

Learning Process: The projected data is used to reconstruct input states and to perform forecasting using a pre-trained language model (T5 model). The model architecture includes a convolutional layer for encoding, a PLM encoder, and a PLM decoder with additional linear adapters to aid in reconstruction and prediction. The loss function is an L1 loss applied to both the reconstruction and prediction components.

To model the evolution of dynamics, the authors employ a Graph Neural Network (GNN) with a single-layer normalized Laplacian and a trainable linear layer to encode the infinitesimal changes in the system state. Integration is then applied to derive the evolution of the hidden state, which is decoded by the decoder component of PDEDER.

They use 4 baselines:  NDCN Zang & Wang (2020a), ST-GODE Fang et al. (2021), MT-GODE Jin et al.
(2022) and TANGO Huang et al. (2024b).

Authors show results for short term/long term forecasting, in-domain and cross-domain setting.

As an active researcher in this field, it is challenging to assess the validity of the model without visual representations of the dataset’s dynamics. Showing figures that capture these dynamics would greatly improve the clarity and reliability of the experimental evaluation.

### Strengths
1. Work with large number of dynamical systems
2. Single model (modulo projection layer) that aims at reconstructing and forecasting dynamical systems is very hard.

### Weaknesses
Experimental setting is obscure and not written clearly (see and address questions for baselines, evaluation metrics, visualization of time-series forecasts vs ground truth).

Evaluations metrics:
Error Metrics for Dynamical Systems: Metrics such as MSE and MAE may not fully capture the performance of models on dynamical systems, as they might obscure certain dynamics-specific behaviors. Baselines should be better anchored to the dynamics with a simple, interpretable baseline for comparison. Try to include mean relative absolute error  Mean[ |(y_hat - y)/y| ] . Add another simple baseline for dynamics: e.g. prediction is last value plus numerical estimate of derivative plus some time series baselines. 

Baselines used are focused on GNN-type models for dynamical systems.

Why Language model like T5 should be used for dynamical systems? If I am right, you have re-used language model? Provide more intuition why do you believe it has valid grounds e.g. what kind of biases for transfer learning do you see in this pre-trained model?

### Questions
1. Forecasting Task Visualizations: It would be helpful to include figures illustrating the in-domain and cross-domain forecasting tasks. Specifically, showing a time series up to a certain point in time, followed by model forecasts alongside the ground truth values, would provide valuable insights.

    Limitations of Tables for Dynamical System Predictions: Tables alone do not clarify which dynamical regimes are being predicted. There is a possibility that only simple, easily predictable regimes are being tested. Visuals displaying different regimes in the time series would help clarify the difficulty of the forecasting tasks being evaluated.

2. Use of Benchmark Models for Forecasting:

    Incorporating Established Forecasting Models: It would strengthen the analysis to include well-known models for time-series forecasting in the experiments, such as SOTA models from recent M-competitions (e.g., Smyl, Slawek, Grzegorz Dudek, and Paweł Pełka. "ES-dRNN: a hybrid exponential smoothing and dilated recurrent neural network model for short-term load forecasting." IEEE transactions on neural networks and learning systems (2023)). These models could serve as benchmarks for comparison, adding credibility to the experimental findings.

3. Novel Initial Value Conditions in Forecasting Tasks:

    Generalizability Across Initial Conditions: The current experimental setup does not appear to include tests on dynamics with novel initial conditions? This raises concerns about the model's reliance on specific initial values. Evaluating the model’s performance on dynamics with varied initial conditions would clarify whether it is generalizable or inherently tied to specific initial states.

4. Discuss potential advantages or relevant biases from language models that may transfer well to dynamical systems modeling.

### Soundness
3

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
This paper introduces PDEDER (Pre-trained Dynamic EncoDER), a method to generalize dynamics modeling by embedding original states into a latent space using pre-trained language models.  The key idea is to pre-train an encoder using language models that can embed states from various dynamic systems into a latent space where dynamics can be more easily captured and fine-tuned for specific systems. The key contribution is a framework that pre-trains 153 sets of observations from 24 complex systems, followed by fine-tuning for specific dynamics. The method employs data projection, tokenization, and PLM-based encoding to learn dynamics-enriched embeddings. The authors evaluate 18 dynamic systems through long/short-term forecasting under in- and cross-domain settings.

### Strengths
* Novel approach using pre-trained models for dynamics modeling generalization
* Comprehensive dataset collection across multiple domains
* Clear empirical validation through both in-domain and cross-domain experiments
* Strong cross-domain performance after fine-tuning, even when excluding entire systems during pre-training

### Weaknesses
 * Difference between short-term and long-term forecasting in results  is not defined
* The connection between the pre-training objectives and dynamics modeling is not formally established
* Experimental limitations:
    1. The ablation studies don't fully isolate the contribution of each component
    2. Comparison with TANGO is limited to small-scale systems due to memory constraints. It would be useful to provide memory complexity analysis, Discuss potential solutions for scaling to larger systems
    3. The selection of 24 systems lacks justification for representativeness
* Technical details requiring clarification:
    1. How is the data projection module's dimension chosen?
    2. What is the impact of different PLM architectures?
    3. How sensitive is the method to tokenization parameters?
* The core idea of using pre-trained models for time series/dynamics has been explored in recent works (as cited in Related Work section, e.g., Gruver et al. 2024, PromptCast, AutoTimes). While this paper applies it to dynamics modeling in a new way, the conceptual novelty is incremental
Minor comment:
* Memory requirements should be discussed earlier in the paper

### Questions
* Why was T5 chosen as the base PLM? Have other architectures been considered?
* The data projection module reduces dimensionality to 1, but the justification for this choice isn't clear. Could this limit the model's expressiveness for complex systems?
* The data projection module seems crucial for handling different state dimensions. How do you determine the optimal projection dimension?
* The tokenization process (patch length 30, stride 6) seems to work well empirically, but how sensitive is the model to these choices? Some analysis of this would be valuable.
* Could you provide theoretical analysis/insights on why the pre-training objectives (reconstruction and forecasting) are sufficient for learning dynamics-enriched embeddings?
* How does the choice of T5 as the base PLM impact results? Have you tried other architectures?
* For the cross-domain experiments, how do you ensure the held-out systems are sufficiently different from the training systems?
What properties of the dynamics are preserved in the embedding space?

### Soundness
3

### Presentation
3

### Contribution
2
